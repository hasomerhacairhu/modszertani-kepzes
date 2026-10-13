# Célzott QA – a D-csomagok átvezetése (8bb4d7d), AP-2026-10-13-01

> **Audit trail, nem kánon.** A `/course-fix` 4. lépése: diffre szabott újraellenőrzés a `3dfc451..8bb4d7d` tartalmi diffre
> (HUM 15 és a projektgazdai hatáskörű D-tételek átvezetése, 24 fájl). Nem teljes audit: csak a módosított sorokra.

- **Lencsék:** biztonság-jog (`QA17-BIZT`), implementáció (`QA17-IMPL`), értékelés (`QA17-ERT`), nyelv (`QA17-NYELV`). A pedagógiai
  lencse a beépítés előtt futott (a D-20 vágási terv reviewereinek PED-5, PED-6 megfigyelése és az M1.F kapacitásmondat); ezek a fő session
  ellenőrzése után `QA17-PED-1…3` kulccsal kerültek be a `8bb4d7d`-be.
- **Verifikáció:** a biztonsági, implementációs és értékelési findingokat két adverzális verifier vizsgálta (A köteg: Moodle/H5P-forrással,
  MOODLE_405_STABLE és h5p GitHub; B köteg: repóból). A nyelvi findingokat a fő session a fájlban ellenőrizte.
- **Javító commit:** `9788c05` (13 fájl, látható szöveg újrapinnelve). Kulcs, küszöb, rubrikaszint, időtartam nem változott.
- **Ellenőrzés a javítás után:** `content_integrity.py` 0 ERROR; `tools.test_media_manifest` 159 teszt OK; `media_manifest.py check` és `reconcile` rendben; `git diff --check` tiszta.

## I. Tételes eredmény

| Kulcs | Súly | Típus | Állapot | Bizonyíték / döntési igény |
|---|---|---|---|---|
| M3:QA17-PED-1 | P2 | objektív | FIXED | PRG-1: az M3.A zárókörét a D-03 nem rövidíti — 8bb4d7d M3.A:566; fő session ellenőrizte (D-20 vágási terv, a pedagógiai QA javaslata) |
| M2:QA17-PED-2 | P2 | objektív | FIXED | GYV-20: az M2.A:254 a reflexiót nem érzékeny állításra korlátozza, a „körbenézzenek” kikerült — 8bb4d7d M2.A:254; célzott biztonsági QA rendben |
| M1:QA17-PED-3 | P2 | objektív | FIXED | PRG-5: az M1.F kapacitásmondata a többi F-peulával egyezően — 8bb4d7d M1.F:66; fő session ellenőrizte |
| KANON:QA17-IMPL-2 | P1 | objektív | FIXED | D-11 / GYV-23: az LMS-M0-06 override a `mod/quiz:grade`-et is elvonja (a Manual grading riport ezzel nyílik, MOODLE_405_STABLE) — 9788c05 Adatvédelem :140, manifest :31, :46, RA 15 negatív teszt (Manual grading, közvetlen URL); verifier A MEGERŐSÍTVE |
| KANON:QA17-BIZT-1 | P1 | objektív | DUPLICATE | = KANON:QA17-IMPL-2 (verifier A) |
| KANON:QA17-BIZT-2 | P1 | objektív | FIXED | D-11: a kurzus „Separate groups” az új activityk alapértéke (`course/modlib.php`); a FORUM-C „Group mode” = „No groups” rögzítve — 9788c05 manifest FORUM-C (:21), Adatvédelem :141, RA 27; verifier A RÉSZBEN (a FEEDBACK-N rész: KANON:QA17-BIZT-2b) |
| KANON:QA17-BIZT-2b | P1 | emberi-döntés | BLOCKED_HUMAN | EMBERI DÖNTÉS: a FEEDBACK-N (Z.4) csoportmódja, a mentor Z.4-hozzáférésével együtt (Adatvédelem §3, BIZT-6) — DPO / jogi felelős; jelölve: 9788c05 manifest FEEDBACK-N „nyitott”; DPO-csomag |
| KANON:QA17-IMPL-3 | P2 | objektív | DUPLICATE | = KANON:QA17-BIZT-2 (verifier A) |
| M3:QA17-IMPL-1 | P1 | emberi-döntés | BLOCKED_HUMAN | EMBERI DÖNTÉS: a D-08 (b) megjelenítési módja — a h5p-branching-scenario forrása (master, `libraryScreen.js`) szerint a `showContentTitle` Branching Question-csomópontnál nem frissíti a fejlécet; a build-spec gazda (projektgazda) válasszon működő módot (pl. a szitu meglévő címe a megelőző csomóponton, vagy külön címcsomópont), Memuna-QA-val; a §7.1 kérdés és a két opció nem változik; addig az RA 11 tesztje várhatóan bukik (BSPEC-05 újranyílik); verifier A |
| KANON:QA17-IMPL-6 | P2 | objektív | FIXED | D-23: a Review options alóli kivételhez a `mod/quiz:viewreports` és a `moodle/grade:viewhidden` együtt kell (`quiz_get_review_options()`); a „During the attempt” az Adaptive viselkedésnél is elérhető — 9788c05 manifest LMS-M7-07 (:105), RA 19 (:96); a mátrix értékei változatlanok; verifier A |
| KANON:QA17-BIZT-7 | P2 | emberi-döntés | BLOCKED_HUMAN | EMBERI DÖNTÉS: láthatja-e a mentor a pontkönyvben a saját csoportja egyéni LMS-M0-06-pontszámát (GYV-23) — programvezető + Memuna, adatkör: DPO; jelölve: 9788c05 RA 15 „a várt eredmény nyitott”; Memuna-csomag, DPO-csomag |
| KANON:QA17-BIZT-6 | P2 | objektív | FIXED | ADV-2 („Memuna szükség esetén”, HUM 14) átvezetése a D-11 mechanizmusba — 9788c05 Adatvédelem :139, RA 15; a Memuna- és DPO-QA bizonyíték-kapu marad (X-1, X-2); verifier A |
| KANON:QA17-BIZT-3 | P1 | objektív | FIXED | HUM 15 D-16 vétó/QA oszlopa a 14. szakasz ERT-38 és ERT-3 cellája szerint (értékelési felelős is) — 9788c05 Emberi jóváhagyás szükséges.md D-16 sor; verifier B (a hatásköri rész: KANON:QA17-BIZT-3b) |
| KANON:QA17-BIZT-3b | P1 | emberi-döntés | BLOCKED_HUMAN | EMBERI DÖNTÉS: a D-16 besorolása — a lezárt táblában marad-e (a 14. szakasz bevezetője szerint az ERT-38/ERT-3 jobb oszlopa utólagos vétó/QA), vagy a nyitott táblába kerül, mert a döntési csomag a D-16 (a)/(b) részét az értékelési felelősnek adta — projektgazda + értékelési felelős; addig a Z.4 mércéje sem nem enyhül, sem nem szigorodik; értékelési csomag D-16 |
| KANON:QA17-BIZT-4 | P2 | objektív | FIXED | D-06 kikötése („Az issue nyilvános: személyes adat nem kerül bele.”) — 9788c05 Gyermekvédelem – release gate.md:33; verifier B |
| M2:QA17-BIZT-5 | P2 | objektív | FIXED | D-15 (e) regresszió: az M2.1 SLIDE 4 tanulói ígérete visszaszűkítve a válaszra — 9788c05 M2.1:437 („és a válaszod nem kerül mentésre.”); verifier B |
| KANON:QA17-IMPL-4 | P2 | objektív | FIXED | D-15 (e): a BSPEC-06 LMS-M2-01 része a követett CP interakció nélküli diájára mutat — 9788c05 manifest BSPEC-06; verifier B |
| KANON:QA17-IMPL-5 | P2 | objektív | FIXED | D-15 „Mindegyik külön tesztelendő”: tesztlépés a (c) LMS-M4-05 rubrika-megjelenítéshez (RA 26) és az (f) LMS-M0-05 zárt/nyitott állapotához (új RA 27) — 9788c05 runtime acceptance; beállításnév nincs kitalálva; verifier B |
| M7:QA17-ERT-1 | P1 | objektív | FIXED | D-23: a 8bb4d7d-ben bekerült, a döntésben nem szereplő „a kulcsot a javító próbálkozás után a mentor beszéli át” mondatrész törölve — 9788c05 M7 KAPU:51, manifest LMS-M7-07; verifier B (új szabály kérdése: M7:QA17-ERT-1b) |
| M7:QA17-ERT-1b | P1 | emberi-döntés | BLOCKED_HUMAN | EMBERI DÖNTÉS: legyen-e mentori kulcs-átbeszélés az M7 kapukvíz után, és ha igen, mikor (csak az utolsó próbálkozás után, vagy további kézi próbálkozás csak validált itemváltozattal) — értékelési felelős; a Review options mátrixa, a ≥12/14 küszöb és a Q13 blokkoló státusza nem változik; értékelési csomag |
| M3:QA17-ERT-2 | P2 | objektív | FIXED | D-03: az M3.B :385 igazítva az esetenkénti visszahozáshoz (:383), a „nem jelenet” védelem marad — 9788c05 M3.B:385; verifier B |
| KANON:QA17-ERT-3 | P2 | emberi-döntés | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-M4-05 rubrikájának build-paraméterei (Grade type, Maximum grade, a három szint pontja; rejtve, küszöb- és completion-hatás nélkül; MoodleDocs „Rubrics”: a pontérték kötelező) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| KANON:QA17-NYELV-1 | P2 | objektív | FIXED | egybeírás: „háromrészes” (HUM 15 D-16) — 9788c05 Emberi jóváhagyás szükséges.md D-16 sor; a HUM 14 ERT-38 szó szerinti idézete nem változik; fő session ellenőrizte |
| KANON:QA17-NYELV-2 | P2 | objektív | FIXED | „megterhelő-e” a „terhelő-e” helyett (HUM 15 D-08 (b), az M3.3 :78 szóhasználatával) — 9788c05; fő session ellenőrizte |
| M0:QA17-NYELV-3 | P2 | objektív | FIXED | névmási zuhanás: „az eszközön” a „rajta” helyett — 9788c05 M0.A:604; fő session ellenőrizte |
| M3:QA17-NYELV-4 | P2 | objektív | FIXED | „esetről esetre” (’alkalmanként’ félreolvasás ellen), és csak ahol két csoport dolgozta fel az esetet — 9788c05 M3.B:383, HUM 15 D-03; fő session ellenőrizte |
| M7:QA17-NYELV-5 | P2 | objektív | FIXED | egységes fogalom: „a javító próbálkozást nyitó felhasználói felülbírálás” — 9788c05 M7 KAPU:415; fő session ellenőrizte |
| Z:QA17-NYELV-6 | P2 | objektív | FIXED | „negatív tesztjével” (a teszt nem tesztelendő) — 9788c05 Z.4:400; fő session ellenőrizte |
| KANON:QA17-NYELV-7 | P2 | objektív | FIXED | hiányzó állítmány („látja”) az RA 19 pozitív esetében — 9788c05 runtime acceptance :96; fő session ellenőrizte |
| KANON:QA17-NYELV-8 | P2 | objektív | FIXED | hiányzó alaptag: „az M2.A csoportnormájának kiterjesztése” (HUM 15 D-13 nyitott sor) — 9788c05; fő session ellenőrizte |
| KANON:QA17-NYELV-9 | P2 | objektív | FIXED | vonzat: „nem sorolta a szerepköri döntések közé” (HUM 15 bevezető) — 9788c05; fő session ellenőrizte |
| M2:QA17-NYELV-10 | P2 | objektív | FIXED | tartalomvesztés: a „körbenézzenek” lépés visszaállítva a nem érzékeny állításokra (a :271 lezárás erre épít; a GYV-20-kivétel megmarad) — 9788c05 M2.A:254; fő session ellenőrizte |
| M7:QA17-NYELV-11 | P1 | objektív | DUPLICATE | = M7:QA17-ERT-1 |
| KANON:QA17-NYELV-12 | P2 | objektív | FIXED | „F-peula-képző” (HUM 15 D-11); egymást követő zárójelek összevonva (Adatvédelem :116, manifest LMS-M3-06, BSPEC-01) — 9788c05; a (b) rész az új, mellérendelt birtokos szerkezet miatt tárgytalan; fő session ellenőrizte |
| KANON:QA17-NYELV-13 | P2 | objektív | FIXED | tautológia: „név helyett szerepnév áll” — 9788c05 RELEASE-READINESS.md:39; fő session ellenőrizte |
| M3:QA17-NYELV-14 | P2 | emberi-döntés | BLOCKED_HUMAN | EMBERI DÖNTÉS: mire utal az M3.B 4.3.3 címében a „kívülről” az „új” törlése után (D-03) — M3 modulgazda; szövegjavaslat nincs |

## II. Vétólista

- Answer key, küszöb, ponthatár, rubrikaszint, időtartam: nem változott.
- Adatvédelmi megfogalmazás: az LMS-M0-06 role override a `mod/quiz:grade`-re is kiterjed (szigorítás a GYV-23 / D-11 átvezetéseként; Adatvédelem :140, manifest :31, :46); a FORUM-C „No groups” rögzítése a meglévő „kurzusrésztvevők látják” szabályt tartja meg; a Memuna ADV-2 szerinti, eljáráshoz kötött hozzáférése (Adatvédelem :139) a HUM 14 ADV-2 szó szerinti tartalma; az M2.1 SLIDE 4 tanulói ígérete a válaszra szűkült vissza (M2.1 :437).
- Értékelési megfogalmazás: az M7 kapuban és az LMS-M7-07-ben törölve a `8bb4d7d`-ben bekerült, a D-23-ban nem szereplő „a kulcsot a javító próbálkozás után a mentor beszéli át” mondatrész; a Review options mátrix értékei nem változtak.

## A. Verifier-utasítás

### Verifier – a célzott QA (QA17) findingjai, AP-2026-10-13-01

Adverzális második kör, read-only. Repó: a projekt munkapéldánya (ág: next-version/AP-2026-10-11-01, HEAD 158fdd8). NEM keresel új findingot: a megadott QA-findingokat vizsgálod felül. A findingok a `8bb4d7d` commit diffjére szóltak (diff: (munkamenet-scratchpad) diff-fix1.txt). A findingok teljes szövege:
- biztonság: (munkamenet-scratchpad) out-QA17-BIZT.md
- implementáció: (munkamenet-scratchpad) out-QA17-IMPL.md
- értékelés: (munkamenet-scratchpad) out-QA17-ERT.md

Háttér:
- A projektgazda 2026-10-13-i irányai szó szerint: `01 Fejlesztés/04 Audit/2026-10-13 Projektgazdai felhatalmazás és irányok – D-01…D-23, AP-2026-10-13-01.md`.
- `02 Tervezet/Emberi jóváhagyás szükséges.md`: a 14. szakasz (:601-től) bevezetője szerint a jobb oldali oszlop utólagos vétó/QA; az `F` sorban megnevezett feltétel a döntés része. A 15. szakasz (:771-től) a 2026-10-13-i projektgazdai döntéseket (lezárt tábla) és a nyitott, szerepköri sorokat rögzíti.
- Lezárt döntés és bizonyíték-kapu (szó szerint, `.claude/rules/safety-and-human-gates.md`): Lezárt projektgazdai döntés: az `Emberi jóváhagyás szükséges.md` `LEZÁRVA` + `Jóváhagyta:` tételei, és a 8. szakasztól kezdődő datált projektgazdai döntés-szakaszai (a kifejezetten nyitottként jelölt sorok kivételével); követni és átvezetni kell, nem újranyitni. Bizonyíték-kapu: a vétó/QA-szerepek írásos bizonyítéka és a runtime-bizonyíték a `RELEASE-READINESS.md` G1–G8 kapuihoz tartozik; nem írod be és nem feltételezed.
- Egy lezárt döntés szó szerinti átvezetése és egy bizonyított tényhiba javítása objektív; ami a döntésen túlmegy, új gyermekvédelmi, adatvédelmi vagy értékelési szabályt hoz, az emberi döntés (kié).

Tételenként:
1. Igaz-e a finding a fájl jelenlegi állapotában (idézd a sort), és a Moodle/H5P-állítás az elsődleges forrás szerint (docs.moodle.org, a moodle/moodle MOODLE_405_STABLE forrása, a h5p GitHub-forrás) — WebFetch-csel ellenőrizd, ha a finding forrásra hivatkozik.
2. A típus helyes-e (objektív / emberi-döntés / bizonyíték-kapu), és ha emberi: kié a döntés.
3. Objektív tételnél add meg a végleges javítást: fájl, OLD (szó szerint és egyedien a fájlban; Grep-pel ellenőrizve), NEW; a javítás a lehető legkisebb legyen, és ne hozzon új szabályt. Ha a javasolt javítás túlmegy a döntésen, mondd meg, mi a még objektív minimum.
4. A duplikátumokat jelöld (= melyik kulccsal).

Verdikt tételenként: MEGERŐSÍTVE (objektív, a végleges OLD→NEW-val) / MEGERŐSÍTVE – EMBERI DÖNTÉS (kié, mit) / RÉSZBEN (mi objektív, mi emberi) / ELVETVE (miért). A végén egy sor: hány tétel melyik verdikt. Tömör légy; legfeljebb kb. 45 lépés; ha nem fér bele, add le a kész verdikteket, és sorold fel a hiányzókat.

## B. Verdiktek – A köteg

A köteg, 8 ID. Minden Moodle- és H5P-állítást a forrásban néztem meg, WebFetch-csel: moodle/moodle MOODLE_405_STABLE, docs.moodle.org/405, h5p GitHub master.

**Verdiktek**

- **QA17-IMPL-2 · MEGERŐSÍTVE · objektív · ez a klaszter 1 megtartott kulcsa.**
  - A forrás szerint a Manual grading riport a `mod/quiz:grade` joggal nyílik meg (`grading/db/install.php`: `$record->capability = 'mod/quiz:grade';`).
  - A `quiz_report_list()` csak akkor használja a `mod/quiz:viewreports`-ot, ha a riportnak nincs saját joga (`if (empty($capability)) { $capability = 'mod/quiz:viewreports'; }`).
  - A `report.php` maga nem kér `viewreports`-ot, a `grading/report.php` viszont kér: `require_capability('mod/quiz:grade', …)`, és van `includeauto` paramétere. Az `access.php` szerint a `teacher` szerep alapból megkapja a `mod/quiz:grade` jogot.
  - A D-11 (HUM 15 :800) csak annyit mond: „az M0 belépőkvíz egyéni válaszai a GYV-23 szerint”. A mechanizmus javítása ezért a döntés átvezetése, nem újranyitás.
  - A `quiz/grading:viewstudentnames` rögzítése fölösleges: `mod/quiz:grade` nélkül a riport el sem érhető. Ez a pont kihagyható.
  - Javítás:
    - ADV :140. OLD: „vonja el a `mod/quiz:viewreports` capabilityt” → NEW: „vonja el a `mod/quiz:viewreports` és a `mod/quiz:grade` capabilityt (a Manual grading riport a `mod/quiz:grade`-del nyílik: `mod/quiz/report/grading/db/install.php`, `MOODLE_405_STABLE`)”.
    - Manifest :31. OLD: „vonja el a `mod/quiz:viewreports`-ot a nem szerkesztő” → NEW: „vonja el a `mod/quiz:viewreports`-ot és a `mod/quiz:grade`-et a nem szerkesztő”.
    - Manifest :46. OLD: „vonja el a `mod/quiz:viewreports`-ot: a mentor” → NEW: „vonja el a `mod/quiz:viewreports`-ot és a `mod/quiz:grade`-et: a mentor”.
    - RA :87. OLD: „sem nyithatja meg a kvízriportokat és más tanuló próbálkozásának áttekintését” → NEW: „sem nyithatja meg a kvízriportokat (a Manual grading riportot sem, „Also show questions that have been graded automatically” bekapcsolásával és közvetlen URL-lel sem: `mod/quiz/report.php?mode=grading`) és más tanuló próbálkozásának áttekintését”.
  - Mindegyik OLD egyszer fordul elő a fájljában, Greppel ellenőrizve.

- **QA17-BIZT-1 · MEGERŐSÍTVE · objektív · duplikátum, a kulcs a QA17-IMPL-2.** Ugyanaz a tényállás. A pontos sorhelyeit (ADV :140, manifest :31 és :46, RA :87) a fenti javítás már tartalmazza.

- **QA17-BIZT-2 · RÉSZBEN · objektív (FORUM-C) / EMBERI DÖNTÉS (FEEDBACK-N) · ez a klaszter 2 megtartott kulcsa.**
  - A forrás igazolja a csoportmód öröklését:
    - `course/modlib.php`: `$data->groupmode = $course->groupmode;`;
    - MoodleDocs 4.5: „The group mode defined at the course level is the default mode for all activities defined within that course.”
  - A FORUM-C profilja (manifest :21) nem rögzít csoportmódot, és „No groups” sehol nincs a `02 Tervezet/`-ben. Az ADV :141 mondata ezért nem igaz: „minden activity a saját, a buildben rögzített csoportmódját tartja”.
  - A FORUM-C javítása a meglévő „kurzusrésztvevők látják” szabály átvezetése:
    - Manifest :21. OLD: „| kurzusrésztvevők látják |” → NEW: „| kurzusrésztvevők látják; „Group mode” = „No groups” (a kurzus „Separate groups” alapértéke miatt rögzítve, D-11; stagingben visszaolvasandó) |”.
    - ADV :141. OLD: „és a FORUM-C kurzusszintű láthatósága” → NEW: „és a FORUM-C kurzusszintű láthatósága („Group mode” = „No groups”)”.
  - FEEDBACK-N: a mentor Z.4-hozzáférése már nyitott DPO-kérdés (ADV :119, BIZT-6), ezért a csoportmód értékéről a DPO dönt. Addig a FEEDBACK-N profilban csak a „Group mode: nyitott (DPO, BIZT-6)” jelölés objektív.

- **QA17-IMPL-3 · MEGERŐSÍTVE · objektív · duplikátum, a kulcs a QA17-BIZT-2.** Az LMS-M0-05 (manifest :45) helyét és a MoodleDocs-idézetét érdemes átvenni. A javaslat utolsó mondata („a többi activity csoportmódját is érdemes rögzíteni”) nem bizonyított és nem objektív, ezt kihagyandó.

- **QA17-IMPL-1 · EMBERI DÖNTÉS · emberi-döntés · a forrásállítás igaz, a döntés a projektgazdáé.**
  - A `libraryScreen.js` `showNextLibrary()`-jében a `libraryTitle.innerHTML = (library.showContentTitle && contentTitle ? …)` csak az `if (!LibraryScreen.isBranching(library))` ágban áll. A `// Show a branching question` ág a címhez nem nyúl.
  - A `branchingQuestion.js` nem jelenít meg metadata-címet, csak ezt: `title.innerHTML = parameters.branchingQuestion.question`.
  - Az M3.3 :70 szerint a P1–P4 csomópont Branching Question. A D-08 (b) maga nevezi meg a `showContentTitle`-t, így ez a megoldás a master forrás szerint nem fog működni. A célverzió ismeretlen, és az RA 11 már rögzíti, hogy ilyenkor a BSPEC-05 újranyílik.
  - Más megjelenítési mód választása (például új csomópont) a build-spec gazdájának, a projektgazdának a döntése, Memuna-QA-val.

- **QA17-IMPL-6 · MEGERŐSÍTVE · objektív.**
  - (a) A `quiz_get_review_options()` feltétele `has_capability('mod/quiz:viewreports') && has_capability('moodle/grade:viewhidden')`: a kivételhez mindkét jog kell.
  - (b) Az ősosztály `get_unused_display_options()` alapból `array()`-t ad vissza, és az `adaptive` típus ezt nem írja felül. Az „Adaptive mode” és az „Adaptive mode (no penalties)” viselkedésnél tehát a „During the attempt” oszlop is elérhető.
  - Javítás:
    - Manifest :105. OLD: „a `moodle/grade:viewhidden` jogú szerepekre a beállítás nem vonatkozik” → NEW: „a `mod/quiz:viewreports` és a `moodle/grade:viewhidden` jogot együtt birtokló szerepekre a beállítás nem vonatkozik (`mod/quiz/locallib.php`, `quiz_get_review_options()`)”.
    - RA :96. OLD: „(`moodle/grade:viewhidden`) jogú felhasználóra” → NEW: „(`moodle/grade:viewhidden`) és a `mod/quiz:viewreports` jogot együtt birtokló felhasználóra”.
    - Manifest :105. OLD: „„Immediate feedback”, „Immediate feedback with CBM” vagy „Interactive with multiple tries”” → NEW: „„Adaptive mode”, „Adaptive mode (no penalties)”, „Immediate feedback”, „Immediate feedback with CBM” vagy „Interactive with multiple tries””.
  - A mátrix értékei nem változnak.

- **QA17-BIZT-7 · EMBERI DÖNTÉS · emberi-döntés.**
  - Az RA :87 záró mondata („rögzíteni kell, hogy a mentor a pontkönyvben látja-e…”) tényleg várt eredmény nélküli teszt.
  - Sem a GYV-23 (HUM :646, amely a válaszhozzáférésről szól), sem a D-12 (amely a nyilvános itemvisszajelzésről szól) nem dönti el szó szerint az egyéni összpontszám mentori láthatóságát.
  - Adatvédelmi kérdés: a programvezető és a Memuna dönt, az adatkörről a DPO. A finding javaslata használható.

- **QA17-BIZT-6 · MEGERŐSÍTVE · objektív (az ADV-2 átvezetése; nem emberi döntés).**
  - A hiány valós: az ADV §3 :139 felsorolásából kimarad a Memuna.
  - A lezárt ADV-2 (HUM :648) szó szerint megválaszolja a kérdést: „Memuna szükség esetén”. Ugyanez áll az ADV §5 :158-ban is: „a Memuna szükség esetén”.
  - A technikai módot a :139 már az LMS-gazdára bízza. A finding EMBERI DÖNTÉS javaslata ezért nem használható.
  - Javítás, ADV :139. OLD: „A második vagy fellebbezési értékelő és az F-peula képzője csak az ADV-2 szerinti” → NEW: „A második vagy fellebbezési értékelő, az F-peula képzője és – szükség esetén – a Memuna csak az ADV-2 szerinti”.
  - Következményként az RA :87 „A második vagy fellebbezési értékelő és az F-peula képzője hozzáférését…” mondatába is felvehető a Memuna.
  - A Memuna- és a DPO-QA bizonyíték-kapu marad (G-kapu).

**Összesen**
- 5 MEGERŐSÍTVE: QA17-IMPL-2, QA17-BIZT-1 (duplikátum), QA17-IMPL-6, QA17-BIZT-6, QA17-IMPL-3 (duplikátum).
- 1 RÉSZBEN: QA17-BIZT-2 (FORUM-C objektív, FEEDBACK-N emberi döntés).
- 2 EMBERI DÖNTÉS: QA17-IMPL-1 (projektgazda, Memuna-QA), QA17-BIZT-7 (programvezető + Memuna; adatkör: DPO).
- 0 ELVETVE.
- 0 bizonyíték-kapu típusú finding; a QA17-BIZT-6-nál a Memuna- és a DPO-QA bizonyíték-kapuként nyitva marad.

**Duplikátumok**
- QA17-BIZT-1 = QA17-IMPL-2; a megtartott kulcs a QA17-IMPL-2.
- QA17-IMPL-3 = QA17-BIZT-2 (FORUM-C rész); a megtartott kulcs a QA17-BIZT-2.

Érintett fájlok:
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md

## B. Verdiktek – B köteg

B köteg, a QA17 verdiktjei (HEAD 158fdd8, read-only). Mind a nyolc ID-hez van verdikt.

QA17-BIZT-3 · MEGERŐSÍTVE (objektív minimum) + EMBERI DÖNTÉS (hatáskör) · objektív + emberi-döntés · A D-16 vétó/QA oszlopából tényleg kimaradt az értékelési felelős. A D-15 (c) és a D-23 a 14. szakasz szerepeit átmásolta, a D-16 nem.
- Az ERT-38 cellája (:708): „értékelési felelős; vétó/QA: programvezető.” Az ERT-3 cellája (:673): „értékelési felelős (Z.4); vétó/QA: DPO + programvezető (Z.4)”. A D-16 sora (:804): „ERT-38: programvezető; Z.4: DPO + programvezető.”
- Végleges javítás az `Emberi jóváhagyás szükséges.md`-ben. OLD (egyedi): `| ERT-38, ERT-3 | ERT-38: programvezető; Z.4: DPO + programvezető. |`. NEW: `| ERT-38, ERT-3 | ERT-38: értékelési felelős, programvezető; Z.4: értékelési felelős, DPO + programvezető. |`
- A hatásköri kérdés valós, ezért emberi döntés. A döntési csomag D-16 „Ki dönt” sora: „(a) értékelési felelős; (b) értékelési felelős a DPO-val; (c) projektgazda”, és az „Addig” bekezdés szerint „a feloldása küszöbdöntés”. A projektgazda 2. végrehajtási szabálya: „az értékelési felelős … döntési hatáskörét ne vedd át”. A HUM 15 ennek ellenére a lezárt táblába tette a D-16-ot.
- Kié a döntés: a projektgazdáé és az értékelési felelősé, a D-16 (a)/(b) részéről. A sort nem mi nyitjuk újra.

QA17-BIZT-4 · MEGERŐSÍTVE · objektív · A GK :33 a nyilvános G1 issue-t nevezi meg a JOG-1 nyilvántartásának, a D-06 kikötése nélkül. A HUM :798 és a RELEASE-READINESS :39 tartalmazza a kikötést.
- A javítás a lezárt D-06 szó szerinti átvezetése, invariánst nem sért.
- `Gyermekvédelem – release gate.md`. OLD (egyedi): `G1 tracker-issue (#1; projektgazdai döntés, 2026-10-13, D-06).` NEW: `G1 tracker-issue (#1; projektgazdai döntés, 2026-10-13, D-06). Az issue nyilvános: személyes adat nem kerül bele.`

QA17-BIZT-5 · MEGERŐSÍTVE · objektív · Regresszió a 8bb4d7d-ben. A diff a „A válaszod nem kerül mentésre.” mondatot „…és semmi nem kerül mentésre.”-re tágította, pedig a követett CP próbálkozást, állapotot és completiont rögzít (lásd a :431 megjegyzést és az RA 21. pontot).
- A javasolt „sehol” felesleges új abszolút állítás, ezért az eredeti szűkítést javaslom visszaállítani.
- M2.1 :437. OLD (egyedi): `nem kell bejelölnöd, és semmi nem kerül mentésre.` NEW: `nem kell bejelölnöd, és a válaszod nem kerül mentésre.`
- Látható szöveg, ezért pin kell.

QA17-IMPL-4 · MEGERŐSÍTVE · objektív · A BSPEC-06 (:319) még ezt írja: „LMS-M2-01: IMPL-6 korlátja”. Az IMPL-6 szövege: „ne a követett activityben fusson”. Ez ellentmond a D-15 (e)-nek, a H5P-C cellának (:16) és az LMS-M2-01 sornak (:54).
- `LMS – activity manifest.md`. OLD (egyedi): `LMS-M2-01: IMPL-6 korlátja;` NEW: `LMS-M2-01: a követett CP interakció nélküli reflexiós diája (kiegészítés, 2026-10-13, D-15 (e), PRG-9 b; az IMPL-6 korlátja ezzel módosult; a sor állapota nem változik);`

QA17-IMPL-5 · MEGERŐSÍTVE · objektív · A HUM D-15 szerint „Mindegyik külön tesztelendő.” Az RA-ban azonban sem az LMS-M4-05 rubrikájának rejtésére (c), sem az LMS-M0-05 zárt és nyitott állapotára (f) nincs tesztlépés.
- A „fórum”, „FORUM”, „M0-05” és „szintpont” keresés 0 találatot adott. A 26. pont csak az LMS-M1-05-öt nézi.
- A javaslat iránya jó. A beállításneveket azonban a tesztlépésbe csak elsődleges forrásból (MOODLE_405_STABLE) szabad beírni; amíg nincs ilyen forrás, maradjon a „rögzíteni kell a beállítás nevét” fordulat.

QA17-ERT-1 · MEGERŐSÍTVE (objektív minimum) · objektív · A „mentor beszéli át a kulcsot” mondatrészt a 8bb4d7d vezette be, és nincs a döntés mögött.
- A HUM D-23 csak a D1 (a) és a D2 (1) változatot tartalmazza. A projektgazda iránya sem tartalmazza a mondatrészt. A mentori átbeszélés csak a csomag el nem fogadott (3) opciójában szerepel (:518).
- Objektív minimum: a mondatrész törlése mindkét helyen.
  - M7 KAPU :51. OLD (egyedi): `; a kulcsot a javító próbálkozás után a mentor beszéli át a madrihhal (projektgazdai döntés, 2026-10-13, D-23; ERT-5).` NEW: ` (projektgazdai döntés, 2026-10-13, D-23; ERT-5).`
  - Manifest :105. OLD (egyedi): `, a kulcsot a javító után a mentor beszéli át;` NEW: `;`
- Mindkét OLD egyedi: a „a kulcsot a javító” kifejezés 1–1 találat. A „szabályos javítási útmutatás” mondat marad.
- Hogy legyen-e mentori kulcs-átbeszélés, az új értékelési szabály. Döntéshozó: az értékelési felelős. A javasolt „emberi-döntés” típus csak erre a részre áll.

QA17-ERT-2 · MEGERŐSÍTVE · objektív · A :383 (D-03, esetenként: „az egyik csoport ismerteti …, a másik kiegészíti”) és a változatlanul hagyott :385 („Minden csoport **ismerteti az elemzését**”) ütközik.
- A javasolt átírás a szükségesnél többet változtat. A legkisebb javítás, amely a „nem jelenet” védelmet megtartja: M3.B. OLD (egyedi): `* Minden csoport **ismerteti az elemzését**, nem jelenetet mutat be.` NEW: `* A csoportok **az elemzésüket ismertetik**, nem jelenetet mutatnak be.`
- A :386, a „3–4 perc / eset” és a „12 perc” nem változik.

QA17-ERT-3 · EMBERI DÖNTÉS · emberi-döntés · A hiány valós.
- Az LMS-M4-05 (:80) az LMS-M2-05 mintájára hivatkozik, de nincs benne Grade type, Maximum grade és szintpont. A kánoni M4-rubrikának nincs pontja: „nincs fix pontszám” (M4 hub :131).
- A MoodleDocs 4.5 „Rubrics” oldala (WebFetch, egyezik a findinggal): „Numeric points are required, but … it is possible to hide these from students”, valamint: „the ultimate grade for the assignment will be recalculated as the proportion of that maximum grade.”
- A pontértékek új build-paraméterek egy rubrikához, ezért ezeket nem pótolhatjuk magunk. Döntéshozó: a projektgazda mint build-spec gazda, QA: az értékelési felelős.

Összesítés: 7 MEGERŐSÍTVE (BIZT-3, BIZT-4, BIZT-5, IMPL-4, IMPL-5, ERT-1, ERT-2), 0 ELVETVE, 1 EMBERI DÖNTÉS (ERT-3). Ebből bizonyíték-kapu: 0. Két MEGERŐSÍTVE tételnek emberi része is van: a BIZT-3 hatáskör-kérdése (projektgazda és értékelési felelős) és az ERT-1 esetleges új szabálya (értékelési felelős). Duplikátum nincs. Az IMPL-5 (c) és az ERT-3 ugyanarra a sorra vonatkozik, de az egyik tesztlépés, a másik build-paraméter, ezért nem duplikátumok.

## C. Nyers lencse-kimenet – biztonság-jog

Lencse: biztonság-jog, ID-prefix QA17-BIZT. Ez diffre szabott ellenőrzés volt (diff-fix1.txt), read-only. 7 findingot adok; a cap alatt maradtam, egyet sem hagytam ki.

Három Moodle-állítást elsődleges forrásból ellenőriztem: a moodle/moodle MOODLE_405_STABLE ágának forráskódját olvastam a raw.githubusercontent.com-on. A többi a repóból bizonyítható.

---

**QA17-BIZT-1**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:140`
  - `02 Tervezet/LMS – activity manifest.md:31` és `:46` (LMS-M0-06)
  - `02 Tervezet/LMS – H5P runtime acceptance.md:87`
- **Probléma:** Az M0 belépőkvíz D-11/GYV-23 szerinti védelme csak a `mod/quiz:viewreports` jogot vonja el. A Moodle 4.5 kézi értékelési riportja (Manual grading) viszont a `mod/quiz:grade` joggal nyílik meg. A nem szerkesztő tanári szerep ezt alapból megkapja, és a riport az automatikusan értékelt kérdések egyéni válaszait is megmutatja, a tanulók nevével. Így a „tételszintű egyéni válaszokat alapból nem látja” állítás a leírt beállítással nem teljesül. Besorolás: TÉNY.
- **Bizonyíték:**
  - Manifest LMS-M0-06: „activity-szintű role override vonja el a `mod/quiz:viewreports`-ot: a mentor a tételszintű egyéni válaszokat alapból nem látja”.
  - Forrás: `mod/quiz/report/grading/db/install.php`: „$record->capability = 'mod/quiz:grade';”
  - Forrás: `report.php`: „require_capability('mod/quiz:grade', $this->context);”, továbbá „if (!$includeauto && $counts->needsgrading == 0 && $counts->manuallygraded == 0) { continue; }”
  - Forrás: `mod/quiz/db/access.php`: `'mod/quiz:grade'` → `'teacher' => CAP_ALLOW`
  - Forrás: `quiz/grading:viewstudentnames` → `'teacher' => CAP_ALLOW`
- **Hatás:** Egy saját csoportjába sorolt mentor a GYV-23 által tiltott módon látja a biztonsági 1–2. item egyéni válaszait, névvel együtt. A tanulóknak és a DPO-nak szóló hozzáférési állítás hamis lenne.
- **Javaslat:** Az LMS-M0-06 activity-szintű role override-ja a `mod/quiz:viewreports` mellett vonja el a `mod/quiz:grade` jogot is (a kvízben nincs kézzel értékelt item). A szöveget három helyen kell átvezetni: ADV §3 :140, manifest :31 és :46. A runtime acceptance 15. pontjába kerüljön be kifejezetten a Manual grading riport („Also show questions that have been graded automatically”) negatív tesztje. A GYV-23 tartalmához, a D-11 kiterjedéséhez és a statisztikai riport kérdéséhez ne nyúlj.
- **Típus:** objektív
- **Verdikt:**

---

**QA17-BIZT-2**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:135` és `:141`
  - `02 Tervezet/LMS – activity manifest.md` §1, a „Mentori csoportszűkítés” bekezdés, valamint a FORUM-C és a FEEDBACK-N sor
- **Probléma:** A D-11 a kurzus „Group mode” beállítását „Separate groups”-ra állítja. Moodle-ben az új activity alapértelmezett csoportmódja a kurzusé. A FORUM-C (Bemutatkozó fal) és a FEEDBACK-N (Z.4) csoportmódját viszont sehol nem rögzíti a build: a „No groups” érték a repóban sehol nem szerepel. Ezért nem igaz, hogy „minden activity a saját, a buildben rögzített csoportmódját tartja”, és hogy a FORUM-C láthatósága nem változik. Besorolás: TÉNY. A FEEDBACK-N csoportmódjának értéke: EMBERI JÓVÁHAGYÁS KELL.
- **Bizonyíték:**
  - ADV §3 :141: „így minden activity a saját, a buildben rögzített csoportmódját tartja, és a FORUM-C kurzusszintű láthatósága […] nem változik”.
  - Forrás: `course/modlib.php`, `prepare_new_moduleinfo_data`: „$data->groupmode = $course->groupmode;”
- **Hatás:**
  - A bemutatkozó fal csoportokra szakadhat, és az M0.4 :520 tanulói mondata („a kurzus résztvevői látják”) pontatlanná válik.
  - A név nélküli Z.4-visszajelzés csoportszintű (legfeljebb 8 fős) bontásban könnyebben visszaazonosítható lehet. A mentor Z.4-hozzáférése amúgy is nyitott DPO-kérdés (BIZT-6).
- **Javaslat:** A FORUM-C profilban és az ADV §3 mechanizmusában rögzíteni kell, hogy „Group mode” = „No groups”. Ez a meglévő „kurzusrésztvevők látják” szabály átvezetése. A FEEDBACK-N csoportmódjára: EMBERI DÖNTÉS: a DPO döntse el a BIZT-6-tal együtt, a mentor tényleges Z.4-hozzáférésének staging-visszaolvasásával. Addig a build-specben jelölni kell, hogy az érték nyitott.
- **Típus:** objektív (FORUM-C) / emberi-döntés (FEEDBACK-N)
- **Verdikt:**

---

**QA17-BIZT-3**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Emberi jóváhagyás szükséges.md` > 15. szakasz, a „Lezárt döntés” bekezdés (~:784–786) és a D-16 sora (~:804)
- **Probléma:** A HUM 15 csak azt a tételt sorolja lezárt projektgazdai döntésnek, amelynél „a 14. szakasz érintett sorában nincs más szerepnek fenntartott jóváhagyás”. Az ERT-38 és az ERT-3 (Z.4) cellája azonban az értékelési felelőst a „vétó/QA:” jelölés előtt nevezi meg. Ugyanezen a helyen áll az ERT-8-ban és az ADV-3-ban a döntéshozó („projektgazda;”). A D-16 sor vétó/QA oszlopából ráadásul az értékelési felelős teljesen kimaradt. Besorolás: hogy a D-16 projektgazdai hatáskör-e, az EMBERI JÓVÁHAGYÁS KELL; hogy a szerep kimaradt, az TÉNY.
- **Bizonyíték:**
  - ERT-38 (:708): „értékelési felelős; vétó/QA: programvezető.”
  - ERT-3 (:673): „projektgazda (QUIZ-D, build-spec); értékelési felelős (Z.4); vétó/QA: DPO + programvezető (Z.4).”
  - D-16: „ERT-38: programvezető; Z.4: DPO + programvezető.”
- **Hatás:** A Z.4 „Teljesítve”-mércéjét (szenzitív részek passzolhatósága, bukási ok) lezártként kezelik. Az értékelési felelős vétója így nem kerül hozzá. Ez szerepkörön kívüli lezárás kockázata.
- **Javaslat:** Objektív minimum: a D-16 vétó/QA oszlopába vissza kell írni az értékelési felelőst a 14. szakasz cellái szerint. EMBERI DÖNTÉS: a projektgazda és az értékelési felelős döntse el, hogy a D-16 a lezárt táblában marad-e, vagy átkerül a nyitott, szerepköri táblába. Bizonyíték: az ERT-38/ERT-3 cellaszerkezete és a verifier indoklása. Addig a Z.4 tanulóbarát (passzolható) mércéje nem enyhíthető és nem szigorítható.
- **Típus:** emberi-döntés
- **Verdikt:**

---

**QA17-BIZT-4**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Gyermekvédelem – release gate.md:33`
- **Probléma:** A D-06 átvezetése a gyermekvédelmi release gate-be hiányos. A nyilvános tracker-issue-t nevezi meg a JOG-1 elsődleges nyilvántartásának, de a döntés része, hogy „személyes adat nem kerül bele”, ez innen kimaradt. A HUM 15 és a RELEASE-READINESS.md :39 tartalmazza. Besorolás: PROJEKT-DÖNTÉS (D-06), hiányos átvezetés.
- **Bizonyíték:**
  - GK :33: „A jogászi ellenőrzés (JOG-1) elsődleges nyilvántartása a `RELEASE-READINESS.md` szerinti G1 tracker-issue (#1; projektgazdai döntés, 2026-10-13, D-06).”
  - HUM D-06: „Az issue nyilvános: személyes adat nem kerül bele.”
- **Hatás:** A gyermekvédelmi dokumentumból kiinduló szereplő nem látja, hogy a nyilvános GitHub-issue-ba nem kerülhet személyes adat. Ilyen adat lehet egy konkrét eset vagy a jogász, illetve más szereplő azonosító adata.
- **Javaslat:** A GK :33 mondata egészüljön ki a D-06 szó szerinti kikötésével: „Az issue nyilvános: személyes adat nem kerül bele.” Más tartalomhoz ne nyúlj.
- **Típus:** objektív
- **Verdikt:**

---

**QA17-BIZT-5**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrihként – identitás-körök.md:437`
- **Probléma:** Az új tanulói mondat a korábbi, a válaszra szűkített ígéretet („A válaszod nem kerül mentésre.”) általános „semmi nem kerül mentésre” ígéretre bővíti. A követett Course Presentation viszont a lecke próbálkozását, mentett állapotát és completionjét rögzíti. Besorolás: TÉNY.
- **Bizonyíték:** „> *Csak gondold végig – nem kell bejelölnöd, és semmi nem kerül mentésre.*”
- **Hatás:** A különleges adathoz közeli identitás-kérdésnél a tanuló tágabb adatvédelmi ígéretet kap, mint ami igaz. Ez ellentétes azzal, hogy a tanulói ígéreteknek a tényleges beállítást kell követniük (ADV-1, runtime acceptance 21. és 24. pont).
- **Javaslat:** Az ígéretet vissza kell szűkíteni a SLIDE 4 válaszára. Példa: „Csak gondold végig – nem kell bejelölnöd, és a válaszod sehol nem kerül mentésre.” A D-15 (e) mechanizmusához, a kérdéshez és az opciókhoz ne nyúlj. Látható szöveg, ezért pin kell.
- **Típus:** objektív
- **Verdikt:**

---

**QA17-BIZT-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:**
  - `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:139`
  - `02 Tervezet/LMS – activity manifest.md` LMS-M3-05, LMS-M3-08, LMS-M3-07 (a Megjegyzés oszlop)
- **Probléma:** A D-11 a beadásokat és a GATE-CP-t csoportra szűkíti. A mechanizmus azonban csak a második vagy fellebbezési értékelő és az F-peula képzője hozzáférését rendezi. Nincs rögzítve, hogyan fér hozzá a Memuna egy másik csoport M3-helyzetleírásához és GATE-CP-jéhez, holott az R2/R4 blokkoló kimenetnél a döntést „a mentor, a második képző és a Memuna együtt hozza”. Besorolás: EMBERI JÓVÁHAGYÁS KELL.
- **Bizonyíték:**
  - ADV §3 :139: „A második vagy fellebbezési értékelő és az F-peula képzője csak az ADV-2 szerinti, konkrét eljáráshoz kötött, dokumentált hozzáférést kap”.
  - Manifest: „R2/R4 blokkoló kimenetnél a döntést a mentor, a második képző és a Memuna együtt hozza (§4)”.
- **Hatás:** A gyermekvédelmi kapudöntés Moodle-ben nem lesz elvégezhető, vagy a beadást Moodle-en kívül, dokumentálatlanul osztják meg. Ez adatvédelmi és eljárási kockázat.
- **Javaslat:** EMBERI DÖNTÉS: a Memuna (ADV-2: „a Memuna szerepéről a Memuna”) és a DPO / jogi felelős döntse el az LMS-gazdával a Memuna eljáráshoz kötött, dokumentált hozzáférésének módját. Bizonyíték: a staging role-matrix és a runtime acceptance 15. pontjának visszaolvasása. Új hozzáférési szabályt addig ne írj be.
- **Típus:** emberi-döntés
- **Verdikt:**

---

**QA17-BIZT-7**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:87` (15. pont, a mondat vége)
- **Probléma:** A pontkönyvben (`moodle/grade:viewall`, a nem szerkesztő tanárnak alapból megvan) a mentor a saját csoportja egyéni M0-belépőkvíz-pontszámát láthatja. A teszt ezt csak rögzítteti, várt eredmény és döntési gazda nélkül. A GYV-23 és a D-12 a biztonsági itemekre név és egyéni eredmény nélküli, csoportszintű kezelést ír elő. Besorolás: EMBERI JÓVÁHAGYÁS KELL.
- **Bizonyíték:** „azt is rögzíteni kell, hogy a mentor a pontkönyvben látja-e a saját csoportja LMS-M0-06-pontszámát (GYV-23).”
- **Hatás:** Az egyéni eredmény a pontkönyvben megmaradhat, és lehetővé teheti a megbélyegző egyéni utánkövetést. Ez a GYV-23 célját kerüli meg, és a teszt nem tud megbukni.
- **Javaslat:** EMBERI DÖNTÉS: a programvezető, a Memuna és a DPO (a GYV-23 szerepei) döntse el, hogy a mentor láthatja-e az egyéni LMS-M0-06 pontszámot a pontkönyvben. Ennek alapján kell a 15. pontba a várt eredményt beírni. Addig a mondat nyitott kérdésként jelölendő, és nem tekinthető átmenő tesztnek.
- **Típus:** emberi-döntés
- **Verdikt:**

---

Fájlonként, megállapítás nélkül ellenőrizve:
- **HUM 15:** mind a 23 csomag szerepel. A nyitott tábla `nyitott` jelölésű. Nem állít release-t és jóváhagyást. A G1–G8 bizonyíték, a runtime és a pilot nyitva marad.
- **D-12 (M0 hub):** megfelel a GYV-23-nak.
- **D-13 (a) (M0.A) és D-13 (e) (M2 kapu):** a névmező megszűnt, maradék hivatkozás nincs.
- **D-15 (e) (M2.1, a manifest LMS-M2-01, runtime acceptance 21. pont):** a tárolásmentesség célja megmaradt.
- **M2.A:254 (GYV-20):** a „körbenézzenek” kikerült, a reflexió nem érzékeny állításra korlátozódik, összhangban a :251 és a :266 sorral.
- **D-03 (M3.A, M3.B):** megmaradt a harmadik személyű esetelemzés, a „senki nem alakítja” mondat, a „Fontos különbség” doboz (:410, :471) és a valós eset tilalma.
- **D-16 (Z.4 és runtime acceptance 16. pont):** a negatív teszt helyes; a törlés a DPO-nál marad.
- **D-23:** a kulcs nem szivárog; a `viewhidden` kivétel kezelve van.

## C. Nyers lencse-kimenet – implementáció

6 finding: 2×P1, 4×P2. Lencse: implementáció, csak a diff-fix1 módosított soraira.

**QA17-IMPL-1**
- **Súlyosság:** P1
- **Bizalom:** közepes. Az upstream master forrásból igazolt, a célverzió még ismeretlen.
- **Lencse:** implementáció
- **Hely:**
  - `02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md` > „A csomóponttérkép szabályai”, „Témajelzés a passz-választón”; a térkép 4., 9., 13. és 16. sora
  - `02 Tervezet/LMS – activity manifest.md` > BSPEC-05 (LMS-M3-03)
  - `02 Tervezet/LMS – H5P runtime acceptance.md` > 11. pont, „Témajelzés a passz-választón”
- **Probléma:** a D-08 (b) build-specje a témajelzést a P1–P4 Branching Question-csomópont saját `showContentTitle` beállítására bízza. A H5P Branching Scenario forrása szerint Branching Question-csomópontnál ez a beállítás nem frissíti a fejléc címét. A kérdés rétegként (overlay) jelenik meg az előző képernyő fölött.
- **Bizonyíték:**
  - M3.3: „a P1–P4 csomópont tartalomcíme a soron következő szitu meglévő címe … és a csomóponton a `showContentTitle` be van kapcsolva”.
  - h5p-branching-scenario (master), `src/scripts/libraryScreen.js`, `showNextLibrary()`: a cím frissítése, `this.libraryTitle.innerHTML = (library.showContentTitle && contentTitle ? contentTitle : '&nbsp;');`, csak az `if (!LibraryScreen.isBranching(library))` ágban áll. Az `else { // Show a branching question` ág a `libraryTitle`-hoz nem nyúl, és a forrás szerint „BS could be showing start screen or library screen”.
  - A `semantics.json` leírása: „If selected, the user will see the content title in the top bar above this content.”
  - A h5p-branching-question nem jeleníti meg a metadata címet. A cím elem a kérdésszöveg: `title.innerHTML = parameters.branchingQuestion.question;`.
- **Hatás:** a GYV-2 szerinti előzetes témajelzés a passz-döntés pillanatában várhatóan nem jelenik meg. A fejlécben az előző csomópont (INSTR-12, S1-SAFE-2, INSTR-34, S3-SAFE) címe vagy üres sor áll. A 11. pont tesztje így előre láthatóan bukik, és a BSPEC-05 újranyílik. A spec ebben a formában nem építhető meg.
- **Javaslat:** EMBERI DÖNTÉS: a build-spec gazdája (projektgazda) válasszon olyan megjelenítési módot, amely Branching Question előtt is megjelenik. Lehetőségek: minden P-csomópont elé egy csak a szitu meglévő címét tartalmazó csomópont, vagy a cím a megelőző csomóponton. Ehhez Memuna-QA kell, és a 11. pont tesztje a választott módot ellenőrizze.
  - Javítási korlát: a §7.1 szerinti kérdés és a két opció szó szerint nem változhat; a passz-szabály és a biztonsági csomópontok rendje sem.
- **Típus:** emberi-döntés
- **Verdikt:**

**QA17-IMPL-2**
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:**
  - `02 Tervezet/LMS – activity manifest.md` > §2 LMS-M0-06; §1 QUIZ-D mentor-láthatóság; „Mentori csoportszűkítés” bekezdés
  - `02 Tervezet/Adatvédelem – tanulói adatok és AI.md` > §3, „A mentor-láthatóság mechanizmusa”, LMS-M0-06 pont; a profiltábla QUIZ-D/QUIZ-M sora
  - `02 Tervezet/LMS – H5P runtime acceptance.md` > 15. pont
- **Probléma:** az LMS-M0-06 role override csak a `mod/quiz:viewreports`-ot vonja el. A nem szerkesztő tanárnál alapból megmarad a `mod/quiz:grade`, ezzel pedig megnyílik a kézi értékelés riport (Manual grading), amely az automatikusan pontozott kérdések egyéni válaszait is megmutatja. A „mentor … nem látja” állítás ezért hamis.
- **Bizonyíték:**
  - Manifest: „activity-szintű role override vonja el a `mod/quiz:viewreports`-ot: a mentor a tételszintű egyéni válaszokat alapból nem látja”.
  - Moodle `MOODLE_405_STABLE`, `mod/quiz/report/grading/db/install.php`: `$record->capability   = 'mod/quiz:grade';`.
  - `mod/quiz/report/reportlib.php`, `quiz_report_list()`: a `mod/quiz:viewreports` csak akkor az alapértelmezés, ha a riportnak nincs saját capabilityje: `if (empty($capability)) { $capability = 'mod/quiz:viewreports'; }`.
  - `grading/report.php`: `require_capability('mod/quiz:grade', $this->context);` és `$includeauto = optional_param('includeauto', false, PARAM_BOOL);`.
  - `mod/quiz/db/access.php`: `'mod/quiz:grade'` archetípusai között ott van a `'teacher' => CAP_ALLOW`.
- **Hatás:** a GYV-23 / D-11 adatvédelmi kikötése technikailag nem teljesül. A saját csoportjában a mentor tételenként, név szerint látja a belépőkvíz válaszait (`quiz/grading:viewstudentnames`).
- **Javaslat:** az LMS-M0-06 override terjedjen ki a `mod/quiz:grade`-re is; rögzíteni kell a `quiz/grading:viewstudentnames` állapotát; a manifest és az Adatvédelem mondata ehhez igazodjon. A 15. pontba kerüljön kifejezett negatív teszt: Results → Manual grading → „Also show questions that have been graded automatically”, valamint közvetlen URL-lel `mod/quiz/report.php?mode=grading`.
  - Javítási korlát: a statisztikai riport kérdése stagingtétel marad, a GYV-23 tartalmához nem nyúlunk.
- **Típus:** objektív
- **Verdikt:**

**QA17-IMPL-3**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:**
  - `02 Tervezet/Adatvédelem – tanulói adatok és AI.md` > §3 mechanizmus, utolsó pont
  - `02 Tervezet/LMS – activity manifest.md` > §1 FORUM-C; §2 LMS-M0-05
- **Probléma:** a diff a kurzus „Group mode” beállítását „Separate groups”-ra állítja, és kimondja, hogy a FORUM-C láthatósága ettől nem változik. A FORUM-C profilja és az LMS-M0-05 sora azonban nem rögzíti a fórum csoportmódját, a kurzusszintű érték pedig az új activityk alapértéke.
- **Bizonyíték:**
  - Adatvédelem: „a „Force group mode” „No” marad, így minden activity a saját, a buildben rögzített csoportmódját tartja, és a FORUM-C kurzusszintű láthatósága … nem változik”.
  - MoodleDocs 4.5, Groups: „The group mode defined at the course level is the default mode for all activities defined within that course.”
- **Hatás:** ha a fórum a kurzusbeállítás után készül, alapból „Separate groups” lesz. A tanulók csak a saját mentor-csoportjuk posztjait látják, ami ellentmond a „kurzusrésztvevők látják” szabálynak és a tanulói tájékoztatónak.
- **Javaslat:** a FORUM-C profilba (és az LMS-M0-05 sorába) kerüljön be: „Group mode” = „No groups”, stagingben visszaolvasva. A hat profilon kívüli többi activity csoportmódját is érdemes kifejezetten rögzíteni.
- **Típus:** objektív
- **Verdikt:**

**QA17-IMPL-4**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – activity manifest.md` > §8 BSPEC-06 sor
- **Probléma:** a diff a BSPEC-01, -02 és -05 sort kiegészítette, a BSPEC-06-ot nem. Ott az LMS-M2-01 továbbra is az „IMPL-6 korlátjára” mutat („ne a követett activityben fusson”), az új H5P-C cella és az LMS-M2-01 sor viszont a követett CP interakció nélküli diáját írja elő (D-15 (e)).
- **Bizonyíték:**
  - BSPEC-06: „LMS-M2-01: IMPL-6 korlátja”.
  - IMPL-6 a validált findingok között (`2026-10-05 Validált findingok – MAN completion és mentor-láthatóság.md`): „csak az köthető ki, hogy az identitás-kör kérdése ne a követett activityben fusson”.
  - Új H5P-C cella: „az identitás-kör kérdése a követett CP interakció nélküli reflexiós diája”.
- **Hatás:** a build-spec nyilvántartás a megszűnt megvalósítási korlátra mutat, a fejlesztő két ellentétes utasítást kap.
- **Javaslat:** a BSPEC-06 kapjon kiegészítést (2026-10-13, D-15 (e), PRG-9 b): LMS-M2-01 = a követett CP interakció nélküli diája, az IMPL-6 korlát ezzel módosult, a sor állapota nem változik.
- **Típus:** objektív
- **Verdikt:**

**QA17-IMPL-5**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:**
  - `02 Tervezet/LMS – H5P runtime acceptance.md`: nincs hozzá pont
  - Hivatkozik rá: `02 Tervezet/Emberi jóváhagyás szükséges.md` > 15. szakasz D-15; `02 Tervezet/LMS – activity manifest.md` > LMS-M4-05, LMS-M0-05
- **Probléma:** a D-15 szerint mindhat build-spec tételt külön kell tesztelni. A runtime acceptance a (c) és az (f) tételhez nem hoz tesztlépést:
  - (c): az LMS-M4-05 rubrikájánál a tanuló a szintleírást látja, a pontot nem; a 26. pont csak az LMS-M1-05-öt nézi.
  - (f): az LMS-M0-05 zárt állapota (rejtett, semmi nem hivatkozik rá) és az új kohorsz kurzusteljesítési kritériuma.
- **Bizonyíték:**
  - HUM D-15: „Mindegyik külön tesztelendő.”
  - LMS-M4-05: „a rejtés Moodle-beállításának nevét stagingben kell igazolni”. A RA-ban az LMS-M4-05 csak a 19. pontban szerepel, ott is csak a javító beadás miatt.
- **Hatás:** a két lezárt döntés megvalósítását nem igazolja tesztlépés, így a G3-bizonyíték hiányos marad.
- **Javaslat:**
  - A 26. pont terjedjen ki az LMS-M4-05-re: tanulói fiókkal a szintleírás és a komment látszik, a szintpont és a végső pont nem; rögzíteni kell a beállítás nevét.
  - Új alpont az LMS-M0-05 beállítás-visszaolvasásához: zárt állapotban rejtett, nincs rá mutató hozzáférési feltétel és kurzusteljesítési kritérium; megnyitás után csak az új kohorsz kurzusában kritérium.
- **Típus:** objektív
- **Verdikt:**

**QA17-IMPL-6**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:**
  - `02 Tervezet/LMS – activity manifest.md` > §2 LMS-M7-07, Review options
  - `02 Tervezet/LMS – H5P runtime acceptance.md` > 19. pont, utolsó alpont
- **Probléma:** a D-23 átvezetésében két Moodle-állítás pontatlan:
  - (a) A Review options alóli kivételhez a `moodle/grade:viewhidden` önmagában nem elég, a `mod/quiz:viewreports` is kell.
  - (b) A „During the attempt” oszlopot az Adaptive mode és az Adaptive mode (no penalties) viselkedés is engedélyezi, ezeket a lista kihagyja.
- **Bizonyíték:**
  - (a) Manifest: „a `moodle/grade:viewhidden` jogú szerepekre a beállítás nem vonatkozik”. `MOODLE_405_STABLE`, `mod/quiz/locallib.php`, `quiz_get_review_options()`: `has_capability('mod/quiz:viewreports', $context) && has_capability('moodle/grade:viewhidden', $context)`.
  - (b) A `question/behaviour/deferredfeedback/behaviourtype.php` `get_unused_display_options()` metódusa a `'correctness', 'marks', 'specificfeedback', 'generalfeedback', 'rightanswer'` listát adja vissza. A `qbehaviour_adaptive_type` ilyen metódust nem definiál.
- **Hatás:** kicsi: a beállítás-mátrix helyes, és a teszt tisztán tanulói fiókkal fut. A szerepmátrix és a viselkedésválasztás leírása viszont félrevezető.
- **Javaslat:**
  - (a) „a `mod/quiz:viewreports` és a `moodle/grade:viewhidden` jogot együtt birtokló szerepekre”.
  - (b) A felsorolásba kerüljön be az „Adaptive mode” és az „Adaptive mode (no penalties)”, vagy általánosabban: „csak azonnali visszajelzést adó viselkedésnél”.
  - Javítási korlát: a mátrix értékei nem változnak.
- **Típus:** objektív
- **Verdikt:**

Amit ellenőriztem, és rendben találtam:
- **LMS-M3-08 hivatkozásai:** a §1 GATE-CP és ASSIGN-M, a §2 (M3-05/06/07/08), a §4 M3 sora, a kurzusteljesítési lista és a „Fontos” utáni bekezdés, a §7 kapuablak és a `M3_QUIZ`, a BSPEC-01, a RA 8 és a M3 KAPU teljes és egymással egyező.
- **LMS-M6-05 rubrika-beállítása:** a `lockzeropoints`-os képlet (`max($mingrade, $curscore / $scores['maxscore'] * $maxgrade)`) és a 4.5-ös felirat szó szerint helyes, a 15-ös maximum mellett a pont a nyers rubrikaösszeg.
- **Review options űrlapja:** a `disabledIf($field . 'closed', 'timeclose[enabled]')` és a „Maximum marks” → „Marks” függés a 4.5 `mod_form.php`-ban igazolt.
- **RA 16:** a `multichoicerated` kötelező-szabálya (üres vagy „Not selected” nem küldhető be) a 4.5 forrásban igazolt.
- **RA 15:** a `setup_groups()` / `groups_get_course_groupmode` állítás helyes, a `mod_h5pactivity` támogatja a `FEATURE_GROUPS`-ot.
- **M2.1 SLIDE 4, Z.3, Z.4:** nem találtam implementációs hibát.

Források (Moodle és H5P, 2026-10-13):
- https://raw.githubusercontent.com/h5p/h5p-branching-scenario/master/src/scripts/libraryScreen.js
- https://raw.githubusercontent.com/h5p/h5p-branching-scenario/master/semantics.json
- https://raw.githubusercontent.com/h5p/h5p-branching-question/master/branchingQuestion.js
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/report/grading/db/install.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/report/reportlib.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/report/grading/report.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/db/access.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/locallib.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/mod_form.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/question/behaviour/deferredfeedback/behaviourtype.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/question/behaviour/adaptive/behaviourtype.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/grade/grading/form/rubric/lib.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/grade/grading/form/rubric/lang/en/gradingform_rubric.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/feedback/item/multichoicerated/lib.php
- https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/grade/report/lib.php
- https://docs.moodle.org/405/en/Groups

## C. Nyers lencse-kimenet – értékelés

#### QA17 – értékelés lencse, célzott QA (diff-fix1, AP-2026-10-13-01)

A koordinátor kérésére itt lezártam az ellenőrzést. 3 findingot találtam, egy P1-est és két P2-est.

**QA17-ERT-1**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md:51` (és :50, :52); `02 Tervezet/LMS – activity manifest.md:105` (LMS-M7-07)
- **Probléma:** A diff új szabályt vezet be: a javító próbálkozás után a mentor átbeszéli a kulcsot. Ez nincs benne a HUM 15 D-23 sorában, és a projektgazda szó szerinti irányában sem. A döntési csomagban csak a (3) opció része volt, ott is csak arra az esetre, „ha kötelező kvízzárás kell”. Közben a képző kézzel további próbálkozást nyithat ugyanarra a 14 itemre.
- **Bizonyíték:** :51 „a kulcsot a javító próbálkozás után a mentor beszéli át a madrihhal (projektgazdai döntés, 2026-10-13, D-23; ERT-5)”; :50 „további próbálkozást a képző nyit kézzel”; :52 „(a javító próbálkozás miatt ne legyen megjegyezhető a sorrend)”
- **Hatás:** A kulcs átbeszélése után egy kézzel nyitott újabb próbálkozás emlékezetből is teljesíthető, a blokkoló gyermekvédelmi Q13 is. A bank csak kevert, változata nincs. Így az LMS-M7-09 és az LMS-M7-08 „Teljesítve” lehet igazolt elsajátítás nélkül. A szabály a kohorszon belüli kulcsszivárgást is visszahozza, pedig a D-23 éppen ezt zárta ki.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős, a D-23 vétó/QA-szerepe): (1) marad-e a mentori kulcs-átbeszélés; (2) ha marad, csak a tanuló utolsó próbálkozása után jöhet, vagy további kézi próbálkozást csak validált itemváltozattal lehet nyitni. Döntésig a két mondatrész a HUM 15 D-23 szövegéhez igazítható, vagyis törölhető. Javítási korlát: a Review options mátrixa, a ≥12/14 küszöb, a Q13 blokkoló státusza és a „Grade to pass” negatív teszt nem változik.
- **Típus:** emberi-döntés
- **Verdikt:** —

**QA17-ERT-2**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépéstérkép.md:383` és `:385`
- **Probléma:** A D-03 szerinti, esetenkénti visszahozás (:383) ellentmond a változatlanul hagyott szomszédos sornak (:385).
- **Bizonyíték:** :383 „az esetet feldolgozó egyik csoport ismerteti az elemzését, a másik kiegészíti”; :385 „Minden csoport **ismerteti az elemzését**, nem jelenetet mutat be.”
- **Hatás:** Négy–hat csoportnál a képző a :385 alapján minden csoporttal teljes ismertetést tarthat. Így a „3 eset → kb. 12 perc” idő túlfut, és a lépéstérkép csúszik, holott a D-03 éppen ezt kezelte.
- **Javaslat:** A :385 alanyát kell igazítani, a védelmet megtartva, pl. „Az ismertetés elemzés, nem jelenet: senki nem mutat be jelenetet.” A :386 szerepjáték-tilalma, a „kb. 3–4 perc / eset” és a „12 perc” nem változik.
- **Típus:** objektív
- **Verdikt:** —

**QA17-ERT-3**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** `02 Tervezet/LMS – activity manifest.md` > §2, LMS-M4-05
- **Probléma:** A D-15 (c) szerint a rubrika az LMS-M4-05-ön rögzül, és a sor az LMS-M2-05 mintájára hivatkozik. A mintától eltérően azonban nincs megadva a Grade type, a Maximum grade és a szintpontok. A kánoni M4-rubrikának nincs pontértéke, a Moodle-rubrikához viszont pontos értékelés és szintenkénti pont kell (MoodleDocs „Rubrics”; élőben nem ellenőriztem).
- **Bizonyíték:** LMS-M4-05: „a tanuló a rubrika szöveges szintleírását és a kommentet látja, a szintpontot és a végső pontszámot nem”. LMS-M2-05: „Grade type: Point, Maximum grade = 8 (csak build-paraméter…)”. M4 hub :131: „nincs fix pontszám”.
- **Hatás:** A rubrika a megadott beállításokkal nem építhető fel, a builder pedig magától találna ki pontértéket egy vétólistás rubrikához.
- **Javaslat:** EMBERI DÖNTÉS (build-spec gazda, azaz a projektgazda; QA: értékelési felelős): Grade type, Maximum grade és a három szint pontja, kizárólag build-paraméterként, a tanuló elől rejtve, küszöb és completion-hatás nélkül. Az LMS-M4-10 CONFIRMED-feltétele és az „Alapszint / rendben” formatív státusza nem változik.
- **Típus:** emberi-döntés
- **Verdikt:** —

##### Fájlonként, mit ellenőriztem
- **`Emberi jóváhagyás szükséges.md`:** a 15. szakasz D-03, D-15, D-16, D-19, D-23 sorait vetettem össze a projektgazdai iránnyal és a döntési csomaggal.
- **`LMS – activity manifest.md`:**
  - QUIZ-M, ASSIGN-M és GATE-CP profil;
  - az LMS-M3-05…08, LMS-M4-05/10, LMS-M6-05, LMS-M7-07/09, LMS-Z-03/04/08 sorok;
  - a §4 M3-sora és a kurzusteljesítés;
  - a §7 M3_QUIZ, M7_QUIZ és BSPEC-01.
  - Eredmény: a kapu konjunktív marad; a kvíz bármely beírt LMS-M3-08 értékkel nyílik, érték nélkül nem; az M3 completion-változás jelölt; a kulcs és a küszöb nem változott.
- **`LMS – H5P runtime acceptance.md`:** a 8. pont M6-esete és az LMS-M3-08 mátrixa; a 16. pont D-16 negatív tesztje; a 19. pont M7 Review options-teszte (az ERT-5, az ERT-40 és a D-23 összhangban van, az M3 változatlan).
- **M3 KAPU (:37, :335):** a kvíznyitás bármely értékkel, az LMS-M3-08 hivatkozása; a küszöb változatlan.
- **M3.B:** a D-03 kártya- és időkezelése (ERT-2).
- **M3.A:** a kártya-duplikálást ellenőriztem. A zárókör „nem rövidítem” változását csak észleltem, értékelés lencsével nem minősítettem (PRG-1).
- **M4.1:** az ILO 2 és a mikrocél „felismeri”-szűkítése megfelel a D-19 (b)-nek; a hub és a Program terv tükörszövege nem ütközik.
- **M6 KAPU:** a D-15 (d) beállítás; a rubrikapontok (1/2/3) és a küszöb nem változtak.
- **M7 KAPU (:51, :415):** a D-23-mátrix (ERT-1).
- **Z.4 és Z.3:** a D-16 „beadás egésze” és a D-15 (b) jelölt; a Z hub :185 összhangban van.

##### Nem ellenőriztem
- `Adatvédelem – tanulói adatok és AI.md` (D-11);
- `Gyermekvédelem – release gate.md`, `RELEASE-READINESS.md` (D-06);
- M0 hub, M0.4, M0.A, M1.F, M2 KAPU, M2.1, M2.A: ezeket csak átfutottam, nem ellenőriztem;
- M3.3 (D-08 (b));
- M7.B (D-22);
- a Moodle 4.5 feliratait és viselkedését élőben (lockzeropoints, „Maximum marks”, a disabledIf mentett értéke).

## C. Nyers lencse-kimenet – nyelv

QA17-NYELV: célzott nyelvi QA a diff-fix1.txt `+` soraira

Lefedettség: a diff mind a 24 `02 Tervezet/` fájljának `+` sora. 14 findingot találtam, ebből 1 db P1 és 13 db P2.

---

**QA17-NYELV-1**
- Súlyosság: P2 · Bizalom: magas · Lencse: nyelv
- Hely: `02 Tervezet/Emberi jóváhagyás szükséges.md:804` (D-16)
- Probléma: egybeírási hiba. A számnév + -s képzős melléknév egybeírandó („háromrészes”). A korpusz mindenhol egybeírja: manifest LMS-Z-08, Z.4 :262/:278/:310/:347, M2.4 :590.
- Bizonyíték: „a három részes szerkezet formatív útmutató”
- Hatás: helyesírási hiba és írásmód-eltérés a kánoni döntési helyen.
- Javaslat: OLD `a három részes szerkezet` → NEW `a háromrészes szerkezet`. Ugyanez a hiba áll a :708-ban is, de az a diffen kívül esik: csak jelzem, nem a diff része.
- Típus: objektív · Verdikt: —

**QA17-NYELV-2**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/Emberi jóváhagyás szükséges.md:799` (D-08 (b), jobb oszlop)
- Probléma: rossz szóválasztás. A „terhelő” elsődleges jelentése ’inkrimináló’ vagy ’súlyosító’ (terhelő bizonyíték, terhelő körülmény). A forrásjavaslat „nem megterhelő-e maga a cím”, és az M3.3 új bekezdése is „megterhelő”-t mond.
- Bizonyíték: „Memuna (QA: a cím terhelő-e).” – az M3.3 :78 sorában: „hogy a cím nem megterhelő-e, a Memuna QA-ja dönti el”
- Hatás: a Memunának szóló QA-kérdés félreolvasható, és a két kánoni hely más szót használ ugyanarra.
- Javaslat: OLD `a cím terhelő-e` → NEW `a cím megterhelő-e`. A scratchpad Memuna-csomagja (`pkg/Memuna.md:34`) ugyanezt örökli: frissítendő.
- Típus: objektív · Verdikt: —

**QA17-NYELV-3**
- Súlyosság: P2 · Bizalom: magas · Lencse: nyelv
- Hely: `02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md:604`
- Probléma: névmási zuhanás (3. regressziós minta). A beszúrt tagmondat miatt a „rajta” legközelebbi előzménye már „a saját fiókjával”, nem a tartalék eszköz.
- Bizonyíték: „mindenki a saját fiókjával dolgozik; rajta jelszót menteni és személyes munkapéldányt hagyni tilos”
- Hatás: a képző a tilalmat a fiókra értheti, nem az eszközre (képzői utasítás).
- Javaslat: OLD `dolgozik; rajta jelszót menteni` → NEW `dolgozik; az eszközön jelszót menteni`
- Típus: objektív · Verdikt: —

**QA17-NYELV-4**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/Emberi jóváhagyás szükséges.md:797` (D-03); `02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépéstérkép.md:383`
- Probléma: az „esetenként” köznyelvi jelentése ’alkalmanként, néha’, itt viszont ’esetről esetre’ értendő. Ezen felül az M3.B mondata úgy fogalmaz, mintha minden esetet két csoport dolgozna fel, holott a :366 szerint négy csoportnál csak egy eset van két példányban. (A :366 a szerkesztés utáni állapot sora; régi számozással :353.)
- Bizonyíték: HUM: „visszahozás esetenként”. M3.B: „Négy vagy több csoportnál is esetenként haladj: az esetet feldolgozó egyik csoport ismerteti az elemzését, a másik kiegészíti”
- Hatás: a felolvasott instrukció félreérthető („néha haladj”), és a „másik csoport” nem létezik a nem duplázott eseteknél.
- Javaslat: M3.B: OLD `is esetenként haladj: az esetet feldolgozó egyik csoport` → NEW `is esetről esetre haladj: ahol két csoport dolgozta fel ugyanazt az esetet, az egyik csoport`. HUM: OLD `visszahozás esetenként` → NEW `visszahozás esetről esetre`. A :383 második mondatának „esetenként két kérdésre” fordulata (’esetenként’ = ’egy-egy esetnél’) régi szöveg, maradhat.
- Típus: objektív · Verdikt: —

**QA17-NYELV-5**
- Súlyosság: P2 · Bizalom: magas · Lencse: nyelv
- Hely: `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md:415`
- Probléma: rossz igenév. A „készülő” jelentése ’folyamatban lévő’, a szöveg viszont egy létrehozott felülbírálásról szól. Ugyanerre a fogalomra a kánon máshol „a javító próbálkozást nyitó felhasználói felülbírálás” alakot használ: M7 KAPU :51, manifest LMS-M7-07, runtime :96.
- Bizonyíték: „a javítóhoz készülő felhasználói felülbírálás zárási ideje a javító határideje”
- Hatás: terminológiai széttartás egy QA-checklistben.
- Javaslat: OLD `a javítóhoz készülő felhasználói felülbírálás` → NEW `a javító próbálkozást nyitó felhasználói felülbírálás`
- Típus: objektív · Verdikt: —

**QA17-NYELV-6**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md:400`
- Probléma: az értelmező a „működését” tárgyat a „negatív tesztjét” szóval azonosítja, így a mondat szó szerint azt mondja, hogy a tesztet kell tesztelni.
- Bizonyíték: „A „kiürítés” valós működését – az üres kötelező beküldés negatív tesztjét: … – stagingben tesztelni kell”
- Hatás: zavaros stábinstrukció.
- Javaslat: OLD `negatív tesztjét:` → NEW `negatív tesztjével:`
- Típus: objektív · Verdikt: —

**QA17-NYELV-7**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `02 Tervezet/LMS – H5P runtime acceptance.md:96` (19. pont, M7 pozitív esetek)
- Probléma: az utolsó tagmondatból hiányzik az állítmány. Pontosvessző és egy közbeékelt „vissza kell olvasni, hol jelenik meg …” után a hiányzó ige nem a „látja”-ra, hanem a legközelebbi „vissza kell olvasni”/„látszik” igére olvasódik.
- Bizonyíték: „…mi látszik a felülbírálás zárási ideje után; a hibázott kompetenciát vagy kritikus követelményt pedig az LMS-M7-09 visszajelzés-mezőjében, kulcs nélkül.”
- Hatás: a tesztelő nem tudja biztosan, mi a várt pozitív eredmény.
- Javaslat: OLD `visszajelzés-mezőjében, kulcs nélkül.` → NEW `visszajelzés-mezőjében látja, kulcs nélkül.`
- Típus: objektív · Verdikt: —

**QA17-NYELV-8**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/Emberi jóváhagyás szükséges.md:821` (D-13 (b), (c), (d))
- Probléma: hiányzik az alaptag (1. regressziós minta). A felsorolás első tagjának van feje („besorolása”), a másodiknak nincs. A forráskérdés: „kerüljön-e az M2.A:177 és :410 csoportos normájába »és felismerhető részlettel sem«”.
- Bizonyíték: „az M2.A csoportnorma a felismerhető részletre”
- Hatás: a nyitott tétel tárgya nem olvasható ki a kánoni sorból.
- Javaslat: OLD `az M2.A csoportnorma a felismerhető részletre` → NEW `az M2.A csoportnormájának kiterjesztése a felismerhető részletre`
- Típus: objektív · Verdikt: —

**QA17-NYELV-9**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/Emberi jóváhagyás szükséges.md:781` (15. szakasz bevezetője)
- Probléma: vonzathiba. A „sorol” igét nem a ’vminek’ vonzattal használjuk (vagy „vmi közé sorol”, vagy „vminek minősít”).
- Bizonyíték: „a független ellenőrzés (verifier) a tételt nem sorolta szerepköri döntésnek”
- Hatás: nem magyaros mondat a kánoni döntési helyen.
- Javaslat: OLD `nem sorolta szerepköri döntésnek` → NEW `nem sorolta a szerepköri döntések közé`
- Típus: objektív · Verdikt: —

**QA17-NYELV-10**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `02 Tervezet/Modulok/M2/Peulák/M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md:254`
- Probléma: tartalomvesztés (9. regressziós minta). Az átírás kiejtette a „körbenézzenek” lépést, a :271 lezárás viszont továbbra is erre épít.
- Bizonyíték: :254: „hagyj időt, hogy elhelyezkedjenek – … –, és néhány más állításnál legyen 1–2 rövid reflexió”. :271: „Ha körbenéztek, látszik, hogy mindenki máshol áll”
- Hatás: a képzői instrukció és a lezáró szöveg széttart.
- Javaslat: OLD `saját papírjukon –, és néhány más állításnál` → NEW `saját papírjukon –, körbenézzenek, és néhány más állításnál`. Ha a kihagyás szándékos volt, akkor a :271-et kell igazítani, de ezt a modulgazda dönti el.
- Típus: objektív · Verdikt: —

**QA17-NYELV-11**
- Súlyosság: P1 · Bizalom: magas · Lencse: nyelv
- Hely: `…/M7 – Kapu – értékelő (item-bank + rubrika).md:51`; `02 Tervezet/LMS – activity manifest.md:105` (LMS-M7-07)
- Probléma: kitalált szabály (8. regressziós minta), amely ugyanazon a helyen önmagának is ellentmond. A forrásjavaslat (3) opciója „a mentor beszéli át az itemeket” volt. A kánonban ebből „a kulcsot … beszéli át” lett, ugyanabban a bekezdésben, ahol „a kulcs felfedése nélkül” áll. A HUM 15 D-23 sora egyiket sem tartalmazza. Átfedés: QA17-ERT-1 (MEGERŐSÍTVE), ugyanazzal a javítással.
- Bizonyíték: M7 KAPU :51: „a kulcsot a javító próbálkozás után a mentor beszéli át a madrihhal (…, D-23; ERT-5)”. Ugyanott: „a mentor szabályos javítási útmutatást ad, a kulcs felfedése nélkül”
- Hatás: a mentor ellentmondó utasítást kap a kulcs kezeléséről.
- Javaslat: a QA17-ERT-1 OLD → NEW cseréje (M7 KAPU :51 és manifest :105). Csak ezen a két mondatrészen.
- Típus: objektív · Verdikt: —

**QA17-NYELV-12**
- Súlyosság: P2 · Bizalom: közepes · Lencse: nyelv
- Hely: `…/Emberi jóváhagyás szükséges.md:800` (D-11); `…/LMS – H5P runtime acceptance.md:87` (15. pont); `…/Adatvédelem – tanulói adatok és AI.md:116` (QUIZ-D/M sor); `…/LMS – activity manifest.md:70` (LMS-M3-06) és `:314` (BSPEC-01)
- Probléma: írásmód és tipográfia. (a) Az „F-peula képző” alakból hiányzik az összetételi kötőjel; a manifest :31 helyesen „F-peula-képzői”. (b) A runtime :87 birtokos láncából hiányzik a -nak/-nek. (c) Három helyen két zárójel áll közvetlenül egymás után.
- Bizonyíték: „második értékelő és F-peula képző az ADV-2 szerint”; „az F-peula képzője hozzáférését”; „(activity-szintű role override, GYV-23) (projektgazdai döntés, 2026-10-13, D-11; …)”
- Hatás: írásmód-ingadozás és nehezebb olvashatóság a kánoni fájlokban.
- Javaslat: (a) OLD `és F-peula képző az ADV-2` → NEW `és F-peula-képző az ADV-2`. (b) OLD `az F-peula képzője hozzáférését` → NEW `az F-peula képzőjének hozzáférését`. (c) Az egymást követő zárójelek összevonása pontosvesszővel, például OLD `GYV-23) (projektgazdai döntés` → NEW `GYV-23; projektgazdai döntés`. A manifest :70 (`D-15 (a)) (§7:`) és :314 (`nem változik) (§2)`) ugyanígy javítandó.
- Típus: objektív · Verdikt: —

**QA17-NYELV-13**
- Súlyosság: P2 · Bizalom: alacsony · Lencse: nyelv
- Hely: `02 Tervezet/RELEASE-READINESS.md:38`
- Probléma: tautológia. A „szerep–szerepnév–szerepel” halmozás szó szerint üres állítás. A szándék valószínűleg a nyilvános repó névszabálya: személyek csak szerepnéven.
- Bizonyíték: „Az issue nyilvános: személyes adat nem kerül bele, a szerepek szerepnéven szerepelnek.”
- Hatás: a nyilvánossági szabály homályos.
- Javaslat: OLD `a szerepek szerepnéven szerepelnek` → NEW `az érintettek csak szerepnéven szerepelnek`
- Típus: objektív · Verdikt: —

**QA17-NYELV-14**
- Súlyosság: P2 · Bizalom: alacsony · Lencse: nyelv
- Hely: `…/M3.B – Red flag vagy nem – Esetelemzés & lépéstérkép.md:466` (4.3.3 cím)
- Probléma: az „új” törlése (D-03) után a „kívülről” elvesztette a viszonyítási pontját. Mivel a 4. eset már a peula saját kártyakészletének része, a cím ’fejből’ jelentésben is olvasható.
- Bizonyíték: „### 4.3.3. Gyors alkalmazás – a 4. eset kívülről (5–8’)”
- Hatás: kétértelmű lépéscím a képzőnek.
- Javaslat: EMBERI DÖNTÉS (M3 modulgazda): mire utal a „kívülről”, a 4.2-ben ki nem osztott esetre vagy másra. Szöveget erre nem javaslok.
- Típus: emberi-döntés · Verdikt: —

