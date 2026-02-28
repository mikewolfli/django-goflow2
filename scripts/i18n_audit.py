from pathlib import Path

LANGS = ['zh_Hant', 'ja', 'ko', 'fr', 'de', 'it', 'es', 'pt', 'ru']
BASE_DIR = Path(__file__).resolve().parents[1]
ROOTS = [BASE_DIR / 'goflow/locale', BASE_DIR / 'leavedemo/locale', BASE_DIR / 'sampleproject/locale']


def parse_po(path: Path):
    lines = path.read_text(encoding='utf-8', errors='ignore').splitlines()
    i = 0
    total = 0
    empty = 0
    same = 0
    non_ascii = 0
    while i < len(lines):
        if lines[i].startswith('msgid ""'):
            i += 1
            continue
        if not lines[i].startswith('msgid '):
            i += 1
            continue

        msgid = lines[i][7:-1] if lines[i].endswith('"') else ''
        j = i + 1
        while j < len(lines) and lines[j].startswith('"'):
            msgid += lines[j][1:-1]
            j += 1

        if j < len(lines) and lines[j].startswith('msgstr '):
            msgstr = lines[j][8:-1] if lines[j].endswith('"') else ''
            k = j + 1
            while k < len(lines) and lines[k].startswith('"'):
                msgstr += lines[k][1:-1]
                k += 1
            total += 1
            if msgstr == '':
                empty += 1
            if msgstr == msgid:
                same += 1
            if any(ord(ch) > 127 for ch in msgstr):
                non_ascii += 1
            i = k
        else:
            i = j
    return total, empty, same, non_ascii


def main():
    for root in ROOTS:
        print('\n' + str(root.relative_to(BASE_DIR)))
        for lang in LANGS:
            po = root / lang / 'LC_MESSAGES' / 'django.po'
            if not po.exists():
                continue
            total, empty, same, non_ascii = parse_po(po)
            print(f'{lang}: total={total} empty={empty} same_as_msgid={same} non_ascii={non_ascii}')


if __name__ == '__main__':
    main()