#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PUT payload for news_id 7980004 (mikimiki web スクール / Claude basics)."""
import json
import urllib.request

URL = "https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news/7980004"

payload = {
    "title": "【最新版】超初心者OK！Claudeの使い方・基礎をわかりやすく徹底解説(P90超資料付き)",
    "source": "mikimiki web スクール (@mikimikiweb)",
    "url": "https://www.youtube.com/watch?v=-cr4a60X2N4",
    "video_id": "-cr4a60X2N4",
    "date": "2026-10-20",
    "category": "AIニュース",
    "summary": ("Claude超入門ガイド。Anthropic開発の生成AI「Claude」のはじめ方から、"
                "モデル・プランの選び方、プロンプト5要素の型、Web検索・スライド作成・アーティファクトなどの全機能を解説。"
                "さらにClaude Cowork / in Chrome / Claude Codeのエージェント機能の使い分けやOffice・Slackとの連携、"
                "ハルシネーション対策といった安全な使い方まで、仕事で使える活用術を1本にまとめています。"),
    "tags": "Claude,Anthropic,AI入門,プロンプトエンジニアリング,AIエージェント,仕事の効率化",
    "infographic_url": "docs/20261020_claude_basics_mikimiki.html",
}

req = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="PUT",
)
with urllib.request.urlopen(req, timeout=30) as resp:
    body = resp.read().decode("utf-8")
    print("HTTP", resp.status)
    print(body[:2000])
