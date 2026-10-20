#!/usr/bin/env python3
"""Payload for news_id 7980003 (KEITO AI agent security video) - PUT update."""
import json
import urllib.request

URL = "https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news/7980003"

payload = {
    "title": "【知らないと危険】AIエージェントから情報が漏れる理由と今すぐできる対策",
    "source": "KEITO【AI&WEB ch】(YouTube)",
    "url": "https://www.youtube.com/watch?v=xhm4jlXtzMU",
    "video_id": "xhm4jlXtzMU",
    "date": "2026-10-20",
    "category": "AIニュース",
    "summary": "AIの登場で攻撃側のコストが約1/10に下がり、セキュリティの弱い日本が集中的に狙われて情報漏洩が急増していると、KEITO氏がIPA・Gambit Security・Anthropicの3つの根拠とともに解説。Claude Codeの「読む・実行する・外に出る」能力がそのまま情報流出の出口になる仕組みとプロンプトインジェクションの実態を整理した上で、権限モード4種、settings.jsonのDeny/Ask/Allow/Hook設定、プロジェクトルート起動やAPIキーのローテーションなどの基礎対策5つ、MCP連携の危険性と.mcp.jsonの注意点、OSレベルで守るサンドボックス活用までを順を追って紹介する。",
    "tags": "AIエージェント,Claude Code,セキュリティ,情報漏洩,プロンプトインジェクション,MCP,サンドボックス,権限設定",
    "infographic_url": "docs/20261020_agent_security_claude_code_keito.html",
}

req = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="PUT",
)
with urllib.request.urlopen(req, timeout=30) as resp:
    print("HTTP", resp.status)
    print(resp.read().decode("utf-8")[:2000])
