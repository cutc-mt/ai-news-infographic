#!/usr/bin/env python3
"""news_id=8070005 (PIVOT: 現場データが経営に届かない問題をAIでつなぐ) の
infographic_url / tags / summary を PUT で更新し、GET で反映を確認する。"""
import json
import sys
import urllib.error
import urllib.request

BASE = 'https://ai-news-api-1071356095208.asia-northeast1.run.app/api/news'
NEWS_ID = 8070005

payload = {
    'title': '【現場が見えずに経営するリスク】現場のデータが経営に届かない／現場と経営の分断をAIでつなぐ／データから「事故の予兆」をつかむ',
    'summary': (
        'PIVOTの企業インタビュー番組 &SESSION（カミナシ提供）。'
        'カミナシの諸岡遼平代表（機内食工場の後継ぎとして5年間現場勤務後に起業）と、'
        'キリングループロジスティックスの松本哲執行役員（約50拠点・1日3,000台以上を管理）が、'
        '「経営と現場の分断」を実例とともに解き明かす。'
        '現場の情報は紙の中に留まり、悪い情報ほど1週間〜1ヶ月後に判明。'
        '紙からエクセルへの転記に1日の1〜2割を使う現場もあり、「暗闇の中で経営しているようなもの」という声もある。'
        'AIは作業記録の代行はできず「データが集まった後」に輝くが、'
        'ベテランの音声指導の文字起こしからの記録・マニュアル化は既に実用域。'
        'カミナシはレポート・生産実績・設備保全・従業員・教育・カミナシIDの6製品で現場データを収集し、'
        'ERPの経営データや安全データと統合した「現場統合データベース」を構築。'
        'クレンジングとエンリッチメントを経てBI分析・AI自動化に繋げる。'
        'キリン物流では物流DX推進部（前年4月発足）のヒアリングを起点に4拠点でPOCを実施し、'
        '10年以上の事故・ヒヤリハットデータと「気づき」を横断比較して事故の予兆を掴む取り組みを進める。'
        '現場訪問年間3,900回・5〜10分でアプリ改変・継続率99%超の「現場ドリブン」文化や、'
        '共有アカウント問題を解く1人1ID構想、生産数の「100%」が実測90%だった製造業の事例まで。'
        '10月21日には「現場から日本を変え、産業を変える」現場オペレーションハブ構想を発表。'
        '結論: 現場で見えていないことは非効率だけでなく重大なリスク。'
        '記録は人・分析と整形はAIという役割分担で、現場起点の経営を実現する。'
    ),
    'tags': 'カミナシ,キリングループロジスティックス,PIVOT,現場DX,物流DX,カミナシID,ヒヤリハット,事故の予兆,データ統合,現場オペレーションハブ',
    'infographic_url': 'docs/20261021_pivot_kaminashi_field_data_ai.html',
}


def main() -> int:
    url = f'{BASE}/{NEWS_ID}'
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        method='PUT',
        headers={'Content-Type': 'application/json'},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = json.loads(r.read().decode())
            print(f'PUT HTTP {r.status}')
            print(f"  title: {body.get('title', '')}")
            print(f"  tags: {body.get('tags', '')}")
            print(f"  infographic_url: {body.get('infographic_url', '')}")
    except urllib.error.HTTPError as e:
        print(f'PUT HTTPError {e.code}: {e.read().decode("utf-8")[:400]}')
        return 1

    # 反映確認
    with urllib.request.urlopen(url, timeout=30) as r:
        got = json.loads(r.read().decode())
    ok = (
        got.get('infographic_url') == payload['infographic_url']
        and got.get('tags') == payload['tags']
    )
    print(f"GET  infographic_url={got.get('infographic_url')} tags={got.get('tags')}")
    print('VERIFY ' + ('OK' if ok else 'NG'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
