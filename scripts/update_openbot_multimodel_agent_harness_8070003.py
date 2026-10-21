#!/usr/bin/env python3
"""news_id=8070003 (まさおAIじっくり解説ch: OpenBOT解説) の
infographic_url / tags / summary を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070003

payload = {
    'title': '【今注目】話題の外ループハーネス『OpenBOT』を解説！GrokBOT風でマルチモデル対応！',
    'summary': (
        '複数のエージェント（ボット）を定義してチームのように働かせられるオープンソースのローカルアプリ「OpenBOT」を解説。'
        'GrokBOTとは違い、ClaudeのOpusとGPT系モデルなどを同じチームで混在させられるマルチモデル対応が最大の特徴で、'
        'ソースコードはGitHubで公開され、コミット数約1,800、今もリアルタイムで更新が続く。'
        'デスクトップアプリはmacOS・Windows・Linux対応で、iPhone（ベータ版）・Androidのモバイルアプリからも'
        'PC上のボットへ指示やモデル変更・メモリ／スキル追加ができる。'
        'エージェントは右クリックで作成し、ロール・指示・メモリ・推論レベル・バックアップモデルを設定。'
        'スキルはボットごとにオン／オフできマーケットプレイスから追加可能、'
        '「テーブル」は複数ボットで共有できる軽量データベース。'
        'タスクはデフォルトで同時2件まで並列実行し、3件目は待機、超過分はサブエージェント（Claude Sonnet／Claude Code）が処理。'
        '内部構造は「ボットファイル＋付け替え可能なCLIエージェント」で、イベントログ・定期実行・記憶はアプリ側に集約したシンプルな設計。'
        '作ったボットはURLで公開しコンテキストとルーティンごと共有でき、ダイナミックアイランド風UIで作業中タスクの停止・確認が可能。'
        '自分の複数マシン（例: Mac Studio＋MacBook）をサーバーとして登録すれば1つの操作席からリモート運用でき、'
        'Slack・Discord（メンションで指示）・Canva・PayPal・Figmaなどとの連携も用意。'
        'ルーティンは「毎日朝10時にハロー」と会話で作れてオン／オフ・テスト実行・スケジュール画面も完備。'
        '音声は入力モデル＋音声変換のパイプライン構成で、入力の質とリアルタイム性が課題。'
        '結論: GrokBOTを強く意識しつつマルチモデル・複数サーバー・モバイルで差別化する面白い選択肢で、'
        '自作ハーネス派にとって参考になる設計が多い。'
    ),
    'tags': 'AIエージェント,OpenBOT,外ループハーネス,マルチモデル,GrokBOT,エージェントハーネス,オープンソース,Claude Code,サブエージェント,ルーティン,Discord連携,マルチプロバイダー',
    'infographic_url': 'docs/20261021_openbot_multimodel_agent_harness.html',
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
