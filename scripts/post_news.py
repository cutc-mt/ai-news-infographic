"""
ニュースAPI POST スクリプト (Phase 5d)

YouTube監視で検知した新着動画を
ai-news-app API にPOSTする。
"""
import json
import urllib.request
import urllib.error
from typing import Optional


def build_news_payload(video: dict) -> dict:
    """YouTube動画情報からAPIペイロードを構築"""
    # publishedAtから日付を抽出 (2026-08-04T10:00:00Z → 2026-08-04)
    date_str = video.get('publishedAt', '')[:10] or '2026-08-04'

    # summary: descriptionがあれば使う、なければフォールバック
    summary = video.get('description', '').strip()
    if not summary:
        summary = f"{video.get('channel_name', '')}の最新動画"

    # titleからカテゴリを推定（シンプルなルールベース）
    title_lower = (video.get('title', '') + ' ' + summary).lower()
    category = 'AIニュース'  # デフォルト
    # ※ 将来的にLLMで判定する場合はここを置き換える

    return {
        'title': video.get('title', ''),
        'summary': summary,
        'source': video.get('channel_name', video.get('channel_title', '')),
        'date': date_str,
        'category': category,
        'url': video.get('url', ''),
        'tags': '',
        'video_id': video.get('video_id', ''),
        'channel_id': video.get('channel_handle', ''),
        'infographic_url': '',
    }


def post_news(payload: dict, api_url: str = 'http://localhost:8000/api/news') -> bool:
    """APIにニュースをPOSTする"""
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(
        api_url,
        data=data,
        headers={
            'Content-Type': 'application/json',
        },
        method='POST',
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  ✅ POST成功: {payload.get('title', '')[:40]}")
            return True
    except urllib.error.HTTPError as e:
        if e.code == 409:
            # 重複は正常（既に登録済み）
            print(f"  ⏭️ スキップ（重複）: {payload.get('video_id', '')}")
            return True
        else:
            print(f"  ❌ POST失敗 ({e.code}): {payload.get('title', '')[:40]}")
            return False
    except Exception as e:
        print(f"  ❌ エラー: {e}")
        return False


def batch_post_news(
    videos: list,
    api_url: str = 'http://localhost:8000/api/news'
) -> dict:
    """複数の新着動画をバッチPOSTする"""
    success = 0
    failed = 0
    skipped = 0

    for video in videos:
        payload = build_news_payload(video)
        result = post_news(payload, api_url)

        if result:
            success += 1
        else:
            failed += 1

    return {
        'success': success,
        'failed': failed,
        'skipped': skipped,
        'total': len(videos),
    }


if __name__ == '__main__':
    import os
    import sys
    from youtube_monitor import YouTubeMonitor

    api_key = os.environ.get('YOUTUBE_API_KEY', '')
    news_api_url = os.environ.get('NEWS_API_URL', 'http://localhost:8000/api/news')

    if not api_key:
        print("❌ YOUTUBE_API_KEY environment variable not set")
        sys.exit(1)

    # 1. 新着動画を検知
    print("=== YouTube チャンネル監視 ===")
    monitor = YouTubeMonitor(api_key)
    new_videos = monitor.check_all_channels()

    if not new_videos:
        print("\n✅ 新着動画なし")
        sys.exit(0)

    print(f"\n=== {len(new_videos)}本の新着動画をAPIにPOST ===")

    # 2. APIにPOST
    results = batch_post_news(new_videos, api_url=news_api_url)
    print(f"\n=== 結果 ===")
    print(f"  成功: {results['success']}")
    print(f"  失敗: {results['failed']}")
    print(f"  合計: {results['total']}")
