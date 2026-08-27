#!/usr/bin/env python3
# ==========================================================================
# NYUGDÍJAZOTT — NE FUTTASD.
#
# Ez a fájl a média-asset regiszter v1 (2026-06) pipeline-jának része. A kánoni
# rendszer 2026-08 óta a `tools/media_manifest.py` fordító, amely a jelenlegi
# Markdown `@asset` / `@source` deklarációiból építi a regisztert.
#
# Miért maradt itt: forenzikus bizonyíték. A `media-merged.json` befagyasztott
# leltára a 747 történeti sor egyeztetésének bemenete (`media_manifest.py
# reconcile`), a szkriptek pedig azt dokumentálják, hogyan készült.
#
# Amit NEM szabad: lefuttatni. A `build-data.py` és a `format-media.js` a v2
# generált kimeneteire írna rá a befagyasztott JSON-ból, azaz visszaállítaná a
# 2026-06-os pillanatképet a jelenlegi tananyagszöveg helyett.
# ==========================================================================

# A verbatim-workflow outputját beolvassa és hozzáadja a merged.json assetjeihez.
import json, os, sys
TERV = "/Users/heymarcell/DEV/modszertani-kepzes/02 Tervezet"
MJ = os.path.join(TERV, "Média-assetek/_build/media-merged.json")
OUT = sys.argv[1]

raw = json.load(open(OUT, encoding="utf-8"))
if isinstance(raw.get("result"), str):
    try: raw = json.loads(raw["result"])
    except: pass
if isinstance(raw.get("result"), dict): raw = raw["result"]
verb = raw.get("verbatim", {})

d = json.load(open(MJ, encoding="utf-8"))
filled = 0
for a in d["assets"]:
    t = verb.get(a["assetId"], "")
    a["verbatim"] = t
    if t.strip(): filled += 1
json.dump(d, open(MJ, "w", encoding="utf-8"), ensure_ascii=False)

TEXT_TYPES = {"narráció", "felirat", "leirat-transzkript", "alt-szöveg", "egyéb"}
expected = sum(1 for a in d["assets"] if a.get("assetType") in TEXT_TYPES)
print(f"verbatim beírva: {filled} asset / {expected} szöveg-asset")
# minta
for a in d["assets"]:
    if a["assetType"] == "narráció" and a.get("verbatim", "").strip():
        print("minta narráció:", a["assetId"])
        print("  ", a["verbatim"][:160].replace("\n", " ⏎ "))
        break
