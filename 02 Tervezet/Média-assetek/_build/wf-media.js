export const meta = {
  name: 'media-asset-register',
  description: 'Precíz média-asset kinyerés + 2 körös validálás + dedup + 5-dim audit → regiszter',
  phases: [
    { title: 'Kinyerés+Validálás' },
    { title: 'Dedup' },
    { title: 'Audit' },
    { title: 'Szekció-írás' },
  ],
}

// ---------- FÁJL-LISTÁK (literál, nincs felderítő-SPOF) ----------
const LESSONS = [
  "MODULOK/M0/M0_ONLINE_LECKE/M0.1 – „Üdv a képzésben!” – Éves útiterv & mi köze hozzám.md",
  "MODULOK/M0/M0_ONLINE_LECKE/M0.2 – „Madrich, nem terapeuta” – szerepek és elvárások.md",
  "MODULOK/M0/M0_ONLINE_LECKE/M0.3 – „Hogyan működik a Moodle _ H5P _ gate_”.md",
  "MODULOK/M0/M0_ONLINE_LECKE/M0.4 – „Dugma ishit az online térben + bemutatkozó fórum”.md",
  "MODULOK/M1/M1_ONLINE_LECKE/M1.1 – Johari-ablak – vakfoltjaim felismerése.md",
  "MODULOK/M1/M1_ONLINE_LECKE/M1.2 – Megfigyelés ≠ értelmezés.md",
  "MODULOK/M1/M1_ONLINE_LECKE/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést_.md",
  "MODULOK/M1/M1_ONLINE_LECKE/M1.4 – Miniszituációk_ „Mondd el SBI-ben”.md",
  "MODULOK/M2/M2_ONLINE_LECKE/M2.1 – Ki vagyok én madrichként_ – identitás-körök.md",
  "MODULOK/M2/M2_ONLINE_LECKE/M2.2 – Értékeim mint iránytű.md",
  "MODULOK/M2/M2_ONLINE_LECKE/M2.3 – Somer 3 pillére – mini-kapszula.md",
  "MODULOK/M2/M2_ONLINE_LECKE/M2.4 – Reflektív napló & határok_ „A dugma ishit nem terapeuta”.md",
  "MODULOK/M3/M3_ONLINE_LECKE/M3.1 – „Történetek egy kvucáról” – Tuckman-szakaszok felismerése.md",
  "MODULOK/M3/M3_ONLINE_LECKE/M3.2 – „Parparim, Kivsza, Leviatan, Zorea” – 4 kvuca, 4 világ.md",
  "MODULOK/M3/M3_ONLINE_LECKE/M3.3 – „Gyerekvédelem 101” – red flag felismerése & első lépések.md",
  "MODULOK/M3/M3_ONLINE_LECKE/M3.4 – „Do _ Don’t madrichként” – határok, red flag-ek és modulproduktum.md",
  "MODULOK/M4/M4_ONLINE_LECKE/M4.1 – Mit üzen a testem_ – Nonverbális kiállás.md",
  "MODULOK/M4/M4_ONLINE_LECKE/M4.2 – Aktív hallgatás & visszatükrözés.md",
  "MODULOK/M4/M4_ONLINE_LECKE/M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md",
  "MODULOK/M4/M4_ONLINE_LECKE/M4.4 – 45 mp-es peula-pitch – vázlat egy konkrét kvucára.md",
  "MODULOK/M5/M5_ONLINE_LECKE/M5.1 – Mi a nonformális nevelés_ – Suli _ Somer _ random.md",
  "MODULOK/M5/M5_ONLINE_LECKE/M5.2 – Feladat → módszer döntési fa – Mit választok először_.md",
  "MODULOK/M5/M5_ONLINE_LECKE/M5.3 – Hogyan tanulunk tényleg_ – Gyakorlás, visszahívás, spacing.md",
  "MODULOK/M5/M5_ONLINE_LECKE/M5.4 – „Cél–kvuca–módszer mini-táblázat” – saját adatbázisod madrichként.md",
  "MODULOK/M6/M6_ONLINE_LECKE/M6.1 – „Játék-kategóriák 4 kvucára”.md",
  "MODULOK/M6/M6_ONLINE_LECKE/M6.2 – „Történet, mint tükör”.md",
  "MODULOK/M6/M6_ONLINE_LECKE/M6.3 – „Kézműves, ami tanít is”.md",
  "MODULOK/M6/M6_ONLINE_LECKE/M6.4 – „Döntési szcenáriók_ mit választanál_”.md",
  "MODULOK/M7/M7_ONLINE_LECKE/M7.1 – „Ez még csak vágy, nem cél” – SMART nevelési cél someres módra.md",
  "MODULOK/M7/M7_ONLINE_LECKE/M7.2 – „Nem csak játék, hanem peula” – 11 tervezési pont & AI-támogatás.md",
  "MODULOK/M7/M7_ONLINE_LECKE/M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség.md",
  "MODULOK/M7/M7_ONLINE_LECKE/M7.4 – „Peula v2 + AI” – modulproduktum váz.md",
  "MODULOK/Z/Z_ONLINE_LECKE/Z.1 – „Visszanéző tükör” – M0–M7 timeline.md",
  "MODULOK/Z/Z_ONLINE_LECKE/Z.2 – „Tanultam valamit_!” – saját tanulási pillanataim.md",
  "MODULOK/Z/Z_ONLINE_LECKE/Z.3 – „Híd a terepre” – következő lépések.md",
  "MODULOK/Z/Z_ONLINE_LECKE/Z.4 – „Záró reflexió + képzés feedback”.md",
]
const PEULAS = [
  "MODULOK/M0/M0_PEULA/M0.A – „Kickoff & ismerkedés + közös keret”.md",
  "MODULOK/M1/M1_PEULA/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md",
  "MODULOK/M1/M1_PEULA/M1.B – SBI-lab – Smiley-től a használható visszajelzésig (45’).md",
  "MODULOK/M1/M1_PEULA/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md",
  "MODULOK/M2/M2_PEULA/M2.A – Identitás-körök élőben – mit mutatok magamból_  (45’).md",
  "MODULOK/M2/M2_PEULA/M2.B – Somer-értékek a gyakorlatban – döntések, amelyek tanítanak.md",
  "MODULOK/M2/M2_PEULA/M2.F – Felzárkóztató peula – Identitás, értékek, pillérek, személyes példamutatás (Study Lab).md",
  "MODULOK/M3/M3_PEULA/M3.A – Találd ki, hol tart a kvuca! – Történetek Tuckman szemüvegén át.md",
  "MODULOK/M3/M3_PEULA/M3.B – Red flag vagy nem_ – Miniszínház & lépés-térkép.md",
  "MODULOK/M3/M3_PEULA/M3.F – Felzárkóztató peula – Kvucadinamika & gyerekvédelem (Study Lab).md",
  "MODULOK/M4/M4_PEULA/M4.A – „Állj oda!” – Kiállás & jelenlét a térben.md",
  "MODULOK/M4/M4_PEULA/M4.B –  „Mit és hogyan kérdezek_” – Kérdezés & pitch gyakorlása.md",
  "MODULOK/M4/M4_PEULA/M4.F – Felzárkóztató peula – Test, hang, kérdések & pitch (Study Lab).md",
  "MODULOK/M5/M5_PEULA/M5.A – „Suli, Somer vagy random_” – Hol tanulunk és hogyan_.md",
  "MODULOK/M5/M5_PEULA/M5.B – „Tervezek egy nonformális peula-részletet” – hogy tényleg tanuljunk is.md",
  "MODULOK/M5/M5_PEULA/M5.F – Felzárkóztató peula – Suli, Somer & tanulástan (Study Lab).md",
  "MODULOK/M6/M6_PEULA/M6.A – Peula_ „Játék-labor 4 kvucára” (45’).md",
  "MODULOK/M6/M6_PEULA/M6.B – Peula_ „Játéklap workshop – saját eszköz tervezése” (45’).md",
  "MODULOK/M6/M6_PEULA/M6.F – Felzárkóztató peula – Toolbox & játéklap (Study Lab).md",
  "MODULOK/M7/M7_PEULA/M7.A – Célból peula – SMART & 11 pont élőben.md",
  "MODULOK/M7/M7_PEULA/M7.B – Peula v2 & Zmán Kvucá – amikor a papír találkozik a valósággal.md",
  "MODULOK/M7/M7_PEULA/M7.F – Felzárkóztató peula – Peula & Zmán Kvucá (Study Lab).md",
  "MODULOK/Z/Z_PEULA/Z.A – „Mit viszek magammal_” – Záró kvuca-peula.md",
]
const HUBS = [
  "MODULOK/M0/M0 – „Kickoff, keret, technika”.md",
  "MODULOK/M1/M1 – „Vakfolt, tükör, feedback” – Önismeret & visszajelzés_ Johari + SBI .md",
  "MODULOK/M2/M2 – „Ki vagyok madrichként_” – Identitás, Somer-értékek és dugma ishit.md",
  "MODULOK/M3/M3 – „Kvuca, red flag, felelősség” – Csoportdinamika, korosztályok és gyerekvédelem .md",
  "MODULOK/M4/M4 – „Hallható és érthető vagyok_” – Kiállás, kapcsolódás & kérdezéstechnika.md",
  "MODULOK/M5/M5 – „Ez most játék vagy tanulás_” – Nonformális nevelés, módszerválasztás & tanulástan.md",
  "MODULOK/M6/M6 – „Toolbox_ játék, történet, kézműves & inkluzivitás”.md",
  "MODULOK/M7/M7 – „Peula a papírtól a valóságig” – Programírás, Zmán Kvucá & AI-támogatott tervezés.md",
  "MODULOK/Z/Z – „Zárás & híd a terepre”.md",
]

const FILES = [
  ...LESSONS.map(p => ({ path: p, kind: 'online-lecke' })),
  ...PEULAS.map(p => ({ path: p, kind: 'peula' })),
  ...HUBS.map(p => ({ path: p, kind: 'hub' })),
]

function moduleOf(p) { const m = p.match(/MODULOK\/(M\d|Z)\//); return m ? m[1] : 'EGYÉB' }
const ROOT = '02 Tervezet'

// ---------- KONTROLLÁLT SZÓKINCS ----------
const VOCAB = `assetType KÖTELEZŐ az alábbi enumból:
 narráció | beszélőfej-videó | interaktív-videó | animált-diagram | illusztráció | ikon-készlet | fotó-kép | hang-zene-SFX | felirat | leirat-transzkript | alt-szöveg | print-poszter | print-kártya | print-munkalap | egyéb
category KÖTELEZŐ: "digitális-generálandó" (narráció, videók, diagram, illusztráció, ikon, fotó, hang) | "szöveges-ekvivalens" (felirat, leirat, alt-szöveg) | "print-fizikai" (poszter, kártya, munkalap).
ID-séma: <egységkód>-<típusrövidítés>-<2 számjegy>, pl. M2.3-VID-01, M2.A-POSZ-02, M3-HUB-DIA-01.
Típusrövidítések: NAR(narráció) VID(videó) DIA(diagram) ILL(illusztráció) IKO(ikon) FOTO(fotó) HANG(hang) FEL(felirat) LEI(leirat) ALT(alt-szöveg) POSZ(poszter) KART(kártya) MUNK(munkalap) EGY(egyéb).`

const ASSET_ITEM = {
  type: 'object',
  required: ['assetId', 'assetType', 'category', 'location', 'contentSpec', 'purpose', 'provenance'],
  properties: {
    assetId: { type: 'string' },
    assetType: { type: 'string' },
    category: { type: 'string' },
    location: { type: 'string', description: 'pl. SLIDE 3 / "Mit látunk?" blokk / Branching node 2' },
    lineRef: { type: 'string', description: 'sor-szám vagy rövid idézet-horgony a forrásból' },
    title: { type: 'string', description: 'rövid, beszédes cím' },
    contentSpec: { type: 'string', description: 'PRECÍZ, de tömör leírás MIT kell generálni (1-3 mondat). NE a teljes verbatim szöveget — az a forrásban van a lineRef-en.' },
    purpose: { type: 'string', description: 'pedagógiai cél: miért kell ez az asset' },
    techSpec: { type: 'string', description: 'hossz/formátum/méret/hang/nyelv/arány' },
    a11y: { type: 'string', description: 'alt-szöveg / felirat / leirat igény; ha maga is a11y-asset: "—"' },
    provenance: { type: 'string', description: 'AI-generált | emberi-felvétel | stock | vegyes' },
    notes: { type: 'string' },
  },
}
const ASSETS_ARRAY = { type: 'array', items: ASSET_ITEM }

const EXTRACT_SCHEMA = {
  type: 'object',
  required: ['unitCode', 'assets'],
  properties: {
    unitCode: { type: 'string' },
    assets: ASSETS_ARRAY,
  },
}
const VALIDATE_SCHEMA = {
  type: 'object',
  required: ['unitCode', 'assets', 'changeLog'],
  properties: {
    unitCode: { type: 'string' },
    assets: ASSETS_ARRAY,
    changeLog: {
      type: 'array',
      items: {
        type: 'object',
        required: ['action', 'detail'],
        properties: { action: { type: 'string', description: 'hozzáadva | törölve(álpozitív) | javítva | spec-pótolva' }, assetId: { type: 'string' }, detail: { type: 'string' } },
      },
    },
  },
}
const DEDUP_SCHEMA = {
  type: 'object',
  required: ['bucket', 'groups'],
  properties: {
    bucket: { type: 'string' },
    groups: {
      type: 'array',
      items: {
        type: 'object',
        required: ['canonicalId', 'memberIds', 'reason'],
        properties: {
          canonicalId: { type: 'string', description: 'a megtartandó kanonikus asset ID' },
          memberIds: { type: 'array', items: { type: 'string' }, description: 'MIND, ami ezzel azonos/újrahasznosítás (a kanonikust is beleértve)' },
          reason: { type: 'string' },
          reuseNote: { type: 'string', description: 'hogyan tér el a felhasználás (ha egyáltalán)' },
        },
      },
    },
    note: { type: 'string' },
  },
}
const AUDIT_SCHEMA = {
  type: 'object',
  required: ['dimension', 'findings', 'summary'],
  properties: {
    dimension: { type: 'string' },
    findings: {
      type: 'array',
      items: {
        type: 'object',
        required: ['assetId', 'severity', 'issue'],
        properties: { assetId: { type: 'string' }, severity: { type: 'string', description: 'blokkoló | fontos | javasolt' }, issue: { type: 'string' }, fix: { type: 'string' } },
      },
    },
    summary: { type: 'string' },
  },
}

// ---------- tryAgent: 529-tűrő retry ----------
async function tryAgent(prompt, opts, tries = 4) {
  for (let i = 0; i < tries; i++) {
    const r = await agent(prompt, { ...opts, label: (opts.label || 'a') + (i ? `·r${i}` : '') })
    if (r) return r
  }
  return null
}

// ================= 1. KINYERÉS + 2 VALIDÁLÓ KÖR (pipeline) =================
phase('Kinyerés+Validálás')
log(`Média-asset kinyerés indul: ${FILES.length} fájl, fájlonként 1 kinyerés + 2 független validáló kör.`)

const COMMON = `A "${ROOT}" mappa egy magyar nyelvű Hasomer Hacair madrich-képzés tananyaga (Moodle/H5P online leckék + élő peulák).
Média-asset = MINDEN, amit le kell GYÁRTANI a tananyaghoz: narráció (hang), AI beszélő-fej videó, interaktív/animált videó, animált diagram/ábra, illusztráció/storyboard, ikon-készlet, fotó/kép, háttérzene/SFX, valamint a hozzájuk tartozó SZÖVEGES EKVIVALENSEK (felirat, leirat/transzkript, alt-szöveg), és a PRINT/fizikai anyagok (poszter, kártyaszett, munkalap, flipchart-sablon).
${VOCAB}`

const perFile = await pipeline(
  FILES,
  // --- STAGE 1: kinyerés ---
  async (item) => {
    const r = await tryAgent(
      `${COMMON}

FELADAT: Olvasd el TELJESEN ezt az EGY fájlt és nyerd ki belőle az ÖSSZES legyártandó média-asszetet, kihagyás nélkül.
Fájl: ${ROOT}/${item.path}
Típus: ${item.kind} | Modul: ${moduleOf(item.path)}

Módszer:
- Menj végig SLIDE-ról SLIDE-ra / blokkról blokkra. Keresd: "Narráció", "videó"/"beszélő fej", "Mit látunk?"/vizuális leírás, "diagram"/"görbe", "illusztráció"/"jelenet"/"storyboard", "ikon", "kép"/"fotó", "felirat"/"leirat", "alt-szöveg", peuláknál "poszter"/"kártya"/"flipchart"/"nyomtat"/"munkalap".
- MINDEN vizuálishoz, ami nem dekoratív, vegyél fel külön sort. Ha egy slide-nak van narrációja ÉS videója ÉS feliratja, az 3 külön asset (kapcsold össze a notes-ban).
- contentSpec = PRECÍZ, de tömör (mit kell generálni), NE a teljes verbatim szöveg. lineRef-be tedd a forrás-horgonyt (sor-szám vagy rövid idézet), hogy a teljes szöveg visszakereshető legyen.
- a11y mező: minden vizuálishoz írd be, kell-e alt-szöveg; minden videóhoz/hanghoz felirat+leirat.
- provenance: a beszélő-fej videók és illusztrációk jellemzően "AI-generált"; jelöld pontosan.
- Adj egyedi assetId-t az ID-séma szerint, az egységkódot (pl. ${moduleOf(item.path)}.x vagy ${moduleOf(item.path)}-HUB) a fájl fejlécéből vedd.

Csak a StructuredOutput-ot add vissza. Ha a fájlban TÉNYLEG nincs legyártandó média-asset, adj üres assets tömböt.`,
      { schema: EXTRACT_SCHEMA, label: `kinyer:${item.path.split('/').pop().slice(0, 18)}`, phase: 'Kinyerés+Validálás' },
    )
    if (!r) return { unitCode: '?', assets: [], _file: item.path, _kind: item.kind, _mod: moduleOf(item.path), _failed: true }
    return { ...r, _file: item.path, _kind: item.kind, _mod: moduleOf(item.path) }
  },
  // --- STAGE 2: validálás 1. kör (completeness + accuracy + spec) ---
  async (s1, item) => {
    if (s1._failed) return s1
    const r = await tryAgent(
      `${COMMON}

FELADAT: FÜGGETLEN VALIDÁLÁS (1. kör). Itt a fájl, és egy korábbi ágens által kinyert asset-lista. A te dolgod hibát találni és JAVÍTANI:
Fájl: ${ROOT}/${item.path}

Kinyert lista (JSON):
${JSON.stringify(s1.assets, null, 1)}

Ellenőrizd és javítsd:
1) HIÁNYZÓ assetek (a forrásban van, a listából kimaradt) → add hozzá.
2) ÁLPOZITÍV (felvett, de valójában nem legyártandó asset, pl. tiszta szöveges UI vagy dekoráció) → töröld.
3) PONTOSSÁG: location/lineRef tényleg a forrásra mutat? contentSpec hűen tükrözi a forrást? purpose helyes? → javítsd.
4) SPEC-TELJESSÉG: minden vizuálisnak van értelmes techSpec + a11y? minden videónak/hangnak felirat+leirat az a11y-ban? provenance kitöltve? → pótold.
5) ID-konzisztencia és egyediség az ID-séma szerint.

Add vissza a TELJES, javított asset-listát (assets) + a changeLog-ot (mit változtattál és miért). Csak StructuredOutput.`,
      { schema: VALIDATE_SCHEMA, label: `val1:${item.path.split('/').pop().slice(0, 16)}`, phase: 'Kinyerés+Validálás' },
    )
    if (!r) return s1
    return { ...s1, assets: r.assets, _cl1: r.changeLog }
  },
  // --- STAGE 3: validálás 2. kör (adverzariális dupla-ellenőrzés) ---
  async (s2, item) => {
    if (s2._failed) return s2
    const r = await tryAgent(
      `${COMMON}

FELADAT: FÜGGETLEN VALIDÁLÁS (2. kör, adverzariális). A lista már átment egy validáláson; a te dolgod a maradék hibát megtalálni — légy szkeptikus, de NE ronts el jót.
Fájl: ${ROOT}/${item.path}

Jelenlegi lista (JSON):
${JSON.stringify(s2.assets, null, 1)}

Fókusz: (a) maradt-e MÉG kimaradt asset (különösen rejtett vizuálisok, háttérzene, feliratok, peula-print)? (b) van-e még pontatlan lineRef/contentSpec? (c) van-e még a11y- vagy techSpec-hiány? (d) ID-ütközés?
Csak akkor változtass, ha biztos a hiba. Add vissza a TELJES, véglegesített assets-listát + changeLog. Csak StructuredOutput.`,
      { schema: VALIDATE_SCHEMA, label: `val2:${item.path.split('/').pop().slice(0, 16)}`, phase: 'Kinyerés+Validálás' },
    )
    if (!r) return s2
    return { ...s2, assets: r.assets, _cl2: r.changeLog }
  },
)

const ok = perFile.filter(Boolean)
const failed = ok.filter(x => x._failed).map(x => x._file)
let allAssets = []
for (const f of ok) {
  for (const a of (f.assets || [])) {
    allAssets.push({ ...a, _file: f._file, _kind: f._kind, _mod: f._mod })
  }
}
log(`Kinyerve+validálva: ${allAssets.length} asset, ${ok.length - failed.length}/${FILES.length} fájl OK${failed.length ? `, SIKERTELEN: ${failed.length}` : ''}.`)

// ================= 2. DEDUPLIKÁCIÓ (típus-bucketenként, barrier) =================
phase('Dedup')
const BUCKETS = {
  'Narráció & hang': ['narráció', 'hang-zene-SFX'],
  'Videó': ['beszélőfej-videó', 'interaktív-videó'],
  'Diagram & ábra': ['animált-diagram'],
  'Illusztráció & storyboard': ['illusztráció'],
  'Ikon': ['ikon-készlet'],
  'Fotó & kép': ['fotó-kép'],
  'Szöveges ekvivalens (a11y)': ['felirat', 'leirat-transzkript', 'alt-szöveg'],
  'Print / fizikai': ['print-poszter', 'print-kártya', 'print-munkalap'],
}
function compact(a) {
  return { id: a.assetId, type: a.assetType, mod: a._mod, file: a._file.split('/').pop(), loc: a.location, title: a.title || '', spec: (a.contentSpec || '').slice(0, 260) }
}
const bucketKeys = Object.keys(BUCKETS)
const dedupResults = await parallel(bucketKeys.map(bk => async () => {
  const types = BUCKETS[bk]
  const rows = allAssets.filter(a => types.includes(a.assetType)).map(compact)
  if (rows.length < 2) return { bucket: bk, groups: [], note: 'kevés elem, nincs dedup' }
  const r = await tryAgent(
    `Média-asset deduplikáció. Az alábbi azonos kategóriájú ("${bk}") assetek közül keresd meg azokat, amelyek VALÓJÁBAN UGYANAZT az egy legyártandó médiát jelentik (ugyanaz a narráció/ikon/diagram/sablon több helyen újrahasználva), vagy gyakorlatilag azonosak és egyszer kell legyártani.
Légy konzervatív: csak akkor csoportosíts, ha tényleg egyszer kellene legyártani és újrahasználni. A pusztán "hasonló téma" NEM duplikátum.
Minden csoporthoz: canonicalId (a megtartandó), memberIds (mind, a kanonikussal együtt), reason, reuseNote.

Assetek (JSON):
${JSON.stringify(rows, null, 1)}

Csak StructuredOutput.`,
    { schema: DEDUP_SCHEMA, label: `dedup:${bk.slice(0, 14)}`, phase: 'Dedup' },
  )
  return r || { bucket: bk, groups: [], note: 'dedup sikertelen' }
}))

// dedup-annotáció a sorokra
const dedupOf = {} // assetId -> {canonical, reuseNote}
for (const dr of dedupResults.filter(Boolean)) {
  for (const g of (dr.groups || [])) {
    for (const mid of (g.memberIds || [])) {
      if (mid !== g.canonicalId) dedupOf[mid] = { canonical: g.canonicalId, reuseNote: g.reuseNote || g.reason || '' }
    }
  }
}
const dupCount = Object.keys(dedupOf).length
const uniqueCount = allAssets.length - dupCount
log(`Dedup kész: ${allAssets.length} sorból ${dupCount} újrahasznosítás → ${uniqueCount} EGYEDI legyártandó asset.`)

// ================= 3. AUDIT (5 dimenzió, párhuzamos) =================
phase('Audit')
const compactFull = allAssets.map(a => ({ id: a.assetId, type: a.assetType, cat: a.category, mod: a._mod, loc: a.location, spec: (a.contentSpec || '').slice(0, 180), tech: a.techSpec || '', a11y: a.a11y || '', prov: a.provenance || '' }))
const AUDIT_DIMS = [
  { key: 'Akadálymentesség (WCAG 2.2)', task: 'Minden NEM-dekoratív vizuálisnak (illusztráció, diagram, ikon, fotó, videó) van értelmes alt-szöveg / hangleírás specje? Minden videónak/hangnak van felirat ÉS leirat/transzkript? Jelöld azokat, ahol az a11y hiányzik vagy üres. severity: blokkoló ha videó/hang felirat nélkül; fontos ha kép alt nélkül.' },
  { key: 'AI-jelölés & jogtisztaság (EU AI Act 50. cikk, IP)', task: 'Minden AI-generált asset (provenance=AI) jelölve van-e gépi olvasható AI-jelölésre? Van-e stock/3rd-party IP-kockázat (zene, fotó, karakterek)? Jelöld a hiányzó AI-jelölést és a jogi kockázatot.' },
  { key: 'Produkciós megvalósíthatóság & alulspecifikáltság', task: 'Mely assetek alulspecifikáltak a legyártáshoz (hiányzó hossz/arány/stílus/hang)? Mi köthető batch-be (azonos stílusú ikon/illusztráció-készletek)? Jelöld a hiányos technikai specet.' },
  { key: 'Stílus- & hang-konzisztencia', task: 'Konzisztens-e a vizuális stílus és a narrátor-hang az egész tananyagban? Hol térnek el indokolatlanul (eltérő illusztrációs stílus, eltérő narrátor-hangnem)? Jelöld a konzisztencia-töréseket.' },
  { key: 'Tartalmi & terminológiai helyesség', task: 'Az asset-tartalmak (contentSpec) helyesek és ellentmondásmentesek? Használják a kánoni terminológiát (cionizmus NEM zionizmus; Hasomer Hacair; Somer; kvuca; dugma ishit; Leviatan)? Jelöld az ellentmondást, téves célt vagy terminológia-hibát.' },
]
const auditResults = await parallel(AUDIT_DIMS.map(d => async () => {
  const r = await tryAgent(
    `Média-asset regiszter AUDIT — dimenzió: "${d.key}".
${d.task}
Csak valós, konkrét megállapításokat sorolj fel (assetId-vel). Ha egy dimenzió tiszta, adj üres findings-ot és írd meg a summary-ban.

Asset-regiszter (JSON, tömörített):
${JSON.stringify(compactFull, null, 1)}

Csak StructuredOutput.`,
    { schema: AUDIT_SCHEMA, label: `audit:${d.key.slice(0, 16)}`, phase: 'Audit' },
  )
  return r || { dimension: d.key, findings: [], summary: 'audit sikertelen' }
}))

// audit-annotáció a sorokra
const auditOf = {} // assetId -> [{dim, severity, issue, fix}]
for (const ar of auditResults.filter(Boolean)) {
  for (const f of (ar.findings || [])) {
    (auditOf[f.assetId] = auditOf[f.assetId] || []).push({ dim: ar.dimension, severity: f.severity, issue: f.issue, fix: f.fix || '' })
  }
}
const auditTotal = Object.values(auditOf).reduce((s, x) => s + x.length, 0)
log(`Audit kész: ${auditTotal} megállapítás ${Object.keys(auditOf).length} asseten.`)

// ================= 4. ANNOTÁLT SOROK ÖSSZEÁLLÍTÁSA (determinisztikus, nincs writer-ágens) =================
phase('Szekció-írás')
function annotRow(a) {
  const d = dedupOf[a.assetId]
  const au = auditOf[a.assetId] || []
  return {
    assetId: a.assetId, assetType: a.assetType, category: a.category, mod: a._mod,
    file: a._file, fileShort: a._file.split('/').pop(), kind: a._kind,
    location: a.location, lineRef: a.lineRef || '',
    title: a.title || '', contentSpec: a.contentSpec, purpose: a.purpose,
    techSpec: a.techSpec || '', a11y: a.a11y || '', provenance: a.provenance || '',
    notes: a.notes || '',
    dedup: d ? `🔁 = ${d.canonical}${d.reuseNote ? ' (' + d.reuseNote + ')' : ''}` : '',
    audit: au.map(x => `${x.severity === 'blokkoló' ? '⛔' : x.severity === 'fontos' ? '⚠️' : 'ℹ️'} ${x.issue}${x.fix ? ' → ' + x.fix : ''}`).join(' · '),
  }
}
const rowsOut = allAssets.map(annotRow)
// mely fájlok vannak képviselve / kiestek
const repFiles = new Set(allAssets.map(a => a._file))
const missingFiles = FILES.map(f => f.path).filter(p => !repFiles.has(p))
log(`Annotált sorok: ${rowsOut.length}. Képviselt fájl: ${repFiles.size}/${FILES.length}. Kiesett: ${missingFiles.length}`)

// ================= VISSZATÉRÉS: teljes sor-lista + összegzés =================
const byType = {}
const byCat = {}
const byMod = {}
const byProv = {}
for (const a of allAssets) {
  byType[a.assetType] = (byType[a.assetType] || 0) + 1
  byCat[a.category] = (byCat[a.category] || 0) + 1
  byMod[a._mod] = (byMod[a._mod] || 0) + 1
  const pv = /AI/i.test(a.provenance || '') ? 'AI-generált' : (a.provenance || 'ismeretlen')
  byProv[pv] = (byProv[pv] || 0) + 1
}
return {
  stats: { total: allAssets.length, unique: uniqueCount, duplicates: dupCount, filesRepresented: repFiles.size, filesTotal: FILES.length, missingFiles, byType, byCat, byMod, byProv },
  assets: rowsOut,
  dedup: dedupResults.filter(Boolean).map(d => ({ bucket: d.bucket, groups: (d.groups || []).map(g => ({ canonicalId: g.canonicalId, memberIds: g.memberIds, reason: g.reason, reuseNote: g.reuseNote || '' })) })),
  audit: auditResults.filter(Boolean).map(a => ({ dimension: a.dimension, summary: a.summary, findings: a.findings || [] })),
}
