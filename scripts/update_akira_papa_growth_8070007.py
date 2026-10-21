#!/usr/bin/env python3
"""news_id=8070007 (あきらパパ: AIで速くなったのに、なぜ成長した気がしない？) の
infographic_url / tags / summary を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070007

payload = {
    'title': '【AI時代の評価】AIで速くなったのに、なぜ成長した気がしない？新しい「上がるポイント」と自分の物差し',
    'summary': (
        'IT系YouTuberのあきらパパが、Claude CodeやCodexに毎日仕事を振り、'
        '前なら数日かかったことが1日で終わるようになった一方で「成長したなと感じる瞬間が減っている」違和感を言語化。'
        '雪山の「石の階段 vs AIというロープウェイ」という例えで、'
        '①段差はどこへ行ったのか（力は落ちていない、階段がなだらかな坂になって見えにくくなった）、'
        '②物差しは何を測っているのか（成果物の量と作業の速さはAIが一番得意で、山頂の写真はロープウェイでも徒歩でも同じ）、'
        '③新しい上がるポイントはどこか（何をAIに任せて何を任せなかったかという判断の質——問いを立てる・疑って止める・仕組みにする）を検証。'
        'ただしこの判断は成果物に残らず「雪の下に隠れる」。'
        '解き方は判断を一行で外に出すこと（雪の上の赤い目印の竿）で、'
        '実践としてObsidianの第2の脳に判断記録（任せたこと・任せなかったこと・理由）を残す。'
        '結論: 上がっていないのではなく上がった場所が見えないだけ——判断を一行で外に出し、物差しは自分で持っておく。'
    ),
    'tags': 'AI時代の評価,成長実感,判断の質,Claude Code,Codex,AI活用,雪山の例え,判断記録,Obsidian,第2の脳,物差し,キャリア',
    'infographic_url': 'docs/20261021_akira_papa_ai_growth_milestone.html',
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
