#!/usr/bin/env python3
"""news_id=8370001 (Manu AGI: GitHubトレンドOSS 6選 #303) の
infographic_url / tags / summary / title を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

url = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news/8370001'

payload = {
    'title': '【GitHubトレンド】PHPの心臓部からDeepSeekの推論基盤まで——今週注目のOSS 6選（php-src / Impeccable / claude-mem / SPACE / DeepInfer / Filee）',
    'summary': (
        'Manu AGIの週次GitHubトレンド紹介#303（全20プロジェクト）から、特に注目の6つを厳選解説。'
        'Webの大部分を支えるPHP言語の公式処理系「php-src」、'
        'AIコーディング環境のフロントエンド設計力を鍛える設計スキル「Impeccable」、'
        'エージェントにセッションをまたぐ永続記憶を持たせる「claude-mem」、'
        'Perplexityが公開したFirecrackerマイクロVMによるエージェント用サンドボックス「SPACE」、'
        'DeepSeekが本番運用する推論フレームワーク「DeepInfer」、'
        'そしてカーソル位置のドーナツメニューでドラッグ＆ドロップ変換するオフライン対応の「Filee」。'
        '処理系・設計・記憶・分離・推論・変換と、OSS開発の今週の流れが一望できる18カード構成。'
    ),
    'tags': 'GitHub,オープンソース,php-src,PHP,Impeccable,claude-mem,AIエージェント,SPACE,Perplexity,Firecracker,サンドボックス,DeepInfer,DeepSeek,推論フレームワーク,Filee,ファイル変換,Manu AGI',
    'infographic_url': 'docs/20261025_github_trending_oss_6picks.html',
}


def main() -> int:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='PUT',
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = json.loads(r.read().decode())
            print(f'PUT HTTP {r.status}')
            print(f"  title: {body.get('title', '')}")
            print(f"  tags: {body.get('tags', '')}")
            print(f"  infographic_url: {body.get('infographic_url', '')}")
    except urllib.error.HTTPError as e:
        print(f'PUT HTTPError {e.code}: {e.read().decode("utf-8")[:400]}')
        return 1

    with urllib.request.urlopen(url, timeout=30) as r:
        got = json.loads(r.read().decode())
    ok = (
        got.get('infographic_url') == payload['infographic_url']
        and got.get('tags') == payload['tags']
    )
    print(f"GET  infographic_url={got.get('infographic_url')} tags={got.get('tags')}")
    print('VERIFY ' + ('OK' if ok else 'NG'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
