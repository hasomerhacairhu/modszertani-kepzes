#!/usr/bin/env python3
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
