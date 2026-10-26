#!/usr/bin/python3
"""news_id=8520002 (PIVOT: 日経平均急落の今が買い) の infographic_url / tags / title / summary をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8520002

payload = {
    "title": "【日経平均 急落の今が買い】AIに奪われない会社／ソニーG・任天堂はまた上がる？／TOTOは隠れ半導体株／格差拡大で防犯需要が高まる／オルカンS&P500の盲点（マネースキルセット）",
    "summary": "PIVOT公式チャンネル「マネースキルセット」にファンドマネージャー・藤野英人さんを迎え、日経平均急落の局面を「買い」と捉える思考法を解説。AI関連銘柄をAIネイティブ（AI自体が成長エンジン＝Anthropic・OpenAI、日本ではキオクシアや東京エレクトロン等の関連株）／AIレジスタント（観光・体験・アニメ視聴・お笑いなどAIが発展しても価値が増す領域）／AIトランスフォーム（AIで既存業種を変える、全企業が対象）の3分類で仕分けるフレームワークを提示。10年前にAIに名人が負けた将棋が棋女子ブームで大復活した例など、AIと人間の共存事例も紹介。スペースXで従業員400人が100億円超の資産を得た話を「嫉妬・他人ごと・チャンス」の3択で問い、ハワイ島フォーシーズンズでAI・IPO・キャピタルゲインの話に花を咲かせる米国人の姿から、米国人旅行先トップ3常連の日本へ九州の超高級温泉ツアー等で富を取り込む発想へ。アニメ主要企業の時価総額が自動車主要企業を抜いた歴史的転換を受け、出遅れ中の任天堂・ソニーは仕込み時、オリエンタルランドはクルーズ（フォーシーズンズ・アマン・ジャパネットも参入）が次の材料。東映アニメーションとアジア勢（インドネシア「ジャンボ」、韓国「デーモンハンターズ」）の躍進、IPを歌・ゲーム・グッズに展開する人材不足で制作現場の交渉力が上昇中とも。格差拡大で犯罪が増えセコム・ALSOKの防犯需要が増え続ける一方、タンス預金100兆円が戦後初めて減少。TOTOは静電チャック（半導体製造装置用セラミック絶縁部材）で隠れ半導体株として急騰後調整し再び仕込み時。日経平均も実はAIの塊でTOPIXの方がよく、オルカン・S&P500一本は米国ベットのリスクがあるため日本株も一部持つべき。選択肢として日本小型株アクティブ、バリュー、未上場から上場後も持つクロスオーバー（藤野さん商品は500億円集めた）を挙げ、「株を買わない選択肢はない、まず証券口座を」と結ぶ。",
    "infographic_url": "docs/20261026_nikkei_buy_pivot.html",
    "tags": "PIVOT,マネースキルセット,日経平均,日本株,AI関連株,任天堂,ソニーグループ,オリエンタルランド,東映アニメーション,TOTO,セコム,ALSOK,キオクシア,東京エレクトロン,オルカン,S&P500,投資,Infographic",
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

# 検証: GET で反映確認
with urllib.request.urlopen(url, timeout=30) as r:
    data = json.loads(r.read().decode('utf-8'))
print('GET check:')
print('  title:', data.get('title', '')[:60])
print('  infographic_url:', data.get('infographic_url', ''))
print('  tags:', data.get('tags', ''))
