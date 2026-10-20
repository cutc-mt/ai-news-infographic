#!/usr/bin/env python3
"""PUT payload for news_id 7980001 (Cua Space SDK / まさおAIじっくり解説ch)."""
import json
import urllib.request

URL = "https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news/7980001"

payload = {
    "title": "【最高】AI専用の PC をコードで作れる『Cua Space』にSDK が遂に登場！Claude Code に専用 PC を",
    "source": "YouTube (まさおAIじっくり解説ch)",
    "url": "https://www.youtube.com/watch?v=sbGN5P17CKI",
    "video_id": "sbGN5P17CKI",
    "date": "2026-10-20",
    "category": "AIニュース",
    "summary": "Cuaの仮想環境サービス「Cua Space」にSDKが登場し、LinuxやmacOSのVMをコードから作成・操作できるようになりました。Claude CodeなどのCLIエージェントに専用PCを渡して自由に作業させることが可能です。スペースの作成・削除、ターミナル操作、カーソル操作、ピクチャーインピクチャーや人間の介入、チーム共有にも対応します。Grokボットの1アカウント1台形式と異なり、スペースA/B/Cと追加できる点が強みで、自作ハーネスやエージェントOS構築の有力な選択肢となります。",
    "tags": "CuaSpace,CuaDriver,SDK,ClaudeCode,エージェントOS,ComputerUse,AIニュース",
    "infographic_url": "docs/20261020_cua_spaces_sdk_masao.html",
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
