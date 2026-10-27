#!/usr/bin/env python3
"""news_id=8610001 (AI大学: Meta Muse) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8610001

payload = {
    "title": "Metaの無料パーソナルAIエージェント「Muse」の特徴・使い方・活用事例！～Gmail・カレンダー連携から動画・画像生成まで丸投げできる～",
    "summary": "AI大学【AI&ChatGPT最新情報】が、2026年10月23日に日本展開が始まったMetaの無料パーソナルAIエージェント「Muse（ミューズ）」を3章構成で解説。Museはクラウド上の隔離された専用コンピューターで稼働し、高性能モデル「Muse Spark」がメール送信やレストラン予約から大きな目標の計画・実行・交渉・安全な決済まで自立的にこなし、アプリを閉じても作業を継続、一度話した大事なことを記憶して先回り提案する。GmailやGoogleカレンダー、Instagramなど多くのサービスと連携して機能をコントロールでき、画像・動画・ポッドキャスト生成も内蔵。米国では公開わずか40日でモバイルアプリのダウンロード1000万件を突破。安全面では認証情報を中身を見ないまま安全なストレージで保管し、操作実行前にユーザー確認・全履歴チェック・アクセス範囲設定が可能。対応プラットフォームはWeb・iOS・Android・Macで、近日中にMetaのAIグラスにも対応予定。導入時はデータコントロールの学習協力設定の確認と、Instagram/Facebookのデフォルト連携の見直しが推奨。名前・人格（ソウル）・長期記憶（メモリー）はユーザーが直接編集できる。活用事例はアイデアページの「やってみよう」、毎朝のGmailチェック、カレンダー自動登録、チャット経由の画像・動画生成など。無料プランは週次利用上限あり、上位モデル「Muse Wonder」などのサブスクプランも用意される。",
    "infographic_url": "docs/20261027_meta_muse_agent_ai_daigaku.html",
    "url": "https://www.youtube.com/watch?v=9FLNYHMFeGc",
    "video_id": "9FLNYHMFeGc",
    "tags": "Meta,Muse,AIエージェント,Muse Spark,Muse Wonder,パーソナルAI,Gmail連携,Googleカレンダー,AI大学,無料AIツール,画像生成,動画生成,Infographic",
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
