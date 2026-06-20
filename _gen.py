#!/usr/bin/env python3
"""Generate the Abacus Studio infographic HTML."""
import os

filepath = os.path.join("docs", "20260620-Abacus-Studio-AI映像制作-画像動画音声統合ワークスペース.html")

css = """\
:root { --ui-color-1: #2D6A4F; --ui-color-2: #E76F51; --ui-color-3: #D8F3DC; --ui-color-4: #1B3A2D; --ui-color-5: #F4A261; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { background-color: #F0F7F4; font-family: 'Kaisei Decol', serif; color: #333; line-height: 1.6; }
.container { max-width: 2000px; margin: 0 auto; padding: 20px; }
.header { text-align: center; padding: 40px 20px; margin-bottom: 30px; background: linear-gradient(135deg, var(--ui-color-1), #40916C, var(--ui-color-2)); border-radius: 30px; color: white; position: relative; overflow: hidden; }
.header::before { content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%); animation: headerGlow 8s ease-in-out infinite; }
@keyframes headerGlow { 0%, 100% { transform: translate(0, 0); } 50% { transform: translate(20px, 20px); } }
.header-icon { font-size: 5em; margin-bottom: 10px; animation: fa-bounce 2s infinite; }
.header h1 { font-size: 2.4em; font-weight: 900; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
.header .subtitle { font-size: 1.3em; opacity: 0.9; font-family: 'Yomogi', cursive; }
.header .date { font-size: 0.9em; opacity: 0.7; margin-top: 10px; }
.section-layout { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; margin-bottom: 20px; }
.section-card { flex: 1; min-width: 280px; max-width: 450px; background-color: white; border-radius: 20px; padding: 20px; box-shadow: 5px 5px 15px rgba(0,0,0,0.1); position: relative; overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; }
.section-card:hover { transform: translateY(-5px); box-shadow: 8px 8px 25px rgba(0,0,0,0.15); }
.section-card::before { content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 5px; background: linear-gradient(90deg, var(--ui-color-1), var(--ui-color-5)); }
.mega-icon-container { text-align: center; margin: 15px 0; }
.mega-icon-container h2 { font-size: 1.3em; color: var(--ui-color-4); margin-top: 10px; }
.card-content { padding: 0 10px 15px; }
.keyword-list { margin: 15px 0; padding: 0; list-style-type: none; }
.keyword-list li { margin-bottom: 10px; display: flex; align-items: flex-start; font-size: 15px; line-height: 1.6; }
.keyword-list li i { margin-right: 8px; color: var(--ui-color-2); min-width: 16px; margin-top: 4px; }
.keyword-tag { background-color: var(--ui-color-3); color: var(--ui-color-4); padding: 3px 8px; border-radius: 5px; margin-right: 5px; display: inline-block; font-weight: bold; font-size: 14px; }
.speech-bubble { position: relative; background: #fff; border: 3px solid var(--ui-color-1); border-radius: 20px; padding: 12px 15px; margin: 15px 5px; font-family: 'Yomogi', cursive; box-shadow: 3px 3px 10px rgba(0,0,0,0.1); transform: rotate(-1deg); }
.speech-bubble::after { content: ''; position: absolute; bottom: -13px; left: 20px; border-width: 12px 8px 0; border-style: solid; border-color: var(--ui-color-1) transparent; display: block; width: 0; }
.speech-bubble.right::after { left: auto; right: 20px; transform: rotate(15deg); }
.speech-bubble.top::after { bottom: auto; top: -13px; border-width: 0 8px 12px; transform: rotate(-5deg); }
.speech-bubble.variant-1 { background: #FFF9E3; border-color: var(--ui-color-2); transform: rotate(1deg); }
.speech-bubble.variant-1::after { border-color: var(--ui-color-2) transparent; }
.speech-bubble.variant-2 { background: #FFE9E9; border-color: #E76F51; transform: rotate(-2deg); }
.speech-bubble.variant-2::after { border-color: #E76F51 transparent; }
.handwritten { font-family: 'Yomogi', cursive; font-size: 15px; line-height: 1.5; color: #333; }
.highlight { background: linear-gradient(transparent 60%, rgba(231,111,81,0.3) 60%); font-weight: bold; }
.footer { text-align: center; padding: 30px 20px; margin-top: 20px; background: linear-gradient(135deg, var(--ui-color-4), var(--ui-color-1)); border-radius: 20px; color: #ddd; font-size: 14px; line-height: 2; }
.footer a { color: var(--ui-color-5); text-decoration: none; font-weight: bold; }
.footer a:hover { text-decoration: underline; }
.fade-in-scale { animation: fadeInScale 0.6s ease-out forwards; opacity: 0; }
@keyframes fadeInScale { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }
.section-card:nth-child(1) { animation-delay: 0.05s; }
.section-card:nth-child(2) { animation-delay: 0.1s; }
.section-card:nth-child(3) { animation-delay: 0.15s; }
.section-card:nth-child(4) { animation-delay: 0.2s; }
@media (max-width: 1600px) { .section-card { min-width: 280px; } }
@media (max-width: 1200px) { .section-card { min-width: 320px; } }
@media (max-width: 900px) { .section-card { min-width: 380px; } }
@media (max-width: 768px) { .section-layout { flex-direction: column; } .section-card { width: 100%; min-width: auto; } }
"""

# Cards data: (icon, color, anim, title, items, bubble_text, bubble_icon, bubble_variant, bubble_pos)
cards = [
    # Row 1
    ("fa-cube", "var(--ui-color-1)", "fa-beat-fade 2s infinite", "①Abacus Studioとは何か", [
        ("fa-circle-info", "生成AIメディア制作のための<span class='highlight'>オールインワン型ワークスペース</span>"),
        ("fa-images", "画像生成・動画生成・編集をひとつの場所で完結"),
        ("fa-music", "音声生成やリップシンク、アップスケーリングにも対応"),
        ("fa-layer-group", "別々のプラットフォームを行き来する必要がない"),
    ], "ひとつのクリエイティブ環境で<br>最初のコンセプトから完成品まで！", "fa-wand-magic-sparkles", "", ""),
    
    ("fa-puzzle-piece", "var(--ui-color-2)", "fa-bounce 2s infinite", "②従来ツールの課題と解決策", [
        ("fa-triangle-exclamation", "多くのAIツールは<span class='highlight'>ひとつのことしか得意ではない</span>"),
        ("fa-link-slash", "ワークフローが複雑になると別ツールへの移動が必要"),
        ("fa-check-circle", "Abacus Studioはプロセス全体を同じ環境で管理"),
        ("fa-arrows-rotate", "ステップバイステップでアイデアを組み立てていく"),
    ], "ツール切替えゼロで<br>制作フローがスムーズに！", "fa-lightbulb", "variant-1", "right"),
    
    ("fa-palette", "#40916C", "fa-flip 3s infinite", "③アクセシビリティなUI設計", [
        ("fa-desktop", "高度な<span class='highlight'>技術的セットアップを前提としない</span>"),
        ("fa-hand-pointer", "直感的な操作でクリエイティブ作業に集中できる"),
        ("fa-comment-dots", "チャット形式の指示でAIに要望を伝える仕組み"),
        ("fa-user-gear", "各モデルの技術仕組みを意識する必要がない"),
    ], "「何を作りたいか」に集中すればOK！", "fa-face-smile", "variant-2", "top"),
    
    ("fa-bullseye", "var(--ui-color-1)", "fa-beat-fade 2s infinite", "④レビュー実例：エナジードリンク", [
        ("fa-beer-mug-empty", "実在する<span class='highlight'>エナジードリンクの缶写真1枚</span>から出発"),
        ("fa-bullhorn", "SNS向けのプロモーション映像に変換する"),
        ("fa-mobile-screen", "縦型UGCスタイルの動画が最終目標"),
        ("fa-headphones", "リアルな音声も追加して完成させる"),
    ], "静止画1枚から映像を作る<br>実践的なテストです！", "fa-mug-hot", "", ""),
    
    # Row 2
    ("fa-upload", "var(--ui-color-2)", "fa-bounce 2s infinite", "⑤ステップ1：写真のアップロード", [
        ("fa-cloud-arrow-up", "PCから<span class='highlight'>商品の静止画をアップロード</span>する"),
        ("fa-file-image", "基本的な缶の写真1枚がスタート地点"),
        ("fa-sitemap", "この画像をベースにフルシーケンスを構築"),
        ("fa-rocket", "以後の全工程を同じチャット内で進行可能"),
    ], "アップロードしただけで<br>AIが商品を理解してくれる！", "fa-arrow-up-from-bracket", "variant-1", ""),
    
    ("fa-pen-fancy", "#40916C", "fa-flip 3s infinite", "⑥ステップ2：詳細なプロンプト指示", [
        ("fa-pen-fancy", "マクロ撮影風の<span class='highlight'>マットアルミの質感</span>を指定"),
        ("fa-droplet", "冷たい結露の水滴を表現するよう指示"),
        ("fa-lightbulb", "プロのスタジオ照明で照らす設定を追加"),
        ("fa-eye", "あいまいではなく具体的な描写が重要"),
    ], "プロンプトが具体的なほど<br>結果の品質も上がるよ！", "fa-pencil", "", "right"),
    
    ("fa-brain", "var(--ui-color-1)", "fa-beat-fade 2s infinite", "⑦AIによる商品認識機能", [
        ("fa-magnifying-glass", "アップロード画像を<span class='highlight'>自動で分析・認識</span>する"),
        ("fa-tag", "ブランド名・ロゴデザイン・缶の質感を理解"),
        ("fa-shield-halved", "ランダム画像ではなく商品として扱う"),
        ("fa-list-check", "リデザインやバリエーション方向を提案"),
    ], "商品の特徴を自動で把握。<br>それが作品のクオリティに直結！", "fa-robot", "variant-2", "top"),
    
    ("fa-route", "var(--ui-color-2)", "fa-bounce 2s infinite", "⑧ライフスタイル方向の選択", [
        ("fa-person-running", "<span class='highlight'>スタジオ撮影ではなくライフスタイル風</span>を選択"),
        ("fa-hashtag", "SNSプロモ映像としての仕上がりを目指す"),
        ("fa-hand", "缶を人の手に自然に持たせるよう指示"),
        ("fa-paintbrush", "元の色とテクスチャを保持したまま統合"),
    ], "商品をリアルな生活シーンに<br>自然に馴染ませるのがポイント！", "fa-hand-point-up", "", ""),
    
    # Row 3
    ("fa-camera-retro", "#40916C", "fa-flip 3s infinite", "⑨生成画像の高品質な仕上がり", [
        ("fa-sun", "<span class='highlight'>自然光と柔らかい背景のぼかし</span>を表現"),
        ("fa-check-double", "リアルな商品統合で完成度が高い仕上がり"),
        ("fa-star", "プロフェッショナルなカメラワークを再現"),
        ("fa-thumbs-up", "チャットの次の指示でさらに進化が可能"),
    ], "スタジオ撮影レベルの<br>クオリティが簡単に手に入る！", "fa-gem", "variant-1", "right"),
    
    ("fa-video", "var(--ui-color-1)", "fa-beat-fade 2s infinite", "⑩静止画から動画への変換", [
        ("fa-face-smile", "キャラクターに<span class='highlight'>自然な笑顔とカメラ目線</span>を指定"),
        ("fa-glass-water", "商品を飲む動作を滑らかに生成"),
        ("fa-camera", "ハンドヘルド風の手ブレ感でUGC演出"),
        ("fa-clock", "8秒間の縦型クリップが完成"),
    ], "毎回ゼロからではなく<br>ステップを重ねて組み立てる！", "fa-play", "", ""),
    
    ("fa-volume-high", "var(--ui-color-2)", "fa-bounce 2s infinite", "⑪音声の追加：ナレーション", [
        ("fa-microphone", "同じチャット内で<span class='highlight'>ナチュラルな男性ボイス</span>を生成"),
        ("fa-user", "キャラクターに合った声を自動で付与"),
        ("fa-comments", "別のツールにエクスポートする必要がない"),
        ("fa-wand-sparkles", "マルチモーダル機能でシームレスに統合"),
    ], "映像と音声を同じ環境で<br>まとめて作れるのが強み！", "fa-microphone-lines", "variant-2", "top"),
    
    ("fa-drum", "#40916C", "fa-flip 3s infinite", "⑫効果音と環境音の生成", [
        ("fa-ring", "<span class='highlight'>アルミ缶を開ける音</span>をリアルに生成"),
        ("fa-glass-water-droplet", "飲む時の音も自然に再現"),
        ("fa-tower-broadcast", "軽いスタジオ環境音を背景に追加"),
        ("fa-sliders", "ボイス・効果音・環境音を同期して出力"),
    ], "写真1枚から映像＋音声の<br>プロモ映像が完成した！", "fa-headphones", "", "right"),
    
    # Row 4
    ("fa-mountain-sun", "var(--ui-color-1)", "fa-beat-fade 2s infinite", "⑬第2のワークフロー：シネマティック風景", [
        ("fa-house-chimney", "<span class='highlight'>木とガラスのモダンな山小屋</span>を生成"),
        ("fa-tree", "緑の山の斜面に配置する設定"),
        ("fa-cloud-sun", "ゴールデンアワーの朝の光を指定"),
        ("fa-smog", "谷間を漂うドラマティックな霧の演出"),
    ], "観光や不動産向けの<br>プレミアムな映像が作れる！", "fa-panorama", "", ""),
    
    ("fa-image", "var(--ui-color-2)", "fa-bounce 2s infinite", "⑭風景画像の高品質な生成", [
        ("fa-photo-film", "<span class='highlight'>ドキュメンタリー風のプレミアム感</span>を再現"),
        ("fa-cube", "シーンに奥行きがあり照明が高価に見える"),
        ("fa-diamond", "ラフなスケッチではなく洗練されたビジュアルに近い"),
        ("fa-certificate", "旅行業や高級不動産のプロモに最適"),
    ], "第1弾の生成で<br>すでに高品質な仕上がり！", "fa-award", "variant-1", "right"),
    
    ("fa-helicopter", "#40916C", "fa-flip 3s infinite", "⑮ドローン風のカメラワーク", [
        ("fa-arrows-up-down", "<span class='highlight'>ゆっくりスムーズな前方＋上方への移動</span>"),
        ("fa-jet-fighter", "プロのドローンショットのようなカメラワーク"),
        ("fa-wind", "樹木の微妙な揺れと朝の霧の流れを追加"),
        ("fa-sun", "ヘイズを通過する太陽光の変化を表現"),
    ], "プロの映像作家が撮ったような<br>カメラワークが自動で生成！", "fa-video", "variant-2", "top"),
    
    ("fa-leaf", "var(--ui-color-1)", "fa-beat-fade 2s infinite", "⑯環境音で雰囲気を完成させる", [
        ("fa-dove", "<span class='highlight'>静かな自然のアンビエント音</span>を追加"),
        ("fa-heart", "単に綺麗にするだけでなくムードを形成する"),
        ("fa-gauge", "ペーシングと最終的なフィーリングを整える"),
        ("fa-gem", "プレミアムプロモ映像に仕上がる"),
    ], "映像だけでなく<br>「雰囲気」まで作り込める！", "fa-music", "", ""),
    
    # Row 5
    ("fa-check-double", "var(--ui-color-2)", "fa-bounce 2s infinite", "⑰レビュー総括：プラットフォームの評価", [
        ("fa-star", "異なるツール間を<span class='highlight'>行き来することなく多彩な作業</span>が可能"),
        ("fa-arrow-trend-up", "画像の改善から動画化・音声追加まで段階的に進行"),
        ("fa-shuffle", "商品プロモからシネマティック風景まで幅広い用途"),
        ("fa-flask", "クリエイティブな実験を繰り返せるワークスペース"),
    ], "クリエイティブな<br>アイデアを素早く試せる！", "fa-fire", "variant-1", "right"),
    
    ("fa-lightbulb", "#40916C", "fa-flip 3s infinite", "⑱適用先と期待される効果", [
        ("fa-bullhorn", "商品広告のSNSプロモ映像制作に活用"),
        ("fa-hotel", "観光・ホテル・<span class='highlight'>高級不動産のプレミアム映像</span>"),
        ("fa-bolt", "アイデアのテストと洗練されたAIメディアの構築"),
        ("fa-paper-plane", "プロンプトの品質が結果に直結する"),
    ], "AI時代のクリエイターにとって<br>強力な制作ツール！", "fa-trophy", "variant-2", "top"),
]

# Build cards HTML
rows = []
for i, card in enumerate(cards):
    icon, color, anim, title, items, bubble, bicon, bvar, bpos = card
    
    items_html = "\n".join(
        f'<li><i class="fas {item_icon} fa-lg" aria-hidden="true"></i><span>{text}</span></li>'
        for item_icon, text in items
    )
    
    bubble_classes = "speech-bubble " + bvar + (" " + bpos if bpos else "")
    bubble_html = f'<div class="{bubble_classes}"><span class="handwritten"><i class="fas {bicon} fa-lg" style="color: var(--ui-color-5);"></i> {bubble}</span></div>'
    
    card_html = f'''<div class="section-card fade-in-scale">
    <div class="mega-icon-container">
        <i class="fas {icon} fa-5x" style="color: {color}; animation: {anim};" aria-hidden="true"></i>
        <h2>{title}</h2>
    </div>
    <div class="card-content">
        <ul class="keyword-list">
{items_html}
        </ul>
    </div>
    {bubble_html}
</div>'''
    rows.append(card_html)

# Split into rows of 4
card_groups = [rows[i:i+4] for i in range(0, len(rows), 4)]
rows_html = "\n".join(
    f'<div class="section-layout">\n{"".join(g)}\n</div>'
    for g in card_groups
)

full_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Abacus Studio - AIで画像・動画・音声を統合制作するワークスペース</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kaisei+Decol&family=Yomogi&family=Zen+Kurenaido&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
        {css}
    </style>
</head>
<body>
<div class="container">

<div class="header">
    <div class="header-icon"><i class="fas fa-film" aria-hidden="true"></i></div>
    <h1>Abacus Studio でAI映像制作の常識が変わる</h1>
    <p class="subtitle">画像・動画・音声をひとつのワークスペースで統合生成</p>
    <p class="date">📅 2026年6月20日</p>
</div>

{rows_html}

<div class="footer">
    🎬 動画: <a href="https://www.youtube.com/watch?v=GrMo5NwozPs" target="_blank">Abacus Studio - AI Creative Workspace for Images, Video &amp; Audio</a><br>
    📅 2026年6月20日
</div>

</div>
</body>
</html>"""

with open(filepath, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Written {len(full_html)} bytes to {filepath}")
print(f"Card count: {len(cards)}")
