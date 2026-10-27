#!/usr/bin/env python3
"""news_id=8610007 の API 更新（PUT）— Gemini agent skillset (PIVOT)"""
import json
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = '8610007'

payload = {
    'title': '【Gemini で AI エージェントつくってみた】自分専用 AI エージェントで仕事はどう変わる？/AI を使うから AI と働くへ',
    'summary': ('グーグル・クラウド・ジャパン提供「Gemini 企業活用 SKILL SET」第2弾。カスタマーエンジニアのスワッチさんが '
                'PIVOT のMC野嶋さんの業務ヒアリングをもとに、テーマ調査・番組準備アシスタント・台本レビューの3つのカスタムエージェントを構築。'
                'ノーコードの Workflow Builder を自然言語で操作してワークフローを自動構築し、過去動画のグラウンディングで「私風」の切り口や質問リスト・タイトル案・サムネまで生成。'
                'ファクトチェックの自動分類、スマホ対応の台本レビュー、スラッシュで起動するスキル、権限・ID管理などのガバナンス機能まで、'
                '「AI を使う」から「AI と働く」への定着の処方箋を実演する。'),
    'infographic_url': 'docs/20261027_gemini_agent_skillset_pivot.html',
    'url': 'https://www.youtube.com/watch?v=KyLlOyk023Y',
    'video_id': 'KyLlOyk023Y',
    'tags': 'Gemini Enterprise,AIエージェント,Workflow Builder,ノーコード,Google Cloud,PIVOT,業務効率化',
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
