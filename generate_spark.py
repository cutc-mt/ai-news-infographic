#!/usr/bin/env python3
"""Generate Gemini Spark infographic HTML."""
import os

OUT = os.path.join(os.path.dirname(__file__), "docs", "20260530-Gemini-Spark-AIエージェント-使える活用術-mikimiki-webスクール.html")

css = """
@import url('https://fonts.googleapis.com/css2?family=Kaisei+Decol&family=Yomogi&family=Zen+Kurenaido&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
:root{--ui-color-1:#00897B;--ui-color-2:#F9A825;--ui-color-3:#E0F2F1;--ui-color-4:#004D40;--ui-color-5:#FF8F00}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#FAFAFA;font-family:'Kaisei Decol',serif;color:#333;line-height:1.6}
.container{max-width:2000px;margin:0 auto;padding:20px}
.header{text-align:center;padding:50px 20px;margin-bottom:30px;background:linear-gradient(135deg,var(--ui-color-4),var(--ui-color-1),var(--ui-color-2));border-radius:30px;color:#fff;position:relative;overflow:hidden}
.header::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle,rgba(255,255,255,.08)0%,transparent 60%);animation:hg 8s ease-in-out infinite}
@keyframes hg{0%,100%{transform:translate(0,0)}50%{transform:translate(20px,20px)}}
.header-icon{font-size:5em;margin-bottom:10px;animation:fa-bounce 2s infinite}
.header h1{font-size:2.4em;font-weight:900;margin-bottom:10px;text-shadow:2px 2px 4px rgba(0,0,0,.3)}
.header .subtitle{font-size:1.3em;opacity:.9;font-family:'Yomogi',cursive}
.header .date{font-size:.9em;opacity:.7;margin-top:10px}
.header .spark-label{display:inline-block;margin-top:15px;background:rgba(0,0,0,.3);padding:5px 20px;border-radius:20px;font-size:1.1em;font-weight:bold}
.tl{color:#80CBC4}.gl{color:#FFE082}
.section-layout{display:flex;flex-wrap:wrap;gap:20px;justify-content:center;margin-bottom:20px}
.section-card{flex:1;min-width:280px;max-width:450px;background:#fff;border-radius:20px;padding:20px;box-shadow:5px 5px 15px rgba(0,0,0,.1);position:relative;overflow:hidden;transition:transform .3s,box-shadow .3s}
.section-card:hover{transform:translateY(-5px);box-shadow:8px 8px 25px rgba(0,0,0,.15)}
.section-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:5px;background:linear-gradient(90deg,var(--ui-color-1),var(--ui-color-2))}
.section-card.teal-accent::before{background:linear-gradient(90deg,var(--ui-color-4),var(--ui-color-1))}
.section-card.gold-accent::before{background:linear-gradient(90deg,var(--ui-color-2),var(--ui-color-5))}
.mega-icon-container{text-align:center;margin:15px 0}
.mega-icon-container h2{font-size:1.2em;color:var(--ui-color-4);margin-top:10px}
.card-content{padding:0 10px 15px}
.keyword-list{margin:15px 0;padding:0;list-style:none}
.keyword-list li{margin-bottom:10px;display:flex;align-items:flex-start;font-size:15px;line-height:1.6}
.keyword-list li i{margin-right:8px;color:var(--ui-color-1);min-width:16px;margin-top:4px}
.keyword-list li .gold-icon{color:var(--ui-color-2)}
.keyword-tag{background:var(--ui-color-3);color:var(--ui-color-4);padding:3px 8px;border-radius:5px;margin-right:5px;display:inline-block;font-weight:bold;font-size:14px}
.keyword-tag.teal{background:#E0F2F1;color:#004D40}
.keyword-tag.gold{background:#FFF8E1;color:#E65100}
.speech-bubble{position:relative;background:#fff;border:3px solid var(--ui-color-1);border-radius:20px;padding:12px 15px;margin:15px 5px;font-family:'Yomogi',cursive;box-shadow:3px 3px 10px rgba(0,0,0,.1);transform:rotate(-1deg)}
.speech-bubble::after{content:'';position:absolute;bottom:-13px;left:20px;border-width:12px 8px 0;border-style:solid;border-color:var(--ui-color-1) transparent;display:block;width:0}
.speech-bubble.right::after{left:auto;right:20px;transform:rotate(15deg)}
.speech-bubble.top::after{bottom:auto;top:-13px;border-width:0 8px 12px;transform:rotate(-5deg)}
.speech-bubble.variant-1{background:#FFF9E3;border-color:var(--ui-color-2);transform:rotate(1deg)}
.speech-bubble.variant-1::after{border-color:var(--ui-color-2) transparent}
.speech-bubble.variant-2{background:#E0F7FA;border-color:#00ACC1;transform:rotate(-2deg)}
.speech-bubble.variant-2::after{border-color:#00ACC1 transparent}
.speech-bubble.variant-3{background:#FFF3E0;border-color:var(--ui-color-5);transform:rotate(.5deg)}
.speech-bubble.variant-3::after{border-color:var(--ui-color-5) transparent}
.handwritten{font-family:'Yomogi',cursive;font-size:15px;line-height:1.5;color:#333}
.highlight{background:linear-gradient(transparent 60%,rgba(0,137,123,.25)60%);font-weight:bold}
.highlight.gold{background:linear-gradient(transparent 60%,rgba(249,168,37,.25)60%)}
.fade-in-scale{opacity:0;transform:scale(.95);animation:fis .6s ease forwards}
@keyframes fis{to{opacity:1;transform:scale(1)}}
footer{text-align:center;padding:30px 20px;margin-top:30px;font-size:14px;color:#777;border-top:2px dashed #ddd}
footer a{color:var(--ui-color-1);text-decoration:none}footer a:hover{text-decoration:underline}
.price-table{width:100%;border-collapse:collapse;font-size:14px;margin-top:10px}
.price-table th{background:linear-gradient(90deg,var(--ui-color-4),var(--ui-color-1));color:#fff;padding:8px 6px;font-size:13px}
.price-table td{padding:6px;text-align:center;border-bottom:1px dashed #eee}
.price-table tr:nth-child(even){background:#f9f9f9}
.price-highlight{font-weight:bold}
@media(max-width:1600px){.section-card{min-width:280px}}
@media(max-width:1200px){.section-card{min-width:320px}}
@media(max-width:900px){.section-card{min-width:380px}}
@media(max-width:768px){.section-layout{flex-direction:column}.section-card{width:100%;min-width:auto}}
"""

def li(icon, text, gold=False):
    cls = ' class="gold-icon"' if gold else ''
    return f'<li><i class="{icon}"{cls}></i><span>{text}</span></li>'

def card(n, title, icon, color, anim, accent, items, bub_cls, bub_text, extra=''):
    items_html = '\n                    '.join(items)
    return f"""            <div class="section-card fade-in-scale {accent}">
                <div class="mega-icon-container">
                    <i class="{icon} fa-5x" style="color: {color}; animation: {anim};"></i>
                    <h2>{n} {title}</h2>
                </div>
                <div class="card-content">
                    <ul class="keyword-list">
                    {items_html}
                    </ul>
                    {extra}
                    <div class="speech-bubble {bub_cls}"><span class="handwritten">{bub_text}</span></div>
                </div>
            </div>"""

# Build cards
cards = []
cards.append(card("①","Gemini Sparkとは？24時間動くAIエージェント",
    "fa-solid fa-fire","var(--ui-color-5)","fa-beat-fade 2s infinite","teal-accent",
    [li("fa-solid fa-circle-check","Google I/O 2026で発表された<span class=\"highlight\">24時間365日動くパーソナルAIエージェント</span>"),
     li("fa-solid fa-cloud","クラウド上で<span class=\"keyword-tag teal\">常にバックグラウンドで稼働</span>。従来のチャットボットとは根本的に違う"),
     li("fa-solid fa-microchip","動力は<span class=\"keyword-tag gold\">Gemini 3.5 Flash</span>とGoogleの<span class=\"keyword-tag teal\">Antigravity</span>ハーネス"),
     li("fa-solid fa-user-clock","スマホを閉じてもデバイスをロックしても<span class=\"highlight\">自律的にタスクをこなし続ける</span>"),
     li("fa-solid fa-circle-info","「反応型のアシスタント」から<span class=\"keyword-tag gold\">「能動型のエージェント」</span>への大転換")],
    "variant-3","<i class=\"fa-solid fa-lightbulb fa-lg\" style=\"color:var(--ui-color-5)\"></i>「話しかけたら答える」じゃなくて<br><span class=\"keyword-tag gold\">「勝手に動いてくれる」</span><br>それがエージェントの革命！"))

cards.append(card("②","チャットボットと何が違う？従来との比較",
    "fa-solid fa-code-compare","var(--ui-color-1)","fa-flip 3s infinite","teal-accent",
    [li("fa-solid fa-comments","<span class=\"keyword-tag\">従来のアシスタント</span> — ユーザーが入力して初めて反応する「待ち」の姿勢"),
     li("fa-solid fa-robot","<span class=\"keyword-tag gold\">Gemini Spark</span> — <span class=\"highlight\">自律的に判断して行動</span>する「攻め」の姿勢"),
     li("fa-solid fa-clock","プロンプトを入れなくても<span class=\"keyword-tag teal\">設定したルールとゴール</span>に沿って動き続ける"),
     li("fa-solid fa-arrows-spin","<span class=\"highlight gold\">複数ステップのタスク</span>を一連の流れで自動実行できるのが最大の違い"),
     li("fa-solid fa-circle-check","メール仕分け、カレンダー調整、リサーチを<span class=\"keyword-tag teal\">バックグラウンドで24時間</span>実行")],
    "variant-2 right","<i class=\"fa-solid fa-arrow-up fa-lg\" style=\"color:#00ACC1\"></i>「聞かれたら答える」から<br><span class=\"keyword-tag teal\">「気づいて動く」</span>へ。<br>AIの進化の大きな一歩！"))

cards.append(card("③","動力源: Antigravityハーネスとは？",
    "fa-solid fa-gears","var(--ui-color-5)","fa-bounce 2s infinite","gold-accent",
    [li("fa-solid fa-wrench","<span class=\"keyword-tag gold\">Antigravity</span>はGoogleの<span class=\"highlight\">エージェントファースト開発プラットフォーム</span>",True),
     li("fa-solid fa-server","Gemini Sparkを支えるエンジンとして<span class=\"keyword-tag teal\">クラウド上で常時稼働</span>させる基盤",True),
     li("fa-solid fa-bolt","<span class=\"keyword-tag gold\">Gemini 3.5 Flash</span>と共同最適化された高速エンジンでリアルタイム処理を実現",True),
     li("fa-solid fa-puzzle-piece","Antigravity 2.0はデスクトップアプリで複数のエージェントを<span class=\"highlight\">一元管理・並列実行</span>",True),
     li("fa-solid fa-terminal","CLIとSDKも提供。開発者がエージェントをカスタム構築することも可能",True)],
    "variant-1","<i class=\"fa-solid fa-cogs fa-lg\" style=\"color:var(--ui-color-2)\"></i>Antigravityはエージェントの<br><span class=\"keyword-tag gold\">「心臓と血管」</span>。<br>Sparkを動かす命の源です。"))

cards.append(card("④","頭脳: Gemini 3.5 Flashのスペック",
    "fa-solid fa-brain","var(--ui-color-1)","fa-beat-fade 2s infinite","teal-accent",
    [li("fa-solid fa-microchip","Gemini Sparkを駆動するモデルは<span class=\"keyword-tag gold\">Gemini 3.5 Flash</span>"),
     li("fa-solid fa-dollar-sign","API価格は<span class=\"highlight\">入力$1.50 / 出力$9.00</span>（100万トークンあたり）でコスト効率良好"),
     li("fa-solid fa-gauge-high","Flashシリーズ最大の特徴は<span class=\"highlight gold\">高速処理能力</span>。リアルタイム動作に不可欠"),
     li("fa-solid fa-code","<span class=\"keyword-tag teal\">長期間のソフトウェア開発</span>やMLエンジニアリングのタスクにも対応"),
     li("fa-solid fa-rocket","2026年5月リリースの最新モデルでAntigravityと<span class=\"keyword-tag gold\">共同最適化</span>されている")],
    "variant-3 top","<i class=\"fa-solid fa-star fa-lg\" style=\"color:var(--ui-color-5)\"></i>高速で安い。<br><span class=\"keyword-tag gold\">エージェントの頭脳</span>として<br>これ以上の組み合わせはない。"))

cards.append(card("⑤","Google Workspaceとネイティブ連携",
    "fa-solid fa-layer-group","var(--ui-color-1)","fa-spin 4s linear infinite","teal-accent",
    [li("fa-solid fa-envelope","<span class=\"keyword-tag teal\">Gmail</span> — メール仕分け、返信下書き、重要メッセージの自動抽出"),
     li("fa-solid fa-calendar","<span class=\"keyword-tag teal\">カレンダー</span> — 招待への自動返信、予定調整、イベントの作成"),
     li("fa-solid fa-file-lines","<span class=\"keyword-tag teal\">Docs / Sheets / Slides</span> — ドキュメント作成、データ整理、プレゼン生成"),
     li("fa-solid fa-hard-drive","<span class=\"keyword-tag teal\">Google Drive</span> — ファイル整理、プロジェクトノートの収集と要約"),
     li("fa-solid fa-map","<span class=\"keyword-tag teal\">Maps / YouTube</span> — 位置情報の活用や動画管理にも対応")],
    "variant-2","<i class=\"fa-solid fa-link fa-lg\" style=\"color:#00ACC1\"></i>Googleサービスを<span class=\"keyword-tag teal\">まるごと</span><br>つなげて使えるのが<br>最大の強みです。"))

cards.append(card("⑥","メール自動化: Gmail連携の威力",
    "fa-solid fa-envelope-open-text","var(--ui-color-2)","fa-bounce 2s infinite","gold-accent",
    [li("fa-solid fa-inbox","受信トレイを<span class=\"keyword-tag gold\">自動で仕分け</span>。重要メールとそうでないものに分類",True),
     li("fa-solid fa-reply","返信の<span class=\"highlight gold\">下書きを自動作成</span>。確認して送信するだけ",True),
     li("fa-solid fa-list-check","スレッドから<span class=\"keyword-tag teal\">アクションアイテムを抽出</span>してタスクリスト化",True),
     li("fa-solid fa-eye","カレンダーの空きを確認して<span class=\"highlight\">会議の日程調整</span>まで自動で行う",True),
     li("fa-solid fa-circle-info","設定は<span class=\"keyword-tag gold\">自然な会話</span>でOK。「毎朝重要メールをまとめて」で完了",True)],
    "variant-1 right","<i class=\"fa-solid fa-paper-plane fa-lg\" style=\"color:var(--ui-color-2)\"></i>朝起きたら<span class=\"keyword-tag gold\">メール整理</span>が<br>終わってる。<br>それが日常になります。"))

cards.append(card("⑦","スケジュール管理: カレンダーの自動調整",
    "fa-solid fa-calendar-days","var(--ui-color-4)","fa-flip 3s infinite","teal-accent",
    [li("fa-solid fa-calendar-check","空き枠を確認して<span class=\"keyword-tag teal\">会議候補を自動出し</span>"),
     li("fa-solid fa-envelope-circle-check","イベントへの招待を<span class=\"highlight\">確認して自動でRSVP</span>"),
     li("fa-solid fa-clock","一日のタスクを<span class=\"keyword-tag gold\">優先順位に合わせてスケジューリング</span>"),
     li("fa-solid fa-users","複数人のカレンダーを<span class=\"highlight\">跨いだ調整</span>も可能"),
     li("fa-solid fa-bell","重要イベントの前に<span class=\"keyword-tag teal\">リマインダー</span>を自動送信して準備を促す")],
    "","<i class=\"fa-solid fa-handshake fa-lg\" style=\"color:var(--ui-color-1)\"></i>「金曜3時以降空いてる？」<br><span class=\"keyword-tag teal\">誰に聞く必要もない</span>。<br>Sparkが全部やってくれます。"))

cards.append(card("⑧","ドキュメント自動作成: 会議メモからレポート",
    "fa-solid fa-file-pen","var(--ui-color-5)","fa-beat-fade 2s infinite","gold-accent",
    [li("fa-solid fa-file-lines","プロジェクトの<span class=\"keyword-tag gold\">ノートを自動収集して要約</span>。複数ソースから統合",True),
     li("fa-solid fa-pen-fancy","会議の議事録を<span class=\"highlight gold\">自動で生成</span>してアクションアイテムまで抽出",True),
     li("fa-solid fa-table-columns","Sheetsで<span class=\"keyword-tag teal\">データ整理や分析</span>を自動実行。レポート作成も可能",True),
     li("fa-solid fa-display","プレゼン資料の<span class=\"keyword-tag gold\">構成案を自動作成</span>してスライドの下書きまで生成",True),
     li("fa-solid fa-wand-magic-sparkles","自然な会話で<span class=\"highlight\">複数アプリをまたいだタスク</span>を設定できるのが魅力")],
    "variant-3 top","<i class=\"fa-solid fa-wand-magic-sparkles fa-lg\" style=\"color:var(--ui-color-5)\"></i>「今週の進捗を<br><span class=\"keyword-tag gold\">スライドにまとめて」</span><br>それだけで完了。"))

cards.append(card("⑨","利用条件: 誰が使える？",
    "fa-solid fa-user-check","var(--ui-color-4)","fa-bounce 2s infinite","teal-accent",
    [li("fa-solid fa-flag","現在は<span class=\"highlight\">米国在住のAI Ultra加入者</span>（18歳以上）に順次ロールアウト中"),
     li("fa-solid fa-building","一部の<span class=\"keyword-tag teal\">ビジネスユーザー</span>も対象。企業向けの展開を加速中"),
     li("fa-solid fa-flask","初期段階では<span class=\"keyword-tag gold\">信頼済みテスター</span>への提供から始まり段階的に拡大"),
     li("fa-solid fa-earth-americas","現在は<span class=\"highlight gold\">米国限定</span>。今後のグローバル展開が期待される"),
     li("fa-solid fa-circle-info","AI Ultraは<span class=\"keyword-tag teal\">$100/月または$200/月</span>のサブスクが必要")],
    "variant-2 right","<i class=\"fa-solid fa-earth-americas fa-lg\" style=\"color:#00ACC1\"></i>残念ながら<span class=\"keyword-tag teal\">米国限定</span>。<br>でも世界展開は時間の問題。<br>楽しみに待ちましょう！"))

# Card 10 with price table
price_table = """<table class="price-table">
<tr><th>プラン</th><th>月額料金</th><th>Spark対応</th></tr>
<tr><td>AI Ultra ($100)</td><td class="price-highlight">$100/月</td><td>✅ 利用可</td></tr>
<tr><td>AI Ultra ($200)</td><td class="price-highlight">$200/月</td><td>✅ 利用可</td></tr>
<tr><td>AI Pro</td><td>$19.99/月</td><td>❌ 対象外</td></tr>
<tr><td>AI Plus</td><td>$7.99/月</td><td>❌ 対象外</td></tr>
<tr><td>Free</td><td>$0</td><td>❌ 対象外</td></tr>
</table>"""
cards.append(card("⑩","料金プラン: Google AI Ultraの価格",
    "fa-solid fa-tags","var(--ui-color-2)","fa-flip 3s infinite","gold-accent",
    [li("fa-solid fa-circle-info","Gemini Sparkを利用するには<span class=\"highlight gold\">AI Ultraへの加入が必須</span>",True),
     li("fa-solid fa-gift","Ultraには<span class=\"keyword-tag teal\">5倍〜20倍の使用量上限</span>、クラウドストレージ、YouTube Premiumも付帯",True)],
    "variant-1","<i class=\"fa-solid fa-coins fa-lg\" style=\"color:var(--ui-color-2)\"></i><span class=\"keyword-tag gold\">$100/月</span>から使える。<br>以前は$250だったので<br>大幅な値下がりです。",price_table))

cards.append(card("⑪","プライバシーと権限: 安全に使うために",
    "fa-solid fa-shield-halved","var(--ui-color-4)","fa-beat-fade 2s infinite","teal-accent",
    [li("fa-solid fa-toggle-off","Googleアプリとの連携は<span class=\"highlight\">デフォルトでオフ</span>。ユーザーが有効にする必要がある"),
     li("fa-solid fa-sliders","<span class=\"keyword-tag teal\">権限コントロール</span>でSparkがアクセスできるデータを細かく指定可能"),
     li("fa-solid fa-lock","<span class=\"highlight teal\">制御された委譲</span>の概念に基づき、自律性のレベルをユーザーが設定"),
     li("fa-solid fa-eye-slash","Workspaceデータは<span class=\"keyword-tag gold\">AIモデルの学習に使われない</span>（有料サービス）"),
     li("fa-solid fa-certificate","ISO 42001、BSI C5、FedRAMP Highなど<span class=\"keyword-tag teal\">厳格なセキュリティ認証</span>を取得済み")],
    "","<i class=\"fa-solid fa-lock fa-lg\" style=\"color:var(--ui-color-4)\"></i>「AIに勝手に動かされるのは嫌」<br><span class=\"keyword-tag teal\">権限設定でコントロール</span>。<br>初期設定はオフだから安心。"))

cards.append(card("⑫","コーディング不要: 会話で設定する",
    "fa-solid fa-comments","var(--ui-color-2)","fa-bounce 2s infinite","gold-accent",
    [li("fa-solid fa-comment-dots","<span class=\"keyword-tag gold\">プログラミングは一切不要</span>。自然な会話でタスクを設定",True),
     li("fa-solid fa-wand-magic-sparkles","例：「<span class=\"highlight\">毎朝8時に未読メールをまとめて</span>」「週末にレポートを作って」",True),
     li("fa-solid fa-diagram-project","複数のアプリをまたぐ<span class=\"keyword-tag teal\">複雑なスケジュール</span>も会話で設定可能",True),
     li("fa-solid fa-lightbulb","日常的なタスクの自動化が<span class=\"highlight gold\">誰でも手軽に</span>できるのが最大の魅力"),
     li("fa-solid fa-user-graduate","技術知識が不要なので<span class=\"keyword-tag gold\">ビジネスパーソン</span>にもすぐに使い始められる",True)],
    "variant-3 top","<i class=\"fa-solid fa-face-smile fa-lg\" style=\"color:var(--ui-color-5)\"></i>コードを書かなくても<br><span class=\"keyword-tag gold\">AIエージェント</span>が使える。<br>これが未来の働き方。"))

cards.append(card("⑬","Antigravity 2.0: 開発者向けプラットフォーム",
    "fa-solid fa-cubes","var(--ui-color-1)","fa-flip 3s infinite","teal-accent",
    [li("fa-solid fa-desktop","<span class=\"keyword-tag teal\">デスクトップアプリ</span>として複数のエージェントを<span class=\"highlight\">一元管理・監視</span>できる"),
     li("fa-solid fa-terminal","<span class=\"keyword-tag gold\">CLI（コマンドライン）</span>で軽量にエージェントをビルド＆デプロイ"),
     li("fa-solid fa-code","<span class=\"keyword-tag gold\">SDK</span>を使えばプログラムからAntigravityハーネスに直接アクセス可能"),
     li("fa-solid fa-rocket","Gemini Enterprise Agent Platform経由で<span class=\"keyword-tag teal\">企業でも利用可能</span>"),
     li("fa-solid fa-circle-check","AI Studio連携でプロジェクトを<span class=\"highlight\">ビルドしてエクスポート</span>できる")],
    "variant-2 right","<i class=\"fa-solid fa-laptop-code fa-lg\" style=\"color:#00ACC1\"></i>開発者なら<span class=\"keyword-tag teal\">Antigravity</span>で<br>自分だけのエージェントを<br><span class=\"keyword-tag gold\">自由に構築</span>できます。"))

cards.append(card("⑭","具体的な活用例: 日常をどう変える？",
    "fa-solid fa-lightbulb","var(--ui-color-5)","fa-beat-fade 2s infinite","gold-accent",
    [li("fa-solid fa-credit-card","<span class=\"keyword-tag gold\">クレジットカード明細の監視</span> — 怪しい請求を自動チェックして通知",True),
     li("fa-solid fa-inbox","<span class=\"keyword-tag teal\">メールのトリアージ</span> — 緊急度に応じて振り分け、返信の優先順位を整理",True),
     li("fa-solid fa-folder-open","<span class=\"keyword-tag teal\">プロジェクトノートの収集</span> — チームのドキュメントを自動で集めて要約",True),
     li("fa-solid fa-magnifying-glass","<span class=\"keyword-tag gold\">バックグラウンドリサーチ</span> — テーマを指定しておくと関連情報を自動収集",True),
     li("fa-solid fa-chart-pie","<span class=\"highlight\">週次レポートの自動生成</span> — 複数のデータソースから統合レポートを作成")],
    "variant-1","<i class=\"fa-solid fa-bolt fa-lg\" style=\"color:var(--ui-color-2)\"></i>ルーティンワークを<span class=\"keyword-tag gold\">AIに丸投げ</span>。<br>人間は<span class=\"keyword-tag teal\">考える時間</span>に<br>集中できます。"))

cards.append(card("⑮","企業での活用: ビジネスユースの可能性",
    "fa-solid fa-building","var(--ui-color-4)","fa-bounce 2s infinite","teal-accent",
    [li("fa-solid fa-users","一部の<span class=\"keyword-tag teal\">ビジネスユーザー</span>にすでに提供開始。企業向け展開を加速中"),
     li("fa-solid fa-handshake","<span class=\"highlight\">Gmail / Docs / Sheets</span>とのネイティブ連携で<span class=\"keyword-tag gold\">チームのコラボレーション</span>を強化"),
     li("fa-solid fa-chart-line","定期的な<span class=\"keyword-tag teal\">データレポートの生成</span>や、顧客向けパーソナライズ通信の作成"),
     li("fa-solid fa-flask","Antigravityエージェントは<span class=\"keyword-tag gold\">科学的発見の加速</span>やコードベースの研究にも活用可能"),
     li("fa-solid fa-circle-check","<span class=\"highlight teal\">Gemini Enterprise Agent Platform</span>で企業レベルのセキュリティとガバナンスを提供")],
    "variant-3","<i class=\"fa-solid fa-briefcase fa-lg\" style=\"color:var(--ui-color-5)\"></i>個人だけでなく<span class=\"keyword-tag teal\">企業の業務効率化</span>にも<br>エージェントが革命的な変化を<br>もたらします。"))

cards.append(card("⑯","競合比較: 他のAIエージェントとの違い",
    "fa-solid fa-scale-balanced","var(--ui-color-2)","fa-beat-fade 2s infinite","gold-accent",
    [li("fa-solid fa-circle-check","<span class=\"keyword-tag gold\">ChatGPT</span> — 反応型。プロンプト必須で継続的なバックグラウンド動作はしない",True),
     li("fa-solid fa-circle-xmark","<span class=\"keyword-tag\">Microsoft Copilot</span> — Workspace連携はあるが自律的なマルチステップ実行は限定的",True),
     li("fa-solid fa-fire","<span class=\"keyword-tag teal\">Gemini Spark</span> — <span class=\"highlight\">24/7常時稼働</span>で複数サービスをまたいだ自律タスク実行が可能"),
     li("fa-solid fa-link","Google Workspaceへの<span class=\"highlight teal\">ネイティブ連携</span>が他社にはない最大の差別化ポイント"),
     li("fa-solid fa-gem","<span class=\"keyword-tag gold\">制御された委譲</span>モデルで、自律性と安全性のバランスを取った設計")],
    "variant-1 right","<i class=\"fa-solid fa-trophy fa-lg\" style=\"color:var(--ui-color-2)\"></i>Workspaceへの<span class=\"keyword-tag teal\">深い連携</span>が<br>Sparkの<span class=\"keyword-tag gold\">最大の強み</span>。<br>他の追随を許さない構成です。"))

cards.append(card("⑰","設定と利用のステップ: さあ始めよう",
    "fa-solid fa-list-ol","var(--ui-color-1)","fa-bounce 2s infinite","teal-accent",
    [li("fa-solid fa-1","<span class=\"keyword-tag teal\">Step 1</span> — Google AI Ultra（$100/月以上）にサブスクリプションを申し込む"),
     li("fa-solid fa-2","<span class=\"keyword-tag teal\">Step 2</span> — GeminiアプリでSparkを有効にして初期セットアップを完了する"),
     li("fa-solid fa-3","<span class=\"keyword-tag teal\">Step 3</span> — 連携したいGoogleサービス（Gmailやカレンダーなど）を選択して有効にする"),
     li("fa-solid fa-4","<span class=\"keyword-tag gold\">Step 4</span> — 自然な会話でタスクやルールを設定。「毎朝8時にメールをまとめて」等"),
     li("fa-solid fa-5","<span class=\"keyword-tag gold\">Step 5</span> — <span class=\"highlight\">権限レベルを調整</span>して、Sparkの自律性を自分の好みに合わせる")],
    "variant-2","<i class=\"fa-solid fa-play fa-lg\" style=\"color:#00ACC1\"></i>たった5ステップで<span class=\"keyword-tag teal\">AIエージェント</span>が<br>自分専用のアシスタントに。<br>設定は<span class=\"keyword-tag gold\">会話だけ</span>で完了。"))

cards.append(card("⑱","まとめ: エージェント時代の幕開け",
    "fa-solid fa-hand-point-right","var(--ui-color-2)","fa-bounce 2s infinite","gold-accent",
    [li("fa-solid fa-fire","<span class=\"keyword-tag teal\">Gemini Spark</span> — 24時間365日動くGoogleのパーソナルAIエージェント"),
     li("fa-solid fa-gears","<span class=\"keyword-tag gold\">Antigravity</span> — Sparkを支えるエージェント開発プラットフォーム"),
     li("fa-solid fa-brain","<span class=\"keyword-tag gold\">Gemini 3.5 Flash</span> — 高速・低コストの頭脳でリアルタイム処理を実現",True),
     li("fa-solid fa-lock","<span class=\"keyword-tag teal\">プライバシー保護</span> — デフォルトオフの連携、権限コントロール、厳格なセキュリティ認証"),
     li("fa-solid fa-circle-check","コーディング不要で<span class=\"highlight gold\">誰でも使える</span>。エージェント時代がいよいよ本格的に幕開け")],
    "variant-3 right","<i class=\"fa-solid fa-check-double fa-lg\" style=\"color:var(--ui-color-5)\"></i>「AIに任せる」から<br><span class=\"keyword-tag teal\">Gemini Sparkで<br><span class=\"keyword-tag gold\">エージェント時代が幕開け</span>！<br>未来の働き方が変わります。"))

# Assemble HTML
rows = []
for i in range(0, len(cards), 4):
    rows.append('\n        <div class="section-layout">\n' + '\n'.join(cards[i:i+4]) + '\n        </div>')

body = '\n'.join(rows)

html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google「Gemini Spark」使えるAIエージェント登場！使い方と活用例を徹底解説</title>
    <style>{css}</style>
</head>
<body>
<div class="container">
    <div class="header">
        <div class="header-icon"><i class="fas fa-fire fa-7x"></i></div>
        <h1>Google「Gemini Spark」ついに登場！</h1>
        <div class="subtitle">24時間365日動くAIエージェントの使い方と活用例を徹底解説</div>
        <div class="date"><i class="fas fa-calendar"></i> 2026年5月公開 | Google I/O 2026 発表</div>
        <div class="spark-label">
            <span class="tl"><i class="fas fa-bolt"></i> Gemini Spark</span>
            <span style="margin:0 10px">✨</span>
            <span class="gl"><i class="fas fa-robot"></i> Antigravity</span>
        </div>
    </div>
{body}
    <footer>
        <p>🎬 動画: <a href="https://www.youtube.com/watch?v=qY8mmhQAmB4" target="_blank" style="color:var(--ui-color-1)">mikimiki web スクール</a> | 📅 2026年5月公開</p>
        <p style="margin-top:5px;font-size:13px;color:#999">Gemini Spark インフォグラフィック | 2026年5月30日作成</p>
    </footer>
</div>
</body>
</html>"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated: {OUT}")
print(f"Card count: {len(cards)}")
print(f"File size: {os.path.getsize(OUT)} bytes")
