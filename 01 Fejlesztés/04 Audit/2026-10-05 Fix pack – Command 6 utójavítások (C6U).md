# Fix pack — Command 6 utójavítások (C6U, 2026-10-05)

> **Audit trail, nem kánon.** Szűk, csak objektív utójavítás.
>
> - **Bemenet:** a Command 6 célzott újraellenőrzésének findingjai, a lencsék szerint:
>   - biztonság-jog: C6-BIZT-2, -5, -6, -7;
>   - nyelvi: C6-NYELV-1, -2, -4, -5, -6;
>   - implementációs: C6-IMPL-1, -2, -3, -4, -6, -7, -8.
>
>   A findingok teljes leírása: `2026-10-05 course-fix napló – Command 6.md`.
> - **Alap:** a lezárt kánon és a projektgazda 2026-10-05-i, szó szerint rögzített utasítása (0. szakasz).
> - **Állapot:** munkaág `fix/moodle-build-hardening`; javítás nem történt, commit nincs.
> - **Nem tárgya ennek a csomagnak, és nyitva marad:**
>   - C6-BIZT-1, C6-BIZT-3, C6-BIZT-4, C6-BIZT-8 (DPO, jogi felelős, Memuna);
>   - C6-IMPL-5 (projektgazda, Memuna QA);
>   - C6-NYELV-3 (DPO);
>   - SAFE-7, A11Y-15/18, BSPEC-05/06/07 és M6.4.

**Állapotszabály.** A PR-01 és a PR-02 build-checklist sora a checkerben lezárt (`[x]`, „repo-spec”). Érdemben mégsem tekinthetők késznek, amíg ez a csomag sikeresen le nem fut. A fenti emberi és DPO-tételek ettől függetlenül nyitva maradnak.

## 0. A projektgazda utasítása (2026-10-05, szó szerint)

```
Before M6.4 or the BSPEC round, close the objective post-fixes introduced by Command 6.

Do NOT start a general review.

Create one narrow audit-only fix pack and return one user-invoked /course-fix command for ONLY these already-identified objective findings:

- C6-BIZT-2 / C6-NYELV-1
- C6-NYELV-2
- C6-IMPL-2
- C6-BIZT-5 / C6-NYELV-5
- C6-BIZT-6
- C6-BIZT-7
- C6-NYELV-4
- C6-IMPL-1
- C6-IMPL-3
- C6-IMPL-4
- C6-IMPL-6
- C6-IMPL-7
- C6-IMPL-8
- C6-NYELV-6

These are objective consistency/restoration fixes from already closed canon. Do not convert any of the human/DPO questions below into project-owner decisions.

Exact constraints:

1. C6-BIZT-2 / NYELV-1
Align the learner-facing privacy text with the existing canonical rule:
- political, religious, health, safeguarding or other special-category/sensitive case data must NOT be entered into a normal learning activity;
- if a disclosure nevertheless appears, it is removed from Moodle and handled through the separate safeguarding/incident process.
Do not weaken this to “not required” or “prefer not to enter”.
Use the existing canonical wording/basis from `Adatvédelem – tanulói adatok és AI.md` §3 and the already closed HUM-PRIV decision.

2. C6-NYELV-2
Restore the two lost canonical qualifications:
- where applicable, retention is “a cél teljesüléséig, legfeljebb 90 nap”, not merely “90 nap”;
- the field-observation note is included under the existing “Mentori fejlesztési jegyzet” handling, as already stated in canon.
Do not invent a new retention period.

3. C6-IMPL-2
Restore all four PR-01 runtime-test conditions from D-a…D-d §2:
- two mentors;
- two groups;
- direct-URL access test;
- learner-to-learner visibility test.
Do not change their expected semantics.

4. C6-BIZT-5 / NYELV-5
Fix the missing verb/grammar and preserve the existing rule that the assigned mentor reads mandatory submissions as required by the canonical activity model.
No access-policy expansion.

5. C6-BIZT-6
Replace the erroneous “téma kategóriája” with the canonical “cél kategóriája”.

6. C6-BIZT-7
For the already-decided optional archival/photo/video consent rule:
- under 18: participant + guardian together;
- 18+: participant.
Restore the existing HUM-PRIV-02 rule. Do not introduce a new consent basis.

7. C6-NYELV-4
Use the exact canonical Z.4 activity/title wording already present in the manifest/module source. Do not create a new label.

8. C6-IMPL-1
Correct the A11Y-07 implementation example.
Do NOT hard-code an unsafe assumption that simply splitting on `|` always yields the title.
The normative result remains: iframe `title` equals the canonical H5P/activity title.
A maintained implementation may normalize the embedded document title by removing the Moodle/site suffix, but the exact delimiter/normalization must be verified on the target environment.
Keep this as implementation guidance, not a new accessibility rule.

9. C6-IMPL-3
Disambiguate references so `A11Y-07` (checklist/finding) and `RT-A11Y-07` (runtime test, if that is the actual runtime ID) cannot be confused. Use the repository’s exact existing IDs.

10. C6-IMPL-4
Correct the offline File-resource availability/opening rule using the already approved schedule/access model. Do not invent a date or weaken prerequisites.

11. C6-IMPL-6
Propagate the already approved A11Y-07 G5a/G5b decision into HUM section 11 as a decision/reference, without claiming runtime verification.

12. C6-IMPL-7
Restore/add the mentor row in the relevant profile/role table from the already approved PR-01 role model. Do not expand Moodle access beyond the approved mentor scope.

13. C6-IMPL-8
Correct the source/reference for the offline document/resource to the actual canonical source. No new content.

14. C6-NYELV-6
Use this learner-facing schedule-neutral wording:
`Offline alkalom: a központi naptár szerint.`
No SCHEDULE_TO_RESYNC marker in learner-facing text.

Human/DPO items that MUST remain open and MUST NOT be solved in this fix:
- C6-BIZT-1
- C6-BIZT-3
- C6-BIZT-4
- C6-IMPL-5
- C6-BIZT-8
- C6-NYELV-3

Also leave SAFE-7, A11Y-15/18, BSPEC-05/06/07 and M6.4 untouched.

Important status rule:
Until this objective post-fix succeeds, do not claim PR-01/PR-02 are substantively finished merely because the checker currently shows their build checklist rows closed.
```

## 1. Lépések

**Alkalmazási szabályok:**
- A lépéseket a táblázat sorrendjében kell alkalmazni.
- Minden lépés egy pontos szöveg cseréje vagy beszúrása. Ahol egy lépés két helyet érint, két `Edit` kell, az (a) és a (b) jelölés szerint.
- **Bizonyíték** = a fájlban **most** álló szöveg (a 2026-10-05-i Command 6 után, `grep -cF`-fel egyszer előforduló horgony). **Javítás** = a beírandó szöveg, szó szerint.

**Fájlrövidítések:**
- `ADV` = `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`
- `MAN` = `02 Tervezet/LMS – activity manifest.md`
- `RT` = `02 Tervezet/LMS – H5P runtime acceptance.md`
- `STD` = `02 Tervezet/LMS – hozzáférhetőségi sztenderd.md`
- `HUM` = `02 Tervezet/Emberi jóváhagyás szükséges.md`

| ID | Finding | Hely | Bizonyíték (most) | Javítás (szó szerint) | Kánoni alap |
|---|---|---|---|---|---|
| C6U-01 | C6-BIZT-2 / C6-NYELV-1 | ADV :241 | „Felesleges személyes adatot nem kérünk. Érzékeny személyes történetet (például családi, egészségügyi vagy gyermekvédelmi ügyet) egyik feladat sem kér kötelezően: írhatsz fiktív vagy általánosított példát is.” | „Felesleges személyes adatot nem kérünk, és ahol egy feladat személyes példát kér, írhatsz fiktív vagy általánosított példát is, ha nem maga a személyes adat a feladat tárgya. Politikai, vallási, egészségügyi vagy más különleges adatot és valós gyermekvédelmi esetet egyik tanulási feladatba se írj be: ilyen adatot normál tanulási feladatban nem gyűjtünk. Ha mégis megjelenik – például egy valós eset feltárásakor –, kikerül a Moodle-ből, és a külön, hozzáférés-korlátozott gyermekvédelmi incidensfolyamatba kerül.” | ADV §3 :75 („Politikai, vallási, egészségügyi vagy más különleges adat **normál tanulási activityben nem gyűjthető**. Ha feltáráskor mégis megjelenik, kikerül a Moodle-ből, és az incidensfolyamatba kerül”); §3 :82 („valós gyermekvédelmi eset soha nem pedagógiai feladat”); §5 :115 (külön, hozzáférés-korlátozott incidensnyilvántartás, HUM-SAFE-01); §2 :29 (fiktív vagy általánosított alternatíva, „ha a személyes adat nem a mérés tárgya”); HUM-PRIV-01 |
| C6U-02 | C6-NYELV-2 (a) | ADV :253 | „> - a mentorod fejlesztési jegyzetét (akkor is,” | „> - a mentorod fejlesztési és terepi megfigyelési jegyzetét (akkor is,” | ADV §3 :69 („Mentori fejlesztési jegyzet … a terepi megfigyelési jegyzet is”); §5 :113 („ide tartozik a terepi megfigyelési jegyzet is”) |
| C6U-03 | C6-NYELV-2 (b) + C6-BIZT-7 | ADV :260 | „Felvétel csak külön, önkéntes hozzájárulással készül – ha 18 év alatti vagy, a hozzájárulást te és a gondviselőd együtt adjátok meg –, és legfeljebb 90 napig őrizzük meg, hacsak külön nem járulsz hozzá a hosszabb megőrzéshez.” | „Felvétel csak külön, önkéntes hozzájárulással készül, és a cél teljesüléséig, legfeljebb 90 napig őrizzük meg, hacsak nincs külön hozzájárulás a hosszabb megőrzéshez. Mindkét hozzájárulást 18 év alatt te és a gondviselőd együtt adjátok meg, 18 év felett te magad.” | ADV §3 :72 („a cél teljesüléséig, legfeljebb 90 nap, hacsak nincs külön archiválási hozzájárulás”); §4 :103; §6 :133 („A hozzájárulást 18 év alatt a résztvevő és a gondviselő együtt adja, 18 év felett a résztvevő”); HUM-PRIV-02 |
| C6U-04 | C6-BIZT-5 / C6-NYELV-5 | ADV :245 | „A szöveges válaszaidat és a beadandóidat a kijelölt mentorod vagy értékelőd, és ő is csak akkor nézi meg, ha ténylegesen szükséges.” | „A szöveges válaszaidat és a beadandóidat a kijelölt mentorod vagy értékelőd látja. A beadandóidat és a Z.3 lecke kötelező szöveges válaszait a teljesítésed megerősítéséhez elolvassa; a többi szöveges válaszodat csak akkor nézi meg, ha ténylegesen szükséges.” | MAN §1 ASSIGN-S („a tartalmat a kijelölt mentor/értékelő erősíti meg”), ASSIGN-M (megerősített kapueredmény), LMS-Z-07 („Teljesítve” = a kijelölt mentor az LMS-Z-06 válaszait tartalmilag elfogadta, BS-D8); TEXT-C (BS-D4: „ha szükséges, a kijelölt mentor/értékelő végzi”); ADV §5 (P2: csak ha ténylegesen szükséges). Hozzáférés nem bővül. |
| C6U-05 | C6-BIZT-6 | ADV :254 | „a téma kategóriája” | „a cél kategóriája” | ADV §5 :114 („célkategória”); GK §4.2 |
| C6U-06 | C6-NYELV-4 | (a) ADV :256; (b) ADV :264 | (a) „> - a záró képzési visszajelzés (Z.4) válaszait: 90 napig, utána csak összesítve.”; (b) „> **Záró visszajelzés (Z.4).** A válaszok név nélkül jelennek meg a feldolgozásban.” | (a) „> - a „Képzési visszajelzés – név nélkül” kérdőív (Z.4) válaszait: 90 napig, utána csak összesítve.”; (b) „> **„Képzési visszajelzés – név nélkül” (Z.4).** A válaszok név nélkül jelennek meg a feldolgozásban.” | MAN :108 (LMS-Z-05 „Név”: „Képzési visszajelzés – név nélkül”); Z.4 :294, :365. A HUM-PRIV-03 kanonikus mondata („A válaszok név nélkül jelennek meg a feldolgozásban.”) szó szerint marad. |
| C6U-07 | C6-IMPL-7 | ADV :104 (szerepkörtábla, a nem szerkesztő tanár sora) | „\| a TEXT-C-ben csak a saját mentor-csoportja válaszait (lent) \|” | „\| a TEXT-C-ben csak a saját mentor-csoportja válaszait (lent); az ASSIGN-S/M és a P2-es H5P-C adatait a Moodle-alapértelmezés szerint csoporttól függetlenül (lent, profiltábla; a szűkítés DPO-kérdés: BIZT-5) \|” | ugyanennek a szakasznak a profiltáblája (:115, :117: „nem szerkesztő tanár … \| nincs rögzítve (BIZT-5)”); PR-01 szerepkör-modell (D-a…D-d 2. pont). Tényállítás a meglévő alapértelmezésről; hozzáférést nem bővít, és a BIZT-5-öt nem dönti el. |
| C6U-08 | C6-IMPL-2 | RT :80 (15. pont), a „… a beküldési értesítés kikapcsolva (BIZT-11).” mondat után | „a beküldési értesítés kikapcsolva (BIZT-11).” | a mondat után: „ A mentor-láthatósági mechanizmust legalább két mentorral és két elkülönített tanulói csoporttal kell igazolni: az A mentor csak az A csoport válaszait látja; a B mentor csak a B csoport válaszait látja; egyik mentor sem jut közvetlen URL-lel más csoport tanulójának válaszához; a tanuló nem látja más tanuló válaszát (projektgazdai döntés, 2026-10-05: `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`, 1. szakasz 2. pont).” | D-a…D-d 1. szakasz 2. pont: „legalább két mentorral és két elkülönített learner-csoporttal: Mentor A csak A-csoport válaszait látja / Mentor B csak B-csoport válaszait látja / egyik mentor sem tud közvetlen URL-lel más csoport learner response-ára jutni / learner nem lát más learner válaszát”. A szemantika változatlan; a futtatás bizonyíték-kapu marad (BIZT-9, G2). |
| C6U-09 | C6-IMPL-1 | (a) STD :92; (b) STD :100 | (a) „A beágyazott oldal dokumentumcímét viszont a `h5p/embed.php` a H5P-tartalom címéből állítja be (`$h5pplayer->get_title()`).*”; (b) „és beállítja vele a külső iframe `title`-jét.” | (a) „A beágyazott oldal dokumentumcímét viszont a `h5p/embed.php` a H5P-tartalom címéből állítja be (`$h5pplayer->get_title()`); a `moodle_page::set_title()` ehhez alapértelmezésben az oldal nevét is hozzáfűzi (Moodle 4.5, `lib/pagelib.php`), ezért a dokumentumcím nem azonos a H5P-címmel.*”; (b) „és beállítja vele a külső iframe `title`-jét. Mivel a dokumentumcím az oldal nevét is tartalmazhatja, a karbantartott megoldás normalizálhatja: eltávolíthatja a Moodle által hozzáfűzött oldalnév-utótagot. A pontos elválasztót és normalizálást a célkörnyezetben kell igazolni; egyetlen elválasztó mentén vágva nem garantált a helyes cím. A normatív eredmény változatlan: az iframe `title`-je a kanonikus H5P-/activity-cím.” | Moodle `MOODLE_405_STABLE` `lib/pagelib.php`: `public function set_title($title, bool $appendsitename = true)` és `TITLE_SEPARATOR = ' \| '` (a csomag összeállításakor ellenőrizve); `h5p/embed.php` :63. Megvalósítási útmutatás, nem új hozzáférhetőségi szabály. |
| C6U-10 | C6-IMPL-3 | (a) RT :26; (b) RT :108 | (a) „\| A H5P-iframe-cím megvalósítása (A11Y-07):”; (b) „`LMS – hozzáférhetőségi sztenderd.md`, A11Y-07);” | (a) „\| A H5P-iframe-cím megvalósítása (a hozzáférhetőségi sztenderd „Magyar nyelv + iframe-title” tétele, leltár-azonosító: A11Y-07; nem azonos az RT-A11Y-07 teszttel):”; (b) „`LMS – hozzáférhetőségi sztenderd.md`, „Magyar nyelv + iframe-title” tétel, leltár-azonosító: A11Y-07; nem azonos az RT-A11Y-07 teszttel);” | A meglévő azonosítók: A11Y-07 = a build-blocker leltár és a HUM :553 (D-a) checklist-azonosítója; RT-A11Y-07 = az RT „Teszt-állapot” táblájának sora („a narráció és a videó leirata …”). Az (a) sor az environment record `RUNTIME_OUTPUT` sora marad, az első cellában nincs `\|`. |
| C6U-11 | C6-IMPL-4 | MAN :121 | „Moodle File erőforrás a lecke activityje mellett, ugyanabban a szakaszban, saját completion nélkül.” | „Moodle File erőforrás a lecke activityje mellett, ugyanabban a szakaszban, saját completion nélkül, ugyanazzal a hozzáférési feltétellel (Restrict access), mint a lecke activityje: a §2 sor „Unlock / előfeltétel” oszlopa és a §7 ütemezése szerint, így a lecke nyitása előtt nem érhető el.” | MAN §2 fejléce (:37: „Unlock / előfeltétel”); §7; PILOT-2 (dátumot nem találunk ki). Az előfeltételek nem gyengülnek. |
| C6U-12 | C6-IMPL-8 | MAN :122 | „szövegalapú, képernyőolvasóval olvasható dokumentum.” | „szövegalapú, képernyőolvasóval olvasható dokumentum. Forrása a lecke kánoni forrásfájlja (`02 Tervezet/Modulok/<modul>/Online leckék/`) és a média-manifestben (`02 Tervezet/Média-assetek/_build/media-manifest.v2.json`) a lecke narrációs és videós assetjeinek leirata (`::TRANSCRIPT`), valamint a kulcsképek alt-szövege (`::ALTTEXT`). Ahol egy assetnek nincs leirat-deliverable-je, ott a lecke forrásszövege a forrás. Új tartalom nem készül hozzá.” | A média-manifest: a 27 videós assetből 23-nak van `transcript` derivatívája (hiányzik: M1.1-VID-02, M4.1-VID-03, -04, -05), 131 `::ALTTEXT` deliverable van; a csomag összeállításakor ellenőrizve. |
| C6U-13 | C6-IMPL-6 | (a) HUM 11. szakasz, a táblázat utolsó sora után; (b) STD :88 | (a) a sor vége: „csak a sikerhez kötött downstream/kapus elemek maradnak zárva. \| pilot-ütemezés, 5. szakasz 5. pont \| — \|”; (b) „(A11Y-07; projektgazdai döntés, 2026-10-05)” | (a) új sor az **A.1** pont szó szerinti szövegével; (b) „(A11Y-07; projektgazdai döntés, 2026-10-05: `Emberi jóváhagyás szükséges.md` 11. szakasz)” | A Command 6 fix pack 0. szakasza (a projektgazda második és harmadik üzenete, szó szerint). Runtime-bizonyítékot nem állít. |
| C6U-14 | C6-NYELV-6 | (a) `02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md` :12; (b) `02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md` :6 | (a) „* **Offline alkalom:** a központi naptár szerint – **Peula A (M0.A, 45–60’)**”; (b) „* **Offline alkalmak:** a központi naptár szerint – M1.A (1. hét)” | (a) „* **Offline alkalom:** a központi naptár szerint. **Peula A (M0.A, 45–60’)**”; (b) „* **Offline alkalom:** a központi naptár szerint. M1.A (1. hét)” | A projektgazda előírt mondata: „Offline alkalom: a központi naptár szerint.”; jelölő nem kerül be (PILOT-2) |

### A.1 — a C6U-13 (a) új HUM-sora (szó szerint)

```markdown
| Az A11Y-07 iframe-címe (G5a/G5b) | Az A11Y-07 a G5a/G5b modell szerint kettéválik. G5a (build, repó- és spec-szint): minden tanulói Moodle H5P-iframe-nek beszédes magyar `title` attribútuma van, amelynek értéke a kanonikus H5P-/activity-cím; Moodle core fájl nem módosul; a megvalósítás karbantartott, theme-szintű JS/AMD-kiegészítés, renderer- vagy kontextusbővítés, illetve egyenértékű, karbantartott local/plugin megoldás lehet; Mustache-felülírás csak akkor elfogadható, ha a megvalósítás a címet a sablon kontextusába is átadja; a pontos megvalósítást a cél-Moodle-környezetben kell igazolni; ha egyik mechanizmus sem telepíthető, TARGET-ENVIRONMENT blokkolót kell rögzíteni, és a követelmény nem gyengül. A követelmény rögzítésével a G5a repó- és spec-része lezárható. G5b (post-build): a renderelt DOM-nak és a képernyőolvasó bejelentésének kell igazolnia; ez nem jelölhető `RUNTIME_VERIFIED`-nek, amíg nem fut. Ez nem felmentés a hozzáférhetőségi követelmény alól, és nem állítja, hogy a core Moodle teljesíti. | `01 Fejlesztés/04 Audit/2026-10-05 Fix pack – Command 6 – PR-01, PR-02, A11Y-07, A11Y-17 és konzisztencia.md`, 0. szakasz (második és harmadik üzenet) | — (a döntés nem nevez meg utólagos ellenőrzőt) |
```

## 2. A futás után

- **Látható szöveg** változik (ADV §11, M0/M1 hub): egyetlen pin.
- **Média:** `@asset` és `@source` nem változik. A `media_manifest.py validate`, `check` és `reconcile` csak ellenőrzésként fut; build nem kell, hacsak a `check` elcsúszást nem mutat.
- **Ellenőrzések:**
  - `content_integrity.py` (0 hiba) és `--selftest`;
  - `python3 -m unittest tools.test_media_manifest`;
  - `git diff --check`, a teljes PR-tartományra is;
  - `--release-report`.
- **Célzott újraellenőrzés** csak a módosított sorokra:
  - nyelvi lencse: ADV §11 és a hubok;
  - biztonság-jog lencse: ADV :241, :245, :260;
  - implementációs lencse: RT, MAN, STD és a HUM-sor.

## 3. Várt gépi állapot

Checklist-tétel és BSPEC-sor nem változik, így:
- a `MOODLE-BUILD-VERDICT` **`NOT_READY` marad, kizárólag a `MANIFEST-OPEN 3` (BSPEC-05, -06, -07) miatt**;
- a `LEARNER-RELEASE-VERDICT` `NO-GO` marad;
- a C6-BIZT-1/3/4/8, a C6-IMPL-5 és a C6-NYELV-3 nyitva marad.

## 4. Futás (`/course-fix`, 2026-10-05)

**Lépések:** a C6U-01…C6U-14 mindegyike alkalmazva, 19 `Edit`-tel. Minden horgony a futás előtt pontosan egyszer szerepelt (`grep -cF`). A javítások szövege a futás után egyszer megvan a fájlokban. Az RT „nem azonos az RT-A11Y-07 teszttel” szövege a két célhely miatt kétszer szerepel.

**Pin:** egyetlen pin, 7 fájl.

**Ellenőrzések:**
- média: `validate` és `check` OK, a `reconcile` szerint 0 sor nincs egyeztetve; build nem kellett, mert az `@asset` és a `@source` nem változott;
- `py_compile` OK; selftest 57/57; `content_integrity` 0 hiba; 159 teszt OK;
- `git diff --check` tiszta, a PR-tartományra is.

**Release report:**
- `MOODLE-BUILD-VERDICT: NOT_READY`, csak a `MANIFEST-OPEN 3` (BSPEC-05/06/07) miatt;
- `LEARNER-RELEASE-VERDICT: NO-GO`;
- a számlálók változatlanok: post-build 14, release-evidence 8, environment record 18.

**Commit és push:** nincs.

### Célzott újraellenőrzés (csak a módosított sorokon; a talált hibák nincsenek javítva, a riportba mennek)

| ID | Súly | Hely | Típus | Lényeg |
|---|---|---|---|---|
| C6U-BIZT-1 | P1 | ADV :241 | objektív; a feltáráson kívüli eset kezelése emberi döntés (DPO) | A C6U-01 szövege a kánoni feltételt („feltáráskor”, §3 :75; §5 :153) példává tette („például egy valós eset feltárásakor”), így minden különleges adat az incidensfolyamatba kerülne. Ez a saját fogalmazási hibám. Javítás: „Ha egy feltárásban mégis megjelenik ilyen adat, kikerül a Moodle-ből, és a külön, hozzáférés-korlátozott gyermekvédelmi incidensfolyamatba kerül.” |
| C6U-BIZT-2 | P2 | ADV :241 | objektív | Kiesett a §2 :29 garanciája, hogy érzékeny családi vagy identitással kapcsolatos történet nem lehet kötelező. Vissza kell tenni, csak erre a körre. |
| C6U-BIZT-3 | P2 | ADV :241 | emberi döntés (Memuna, DPO-QA) | Kerüljön-e a tájékoztatóba utalás a GK §4.1 jelzési útjára? |
| C6U-BIZT-4 | P2 | ADV :245 | objektív | „A kvízek és a kapuk eredményét az értékelőd **látja**.” (§5) |
| C6U-IMPL-1 | P2 | STD :92, :100 | objektív | A `set_title()` a portál (site) nevét fűzi hozzá, nem az „oldal” nevét. A :92 „nem azonos” helyett: „eltérhet”. |
| C6U-IMPL-2 | P2 | RT :80 | megjegyzés, projektgazdai kérdés | A négy feltételt a sor „projektgazdai döntés”-ként hivatkozza. A D-a…D-d jegyzőkönyv 2. szakasza a kutatási eredményt validálási bemenetnek nevezi, a validált findingok 5. pontja „projektgazdai feltételes elfogadás”-nak; a HUM 11. szakaszba nincs átvezetve. |

**Rendben van:**
- a :104, :253, :254, :256, :260 és :264 sor a kánonból következik;
- a Z.4 kanonikus mondata változatlan;
- a négy RT-feltétel jelentésben egyezik a jegyzőkönyvvel;
- a kereszthivatkozások feloldódnak;
- a :26-os environment-sor továbbra is `RUNTIME_OUTPUT`-sorként értelmeződik;
- a :100 útmutatás nem rögzít elválasztót.
