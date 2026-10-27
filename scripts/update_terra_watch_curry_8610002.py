#!/usr/bin/env python3
"""news_id=8610002 (カレーちゃんのAI道場: GPT-6.1 Terraリリース配信) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8610002

payload = {
    "title": "GPT-6.1 Terraのリリースを見る、今日のAIニュースを話そう(10月27日8時30分から)",
    "summary": "カレーちゃんのAI道場が10月27日8時30分から配信した、OpenAIの新モデル「GPT-6.1 Terra」リリースをリアルタイムで見ながら当日のAIニュースを語る生配信。チャット自由・リクエスト募集の参加型スタイル。配信の主題となったGPT-6.1 Terraは、6.1で初登場した量産向けモデルで、ラインナップは最安ルナ／高速・量産向けテラ／難問コード向けソル／最上位アストラの4段構成。料金は1Mトークンあたり入力1ドル・出力5ドルと旧テラから半分以下、実測速度はソルの42.9TPSに対し約150TPSと約3.5倍。Artificial AnalysisスコアはGrok 4.7やMiMo V2.6 Proを上回り、エージェント系ベンチではソル並みのスコアを半額・3倍速で達成。OSWorld（コンピューターユース）ではアストラとほぼ互角でコスト1/5以下。事実の誤りは改善する一方Terminal Benchでは下位。安全性評価はサイバーが最上位クリティカル。検証デモでは3.8Kトークン・39秒でタスクを完了するトークン効率が最大の話題に。効率路線の背景にはオープンウェイトモデルの追い上げがあり、「賢さはClaude・速度はOpenAI」というタスク別使い分けの時代へ。なお配信には字幕がなく、Terra関連の要点は公開情報・同日の検証記事ベースでカード化。",
    "infographic_url": "docs/20261027_gpt61_terra_watch_curry.html",
    "url": "https://www.youtube.com/watch?v=7CcHXQNV_4A",
    "video_id": "7CcHXQNV_4A",
    "tags": "GPT-6.1,Terra,OpenAI,カレーちゃんのAI道場,ライブ配信,Token効率,コストパフォーマンス,コンピューターユース,OSWorld,エージェント,モデル使い分け,Infographic",
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
