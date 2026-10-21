#!/usr/bin/env python3
"""news_id=8070006 (ずんめたラボ: ChatGPT広告の実態調査) の
infographic_url / tags / title / summary を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070006

payload = {
    'title': '【ChatGPT】広告が出やすいのは誰？ 米大学が91のおとりアカウントで実態調査｜今知っておきたいAI',
    'summary': (
        '無料プランなどで表示され始めたChatGPTの広告。米ペンシルベニア大学とハーバード大学の研究チームは、'
        '人種3×所得3を組み合わせた91個のおとりアカウント（ソックパペット）を作り、'
        '町の回線から接続して毎日街の話題に触れながら、Reddit人気投稿146問やOpenAIの使い方調査95問など'
        '全335問（毎日共通30問）を約3週間（3月8日〜31日）かけて聞き、答えの下に出る広告を記録した。'
        'その結果、広告はアカウント作成から約2週間で出始め（最初の7日間は皆無）、'
        '所得が低いほど出やすいことが判明——出た人は世帯年収6万ドル付近、出なかった人は8万ドル付近に多く、'
        '人種では差が見られなかった（1グループの数が少ないため要継続観察）。'
        '出始めたアカウントの会話に広告がついた割合は低所得27.4％・中16.9％・高19.6％。'
        '全会話63,657回のうち広告が出たのは3,573回（5.61%）。'
        '広告は全3,602件で約57%が産業・IT関連サービス、1位Target（130回）・2位top10.com・3位Preply。'
        '買い物や美容の話題は約10〜14%で出やすい一方、人間関係は3%未満、医療・メンタル・政治にはほぼ出ず、'
        'OpenAIのルール通り「答えの下の別枠・スポンサード印付き」だった。'
        'ただし論文は今後変わる可能性を指摘。4月2日にはおとりと見破られたか広告が出なくなった。'
        '日本でも6月19日にテスト開始が発表され、気になる場合は設定の「広告の制御」から上位プランか'
        '無料回数の削減で対処できる。買う前は自分でも比べるのが大事。'
    ),
    'tags': 'ChatGPT,ChatGPT広告,ターゲティング広告,おとりアカウント,ソックパペット,ペンシルベニア大学,ハーバード大学,The Beginning of ChatGPT Ads,arXiv,OpenAI,AI広告,広告の制御',
    'infographic_url': 'docs/20261021_chatgpt_ads_sockpuppet_study.html',
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
