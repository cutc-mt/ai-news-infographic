#!/usr/bin/env python3
"""news_id=8370002 (Daniel | Tech & Data: 印刷後に変更できるQRコード) の
infographic_url / tags / summary / title を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8370002

payload = {
    'title': '【保存版】印刷した後にリンク先を変えられる！ダイナミックQRコードの作り方（QRTiger実演）',
    'summary': (
        'Daniel | Tech & Dataのダニエルさんが、QRコード作成サービス「QRTiger」を使った'
        'ダイナミックQRコードの作成手順を実演。'
        '数百枚の広告看板を掲載済みでも、キャンペーンが変わるたびに刷り直す必要はない——'
        '静的コード（情報がずっと変わらない向け）と動的コード（後でリンク先を変更可能）の違いを解説し、'
        '動的タイプを選んでURLを貼り付けて生成、パターン・形状・ロゴ追加でブランドに合わせてカスタマイズ、'
        '実機スキャンでテストするまでの流れを数分で示す。'
        'その後、管理画面の編集オプションからリンク先を更新すると、同じQRコードをスキャンしたのに'
        'YouTubeチャンネルへリダイレクトされることを実際に確認。'
        'さらに総スキャン数や主要なスキャン場所を確認できるトラッキング・分析機能も紹介。'
        'まとめでは「ダニエルズ・メンズウェア」の例を挙げ、週替わりセールからソーシャルメディア誘導へ'
        'ポスターはそのまま切り替えられることが物理広告への価値だと強調。'
        '印刷資産を使い捨てにせず、裏側のキャンペーンだけを差し替える運用方法が学べるチュートリアル。'
        '（※本動画はQRTiger提供のスポンサー動画）'
    ),
    'tags': 'ダイナミックQRコード,QRコード,QRTiger,マーケティング,物理広告,キャンペーン運用,印刷物,リダイレクト,スキャン解析,ブランディング,Daniel Tech and Data,スポンサードレビュー',
    'infographic_url': 'docs/20261025_dynamic_qr_code_qrtiger_daniel.html',
}


def main() -> int:
    url = f'{BASE}/{NEWS_ID}'
    req = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
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
