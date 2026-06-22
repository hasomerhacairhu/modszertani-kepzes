#!/usr/bin/env python3
# A merged.json-ból legenerál egy workflow-scriptet, ami fájlonként kinyeri a
# szó szerinti (verbatim) szöveget minden szöveg-hordozó assethez.
import json, os
TERV = "/Users/heymarcell/DEV/modszertani-kepzes/02 Tervezet"
MJ = os.path.join(TERV, "Média-assetek/_build/media-merged.json")
d = json.load(open(MJ, encoding="utf-8"))

TEXT_TYPES = {"narráció", "felirat", "leirat-transzkript", "alt-szöveg", "egyéb"}
filemap = {}
for a in d["assets"]:
    if a.get("assetType") in TEXT_TYPES:
        filemap.setdefault(a["file"], []).append({
            "id": a["assetId"], "type": a["assetType"],
            "loc": a.get("location", ""), "spec": (a.get("contentSpec", "") or "")[:120]
        })

n_files = len(filemap); n_items = sum(len(v) for v in filemap.values())
FILEMAP_JS = json.dumps(filemap, ensure_ascii=False)

script = '''export const meta = {
  name: 'verbatim-extract',
  description: 'Szó szerinti narráció/felirat/leirat szöveg kinyerése a forrásfájlokból a regiszterhez',
  phases: [{ title: 'Verbatim kinyerés' }],
}

const FILEMAP = ''' + FILEMAP_JS + '''
const ROOT = '02 Tervezet'

const SCHEMA = {
  type: 'object',
  required: ['items'],
  properties: {
    items: {
      type: 'array',
      items: {
        type: 'object',
        required: ['assetId', 'verbatim'],
        properties: {
          assetId: { type: 'string' },
          verbatim: { type: 'string', description: 'A SZÓ SZERINTI szöveg a forrásból; ne fogalmazd át. Ha tényleg nincs konkrét szöveg, üres string.' },
        },
      },
    },
  },
}

async function tryAgent(prompt, opts, tries = 4) {
  for (let i = 0; i < tries; i++) {
    const r = await agent(prompt, { ...opts, label: (opts.label || 'a') + (i ? `·r${i}` : '') })
    if (r) return r
  }
  return null
}

const files = Object.keys(FILEMAP)
const results = await parallel(files.map(f => async () => {
  const items = FILEMAP[f]
  const r = await tryAgent(
    `Egy magyar Hasomer Hacair madrich-képzés egy leckefájljából a SZÓ SZERINTI szövegeket kell kinyerned, hogy egy gyártási listába kerüljenek (szinkronhang felmondja / AI-narrátor generálja / felirat-leirat lesz belőle).

Fájl: ${ROOT}/${f}

Az alábbi asseteket kell kitöltened. MINDEGYIKHEZ add meg a forrásból a PONTOS, SZÓ SZERINTI szöveget (ne tömörítsd, ne fogalmazd át, ne told meg semmivel):
- "narráció": a felmondandó/narrálandó szöveg szó szerint (a "Mit hallunk? – narráció" blokk / az adott slide narrációs szövege, idézőjelek nélkül vagy azokkal együtt, ahogy a forrásban van).
- "felirat": a felirat szövege = a narráció szövege szó szerint (a forrás kimondja, hogy a felirat a narrációt szó szerint közli). Add meg a teljes feliratszöveget.
- "leirat-transzkript": a teljes átirat/leirat szövege szó szerint (narrációnál = a narráció szövege; ábránál/diagramnál = a forrásban megadott szöveges leírás).
- "alt-szöveg": a rövid alt-szöveg. Ha a forrás megadja, szó szerint; ha nem, írj egy hű, rövid alt-szöveget a forrás vizuális leírása alapján.
- "egyéb": ha konkrét megjelenő szöveg (pl. AI-jelölés címke, kártya-szöveg), add meg szó szerint.

Assetek (JSON: id, type, loc=hol a forrásban, spec=rövid leírás):
${JSON.stringify(items, null, 1)}

Olvasd el a fájlt, és a "loc" mező + a típus alapján találd meg a megfelelő blokkot. Add vissza MINDEN asset-hez az assetId-t és a verbatim szöveget. A többsoros szöveget tartsd meg sortörésekkel. Csak StructuredOutput.`,
    { schema: SCHEMA, label: `verb:${f.split('/').pop().slice(0, 20)}`, phase: 'Verbatim kinyerés' },
  )
  if (!r) return { file: f, items: [], failed: true }
  return { file: f, items: r.items || [] }
}))

const flat = {}
let filled = 0, failed = []
for (const res of results.filter(Boolean)) {
  if (res.failed) { failed.push(res.file); continue }
  for (const it of res.items) {
    if (it.assetId) { flat[it.assetId] = it.verbatim || ''; if (it.verbatim) filled++ }
  }
}
log(`Verbatim kinyerve: ${filled} asset kitöltve, ${Object.keys(flat).length} összesen, sikertelen fájl: ${failed.length}`)
return { verbatim: flat, failed }
'''

open("/tmp/wf-verbatim.js", "w", encoding="utf-8").write(script)
print(f"workflow kész: /tmp/wf-verbatim.js — {n_files} fájl, {n_items} szöveg-asset")
print("típus-bontás:", {t: sum(1 for a in d['assets'] if a.get('assetType')==t) for t in sorted(TEXT_TYPES)})
