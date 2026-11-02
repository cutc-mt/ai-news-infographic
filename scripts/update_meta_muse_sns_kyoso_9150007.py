#!/usr/bin/env python3
"""news_id=9150007 (AI共創イノベーション: Meta Muse SNS自動投稿) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 9150007

payload = {
    "title": "【AI自動運営】Meta Museでインスタグラム等のSNSに投稿する方法を徹底解説！フェイスブック・スレッズ等にも自動投稿できる！",
    "summary": "AI共創イノベーションが、MetaのAIエージェント「Meta Muse（メタ・ミューズ）」を使ったInstagram・Facebook・ThreadsなどSNSへの自動投稿方法を実演解説。MuseはMeta傘下のSNSと最初から連携しており、「インスタに投稿して」と普通に話しかけるだけで投稿文と画像を用意し、投稿前に「投稿していいですか？」の確認が来る承認制で安全に投稿できる。動画の最重要ポイントは投稿経路が2系統あることで、①ログイン不要の連携ルート（投稿・閲覧向け。ただし投稿後の文章変更は不可）と、②Muse内の仮想PCでブラウザを起動してログインし編集・削除を行う内部ブラウザルートを使い分ける。実演では「元の内容を面白くして」と依頼するとMuseがバックグラウンドでブラウザを操作してInstagramのWeb版投稿を自動で書き直す様子を紹介。ログイン時は「この端末を覚えさせる」を許可しないなどセキュリティ注意を強調し、怖い場合は投稿だけAIに任せ編集は自分で行うリスク軽減運用も推奨。規約によってはAIログインがまずいプラットフォームもあるため事前確認を促す。さらに、画像を組み合わせたパラパラ漫画方式のショート動画制作、サムネイルの自動取得（リンク化は不可）、ノートやブログ記事の執筆まで内部ブラウザで拡張可能。「インスタの運営は任せた」の一言でスケジュールを組んで自律的に投稿案を立て、審査・許可のフローで自動運営でき、プロフィール案（A/B案の自己紹介文）まで自ら提案する。相棒型AIとして情報発信を効率化できるというまとめ。",
    "infographic_url": "docs/20261102_meta_muse_sns_autopost_kyoso.html",
    "url": "https://www.youtube.com/watch?v=F1vDhj_lzvY",
    "video_id": "F1vDhj_lzvY",
    "tags": "Meta,Muse,Meta Muse,AIエージェント,Instagram,自動投稿,Facebook,Threads,SNS運用,AI自動運営,内部ブラウザ,連携ルート,ショート動画,AI共創イノベーション,Infographic",
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
print('GET video_id:', item.get('video_id'))
