#!/usr/bin/env python3
"""news_id=8610008 の API 更新（PUT）— Dessa voice AI (ずんめたラボ)"""
import json
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = '8610008'

payload = {
    'title': '【Dessa】声だけで学んだ会話AIは何が人間っぽい？ ChatGPTの声・Gemini Liveと比較｜今知っておきたいAI',
    'summary': ('ジャック・ドーシー氏が率いるBlockが、会話AI「Dessa」を研究プレビューとして発表。'
                '文字も学習済みモデルも使わず人の会話の声だけで一から学習させた、知る限り世界初の会話AIです。'
                '声を文字に変えないため感情や皮肉・笑い声・ため息が落ちず、聞きながら同時に話し、話の途中ですぐ笑う・大きな声でと頼むと実際に大きくなるなどの振る舞いを見せます。'
                'ただし聞きながら話すのはGPT-Liveにも可能で、本当の違いは学び方。日本で今使えるのはChatGPTとGemini Liveで、Dessaは少数のAI安全研究者のみが利用可能。'
                'なりすまし・頼りすぎ・声の記録という3つの注意点と、お金の電話はかけ直すなどの防衛策も解説します。'),
    'infographic_url': 'docs/20261027_dessa_voice_ai_zunmeta.html',
    'url': 'https://www.youtube.com/watch?v=uQafiY5r0-A',
    'video_id': 'uQafiY5r0-A',
    'tags': 'Dessa,Block,音声AI,会話AI,ChatGPT,Gemini Live,GPT-Live,ずんだもん',
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
print('GET check:')
print('  title:', data.get('title'))
print('  infographic_url:', data.get('infographic_url'))
print('  video_id:', data.get('video_id'))
print('  tags:', data.get('tags'))
