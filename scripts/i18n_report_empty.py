from pathlib import Path

LANGS = ['zh_Hant', 'ja', 'ko', 'fr', 'de', 'it', 'es', 'pt', 'ru']
ROOT = Path('goflow/locale')


def unquote(value: str) -> str:
    value = value.strip()
    if not (value.startswith('"') and value.endswith('"')):
        return ''
    body = value[1:-1]
    return bytes(body, 'utf-8').decode('unicode_escape')


def report(po_path: Path):
    lines = po_path.read_text(encoding='utf-8', errors='ignore').splitlines()
    i = 0
    result = []
    while i < len(lines):
        if lines[i].startswith('msgid ""'):
            i += 1
            continue
        if not lines[i].startswith('msgid '):
            i += 1
            continue
        msgid = unquote(lines[i][6:])
        j = i + 1
        while j < len(lines) and lines[j].startswith('"'):
            msgid += unquote(lines[j])
            j += 1
        if j < len(lines) and lines[j].startswith('msgstr ""'):
            result.append(msgid)
        i = j
    return result


for lang in LANGS:
    po = ROOT / lang / 'LC_MESSAGES' / 'django.po'
    if not po.exists():
        continue
    empties = report(po)
    print(f'\n{lang}: {len(empties)}')
    for item in empties:
        print(' -', item)