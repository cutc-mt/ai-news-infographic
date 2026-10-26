#!/usr/bin/python3
"""news_id=8550003 (AI共創イノベーション: AIで3D制作) をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8550003

payload = {
    "title": "【AIで3D制作】AIエージェントで3Dアニメーションの動く世界を作る！キャラクター設計や背景設計を徹底解説【Gemini】",
    "summary": "AI共創イノベーションのワンダ佐藤さんが、Gemini（Argon）やClaude Code、CodexなどのAIエージェントで、クリック・カーソル操作で歩き回れる3Dアニメーション世界の作り方を解説。テーマは最高の品質ではなく「いかにコスパよく作るか」。制作のコツは①一番難しいキャラクター（特に髪の毛）から着手し以降は丸ごと移植、②アニメ風に割り切ってAI臭い違和感とコード量を削減、③自然物だけに1/f揺らぎを後から与え人工物はそのまま、④ゲシュタルト（形の心理学）で「パッと見で分かる」水準を狙い人間の認知に補完させる、⑤スーパーマリオの雲と木よろしく素材（屋根・輪郭・目鼻）を使い回しノイズと長さ変化で別物に見せる、⑥自然界の数学で調整——尖った富士山はネイピア数の指数関数でなだらかに、桜の枝はフィボナッチ、花びらの落下は1/f揺らぎ＋ランダム性、⑦AIの枝を上に固める癖（OpusもArgonも共通）は1つに集中させて作らせ分担、OpusでダメならArgon、Codexを試して後から合体させるマルチモデル運用。一気に作る方式（架空の不思議世界）と部分から合体させる方式（江戸時代編のおもちゃ屋・居酒屋・長屋・湯屋・旅館を1個ずつ調査再現）の使い分け、湯屋で顔がはみ出す失敗を「調整対象」として残す教育工夫も。必要な知識は専門知識でなく中途半端な知識の組み合わせ（全体を見る力）で、最後は自分の作ったものに責任を持つことが重要と強調。ChatGPTプラス／Claudeプロ級でも作れて、営業資料・商品説明の3D化へのビジネス応用も予定。",
    "source": "AI共創イノベーション",
    "date": "2026-10-26",
    "category": "AIニュース",
    "url": "https://www.youtube.com/watch?v=kh7AwekVq9Q",
    "tags": "AI共創イノベーション,ワンダ佐藤,3D制作,3Dアニメーション,Gemini,Argon,ClaudeCode,Codex,AIエージェント,トークン効率,1/f揺らぎ,フィボナッチ,ネイピア数,ゲシュタルト,江戸時代,Infographic",
    "video_id": "kh7AwekVq9Q",
    "channel_id": "@AICoCreation",
    "infographic_url": "docs/20261027_ai_3d_world_kyoso_kh7.html",
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
