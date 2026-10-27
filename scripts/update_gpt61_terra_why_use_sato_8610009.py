#!/usr/bin/python3
"""news_id=8610009 のAPI更新（PUT）→ GETで反映確認"""
import json
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = '8610009'

payload = {
    'title': 'GPT-6.1 Terra（テラ）を使った方がいい理由を徹底解説！GPT Sol・Claude Sonnetと比較',
    'summary': ('OpenAIのGPT-6.1ラインナップに加わったTerra（テラ）は、自然な文章力と画像理解に強く、'
                'Sol比で約3倍の速さと半分のAPI価格を両立する量産向けモデル。AIエージェント系ベンチマークでは'
                '部分的にアストラやSolを超え、ルナの代替としても推奨される。動画ではClaude Sonnetとのコスト比較に加え、'
                'Codexでの動画制作・サムネイル生成・note執筆を実演。Solで探索してスキル化し、Terraでエフォート高めに回す'
                '使い分けが結論。'),
    'infographic_url': 'docs/20261027_gpt61_terra_why_use_sato.html',
    'url': 'https://www.youtube.com/watch?v=JS_pLng0rQY',
    'video_id': 'JS_pLng0rQY',
    'tags': 'GPT-6.1 Terra,OpenAI,Codex,Claude Sonnet,ベンチマーク,AIエージェント,画像理解,モデル比較,AI共創イノベーション',
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
    data = json.loads(r.read())
print('GET title:', data.get('title'))
print('GET infographic_url:', data.get('infographic_url'))
print('GET video_id:', data.get('video_id'))
