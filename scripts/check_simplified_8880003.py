#!/usr/bin/env python3
"""簡体字中国語・機密情報チェック (8880003 / 1DmznuvBVFU)"""
import re
import sys


def _cp932_fail(ch: str) -> bool:
    try:
        ch.encode('cp932')
        return False
    except UnicodeEncodeError:
        return True


PATHS = [
    'docs/20261030_grok_bot_ai_team_keito.html',
    'scripts/update_grok_bot_ai_team_8880003.py',
]

secret_pat = re.compile(
    r'(sk-[A-Za-z0-9]{10,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_\-]{20,}|'
    r'ghp_[A-Za-z0-9]{20,}|gho_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|'
    r'Bearer\s+[A-Za-z0-9._\-]{20,}|-----BEGIN)'
)

fail = False
for p in PATHS:
    try:
        text = open(p, encoding='utf-8').read()
    except FileNotFoundError:
        continue
    bad = sorted({ch for ch in text if '\u4e00' <= ch <= '\u9fff' and _cp932_fail(ch)})
    if bad:
        fail = True
        print(f'[{p}] 簡体字(疑い)検出: {bad}')
    else:
        print(f'[{p}] 簡体字: なし')
    m = secret_pat.findall(text)
    if m:
        fail = True
        print(f'[{p}] 機密情報検出: {m[:5]}')
    else:
        print(f'[{p}] 機密情報: なし')

sys.exit(1 if fail else 0)
