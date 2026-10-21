#!/usr/bin/env python3
"""news_id=8070009 (Latent Space Podcast: AI in NYC — How Tenex Builds an
AI-Native Engineering Team) の infographic_url / tags / summary を PUT で更新し、
GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070009

payload = {
    'title': '【成果で払うAIネイティブ組織】Tenexのストーリーポイント報酬とMetaHarness／エンタープライズAI導入の現実',
    'summary': (
        'Latent Space PodcastがAI Engineer New YorkでTenexのAlex Lieberman氏と'
        'Special Projects LeadのCJ Hess氏にインタビュー。'
        'Tenexは「AIアプリからAIネイティブへ」を支援するapplied AIパートナーで、'
        '設立18ヶ月で75人・90%がエンジニアかAIストラテジスト。顧客の50%はFortune 2000。'
        'エンジニア報酬はストーリーポイント単位の成果報酬で、最高と最低の給与差は約4倍、'
        '年100万ドル超を稼ぐエンジニアもいる。「AIは人間の知性と労働倫理へのレバレッジベット」'
        'というテーゼのもと、ポイント駆け引きや粗悪コードの懸念はAIストラテジストとの'
        'インセンティブ設計で未発生。今年のエンジニア生産性は約2倍（Opus 4.5から5.5の進化）。'
        '決定ログをすべてgitに残すMetaHarnessプロセス、Opus 5.5へのツール収斂とAmp/Orb活用、'
        'トークン支出比1:1〜2:1のコスト観。'
        'エンタープライズAI導入は汎用LLM展開90%・トレーニング60%・コーディングエージェント50%・'
        '非エンジニアリング領域の本番エージェント5%というマイルストーン格差があり、'
        '「存在しないプロセスは自動化できない」が口癖。'
        'バーティカルAI懐疑論とswyxの反論、Kill My SaaS（4万ドルのSaaSを1000ドルで置換）、'
        'AIと雇用の再配置論、NYCのAIエコシステム論まで。'
    ),
    'tags': 'Latent Space Podcast,Tenex,AIネイティブ,成果報酬,ストーリーポイント,MetaHarness,Opus 5.5,Amp,エンタープライズAI,コーディングエージェント,Kill My SaaS,AIと雇用,NYC',
    'infographic_url': 'docs/20261021_tenex_ai_native_engineering.html',
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
