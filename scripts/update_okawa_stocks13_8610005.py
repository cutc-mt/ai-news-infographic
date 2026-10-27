#!/usr/bin/env python3
"""8610005: 大川智宏 日本株13選・米中間選挙 インフォグラフィック API更新 (PUT)"""
import json
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = '8610005'

payload = {
    'title': '【大川智宏の最新注目銘柄】注目の日本株13選／米中間選挙が招く波乱シナリオ／日米で株価急落リスク／AI相場の復活はいつか／コアウィーブ・ショックは収束へ／ディフェンシブ株の逆襲【マーケット超分析】',
    'summary': 'PIVOT「マーケット超分析」前編。智剣・OskarグループCEO兼主席ストラテジストの大川智宏さんが、日経平均6万2000円割れの急落局面について「バブル崩壊ではなく調整」と診断。年末想定は上7万円・下5万円台のレンジとします。コアウィーブ・ショックは自己資本比率約6%の財務不安が発端で、AIブーム終焉のサインではなく強者勝ち残りの選別時期と分析。11月3日の米中間選挙は民主党優勢ならAI・データセンター関連やトランプ銘柄が一時売られ得るものの、AI開発が止まる見込みは乏しいと指摘します。メモリ価格は中国勢（CXMT）の台頭で3期先に成長フラット、4〜5期先マイナスへ。検査・製造装置（アドバンテスト等）は個数で稼ぐため影響小。内需ではサイゼリヤの値上げ報道によるストップ高に象徴される通り、値上げ発表から60営業日で7〜8割の銘柄が上昇。ファーストリテイリング（海外比率約60%）やニトリ（同約40%）の値上げ×海外展開によるディフェンシブ株の逆襲に注目します。イベント集中の今週は中間選挙の結果確定を待つのが得策との結論。',
    'infographic_url': 'docs/20261027_okawa_japan_stocks13_midterm_pivot.html',
    'url': 'https://www.youtube.com/watch?v=X40xAu-N0LY',
    'video_id': 'X40xAu-N0LY',
    'tags': 'PIVOT,マーケット超分析,大川智宏,日本株,米中間選挙,コアウィーブ・ショック,日経平均,メモリ価格,ディフェンシブ株,値上げ銘柄',
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
