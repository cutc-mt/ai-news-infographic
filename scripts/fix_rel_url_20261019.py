#!/usr/bin/env python3
"""infographic_url を相対パス(docs/xxx.html)へ揃えて再PUT+GET検証"""
import json
import urllib.request
import urllib.error

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app'
targets = {
    7830003: 'docs/20261019_okou_ai_onboarding_daniel.html',
    7830004: 'docs/20261019_claude_haiku55_zunmeta.html',
}

for nid, rel in targets.items():
    # GET で現在値を確認
    with urllib.request.urlopen(f'{BASE}/api/news/{nid}', timeout=30) as r:
        cur = json.loads(r.read().decode())
    if cur.get('infographic_url') == rel:
        print('already relative', nid, cur.get('infographic_url'))
        continue
    data = json.dumps({'infographic_url': rel}, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(f'{BASE}/api/news/{nid}', data=data,
                                 headers={'Content-Type': 'application/json'}, method='PUT')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print('PUT OK', resp.status, nid)
    except urllib.error.HTTPError as e:
        print('PUT HTTPError', e.code, nid, e.read().decode('utf-8', 'replace')[:300])
        continue
    # 検証
    with urllib.request.urlopen(f'{BASE}/api/news/{nid}', timeout=30) as r:
        v = json.loads(r.read().decode())
    print('VERIFY', nid, 'infographic_url=', v.get('infographic_url'),
          '| video_id=', v.get('video_id'), '| title=', (v.get('title') or '')[:30])
