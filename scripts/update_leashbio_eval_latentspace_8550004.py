#!/usr/bin/python3
"""news_id=8550004 (Latent Space Podcast: Leash Bio AI科学者評価) をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8550004

payload = {
    "title": "【答えを知るAI科学者評価】Leash BioのSARサンドボックス——予算100分子でLLMエージェントの科学的意思決定を採点、9万ロールアウトで失敗パターンを分類（Latent Space Podcast）",
    "summary": "Latent Space PodcastにLeash BioのIan Quigleyさんを再び迎え、DNAエンコードライブラリ（DEL）の大規模スクリーニングデータ（数百万化合物×数千タンパク質）を「答えのカギを知る」AI科学者評価環境へ変換する取り組みを解説。医薬品化学者の日常課題である構造活性相関（SAR）問題をゲーム化し、言語モデルエージェントにカタログと100分子の予算だけを与えてターゲットタンパク質に結合する良い分子を探索させる。エージェントは自然言語のSAR仮説を出力しながら限られた実験予算を配分し、早期に諦める・同じ分子を再テストし続ける・探索と活用のバランスを誤るといった人間と似た失敗パターンが観察された。環境全体が事前測定済みのため理想的な探索者との差を正確に採点でき、約90,000ロールアウトでモデルファミリー・性能レベル間の優れた分離を確認。分子情報を削除すると決定が悪化することから文脈内学習の証拠も示唆。ベイズ最適化は地形が尖りすぎた高次元のため不採用。一度記録すれば実質無限のロールアウトが可能な「償却済みラボ・イン・ザ・ループ」として、1日2個→20個ペースで環境量産を計画。約1000タンパク質のスクリーニング資産を巨大強化学習環境へ育て、RLの進歩を新しい生物学へ転移する挑戦と、限られた実験予算の使い方という意思決定科学との接続まで語る。プレプリント・データセット・ブログを同時公開。",
    "source": "Latent Space Podcast",
    "date": "2026-10-26",
    "category": "AIニュース",
    "url": "https://www.youtube.com/watch?v=vhPCo-8K78U",
    "tags": "LatentSpace,LeashBio,IanQuigley,DNAエンコードライブラリ,SAR,構造活性相関,AI科学者,エージェント評価,強化学習,ラボインザループ,創薬,LLMエージェント,Infographic",
    "video_id": "vhPCo-8K78U",
    "channel_id": "@LatentSpacePod",
    "infographic_url": "docs/20261027_leashbio_ai_scientist_eval_latentspace.html",
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
    print(f'PUT HTTPError {e.code}: {e.read().decode("utf-8")[:500]}')
    raise SystemExit(1)

with urllib.request.urlopen(url, timeout=30) as r:
    data = json.loads(r.read().decode('utf-8'))
print('GET check:')
print('  title:', data.get('title', '')[:80])
print('  infographic_url:', data.get('infographic_url', ''))
print('  tags:', data.get('tags', '')[:120])
