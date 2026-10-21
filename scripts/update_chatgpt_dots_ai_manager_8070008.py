#!/usr/bin/env python3
"""news_id=8070008 (AI共創イノベーション: ChatGPT Dotsで自分専用AIマネジャー) の
infographic_url / tags / summary を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070008

payload = {
    'title': '【AI秘書】ChatGPT Dotsの使い方！自分専用AIマネジャーを作る方法【Google Drive・Codex連携を実演】',
    'summary': (
        'OpenAIのクラウドエージェント「ChatGPT Dots（ドッツ）」を実演解説。'
        'クラウド上の仮想PCをAIが自分で操作し、PCを閉じても指示した作業が自動で継続する。'
        '中にはAsterが入っており操作が非常に上手く、ペイントでの描画やBlenderでの3D制作も高品質。'
        '作成物は取り出しやすいようGoogle Driveに保存させ、'
        '「ドッツのワンダフル」フォルダを拠点にAIエージェントのファイル・報告・メモリー・スケジュールを設計。'
        'エージェントに名前を付けると文脈が生まれ、「ヘリたんに探索やっといて」と名前指名で指示できる。'
        'ワーキングメモリーにはCodexやClaudeのリセット・クレジット期限を登録して期限が近づいたら通知。'
        'スケジュールタスクではゴミ出し3日分の毎朝通知、メール・カレンダー・ワーキングメモリー確認を'
        '1つの「毎日のマネジメント」タスクにまとめ、AI論文・ニュース取得や自分の動画・note記事の改善提案も自動化。'
        '朝は「おはようワンダーさん」のブリーフィングで一日が始まる。'
        'さらにDotsを「頭」、Codexを「手足」とする間接連携でローカルやiCloudへの書き出しを実演——'
        '「ダイヤモンドのように光る3Dイチゴ」を、ユーザーが打ったプロンプトより複雑なプロンプトをDotsが自律的に構成し、'
        'Blenderを勝手に選んで制作。使うのはアイデア次第で、生活・仕事・遊びまで支える自分専用AIマネジャーが作れる。'
    ),
    'tags': 'ChatGPT Dots,OpenAI,AIエージェント,AIマネジャー,Aster,Google Drive,Codex連携,Blender,ワーキングメモリー,スケジュールタスク,自動化,在宅エージェント',
    'infographic_url': 'docs/20261021_chatgpt_dots_ai_manager.html',
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
