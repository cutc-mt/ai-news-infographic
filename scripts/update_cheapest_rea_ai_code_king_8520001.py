#!/usr/bin/env python3
"""news_id=8520001 (AI Code King: Cheapest REA Setup YET!) の infographic_url / tags / title / summary をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8520001

payload = {
    "title": "Cheapest REA Setup YET! (Deepseek V4.1+LeanREA)",
    "summary": "AI Code Kingが、Claude CodeやCodexがREA形式のプロンプトをブロックし始めた状況でも機能する、史上最安のリバースエンジニアリング構成を紹介。3つの要素は、REAの207ツールMCPサーバーを8KBのスキルファイル1個で置き換える「LeanREA」（Sonnet 5.5比較で38%高速・35%安価・精度同等・ターン数56%削減、単純な応答1つの消費トークンを約40万から約3万4千に圧縮）、KingBench 3で思考最大時に81.25%を記録しGemini 3.8 Flashと同率の「DeepSeek V4.1 Flash」、DeepSeek独自ハーネスdshで直接実行できるデスクトップアプリ「PandaCode」。API料金はオフピーク時で入力100万トークンあたり0.15ドル・出力0.60ドル・キャッシュ入力0.003ドルと、Sonnet 5.5比で入力約13倍・出力約17倍・キャッシュ約67倍安く、Sonnetで2.17ドルかかったLeanREAベンチマークは概算16〜17セントに。セットアップはnpm install -g @deepseek-ai/dsh、npx skills add aicodeking/leanrea、PandaCodeでV4.1 Flash選択とthinking effort最大設定（オフだとスコア約30ポイント低下）のみ。実演ではElectronアプリの検索機能解析を証拠付きで完了し、各主張を確認済み・推論・不明に分類。弱点として最難関タスクではOpus 5.5が優位なこと、コードがDeepSeekサーバーに送信されること、ピーク時は料金2倍であることに注意。",
    "infographic_url": "docs/20261026_cheapest_rea_codexking.html",
    "tags": "REA,LeanREA,DeepSeek V4.1 Flash,PandaCode,dsh,リバースエンジニアリング,Claude Code,Codex,AIコーディング,LLM,Infographic",
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
