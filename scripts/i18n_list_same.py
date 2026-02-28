from pathlib import Path

LANGS = ['zh_Hant', 'ja', 'ko', 'fr', 'de', 'it', 'es', 'pt', 'ru']
BASE = Path(__file__).resolve().parents[1] / 'goflow' / 'locale'


def parse_same(path: Path):
    lines = path.read_text(encoding='utf-8', errors='ignore').splitlines()
    i = 0
    same = []
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
            if msgid and msgstr and msgid == msgstr:
                same.append(msgid)
            i = k
        else:
            i = j
    return same


def main():
    for lang in LANGS:
        po = BASE / lang / 'LC_MESSAGES' / 'django.po'
        same = parse_same(po)
        print(f'\n{lang}: {len(same)}')
        for text in same:
            print('-', text)


if __name__ == '__main__':
    main()
