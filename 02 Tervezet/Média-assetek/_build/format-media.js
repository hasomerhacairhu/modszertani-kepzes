#!/usr/bin/env node
// Determinisztikus média-asset regiszter formázó — TÖBB bemenetet fésül össze.
// Használat: node format-media.js <dest.md> <result1.json> [result2.json ...]
const fs = require('fs')
const argv = process.argv.slice(2)
const DEST = argv[0]
const SRCS = argv.slice(1)
if (!DEST || !SRCS.length) { console.error('Használat: node format-media.js <dest.md> <result1.json> [result2.json ...]'); process.exit(1) }

function loadResult(p) {
  let d = JSON.parse(fs.readFileSync(p, 'utf8'))
  if (d && typeof d.result === 'string') { try { d = JSON.parse(d.result) } catch {} }
  if (d && d.result && (d.result.assets || d.result.stats)) d = d.result
  return d
}

// ---- merge ----
const assetsById = new Map()
let dedup = []
const auditByDim = new Map()
const emptyFilesSet = new Set()
let productionRules = []
for (const p of SRCS) {
  const d = loadResult(p)
  if (d.productionRules && d.productionRules.length) productionRules = d.productionRules
  for (const a of (d.assets || [])) if (!assetsById.has(a.assetId)) assetsById.set(a.assetId, a)
  for (const grp of (d.dedup || [])) dedup.push(grp)
  for (const a of (d.audit || [])) {
    const key = a.dimension
    if (!auditByDim.has(key)) auditByDim.set(key, { dimension: key, summary: a.summary || '', findings: [] })
    auditByDim.get(key).findings.push(...(a.findings || []))
  }
  for (const mf of (d.missingFiles || [])) emptyFilesSet.add(mf)
}
const assets = [...assetsById.values()]
const audit = [...auditByDim.values()]
// csak azok az "üres" fájlok, amelyeknek tényleg NINCS assetje a fésült halmazban
const filesWithAssets = new Set(assets.map(a => a.file))
const emptyFiles = [...emptyFilesSet].filter(f => !filesWithAssets.has(f)).sort()

// ---- stats a fésült sorokból ----
const stats = { total: assets.length, byType: {}, byCat: {}, byMod: {}, filesRepresented: new Set(assets.map(a => a.file)).size }
for (const a of assets) {
  stats.byType[a.assetType] = (stats.byType[a.assetType] || 0) + 1
  stats.byCat[a.category] = (stats.byCat[a.category] || 0) + 1
  stats.byMod[a.mod] = (stats.byMod[a.mod] || 0) + 1
}
// dedup-tagok száma
const dgroups = []
for (const d of dedup) for (const g of (d.groups || [])) dgroups.push({ bucket: d.bucket || '—', ...g })
let dupMembers = 0
for (const g of dgroups) dupMembers += Math.max(0, (new Set(g.memberIds || [])).size - 1)
stats.unique = stats.total - dupMembers
stats.duplicates = dupMembers

const today = new Date().toISOString().slice(0, 10)
const esc = s => (s == null ? '' : String(s)).replace(/&amp;/g, '&').replace(/\r?\n+/g, ' ').replace(/\|/g, '∕').replace(/\s+/g, ' ').trim()
const cell = s => esc(s) || '—'
function provBucket(p) {
  p = (p || '').toLowerCase()
  if (/^ai|ai-gener/.test(p)) return 'AI-generált'
  if (/stock/.test(p)) return 'stock'
  if (/vegyes/.test(p)) return 'vegyes'
  if (/emberi|ember által|narrác|forrásban kész|lektorált/.test(p)) return 'emberi-felvétel / kész szöveg'
  if (/szöveges-ekviv/.test(p)) return 'szöveges-ekvivalens (származtatott)'
  return 'egyéb/ismeretlen'
}
const KAT = { 'digitális-generálandó': 'digi', 'szöveges-ekvivalens': 'a11y-szöveg', 'print-fizikai': 'print' }

const out = []
const P = s => out.push(s)

P(`# 🎬 Média-asset regiszter — Hasomer Hacair madrich-képzés`)
P(``)
P(`> Generálva: **${today}** · Forrás: \`02 Tervezet/\` · Módszer: per-fájl kinyerés → **2 független validáló kör** → típus-bucket **dedup** → **5 dimenziós audit**. ${SRCS.length > 1 ? `(${SRCS.length} futás összefésülve.)` : ''}`)
P(`>`)
P(`> **Mi ez?** A teljes leltár MINDEN legyártandó média-assetről (narráció, AI beszélő-fej videó, animált diagram, illusztráció, ikon, fotó, hang) és a hozzájuk tartozó **szöveges ekvivalensekről** (felirat, leirat, alt-szöveg) + a **print/fizikai** anyagokról. Minden sor **visszautal** a forrásfájlra, slide-ra és sorra — a teljes verbatim szöveg ott él; ez a *legyártandó* leltár.`)
P(`>`)
P(`> **Jelölések:** ⛔ blokkoló · ⚠️ fontos · ℹ️ javasolt audit-megjegyzés · 🔁 dedup-újrahasznosítás (egyszer gyártandó, többször használt).`)
P(``)

P(`## 📊 Összesítő`)
P(``)
P(`| Mutató | Érték |`)
P(`|---|--:|`)
P(`| Összes azonosított asset-sor | **${stats.total}** |`)
P(`| Egyedi, ténylegesen legyártandó | **${stats.unique}** |`)
P(`| Dedup-újrahasznosítás (nem kell újra gyártani) | ${stats.duplicates} |`)
P(`| Lefedett forrásfájl | ${stats.filesRepresented} |`)
P(``)

function tally(title, obj, sortByCount = true, order = null) {
  if (!obj) return
  P(`**${title}**`); P(``)
  P(`| Tétel | Db |`); P(`|---|--:|`)
  let ents = Object.entries(obj)
  if (order) { const o = {}; for (const k of order) if (obj[k] != null) o[k] = obj[k]; for (const k of Object.keys(obj)) if (o[k] == null) o[k] = obj[k]; ents = Object.entries(o) }
  else if (sortByCount) ents.sort((a, b) => b[1] - a[1])
  for (const [k, v] of ents) P(`| ${esc(k)} | ${v} |`)
  P(``)
}
tally('Kategória szerint', stats.byCat)
tally('Típus szerint', stats.byType)
tally('Modul szerint', stats.byMod, false, ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'Z'])
const provAgg = {}
for (const a of assets) { const b = provBucket(a.provenance); provAgg[b] = (provAgg[b] || 0) + 1 }
tally('Eredet (provenance) szerint — gyártási mód', provAgg)

if (emptyFiles.length) {
  P(`**Ellenőrzött, médiamentes fájlok (${emptyFiles.length})** — átnézve, NINCS bennük legyártandó média-asset (item-bank/áttekintő/reflexiós fájlok; a bennük lévő videó-/kép-utalások tanulói beadványra vagy más fájl már katalogizált assetjére mutatnak):`)
  P(``)
  for (const f of emptyFiles) P(`- \`${esc(f)}\``)
  P(``)
}

if (productionRules.length) {
  P(`## 🛠️ Produkciós konvenciók (osztály-szabályok)`)
  P(``)
  P(`> A „fontos" audit-tételek nagy része nem egyedi hiba, hanem ugyanaz a néhány produkciós konvenció. Ezek a szabályok zárják le őket; a szervezet-specifikus részek (hex-paletta, licenc-igazolás, voice-ID) ⟬KITÖLTENDŐ⟭ maradnak.`)
  P(``)
  P(`| Szabály | Megnevezés | Tartalom |`)
  P(`|---|---|---|`)
  for (const r of productionRules) P(`| **${esc(r.id)}** | ${esc(r.title)} | ${esc(r.text)} |`)
  P(``)
}

P(`## 🔁 Dedup-térkép — ${dgroups.length} újrahasznosítási csoport`)
P(``)
if (!dgroups.length) { P(`_Nincs azonosított duplikátum._`); P(``) }
else {
  P(`| Kanonikus (megtartandó) | Tagok | Bucket | Indok / újrahasznosítás |`)
  P(`|---|---|---|---|`)
  for (const g of dgroups) P(`| \`${cell(g.canonicalId)}\` | ${cell((g.memberIds || []).join(', '))} | ${cell(g.bucket)} | ${cell((g.reason || '') + (g.reuseNote ? ' — ' + g.reuseNote : ''))} |`)
  P(``)
}

const sevRank = { 'blokkoló': 0, 'fontos': 1, 'javasolt': 2 }
const sevIcon = { 'blokkoló': '⛔', 'fontos': '⚠️', 'javasolt': 'ℹ️' }
let auditTotal = 0
for (const a of audit) auditTotal += (a.findings || []).length
P(`## 🔎 Audit-jelentés — ${auditTotal} megállapítás, ${audit.length} dimenzió`)
P(``)
for (const a of audit) {
  const fs2 = (a.findings || []).slice().sort((x, y) => (sevRank[x.severity] ?? 3) - (sevRank[y.severity] ?? 3))
  P(`### ${esc(a.dimension)} — ${fs2.length} megállapítás`); P(``)
  if (a.summary) { P(`> ${esc(a.summary)}`); P(``) }
  if (fs2.length) {
    P(`| Súly | Asset | Probléma | Javasolt javítás |`); P(`|---|---|---|---|`)
    for (const f of fs2) P(`| ${sevIcon[f.severity] || ''} ${cell(f.severity)} | \`${cell(f.assetId)}\` | ${cell(f.issue)} | ${cell(f.fix)} |`)
    P(``)
  }
}

P(`## 📁 Modulonkénti asset-leltár`)
P(``)
const order = ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'Z']
const byMod = {}
for (const a of assets) (byMod[a.mod] = byMod[a.mod] || []).push(a)
const modKeys = order.filter(m => byMod[m]).concat(Object.keys(byMod).filter(m => !order.includes(m)))
for (const mod of modKeys) {
  const rows = byMod[mod]
  P(`### ${mod} modul — ${rows.length} asset`); P(``)
  const byFile = {}
  for (const a of rows) (byFile[a.fileShort || a.file] = byFile[a.fileShort || a.file] || []).push(a)
  const kindRank = { 'online-lecke': 0, 'peula': 1, 'hub': 2, 'kapu': 3 }
  const files = Object.keys(byFile).sort((x, y) => {
    const kr = (kindRank[byFile[x][0].kind] ?? 9) - (kindRank[byFile[y][0].kind] ?? 9)
    return kr || x.localeCompare(y, 'hu', { numeric: true })
  })
  for (const f of files) {
    const fr = byFile[f].slice().sort((x, y) => String(x.assetId).localeCompare(String(y.assetId), 'hu', { numeric: true }))
    P(`#### ${esc(fr[0].fileShort || f)}  \`(${fr[0].kind})\``); P(``)
    P(`| ID | Típus | Kat. | Hol (slide ▸ sor) | Mit kell generálni | Felmondandó / generálandó szöveg (verbatim) | Miért (cél) | Tech-spec | A11y | Eredet | Dedup / Audit |`)
    P(`|---|---|---|---|---|---|---|---|---|---|---|`)
    for (const a of fr) {
      const hol = [a.location, a.lineRef].filter(Boolean).map(esc).join(' ▸ ')
      const da = [a.dedup, a.audit].filter(Boolean).map(esc).join(' · ')
      P(`| \`${cell(a.assetId)}\` | ${cell(a.assetType)} | ${KAT[a.category] || cell(a.category)} | ${cell(hol)} | ${cell(a.contentSpec)} | ${cell(a.verbatim)} | ${cell(a.purpose)} | ${cell(a.techSpec)} | ${cell(a.a11y)} | ${cell(provBucket(a.provenance))} | ${da || '—'} |`)
    }
    P(``)
  }
}

P(`---`)
P(`*Regiszter vége. ${stats.total} asset-sor, ${stats.unique} egyedi, ${dgroups.length} dedup-csoport, ${auditTotal} audit-megállapítás. A ⟬KITÖLTENDŐ⟭ jellegű emberi/szervezeti tételek a forrásfájlokban és a \`_EMBERI-JÓVÁHAGYÁS-SZÜKSÉGES.md\`-ben élnek.*`)

fs.writeFileSync(DEST, out.join('\n') + '\n')
console.error(`KÉSZ: ${DEST} — ${assets.length} egyedi sor, ${out.length} md-sor, ${dgroups.length} dedup, ${auditTotal} audit, ${stats.filesRepresented} fájl.`)
