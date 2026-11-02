#!/usr/bin/env python3
"""news_id=9150005 (PIVOT: 経済安全保障・米中AI覇権) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 9150005

payload = {
    "title": "【米国一辺倒のリスク】日米同盟を大前提とした生存戦略／安全をお金で買う時代？自国生産の経済的負担／米中AI覇権争いとサイバー空間の脅威／サプライチェーン再編のリアル／直近の注目は米中間選挙",
    "summary": "PIVOT公式チャンネルが経済安全保障論の専門家を迎え、経済安全保障の脅威とリスクを解説。モノ・ヒト・カネ・情報の相互依存が深まるグローバリゼーションにおいて、繋がりがもたらす利益だけでなくリスクを管理する時代に入ったと指摘する。概念の原点は1970年代の第四次中東戦争に伴うオイルショック（石油禁輸）であり、日本では大平政権の総合安全保障戦略（1980年頃）が現在の経済安全保障政策の出発点となった。安全保障の対象は軍事的脅威から経済的手段による圧力へ拡大し、防衛装備の供給依存を通じて軍事安保と経済安保は直結している。サイバー攻撃では、システム脆弱性を高度に発見できるAIが攻撃・防御の両面のツールとなり、先端AIが米中に集中する限り依存国は外国の規制リスクに晒される。Anthropicの先端モデル「ミトス」「フェイブル」リリース時には米政府の輸出管理で外国人アクセスが禁止され、同盟国であっても供給を一方的にコントロールされうる事例となった。日本は日米同盟と米軍との相互運用性を大前提にパランティア等の米製AIをリスク軽減しつつ活用し、AI主権喪失を避けるため国産AI開発も進める二軸戦略。欧州は逆に米AI排除とEU全体でのデジタル主権回復へ動き、独軍・仏軍は自国系AI企業への切り替えを進める。ウクライナでは実戦データのフィードバックで兵器開発サイクルが桁違いに高速化している。経済的手段で他国に圧力をかけるエコノミック・ステイトクラフトは経済安全保障の裏返しであり、巨大市場を持つ米中の関税（トランプ関税）や禁輸がその典型で、WTO中心の国際ルールは軽視化。ミドルパワーと中小国にとってルールで動く世界は生存条件となる。サプライチェーン再編はフレンドショアリングとリショアリングが基本だが「安全をお金で買う」コストがかかり、経済合理性が低下してもやる合意を国と企業のどこまで作れるかが問われる。大企業は経済安保担当役員の設置やリスク管理を進める一方、中小企業はリソース不足で官民協力と政策的補助が必要。今後5年の直近の焦点は11月3日の米中間選挙とその後のトランプ外交、次期米政権の対中政策であり、米中対立由来のリスクとそれ以外の個別リスクを区別して見極めることが日本の生存戦略となる。",
    "infographic_url": "docs/20261102_pivot_keizai_anzenhosho_senryaku.html",
    "url": "https://www.youtube.com/watch?v=fLjBTjkaTwA",
    "video_id": "fLjBTjkaTwA",
    "tags": "PIVOT,経済安全保障,米中対立,AI覇権,サイバーセキュリティ,エコノミックステイトクラフト,フレンドショアリング,リショアリング,サプライチェーン,パランティア,国産AI,ミドルパワー,WTO,トランプ関税,米中間選挙,日米同盟,総合安全保障,オイルショック,Infographic",
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
