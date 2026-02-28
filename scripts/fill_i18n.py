import re
from pathlib import Path

source_files = [
    'goflow/workflow/views.py',
    'goflow/workflow/templates/goflow/workflow_designer.html',
    'goflow/runtime/templates/goflow/monitor.html',
    'goflow/runtime/templates/goflow/sample_task_form.html',
]

msgids = set()
for fp in source_files:
    text = Path(fp).read_text(encoding='utf-8')
    msgids.update(re.findall(r"gettext\('([^']+)'\)", text))
    msgids.update(re.findall(r'\{\%\s*trans\s+"([^"]+)"\s*\%\}', text))

langs = ['zh_Hant', 'ja', 'ko', 'fr', 'de', 'it', 'es', 'pt', 'ru']
locale_roots = [Path('goflow/locale'), Path('leavedemo/locale'), Path('sampleproject/locale')]

def esc(value: str) -> str:
    return value.replace('\\', '\\\\').replace('"', '\\"')

def fill_po(po_path: Path, keys):
    lines = po_path.read_text(encoding='utf-8').splitlines(keepends=True)
    changed = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('msgid "') and line.rstrip().endswith('"'):
            msgid = line[len('msgid "'):-2]
            if msgid in keys:
                j = i + 1
                while j < len(lines) and not lines[j].startswith('msgstr '):
                    if lines[j].startswith('msgid_plural'):
                        break
                    j += 1
                if j < len(lines) and lines[j].startswith('msgstr "'):
                    current = lines[j][len('msgstr "'):-2]
                    k = j + 1
                    while k < len(lines) and lines[k].startswith('"'):
                        k += 1
                    if current == '':
                        lines[j:k] = [f'msgstr "{esc(msgid)}"\n']
                        changed += 1
                        i = j
        i += 1

    if changed:
        po_path.write_text(''.join(lines), encoding='utf-8')
    return changed

for root in locale_roots:
    for lang in langs:
        po = root / lang / 'LC_MESSAGES' / 'django.po'
        if po.exists():
            count = fill_po(po, msgids)
            if count:
                print(f'updated {count:3d} -> {po}')

print('done')
