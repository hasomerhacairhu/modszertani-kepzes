# Fix pack — Command 6: PR-01, PR-02, A11Y-07, A11Y-17, BIZT-2/3/4/11 és három konzisztencia-javítás (2026-10-05)

> **Audit trail, nem kánon.** Ez a `/course-fix` bemenete.
>
> - **Munkaág:** `fix/moodle-build-hardening`, HEAD `9ef2b25`, rajta a nem commitolt FREEZE-A- és FP-kör.
> - **Állapot:** javítás nem történt, commit nincs.
> - **Hatókör:** a négy `gate: build` checklist-tétel (D-a) és a hozzájuk tartozó validált BIZT-findingok, M0/M1 első prioritással, teljes M0–Z build-hatókörrel; ezen felül a projektgazda 2026-10-05-i utasításának három konzisztencia-javítása (0. szakasz).
> - **2. változat:** a projektgazda végrehajtás előtti pontosítása (0. szakasz, második blokk) szerint átdolgozva. Az A11Y-07 kettéválik, és a megállási pont megszűnik. Az A11Y-17 az eredeti hatókörre áll vissza. A PR-02 belső jelölői kikerülnek a tanulói szövegből. A C6-17 marad, a C6-19 új lépés.
> - **3. változat:** a projektgazda technikai javítása (0. szakasz, harmadik blokk) szerint csak az A11Y-07 megvalósítási követelménye változik (C6-09, C6-10/A.4, C6-11, C6-19). A 2. változat téves állítása, hogy a két Mustache-sablon felülírása önmagában kiolvashatja a címet a renderelt oldalból, kikerült. Minden más rész szó szerint a 2. változat szerinti.

## 0. Bemenetek és a projektgazda utasításai

### Döntések (nem nyitjuk újra)

- **D-a:** a 38 tétel besorolása; build-tétel a PR-01, a PR-02, az A11Y-07 és az A11Y-17. A tételek javasolt teendője a `2026-10-05 Build-blocker leltár – H-1…H-5, 38 checklist-tétel, 4 fotó.md` 103., 104., 125. és 135. sorában áll.
- **D-a…D-d jegyzőkönyv:**
  - Az 1. szakasz 2. pontja a mentor-láthatóság jelöltje: Separate groups, `mod/feedback:viewreports`, `moodle/site:accessallgroups` nélkül.
  - A 2. szakasz pontosítása szerint ez csak a mentor szerepkört szűkíti.
- **PILOT-3.**
- **HUM-PRIV-01–04:** `Adatvédelem – tanulói adatok és AI.md` §3–§8.
- **RELEASE-READINESS G5a/G5b:**
  - G5a: „spec és build-beállítások”, benne az „iframe-cím”; kapu: BUILD.
  - G5b: „renderteszt”; kapu: POST-BUILD.

### Validált findingok

Forrás: `2026-10-05 Validált findingok – MAN completion és mentor-láthatóság.md`, 2. pont; verdikt: MEGERŐSÍTVE.

- BIZT-3, BIZT-4, BIZT-11 és a BIZT-2 objektív része.

**Nyitva maradnak; ez a csomag nem válaszol rájuk:**
- BIZT-1, a BIZT-2 adatvédelmi része, BIZT-5, -6, -7, -8, -10, -12;
- az IMPL-11 DPO-része, PR-04, az LMS-Z-06 megőrzése (BS-D6);
- N-1, N-3…N-9, BIZT-R5, RT-P0-24, G1/G2/G3b;
- SAFE-7.

### A projektgazda utasítása (2026-10-05, első üzenet, a három konzisztencia-javításról; szó szerint)

```
1. M0 és M1 hub schedule wording
A jelenlegi „Heti offline: péntek 2. sáv” szöveg stale és ütközik a PILOT-2 döntéssel.
Ne találj ki új pilotnapot vagy idősávot.
A learner-facing megfogalmazás legyen schedule-neutral, pl.:
„Offline alkalom: a központi naptár szerint.”
Belső SCHEDULE_TO_RESYNC marker learner-facing szövegbe nem kerülhet.

2. Program terv.md §9.3 Memuna-review scope
A régi szűk felsorolás példálózó, nem kimerítő.
A kánoni review-hatókör a Gyermekvédelem – release gate.md §2.
A történeti felsorolást ne töröld, csak igazítsd ugyanahhoz a státuszhoz, amit HUM :481-nél már alkalmaztunk.

3. M4.1 fallback modality consistency
A NAR-06 és a hozzá tartozó 2. kérdés ne feltételezze, hogy minden learner képet lát.
A már elfogadott kép + text-card fallback miatt a learner-facing és narration wording legyen modalitássemleges:
„kép” helyett „példa” / „az alábbi példa” jellegű megfogalmazás, az eredeti jelentés megváltoztatása nélkül.
Ne adj új pedagógiai vagy érzékeny tartalmat.
Ha ezt tiszta terminológiai cserével nem lehet konzisztensen megoldani, jelezd az exact blocker-t, de ne indíts review-t.

A11Y-15 és A11Y-18:
- marad RELEASE-EVIDENCE, repo-fixable;
- ebben a Command 6 körben NE nyisd újra és NE változtasd a besorolásukat;
- a két statikus előfeltételt külön, szűk targeted review/fix körben zárjuk még ma.

SAFE-7 marad OPEN / FINAL_RELEASE_QA, staging buildet nem blokkolja.
```

### A projektgazda végrehajtás előtti pontosítása (2026-10-05, második üzenet; szó szerint)

```
Project-owner clarification for A11Y-07:

The finding that Moodle core H5P iframe output lacks a title attribute does NOT mean the repository build specification must remain open indefinitely.

A11Y-07 is split according to the existing G5a/G5b release model:

1. BUILD / repository specification:
   deterministically pin the required staging implementation:
   - every rendered Moodle H5P iframe must have a meaningful Hungarian `title`;
   - the title is derived from the canonical Moodle/H5P activity name;
   - preferred implementation is a theme template override of the Moodle `core_h5p/h5piframe` template;
   - do not modify Moodle core files directly;
   - if the target environment cannot deploy a theme/template override (or an equivalent maintained platform extension), staging implementation must stop on an explicit TARGET-ENVIRONMENT blocker rather than weakening the requirement.

Once this deterministic build requirement is canonically specified, A11Y-07's repository/build-spec part may be marked RESOLVED/CLOSED according to the checklist semantics.

2. POST-BUILD evidence:
   the actual rendered DOM must later prove that the iframe has the expected title, and screen-reader/runtime behaviour remains G5b / POST-BUILD evidence.
   Do not mark that evidence RUNTIME_VERIFIED now.

This is not a waiver of accessibility and not a claim that Moodle core already satisfies the requirement.

Additional clarifications:

- Keep C6-17. The second narrow Memuna enumeration must also be marked illustrative / governed by the canonical GK §2 scope.
- Accept the M4.1 modality-neutral wording using “példa” for the complete example and “változat” for left/right members of a pair. Preserve the same correct option and meaning. NAR-06 may be re-rendered later.
- PR-02 internal unresolved markers (`PRIVACY_CONTACT_TO_CONFIGURE`, `DPO_RETENTION_TO_CONFIRM`) may exist ONLY in internal build specification/evidence fields. They must never appear in learner-facing notice text or rendered learner content.
- Do not narrow A11Y-17 to video lessons unless the already validated A11Y-17 finding itself explicitly limits the requirement to lessons delivering video. Use the validated finding's original scope. If the fix pack currently narrowed it beyond the validated finding, correct the pack before producing the command.
- A11Y-15/18 remain untouched in this round.
- SAFE-7 remains open FINAL_RELEASE_QA.
- No BSPEC or M6.4 edits in this round.
- no commit, no push.
```

### A projektgazda technikai javítása az A11Y-07-hez (2026-10-05, harmadik üzenet; szó szerint)

```
One technical correction to A11Y-07 before Command 6 is executed.

The Moodle source confirms that a Mustache-template override alone cannot derive the dynamic H5P/activity title:

- `core_h5p/h5pembed.mustache` receives `embedurl`, `editurl`, `extraactions`; no title/activity-name value.
- `core_h5p/h5piframe.mustache` receives only `h5pid`; no title value.
- `core_h5p\player::display()` does not add the content title to the `h5pembed` template context.
- `/h5p/embed.php`, however, sets the embedded document title from `$h5pplayer->get_title()`.

Therefore correct C6-11/C6-19 so that the deterministic BUILD requirement is:

- every learner-facing H5P iframe must expose a meaningful Hungarian `title` equal to the H5P/activity title;
- Moodle core files must not be edited;
- implementation may use a maintained theme-level JS/AMD enhancement, a renderer/context extension, or an equivalent maintained local/plugin solution;
- a Mustache override is acceptable only if the implementation also supplies the required title value to its template context; do not claim the two template overrides alone can read the rendered page;
- one acceptable implementation pattern is same-origin post-render enhancement: after the H5P embed loads, derive the title from the embedded document title (`/h5p/embed.php` already sets it from the H5P title) and set the iframe `title`; the embedded H5P page must likewise ensure its inner H5P iframe receives the meaningful title;
- exact implementation is verified on the target Moodle environment;
- if none of these maintained mechanisms can be installed, record TARGET-ENVIRONMENT blocker and do not weaken the requirement.

G5a may still close at repository/spec level once this implementation requirement is pinned.
G5b remains POST-BUILD and must verify the actual rendered DOM and screen-reader announcement.

Do not reopen any other part of Command 6.
Keep the corrected A11Y-17 scope, C6-17, PR-02 marker rule and M4.1 wording exactly as in v2.

Update the fix pack only, then return the corrected final /course-fix command. STOP.
```

### Elsődleges források (a csomag összeállításakor ellenőrizve, github.com/moodle/moodle)

**Capability-alapértelmezések** (`MOODLE_405_STABLE`, `db/access.php`):

| Capability | Alapértelmezett szerepek |
|---|---|
| `moodle/site:accessallgroups` | editingteacher, manager |
| `mod/feedback:viewreports` | teacher, editingteacher, manager |
| `mod/feedback:receivemail` | teacher, editingteacher |
| `mod/feedback:viewanalysepage` | student, editingteacher, manager |
| `mod/h5pactivity:reviewattempts`, `mod/quiz:viewreports`, `mod/quiz:grade`, `mod/assign:grade`, `mod/assign:viewgrades`, `report/log:view`, `moodle/grade:viewall` | teacher, editingteacher, manager |

**A H5P két iframe-je:**
- **Külső iframe** a `mod_h5pactivity` oldalán (`mod/h5pactivity/view.php` → `player::display()`): a `core_h5p/h5pembed` sablon rajzolja. A kontextusa: `embedurl`, `editurl`, `extraactions`.
- **Belső iframe** a beágyazott oldalon (`h5p/embed.php` → `player::output()`): a `core_h5p/h5piframe` sablon rajzolja. A kontextusa: `h5pid`.
- Egyik sem kap `title` attribútumot (`MOODLE_405_STABLE`, `MOODLE_500_STABLE`, `MOODLE_501_STABLE`/`public/`).
- A `player::display()` a tartalom címét nem teszi a `core_h5p/h5pembed` kontextusába, ezért Mustache-felülírás önmagában nem tudja előállítani a címet.
- A beágyazott oldal `<title>`-je a H5P-tartalom címe: `$PAGE->set_title($h5pplayer->get_title())`.

## A. Build-blokkolók

A lépéseket a táblázat sorrendjében kell alkalmazni; a C6-19 a C6-11 után jön. Ahol a „Javítás” oszlop szó szerinti szöveget ad, ott pontosan azt kell beírni.

| ID | Hely | Bizonyíték (jelenlegi szöveg) | Javítás | Korlát, alap |
|---|---|---|---|---|
| C6-01 | `LMS – activity manifest.md` :24 (TEXT-C, „Rögzített beállítások”) | „… `feedback_save_tmp_values()`); a kérdés(ek) szövege a mező címkéje;” | a `feedback_save_tmp_values()`); után, a „a kérdés(ek) szövege” elé: „„Group mode” = „Separate groups”, „Grouping” = nincs, a kurzus „Force group mode” beállítása = „No” (BIZT-4, BIZT-3); „Enable notification of submissions” = „No” (BIZT-11); a mentor-láthatóság mechanizmusa: `Adatvédelem – tanulói adatok és AI.md` §3, „Activity-szintű adatleltár – build-rész” (PR-01);” | A BIZT-3/-4/-11 javítási korlátjából következik. A grouping és az értesítés értéke a validált korláton belüli választás, a legszűkebb szükséges hozzáférés elve szerint (HUM-PRIV-01). A BS-D1 nem nyílik újra. |
| C6-02 | ugyanott, a „Mentor-láthatóság” cella (a BIZT-2 objektív része) | „a válaszokat a `mod/feedback:viewreports` jogú szerepkör látja, ez alapból a tanári és a menedzseri szerep; ezért a láthatóságot a HUM-PRIV-01 szerint a kijelölt mentorra/értékelőre kell szűkíteni” | Két csere. (1) „ez alapból a tanári és a menedzseri szerep;” → „ez a Moodle 4.5 alapértelmezése szerint a nem szerkesztő tanári, a szerkesztő tanári és a menedzseri szerep, a rendszergazda pedig minden capabilityvel rendelkezik (a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés elfogadhatósága DPO-kérdés: BIZT-2);”. (2) „kell szűkíteni” → „kell szűkíteni (`Adatvédelem – tanulói adatok és AI.md` §3, „Activity-szintű adatleltár – build-rész”)” | a mondat többi része változatlan |
| C6-03 | `LMS – H5P runtime acceptance.md` :79 (15. pont), a pont végén | „… és azzal, amit a tanulói felület állít (Program terv §4, Adatvédelem §5).” | a mondat után: „ A TEXT-C-nél a beállítást is vissza kell olvasni (`Adatvédelem – tanulói adatok és AI.md` §3, „Activity-szintű adatleltár – build-rész”): nincs csoport nélküli, `mod/feedback:viewreports` jogú mentorfiók, mert a csoport nélküli néző az elemzőoldalon (`analysis.php`) és az Excel-exportban minden választ látna (BIZT-3); a beküldési értesítés kikapcsolva (BIZT-11).” | a BIZT-9 kiterjesztett negatív esetei bizonyíték-kapuk maradnak |
| C6-04 | `Adatvédelem – tanulói adatok és AI.md` §3, a :93 („A lista M2-, M3- és M7-sorának szabálya …”) után, a „## 4.” elé | — (a build-rész ma nincs meg; leltár 103. sor) | új alszakasz, az **A.1** pont szó szerinti szövegével | csak a címzettek, a szerepkör/capability és a mechanizmus kerül bele |
| C6-05 | `Adatvédelem…` :168 (PR-01) | „- [ ] teljes activity-szintű adatleltár elkészült (§3), a nem Moodle-ben vezetett mentori jegyzettel és a Google-sablonokkal együtt; <!-- gate: build, repo-fixable -->” | A sor két sorra cserélődik. (1) „- [x] az activity-szintű adatleltár build-része elkészült (§3, „Activity-szintű adatleltár – build-rész”): címzettek, Moodle-szerepkör/capability és a mentor-láthatóság mechanizmusa profilonként, az `LMS – activity manifest.md` §2 „Profil” oszlopával activityre bontva; **repo-spec: 2026-10-05** (PR-01; BIZT-2 objektív része, BIZT-3, BIZT-4, BIZT-11);”. (2) „- [ ] az activity-szintű adatleltár többi mezője (adatmező, cél, a jogalap- és a megőrzési sor hozzárendelése, törlés, export/hozzáférési kérelem, harmadik fél, kiskorú-specifikus szabály) kitöltve, a nem Moodle-ben vezetett mentori jegyzettel és a Google-sablonokkal együtt (§3: az LMS-gazda és a privacy felelős; vétó: DPO); <!-- gate: release-evidence -->” | a kettébontás a leltár 103. sorának D-a-val elfogadott javaslata |
| C6-06 | `Adatvédelem…`: a §10 forráslistája után, a záró „Ez a dokumentum adatvédelmi követelményrendszer, …” bekezdés elé | — (a tájékoztatónak nincs szövege, a PT §7-ben csak sablon van) | új szakasz, az **A.2** pont szó szerinti szövegével | a tanulói szövegbe jelölő nem kerül (0. szakasz, második üzenet) |
| C6-07 | `Adatvédelem…` :169 (PR-02) | „- [ ] learner-facing adatvédelmi tájékoztató rövid, magyar és érthető; <!-- gate: build, repo-fixable -->” | Két sor. (1) „- [x] learner-facing adatvédelmi tájékoztató rövid, magyar és érthető: a szövege a §11-ben; **repo-spec: 2026-10-05** (PR-02);”. (2) „- [ ] a tájékoztató belső mezői kitöltve, és az értékük a §11 szerint a tanulói szövegbe került (`PRIVACY_CONTACT_TO_CONFIGURE`: az adatvédelmi kontakt; `DPO_RETENTION_TO_CONFIRM`: az LMS-Z-06 megőrzése, BS-D6); a jelölő sem a tanulói szövegben, sem a renderelt tanulói tartalomban nem jelenik meg; <!-- gate: release-evidence -->” | a jelölők csak belső mezőben szerepelnek |
| C6-08 | `LMS – activity manifest.md` :114 | „- az adatvédelmi tájékoztató (HUM-PRIV-01);” | „- az adatvédelmi tájékoztató (HUM-PRIV-01): Moodle-oldal (PAGE-C) a kurzus elején; szövege: `Adatvédelem – tanulói adatok és AI.md` §11 (PR-02);” | — |
| C6-09 | A11Y-07: `LMS – activity manifest.md` :16 (H5P-C, „A11y / fallback” cella) | „WCAG 2.2 AA pre-flight; húzásmentes út; felirat/leirat; alacsony adatú szöveges út \|” | a cella végére: „; A11Y-07: a H5P-szerkesztő nyelve (Language) magyar, a H5P-tartalom címe (Title) az activity §2 szerinti „Név” értéke, és minden tanulói H5P-iframe `title` attribútuma ez a cím (Moodle core módosítása nélkül, karbantartott theme-, renderer- vagy local/plugin szintű megoldással; build-specifikáció: `LMS – hozzáférhetőségi sztenderd.md`, A11Y-07)” | projektgazdai döntés (2026-10-05, második és harmadik üzenet) |
| C6-10 | A11Y-07: `LMS – hozzáférhetőségi sztenderd.md` :88 | „- [ ] **Magyar nyelv + iframe-title** — az elem nyelve magyarra állítva, az iframe-nek **beszédes magyar címe** van (képernyőolvasó felolvassa, melyik aktivitásban jár a madrih). <!-- gate: build, repo-fixable -->” | a sor helyére az **A.4** pont szó szerinti szövege jön: lezárt build-rész, specifikáció-alpont, nyitott renderbizonyíték | a renderbizonyíték nem `RUNTIME_VERIFIED`; a követelmény nem gyengül |
| C6-11 | A11Y-07: `LMS – H5P runtime acceptance.md`, „Accessibility acceptance”, a „- screen-reader ellenőrzés;” pont | „- screen-reader ellenőrzés;” | „- screen-reader ellenőrzés (H5P-nél: a renderelt DOM-ban minden tanulói H5P-iframe – a lecke oldalán lévő külső és a beágyazott oldalon lévő belső is – `title`-je a várt magyar H5P-/activity-cím, a képernyőolvasó ezzel azonosítja a beágyazott tartalmat, és magyarul olvassa fel; `LMS – hozzáférhetőségi sztenderd.md`, A11Y-07);” | új pont nem kerül be, mert az RT-A11Y-azonosítók a pontok sorrendjét követik; az RT-A11Y-03 sora és állapota változatlan |
| C6-19 | A11Y-07: `LMS – H5P runtime acceptance.md`, „Environment record” táblázat, a „Browser/device matrix” sor után | — | új sor: „\| A H5P-iframe-cím megvalósítása (A11Y-07): karbantartott theme-szintű JS/AMD-kiegészítés, renderer-/kontextusbővítés vagy egyenértékű local/plugin megoldás, Moodle core módosítása nélkül; ha egyik sem telepíthető: TARGET-ENVIRONMENT blokkoló \| `RUNTIME_OUTPUT` \| \| \|” | a célkörnyezet ténye; a gép az unresolved environment-sorok között követi (ENVIRONMENT-RECORD +1) |
| C6-12 | A11Y-17: `LMS – activity manifest.md` §2 „Kurzusszintű elemek”, a „- a kurzus opcionális AI-segédje …” pont után | — (ma csak elv: STD §5; leltár 135. sor) | új pont, az **A.3** pont szó szerinti szövegével | az eredeti hatókör: „videós/adatigényes lecke”, szűkítés nélkül; a completion-feltétel nem változik |
| C6-13 | A11Y-17: `LMS – hozzáférhetőségi sztenderd.md` :113 | „- [ ] Adatigényes/videós leckéhez offline letölthető, alacsony adatigényű változat + eszközhöz-jutási pont (a ken közös eszköze, illetve az F-peula); eszközhiány nem zár ki a completionből <!-- gate: build, repo-fixable -->” | Két sor. (1) „- [x] Adatigényes/videós leckéhez offline letölthető, alacsony adatigényű változat + eszközhöz-jutási pont (a ken közös eszköze, illetve az F-peula); eszközhiány nem zár ki a completionből — build-definíció és hatókör: `LMS – activity manifest.md` §2, „Kurzusszintű elemek”; **repo-spec: 2026-10-05** (A11Y-17)”. (2) „- [ ] az adatigényes/videós leckék offline változata a buildben letölthető és képernyőolvasóval olvasható <!-- gate: post-build -->” | — |

### A.1 — a C6-04 szövege (szó szerint)

```markdown
### Activity-szintű adatleltár – build-rész (PR-01)

A fenti mezőtáblázatból a buildhez szükséges rész: a **címzettek**, a **Moodle-szerepkör/capability** és a **mentor-láthatóság mechanizmusa**, profilonként. Egy activity sorát az `LMS – activity manifest.md` §2 „Profil” oszlopa köti ide; az activitynkénti eltéréseket a manifest adott sora és a fenti „Külön review” lista rögzíti. A többi mező (adatmező, cél, a jogalap- és a megőrzési sor hozzárendelése, törlés, export/hozzáférési kérelem, harmadik fél, kiskorú-specifikus szabály) kitöltése az LMS-gazda és a privacy felelős feladata (§9). A Moodle-alapértelmezések forrása a Moodle 4.5 `db/access.php` fájljai (`MOODLE_405_STABLE`); a célverzión a tényleges szerepkiosztást és capability-állapotot stagingben tesztfiókkal vissza kell olvasni (runtime acceptance 15. pont; §5).

**Szerepkörök a kurzusban:**

| Moodle-szerep | Kinek | `mod/feedback:viewreports` | `moodle/site:accessallgroups` | Mit lát a P2 szövegekből |
|---|---|---|---|---|
| Tanuló (Student) | a madrihok | nincs | nincs | csak a saját válaszát; a TEXT-C-ben a `mod/feedback:viewanalysepage` tiltva (`LMS – activity manifest.md` §1) |
| Nem szerkesztő tanár (Non-editing teacher) | a kijelölt mentor/értékelő | van (alapértelmezés) | nincs (alapértelmezés; nem kaphatja meg) | a TEXT-C-ben csak a saját mentor-csoportja válaszait (lent) |
| Szerkesztő tanár (Editing teacher) | a kiosztást a privacy felelős tölti ki | van (alapértelmezés) | van (alapértelmezés) | csoporttól függetlenül minden választ |
| Menedzser (Manager) | a kiosztást a privacy felelős tölti ki | van (alapértelmezés) | van (alapértelmezés) | csoporttól függetlenül minden választ |
| Rendszergazda (site administrator) | a kiosztást a privacy felelős tölti ki | minden capability | minden capability | minden választ |

A szerkesztő tanári, a menedzseri és a rendszergazdai, csoporttól független hozzáférés elfogadhatósága DPO-kérdés (BIZT-2): ez a szakasz nem dönti el.

**Profilonként: ki lát még tanulói adatot** (Moodle 4.5 alapértelmezés):

| Profil (`LMS – activity manifest.md` §1) | A tanuló | Ki lát még (capability) | Csoport szerinti szűkítés | Megjegyzés |
|---|---|---|---|---|
| H5P-C | a saját próbálkozásait | a próbálkozás-riportot (`mod/h5pactivity:reviewattempts`): nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve: DPO-kérdés (BIZT-5) | a tanuló-lokális lépések nem tárolódnak (manifest §2); a riport tényleges tartalmát a runtime acceptance 15. pontja olvassa vissza |
| QUIZ-D, QUIZ-M | a saját próbálkozásait és eredményét | a kvízriportot és az értékelést (`mod/quiz:viewreports`, `mod/quiz:grade`): nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5) | a zárt kvíz pontszámát az értékelő látja (§5) |
| ASSIGN-S, ASSIGN-M, GATE-CP | a saját beadványát és értékelését | az értékelői nézetet (`mod/assign:grade`, `mod/assign:viewgrades`): nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5) | P2 beadandót csak a kijelölt értékelő/mentor lát, csak ha ténylegesen szükséges (§5) |
| TEXT-C | a saját válaszát (felülírhatja) | a válaszokat (`mod/feedback:viewreports`): a kijelölt mentor a saját csoportjában; a szerkesztő tanár, a menedzser és a rendszergazda csoporttól függetlenül | Separate groups (a mechanizmus lent) | — |
| FEEDBACK-N (Z.4) | — | a válaszokat név nélkül megjelenítve (`mod/feedback:viewreports`; HUM-PRIV-03) | — | a mentor hozzáférése DPO-kérdés (BIZT-6) |
| FORUM-C | a kurzus résztvevőinek posztjait | a kurzus résztvevői | — | a résztvevő előre tudja, hogy a csoport látja (§5) |
| PAGE-C | — | — | — | tanulói adatot nem rögzít |

A kurzusnaplót (`report/log:view`) és a pontkönyvet (`moodle/grade:viewall`) alapértelmezésben a nem szerkesztő tanár, a szerkesztő tanár és a menedzser látja.

**A mentor-láthatóság mechanizmusa (TEXT-C).** Projektgazdai döntés (2026-10-05; `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`, 1. szakasz 2. pont). Ez technikai hozzáférés-szűkítés, nem a BS-D1 által elvetett, csoport-alapú kapuállapot. A döntés feltételes: a mechanizmust az RT-P0-15 kiterjesztett stagingtesztjének kell igazolnia; a DPO QA megmarad.

- A TEXT-C activity csoportmódja („Group mode”) „Separate groups”, groupingot nem kap („Grouping”: nincs); a kurzus „Force group mode” beállítása „No” (BIZT-4, BIZT-3). Group- vagy Grouping-alapú hozzáférési feltétel sehol nincs (BS-D1).
- A kurzus csoportjai a mentor-csoportok: minden tanuló a saját mentor-csoportjában van, és a kijelölt mentor ugyanennek a csoportnak a tagja. Más célú csoport a kurzusban nem jön létre; ha mégis kell, a TEXT-C elkülönítése új build-spec kérdés (BIZT-3, grouping-ág).
- A mentor a nem szerkesztő tanári szerepet csak a csoportba sorolása után kapja meg, mert a csoport nélküli, `mod/feedback:viewreports` jogú néző az elemzőoldalon és az Excel-exportban minden választ látna (BIZT-3).
- A mentor nem kap `moodle/site:accessallgroups` jogot; a tanuló nem kap riport-capabilityt.
- „Enable notification of submissions” = „No” (BIZT-11): így a `mod/feedback:receivemail` jogúak nem kapnak a beküldőről nevet és közvetlen linket tartalmazó értesítést.
```

### A.2 — a C6-06 szövege (szó szerint)

```markdown
## 11. A kurzus adatvédelmi tájékoztatója (tanulói szöveg)

*Fejlesztői feltétel (nem tanulói szöveg):*
- A tájékoztató a kurzus elején, Moodle-oldalként (PAGE-C) áll (`LMS – activity manifest.md` §2, „Kurzusszintű elemek”).
- Tartalma a §3–§8 lezárt döntéseiből és a `Program terv.md` §7 sablonjából származik (HUM-PRIV-01–04).
- A „Ki látja?” rész a §5 lezárt szabályát közli. Hogy a tényleges beállítás ezzel egyezik-e, azt a runtime acceptance 15. pontja olvassa vissza; a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés (BIZT-2) és a nem TEXT-C profilok szűkítése (BIZT-5) DPO-kérdés. A tájékoztató a §1 release-szabálya szerint a DPO jóváhagyása előtt nem élesíthető.

**Belső mezők, a közzététel előtt kitöltendők.** A jelölők csak ebben a táblázatban és a §9 bizonyíték-tételében szerepelhetnek. A tanulói szövegbe és a renderelt tanulói tartalomba soha nem a jelölő kerül, hanem a kitöltött érték.

| Mező | Mi kerül a tanulói szövegbe | Hová | Állapot |
|---|---|---|---|
| `PRIVACY_CONTACT_TO_CONFIGURE` | az adatvédelmi kontakt tényleges elérhetősége, külön sorban | a „Kihez fordulhatsz?” bekezdés alá | nyitott: a HUM-PRIV-01 szerint jóváhagyott kontakt (`Program terv.md` §4) |
| `DPO_RETENTION_TO_CONFIRM` | egy új sor a „Meddig őrizzük meg?” listába: „a Z.3 szöveges válaszaidat:” és utána a DPO által rögzített megőrzés | a „szöveges reflexióidat” sor után | nyitott: BS-D6, LMS-Z-06 (§3) |

> **Adatvédelem a kurzusban – röviden**
>
> **Mit rögzítünk?** A Moodle-fiókodat, a részvételedet és azt, hogy mit teljesítettél; a kvízek és a kapuk eredményét; és azt, amit egy beadandóba vagy egy szöveges mezőbe beírsz vagy feltöltesz. A szöveges mezőkbe írt válaszaid a neveddel együtt rögzülnek, hogy a mentorod szükség esetén neked szóló visszajelzést adhasson. Felesleges személyes adatot nem kérünk. Érzékeny személyes történetet (például családi, egészségügyi vagy gyermekvédelmi ügyet) egyik feladat sem kér kötelezően: írhatsz fiktív vagy általánosított példát is.
>
> **Miért?** Hogy lásd a saját haladásodat a teljesítési kapukon, és hogy a kijelölt mentorod vagy értékelőd – ahol ez ténylegesen szükséges – visszajelzést tudjon adni. A program fejlesztéséhez csak összesített, beazonosíthatatlan adatot használunk. Egyedi szöveget más célra csak névtelenítve és a külön, visszavonható hozzájárulásoddal használunk; ha nem járulsz hozzá, az semmiben nem korlátoz a kurzusban.
>
> **Ki látja?** A kvízek és a kapuk eredményét az értékelőd. A szöveges válaszaidat és a beadandóidat a kijelölt mentorod vagy értékelőd, és ő is csak akkor nézi meg, ha ténylegesen szükséges. A kurzusfórumra írt hozzászólásodat a kurzus résztvevői látják. A szöveges válaszaidat a többi résztvevő nem látja.
>
> **Meddig őrizzük meg?**
> - a fiókodat, a részvételedet és a végső teljesítésedet: a képzés vége után 24 hónapig;
> - a kvízpróbálkozásaid részleteit: a végső eredményed megerősítése után 90 napig;
> - a végső pontszámodat és a kapueredményedet: 24 hónapig;
> - a szöveges reflexióidat (a záró reflexiót is): a képzés vége után 90 napig;
> - a beadandóidat és a peulaterveidet: a képzés vége után 12 hónapig;
> - a mentorod fejlesztési jegyzetét (akkor is, ha nem a Moodle-ben készül; csak a fejlődésed támogatásához szükséges minimum kerül bele): az utolsó mentorálás után 6 hónapig;
> - a mentori beszélgetéseitek naplóját (csak a dátum, a résztvevők, az időtartam, a téma kategóriája és az utánkövetés, a beszélgetés tartalma nem): az utolsó mentorálás után 6 hónapig;
> - a peulákon név nélkül, papíron begyűjtött munkalapokat: összesítés után 30 napon belül megsemmisítjük;
> - a záró képzési visszajelzés (Z.4) válaszait: 90 napig, utána csak összesítve.
>
> A megőrzési idő lejárta után az adatot töröljük vagy anonimizáljuk.
>
> **Fotó, videó, hang.** Alapból nem készül felvétel. Saját fotó vagy videó csak akkor kötelező, ha a feladathoz szakmailag elengedhetetlen; egyébként felvétel nélkül is teljesítheted a feladatot. Felvétel csak külön, önkéntes hozzájárulással készül – ha 18 év alatti vagy, a hozzájárulást te és a gondviselőd együtt adjátok meg –, és legfeljebb 90 napig őrizzük meg, hacsak külön nem járulsz hozzá a hosszabb megőrzéshez.
>
> **AI-segéd.** Az AI használata mindig opcionális: minden feladat nélküle is teljesíthető. Saját AI-fiókra nincs szükség: a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj.
>
> **Záró visszajelzés (Z.4).** A válaszok név nélkül jelennek meg a feldolgozásban.
>
> **Kihez fordulhatsz?** Ha kérdésed vagy kérésed van az adataiddal kapcsolatban, az adatvédelmi kapcsolattartónkhoz fordulhatsz; az elérhetősége ez alatt áll.
```

**Mondatonkénti forrás (A.2):**

- **Mit rögzítünk?**
  - a felsorolás: a §3 mátrixa;
  - a névvel rögzülés: a manifest TEXT-C profilja (nem anonim, BS-D4);
  - „Felesleges személyes adatot nem kérünk”: PT §7;
  - az érzékeny történet: a §2 alapértelmezése és a §9 :173.
- **Miért?** A PT §7 sablonja és a „Célonként elkülönített adatkezelés” bekezdés.
- **Ki látja?** §5.
- **Meddig őrizzük meg?**
  - a megőrzési sorok: a §3 mátrixa (HUM-PRIV-01, -02);
  - a mentori napló: §5;
  - „töröljük vagy anonimizáljuk”: PT §7.
- **Fotó, videó, hang:** §6 (HUM-PRIV-02) és §4.
- **AI-segéd:** §7 (HUM-PRIV-04); az utolsó két mondat a §7 kanonikus tanulói szövege, szó szerint.
- **Záró visszajelzés:** a §8 kanonikus mondata, szó szerint.
- **Kihez fordulhatsz?** PT §4 és §7. Az elérhetőség belső mezőből kerül a szövegbe.

### A.3 — a C6-12 szövege (szó szerint)

```markdown
- az alacsony adatigényű, offline letölthető leckeváltozat (`LMS – hozzáférhetőségi sztenderd.md` §5; A11Y-17):
  - **Melyik leckéhez:** minden videós vagy adatigényes online leckéhez (a sztenderd §5: „Kötelező minimum a videós/adatigényes leckékhez”; A11Y-17). A build kétféleképpen azonosítja ezeket.
    - (a) Minden online lecke, amelynek specifikációjában videó szerepel (`video` fajtájú média-asset). Az, hogy a videó elkészült-e, vagy a helyén még tartalék áll, ezen nem változtat.
    - (b) Minden további online lecke, amelyet a saját fejlesztői megjegyzése adatigényesnek vagy csak online teljesíthetőnek jelöl (a sztenderd §5 utolsó pontja).
    - A 2026-10-05-i állapotban ez 18 lecke: M1.1, M1.2, M1.3, M2.1, M2.2, M2.3, M2.4, M3.1, M3.2, M3.3, M3.4, M4.1, M5.1, M6.1, M6.2, M7.2, M7.3, M7.4. Az (a) pont szerint mind videós; az M4.1 a saját megjegyzése szerint is adatigényes.
  - **Moodle-forma:** Moodle File erőforrás a lecke activityje mellett, ugyanabban a szakaszban, saját completion nélkül.
  - **Tartalom:** a sztenderd §5 és az M4.1 :68 szerint a narrációk és a videók teljes szöveges leirata és a kulcsképek, alt-szöveggel vagy szöveges megfelelővel; szövegalapú, képernyőolvasóval olvasható dokumentum.
  - **Eszközhöz jutás:** a ken közös eszköze, az F-peula és a Csendes pótlás, a sztenderd §5 szerint; az eszközhiány nem zár ki a completionből. A lecke completion-feltétele nem változik.
```

**A hatókör forrása:**
- A szöveg a `LMS – hozzáférhetőségi sztenderd.md` :113 (A11Y-17) „Adatigényes/videós leckéhez” mondatából és a §5 :52–55 soraiból jön: „Kötelező minimum a videós/adatigényes leckékhez”, „(a videós leckék adatigényesek)”, „Tedd explicitté a lecke fejlesztői megjegyzésében, ha egy elem csak online, élő neten teljesíthető”.
- További forrás: a `Média-assetek/PRODUCTION-STACK.md` :521 („videós/adatigényes leckék”) és az M4.1 :68.
- A leltár 135. sora két utat kínál („vagy”). A (b) út („csak a videót/adatigényes médiát ténylegesen szállító leckékhez”) szűkebb a tételnél, és az 1. változat ezen túl a videóra is szűkített. A projektgazda pontosítása szerint az eredeti hatókör érvényes, ezért ez a változat az (a) utat követi: a build-definíció (erőforrás-típus, mely leckékhez, tartalom) a manifestbe kerül, szállítási feltétel és videóra szűkítés nélkül.

### A.4 — a C6-10 szövege (szó szerint; a :88 sor helyére)

```markdown
- [x] **Magyar nyelv + iframe-title — build-specifikáció (G5a)** — az elem nyelve magyarra állítva, az iframe-nek **beszédes magyar címe** van (képernyőolvasó felolvassa, melyik aktivitásban jár a madrih); a staging-megvalósítás az alpontban rögzítve; **repo-spec: 2026-10-05** (A11Y-07; projektgazdai döntés, 2026-10-05)
  - *(Build-specifikáció, projektgazdai döntés, 2026-10-05:*
    - *(1) A H5P-szerkesztő nyelve (Language) magyar; a H5P-tartalom címe (Title) az activity „Név” értéke (`LMS – activity manifest.md` §1, H5P-C; §2 „Név”).*
    - *(2) Minden tanulói H5P-iframe-nek beszédes magyar `title` attribútuma van, amelynek értéke a H5P-tartalom, illetve az activity címe. Ez a lecke oldalán lévő külső iframe-re és a beágyazott oldalon lévő belső iframe-re is vonatkozik.*
    - *(3) A core Moodle 4.5–5.1 ezt nem adja meg, és Mustache-sablon felülírása önmagában sem tudja előállítani. A külső iframe-et a `core_h5p/h5pembed` sablon rajzolja; a kontextusa `embedurl`, `editurl`, `extraactions`, és a `player::display()` a tartalom címét nem teszi bele. A belső iframe-et a beágyazott oldalon (`h5p/embed.php`) a `core_h5p/h5piframe` rajzolja, ennek kontextusa csak `h5pid`. Egyik sablon sem kap `title` attribútumot. A beágyazott oldal dokumentumcímét viszont a `h5p/embed.php` a H5P-tartalom címéből állítja be (`$h5pplayer->get_title()`).*
    - *(4) Megvalósítás, Moodle core fájl módosítása nélkül, a következők valamelyikével:*
      - *karbantartott, theme-szintű JS/AMD-kiegészítés;*
      - *renderer- vagy kontextusbővítés;*
      - *egyenértékű, karbantartott local/plugin megoldás.*

      *Mustache-felülírás csak akkor elfogadható, ha a megvalósítás a szükséges címet a sablon kontextusába is átadja: a két sablon felülírása önmagában nem olvassa ki a renderelt oldalt.*

      *Egy elfogadható minta az azonos eredetű, renderelés utáni kiegészítés. Amikor a H5P-beágyazás betöltődött, a kiegészítés a beágyazott dokumentum címéből (ezt a `h5p/embed.php` a H5P-címből állítja be) veszi az értéket, és beállítja vele a külső iframe `title`-jét. A beágyazott H5P-oldalon ugyanígy gondoskodni kell arról, hogy a belső H5P-iframe is megkapja a beszédes címet.*

      *A pontos megvalósítást a cél-Moodle-környezetben kell igazolni.*
    - *(5) Ha egyik karbantartott mechanizmus sem telepíthető a célkörnyezetbe, kifejezett TARGET-ENVIRONMENT blokkolót kell rögzíteni (`LMS – H5P runtime acceptance.md`, Environment record); a követelmény nem gyengül.*
    - *Ez nem felmentés a hozzáférhetőségi követelmény alól, és nem állítja, hogy a core Moodle teljesíti.)*
- [ ] **Magyar nyelv + iframe-title — renderelt bizonyíték (G5b):** a stagingben renderelt DOM-ban minden tanulói H5P-iframe (a külső és a belső is) `title`-je a várt magyar H5P-/activity-cím; a képernyőolvasó ezzel azonosítja a beágyazott tartalmat, és magyarul olvassa fel (`LMS – H5P runtime acceptance.md`, Accessibility acceptance, RT-A11Y-03) <!-- gate: post-build -->
```

**Megjegyzés (3. változat):**
- A 2. változat a két Mustache-sablon felülírását úgy írta le, mintha az a renderelt oldalból kiolvashatná a címet. Ez téves: a sablonok kontextusában a cím nincs benne (0. szakasz, elsődleges források).
- A 3. változat a projektgazda technikai javítása szerint a mechanizmus helyett a követelményt és az elfogadható megvalósítási utakat rögzíti.
- A G5a a repó- és spec-szinten ezzel lezárható. A G5b post-build bizonyíték marad: a renderelt DOM-ot és a képernyőolvasó bejelentését igazolja.

## B. Konzisztencia-javítások (a projektgazda 2026-10-05-i utasításai, 0. szakasz)

| ID | Hely | Bizonyíték | Javítás | Korlát |
|---|---|---|---|---|
| C6-14 | `Modulok/M0/M0 – Kickoff, keret, technika.md` :12 | „* **Heti offline:** péntek 2. sáv – **Peula A (M0.A, 45–60’)** – Kickoff & ismerkedés + technikai segítségpont” | „* **Offline alkalom:** a központi naptár szerint – **Peula A (M0.A, 45–60’)** – Kickoff & ismerkedés + technikai segítségpont” | nap, idősáv és jelölő nem kerül bele |
| C6-15 | `Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md` :6 | „* **Heti offline:** péntek 2. sáv – M1.A (1. hét) és M1.B (2. hét), kb. 45’ + 45’” | „* **Offline alkalmak:** a központi naptár szerint – M1.A (1. hét) és M1.B (2. hét), kb. 45’ + 45’” | az „1. hét / 2. hét” és a „45’ + 45’” nem változik |
| C6-16 | `Program terv.md` :392 (az utasítás „§9.3”-at ír; a sor a §9.2 2. pontja) | „A gyermekvédelmi tartalmaknál (M3.3, M3.B, az M3 kapuja, az M7 gyermekvédelmi részei) ez élesítés előtt egyszeri, írásos „átnéztem”” | a zárójel után: „ **[a felsorolás példálózó; a kánoni hatókör a `Gyermekvédelem – release gate.md` §2 — 2026-10-05, `Emberi jóváhagyás szükséges.md` 11. szakasz]**” | a HUM :481 mintája; a történeti felsorolás marad |
| C6-17 | `LMS – activity manifest.md` :200 (§6, 9. pont) | „A gyermekvédelmi tartalmaknál (M3.3, M3.B, az M3 kapuja, az M7 gyermekvédelmi részei) élesítés előtti QA-lépés a Memuna …” | ugyanaz a jelölés a zárójel után | A projektgazda megerősítette („Keep C6-17”). Az RR :24 („köztük …”) már példálózó, az RR :85 más szabály, a HUM :33 történeti sor; ezek nem változnak. |
| C6-18 | `Modulok/M4/Online leckék/M4.1 – Mit üzen a testem – Nonverbális kiállás.md`, SLIDE 4 | NAR-06 (:996, :1001); kártyacímkék (:1012–1013, :1037–1038); a 2. kérdés (:1042) és opciói | a **B.2** pont cseréi | A ✅ ugyanazon az opción marad. A „Mit látunk?” blokk és a fejlesztői jegyzet nem változik. A projektgazda elfogadta (második üzenet). |

### B.2 — a C6-18 cseréi (modalitássemleges szóhasználat, elfogadva)

- A „példa” az egész példát jelenti: a „Példa 1” és a „Példa 2” egy-egy képpárt nevez meg.
- A „változat” egy páron belül a bal, illetve a jobb oldali tagot jelenti.
- A „két kép” a páron belüli bal és jobb tagra utalt. A „két példa” a két páros közötti különbségre fordítaná, ezért itt a „változat” szó kell.

| Hely | Most | Utána |
|---|---|---|
| NAR-06 1. sora (@source) | „Most néhány pillanatképet nézünk meg.” | „Most néhány példát nézünk meg.” |
| NAR-06 (@source) | „**mi a különbség** a két kép között,” | „**mi a különbség** a két változat között,” |
| kártyacímke (`replace_all`, pontosan 2 előfordulás) | „**Bal oldali kép:**” | „**Bal oldali változat:**” |
| kártyacímke (`replace_all`, pontosan 2 előfordulás) | „**Jobb oldali kép:**” | „**Jobb oldali változat:**” |
| 2. kérdés | „Melyik képen látsz **nyitottabb kiállást**, és miért?” | „Melyik változatban látsz **nyitottabb kiállást**, és miért?” |
| 2. kérdés, 1. opció | „„A bal oldalin – mert” | „„A bal oldaliban – mert” |
| 2. kérdés, 2. opció (✅) | „„A jobb oldalin – mert” | „„A jobb oldaliban – mert” |

**Következmények:**
- A NAR-06 `@source`-a megváltozik, ezért a média-buildet kétszer kell futtatni, majd a `check` és a `reconcile` jön. A leirat ebből a forrásból generálódik.
- A narráció még legyártandó („pending-rights”), később újrarenderelhető (a VO QA-repó végzi).
- Ha a csere után is marad „kép” a NAR-06-ban vagy a 2. kérdésben, a lépés megáll.

## C. Megállási pontok

Nincs előre ismert megállási pont: az 1. változat A11Y-07-es pontját a projektgazda pontosítása lezárta. A `/course-fix` általános megállási szabályai érvényesek. Ha egy lépés a 0. szakasz nyitott tételeitől függ, a lépés megáll.

## D. Várt gépi állapot a csomag után

| Számláló | Változás | Oka |
|---|---|---|
| `CHECKLIST-BUILD` | 4 → **0** | PR-01, PR-02, A11Y-07, A11Y-17 |
| `RELEASE-EVIDENCE` | +2 | a PR-01 többi mezője; a PR-02 belső mezői |
| `POST-BUILD: CHECKLIST` | +2 | az A11Y-07 renderbizonyítéka; az A11Y-17 buildbeli megléte |
| `POST-BUILD: ENVIRONMENT-RECORD` | +1 | C6-19 |
| `MANIFEST-OPEN 3` (BSPEC-05, -06, -07) | változatlan | ez a csomag nem nyúl hozzájuk |

A `MOODLE-BUILD-VERDICT` ezért **`NOT_READY` marad, kizárólag a BSPEC-05/06/07 miatt**. Az A11Y-15/18 és a SAFE-7 nem változik.
