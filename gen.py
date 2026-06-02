#!/usr/bin/env python3
"""Generate the infographic HTML for OpenAI enterprise AI adoption report."""
import os

parts = []

# Helper
def card(icon, icon_color, icon_anim, title, title_icon, items, bubble_text, bubble_variant="", accent="", wall_num=None):
    a = accent
    wall_html = f'<span class="wall-number">{wall_num}</span>' if wall_num else ""
    lis = ""
    for it in items:
        lis += f'<li>{it}</li>\n'
    bub_cls = f" variant-{bubble_variant}" if bubble_variant else ""
    return f'''<div class="section-card{f" {a}"} fade-in-scale">
    <div class="mega-icon-container">
        {wall_html}
        <i class="fa-solid fa-{icon} fa-5x" style="color: {icon_color}; animation: fa-{icon_anim} 2s infinite;"></i>
        <h2><i class="fa-solid fa-{title_icon}"></i> {title}</h2>
    </div>
    <div class="card-content">
        <ul class="keyword-list">
            {lis}
        </ul>
    </div>
    <div class="speech-bubble{bub_cls}"><span class="handwritten">{bubble_text}</span></div>
</div>'''

def li(icon, icon_cls, text):
    return f'<li><i class="fa-solid fa-{icon} {icon_cls}"></i><span>{text}</span></li>'

# Build HTML
parts.append('''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>なぜ会社でAIは広まらないのか｜OpenAI公式が出した答えを全解説</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Kaisei+Decol&family=Yomogi&family=Zen+Kurenaido&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');
:root{--c1:#1E3A5F;--c2:#3B82F6;--c3:#F59E0B;--c4:#0F172A;--c5:#EF4444;--cb:#FFF}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#F8FAFC;font-family:'Kaisei Decol',serif;color:#334155;line-height:1.6}
.container{max-width:2000px;margin:0 auto;padding:20px}
.header{text-align:center;padding:50px 20px;margin-bottom:30px;background:linear-gradient(135deg,#0F172A 0%,#1E3A5F 40%,#3B82F6 100%);border-radius:30px;color:#fff;position:relative;overflow:hidden}
.header::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:radial-gradient(circle,rgba(59,130,246,.12) 0%,transparent 60%);animation:glow 8s ease-in-out infinite}
@keyframes glow{0%,100%{transform:translate(0,0)}50%{transform:translate(20px,20px)}}
.header-icon{font-size:5em;margin-bottom:10px;animation:fa-bounce 2s infinite}
.header h1{font-size:2.2em;font-weight:900;margin-bottom:10px;text-shadow:2px 2px 4px rgba(0,0,0,.3)}
.header .subtitle{font-size:1.3em;opacity:.9;font-family:'Yomogi',cursive}
.header .date{font-size:.9em;opacity:.7;margin-top:10px}
.header .vs-label{display:inline-block;margin-top:15px;background:rgba(0,0,0,.3);padding:5px 20px;border-radius:20px;font-size:1.1em;font-weight:bold}
.stl{display:flex;flex-wrap:wrap;gap:20px;justify-content:center;margin-bottom:20px}
.stb{width:100%;text-align:center;padding:15px 20px;margin:10px 0 5px;border-radius:15px;font-size:1.4em;font-weight:900;color:#fff}
.stb i{margin-right:10px}
.stb.slate{background:linear-gradient(90deg,#0F172A,#1E3A5F)}
.stb.cobalt{background:linear-gradient(90deg,#1E3A5F,#3B82F6)}
.stb.amber{background:linear-gradient(90deg,#92400E,#F59E0B)}
.stb.emerald{background:linear-gradient(90deg,#065F46,#10B981)}
.sc{flex:1;min-width:280px;max-width:450px;background:var(--cb);border-radius:20px;padding:20px;box-shadow:5px 5px 15px rgba(0,0,0,.1);position:relative;overflow:hidden;transition:transform .3s,box-shadow .3s}
.sc:hover{transform:translateY(-5px);box-shadow:8px 8px 25px rgba(0,0,0,.15)}
.sc::before{content:'';position:absolute;top:0;left:0;width:100%;height:5px;background:linear-gradient(90deg,var(--c2),var(--c3))}
.sc.danger::before{background:linear-gradient(90deg,var(--c5),#F97316)}
.sc.success::before{background:linear-gradient(90deg,#10B981,#3B82F6)}
.sc.amber-a::before{background:linear-gradient(90deg,var(--c3),#FBBF24)}
.mic{text-align:center;margin:15px 0}
.mic h2{font-size:1.15em;color:var(--c4);margin-top:8px}
.wn{display:inline-block;width:40px;height:40px;line-height:40px;border-radius:50%;background:var(--c5);color:#fff;font-weight:900;font-size:1.3em;margin-right:5px;vertical-align:middle;text-shadow:1px 1px 2px rgba(0,0,0,.3)}
.cc{padding:0 10px 15px}
.kl{margin:12px 0;padding:0;list-style:none}
.kl li{margin-bottom:9px;display:flex;align-items:flex-start;font-size:15px;line-height:1.6}
.kl li i{margin-right:8px;color:var(--c2);min-width:16px;margin-top:4px}
.kl li .a{color:var(--c3)}.kl li .r{color:var(--c5)}.kl li .g{color:#10B981}
.kt{background:#DBEAFE;color:#1E3A5F;padding:2px 8px;border-radius:5px;margin-right:5px;display:inline-block;font-weight:bold;font-size:13px}
.kt.a{background:#FEF3C7;color:#92400E}.kt.r{background:#FEE2E2;color:#991B1B}.kt.g{background:#D1FAE5;color:#065F46}
.hl{background:linear-gradient(transparent 60%,#FBBF24 60%);padding:0 3px;font-weight:bold}
.hr{background:linear-gradient(transparent 60%,#FCA5A5 60%);padding:0 3px;font-weight:bold}
.sb{position:relative;background:#fff;border:3px solid var(--c2);border-radius:20px;padding:10px 15px;margin:12px 5px;font-family:'Yomogi',cursive;box-shadow:3px 3px 10px rgba(0,0,0,.08);transform:rotate(-1deg)}
.sb::after{content:'';position:absolute;bottom:-13px;left:20px;border-width:12px 8px 0;border-style:solid;border-color:var(--c2) transparent;display:block;width:0}
.sb.v1{background:#FFFBEB;border-color:var(--c3);transform:rotate(1deg)}.sb.v1::after{border-color:var(--c3) transparent}
.sb.v2{background:#FEF2F2;border-color:var(--c5);transform:rotate(-2deg)}.sb.v2::after{border-color:var(--c5) transparent}
.sb.v3{background:#ECFDF5;border-color:#10B981;transform:rotate(.5deg)}.sb.v3::after{border-color:#10B981 transparent}
.hw{font-family:'Yomogi',cursive;font-size:15px;line-height:1.5;color:#334155}
.footer{text-align:center;padding:30px 20px;margin-top:30px;background:linear-gradient(135deg,#0F172A 0%,#1E3A5F 100%);border-radius:20px;color:#94A3B8}
.footer a{color:#60A5FA;text-decoration:none}.footer a:hover{text-decoration:underline}
.footer .st{font-size:1.1em;color:#fff;margin-bottom:10px}
.fis{animation:fis .6s ease-out both}
@keyframes fis{from{opacity:0;transform:scale(.95)}to{opacity:1;transform:scale(1)}}
@media(max-width:1600px){.sc{min-width:280px}}
@media(max-width:1200px){.sc{min-width:320px}}
@media(max-width:900px){.sc{min-width:380px}}
@media(max-width:768px){.stl{flex-direction:column}.sc{width:100%;min-width:auto}.header h1{font-size:1.5em}}
</style>
</head>
<body>
<div class="container">
<div class="header">
<div class="header-icon">🏢</div>
<h1>なぜ会社でAIは広まらないのか</h1>
<div class="subtitle">OpenAI公式が出した答えを全解説</div>
<div class="date">📅 2026年6月2日</div>
<div class="vs-label" style="color:#60A5FA"><i class="fa-solid fa-robot"></i> 技術の問題ではなく<span style="color:#FBBF24">組織の問題</span> <i class="fa-solid fa-building"></i></div>
</div>
''')

# Section 1: 現状 (3 cards)
parts.append('<div class="stb slate"><i class="fa-solid fa-chart-line"></i> 企業AI導入の現状</div><div class="stl">')

parts.append(card('file-lines','var(--c2)','beat-fade','OpenAI公式レポート発表','landmark',[
    li('circle-info','','OpenAIが<span class="hl">企業向けAI導入リポート</span>を公式に発表'),
    li('calendar','','2025年・2026年の<span class="kt">企業レポート</span>で組織的制約がモデル性能以上の課題と指摘'),
    li('lightbulb','a','ChatGPT Enterpriseだけでは<span class="hl">「深いワークフロー自動化」</span>には不十分'),
    li('arrow-right','','モデルの性能ではなく、<span class="kt r">組織</span>の側に課題があると明言'),
],'<i class="fa-solid fa-quote-left fa-lg" style="color:var(--c3)"></i> AIの<span class="hl">真のボトルネック</span>は技術じゃない！<br>人と組織の準備なんだって💡','1'))

parts.append(card('chart-pie','var(--c5)','bounce','導入率のギャップ','arrow-trend-down',[
    li('circle-check','g','企業の<span class="hl">AI導入率</span>は表面上は高い'),
    li('triangle-exclamation','r','実際の従業員利用率はわずか<span class="kt r">10〜12%</span>'),
    li('user-tie','','リーダーシップ層は<span class="hl">「AIを導入した」</span>と認識'),
    li('ban','r','しかし現場での活用は進んでいない'),
    li('arrows-up-down','','経営層と現場の<span class="kt">認識乖離</span>が構造的課題'),
],'<i class="fa-solid fa-face-surprise fa-lg" style="color:var(--c5)"></i> 「導入した」≠「使っている」<br>経営層の思い込みに<span class="hr">要注意</span>！','2'))

parts.append(card('person-running','var(--c2)','flip','個人の生産性 vs 組織利益','scale-balanced',[
    li('user','g','個人の<span class="hl">生産性向上</span>は確認できている'),
    li('building','r','組織全体への<span class="kt r">利益還元</span>ができていない'),
    li('puzzle-piece','','個人の効率化が組織全体の利益に<span class="hr">繋がっていない</span>'),
    li('chart-simple','','マクロレベルの<span class="kt">ビジネス成果</span>への翻訳が失敗'),
    li('circle-exclamation','a','これが<span class="hl">壁5</span>の根本的な問題'),
],'<i class="fa-solid fa-lightbulb fa-lg" style="color:var(--c3)"></i> 個人なら上手く使えても、<br>組織まるごとは<span class="hl">別物</span>なんだね 🤔'))

parts.append('</div>')

# Section 2: 5つの壁 (8 cards)
parts.append('<div class="stb cobalt"><i class="fa-solid fa-shield-halved"></i> AIが広まらない 5つの壁</div><div class="stl">')

parts.append(card('sitemap','var(--c5)','beat-fade','組織の準備不足','user-gear',[
    li('xmark','r','<span class="hr">技術的な問題ではなく</span>、組織的制約が最大の障壁'),
    li('star','a','直属の上司の支援（<span class="kt">Manager Support</span>）がAI活用の<span class="hl">決定的な成功要因</span>'),
    li('comment-slash','r','マネージャーが<span class="kt r">「AIを使いなさい」</span>と言うだけでは不十分'),
    li('map','r','部門ごとの<span class="hl">AI活用方針</span>の不在'),
    li('people-group','','マネージャー自身が<span class="kt">ロールモデル</span>として使う必要がある'),
],'<i class="fa-solid fa-hand-point-up fa-lg" style="color:var(--c5)"></i> 上司が「使って」って言うだけじゃダメ！<br><span class="hr">自分から使って見せないと</span>💡','2','danger',1))

parts.append(card('lock','var(--c5)','bounce','データセキュリティとガバナンス','shield-halved',[
    li('bug','r','AI導入に伴う<span class="hr">データ露出リスク</span>が急増'),
    li('skull-crossbones','r','<span class="kt r">プロンプトインジェクション攻撃</span>の脅威'),
    li('database','r','モデルの記憶悪用・<span class="kt r">APIロギング</span>の脆弱性'),
    li('plug','r','第三者SaaS連携での<span class="hr">セキュリティホール</span>'),
    li('triangle-exclamation','a','構造化されたセキュリティアーキテクチャなしでは<span class="kt r">データ漏洩リスク大</span>'),
],'<i class="fa-solid fa-lock fa-lg" style="color:var(--c5)"></i> セキュリティを<span class="hr">後付け</span>にすると<br>後で大変なことに…🔒','2','danger',2))

parts.append(card('graduation-cap','var(--c3)','flip','スキルギャップと教育不足','book-open',[
    li('user-slash','r','従業員の<span class="hr">AIスキル不足</span>が重大な障壁'),
    li('pen-fancy','a','適切な<span class="kt">プロンプト作成</span>の知識が不足'),
    li('arrows-rotate','a','<span class="kt">反復的な出力改善</span>のスキル不足'),
    li('layer-group','a','コンテキスト提供・<span class="kt">タスク分割</span>の知識不足'),
    li('circle-xmark','r','ツールが「効かない」という<span class="hr">誤解</span>が蔓延'),
    li('school','r','AI教育・<span class="kt">トレーニングプログラム</span>の不在'),
],'<i class="fa-solid fa-pen fa-lg" style="color:var(--c3)"></i> 「AIダメだね」じゃなくて<br><span class="hl">使い方を教えてない</span>だけかも！📝','1'))

parts.append(card('people-arrows','var(--c5)','beat-fade','文化的抵抗とリーダーシップ','face-frown',[
    li('face-sad-tear','r','多くの従業員がAIに<span class="hr">仕事を奪われる不安</span>を感じている'),
    li('arrows-left-right','r','リーダーシップの認識と現場の実態の<span class="kt r">乖離</span>'),
    li('ban','r','<span class="hr">「技術の問題」ではなく「文化の問題」</span>'),
    li('comments','a','不安に対する<span class="kt">オープンな対話</span>が不足'),
    li('handshake','','組織文化としてAIを取り込む<span class="kt">仕組み</span>が必要'),
],'<i class="fa-solid fa-heart-pulse fa-lg" style="color:var(--c5)"></i> 不安を<span class="hr">放置</span>すると<br>みんな使わなくなるよ…😢','2','danger',4))

parts.append(card('diagram-project','var(--c5)','bounce','個人→組織への効果波及の失敗','link-slash',[
    li('user','g','個人の生産性向上は<span class="kt g">確認できている</span>'),
    li('building-columns','r','組織レベルの<span class="hr">利益に繋がっていない</span>'),
    li('language','r','マクロレベルの<span class="kt r">ビジネス成果</span>への翻訳が失敗'),
    li('gears','r','個人の効率化が組織全体の利益にならない<span class="hr">構造的問題</span>'),
    li('chart-column','','組織KPIへの<span class="kt">影響測定</span>の仕組みが不在'),
],'<i class="fa-solid fa-arrow-right-from-bracket fa-lg" style="color:var(--c5)"></i> 個人戦力が<strong>チーム戦力</strong>に<br><span class="hr">変換されない</span>のが最大の敗因 📊','2','danger',5))

# 5つの壁まとめ
parts.append(card('circle-exclamation','var(--c5)','beat-fade','5つの壁 まとめ','list-check',[
    li('1','r','<span class="kt r">組織の準備不足</span> — マネージャー支援の欠如'),
    li('2','r','<span class="kt r">セキュリティ</span> — データガバナンスの懸念'),
    li('3','r','<span class="kt r">スキルギャップ</span> — 教育プログラムの不在'),
    li('4','r','<span class="kt r">文化的抵抗</span> — リーダーシップの乖離'),
    li('5','r','<span class="kt r">波及の失敗</span> — 個人→組織への変換'),
    li('circle-info','a','どれも<span class="hr">技術の壁ではなく組織の壁</span>'),
],'<i class="fa-solid fa-rocket fa-lg" style="color:var(--c5)"></i> つまり<span class="hr">モデル性能じゃない</span>！<br>人と組織をどう変えるかが鍵🚀','2','danger'))

# 壁の連鎖
parts.append(card('share-nodes','var(--c2)','flip','壁は連鎖している','timeline',[
    li('link','','5つの壁は<span class="hl">相互に影響し合う</span>'),
    li('arrow-down','','準備不足 → 教育不足 → スキルギャップ → 使用率低下 → 組織効果ゼロ'),
    li('infinity','','<span class="kt r">負の連鎖</span>を断ち切るには<span class="hl">根本的な組織変革</span>が必要'),
    li('arrow-right','','壁1の<span class="kt">マネージャー支援</span>が他の壁の<span class="hl">ブレイクスルーポイント</span>'),
    li('lightbulb','a','一つの壁を突破すれば<span class="hl">連鎖的に他の壁も崩れる</span>可能性'),
],'<i class="fa-solid fa-link fa-lg" style="color:var(--c2)"></i> つながってるんだ！<br><span class="hl">一つ崩せば全体が動く</span>かも🔗'))

parts.append('</div>')

# Section 3: 解決策 (4 cards)
parts.append('<div class="stb amber"><i class="fa-solid fa-lightbulb"></i> OpenAIが提唱する解決策</div><div class="stl">')

parts.append(card('clipboard-check','var(--c3)','beat-fade','組織Readinessの評価','clipboard-check',[
    li('stethoscope','','導入前に組織の<span class="hl">AI受け入れ準備度</span>を診断'),
    li('map','a','現状の<span class="kt">組織成熟度</span>を客観的に測定'),
    li('bullseye','','どこに<span class="hl">最も手を入れるべきか</span>を優先順位付け'),
    li('chart-line','','定期的な<span class="kt">評価サイクル</span>で進捗を管理'),
],'<i class="fa-solid fa-stethoscope fa-lg" style="color:var(--c3)"></i> 診断してから<br><span class="hl">治療</span>しないとね🏥','1','amber-a'))

parts.append(card('chalkboard-user','var(--c2)','bounce','マネージャー教育','chalkboard-user',[
    li('user-tie','','直接の上司にAI活用の<span class="hl">ロールモデル</span>としての役割を担わせる'),
    li('person-chalkboard','a','マネージャー自身が<span class="kt">日常的にAIを使う</span>文化を創出'),
    li('people-group','','部門ごとに<span class="kt">AI活用方針</span>を策定させる'),
    li('star','a','<span class="hl">Manager Support</span>が<span class="kt">最大の成功要因</span>と明言'),
],'<i class="fa-solid fa-user-tie fa-lg" style="color:var(--c2)"></i> 上司が先陣を切る！<br><span class="hl">見せるリーダーシップ</span>が鍵👔'))

parts.append(card('shield-halved','var(--c2)','flip','セキュリティ・ガバナンス構築','shield-halved',[
    li('lock','r','構造化された<span class="hl">セキュリティアーキテクチャ</span>の設計'),
    li('file-shield','','<span class="kt">データ分類</span>と<span class="kt">アクセス制御</span>の仕組み'),
    li('gavel','','AI利用の<span class="kt">ガバナンスポリシー</span>策定'),
    li('plug','a','SaaS連携時の<span class="kt r">セキュリティ監査</span>を徹底'),
    li('shield','g','従業員が<span class="hl">安心して使える環境</span>の構築'),
],'<i class="fa-solid fa-shield fa-lg" style="color:var(--c2)"></i> 安心して使えるから<br><span class="hl">広まる</span>んだね🛡️'))

parts.append(card('laptop-code','var(--c3)','bounce','従業員トレーニング','laptop-code',[
    li('graduation-cap','a','AI<span class="kt">スキル教育プログラム</span>の実装'),
    li('pen-fancy','','<span class="hl">プロンプト作成</span>・<span class="kt">出力改善</span>・<span class="kt">タスク分割</span>を体系的に教える'),
    li('repeat','','反復練習で<span class="kt">スキルを定着</span>させる仕組み'),
    li('trophy','g','<span class="hl">成果を可視化</span>してモチベーションを維持'),
    li('comments','','<span class="kt">ピアラーニング</span>で組織内の知識共有を促進'),
],'<i class="fa-solid fa-chalkboard fa-lg" style="color:var(--c3)"></i> 教えるから<span class="hl">使える</span>！<br>スキル投資はコスパ最強📚','1','amber-a'))

parts.append('</div>')

# Section 4: 成功する企業の共通点 (2 cards)
parts.append('<div class="stb emerald"><i class="fa-solid fa-trophy"></i> 成功する企業の共通点</div><div class="stl">')

parts.append(card('handshake','