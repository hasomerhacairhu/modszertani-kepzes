export const meta = {
  name: 'media-asset-supplement',
  description: 'Kiegészítő média-asset kinyerés a 9 kimaradt/üres fájlra (6 KAPU + Z.4 + M0/M4 hub)',
  phases: [{ title: 'Kinyerés+Validálás' }, { title: 'Dedup+Audit' }],
}

const FILES = [
  { path: "MODULOK/M1/M1 – KAPU – értékelő (item-bank + rubrika).md", kind: 'kapu' },
  { path: "MODULOK/M2/M2 – KAPU – értékelő (item-bank + rubrika).md", kind: 'kapu' },
  { path: "MODULOK/M3/M3 – KAPU – értékelő (item-bank + rubrika).md", kind: 'kapu' },
  { path: "MODULOK/M5/M5 – KAPU – értékelő (item-bank + rubrika).md", kind: 'kapu' },
  { path: "MODULOK/M6/M6 – KAPU – értékelő (item-bank + rubrika).md", kind: 'kapu' },
  { path: "MODULOK/M7/M7 – KAPU – értékelő (item-bank + rubrika).md", kind: 'kapu' },
  { path: "MODULOK/Z/Z_ONLINE_LECKE/Z.4 – „Záró reflexió + képzés feedback”.md", kind: 'online-lecke' },
  { path: "MODULOK/M0/M0 – „Kickoff, keret, technika”.md", kind: 'hub' },
  { path: "MODULOK/M4/M4 – „Hallható és érthető vagyok_” – Kiállás, kapcsolódás & kérdezéstechnika.md", kind: 'hub' },
]
function moduleOf(p) { const m = p.match(/MODULOK\/(M\d|Z)\//); return m ? m[1] : 'EGYÉB' }
const ROOT = '02 Tervezet'

const VOCAB = `assetType KÖTELEZŐ enum: narráció | beszélőfej-videó | interaktív-videó | animált-diagram | illusztráció | ikon-készlet | fotó-kép | hang-zene-SFX | felirat | leirat-transzkript | alt-szöveg | print-poszter | print-kártya | print-munkalap | egyéb
category KÖTELEZŐ: "digitális-generálandó" | "szöveges-ekvivalens" | "print-fizikai".
ID-séma: <egységkód>-<típusrövidítés>-<2 számjegy>, pl. M3-KAPU-DIA-01, Z.4-IKO-01, M4-HUB-DIA-01.
Típusrövidítések: NAR VID DIA ILL IKO FOTO HANG FEL LEI ALT POSZ KART MUNK EGY.`

const ASSET_ITEM = {
  type: 'object',
  required: ['assetId', 'assetType', 'category', 'location', 'contentSpec', 'purpose', 'provenance'],
  properties: {
    assetId: { type: 'string' }, assetType: { type: 'string' }, category: { type: 'string' },
    location: { type: 'string' }, lineRef: { type: 'string' }, title: { type: 'string' },
    contentSpec: { type: 'string' }, purpose: { type: 'string' }, techSpec: { type: 'string' },
    a11y: { type: 'string' }, provenance: { type: 'string' }, notes: { type: 'string' },
  },
}
const ASSETS_ARRAY = { type: 'array', items: ASSET_ITEM }
const EXTRACT_SCHEMA = { type: 'object', required: ['unitCode', 'assets'], properties: { unitCode: { type: 'string' }, assets: ASSETS_ARRAY } }
const VALIDATE_SCHEMA = { type: 'object', required: ['unitCode', 'assets', 'changeLog'], properties: { unitCode: { type: 'string' }, assets: ASSETS_ARRAY, changeLog: { type: 'array', items: { type: 'object', required: ['action', 'detail'], properties: { action: { type: 'string' }, assetId: { type: 'string' }, detail: { type: 'string' } } } } } }
const DEDUP_SCHEMA = { type: 'object', required: ['groups'], properties: { groups: { type: 'array', items: { type: 'object', required: ['canonicalId', 'memberIds', 'reason'], properties: { canonicalId: { type: 'string' }, memberIds: { type: 'array', items: { type: 'string' } }, reason: { type: 'string' }, reuseNote: { type: 'string' } } } }, note: { type: 'string' } } }
const AUDIT_SCHEMA = { type: 'object', required: ['dimension', 'findings', 'summary'], properties: { dimension: { type: 'string' }, findings: { type: 'array', items: { type: 'object', required: ['assetId', 'severity', 'issue'], properties: { assetId: { type: 'string' }, severity: { type: 'string' }, issue: { type: 'string' }, fix: { type: 'string' } } } }, summary: { type: 'string' } } }

async function tryAgent(prompt, opts, tries = 4) {
  for (let i = 0; i < tries; i++) { const r = await agent(prompt, { ...opts, label: (opts.label || 'a') + (i ? `·r${i}` : '') }); if (r) return r }
  return null
}

const COMMON = `A "${ROOT}" mappa egy magyar Hasomer Hacair madrich-képzés tananyaga. Média-asset = MINDEN legyártandó média: narráció, AI beszélő-fej videó, interaktív/animált videó, animált diagram, illusztráció/storyboard, ikon, fotó/kép, hang, + szöveges ekvivalensek (felirat, leirat, alt-szöveg), + print (poszter, kártya, munkalap).
FONTOS: a KAPU-fájlok értékelő item-bankok — itt jellemzően KEVÉS vagy SEMMI legyártandó média van (a kérdések szövegesek). CSAK valódi, legyártandó vizuális/média assetet vegyél fel; a puszta szöveges kvíz-item NEM asset. Ha nincs, üres lista a helyes válasz.
${VOCAB}`

phase('Kinyerés+Validálás')
const perFile = await pipeline(
  FILES,
  async (item) => {
    const r = await tryAgent(`${COMMON}

FELADAT: Olvasd el TELJESEN ezt az EGY fájlt és nyerd ki MINDEN legyártandó média-asszetjét (ha van).
Fájl: ${ROOT}/${item.path}
Típus: ${item.kind} | Modul: ${moduleOf(item.path)}
contentSpec = precíz, tömör (mit kell generálni); lineRef = forrás-horgony; a11y = alt/felirat/leirat igény; provenance pontosan. Egyedi assetId az ID-séma szerint (egységkód a fájl fejlécéből).
Ha nincs legyártandó média-asset, adj üres assets tömböt. Csak StructuredOutput.`,
      { schema: EXTRACT_SCHEMA, label: `kinyer:${item.path.split('/').pop().slice(0, 16)}`, phase: 'Kinyerés+Validálás' })
    if (!r) return { unitCode: '?', assets: [], _file: item.path, _kind: item.kind, _mod: moduleOf(item.path), _failed: true }
    return { ...r, _file: item.path, _kind: item.kind, _mod: moduleOf(item.path) }
  },
  async (s1, item) => {
    if (s1._failed) return s1
    const r = await tryAgent(`${COMMON}

FELADAT: FÜGGETLEN VALIDÁLÁS (1. kör). Fájl: ${ROOT}/${item.path}
Kinyert lista (JSON): ${JSON.stringify(s1.assets, null, 1)}
Ellenőrizd: (1) hiányzó asset → add; (2) álpozitív (nem legyártandó, pl. puszta szöveges item) → töröld; (3) location/lineRef/contentSpec pontosság → javítsd; (4) spec-teljesség (techSpec, a11y, provenance) → pótold; (5) ID-egyediség.
Add vissza a TELJES javított listát + changeLog. Csak StructuredOutput.`,
      { schema: VALIDATE_SCHEMA, label: `val1:${item.path.split('/').pop().slice(0, 14)}`, phase: 'Kinyerés+Validálás' })
    if (!r) return s1
    return { ...s1, assets: r.assets }
  },
  async (s2, item) => {
    if (s2._failed) return s2
    const r = await tryAgent(`${COMMON}

FELADAT: FÜGGETLEN VALIDÁLÁS (2. kör, adverzariális). Fájl: ${ROOT}/${item.path}
Jelenlegi lista (JSON): ${JSON.stringify(s2.assets, null, 1)}
Maradt-e kimaradt asset / pontatlan lineRef-contentSpec / a11y-techSpec hiány / ID-ütközés? Csak biztos hibát javíts. Add vissza a TELJES véglegesített listát + changeLog. Csak StructuredOutput.`,
      { schema: VALIDATE_SCHEMA, label: `val2:${item.path.split('/').pop().slice(0, 14)}`, phase: 'Kinyerés+Validálás' })
    if (!r) return s2
    return { ...s2, assets: r.assets }
  },
)

const ok = perFile.filter(Boolean)
let allAssets = []
for (const f of ok) for (const a of (f.assets || [])) allAssets.push({ ...a, _file: f._file, _kind: f._kind, _mod: f._mod })
const repFiles = new Set(allAssets.map(a => a._file))
const missingFiles = FILES.map(f => f.path).filter(p => !repFiles.has(p))
log(`Kiegészítő kinyerés: ${allAssets.length} asset, képviselt fájl ${repFiles.size}/${FILES.length}, üres: ${missingFiles.join(', ') || '—'}`)

phase('Dedup+Audit')
const compact = a => ({ id: a.assetId, type: a.assetType, mod: a._mod, file: a._file.split('/').pop(), loc: a.location, title: a.title || '', spec: (a.contentSpec || '').slice(0, 240), a11y: a.a11y || '', prov: a.provenance || '' })
const idx = allAssets.map(compact)

const dedupP = tryAgent(`Média-asset deduplikáció a kiegészítő halmazon. Keresd a VALÓBAN azonos (egyszer legyártandó, többször használt) asseteket. Konzervatív: csak valódi duplikátum. canonicalId + memberIds + reason + reuseNote.
Assetek (JSON): ${JSON.stringify(idx, null, 1)}
Csak StructuredOutput.`, { schema: DEDUP_SCHEMA, label: 'dedup:supp', phase: 'Dedup+Audit' })

const AUDIT_DIMS = [
  { key: 'Akadálymentesség (WCAG 2.2)', task: 'Minden nem-dekoratív vizuálisnak van alt/leirat? Videónak/hangnak felirat+leirat? Jelöld a hiányt.' },
  { key: 'AI-jelölés & jogtisztaság (EU AI Act, IP)', task: 'AI-generált assetek jelölve? Stock/IP-kockázat? Jelöld.' },
  { key: 'Produkciós megvalósíthatóság & terminológia', task: 'Alulspecifikált assetek? Kánoni terminológia (cionizmus, Hasomer Hacair, Somer, kvuca, dugma ishit, Leviatan)? Tartalmi ellentmondás? Jelöld.' },
]
const auditP = parallel(AUDIT_DIMS.map(d => async () => {
  const r = await tryAgent(`Kiegészítő média-asset AUDIT — "${d.key}". ${d.task} Csak valós megállapítás assetId-vel. Ha tiszta, üres findings.
Assetek (JSON): ${JSON.stringify(idx, null, 1)}
Csak StructuredOutput.`, { schema: AUDIT_SCHEMA, label: `audit:${d.key.slice(0, 14)}`, phase: 'Dedup+Audit' })
  return r || { dimension: d.key, findings: [], summary: 'sikertelen' }
}))

const [dedupR, auditR] = await Promise.all([dedupP, auditP])
const dedupGroups = (dedupR && dedupR.groups) || []
const dedupOf = {}
for (const g of dedupGroups) for (const mid of (g.memberIds || [])) if (mid !== g.canonicalId) dedupOf[mid] = { canonical: g.canonicalId, reuseNote: g.reuseNote || g.reason || '' }
const auditOf = {}
for (const ar of auditR.filter(Boolean)) for (const f of (ar.findings || [])) (auditOf[f.assetId] = auditOf[f.assetId] || []).push({ dim: ar.dimension, severity: f.severity, issue: f.issue, fix: f.fix || '' })

function annotRow(a) {
  const d = dedupOf[a.assetId]; const au = auditOf[a.assetId] || []
  return {
    assetId: a.assetId, assetType: a.assetType, category: a.category, mod: a._mod,
    file: a._file, fileShort: a._file.split('/').pop(), kind: a._kind,
    location: a.location, lineRef: a.lineRef || '', title: a.title || '', contentSpec: a.contentSpec, purpose: a.purpose,
    techSpec: a.techSpec || '', a11y: a.a11y || '', provenance: a.provenance || '', notes: a.notes || '',
    dedup: d ? `🔁 = ${d.canonical}${d.reuseNote ? ' (' + d.reuseNote + ')' : ''}` : '',
    audit: au.map(x => `${x.severity === 'blokkoló' ? '⛔' : x.severity === 'fontos' ? '⚠️' : 'ℹ️'} ${x.issue}${x.fix ? ' → ' + x.fix : ''}`).join(' · '),
  }
}
log(`Kiegészítő kész: ${allAssets.length} asset, ${dedupGroups.length} dedup, ${Object.keys(auditOf).length} auditált.`)
return {
  assets: allAssets.map(annotRow),
  dedup: [{ bucket: 'kiegészítő', groups: dedupGroups }],
  audit: auditR.filter(Boolean).map(a => ({ dimension: a.dimension, summary: a.summary, findings: a.findings || [] })),
  missingFiles,
}
