#!/usr/bin/env python3
"""8610006: コンフィデンシャルコンピューティング インフォグラフィック API更新 (PUT)"""
import json
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = '8610006'

payload = {
    'title': '【コンフィデンシャルコンピューティングとは？】AI時代のサイバー攻撃から自社を守る最新技術／123件過去最多のランサムウェア被害／処理中も暗号化で情報漏洩を防ぐ／日米欧のAI主権とデータ主権',
    'summary': 'PIVOTがコンフィデンシャルコンピューティング（秘密計算）を特集。Acompany CEOの高橋亮祐さんが解説します。2026年上半期のランサムウェア被害は警察庁集計で123件と過去最多。AIの高度化によりコーディング能力が向上した結果、脆弱性発見から攻撃実行までAIで完結する時代になりました。コンフィデンシャルコンピューティングはCPUやGPUのチップ上に「金庫」を作り、暗号化したまま計算処理を行う技術で、クラウド事業者やAIベンダー自身もユーザーデータを見られない状態を担保します。Apple Intelligenceは既に採用済みで、OpenAIは9月末のDevDayでプライベートインファレンスを発表、Anthropicも10月に米セキュリティ系スタートアップを買収。境界型から「入られても守る」侵入前提の多層防御への転換が進みます。導入はAWS・GCP・さくらインターネット等の対応クラウドから。KDDIが4000万人以上のユーザーデータを安全にAI活用する基盤として採用済み。秘密計算研究でNTT・NECが世界トップ級であり、ハードからソフトまで全部持つ国は米中以外では日本だけで、第3極としての輸出可能性があります。2030年頃には通信暗号化のように標準化が進む見通しです。',
    'infographic_url': 'docs/20261027_confidential_computing_acompany_pivot.html',
    'url': 'https://www.youtube.com/watch?v=QAERWR9nxwE',
    'video_id': 'QAERWR9nxwE',
    'tags': 'PIVOT,コンフィデンシャルコンピューティング,秘密計算,サイバーセキュリティ,ランサムウェア,Acompany,データ主権,AIセキュリティ,Apple Intelligence,OpenAI',
}

req = urllib.request.Request(
    f'{BASE}/{NEWS_ID}',
    data=json.dumps(payload, ensure_ascii=False).encode(),
    method='PUT',
    headers={'Content-Type': 'application/json'},
)
with urllib.request.urlopen(req, timeout=30) as r:
    print('PUT status:', r.status)
    print(r.read().decode()[:500])

with urllib.request.urlopen(f'{BASE}/{NEWS_ID}', timeout=30) as r:
    body = json.loads(r.read())
    print('GET title:', body.get('title'))
    print('GET infographic_url:', body.get('infographic_url'))
    print('GET url:', body.get('url'))
