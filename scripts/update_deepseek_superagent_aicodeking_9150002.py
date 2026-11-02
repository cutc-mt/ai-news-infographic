#!/usr/bin/env python3
"""news_id=9150002 (AI Code King: DeepSeek SuperAgent Harness) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 9150002

payload = {
    "title": "I Tried Deepseek's New SuperAgent Harness... Is IT ANY GOOD?",
    "summary": "AI Code Kingが、DeepSeekのHarnessチームが公開した長文記事「Exploring Super Agent Design」を徹底解説。エージェントが自力で動けるようになった今、ボトルネックはモデルではなく人間の注意力（同時に追えるセッションは3〜5個が限界）だとする問題意識から、チャットやGitHubコメントなど既存の場所で1つのエージェントとだけ会話し、裏でセッションを自動生成・管理する「スーパーエージェント」設計を提案する。中核は二層構造で、人と話して仕事を割り振る長寿命の「ルーター」（bashツールなし・軽量モデルで十分）と、1タスクにクリーンなコンテキストを持つ隔離された「ワーカー」（コードを書く側に最強モデル）に分離。グループチャット・メール・レビューコメント・CI結果をすべてイベント（トリガー）として受け、通常コードでのフィルタ→自然言語ルールでのモデル判定の2段ろ過を通す。ワーカーは担当タスクのスレッド（PR等）を購読してイベントを直受けし、同じPRを触る複数ワーカーが自ら競合に気づける。コンテキストウィンドウをキャッシュとして扱い、IDリンクを辿る「想起の連鎖（Chain of Recall）」で数週間後の旧タスクも復元可能。DeepSeek自身のユーザーグループでは「サイレントに再現して直す」方針で、報告された問題をバックグラウンドで再現し、確認できれば議論中にPRを開く運用を実践。実験（1回約300メッセージ、実依頼約20件、コーディングは時間消費ツールでシミュレート、結果は参考値）では、典型的タスクが12.4分（遅いケース15.7分）に対し、中立プロンプトの単一セッションは5回中一度もサブエージェントを呼ばず29.5分——委譲はプロンプトではなく構造で強制すべきが最大の教訓。ルーターは1分あたり約40決定まで1セッションで持ち、決定あたり6.4秒→1.6秒に短縮。コストは1実行約2,320万キャッシュ読みトークンで、安いモデル（DeepSeek V4.1 Flash等）でこそ割に合う設計。未解決は長期記憶と、外部イベント経由のプロンプトインジェクション（クラウドループ侵入で接続マシン全体が危険化）というセキュリティ。実践編として、無料OSSデスクトップアプリPandaCodeの常駐「ボット」機能でルーターbot（拒否ルールでshell/edit禁止）＋ワーカーbot（Kimi K3.1 Pro/GLM 5.3等）＋30分毎のウォッチドッグbotを組み、月9.99ドルのKlein Pass定額プランやスケジュール実行のクライアントデスクトップで夜間PRレビュー等の固定ジョブを回す構成を紹介。GitHubの試作DSH Super Agentは研究用コードで承認なしにコマンド実行するため隔離環境での利用を推奨。",
    "infographic_url": "docs/20261102_deepseek_superagent_harness_aicodeking.html",
    "url": "https://www.youtube.com/watch?v=ZIcvDE0HoWE",
    "video_id": "ZIcvDE0HoWE",
    "tags": "DeepSeek,SuperAgent,DSH,エージェントハーネス,ルーター,ワーカー,トリガー,プロンプトインジェクション,Chain of Recall,PandaCode,Klein Pass,Kimi,GLM,AI Code King,コーディングエージェント,Infographic",
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
