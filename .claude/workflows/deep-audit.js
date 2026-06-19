// ============================================================================
//  DEEP-AUDIT — iteratív kiértékelő → felülvizsgáló → javító → önállóan commitoló
//  harness a Hasomer Hacair madrichképzés (02 Tervezet) tananyagához.
//
//  ÍV (loop-until-dry konvergencia, körönként):
//    1. ASSESS    — fan-out auditor-ügynökök (modulonként + program-szinten),
//                   a kutatott DEEP-AUDIT-RUBRIC.md dimenziói szerint
//    2. VERIFY    — adverzális megerősítés: minden auto-javítandó találatot
//                   skeptikusok próbálnak cáfolni; csak a túlélők maradnak
//    3. (DEDUP)   — körök közti deduplikáció (seen halmaz)
//    4. FIX       — dimenziónként, fájlonként párhuzamos javítás (ütközésmentes)
//    5. GATE      — integritás-kapu (félkövér-balansz, ⟦?⟧, törött link) commit ELŐTT
//    6. COMMIT    — dimenziónként egy önálló commit (stagenként)
//    + ROUTE      — safety / ideológiai-mélység / architekturális találatok
//                   review-docba kerülnek, NEM auto-javítjuk
//    A kör addig ismétel, amíg DRY_STREAK egymást követő kör 0 új találatot ad.
//
//  args (mind opcionális):
//    { dryRun: bool=false,           // true: csak ASSESS+VERIFY+riport+review, NINCS fix/commit
//      maxRounds: number=3,
//      dryStreak: number=2,          // ennyi üres kör után konvergens
//      modules: string[]=M0..Z,
//      rubricPath: string,
//      skepticsPerFinding: number=2,
//      branch: string='deep-audit' } // dryRun=false esetén külön branch-re commitol
// ============================================================================

export const meta = {
  name: 'deep-audit',
  description: 'Iteratív deep-audit: kiértékel → adverzálisan verifikál → javít → stagenként önállóan commitol, konvergenciáig',
  phases: [
    { title: 'Setup', detail: 'branch + rubrika + kiindulási integritás' },
    { title: 'Assess', detail: 'auditor-ügynökök modulonként + program-szinten, rubrika szerint' },
    { title: 'Verify', detail: 'adverzális megerősítés (skeptikusok cáfolnak)' },
    { title: 'Fix', detail: 'dimenziónként, fájlonként párhuzamos javítás' },
    { title: 'Commit', detail: 'integritás-kapu + dimenziónkénti önálló commit' },
    { title: 'Konvergencia', detail: 'loop-until-dry + záró riport' },
  ],
}

// ---- paraméterek ----
const A = args || {}
const ABS = '/Users/heymarcell/DEV/modszertani-kepzes/02 Tervezet'
const REPO = '/Users/heymarcell/DEV/modszertani-kepzes'
const MOD = ABS + '/MODULOK'
const RUBRIC = A.rubricPath || ABS + '/_AUDIT/DEEP-AUDIT-RUBRIC.md'
const MODULES = A.modules || ['M0', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'Z']
const DRY_RUN = !!A.dryRun
const MAX_ROUNDS = A.maxRounds || 3
const DRY_STREAK = A.dryStreak || 2
const SKEPTICS = A.skepticsPerFinding || 2
const BRANCH = A.branch || 'deep-audit'

// program-szintű auditor-fókuszok (a modulokon átívelő dimenziókra)
const PROGRAM_LENSES = [
  { key: 'curriculum-ív', scope: 'A Program terv + minden modul-áttekintő: kompetencia-ív, prerekvizitek, árva/alátámasztatlan kompetenciák, a produktumok összeállása a záró Peula v2-be (capstone).' },
  { key: 'kapu-rendszer', scope: 'A Program terv §5 + minden modul Kapuk szakasza + a "<M> – KAPU – értékelő" fájlok: kapu-validitás, küszöbök védhetősége, rubrika/item minőség, kapu-architektúra koherenciája.' },
  { key: 'konzisztencia', scope: 'Az EGÉSZ korpusz: terminológia (a GLOSSZÁRIUM szerint), kereszthivatkozások kétirányú épsége, sablon-konformitás, cím↔fájlnév egyezés, törött linkek.' },
]

// ---- sémák ----
const FINDING = {
  type: 'object',
  properties: {
    findings: { type: 'array', items: { type: 'object', properties: {
      dimension: { type: 'string', description: 'a rubrika dimenzió-azonosítója, pl. D3' },
      severity: { type: 'string', enum: ['red', 'yellow', 'green'] },
      file: { type: 'string', description: 'abszolút útvonal, vagy "program" ha több fájlt érint' },
      location: { type: 'string' },
      issue: { type: 'string' },
      recommendation: { type: 'string' },
      autoFixable: { type: 'boolean', description: 'true ha egyértelmű szerkesztéssel javítható; false ha gyerekvédelmi/ideológiai-mélység/szervezeti/architekturális DÖNTÉS kell' },
      routeTo: { type: 'string', enum: ['fix', 'safeguarding-review', 'ideology-gate-review', 'architecture-review', 'none'], description: 'hova tartozik' },
      sources: { type: 'array', items: { type: 'string' } },
    }, required: ['dimension', 'severity', 'issue', 'autoFixable', 'routeTo'] } },
  },
  required: ['findings'],
}
const VERDICT = {
  type: 'object',
  properties: { refuted: { type: 'boolean' }, reason: { type: 'string' } },
  required: ['refuted'],
}
const FIXREPORT = {
  type: 'object',
  properties: {
    file: { type: 'string' }, applied: { type: 'number' },
    changes: { type: 'array', items: { type: 'string' } }, skipped: { type: 'array', items: { type: 'string' } },
  },
  required: ['file', 'applied'],
}
const OPRESULT = { type: 'object', properties: { ok: { type: 'boolean' }, detail: { type: 'string' } }, required: ['ok', 'detail'] }

// ---- segédek ----
const fkey = (f) => `${f.file || 'program'}|${f.dimension}|${(f.issue || '').slice(0, 70).toLowerCase().replace(/\s+/g, ' ')}`
const sevRank = { red: 0, yellow: 1, green: 2 }

// ============================================================================
//  SETUP
// ============================================================================
phase('Setup')
const setup = await agent(
  `Setup a deep-audit futáshoz. Bash-sel:
1. Ellenőrizd, hogy a "${RUBRIC}" fájl létezik (test -f). Ha NEM, jelezd ok:false-szal (a rubrika kötelező).
2. Ellenőrizd, hogy a git working tree TISZTA (git -C "${REPO}" status --porcelain). Ha nem tiszta, jelezd (ok:false, detail a piszkos fájlokkal) — ne kezdjünk piszkos fán.
${DRY_RUN ? '3. DRY RUN mód: NE válts branch-et, ne commitolj.' : `3. Hozz létre / válts a "${BRANCH}" branch-re (git -C "${REPO}" checkout -B ${BRANCH}).`}
Add vissza ok + detail (a rubrika dimenzió-azonosítóinak listája, ha ki tudod olvasni a fájl elejéből).`,
  { schema: OPRESULT, phase: 'Setup', label: 'setup', agentType: 'claude' })

if (!setup || !setup.ok) {
  log('⛔ Setup megállította a futást: ' + (setup ? setup.detail : 'nincs válasz'))
  return { aborted: true, reason: setup && setup.detail }
}
log('Setup OK. ' + (DRY_RUN ? '[DRY RUN]' : 'Branch: ' + BRANCH) + ' — ' + setup.detail)

// ============================================================================
//  ITERATÍV KÖRÖK
// ============================================================================
const seen = new Set()
const allConfirmed = []        // minden megerősített találat (riporthoz)
const routed = { 'safeguarding-review': 0, 'ideology-gate-review': 0, 'architecture-review': 0 }
const commits = []
let dryStreak = 0
let round = 0

while (round < MAX_ROUNDS && dryStreak < DRY_STREAK) {
  round++
  log(`\n========== KÖR ${round}/${MAX_ROUNDS} ==========`)

  // ---- 1) ASSESS ----
  phase('Assess')
  const assessPrompt = (scopeLabel, scopeInstr) => `Deep-audit AUDITOR vagy. Olvasd be a rubrikát: ${RUBRIC} (dimenziók + ellenőrizhető kritériumok + súlyozás + mely dimenziók AUTO-JAVÍTHATÓK vs. review-t igénylők).

HATÓKÖR: ${scopeInstr}

FELADAT: vizsgáld át a hatókörödbe eső tananyagot a rubrika MINDEN releváns dimenziója szerint. Minden valós problémához adj egy findingot: dimension (rubrika-azonosító, pl. D3), severity (red/yellow/green), file (abszolút útvonal vagy "program"), location, issue, recommendation, autoFixable, routeTo.
- autoFixable=true + routeTo='fix' CSAK ha egyértelmű, biztonságos szerkesztéssel javítható (szöveg, formázás, konzisztencia, hiányzó-de-kikövetkeztethető tartalom, link, terminológia, akadálymentesítési jegyzet, hiányzó rubrika/item-elem).
- autoFixable=false + routeTo='safeguarding-review' a gyerekvédelmi DÖNTÉST igénylő tételekhez; 'ideology-gate-review' az ideológiai-mélység és kapu-filozófia DÖNTÉSEKHEZ; 'architecture-review' a nagy strukturális átalakításhoz.
- Ahol tárgyi/forrás-pontosság kell, ToolSearch → WebSearch/WebFetch és add meg a sources-t.
- Ami már RENDBEN van, arról adj 1-2 green findingot (routeTo='none').
NE módosíts SEMMILYEN fájlt — csak olvass. Légy konkrét (fájl+hely). Add vissza a FINDING sémát.`

  const assessThunks = [
    ...MODULES.map((m) => () => agent(assessPrompt(m, `A(z) ${m} modul minden .md fájlja: "${MOD}/${m}" és almappái (ls -R). Modul-áttekintő + online leckék + peulák + a "${m} – KAPU" fájl ha van.`),
      { schema: FINDING, phase: 'Assess', label: `assess:${m}`, agentType: 'claude' })),
    ...PROGRAM_LENSES.map((l) => () => agent(assessPrompt(l.key, l.scope),
      { schema: FINDING, phase: 'Assess', label: `assess:${l.key}`, agentType: 'claude' })),
  ]
  const assessed = []
  const BATCH = 6
  for (let i = 0; i < assessThunks.length; i += BATCH) {
    const r = await parallel(assessThunks.slice(i, i + BATCH))
    assessed.push(...r.filter(Boolean))
  }
  const rawFindings = assessed.flatMap((a) => a.findings || [])

  // ---- dedup vs seen, és csak actionable (nem-green, nem-seen) ----
  const fresh = []
  for (const f of rawFindings) {
    if (f.severity === 'green' || f.routeTo === 'none') continue
    const k = fkey(f)
    if (seen.has(k)) continue
    seen.add(k)
    fresh.push(f)
  }
  log(`Kör ${round}: ${rawFindings.length} nyers finding → ${fresh.length} friss, actionable`)

  if (fresh.length === 0) { dryStreak++; log(`Üres kör (dry streak ${dryStreak}/${DRY_STREAK})`); continue }
  dryStreak = 0

  // ---- route: review-be menők elkülönítése ----
  const toReview = fresh.filter((f) => f.routeTo !== 'fix')
  const toFixAll = fresh.filter((f) => f.routeTo === 'fix' && f.autoFixable)

  // ---- 2) VERIFY (adverzális) a fix-jelölteken ----
  phase('Verify')
  const confirmed = []
  const verifyThunks = toFixAll.map((f) => () =>
    parallel(Array.from({ length: SKEPTICS }, (_, i) => () =>
      agent(`Adverzális ELLENŐR vagy. Próbáld CÁFOLNI az alábbi audit-találatot. Olvasd be az érintett fájlt (${f.file}) és a rubrikát (${RUBRIC}); ha tárgyi kérdés, ToolSearch → WebSearch.
TALÁLAT [${f.dimension}/${f.severity}] ${f.location || ''}: ${f.issue}
JAVASLAT: ${f.recommendation || ''}
Ha a találat HIBÁS, túlzó, már javított, vagy a "javítás" rontana a tananyagon → refuted=true. Bizonytalanságnál hajlj a refuted=true felé (csak valós, egyértelmű problémát fixálunk). Add vissza VERDICT.`,
        { schema: VERDICT, phase: 'Verify', label: `verify:${(f.dimension || '?')}#${i + 1}`, agentType: 'claude' })))
      .then((votes) => {
        const refutes = votes.filter(Boolean).filter((v) => v.refuted).length
        const survives = refutes < Math.ceil(SKEPTICS / 2 + 0.001) // többségi cáfolat kell a kiejtéshez
        return survives ? f : null
      }))
  const vBatch = 8
  for (let i = 0; i < verifyThunks.length; i += vBatch) {
    const r = await parallel(verifyThunks.slice(i, i + vBatch))
    confirmed.push(...r.filter(Boolean))
  }
  log(`Verify: ${toFixAll.length} jelölt → ${confirmed.length} megerősítve (${toReview.length} review-be)`)
  allConfirmed.push(...confirmed)

  // ---- review-be route-olt találatok kiírása (NEM dry-specifikus: mindig dokumentáljuk) ----
  if (toReview.length) {
    const byDoc = {
      'safeguarding-review': toReview.filter((f) => f.routeTo === 'safeguarding-review'),
      'ideology-gate-review': toReview.filter((f) => f.routeTo === 'ideology-gate-review'),
      'architecture-review': toReview.filter((f) => f.routeTo === 'architecture-review'),
    }
    for (const [doc, items] of Object.entries(byDoc)) {
      if (!items.length) continue
      routed[doc] += items.length
      const fname = doc === 'safeguarding-review' ? 'SAFEGUARDING-REVIEW.md'
        : doc === 'ideology-gate-review' ? 'IDEOLOGY-GATE-REVIEW.md' : 'ARCHITECTURE-REVIEW.md'
      await agent(`Egészítsd ki (append) a "${ABS}/_AUDIT/${fname}" review-dokumentumot (ha nincs, hozd létre megfelelő fejléccel) az alábbi, DÖNTÉST igénylő találatokkal — egy "## Deep-audit kör ${round}" szakasz alatt, tételenként: dimenzió, fájl/hely, probléma, javaslat, forrás. NE módosíts tananyag-forrásfájlt, csak ezt a review-doksit.
TÉTELEK (JSON): ${JSON.stringify(items.map((f) => ({ dimension: f.dimension, file: f.file, location: f.location, issue: f.issue, recommendation: f.recommendation, sources: f.sources })))}
Add vissza ok + detail.`, { schema: OPRESULT, phase: 'Verify', label: `route:${doc}`, agentType: 'claude' })
    }
  }

  if (DRY_RUN) { log(`[DRY RUN] Kör ${round}: ${confirmed.length} megerősített javítandó (nem alkalmazva), ${toReview.length} review-be írva.`); continue }
  if (confirmed.length === 0) { log(`Kör ${round}: nincs megerősített auto-javítás.`); continue }

  // ---- 4) FIX — dimenziónként, fájlonként; majd 5) GATE + 6) COMMIT dimenziónként ----
  const byDim = {}
  for (const f of confirmed) { (byDim[f.dimension] = byDim[f.dimension] || []).push(f) }
  const dims = Object.keys(byDim).sort()

  for (const dim of dims) {
    phase('Fix')
    const dimFindings = byDim[dim]
    // fájlonként csoportosít (a "program" hatókörűeket külön kezeljük, fájlonként a recommendation szerint)
    const byFile = {}
    for (const f of dimFindings) { const key = f.file && f.file !== 'program' ? f.file : `__program__:${(f.location || f.issue).slice(0, 30)}`; (byFile[key] = byFile[key] || []).push(f) }
    const fileKeys = Object.keys(byFile)

    const fixResults = []
    const fxBatch = 6
    const fileThunks = fileKeys.map((key) => () => {
      const items = byFile[key]
      const target = key.startsWith('__program__') ? 'a finding(ek)ben megnevezett fájl(ok) (a recommendation szerint, jellemzően a Program terv vagy egy áttekintő)' : key
      return agent(`Deep-audit JAVÍTÓ vagy. Hajtsd végre az alábbi, MÁR MEGERŐSÍTETT (${dim} dimenziós) találatok javítását. Cél: ${target}.
Olvasd be a fájl(oka)t és a rubrikát (${RUBRIC}). Minden találatra: PRECÍZ, MINIMÁLIS Edit; a meglévő helyes tartalmat ne töröld; a pótolt/kiemelt részt **félkövérrel**; tegező, someres hangnem; tárgyi pontosságnál ToolSearch → WebSearch + forrás. Őrizd az integritást: páros félkövér, nincs ⟦?⟧, nincs törött link, cím↔fájlnév egyezés. Ne nyúlj a finding hatókörén kívüli tartalomhoz.
TALÁLATOK (JSON): ${JSON.stringify(items.map((f) => ({ file: f.file, location: f.location, issue: f.issue, recommendation: f.recommendation, sources: f.sources })))}
Ellenőrizd Read-del. Add vissza FIXREPORT (file, applied, changes[], skipped[]).`,
        { schema: FIXREPORT, phase: 'Fix', label: `fix:${dim}:${(key.split('/').pop() || key).slice(0, 18)}`, agentType: 'claude' })
    })
    for (let i = 0; i < fileThunks.length; i += fxBatch) {
      const r = await parallel(fileThunks.slice(i, i + fxBatch))
      fixResults.push(...r.filter(Boolean))
    }
    const applied = fixResults.reduce((a, b) => a + (b.applied || 0), 0)
    if (applied === 0) { log(`${dim}: 0 javítás alkalmazva — nincs commit.`); continue }

    // ---- 5) INTEGRITÁS-KAPU + 6) COMMIT (egy ügynök, szekvenciális → nincs git-verseny) ----
    phase('Commit')
    const commit = await agent(`Integritás-kapu + commit a deep-audit ${dim} dimenziójának javításaihoz (kör ${round}).
1. Futtass egy integritás-ellenőrzést a megváltozott fájlokon (git -C "${REPO}" diff --name-only). Minden megváltozott .md-re Node-dal ellenőrizd: (a) a félkövér ** párokban van-e (a *** vízszintes elválasztókat és a *dőlt***félkövér** szomszédosságot kezeld helyesen: előbb dobd a csak-*** sorokat, majd cseréld a "***"-t "** *"-ra, úgy számold a **-okat — páratlan = HIBA); (b) nincs ⟦?⟧ maradék jelölő; (c) nincs "file:///workspace" törött link.
2. Ha az integritás HIBÁS: NE commitolj; add vissza ok:false + detail (mely fájl, mi a hiba), hogy a következő kör javíthassa.
3. Ha OK: git -C "${REPO}" add -u -- "02 Tervezet" (és add hozzá az új fájlokat is, ha a javítás hozott létre ilyet), majd commitolj egy beszédes üzenettel:
   "fix(deep-audit ${dim}): <rövid összefoglaló> [kör ${round}]\n\n<dimenzió szerinti felsorolás>\n\nCo-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
   (a commit üzenetet írd FÁJLBA és git commit -F-fel add be, a magyar karakterek/zárójelek miatt). NE pushelj.
Add vissza ok + detail (a commit SHA és a megváltozott fájlok száma).`,
      { schema: OPRESULT, phase: 'Commit', label: `commit:${dim}`, agentType: 'claude' })
    commits.push({ round, dim, ok: commit && commit.ok, detail: commit && commit.detail })
    log(`${dim} commit: ${commit && commit.ok ? '✓ ' + commit.detail : '⛔ ' + (commit && commit.detail)}`)
  }
}

// ============================================================================
//  ZÁRÓ RIPORT
// ============================================================================
phase('Konvergencia')
const sevTally = (arr) => arr.reduce((a, f) => (a[f.severity] = (a[f.severity] || 0) + 1, a), {})
const summary = {
  rounds: round,
  converged: dryStreak >= DRY_STREAK,
  confirmedFixes: allConfirmed.length,
  bySeverity: sevTally(allConfirmed),
  routedToReview: routed,
  commits: commits.filter((c) => c.ok).length,
  dryRun: DRY_RUN,
}
await agent(`Írd meg / frissítsd a "${ABS}/_AUDIT/DEEP-AUDIT-REPORT.md" záró riportot (Write/Edit). Tartalom: a deep-audit futás összegzése.
ÖSSZEGZŐ ADATOK (JSON): ${JSON.stringify(summary)}
MEGERŐSÍTETT TALÁLATOK (JSON, dimenziónként csoportosítva, fájl+hely+probléma): ${JSON.stringify(allConfirmed.map((f) => ({ dimension: f.dimension, severity: f.severity, file: f.file, location: f.location, issue: f.issue })).slice(0, 200))}
Szakaszok: (1) Vezetői összefoglaló (hány kör, konvergált-e, hány javítás/commit, mi ment review-ba); (2) Megerősített javítások dimenziónként; (3) Review-be route-olt döntések (SAFEGUARDING-REVIEW / IDEOLOGY-GATE-REVIEW / ARCHITECTURE-REVIEW — utalás); (4) Következő lépések. Tegező-szakmai, magyar. NE módosíts tananyag-forrást, csak ezt a riportot. Add vissza ok + detail.`,
  { schema: OPRESULT, phase: 'Konvergencia', label: 'záró-riport', agentType: 'claude' })

log(`\n✅ DEEP-AUDIT kész: ${round} kör, ${summary.converged ? 'KONVERGÁLT' : 'maxRounds elérve'}, ${allConfirmed.length} megerősített javítás, ${commits.filter((c) => c.ok).length} commit, ${Object.values(routed).reduce((a, b) => a + b, 0)} review-be.`)
return summary
