#!/usr/bin/env python3
"""news_id=9150004 (PIVOT マネースキルセット: 日経平均冷静に分析) の infographic_url / tags / title / summary / url / video_id をPUTで更新"""
import json
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 9150004

payload = {
    "title": "【日経平均 積立のベストは1月〜6月】AI・半導体株は来年も好調？／過激な予想に振り回されるな／アドバンテスト、東京エレク、フジクラの今後／積立より一括投資？／ハセン＆りんたろー【マネースキルセット】",
    "summary": "PIVOT公式チャンネル「マネースキルセット」で、ニッセイ基礎研究所 研究理事・チーフ株式ストラテジストの井出真吾氏が日経平均の冷静な分析方法を解説。年初5万円台だった日経平均は6月に7万2,000円付近まで急上昇したが、日本企業の純利益は今年26%増・来年も10.8%増の2年連続2桁増益見通しで、バブルではなく業績の裏付けのある上昇と分析。井出氏愛用の「身の丈グラフ」ではPER14〜16倍を適正水準とし、現在はストライクゾーン上限の6万9,500円付近、リスクイベントで6万円まで下がれば割安と評価。1989年バブル（3万8,915円・実力の4倍）とは構造が違い、2012年に身の丈回帰後は基本上昇トレンドで、2030年ごろに日経平均10万円との展望。積立投資と一括投資の比較では、過去20数年の検証でS&P500は勝率6〜7割で1月一括投資が毎月積立を上回り、井出氏自身は年間の投資予定額を1月〜6月の前半で投入し急落用の余資金を確保する戦略を実践。金利面では日本の長期金利が3%超となり配当利回り約2%の日経平均との比較で株から国債への乗り換えも出始めたが、金利上昇には景気正常化の「良い金利上昇」と財政懸念（2040年度までに370兆円投資の骨太方針）の「悪い金利上昇」が混在すると分析。AI関連では、学習フェーズ（GPU・NVIDIA、検査装置のアドバンテスト）→推論（メモリー）→データセンター（村田製作所MLCC、電力用電線・光ファイバーのフジクラ）→AIエージェント／フィジカルAIとフェーズが変わるごとに日本企業が入り込み、世界シェア7〜8割の企業も多い。日本企業の純利益で自動車産業と半導体産業が今年初めて逆転しそうなこと、「AIバブル」論は2020年ガーファム時代の歪み論の繰り返しで井出氏が過去の自説を6年後に誤りと認めた事実、NVIDIAの2つのリスク（同業他社・GPU不要の中国AI）はいずれも実現しづらいとの見解も解説。来年の日経平均予想は7万5,000円（場合によって7万7,800円）、1年後には7万円台・1ドル160円台の定着を展望。投資と企業の応援は別物で、長期投資なら利益確定は不要、「基本ガチホ」と結論。",
    "infographic_url": "docs/20261102_pivot_money_skillset_nikkei_cool_analysis.html",
    "url": "https://www.youtube.com/watch?v=rono_lB9Fik",
    "video_id": "rono_lB9Fik",
    "tags": "PIVOT,マネースキルセット,日経平均,積立投資,一括投資,NISA,井出真吾,ニッセイ基礎研究所,PER,AIバブル,NVIDIA,アドバンテスト,フジクラ,村田製作所,インフレ,金利,投資,Infographic",
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
print('GET video_id:', item.get('video_id'))
