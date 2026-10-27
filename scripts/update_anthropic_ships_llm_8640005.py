#!/usr/bin/env python3
"""news_id=8640005 (Latent Space: Anthropic ships LLM) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8640005

payload = {
    "title": "Anthropicはどうやって世界最高のLLMを出荷しているのか — S-1・Opus 5.5・Rustリライト・安全策のすべて | Latent Space Podcast",
    "summary": "Latent Space PodcastがAnthropicのS-1提出を受けて開始したIPO特別シリーズ第1弾。Claude Platformのプロダクト責任者Katelyn Lさんとエンジニアリング責任者AngelaさんをOpus 5.5ローンチ翌日に迎え、「世界最強のモデルを最も効率的に出荷する仕組み」を内部視点で解き明かす。S-1分析では、従業員1人あたり年収益が1年前の140万ドルから660万ドルへ約5倍、計算コスト1ドルあたり収益は2025年Q2の0.5ドル赤字から2ドル黒字へ転換、GAAPベースで初の黒字四半期（利益率19%、1年前は▲129%）、生涯キャッシュ調達1,000億ドル超に対し累積バーンは100億ドル未満と紹介。成長エンジンは「改善ループ（Claude→良いモデル→用途拡大→フィードバック→より良いClaude）」と「投資ループ（収益→成長→投資→能力→より良いClaude）」の無限ループ。Claude Platformは年間10万ドル以上の顧客の50%超が利用し、Claude Code/Co-workと同一プリミティブの上に構築される。Opus 5.5は文章の癖をクリーンアップし大幅値下げ、「1ドルあたりの知能」を追求。思考トークン蒸留（Stealing Reasoning Traces論文）対策として思考ブロックのターン間保全・compaction新API・OSSハーネス保守者との協働を実施し、動機は商業ではなく安全性。スケール面ではCPUが最大の制約となり、Rust経験者ゼロのチームがClaudeにコードを書かせてMessages API全量をRustへ一気に移植（シャドウトラフィック検証、CPU40〜50%削減、最初のトークンまで10〜20%高速化）。モデルローンチは安全性検証→内部ant fooding→Cognition等へのアーリーアクセス→公開の工程で、アーキテクチャ/オンライン/オフラインの3次元の安全策、データ保持ポリシー、cyber・ライフサイエンス検証プログラム、trust grants、一括ロールバック・ボタンを整備。Claude Managed Agentsはbrain（耐久サーバーのハーネス）とhands（サンドボックス実行）を分離し、資格情報は独立vault＋egressプロキシ注入、ドメイン許可リストでsecure by defaultを実現。DreamingはCMA上のマルチエージェント・システムで、近日中にマルチエージェント戦略プリミティブを公開予定。evalは「多く必要・シンプルに始める・投資不足が最大の失敗」、スロップ対策は「品質責任は人間が持つ」、DevRelではAddy Osmaniさんらがジョイン。結論として、費用対効果の上がったOpus 5.5で「1人のリード＋並列化＋共有状態＋非同期サブエージェント」のマルチエージェント実験を推奨。",
    "infographic_url": "docs/20261028_anthropic_ships_llm_latentspace.html",
    "url": "https://www.youtube.com/watch?v=MRQTlwcW-aQ",
    "video_id": "MRQTlwcW-aQ",
    "tags": "Anthropic,Latent Space,Opus 5.5,Claude,Claude Platform,Claude Managed Agents,Rust,IPO,S-1,ディスティレーション対策,マルチエージェント,eval,Infographic",
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
