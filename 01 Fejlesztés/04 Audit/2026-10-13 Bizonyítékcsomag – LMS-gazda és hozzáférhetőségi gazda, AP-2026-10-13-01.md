# Jóváhagyási és bizonyítékcsomag – LMS-gazda / build-felelős és hozzáférhetőségi gazda (AP-2026-10-13-01)

> **Audit trail, nem kánon.** A 2026-10-13-i futás után a staging build és a runtime-bizonyíték teendői. A repó tervet és
> tesztlépést ír elő; eredményt nem állít. `RUNTIME_VERIFIED` csak dátummal, Moodle- és H5P-verzióval rögzített tényleges
> teszt után írható be (`02 Tervezet/RELEASE-READINESS.md`, G3b). A staging deployment ebben a futásban nem volt
> engedélyezett; ez a csomag a következő engedélyezett lépéshez készült.

## A gépi állapot (`python3 tools/content_integrity.py --release-report`, `8bb4d7d`)

- `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` (build-spec blokkoló: 0).
- `LEARNER-RELEASE-VERDICT: NO-GO` (learner-release blokkoló: 7 csoport). POST-BUILD: 76 feloldatlan `BUILD_OUTPUT` érték
  (az új LMS-M3-08 sorral együtt), 19 feloldatlan `RUNTIME_OUTPUT`, 38 nem `RUNTIME_VERIFIED` teszt; ellenőrzőlisták:
  POST-BUILD 14, RELEASE-EVIDENCE 8, FINAL-RELEASE-QA 15, SIGNOFF 4 nyitott; média: 1 asset fallbacken (M0.3-FOTO-01).

## Hogyan válaszolj

- Tesztenként: a `02 Tervezet/LMS – H5P runtime acceptance.md` Teszt-állapot táblájába a dátum, a Moodle- és H5P-verzió, a
  tesztfiók-szerepek (név nélkül) és az eredmény (megfelel / nem felel meg + eltérés). Képernyőkép személyes adat nélkül.
- A tracker-helyek: G3a/G3b + G5a/G5b → #3; G4 + G8 → #4 (`RELEASE-READINESS.md` tracker-tábla).
- Ha egy teszt nem felel meg, a spec érintett sora újranyílik; a repó nem állít helyette eredményt.

## A futásban új vagy módosult tesztlépések (a staging build után elsőként)

| RA pont | Mit kell visszaolvasni | Kapcsolódó döntés / kulcs | Szerep |
|---|---|---|---|
| 8. (RT-P0-08) | az új LMS-M3-08 GATE-CP: érték nélkül a kapukvíz zárva; „Még nem teljesítve” és „Teljesítve” értékkel is nyílik; az LMS-M6-05 pontbeállítása (Point, max 15, a rubrika minimum-beállítása; a pont rejtve, a tanuló a szintleírást és a kommentet látja); a célverzió rubrika-feliratát rögzíteni | D-15 (a), (d); ERT-9, LMS-4 | LMS-gazda; QA: értékelési felelős |
| 11. | az M3.3 P1–P4 passz-választón a `showContentTitle` mellett a soron következő szitu címe látszik-e (melyik csomópont címe jelenik meg) | D-08 (b); GYV-2 | LMS-gazda; QA: Memuna |
| 15. (RT-P0-15) | profilonként két mentor, két csoport: H5P-C, QUIZ-D/M, ASSIGN-S/M, GATE-CP; közvetlen URL; csoportba nem sorolt mentorfiók; a tanuló nem látja másét; az LMS-M0-06 role override; a pontkönyv a kurzus „Separate groups” módjával; szerkesztő tanár/menedzser név szerint; ADV-2 eljárásos hozzáférés | D-11; ADV-1, ADV-2, GYV-23 | LMS-gazda + DPO |
| 16. | a Z.4 Feedback üres kötelező beküldése nem sikerül („Not selected” is), a completion nem áll be; pozitív kontroll | D-16; ERT-3 | LMS-gazda; QA: értékelési felelős |
| 19. (RT-P0-19) | az M7 kapukvíz Review options mátrixa (LMS-M7-07) minden ablakban, tisztán tanulói fiókkal; az „After the quiz is closed” oszlop kvízszintű zárás nélkül; pozitív kontroll egy tesztkvízen | D-23; ERT-5, ERT-40 | LMS-gazda / TEST_OWNER |
| 21. (RT-P0-21) | az M2.1 SLIDE 4 statikus diája: nincs tárolt válasz, nincs mentett állapot, a completion nem függ tőle | D-15 (e); PRG-9 b | LMS-gazda |

## A fennálló bizonyíték-kapuk (változatlanul nyitva)

| Kapu | Mi kell | Kulcsok |
|---|---|---|
| RT-1 | valódi kontaktok helyes megjelenése (program, technika, mentor, Memuna) | M0:IMPL-9 |
| RT-2 | M0/M1 completion, unlock, próbálkozás, GATE-CP; H5P saved-state, xAPI/LRS, jogosultságok | M1:BIZT-G1-3, M1:ERT-G1-2, M1:IMPL-G2-4 |
| RT-3 | M4 kapu, completion, a11y, értesítés | M4:IMPL-G2-12 |
| RT-4 | M6.4 Branching Scenario végponti completion, passz, érintésmentes működés | M6:IMPL-G2-2 |
| RT-5 | M7 AI-csatorna audit és a no-AI út paritása (a DPO-val) | M7:IMPL-G1-11 |
| RT-6 | M7.2/M7.3 billentyűzetes és egyérintéses párosítás, mobil portrait | M7:IMPL-G2-10 |
| BK-02 | M5.3 completion-profil mindkét úton (RA 4.), a módszertani lektorral | M5:IMPL-G2-2 |
| BK-05 | ADV-4: H5P saved-state, xAPI/LRS, próbálkozás-riport visszaolvasása az M3 SAFE-1-nél és az M3.4 önjelzésnél; utána a DPO/Memuna technikaválasztása | M3:BIZT-G1-5, M3:BIZT-G2-7 |
| BK-08 | LMS-7: a hozzáférhetőségi gazda verdiktje az M7.2 diagram alt-szövegéről | M7:IMPL-G2-12 |

## A hozzáférhetőségi gazdának

- **LMS-7 (BK-08):** a `Program terv.md` M7.2-DIA-01 rövid altja és a látható kísérőszöveg együtt teljes értékű-e; addig a részletes alt marad.
- **Megfigyelés (nem validált finding):** az M3.1 Drag & Drop útja megmaradt, mert a HUM 14 LMS-2 csak az M3.2 és az M3.4 mellékútjáról döntött (mindkettő kivezetve: `ce04b9c`, `3b160fc`). A hozzáférhetőségi sztenderd :34 modulon belüli konzisztencia-szabálya miatt érdemes megnézni, kell-e az M3.1-en is húzásmentes egyetlen út.
- **G5a/G5b:** a független a11y pre-flight és a renderelt felület (felirat, leirat, kontraszt, billentyűzet, ≥24px célfelület) a `FINAL_RELEASE_QA` része.

## Mi kell a staging buildhez, és mi a learner release-hez

- **Staging build:** a gépi verdikt engedi (`READY_FOR_STAGING_BUILD`); a tényleges staging deploymenthez a projektgazda
  külön, kifejezett engedélye kell (ebben a futásban nem volt), és a G4 build-előfeltételei (dátumok, kontaktok, `#4`).
- **Learner release:** `NO-GO`. Kell hozzá: a fenti runtime-tesztek `RUNTIME_VERIFIED` állapota (G3b, G5b), a G1 Memuna
  „átnéztem” (GYV-24), a G2 DPO release-QA (ADV-E1–E3), a SIGNOFF-ok (SIG-1…SIG-6, ERT-19), a média-jogosultsági kapuk
  (J1, J2, V1, V3; SIG-6), a VO fix pack, a szerepköri döntések (D-01, D-04, D-05, D-07…D-10, D-13, D-14, D-17–D-21), majd
  a `FINAL_RELEASE_QA` és a go/no-go döntés.

## Kiegészítés a célzott QA után (`9788c05`)

A `8bb4d7d` célzott QA-ja (QA17; riport: `2026-10-13 Célzott QA – D-csomagok átvezetése (8bb4d7d), AP-2026-10-13-01.md`) után ehhez a szerephez került tételek. Ezek tesztlépések a `9788c05` után.

- **RA 15:** az M0 belépőkvíznél a Manual grading riport negatív tesztje („Also show questions that have been graded automatically” bekapcsolva, és közvetlen URL-lel: `mod/quiz/report.php?mode=grading`); a pontkönyvi LMS-M0-06-pontszám várt eredménye nyitott (KANON:QA17-BIZT-7), addig nem átmenő teszt; a Memuna ADV-2 szerinti hozzáférése.
- **RA 19:** a Review options alóli kivételhez a `mod/quiz:viewreports` és a `moodle/grade:viewhidden` együtt kell, ezért a tesztfiók tisztán tanulói szerepű legyen.
- **RA 26:** az LMS-M4-05 rubrikájánál a szintleírás és a komment látszik, a szintpont és a végső pont nem; a beállítás nevét rögzíteni kell.
- **RA 27 (új):** az LMS-M0-05 zárt állapota (rejtett, semmi nem hivatkozik rá), a megnyitás utáni új kohorszban kurzusteljesítési kritérium, futó kohorszban nem; a fórum „Group mode” = „No groups”.
- **RA 11:** a D-08 (b) `showContentTitle` a h5p-branching-scenario forrása szerint Branching Question-csomópontnál nem frissíti a fejlécet (M3:QA17-IMPL-1); a teszt várhatóan bukik, amíg a projektgazda más megjelenítési módot nem választ.
