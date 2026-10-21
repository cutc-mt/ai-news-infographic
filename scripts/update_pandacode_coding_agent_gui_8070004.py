#!/usr/bin/env python3
"""news_id=8070004 (AI Code King: Panda Code) の
infographic_url / tags / summary を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070004

payload = {
    'title': '【徹底解説】12MB・4倍速・完全OSSのAIコーディングエージェントGUI「Panda Code」',
    'summary': (
        'AI Code King チャンネル運営者が自作したデスクトップアプリ「Panda Code」。'
        'Claude Code・Codex・Kimi Code・OpenCode・GLM・Mimo・Grok Build・Antigravity などの'
        'コーディングエージェントを1つのウィンドウで実行できる。'
        'OSのWebViewを使う設計でサイズ12MB・起動約0.3秒・アイドル時メモリ約130〜160MB'
        '（比較対象のT3 Codeは起動約3秒・約700MB）。'
        '無料・オープンソース（MIT）でアカウント登録・データ収集なし。'
        'モデルやプランは売らず、既に支払済みのコーディングプランをそのまま利用し、'
        'APIキーはキーチェーンに保存、自動通信は3種のみというプライバシー設計。'
        'プロンプトボックスでのエージェント×モデル選択、権限モード4種、'
        '承認バーとメッセージキュー・Command+Enterステアリング、'
        'ターン単位のdiffと内蔵Git、要素ピック・スクリーンショット対応の内蔵ブラウザ、'
        'iOS/Androidシミュレータ、スケッチ・ムードボード、'
        'Git Worktreeによる並行実行とmainへの安全マージ、GitHub（PR・Issue）統合、'
        '4列タスクボード、Architect＋最大3 Workerのエージェントチーム（混成・名前付きチーム対応）、'
        'Telegram/Slack/Discord/WhatsAppボット、TartによるmacOS/Linux仮想マシン、'
        'Daytona/Cloudflare/AWSサンドボックスとVercel等へのデプロイ、'
        '使用量ダッシュボード・resume at reset・トークンセイバー（フォローアップ約8秒→約4秒）まで統合。'
        '注意点は未署名警告、シミュレータ・VMがMac中心、エージェント側変更への追従は自動更新で補うの3点。'
        'セルフビルドは clone → npm ci → npm run desktop。'
    ),
    'tags': 'AI Code King,Panda Code,コーディングエージェント,Claude Code,Codex,GLM,オープンソース,開発ツール,GUI',
    'infographic_url': 'docs/20261021_pandacode_coding_agent_gui.html',
}


def main() -> int:
    url = f'{BASE}/{NEWS_ID}'
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        method='PUT',
        headers={'Content-Type': 'application/json'},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = json.loads(r.read().decode())
            print(f'PUT HTTP {r.status}')
            print(f"  title: {body.get('title', '')}")
            print(f"  tags: {body.get('tags', '')}")
            print(f"  infographic_url: {body.get('infographic_url', '')}")
    except urllib.error.HTTPError as e:
        print(f'PUT HTTPError {e.code}: {e.read().decode("utf-8")[:400]}')
        return 1

    # 反映確認
    with urllib.request.urlopen(url, timeout=30) as r:
        got = json.loads(r.read().decode())
    ok = (
        got.get('infographic_url') == payload['infographic_url']
        and got.get('tags') == payload['tags']
    )
    print(f"GET  infographic_url={got.get('infographic_url')} tags={got.get('tags')}")
    print('VERIFY ' + ('OK' if ok else 'NG'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
