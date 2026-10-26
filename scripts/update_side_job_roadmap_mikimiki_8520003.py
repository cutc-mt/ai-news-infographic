#!/usr/bin/env python3
"""news_id=8520003 (mikimiki web スクール: 在宅副業 月10万円ロードマップ) の infographic_url / tags / title / summary をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8520003

payload = {
    "title": "【在宅/スキマ時間】スキル0から始められる副業！月10万円を稼ぐ全手順・ロードマップ",
    "summary": "mikimiki web スクールが、未経験・在宅・スキマ時間で始められる8つの副業と月10万円までの全手順・ロードマップを解説。副業経験者は4年で1.4倍だが年間収入30万円以下が約半数・100万円超えは20%という現実を踏まえ、月10万円の目安を時給2000円×50時間と設定。稼げる副業の3条件（継続案件になりやすい／単価が上がる道がある／AIを味方にできる）で選定した8つの副業は、ショート動画編集（CapCut、1本5000円×20本）、Canvaデザイン・資料作成（1件5万円×2件）、専門ライター、SNS運用代行（1社月5万円×2社）、オンライン事務（月20時間で3〜5万円×2社）、インサイドセールス、AI業務効率化サポート（仕組み作り4万円＋月額2万円×3社）、ノーコードWeb・ネットショップ制作（Shopify／WordPress、1件10万円）。好き・得意・経験からの副業診断、0→1万→5万→10万円の成長3段階、最初の3ヶ月を研修期間と考える心構え、確定申告（給与以外20万円超）や住民税申告・会社の副業ルール確認などの注意点、「単価は任せられる範囲で決まる」掛け算戦略まで収録。",
    "infographic_url": "docs/20261026_side_job_roadmap_mikimiki.html",
    "tags": "副業,在宅副業,月10万円,ショート動画編集,CapCut,Canva,SNS運用代行,オンライン事務,AI業務効率化,ノーコード,Shopify,WordPress,ロードマップ,Infographic",
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
