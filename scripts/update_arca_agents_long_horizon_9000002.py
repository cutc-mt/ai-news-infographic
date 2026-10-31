#!/usr/bin/python3
"""news_id=9000002 (Latent Space: Arca 長期金融エージェント) をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 9000002

payload = {
    "title": "【AIネイティブ資産運用】Arcaの長期タスク金融エージェント——カスタムハーネスと永続メモリで数日単位の業務を自動化、人間承認・監査可能性を初期設計に組み込む（Latent Space Podcast）",
    "summary": "AIネイティブなウェルスマネジメント企業ArcaのAI責任者Aman Singhが、AI Engineer New YorkでLatent SpaceのRichard MacManusと対談。Arcaは人間のファイナンシャルアドバイザーをAIエージェントが支える体制で、汎用リーダーボードではなく自社タスクの内部ベンチマークでモデルを選定し、タスクごとにルーティングするカスタムハーネスを内製。数日単位で走る長期ワークフローでは永続メモリで文脈を保持し、10万ドルの税務請求への対応例のように、エージェントが調査と計画をまとめ、実行前に人間のアドバイザーが承認するゲートを通す。プロンプトインジェクション防御の多層ガードレール、コンプライアンスと監査可能性の初期組み込み、「エージェントが人をプロンプトする」逆転した日常工作、サンドボックスでのファイナンシャルプラン検証、決定モデルによる金融事実のチェック、トレード実行は人間の専門家が担う責任設計まで解説。さらに現場スタッフのフィードバックをevalsに変換する改善サイクル、運用ナレッジのエージェント文脈化、隠れた手数料の発見や先回りの顧客サービスといった実例、「AIツールを使う企業」と「AIネイティブ企業」の違いを語る。",
    "source": "Latent Space Podcast",
    "date": "2026-11-01",
    "category": "AIニュース",
    "url": "https://www.youtube.com/watch?v=KM3VQZKjpiY",
    "tags": "LatentSpace,Arca,AmanSingh,ウェルスマネジメント,金融AI,エージェント,カスタムハーネス,永続メモリ,長期タスク,人間承認,プロンプトインジェクション,コンプライアンス,監査可能性,evals,Infographic",
    "video_id": "KM3VQZKjpiY",
    "channel_id": "@LatentSpacePod",
    "infographic_url": "docs/20261101_arca_agents_long_horizon_finance_latentspace.html",
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
    print(f'PUT HTTPError {e.code}: {e.read().decode("utf-8")[:500]}')
    raise SystemExit(1)

with urllib.request.urlopen(url, timeout=30) as r:
    data = json.loads(r.read().decode('utf-8'))
print('GET check:')
print('  title:', data.get('title', '')[:80])
print('  infographic_url:', data.get('infographic_url', ''))
print('  tags:', data.get('tags', '')[:120])
print('  video_id:', data.get('video_id', ''))
