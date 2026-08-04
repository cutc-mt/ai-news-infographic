"""
YouTube チャンネル監視システム (Phase 5c)

channels.yamlから監視対象チャンネルを読み込み、
YouTube Data API v3で新着動画を検知する。
"""
import os
import json
import urllib.request
import urllib.parse
from typing import Optional
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
    """urllibでGETリクエスト（requests互換の戻り値）"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=30) as resp:
        status_code = resp.status
        body = resp.read().decode('utf-8')
    return {'status_code': status_code, 'json': lambda: json.loads(body)}


# --- YouTube API ---

def get_channel_id(handle: str, api_key: str) -> Optional[str]:
    """handle（@xxx）からチャンネルIDを取得"""
    clean = handle.lstrip('@')
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
        return items[0].get('id')
    # forHandleが効かない場合はsearchでフォールバック
    url2 = (
        f"https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&q={urllib.parse.quote(clean)}&type=channel&maxResults=1&key={api_key}"
    )
    result2 = requests_get(url2)
    status_code2 = getattr(result2, 'status_code', result2.get('status_code') if isinstance(result2, dict) else None)
    json_fn2 = getattr(result2, 'json', None) or (lambda: result2['json']() if isinstance(result2, dict) else {})
    items2 = json_fn2().get('items', [])
    if items2:
        return items2[0].get('id', {}).get('channelId')
    return None


def get_latest_videos(channel_id: str, api_key: str, max_results: int = 5) -> list:
    """チャンネルの最新動画を取得"""
    url = (
        f"https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&channelId={channel_id}"
        f"&order=date&type=video&maxResults={max_results}&key={api_key}"
    )
    result = requests_get(url)
    status_code = getattr(result, 'status_code', result.get('status_code') if isinstance(result, dict) else None)
    json_fn = getattr(result, 'json', None) or (lambda: result['json']() if isinstance(result, dict) else {})
    if status_code != 200:
        return []

    items = json_fn().get('items', [])
    videos = []
    for item in items:
        video_id = item.get('id', {}).get('videoId')
        if not video_id:
            continue
        snippet = item.get('snippet', {})
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


# --- 統合クラス ---

class YouTubeMonitor:
    """チャンネル監視の統合クラス"""

    def __init__(self, api_key: str, yaml_path: Optional[str] = None):
        self.api_key = api_key
        self.channels = load_channels(yaml_path, only_enabled=True)
        # チャンネルIDキャッシュ
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
        import re
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

    def check_all_channels(self, max_per_channel: int = 5) -> list:
        """全チャンネルをチェックして新着動画を返す"""
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
