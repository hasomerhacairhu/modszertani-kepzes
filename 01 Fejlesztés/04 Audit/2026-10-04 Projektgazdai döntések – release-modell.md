# Projektgazdai döntések — release-modell v2 (2026-10-04)

> **Audit trail, nem tananyag.** A projektgazda döntései a release-readiness modell kétlépcsőssé tételéről. Előzmény:
> a 2026-10-04-i csak olvasó governance-audit (a munkamenetben) és a modell-dokumentum
> (`2026-10-04 Release-modell v2 – Moodle build és learner release.md`). A projektgazda a válaszait a munkamenetben
> írásban adta meg, és mindkét körben megerősítette, hogy azok az ő döntései és utasításai (AskUserQuestion: „Igen,
> helyi commitokkal”). A válaszok szó szerint állnak.

**Jóváhagyta:** projektgazda · **Dátum:** 2026-10-04

## 1. A kiinduló utasítás (szó szerint, kivonat)

> „Előbb javítsuk ki a release-readiness modell alapvető fogalmi problémáját: külön kell választani azt, hogy a
> repository READY-E A MOODLE BUILDRE attól, hogy a kész Moodle-rendszer READY-E LEARNER RELEASE-RE.”
>
> „A MOODLE buildre readiness-t SOHA ne blokkolja olyan bizonyíték, amely csak a Moodle build vagy runtime során
> keletkezhet. Ezért a BUILD_OUTPUT, RUNTIME_OUTPUT, runtime accessibility teszt, végső Memuna/DPO/a11y QA,
> program-transfer és szervezeti go-live sign-off nem lehet Moodle-build előfeltétel. Viszont a buildet ténylegesen
> meghatározó specnek késznek kell lennie: implementálható activity-definíciók, szükséges célkörnyezeti paraméterek,
> buildet érintő safeguarding/privacy/a11y szabályok, valamint minden REQUIRED_FOR_FIRST_RELEASE médiához asset vagy
> elfogadott fallback. A learner release már csak a tényleges build és runtime bizonyítékokkal zárható.”
>
> „Az R2/R3 production rule a jelenlegi kánonnal összhangban ne blokkolja a staging buildet, ha az érintett asset nem
> REQUIRED_FOR_FIRST_RELEASE vagy van egyenértékű fallback.”

## 2. A három nyitott kérdés lezárása

### RM-D1 — PROGRAM-TRANSFER

> „Maradjon a Q-REL-1. A 6 valós terepi peula + mentori ciklus **nem learner-release gate**, hanem release utáni
> programvalidáció. A lifecycle: `INTERNAL_STAGING → CONTROLLED_PILOT → GENERAL_RELEASE → PROGRAM_TRANSFER_VALIDATED`.
> Tehát a PROGRAM-TRANSFER kerüljön ki a `NO-GO` release blockerek közül, és külön lifecycle-státuszként jelenjen meg.”

### RM-D2 — Q-REL-3 / EXPERT_QA

> „Módosítsuk a modellt. Két külön QA-fogalmat akarok:
> - `SPEC_QA`: specifikációs/szakértői review, amely lehet korai veto vagy tanácsadó ellenőrzés, de önmagában nem
>   Moodle-build gate.
> - `FINAL_RELEASE_QA`: a ténylegesen implementált és runtime-ellenőrzött kész rendszer szakértői ellenőrzése. Ez
>   release gate.
>
> A kötelező release-lánc legyen: `OWNER_DECIDED → IMPLEMENTED → RUNTIME_VERIFIED → FINAL_RELEASE_QA →
> RELEASE_APPROVED`. A Memuna végső átnézése, a DPO release-ellenőrzése és a független a11y pre-flight a
> `FINAL_RELEASE_QA` réteghez tartozik.”

Ez a Q-REL-3 láncának (`PROPOSED → OWNER_DECIDED → EXPERT_QA → IMPLEMENTED → RUNTIME_VERIFIED → RELEASE_APPROVED`)
sorrendjét módosítja. A `PROPOSED`, a `SUPERSEDED` és a `REOPENED` a Q-REL-3 szerint megmarad.

### RM-D3 — a verdiktek állapotai

> „Ne használjunk az új kanonikus modellben csupasz `READY` állapotot, mert később megint összekeveredik a staging, a
> controlled pilot és a general release. Legyen pontosan:
> `MOODLE-BUILD-VERDICT` – `NOT_READY` – `READY_FOR_STAGING_BUILD`;
> `LEARNER-RELEASE-VERDICT` – `NO-GO` – `CONTENT_READY / MEDIA_PENDING` – `READY_FOR_CONTROLLED_PILOT`.
> A `GENERAL_RELEASE` ne repo-verdikt legyen, hanem lifecycle-fázis. A CONTROLLED_PILOT után, a pilot findingok
> javítása, újratesztelése és a szükséges go/no-go döntés után léphet oda a program. A régi `RELEASE-VERDICT` egy
> release-ciklusig maradhat kompatibilitási aliasként, de az új kanonikus állapotok legyenek a fentiek.”

### RM-D4 — a migrációs terv jóváhagyása, feltételekkel

> „A migrációs tervet is jóváhagyom azzal, hogy:
> - meglévő bizonyítékot és kipipált tételt nem törlünk vagy nyitunk újra;
> - minden jelenlegi blocker pontosan egy új kategóriába kerüljön;
> - legyen selftest a hamis zöld esetekre;
> - ERROR mellett semmilyen build-ready állapot nem lehet zöld;
> - a média gate asset-szintű legyen, fallbackkel;
> - a Q-REL-1…4 és Q-MED-1 kerüljön át a kánoni HUM/döntési helyre.”

## 3. Végrehajtási döntések (AskUserQuestion, 2026-10-04)

### RM-D5 — a munka elosztása

- **Kérdés:** „Hogyan osszuk el a négy lépést?” (a governance-változás után új session kell, mielőtt skill vagy
  review fut).
- **Válasz:** „1–2 itt, 3–4 új sessionben” — „Itt: modell-dokumentum + governance-csomag + tesztek + commitok. Új
  sessionben: te indítod a /course-fix-et a négy build-spec findingra (a dokumentumban teljes finding-formátumban
  lesznek), utána fut a 38-as leltár az új szabályokkal.”

### RM-D6 — LMS-M5-07, késleltetett felidézés

- **Kérdés:** „Az egyik build-spec hiány (LMS-M5-07: késleltetett felidézés, „M5-03 completion + 72 óra,
  tanulónként”) technikai útválasztást kér, mert a core Moodle nem tud teljesítéshez relatív késleltetést. Melyik
  legyen a kanonikus út?”
- **Válasz:** „Plugin + kézi tartalék” — „Elsődleges: „Restriction by relative date” plugin (a site admin
  telepíti); ha nincs telepítve, a pont az M5-03 után látható, és a lecke kéri a 72 órás várakozást. Így a build nem
  vár a pluginra.”
- **Utólagos ellenőrzés (vétó/QA):** az LMS-gazda / site admin (a plugin telepítése).

## 4. A célkitűzés (szó szerint)

> „A cél az, hogy a végén teljesen egyértelműen külön lássuk: **felépíthetjük-e már Moodle-ban**, és **odaadhatjuk-e
> már valódi résztvevőknek controlled pilotként**.”
