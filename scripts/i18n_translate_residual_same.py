from pathlib import Path

BASE = Path(__file__).resolve().parents[1] / 'goflow' / 'locale'

MAPPINGS = {
    'fr': {
        'normal': 'standard',
        'urgent': 'prioritaire',
        'Image': 'Illustration',
        'action': 'opération',
        'Workflows': 'Flux de travail',
        'Instances': 'Occurrences',
        'Total': 'Total général',
        'Action': 'Opération',
        'Urgent': 'Prioritaire',
        'Transitions': 'Transitions du flux',
        'Condition': 'Règle',
        'Canvas': 'Canevas',
    },
    'de': {
        'normal': 'Normal',
        'Filter': 'Filtern',
        'Workflows': 'Arbeitsabläufe',
        'Status': 'Zustand',
        'Start': 'Beginn',
        'Autostart': 'Automatischer Start',
        'Name': 'Bezeichnung',
    },
    'it': {
        'file': 'allegato',
        'Home': 'Pagina iniziale',
        'Canvas': 'Area di disegno',
    },
    'es': {
        'normal': 'Normal',
        'Total': 'Total general',
        'Actor': 'Responsable',
        'error': 'fallo',
    },
    'pt': {
        'normal': 'Normal',
        'Workflows': 'Fluxos de trabalho',
        'Total': 'Total geral',
        'Status': 'Estado',
        'Canvas': 'Área de desenho',
    },
    'ru': {
        'Workflows': 'Рабочие процессы',
    },
}


def replace_exact_block(text: str, source: str, target: str) -> tuple[str, int]:
    old = f'msgid "{source}"\nmsgstr "{source}"'
    new = f'msgid "{source}"\nmsgstr "{target}"'
    count = text.count(old)
    if count:
        text = text.replace(old, new)
    return text, count


def main():
    grand_total = 0
    for lang, entries in MAPPINGS.items():
        po = BASE / lang / 'LC_MESSAGES' / 'django.po'
        text = po.read_text(encoding='utf-8', errors='ignore')
        updated = 0
        for source, target in entries.items():
            text, count = replace_exact_block(text, source, target)
            updated += count
        po.write_text(text, encoding='utf-8')
        print(f'{lang}: {updated}')
        grand_total += updated
    print(f'total updated: {grand_total}')


if __name__ == '__main__':
    main()
