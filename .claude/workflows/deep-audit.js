// ============================================================================
//  DEEP-AUDIT — iteratív kiértékelő → felülvizsgáló → javító → önállóan commitoló
//  harness a Hasomer Hacair madrichképzés (02 Tervezet) tananyagához.
//
//  ⚠️ MÓD-VÁLASZTÁS: a futás módját a lenti MODE LITERÁL vezérli — NEM args-ból,
//  mert ebben a környezetben az args nem ér át megbízhatóan a scripthez.
//  Élesben futtatáshoz: állítsd MODE='live'-ra, mentsd, majd indítsd a Workflow-t.
//  Alapértelmezett SAFE: 'dry' (csak kiértékel + riportál, semmit nem javít/commitol).
//
//  ÍV (loop-until-dry konvergencia, körönként):
//    1. ASSESS  — auditor-ügynökök (modulonként + program-szinten), a kutatott
//                 DEEP-AUDIT-RUBRIC.md szerint. CAP: max N finding / auditor, csak 🔴/🟡.
//    2. (DEDUP + GLOBÁLIS CAP) — körök közti dedup + max finding/kör.
//    3. VERIFY  — FÁJLONKÉNT egy szkeptikus ügynök erősíti meg a fájl találatait
//                 (bounded a fájlszámmal — NINCS találatonkénti robbanás).
//    4. FIX     — dimenziónként, fájlonként párhuzamos javítás (ütközésmentes).
//    5. GATE    — integritás-kapu (félkövér-balansz, ⟦?⟧, törött link) commit ELŐTT.
//    6. COMMIT  — dimenziónként egy önálló commit (stagenként).
//    + ROUTE    — safety (D7) / ideológiai-mélység (D6) / architekturális találatok
//                 review-docba; SOHA nem auto-javítjuk.
//  A kör addig ismétel, amíg DRY_STREAK egymást követő kör 0 új találatot ad.
//  Push SOHA. Élesben külön BRANCH-en commitol.
// ============================================================================

export const meta = {
  name: 'deep-audit',
  description: 'Iteratív deep-audit: kiértékel → verifikál → javít → stagenként önállóan commitol, konvergenciáig (MODE a scriptben)',
  phases: [
    { title: 'Setup', detail: 'mód + branch + rubrika + tiszta-fa előfeltétel' },
    { title: 'Assess', detail: 'auditorok modul + program-szinten, capelt findinggel' },
    { title: 'Verify', detail: 'fájlonként egy szkeptikus megerősítés (bounded)' },
    { title: 'Fix', detail: 'dimenziónként, fájlonként párhuzamos javítás' },
    { title: 'Commit', detail: 'integritás-kapu + dimenziónkénti önálló commit' },
    { title: 'Konvergencia', detail: 'loop-until-dry + záró riport' },
  ],
}

// ============================================================================
//  ⚙️  KONFIG — LITERÁLOK (NEM args). Éleshez: MODE='live'.
// ============================================================================
const MODE = 'dry'              // 'dry' = csak kiértékel+riportál | 'live' = javít+commitol
const MAX_ROUNDS = MODE === 'live' ? 2 : 1   // dry: 1 kör (a tananyag nem változik); live: 2
const DRY_STREAK = 1            // ennyi üres kör után konvergens (dry módban 1 elég: 1 kör)
const MAX_FINDINGS_PER_ASSESSOR = 10   // auditoronkénti finding-plafon
const MAX_FINDINGS_PER_ROUND = 60      // körönkénti globális finding-plafon (top by severity)
const BRANCH = 'deep-audit'    // élesben ide commitol (külön a main-től)

const DRY_RUN = MODE !== 'live'
const ABS = '/Users/heymarcell/DEV/modszertani-kepzes/02 Tervezet'
const REPO = '/Users/heymarcell/DEV/modszertani-kepzes'
const MOD = ABS + '/MODULOK'
const RUBRIC = ABS + '/_AUDIT/DEEP-AUDIT-RUBRIC.md'
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
  `Setup a deep-audit futáshoz (MÓD: ${MODE}). Bash-sel:
1. test -f "${RUBRIC}" — a rubrika kötelező; ha nincs, ok:false.
2. git -C "${REPO}" status --porcelain — ha NEM tiszta a working tree, ok:false (a piszkos fájlokkal).
${DRY_RUN ? '3. DRY mód: NE válts branch-et, ne commitolj. Maradj a jelenlegi branch-en.' : `3. LIVE mód: git -C "${REPO}" checkout -B ${BRANCH} (külön branch a main-től).`}
Add vissza ok + detail (a jelenlegi branch neve).`,
  { schema: OPRESULT, phase: 'Setup', label: 'setup', agentType: 'claude' })
if (!setup || !setup.ok) { log('⛔ Setup megállt: ' + (setup ? setup.detail : 'nincs válasz')); return { aborted: true, reason: setup && setup.detail } }
log(`Setup OK [${MODE}] — ${setup.detail}`)

// ============================================================================
//  ITERATÍV KÖRÖK
// ============================================================================
const seen = new Set()
const allConfirmed = []
const routed = { 'safeguarding-review': 0, 'ideology-gate-review': 0, 'architecture-review': 0 }
const commits = []
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
      await agent(`Egészítsd ki (append) a "${ABS}/_AUDIT/${fname}" review-dokumentumot egy "## Deep-audit kör ${round}" szakasszal, az alábbi DÖNTÉST igénylő találatokkal (dimenzió · fájl/hely · probléma · javaslat · forrás). NE módosíts tananyag-forrást, csak ezt a doksit.
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
  if (DRY_RUN) { log(`[DRY] Kör ${round}: ${confirmed.length} megerősített javítandó (nem alkalmazva), ${toReview.length} review-be.`); continue }
  if (!confirmed.length) continue

  // ---- 4) FIX dimenziónként, fájlonként + 5) GATE + 6) COMMIT ----
  const byDim = {}
  for (const f of confirmed) (byDim[f.dimension] = byDim[f.dimension] || []).push(f)
  for (const dim of Object.keys(byDim).sort()) {
    phase('Fix')
    const byFile = {}
    for (const f of byDim[dim]) (byFile[f.file] = byFile[f.file] || []).push(f)
    const fixThunks = Object.entries(byFile).map(([file, items]) => () =>
      agent(`Deep-audit JAVÍTÓ vagy (${dim}). Cél: ${file === 'program' ? 'a finding-ekben megnevezett fájl(ok)' : file}. Olvasd be a fájl(oka)t + a rubrikát (${RUBRIC}). Minden találatra PRECÍZ, MINIMÁLIS Edit; a meglévő helyes tartalmat ne töröld; a pótolt/kiemelt részt **félkövérrel**; tegező, someres hangnem; tárgyinál ToolSearch → WebSearch + forrás. Integritás: páros félkövér, nincs ⟦?⟧, nincs törött link, cím↔fájlnév egyezés. Ne nyúlj a finding hatókörén kívülre.
TALÁLATOK: ${JSON.stringify(items.map((f) => ({ location: f.location, issue: f.issue, recommendation: f.recommendation, sources: f.sources })))}
Ellenőrizd Read-del. Add vissza FIXREPORT.`,
        { schema: FIXREPORT, phase: 'Fix', label: `fix:${dim}:${(file.split('/').pop() || file).slice(0, 14)}`, agentType: 'claude' }))
    const fixRes = []
    for (let i = 0; i < fixThunks.length; i += 6) fixRes.push(...(await parallel(fixThunks.slice(i, i + 6))).filter(Boolean))
    if (fixRes.reduce((a, b) => a + (b.applied || 0), 0) === 0) { log(`${dim}: 0 javítás.`); continue }

    phase('Commit')
    const commit = await agent(`Integritás-kapu + commit a deep-audit ${dim} javításaihoz (kör ${round}).
1. Integritás a megváltozott fájlokon (git -C "${REPO}" diff --name-only). Node-dal minden .md-re: (a) a *** elválasztó-sorok eldobása + a "***" → "** *" csere UTÁN a ** párok száma PÁROS legyen (páratlan=HIBA); (b) nincs ⟦?⟧; (c) nincs "file:///workspace".
2. HIBA esetén NE commitolj, ok:false + detail (mely fájl/mi).
3. OK esetén: git -C "${REPO}" add -u -- "02 Tervezet" (+ új fájlok); commit -F fájlból (magyar karakterek!): "fix(deep-audit ${dim}): <összefoglaló> [kör ${round}]\\n\\n<felsorolás>\\n\\nCo-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>". NE pushelj.
Add vissza ok + detail (commit SHA + fájlszám).`,
      { schema: OPRESULT, phase: 'Commit', label: `commit:${dim}`, agentType: 'claude' })
    commits.push({ round, dim, ok: commit && commit.ok })
    log(`${dim} commit: ${commit && commit.ok ? '✓ ' + commit.detail : '⛔ ' + (commit && commit.detail)}`)
  }
}

// ============================================================================
//  ZÁRÓ RIPORT
// ============================================================================
phase('Konvergencia')
const summary = { mode: MODE, rounds: round, converged: dryStreak >= DRY_STREAK, confirmed: allConfirmed.length, routed, commits: commits.filter((c) => c.ok).length }
await agent(`Írd meg/frissítsd a "${ABS}/_AUDIT/DEEP-AUDIT-REPORT.md" záró riportot (Write).
ÖSSZEGZÉS: ${JSON.stringify(summary)}
MEGERŐSÍTETT TALÁLATOK (dimenziónként, fájl+hely+probléma): ${JSON.stringify(allConfirmed.map((f) => ({ dimension: f.dimension, severity: f.severity, file: f.file, location: f.location, issue: f.issue })).slice(0, 120))}
Szakaszok: (1) Vezetői összefoglaló (mód, körök, konvergált-e, hány javítás/commit, mi ment review-ba); (2) Megerősített találatok dimenziónként; (3) Review-be route-olt döntések (utalás a SAFEGUARDING/IDEOLOGY-GATE/ARCHITECTURE-REVIEW-ra); (4) Következő lépések. Magyar, tegező. Add vissza ok + detail.`,
  { schema: OPRESULT, phase: 'Konvergencia', label: 'záró-riport', agentType: 'claude' })
log(`\n✅ DEEP-AUDIT [${MODE}] kész: ${round} kör, ${allConfirmed.length} megerősített, ${commits.filter((c) => c.ok).length} commit, ${Object.values(routed).reduce((a, b) => a + b, 0)} review-be.`)
return summary
