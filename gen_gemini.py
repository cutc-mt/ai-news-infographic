#!/usr/bin/env python3
"""Generate Gemini 3.6 Flash infographic HTML."""

import os

output_path = "/home/victo/work/ai-news-infographic/docs/20260723-Gemini-3.6-Flash-3.5-FlashLight-FlashCyber-新モデル解説.html"

cards = [
    # Row 1
    {
        "icon": "fa-bolt", "anim": "fa-beat-fade 2s",
        "title": "①新モデル3兄弟が同時登場: Gemini の刷新が始まった",
        "items": [
            ('fa-star', '<span class="keyword-tag">Gemini 3.6 Flash</span> — 世代更新のメインモデル'),
            ('fa-star', '<span class="keyword-tag">3.5 Flash Light</span> — 爆速特化の軽量モデル'),
            ('fa-star', '<span class="keyword-tag">Flash Cyber</span> — セキュリティ特化の専門モデル'),
            ('fa-circle-info', 'Google から <span class="highlight">3つの新モデルが同時に発表</span> された'),
            ('fa-users', '競合には GPT-5.6 Sol、Kimi K3、GLM-4.5 など強力モデルが多数'),
        ],
        "bubble": ("", '<i class="fa-solid fa-lightbulb fa-lg" style="color:var(--color-5)"></i> Gemini ファミリーが一気に3モデル追加！<br>それぞれ得意分野が違うのがポイントだね'),
    },
    {
        "icon": "fa-rocket", "anim": "fa-bounce 2s",
        "title": "②3.6 Flash: トークンを減らして性能を向上",
        "items": [
            ('fa-code', 'コーディング性能とツール性能が <span class="highlight">前世代から向上</span>'),
            ('fa-arrow-down', 'トークン数を削減しつつ精度は改善された'),
            ('fa-chart-line', '1年前の <span class="keyword-tag">3.1 Pro</span> を複数のベンチマークで上回る'),
            ('fa-brain', 'SWE-bench や OS World など新ベンチマークにも対応'),
            ('fa-gauge-high', '日常タスクの性能も着実に伸びている'),
        ],
        "bubble": ("variant-1", '<i class="fa-solid fa-circle-check fa-lg" style="color:var(--color-2)"></i> 前世代 3.1 Pro より賢くなった！<br>ただ GPT-4.5 や Claude を置き換えるほどではない'),
    },
    {
        "icon": "fa-gauge-high", "anim": "fa-flip 3s",
        "title": "③Flash Light: 毎秒350トークンの爆速モデル",
        "items": [
            ('fa-tachometer-alt', '<span class="highlight">TPS 350</span> を達成、比類なき出力速度'),
            ('fa-arrow-up', 'コンポーザー2.5（TPS 250）やノーノマックス（TPS 100）を上回る'),
            ('fa-terminal', 'ターミナルベンチでも前世代から大きくスコアアップ'),
            ('fa-list-check', 'SWE-bench Pro で <span class="keyword-tag">54%</span> を達成'),
            ('fa-laptop-code', 'コンピューターユースの性能も前世代から大幅に改善'),
        ],
        "bubble": ("right", '<i class="fa-solid fa-fire fa-lg" style="color:var(--color-5)"></i> 350 TPS は本当に速い！<br>実際のLP制作デモでそのスピードを体感'),
    },
    {
        "icon": "fa-shield-halved", "anim": "fa-beat-fade 2s",
        "title": "④Flash Cyber: 脆弱性発見に特化した専門モデル",
        "items": [
            ('fa-bug', 'セキュリティの穴を発見して修正する <span class="highlight">専門特化モデル</span>'),
            ('fa-lock', '悪用防止のため <span class="keyword-tag">政府と信頼できる相手限定</span> で提供'),
            ('fa-user-shield', '一般利用者はアクセスできない'),
            ('fa-magnifying-glass', 'サイバーセキュリティ分野に特化したポジショニング'),
            ('fa-building-columns', '政府機関・パートナー企業向けのエンタープライズ戦略'),
        ],
        "bubble": ("variant-2", '<i class="fa-solid fa-triangle-exclamation fa-lg" style="color:#D97706"></i> 一般ユーザーは使えないモデル。<br>でもセキュリティ特化という新しい方向性は注目！'),
    },
    # Row 2
    {
        "icon": "fa-dollar-sign", "anim": "fa-bounce 2s",
        "title": "⑤料金体系: Flash Light は名前の割に安くない",
        "items": [
            ('fa-money-bill-wave', '<span class="keyword-tag">3.6 Flash</span>: 入力 $1.5 / 出力 $7.5（MTok）'),
            ('fa-money-bill-wave', '<span class="keyword-tag">Flash Light</span>: 入力 $0.3 / 出力 $2.5（MTok）'),
            ('fa-scale-balanced', 'GLM-4.5（$2/$6）とほぼ同価格帯'),
            ('fa-arrow-down', 'トップクラスモデル（$10/$15）と比べれば <span class="highlight">約半額</span>'),
            ('fa-face-frown', 'MiniMAX M3（入力 $0.3 / 出力 $1.2）よりは高い'),
        ],
        "bubble": ("variant-2", '<i class="fa-solid fa-comment-dots fa-lg" style="color:#D97706"></i> "Light" なのに安くないのが不思議…<br>DeepSeek とかと比べるとかなり高い'),
    },
    {
        "icon": "fa-table", "anim": "fa-beat-fade 2s",
        "title": "⑥価格比較: 競合モデルの MTok 単価一覧",
        "items": [
            ('fa-money-bill', '<span class="keyword-tag">3.6 Flash</span>: 入力 $1.5 / 出力 $7.5 — 中堅帯'),
            ('fa-money-bill', '<span class="keyword-tag">Flash Light</span>: 入力 $0.3 / 出力 $2.5 — 中堅帯'),
            ('fa-money-bill', '<span class="keyword-tag">MiniMAX M3</span>: 入力 $0.3 / 出力 $1.2 — <span class="highlight">低価格でコスパ最強</span>'),
            ('fa-money-bill', '<span class="keyword-tag">DeepSeek</span>: 格安 — 激安帯'),
            ('fa-money-bill', '<span class="keyword-tag">GLM-4.5</span>: 入力 $2.0 / 出力 $6.0 — 中堅帯'),
        ],
        "bubble": ("top", '<i class="fa-solid fa-circle-info fa-lg" style="color:var(--color-2)"></i> Gemini 系は中堅価格帯。<br>コスパ最強は DeepSeek や MiniMAX'),
    },
    {
        "icon": "fa-chart-bar", "anim": "fa-beat-fade 2s",
        "title": "⑦ベンチマーク: 前世代を着実に超えるが…",
        "items": [
            ('fa-trophy', '3.1 Pro を <span class="highlight">複数のベンチマークで上回る</span>'),
            ('fa-list-check', 'SWE-bench: コーディング実務能力で改善'),
            ('fa-desktop', 'OS World: コンピュータ操作ベンチマークにも対応'),
            ('fa-pen-fancy', '文章品質は 3.5 Flash より明らかに良い印象'),
            ('fa-scale-balanced', '出力トークン <span class="keyword-tag">17% 減</span> でスマートな回答を実現'),
        ],
        "bubble": ("", '<i class="fa-solid fa-lightbulb fa-lg" style="color:var(--color-5)"></i> 1年前の Pro を超えたとはいえ、<br>今の激しい競争環境では「そこそこ」に留まる'),
    },
    {
        "icon": "fa-display", "anim": "fa-fade 2s",
        "title": "⑧Flash Light デモ: 爆速の実力を体感",
        "items": [
            ('fa-image', '画像から SVG で再現するタスクをテスト'),
            ('fa-palette', '「もっとリッチに」の追加指示にも <span class="highlight">高速で対応</span>'),
            ('fa-keyboard', 'キーボードの LP 制作で TPS 205〜280 を記録'),
            ('fa-gamepad', '3D ゲーム制作もある程度ちゃんと動く'),
            ('fa-fish', 'ただしアクアリウムなど複雑なものはまだ不十分'),
        ],
        "bubble": ("variant-1", '<i class="fa-solid fa-bolt fa-lg" style="color:var(--color-5)"></i> 昔の爆速モデルより全然使える！<br>速度と品質のバランスが取れてきた'),
    },
    # Row 3
    {
        "icon": "fa-laptop-code", "anim": "fa-beat-fade 2s",
        "title": "⑨LP制作比較: キーボードサイトの出来栄え",
        "items": [
            ('fa-code', 'キーボードメーカーの LP を各モデルで制作'),
            ('fa-eye', '3.5 Flash の方が色使いが良く見やすい印象'),
            ('fa-wand-magic-sparkles', '3.6 Flash はホバーアニメーションが少し不自然'),
            ('fa-star-half-stroke', '<span class="highlight">3.5 Flash の方がデザインセンスが上</span> という評価も'),
            ('fa-masks-theater', 'アイドル LP でも 3.5 Flash の方が豪華な仕上がり'),
        ],
        "bubble": ("variant-2", '<i class="fa-solid fa-face-surprise fa-lg" style="color:#D97706"></i> 新モデルの 3.6 より<br>旧モデルの 3.5 の方がいい場面も'),
    },
    {
        "icon": "fa-puzzle-piece", "anim": "fa-bounce 2s",
        "title": "⑩Figma プレビュー: グリッドレイアウトのテスト",
        "items": [
            ('fa-table-cells', 'プチ Figma のようなグリッドエディターで比較'),
            ('fa-circle-xmark', '3.6 Flash・3.5 Flash どちらも <span class="highlight">操作時に不具合</span>'),
            ('fa-arrows-up-down-left-right', 'ブロックエディターの挙動が不安定'),
            ('fa-circle-check', '一方で SVG 描画や鍵盤の図などはそこそこ綺麗'),
            ('fa-wrench', 'ツールの安定性は Gemini 系の課題として残る'),
        ],
        "bubble": ("right", '<i class="fa-solid fa-wrench fa-lg" style="color:var(--color-5)"></i> ツールの不安定さが気になる…<br>これが改善されればもっと評価が上がるはず'),
    },
    {
        "icon": "fa-gamepad", "anim": "fa-beat-fade 2s",
        "title": "⑪3D ゲーム制作: ピンボールとファイティングゲーム",
        "items": [
            ('fa-circle', 'ピンボール: <span class="highlight">ボールが転がり下に入るデモ</span> は秀逸'),
            ('fa-dice', '3D ファイティングゲームのビジュアルは高クオリティ'),
            ('fa-circle-xmark', 'マーブルランは途中で投げ出される不十分な結果'),
            ('fa-arrows-spin', 'ゴブリンスレイヤー風ゲームでフリーズする場面も'),
            ('fa-puzzle-piece', 'ゲーム制作は得意・不得意が安定しない'),
        ],
        "bubble": ("", '<i class="fa-solid fa-circle-info fa-lg" style="color:var(--color-2)"></i> ピンボールの物理デモはすごかった！<br>でもマーブルランは途中で挫折…'),
    },
    {
        "icon": "fa-arrow-right-arrow-left", "anim": "fa-flip 3s",
        "title": "⑫3.6 vs Grok vs Claude: スライド制作比較",
        "items": [
            ('fa-file-powerpoint', 'ハーネスエンジニアリングのスライド制作で比較'),
            ('fa-eye', 'Grok が <span class="highlight">最も読みやすいスライド</span> を生成'),
            ('fa-circle-exclamation', '3.6 Flash は <span class="keyword-tag">テキストがはみ出しまくり</span> で不満'),
            ('fa-scissors', '折り紙の 3D 解説も Gemini 系は分かりにくい'),
            ('fa-paint-roller', '画像からの再現タスクは Grok がクオリティ上位'),
        ],
        "bubble": ("variant-2", '<i class="fa-solid fa-face-sad-tear fa-lg" style="color:#D97706"></i> 3.6 Flash のスライドは<br>はみ出しすぎてちょっとむかつく…'),
    },
    # Row 4
    {
        "icon": "fa-image", "anim": "fa-beat-fade 2s",
        "title": "⑬画像認識・SVG 描画: 再現力を検証",
        "items": [
            ('fa-keyboard', 'キーボード画像の再現: ポイントは押さえている'),
            ('fa-paw', 'ライオン SVG: <span class="highlight">3.6 Flash は頑張るが Grok が上位</span>'),
            ('fa-mouse', '電気ネズミ SVG: 3.5 Flash がツール呼び出しをミス'),
            ('fa-person-walking', '棒人間アニメーション: Claude 3.5 Sonnet が最強'),
            ('fa-traffic-light', '交通ルール SVG: 信号の色切り替えは Gemini 系が健闘'),
        ],
        "bubble": ("variant-1", '<i class="fa-solid fa-circle-info fa-lg" style="color:var(--color-5)"></i> SVG 描画はポテンシャルを感じる。<br>でもツール呼び出しのミスが目立つ…'),
    },
    {
        "icon": "fa-pen-nib", "anim": "fa-bounce 2s",
        "title": "⑭文章生成: 3.6 Flash は 3.5 より読みやすい",
        "items": [
            ('fa-book-open', '2030年の AI 予想を書かせると <span class="highlight">興味深い洞察</span>'),
            ('fa-link', '「連続的常時オンライン世界モデル」の予測は鋭い'),
            ('fa-circle-xmark', 'しかし <span class="keyword-tag">文字の並びが不自然</span> な部分がある'),
            ('fa-brain', 'AGI 論では 3.6 Flash が文章の深さで 3.5 を上回る'),
            ('fa-face-meh', 'LLM スコア的にも 3.6 Flash が高い評価'),
        ],
        "bubble": ("", '<i class="fa-solid fa-lightbulb fa-lg" style="color:var(--color-2)"></i> 文章は全体的に 3.6 Flash がいいけど、<br>認知負荷が高い文字並びが気になる'),
    },
    {
        "icon": "fa-earth-americas", "anim": "fa-beat-fade 2s",
        "title": "⑮競争環境: 激しい AI モデル戦争の中で",
        "items": [
            ('fa-fire', '低価格帯: <span class="highlight">DeepSeek、MiniMAX M3</span> が激安'),
            ('fa-crown', 'ハイエンド: Claude Opus 4、GPT-5.6 Sol が強力'),
            ('fa-globe', 'Kimi K3、GLM-4.5、Grok など中堅層も層が厚い'),
            ('fa-robot', 'オープン系モデルも急速に進化中'),
            ('fa-chart-line', '昔なら Gemini Flash もそこそこ良かったが、今は厳しい'),
        ],
        "bubble": ("variant-2", '<i class="fa-solid fa-face-meh fa-lg" style="color:#D97706"></i> 正直ちょっと競争に勝ててない感。<br>全然悪くはないんだけど…'),
    },
    {
        "icon": "fa-scale-balanced", "anim": "fa-bounce 2s",
        "title": "⑯総合評価: 圧倒的進化とは言えない",
        "items": [
            ('fa-thumbs-up', 'めちゃくちゃ悪いわけではない、安定した改善'),
            ('fa-thumbs-down', '前世代から <span class="highlight">圧倒的な進化</span> とは言えない'),
            ('fa-circle-check', 'FaaS（Claude環境）や Grok と比べると見劣りする場面も'),
            ('fa-wrench', '出力の不安定さが課題 — ツール呼び出しミスが目立つ'),
            ('fa-face-meh', 'メインモデルとしては使わないという正直な評価'),
        ],
        "bubble": ("variant-1", '<i class="fa-solid fa-hand fa-lg" style="color:var(--color-5)"></i> ベストオブブレンドの1枠には<br>入れてもいいかもしれないレベル'),
    },
    # Row 5 (last 2)
    {
        "icon": "fa-wrench", "anim": "fa-beat-fade 2s",
        "title": "⑰改善してほしい点: 出力の安定性が最大の課題",
        "items": [
            ('fa-triangle-exclamation', 'ツール呼び出しのミスが頻発する'),
            ('fa-arrows-spin', '出力の安定性にばらつきがある — 成功と失敗の差が激しい'),
            ('fa-clipboard-check', 'スライド制作ではテキストがはみ出す等のレイアウト崩れ'),
            ('fa-palette', 'デザインセンスで 3.5 Flash に負ける場面がある'),
            ('fa-arrow-up', 'カーソル（Claude環境）に対応した FaaS 化が期待されている'),
        ],
        "bubble": ("", '<i class="fa-solid fa-circle-info fa-lg" style="color:var(--color-2)"></i> 最大の課題は「安定性」。<br>これさえ直れば評価はかなり変わる'),
    },
    {
        "icon": "fa-thumbs-up", "anim": "fa-bounce 2s",
        "title": "⑱まとめ: 使い道を考えるなら Flash Light が面白い",
        "items": [
            ('fa-star', '3.6 Flash: 安定した改善だが特別感は薄い'),
            ('fa-bolt', 'Flash Light: <span class="highlight">爆速かつそこそこ賢い</span> ので使い道がありそう'),
            ('fa-shield-halved', 'Flash Cyber: セキュリティ特化で政府向けの戦略モデル'),
            ('fa-gem', 'FaaS 化やセレブラス環境対応が今後のカギ'),
            ('fa-circle-info', 'ベストオブブレンドの選択肢の1つとしてはあり'),
        ],
        "bubble": ("variant-2", '<i class="fa-solid fa-lightbulb fa-lg" style="color:#D97706"></i> 個人的には Flash Light が<br>一番面白いモデルじゃないかな！'),
    },
]

def make_card_html(c, idx):
    icon_color = "var(--color-1)" if idx % 2 == 0 else "var(--color-5)"
    if idx in [4, 14]:
        icon_color = "var(--color-2)"
    items_html = "\n".join(
        f'<li><i class="fa-solid {icon}" aria-hidden="true"></i><span>{text}</span></li>'
        for icon, text in c["items"]
    )
    bubble_cls, bubble_content = c["bubble"]
    bubble_html = f'<div class="speech-bubble {bubble_cls}"><span class="handwritten">{bubble_content}</span></div>'
    return f"""<div class="card fade-in-scale">
    <div class="mega-icon-container">
        <i class="fas {c['icon']} fa-5x" style="color:{icon_color};animation:{c['anim']}" aria-hidden="true"></i>
        <h2>{c['title']}</h2>
    </div>
    <div class="card-content">
        <ul class="keyword-list">
            {items_html}
        </ul>
    </div>
    {bubble_html}
</div>"""

css = """@import url('https://fonts.googleapis.com/css2?family=Kaisei+Decol&family=Yomogi&family=Zen+Kurenaido&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
        :root { --color-1:#0EA5E9; --color-2:#0284C7; --color-3:#BAE6FD; --color-4:#0C4A6E; --color-5:#06B6D4; }
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background-color:#F0FDFA; font-family:'Kaisei Decol',serif; color:#333; line-height:1.6; }
        .container { max-width:2000px; margin:0 auto; padding:20px; }
        .header { text-align:center; padding:50px 20px; margin-bottom:30px; background:linear-gradient(135deg,#0C4A6E,#0EA5E9,#06B6D4); border-radius:30px; color:white; position:relative; overflow:hidden; }
        .header::before { content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%; background:radial-gradient(circle,rgba(255,255,255,0.08) 0%,transparent 60%); animation:headerGlow 8s ease-in-out infinite; }
        @keyframes headerGlow { 0%,100%{transform:translate(0,0)} 50%{transform:translate(20px,20px)} }
        .header-icon { font-size:5em; margin-bottom:10px; animation:fa-bounce 2s infinite; }
        .header h1 { font-size:2.4em; font-weight:900; margin-bottom:10px; text-shadow:2px 2px 4px rgba(0,0,0,0.3); position:relative; z-index:1; }
        .header .subtitle { font-size:1.3em; opacity:0.9; font-family:'Yomogi',cursive; position:relative; z-index:1; }
        .header .date { font-size:0.9em; opacity:0.7; margin-top:10px; position:relative; z-index:1; }
        .section-layout { display:flex; flex-wrap:wrap; gap:20px; justify-content:center; margin-bottom:20px; }
        .card { flex:1; min-width:280px; max-width:450px; background-color:white; border-radius:20px; padding:20px; box-shadow:5px 5px 15px rgba(0,0,0,0.1); position:relative; overflow:hidden; transition:transform 0.3s ease,box-shadow 0.3s ease; }
        .card:hover { transform:translateY(-5px); box-shadow:8px 8px 25px rgba(14,165,233,0.2); }
        .card::before { content:''; position:absolute; top:0; left:0; width:100%; height:5px; background:linear-gradient(90deg,var(--color-1),var(--color-5)); }
        .mega-icon-container { text-align:center; margin:15px 0; }
        .mega-icon-container h2 { font-size:1.25em; color:var(--color-4); margin-top:10px; line-height:1.4; }
        .card-content { padding:0 10px 15px; }
        .keyword-list { margin:15px 0; padding:0; list-style-type:none; }
        .keyword-list li { margin-bottom:10px; display:flex; align-items:flex-start; font-size:15px; line-height:1.6; }
        .keyword-list li i { margin-right:8px; color:var(--color-2); min-width:16px; margin-top:4px; }
        .keyword-tag { background-color:var(--color-3); color:var(--color-4); padding:3px 8px; border-radius:5px; margin-right:5px; display:inline-block; font-weight:bold; font-size:14px; }
        .speech-bubble { position:relative; background:#fff; border:3px solid var(--color-1); border-radius:20px; padding:12px 15px; margin:15px 5px; font-family:'Yomogi',cursive; box-shadow:3px 3px 10px rgba(0,0,0,0.1); transform:rotate(-1deg); }
        .speech-bubble::after { content:''; position:absolute; bottom:-13px; left:20px; border-width:12px 8px 0; border-style:solid; border-color:var(--color-1) transparent; display:block; width:0; }
        .speech-bubble.right::after { left:auto; right:20px; transform:rotate(15deg); }
        .speech-bubble.top::after { bottom:auto; top:-13px; border-width:0 8px 12px; transform:rotate(-5deg); }
        .speech-bubble.variant-1 { background:#F0FDFA; border-color:var(--color-5); transform:rotate(1deg); }
        .speech-bubble.variant-1::after { border-color:var(--color-5) transparent; }
        .speech-bubble.variant-2 { background:#FFF9E3; border-color:#D97706; transform:rotate(-2deg); }
        .speech-bubble.variant-2::after { border-color:#D97706 transparent; }
        .handwritten { font-family:'Yomogi',cursive; font-size:15px; line-height:1.5; color:#333; }
        .highlight { background:linear-gradient(transparent 60%,rgba(6,182,212,0.3) 60%); font-weight:bold; }
        .fade-in-scale { opacity:0; transform:scale(0.95); animation:fadeInScale 0.6s ease forwards; }
        @keyframes fadeInScale { to { opacity:1; transform:scale(1); } }
        .card:nth-child(1){animation-delay:0.1s} .card:nth-child(2){animation-delay:0.2s} .card:nth-child(3){animation-delay:0.3s} .card:nth-child(4){animation-delay:0.4s}
        footer { text-align:center; padding:30px 20px; margin-top:30px; font-size:14px; color:#777; border-top:2px dashed #ddd; }
        footer a { color:var(--color-2); text-decoration:none; }
        footer a:hover { text-decoration:underline; }
        @media(max-width:1600px){.card{min-width:280px}} @media(max-width:1200px){.card{min-width:320px}} @media(max-width:900px){.card{min-width:380px}} @media(max-width:768px){.section-layout{flex-direction:column} .card{width:100%;min-width:auto}}"""

# Build rows of 4 cards each
rows = []
for i in range(0, len(cards), 4):
    row_cards = cards[i:i+4]
    row_html = "\n".join(make_card_html(c, i+j) for j, c in enumerate(row_cards))
    rows.append(f'<div class="section-layout">\n{row_html}\n</div>')

body = "\n".join(rows)

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gemini 3.6 Flash / 3.5 Flash Light / Flash Cyber 新モデル解説</title>
    <style>{css}</style>
</head>
<body>
<div class="container">
<div class="header">
    <div class="header-icon"><i class="fas fa-gem" aria-hidden="true"></i></div>
    <h1>Gemini 新モデル三冠発表</h1>
    <div class="subtitle">3.6 Flash / 3.5 Flash Light / Flash Cyber を徹底解説</div>
    <div class="date"><i class="fas fa-calendar-alt"></i> 2026年7月23日</div>
</div>
{body}
<footer>
    🎬 動画: <a href="https://www.youtube.com/watch?v=jpCfUB0W6Gg" target="_blank" style="color:var(--color-2)">マオ</a> | 📅 2026年7月23日<br>
    <span style="font-size:12px; color:#aaa">Generated by AI News Infographic Generator</span>
</footer>
</div>
</body>
</html>"""

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Written {len(cards)} cards to {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")

# Verify card count
with open(output_path, 'r', encoding='utf-8') as f:
    content = f.read()
card_count = content.count('class="card"')
print(f"Card count (class='card'): {card_count}")
