#!/usr/bin/env python3
"""news_id=8070002 (AI大学: Gemini 4 Argon 徹底解説) の infographic_url / tags / title / summary をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070002

payload = {
    "title": "Googleの最先端AIモデル「Gemini 4 Argon」徹底解説！ ～性能・使い方・Antigravity・AI Studioを使った活用事例10選～",
    "summary": "AI大学が2026年10月中旬にGoogleが公開した最先端AIモデル「Gemini 4 Argon」を徹底解説。推論・コーディング・マルチモーダル能力を組み合わせて複雑なタスクを長時間継続実行でき、1回の回答で出力できるトークン数が従来の6万4000から最大100万へ拡大。金融・法務・税務などの専門業務やサイバーセキュリティにも強く、公式ベンチマークではGPT-6.1 Terra・Claude Fable 5.1・Claude Opus 5.5と同等の性能を示し、Artificial Analysis総合ランキングで同率4位、テキストアリーナで1位、エージェントアリーナで6位を獲得。Gemini・Google Antigravity（デスクトップアプリ・CLI版）・Google AI Studioで利用でき、API料金は導入期間中100万トークンあたり入力2ドル・出力10ドル（2026年11月30日終了後に4ドル・20ドルへ）。活用事例として開発編（Three.jsによる3Dゲーム生成、約400行プロンプトから全30項目管理のパーソナルWebアプリ、Nano Banana画像×パララックスの動くサイト、デスクトップアプリ・Chrome拡張機能）と実務編（JavaScriptのみのアニメーション動画、Gemini+Canvasで10枚のスライド資料、スプレッドシート調査まとめ、コーヒー豆価格上昇のレポート、制約条件を守る1万字超の日本語長文、図表・動画分析）の計10例を紹介。",
    "infographic_url": "docs/20261021_gemini4_argon_usecases_ai_daigaku.html",
    "tags": "Gemini 4 Argon,Google,Google Antigravity,Google AI Studio,Nano Banana,AIコーディング,AIモデル,LLM,Infographic",
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
