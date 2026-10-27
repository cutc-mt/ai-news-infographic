#!/usr/bin/python3
"""news_id=8610004 (EmDash / KEITO) をPUTで更新"""
import json
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = '8610004'

payload = {
    "title": "EmDash完全解説——WordPressからCloudflareのAIネイティブCMSへ本番のまま移管し、Claudeに話しかけるだけでサイト更新する方法",
    "summary": "KEITO【AI&WEB ch】が、Cloudflareが2026年9月28日に正式リリースした新CMS「EmDash」へのWordPress移行を、ドメイン移管・デザイン再構築・コンテンツ移行まで本番環境で実演する完全解説。EmDashはMITライセンスで無料・商用利用可で、PHPを使わずTypeScript/JavaScriptとAstroで構築され、ログインはIDやパスワードではなくパスキー(指紋認証など)のみ。データベースはCloudflare D1、画像はR2、サーバーはWorkersへ集約され、更新管理はEmDash本体だけで済む。最大の特徴はMCPを標準内蔵しており、Claude DesktopやスマホのClaudeアプリから「ニュースを投稿して」と伝えるだけで本番サイトが更新できる点。書き込み系ツールは承認制にでき、AIが触れるのは用意した投稿枠だけで静的にコーディングされた部分は変更できないため安全。移行は公式のEmDash Exporterプラグインでキーを出力しインポートするだけで記事・カテゴリー・SEO設定が移り、テーマデザインはFTPでダウンロードしたファイルをClaude Codeに渡して再構築させる。ドメインはネームサーバー変更とレジストラロック解除を経てCloudflareへ移管し、URLは変わらない。作業は丁寧にやっても3日程度で、移行サービスは10万円弱からの想定。",
    "infographic_url": "docs/20261027_wordpress_emdash_migration_keito.html",
    "url": "https://www.youtube.com/watch?v=kuRFAngTJsU",
    "video_id": "kuRFAngTJsU",
    "tags": "EmDash,Cloudflare,WordPress移行,MCP,AIネイティブCMS,KEITO,パスキー,Claude",
}

req = urllib.request.Request(
    f'{BASE}/{NEWS_ID}',
    data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
    method='PUT',
    headers={'Content-Type': 'application/json'},
)
with urllib.request.urlopen(req, timeout=30) as r:
    print('PUT status:', r.status)
    print(r.read().decode()[:300])

# 反映確認
with urllib.request.urlopen(f'{BASE}/{NEWS_ID}', timeout=30) as r:
    data = json.loads(r.read().decode())
print('GET title:', data.get('title'))
print('GET infographic_url:', data.get('infographic_url'))
print('GET tags:', data.get('tags'))
