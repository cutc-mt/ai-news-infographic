#!/usr/bin/env python3
"""2026-10-19分: 既存エントリ(video_id)を検索してPUTで更新する"""
import json
import urllib.request
import urllib.error

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app'
updates = {
    "qSDwhJAC0wg": {
        "title": "【実機レビュー】Okou AIで新入社員オンボーディングを自動化——1つの依頼で計画・日程・Slack・メールまで完結",
        "summary": "テック系YouTuberのDaniel氏が、クラウド型AI自動化ツール「Okou AI」を実際の新入社員オンボーディング業務で検証。1つのプロンプトだけで、Googleドキュメントへの1週間のオンボーディング計画作成、Googleカレンダーでの会議スケジュール、Slackチャンネルへの入社アナウンス、ウェルカムメールの下書きまで完結した。3,000以上のコネクタに対応しローカル環境やコーディングの設定は不要。Claude Coworkとの主な違いは、エージェントやワークフローを共有するチーム向けワークスペース設計と、タスクごとに異なるプロバイダーのモデルを選べる点。メールは下書き保存して人の承認後に送信するなど、承認が必要な場面では人間が主導権を保てる設計。※本動画はOkou提供のスポンサードレビュー。",
        "source": "Daniel | Tech & Data",
        "date": "2026-10-18",
        "category": "AIツールレビュー",
        "url": "https://www.youtube.com/watch?v=qSDwhJAC0wg",
        "tags": "Okou AI,AI自動化,オンボーディング,Claude Cowork,AIエージェント,スポンサードレビュー",
        "video_id": "qSDwhJAC0wg",
        "channel_id": "@daniel-dann",
        "infographic_url": "https://cutc-mt.github.io/ai-news-infographic/docs/20261019_okou_ai_onboarding_daniel.html",
    },
    "x-e1bG1otO4": {
        "title": "Claude Haiku 5.5は本当にお得? 日本語の仕事3つで分かった「任せていい仕事」と本気モードの落とし穴",
        "summary": "Anthropicが2026年10月7日に公開した最軽量モデル「Claude Haiku 5.5」の中身を、ずんめたラボが解説。全プランのClaude.aiで選べ、API料金は100万トークンあたり入力0.10ドル・出力0.50ドルで、Sonnet 5.5とは20倍の差。ITmedia AI＋がお詫びメール・議事録・英文返信の日本語3課題で検証した結果、型の決まった文章ではHaikuの標準設定(ミディアム)がSonnet 5.5に近い点を大幅に安い費用(議事録は同点で約18分の1)で出した一方、取引の立場を読み取る英文では3回中2回が立場を取り違えた。さらに考える深さを最大(マックス)にすると費用は15.4倍・時間は12.6倍に跳ね上がり、Sonnet 5.5を普通に使うのとほぼ同費用になる。結論は「AIの値段を決めるのはモデルの単価より考えさせた量」——型の決まった仕事はHaikuミディアム、判断がいる仕事は上位モデルへ、日付・担当者・立場は最後に人が確認するのが正しい使い分け。",
        "source": "ずんめたラボ",
        "date": "2026-10-18",
        "category": "AIモデル",
        "url": "https://www.youtube.com/watch?v=x-e1bG1otO4",
        "tags": "Claude Haiku 5.5,Anthropic,Sonnet 5.5,GPT-6 Luna,API料金,AIモデル選び",
        "video_id": "x-e1bG1otO4",
        "channel_id": "@zunmeta_lab_ch",
        "infographic_url": "https://cutc-mt.github.io/ai-news-infographic/docs/20261019_claude_haiku55_zunmeta.html",
    },
}

# 1) 一覧から video_id で該当エントリを探す
found = {}
for path in ['/api/news', '/api/news?limit=200']:
    try:
        with urllib.request.urlopen(BASE + path, timeout=30) as r:
            data = json.loads(r.read().decode())
        items = data if isinstance(data, list) else data.get('news', data.get('items', []))
        for it in items:
            vid = it.get('video_id')
            if vid in updates:
                found[vid] = it
        break
    except Exception as e:
        print('list err', path, e)

if not found:
    print('NOT FOUND in list; items sample:', json.dumps(items[:1], ensure_ascii=False)[:400] if isinstance(data, list) or data else 'none')
else:
    for vid, it in found.items():
        print('FOUND', vid, 'news_id=', it.get('news_id') or it.get('id'))

# 2) PUT で更新
for vid, payload in updates.items():
    nid = found.get(vid, {}).get('news_id') or found.get(vid, {}).get('id')
    if nid is None:
        print('SKIP(no id)', vid)
        continue
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(f'{BASE}/api/news/{nid}', data=data,
                                 headers={'Content-Type': 'application/json'}, method='PUT')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print('PUT OK', resp.status, vid, 'news_id=', nid, resp.read().decode('utf-8', 'replace')[:200])
    except urllib.error.HTTPError as e:
        print('PUT HTTPError', e.code, vid, e.read().decode('utf-8', 'replace')[:400])
    except Exception as e:
        print('PUT ERR', vid, e)
