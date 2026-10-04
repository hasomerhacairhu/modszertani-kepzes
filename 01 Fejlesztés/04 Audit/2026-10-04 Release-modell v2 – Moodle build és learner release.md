# Release-modell v2 — Moodle build és learner release (2026-10-04)

> **Tervezési jegyzőkönyv, nem kánon.** A kánoni szöveg a `02 Tervezet/RELEASE-READINESS.md`, az
> `Emberi jóváhagyás szükséges.md` 10. szakasza és a `tools/content_integrity.py`. Ez a dokumentum rögzíti, miért és
> hogyan változott a modell, és mi maradt a következő lépésekre. Döntések: `2026-10-04 Projektgazdai döntések –
> release-modell.md` (RM-D1…D6), Q-REL-1…4, Q-MED-1 (`2026-10-04 Projektgazdai döntések – összesítő 24 kérdése.md`).

## 1. Két kérdés, két verdikt

| Kérdés | Verdikt | Állapotok |
|---|---|---|
| Felépíthetjük-e már Moodle-ban? | `MOODLE-BUILD-VERDICT` | `NOT_READY` / `READY_FOR_STAGING_BUILD` |
| Odaadhatjuk-e valódi résztvevőknek kontrollált pilotként? | `LEARNER-RELEASE-VERDICT` | `NO-GO` / `CONTENT_READY / MEDIA_PENDING` / `READY_FOR_CONTROLLED_PILOT` |

Csupasz `READY` állapot nincs (RM-D3). A régi `RELEASE-VERDICT` sor egy release-ciklusig kompatibilitási alias, az
értéke a `LEARNER-RELEASE-VERDICT` értéke.

**A régi modell hibája:** egyetlen verdikt volt, és ebbe a build és a runtime kimenetei (52 `BUILD_OUTPUT`, 17
`RUNTIME_OUTPUT`) is blokkerként számítottak. A buildet tehát az a bizonyíték blokkolta, amelyet csak maga a build
állíthat elő. Ezen felül: kézzel írt harmadik állapot („READY WITH NAMED HUMAN GATES”); egész fájlos checklist-blokkolás
vegyes tartalommal; a program-transzfer release-blokkerként (a Q-REL-1-gyel ellentétben); hamis zöld lehetőségek
(kitöltött verziósorok futatlan tesztekkel; az R2-jelölő kivétele nyitott jogi alkapuval; ERROR mellett `READY`);
szabály-szintű médiakapu az asset-szintű kánon mellett; és a gép által nem látott valódi build-spec hiányok.

## 2. Az állapotgép

### 2.1. `MOODLE-BUILD-VERDICT`

`NOT_READY`, ha bármelyik BUILD-SPEC kategória nem üres; különben `READY_FOR_STAGING_BUILD`.

| BUILD-SPEC kategória | Mit jelent | Gépi forrás |
|---|---|---|
| `ERROR` | bármely objektív integritási hiba (G7) | a `content_integrity.py` ellenőrzései |
| `SOURCE-PLACEHOLDERS` | `⟬KITÖLTENDŐ⟭` a modulforrásban (G4a) | `02 Tervezet/Modulok/**` |
| `HUMAN-DECISIONS` | nyitott (nem `LEZÁRVA` = nem `OWNER_DECIDED`) release-regiszterbeli HUM-döntés | `Emberi jóváhagyás szükséges.md` |
| `MANIFEST-OPEN` | nem implementálható activity-definíció | `BUILD_SPEC_OPEN` sorok a manifest „Nyitott build-spec tételek” táblájában |
| `CHECKLIST-BUILD` | `gate: build` jelölésű nyitott checklist-tétel | a négy checklist-forrás |
| `CHECKLIST-UNCLASSIFIED` | jelölés nélküli nyitott checklist-tétel — hibabiztos: amíg a leltár be nem sorolja, nem tudjuk, hogy build-feltétel-e | ugyanott |
| `MEDIA-REQUIRED-WITHOUT-FALLBACK` | release-kötelező (A fázisú) asset nyitott médiakapun, elfogadott fallback nélkül | a média-manifest assetjei (lásd 6.) |

A build-verdikt **soha nem** olvassa: `BUILD_OUTPUT`, környezeti rekord, runtime-tesztek, a11y-renderteszt,
`FINAL_RELEASE_QA`, sign-off, program-transzfer.

### 2.2. `LEARNER-RELEASE-VERDICT`

1. `NO-GO`, ha a build-verdikt `NOT_READY`, vagy bármelyik learner-release kategória nem üres.
2. Különben `CONTENT_READY / MEDIA_PENDING`, ha van nyitott MEDIA-RELEASE tétel.
3. Különben `READY_FOR_CONTROLLED_PILOT`.

| Learner-release kategória | Mit jelent | Gépi forrás |
|---|---|---|
| `POST-BUILD: BUILD-OUTPUT` | Moodle `cmid` még nincs rögzítve | `BUILD_OUTPUT` sorok, activity manifest |
| `POST-BUILD: ENVIRONMENT-RECORD` | a célkörnyezet verziói még nincsenek rögzítve (a build 1. lépésének kimenete) | `RUNTIME_OUTPUT` sorok, runtime acceptance |
| `POST-BUILD: RUNTIME-TESTS` | P0- és a11y-teszt még nem `RUNTIME_VERIFIED` | `RT-*` sorok `IMPLEMENTATION_TEST_REQUIRED` állapottal, runtime acceptance „Teszt-állapot” táblája |
| `POST-BUILD: CHECKLIST` | `gate: post-build` jelölésű nyitott tétel | checklistek, `RELEASE-READINESS.md` |
| `RELEASE-EVIDENCE` | `gate: release-evidence` jelölésű nyitott tétel | checklistek |
| `FINAL-RELEASE-QA` | `gate: human-qa` jelölésű nyitott tétel (Memuna végső átnézése, DPO release-ellenőrzése, független a11y pre-flight) | checklistek |
| `SIGNOFF` | `gate: signoff` jelölésű nyitott tétel (pl. a `CONTROLLED_PILOT` go/no-go döntése) | checklistek, `RELEASE-READINESS.md` |
| `MEDIA-RELEASE` (→ `MEDIA_PENDING`) | release-kötelező asset nyitott médiakapun, átmeneti fallbackkel; nyitott HUM-MEDIA döntés | média-manifest; HUM |

### 2.3. Invariánsok (selftest védi)

1. `ERROR` mellett a build-verdikt `NOT_READY`, tehát a learner-verdikt `NO-GO`.
2. Ha a learner-verdikt nem `NO-GO`, akkor a build-verdikt `READY_FOR_STAGING_BUILD`.
3. A program-transzfer (`LIFECYCLE`) egyik verdiktet sem befolyásolja.
4. Jelölés nélküli checklist-tétel blokkolja a buildet (hibabiztos), amíg a leltár be nem sorolja.
5. Kitöltött környezeti rekord mellett is `NO-GO`, amíg runtime-teszt `IMPLEMENTATION_TEST_REQUIRED`.
6. Az R2-jelölő kivétele nem zárja a jogi médiakaput, amíg a `RIGHTS-EVIDENCE.md` J1/J2/V1/V3 alkapuja `HIÁNYZIK`.
7. Minden régi blokker pontosan egy új kategóriába kerül (lásd 7.).

### 2.4. Életciklus (Q-REL-1, RM-D1, RM-D3)

`INTERNAL_STAGING → CONTROLLED_PILOT → GENERAL_RELEASE → PROGRAM_TRANSFER_VALIDATED`

| Fázis | Belépés feltétele | Ki rögzíti |
|---|---|---|
| `INTERNAL_STAGING` | `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` | LMS-gazda, a release-jegyzőkönyvben |
| `CONTROLLED_PILOT` | `LEARNER-RELEASE-VERDICT: READY_FOR_CONTROLLED_PILOT` + go/no-go döntés | release owner, a release-jegyzőkönyvben |
| `GENERAL_RELEASE` | a pilot-findingok javítva, újratesztelve, go/no-go — nem repo-verdikt | release owner |
| `PROGRAM_TRANSFER_VALIDATED` | a 6 valós terepi peula + mentori ciklus lefutott | programvezető |

A fázisokat ember rögzíti; a gép csak a két verdiktet és a nyitott `LIFECYCLE` tételt jelzi.

### 2.5. Döntési és QA-lánc (Q-REL-3, RM-D2)

`OWNER_DECIDED → IMPLEMENTED → RUNTIME_VERIFIED → FINAL_RELEASE_QA → RELEASE_APPROVED`; mellette `PROPOSED`,
`SUPERSEDED`, `REOPENED`. A `SPEC_QA` korai vétó vagy tanácsadó ellenőrzés, nem build-kapu. **Átmenet:** a HUM-fejlécek
ma `LEZÁRVA` jelölést viselnek; ez az `OWNER_DECIDED`-nak felel meg, és a buildhez elég. A fejlécek átállítása a láncra
külön, későbbi lépés (a parser ma a `LEZÁRVA` szót olvassa, lásd 10.).

## 3. Jelölési konvenciók

- **Checklist-tétel osztálya:** a `- [ ]` sor végén HTML-komment, pl. `<!-- gate: build -->`. Értékek: `build`,
  `post-build`, `release-evidence`, `human-qa`, `signoff`, `lifecycle`; mellé vesszővel a `repo-fixable` jelző
  (`<!-- gate: build, repo-fixable -->`). Csak `repo-fixable` jelzővel, osztály nélkül a tétel `build` (hibabiztos).
  Jelölés nélkül: `CHECKLIST-UNCLASSIFIED`. A leltár kategóriái: BUILD BLOCKER = `build`; POST-BUILD TEST =
  `post-build`; RELEASE EVIDENCE = `release-evidence` (vagy `signoff`, ha szervezeti jóváhagyás); HUMAN QA =
  `human-qa`; REPO-FIXABLE = jelző.
- **Runtime-tesztek:** a `LMS – H5P runtime acceptance.md` „Teszt-állapot” táblája; soronként `RT-P0-nn` vagy
  `RT-A11Y-nn`, állapot `IMPLEMENTATION_TEST_REQUIRED` → `RUNTIME_VERIFIED` (dátummal, verzióval, bizonyítékkal).
- **Build-spec nyilvántartás:** a `LMS – activity manifest.md` „Nyitott build-spec tételek” táblája; soronként
  `BSPEC-nn`, állapot `BUILD_SPEC_OPEN` → `BUILD_SPEC_RESOLVED` (a sor marad, mint bizonyíték).
- **Média:** asset-szintű mezők a média-manifestben: `release_phase` (`A`/`B`/`C`), `fallback` (az elfogadott
  fallback leírása), `fallback_final` (igaz, ha a fallback végleges helyettesítés). Ma egyik sincs a manifestben (lásd
  6. és 10.).

## 4. A G1–G8 kapuk besorolása

| Kapu | Spec-rész (build) | Build után / runtime | Bizonyíték / QA / sign-off |
|---|---|---|---|
| G1 Gyermekvédelem | HUM-SAFE (lezárva), safeguarding-szabályok a specben | — | Memuna végső átnézése: `FINAL-RELEASE-QA` |
| G2 Adatvédelem | HUM-PRIV (lezárva), activity-szintű adatleltár (Moodle-szerepkör/capability), tájékoztató szövege | láthatósági és szerepkör-tesztek | DPO release-ellenőrzése: `FINAL-RELEASE-QA` |
| **G3a / G3b** | célkörnyezeti paraméterek: H5P-integráció, content type-lista, plugin-lista (RM-D6), MCP, mechanizmusok tartalékúttal | környezeti rekord (17) + 23 P0-teszt | — |
| **G4a / G4b** | nincs `⟬KITÖLTENDŐ⟭` és törött link a forrásban | a renderelt learner-facing felület visszaauditja | — |
| **G5a / G5b** | a11y-spec + build-beállítások (autoplay, Auto continue, iframe-cím, AD-besorolás) | renderteszt (12 a11y-pont; RT 13, 14, 22, 23) | független pre-flight + a11y-gazda: `FINAL-RELEASE-QA` |
| G6 Mozgalmi tartalom | HUM-SOMER (lezárva) | — | — |
| G7 Regresszió | CI, tesztek, `ERROR` = 0 | — | — |
| G8 Ütemezés és support | naptár, Q-REL-4 | a „Segítség és kapcsolatok” blokk megjelenése (RT-P0-17) | valódi kontaktok: `RELEASE-EVIDENCE` (stagingben belső build-jelölő megengedett) |
| Médiakapuk | release-kötelező asset vagy fallback | — | jogi/gyermekvédelmi alkapuk: `MEDIA-RELEASE` |
| Program-transzfer | — | — | `LIFECYCLE` |
| Go/no-go a pilotra | — | — | `SIGNOFF` |

## 5. Hamis zöld elleni védelem

Lásd 2.3. Mindegyik invariánsnak saját selftest-esete van a `content_integrity.py --selftest`-ben.

## 6. Asset-szintű médiakapu

- **Fázis:** a `release_phase` mező; ha hiányzik, a Q-MED-1 közvetlen megfeleltetése: `voiceover` → B (narráció),
  `video` → C (videó); minden más típus → A (hibabiztos alapértelmezés a fázis-hozzárendelésig).
- **Fallback:** a B és a C fázisnak a Q-MED-1 szerint mindig van fallbackje (leirat/felirat, illetve A/B-s statikus vagy
  szöveges); ezek végleges helyettesítésnek számítanak a kontrollált pilothoz. Az A fázisnál csak az asset saját
  `fallback` mezője számít.
- **Nyitott médiakapu egy assetre:** a manifest-státusza nem `spec-ready`, vagy az asset R2-es, és az R2 szövegében
  `⟬KITÖLTENDŐ⟭` áll, vagy a `RIGHTS-EVIDENCE.md` J1/J2/V1/V3 alkapuja közül bármelyik `HIÁNYZIK`.
- **Döntés:** A fázis + nyitott kapu + nincs fallback → `BUILD-SPEC: MEDIA-REQUIRED-WITHOUT-FALLBACK`; A fázis +
  nyitott kapu + átmeneti fallback → `MEDIA-RELEASE` (→ `MEDIA_PENDING`); végleges fallback, illetve B/C fázis → nem
  blokkol.
- **Ma:** a jogi kapun álló 119 asset közül 89 narráció (B) és 26 videó (C) — nem blokkol; 4 fotó (R8) fázis nélkül A,
  fallback nélkül → build-spec tétel, amíg a fázis vagy a fallback nincs rögzítve.

## 7. Régi → új leképezés

| Régi blokker | Új kategória |
|---|---|
| `ERROR` (a verdiktbe eddig nem számított) | BUILD-SPEC `ERROR` |
| `MODULE-PLACEHOLDERS` | BUILD-SPEC `SOURCE-PLACEHOLDERS` |
| `HUMAN-DECISIONS` | BUILD-SPEC `HUMAN-DECISIONS` |
| `RUNTIME-ACCEPTANCE` (17) | POST-BUILD `ENVIRONMENT-RECORD` |
| `LMS-BUILD` (52) | POST-BUILD `BUILD-OUTPUT` |
| `SAFEGUARDING-CHECKLIST` (11), `PRIVACY-CHECKLIST` (7), `A11Y-CHECKLIST` (20) | tételenként a jelölés szerint; jelölés nélkül BUILD-SPEC `CHECKLIST-UNCLASSIFIED` (38) |
| `PROGRAM-TRANSFER` (1) | `LIFECYCLE` (nem kapu) |
| `PRODUCTION-RULES` (R2, R3) | asset-szintű média (BUILD-SPEC `MEDIA-REQUIRED-WITHOUT-FALLBACK` / `MEDIA-RELEASE`); a nyitott szabályok tájékoztató sorként maradnak |
| `MEDIA-HUMAN-DECISIONS` | `MEDIA-RELEASE` |
| `GOVERNANCE-DECISIONS` | `GOVERNANCE` (nem kapu, változatlan) |

**Új, eddig gépileg nem látott tételek** (a kánon eddig is előírta őket): `POST-BUILD: RUNTIME-TESTS` (23 P0 + 12
a11y), `MANIFEST-OPEN` (BSPEC-01…04), `POST-BUILD` G4b-visszaaudit és `SIGNOFF` go/no-go (`RELEASE-READINESS.md`).

## 8. Kimenet

```
Objective integrity errors: 0
Build-spec blockers: n
BUILD-SPEC: MANIFEST-OPEN 4 open: BSPEC-01, BSPEC-02, BSPEC-03, BSPEC-04
BUILD-SPEC: CHECKLIST-UNCLASSIFIED 38 open: …
BUILD-SPEC: MEDIA-REQUIRED-WITHOUT-FALLBACK 4: …
MOODLE-BUILD-VERDICT: NOT_READY
Learner-release blockers: n
POST-BUILD: BUILD-OUTPUT 52 unresolved
POST-BUILD: ENVIRONMENT-RECORD 17 unresolved
POST-BUILD: RUNTIME-TESTS 35 not RUNTIME_VERIFIED
POST-BUILD: CHECKLIST 1 open
SIGNOFF: CHECKLIST 1 open
MEDIA-INFO: PRODUCTION-RULES 2 open: R2, R3 (asset-szinten értékelve)
LIFECYCLE: PROGRAM-TRANSFER 1 open (release utáni validáció, Q-REL-1; nem kapu)
LEARNER-RELEASE-VERDICT: NO-GO
RELEASE-VERDICT: NO-GO
```

A `RELEASE-VERDICT` sor az alias. A `--strict-release` 2-vel lép ki, ha a learner-verdikt nem
`READY_FOR_CONTROLLED_PILOT`. A parancs (`--release-report`) nem változik, ezért a CI-hoz és a hook engedélylistájához
nem kell nyúlni.

## 9. Migráció

| Fázis | Tartalom | Állapot |
|---|---|---|
| 0 | a nyitott kérdések lezárása (RM-D1…D3) | kész |
| 1 | a Q-REL-1…4, Q-MED-1 és RM-D1…D6 átvezetése a HUM 10. szakaszába | kész (ez a munkaág) |
| 2 | `content_integrity.py`: két verdikt, kategóriák, alias, hamis zöld selftestek | kész (ez a munkaág) |
| 3 | forrásdokumentumok: `RELEASE-READINESS.md` (G-tábla, életciklus, go/no-go és G4b tétel), runtime acceptance „Teszt-állapot” tábla, manifest BSPEC-tábla | kész (ez a munkaág) |
| 4 | governance-szövegek: CLAUDE.md, release-check skill, biztonsági szabályfájl | kész (ez a munkaág); utána új session |
| 5 | **új session:** `/course-fix` a BSPEC-01…04-re (lásd 11.) | következik |
| 6 | **új session:** a 38 tételes leltár, a tételek jelölése (lásd 12.) | következik |
| 7 | `release_phase`/`fallback` a média-manifestben (a `media_manifest.py` séma, build, tesztek) | következik |
| 8 | a HUM-fejlécek átállítása a Q-REL-3/RM-D2 láncra, a parserrel együtt | következik |
| 9 | az alias kivezetése egy release-ciklus után | később |

**Bizonyíték-megőrzés:** kipipált tételt nem nyitottunk vissza, bizonyítékszöveget nem töröltünk. A program-transzfer
`[x]` tétele (a médiaregiszter újragenerálása, CI-futás `36605020566`) a helyén maradt.

## 10. Ismert korlátok

- A HUM-lánc állapotait (`IMPLEMENTED`, `RUNTIME_VERIFIED` stb.) a parser még nem olvassa; a 8. fázis teszi meg.
- A média-manifest még nem viseli a `release_phase`, `fallback`, `fallback_final` mezőt; addig a 6. pont
  alapértelmezései érvényesek.
- A `RIGHTS-EVIDENCE.md` alkapuit a gép a §1/A.5 tábla `**HIÁNYZIK**` jelöléséből olvassa; más alkapu-formát nem ismer.
- A 38 checklist-tétel jelöletlen, ezért a build-verdikt a leltárig hibabiztosan `NOT_READY`.

## 11. A négy build-spec finding (a következő session `/course-fix`-éhez)

A tételeket a fő session a forrásban ellenőrizte (2026-10-04); a `/course-fix` lépésenként újra bizonyítja őket. A
nyilvántartásuk: `LMS – activity manifest.md`, „Nyitott build-spec tételek” (BSPEC-01…04).

### BSPEC-01 — a `GATE_CONFIRMED_<module>` checkpoint nincs specifikálva

- **Hely:** `02 Tervezet/LMS – activity manifest.md:133`; `02 Tervezet/LMS – H5P runtime acceptance.md` 8. pont (:42).
- **Probléma:** az összetett kapuk (M1, M3, M5, M6, M7) downstream nyitásához a manifest kézi/stáb-checkpointot ír elő,
  de nincs hozzá Moodle-objektumtípus, `build_id`, completion-szabály, és nincs megadva, mihez kötődik a restrict access.
- **Bizonyíték:** :133 „Ha Moodle-ben az összetett feltétel nem kódolható bizonyítottan, egy `GATE_CONFIRMED_<module>`
  kézi/stáb-checkpointot kell létrehozni”; RA :42 „skalár küszöbbel **nem is kódolható**”.
- **Javaslat (javítási korlát):** modulonként egy checkpoint-sor a manifest táblájában (`build_id`, profil, completion,
  unlock), a választott Moodle-mechanizmussal és tartalékúttal; a kapu-logika, a küszöbök és a mentori megerősítés
  szabálya nem változik. A mechanizmus kiválasztásához a Moodle core restrict access feltételeit (activity completion,
  date, grade, group, user profile) a hivatalos dokumentációból kell igazolni.
- **Súlyosság:** P1 · **Típus:** objektív · **Ellenőrzés:** forrásban igazolva.

### BSPEC-02 — a Moodle-oldali szabadszöveg-mezőknek nincs manifest-sora

- **Hely:** `02 Tervezet/LMS – activity manifest.md:33`; RA 6. és 12. pont (:40, :54); érintett sorok: LMS-M2-01 (:48),
  LMS-M4-01/02 (:59–60), Z.3.
- **Probléma:** a manifest szerint a Moodle-oldali szabadszöveg-mező „a build előtt saját sort kap”, de egy ilyen sor
  sincs; a megvalósítás útját a runtime acceptance a célverziós tesztre bízza, így a két szabály körbeér.
- **Bizonyíték:** :33 „akkor a build előtt saját sort kap ebben a táblázatban (build_id, profil, completion, privacy)”;
  RA :54 „a lépés helyéről és completion-kötéséről külön kell dönteni”.
- **Javaslat:** mezőnként egy alapértelmezett út (a hozzáférhetőségi sztenderd :64–68 szerint) és a sor felvétele;
  a HUM 6. szakasza szerint ez technikai kérdés, nem szervezeti döntés. A pedagógiai kötelezőség nem gyengül.
- **Súlyosság:** P1 · **Típus:** objektív · **Ellenőrzés:** forrásban igazolva.

### BSPEC-03 — az LMS-M5-07 típusa nyitott

- **Hely:** `02 Tervezet/LMS – activity manifest.md:70` (LMS-M5-07).
- **Probléma:** a sor eszköze „KUTATÁS KELL”, mert a core Moodle-ben nincs teljesítéshez relatív, tanulónkénti
  késleltetés.
- **Bizonyíték:** :70 „eszköz: KUTATÁS KELL, mert a core Moodle-ben nincs teljesítéshez relatív, felhasználónkénti
  késleltetés”.
- **Javaslat:** az RM-D6 szerint: elsődleges út a „Restriction by relative date” plugin (site admin telepíti); ha nincs,
  a pont az LMS-M5-03 után látható, és a lecke kéri a 72 órás várakozást. A típus (PAGE-C vagy H5P-C) a forrás szerint
  rögzítendő. A plugin kompatibilitását a plugin hivatalos oldaláról kell igazolni.
- **Súlyosság:** P1 · **Típus:** objektív (a döntés: RM-D6) · **Ellenőrzés:** forrásban igazolva.

### BSPEC-04 — a manifest unlock-sorai ellentmondanak a Q-REL-2-nek

- **Hely:** `02 Tervezet/LMS – activity manifest.md:124–130` (modulonkénti nyitás), :53 (LMS-M3-01 „M2 complete”),
  :59 (LMS-M4-01 „M3 complete”).
- **Probléma:** a Q-REL-2 szerint bukott éles kapu után a következő modul tanulási része megnyílhat, csak a következő
  éles kapu lezárása blokkolt; a manifest a következő modult a kapu sikeréhez köti.
- **Bizonyíték:** :124 „| M1 | H5P-k + LMS-M1-05 mastery | M2 nyitható |”; Q-REL-2 „Bukott éles kapu után a következő
  modul **tanulási része megnyílhat**, de a következő éles kapu lezárása és minden, a hiányzó kompetenciára épülő
  magas tétű előrehaladás blokkolt marad.”
- **Javaslat (javítási korlát):** a tanulási rész nyitása a kapueredmény megerősítéséhez (siker vagy bukás) kötődjön
  (kapcsolat a BSPEC-01 checkpointjával), a következő éles kapu lezárása az előző kapu sikeréhez. Küszöb, F-peula és
  javító határidő nem változik.
- **Súlyosság:** P1 · **Típus:** objektív (a döntés: Q-REL-2) · **Ellenőrzés:** forrásban igazolva.

## 12. A 38 tételes leltár (a következő sessionben)

- **Forrás:** `Gyermekvédelem – release gate.md` §6 (11 nyitott), `Adatvédelem – tanulói adatok és AI.md` §9 (7),
  `LMS – hozzáférhetőségi sztenderd.md` (20, elemenkénti sablonok).
- **Tételenként:** BUILD BLOCKER / POST-BUILD TEST / RELEASE EVIDENCE / HUMAN QA / REPO-FIXABLE, indoklással és a
  felelős szereppel; szervezeti jóváhagyásnál RELEASE EVIDENCE + `signoff`.
- **Kimenet:** a jelölések (`<!-- gate: … -->`) a tételek végére; a hozzáférhetőségi sablonoknál külön javaslat, hogy
  maradjon-e checkbox (elemenkénti sablon, nem globális kapu).
- **Szabály:** kipipált tételt nem nyitunk vissza; szerepköri bizonyítékot nem írunk be.
