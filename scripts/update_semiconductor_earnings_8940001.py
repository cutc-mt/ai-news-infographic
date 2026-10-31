#!/usr/bin/env python3
"""API更新スクリプト (news_id=8940001 / tnSYlmkMHy8)
カレーちゃんのAIニュース「半導体株急落・決算を見る。今日のAIニュースを話そう(10月31日8時30分から)」
"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8940001

payload = {
    'title': '半導体株急落・決算を見る。今日のAIニュースを話そう(10月31日8時30分から)',
    'summary': (
        '2026年10月31日の朝ライブ。インテルのQ3決算はEPS・売上・利益率ともに予想を上回った一方、'
        'Q4ガイダンス（売上150〜160億ドル・EPS0.25ドル）が市場予想を大きく下回り、株価は28.6%急落。'
        'SOX半導体指数は7.2%下落し、米アジアの主要半導体23社で約1兆ドルの時価総額が消失した。'
        'アマゾン決算の失望とAI投資回収への疑念、日経平均1,369円安・ソフトバンクG7%安など日本・アジアへの波及、'
        '日銀のタカ派化、アドバンテスト・東京エレクトロンの好決算、11月3日のAMD決算への注目まで解説。'
    ),
    'url': 'https://www.youtube.com/watch?v=tnSYlmkMHy8',
    'video_id': 'tnSYlmkMHy8',
    'infographic_url': 'docs/20261031_semiconductor_earnings_currychan.html',
    'tags': '半導体株急落,インテル決算,AI投資,日経平均,アドバンテスト,東京エレクトロン,AMD,カレーちゃん',
    'source': 'カレーちゃんのAIニュース',
}


def main() -> int:
    url = f'{BASE}/{NEWS_ID}'
    req = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
        method='PUT',
        headers={'Content-Type': 'application/json'},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read().decode('utf-8')
            print(f'HTTP {r.status}')
            print(body[:500])
            return 0 if r.status == 200 else 1
    except urllib.error.HTTPError as e:
        print(f'HTTPError {e.code}: {e.read().decode("utf-8")[:500]}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
