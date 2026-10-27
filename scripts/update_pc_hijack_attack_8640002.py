#!/usr/bin/env python3
"""news_id=8640002 (ウェブ職TV: PC乗っ取り攻撃) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8640002

payload = {
    "title": "90%以上の確率でPCを乗っ取られる悪魔の攻撃手法が見つかりました…",
    "summary": "ウェブ職TVの中島さんが、X（旧Twitter）で277万インプレッションを記録した衝撃のセキュリティ投稿を解説。セキュリティ機関4everが実際の顧客PCで捕獲した「野生の攻撃」で、過去30年のシステムセキュリティ常識がAI時代にゼロになったと指摘されています。攻撃の仕組みは、Chrome等のブラウザがプレーンテキスト（.md）を確認なしでダウンロードフォルダに自動保存する仕様を悪用。悪意あるウェブサイトにアクセスしただけでJavaScriptにより13KBの悪意あるCLAUDE.md／AGENTS.mdが静かに落ちてきます。約50%の開発者がやっているという「ダウンロードフォルダでClaude CodeやCodexを起動してファイル整理を頼む」行為が条件となり、エージェントが罠のMDをルールファイルとして忠実に実行。Codexでは成功率90%超で~/.codex/config.tomlに悪意あるMCPサービスを登録させサンドボックス・承認回避オプションを追加、トロイの木馬として常駐します。Claude Codeでは成功率約50%でclaude/settings.jsonを作成しベースURLをハッカーサーバーへ書き換え、ログイントークンを平文送信した上でサンドボックスを解除するbashコマンドでPCを直接乗っ取ります。最も恐ろしいのはCVEもパッチも存在しない点で、ブラウザの自動保存もAIのMD実行も「正常機能」のためOpenAI・Anthropicは対応できません。ウイルス対策ソフトでもただのテキストファイルは検知困難。対策は、①ダウンロードフォルダを作業ディレクトリにせず絶対に起動しない、②あらかじめダウンロードフォルダにCLAUDE.md等を作成して上書きを防ぐ（補助策）の2つ。ChatGPTなどチャットUIでは起こらず、ローカルで動くAIエージェント特有の問題です。動画後半では、ITリテラシーの重要性と、ITパスポート→基本情報→応用情報→登録スペ・ネスペという資格取得ロードマップも紹介しています。",
    "infographic_url": "docs/20261028_pc_hijack_attack_websyoku.html",
    "url": "https://www.youtube.com/watch?v=acbG_9yTesc",
    "video_id": "acbG_9yTesc",
    "tags": "セキュリティ,プロンプトインジェクション,Claude Code,Codex,CLAUDE.md,AGENTS.md,MCP,ダウンロードフォルダ,PC乗っ取り,トークン盗難,サンドボックス,ゼロデイ,ITリテラシー,ウェブ職TV,Infographic",
}

url = f'{BASE}/{NEWS_ID}'
req = urllib.request.Request(
    url,
    data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
    method='PUT',
    headers={'Content-Type': 'application/json'},
)
try:
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read().decode('utf-8')
        print(f'PUT HTTP {r.status}')
        print(body[:500])
except urllib.error.HTTPError as e:
    print(f'PUT HTTP {e.code}')
    print(e.read().decode('utf-8')[:800])
    raise SystemExit(1)

# 反映確認
with urllib.request.urlopen(f'{BASE}/{NEWS_ID}', timeout=30) as r:
    got = json.loads(r.read().decode('utf-8'))
item = got.get('item', got) if isinstance(got, dict) else got
print('GET id:', item.get('id'))
print('GET infographic_url:', item.get('infographic_url'))
print('GET title:', item.get('title', '')[:60])
print('GET tags:', item.get('tags', '')[:80])
