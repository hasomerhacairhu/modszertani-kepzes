# Merge előtti átvételi review és vétó-jegyzék — next-version M0–Z (AP-2026-10-11-01)

- **Scope:** a `next-version/AP-2026-10-11-01` ág nagy hatású tartalmi változásai a `main@213a4c5` (a futó pilot forrása) óta, a `1d7b58d` állapoton (72 commit). Ez **nem új teljes audit**: csak azt vizsgálja, hogy a változások validált findingra vagy lezárt döntésre vezethetők-e vissza, és helyesek-e.
- **Fókusz (a projektgazda 2026-10-12-i kérése szerint):** az answer key jelentése, a disztraktorok és a visszajelzések; a completion- és unlock-logika; a rubrika értelmezése; a munkaterhelés, az időtartamok és a leadandók terjedelme; a gyermekvédelem és az eszkaláció; a személyes adatok és a megőrzés; az akadálymentességi alternatívák és a Moodle/H5P runtime-feltevések. Kifejezetten: az M5.1 időtartam-változás, az M7.4 leadandó-terjedelem, az M6 gyermekvédelmi változásai és az M3 kritikus itemeinek completion-megvalósítása.
- **Módszer:** három read-only specialista reviewer (értékelés, implementáció, biztonság-jog) a tartalmi diffen (a generált médiakimenetek nélkül), a ledger FIXED-soraival, a validált és célzott QA-riportokkal és a lezárt döntésekkel. A fő session minden PR-BLOCKER- és KOCKÁZAT-állítást a fájlban és a ledgerben visszaellenőrzött. A vétó-jegyzéket gépi szkript állította elő a diffből (III. rész).
- **Read-only:** a review alatt a `02 Tervezet/` alatt semmi nem változott. Egyetlen ledger-pontosítás történt: az `M5:ERT-G1-3` sorában rögzítve lett a KAPU:196 szándékos kihagyása (HIR-ERT-1).

## I. Eredmény

**0 megerősített PR-BLOCKER.** Az implementációs reviewer egyetlen BLOCKER-jelöltje (HIR-IMPL-1, M0.2:11) téves riasztás volt: a ledger `M0:ERT-9` sora kifejezetten lefedi („:11 (típuslista)”).

| Fókuszpont | Eredmény | Finding / döntés |
|---|---|---|
| M5.1 időtartam | OK, a korláton belül: a fejlesztői időösszeg 10–15 → 15–20 perc, a lecke metája (:7) és a hub (:41) szerint; a 3,5 óra nem változik. Nyitott: a részidők összege 9–13 perc, ellentmondás a fejlesztői checklisten belül | `M5:PED-G1-7`; nyitott: `M5:QA-PED-2` (X-10) |
| M7.4 leadandó-terjedelem | OK: „3–8 soros” → „összesen kb. 10–20 soros”, egyezik az M7.4:772-vel; az új önállómunka-becslések (30–45, 105–160 perc) a hub saját számaival egyeznek | `M7:PED-G2-6`, `M7:PED-G1-3` |
| M6 gyermekvédelem | Védelem nem tűnt el és nem gyengült. Jelzendő: a KAPU P1 ✅ A opciójában a Memuna bevonása feltételes lett (M6-NY-D3/D27 szerint, ezek még nincsenek a HUM-regiszterben); az M6.F:323 „a közös eszközön nem” finding nélkül került be (már nyitott) | `M6:BIZT-G1-2`, `-G1-3`, `-G3-3`, `-G2-1.obj`, `M6:IMPL-G3-1`, `M6:ERT-G1-5`; nyitott: `M6:QA-BIZT-1` |
| M3 kritikus itemek, completion | OK: a kézi kritikusitem-ellenőrzés a `GATE_CONFIRMED_M3` előtt, ≥10/12 ÉS Q2/Q4/Q7/Q9 változatlan; az M3.3 CP-csomópontjain „Hide summary slide” = be, a grade a végképernyőről; a SAFE-1 teszt az RA 11. pontjában. Tesztre utalt feltételek, nem igazolatlan állítások | `M3:IMPL-G2-3`, `M3:IMPL-G2-12`, `M3:ERT-G1-6`, BS-D1, MAN §4 |
| Answer key | A ✅ darabszáma és helye mind a 25 érintett diffblokkban változatlan; a kulcsopció szövege néhol változott (vétólista, II. és III. rész) | HIR-ERT-2 |
| Küszöb, kaputípus, completion-feltétel | engedély nélküli változás nincs | — |

**Nem blokkoló kockázatok** (a PR-ben jelezve; a HIR-IMPL-2/-3 javítása előtt verifier kell):

| ID | Hely | Kockázat | Minimális helyreállítás |
|---|---|---|---|
| HIR-ERT-1 | M5 KAPU:196 (Q8) | a stáboldali indoklás betűvel hivatkozik a kulcsra; ha a build tanulói visszajelzésbe teszi, keverés után rossz opcióra mutat | csak ha tanulóhoz kerül: „**Miért a B a helyes:**” → „**Miért a páros visszamondós játék a helyes:**” |
| HIR-ERT-3 | M7 KAPU:19, :44 | a fejlesztői kvízcím eltér a MAN:101 nevétől | a két címke a MAN:101 nevére |
| HIR-BIZT-1 | M3.F:387 | a név nélkül begyűjtött lapok visszaosztása keveredhet vagy azonosíthat (a verifier-korláton belül) | opcionális modulgazdai döntés (QA: DPO): marad, vagy a 2.1 témakérő cetlije (M3.F:63) |
| HIR-BIZT-2 | M6 KAPU:353 | a ✅ kulcsopció feltételes Memuna-bevonása; a forrásdöntés (M6-NY-D3/D27) nincs átvezetve a HUM-ba | a szöveg marad; a D3/D27 szó szerinti átvezetése a HUM-regiszterbe (governance-követő lépés) |
| HIR-IMPL-2 | M3 KAPU §2; MAN LMS-M3-05; RA 26 | az M3 kapurubrika tanulói láthatóságát egyetlen RA-pont sem teszteli | az RA 26 hatóköre „(LMS-M1-05, LMS-M3-05)”; a KAPU-mondat az RA 26-ra hivatkozzon |
| HIR-IMPL-3 | RA 11 SAFE-1 ↔ RA 24 | a 24. pont pozitív kontrollja miatt a SAFE-1 nem értékelhető, ha a BS-verzió nem folytat | félmondat: a SAFE-1-nél a folytatás eredménye rögzítendő, nem érvényességi feltétel; a BS-könyvtárverzió rögzítése |
| HIR-IMPL-4 | Z HUB:35 (= MAN:247) | a „Moodle felhasználói felülbírálás” a Feedbacknél talán nem elérhető; RA-pont nem fedi | runtime-kérdés az LMS-gazdának (G3b); szöveg nem változik |
| HIR-IMPL-5 | az egész ág ↔ CC-04 | a merge felülírná a futó pilot M0/M1 forrását | merge csak a pilot után vagy tételes freeze-kivétellel (projektgazda) |

## II. A három reviewer riportja (a fő session megjegyzéseivel)


### HIR-ERT — értékelés, munkaterhelés, rubrika (assessment-reviewer, read-only)

**Összefoglaló:** 0 PR-BLOCKER · 3 KOCKÁZAT · 6 MÁR NYITOTT · kb. 45 OK.

A kért fókuszpontok mindegyike megnézve: M5.1 időösszeg, M7.4 terjedelem, M7 HUB és M7.4 önállómunka-becslés, Z.A 3 perc, M7.A 3–4 pont, M4 PED-G2-3, M5 ERT-G1-3, M6 PED-G1-7, M7 Q1 és „Kérek”. Mind validált findingra vezethető vissza, és a javítási korláton belül marad. Answer key (✅ helye), küszöb vagy kaputípus engedély nélkül nem változott.

#### KOCKÁZAT

**HIR-ERT-1 · KOCKÁZAT · P2**
- **Hely:** `02 Tervezet/Modulok/M5/M5 – Kapu – értékelő (item-bank + rubrika).md:196` (Q8)
- **Probléma:** A Q8 indoklása betűvel hivatkozik a kulcsra („**Miért a B a helyes:**”), miközben a KAPU:23 a válaszsorrend keverését írja elő. Az M5:ERT-G1-3 verifier-korlátja (M5 validált riport, B. verdikt) szerint „A :196 („Miért a B a helyes”) csak akkor változik, ha tanulóhoz kerül”. A fix-terv úgy ítélte, hogy nem kerül tanulóhoz, mert nem „Visszajelzés” címkéjű. Ezért kimaradt. A ledger FIXED-sora ezt nem rögzítette. *(Fő session: a feltételes kihagyás a korláton belül van; a ledger-sor kiegészítve.)*
- **Hatás:** Ha a buildelő ezt az indoklást Moodle-visszajelzésbe teszi, keverés után a „B” más opcióra mutat.
- **Minimális helyreállítás (ha tanulóhoz kerül):** `**Miért a B a helyes:**` → `**Miért a páros visszamondós játék a helyes:**`. Kulcs, opció és Disztraktor-indok nem változik.

**HIR-ERT-2 · KOCKÁZAT · P2 · vétólista**
- A ✅ vagy elosztó opció szövegét érintő, engedélyezett változások. Szöveghez nem kell nyúlni, de a vétólistában tételesen meg kell nevezni őket:
  - M6 KAPU:353 (P1 ✅ A): „és ha valaki erősen érintett, még a peula alatt bevonom…” · M6:ERT-G1-5 (tartalmi; lásd HIR-BIZT-2)
  - M6 KAPU:233 (4. item ✅ B): „/ … +” → „vagy … és” · M6:NYELV-G1-12
  - M6 KAPU:296–299 (9. item, mind a négy opció): „→” → „; ezt” · M6:NYELV-G1-12
  - M7 KAPU:195 (Q11 ✅ D): „Megkérek” → „Kérek” · M7:NYELV-G1-3
  - M4.4:527 (1. elosztó cseréje) · M4:PED-G2-3
  - M0.2:264 belépőkvíz ✅ B („→” → „:”), M3.3:934 ✅ („red flag-eket” → „red flageket”): helyesírási.
  - M7.1:437 ✅ 2.: „ami tetszik” → „ami illik a kvucámhoz” · M7:ERT-G1-10 (fő session, a vétó-jegyzékből)

**HIR-ERT-3 · KOCKÁZAT · P2**
- **Hely:** `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md:19`, `:44`
- **Probléma:** Az M7:IMPL-G1-12 a tanulói helyeken átvezette a kvíz MAN:101 szerinti nevét („M7 – SMART & Zmán Kvucá kvíz (felkészültségi, a v2 előtt)”). A KAPU-fájl viszont a régi címkét viseli: „(A) ITEM-BANK – „SMART & Zmán Kvucá kvíz (felkészültségi)” (14 item)”.
- **Hatás:** Aki a kapufájlból buildel, eltérő activity-nevet adhat. Nem blokkoló, mert a tanulói szöveg és a MAN egyezik.
- **Minimális helyreállítás:** a két címke a MAN:101 nevére cserélődik, más nem változik. *(A M7 célzott QA ezt a fejlesztői címet a verifier-korlát szerint megengedettnek hagyta, lásd a modulközi riportot.)*

#### MÁR NYITOTT (ledger-kulcs)
- **M5:QA-PED-2** (BLOCKED_HUMAN, X-10): az M5.1:651–655 részidőinek összege 9–13 perc, a sor mégis „→ összesen 15–20 perc”. A PED-G1-7 javítás csak az összeget igazította a meta :7 és a HUB:41 szerint (korlát). A fejlesztői checklisten belül számtani ellentmondás maradt; tanulói szövegben nem jelenik meg.
- **M7:PED-G3-11 (c)**: az M7.A KART-01 „10–12 kártya” ↔ 5 megírt mondat (X-10).
- **M6:BIZT-G1-1**: a KAPU P1 helyszíni 18+ felnőttje (X-5).
- **M7:IMPL-G1-3**: a Q11/Q14 részpontozása, ≥80% ↔ ≥12/14 (X-6, X-11).
- **M7:ERT-G1-5**: a Q13 modified-Angoff küszöbe (EVIDENCE_GATE, X-9).
- **M5:NYELV-G1-11 / M6:ERT-G1-10**: nézőpont- és nyelvijel-kulcsárulás (X-6).

#### OK (egysoros, csoportonként)
**Munkaterhelés, idő, terjedelem:** M5.1:655 összeg 15–20 · M5:PED-G1-7 (korláton belül; nyitott rész: QA-PED-2) — M5 HUB:8 tényközlő félmondat · M5:PED-G1-7 — M7.4:548 „összesen kb. 10–20 soros” · M7:PED-G2-6 (= M7.4:772) — M7.4:12, :77, :857 „kb. 30–45 perc” · M7:PED-G2-6 (= HUB:118) — M7 HUB:148 „105–160 perc” · M7:PED-G1-3 (30–45 + 15–25 + 60–90) — M7.A:335 „3–4 megjelölt pont” · M7:PED-G3-11.obj (a 4 pont alapérték marad) — Z.A:214 „fejenként kb. 3 perc” · Z:PED-G1-6 (= :215) — M5.3:675 72 órás felidézés · M5:PED-G2-5 (= HUB:191, MAN:160).

**Kvíz- és kapuitemek:** M4.4:527 · M4:PED-G2-3 (a kettős kulcsot szünteti meg; ✅ 2. változatlan) — M4.4:62 · M4:QA-ERT-1 — M5 KAPU:69, :223, :241 · M5:ERT-G1-3 — M5.1:486, :538 · M5:ERT-G1-3 — M5 KAPU:313 · M5:IMPL-G1-2 — M5 KAPU:303 · M5:ERT-G1-5 — M5 KAPU:305 · IMPL-G1-3 — M5.1 SLIDE 3/4 visszajelzés · M5:PED-G1-4.obj — M6 KAPU:314 · M6:PED-G1-7 — M6 KAPU:216 · IMPL-G3-7; :119, :209 · ERT-G2-4, QA-NYELV-5; :365 · BIZT-G1-2; :347 · IMPL-G1-4, QA-IMPL-1; :22–23, :72 · IMPL-G1-3.obj; :384 · BIZT-G1-3; :416 · ERT-G1-4; :439 · PED-G1-6, QA-PED-1; :82, :148 · NYELV-G1-5; :263–266 · NYELV-G1-12 — M7 KAPU:71 · M7:ERT-G1-6 — M7 KAPU:195 · M7:NYELV-G1-3.

**Rubrika és kapuértelmezés:** M7 KAPU „nem nyílik” → „nem teljesül” · M7:NYELV-G1-9 (R4-logika és szintek változatlanok) — M7 KAPU „M6 complete” · M7:IMPL-G1-2 — M7 KAPU (C) „R4, R5 és R7” · M7:ERT-G1-13 — M7 KAPU R2 „kvuca-infó” · M7:NYELV-G2-1 — M7.4:845 küszöbsor · M7:ERT-G2-9 (= KAPU:20) — M7.4:704 · ERT-G2-9 — M7.4:702, :842 · IMPL-G1-12 — M7.4:731 · IMPL-G2-9 — M7.4:70 · ERT-G2-12 — M7.4:72 · NYELV-G2-7 — M7 HUB:173, :359 · ERT-G1-9; :381 · ERT-G1-8; :284 · PED-G1-12.obj; :144 · IMPL-G1-2 (b) — M2 KAPU:24 · M2:IMPL-G1-5; :37 · NYELV-G1-4; :58 · IMPL-G1-8 — M1 KAPU:132 · M1:NYELV-G2-7 (jelentés-helyreállítás).

#### Nem néztem meg (lépéskorlát)
- A tanulói leckék beépített kvízeinek opció- és visszajelzés-hunkjai: M7.1 (:309–456), M7.2 (:888–944), M7.3, M6.1/M6.2, M4.1–M4.3, M5.2, M5.4.
- M5.A, M5.B, M5.F; M7.B, M7.F; Z-leckék.
- A `diff-canon.patch` a ✅-sorokon túl; M0, M1, M3 a ✅-sorokon túl.
*(Fő session: a ✅-sorok teljes köre és a szám+mértékegység változások gépileg lefedve a vétó-jegyzékben.)*

### HIR-IMPL — completion/unlock, M3 kritikus itemek, a11y, runtime-feltevések (implementation-reviewer, read-only)

**Összefoglaló (a reviewer szerint):** 25 OK · 1 PR-BLOCKER · 4 KOCKÁZAT · 8 MÁR NYITOTT. **A fő session visszaellenőrzése után:** 26 OK · **0 PR-BLOCKER** · 4 KOCKÁZAT · 8 MÁR NYITOTT. A HIR-IMPL-1 téves riasztás, lásd lent.

A fókuszpontok rendben vannak: az M3 kritikus itemek és a blokkoló logika, az M3.3 Branching Scenario completionje és grade-je a CP-csomópontok „Hide summary slide” beállításával, a SAFE-1 teszt és a runtime acceptance (RA) 25. és 26. pontja mind validált findingra vezethető vissza. A runtime-állítások tesztre utalt feltételek, nem igazolatlan tényállítások.

Elsődleges forrásból ellenőrizve:
- h5p-multi-choice `semantics.json`: „Single Choice (Radio Buttons)”, „Randomize answers” alapérték true.
- Moodle MOODLE_405_STABLE:
  - assign.php: „Grant attempts” / „Manually” / „Allowed attempts” / „Unlimited”; „Require students to click the submit button”.
  - gradingform_rubric.php: „Allow users to preview rubric…”, „Show remarks to those being graded”, „Display points for each level to those being graded”.
  - quiz.php `shufflewithin_help`.
- h5p-branching-scenario master: `getCurrentState()` és `previousState` implementálva; a 2022-es #118 issue szerint verziófüggő.

#### HIR-IMPL-1 — a reviewer szerint PR-BLOCKER → a fő session szerint OK (téves riasztás)
- **Hely:** `02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrih, nem terapeuta – szerepek és elvárások.md:11`
- **Állítás:** a típuslistából kikerült a „Multi Choice”, és ezt egyik validált finding sem engedélyezi (az M0:QA-ERT-3 és a QA-IMPL-2 kizárja az M0.2:11-et).
- **Visszaellenőrzés (fő session):** a változás a `df2792d` commitból jön, és a ledger `M0:ERT-9` sora kifejezetten lefedi: „df2792d; M0.2:195, :199–203 (opciók a listából szó szerint, típus Multiple Choice egyválaszos), :11 (típuslista)”. Az M0:ERT-9 (= IMPL-6 b) validált korlátja: „kérdés és típus összhangban”. A SLIDE 2 már nem Multi Choice, ezért a típuslistából a nem létező elem közvetlen következményként esett ki. A QA-ERT-3 kizárása egy másik kérdésre vonatkozott (a „Single Choice” zárójeles magyarázatának átvitele). **Nincs teendő.**

#### KOCKÁZAT
**HIR-IMPL-2 · P2 · objektív (nem validált, követő tétel)**
- **Hely:** `02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md` §2 „LMS-eszköz”; `LMS – activity manifest.md` LMS-M3-05; `LMS – H5P runtime acceptance.md` 26. pont.
- **Probléma:** Az M3:ERT-G1-13 javítása tanulói tesztfiókos igazolást ír elő („runtime acceptance”), de egyetlen RA-pont vagy RT-sor sem fedi az LMS-M3-05-öt. Az RA 26 csak az LMS-M1-05-re szól.
- **Hatás:** Az M3 gyermekvédelmi kapu rubrikájának tanulói láthatóságát senki nem teszteli. A KAPU „pontos beállításnevek a célverzión” mondata ellentmond az RA 26-nak, ahol a nevek már rögzítettek.
- **Minimális helyreállítás:** az RA 26 hatóköre „(LMS-M1-05, LMS-M3-05)”, és a KAPU-mondat az RA 26-ra hivatkozik. Rubrika, pont és küszöb nem változik. Javítás előtt verifier kell.

**HIR-IMPL-3 · P2 · objektív (nem validált, követő tétel)**
- **Hely:** `LMS – H5P runtime acceptance.md` 11. pont „Szünet és visszatérés (SAFE-1)” ↔ 24. pont.
- **Probléma:** A SAFE-1 a 24. pont eljárására hivatkozik. A 24. pont érvényességi szabálya (ha nincs folytatás, ismétlés) ütközik a 11. pont „folytatja vagy elölről indítja – mindkettő rögzítendő” elvével. Ha a célverzió Branching Scenariója nem folytat, a teszt nem értékelhető.
- **Minimális helyreállítás:** egy félmondattal kimondani, hogy a 24. pont pozitív kontrollja itt nem érvényességi feltétel, csak rögzítendő eredmény, és rögzíteni a Branching Scenario könyvtárverzióját. Az M3.3 és a BSPEC-05 nem változik. Javítás előtt verifier kell.

**HIR-IMPL-4 · P2 · bizonyíték-kapu (G3b)**
- **Hely:** `02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md:35` (Z:PED-G1-1, szó szerint a MAN:247-ből); MAN §7 `Z_REFLECTION`, `Z_FEEDBACK`.
- **Probléma:** A Z és az M7 egyéni ütemezése „Moodle felhasználói felülbírálással” runtime-mechanizmusként szerepel, de RA-pont nem fedi. A reviewer szerint felhasználói felülbírálás csak Quiznél, Assignmentnél és Lessonnél van, Feedbacknél nincs. Ezt elsődleges forrásból nem ellenőrizte.
- **Javaslat:** Nem az ág hibája (a MAN:247 már így szól). A PR-ben jelezni kell. Runtime-kérdés az LMS-gazdának: mely Z/M7 activityknél van felülbírálás, és a Feedbacknek van-e zárási dátuma.

**HIR-IMPL-5 · P1 · emberi döntés (merge-időzítés)**
- **Hely:** `Emberi jóváhagyás szükséges.md` 13. szakasz (CC-04) ↔ az ág M0- és M1-változásai.
- **Probléma:** A lezárt CC-04 érvényben tartja az M0+M1 freeze-t („Freeze-kivételt csak tényleges P0 … hiba indokolhat”). Az ág M0- és M1-tartalmat módosít. Ha a mainre, a pilot forrására kerülne, felülírná a futó pilot M0/M1 forrását.
- **Javaslat:** A PR-ben ki kell mondani. Merge csak a pilot után, vagy a projektgazda tételes freeze-kivételével. Most nincs merge.

#### MÁR NYITOTT (ledgerkulcsok)
M3:IMPL-G2-4 (BS képek alt-szövege) · M3:IMPL-G2-5 (P1–P4 cím) · M3:BIZT-G1-7 (ITEM 10 kritikus-e) · M2:IMPL-G2-1 (LMS-M2-03 grade) · M2:BIZT-G2-2 (M2.4 SLIDE 5 passz-út) · Z:ERT-G1-7 (Z javító útjának időpontja) · M6:IMPL-G1-7 (Grade type / Maximum grade) · M1:BIZT-G2-2 (EVIDENCE_GATE, RT-P0-15).

#### OK (egysoros)
**Completion / unlock / BSPEC:**
- MAN §1 H5P-C „Hide summary slide” · M3:IMPL-G2-3
- M3.3:94 CP-1/2/3 · M3:IMPL-G2-3
- RA 11 pozitív eset · M3:IMPL-G2-3
- RA 11 SAFE-1 · M3:IMPL-G2-12
- RA 9, RA 25, RT-P0-25 · M0:ERT-2
- RA 26, RT-P0-26, MAN LMS-M1-05 · M1:QA-IMPL-3, M1:ERT-G2-6
- MAN ASSIGN-M · M1:QA-IMPL-2
- MAN LMS-M2-01 · M2:IMPL-G1-2
- LMS-M2-02 · M2:ERT-G2-2
- LMS-M2-05 · M2:IMPL-G1-6
- LMS-M3-04 · M3:BIZT-G2-1
- LMS-M3-05 · M3:ERT-G1-13
- LMS-M4-03 · M4:PED-G1-2.obj
- Z-hub :35 · Z:PED-G1-1
- M0.2:11 típuslista · M0:ERT-9 (fő session)

**M3 kritikus itemek:**
- KAPU §0 belépő feltétel · M3:ERT-G1-6
- Item-randomizálás · M3:IMPL-G1-4
- ITEM 10 · M3:ERT-G1-7
- 1.3 újraértékelés · M3:PED-G1-1 (BS-D2)
- ITEM 2/7/12 indoklásai · M3:PED-G1-8
- Komponens A és §2.3 unlock: kézi kritikusitem-ellenőrzés a `GATE_CONFIRMED_M3` előtt. A ≥10/12 ÉS Q2/Q4/Q7/Q9 változatlan (MAN §4, BS-D1).

**Akadálymentesség:**
- M2.2/M2.3 SC 1.2.2/1.2.3 · M2:IMPL-G2-3
- HUM 10. szakasz Q-MED-2, Q-PED-4 (szó szerint a 2026-10-04 összesítőből)

**H5P típusok:** M7:IMPL-G1-4, M7:IMPL-G2-6, M0:QA-ERT-3, M0:XMOD-2, M6:NYELV-G2-2, Z:NYELV-G1-8, M2:NYELV-G2-10 (semantics.json).

#### Nem néztem meg
- Az M3.1/M3.2/M3.4/M3.A/M3.B és az M4–M7 lecke-diffek részletesen.
- Az alt-szövegek egyenkénti visszavezetése.
- Néhány hub-sor finding-ID-ja (tartalmilag egyezik a MAN-nal).
- A Moodle Feedback felülbírálásának elsődleges forrása.

### HIR-BIZT — gyermekvédelmi és adatkezelési változások (safety-policy-reviewer, read-only)

**Összefoglaló:** 0 PR-BLOCKER · 2 KOCKÁZAT · 5 MÁR NYITOTT · 18 OK.

A fókuszban egyetlen védelem sem tűnt el, és egyik sem gyengült. Feltételessé egy vált: a KAPU P1 A opciójában a Memuna bevonása; ez a lezárt projektgazdai küszöböt követi (HIR-BIZT-2). Új, a kánonban nem szereplő szabály egy került be: az M6.F:323 „a közös eszközön nem” tilalma, és ez már BLOCKED_HUMAN (M6:QA-BIZT-1). (A reviewer eszközei: Read/Grep/Glob; a main-beli előzményt a patch `-` soraiból olvasta.)

#### KOCKÁZAT

**HIR-BIZT-1 · KOCKÁZAT · P2 · bizalom: közepes**
- **Hely:** `02 Tervezet/Modulok/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyermekvédelem (Study Lab).md:387`
- **Probléma:** A „Név nélküli mód” új mondatot kapott: a begyűjtött, név nélküli lapok visszakerülnek a résztvevőkhöz. Név nélküli lapot nem lehet biztosan a gazdájához visszajuttatni. A lapokon gyermekvédelmi kérdések állnak, így szétosztáskor keveredhetnek, vagy a kézírásból azonosíthatók.
- **Bizonyíték:** main: „…felírod a táblára a kulcsterületeket… „Storming vs. bántalmazás?”).”; most: „A lapok utána visszakerülnek a résztvevőkhöz, mert a felírt kérdéseiket és az „ezt pótolom” bejegyzéseiket a javító próbálkozás előtt is használják”.
- **Mire vezethető vissza:** M3:BIZT-G3-10. A verifier korlátja (M3 validált riport, B. verdikt) szerint „A visszaadás csak a fájl saját feltételezéséből vezethető le (:50; a MUNK-01 spec „ezt pótolom…” bejegyzései), új eljárást nem kap”. A javítás tehát a korláton belül van. Ugyanakkor az IMPL-G3-13 verdiktje szerint, ha a modulgazda a témakérő cetlire váltana, az EMBERI DÖNTÉS (M3 modulgazda; QA: DPO).
- **Javaslat:** Nem blokkoló. A PR-ben jelezni kell. Opcionális modulgazdai döntés: maradjon-e a név nélküli lapgyűjtés és a visszaadás, vagy a 2.1 név nélküli témakérő cetlije (M3.F:63) váltsa fel.

**HIR-BIZT-2 · KOCKÁZAT · P2 · bizalom: közepes**
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:353` (P1 pool-item, A opció ✅)
- **Probléma:** A ✅ A opcióban a Memuna bevonása feltételessé vált („ha valaki erősen érintett”). Ez egyezik az M6.A:499, az M6.4:939 és a KAPU :361/:365 szövegével. Alapja az M6-NY-D3 és a D27 projektgazdai döntés, de ezek csak a `01 Fejlesztés/04 Audit/2026-10-04 Projektgazdai döntések – M6 nyelvi review.md` jegyzőkönyvben állnak. Az `Emberi jóváhagyás szükséges.md` datált szakaszaiban nincsenek átvezetve (Grep „M6-NY|M6 nyelvi review”: 0 találat).
- **Bizonyíték:** main: „…nem állítom reflektorfénybe az érintettet – és még a peula alatt bevonom a kijelölt Memunát”; most: „– és ha valaki erősen érintett, még a peula alatt bevonom a kijelölt Memunát”. D27: „A D1 kiváltó feltétele és a Memuna bevonásának küszöbe ne változzon.”
- **Hatás:** Tartalmilag helyes, a validált M6:ERT-G1-5 fedezi. Az itemszár („könnybe lábad a szeme”) viszont a tanulóra bízza, hogy „erősen érintett”-e az illető.
- **Javaslat:** A szöveg maradjon. A PR-ben jelezni kell. A D3/D27 szó szerinti átvezetése a HUM-fájlba objektív governance-feladat („Hivatkozott, de még át nem vezetett döntés”), külön lépésben. Nem blokkolja ezt a PR-t.

#### MÁR NYITOTT (a ledgerben)
- **M6.F:323** — „papíron vagy a saját eszközén, a közös eszközön nem”: az M6:IMPL-G3-2 javítása közben került be. Validált finding vagy döntés nincs mögötte (forrása a verifier K24-korlátja). Ütközik az M6.F saját tartalék eszközével (:96–97) és az A11Y-17-tel. Kulcs: **M6:QA-BIZT-1** (BLOCKED_HUMAN, LMS-gazda + DPO, X-4; „a döntésig a tagmondat marad”). Ez az egyetlen engedély nélkül bekerült új szabály a fókuszban.
- **KAPU:365, M6.4:938** — a „felkavart kiskorút nem küldesz ki egyedül” rövid alakból hiányzik a GK:64 és a HUM:72 „kijelölt biztonságos hely” eleme: **M6:BIZT-G2-3 / G2-7** (EVIDENCE_GATE, Memuna).
- **Játéklap-adatmondat bővebb alakja** (KAPU:384, HUB:10, :208, M6.B:244, M6.B:32): **M6:QA-BIZT-2** (DPO).
- **M6.4:772** — a kirekesztés-szimuláció tilalmának második betoldása a szerepjáték-opcióhoz: **M6:BIZT-G2-1 / G2-2** (Memuna).
- **Z.3:305** — „nem vezetek éles foglalkozást, hanem jelzem a képzőnek” (kánonon kívüli eszkalációs szabály): **Z:BIZT-G1-1** (Memuna + programvezető).

#### OK (egysoros)
- M6 KAPU:365 kiülés-mondat · M6:BIZT-G1-2 (az M6.4:938 szó szerint; ✅ és opciók változatlanok)
- M6 KAPU:353 „ha valaki erősen érintett” · M6:ERT-G1-5 (lásd HIR-BIZT-2)
- M6 játéklap-adatmondat HUB:10, HUB:208, KAPU:384, M6.B:244 · M6:BIZT-G1-3 (az M6.B:32 szó szerint)
- M6.4:811 passz · M6:BIZT-G2-1.obj + M6:QA-NYELV-1 (a passzjog szó szerint marad)
- M6.A:509, :527 passz · M6:BIZT-G3-3 (az M6.F:451 szó szerint)
- M6.F:96–101, :474, :508 közös eszköz, kijelentkezés · M6:IMPL-G3-1 (az A11Y:57 szó szerint)
- M6 HUB:177, M6.F:3 „Mentori fejlesztési jegyzet” · M6:BIZT-G1-5 (ADV:69, :151)
- HUM:34 HUM-SAFE-01 „Érintett források” · M6:BIZT-G2-8 (a döntés szövege, jóváhagyója és „Blokkol” sora változatlan)
- Z.4:201 „Egy fontos kivétel” · Z:BIZT-G1-2.obj (a jelzési szabály, a titoktartási kivétel és a 112 változatlan)
- Z.3:61 BS-D6 · Z:BIZT-G1-3 (ADV:90 / MAN:108; erősítés)
- Z.A:40 felvételi szabály · Z:BIZT-G1-9.obj (HUM:151, az M1.A:144-gyel azonos)
- Z HUB:206 „Mentori fejlesztési jegyzet” · Z:XMOD-1 (ADV:69)
- M7.4:564–567 adatbeírási tilalom · M7:BIZT-G2-7 (az M7.2:572–575 szó szerint)
- M7.B:115, :571 kilépőkártya, 30 nap · M7:BIZT-G3-5 (ADV:67 szó szerint)
- M7.4 kvízleírás, Q13 „ötlépéses jelzési út” + M3.B · M7:ERT-G2-9 (KAPU:48)
- M7.F:3, HUB:335 „Mentori fejlesztési jegyzet” · M7:IMPL-G3-3, M7:QA-BIZT-1
- M7.2:554 és M7.4 Memuna-doboz · csak „/”→„vagy” és „red flag-ek”→„red flagek”

#### Nem néztem meg / szúrópróba
- M6 KAPU :219, :260 forráshivatkozás-változása finding-ID-hez nem kötve.
- M0–M5 gyermekvédelmi változásai csak szúrópróbával (M0.2:473, M0.A:638 = GK:78, M2 passz-betoldás, M3 Memuna-QA doboz: kánonnal egyezőnek tűnnek).
- A generált médiakimenetek nem.

## III. Vétó-jegyzék — a vétó-osztályú változások teljes köre (gépi, a diffből)

A modulonkénti vétólisták helye:
- a ledger `Napló` FIX-sorai: M3, M4, M5, M6, M7, Z és a közös kánoni kör;
- az M0-é a célzott QA-riport.

Az M1 és az M2 FIX-sora nem tartalmaz vétólistát. Ezért ez a jegyzék **minden modulra** gépileg felsorolja a vétó-osztályba eső változásblokkokat a `origin/main...HEAD` tartalmi diffjéből, a `02 Tervezet/` alatt. Nincsenek benne a generált médiakimenetek: `_build`, CSV, XLSX, a regiszter, a gyártási terv és a migrációs napló.

- **Osztályok:**
  - answer key (megváltozott ✅/❌-sor);
  - munkaterhelés, időtartam, terjedelem, pontszám (megváltozott szám + mértékegység);
  - rubrika, küszöb;
  - completion, kapu;
  - gyermekvédelem;
  - adatvédelem, megőrzés.

  Az utolsó négy kulcsszó-alapú: azt jelzi, hogy a blokk érinti a témát. Ezért sok tisztán nyelvi javítás is bekerül. Ez szűrő, nem verdikt.
- **Oszlopok:**
  - hely a HEAD-en (fájlrövidítés:sor);
  - a blokkot utoljára érintő commit (soronkénti szerzőség, „blame”);
  - további osztályok;
  - szószintű változás (− régi, + új; hosszú blokknál csonkolva).
- **Visszakereshetőség:** commit → a modul fix-commitja → a ledger FIXED-sora → a validált riport.
- **Fő session-ellenőrzés:**
  - A 25 answer-key blokk mindegyikében a ✅ darabszáma és helye változatlan.
  - A szám és mértékegység változásai az I. táblázat fókuszpontjai, illetve tisztán formai esetek. Formai például a „30 nap”, amely az ADV §3 szó szerinti átvétele.


#### Answer key — a ✅/❌-jelölt sorok szövege (25)

| Hely (HEAD) | Commit | Egyéb osztály | Változás (szószintű: − régi, + új) |
|---|---|---|---|
| LMS – H5P runtime acceptance:76 | b429420 | completion-gate, safeguarding | −„attempts”).” +„attempts”); a CP-csomópontokon (CP-1, CP-2, CP-3) nincs összefoglaló dia („Hide summary slide” = be), és a Branching Sce” |
| M0.2:264 | df2792d | — | −„egyedül →” +„egyedül:” |
| M1 KAPU:132 | ed4f52d | rubric-threshold, completion-gate | −„érzés-helyett-hatás),” +„hatás helyett érzés),” |
| M2 KAPU:58 | cee9849 | — | −„(Single Choice Setben a helyes opciót kell elsőként felvenni – ott mindig az első a helyes –, és a megjelenítési sorrend” +„(Multiple” −„kapcsold be” −„Quizben:” +„Quizben a” −„questions”),” +„questions” beállítást, és minden kérdésben a „Shuffle the choices … |
| M2 KAPU:135 | cee9849 | — | +„az” −„mi *látszik*” +„mit *lát*” +„rajtad” −„kvucádon.” +„kvucád.” |
| M2 KAPU:146 | cee9849 | rubric-threshold, safeguarding | +„az” −„sávba” +„szintre” −„sáv” +„szint” |
| M2 KAPU:157 | cee9849 | — | +„Az” +„az” |
| M2 KAPU:168 | cee9849 | — | +„Az” |
| M3.3:934 | 3ae0c09 | — | −„flag-eket,” +„flageket,” −„flag-ekkel,” +„flagekkel,” |
| M3.3:982 | 3ae0c09 | safeguarding | −„flag-ek” +„flagek” |
| M4.4:576 | 37472dc 4119d16 | workload-number | −„sablon-vizuál +” −„produktum-megírást és a felcímkézett kitöltési sablont.",” +„produktum-megírást.",” +„átvezetés” −„szabad szöveges mező 5 felcímkézett mezővel (kihez / miről / miért nekik / mit csinálunk / mit vigyenek haza), 8–12 sor.” +„lecke melletti s … |
| M5.1:478 | b429420 | — | −„részvétel-alapú.”” +„részvételalapú.”” |
| M5.4:162 | 0932de3 | — | −„érték-reflexióhoz” +„értékreflexióhoz” −„gyakorlás**.” +„gyakorlás**, és ott a 4. mező konkrét cselekvést ír le, nem csak a fogalom nevét ismétli.” |
| M6 KAPU:119 | 33d77d9 | — | −„(M6.4,” +„(M6.1, SLIDE 6; példa: M6.4,” −„szcenárió)” +„szcenárió, játékág)” |
| M6 KAPU:152 | cf20a55 | — | −„/” +„vagy” −„+” +„és” |
| M6 KAPU:163 | cf20a55 | — | −„felelősség-téma” +„felelősségtéma” |
| M6 KAPU:187 | cf20a55 | — | −„Bizalom-/kontaktjátéknál” +„Bizalom- és kontaktjátéknál” |
| M6 KAPU:209 | 33d77d9 | — | −„(M6.4,” +„(M6.1, SLIDE 6; példa: M6.4,” −„szcenárió)” +„szcenárió, játékág)” |
| M6 KAPU:253 | cf20a55 | — | −„dísz-szerep.” +„díszszerep.” |
| M6 KAPU:263 | cf20a55 | — | −„belőle →” +„belőle; ezt” −„kimaradnak →” +„kimaradnak; ezt” −„papírt →” +„papírt; ezt” −„lehet →” +„lehet; ezt” |
| M6 KAPU:353 | cf20a55 | safeguarding | +„ha valaki erősen érintett,” |
| M6 KAPU:365 | cf20a55 | safeguarding | −„kiülést,” +„kiülést (felkavart kiskorút nem küldesz ki egyedül, legyen vele egy felnőtt),” |
| M7 KAPU:195 | 729342a | — | −„Megkérek” +„Kérek” |
| M7.1:437 | 729342a | — | −„tetszik,” +„illik a kvucámhoz,” |
| M7.3:472 | 729342a | — | −„/” +„vagy” |

#### Munkaterhelés, időtartam, terjedelem, pontszám — megváltozott szám + mértékegység (27)

| Hely (HEAD) | Commit | Egyéb osztály | Változás (szószintű: − régi, + új) |
|---|---|---|---|
| Emberi jóváhagyás szükséges:589 | b429420 | rubric-threshold, privacy-retention | +„## 13. Projektgazdai döntések – az M0.1 SLIDE 5 kérdésének finomítása (CC-04) és a Moodle-összevetés (CC-06) (2026-10-10” |
| M0.2:199 | df2792d | safeguarding | −„felsorolásból 3–4 mondat (pl. terápia, éjjel-nappali ügyelet,” +„* terápiát tartani, „meggyógyítani” valakit * éjjel-nappal elérhető „ügyelet” lenni minden problémára * **azonnal jelzek” −„flag jelzése stb.)” +„flag-et látok” |
| M1.2:629 | ed4f52d | — | −„„nem készültél”, „végig a többiek szavába vágtál” inkább megfigyelés, a” −„címkék.)” +„címkék. A többi rész nem címke, de nem is mind tiszta megfigyelés: a „megint”, a „végig”, az „egész idő alatt” és az „5 ” |
| M1.F:100 | adde9dd | rubric-threshold | −„rubrikasor” +„kapufeltétel” −„teljesült),” +„teljesült: van-e 0 pontos sor, vagy minden sor csak „Rendben”),” |
| M1.F:277 | adde9dd | — | −„**körbejár**, de csak” +„**körbejár**: technikai kérdésben” −„(technika, „hol” +„(„hol” −„ezt?”).” +„ezt?”), és akinek a kapuja nem teljesült, annak a javított SBI vázlatára rövid, **Megfigyelés → Hatás → Következő lépés*” |
| M2.1:8 | cee9849 | — | −„(7” +„(6” +„+ a SLIDE 4 kérdése különálló, nem követett elemként: az identitás-kör kérdése nem futhat a követett activityben; a HUM-” |
| M2.1:452 | cee9849 | — | +„*(Fejlesztői megjegyzés – beállítás a Course Presentationön kívüli elemre: minden opció helyesként jelölve; „Enable "Sho” |
| M3 KAPU:78 | 3ae0c09 | rubric-threshold, safeguarding | −„12-item” +„12 item” −„**a” +„**projektgazdai döntés** lenne; utólagos ellenőrzése (vétó/QA): az értékelési felelős és a” −„döntése** az élesítés előtti ellenőrzéskor.” +„(`Emberi jóváhagyás szükséges.md` 8. szakasz, „Új kvíztételek”).” |
| M3.3:850 | 3ae0c09 | — | −„1–3 mondatot:” +„1–2 mondatot (ha nincs kedved írni, az is oké, elég végiggondolni):” |
| M4.4:725 | 4119d16 | — | −„itt” +„a mező az LMS-M4-09 (TEXT-C) egyetlen „Required” kérdése: az űrlap első „Label” eleme a just-in-time tájékoztató (`LMS –” |
| M5.1:428 | 0932de3 105b451 | — | +„*(Megvalósítás: az 5–6 kérdés a Course Presentation elemszintű „Display as button” opciójával, gombról nyíló elemként ke” |
| M5.1:655 | 0932de3 | — | −„10–15” +„15–20” |
| M5.3:675 | 0932de3 | — | +„Az M5.3 teljesítése után **72 órával** gyere vissza egy nagyon rövid (1–2 perces) felidézési pontra. **Kötelező**, de **” |
| M7 HUB:148 | 729342a | — | +„> Az önálló munka (a v1, a kvíz és a v2 véglegesítése) reálisan kb. **105–160 perc** az online leckéken és a peulákon **” |
| M7.4:12 | 729342a | — | −„kitöltése)” +„kitöltése); a v1 megírása ezen felül önálló munka, kb. 30–45 perc (modulhub §1)” |
| M7.4:77 | 729342a | — | +„A vázlat megírására a leckén felül kb. 30–45 percet számolj.” |
| M7.4:245 | 729342a | — | −„amely felsorolja” +„szó szerint” −„3 építőkockát és tartalmukat;” +„Program terv §4 szerint: „Három építőkocka, amire a Peula v2 épül: SMART nevelési cél (M7.1), Peula 11 pontja (M7.2), Zm” |
| M7.4:548 | 729342a | — | −„3–8” +„összesen kb. 10–20” |
| M7.4:857 | 729342a | — | −„perc.” +„perc; a v1 megírása ezen felül önálló munka, kb. 30–45 perc (modulhub §1).” |
| M7.A:64 | 729342a | — | −„Mini-műhely:” +„Miniműhely:” −„kidolgozott pontom.”” +„pontom”” |
| M7.B:44 | 729342a | safeguarding | −„bulletben” +„pontban” |
| M7.B:73 | 729342a | — | −„bulletben.” +„pontban.” |
| M7.B:115 | 729342a | safeguarding, privacy-retention | −„/ kattant” −„nélkül.",” +„nélkül. A begyűjtött lapok sorsa: a peula után összesítés, majd 30 napon belül megsemmisítés (`Adatvédelem – tanulói ada” |
| M7.B:570 | 729342a | safeguarding | −„**Mini kilépőkártya” +„**Mini-kilépőkártya” +„A begyűjtött lapokat a peula után összesítsd, majd 30 napon belül semmisítsd meg (`Adatvédelem – tanulói adatok és AI.md” −„/ kattant” |
| Z.1:13 | 5fcf2b0 | completion-gate | −„Multi” +„Multiple” −„Single” +„kérdésenként egy H5P Multiple” −„Set.” +„elem, egyválaszos („Single Choice (Radio Buttons)”) módban.” |
| Z.A:214 | 5fcf2b0 | — | −„3–4” +„3” |
| Média-assetek/PRODUCTION-DECISIONS:522 | b429420 | privacy-retention | +„¦ **Q-MED-2** ¦ A narrációk besorolása (animáció hangsávja vagy önálló dia-narráció; projektgazdai döntés, 2026-10-04). ” |

#### Rubrika, küszöb, szint — érintett megfogalmazás (95)

| Hely (HEAD) | Commit | Egyéb osztály | Változás (szószintű: − régi, + új) |
|---|---|---|---|
| LMS – H5P runtime acceptance:107 | b429420 | completion-gate | +„25. **QUIZ-D completion (LMS-M0-06):** negatív eset: üres itemekkel beküldött kvízpróbálkozás. Rögzíteni kell, verzióval” |
| LMS – H5P runtime acceptance:157 | b429420 | completion-gate | +„¦ RT-P0-25 ¦ `IMPLEMENTATION_TEST_REQUIRED` ¦ 25. QUIZ-D completion (LMS-M0-06) ¦ ¦ ¦ ¦ ¦ RT-P0-26 ¦ `IMPLEMENTATION_TES” |
| LMS – activity manifest:16 | b429420 | completion-gate, privacy-retention | +„A „Hide summary slide” = No szabály a Branching Scenario-alapú sorok Course Presentation-csomópontjaira nem vonatkozik, ” |
| LMS – activity manifest:20 | b429420 | completion-gate, privacy-retention | −„próbálkozást,” +„próbálkozást (az Assignmentben „Grant attempts” = „Manually”, „Allowed attempts” = „Unlimited”),” |
| LMS – activity manifest:50 | b429420 | — | −„8” +„8; a rubrika tanulói megjelenítése: előnézet a beadás előtt („Allow users to preview rubric” = Yes), értékelés után soro” |
| LMS – activity manifest:60 | b429420 | completion-gate | −„§5)” +„§5); a tanulói Assignment-leírásba kerülő és onnan kimaradó KAPU-szakaszok: M2 KAPU §0 („LMS-eszköz”); Grade type: Point” |
| LMS – activity manifest:65 | b429420 | completion-gate, safeguarding | +„learner release előtt a Memuna írásos átnézése (QA, a release-jegyzőkönyvben; `Gyermekvédelem – release gate.md` §2, §6;” −„pont)” +„pont); a rubrika tanulói megjelenítése: előnézet a beadás előtt („Allow users to preview rubric”), értékelés után soronk” |
| M0.3:293 | df2792d | — | −„peula-tervedet” +„peulatervedet” |
| M1 KAPU:23 | ed4f52d | — | −„**Kapu-küszöb” +„**Kapuküszöb” −„az átmenethez” +„a teljesítéshez” |
| M1 KAPU:30 | ed4f52d | — | −„rubrika-küszöböt” +„rubrikaküszöböt” |
| M1 KAPU:43 | ed4f52d | — | −„*kapu-küszöbnél*” +„*kapuküszöbnél*” |
| M1 KAPU:87 | ed4f52d | — | −„ők” +„a többiek” |
| M1 KAPU:109 | ed4f52d | — | −„adnak” +„ad” |
| M1 KAPU:113 | ed4f52d | — | −„Rubrika-pontok” +„Rubrikapontok” −„Kapu-eredmény” +„Kapueredmény” |
| M1 KAPU:299 | ed4f52d | — | +„- **A rubrika a tanulónak:** a tanuló a rubrikát a beadás előtt is lássa („Allow users to preview rubric” = Yes; a MOODL” |
| M1 KAPU:304 | adde9dd ed4f52d | completion-gate, privacy-retention | −„kapu-eredmény**” +„kapueredmény**” −„hogy a cél-Moodle **mivel** rögzíti és kényszeríti ki ezt” −„(kézi „Teljesítve” jelölés, külön completion-feltétel, restrict access, vagy sor-szintű feltétel),” −„build **acceptance-tesztjén** dől el” +„stáb a `GATE_CONFI … |
| M1 HUB:249 | ed4f52d | — | −„az átmenethez” +„a teljesítéshez” |
| M1.4:582 | ed4f52d | — | −„rubrika-szintek” +„rubrikaszintek” |
| M1.4:641 | ed4f52d | — | −„Kapu-szint” +„Kapuszint” |
| M1.4:648 | ed4f52d | — | −„kapu-küszöböt” +„kapuküszöböt” |
| M2 KAPU:24 | cee9849 | completion-gate | +„A megerősítés az LMS-M2-10 mentori checkpoint (BSPEC-07): „Teljesítve” = az LMS-M2-05 legutóbb leadott jegyzetének előír” |
| M2 KAPU:26 | cee9849 | completion-gate | +„**Az Assignment tanulói leírásába** ebből a fájlból az A. önellenőrző lista, a D. szakasz bevezetője a 🔒 „Mit kérünk és ” −„újra beadás.” +„újrabeadás.” |
| M2 KAPU:174 | cee9849 | — | −„szintes,” +„szintű,” |
| M2 KAPU:178 | cee9849 | — | −„újra beadás” +„újrabeadás” |
| M2 KAPU:263 | cee9849 | completion-gate | −„újra beadás.” +„újrabeadás.” +„**Megerősítés (LMS-M2-10, BSPEC-07):** „Teljesítve” = az LMS-M2-05 legutóbb leadott jegyzetének előírt mezőiben ténylege” |
| M2 HUB:183 | 5bab331 | completion-gate | +„az” +„a Check-kérdések eredménye elküldve ÉS” |
| M2 HUB:222 | cee9849 | completion-gate | +„> > **Mentori megerősítés (LMS-M2-10, BSPEC-07):** „Teljesítve” = az LMS-M2-05 legutóbb leadott jegyzetének előírt mezői” |
| M2.F:167 | cee9849 | privacy-retention | −„fogalom-térkép” +„fogalomtérkép” |
| M2.F:217 | cee9849 | — | +„– elsősorban a javítandó rubrikasorokhoz tartozó leckéknél –” |
| M3 KAPU:30 | 3ae0c09 | completion-gate | +„a kvízkomponensen (LMS-M3-06)” −„kapu” +„stáb a kapueredményt beírja a `GATE_CONFIRMED_M3` checkpointba (a” −„állapotba kerül,” +„értéket mindig a stáb írja be; lásd 1.2” +„2.3). *(Nem használt út –” −„továbblépés megnyílik (lásd 1.2).” +„kánoni build-szerző … |
| M3 KAPU:37 | 3ae0c09 | completion-gate, safeguarding | −„completion.” +„completion (LMS-M3-04) + **M1 complete** (`LMS – activity manifest.md` §4; Q-REL-2).” −„belépő feltétele is csak az L1–L4 completion + Komponens B),” +„követelményei között sem szerepel),” −„red-flag-felismerés,” +„red flag-felismerés,” −„kapu … |
| M3 KAPU:310 | 3ae0c09 | — | +„A tanuló a beadás előtt előnézetben látja a rubrikát („Allow users to preview rubric”), értékelés után pedig soronként a” |
| M3 KAPU:333 | 3ae0c09 | completion-gate | −„alapján; ha az összetett feltétel Moodle-ben nem kódolható bizonyítottan,” +„alapján:” −„feltételét” +„mindig” −„kell kötni.” +„(LMS-M3-07) kötött. Az M4 már az **M3 megerősítve** feltétellel nyitható (Q-REL-2); az **M3 complete** a következő éles ” |
| M3.4:837 | 3ae0c09 | completion-gate, safeguarding | −„kritikus” +„kötelező” |
| M3.B:512 | 3ae0c09 | completion-gate, safeguarding | +„vagy a titoktartás kérdését meg sem említi, illetve ha” −„kritikus” +„kötelező” |
| M3.F:187 | 3ae0c09 | — | −„visszajelzésedet.” +„visszajelzésedet: a helyzetleírásod beadásánál a rubrikát és a visszajelzést, az ‘M3 – kapueredmény’ elemnél pedig az ot” |
| M4 HUB:62 | 4119d16 | completion-gate | −„videókkal és” +„videókkal; a” −„kérdésekkel.” +„kérdések a lecke melletti szövegmezőben vannak (LMS-M4-06).” −„lecke végignézve +” +„a pontozott interakciók eredménye, amelyet a Course Presentation az összefoglaló dián küld el (Moodle: „Receive a grade”” −„( … |
| M4 HUB:70 | 4119d16 | completion-gate | −„lecke végignézve +” +„a pontozott interakciók eredménye, amelyet a Course Presentation az összefoglaló dián küld el (Moodle: „Receive a grade”” −„megfogalmazása).” +„megfogalmazása) a lecke melletti szövegmezőben (LMS-M4-07).” |
| M4 HUB:76 | 4119d16 | completion-gate | −„mini-kvíz” +„minikvíz” −„lecke végignézve +” +„a pontozott interakciók eredménye, amelyet a Course Presentation az összefoglaló dián küld el (Moodle: „Receive a grade”” −„használni).” +„használni) megválaszolva a lecke melletti szövegmezőben (LMS-M4-08).” |
| M4 HUB:84 | 4119d16 | completion-gate | +„a” +„pontozott minikvízének (SLIDE 4, Check) eredménye, amelyet a Course Presentation az összefoglaló dián küld el (Moodle: „” −„végignézve +” +„záró vázlata beküldve a lecke melletti szövegmezőben (LMS-M4-09); modulszinten pedig” |
| M4 HUB:143 | 4119d16 | completion-gate | +„mentori megerősítés helye az LMS-M4-10 (BSPEC-07): „Teljesítve” = az LMS-M4-05 legutóbb leadott vázlatának előírt mezőib” |
| M4 HUB:168 | 4119d16 | — | +„az” |
| M4.1:23 | 4119d16 | completion-gate | −„H5P” +„a pontozott interakciók eredménye, amelyet a” −„végignézve +” +„az összefoglaló dián küld el (Moodle: „Receive a grade”, Grade to pass nélkül; „Hide summary slide” = No; H5P-C profil, ” −„kitöltve.” +„kitöltve a lecke melletti szövegmezőben (LMS-M4-06 … |
| M4.2:21 | 4119d16 | completion-gate | −„H5P” +„a pontozott interakciók eredménye, amelyet a” −„végignézve +” +„az összefoglaló dián küld el (Moodle: „Receive a grade”, Grade to pass nélkül; „Hide summary slide” = No; H5P-C profil, ” −„kitöltve.” +„kitöltve a lecke melletti szövegmezőben (LMS-M4-07 … |
| M4.3:19 | 4119d16 | completion-gate | −„Mini-kvíz” +„Minikvíz” −„H5P Course Presentation” −„mini-kvízének (Check)” +„interakciók” |
| M4.4:26 | 4119d16 | completion-gate | −„mini-kvízének” +„minikvízének” |
| M5 HUB:172 | b429420 | — | −„fogalom-kvíz” +„fogalomkvíz” −„produktum-alapú” +„produktumalapú” |
| M5 KAPU:13 | b429420 | — | −„fogalom-kvíz.” +„fogalomkvíz.” −„fogalom-kvíz” +„fogalomkvíz” |
| M5 KAPU:305 | 105b451 | completion-gate | −„kódolja; ha az összetett feltétel Moodle-ben nem kényszeríthető ki bizonyítottan,” +„kódolja, ezért” −„feloldását” +„feloldása” −„kell kötni” +„(LMS-M5-08) kötődik, nem a nyers pontszámhoz: az M6 már az **M5 megerősítve** feltétellel” −„választott mechanizmu … |
| M5 KAPU:312 | 0932de3 105b451 | — | −„sorrend-tényt” +„sorrendtényt” −„**Magolás-védelem:**” +„**Magolásvédelem:**” +„Build-megjegyzés: a válaszsorrend keveréséhez a kvízszintű „Shuffle within questions” és kérdésenként a „Shuffle the cho” −„**Küszöb-érzékenység:**” +„**Küszöbérzékenység:**” |
| M5.2:9 | 0932de3 | completion-gate | −„végképernyője.” +„végképernyőjéig.” |
| M5.B:93 | 0932de3 | — | −„táblázat-vázlat” +„táblázatvázlat” −„kapu-leadás” +„kapuleadás” −„kapu-leadás” +„kapuleadás” −„táblázat-vázlata” +„táblázatvázlata” −„kapu-leadás” +„kapuleadás” |
| M6 HUB:10 | 33d77d9 cf20a55 | safeguarding, privacy-retention | +„Cím,” −„érték-kapcsolódás,” +„értékkapcsolódás,” −„létszám,” +„létszám + hangulat,” +„+ időkeret + tér” +„játéklapon a kvucáról ne szerepeljen azonosító adat, például név vagy konkrét, beazonosítható eset; elég a korosztály, a” −„"mixed",” +„"human",” −„"veg … |
| M6 HUB:20 | cf20a55 | — | −„HASZNÁLJA, de NEM definiálja” +„HASZNÁLJA;” −„rovatstruktúrát, ezért” +„rovatstruktúra forrása az M6.B-MUNK-01, és a két spec azonos;” |
| M6 HUB:189 | cf20a55 | — | −„kapu-logika” +„kapulogika” |
| M6 HUB:207 | cf20a55 | — | −„(M6 játéklap feladat).” +„(a kurzusban: „M6 – Játéklap”).” +„A játéklapon a kvucáról ne szerepeljen azonosító adat, például név vagy konkrét, beazonosítható eset; elég a korosztály,” |
| M6 KAPU:18 | cf20a55 | — | −„kapu-filozófiát” +„kapufilozófiát” |
| M6 KAPU:22 | cf20a55 | — | −„rubrika**;” +„rubrika** (a kurzusban: „M6 – Játéklap”);” −„rubrika-sor” +„rubrikasor” −„vagy **H5P Question Set**” +„(LMS-M6-06, QUIZ-D; a kurzusban: „M6 – Szcenárió-önellenőrzés”)” |
| M6 KAPU:36 | cf20a55 | — | −„rubrika-sora” +„rubrikasora” |
| M6 KAPU:48 | cf20a55 | — | −„kapu-validitási” +„kapuvaliditási” |
| M6 KAPU:347 | 33d77d9 | — | +„– csak a kohorsz első próbálkozása előtt, menet közben nem –” |
| M6.B:52 | cf20a55 | — | −„kapu-rubrika” +„kapurubrika” |
| M6.B:137 | cf20a55 | — | −„minimum-checklista” +„minimum-ellenőrzőlista” |
| M6.B:139 | cf20a55 | — | −„mini-bemutatók” +„minibemutatók” |
| M6.B:155 | cf20a55 | — | −„checklist” +„ellenőrzőlista” |
| M6.B:220 | cf20a55 | — | −„rubrika-felütés” +„rubrikafelütés” |
| M6.B:244 | cf20a55 | — | −„használom?;” +„használod?;” +„A játéklapon a kvucáról ne szerepeljen azonosító adat, például név vagy konkrét, beazonosítható eset; elég a korosztály,” |
| M6.B:533 | cf20a55 | safeguarding | −„játék-példa,” +„játékpélda,” −„vállalás-körre” +„vállaláskörre” |
| M6.F:26 | cf20a55 | — | −„(játék-kategóriák,” +„(játékkategóriák,” |
| M6.F:40 | cf20a55 | — | −„rubrika-sorban” +„rubrikasorban” +„A javító leadás határideje a központi naptár szerint az F-peula utáni szerda 18:00.” |
| M6.F:474 | cf20a55 | privacy-retention | +„a közös eszközön saját fiókkal belépés és kijelentkezés, az M6.1 és az M6.2 offline letölthető leckeváltozata,” −„tábla,” +„tájékozódó tábla (POSZ-01),” |
| M7 KAPU:20 | 729342a | completion-gate, safeguarding | −„nyílik,” +„teljesül,” −„nyílik,” +„nyílik (az M6 complete feltétellel: `LMS – activity manifest.md` LMS-M7-07, §4),” |
| M7 KAPU:34 | 729342a | — | −„tét,” +„tétű,” +„az M6 complete feltétellel,” −„LMS-M7-07).” +„LMS-M7-07, §4).” |
| M7 KAPU:216 | 729342a | safeguarding | −„nyílik.” +„teljesül.” |
| M7 KAPU:240 | 729342a | safeguarding | −„nyílik):” +„teljesül):” |
| M7 KAPU:254 | 729342a | — | −„leadás” +„leadása” −„rubrika-pont).**” +„rubrikapont).**” |
| M7 KAPU:261 | 729342a | — | −„leadás” +„leadása” −„rubrika-pont).**” +„rubrikapont).**” |
| M7 KAPU:268 | 729342a | safeguarding | −„rubrika-minimumában” +„rubrikaminimumában” |
| M7 KAPU:289 | 729342a | — | −„kvuca-meta” +„kvuca-infó” −„meta” +„kvuca-infó” −„keret-erősítő” +„kereterősítő” |
| M7 KAPU:376 | 729342a | — | −„R4” +„R4, R5” −„kapu-szám,” +„kapuszám,” |
| M7 KAPU:421 | 729342a | completion-gate, safeguarding | −„tét,” +„tétű,” −„leadás” +„leadása” −„leadás” +„leadása” |
| M7 HUB:10 | 729342a | — | −„tét,” +„tétű,” |
| M7 HUB:143 | 729342a | safeguarding | −„tét**:” +„tétű**:” −„a „SMART” +„az „M7 – SMART” −„(felkészültségi)”” +„(felkészültségi, a v2 előtt)”” +„kvíz megerősített,” −„kvíz” +„eredménye” |
| M7 HUB:349 | 729342a | completion-gate | −„tét,” +„tétű,” −„a „SMART” +„az „M7 – SMART” −„(felkészültségi)”” +„(felkészültségi, a v2 előtt)”” +„az M6 complete feltétellel,” −„LMS-M7-07);” +„LMS-M7-07, §4);” |
| M7 HUB:374 | 729342a | — | −„**Rubrika-minimum” +„**Rubrikaminimum” |
| M7 HUB:381 | 729342a | safeguarding, privacy-retention | −„(R1, R5,” +„(R1 – SMART nevelési cél, R5 – Inkluzivitás & hozzáférhetőség és” −„mindegyike” +„– Módszer-illeszkedés: mindegyik” −„„SMART” +„„M7 – SMART” −„(felkészültségi)”**” +„(felkészültségi, a v2 előtt)”**” +„az M6 complete feltétellel (`LMS – activity m … |
| M7 HUB:412 | 729342a | safeguarding | −„rubrika-sorok” +„rubrikasorok” −„kvuca-meta”)” +„kvuca-infó”)” −„mini-anyagot” +„minianyagot” |
| M7.4:845 | 729342a | — | −„sor,” +„sor;” −„/ kritikus sorok” +„(≥17/24) ÉS R1, R5, R6 ≥2 ÉS R4” |
| M7.B:28 | 729342a | — | −„szerzett” +„végzett” −„A „SMART” +„Az „M7 – SMART” −„Kvucá”” +„Kvucá” +„(felkészültségi, a v2 előtt)”” −„nyílik, és” +„nyílik; ajánlott még az M7.B előtt teljesíteni,” +„Peula” −„kell teljesíteni: ez” +„kötelező, és a megerősített eredménye a v2 leadásának f … |
| M7.B:163 | 729342a | — | −„rubrika-pont;” +„rubrikapont;” |
| M7.B:564 | 729342a | — | −„rubrika-pont,” +„rubrikapont,” |
| Program terv:110 | b429420 | — | −„fogalom-kvíz” +„fogalomkvíz” |
| Program terv:183 | b429420 | — | −„**fogalom-kvíz” +„**fogalomkvíz” |
| Program terv:257 | c299aab | safeguarding, privacy-retention | −„részvétel-alapú” +„részvételalapú” |
| Program terv:273 | b429420 | — | −„fogalom-kvíz” +„fogalomkvíz” |

#### Completion, kapu, feloldás — érintett megfogalmazás (69)

| Hely (HEAD) | Commit | Egyéb osztály | Változás (szószintű: − régi, + új) |
|---|---|---|---|
| LMS – H5P runtime acceptance:72 | b429420 | — | +„Negatív eset: az összefoglaló dia elérése megválaszolatlan interakciókkal (minden dia válasz nélkül); rögzíteni kell, ve” |
| LMS – H5P runtime acceptance:78 | b429420 | safeguarding | +„- **Szünet és visszatérés (SAFE-1):** kilépés egy szcenárió közben, majd újranyitás egy új munkamenetben, a 24. pont men” |
| LMS – activity manifest:52 | b429420 | privacy-retention | −„pont)” +„pont); ha a kérdés külön H5P activityként készül, saját build_id kell neki, és nem completion-elem” |
| LMS – activity manifest:54 | b429420 | — | −„profil (értékválasztás);” +„profil: a H5P SLIDE 7 Check-kérdéseinek eredménye, amelyet a Course Presentation az összefoglaló dián küld el (M2.2, „Co” |
| LMS – activity manifest:73 | b429420 | — | −„mini-kvíz” +„pontozott interakciók” |
| LMS – activity manifest:82 | b429420 | — | −„vázlatmezője” +„vázlata” |
| LMS – activity manifest:85 | b429420 | — | −„a forrás a Moodle Label-t is megengedi, de” |
| LMS – activity manifest:98 | b429420 | — | −„(kvuca-meta,” +„(kvuca-infó,” |
| M0 HUB:43 | df2792d | — | −„alap” +„alapszintű” |
| M0.1:13 | c299aab | — | −„Multi” +„Multiple” |
| M0.1:61 | df2792d | — | −„cél verzión.” +„célverzión.” |
| M0.2:62 | df2792d | — | −„cél verzión.” +„célverzión.” |
| M0.3:59 | df2792d | — | −„cél verzión.” +„célverzión.” |
| M0.3:257 | df2792d | — | −„sikerül →” +„sikerül, az” −„lehetőséget.” +„lehetőséget, > – a javító próbálkozás csak a kötelező felzárkóztató peula (F-peula) után nyílik.” |
| M0.4:61 | df2792d | — | −„cél verzión.” +„célverzión.” |
| M1 HUB:266 | ed4f52d | — | −„modulonként” +„leckénként” |
| M1.1:344 | ed4f52d | — | −„(Completion,” +„(Nem completion-elem,” |
| M1.2:976 | adde9dd | — | −„billentyűzet-alternatíva** (pl. kattintásos/kijelölős párosítás),” +„a SLIDE 5 szerinti húzásmentes út** (alapértelmezésként kártyánkénti rádiógombos választás, kattintással/koppintással és” |
| M1.4:153 | ed4f52d | — | −„megvalósítási típust” +„kártyaválasztás pontozatlan választó, ezért nem önálló completion-elem (D-d/D-i). Hogy a választott megoldás egyetlen vá” −„rögzíti.” +„14. pontja igazolja.” |
| M1.B:476 | ed4f52d | — | −„Assignmentben,” +„SBI-beadandóban (oda már csak kitalált, életszerű helyzet kerülhet),” −„javítás.” +„javító próbálkozás.” −„el:” +„el a teljesítést:” |
| M1.F:270 | adde9dd | — | −„Assignmentben” +„SBI-beadandóban” −„SBI-mondatot**, amit majd a peulán / terepen tényleg használni fog;” +„SBI-mondatot** (oda már csak kitalált, életszerű helyzet kerülhet);” −„kérje meg a képzőt, hogy nyisson” +„szóljon nekem, és nyitok” |
| M1.F:361 | ed4f52d | — | −„Assignmentben.” +„SBI-beadandóban.” |
| M2 HUB:242 | cee9849 | privacy-retention | −„Melyik pillérnél (cionizmus / szocializmus / humanista zsidóság) állnak meg sokan M2.3-ban. * Az M2.3-mutató csak akkor ” +„A pillér-ág választásának tanulói fiókhoz kötött tartós tárolása nem pedagógiai követelmény, és nem kívánt adat; a compl” −„`LMS – H5P … |
| M2.1:18 | cee9849 | — | +„a” +„SLIDE 6 Check-kérdéseinek eredménye, amelyet a” −„végignézve +” +„az összefoglaló dián küld el (Moodle: „Receive” +„grade”; „Hide summary slide” = No; H5P-C profil, BSPEC-06), és a SLIDE 5” −„válasz beadva.” +„válasza beküldve a lecke melletti szövegmez … |
| M2.3:11 | cee9849 | — | −„videó-oldal” +„oldal (Course Presentation-csomópont, benne a videó)” |
| M3 KAPU:76 | 045a876 | — | +„kritikus itemek ellenőrzésének” −„megvalósítás:**” +„megvalósítása a kvízkomponensben:**” −„kapu „Teljesítve” állapotba állítása és a továbblépés megnyitása” +„kapueredmény beírása (`GATE_CONFIRMED_M3`, lásd 2.3)” |
| M3 KAPU:84 | 3ae0c09 | safeguarding | −„M4 megnyílik.” +„M5 kapufeladata megnyílna.” |
| M3 HUB:8 | 3ae0c09 | safeguarding | −„kapu-kvíz” +„kapukvíz” |
| M3 HUB:249 | 3ae0c09 | safeguarding | −„csak” +„nem használt (`LMS – activity manifest.md`, LMS-M3-06: QUIZ-M; a korábbi feltételek” −„§0-ban rögzített feltételekkel (grade-alapú completion, igazoltan kikényszerített kritikus itemek).” +„§0-ban).” |
| M3.1:586 | 3ae0c09 | — | −„(Tab + Enter)” +„(Tab, majd nyílbillentyűk vagy Szóköz)” |
| M3.2:624 | 3ae0c09 | — | −„(Tab+Enter)” +„(Tab, majd nyílbillentyűk vagy Szóköz)” |
| M3.2:675 | 3ae0c09 | — | +„ez” −„választott H5P-típus” +„forma” −„igazolni), és biztosíts” +„igazolni); a koppintásos párosítás maga a” −„változatot is:” +„változat:” −„(Tab + Enter)” +„(Tab, majd nyílbillentyűk vagy Szóköz)” |
| M3.3:94 | 3ae0c09 | — | +„- CP-csomópontok (CP-1, CP-2, CP-3): „Hide summary slide” (`hideSummarySlide`) = be; a grade a Branching Scenario végkép” |
| M3.4:442 | 3ae0c09 | — | −„(Tab+Enter)” +„(Tab, majd nyílbillentyűk vagy Szóköz)” |
| M3.4:512 | 3ae0c09 | — | −„(Tab + Enter)” +„(Tab, majd nyílbillentyűk vagy Szóköz)” |
| M3.F:216 | 045a876 | safeguarding | +„és a helyzetleírás konkrét javítási tervének” |
| M3.F:247 | 3ae0c09 | — | −„**javítására**.” +„**javítási tervének elkészítésére**.” |
| M3.F:262 | 045a876 | — | −„helyzetleírásodat,” +„beadott helyzetleírásodat” −„visszajelzés „Következő lépés”” +„visszajelzést, és a ‘Következő lépés’” −„elkezded javítani.”” +„papíron, a jegyzetlapodon megírod a **konkrét javítási tervedet**; a javított leírást a javító próbálkozás me … |
| M3.F:387 | 3ae0c09 | safeguarding | +„A lapok utána visszakerülnek a résztvevőkhöz, mert a felírt kérdéseiket és az „ezt pótolom” bejegyzéseiket a javító prób” |
| M3.F:488 | 3ae0c09 | — | −„próbálkozás**:” +„próbálkozás** (határideje a központi naptár szerint az F-peula utáni szerda 18:00):” |
| M3.F:558 | 3ae0c09 | — | −„kvíz),” +„kvíz; határideje a központi naptár szerint az F-peula utáni szerda 18:00),” |
| M4.1:53 | 4119d16 | — | +„Ha a kapunál akadsz el, ez nem zsákutca: ha a kapu nem teljesül, az **M4.F felzárkóztató peula (F-peula)** ajánlott, vez” |
| M4.2:57 | 4119d16 | — | +„Ha a kapunál akadsz el, ez nem zsákutca: ha a kapu nem teljesül, az **M4.F felzárkóztató peula (F-peula)** ajánlott, vez” |
| M4.3:52 | 4119d16 | — | −„kapu-kvízben),” +„kapukvízben),” +„Ha a kapunál akadsz el, ez nem zsákutca: ha a kapu nem teljesül, az **M4.F felzárkóztató peula (F-peula)** ajánlott, vez” |
| M4.4:62 | 37472dc | — | +„Ha a kapunál akadsz el, ez nem zsákutca: ha a kapu nem teljesül, az **M4.F felzárkóztató peula (F-peula)** ajánlott, vez” |
| M4.4:790 | 4119d16 | — | +„a visszajelzés megnevezi a hiányzó vagy nem érthető sablonelemet;” |
| M5 HUB:177 | 0932de3 | — | −„nyithat)” +„nyithat), és az F-peula utáni szerda 18:00-ig adható le” |
| M5 HUB:187 | b429420 | — | −„fogalom-kvíz:**” +„fogalomkvíz:**” −„felzárkózás-jelző.” +„felzárkózásjelző.” |
| M5 KAPU:303 | 0932de3 | — | +„A javító újraleadás határideje a központi naptár szerint az F-peula utáni szerda 18:00.” |
| M5.1:24 | 0932de3 | — | −„tényleges megvalósítást (Moodle-oldali szövegmező, H5P **Free Text Question** igazolt host/befoglaló-támogatással, vagy ” +„lépés tanuló-lokális, beviteli elem nélkül; a rögzítésmentességet” −„6.” +„24.” −„dönti el és teszteli” +„igazolja” |
| M5.F:45 | 0932de3 | — | +„és az F-peula utáni szerda 18:00-ig adható le;” −„„M5.3-at” +„„Az M5.3-at” |
| M6 HUB:170 | cf20a55 | — | −„feltétele).” +„feltétele), határideje a központi naptár szerint az F-peula utáni szerda 18:00.” |
| M6.F:54 | cf20a55 | — | −„+” +„és” +„határideje a központi naptár szerint az F-peula utáni szerda 18:00;” |
| M7 KAPU:411 | 729342a | safeguarding | +„az M6 complete feltétellel (`LMS – activity manifest.md` LMS-M7-07, §4),” |
| M7 HUB:335 | 5c0cd4a 729342a | privacy-retention | −„1:1 meta-napló”” +„fejlesztési jegyzet”” +„a visszajelzés következő lépései szerint kijavítja a peula-terve érintett részét, vagy” |
| M7.4:704 | 729342a | safeguarding | +„red flag esetén követendő ötlépéses jelzési útról szóló” +„és az **M3.B**” |
| M7.F:30 | 5c0cd4a | — | −„Kvucá-checklist)” +„Kvucá-checklist és operációs táblázat)” |
| M7.F:39 | 729342a | — | −„lehet.” +„lehet, * a javító próbálkozás határideje az M7 javító határideje (a Z utáni hét szerdája, 18:00); ha a kvíz első próbálk” |
| M7.F:171 | 729342a | privacy-retention | −„soros hely” +„soros, letéphető csík” −„(M7.3).').",” +„(M7.3).'): a résztvevő megtartja; ha a lapot név nélkül begyűjtötték, a terv külön cetlire kerül.",” |
| M7.F:202 | 729342a | safeguarding | −„leckerészt,” +„leckerészt (a kvíz gyermekvédelmi kérdései az M3.3 anyagára és az M3.B lépéstérképére is épülnek),” −„Peula-terve” +„peula-terve” |
| M7.F:324 | 729342a | — | −„pótvizsga-íze.” +„pótvizsgaíze.” −„checklist).” +„checklist és operációs táblázat).” |
| M7.F:335 | 5c0cd4a | safeguarding | −„a »SMART” +„az »M7 – SMART” −„Kvucá«” +„Kvucá” +„(felkészültségi, a v2 előtt)«” +„és az M3.B lépéstérképére” −„együtt.”” +„és az operációs táblázattal együtt. A javító próbálkozás határideje az M7 javító határideje: a Z utáni hét szerdája, 18:” |
| M7.F:337 | 729342a | — | +„(ha a jegyzetlapodat begyűjtöttem, külön cetlire)” |
| M7.F:350 | 5c0cd4a | safeguarding, privacy-retention | −„fogalomtérkép-flipchart);” +„fogalomtérkép-flipchart; a közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a sz” −„checklist).",” +„checklist és operációs táblázat; határideje az M7 javító határideje, a Z utáni hét szerd … |
| M7.F:397 | 729342a | — | −„tovább,” +„tovább (határideje az M7 javító határideje, a Z utáni hét szerdája, 18:00; ha a kvíz első próbálkozása nem teljesült, a ” +„és az operációs táblázattal” +„* A peula után megnyitom a javító próbálkozást annak, akinek a kapuja nem teljesült (ha nem  … |
| Z.4:338 | 2116499 | — | −„újrabeadás engedett;” +„a puha kapus beadásoknál – így az LMS-Z-04-nél is – 1 normál + 1 javító beadás nyílik automatikusan, további beadást a k” |
| Z.4:343 | 5fcf2b0 | — | −„Completion csak akkor jár,” +„Két külön állapot, nem vonható össze (BSPEC-07; `LMS – activity manifest.md`, LMS-Z-04 és LMS-Z-08): **SUBMITTED** – a r” −„van;” +„van (üres vagy kitöltetlen sablon, illetve” −„leadás,” +„fájlfeltöltés nem elég), egyébként „Még … |
| Z HUB:33 | 5fcf2b0 | — | −„Mivel a” +„A” −„teljesítése után nyílik, náluk” +„kapueredményével nyílik („Még nem teljesítve” esetén is; Q-REL-2); a javítási úton lévő madrih Z-határidejét, és – ha az” −„határidejét” +„utáni hétre kerül – az M7 és a Z teljes útját” −„(`LMS” +„(Moodle fel … |
| Z HUB:199 | 5fcf2b0 | — | −„után).” +„után), és a kijelölt mentor/értékelő megerősítette (`LMS – activity manifest.md`: az LMS-Z-04 leadásával és az LMS-Z-08 ” |

#### Gyermekvédelem, eszkaláció, passzjog — érintett megfogalmazás (86)

| Hely (HEAD) | Commit | Egyéb osztály | Változás (szószintű: − régi, + új) |
|---|---|---|---|
| Emberi jóváhagyás szükséges:34 | b429420 | — | +„M6.2,” +„M6.B, M6-kapu,” |
| M0 HUB:77 | df2792d | — | −„alap” +„alapszintű” |
| M0.1:17 | df2792d | — | −„**fel” +„**el” −„majd sorolni a képzés 9 állomását a kódjukkal” +„mondani, hány modulból áll az év” −„**egy-egy mondatban megnevezni, miről szólnak az egyes modulok**,” +„**és melyikben lesz szó a visszajelzésről, a gyermekvédelemről és a peulatervezésről**, … |
| M0.1:51 | df2792d | — | +„> A kijelölt **Memuna** (a Somer gyermekvédelmi felelőse) elérhetőségét a kurzus „Segítség és kapcsolatok” blokkjában ta” |
| M0.1:300 | df2792d | — | −„peula-terv),” +„peulaterv),” |
| M0.2:40 | df2792d | — | −„egyedül** (hanem” +„egyedül**. Ezekért” −„–” +„felel:” −„**Memuna**, a” +„**Memuna** (a” −„felelőse – felelőssége).” +„felelőse).” |
| M0.2:285 | df2792d | — | −„kapu-logika,” +„kapulogika,” −„(peula-tervezés)” +„(peulatervezés)” −„tét:” +„tétű:” |
| M0.2:473 | 1d9d15f | — | +„négy szerep (technikai segítség, tanulási/programkontakt, assigned mentor, Memuna / safeguarding) konkrét elérhetősége, ” −„és elérhetősége” −„kint,” +„kint – a Memuna és összeférhetetlenség esetére a név szerint kijelölt helyettese a többi kontakttól külön  … |
| M0.3:254 | df2792d | — | −„peula-terv),” +„peulaterv),” |
| M0.3:303 | df2792d | — | −„kilépsz →” +„kilépsz, ezért” |
| M0.4:336 | df2792d | — | −„róla. > A 3. helyzetben pedig: hanihról csak indokolt célból készülhet fotó, és az is ellenőrzött tárhelyre kerül, nem s” +„róla.”” |
| M0.A:129 | df2792d | — | −„Mini-protokoll.” +„Miniprotokoll.” |
| M0.A:196 | df2792d | — | −„„ÉN,” +„„ÉN” |
| M0.A:520 | df2792d | privacy-retention | −„/” +„vagy” |
| M1.A:488 | ed4f52d | — | +„> Mondhatsz passzt.” |
| M2.4:657 | cee9849 | — | −„‘majd” +„„majd” −„komolyabb’” +„komolyabb”” |
| M2.4:692 | cee9849 | — | −„(pl.” +„(Pl.” |
| M2.4:695 | cee9849 | — | −„(pl.” +„(Pl.” |
| M2.A:224 | cee9849 | — | −„(sor 149).",” +„(4.2 Blokk 2, 3. lépés).",” |
| M2.A:253 | cee9849 | — | −„az előző kérdések” +„a szett könnyed, nem felkavaró” |
| M2.B:380 | cee9849 | — | −„mindenki (vagy” −„szeretné)” +„szeretné,” +„> „Ha most nem szeretnél ilyet mondani, mondhatod azt is, hogy *passz* – ez is teljesen oké.”” |
| M3 KAPU:82 | 3ae0c09 | privacy-retention | −„kettő” +„Program terv §4 és §7” |
| M3 KAPU:104 | 3ae0c09 | — | −„+” +„és a” |
| M3 KAPU:325 | 3ae0c09 | — | −„jelzés /” +„jelzés;” |
| M3 KAPU:337 | 045a876 | — | −„3. dia.)”” +„‘Mi az a red flag?’)”” −„a leggyakoribb” +„gyakori” −„1. és 4. dia.)”” +„‘Mi az a gyermekvédelem madrihként? – az ötlépéses jelzési út’, 2. lépés.)”” −„2. dia.)”” +„‘Mi az a gyermekvédelem madrihként? – az ötlépéses jelzési út’.)”” −„5. dia.)””  … |
| M3 HUB:33 | 3ae0c09 | — | −„flag-ek**” +„flagek**” |
| M3 HUB:276 | 3ae0c09 | — | −„kapu-kvízen” +„kapukvízen” |
| M3.3:15 | 3ae0c09 | — | −„flag-ek” +„flagek” |
| M3.3:36 | 3ae0c09 | — | −„flag-ek” +„flagek” |
| M3.3:405 | b429420 | — | −„korosztály-térképére):” +„korosztálytérképére):” |
| M3.3:545 | 3ae0c09 | — | −„a leggyakoribb” +„gyakori” −„legkockázatosabb” +„kockázatos” |
| M3.3:974 | 3ae0c09 | — | −„flag-nek,” +„flagnek,” |
| M3.4:3 | 3ae0c09 | — | +„> ⚠️ **Élesítés előtt a Memuna (gyermekvédelmi felelős) írásos átnézése szükséges (QA, a release-jegyzőkönyvben).** > Ez” |
| M3.A:355 | 3ae0c09 | — | −„(viharzás)” +„(„balhék”)” |
| M3.A:440 | 3ae0c09 | — | −„(viharzás)” +„(„balhék”)” |
| M3.A:567 | 3ae0c09 | — | −„flag-ek” +„flagek” |
| M3.B:10 | 3ae0c09 | — | +„bántalmazott vagy eltűnt gyermek ügyében 116-000,” |
| M3.B:168 | 3ae0c09 | — | −„flag-ek,” +„flagek,” |
| M3.B:258 | 3ae0c09 | — | +„* Kitöltött helyi gyermekvédelmi útvonal lap (M3.B-MUNK-02; 2.3). * Képzőnek: krízis- / segélyvonal referenciakártya (M3” |
| M3.B:434 | 3ae0c09 | privacy-retention | −„Nagy papíron” +„Használd a lépéstérkép-sablont (M3.B-MUNK-01),” +„nagy papíron,” +„Valós gyermekvédelmi eset soha nem pedagógiai feladat (`Gyermekvédelem – release gate.md` §2); fotóra és más felvételre ” |
| M3.B:462 | 3ae0c09 | — | −„„Nálatok konkrétan kit hívnál fel?”” +„„Ki most a Memuna, ki a helyettese, és hogyan éred el őket?”” |
| M3.B:523 | 33050fa | — | +„lépéstérkép-sablon (M3.B-MUNK-01) vagy” −„filcek.” +„filcek; képzőnek a krízis- / segélyvonal referenciakártya (M3.B-KART-02), a képzői biztonsági gyorskártya (M3.B-KART-03)” |
| M3.F:436 | 3ae0c09 | — | −„flag-ek**” +„flagek**” −„ezeket” +„a red flageket” |
| M4.3:23 | 4119d16 | — | −„mini-kvíz” +„minikvíz” −„kapu-kvíz,” +„kapukvíz,” |
| M4.3:75 | 4119d16 | — | −„mini-szituáció” +„miniszituáció” |
| M4.3:359 | 4119d16 | — | −„hanihcsal” +„hanihhal” |
| M4.B:85 | 4119d16 | — | +„(kezelése: Adatvédelem – tanulói adatok és AI.md §3, „Név nélkül begyűjtött papír munkalap” sor)” |
| M4.B:300 | 4119d16 | — | −„módja; CBE-LSE, azaz a CBE—Life Sciences Education folyóirat).” +„módja).” −„keretben” +„keretében” |
| M5 KAPU:223 | 0932de3 | — | −„(A)” −„(C)” −„D” +„több külön napon, rövid blokkokban végzett gyakorlás” −„mini-kvíz” +„minikvíz” |
| M6 HUB:213 | cf20a55 | — | −„gyermekvédelem &” +„gyermekvédelmi és” +„az” |
| M6 KAPU:314 | cf20a55 | — | −„=” +„mindig” −„tanulás”” +„tanulást hoz”” |
| M6.3:448 | cf20a55 | privacy-retention | −„„poszter\"” +„„poszter”” |
| M6.4:811 | 33d77d9 | — | +„> – a kimaradás lehetősége minden korosztályban megvan: érzékeny gyakorlatból bárki **indoklás nélkül passzolhat**.” |
| M6.A:61 | cf20a55 | — | −„Az M6.B pont innen,” +„Ha” −„mai kilépőkártyájától” +„4.4.3-ban kiosztod a kilépőkártyát” −„készítenél”*) indul.” +„készítenél”*), a résztvevők az M6.B-n abból is indulhatnak.” |
| M6.A:112 | cf20a55 | — | −„játék-eszközök” +„kilépőkártya, fejenként 1 (M6.A-MUNK-01; 4.4.3) * Opcionálisan játékeszközök” |
| M6.A:266 | cf20a55 | — | −„„Az M6.B pont innen,” +„„Ha” −„mai kilépőkártyádtól indul.”” +„4.4.3-ban kiosztod a kilépőkártyát (…), a résztvevők az M6.B-n abból is indulhatnak.”” |
| M6.A:509 | cf20a55 | — | +„> „Ha most nem szeretnél megszólalni, mondhatod azt is, hogy **passz**.”” |
| M6.A:526 | cf20a55 | — | −„/” +„vagy” −„elég.”” +„elég. > Ha most nem szeretnél megszólalni, mondhatod azt is, hogy **passz**.”” |
| M6.A:701 | 33d77d9 cf20a55 | — | +„* Tábla / flipchart az inkluzivitáselemzéshez (KVUCA ¦ KINEK NEHÉZ ¦ KIREKESZTÉS / RIZIKÓ ¦ INKLUZÍV VARIÁCIÓ; M6.A-POSZ” |
| M6.B:396 | cf20a55 | — | −„lapon?” +„játéklapon?” |
| M6.F:451 | cf20a55 | — | −„játékot /” +„játékot,” −„/” +„vagy” |
| M7 KAPU:54 | 729342a | — | −„etikus-AI,” +„etikus AI,” |
| M7 KAPU:171 | 729342a | — | +„a terv” |
| M7 KAPU:197 | 729342a | privacy-retention | −„leadásnál” +„leadásakor” |
| M7 KAPU:250 | 729342a | — | −„nyílik,” +„teljesül,” |
| M7 HUB:408 | 2a7cbc5 5c0cd4a | — | +„Ez a két mutató csak akkor használható, ha az `LMS – H5P runtime acceptance.md` szerinti teszt igazolja, hogy a Moodle r” |
| M7.2:70 | 5c0cd4a | — | −„/” +„vagy” |
| M7.2:762 | 729342a | — | −„flag-ek,” +„flagek,” |
| M7.2:891 | 729342a | — | −„/” +„vagy” |
| M7.2:893 | 729342a | — | −„**éves/modultervben**.”” +„**éves tervben vagy a modultervben**.” **Kulcs (fejlesztőnek; a jobb oldali leírások fenti sorrendjében):** 1. → Kvuca +” |
| M7.3:535 | 729342a | privacy-retention | −„M7.3-IKO-01::ALTTEXT)."” +„M7.3-IKO-01::ALTTEXT); az alt-szöveg szó szerint a Program terv §4 szerint: „Öt ikon: Idő & helyszín; Létszám & madrih–h” |
| M7.4:529 | 729342a | — | −„flag-ek” +„flagek” |
| M7.A:95 | 729342a | — | −„(mini-prezentáció” +„(miniprezentáció” −„ívére épül” +„ívéhez hasonló ívet követ” −„„Miért működik”);” +„„Háttér”);” −„háttér-rationáléja.",” +„háttérpárhuzama.",” |
| M7.A:464 | 729342a | — | −„**»Peula-tervezésnél legközelebb…«**” +„**‘Peula-tervezésnél legközelebb…’**” |
| M7.B:18 | 729342a | — | −„peula végén” +„peulán” |
| M7.B:212 | 729342a | privacy-retention | −„tanulság-körében” +„tanulságkörében” |
| M7.B:229 | 729342a | privacy-retention | −„tanulság-kérdése” +„tanulságkérdése” |
| M7.B:524 | 729342a | privacy-retention | −„lapját.” +„lapját (ha kevesebb van, az összes többiét).” |
| M7.B:562 | 729342a | — | −„**»A” +„**‘A” −„tervezésénél…«**” +„tervezésénél…’**” |
| M7.F:26 | 729342a | — | −„AI).” +„AI); a kvíz gyermekvédelmi kérdései az M3.3 anyagára és az M3.B lépéstérképére is épülnek.” −„Peula-terve” +„peula-terve” −„kérdést**,” +„kérdést** – különösen a nem teljesült kapurészhez tartozó leckéknél –,” |
| M7.F:80 | 729342a | — | +„* Tudja, hogy a kvíz gyermekvédelmi kérdései az M3.3 anyagára és az M3.B lépéstérképére is épülnek, ezért az M3.3-at is ” |
| M7.F:209 | 729342a | — | −„Peula-tervedet” +„peula-tervedet” −„Kvucá-checklist).” +„Kvucá-checklist); a kvíz gyermekvédelmi kérdései az M3.3 anyagára és az M3.B lépéstérképére is épülnek.” |
| M7.F:330 | 729342a | — | −„**Mini-kör” +„**Minikör” −„az?”” +„az? Ha most nem szeretnél megszólalni, mondhatod azt is, hogy **passz**.”” |
| Z.4:201 | 5fcf2b0 | — | −„kivétel (ugyanaz, mint az M3.3-ban):**” +„kivétel:**” |
| Z HUB:206 | c299aab | privacy-retention | −„1:1 meta-napló”)” +„fejlesztési jegyzet”)” |
| Program terv:221 | b429420 | privacy-retention | −„korosztály-térkép” +„korosztálytérkép” −„korosztály-térkép” +„korosztálytérkép” −„korosztály-térkép” +„korosztálytérkép” |

#### Személyes adat, megőrzés, hozzáférés — érintett megfogalmazás (68)

| Hely (HEAD) | Commit | Egyéb osztály | Változás (szószintű: − régi, + új) |
|---|---|---|---|
| Emberi jóváhagyás szükséges:514 | b429420 | — | +„¦ Narrációk besorolása (animáció hangsávja vagy önálló dia-narráció) ¦ **Besorolás:** `M1.1-NAR-03` = animáció hangsávja” |
| M0.4:342 | 1d9d15f df2792d | — | +„**Visszajelzés jó válasznál a 3. helyzetben (B):** > „Igen: hanihról csak indokolt célból készülhet fotó, és az is ellen” |
| M0.A:170 | df2792d | — | −„induló-szavak/rövid” +„indulószavak/rövid” −„stáb-dossziéba” +„stábdossziéba” |
| M0.A:180 | df2792d | — | −„induló-szó-rögzítést).” +„indulószó-rögzítést).” |
| M0.A:264 | df2792d | — | −„stáb-dossziéban)” +„stábdossziéban)” −„stáb-dossziéba” +„stábdossziéba” −„(stáb-dosszié” +„(stábdosszié” |
| M0.A:268 | df2792d | — | −„stáb-dosszié.” +„stábdosszié.” |
| M0.A:286 | df2792d | — | −„stáb-dossziéban” +„stábdossziéban” |
| M0.A:288 | df2792d | — | −„induló-szavak” +„indulószavak” |
| M0.A:366 | df2792d | — | −„stáb-dossziéba**” +„stábdossziéba**” −„**stáb-dossziéba” +„**stábdossziéba” |
| M0.A:502 | df2792d | — | −„induló-szavak” +„indulószavak” −„induló-szavakat**” +„indulószavakat**” |
| M0.A:629 | df2792d | — | −„stáb-dossziéban)?” +„stábdossziéban)?” |
| M0.A:657 | df2792d | — | −„induló-szavait**” +„indulószavait**” |
| M1 HUB:220 | ed4f52d | — | −„Megőrzésére” +„A mentorjegyzet megőrzésére” |
| M1.A:144 | ed4f52d | — | +„* **Felvétel:** a peulán a központi felvételi szabály érvényes (HUM-PRIV-02; `Adatvédelem – tanulói adatok és AI.md` 6. ” |
| M1.F:36 | ed4f52d | — | −„Megőrzésére” +„A mentorjegyzet megőrzésére” |
| M1.F:81 | ed4f52d | — | −„1 db” −„fogalom-térképhez;” +„fogalomtérképhez;” |
| M1.F:379 | ed4f52d | — | −„fogalom-térképhez” +„fogalomtérképhez” |
| M2.2:124 | cee9849 | — | −„(bekapcsolható)” +„(bekapcsolható; WCAG 1.2.2)” −„1.2.2).” +„1.2.3; hozzáférhetőségi sztenderd, 1. szakasz).” |
| M2.2:163 | cee9849 | — | −„ráégetett)” +„ráégetett; WCAG 1.2.2)” −„1.2.2).” +„1.2.3; hozzáférhetőségi sztenderd, 1. szakasz).” |
| M2.2:653 | cee9849 | — | +„(WCAG 1.2.2)” +„(WCAG 1.2.3; hozzáférhetőségi sztenderd, 1. szakasz)” −„(videó/hang, WCAG 1.2.2)” +„(videó/hang)” |
| M2.3:215 | cee9849 | — | −„(M2.3-VID-01::CAPTIONS)” +„(M2.3-VID-01::CAPTIONS; WCAG 1.2.2, A)” −„(M2.3-VID-01::TRANSCRIPT);” +„(M2.3-VID-01::TRANSCRIPT; WCAG 1.2.3, hozzáférhetőségi sztenderd 1. szakasz);” −„teljesíthető (WCAG 1.2.2, A)"” +„teljesíthető"” |
| M2.3:851 | cee9849 | — | +„(WCAG 1.2.2, A)” −„1.2.2, A)” +„1.2.3; hozzáférhetőségi sztenderd, 1. szakasz)” |
| M2.F:3 | cee9849 | — | −„a mentori 1:1 meta-naplóra vonatkozó” +„„Mentori fejlesztési jegyzet”” |
| M2.F:50 | 5bab331 cee9849 | — | +„és **füles**” −„+ **füles**.” +„magukkal.” −„lemerül).” +„lemerül); a közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges v” −„**Wifi**, előkészített Moodle / H5P belépéssel.” +„**Wifi** és működő Moodle … |
| M2.F:269 | cee9849 | — | −„gyorsan” +„gyorsan, név nélkül” +„A lapokat ezután visszaadod, mert ugyanaz a lap fut végig a peulán; ha mégis megtartod őket, az `Adatvédelem – tanulói a” |
| M2.F:374 | cee9849 | — | +„* A közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges válaszait” −„filcek” +„filcek: a tájékozódó tábla az M2 leckelistával és” −„témakérésekhez és” +„témakérésekkel, valamint” −„fogalomtérképhez” +„fo … |
| M3.1:168 | 045a876 | — | −„is."” +„is. A H5P Videónak nincs alt-mezője: a szöveges alternatíva a dián látható vagy a videó mellől megnyitható szövegként je” |
| M3.2:536 | 045a876 3ae0c09 b429420 | — | −„"Korosztály-térkép mini-táblázat” +„"Korosztálytérkép minitáblázat” +„"subtype": "ui-text",” −„„korosztály-térkép\",” +„„korosztálytérkép”,” −„mini-táblázat” +„minitáblázat” −„Mobilon görgethető /” +„Élő szövegként jelenik meg a dián, nem képként;” −„formába … |
| M3.F:3 | 3ae0c09 | — | −„a mentori 1:1 meta-naplóra vonatkozó” +„„Mentori fejlesztési jegyzet”” |
| M3.F:60 | 3ae0c09 | — | −„lemerül).” +„lemerül); a közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges v” −„kurzus).” +„kurzus); ha a wifi kiesik, a leckékhez az alacsony adatigényű, offline letölthető leckeváltozat a tartalékút  … |
| M3.F:287 | 045a876 | — | −„használni.” +„használni; ha a név nélkül begyűjtött lapokat mégis megtartod, az `Adatvédelem – tanulói adatok és AI.md` §3 „Név nélkül” |
| M3.F:540 | 3ae0c09 | — | −„működik.” +„működik; wifi-kiesésre megvan az alacsony adatigényű, offline letölthető leckeváltozat.” +„A közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges válaszait m” −„Tábla” +„Két tábla” −„filcek” + … |
| M4.4:710 | 4119d16 | — | −„szerkezetet (töröld ki a zárójeleket, ha zavar):” +„szerkezetet:” |
| M4.B:44 | 4119d16 | — | −„*(Telefon nem kell: ezen” +„*(Ezen” |
| M4.F:3 | 4119d16 | — | −„mentori 1:1 meta-naplóra vonatkozó” +„„Mentori fejlesztési jegyzet”” |
| M4.F:52 | 4119d16 | — | −„lemerül).” +„lemerül); a közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges v” |
| M4.F:54 | 4119d16 | — | −„flipchart” +„flipchart: **tájékozódó tábla** az M4 leckelistával és” −„témakérésekhez** és a közös fogalomtérképhez;” +„témakérésekkel** (M4.F-POSZ-01);” |
| M4.F:267 | 4119d16 | — | −„legszűkebb-hozzáférés” +„legszűkebb hozzáférés” +„A közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges válaszait m” |
| M4.F:362 | 4119d16 | — | −„fel.” +„fel (a név nélkül leadott lapok kezelése: `Adatvédelem – tanulói adatok és AI.md` §3, „Név nélkül begyűjtött papír munka” |
| M5 HUB:160 | 0932de3 | — | −„1:1 meta-napló”” +„fejlesztési jegyzet”” |
| M5.4:42 | 0932de3 | — | +„a kvízek és a kapuk eredményét,” −„A lecke közbeni vázlatot (a 4–5. dián) magadnak írod le, azt nem adod be.” +„A lecke közbeni vázlatot (a 4–5. dián) magadnak írod le, azt nem adod be.” |
| M5.4:291 | 105b451 | — | −„minta-táblázat” +„mintatáblázat” −„mini-sablon;” +„minisablon;” |
| M5.F:3 | 0932de3 | — | −„1:1 meta-napló”” +„fejlesztési jegyzet”” |
| M5.F:55 | 0932de3 | — | +„A közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik.” |
| M5.F:128 | 105b451 | — | −„fogalom-térkép” +„fogalomtérkép” |
| M5.F:188 | 0932de3 | — | −„(line 172, 222–224).” +„(4.2, 3. lépés; 4.3.1).” −„(line 335)” +„(5. ellenőrző lista)” |
| M5.F:400 | 0932de3 | — | +„* A közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik.” |
| M6 HUB:177 | cf20a55 | — | −„1:1 meta-napló”” +„fejlesztési jegyzet”” |
| M6.F:3 | cf20a55 | — | −„1:1 meta-napló”” +„fejlesztési jegyzet”” |
| M6.F:95 | cf20a55 | — | −„kérjétek,” +„kérje meg a résztvevőket,” −„lemerül).” +„lemerül); a közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges v” |
| M6.F:101 | cf20a55 | — | +„– az M6.1 és az M6.2 **alacsony adatigényű, offline letölthető leckeváltozata** (`LMS – hozzáférhetőségi sztenderd.md` §” |
| M6.F:103 | cf20a55 | — | −„flipchart” +„flipchart: **tájékozódó tábla** az M6 leckelistával, a játéklappal és” −„témakérésekhez** és a közös fogalomtérképhez;” +„témakérésekkel** (M6.F-POSZ-01);” |
| M6.F:180 | cf20a55 | — | −„matrica” +„post-it / cetli” |
| M6.F:289 | cf20a55 | — | −„"ai",” +„"human",” −„"AI-generált",” +„"emberi-felvétel",” |
| M6.F:323 | cf20a55 | — | −„(Moodle-ben” +„papíron” −„külön dokumentumban),” +„a saját eszközén, a közös eszközön nem (a Moodle-ben a javító leadás az F-peula után nyílik meg, ott adja le),” |
| M6.F:508 | cf20a55 | — | −„Tábla” +„A közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges válaszait m” −„filcek” +„filcek: a tájékozódó tábla az M6 leckelistával, a játéklappal és” −„témakérésekhez és” +„témakérésekkel (M6.F-POSZ- … |
| M7 KAPU:419 | 729342a | — | −„R4/R7” +„R4/R5/R7” |
| M7.4:564 | 729342a | — | +„> ❗ *Ide se írd be egy hanih nevét, képét, elérhetőségét, pontos helyét, egészségügyi vagy mentális állapotát, családi h” |
| M7.4:743 | 729342a | — | −„kvuca-metát.*” +„kvuca-infót.*” |
| M7.F:3 | 729342a | — | −„1:1 meta-napló”” +„fejlesztési jegyzet”” |
| M7.F:49 | 729342a | — | −„lemerül).” +„lemerül); a közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges v” +„és az M3.3 lecke” |
| M7.F:380 | 729342a | — | −„működik.” +„működik; a közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges vá” |
| Z.1:59 | 5fcf2b0 | — | −„szabad szöveges” +„adatot rögzítő” +„(a D-2 szerint a Z.1 szöveges lépései nem ilyenek)” |
| Z.3:61 | 5fcf2b0 | — | −„a” +„az LMS-Z-06 válaszainak” −„időt” +„sora („Szabad szöveges reflexió” vagy „Assignment / peulatervek”) DPO-döntés (BS-D6), addig” −„`Adatvédelem” +„activity valódi madrihnak nem nyitható meg (`LMS” −„tanulói adatok és AI.md` 3. szakaszának mátrixa rögzíti … |
| Z.A:23 | 5fcf2b0 | — | +„a” −„visszajelzés”” +„visszajelzés”: a „Záró reflexió + következő lépés”” |
| Z.A:40 | 5fcf2b0 | — | +„* **Felvétel:** a peulán a központi felvételi szabály érvényes (HUM-PRIV-02; `Adatvédelem – tanulói adatok és AI.md` 6. ” |
| Z.A:57 | 5fcf2b0 | — | −„induló-szavak**” +„indulószavak**” |
| Z HUB:190 | 5fcf2b0 | — | −„„Képzés-értékelés”**” +„„Képzési visszajelzés – név nélkül”**” |
