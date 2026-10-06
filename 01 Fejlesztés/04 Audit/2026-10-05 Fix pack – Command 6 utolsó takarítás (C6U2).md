# Fix pack — Command 6 utolsó takarítás (C6U2, 2026-10-05)

> **Audit trail, nem kánon.** Ez a Command 6 **utolsó** takarító köre. A bemenet a C6U-kör célzott újraellenőrzésének
> findingjai: C6U-BIZT-1, -2, -3, -4 és C6U-IMPL-1, -2 (`2026-10-05 Fix pack – Command 6 utójavítások (C6U).md`, 4.
> szakasz). Két kérdést a projektgazda most lezárt: a C6U-BIZT-3-at és a C6U-IMPL-2-t (0. szakasz). Munkaág:
> `fix/moodle-build-hardening`. Javítás még nem történt, commit nincs.
>
> **Nem tárgya ennek a csomagnak, nyitva marad:** C6-BIZT-1, C6-BIZT-3, C6-BIZT-4, C6-BIZT-8, C6-IMPL-5, C6-NYELV-3,
> SAFE-7, A11Y-15/18, BSPEC-05/06/07 és M6.4. A Memuna és a DPO végső QA-ja is nyitva marad.
>
> **Hurokzáró szabály (a projektgazda utasítása):**
> - Ha az ellenőrzés során a C6U2 saját szerkesztésében objektív hiba derül ki (elírás, kihagyás, törött hivatkozás vagy kánoni eltérés), és az új policy- vagy emberi döntés nélkül javítható, **ugyanebben a futásban javítandó**.
> - C6U3 nincs.
> - Megállni csak akkor szabad, ha a javításhoz új projektgazdai, DPO-, jogi vagy Memuna-döntés kellene, vagy answer key, küszöb vagy rubrika változna.

## 0. A projektgazda utasítása (2026-10-05, szó szerint)

```
Yes. Create the final C6U2 cleanup pack, but this is the LAST Command-6 cleanup round.

Also close these two questions now:

1. C6U-BIZT-3
YES: add a short learner-facing pointer to the existing safeguarding reporting route so “do not enter this into a normal learning activity” cannot be read as “do not report it”.

Use only the already canonical GK §4.1 reporting path. Meaning:
- do not put a real safeguarding/sensitive case into the learning activity;
- if the learner needs to report such a situation, use the separate safeguarding reporting route.

This is a cross-reference/clarification, not a new safeguarding policy.
Memuna/DPO final QA remains open.

2. C6U-IMPL-2
YES: propagate the four RT-P0-15 mentor-visibility test conditions as a 2026-10-05 project-owner IMPLEMENTATION decision:
- two mentors;
- two groups;
- direct-URL access test;
- learner-to-learner visibility test.

Do not change their semantics.

Now create one narrow C6U2 fix pack covering:

- C6U-BIZT-1
  Use exactly the canonical conditional meaning:
  “Ha egy feltárásban mégis megjelenik ilyen adat, kikerül a Moodle-ből, és a külön, hozzáférés-korlátozott gyermekvédelmi incidensfolyamatba kerül.”
  Do NOT state that every accidentally appearing special-category datum automatically enters the safeguarding incident process.

- C6U-BIZT-2
  Restore the existing guarantee that a sensitive family- or identity-related story cannot be mandatory.

- C6U-BIZT-3
  Add the GK §4.1 reporting-route cross-reference described above.

- C6U-BIZT-4
  Correct the learner-facing sentence to the already supported access rule:
  “A kvízek és a kapuk eredményét az értékelőd látja.”
  Do not broaden access.

- C6U-IMPL-1
  Correct the A11Y implementation wording:
  Moodle may append the site name to the embedded document title.
  The normative iframe title remains the canonical H5P/activity title.
  Any suffix/delimiter normalization is target-environment implementation detail and must be runtime-verified.
  Replace the inaccurate “nem azonos” claim with precise “eltérhet” wording.

- C6U-IMPL-2
  Propagate the four RT conditions as the project-owner implementation decision above.

Do NOT touch the still genuinely human/DPO items:
- C6-BIZT-1
- C6-BIZT-3
- C6-BIZT-4
- C6-BIZT-8
- C6-IMPL-5
- C6-NYELV-3
- SAFE-7
- A11Y-15/18
- BSPEC-05/06/07
- M6.4

CRITICAL LOOP-BREAK RULE:
During C6U2 verification, if you find an objective typo, omission, broken reference or canonical mismatch introduced by C6U2 itself and it can be corrected without a new policy/human decision, FIX IT IN THE SAME RUN.
Do not create C6U3.
Do not stop merely to report a fixable defect in your own edit.

Only stop if correcting it would require:
- a new project-owner policy decision;
- DPO/legal decision;
- Memuna/safeguarding decision;
- or changing an answer key/threshold/rubric.

After the fix:
- targeted recheck of only C6U2-touched lines;
- content integrity + selftest;
- media tests/check if relevant;
- git diff --check;
- release report/check;
- no commit;
- no push.

First write the C6U2 fix pack and return the exact user-invoked /course-fix command.
STOP.
```

## 1. Lépések

A lépéseket a táblázat sorrendjében kell alkalmazni. Ahol egy lépés két helyet érint, két `Edit` kell, az (a) és a (b) helyre. A „Bizonyíték” oszlop a most a fájlban álló szöveget idézi; minden horgony pontosan egyszer szerepel (`grep -cF`). A „Javítás” oszlop szövegét szó szerint kell beírni.

Fájlrövidítések:

| Rövidítés | Fájl |
|---|---|
| `ADV` | `02 Tervezet/Adatvédelem – tanulói adatok és AI.md` |
| `STD` | `02 Tervezet/LMS – hozzáférhetőségi sztenderd.md` |
| `RT` | `02 Tervezet/LMS – H5P runtime acceptance.md` |
| `HUM` | `02 Tervezet/Emberi jóváhagyás szükséges.md` |
| `GK` | `02 Tervezet/Gyermekvédelem – release gate.md` |

| ID | Finding | Hely | Bizonyíték (most) | Javítás (szó szerint) | Kánoni alap |
|---|---|---|---|---|---|
| C6U2-01 | C6U-BIZT-1, C6U-BIZT-2, C6U-BIZT-3 (ugyanaz a mondatsor, egy csere) | ADV :241 | „Politikai, vallási, egészségügyi vagy más különleges adatot és valós gyermekvédelmi esetet egyik tanulási feladatba se írj be: ilyen adatot normál tanulási feladatban nem gyűjtünk. Ha mégis megjelenik – például egy valós eset feltárásakor –, kikerül a Moodle-ből, és a külön, hozzáférés-korlátozott gyermekvédelmi incidensfolyamatba kerül.” | „Érzékeny családi vagy identitással kapcsolatos történetet egyik feladat sem kér kötelezően. Politikai, vallási, egészségügyi vagy más különleges adatot és valós gyermekvédelmi esetet egyik tanulási feladatba se írj be: ilyen adatot normál tanulási feladatban nem gyűjtünk. Ha egy feltárásban mégis megjelenik ilyen adat, kikerül a Moodle-ből, és a külön, hozzáférés-korlátozott gyermekvédelmi incidensfolyamatba kerül. Ha egy valós gyermekvédelmi helyzetet jelezned kell, azt ne egy tanulási feladatban tedd: azonnal vond be a kijelölt Memunát (a Somer gyermekvédelmi felelősét); az elérhetőségét a kurzus „Segítség és kapcsolatok” blokkjában találod.” | **BIZT-2:** ADV §2 :29 („Érzékeny identitás-, családi- … történet nem lehet kötelező tanulási artefaktum”); az egészségügyi és a gyermekvédelmi rész a különleges adat tilalma alá esik, ezért nem kerül vissza. **BIZT-1:** a projektgazda szó szerinti mondata (0. szakasz), azonos az ADV §3 :75 („Ha feltáráskor mégis megjelenik”) és a §5 („Ha a feltárásban különleges adat jelenik meg”) feltételével. **BIZT-3:** GK §4.1. Az utalás kánoni rövid formája az „azonnal vond be a Memunát”; az első előfordulás „a kijelölt Memuna (a Somer gyermekvédelmi felelőse)”. A leckék a szerepet nevezik meg, és a „Segítség és kapcsolatok” blokkra mutatnak, név és telefonszám nélkül (GK §4.1, „Hol áll a név”). A „ne egy tanulási feladatban” a GK §4.1 „Dokumentálás” pontjából jön („A madrih nem ír Moodle-be, csoportchatbe, kvízválaszba vagy beadandóba az esetről azonosítható részletet”). Ez kereszthivatkozás, nem új policy. |
| C6U2-02 | C6U-BIZT-4 | ADV :245 | „> **Ki látja?** A kvízek és a kapuk eredményét az értékelőd. A szöveges” | „> **Ki látja?** A kvízek és a kapuk eredményét az értékelőd látja. A szöveges” | ADV §5 („a zárt kvíz pontszámát az értékelő látja”); a hozzáférés nem bővül |
| C6U2-03 | C6U-IMPL-1 | (a) STD :92; (b) STD :100 | (a) „a `moodle_page::set_title()` ehhez alapértelmezésben az oldal nevét is hozzáfűzi (Moodle 4.5, `lib/pagelib.php`), ezért a dokumentumcím nem azonos a H5P-címmel.*”; (b) „Mivel a dokumentumcím az oldal nevét is tartalmazhatja, a karbantartott megoldás normalizálhatja: eltávolíthatja a Moodle által hozzáfűzött oldalnév-utótagot. A pontos elválasztót és normalizálást a célkörnyezetben kell igazolni; egyetlen elválasztó mentén vágva nem garantált a helyes cím.” | (a) „a `moodle_page::set_title()` ehhez alapértelmezésben a Moodle-portál (site) nevét is hozzáfűzi (Moodle 4.5, `lib/pagelib.php`; a célkörnyezetben ez eltérhet), ezért a dokumentumcím eltérhet a H5P-címtől.*”; (b) „Mivel a dokumentumcím a Moodle-portál (site) nevét is tartalmazhatja, a karbantartott megoldás normalizálhatja: eltávolíthatja a Moodle által hozzáfűzött portálnév-utótagot. Az utótag és az elválasztó kezelése a célkörnyezet megvalósítási részlete, amelyet runtime-ban kell igazolni; egyetlen elválasztó mentén vágva nem garantált a helyes cím.” | Moodle `MOODLE_405_STABLE` `lib/pagelib.php`: `set_title($title, bool $appendsitename = true)`, a site nevét fűzi hozzá. Az ezt követő mondat („A normatív eredmény változatlan: az iframe `title`-je a kanonikus H5P-/activity-cím.”) változatlan marad. Megvalósítási útmutatás, nem új hozzáférhetőségi szabály. |
| C6U2-04 | C6U-IMPL-2 | (a) HUM 11. szakasz, az „Az A11Y-07 iframe-címe (G5a/G5b)” sor után; (b) RT :80 | (a) a sor vége: „0. szakasz (második és harmadik üzenet) \| — (a döntés nem nevez meg utólagos ellenőrzőt) \|”; (b) „(projektgazdai döntés, 2026-10-05: `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`, 1. szakasz 2. pont).” | (a) új sor az **A.1** pont szó szerinti szövegével; (b) „(projektgazdai megvalósítási döntés, 2026-10-05: `Emberi jóváhagyás szükséges.md` 11. szakasz, „Az RT-P0-15 mentor-láthatósági tesztfeltételei”; forrás: `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`, 1. szakasz 2. pont).” | 0. szakasz 2. pont; a D-a…D-d jegyzőkönyv 1. szakasz 2. pont és 2. szakasz (csak a mentor szerepkört szűkíti; „DPO QA továbbra is megmarad”). A négy feltétel jelentése nem változik. |

### A.1 — a C6U2-04 (a) új HUM-sora (szó szerint)

```markdown
| Az RT-P0-15 mentor-láthatósági tesztfeltételei | Projektgazdai megvalósítási döntés: a TEXT-C mentor-láthatósági mechanizmusát (`Adatvédelem – tanulói adatok és AI.md` §3, „Activity-szintű adatleltár – build-rész”) az RT-P0-15 stagingtesztje legalább két mentorral és két elkülönített tanulói csoporttal igazolja: az A mentor csak az A csoport válaszait látja; a B mentor csak a B csoport válaszait látja; egyik mentor sem jut közvetlen URL-lel más csoport tanulójának válaszához; a tanuló nem látja más tanuló válaszát. A feltételek jelentése azonos a D-a…D-d jegyzőkönyv 1. szakaszának 2. pontjával. A mechanizmus csak a mentor szerepkört szűkíti; a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés DPO-kérdés marad (BIZT-2). A teszt futtatása post-build bizonyíték (G2): ez a sor runtime-igazolást nem állít. | `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`, 1. szakasz 2. pont és 2. szakasz; `01 Fejlesztés/04 Audit/2026-10-05 Fix pack – Command 6 utolsó takarítás (C6U2).md`, 0. szakasz | a DPO (QA) |
```

## 2. A futás után

- **Pin:** a látható szöveg változik (ADV §11), ezért egyetlen pint kell futtatni.
- **Média:** az `@asset` és a `@source` nem változik. A `validate`, a `check` és a `reconcile` csak ellenőrzésként fut.
- **Ellenőrzések:**
  - `content_integrity` és `--selftest`;
  - `python3 -m unittest tools.test_media_manifest`;
  - `git diff --check`, a PR-tartományra is;
  - `--release-report`, majd `/release-check`.
- **Célzott újraellenőrzés:** csak a C6U2 által érintett sorokat nézi (ADV :241, :245; STD :92, :100; RT :80; az új HUM-sor).
  - A biztonság-jog lencse ADV :241-et és :245-öt nézi, a nyelvi szempontokkal együtt.
  - Az implementációs lencse a STD-, RT- és HUM-sorokat nézi.
  - Ha a C6U2 saját szerkesztésében javítható, objektív hiba derül ki, az ugyanebben a futásban javítandó (hurokzáró szabály).

## 3. Várt gépi állapot

- Checklist-tétel és BSPEC-sor nem változik.
- `MOODLE-BUILD-VERDICT`: **`NOT_READY` marad**, kizárólag a `MANIFEST-OPEN 3` (BSPEC-05, -06, -07) miatt.
- `LEARNER-RELEASE-VERDICT`: `NO-GO`.
- A PR-01 és a PR-02 érdemben akkor tekinthető késznek (build-szinten), ha ez a kör sikeresen lefutott, és a célzott újraellenőrzés nem hagy objektív hibát. A nyitott DPO-, jogi és Memuna-tételek ettől függetlenül nyitva maradnak.

## 4. Futás (`/course-fix`, 2026-10-05)

**Lépések:**
- A C6U2-01…C6U2-04 mind alkalmazva, 6 `Edit`-tel.
- Minden horgony a futás előtt pontosan egyszer szerepelt (`grep -cF`), a javítások szövege a futás után megvan.
- A HUM-sor a sztenderd A.1 szövegével betűre egyezik.

**Célzott újraellenőrzés** (csak a C6U2-ben érintett sorokon):
- Biztonság-jog és nyelvi lencse (ADV :241, :245): **0 finding**.
- Implementációs lencse (STD :92, :100; RT :80; HUM :574): **0 finding**.
- A hurokzáró szabályra nem volt szükség: a saját szerkesztésben nem maradt javítandó hiba, és C6U3 nincs.

**Pin:** egyetlen pin, 4 fájl, az újraellenőrzés után.

**Ellenőrzések:**
- Média: `validate` és `check` OK; a `reconcile` szerint 0 sor nincs egyeztetve. Build nem kellett.
- `py_compile` OK, a selftest 57/57, a `content_integrity` 0 hibát ad, a 159 teszt OK.
- `git diff --check` tiszta, a PR-tartományra is.

**Release report:**
- `MOODLE-BUILD-VERDICT: NOT_READY`, csak a `MANIFEST-OPEN 3` (BSPEC-05/06/07) miatt.
- `LEARNER-RELEASE-VERDICT: NO-GO`.
- A számlálók változatlanok: post-build 14, release-evidence 8, environment record 18.

**A PR-01 és a PR-02 állapota:** a build-szintű, repóban javítható rész a Command 6, a C6U és a C6U2 után érdemben kész. Nyitva marad:
- C6-BIZT-1, -3, -4, -8, C6-IMPL-5, C6-NYELV-3;
- a §9 release-evidence tételei;
- a Memuna és a DPO végső QA-ja.

**Commit és push:** nincs.
