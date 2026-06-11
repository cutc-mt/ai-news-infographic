#!/usr/bin/env python3
"""Generate the SpaceX IPO infographic HTML."""
import os

CARD_TEMPLATE = """
<div class="card fi">
    <div class="icon-box"><i class="{icon} fa-5x" style="color:var(--c{color});{anim}"></i><h2>{num} {title}</h2></div>
    <div class="cc"><ul class="kl">{items}</ul>{bubble}</div>
</div>"""

ITEM_TEMPLATE = '<li><i class="{icon}"></i><span>{text}</span></li>'

BUBBLE_TEMPLATE = '<div class="bub{variant}"><span class="hw"><i class="{icon}" style="color:var(--c{color})"></i> {text}</span></div>'

BUBBLE_TOP = '<div class="bub{variant} t"><span class="hw"><i class="{icon}" style="color:var(--c{color})"></i> {text}</span></div>'
BUBBLE_RIGHT = '<div class="bub{variant} r"><span class="hw"><i class="{icon}" style="color:var(--c{color})"></i> {text}</span></div>'

cards = [
    {
        "icon": "fa-solid fa-chart-line", "color": 2, "anim": "animation:fa-bounce 2s infinite",
        "num": "①", "title": "史上最大級の IPO: SpaceX が6月12日に上場",
        "items": [
            ("fa-solid fa-dollar-sign", "1株あたり約<span class=\"hl\">160ドル（約22,000円）</span>。時価総額は<span class=\"tag\">1.75兆ドル（約300兆円）</span>に達する見込み"),
            ("fa-solid fa-trophy", "世界最高の時価総額の Apple（500〜600兆円）の<span class=\"hl\">半分近く</span>。いきなり世界ベスト5クラスに躍り出る"),
            ("fa-solid fa-users", "個人投資家向けに<span class=\"tag\">30%</span>を割り当て（通常は20%）。需要の<span class=\"hl\">4倍超</span>となっている"),
            ("fa-solid fa-triangle-exclamation", "個人投資家の割り当てが多いのは、熱狂による株価上昇を狙っているという見方も存在"),
        ],
        "bubble": {"variant": " v1", "icon": "fa-solid fa-lightbulb fa-lg", "color": 2,
                   "text": "株に興味がない素人が「申し込んだ」と投稿するレベルの熱狂。<span class=\"tag\">バブルの兆候</span>か、それとも上昇の勢いか。"}
    },
    {
        "icon": "fa-solid fa-calculator", "color": 1, "anim": "animation:fa-beat-fade 2s infinite",
        "num": "②", "title": "売上100倍の謎: イーロン・マスクプレミアム",
        "items": [
            ("fa-solid fa-coins", "年間売上はたった<span class=\"tag\">186.7億ドル</span>。時価総額が売上の<span class=\"hl\">約100倍</span>という異常なバリュエーション"),
            ("fa-solid fa-arrow-trend-down", "xAI を買収したことで<span class=\"tag\">約4兆円の累積赤字</span>を抱える会社になっている"),
            ("fa-solid fa-star", "通常の株価形成では説明がつかず、市場は<span class=\"hl\">「イーロン・マスクプレミアム」</span>と呼んでいる"),
            ("fa-solid fa-tags", "評価の内訳：<span class=\"tag\">ロケット</span>＋<span class=\"tag\">Starlink</span>＋<span class=\"tag\">宇宙AIコンピュート</span>＋<span class=\"tag\">マスクプレミアム</span>"),
        ],
        "bubble": {"variant": " v2", "icon": "fa-solid fa-circle-exclamation fa-lg", "color": 5,
                   "text": "売上100倍は<span class=\"tag\">異常すぎる</span>。AI 系のインフレ期待が根底にあるのかもしれません。"}
    },
    {
        "icon": "fa-solid fa-fire", "color": 5, "anim": "animation:fa-bounce 1.5s infinite",
        "num": "③", "title": "バブルか上昇続行か: 機関投資家の見方",
        "items": [
            ("fa-solid fa-shoe-prints", "「靴磨きの少年」が株式を語り始めたらバブル崩壊の兆候——<span class=\"hl\">そのレベルに近づいている</span>"),
            ("fa-solid fa-face-smile", "楽観派：素人が熱狂している＝注目度が高い＝<span class=\"hl\">まだまだ上がる</span>というロジック"),
            ("fa-solid fa-building-columns", "アメリカの機関投資家の多数派は<span class=\"tag\">上昇継続</span>を予想。大衆の熱狂に乗る方が得という判断"),
            ("fa-solid fa-face-frown", "悲観派：素直にバブル崩壊の直前だと見る考え方も根強く存在している"),
        ],
        "bubble": {"variant": "", "pos": "top", "icon": "fa-solid fa-circle-info fa-lg", "color": 1,
                   "text": "Bioshok さんも「最初はバブるだろう」と言いつつ少し申し込んだそう。<span class=\"tag\">お祭り感覚</span>での参加が多い。"}
    },
    {
        "icon": "fa-solid fa-satellite", "color": 2, "anim": "animation:fa-flip 3s infinite",
        "num": "④", "title": "宇宙データセンター構想: 次世代ハイパースケーラー",
        "items": [
            ("fa-solid fa-sun", "人工衛星にソーラーパネルを取り付けデータセンターを構築。<span class=\"hl\">太陽光で24時間発電可能</span>"),
            ("fa-solid fa-temperature-low", "宇宙空間に熱を放出すれば冷却OK。地球上の冷却問題が一切ない"),
            ("fa-solid fa-hourglass-half", "5年以内のビジネス化は困難だが、<span class=\"tag\">2030年代</span>には地上データセンターと競争力を持つ可能性"),
            ("fa-solid fa-server", "AGI 登場で計算資源需要が爆発すれば、SpaceX は<span class=\"hl\">宇宙時代のハイパースケーラー</span>になるかも"),
        ],
        "bubble": {"variant": " v1", "pos": "right", "icon": "fa-solid fa-rocket fa-lg", "color": 2,
                   "text": "CoreWeave のようなハイパースケーラーが宇宙で<span class=\"tag\">SpaceX になる</span>という構図。"}
    },
    {
        "icon": "fa-solid fa-globe", "color": 1, "anim": "animation:fa-beat-fade 2s infinite",
        "num": "⑤", "title": "宇宙経済圏は実在するか: スケールで話は別次元",
        "items": [
            ("fa-solid fa-check-circle", "Bioshok さん：<span class=\"hl\">「実在する」</span>。ただし規模によって段階が全く違う"),
            ("fa-solid fa-layer-group", "<span class=\"tag\">短期的</span>：Starlink や宇宙データセンターなど、現実的なビジネス"),
            ("fa-solid fa-expand", "<span class=\"tag\">長期的</span>：地球経済の何百倍という宇宙文明レベル。200年以上先の話"),
            ("fa-solid fa-clock", "普通の投資家は<span class=\"hl\">5〜10年で元を取りたい</span>。200年先の宇宙経済圏を考えて買う人はほとんどいない"),
        ],
        "bubble": {"variant": " v2", "pos": "top", "icon": "fa-solid fa-exclamation fa-lg", "color": 5,
                   "text": "Starlink の話と<span class=\"tag\">何百倍の宇宙経済圏</span>の話は全く別次元の議論です！"}
    },
    {
        "icon": "fa-solid fa-explosion", "color": 5, "anim": "animation:fa-shake 2s infinite",
        "num": "⑥", "title": "産業爆発: AGI が前提を変える超指数関数的成長",
        "items": [
            ("fa-solid fa-atom", "<span class=\"tag\">産業爆発</span>：数百年先の経済規模が、AGI 後<span class=\"hl\">10〜20年で実現</span>するという概念"),
            ("fa-solid fa-industry", "工場が工場を作るフィードバックループが回れば、<span class=\"hl\">地球経済はゴミのようなレベル</span>に縮小"),
            ("fa-solid fa-mars", "火星に植民地、ラグランジュ点に<span class=\"tag\">マクドナルド・シリンダー</span>級のスペースコロニーが何千個も"),
            ("fa-solid fa-bolt", "カルダシェフスケール文明（タイプ2）への急速な移行が現実的な議論として成立しつつある"),
        ],
        "bubble": {"variant": " v1", "icon": "fa-solid fa-wand-magic-sparkles fa-lg", "color": 2,
                   "text": "マスクがよく言っている「タイプ2文明」の話は<span class=\"tag\">夢物語ではない</span>という見方。"}
    },
    {
        "icon": "fa-solid fa-arrow-trend-up", "color": 2, "anim": "animation:fa-bounce 2s infinite",
        "num": "⑦", "title": "Anthropic が証明した指数関数的成長の現実",
        "items": [
            ("fa-solid fa-chart-line", "Anthropic の売上：<span class=\"tag\">2023年</span>ゼロ → <span class=\"tag\">2024年</span>数億円 → <span class=\"tag\">2025年</span>5000億円 → <span class=\"tag\">2026年</span>4兆円の予測"),
            ("fa-solid fa-brain", "Mythos リリース時の売上予測グラフが<span class=\"hl\">指数関数の曲線</span>を描いていた"),
            ("fa-solid fa-user-tie", "ダリオ・アモが売上ゼロの時点で「数年後に1兆円」と予測し、それが現実になりつつある"),
            ("fa-solid fa-link", "経済史上初めて<span class=\"tag\">指数関数的成長</span>が実証された。これがAGI後の宇宙経済圏のロジックに繋がる"),
        ],
        "bubble": {"variant": "", "icon": "fa-solid fa-star fa-lg", "color": 1,
                   "text": "この成長が証明されたタイミングでSpaceX も「自分も実現する」を主張するストーリー。"}
    },
    {
        "icon": "fa-solid fa-bolt", "color": 2, "anim": "animation:fa-spin 3s linear infinite",
        "num": "⑧", "title": "エネルギーを制する者が宇宙を制す",
        "items": [
            ("fa-solid fa-sun", "太陽系で最大のエネルギー源は<span class=\"hl\">太陽</span>。地球の核の何万倍ものエネルギーを持つ天然の核融合炉"),
            ("fa-solid fa-trophy", "Bioshok さん：<span class=\"hl\">「エネルギーを握ったものが全てを握る」</span>。宇宙の覇者になるための鍵はエネルギー"),
            ("fa-solid fa-satellite-dish", "SpaceX は太陽エネルギーの活用において1〜2歩リード。24時間発電できる宇宙空間の有利さ"),
            ("fa-solid fa-flag", "ただし宇宙の覇者になるには<span class=\"tag\">AGI が必要</span>。SpaceX 単体では勝てないという条件付き"),
        ],
        "bubble": {"variant": " v1", "pos": "right", "icon": "fa-solid fa-crown fa-lg", "color": 2,
                   "text": "太陽エネルギー＋AGI＝宇宙文明の覇者。SpaceX はその条件の一部。"}
    },
    {
        "icon": "fa-solid fa-masks-theater", "color": 5, "anim": "animation:fa-flip 3s infinite",
        "num": "⑨", "title": "Fast Takeoff vs Slow Takeoff: SpaceXの命運",
        "items": [
            ("fa-solid fa-gauge-high", "<span class=\"tag\">Fast Takeoff</span>：AGI が急速に自己改善し、3年で宇宙開発の知見を追い抜く世界"),
            ("fa-solid fa-gauge-simple", "<span class=\"tag\">Slow Takeoff</span>：AGI の進化が10〜20年のスパン。SpaceX の20年のノウハウが生きる"),
            ("fa-solid fa-triangle-exclamation", "Fast Takeoff では<span class=\"hl\">超知能が第1原理計算で全て解決</span>。20年の試行錯誤が無意味化する恐れ"),
            ("fa-solid fa-clock", "Slow ならノウハウが<span class=\"hl\">10年以上有効</span>。Fast なら3年でアドバンテージ消失"),
        ],
        "bubble": {"variant": " v2", "icon": "fa-solid fa-circle-exclamation fa-lg", "color": 5,
                   "text": "Fast Takeoff を信じる人は<span class=\"tag\">SpaceX の株を買わない方がいい</span>。Slow なら微妙に買ってもOK。"}
    },
    {
        "icon": "fa-solid fa-user-astronaut", "color": 1, "anim": "animation:fa-beat-fade 2s infinite",
        "num": "⑩", "title": "Fast Takeoff で覇権を失うシナリオ",
        "items": [
            ("fa-solid fa-brain", "超知能が人間の20年間の打ち上げノウハウを<span class=\"hl\">3日で再現</span>する可能性。蓄積が一瞬で無意味に"),
            ("fa-solid fa-arrow-down", "SpaceX が宇宙覇者である可能性は<span class=\"hl\">徐々に下がっていく</span>。シェアがゼロにはならないが差は縮まる"),
            ("fa-solid fa-ranking-star", "3番手4番手の<span class=\"tag\">大手サプライヤー</span>に落ちる可能性。Anthropic、OpenAI、Google も宇宙覇者に"),
            ("fa-solid fa-microchip", "AGI企業が<span class=\"hl\">計算資源の調達も自律的に解決</span>すれば、外部ローンチの優位性は薄れる"),
        ],
        "bubble": {"variant": "", "pos": "top", "icon": "fa-solid fa-lightbulb fa-lg", "color": 1,
                   "text": "xAI が遅れている以上、AI 面での<span class=\"tag\">出遅れ</span>が致命的な弱点に。"}
    },
    {
        "icon": "fa-solid fa-chess-king", "color": 2, "anim": "animation:fa-bounce 2s infinite",
        "num": "⑪", "title": "マスクの戦略敗北: xAI 合体の失敗と Compute 貸与",
        "items": [
            ("fa-solid fa-xmark", "当初の構想：<span class=\"tag\">宇宙のパイオニア SpaceX</span>＋<span class=\"tag\">AI のトップ xAI</span>が合体して宇宙とAIを制覇"),
            ("fa-solid fa-arrow-right", "現実：SpaceX が<span class=\"hl\">Google に計算リソースを貸すインフラ</span>になっている。つまり余っている"),
            ("fa-solid fa-users-slash", "xAI から創設者が何人か抜け、人材流出も発生。<span class=\"tag\">AI 競争で半分負けを認めている</span>状態"),
            ("fa-solid fa-handshake", "Bioshok さん：Fast Takeoff シナリオなら<span class=\"hl\">負けを認めざるを得ない</span>。Slow なら巻き返せるかも"),
        ],
        "bubble": {"variant": " v2", "pos": "right", "icon": "fa-solid fa-exclamation fa-lg", "color": 5,
                   "text": "宇宙＋AI の夢の構想が<span class=\"tag\">霧散しつつある</span>。しかしマスクは事業家として交渉の余地も残している。"}
    },
    {
        "icon": "fa-solid fa-handshake-angle", "color": 1, "anim": "animation:fa-beat-fade 2s infinite",
        "num": "⑫", "title": "Cursor 買収権: データでAI競争に差をつける狙い",
        "items": [
            ("fa-solid fa-coins", "SpaceX が<span class=\"tag\">約1兆円</span>を支払い、Cursor（旧 Anysphere）の企業買収権を取得。4〜5兆円で完全買収可能"),
            ("fa-solid fa-database", "Bioshok さん：Cursor を経由して何百万人が開発。<span class=\"hl\">良質なコーディングデータ</span>が大量に蓄積"),
            ("fa-solid fa-users-gear", "AI 競争で重要なのは<span class=\"tag\">データ</span>＋<span class=\"tag\">人材</span>＋<span class=\"tag\">学習環境</span>を構築できる人材"),
            ("fa-solid fa-robot", "AI研究はソフトウェア開発に似ており、スーパーコーダーの開発が次のAI研究の自動化に繋がる"),
        ],
        "bubble": {"variant": " v1", "icon": "fa-solid fa-code fa-lg", "color": 2,
                   "text": "Claude Code や Codex の後継に<span class=\"tag\">なる可能性</span>。コーディング環境のデータはAI開発の競争力そのもの。"}
    },
    {
        "icon": "fa-solid fa-comments", "color": 2, "anim": "animation:fa-bounce 2s infinite",
        "num": "⑬", "title": "マスクビジョンの空転: 株価が下がらない理由",
        "items": [
            ("fa-solid fa-face-meh", "xAI が性能面で勝てていない。宇宙＋AI の両面リーディングの物語が<span class=\"hl\">消化しつつある</span>"),
            ("fa-solid fa-crown", "それでも株価が高いのは<span class=\"hl\">「イーロン・マスクプレミアム」</span>の存在。Bioshok さんも大いに存在すると認識"),
            ("fa-solid fa-satellite-dish", "多くの投資家は Starlink や宇宙データセンターに<span class=\"tag\">ワクワク感</span>を抱いて買いに来ている"),
            ("fa-solid fa-users", "期待に乗って参加する人が集まり、「お祭りに参加しよう」というムードも拡大中"),
        ],
        "bubble": {"variant": "", "icon": "fa-solid fa-circle-info fa-lg", "color": 1,
                   "text": "産業爆発を知っている人は少ない。株価を支えているのは<span class=\"tag\">Starlink への期待</span>が大半。"}
    },
    {
        "icon": "fa-solid fa-handshake", "color": 1, "anim": "animation:fa-flip 3s infinite",
        "num": "⑭", "title": "協力シナリオ: SpaceX × Anthropic × Google",
        "items": [
            ("fa-solid fa-puzzle-piece", "Fast Takeoff でも SpaceX が<span class=\"hl\">完全に終わるわけではない</span>。マスクが Anthropic や Google と協力する可能性も"),
            ("fa-solid fa-file-contract", "事業家としてのマスクが<span class=\"tag\">良い形で交渉</span>をすれば、株価が大きく上昇するシナリオもあり得る"),
            ("fa-solid fa-arrows-rotate", "Bioshok さん：Anthropic や OpenAI、Google もいずれ<span class=\"hl\">宇宙に行く</span>。彼らの株を買うことは宇宙文明のインフラを買うのと同じ"),
            ("fa-solid fa-scale-balanced", "ただし短期的に見れば<span class=\"tag\">Anthropic や Google を買っておいた方が確実</span>というのが Bioshok さんの見方"),
        ],
        "bubble": {"variant": " v1", "pos": "right", "icon": "fa-solid fa-forward fa-lg", "color": 2,
                   "text": "SpaceX の株価は短期で<span class=\"tag\">爆発的に上がる</span>可能性もある。協力シナリオ次第。"}
    },
    {
        "icon": "fa-solid fa-share-nodes", "color": 5, "anim": "animation:fa-beat-fade 2s infinite",
        "num": "⑮", "title": "Anthropic vs SpaceX: 投資順序が鍵",
        "items": [
            ("fa-solid fa-earth-americas", "AI企業は世界GDP（100兆ドル）の<span class=\"hl\">0.1%の1000億ドル</span>しかまだ稼げていない。まずは地球経済を制覇する段階"),
            ("fa-solid fa-arrow-up-right-dots", "地球経済を2倍にするだけで<span class=\"tag\">十分な投資余地</span>がある。まだ宇宙経済圏の話をする段階ではない"),
            ("fa-solid fa-chart-pie", "理想的なポートフォリオ：<span class=\"hl\">Anthropic 30%＋OpenAI 30%＋Google 30%＋SpaceX 5〜10%</span>"),
            ("fa-solid fa-arrow-right", "Anthropic や OpenAI が<span class=\"tag\">100兆ドル企業</span>になってから、改めて SpaceX のシェアを増やせばいい"),
        ],
        "bubble": {"variant": "", "pos": "top", "icon": "fa-solid fa-lightbulb fa-lg", "color": 1,
                   "text": "投資には<span class=\"tag\">順序</span>が大事。「今上がる株」と「将来上がる株」は別です。"}
    },
    {
        "icon": "fa-solid fa-robot", "color": 2, "anim": "animation:fa-bounce 2s infinite",
        "num": "⑯", "title": "Claude Fable の実力: AGI まだ遠いが衝撃的",
        "items": [
            ("fa-solid fa-code", "かさん：Fable は<span class=\"hl\">明らかに Claude 4.7や4.8より正確</span>。コーデックスよりも全然上という評価"),
            ("fa-solid fa-clock-rotate-left", "指示を与えれば<span class=\"hl\">何日も勝手に動き続ける</span>。30分→1時間→3時間と自律的に稼働"),
            ("fa-solid fa-circle-xmark", "Bioshok さん：Fable は Mythos とほぼ同じ能力だが、<span class=\"hl\">「まだ全然 AGI ではない」</span>"),
            ("fa-solid fa-brain", "厳密なAGI の定義：アインシュタインレベルの科学的発見をなし、<span class=\"tag\">自己フィードバックループ</span>で人間が介入不要"),
        ],
        "bubble": {"variant": " v2", "icon": "fa-solid fa-circle-exclamation fa-lg", "color": 5,
                   "text": "Fable がAGI ではないと言うのは<span class=\"tag\">AGI があまりにもすごすぎるから</span>。Fable 自体は相当すごい。"}
    },
    {
        "icon": "fa-solid fa-flask", "color": 1, "anim": "animation:fa-beat-fade 2s infinite",
        "num": "⑰", "title": "Bioshok さんの AGI 定義: カルダシェフスケール以上",
        "items": [
            ("fa-solid fa-rocket", "AGI とは<span class=\"hl\">地球上の宇宙科学を全て発展させ、宇宙文明への移行</span>を担えるレベルの能力"),
            ("fa-solid fa-atom", "単にコーディングできるだけでは不十分。<span class=\"tag\">新しい科学的発見</span>や<span class=\"tag\">パラダイムの発見</span>が必要"),
            ("fa-solid fa-infinity", "無限に動ける必要がある。この瞬間に銀河系を制覇できない＝<span class=\"hl\">AGI ではない</span>"),
            ("fa-solid fa-bolt-lightning", "カルダシェフスケールのタイプ1〜2文明への移行まで担えるなら<span class=\"tag\">初めて AGI と呼べる</span>"),
        ],
        "bubble": {"variant": " v1", "icon": "fa-solid fa-star fa-lg", "color": 2,
                   "text": "Bioshok さんのAGI 定義は<span class=\"tag\">一般的な認識より遥かに高い</span>。だからFable がすごくても「まだAGIではない」と言う。"}
    },
    {
        "icon": "fa-solid fa-hat-wizard", "color": 2, "anim": "animation:fa-bounce 2s infinite",
        "num": "⑱", "title": "まとめ: 超知能の観点から見た SpaceX 上場",
        "items": [
            ("fa-solid fa-bullseye", "SpaceX の上場は<span class=\"hl\">宇宙ビジネスの本格参入</span>の歴史的イベントだが、バリュエーションは割高感あり"),
            ("fa-solid fa-yin-yang", "Fast Takeoff では SpaceX の20年のノウハウが<span class=\"hl\">3日で無意味化</span>する可能性。AI競争の出遅れが致命傷"),
            ("fa-solid fa-chart-pie", "短期的に確実なのは<span class=\"tag\">Anthropic や OpenAI</span>。長期なら SpaceX も宇宙覇者になる可能性"),
            ("fa-solid fa-flag-checkered", "株式投資は自己判断で。この番組は<span class=\"tag\">投資助言ではありません</span>"),
        ],
        "bubble": {"variant": " v2", "pos": "right", "icon": "fa-solid fa-exclamation fa-lg", "color": 5,
                   "text": "宇宙×AI×超知能の交差点。<br>歴史的IPOだが、冷静な判断が求められています。"}
    },
]

def render_card(c):
    items_html = "\n".join(ITEM_TEMPLATE.format(icon=i, text=t) for i, t in c["items"])
    b = c["bubble"]
    pos = b.get("pos", "")
    if pos == "top":
        bub_html = BUBBLE_TOP.format(variant=b["variant"], icon=b["icon"], color=b["color"], text=b["text"])
    elif pos == "right":
        bub_html = BUBBLE_RIGHT.format(variant=b["variant"], icon=b["icon"], color=b["color"], text=b["text"])
    else:
        bub_html = BUBBLE_TEMPLATE.format(variant=b["variant"], icon=b["icon"], color=b["color"], text=b["text"])
    return CARD_TEMPLATE.format(icon=c["icon"], color=c["color"], anim=c["anim"], num=c["num"], title=c["title"], items=items_html, bubble=bub_html)

# Split cards into rows of 4
rows = []
for i in range(0, len(cards), 4):
    rows.append("\n".join(render_card(c) for c in cards[i:i+4]))

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Kaisei+Decol&family=Yomogi&family=Zen+Kurenaido&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
:root{--c1:#0B1D3A;--c2:#D4A843;--c3:#E8E0D0;--c4:#1A0A00;--c5:#C0392B}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#F5F0EB;font-family:'Kaisei Decol',serif;color:#333;line-height:1.6}
.container{max-width:2000px;margin:0 auto;padding:20px}
.header{text-align:center;padding:40px 20px;margin-bottom:30px;background:linear-gradient(135deg,var(--c1),#1B3A5C,var(--c2));border-radius:30px;color:#fff;position:relative;overflow:hidden}
.header::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(circle at 30% 50%,rgba(255,255,255,.08) 0%,transparent 60%);animation:glow 8s ease-in-out infinite}
@keyframes glow{0%,100%{opacity:.5}50%{opacity:1}}
.header-icon{font-size:5em;margin-bottom:10px;animation:fa-bounce 2s infinite;position:relative;z-index:1}
.header h1{font-size:2.4em;font-weight:900;margin-bottom:10px;text-shadow:2px 2px 4px rgba(0,0,0,.3);position:relative;z-index:1}
.header .sub{font-size:1.3em;opacity:.9;font-family:'Yomogi',cursive;position:relative;z-index:1}
.header .date{font-size:.9em;opacity:.7;margin-top:10px;position:relative;z-index:1}
.row{display:flex;flex-wrap:wrap;gap:20px;justify-content:center;margin-bottom:20px}
.card{flex:1;min-width:280px;max-width:450px;background:#fff;border-radius:20px;padding:20px;box-shadow:5px 5px 15px rgba(0,0,0,.1);position:relative;overflow:hidden;transition:transform .3s,box-shadow .3s}
.card:hover{transform:translateY(-5px);box-shadow:8px 8px 25px rgba(0,0,0,.15)}
.card::before{content:'';position:absolute;top:0;left:0;width:100%;height:5px;background:linear-gradient(90deg,var(--c1),var(--c2))}
.icon-box{text-align:center;margin:15px 0}
.icon-box h2{font-size:1.2em;color:var(--c4);margin-top:10px}
.cc{padding:0 10px 15px}
ul.kl{margin:15px 0;padding:0;list-style:none}
ul.kl li{margin-bottom:10px;display:flex;align-items:flex-start;font-size:15px;line-height:1.6}
ul.kl li i{margin-right:8px;color:var(--c2);min-width:16px;margin-top:4px}
.tag{background:var(--c3);color:var(--c4);padding:3px 8px;border-radius:5px;margin-right:5px;display:inline-block;font-weight:bold;font-size:14px}
.hl{background:linear-gradient(transparent 60%,rgba(212,168,67,.3) 60%);font-weight:bold}
.bub{position:relative;background:#fff;border:3px solid var(--c1);border-radius:20px;padding:12px 15px;margin:15px 5px;font-family:'Yomogi',cursive;box-shadow:3px 3px 10px rgba(0,0,0,.1);transform:rotate(-1deg)}
.bub::after{content:'';position:absolute;bottom:-13px;left:20px;border-width:12px 8px 0;border-style:solid;border-color:var(--c1) transparent;display:block;width:0}
.bub.r::after{left:auto;right:20px;transform:rotate(15deg)}
.bub.t::after{bottom:auto;top:-13px;border-width:0 8px 12px;transform:rotate(-5deg)}
.bub.v1{background:#FFF9E3;border-color:var(--c2);transform:rotate(1deg)}.bub.v1::after{border-color:var(--c2) transparent}
.bub.v2{background:#FFE9E9;border-color:var(--c5);transform:rotate(-2deg)}.bub.v2::after{border-color:var(--c5) transparent}
.hw{font-family:'Yomogi',cursive;font-size:15px;line-height:1.5;color:#333}
.fi{opacity:0;transform:scale(.95);animation:fis .6s ease forwards}
@keyframes fis{to{opacity:1;transform:scale(1)}}
.card:nth-child(1){animation-delay:.1s}.card:nth-child(2){animation-delay:.2s}.card:nth-child(3){animation-delay:.3s}.card:nth-child(4){animation-delay:.4s}
footer{text-align:center;padding:30px 20px;margin-top:30px;font-size:14px;color:#777;border-top:2px dashed #ddd}
footer a{color:var(--c1);text-decoration:none}footer a:hover{text-decoration:underline}
@media(max-width:1600px){.card{min-width:280px}}@media(max-width:1200px){.card{min-width:320px}}@media(max-width:900px){.card{min-width:380px}}@media(max-width:768px){.row{flex-direction:column}.card{width:100%;min-width:auto}}
"""

rows_html = "\n".join(f'<div class="row">{r}</div>' for r in rows)

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SpaceX上場 — Bioshokさんに聞く史上最大のIPO | 超知能×近未来社会 勉強会第120回</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">
<div class="header">
    <div class="header-icon"><i class="fas fa-rocket fa-7x"></i></div>
    <h1>SpaceX 上場 — 史上最大の IPO</h1>
    <div class="sub">Bioshok さんに聞く — 超知能×近未来社会 勉強会 第120回</div>
    <div class="date"><i class="fas fa-calendar"></i> 2026年6月10日収録 / 6月12日IPO予定</div>
</div>
{rows_html}
<footer>
    <p>🎬 動画: <a href="https://youtu.be/oQ1V0xsWYx8" target="_blank">超知能×近未来社会(AI経済学・AI政治学・AI社会学)</a> | 📅 2026年6月10日収録</p>
    <p style="margin-top:5px;font-size:12px;color:#999">SpaceX上場 インフォグラフィック | 2026年6月11日作成 | ※投資助言ではありません</p>
</footer>
</div>
</body>
</html>"""

outpath = "/home/victo/work/ai-news-infographic/docs/20260611-SpaceX上場-史上最大IPO-超知能×近未来社会.html"
with open(outpath, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Written {len(html)} bytes to {outpath}")
print(f"Cards: {len(cards)}")
