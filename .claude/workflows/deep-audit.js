// ============================================================================
//  DEEP-AUDIT — iteratív kiértékelő → felülvizsgáló → javító → önállóan commitoló
//  harness a Hasomer Hacair madrichképzés (02 Tervezet) tananyagához.
//
//  🔒 READ-ONLY HARNESS. Ez a workflow SOHA nem módosít tananyag-forrást, nem vált
//  branch-et, nem commitol és nem pushol. Csak kiértékel, verifikál és RIPORTOL az
//  audit-mappába. (2026-08-25: a korábbi 'live' mód eltávolítva — a repo elve, hogy
//  tartalmi javítás emberi/ügynöki review-val történik, nem autonóm automatizmussal.
//  A régi live mód `git checkout -B deep-audit`-tal felülírhatott egy meglévő branch-et,
//  és a nem létező `02 Tervezet/_AUDIT/` útvonalra írt volna.)
//
//  ÍV (loop-until-dry konvergencia, körönként):
//    1. ASSESS  — auditor-ügynökök (modulonként + program-szinten), a kutatott
//                 DEEP-AUDIT-RUBRIC.md szerint. CAP: max N finding / auditor, csak 🔴/🟡.
//    2. (DEDUP + GLOBÁLIS CAP) — körök közti dedup + max finding/kör.
//    3. VERIFY  — FÁJLONKÉNT egy szkeptikus ügynök erősíti meg a fájl találatait
//                 (bounded a fájlszámmal — NINCS találatonkénti robbanás).
//    4. ROUTE   — MINDEN találat review-dokumentumba kerül (safety / ideológiai
//                 mélység / architektúra / javasolt javítások); SOHA nem auto-javítjuk.
//  A kör addig ismétel, amíg DRY_STREAK egymást követő kör 0 új találatot ad.
//  Írás KIZÁRÓLAG a `01 Fejlesztés/04 Audit/` mappába. Forrásfájl, commit, push SOHA.
// ============================================================================

export const meta = {
  name: 'deep-audit',
  description: 'Read-only iteratív deep-audit: kiértékel → verifikál → riportál az audit-mappába (nem javít, nem commitol, nem pushol)',
  phases: [
    { title: 'Setup', detail: 'rubrika + tiszta-fa előfeltétel (read-only)' },
    { title: 'Assess', detail: 'auditorok modul + program-szinten, capelt findinggel' },
    { title: 'Verify', detail: 'fájlonként egy szkeptikus megerősítés (bounded)' },
    { title: 'Konvergencia', detail: 'loop-until-dry + záró riport' },
  ],
}

// ============================================================================
//  ⚙️  KONFIG — LITERÁLOK (NEM args). A harness read-only; nincs 'live' mód.
// ============================================================================
const MAX_ROUNDS = 1            // a tananyag a futás alatt nem változik, 1 kör elég
const DRY_STREAK = 1            // ennyi üres kör után konvergens (dry módban 1 elég: 1 kör)
const MAX_FINDINGS_PER_ASSESSOR = 10   // auditoronkénti finding-plafon
const MAX_FINDINGS_PER_ROUND = 60      // körönkénti globális finding-plafon (top by severity)
const REPO = process.cwd()
const ABS = REPO + '/02 Tervezet'
const MOD = ABS + '/Modulok'
const RUBRIC = REPO + '/01 Fejlesztés/04 Audit/DEEP-AUDIT-RUBRIC.md'
const AUDIT_DIR = REPO + '/01 Fejlesztés/04 Audit'   // az EGYETLEN hely, ahová a harness ír
const MODULES = ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'Z']
const PROGRAM_LENSES = [
  { key: 'curriculum-ív', scope: 'A Program terv + minden modul-áttekintő: kompetencia-ív, prerekvizitek, árva/alátámasztatlan kompetenciák, a produktumok összeállása a záró Peula v2-be.' },
  { key: 'kapu-rendszer', scope: 'A Program terv §5 + minden modul Kapuk szakasza + a "<M> – KAPU – értékelő" fájlok: kapu-validitás, küszöbök, rubrika/item minőség, kapu-architektúra.' },
  { key: 'konzisztencia', scope: 'Az EGÉSZ korpusz: terminológia (GLOSSZÁRIUM szerint), kereszthivatkozások épsége, sablon-konformitás, cím↔fájlnév egyezés, törött linkek. FONTOS: a tömeges/ismétlődő apró eltéréseket VOND ÖSSZE egyetlen findingba — ne sorold fel külön minden előfordulást.' },
]

// ---- sémák ----
const FINDING = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: {
      dimension: { type: 'string', description: 'rubrika dimenzió-azonosító, pl. D3' },
      severity: { type: 'string', enum: ['red', 'yellow'] },
      file: { type: 'string', description: 'abszolút útvonal, vagy "program"' },
      location: { type: 'string' },
      issue: { type: 'string' },
      recommendation: { type: 'string' },
      autoFixable: { type: 'boolean' },
      routeTo: { type: 'string', enum: ['fix', 'safeguarding-review', 'ideology-gate-review', 'architecture-review'] },
      sources: { type: 'array', items: { type: 'string' } },
    }, required: ['dimension', 'severity', 'file', 'issue', 'autoFixable', 'routeTo'] } },
  },
  required: ['findings'],
}
const VERIFY = {
  type: 'object',
  properties: {
    confirmed: { type: 'array', items: { type: 'object', properties: {
      idx: { type: 'number', description: 'a bemeneti finding indexe' },
      keep: { type: 'boolean', description: 'true = valós, javítandó; false = fals pozitív/elvetendő' },
      note: { type: 'string' },
    }, required: ['idx', 'keep'] } },
  },
  required: ['confirmed'],
}
const FIXREPORT = { type: 'object', properties: { file: { type: 'string' }, applied: { type: 'number' }, changes: { type: 'array', items: { type: 'string' } } }, required: ['file', 'applied'] }
const OPRESULT = { type: 'object', properties: { ok: { type: 'boolean' }, detail: { type: 'string' } }, required: ['ok', 'detail'] }

const fkey = (f) => `${f.file || 'program'}|${f.dimension}|${(f.location || '').slice(0, 40)}|${(f.issue || '').slice(0, 50).toLowerCase()}`
const sevRank = { red: 0, yellow: 1 }

// ============================================================================
//  SETUP
// ============================================================================
phase('Setup')
const setup = await agent(
  `Setup a deep-audit futáshoz (READ-ONLY). Bash-sel:
1. test -f "${RUBRIC}" — a rubrika kötelező; ha nincs, ok:false.
2. git -C "${REPO}" status --porcelain — ha NEM tiszta a working tree, ok:false (a piszkos fájlokkal).
3. NE válts branch-et, NE commitolj, NE pusholj. Maradj a jelenlegi branch-en.
Add vissza ok + detail (a jelenlegi branch neve).`,
  { schema: OPRESULT, phase: 'Setup', label: 'setup', agentType: 'claude' })
if (!setup || !setup.ok) { log('⛔ Setup megállt: ' + (setup ? setup.detail : 'nincs válasz')); return { aborted: true, reason: setup && setup.detail } }
log(`Setup OK [read-only] — ${setup.detail}`)

// ============================================================================
//  ITERATÍV KÖRÖK
// ============================================================================
const seen = new Set()
const allConfirmed = []
const routed = { 'safeguarding-review': 0, 'ideology-gate-review': 0, 'architecture-review': 0 }
let dryStreak = 0, round = 0

while (round < MAX_ROUNDS && dryStreak < DRY_STREAK) {
  round++
  log(`\n===== KÖR ${round}/${MAX_ROUNDS} =====`)

  // ---- 1) ASSESS ----
  phase('Assess')
  const assessPrompt = (scopeInstr) => `Deep-audit AUDITOR vagy. Olvasd be a rubrikát: ${RUBRIC} (dimenziók + ellenőrizhető kritériumok + súlyozás + auto-fix vs. review besorolás).

HATÓKÖR: ${scopeInstr}

FELADAT: a rubrika releváns dimenziói szerint keresd a VALÓS, FONTOS problémákat.
- CSAK 🔴 (kritikus) és 🟡 (fontos) findingot adj — green/"rendben" megállapítást NE.
- LEGFELJEBB ${MAX_FINDINGS_PER_ASSESSOR} finding, a legfontosabbak. Ne sorold fel a tömeges apró/ismétlődő eltéréseket külön — vond össze.
- autoFixable=true + routeTo='fix' CSAK ha egyértelmű, biztonságos szerkesztéssel javítható.
- routeTo='safeguarding-review' a gyerekvédelmi (D7) DÖNTÉSEKHEZ; 'ideology-gate-review' a D6 ideológiai-mélység / kapu-filozófia DÖNTÉSEKHEZ; 'architecture-review' a nagy strukturális átalakításhoz. Ezeket NE jelöld autoFixable-nek.
- Tárgyi pontosságnál ToolSearch → WebSearch/WebFetch + sources.
NE módosíts fájlt. Légy konkrét (file abszolút útvonal + location). Add vissza FINDING.`

  const assessThunks = [
    ...MODULES.map((m) => () => agent(assessPrompt(`A(z) ${m} modul minden .md fájlja: "${MOD}/${m}" és almappái (ls -R), beleértve a "${m} – KAPU" fájlt.`),
      { schema: FINDING, phase: 'Assess', label: `assess:${m}`, agentType: 'claude' })),
    ...PROGRAM_LENSES.map((l) => () => agent(assessPrompt(l.scope),
      { schema: FINDING, phase: 'Assess', label: `assess:${l.key}`, agentType: 'claude' })),
  ]
  const assessed = []
  for (let i = 0; i < assessThunks.length; i += 6) assessed.push(...(await parallel(assessThunks.slice(i, i + 6))).filter(Boolean))
  let raw = assessed.flatMap((a) => (a.findings || []).slice(0, MAX_FINDINGS_PER_ASSESSOR))

  // ---- dedup vs seen + globális cap (top by severity) ----
  const fresh = []
  for (const f of raw) { const k = fkey(f); if (seen.has(k)) continue; seen.add(k); fresh.push(f) }
  fresh.sort((a, b) => sevRank[a.severity] - sevRank[b.severity])
  const capped = fresh.slice(0, MAX_FINDINGS_PER_ROUND)
  const deferred = fresh.length - capped.length
  log(`Kör ${round}: ${raw.length} nyers → ${fresh.length} friss → ${capped.length} feldolgozva${deferred > 0 ? ` (${deferred} elhalasztva a cap miatt)` : ''}`)
  if (capped.length === 0) { dryStreak++; log(`Üres kör (dry streak ${dryStreak}/${DRY_STREAK})`); continue }
  dryStreak = 0

  // ---- route: review-be ----
  const toReview = capped.filter((f) => f.routeTo !== 'fix')
  const toFix = capped.filter((f) => f.routeTo === 'fix' && f.autoFixable)
  if (toReview.length) {
    const groups = { 'safeguarding-review': 'SAFEGUARDING-REVIEW.md', 'ideology-gate-review': 'IDEOLOGY-GATE-REVIEW.md', 'architecture-review': 'ARCHITECTURE-REVIEW.md' }
    for (const [route, fname] of Object.entries(groups)) {
      const items = toReview.filter((f) => f.routeTo === route)
      if (!items.length) continue
      routed[route] += items.length
      await agent(`Egészítsd ki (append) a "${AUDIT_DIR}/${fname}" review-dokumentumot egy "## Deep-audit kör ${round}" szakasszal, az alábbi DÖNTÉST igénylő találatokkal (dimenzió · fájl/hely · probléma · javaslat · forrás). NE módosíts tananyag-forrást, csak ezt a doksit.
TÉTELEK: ${JSON.stringify(items.map((f) => ({ dimension: f.dimension, file: f.file, location: f.location, issue: f.issue, recommendation: f.recommendation, sources: f.sources })))}
Add vissza ok + detail.`, { schema: OPRESULT, phase: 'Assess', label: `route:${route}`, agentType: 'claude' })
    }
  }
  if (!toFix.length) { log(`Kör ${round}: nincs auto-javítandó (${toReview.length} review-be).`); continue }

  // ---- 2) VERIFY — FÁJLONKÉNT egy szkeptikus (bounded) ----
  phase('Verify')
  const byFileV = {}
  for (const f of toFix) { (byFileV[f.file] = byFileV[f.file] || []).push(f) }
  const vFiles = Object.keys(byFileV)
  const confirmed = []
  const vThunks = vFiles.map((file) => () => {
    const items = byFileV[file]
    return agent(`Adverzális ELLENŐR vagy. Olvasd be a fájlt (${file === 'program' ? 'a finding-ekben megnevezett fájlok' : file}) és a rubrikát (${RUBRIC}). Az alábbi javítandó-jelölt találatok mindegyikéről döntsd el, VALÓS és érdemes-e javítani (keep:true), vagy fals pozitív / túlzó / már javított / a "javítás" rontana (keep:false). Bizonytalanságnál hajlj keep:false felé. Tárgyi kérdésnél ToolSearch → WebSearch.
TALÁLATOK (idx-szel): ${JSON.stringify(items.map((f, i) => ({ idx: i, dimension: f.dimension, location: f.location, issue: f.issue, recommendation: f.recommendation })))}
Add vissza VERIFY (minden idx-re keep + rövid note).`,
      { schema: VERIFY, phase: 'Verify', label: `verify:${(file.split('/').pop() || file).slice(0, 18)}`, agentType: 'claude' })
      .then((v) => { const keep = new Set((v && v.confirmed || []).filter((c) => c.keep).map((c) => c.idx)); return items.filter((_, i) => keep.has(i)) })
  })
  for (let i = 0; i < vThunks.length; i += 8) confirmed.push(...(await parallel(vThunks.slice(i, i + 8))).filter(Boolean).flat())
  log(`Verify: ${toFix.length} jelölt → ${confirmed.length} megerősítve`)
  allConfirmed.push(...confirmed)
  if (!confirmed.length) { log(`Kör ${round}: 0 megerősített javaslat.`); continue }

  // ---- 4) ROUTE: a megerősített javítási JAVASLATOK is review-doksiba mennek ----
  // A harness szándékosan NEM javít és NEM commitol: a tartalmi változtatás emberi
  // vagy ügynöki review-val, külön, átnézett commitban történik.
  phase('Assess')
  await agent(`Egészítsd ki (append) a "${AUDIT_DIR}/DEEP-AUDIT-FINDINGS.md" dokumentumot egy "## Deep-audit kör ${round} — megerősített javaslatok" szakasszal. Tábla: dimenzió · fájl · hely · probléma · javasolt javítás · forrás. **NE módosíts tananyag-forrást, NE commitolj, NE pusholj** — csak ezt az egy doksit írod.
TÉTELEK: ${JSON.stringify(confirmed.map((f) => ({ dimension: f.dimension, severity: f.severity, file: f.file, location: f.location, issue: f.issue, recommendation: f.recommendation, sources: f.sources })))}
Add vissza ok + detail.`, { schema: OPRESULT, phase: 'Assess', label: 'route:findings', agentType: 'claude' })
  log(`Kör ${round}: ${confirmed.length} megerősített javaslat a DEEP-AUDIT-FINDINGS.md-be (nem alkalmazva).`)
}

// ============================================================================
//  ZÁRÓ RIPORT
// ============================================================================
phase('Konvergencia')
const summary = { mode: 'read-only', rounds: round, converged: dryStreak >= DRY_STREAK, confirmed: allConfirmed.length, routed }
await agent(`Írd meg/frissítsd a "${AUDIT_DIR}/DEEP-AUDIT-REPORT.md" záró riportot (Write). NE módosíts tananyag-forrást, NE commitolj, NE pusholj.
ÖSSZEGZÉS: ${JSON.stringify(summary)}
MEGERŐSÍTETT TALÁLATOK (dimenziónként, fájl+hely+probléma): ${JSON.stringify(allConfirmed.map((f) => ({ dimension: f.dimension, severity: f.severity, file: f.file, location: f.location, issue: f.issue })).slice(0, 120))}
Szakaszok: (1) Vezetői összefoglaló (körök, konvergált-e, hány megerősített javaslat, mi ment review-ba — javítás és commit NEM történt); (2) Megerősített találatok dimenziónként; (3) Review-be route-olt döntések (utalás a SAFEGUARDING/IDEOLOGY-GATE/ARCHITECTURE-REVIEW-ra); (4) Következő lépések. Magyar, tegező. Add vissza ok + detail.`,
  { schema: OPRESULT, phase: 'Konvergencia', label: 'záró-riport', agentType: 'claude' })
log(`\n✅ DEEP-AUDIT [read-only] kész: ${round} kör, ${allConfirmed.length} megerősített javaslat, ${Object.values(routed).reduce((a, b) => a + b, 0)} review-be. Forrás nem módosult, commit nem történt.`)
return summary
