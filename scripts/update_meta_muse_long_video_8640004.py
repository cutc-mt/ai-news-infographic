#!/usr/bin/env python3
"""news_id=8640004 (AI共創イノベーション: Meta Muse 長尺動画生成) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8640004

payload = {
    "title": "Meta Museで10分以上の長尺動画生成できる方法を解説！プロンプトでAIエージェントの仮想PCを操作",
    "summary": "AI共創イノベーション（ワンダ佐藤）が、MetaのパーソナルAIエージェント「Muse（ミューズ）」で10分を超える長尺動画を生成する手法を実演。Museの標準動画生成は10秒程度が上限だが、Muse内部のクラウド上に用意された仮想PCをプロンプトで操作し、PythonやFFmpegを動かしてレンダリングすれば長尺化できる。レシピは「ポッドキャスト音声×画像生成×コーディング」の組み合わせで、ポッドキャスト音声はチャットから直接生成可能（1回あたり約5分）。5分＋5分の分割戦略で実際に10分4秒の動画が完成した。裏側では画像複数枚の生成→Pythonによる切り貼り・加工→FFmpegでのレンダリングが何度も反復されている。デフォルト設定では品質はまだ発展途上で、画像・背景色・アニメーションの指定をプロンプトで書き込むことで品質が大きく向上する。Museのキャラクター「ムース」はユーザーのアバター変更が動画内に反映される（プリズム化の事故例あり）。プロンプトは音声入力の雑な指示でも成立する。完成動画はダウンロード可能で「Googleドライブに保存して」の一言でドライブ保存もできる。作り込んだスタイルはSKILL.mdとして保存すれば次回から簡単な指示で再現可能。3D・宇宙映像の生成も可能で別動画での解説を予定。5〜10分クラスの動画をサブチャンネルで展開する構想も明かされた。",
    "infographic_url": "docs/20261028_meta_muse_long_video_aikyoso.html",
    "url": "https://www.youtube.com/watch?v=9Yie_oT4LYM",
    "video_id": "9Yie_oT4LYM",
    "tags": "Meta,Muse,長尺動画生成,仮想PC,Python,FFmpeg,ポッドキャスト音声,画像生成,SKILL.md,AI共創イノベーション,ワンダ佐藤,動画生成AI,Infographic",
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
