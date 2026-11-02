#!/usr/bin/env python3
"""news_id=9150001 (AI大学: Canva Craft) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 9150001

payload = {
    "title": "【無料でも超高性能】Canva初の独自画像生成AIモデル「Canva Craft(キャンバ・クラフト)」徹底解説！ ～性能・使い方・マジックレイヤーを使った活用事例～",
    "summary": "AI大学【AI&ChatGPT最新情報】が、Canvaが2026年10月23日に公開した同社初の独自開発画像生成AIモデル「Canva Craft（キャンバ・クラフト）」を2章構成で解説。Canva Researchがゼロから開発したデザイン特化モデルで、まず画像の構図（テキストとオブジェクトの配置・サイズ）を設計してから画像を生成する2段階方式により、レイアウトの再現性と日本語を含む文字表示精度が高い。数百万点のCanvaプロ級テンプレートを学習し、プロデザイナーによる25,000組以上の画像セット評価・フィードバックでレイアウトとタイポグラフィの原則を習得。最大2K解像度・30以上のアスペクト比に対応し、プロンプトは日本語含む多言語、画像内テキスト描画は日本語含む55言語に対応。LMSYS Chatbot Arenaの画像生成AIカテゴリで総合4位（企業別ではOpenAIに次ぐ2位）、ポートレート部門87モデル中1位、風景・自然部門85モデル中1位、抽象パターン2位、プロダクト4位。使い方はCanvaにログインし左サイドバーのMagic Studioからアクセス、無料ユーザーでも利用可能（月間利用上限あり、設定のAI使用状況で確認可能）。テキストから画像を生成すると4枚が提示され、編集ボタンからテキスト指示による詳細編集ができる。マジックグラブでは画像内のテキストや背景を要素分解して文字を直接書き換え可能。実測では写実的なポートレート・動物・風景でトップモデル並みの品質で、街角の看板の日本語も正確に表示。日本語入りのインフォグラフィック、ブログサムネイル、チラシ、ポスター、漫画も生成でき、小さい文字のつぶれや難読漢字の文字化けが起きにくい。今後は外部開発者向け公開APIの提供に加え、公式Canva MCPサーバー対応でAIエージェントからの利用が可能になる予定。参照画像ベースの生成、高度な画像編集、高速モデルの開発も進む。あわせて10月30日にはレイアウトとレイヤー全体の美しさを理解して編集する新モデル「Brush」も発表され、有料ProユーザーがCanva AIページから利用できる。",
    "infographic_url": "docs/20261102_canva_craft_image_gen_ai_daigaku.html",
    "url": "https://www.youtube.com/watch?v=7crERNYKsNs",
    "video_id": "7crERNYKsNs",
    "tags": "Canva,Canva Craft,キャンバ・クラフト,画像生成AI,マジックレイヤー,マジックグラブ,Magic Studio,Brush,Canva Research,LMSYS Chatbot Arena,日本語描画,テキストから画像,Canva MCP,AI大学,無料AIツール,Infographic",
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
