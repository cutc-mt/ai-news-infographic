#!/usr/bin/env python3
"""news_id=9150003 (ウェブ職TV: Notta Memo Pro / AIっぽい文章) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 9150003

payload = {
    "title": "どうしてAIの文章はAIっぽいのか【Notta Memo Proが進化しすぎてる件】",
    "summary": "ウェブ職TVが、AIに書かせた文章に残る「AIっぽさ」の原因と対策を解説し、音声入力に最適なAIボイスレコーダー「Notta Memo Pro」（2026年10月13日発売）を開封レビューする動画。AIっぽい文章の特徴として、(1)読点が異常に多い（人間のX投稿は100文字あたり約1.8個に対しClaudeは約2.8個で、主語の直後にも不要な読点を打つ）、(2)体験談や数字が入らず一般論ばかりで、文字数を求めると同じ内容を言い換えて繰り返す、(3)感情がないためどこも同じテンションでメリハリがない、(4)「〜していきましょう」型の前向きまとめで閉じる、(5)「頼もしい相棒です」など日常で使わない翻訳調の言い回しが出る——の5点を挙げる。原因はAIが英語で学習して日本語に翻訳する構造にあると推測。「AIっぽくしないで」と指示する書き直しは書き口こそ変えるが、元の情報が一般論では限界があるとして、結論は「自分の音声を書き起こしてそれを元に文章を書かせるのが最強」。自分の言葉遣い・経験に基づくノウハウ・熱量が入るため、プロンプト調整より100倍早く良いコンテンツになると説明する。喋る際は流暢に喋る必要はなく、沈黙や順番の入れ替わりを気にせず、後でAIに整理させればよい。後半のNotta Memo Proは、旧型比で小型化し充電がUSB Type-C直差し化、カラーディスプレイ大型化で録音中表示と経過時間が明確になり、電話/対面の録音モードを自動判別。収音距離は3mから5mへ、ストレージは32GBから64GB（約8000時間録音）へ、連続録音は約30時間から45時間へ、待機は約28日から30日へ向上。リアルタイム文字起こし、登録Wi-Fi環境でのクラウド自動同期、重要マーク機能、AIへの質問（Notta Brain）に対応。録音データは暗号化され国内サーバーに保存、無料文字起こし枠は月300分から600分に倍増（Nottaハード全機種共通）。話者識別精度は公式値90.51%で4〜8人の会議でも強く、デバイスに名前とアバターを登録可能、ストラップ穴で首かけでも使える。価格はProが2万9,700円に対し旧Notta Memoは2万5,500円で、4,000円差なら絶対にProという評価。",
    "infographic_url": "docs/20261102_notta_memo_pro_ai_bunshou.html",
    "url": "https://www.youtube.com/watch?v=4J5tVm0O7_c",
    "video_id": "4J5tVm0O7_c",
    "tags": "Notta,Notta Memo Pro,AIボイスレコーダー,音声入力,文字起こし,AIっぽい文章,AIライティング,話者識別,Notta Brain,ウェブ職TV,Claude,Infographic",
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
