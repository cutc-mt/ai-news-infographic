"""
YouTube チャンネル監視システム (Phase 5c)

channels.yamlから監視対象チャンネルを読み込み、
YouTube Data API v3で新着動画を検知する。

最適化: search API(100 units)の代わりに playlistItems API(1 unit)を使用。
チャンネルIDはスクレイピングで取得しAPI消費を削減。
"""
import os
import re
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from typing import Optional
from datetime import datetime, timedelta, timezone
import yaml


# --- channels.yaml 読み込み ---

def load_channels(yaml_path: Optional[str] = None, only_enabled: bool = False) -> list:
    """channels.yamlを読み込んでチャンネルリストを返す"""
    if yaml_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        yaml_path = os.path.join(script_dir, '..', 'channels.yaml')

    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    channels = data.get('channels', [])

    if only_enabled:
        channels = [ch for ch in channels if ch.get('enabled', False) and ch.get('handle')]

    return channels


# --- HTTP ヘルパー（テスト用にモック可能） ---

def requests_get(url: str) -> dict:
    """urllibでGETリクエスト（requests互換の戻り値）。429は例外ではなく空で返す。"""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            status_code = resp.status
            body = resp.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        if e.code == 429:
            # クォータ枯渇: 空の結果を返す
            print(f"  ⚠️ Rate limited (429), skipping request")
            return {'status_code': 429, 'json': lambda: {}}
        raise
    return {'status_code': status_code, 'json': lambda: json.loads(body)}


# --- チャンネルIDキャッシュ（ファイルベース） ---

CHANNEL_ID_CACHE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'channel_ids_cache.json'
)


def load_channel_id_cache() -> dict:
    """チャンネルIDのキャッシュをファイルから読み込む"""
    try:
        with open(CHANNEL_ID_CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_channel_id_cache(cache: dict):
    """チャンネルIDのキャッシュをファイルに保存"""
    with open(CHANNEL_ID_CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


# --- チャンネルID取得 ---

def get_channel_id_scrape(handle: str) -> Optional[str]:
    """YouTubeチャンネルページをスクレイピングしてchannel_idを取得（API不要）"""
    clean = handle.lstrip('@')
    url = f"https://www.youtube.com/@{clean}"
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        # "channelId":"UC..." または "externalId":"UC..." を探す
        match = re.search(r'"channelId":"(UC[A-Za-z0-9_-]{22})"', html)
        if match:
            return match.group(1)
        match = re.search(r'"externalId":"(UC[A-Za-z0-9_-]{22})"', html)
        if match:
            return match.group(1)
        return None
    except Exception:
        return None


def get_channel_id(handle: str, api_key: str) -> Optional[str]:
    """handle（@xxx）からチャンネルIDを取得。

    優先順位: ファイルキャッシュ → スクレイピング → API(forHandle)
    search API（100 units）は使わない。
    """
    clean = handle.lstrip('@')

    # 1. ファイルキャッシュを確認
    cache = load_channel_id_cache()
    if handle in cache:
        return cache[handle]

    # 2. スクレイピング（API消費ゼロ）
    cid = get_channel_id_scrape(handle)
    if cid:
        cache[handle] = cid
        save_channel_id_cache(cache)
        return cid

    # 3. API forHandle（1 unit）をフォールバックとして使用
    url = (
        f"https://www.googleapis.com/youtube/v3/channels"
        f"?part=snippet&forHandle={urllib.parse.quote(handle)}&key={api_key}"
    )
    result = requests_get(url)
    status_code = getattr(result, 'status_code', result.get('status_code') if isinstance(result, dict) else None)
    json_fn = getattr(result, 'json', None) or (lambda: result['json']() if isinstance(result, dict) else {})
    if status_code != 200:
        return None
    items = json_fn().get('items', [])
    if items:
        cid = items[0].get('id')
        if cid:
            cache[handle] = cid
            save_channel_id_cache(cache)
        return cid

    return None


# --- 動画取得（playlistItems API使用、search APIは使わない） ---

def get_uploads_playlist_id(channel_id: str) -> str:
    """channel_idからuploads playlist IDを生成"""
    if channel_id.startswith('UC'):
        return 'UU' + channel_id[2:]
    return channel_id


def get_latest_videos(channel_id: str, api_key: str, max_results: int = 5) -> list:
    """チャンネルの最新動画を取得。

    playlistItems API(1 unit)を使用。search API(100 units)は使わない。
    """
    playlist_id = get_uploads_playlist_id(channel_id)
    url = (
        f"https://www.googleapis.com/youtube/v3/playlistItems"
        f"?part=snippet&playlistId={playlist_id}"
        f"&maxResults={max_results}&key={api_key}"
    )
    try:
        result = requests_get(url)
    except Exception:
        return []

    status_code = getattr(result, 'status_code', result.get('status_code') if isinstance(result, dict) else None)
    json_fn = getattr(result, 'json', None) or (lambda: result['json']() if isinstance(result, dict) else {})
    if status_code != 200:
        return []

    items = json_fn().get('items', [])
    videos = []
    for item in items:
        snippet = item.get('snippet', {})
        video_id = snippet.get('resourceId', {}).get('videoId')
        if not video_id:
            continue
        videos.append({
            'video_id': video_id,
            'title': snippet.get('title', ''),
            'publishedAt': snippet.get('publishedAt', ''),
            'channel_title': snippet.get('channelTitle', ''),
            'description': snippet.get('description', ''),
            'url': f"https://www.youtube.com/watch?v={video_id}",
        })
    return videos


def filter_new_videos(videos: list, known_video_ids: set) -> list:
    """既知のvideo_idを除外して新しい動画のみ返す"""
    return [v for v in videos if v['video_id'] not in known_video_ids]


def is_likely_short(video: dict) -> bool:
    """タイトル/説明文からショート動画か判定する"""
    text = (video.get('title', '') + ' ' + video.get('description', '')).lower()
    indicators = ['#shorts', '#short', '[short]', '(short)', 'short']
    return any(ind in text for ind in indicators)


def filter_shorts(videos: list) -> list:
    """ショート動画を除外する"""
    return [v for v in videos if not is_likely_short(v)]


def is_recent(published_at: str, max_days: int = 1) -> bool:
    """動画が指定日数以内に公開されたか判定"""
    if not published_at:
        return False
    try:
        # ISO 8601形式をパース（例: 2026-08-04T10:00:00Z）
        pub_date = datetime.fromisoformat(
            published_at.replace('Z', '+00:00')
        )
        if pub_date.tzinfo is None:
            pub_date = pub_date.replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        age = now - pub_date
        return age <= timedelta(days=max_days)
    except (ValueError, TypeError):
        return False


def filter_by_date(videos: list, max_days: int = 1) -> list:
    """指定日数以内に公開された動画のみを残す"""
    return [v for v in videos if is_recent(v.get('publishedAt', ''), max_days)]


# --- 統合クラス ---

class YouTubeMonitor:
    """チャンネル監視の統合クラス"""

    def __init__(self, api_key: str, yaml_path: Optional[str] = None):
        self.api_key = api_key
        self.channels = load_channels(yaml_path, only_enabled=True)
        # チャンネルIDキャッシュ（ファイルベース + インスタンス）
        self._channel_id_cache: dict = {}

    def get_channel_id(self, handle: str) -> Optional[str]:
        """チャンネルIDを取得（キャッシュ付き）"""
        if handle in self._channel_id_cache:
            return self._channel_id_cache[handle]
        cid = get_channel_id(handle, self.api_key)
        if cid:
            self._channel_id_cache[handle] = cid
        return cid

    def get_latest_videos(self, channel_id: str, max_results: int = 5) -> list:
        return get_latest_videos(channel_id, self.api_key, max_results)

    def get_known_video_ids(self) -> set:
        """既存のインフォグラフィックから既知のvideo_idを取得"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        docs_dir = os.path.join(script_dir, '..', 'docs')
        known = set()
        if not os.path.isdir(docs_dir):
            return known
        for filename in os.listdir(docs_dir):
            if not filename.endswith('.html'):
                continue
            filepath = os.path.join(docs_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                # YouTube動画IDパターンを抽出
                ids = re.findall(r'watch\?v=([A-Za-z0-9_-]{11})', content)
                known.update(ids)
            except:
                pass
        return known

    def check_all_channels(self, max_per_channel: int = 5, max_days: int = 2) -> list:
        """全チャンネルをチェックして新着動画を返す

        Args:
            max_per_channel: チャンネルあたり最大取得数
            max_days: 監視時点から遡って何日以内の動画を対象とするか
        """
        known_ids = self.get_known_video_ids()
        new_videos = []

        for ch in self.channels:
            handle = ch['handle']
            name = ch['name']

            channel_id = self.get_channel_id(handle)
            if not channel_id:
                print(f"⚠️ Channel ID not found for {handle} ({name})")
                continue

            videos = self.get_latest_videos(channel_id, max_per_channel)
            videos = filter_shorts(videos)
            videos = filter_by_date(videos, max_days=max_days)
            fresh = filter_new_videos(videos, known_ids)

            for v in fresh:
                v['channel_handle'] = handle
                v['channel_name'] = name
                new_videos.append(v)

            if fresh:
                print(f"📺 {name}: {len(fresh)} new video(s)")
            else:
                print(f"✅ {name}: No new videos")

        return new_videos


# --- CLI エントリーポイント ---

if __name__ == '__main__':
    api_key = os.environ.get('YOUTUBE_API_KEY', '')
    if not api_key:
        print("❌ YOUTUBE_API_KEY environment variable not set")
        exit(1)

    monitor = YouTubeMonitor(api_key)
    new_videos = monitor.check_all_channels()

    if new_videos:
        print(f"\n🎉 Found {len(new_videos)} new video(s)!")
        for v in new_videos:
            print(f"  [{v['channel_name']}] {v['title']}")
            print(f"    {v['url']}")
    else:
        print("\n✅ No new videos found")
