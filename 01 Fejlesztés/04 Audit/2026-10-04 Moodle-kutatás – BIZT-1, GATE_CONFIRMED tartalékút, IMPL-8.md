# Moodle-kutatás — BIZT-1, GATE_CONFIRMED tartalékút, IMPL-8 (2026-10-04)

> **Audit trail, nem kánon.** Read-only kutatás a BSPEC-01 és a BSPEC-02 maradék hatóköréhez, a projektgazda
> utasítására (`2026-10-04 Projektgazdai döntések – BSPEC-01…04 maradék.md`, BS-D1, BS-D4 és a governance-korrekció).
> Tananyag, manifest és runtime acceptance ebben a lépésben nem változott.

| Mező | Érték |
|---|---|
| exact target Moodle version | `UNKNOWN / TARGET-ENVIRONMENT EVIDENCE REQUIRED` (G3-bizonyíték a célkörnyezetből) |
| research compatibility range | Moodle 4.5–5.2 (`MOODLE_405_STABLE`, `MOODLE_500_STABLE`, `MOODLE_501_STABLE`, `MOODLE_502_STABLE`; a 5.2 ág létezik, `version.php`: „5.2.4”) |
| forrás | kizárólag elsődleges: `docs.moodle.org`, `raw.githubusercontent.com/moodle/moodle/<ág>/…` (5.1-től a kód a `public/` alatt), a `moodle/moodle` commitjai, a Moodle Jira (MDL-…) |
| módszer | három read-only kutató subagent (A1: Assignment online text és editor-utak; A2+C: alternatív core activityk és a kikényszeríthető minimum; B: checkpoint és tartalékút); fájlt nem írtak, gitet nem futtattak |
| korlát | az idézetek a WebFetch kivonatolóján át jöttek: kánonba emelés előtt szúrópróbával ellenőrizendők; élő Moodle-on semmi nem futott — minden futásidejű viselkedés kódból vagy dokumentációból következtetett, runtime-teszttel igazolandó |

Rövidítés: B405 = `raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/`, B500 = `…/MOODLE_500_STABLE/`,
B501 = `…/MOODLE_501_STABLE/public/`, B502 = `…/MOODLE_502_STABLE/public/`.

## A. BIZT-1 — privát szöveges válasz fájl-, kép-, média- és embed-út nélkül

### A.1 Megállapítások

| # | Megállapítás | Forrás (idézet) | Verziók | Confidence |
|---|---|---|---|---|
| A1 | Az Assignment online text szerkesztője minden verzióban korlátlan fájlt fogad, és nincs assignment-szintű beállítás, amely ezt korlátozná (csak a szólimit). | `mod/assign/submission/onlinetext/locallib.php`: `'maxfiles' => EDITOR_UNLIMITED_FILES,` `'context' => $this->assignment->get_context(),` | 4.5, 5.0, 5.1, 5.2 | magas |
| A2 | A TinyMCE minden kép- és médiaútja (beillesztés, húzás, képválasztó, média-dialógus, felvétel) ugyanazon a feltöltőn megy, amely a `ctx_id`-t a kliensből küldi; a szerver a repository `:view` capabilityt abban a kontextusban ellenőrzi, amelyet a kliens küld. | `lib/editor/tiny/amd/src/uploader.js`: `formData.append('ctx_id', options.context.id);`; `repository/repository_ajax.php`: `$contextid = optional_param('ctx_id', SYSCONTEXTID, PARAM_INT);` → `$repo->check_capability();` | 4.5–5.2 | magas |
| A3 | Activity-szintű **Prohibit** a Student szerepre (vagy az Authenticated user felülírása az activityben) minden engedélyezett `repository/*:view`, a felvétel (`tiny/recordrtc:record*` 4.5-ben, `tiny/recordrtc:use` 5.0-tól) és 5.0-tól a `tiny/media:use` és `tiny/link:use` capabilityre a normál felhasználói utakat elzárja. A **Prevent** nem elég, mert a jog az Authenticated user szerepből jön. | `docs.moodle.org/405/en/Override_permissions`: „PROHIBIT which can not be overridden”; B500 `tiny/classes/plugin.php`: `$capability = "tiny/$plugin:use";` | 4.5–5.2 | közepes (a picker repository-listájának kontextusa NOT VERIFIED) |
| A4 | Kézzel összeállított feltöltési kéréssel (a tanuló saját user-kontextusával, ahol az Authenticated user `repository/upload:view` joga megvan) fájl mégis bekerülhet a beadásba, mert mentéskor a `file_postupdate_standard_editor` korlátlan fájllal fut. Lezárása kódmódosítást vagy site-wide változtatást igényelne — egyik sem elfogadható. | A2 és A1 együtt (kódból következtetve) | 4.5–5.2 | közepes |
| A5 | Az editor felhasználói preferencia (`htmleditor`); activity-szinten nem kényszeríthető. Az Atto 5.0-ban kikerült a core-ból. | `get_user_preferences('htmleditor', '', $USER)`; MDL-83282 „Remove Atto text editor” | 4.5 (Atto van), 5.0–5.2 (nincs) | magas |
| A6 | AI-képgenerálás (4.5-től) csak site-wide engedélyezett AI-szolgáltatónál és editor-placementnél; a kép Moodle-fájlként (draft) tárolódik; a capability kurzusszintű. | `aiplacement/editor:generate_image` (`CONTEXT_COURSE`); OpenAI provider: `$fileinfo->filearea = 'draft';` | 4.5; 5.x NOT VERIFIED | közepes |
| A7 | **Quiz + Essay, „plain” formátum, attachments = 0:** a tanuló felülete egy puszta `textarea`, editor és fájlmező nélkül. | `question/type/essay/renderer.php`: `html_writer::tag('textarea', s($response), $attributes)`; fájlinput csak `if ($question->attachments)` | 4.5, 5.0, 5.1, 5.2 | magas |
| A8 | **Feedback „Longer text answer”:** puszta `textarea`, editor és fájlmező nélkül; a „Short text answer” egysoros input (`PARAM_NOTAGS`, max. hossz). | mod_feedback textarea item: `['textarea', $inputname, $name, array('rows' => $rows, 'cols' => $cols)]` | 4.5, 5.0, 5.1, 5.2 | magas |
| A9 | Database „Textarea” mező és Lesson essay oldal: **nem** fájlmentes (editor korlátlan fájllal). | `mod/data/field/textarea/field.class.php`: `$options['maxfiles'] = -1;`; Lesson essay: `'maxfiles' => EDITOR_UNLIMITED_FILES` | 4.5–5.2 | magas |
| A10 | Feedback-láthatóság: a „Show analysis page” bekapcsolásakor a tanulók név nélkül látják egymás szöveges válaszait; az alapértelmezés `anonymous = 1`, `publish_stats = 0`; a `mod/feedback:viewreports` alapból teacher, editingteacher, manager; a `viewanalysepage` a studentnek is jár. | `can_view_analysis` (4.5, 5.2); `install.xml` alapértékek | 4.5, 5.2 (5.0/5.1 nem külön) | magas |
| A11 | Feedback megőrzés/törlés: privacy provider (mindhárom delete metódus), kurzus-reset (`feedback_delete_all_completeds`); a core retention a kurzus végétől számol. | 4.5 privacy provider; `docs.moodle.org/502/en/Data_privacy`: „the retention period is measured from the course end date” | 4.5 (provider), 5.2 (docs) | magas |
| A12 | Quiz megőrzés/törlés: `quiz_attempts` + question engine; privacy provider és `reset_quiz_attempts`. Az Essay a próbálkozást „Requires grading” állapotban hagyja. | 4.5 `mod/quiz/classes/privacy/provider.php`; `qbehaviour_manualgraded::process_finish` | 4.5, 5.2 | magas |

### A.2 Következtetés

- **Az Assignment online text (a jelenlegi TEXT-C) a BIZT-1 követelményét nem teljesíti** egyik verzióban sem:
  activity-szinten csak a normál felhasználói utak zárhatók el, a kézzel összeállított kérés nem (A1–A4). Confidence:
  közepes–magas.
- **Fájlmentes core alternatíva létezik:** Feedback „Longer text answer” (A8) és Quiz Essay „plain” + attachments = 0
  (A7), mindkettő 4.5–5.2 között. Confidence: magas a fájlmentességre.
- **Private-by-default a Feedbacknél beállítással érhető el:** nem anonim rögzítés, „Show analysis page” ki,
  `mod/feedback:viewanalysepage` Prohibit a tanulóra az activityben; a `viewreports` alapból a tanári szerepeké, ezért a
  HUM-PRIV-01 szerinti szűkítés ugyanúgy beállítandó és stagingben visszaolvasandó, mint minden más P2 activitynél.

## B. BSPEC-01 — a `GATE_CONFIRMED_<module>` checkpoint és a tartalékút

### B.1 Megállapítások

| # | Megállapítás | Forrás (idézet) | Verziók | Confidence |
|---|---|---|---|---|
| B1 | A Grade-feltétel pontszáma: `((finalgrade - rawgrademin) * 100) / (rawgrademax - rawgrademin)`; a `grade_grades.finalgrade`-et olvassa, a rejtettséget nem nézi. | B405 `availability/condition/grade/classes/condition.php`: `$allow = $score !== false && (is_null($this->min) || $score >= $this->min) && (is_null($this->max) || $score < $this->max);` | 4.5–5.2 | magas |
| B2 | Skálánál `grademin = 1`, `grademax` = a skála elemszáma; a kételemű skálán „Még nem teljesítve” = 0 %, „Teljesítve” = 100 %. | B405 `lib/grade/grade_item.php`: `$this->grademax = count($this->scale->scale_items); $this->grademin = 1;` | 4.5 (a többi közepes) | magas (4.5) |
| B3 | Skálás activitynél a Grade to pass a skálaelem sorszáma: itt **2**. | `course/moodleform_mod.php`: `$grade = count(explode(',', $scalevalues->scale)); if (unformat_float(gradepass) > $grade)` | 4.5, 5.2 | magas |
| B4 | Pass/fail állapot csak `gradepass > 0.000009 && ($returnpassfail \|\| !$item->hidden)` mellett; különben a jegy csak `COMPLETION_COMPLETE`. Staff-override csak COMPLETE/INCOMPLETE lehet, és a COMPLETE-re állított automatikus állapotot befagyasztja. | `lib/completionlib.php` (`internal_get_grade_state`, `update_state`) | 4.5, 5.0, 5.1, 5.2 | magas |
| B5 | „must be complete” = COMPLETE vagy COMPLETE_PASS; pass/fail pontos egyezést kér. | `availability/condition/completion/classes/condition.php` | 4.5, 5.2 | magas |
| B6 | Marking workflow mellett a jegy a „Released” állapotig nem kerül a gradebookba; anonim beadásnál sem (MDL-83195, javítva 4.4.9, 4.5.5, 5.0.1). | `docs.moodle.org/405/en/Assignment_settings`; commit 5047b0e (MDL-49075), bec8c1a (MDL-83195) | 4.5–5.2; a 4.5–5.2 `locallib.php` kódszinten NOT VERIFIED | közepes |
| B7 | Tartalék-opciók: (F1) manuális gradebook-tétel + Grade-feltétel — privacy-safe, core, de ugyanarra a gradebook/Grade-feltétel gépezetre épül, és `moodle/grade:edit` kell hozzá (a non-editing teacher alapból nem kapja); (F2) két kézi completionös activity staff-override-dal — a tanuló „Mark as done” gombja megmarad (a capability-ellenőrzés csak szerveroldali), az override kurzusszintű; (F3) egyedi profilmező — site-szintű, a feltétel a munkamenetben gyorsítótárazott értéket olvassa, **nem determinisztikus**; csoport/grouping — BS-D1 szerint elvetve. | `grade_item::fetch_all(['courseid'=>…])`; `lib/db/access.php` (`moodle/course:togglecompletion`); `report/progress/index.php`; `user/profile/lib.php` (`$USER->profile`) | 4.5–5.2 | közepes–magas |
| B8 | A core availability-feltételek köre 4.5-ben és 5.2-ben is: completion, date, grade, group, grouping, profile. | B405 és B502 `availability/condition/` | 4.5, 5.2 | magas |

### B.2 Következtetés

- **A primary út (Assignment beadás nélkül, kételemű skála, Grade to pass = 2) 4.5–5.2 között támogatott és
  determinisztikus**, ha a beállítások rögzítettek. Confidence: magas a kódutakra, közepes a marking workflow
  mechanizmusára (B6).
- **Determinisztikusabb feltétel-kódolás:** a „Teljesítve”-hez kötött nyitás (Mx complete) is Grade-feltétellel
  (≥ 50 % ugyanazon a grade itemen) írható; ez kiveszi a rejtettség, a completion-beállítás és a staff-override
  befagyasztás hatását az availability-ből (B1, B2, B4). Az „Mx megerősítve” marad: Grade-feltétel határ nélkül.
- **Tartalékút: nincs független, privacy-safe opció.** Az F1 ugyanazon a gépezeten fut, mint a primary (nem fedi le
  annak hibamódjait), az F2 nem determinisztikus felületű, az F3 nem determinisztikus, a csoport elvetve. A primary
  minden ismert hibamódja beállításból ered, amely rögzíthető és runtime-teszttel igazolható. Ezért a spec
  „nincs tartalékút” eredménye a BS-D1 feltételei szerint bizonyított: core, determinisztikusan buildelhető, 4.5–5.2
  között támogatott, runtime-teszttel igazolható.
- **Rögzítendő beállítások:** (1) skála pontosan két elemmel, ebben a sorrendben: „Még nem teljesítve”, „Teljesítve”,
  értékelés előtt létrehozva; (2) Grade to pass = 2; (3) a grade item nem rejtett, „hidden until” nélkül; (4) nem
  zárolt; (5) marking workflow ki, anonim beadás ki, további próbálkozás nincs; (6) completion: automatikus, „Receive a
  grade”; (7) staff completion-override a checkpointon tilos (kurzusszintű capability, ezért működési szabály +
  runtime-teszt; különben egy COMPLETE-re állított bukott tanuló a kurzus-completionben teljesítettnek számíthat — B4 és
  az IMPL-reviewer megfigyelése a course completion `completion_criteria_activity`-ről); (8) az értéket a
  stáb az assignment értékelő felületén írja be, nem gradebook-felülírással.
- **Runtime-teszt (RA 8-hoz):** két tanulói fiók; mindkét érték beállítása sorban; mindkét tanuló csak a saját
  állapotát látja; az „Mx megerősítve” és az „Mx complete” feltétel helyesen vált; üres érték mellett semmi nem nyílik.

## C. IMPL-8 — „minimálisan értelmezhető tartalom”

| Jelölt | Technikailag kikényszeríthető | Csak formai minimum | Emberi / szemantikai ellenőrzés kell |
|---|---|---|---|
| Feedback „Longer text answer”, kötelező | üres beadás nem lehetséges (a `required` szabály szerveroldalon is fut: `lib/pear/HTML/QuickForm.php` `validate()`) | csak szóközből álló válasz valószínűleg átmegy, hacsak a site-wide „csak szóköz tiltása” beállítás nincs bekapcsolva (`docs.moodle.org/405/en/Site_security_settings`; kódszinten NOT VERIFIED); szó- vagy karakterminimum nincs | az értelmezhetőség |
| Feedback „Short text answer”, kötelező | üres nem lehet; maximum hossz | minimum hossz nincs | az értelmezhetőség |
| Quiz Essay „plain”, Require text + minimum szószám | **semmi**: üres vagy rövid válasz mellett is lezárul a próbálkozás, és a „Minimum attempts” completion teljesül (`check_input_word_count` csak figyelmeztet; `process_finish` állapotot zár) | a szószám-figyelmeztetés | minden; a próbálkozás „Requires grading” |
| Assignment online text | üres beadás (a BIZT-1 miatt nem jelölt) | szólimit csak maximum | — |

- **Következmény a BS-D4 szerint:** egyik fájlmentes core út sem bizonyítja a „minimálisan értelmezhető tartalmat”;
  a spec csak a „nem üres” (Feedback: kötelező) kikényszerítést állíthatja, a szemantikai minimumhoz emberi
  ellenőrzést kell jelölni.
- **Z.3 biztonsági lépés:** strukturálisan két külön kötelező mező írható elő (1. ki a Memuna, vagy kit kérdez meg róla;
  2. kinek jelez). Ez a nem-ürességet biztosítja, a helyességet nem. **Nyitott emberi döntés:** a lépés completionje
  várjon-e a kijelölt mentor megerősítésére (Quiz Essay + értékelés, vagy GATE-CP-szerű stáb-megerősítés), vagy a
  kitöltés + utólagos mentori ellenőrzés elég. Ez gyermekvédelmi eljárási szabály, ezért a projektgazdáé, a Memuna
  vétójával — a build spec nem dönti el.

## D. Következmény a BSPEC-01 és a BSPEC-02 szempontjából

**BSPEC-01 (javaslat a következő `/course-fix`-hez):**

1. a §4 tartalékút-bekezdése helyett: „tartalékút nincs” + a B.2 indoklása (forrás: ez a jegyzet);
2. az „Mx complete” kódolása: Grade-feltétel ≥ 50 % a checkpoint grade itemjén (az Activity completion „pass grade”
   helyett);
3. a GATE-CP profilba a B.2 nyolc rögzített beállítása (Grade to pass = 2 számértékkel; marking workflow ki — ez az
   IMPL-11 is);
4. LMS-M7-08: a BS-D3 átvezetése (bukott M7-kapunál „Még nem teljesítve”; nem pass, nem M7-completion; a kurzus- és
   programteljesítés blokkolva);
5. az RA 8. pontba a B.2 runtime-tesztje (IMPL-2).

**BSPEC-02 (javaslat a következő `/course-fix`-hez):**

1. a TEXT-C profil cseréje fájlmentes core útra: **Feedback „Longer text answer”** (kötelező tétel; nem anonim
   rögzítés; „Show analysis page” ki; `mod/feedback:viewanalysepage` Prohibit a tanulóra az activityben; completion:
   beküldés). Indok: fájlmentes (A8), a kötelezőség szerveroldali (C), nem hagy „Requires grading” állapotot (A12);
2. a Quiz Essay „plain” csak akkor alternatíva, ha az emberi ellenőrzés amúgy is kötelező (pl. a Z.3 lépésnél, ha az
   emberi döntés így szól);
3. az activity leírásába a lecke mező melletti adatvédelmi/biztonsági megjegyzése szó szerint (BIZT-3);
4. a kötelező mezők teljes leltára (M2.1, M2.3, M3.1, M3.2, M4.1, M4.2, M4.3, M4.4, Z.3) a `/course-review` futások
   után;
5. a „minimálisan értelmezhető tartalom” csak „nem üres”-ként állítható; a szemantikai ellenőrzés jelölése (BS-D4);
6. a Z.3 biztonsági lépés completion-kötése: nyitott emberi döntés (C);
7. a megőrzés: a reflexióknál az Adatvédelem §3 „Szabad szöveges reflexió” sora; az LMS-Z-06-nál DPO-döntés (BS-D6).

**Nyitott, nem a buildet meghatározó, de runtime-teszttel igazolandó:** A3 (a picker repository-listájának kontextusa),
A6 (AI-kép 5.x-ben), B6 (marking workflow kódszinten), a szóközös kötelező válasz (C).
