#!/usr/bin/env python3
"""news_id=8640003 (Daniel | Tech & Data: Lovable代替Flootレビュー) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8640003

payload = {
    "title": "Lovableの代替になるか？Claude・ChatGPTの中で動くアプリビルダー「Floot」を実際に試した【Daniel | Tech & Data】",
    "summary": "Daniel | Tech & Dataが、Lovableの代替として注目のコネクター型アプリビルダー「Floot（floot.com）」を実際に検証。FlootはClaude・ChatGPT・Cursorに接続するだけで既存のAIチャットを本格的なアプリ構築環境に変えるプラットフォームで、AIトークンを二重に支払うことなく、既に契約しているモデルのサブスクリプションのままアプリを作れる。セットアップはfloot.comで「ClaudeにFlootを追加」→接続→サインイン→権限承認の数回クリック・1分以内で完了し、ターミナル・ローカル環境・デプロイパイプラインは一切不要。検証では、認証（サインイン）付きワークアウトトラッカー「LiftLog」をたった1つのプロンプトで構築し、アカウント作成・ダッシュボード・ワークアウト記録フォーム・過去7日間の統計自動更新まで、コードを一行も書かずに実現。修正はプレビュー上の要素をクリック/ドラッグで選択してチャットに貼り付ける「選択と注釈」機能で、炎アイコン付きの継続日数カードを追加できた。裏側の確認ではServicesタブに本物のPostgreSQLがあり、セッション・ハッシュ化パスワード・ワークアウトエントリーの各テーブルが自動生成されていたほか、分析・SEO設定・ドキュメント・統合機能・プッシュ通知などもバンドルされる。公開はワンクリックで、独自ドメイン接続やアプリストア公開にも対応し、記録は同じアカウントのデータベースにリアルタイム反映される。Lovableとの比較ポイントは①同じチャット内の1プロンプトで開発開始、②言葉の代わりにポイントして注釈で反復改善、③本物のPostgreSQLをセットアップほぼ不要で提供、の3点。決定的にLovableを凌駕するわけではないが、AIトークンの二重払いなしでClaudeやChatGPT内からアプリを公開したい人にとって愛すべき代替手段という結論。なお本レビューはFloot提供。",
    "infographic_url": "docs/20261028_lovable_alternatives_daniel.html",
    "url": "https://www.youtube.com/watch?v=aP9RqN5Vqyg",
    "video_id": "aP9RqN5Vqyg",
    "tags": "Floot,Lovable,Claude,ChatGPT,Cursor,AIアプリ開発,ノーコード,PostgreSQL,Infographic,Daniel Tech & Data,vibecoding,アプリビルダー",
}

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
        print(f'PUT HTTP {r.status}')
        print(body[:500])
except urllib.error.HTTPError as e:
    print(f'PUT HTTP {e.code}')
    print(e.read().decode('utf-8')[:800])
    raise SystemExit(1)

# 反映確認
with urllib.request.urlopen(f'{BASE}/{NEWS_ID}', timeout=30) as r:
    got = json.loads(r.read().decode('utf-8'))
item = got.get('item', got) if isinstance(got, dict) else got
print('GET id:', item.get('id'))
print('GET infographic_url:', item.get('infographic_url'))
print('GET title:', item.get('title', '')[:60])
print('GET tags:', item.get('tags', '')[:80])
