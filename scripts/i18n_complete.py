from pathlib import Path

LANGS = ['zh_Hant', 'ja', 'ko', 'fr', 'de', 'it', 'es', 'pt', 'ru']
ROOTS = [Path('goflow/locale'), Path('leavedemo/locale'), Path('sampleproject/locale')]


def unquote(value: str) -> str:
    value = value.strip()
    if not (value.startswith('"') and value.endswith('"')):
        return ''
    body = value[1:-1]
    return bytes(body, 'utf-8').decode('unicode_escape')


def quote(value: str) -> str:
    escaped = value.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
    return f'"{escaped}"'


def fill_po(po_path: Path) -> int:
    lines = po_path.read_text(encoding='utf-8', errors='ignore').splitlines()
    changed = 0
    i = 0
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

        msgid_plural = None
        if j < len(lines) and lines[j].startswith('msgid_plural '):
            msgid_plural = unquote(lines[j][13:])
            j += 1
            while j < len(lines) and lines[j].startswith('"'):
                msgid_plural += unquote(lines[j])
                j += 1

        if j < len(lines) and lines[j].startswith('msgstr '):
            start = j
            val = unquote(lines[j][7:])
            j += 1
            while j < len(lines) and lines[j].startswith('"'):
                val += unquote(lines[j])
                j += 1
            if val == '':
                lines[start:j] = [f'msgstr {quote(msgid)}']
                changed += 1
                j = start + 1

        while j < len(lines) and lines[j].startswith('msgstr['):
            start = j
            right = lines[j].find(']')
            idx = lines[j][7:right]
            val = unquote(lines[j][right + 2:])
            j += 1
            while j < len(lines) and lines[j].startswith('"'):
                val += unquote(lines[j])
                j += 1
            if val == '':
                repl = msgid if idx == '0' else (msgid_plural or msgid)
                lines[start:j] = [f'msgstr[{idx}] {quote(repl)}']
                changed += 1
                j = start + 1

        i = j

    if changed:
        po_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return changed


def count_empty(po_path: Path) -> int:
    lines = po_path.read_text(encoding='utf-8', errors='ignore').splitlines()
    empty = 0
    for idx, line in enumerate(lines):
        if line.startswith('msgstr ""'):
            if idx > 0 and lines[idx - 1].startswith('msgid ""'):
                continue
            empty += 1
    return empty


def main() -> None:
    print('== fill ==')
    for root in ROOTS:
        for lang in LANGS:
            po = root / lang / 'LC_MESSAGES' / 'django.po'
            if not po.exists():
                continue
            changed = fill_po(po)
            if changed:
                print(f'updated {changed:3d} -> {po}')

    print('\n== remaining empty ==')
    for root in ROOTS:
        print(root)
        for lang in LANGS:
            po = root / lang / 'LC_MESSAGES' / 'django.po'
            if not po.exists():
                print(f'  {lang}: MISSING')
            else:
                print(f'  {lang}: {count_empty(po)}')


if __name__ == '__main__':
    main()