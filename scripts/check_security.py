#!/usr/bin/env python3
"""
HTMLファイルのセキュリティスキャン + 簡体字（簡体中文）チェック。

使い方:
    /usr/bin/python3 scripts/check_security.py docs/20260914_xxx.html

出口コード:
    0 = 問題なし
    1 = シークレット検出（push禁止）
    2 = 簡体字検出（要修正）
"""
import re
import sys

# --- シークレットっぽいパターン ---
SECRET_PATTERNS = [
    (r'sk-[A-Za-z0-9_\-]{20,}', 'OpenAI風APIキー'),
    (r'AIza[0-9A-Za-z_\-]{35}', 'Google APIキー'),
    (r'ghp_[A-Za-z0-9]{36}', 'GitHub PAT'),
    (r'github_pat_[A-Za-z0-9_]{22,}', 'GitHub fine-grained PAT'),
    (r'-----BEGIN [A-Z ]*PRIVATE KEY', '秘密鍵'),
    (r'xox[baprs]-[A-Za-z0-9\-]{10,}', 'Slackトークン'),
    (r'AKIA[0-9A-Z]{16}', 'AWSアクセスキー'),
    (r'ya29\.[0-9A-Za-z_\-]{30,}', 'Google OAuthトークン'),
]

# --- 日本語テキストに出てこない簡体字のみ（誤検知調査済み 2026-09-14） ---
# 日本語常用漢字と字形が同一のもの（数・体・内・声・当・断・担・残・条・写・旧・医・欲・
# 寝・区・湾・属・双・据・欧・宝・机・尽・寿・炉・浅・恋・恒・壮・叶・灯・径・惨・枢・叙・弯）
# は除外済み。日本語の字体（時→时、話→话、創→创 など）と異なる簡体字のみ検出する。
SIMPLIFIED_CHARS = set(
    '们说话语读让这时间东车贝见证长张线结绕给终统经绝继绩现观规视览觉'
    '证评词议记讯谢认训译访报增处备复亚产亲亿仅从仪价众优伞伟传伤'
    '侠侣侧侨倾偿儿兑兰关兴养兽冈册军农冯冲决况冻净凉减凑凤凭凯击划刘则'
    '刚创删别剧剩劝办务劲劳势勋华协单厂厅历厉压厌变爱发叠吓吕吗'
    '启听员呜咏响哑哗唤啰啸喷喽团园围图圆圣场块坚坛坝坟坏垄垒垦垫执扩扫扬'
    '扰抚抛抟抠抡抢护拟拢拣拥择挂挡挤挥捞损换捣捡摆摇摊敌敛斋斗无'
    '旷显晓晕暂术杀杂权杨构柜柠栅标栈栋栌栎栏树样栾桠桡桢档桩梦检'
    '棂椟椤椭楼榄槛槠欢欤殇殒殓殚殡毁毂毕毙氢氩汇汉汤汹沟沥沦沧沫'
    '浑浓济涨涩渍渐渔渊渗溃滚满滨滩潇澜灭灿炼炜烁热焕焊狈狱狲狮'
    '壳壶够夹夺奋奖妆妇妈婴嫒孙宁实宠审宪宫宽宾寻导尔尘尝层屉'
    '屡屿岁岂岖岗岚岛岭崭币帅师帐帘帜带帧帼幂并广庄庆库应庞废开异弃'
    '归录彻忆忧怀态怂怅怜总怼恳恶恸恺恻恼悬悯惊惧惩惫惬惭惮惯'
    '愠愤愦愿慑懒户扑'
)


def main():
    if len(sys.argv) < 2:
        print('usage: check_security.py <file> [file...]', file=sys.stderr)
        sys.exit(3)

    exit_code = 0
    for path in sys.argv[1:]:
        with open(path, encoding='utf-8') as f:
            content = f.read()

        # 1) シークレットスキャン
        for pattern, label in SECRET_PATTERNS:
            m = re.search(pattern, content)
            if m:
                line_no = content[:m.start()].count('\n') + 1
                print(f'🚨 SECRET [{path}:{line_no}] {label}: {m.group(0)[:20]}...')
                exit_code = max(exit_code, 1)

        # 2) 簡体字チェック（タグ・URL・コード部分を除外したテキストのみ）
        text_only = re.sub(r'<script.*?</script>|<style.*?</style>', '', content,
                           flags=re.DOTALL)
        text_only = re.sub(r'<[^>]+>', '', text_only)
        text_only = re.sub(r'https?://[^\s<>"\']+', '', text_only)
        found = sorted({ch for ch in text_only if ch in SIMPLIFIED_CHARS})
        if found:
            print(f'🀄 簡体字検出 [{path}]: {"".join(found)}')
            exit_code = max(exit_code, 2)

    if exit_code == 0:
        print(f'✅ セキュリティスキャン・簡体字チェック合格 ({len(sys.argv)-1}ファイル)')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
