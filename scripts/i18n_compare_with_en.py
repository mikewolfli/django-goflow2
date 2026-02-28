from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
TARGET_LANGS = ["zh_Hant", "ja", "ko", "fr", "de", "it", "es", "pt", "ru"]


def parse_po_entries(po_path: Path):
    lines = po_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    entries = []
    i = 0

    def parse_quoted(value: str) -> str:
        value = value.strip()
        if not (value.startswith('"') and value.endswith('"')):
            return ""
        return value[1:-1]

    while i < len(lines):
        line = lines[i]

        if not line.startswith("msgid "):
            i += 1
            continue

        if line.startswith('msgid ""'):
            i += 1
            while i < len(lines) and lines[i].startswith('"'):
                i += 1
            continue

        msgid = parse_quoted(line[6:])
        i += 1
        while i < len(lines) and lines[i].startswith('"'):
            msgid += parse_quoted(lines[i])
            i += 1

        msgstr_values = []

        if i < len(lines) and lines[i].startswith("msgid_plural "):
            i += 1
            while i < len(lines) and lines[i].startswith('"'):
                i += 1

        if i < len(lines) and lines[i].startswith("msgstr "):
            value = parse_quoted(lines[i][7:])
            i += 1
            while i < len(lines) and lines[i].startswith('"'):
                value += parse_quoted(lines[i])
                i += 1
            msgstr_values.append(value)

        while i < len(lines) and lines[i].startswith("msgstr["):
            right = lines[i].find("]")
            value = parse_quoted(lines[i][right + 2 :])
            i += 1
            while i < len(lines) and lines[i].startswith('"'):
                value += parse_quoted(lines[i])
                i += 1
            msgstr_values.append(value)

        entries.append({"msgid": msgid, "msgstr_values": msgstr_values})

    return entries


def check_against_en(root_relative: str):
    root = BASE_DIR / root_relative
    en_po = root / "en" / "LC_MESSAGES" / "django.po"
    if not en_po.exists():
        return []

    en_entries = parse_po_entries(en_po)
    en_msgids = [entry["msgid"] for entry in en_entries if entry["msgid"]]
    used_fallback = False

    if not en_msgids:
        reference_lang = None
        reference_msgids = []
        for lang in TARGET_LANGS:
            lang_po = root / lang / "LC_MESSAGES" / "django.po"
            if not lang_po.exists():
                continue
            lang_entries = parse_po_entries(lang_po)
            msgids = [entry["msgid"] for entry in lang_entries if entry["msgid"]]
            if len(msgids) > len(reference_msgids):
                reference_msgids = msgids
                reference_lang = lang
        en_msgids = reference_msgids
        used_fallback = True
    en_msgid_set = set(en_msgids)
    results = []

    for lang in TARGET_LANGS:
        lang_po = root / lang / "LC_MESSAGES" / "django.po"
        if not lang_po.exists():
            results.append(
                {
                    "lang": lang,
                    "missing_file": True,
                    "missing_msgids": en_msgids,
                    "empty_msgids": [],
                }
            )
            continue

        lang_entries = parse_po_entries(lang_po)
        lang_map = {entry["msgid"]: entry["msgstr_values"] for entry in lang_entries if entry["msgid"]}
        lang_msgid_set = set(lang_map.keys())

        missing_msgids = [msgid for msgid in en_msgids if msgid not in lang_msgid_set]
        empty_msgids = []
        for msgid in en_msgids:
            if msgid not in lang_map:
                continue
            values = lang_map[msgid]
            if not values or all(value == "" for value in values):
                empty_msgids.append(msgid)

        extra_msgids = sorted(lang_msgid_set - en_msgid_set)
        results.append(
            {
                "lang": lang,
                "missing_file": False,
                "missing_msgids": missing_msgids,
                "empty_msgids": empty_msgids,
                "extra_msgids": extra_msgids,
            }
        )

    return results, used_fallback


def check_without_en(root_relative: str):
    root = BASE_DIR / root_relative
    results = []
    for lang in TARGET_LANGS:
        lang_po = root / lang / "LC_MESSAGES" / "django.po"
        if not lang_po.exists():
            results.append({"lang": lang, "missing_file": True, "empty_msgids": []})
            continue
        entries = parse_po_entries(lang_po)
        empty_msgids = []
        for entry in entries:
            if not entry["msgid"]:
                continue
            values = entry["msgstr_values"]
            if not values or all(value == "" for value in values):
                empty_msgids.append(entry["msgid"])
        results.append({"lang": lang, "missing_file": False, "empty_msgids": empty_msgids})
    return results


def print_block(title: str):
    print("\n" + title)
    print("-" * len(title))


def main():
    print_block("leavedemo: compare with en")
    leavedemo_results, leavedemo_fallback = check_against_en("leavedemo/locale")
    if leavedemo_fallback:
        print("NOTE: en django.po has no entries; fallback baseline = language file with most msgids.")
    for item in leavedemo_results:
        if item["missing_file"]:
            print(f"{item['lang']}: MISSING FILE")
            continue
        print(
            f"{item['lang']}: empty={len(item['empty_msgids'])} missing={len(item['missing_msgids'])} extra={len(item['extra_msgids'])}"
        )
        for msgid in item["empty_msgids"]:
            print(f"  EMPTY -> {msgid}")
        for msgid in item["missing_msgids"]:
            print(f"  MISSING -> {msgid}")

    print_block("sampleproject: compare with en")
    sample_results, sample_fallback = check_against_en("sampleproject/locale")
    if sample_fallback:
        print("NOTE: en django.po has no entries; fallback baseline = language file with most msgids.")
    for item in sample_results:
        if item["missing_file"]:
            print(f"{item['lang']}: MISSING FILE")
            continue
        print(
            f"{item['lang']}: empty={len(item['empty_msgids'])} missing={len(item['missing_msgids'])} extra={len(item['extra_msgids'])}"
        )
        for msgid in item["empty_msgids"]:
            print(f"  EMPTY -> {msgid}")
        for msgid in item["missing_msgids"]:
            print(f"  MISSING -> {msgid}")

    print_block("goflow: per-entry empty check (no en file)")
    for item in check_without_en("goflow/locale"):
        if item["missing_file"]:
            print(f"{item['lang']}: MISSING FILE")
            continue
        print(f"{item['lang']}: empty={len(item['empty_msgids'])}")
        for msgid in item["empty_msgids"]:
            print(f"  EMPTY -> {msgid}")


if __name__ == "__main__":
    main()