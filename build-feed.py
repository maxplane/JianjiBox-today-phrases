#!/usr/bin/env python3
"""Combine the four editorial files into the JianjiBox download."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOCALES = ("zh-Hans", "zh-Hant", "ja", "en")
fields = ("text", "author", "work", "source", "rights")
libraries = {}
for locale in LOCALES:
    entries = json.loads((ROOT / locale / "phrases.json").read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise SystemExit(f"{locale}: expected a nonempty list")
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or any(
            not isinstance(entry.get(key), str) or not entry[key].strip() for key in fields
        ):
            raise SystemExit(f"{locale}: incomplete entry")
        text = entry["text"]
        tags = entry.get("tags")
        if (len(text) > 72 or text in seen or not entry["source"].startswith("https://")
                or not isinstance(tags, list) or not tags
                or any(not isinstance(tag, str) or not tag for tag in tags)):
            raise SystemExit(f"{locale}: invalid or duplicate entry: {text!r}")
        seen.add(text)
    libraries[locale] = entries

sections = []
for locale, entries in libraries.items():
    rows = ",\n".join(
        "    " + json.dumps(entry, ensure_ascii=False, separators=(",", ":")) for entry in entries
    )
    sections.append(f'  "{locale}": [\n{rows}\n  ]')

data = ("{\n" + ",\n".join(sections) + "\n}\n").encode()
if len(data) > 512 * 1024:
    raise SystemExit("Feed exceeds the App’s 512 KiB limit")
(ROOT / "today-phrases.json").write_bytes(data)
