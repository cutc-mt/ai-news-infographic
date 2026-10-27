#!/usr/bin/python3
"""news_id=8640001 (Manu AGI: Top AI Agent Projects) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8640001

payload = {
    "title": "Top AI Agent Projects : VibeiDE, Strawberry, AI Bridge, Many【Manu AGI】今週の注目AIエージェントプロジェクト20選",
    "summary": "Manu AGI - AutoGPT Tutorials による週次「今週のトップAIエージェントプロジェクト」まとめ。動画タイトルに挙がった5本が注目株。(1) VibeiDE はコーディングエージェントを並列実行するデスクトップのコマンドセンターで、Claude Code・Codex・OpenCode を自分のサブスクリプションで持ち込み、各タスクに実際のターミナルを開いてエージェントを起動。複数プロジェクトのキュー投入、アニメーションオフィス/バッテリーに優しいグリッドの監視ビュー、カラーコード付きキューでプロバイダー制限を可視化し、完了前のレビューはトークン課金なし。macOS/Windows 対応で14日間の無料トライアル。(2) Strawberry 1.0 はAIチームメイトを内蔵したブラウザで、18億のWebサイトすべてでサインイン済みアカウント内で動作。リード調達、1000件のスプレッドシート充実、会議の文字起こし、ブランド資料作成、繰り返し作業の自動操縦をエンドツーエンドで処理し、取り返しのつかないアクション前に確認、パスワードはデバイス上で暗号化、SOC2/GDPR準拠。(3) AI Bridge はコーディングエージェントをチームのように運用するMacアプリ。「プロジェクト」（全エージェントへの指示）と「ワークスペース」（独自のルール・ファイル・リポジトリ・ツールを持つ責任領域）で作業を整理し、実ターミナルで動く本物の Claude Code/Codex/Grok/OpenCode CLI を状態ブリッジで追跡。要求を1つの受信ボックスに集約し、Kubernetes・Postgres・MongoDB・Slack を承認待ち権限付きでグリッド表示。すべてテレメトリなしのプレーンなYAML/MarkdownとしてMac上で実行。(4) ManyAgents は Claude Code と Codex のチームを同時実行するネイティブMacアプリ。オーケストレーターがリクエストをタスクに分割し各タブで追跡、既存プランで追加料金なし。各ワーカーは独自ワークツリーで干渉せず、思考担当が設計判断、レビュー担当が別プロバイダーで読み取り専用チェック。組み込みブラウザとiOSシミュレーターを搭載し、コードは分析なしでMac上に保持。(5) Moli by Lexmount はエージェント向けにゼロから構築されたクラウドブラウザエンジンで、Chromeより起動が速くメモリも少なく、プロキシ対応の分離セッション、Web検索API、WebフェッチAPI、エージェント製品とペアリング。構造優先タスクはMoli、永続コンテキストや拡張機能はChromiumと使い分け、SDK/API/Playwrightから接続。このほか全レイヤー編集できるAIビジュアル生成 SurgePix、n8nワークフロー用ブランドチャットウィジェット N8N Chat UI、エージェント・コーディング・コンピュータ使用向けの高速低コストモデル MiniMax M3.1 Flash、頼む前にテキストを送るプロアクティブアシスタント Kiwi、人間とエージェントの共有ドライブ AgentGrid.io、OpenAIモデルをPCで実行する無料OSSの Llama（llama.app）、パスワードを見せずにログインさせる 1Password for Agents、Macのノッチに住む音声制御エージェント sideOS、エージェントの実利用ツールを毎日ランク付けする Agent Hunt（Monid搭載）、長編動画を会話から生成する MOVO AI、非技術チーム向けコーディングエージェント Ovren、音声間モデルファミリー ElevenLabs Realtime、Mac用プライベートAIメモリ ShogunAI、720p動画を高速生成する FLUX 3 Max（fal×Black Forest Labs）まで全20プロジェクトを解説。",
    "infographic_url": "docs/20261028_ai_agent_projects_manuagi.html",
    "url": "https://www.youtube.com/watch?v=eukxvE6QAmQ",
    "video_id": "eukxvE6QAmQ",
    "tags": "AIエージェント,Manu AGI,VibeiDE,Strawberry,AI Bridge,ManyAgents,Moli,Lexmount,コーディングエージェント,Claude Code,Codex,MiniMax M3.1 Flash,1Password,sideOS,AgentGrid,Monid,FLUX 3 Max,Infographic",
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
