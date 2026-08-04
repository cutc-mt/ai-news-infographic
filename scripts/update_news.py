"""
ニュースAPI更新スクリプト (Phase 5e)

インフォグラフィック生成後に、APIのニュースエントリを更新する。
- 日本語タイトル・概要への置き換え
- infographic_urlの登録
"""
import json
import urllib.request
import urllib.error
from typing import Optional


# GitHub Pages のベースURL
GITHUB_PAGES_BASE = "https://cutc-mt.github.io/ai-news-infographic/docs/"


def build_infographic_url(filename: str) -> str:
    """ファイル名からGitHub PagesのURLを構築"""
    return f"{GITHUB_PAGES_BASE}{filename}"


def update_news_entry(
    news_id: int,
    api_url: str,
    title: Optional[str] = None,
    summary: Optional[str] = None,
    infographic_url: Optional[str] = None,
) -> bool:
    """API PUT でニュースエントリを更新"""
    payload = {}
    if title is not None:
        payload['title'] = title
    if summary is not None:
        payload['summary'] = summary
    if infographic_url is not None:
        payload['infographic_url'] = infographic_url

    if not payload:
        return False

    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(
        api_url,
        data=data,
        headers={'Content-Type': 'application/json'},
        method='PUT',
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"  ✅ 更新成功: news_id={news_id}")
            return True
    except urllib.error.HTTPError as e:
        print(f"  ❌ 更新失敗 ({e.code}): news_id={news_id}")
        return False
    except Exception as e:
        print(f"  ❌ エラー: {e}")
        return False


def update_batch(entries: list, api_base: str = 'http://localhost:8000') -> dict:
    """複数のニュースエントリをバッチ更新"""
    success = 0
    failed = 0

    for entry in entries:
        news_id = entry.get('news_id')
        api_url = f"{api_base}/api/news/{news_id}"

        result = update_news_entry(
            news_id=news_id,
            api_url=api_url,
            title=entry.get('title'),
            summary=entry.get('summary'),
            infographic_url=entry.get('infographic_url'),
        )
        if result:
            success += 1
        else:
            failed += 1

    return {
        'success': success,
        'failed': failed,
        'total': len(entries),
    }
