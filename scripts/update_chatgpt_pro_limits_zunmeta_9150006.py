#!/usr/bin/env python3
"""news_id=9150006 (ずんめたラボ: ChatGPT Pro利用枠2倍) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 9150006

payload = {
    "title": "ChatGPT Proの利用枠が2倍に Plusは？ APIクレジットも｜今知っておきたいAI",
    "summary": "ずんめたラボが、2026年10月にOpenAIが発表したChatGPT Pro向け変更を解説。Work（ワーク）とCodex（コーデックス）が共有する利用枠が2倍になり、対象はプロ（月100/200/500ドル）とBusinessプレミアム席で、料金は変わらない。一方で月20ドルのPlusは5時間ごとの目安がそのまま据え置かれ、変更なし。プロ200では10月10日に新規受付を停止し、GPT-6アストラの人気による利用増を理由に9月29日に再開。新規加入者には少ない枠が割り当てられ、10月30日から既存利用者も減らす予告が出ていたが、10月の発表で削減を撤回。少ない組は2倍にされて全員が同じ上限に統一された。プロ100・500とプレミアム席の枠は手続きなしで自動適用。さらにプロには月額と同額のAPIクレジット（プロ100=100ドル分、200=200ドル分、500=500ドル分）が付く。Businessはプレミアム席1つ100ドル分、標準席1つ20ドル分、会社計500ドルまで。ただしAPIキーで動かすコーデックスには使えず、ChatGPT/コーデックスの上限も増えない「別の財布」で、繰り越し不可、受け取りには同一メールアドレス・API組織オーナー・請求設定からの自分での有効化が必要。乗り換え判断は「Workやコーデックスで上限によく当たっているか」が基準で、使用量画面やコーデックスCLIの/statusで1〜2週に1回ペースを確認してから決めるべき。枠の節約コツ（指示を絞る・資料を関係分だけに・成果物の形を先に決める、AGENTS.mdを小さく、未使用MCP切断）も紹介。",
    "infographic_url": "docs/20261102_chatgpt_pro_limits_zunmeta.html",
    "url": "https://www.youtube.com/watch?v=lBwgxinYVO0",
    "video_id": "lBwgxinYVO0",
    "tags": "ChatGPT,ChatGPT Pro,OpenAI,Codex,Work,利用枠,APIクレジット,Pro 200,GPT-6,Plus,ずんめたラボ,サブスク,AIニュース,Infographic",
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
print('GET video_id:', item.get('video_id'))
