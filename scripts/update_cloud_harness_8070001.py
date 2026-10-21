#!/usr/bin/env python3
"""news_id=8070001 (さとるチャンネル: PCを閉じてもAIが働き続ける新ハーネス) の
infographic_url / tags / summary を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070001

payload = {
    'title': '【徹底解説】Grok BotやChatGPTのdotsなど、PCを閉じてもAIが働き続ける新ハーネス',
    'summary': (
        'この秋、PCを閉じてもAIが働き続ける「エージェントハーネス」が大手からOSSまで一斉に登場。'
        'xAIのGrok Botは、アカウントに1台だけのクラウドPCを何体ものボットで分け合い、'
        'グループチャットで仕事を渡し合って並列で回す（プレミアム月30ドルから、ボットの使用量はGrok・Cursorの枠と別枠）。'
        'OpenAIのdotsはGPT-6 AstraをChatGPTの中に常駐させ、SlackやTeamsからも依頼でき、'
        '話しかけていない間は読み取り専用ツールだけで繋いだアプリを探索する「先回りサーチ」をコードで強制する'
        '（ChatGPT Pro月1万6,800円から、欧州・英国等を除き日本は対象）。'
        'MetaのMuseは暮らしとお店の用事の担当で、投稿の公開・送信・支払いは承認なしには実行しない'
        '（ほとんど無料、提供は米国とカナダのみ）。'
        '危ない操作は本体とは別の見張り役AI（Grok BotのAutoReview／dotsの自動レビュー／MuseのSentinel）が先に止めるが、'
        '最後に許可を押すのは人——「常に許可」で住所が送られた一件の教訓も。'
        'ほかにOpenAI Agents API（Codexのハーネスを借用、追加料金なし）、クラウドで動くClaude Cowork、'
        '日本のGoogle AI Proに数週間で順次くるGemini Spark（プロ月2,900円）、会社のMicrosoft 365環境にIDとPCを持つ'
        'Copilot Autopilot、Claude Codeをクラウドのデスクトップで回すSimular Sai（月50ドルから）、'
        'OSSのOpenClaw Enterprise・OpenHuman、ハーネスをAI自身が直すGoogle研究のHarness²まで、'
        '実際に動かした結果（Agents APIの「idle」の罠、OpenHumanの失敗隠蔽とAPIキー平文保存など）とともに解説。'
        '結論: 最初に試すのは今払っているAIプランについてくるもの。手順の決まった仕事を1つ任せるところから始める。'
    ),
    'tags': 'AIエージェント,エージェントハーネス,Grok Bot,dots,Meta Muse,OpenAI Agents API,Claude Cowork,Gemini Spark,Simular Sai,OpenClaw Enterprise,OpenHuman,Harness²',
    'infographic_url': 'docs/20261021_cloud_harness_grok_dots_muse.html',
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
