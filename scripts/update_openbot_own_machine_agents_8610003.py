#!/usr/bin/python3
"""news_id=8610003 (OpenBot / AICodeKing) をPUTで更新"""
import json
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = '8610003'

payload = {
    "title": "OpenBotでGrok Botの常駐AIチームメイトを自分のPCと既払いプランで動かす——無料デスクトップアプリを徹底解説",
    "summary": "AICodeKingが、Grok Botが示した「名前と仕事を持つ永続的なAIチームメイト」という製品形を自分のコンピュータで再現する無料アプリ「OpenBot」を解説。Grok Botはボットが米国のクラウドコンピュータ上で常時稼働しラップトップを閉じても仕事を続ける一方、コンピュータは自分のものではなくログインもクラウド側に残り、モデル選択は運営側の管理でCursorプランやSuperGrok購読と抱き合わせになる。OpenBotはMac/Windows/Linux対応の無料デスクトップアプリで、iPhone/Android/Webアプリから自分のマシンに接続でき、ソースコードはGitHubで公開。OpenBot自身はモデルを売らず、CodexはChatGPTプラン、Claude CodeはClaudeプラン、GeminiはGoogle AI Pro/Ultra、GrokはxAI APIキーなど既に支払い済みのプランをそのまま接続でき、OllamaやLM Studioのローカルモデルも利用可能。プロバイダを変更してもエージェントの役割・ワークスペース・会話は保持され、プラン上限や障害時には別プロバイダのバックアップモデルへ自動で切り替わる。共有チャンネルでのエージェント間の引き継ぎとレビュー、内蔵ブラウザ、ジョブキュー、Slack/Discord/Telegram連携、OS暗号化でログインやカードを保管するVault(1Password/Bitwarden接続)も搭載。常時稼働が必要なら自宅サーバーのほか、月20ユーロ/25ドルからのEUホストサーバーやTeams向け管理サーバーの選択肢がある。注意点として、現状は開発プレビューで初回同意後にアクションごとの承認なしのフルアクセスで動くこと、ライセンスがPolyform Non-Commercialで商用利用には別ライセンスが必要なことが挙げられる。",
    "infographic_url": "docs/20261027_openbot_own_machine_agents_aicodeking.html",
    "url": "https://www.youtube.com/watch?v=iuBuavIinH8",
    "video_id": "iuBuavIinH8",
    "tags": "OpenBot,Grok Bot,AIエージェント,ローカルファースト,AICodeKing,マルチエージェント",
}

req = urllib.request.Request(
    f'{BASE}/{NEWS_ID}',
    data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
    method='PUT',
    headers={'Content-Type': 'application/json'},
)
with urllib.request.urlopen(req, timeout=30) as r:
    print('PUT status:', r.status)
    print(r.read().decode()[:500])

# 反映確認
with urllib.request.urlopen(f'{BASE}/{NEWS_ID}', timeout=30) as r:
    data = json.loads(r.read().decode())
print('GET title:', data.get('title'))
print('GET infographic_url:', data.get('infographic_url'))
print('GET tags:', data.get('tags'))
