#!/usr/bin/python3
"""API更新スクリプト: JSONファイルからペイロードを読みPUT /api/news/<id> に送る。

使い方:
    /usr/bin/python3 scripts/put_news.py payloads.json

payloads.json 形式:
    [
      {
        "news_id": 5400004,
        "title": "...",
        "summary": "...",
        "infographic_url": "..."
      }
    ]
"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'


def put_news(news_id: int, title: str, summary: str, infographic_url: str) -> int:
    url = f'{BASE}/{news_id}'
    payload = {
        'title': title,
        'summary': summary,
        'infographic_url': infographic_url,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        method='PUT',
        headers={'Content-Type': 'application/json'},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode('utf-8')
            print(f'news_id={news_id} HTTP {r.status}')
            data = json.loads(body)
            print(f"  title: {data.get('title', '')}")
            print(f"  infographic_url: {data.get('infographic_url', '')}")
            return r.status
    except urllib.error.HTTPError as e:
        print(f'news_id={news_id} HTTPError {e.code}: {e.read().decode("utf-8")[:300]}')
        return e.code


def main() -> int:
    with open(sys.argv[1], encoding='utf-8') as f:
        items = json.load(f)
    ok = True
    for item in items:
        status = put_news(
            item['news_id'],
            item['title'],
            item['summary'],
            item['infographic_url'],
        )
        if status != 200:
            ok = False
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
