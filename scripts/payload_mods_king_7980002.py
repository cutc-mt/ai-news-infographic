#!/usr/bin/env python3
"""PUT payload for news_id 7980002 (Claude Code Mods 7選 / AI Code King)."""
import json
import urllib.request

URL = "https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news/7980002"

payload = {
    "title": "これらのClaude Code Modは本当に使える：Filetree、Replay Theater、Blast Radiusほか",
    "source": "YouTube (AI Code King)",
    "url": "https://www.youtube.com/watch?v=OTfS65T70L8",
    "video_id": "OTfS65T70L8",
    "date": "2026-10-20",
    "category": "AIニュース",
    "summary": "AI Code KingがClaude Code 2.1.287以降で使える拡張機能「Mod」の中から実用性の高い7つを解説します。会話の横にファイルツリーを表示するFiletree、編集セッションをステップ再生するReplay Theater、危険なbashコマンドを実行前に保留するBlast Radiusなどが対象です。並列エージェントの見える化（Agent Flow）、編集の衝突防止（Collision Guard）、繰り返しの指示の保存（Reflect）も紹介されます。一見節約に見えるCache Taxについては、キャッシュの前提条件やウォームアップ自体のコストなど注意点が詳しく説明されます。",
    "tags": "ClaudeCode,Mod,Filetree,ReplayTheater,BlastRadius,CollisionGuard,AgentFlow,Reflect,CacheTax,AIニュース",
    "infographic_url": "docs/20261020_claude_code_mods_aicodeking.html",
}

req = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="PUT",
)
try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        print("STATUS:", resp.status)
        print(resp.read().decode("utf-8")[:2000])
except urllib.error.HTTPError as e:
    print("HTTP ERROR:", e.code)
    print(e.read().decode("utf-8")[:2000])
