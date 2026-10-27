#!/usr/bin/env python3
"""news_id=8580002 (masao: GPT-6.1 Terra 実機レビュー) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8580002

payload = {
    "title": "【面白い】『GPT-6.1 Terra』が登場したので実際に使ってきた！Token効率や速度をキープしたトレンド性能を押さえたAIでした",
    "summary": "まさおAIじっくり解説chがOpenAIの新モデル「GPT-6.1 Terra」を実機レビュー。6シリーズには無かったテラが6.1で初登場し、公式の位置付けは最安ルナ／高速・量産向けテラ／難問コード向けソル／最上位アストラの4段構成。料金は1Mトークンあたり入力1ドル・出力5ドルと旧テラ（2ドル／12ドル）から半分以下に値下げ。実測TPSはソルの42.9に対し約150と約3.5倍の速さ。Artificial AnalysisスコアはGrok 4.7やMiMo V2.6 Proを上回り、エージェント系ベンチではソル並みのスコアを半分のコスト・3倍以上の速さで達成。OSWorld（コンピューターユース）ではアストラとほぼ互角でコストは1/5以下、画像理解もアストラと横並び。事実の誤りはOpenAI社内ベンチで改善する一方、Terminal Benchでは下位が気になるポイント。安全性評価ではサイバーが最上位クリティカルで、実システムのゼロデイ発見から攻撃コード作成まで可能な水準。デモ検証では歩く人形SVGをわずか3.8Kトークン・39秒で完成（比較対象は11分）するToken効率が最大の見どころ。アイドルLPやゲーム生成はソルより省略的だが要点は押さえ、アクアリウム系も成立。スライド・サムネはチープ気味で、ライティングのLLMジャッジは低め。結論は「ソルの省略版・スマート版」として使い分けに組み込むのが現実解で、大量タスクはテラ、リッチな仕事はソル／アストラへ。",
    "infographic_url": "docs/20261027_gpt61_terra_hands_on_masao.html",
    "url": "https://www.youtube.com/watch?v=GasJL9OrbxE",
    "video_id": "GasJL9OrbxE",
    "tags": "GPT-6.1,Terra,OpenAI,まさおAIじっくり解説ch,Token効率,コストパフォーマンス,コンピューターユース,OSWorld,エージェント,ベンチマーク,Infographic",
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

# 検証: GET で反映確認
with urllib.request.urlopen(url, timeout=30) as r:
    data = json.loads(r.read().decode('utf-8'))
print('GET check:')
print('  title:', data.get('title', '')[:60])
print('  infographic_url:', data.get('infographic_url', ''))
print('  tags:', data.get('tags', ''))
