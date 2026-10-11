# AUTOPILOT-LEDGER — a `/course-autopilot` tartós állapota

> **Audit trail, nem kánon, nem tanulói tartalom.** Egy autopilot-futás egyetlen tartós
> állapotnyilvántartása; egyetlen író: a fő session (`Edit`). Formátum és állapotgép:
> `.claude/skills/course-autopilot/ledger.md`. Ellenőrzés: `python3 tools/autopilot_ledger.py
> validate` (szerkezet) · `check` (végállapot) · `next` (folytatás). A ledger nem bizonyíték: minden
> állapotot a fájlban, a diffben vagy a parancskimenetben bizonyítunk, mielőtt ide kerül.
>
> **Aktív futás: `AP-2026-10-11-01`** (`next-version`, M0–Z, öt lencse). A felhatalmazás teljes szövege:
> `2026-10-11 Projektgazdai felhatalmazás – next-version M0–Z autopilot.md`. Az előző (harness v2-es) sablon
> a git-historyban marad (`99ba147`).

## Futás

| Kulcs | Érték |
|---|---|
| Run-ID | AP-2026-10-11-01 |
| Állapot | ACTIVE |
| Változat | next-version |
| Scope | M0-Z (M0, M1, M2, M3, M4, M5, M6, M7, Z) |
| Lencsék | pedagogy,assessment,language,safety,implementation |
| Felhatalmazás | next-version — projektgazda, 2026-10-11, szó szerint: „Projektgazdaként kifejezetten engedélyezem a módszertani képzés következő verziójának teljes M0–M7 + Z felülvizsgálatát, valamennyi validált objektív hiba javítását, beleértve a korábban POST-PILOT besorolású M0/M1 javításokat is, külön next-version munkaágon, a jelenlegi pilot változatának módosítása nélkül. Engedélyezem a szükséges rutinmódosításokat, ellenőrzéseket, generált médiakimenetek frissítését és helyi checkpoint-commitokat. Új szakpolitikai, gyermekvédelmi, adatvédelmi vagy értékelési döntést nem hozhatsz helyettem.” — fix: igen; commit: helyi munkaágon; push/PR/merge/governance-módosítás/éles Moodle/tanulói release: nem |
| Munkaág | next-version/AP-2026-10-11-01 |
| Bázis-commit | 213a4c5 |
| Indítva | 2026-10-11 |
| Záró QA | — |
| Korlátok | (1) Az M0+M1 pilot-freeze (2026-10-05) és a `POST-PILOT` címke ezen az ágon nem halasztási ok (felhatalmazás); a futó pilot forrása, a `main`, nem változik. (2) Lezárt döntés érvényes és nem nyílik újra: HUM 1–12. szakasz (N-M1-04: `2026-10-10 Projektgazdai döntés – N-M1-04…`), D-a…D-j, PILOT-1…4, a 2026-10-05-i scope-korrekció, a 2026-10-10-i Anna-döntések (CC-04: az M0.1 SLIDE 5 finomítása; CC-06: Moodle-összevetés külön build/runtime feladat; külső kutatási hivatkozás nem igazolt bizonyíték; kerülendő a szükségtelen módosítás és Anna természetes szövegezésének romlása). (3) Új szakpolitikai, gyermekvédelmi, adatvédelmi, értékelési döntés → `BLOCKED_HUMAN`; DPO-, szakértői, runtime-bizonyíték → `EVIDENCE_GATE`. (4) Hangok csak szerepnéven (nyilvános repó, 2026-10-03). (5) Generált médiát csak a `media_manifest.py build`, látható-szöveg pint csak a `--pin-visible` ír. |

## Modulok

| Modul | Review | Lencsék | Riport | Review-bázis | Javítás | Bizonyíték | Következő lépés |
|---|---|---|---|---|---|---|---|
| M0 | VERIFIED | pedagogy,assessment,implementation,safety,language | `2026-10-10 Validált findingok – M0 course-review, B sáv.md`; `2026-10-11 Validált findingok – M0, nyelvi lencse, AP-2026-10-11-01.md` | 82d0c7c (négy lencse); 886165b (language) | FIXING | — | FIX (átfedéssel, a projektgazda 2026-10-11-i gyorsítási döntése szerint): csak az M0 saját fájljai; a közös kánoni fájlok és a Z.A-helyek az összes review után |
| M1 | VERIFIED | pedagogy,assessment,implementation,safety,language | `2026-10-10 Validált findingok – M1 course-review, B sáv.md`; `2026-10-11 Validált findingok – M1, nyelvi lencse, AP-2026-10-11-01.md` | 82d0c7c (négy lencse); 886165b (language) | FIXING | `ed4f52d` fix(M1) + `506fa78` chore(media) | REGRESSION: célzott QA a `ed4f52d` diffjére (fut); a manifest-rész (M1:ERT-G2-6) a közös kánoni körben |
| M2 | VERIFIED | pedagogy,assessment,implementation,safety,language | `2026-10-11 Validált findingok – M2, AP-2026-10-11-01.md` | 886165b (a `02 Tervezet/` változatlan a 213a4c5 óta) | PENDING | — | FIX (a review-fázis után) |
| M3 | VERIFIED | pedagogy,assessment,implementation,safety,language | `2026-10-11 Validált findingok – M3, AP-2026-10-11-01.md` | 4e2b805 (a `02 Tervezet/` változatlan a 213a4c5 óta) | PENDING | — | FIX (a review-fázis után) |
| M4 | VERIFIED | pedagogy,assessment,implementation,safety,language | `2026-10-11 Validált findingok – M4, AP-2026-10-11-01.md` | 4e2b805 (a `02 Tervezet/` változatlan a 213a4c5 óta) | PENDING | — | FIX (átfedéssel, a projektgazda 2026-10-11-i gyorsítási döntése szerint) |
| M5 | VERIFIED | pedagogy,assessment,implementation,safety,language | `2026-10-11 Validált findingok – M5, AP-2026-10-11-01.md` | 4e2b805 (a `02 Tervezet/Modulok/M5` változatlan a 213a4c5 óta) | PENDING | — | FIX (átfedéssel, a projektgazda 2026-10-11-i gyorsítási döntése szerint) |
| M6 | RAW_SAVED | — | `2026-10-11 Validált findingok – M6, AP-2026-10-11-01.md` (nem követett, NYERS: 15/15 lencse-kimenet, 130 nyers ID) | ee209e5 | PENDING | — | VERIFY: klaszter-térkép (A.) → verifierek — a 2026-10-04-i M6 nyelvi review (régi formátum) után a modul változott (PR #19), ezért lefedettséget nem ad |
| M7 | RAW_SAVED | — | `2026-10-11 Validált findingok – M7, AP-2026-10-11-01.md` (nem követett, NYERS: 15/15 lencse-kimenet, 183 nyers ID) | 378d820 | PENDING | — | VERIFY: klaszter-térkép (A.) → verifierek |
| Z | RAW_SAVED | — | `2026-10-11 Validált findingok – Z, AP-2026-10-11-01.md` (nem követett, NYERS: 5/5 lencse, 57 nyers ID) | 378d820 | PENDING | — | VERIFY: klaszter-térkép (A.) → verifierek |

## Külső kapuk

| Kulcs | Típus | Tétel | Kell (mit, kitől) | Állapot |
|---|---|---|---|---|
| X-1 | PRECONDITION | Az N-M1-04 átvezetése (M1.1 SLIDE 5, HUM 12. szakasz, manifest, runtime-teszt) | RESOLVED 2026-10-11: PR #29 mergelve, `213a4c5` (tartalom: `ebf311e`, `96996e2`; `origin/fix/m1-privacy-learner-local` = `6dde193` a `main` őse) | RESOLVED |
| X-2 | PRECONDITION | A harness v2 mergelve, és a futás új sessionben, a repó gyökeréből indul | RESOLVED 2026-10-11: PR #26 mergelve, `d48bc2a` (`origin/gov/claude-harness-v2` = `ffee45e` a `main` őse); a session a repó gyökeréből indult, a projekt-sandbox és -settings betöltve | RESOLVED |
| X-3 | HUMAN_DECISION | Az Anna-megfeleltetés és a 2026-10-10-i döntési jegyzőkönyv a mainen | RESOLVED 2026-10-11: PR #28 mergelve, `0c7e299` (`695e5e4` a `main` őse). A CC-04/CC-06 HUM-átvezetése innen objektív tétel: `M0:ERT-8`, `M1:IMPL-G1-2` | RESOLVED |
| X-4 | HUMAN_DECISION | Adatkör, megőrzés, hozzáférés — DPO-döntések | DPO / jogi felelős: `M0:BIZT-7` (a bemutatkozó fórum megőrzési sora és tájékoztatója; a Program terv :228 szerint addig adatgyűjtő activity nem nyitható meg); `M1:BIZT-G2-4` (ASSIGN-M csoportszűkítés, szerkesztő tanári/menedzseri hozzáférés); `M1:IMPL-G1-5` (M1.1 SLIDE 1–2 választós tartalékútjának rögzítése); `M1:BIZT-G3-8` (M1.A Johari-cetlik sorsa, a tábla fotózása); DPO-vétó vagy -rész még: `M1:BIZT-G2-1`, `M1:BIZT-G2-6`, `M1:BIZT-G3-5`, `M1:ERT-G1-3`, `M1:ERT-G2-4`, `M1:IMPL-G2-10`, `M0:PED-8`; M2: `M2:BIZT-G1-3`, `M2:PED-G1-5`, `M2:BIZT-G2-6` (BIZT-R5: zsidóság-kör, választott pillér, LMS-M2-07 prompt), `M2:BIZT-G1-6`, `M2:BIZT-G2-3` (BIZT-2/BIZT-5 hozzáférés a „csak a mentorod látja” mögött; = az M1:BIZT-G2-4 kapuja), `M2:BIZT-G1-7` (szervezeti Google-fiók), `M2:BIZT-G1-8` (az LMS-M2-09 átolvasásának célja), `M2:BIZT-G3-10` (közös eszköz kezelése); DPO-rész még: `M2:IMPL-G2-1`, `M2:BIZT-G3-3`, `M2:BIZT-G3-5`, `M2:ERT-G1-5`; M3: `M3:IMPL-G2-6` (az M3.1 SLIDE 5 / M3.2 7A reflexiója tanuló-lokális vagy tárolt), `M3:BIZT-G1-5` (az M3.3 passz-választás tárolása, láthatósága), `M3:BIZT-G2-5` (az LMS-M3-05 olvasói köre), `M3:BIZT-G2-7` (az M3.4:188 önjelző kérdés tárolása), `M3:BIZT-G3-8` (az F-peula képzőjének hozzáférése); M4: `M4:BIZT-G1-2` (az M4.1/M4.3 reflexiója tárolt TEXT-C vagy tanuló-lokális), `M4:ERT-G1-10` (az M4.1 IV Free Text kérdése), `M4:BIZT-G1-5` (valós kvuca adata az M4.4-ben, ADV:83 review), `M4:BIZT-G2-5` (az M4.A:381 névvel aláírható kilépőkártyája); rész: `M4:ERT-G2-4` (hol tárolódik a rubrikaszint), `M4:PED-G2-9` (az (a) út); ide olvadt: `M4:BIZT-G2-2` (= `M2:BIZT-G2-3`); M5: `M5:BIZT-G1-5` (valós M4-es kvuca a KAPU R2-ben, az ADV:84 „M5 produktum” review-ja), `M5:BIZT-G2-1` (M5.A:437 kiskorú postere személyes telefonon), `M5:BIZT-G2-4` (M5.4 SLIDE 6 önellenőrzés rögzítésmentes útja), `M5:BIZT-G2-5` (M5.F:305 név nélküli tábla kis létszámnál); ide olvadt: `M5:BIZT-G2-2` (= `M2:BIZT-G2-3`; a második képző része = `M3:BIZT-G2-5`); rész: `M5:BIZT-G1-4` csoportszűkítés (= `M1:BIZT-G2-4`), `M5:BIZT-G2-9` szervezeti fiók (= `M2:BIZT-G1-7`) | OPEN |
| X-5 | HUMAN_DECISION | Gyermekvédelmi szabály-alkalmazás (Memuna, HUM-SAFE-02 QA) | Memuna (egyes tételeknél programvezető, DPO, szakmai lektor): `M0:BIZT-3` (SAFE-7 kiterjed-e az M0.4 SLIDE 3 2. helyzetére), `M0:BIZT-5` (csoportchat-szívatás jelzési küszöbe), `M0:BIZT-9` (két felnőtt az M0.A-n), `M0:PED-8` (egyéni utánkövetés a belépőkvíz 1–2. itemén; adatkör: DPO); `M1:BIZT-G1-4` (Memuna-mondat az M1.1 SLIDE 5 írása előtt), `M1:BIZT-G1-7` (kiskorú madrih önfeltárásának határa), `M1:BIZT-G2-10` (egyedi „nagyon nehéz helyzet” szöveg ↔ támogató blokk), `M1:BIZT-G2-3` (az ADV:241 mondata az M1.3 SLIDE 6-ba, a BIZT-G2-1 és a BIZT-G2-10 döntésével egy lépésben; a blokk kész), `M1:BIZT-G2-6` (feltárást tartalmazó kapubeadvány kezelése), `M1:BIZT-G3-2` (facilitátori minimum a peulákban), `M1:BIZT-G3-5` (anonimizálási korlát szóbeli példákra), `M1:BIZT-G3-9` (Memuna-utalás az M1.B terepi vállalásánál); M2: `M2:BIZT-G2-1` (P0, N-3: az LMS-M2-09 mentori átnézése és az „azonnal bevonja” ígéret), `M2:BIZT-G2-2` (P0, passz-út a kötelező krízis-esetválasznál), `M2:BIZT-G1-1` (KAPU §D ígéret ↔ határidő), `M2:BIZT-G1-2`, `M2:BIZT-G2-5` (munkaidőn kívüli elérhetetlenségi út), `M2:BIZT-G2-4` (SAFE-7 kiterjesztése az M2.4-re; rokon: M0:BIZT-3), `M2:BIZT-G3-2` (második felnőtt a peulákon; rokon: M0:BIZT-9, M1:BIZT-G3-2), `M2:BIZT-G3-3` (nyilvános pozicionálás az identitás-vonalon; + DPO), `M2:BIZT-G3-5` (valós vezetői helyzet; (a) = az M1:BIZT-G3-5 kapuja), `M2:BIZT-G3-9` (a társ ne kérdezzen tovább), `M2:PED-G2-7` (támogató visszajelzés a „túl sok” válaszra), `M2:IMPL-G2-7` (biztonsági doboz a mezőnél); rész: `M2:BIZT-G3-1` (b); M3: `M3:BIZT-G1-1` (KAPU ITEM 4: SAFE-7, kiskorú madrih szerephatára, elérhetetlenség), `M3:BIZT-G2-2` (a GK §3.3/§4.1 116-000-leírása), `M3:BIZT-G2-3` (az M3.3 akut doboza ↔ HUM-SAFE-02 (b)), `M3:BIZT-G2-4` (elérhetetlenségi út az M3.3 SLIDE 2-be), `M3:BIZT-G3-4` (SAFE-7 az M3.B 1. esetkártyáján), `M3:BIZT-G1-10` (GK §4.1-utalás az M3.1:280-ba), `M3:BIZT-G2-8` (az M3.4:363/:590 mércéje), `M3:BIZT-G2-9` („a Memuna és a hatóság dolga”), `M3:BIZT-G3-7` (kirekesztés testi megjelenítése az M3.A-n), `M3:PED-G2-1` (az M3.4 SLIDE 4/6 érzékeny gyakorlat, passz), `M3:IMPL-G2-5` (szcenárió-cím a passz-választón); Memuna-rész: `M3:BIZT-G1-8`, `M3:BIZT-G1-5`, `M3:BIZT-G2-5`, `M3:BIZT-G2-7`, `M3:PED-G1-4`, `M3:PED-G3-1`, `M3:PED-G3-2`, `M3:ERT-G1-5`, `M3:ERT-G2-2`, `M3:ERT-G2-7`, `M3:ERT-G3-2`, `M3:ERT-G3-8`, `M3:IMPL-G2-4`, `M3:IMPL-G3-9`; ide olvadt M3-helyek: `M3:BIZT-G1-3` (= `M1:BIZT-G2-6`), `M3:BIZT-G3-2` (= `M2:BIZT-G3-2`), `M3:BIZT-G3-3` (= `M1:BIZT-G3-2`); M4: `M4:BIZT-G1-6` (a GK:57 félmondata az M4.3:360 mellé), `M4:BIZT-G2-1` (képzői 1:1 megkeresés erős szorongásnál ↔ GK §4.2), `M4:BIZT-G2-9` („felkavart” állapot-e a szereplési szorongás; a második felnőtt alkérdése = `M2:BIZT-G3-2`), `M4:BIZT-G2-10` (a passzszabály az M4.B gyakorlataira); M5: `M5:BIZT-G1-1` (M5.2:313 szorongás-beszélgetés: passz és a Memuna-bevonás küszöbe; programvezetővel) | OPEN |
| X-6 | HUMAN_DECISION | Completion- és értékelési jelentésdöntések | projektgazda / build-spec gazda; QA: értékelési felelős, módszertani lektor: `M0:IMPL-3` (H5P-C completion = összefoglaló dia elérése vagy kikényszerített megválaszolás), `M0:ERT-3` (a D-d/D-i pontozatlan-választó elv általános-e); `M1:BIZT-G2-1` (N-1: valós, névtelenített helyzet az LMS-M1-07-ben; DPO-vétó), `M1:PED-G2-1` (az SBI kánoni hossza), `M1:ERT-G2-1` (a kész minta-SBI visszaadásának értékelői szabálya), `M1:ERT-G2-2` (B-sor ↔ hangnem-sor kettős levonás), `M1:IMPL-G2-2` (ASSIGN-M completion, D-h kiterjesztése), `M1:ERT-G2-4` (a KAPU item-bank tanulói activity vagy szerzői pool); `M1:NYELV-G2-4` (KAPU:55 S-„Erős” horgony olvasata; az M1:ERT-G2-5 S-része ettől függ), `M1:ERT-G2-5` (az M1.4 S-sora a NYELV-G2-4 döntése után; objektív rész: `M1:ERT-G2-5.obj`), `M1:NYELV-G2-8` (KAPU:79 zárójel jelentése); `M0:NYELV-G1-14` (a belépőkvíz projektgazdai itemszövegének nyelvi javíthatósága); M2: `M2:IMPL-G2-1` (mi adja az LMS-M2-03 grade-jét: „rögzítés nélküli” pollok ↔ „Receive a grade”; rokon: M0:IMPL-3), `M2:PED-G1-9` (a KAPU B. kvíze Moodle-activity-e; = az M1:ERT-G2-4 döntéstípusa), `M2:PED-G1-11` (beleszámít-e az „ÉN” az R1-be), `M2:NYELV-G1-13` (a határszabály-mutató alsó határa); maradék: `M2:IMPL-G1-5` (az M2 „a kapu nem teljesült” mondatai, ha kell); M3: `M3:ERT-G2-2` (R1/R2 feltárás nélküli helyzetben), `M3:ERT-G3-8` (az R2 „meg sem említi” szintje), `M3:ERT-G1-5` (életszerűség a blokkoló R4-ben), `M3:ERT-G1-11` (az M3_QUIZ Review options, slotváltozat), `M3:ERT-G2-7` (a HUM:473 elve a lecke-checkekre), `M3:IMPL-G2-14` (az M3.2 párosító kulcsa), `M3:BIZT-G1-7` (az ITEM 10 kritikus item-e); rész: `M3:PED-G2-1` (a kapus belépő); ide olvadt (= `M0:IMPL-3`): `M3:IMPL-G1-6`, `M3:ERT-G2-1`, `M3:IMPL-G2-1`; M4: `M4:PED-G1-2` (a Kapu 1 jelzése és határa), `M4:ERT-G1-1` (az M4.3 K3 kulcsa), `M4:ERT-G2-4` (mi váltja ki az M4.F-ajánlást, hol rögzül a rubrikaszint); rész: `M4:BIZT-G1-2`, `M4:ERT-G1-10` (completion-következmény); ide olvadt (= `M0:IMPL-3`): `M4:ERT-G1-4`, `M4:ERT-G2-2`, `M4:IMPL-G2-2`; M5: `M5:PED-G1-1` (a kapu pontozási egysége: táblázatsor vagy rubrikasor), `M5:PED-G1-2` (az R4 „gyakorlás”-horgonya ↔ GL:197), `M5:ERT-G1-1` (a QUIZ-D üres beadása; a CP-rész = `M0:IMPL-3`), `M5:ERT-G1-4` („Attempts allowed”, melyik próbálkozás a jelző), `M5:ERT-G1-9` (M5.2 SLIDE 8 ✅ „előbb a cél”), `M5:ERT-G2-3` (M5.4 SLIDE 6 ✅, a D-d/D-i új esete), `M5:ERT-G2-8` (M5.3 könnyen kizárható elosztó), `M5:NYELV-G1-11` (KAPU Q12 nézőpont ↔ kulcs); ide olvadt (= `M0:IMPL-3`): `M5:IMPL-G1-1` | OPEN |
| X-7 | EVIDENCE_GATE | Memuna írásos „átnéztem” bejegyzése (G1) | Memuna, G1 (GK :17, tracker #1): `M0:BIZT-1`; `M2:ERT-G1-7` (KAPU 5. item, §D, §E), `M2:BIZT-G2-8` (M2.4 önsértés / akut veszély; segélyvonalak a review napján); `M3:BIZT-G1-2` (hub, KAPU, kritikus slotváltozat), `M3:BIZT-G2-10` (M3.3–M3.4, SAFE-7 FINAL_RELEASE_QA, GK §6), `M3:IMPL-G3-4` (az M3.B, négy biztonságkritikus asset és az M3.F a GK §2 hatókörében); rész: `M3:IMPL-G2-11` (új gyermekvédelmi visszajelzés-szövegek QA-ja); `M4:PED-G1-7` (a HUM-PED-01 Memuna-QA-ja: M4.2 SLIDE 5 K2, M4.3:360); rész: `M4:NYELV-G1-2`, `M4:NYELV-G1-9`, `M4:IMPL-G1-3` (a javított gyermekvédelmi szövegek QA-ja) | OPEN |
| X-8 | RUNTIME | Célkörnyezeti Moodle-visszaolvasás | LMS-gazda, G3b/G4b/G8: `M0:IMPL-9` (a „Segítség és kapcsolatok” blokk kitöltése, RT-17, tanulói fiókkal); `M1:BIZT-G1-3` (RT-P0-24, N-M1-04), `M1:ERT-G1-2` (RT-P0-09/-13/-14, M1.1–M1.2 completion/unlock), `M1:BIZT-G2-2` (RT-P0-15 láthatóság), `M1:IMPL-G2-4` (RT-P0-01/-08/-09/-19, „Allowed attempts”), `M1:ERT-G2-6` (a rubrika tanulói nézete tanulói tesztfiókkal); `M2:BIZT-G1-9` (RT-P0-21, az M2.1 SLIDE 4 nem tárolt), `M2:BIZT-G2-9` (RT-P0-15 mentor-láthatóság), `M2:BIZT-G2-8` (RT 17: „Segítség és kapcsolatok” blokk); `M3:BIZT-G2-10` (RT-P0-09/-11/-13/-14/-22/-24 és RT-A11Y az M3.2–M3.4-re), `M3:BIZT-G1-5` (a passz-adat célverziós visszaolvasása), `M3:ERT-G1-13` (a rubrika-megjelenítés beállításnevei); `M4:IMPL-G2-12` (RT-P0-01/-06/-08/-09/-14/-15/-19/-22/-23 és RT-A11Y az M4-re; értesítő, `M4_ASSIGN` dátuma) | OPEN |
| X-9 | SIGNOFF | Értékelési szerepköri QA | értékelési felelős (az 1–2. itemnél Memuna): `M0:ERT-4` (a belépőkvíz projektgazdai itemszövegének utólagos QA-ja; answer key nem változik); `M3:BIZT-G1-2` (kalibráció, kétszemes döntési rend, modified-Angoff küszöb), `M3:BIZT-G2-10` (a HUM:463 kritikus követelmények QA-ja az M3.4:834-re) | OPEN |
| X-10 | HUMAN_DECISION | Programszintű és modulszerkezeti döntések | programvezető / modulgazda (egyes tételeknél build-felelős, médiafelelős, DPO): `M1:ERT-G1-3` (a hub 4. kompetenciájának záróreflexiós produktuma), `M1:PED-G1-8` (M1.1→M1.2 visszacsatolás, „4/5” mérés), `M1:PED-G3-9` (hub vagy peulafájl az irányadó), `M1:IMPL-G3-8` (PT:219 „Peulák” / „Extra / F-peula” blokk ↔ manifest, N-M4-07); `M1:NYELV-G2-9` (az SBI-sablon S-rése), `M1:NYELV-G3-16` (M1.A:277 „tedd meg nyugodtan”), `M1:IMPL-G1-8` (az M1.2 SLIDE 5 Drag & Drop megtartásának indoka, A11Y:33; objektív rész: `M1:IMPL-G1-8.obj`), `M1:PED-G3-8` (az M1.F létszámsora és kis létszámú változata); `M0:NYELV-G2-22` (M0.A:347 „páratlan a létszám”); M2: `M2:PED-G3-1` (lépésidők a rögzített blokkokon belül; HUM-OPS-01), `M2:PED-G3-11` (kis létszámú M2.F), `M2:ERT-G3-4` (M2.B 3. helyzet lezárása), `M2:IMPL-G1-3` (az M2.1 SLIDE 4 helye), `M2:IMPL-G3-6` (M2.B csoportszám a 8–20 fős sávban), `M2:IMPL-G3-7` (a M2-HUB-DIA-01 szerepe), `M2:NYELV-G1-12` (HUB:103 „megtartás” jelentése); M3: `M3:PED-G3-1` (lépésidők a peulablokkokban), `M3:PED-G3-2` (az M3.B 4.3.3 fiktív esetmondata), `M3:PED-G3-4` (az M3.F zárókérdése), `M3:PED-G3-9` (az M3.A kártyák hátoldala), `M3:PED-G1-4` (adjourning/storming ↔ bántalmazás gyakorlása), `M3:ERT-G2-5` (az M3.2 mikrocélja), `M3:ERT-G3-2` (az M3.B kimaradó 4. esetkártyája), `M3:ERT-G3-10` (javító út az F-peuláról hiányzóknak; programszintű, M1/M3/M5/M6/M7), `M3:IMPL-G3-9` (csoportszám és -létszám), `M3:IMPL-G2-4` (Image-csomópont a passz-választó után), `M3:IMPL-G2-11` (a hiányzó rossz-válasz-visszajelzések szerzője), `M3:NYELV-G3-6` (ki választja ki a 3 kártyát); M4: `M4:PED-G2-2` (lépésidők az M4.A/M4.B blokkjaiban), `M4:PED-G2-1` (az M4.B céljai ↔ a minimum), `M4:NYELV-G2-6` (az M4.B:326 feltétele), `M4:PED-G2-4` (kötelező vagy opcionális SBI), `M4:PED-G2-9` (a fókuszmondat továbbélése), `M4:ERT-G1-5` (a HUB:46 kompetencia ↔ mérés), `M4:ERT-G1-6` (az M4.3 hiányzó rossz-válasz-visszajelzései), `M4:ERT-G1-9` (az M4.3 SLIDE 4 kártyaszáma), `M4:BIZT-G1-7` (mely M4.3-itemek AI-generáltak), `M4:NYELV-G2-2` (az M4.4:62 tagmondat jelentése); M5: `M5:PED-G1-3` (M5.1 SLIDE 4 „formális” kulcsa ↔ határesetek), `M5:PED-G1-4` (hiányzó tanulói visszajelzések; objektív rész: `M5:PED-G1-4.obj`), `M5:PED-G1-6` (a „célzott felzárkóztatás” végrehajtója), `M5:PED-G2-6` (blokkidők az M5.A/M5.B/M5.F-ben; objektív rész: `M5:PED-G2-6.obj`), `M5:PED-G2-14` (mozgás nélküli részvétel a sarokjátékban), `M5:ERT-G2-9` (a valós kvuca-sor kötelező vagy opcionális), `M5:NYELV-G2-14` (az M5.A zárókörének minimuma) | OPEN |
| X-11 | HUMAN_DECISION | LMS-konfigurációs döntések | LMS-gazda + DPO + hozzáférhetőségi gazda: `M1:IMPL-G2-10` (az M1.4 kapu „Accepted file types” és fájlszám, korpusz-szinten); `M3:IMPL-G2-2` (a Drag and Drop mellékút; vétó: hozzáférhetőségi gazda); rész: `M3:IMPL-G2-4` (alt-szöveg a képcsomóponthoz); M5: `M5:IMPL-G2-2` (az M5.3 §3.6 felidézésének H5P-típusa, N-M5-08; objektív rész: `M5:IMPL-G2-2.obj`), `M5:PED-G2-11` (önellenőrzés a felidézés után; ugyanaz a döntési pont) | OPEN |
| X-13 | HUMAN_DECISION | Terminológiai / kánoni forrásütközés (modul ↔ Glosszárium) | modulgazda + értékelési felelős, a Glosszárium gazdájával (ken-vezető / mozgalmi felelős QA): `M1:NYELV-G1-14` (SBI „S” = helyzet vagy szituáció); projektgazda (QA: ken-vezető / mozgalmi felelős): `M0:NYELV-G2-11` (a Glosszárium:27 „kerüld” szabálya a kisbetűs „dugma isit vagy” alakra; M2-helyek: `M2:NYELV-G1-14`); projektgazda, a Memuna vétójával: `M2:NYELV-G2-3` (M2.4 „transzparens” ↔ HUM-SAFE-02 „átlátható”); M3: `M3:IMPL-G2-15` (az M3.4 kánoni leckecíme, „Do / Don’t”), `M3:NYELV-G2-3` (az LMS-M3-05 tanulói neve), `M3:PED-G3-13` (a „Leviatán – év eleji stáb” címke; ha someres szóhasználat: X-14) | OPEN |
| X-14 | HUMAN_DECISION | Helyi someres ideológiai / értéktartalmi döntések | projektgazda; QA: helyi ideológiai felelős (egyes tételeknél értékelési felelős, modulgazda, DPO): `M2:PED-G2-2` (mi számít someres értéknek az R2-nél, érték ↔ hangulat; ide: `M2:ERT-G1-4` és az `M2:ERT-G3-1` (b) része), `M2:ERT-G1-5` (a hub pillér-kompetenciája kimeneti vagy nem mért cél; tárolt ideológiai válasz nem vezethető be); feltételesen: `M3:PED-G3-13` (csak ha a „stáb” someres szóhasználat); M5: `M5:PED-G1-10` (a 3. kompetencia „saját szavaival elmagyarázza” mérése; az `M2:ERT-G1-5` kaputípusa) | OPEN |
| X-15 | HUMAN_DECISION | Jogi szakértői értelmezés: gyermekvédelmi jelzési kötelezettség (Gyvt. 17. §, Btk. 209/A. §; a GK §3.1:33 nyitva hagyja) | jogi szakértő; jóváhagyás: Memuna (GK §5); a nyilvántartás helyéről projektgazda: `M3:BIZT-G1-8` (HUB:40–43: ki tesz külső jelzést, milyen határidővel, a 17. § alkalmazása a szervezetre és a szerepekre; a madrihra külső jelzési feladat nem írható, a hub mondata nem törölhető), `M3:NYELV-G1-3` (HUB:41 „továbblépésnek büntetőjogi relevanciája” ↔ KAPU:359, Btk. 209/A. §); jogi rész: `M3:BIZT-G2-9` (maradhat-e a „hatóság” fordulat) | OPEN |
| X-16 | SIGNOFF | A szakmai lektor utólagos vétó/QA-ja és a release-jegyzőkönyv (HUM-PED-01; PT §9.3, Go/No-Go) | szakmai lektor; a jóváhagyó neve, dátuma és verziója a PT §9.3 release-jegyzőkönyvében (HUM:274), nem a G1 alatt (a G1 egyetlen jóváhagyója a Memuna, RR:39): `M4:PED-G1-7` (kvíz, disztraktor, rubrika, sablon utólagos QA-ja; „Blokkol: az M4 élesítése valódi madrihoknak”); rész: `M4:ERT-G1-1`, `M4:ERT-G1-6`, `M4:ERT-G1-9`, `M4:PED-G2-4`, `M4:PED-G2-3` (a lektor kvíz- és sablon-QA-ja); M5: `M5:ERT-G1-11` (a KAPU szakmai lektorálása, PT §9.2), `M5:BIZT-G1-6` (az AI-generált M5.1/M5.3/M5.4 assetek lektorálási bizonyítéka, PRODUCTION-DECISIONS D3; ide olvadt `M5:BIZT-G2-10`) | OPEN |
| X-12 | EVIDENCE_GATE | DPO írásos jóváhagyása (G2) | DPO, G2: `M1:BIZT-G1-3` (N-M1-04 DPO QA, BIZT-QA-1), `M1:BIZT-G2-2` (LMS-M1-05/-07 adatkezelés, ADV:230); `M2:BIZT-G1-9` (HUM-PRIV-01 DPO QA az LMS-M2-01/-06/-05-re), `M2:BIZT-G2-9` (HUM-PRIV-01 és D-j az M2.2–M2.4 adatfolyamaira), `M2:BIZT-G3-7` (az M2.F nem Moodle-ben vezetett mentorjegyzetének leltára); `M4:BIZT-G2-7` (az ADV:83, :87, :89 „Külön review” sorai, köztük az M4 peulabemutató; ADV:207); rész: `M4:IMPL-G2-12` (DPO-bizonyíték az M4 adatfolyamaira); M5: `M5:BIZT-G1-4` (az ADV:84/:87 „Külön review” sorai: M5/M6 produktum, F-peula mentorjegyzet, M5.4 Google-sablon; ADV:207; ide olvadt `M5:BIZT-G2-9`) | OPEN |
| X-17 | HUMAN_DECISION | Hanggyártási fix pack: a már gyártott narráció `@source`-szövegének javítása a hanggal együtt | médiafelelős / VO-gazda (a hanggyártás fix packja; kurzusoldalon `/course-fix`, utána build; a verifier-korlát szerint a VO-szöveg csak így változik): `M1:BIZT-G2-7` (M1.3 NAR-04-VO „beírni”), `M1:NYELV-G1-6` (M1.2 NAR-04-VO „vagy kifejezésre”), `M1:NYELV-G2-5` (M1.3 NAR-06-VO „az Assignmentben”; objektív rész: `M1:NYELV-G2-5.obj`) | OPEN |

## Findingok

| Kulcs | Súly | Típus | Verdikt | Állapot | Bizonyíték / döntési igény |
|---|---|---|---|---|---|
| M0:ERT-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:324–350 (SLIDE 3, helyzetenkénti helyes és téves visszajelzés); M0.2:276 (a 2. kérdés saját helyes visszajelzése); utána Memuna-QA: M0:BIZT-1 / G1 |
| M0:ERT-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | — (közös kánoni fájl: az RA-tesztpontok az összes review lezárása után; a HUB:181 két ágából melyik működik, az runtime-bizonyíték, X-8) |
| M0:IMPL-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | — (közös kánoni fájl: MAN, az összes review lezárása után; előbb az M1:IMPL-G3-8 ütközését kell feloldani, X-10) |
| M0:IMPL-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | — (közös kánoni fájl: MAN, az összes review lezárása után) |
| M0:ERT-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.2:195, :199–203 (opciók a listából szó szerint, típus Multiple Choice egyválaszos), :11 (típuslista) |
| M0:ERT-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.3:258 (Glosszárium:194 szabálya szó szerint) |
| M0:ERT-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (közös kánoni fájl: a HUM-átvezetés (CC-04, CC-06) az összes review lezárása után; az M0.1 SLIDE 5 kérdésének tartalma a pilot-visszajelzéssel, CC-04) |
| M0:PED-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.1:17–18 (mikrocél a hub 1. kompetenciájához és a 6. itemhez) |
| M0:PED-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a 45’-es és a 60’-es M0.A Blokk 2–3 lépésszintű vágási terve (a meglévő percsávokból nem rakható ki, új percszám kellene) — modulgazda / programvezető, a HUM-OPS-01 keretén belül (X-10); az objektív rész: M0:PED-5.obj |
| M0:PED-5.obj | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.A:647 (a „Madrih, nem terapeuta” lépés a megtartandók közé, az M0.2:504 ígérete szerint) |
| M0:PED-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.1:416 |
| M0:PED-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:569 (a NYELV-G2-3-mal egy blokkban) |
| M0:BIZT-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:172 (az M0.4:434 kánoni mondata szó szerint); utána Memuna-QA: M0:BIZT-1 / G1 |
| M0:BIZT-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:516, :580 (ADV:245 szó szerint); a runtime-visszaolvasás X-8 |
| M0:BIZT-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.2:473 (HUM:550 + GK:147) |
| M0:BIZT-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.1:51 (GK:80 + ADV:243; a HUM-SAFE-03 blokk változatlan); utána Memuna-QA: M0:BIZT-1 / G1 |
| M0:IMPL-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:11 (a); M0.3:338 (c); a (b) = M0:ERT-9, a (d) = M0:ERT-8 |
| M0:IMPL-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:566, :577; HUB:138; M0.3:365; M0.2:514 (a manifest „Név” oszlopa szerint) |
| M0:IMPL-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.3:162, :183 (az M0.3:145 `@source` alt-szöveg a validált soron kívül maradt) |
| M0:PED-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-1 |
| M0:BIZT-4 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-1 |
| M0:IMPL-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-1 |
| M0:IMPL-4 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-2 |
| M0:ERT-6 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:IMPL-2 |
| M0:PED-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-7 |
| M0:PED-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-8 (az IMPL-6 (d) része is ide olvadt; az IMPL-6 (b) része = M0:ERT-9) |
| M0:BIZT-7 | P0 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a bemutatkozó fórumposzt/-válasz megőrzési ideje és §3-sora, a „Bemutatkozó fal” külön review-ja, a megőrzési tájékoztató — DPO / jogi felelős (X-4) |
| M0:BIZT-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiterjed-e a SAFE-7 (HUM :567) az M0.4 SLIDE 3 2. helyzetére (késő esti 1:1 üzenet) — Memuna, HUM-SAFE-02 QA (X-5) |
| M0:BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a csoportchat-szívatás minden esetben Memuna-jelzés (M0.2), vagy csak súlyosság felett (M0.4, belépőkvíz) — Memuna (X-5) |
| M0:BIZT-9 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kötelező-e két felnőtt jelenléte az M0.A-n — programvezető + Memuna (X-5) |
| M0:PED-8 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: egyéni, támogató utánkövetés a belépőkvíz 1–2. itemének első téves válasza után, és ki láthatja ehhez az egyéni válaszokat — programvezető + Memuna; adatkör: DPO (X-5) |
| M0:IMPL-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a H5P-C completion jelentése (összefoglaló dia elérése, és a Completion-sorok ehhez igazodnak — vagy a megválaszolás kikényszerítése, szerkezeti átépítéssel) — projektgazda; QA: értékelési felelős (X-6) |
| M0:ERT-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a pontozatlan választók completion-elve (D-d/D-i) általános, vagy csak a felsorolt tételekre szól (az M0.1 completionje csak pontozatlan választókból áll) — projektgazda; QA: értékelési felelős (X-6) |
| M0:BIZT-1 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna, G1 (GK :17, tracker #1): írásos „átnéztem” az M0 gyermekvédelmi elemeire (X-7) |
| M0:IMPL-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda, G8/G4b, RT-17: a „Segítség és kapcsolatok” blokk kitöltése és visszaolvasása tanulói fiókkal (X-8) |
| M0:BIZT-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M0:IMPL-9 |
| M0:ERT-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | értékelési felelős (az 1–2. itemnél Memuna), G-kapu: értékelési QA: a belépőkvíz itemszövegének utólagos QA-ja (X-9) |
| M0:PED-7 | P2 | objektív | ELVETVE | REJECTED | ízlésbeli: a SLIDE 7 szándékosan sűrít; kár nem bizonyított (verifier) |
| M0:PED-9 | P2 | objektív | ELVETVE | REJECTED | pedagógiai preferencia: az M0.4 SLIDE 4 1. szabálya az M0.2:430 megerősítő ismétlése (verifier) |
| M0:ERT-5 | P1 | objektív | ELVETVE | REJECTED | az M0.1-rész a PED-3 duplikátuma; a hub 2.2/2.5 mérés nélkülisége a lezárt D-4-ből és a puha kapuból következik (verifier) |
| M0:ERT-10 | P2 | objektív | ELVETVE | REJECTED | item-írási preferencia: az M0.3:193 formatív, a visszajelzés tanít (verifier) |
| M0:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.2:348 (a „-nak” minősítés megmaradt); utána Memuna-QA: M0:BIZT-1 / G1 |
| M0:NYELV-G1-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.2:40 (GK:80 formula betűhűen) |
| M0:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.2:285 („kisebb tétű”) |
| M0:NYELV-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.1:200, :300; M0.2:285; M0.3:254, :293; `@asset` M0.2:142 (build: 69c2017) |
| M0:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.2:264 (✅ és jelentés változatlan); M0.3:251, :257, :303, :313; utána Memuna-QA: M0:BIZT-1 / G1 |
| M0:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; HUB:22, :38, :43, :77, :83, :109, :159; M0.2:173; `@asset` M0.2:141 (build: 69c2017) |
| M0:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.2:285; M0.3:139, :235; „célverzión”: M0.1:61, M0.2:62, M0.3:59, M0.4:61; `@asset` M0.3:102 (build: 69c2017) |
| M0:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; HUB:275, :283 (a >30% és az első hét változatlan) |
| M0:NYELV-G1-15 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; HUB:59 |
| M0:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a 45’-es percbontás címkéi (M0.A:152, :154, :155) a validált korlát szerint az M0:PED-5 vágási tervével egy lépésben változnak — modulgazda / programvezető (X-10); az objektív rész: M0:NYELV-G2-1.obj |
| M0:NYELV-G2-1.obj | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.A:147, :148 (60’-es címkék: Blokk 2, Blokk 3); M0.A:647 („Kihez fordulhatok?”) |
| M0:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:569 (az M0:PED-10-zel egy blokkban) |
| M0:NYELV-G2-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.A:636 (a :90 első mondata szó szerint); `@asset` M0.A:58 (build: 69c2017) |
| M0:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.A:638 (GK §4.1 5. lépésének formulája betű szerint) |
| M0:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.A:610 |
| M0:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:580 (csak a :565-ös fórumleírás utolsó pontja) |
| M0:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:567 (a HUB:131 alakja szó szerint) |
| M0:NYELV-G2-16 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.4:516 (a BIZT-8 blokkjában), :520, :540 |
| M0:NYELV-G2-17 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.A:474, :481; `@asset` M0.A:196 (build: 69c2017) |
| M0:NYELV-G2-18 | P2 | objektív | MEGERŐSÍTVE | IN_PROGRESS | — (az M0.A-rész kész: df2792d, M0.A:40, :102, :129, :168, :170, :174, :180, :264, :268, :286, :288, :321, :366, :367, :385, :427, :502, :629, :639, :657; build: 69c2017; a Z.A négy helye a Z-javítással egy menetben) |
| M0:NYELV-G2-21 | P2 | objektív | MEGERŐSÍTVE | FIXED | df2792d; M0.A:355, :426, :594, :598; `@asset` M0.A:520 (build: 69c2017) |
| M0:NYELV-G2-11 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a Glosszárium:27 „kerüld” szabálya kiterjed-e a kisbetűs „dugma isit vagy / dugma isit madrih” alakra (M0.2:26, :417; M0.4:25, :154, :248, :293, :296, :486; HUB:144, :238; M0.4-ILL-03; a HUB:235 projektgazdai itemtörzs) — projektgazda; QA: ken-vezető / mozgalmi felelős (X-13) |
| M0:NYELV-G1-14 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a belépőkvíz projektgazdai itemszövege (HUB:180) nyelvileg javítható-e (7. item „a completion állapotát” különírás; 4. item alanya) — projektgazda, az értékelési felelős QA-jával (X-6) |
| M0:NYELV-G2-22 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M0.A:347 „vagy páratlan a létszám” feltételének jelentése — modulgazda / projektgazda (X-10) |
| M0:NYELV-G1-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:NYELV-G2-11 (az M0.2:26 és a HUB:144 hely átvéve) |
| M0:NYELV-G1-3 | P2 | objektív | ELVETVE | REJECTED | a csatornaszabály szerkezete a korpusz kánoni alakja; a csere szűkítene (verifier) |
| M0:NYELV-G1-4 | P2 | objektív | ELVETVE | REJECTED | közvetlen hangnem, nem magázás (verifier) |
| M0:NYELV-G1-9 | P2 | objektív | ELVETVE | REJECTED | bevett fordulat (verifier) |
| M0:NYELV-G1-10 | P2 | objektív | ELVETVE | REJECTED | H5P típusnév, érvényes Markdown-escape (verifier) |
| M0:NYELV-G1-16 | P2 | objektív | ELVETVE | REJECTED | a nagykötőjel viszonyt is jelöl; preferencia (verifier) |
| M0:NYELV-G1-17 | P2 | objektív | ELVETVE | REJECTED | a beágyazott strong CommonMark szerint helyes (verifier) |
| M0:NYELV-G1-18 | P2 | objektív | ELVETVE | REJECTED | jelentésében többes alany; preferencia (verifier) |
| M0:NYELV-G1-19 | P2 | objektív | ELVETVE | REJECTED | informális, de egyértelmű címke (verifier) |
| M0:NYELV-G1-20 | P2 | objektív | ELVETVE | REJECTED | bevett szerkezet (verifier) |
| M0:NYELV-G2-2 | P2 | objektív | ELVETVE | REJECTED | szabályos különírás, diaszöveg (verifier) |
| M0:NYELV-G2-7 | P2 | objektív | ELVETVE | REJECTED | korpusz-szintű konvenció; a javasolt csere rontana (verifier) |
| M0:NYELV-G2-8 | P2 | objektív | ELVETVE | REJECTED | távirati képzői stílus (verifier) |
| M0:NYELV-G2-9 | P2 | objektív | ELVETVE | REJECTED | a „jelen lenni” kánoni alak (verifier) |
| M0:NYELV-G2-10 | P2 | objektív | ELVETVE | REJECTED | a szakszó megengedett; a csere jelentéseltolás (verifier) |
| M0:NYELV-G2-13 | P2 | objektív | ELVETVE | REJECTED | a hub is „komment”-et ír (verifier) |
| M0:NYELV-G2-15 | P2 | objektív | ELVETVE | REJECTED | szabályos szerkezet (verifier) |
| M0:NYELV-G2-19 | P2 | objektív | ELVETVE | REJECTED | szabályos szórend; a K1 (ERT-1) átírja (verifier) |
| M0:NYELV-G2-20 | P2 | objektív | ELVETVE | REJECTED | szabályos olvasat; nyomtatott biztonsági kártyát írna át (verifier) |
| M0:QA-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 1d9d15f; M0.2:473 (négy szerep konkrét elérhetősége + a Memuna és a mentor neve; HUM:550, GK:147); utána Memuna-QA: M0:BIZT-1 / G1 |
| M0:QA-NYELV-1 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:QA-BIZT-1 (ugyanaz a mondat; a „szerephez tartozó kontakt neve” javaslat a PILOT-3-on túlmenne) |
| M0:QA-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 1d9d15f; `@source` M0.3:145 alt-szöveg utolsó mondata a :162-höz és a HUB:260 kulcshoz igazítva (build: e16a4e1) |
| M0:QA-ERT-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:QA-IMPL-1 (az M0.3:145 alt-szöveg ↔ :162/:183) |
| M0:QA-NYELV-3 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:QA-IMPL-1 (ugyanaz a tényállás) |
| M0:QA-ERT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 1d9d15f; M0.1:11, M0.3:11 (a „Single Choice” = MC egyválaszos mód, nem Single Choice Set; az M0.2:11 a verifier szerint kimarad) |
| M0:QA-IMPL-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:QA-ERT-3 (az M0.2:11-re tett javaslatai elvetve) |
| M0:QA-PED-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 1d9d15f; M0.1:416 („mit mondtál vagy írtál ott”; a QA-NYELV-4-gyel egy szerkesztésben) |
| M0:QA-NYELV-5 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:QA-PED-1 (a „vagy gondoltál” javaslat új tartalom lenne) |
| M0:QA-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 1d9d15f; M0.1:416 (a gondolatjelpár helyén vesszők) |
| M0:QA-ERT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 1d9d15f; M0.4:348 (a 3A téves visszajelzése a helyes teendővel: HUB:240 + M0.4); utána Memuna-QA: M0:BIZT-1 / G1 |
| M0:QA-NYELV-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:NYELV-G2-1 (a 45’-es címkék; a sorrendi korlát miatt a M0:PED-5 döntésével, X-10) |
| M0:QA-NYELV-6 | P2 | objektív | ELVETVE | REJECTED | a PED-3 validált példamondata; az elosztó olvasat természetes, az ismétlés redundancia (verifier) |
| M0:QA-NYELV-7 | P2 | objektív | ELVETVE | REJECTED | az 1B perjele a forrásszöveg változatlan alakja (stílus); a 2B a M0:BIZT-3 miatt fagyasztott (verifier) |
| M0:QA-IMPL-3 | P2 | objektív | ELVETVE | REJECTED | az M0.A:7 metaadat rövid leckecímekkel, nem navigációs utasítás; a df2792d nem érintette (verifier) |
| M1:ERT-G1-1 | P0 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | ebf311e, 96996e2 (N-M1-04, PR #29): M1.1:98 „Moodle-oldali mező és tartalékút nem épül hozzá”, :763/:768 saját jegyzetes alapút, :792–794 a döntés szövege („lehetőleg”: 0 találat); MAN:45, :308; RA 24. pont (:105, LMS-M1-01); HUM 12. szakasz — célzott újraellenőrzés: `2026-10-11 Célzott újraellenőrzés – M1 NEEDS_RECHECK, AP-2026-10-11-01.md` |
| M1:IMPL-G1-2 | P1 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | ebf311e (N-M1-04): HUM 12. szakasz (:576–586) és a `04 Audit` jegyzőkönyv a szó szerinti szöveggel — célzott újraellenőrzés 2026-10-11; a finding CC-04/CC-06 HUM-átvezetési része nem ez a kulcs: = M0:ERT-8 (ott javítandó) |
| M1:PED-G1-4 | P1 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.2:618, :629, :651 (utasítás, magyarázat, visszajelzés; az 5 célszó, a pontozás és a mondatok változatlanok) |
| M1:BIZT-G3-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.F:270; M1.B:476 (az extra SBI csak kitalált helyzetről, nem javító próbálkozás; a NYELV-G3-10/-11/-12 egy lépésben) |
| M1:BIZT-G2-5 | P1 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.4:452–458 (beadás előtti doboz: „Miért?” = ADV:243, a két megőrzési sor = ADV:250, :252; kontakt-sor nincs, verifier-korlát) |
| M1:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a verifier-korlát szerint az ADV:241 mondata az M1.3:914–916-ba csak az M1:BIZT-G2-1 (X-6) és az M1:BIZT-G2-10 (X-5) döntésével egy lépésben megy; a blokk kész — Memuna (X-5) |
| M1:PED-G1-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.1:61, :930 (hídmondatok: a peulán nyitott és rejtett mező, a vakfoltot nem nyitják meg, nem kell megosztani) |
| M1:IMPL-G1-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.1:344 („Nem completion-elem”) |
| M1:ERT-G1-3.obj | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:86 (Check: 3 rövid kvízkérdés, 2 Single Choice + 1 igaz/hamis) |
| M1:ERT-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.2:781, :787, :789 (a három hiányzó kártya-visszajelzés; csak az M1.2-rész; az M1.1 Q2-rész elvetve: preferencia) |
| M1:IMPL-G1-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.2 SLIDE 5 Drag & Drop megtartásának indoka a fejlesztői megjegyzésben (A11Y:33) — szerző/modulgazda; indok híján a hozzáférhetőségi gazda dönt (X-10). Objektív rész: M1:IMPL-G1-8.obj |
| M1:IMPL-G1-8.obj | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.2:803 (húzásmentes alapút: rádiógombos Single Choice; a legördülő csak igazolt CP-típussal; a „mindig, nem feltételesen” marad) |
| M1:ERT-G2-6 | P2 | objektív | MEGERŐSÍTVE | IN_PROGRESS | — (a KAPU-rész kész: ed4f52d, KAPU:299; a manifest LMS-M1-04 sora a közös kánoni körben; a tanulói nézet visszaolvasása G3b, X-8) |
| M1:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: az S-sor (M1.4:482, :585) a KAPU:55 olvasatától függ (M1:NYELV-G2-4) — értékelési felelős (X-6). Objektív rész: M1:ERT-G2-5.obj |
| M1:ERT-G2-5.obj | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.4:492, :573, :611, :619 (az I-sor és a sornév a KAPU:67, :75 szerint; a NYELV-G2-11 egy lépésben; szint, pont, küszöb változatlan) |
| M1:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.4:317, :322–324, :328 (kérdés a KAPU Item 1 mintájára, időjelölt disztraktorok, visszajelzés; a ✅ :321 változatlan) |
| M1:ERT-G2-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.3:731–735 (a mondaton kívüli D opció törölve, a :735 visszajelzés igazítva; a ✅ és az A–C változatlan) |
| M1:BIZT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: hanggyártási fix pack — M1.3:814 `@source` NAR-04-VO „beírni” → „leírni”, a :750 spec ugyanabban a packban, utána build (D-1) — médiafelelős / VO-gazda (X-17) |
| M1:PED-G2-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.3:885 („Írd le magadnak, jegyzetbe vagy papírra” — a :799 mutatója; a név- és kitalálás-kitétel szó szerint marad) |
| M1:IMPL-G2-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; KAPU:305 (`GATE_CONFIRMED_M1`, LMS-M1-06, MAN §4, BS-D1, RT-P0-08), :306 (újranyitás „Manually”) |
| M1:IMPL-G2-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.4:18, :663 (csak Course Presentation), :153 (D-d/D-i + RA 14. pont) |
| M1:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.4:446 („M1.4 – SBI-beadandó”, MAN:50) |
| M1:ERT-G3-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.F:277 (a körbejárás M→H→K visszajelzése a nem teljesült rubrikasorra; a 45’ és a safer-working változatlan) |
| M1:IMPL-G3-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.B:148, :218, :495; `@asset` KART-02 :69, :86 (build: 506fa78) |
| M1:BIZT-G3-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.F:313 (tematikus, személyhez nem kötött kérdés, a :36 elve szerint) |
| M1:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.F létszámsora (6–20 fő) és a kis létszámú (egyéni / 1–5 fős) változat megírása; a létszám számszerű invariáns, kánoni érték nincs — modulgazda (X-10) |
| M1:BIZT-G3-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.A:488 („Mondhatsz passzt.” = GK:104, HUM-SAFE-03; a blokk nem került be) |
| M1:IMPL-G3-4 | P3 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.B:140, :491; `@asset` KART-02 :70, :74 (build: 506fa78) |
| M1:IMPL-G3-9 | P3 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.F:171, :172 (sorvégi `\`) |
| M1:PED-G1-8.obj | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:102 („(nem átírás)”; a :93/:97/:99 és az M1.2 Check érintetlen) |
| M1:BIZT-G3-8.obj | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.A:144 (felvételi szabály: HUM-PRIV-02, ADV §6:163 szó szerint; a cetlik sorsáról nem állít) |
| M1:ERT-G1-11 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: az állítás lényege igaz, a „hasznos információ” laza, de nem hamis; item-írási preferencia (a PED-G1-7 ugyanezt elvetette) |
| M1:ERT-G2-12 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: az M1.4:491–492 nem mond ellent a KAPU:300-nak; a szabály a tanulónak kedvez, kár nem bizonyított |
| M1:ERT-G3-11 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: a KAPU:255, :307 soronkénti M→H→K visszajelzést ír elő minden próbálkozásra; új bukott minta új értékelési tartalom lenne |
| M1:ERT-G3-12 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: bizonyított hiba nélkül elosztó nem cserélhető; item-írási preferencia (a fordítási rész = M1:NYELV-G3-8) |
| M1:IMPL-G3-12 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: múlt idejű történeti metaadat, tanulói/build-hatás nincs |
| M1:IMPL-G3-13 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: a `human` provenance kánonszerű; korpuszszintű minta, nincs szabály, amelyhez képest hibás |
| M1:PED-G3-11 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: az átfedést a forrás deklarálja (M1.A:372); új példa új pedagógiai tartalom; preferencia |
| M1:PED-G3-12 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: ugyanaz a tényállás, mint az elvetett M1:BIZT-G3-6 (fokozatos nyitás, nem megszegett ígéret) |
| M1:BIZT-G1-2 | P0 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-1 |
| M1:IMPL-G1-1 | P0 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-1 (a javaslat (a), (b), (f) pontja — „beviteli elem nem épül” — nem használható) |
| M1:IMPL-G1-3 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-1 (a MAN:308 datált kiegészítésének módszere ebből) |
| M1:PED-G1-1 | P0 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-1 |
| M1:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G1-2 (a mátrix-frissítési javaslat nem használható) |
| M1:ERT-G1-5 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:PED-G1-4 (a mondatcsere-javaslat túlmegy a minimálison) |
| M1:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:BIZT-G3-1 |
| M1:ERT-G3-5 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:PED-G1-3 |
| M1:ERT-G1-10 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G1-6 |
| M1:PED-G1-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:IMPL-G1-6 (objektív rész); tárolási rész = M1:IMPL-G1-5; a :80-as rész elvetve (nem bizonyított hiba) |
| M1:BIZT-G1-5 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-3.obj; a 4. kompetencia adatvédelmi korlátja = M1:ERT-G1-3 |
| M1:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-3.obj (a HUB:81 „6–8 slide” rész nem hiba, elhagyva) |
| M1:PED-G2-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G2-6 (az M1.4-MUNK-01-rész nem bizonyított hiba) |
| M1:IMPL-G2-5 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | szövegrész = M1:ERT-G2-5; megjelenítési rész = M1:ERT-G2-6 |
| M1:PED-G2-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G2-7 |
| M1:ERT-G2-11 | P2 | objektív | — | DUPLICATE | = M1:BIZT-G2-7 (levágott P2, beolvadt) |
| M1:IMPL-G2-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:PED-G2-6 |
| M1:PED-G2-11 | P2 | objektív | — | DUPLICATE | = M1:IMPL-G2-6 (levágott P2, beolvadt) |
| M1:PED-G3-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G3-1 (az (a) rész); a (b) rész (hangnem-kulcspont) elvetve |
| M1:ERT-G3-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G3-3 |
| M1:PED-G3-3 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G3-3 (a többletjavaslatok — A–D sarokjelölő, új „→” visszajelzés — nem kellenek) |
| M1:IMPL-G3-11 | P2 | objektív | — | DUPLICATE | = M1:PED-G3-8 (levágott P2, beolvadt) |
| M1:ERT-G3-9 | P3 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G3-4 |
| M1:PED-G3-4 | P3 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G3-4 (a „kézjel” alternatíva szerzői választás) |
| M1:ERT-G3-13 | P2 | objektív | — | DUPLICATE | = M1:IMPL-G3-9 (levágott P2, beolvadt) |
| M1:ERT-G1-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | HUB:102-rész = M1:PED-G1-8.obj; a HUB:93 „4/5”-rész = M1:PED-G1-8 |
| M1:PED-G2-12 | P2 | emberi-döntés | — | DUPLICATE | = M1:BIZT-G2-1 (levágott P2, beolvadt) |
| M1:ERT-G1-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G2-1 |
| M1:ERT-G2-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G2-1 |
| M1:ERT-G3-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G2-1 |
| M1:PED-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G2-1 |
| M1:PED-G2-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G2-2 |
| M1:PED-G1-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G1-3 |
| M1:IMPL-G2-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | döntési rész = M1:BIZT-G2-4; visszaolvasási rész (RT-P0-15) = M1:BIZT-G2-2 |
| M1:PED-G2-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G2-4 |
| M1:IMPL-G2-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G2-4 |
| M1:ERT-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:ERT-G3-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:IMPL-G3-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:IMPL-G3-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:IMPL-G3-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:BIZT-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:IMPL-G1-5 |
| M1:PED-G1-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:BIZT-G1-7 (a pedagógiai rész — áthelyezés SLIDE 3/4-re — preferencia, elvetve) |
| M1:IMPL-G1-4 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M1:BIZT-G1-3 |
| M1:PED-G1-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M1:BIZT-G1-3 |
| M1:IMPL-G3-2 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G2-4 (az „Allowed attempts” értéke, RT-P0-19; a peula-szöveg szűkítése nem javasolt) |
| M1:BIZT-G2-1 | P0 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: N-1 — kerülhet-e az LMS-M1-07 (M1.3 saját mini-SBI, tárolt, névhez kötött TEXT-C) mezőbe valós, névtelenített helyzet, vagy – mint az M1.4-ben – csak kitalált (MAN:48 nyitott; BSPEC-02 leltár: learner-release emberi döntés) — projektgazda; vétó: DPO (X-6) |
| M1:PED-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az SBI kánoni hossza 2–3 mondat (PT:106/:138/:142, hub, KAPU:21/:197) vagy 1–2 (M1.3:45/:801, M1.4:10/:450, M1.B:359, KAPU 4.1-minta); lezárt döntés nincs, a rubrika a hosszt nem pontozza — projektgazda / modulgazda + értékelési felelős (X-6) |
| M1:ERT-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.4:475–476 kész SBI a B kapuhelyzetre — kapjon-e a KAPU §5 értékelői szabályt a minta (közel) szó szerinti visszaadására, és cserélődjön-e a példa (a csere önmagában nem elég, M1.4:457) — értékelési felelős; QA: módszertani lektor (X-6) |
| M1:ERT-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a B-sor („becsúszik egy ítélkező szó”) és a hangnem-sor („enyhe minősítés”) ugyanazt vonja-e le (KAPU:126 „nincs kettős súlyozás”), és a 4.1 határeset-minta B ↔ hangnem indoklása közül melyik érvényes — értékelési felelős + módszertani lektor (X-6) |
| M1:ERT-G1-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a hub 4. kompetenciájának „záróreflexiós” produktuma sehol nincs — meglévő elemekre képeződjön le (és kerüljön ki a „reflexiós produktum” kitétel), vagy legyen új lépés; tárolt produktumként új adatkör (HUM-PRIV-01/DPO) — programvezető; DPO, ha tárolt (objektív része: M1:ERT-G1-3.obj) (X-10) |
| M1:IMPL-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-M1-05 (ASSIGN-M) saját completion-beállítása nincs rögzítve; kiterjeszthető-e a D-h kétállapotú mintája (SUBMITTED / CONFIRMED) az ASSIGN-M sorokra (a D-f szó szerint nem fedi) — projektgazda / build-spec gazda (X-6) |
| M1:BIZT-G2-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.4:502 „a kijelölt mentorod/értékelőd látja” mögött nyitott az ASSIGN-M csoport szerinti szűkítése (BIZT-5) és a szerkesztő tanári/menedzseri hozzáférés (BIZT-2) (ADV:104, :117); a mondat a döntés előtt nem változik — DPO (X-4) |
| M1:ERT-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU §3 item-bankja tanulói activity (manifest-sor: profil, completion, privacy a szabad szöveges Item 5–6-ra) vagy szerzői itempool (a KAPU:11/:28/:200/:308 igazodik) — projektgazda + értékelési felelős; DPO, ha activity (X-6) |
| M1:PED-G1-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a hub M1.1→M1.2 visszacsatolást és Johari-felidézést ígér (HUB:97/:99), és „4/5”-öt mér (HUB:93), a leckében egyik sincs — bekerüljön (Moodle-intróba), vagy a hub igazodjon — programvezető (objektív része: M1:PED-G1-8.obj) (X-10) |
| M1:PED-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: modulon belül a hub vagy a részletes peulafájl az irányadó — M1.A percbontás (hub:147–151), M1.F fogalomtérkép-poszter és „cél 4” (hub:172–203, :221–222), M1.B-végi analitikai kérdés (hub:275–278) — modulgazda / programvezető (a poszterről médiafelelős) (X-10) |
| M1:IMPL-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a PT:219 minden modulban „Peulák” és „Extra / F-peula” Moodle-blokkot ír, a manifest egyiket sem (MAN:114, :248) — MAN-bővítés vagy PT-pontosítás, programszintű, az N-M4-07-hez kötve — programvezető + build-felelős (X-10) |
| M1:IMPL-G2-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.4 kapu fájlos útjának „Accepted file types” és fájlszám-beállítása (üres mező = minden típus), a „két egyenértékű út” akadálymentességére figyelve; korpusz-szintű hiány — LMS-gazda + DPO + hozzáférhetőségi gazda (X-11) |
| M1:IMPL-G1-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: megengedett-e, hogy az M1.1 SLIDE 1–2 érzelmi önbevallásának választós tartalékútja követett H5P-C-ben tanulónként rögzítsen (a próbálkozás-riportot a nem szerkesztő tanár is látja, ADV:115; a D-d/D-i, a D-j és az N-M1-04 nem fedi) — DPO; addig a build a nem rögzítő szöveg + Tovább utat követheti (X-4) |
| M1:BIZT-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kapjon-e az M1.1 SLIDE 5 a mező (írás) előtt feltárást a Memunához irányító mondatot a Z.2:307 mintájára; „csak nálad marad” mondat az RT-P0-24 visszaolvasásáig tilos — Memuna. A hely a 82d0c7c óta változott (M1.1:763, :768; ebf311e, 96996e2: alapból nincs beviteli elem, „a saját jegyzetedbe … Nem kell beküldened”); a jegyzőkönyv 3. szakasza szerint a kérdés nyitott (X-5) |
| M1:BIZT-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.1:926 a (kiskorú) madrih önfeltárását a kvucához való közelség eszközeként keretezi határ-mondat nélkül — kell-e határ az M1.A:282 mintájára (az M1 nincs a Memuna G1-hatókörében, GK:17) — Memuna + szakmai lektor (X-5) |
| M1:BIZT-G2-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.3:914–916 és az M1.4:506–507 egyedi „ha nagyon nehéz helyzet” szövege kiváltandó támogató blokk (Gyermekvédelem §4.3:102), vagy feladatszintű adattakarékossági utasítás; az M1.4:508 Memuna-mondata nem törölhető — Memuna (X-5) |
| M1:BIZT-G2-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU:27 eszkalációjánál ki és hogyan veszi ki a feltárást tartalmazó beadványt (ADV:75), mi lesz a kapueredménnyel, és mi az alternatív beadási út (az M3-ra N-9-ként nyitott) — Memuna + DPO; értékelési felelős (X-5) |
| M1:BIZT-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mi lesz az M1.A önfeltáró Johari-cetlijeivel a peula után (kézírásos plakát, név nélküli munkalap vagy visszaadás), és fotózható-e a tábla — DPO (a HUM:149-hivatkozás átvezetése: M1:BIZT-G3-8.obj) (X-4) |
| M1:BIZT-G3-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a peulák képzői in-the-moment utasításának (M1.A:503–505, M1.B:389–391, M1.F:107) szó szerint át kell-e vennie a HUM-SAFE-03 facilitátori minimumát (felkavart kiskorút nem küldünk ki egyedül), vagy elég a képzőképzés (HUM-SAFE-05) — Memuna (X-5) |
| M1:BIZT-G3-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiterjedjen-e a „név és felismerhető részlet nélkül” korlát a szóbeli peula-példákra (M1.A:372 „a saját kvucádra szabva”, M1.B:157) — Memuna + DPO (X-5) |
| M1:BIZT-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kell-e az M1.B 4.4.2 terepi SBI-vállalásához „valódi gyermekvédelmi aggálynál vond be a Memunát” utalás (az M1.4:508 ugyanennek a tanulónak kimondja) — Memuna (X-5) |
| M1:BIZT-G1-3 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda (RT-P0-24, G3b); DPO (G2): N-M1-04 — az M1.1 H5P-C a SLIDE 5 szövegét nem tárolja-e (próbálkozás-riport, mentett állapot/`enablesavestate`, mentori hozzáférés, completion-függetlenség); RT-P0-24 `IMPLEMENTATION_TEST_REQUIRED`, DPO QA nyitott (BIZT-QA-1); addig saját jegyzetes, adatmentes út. Ide olvadt: IMPL-G1-4, PED-G1-2, az ERT-G1-2 SLIDE 5-része (X-8, X-12) |
| M1:ERT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda, G3b: az M1.1–M1.2 completion/unlock runtime-ja — SLIDE 1–2 pontozatlan választói, CP-completion, az M1.2 húzásmentes útja (RT-P0-09, RT-P0-13, RT-P0-14); csak a többletrész, a SLIDE 5-része = M1:BIZT-G1-3 (X-8) |
| M1:BIZT-G2-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO (G2; ADV:230, Adatvédelem §9 :207/:209); LMS-gazda (RT-P0-15, G3b): az LMS-M1-05 és az LMS-M1-07 adatkezelési jóváhagyása és láthatósági visszaolvasása két mentorral, két csoporttal, tesztfiókkal; ha más mentor is látja a beadást: P0. Ide olvadt: az IMPL-G2-3 visszaolvasási része (X-8, X-12) |
| M1:IMPL-G2-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda, G3b: RT-P0-08 (0/1/2/2 = 5 negatív eset, GATE-CP állapotmátrix), RT-P0-19 (javító próbálkozás az F-peula előtt nem indul, kézi nyitás, a legjobb megerősített eredmény számít; az „Allowed attempts” értéke a repóban nincs), RT-P0-01 (Max grade 8, Grade to pass 5), RT-P0-09 (LMS-M1-03 → -07 → -04 → -05 lánc). Ide olvadt: IMPL-G3-2 (X-8) |
| M1:ERT-G1-6 | P1 | objektív | ELVETVE | REJECTED | a „háromszor”-jel és az abszolút disztraktorok a tanított szabályt alkalmazzák; bizonyított hiba nélküli disztraktorcsere = preferencia (verifier) |
| M1:ERT-G3-3 | P1 | objektív | ELVETVE | REJECTED | az M1.B trió-checklist a saját deklarált célját követi, kánon nem köti a kapurubrikához; a háromfokú átalakítás tervezési preferencia (verifier) |
| M1:BIZT-G3-3 | P1 | emberi-döntés | ELVETVE | REJECTED | a cetliket a teljes csoportnak tették láthatóvá, a felolvasás név nélküli; szabálysértés (§4:61 passz) nem igazolható, a kézírás-felismerés spekuláció (verifier) |
| M1:ERT-G3-2 | P1 | objektív | ELVETVE | REJECTED | a Blokk 3 a kapus hiányokra fókuszál, a hangnem lényegét a „címke = ítélet” magyarázat fedi; negyedik kulcspont a fix 10’-be preferencia (verifier) |
| M1:IMPL-G3-1 | P1 | objektív | ELVETVE | REJECTED | az F-peula „jelenléti completion” útja szó szerint a lezárt 2026-10-02-i döntés (MAN:20, :149, RT:90), a MAN:248 kezeli; ellentmondás nincs (verifier) |
| M1:ERT-G1-9 | P2 | objektív | ELVETVE | REJECTED | formatív, nem kapuzott mikrocél; a Q1 opciói mind a 4 mezőt megnevezik; a mikrocél átírása célszöveg-preferencia (verifier) |
| M1:IMPL-G1-9 | P2 | objektív | ELVETVE | REJECTED | az M1.1-ILL-02 a11y-jegyzete egyezik a dia szabályával; a :952 zárójele laza fogalmazás, nem ellentmondás; az IKO-jegyzetek feltételesek (verifier) |
| M1:IMPL-G1-10 | P2 | objektív | ELVETVE | REJECTED | a Label-megjelenítési hatás feltételezés; a linkformát kánoni szabály nem írja elő — formázási preferencia (verifier) |
| M1:PED-G1-6 | P2 | objektív | ELVETVE | REJECTED | a rács és a narráció példái parafrázisok, az asset-spec szándékosan így rögzíti — multimédia-preferencia (verifier) |
| M1:PED-G1-7 | P2 | emberi-döntés | ELVETVE | REJECTED | a két T/F szándékosan ellentétes polaritással kérdez (M1.1:501); itemcsere bizonyított hiba nélkül — preferencia (verifier) |
| M1:PED-G2-5 | P2 | objektív | ELVETVE | REJECTED | a trió-checklist (M1.B:134–139) a saját célját követi; az M1.3 önellenőrzés átvétele preferencia (verifier, K17) |
| M1:ERT-G2-9 | P2 | emberi-döntés | ELVETVE | REJECTED | repón belül nincs ellentmondás (a KAPU:87 megengedi az én-perspektívás I-t); answer keyhez bizonyíték nélkül nem nyúlunk (verifier) |
| M1:ERT-G2-10 | P2 | objektív | ELVETVE | REJECTED | a KAPU a régi szóhasználatot történetiként jelöli (:43, :97, :100), a döntési szabály egyértelmű; kalibrációs zaj nem bizonyított (verifier) |
| M1:PED-G2-9 | P2 | objektív | ELVETVE | REJECTED | a tanulói narráció (M1.4:146–147) már őszintén keretez, a :154 kimondja, hogy a választás nem kerül át az Assignmentbe — élményminőségi preferencia (verifier) |
| M1:BIZT-G2-8 | P2 | emberi-döntés | ELVETVE | REJECTED | az M1.4:526 már a lezárt HUM-PRIV-01 szövegét alkalmazza, a .docx-út egyenértékű; az M1 SBI-beadandó a külön review listán van (ADV:80) (verifier) |
| M1:BIZT-G2-9 | P2 | emberi-döntés | ELVETVE | REJECTED | a KAPU:212/:224 „a hely külön kérdés” tényszerű tévesztő-magyarázat, nem ad négyszemközti utasítást, nem ütközik a HUM-SAFE-02-vel — ízlés (verifier) |
| M1:PED-G3-10 | P2 | objektív | ELVETVE | REJECTED | azonos tényállás a BIZT-G3-3-mal; az „előre jelezd” javaslat preferencia (verifier) |
| M1:BIZT-G3-6 | P2 | emberi-döntés | ELVETVE | REJECTED | nincs bizonyítható ellentmondás: az M1.A a vakfolt valódi feltárását halasztja, az M1.B opcionális, pozitív, passzolható visszajelzést köt — fokozatos nyitás (verifier) |
| M1:ERT-G3-6 | P2 | objektív | ELVETVE | REJECTED | a 4. kérdés opciói mellett típusjegyzet áll (M1.B:242–245); kár nem bizonyított, képzői szinten áthidalható (verifier) |
| M1:PED-G2-10 | P2 | objektív | ELVETVE | REJECTED | az M1.4:500 már kimondja, hogy az önkéntes újrabeadás nem veszélyezteti a teljesítést; tájékoztatási finomítás, kár nem bizonyított (verifier) |
| M1:IMPL-G3-10 | P2 | objektív | ELVETVE | REJECTED | a hozzáférhetőségi sztenderdben nincs mozgásra vonatkozó követelmény; nem pontozott bemelegítő játékok, a képző helyben alkalmazkodik (verifier) |
| M1:PED-G3-5 | P2 | objektív | ELVETVE | REJECTED | a 4 fős csoport forgása alulspecifikált, de végrehajtható (M1.B:350 „3 vagy 4 kör”, puffer); a forgásszabály új tervezés (verifier) |
| M1:PED-G3-6 | P2 | objektív | ELVETVE | REJECTED | a képző előzetesen átnézte az M1.1–M1.4-et; az „érzés az I-ben” válasza a fájlban (M1.F:331) és a mintakvízben ott áll; kár nem bizonyított (verifier) |
| M1:PED-G3-7 | P2 | objektív | ELVETVE | REJECTED | a „nézd meg a Moodle-ben” magában foglalja a belépést; sorrendi finomítás, kár nem bizonyított (verifier) |
| M1:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.2:912 („lusta vagy” felső szintű idézőjellel; a ✅ változatlan) |
| M1:NYELV-G1-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.2:891, :940 („vagy”; a kulcs és a drop-zóna címke változatlan) |
| M1:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: hanggyártási fix pack — M1.2:640 `@source` NAR-04-VO „vagy kifejezésre” törlése, a :573 spec ugyanabban a packban, utána build; célszó, pontozás marad — médiafelelős / VO-gazda (X-17) |
| M1:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:253 (háromrészes bontás; a három elem, az M1.B-utalás és a „fogódzóként” marad) |
| M1:NYELV-G1-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:77 |
| M1:NYELV-G1-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:132 („az SBI írójára”) |
| M1:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:220; M1.F:36 („A mentorjegyzet megőrzésére”; a szabály és a §3-hivatkozás változatlan) |
| M1:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:249; KAPU:23 („a teljesítéshez”; a küszöb változatlan) |
| M1:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:266 („leckénként”) |
| M1:NYELV-G1-15 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; HUB:177, :183, :222; M1.1:15, :66, :74; M1.2:28, :741, :964; M1.F:82, :379 (build: 506fa78; a „bulletpontokkal” és a „személyes kapcsolás” elvetve) |
| M1:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; KAPU:87; M1.4:637 („a többiek”) |
| M1:NYELV-G2-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.3:1028, :1031 |
| M1:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.3:310 („(S, B és I)”) |
| M1:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: hanggyártási fix pack — M1.3:1059 `@source` NAR-06-VO „az Assignmentben” → „a beadandóban”, a :941 spec ugyanabban a packban, utána build — médiafelelős / VO-gazda (X-17). Objektív rész: M1:NYELV-G2-5.obj |
| M1:NYELV-G2-5.obj | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; KAPU:200 („az M1.4 SBI-beadandóba”; a NYELV-G2-13 „kapuérett” egy blokkban) |
| M1:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; KAPU:109 („ad”; a küszöb változatlan) |
| M1:NYELV-G2-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; KAPU:132 („hatás helyett érzés”) |
| M1:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.4:619 („a beadvány írójával”, az M1:ERT-G2-5.obj blokkjában) |
| M1:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; KAPU:23, :30, :43, :97, :111, :113, :200, :271, :304; M1.4:14, :448, :582, :641, :648; M1.3:983 (`@asset`, build: 506fa78) |
| M1:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.4:136 |
| M1:NYELV-G3-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.F:55 |
| M1:NYELV-G3-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.A:316; M1.F:330 (a modul meglévő két alakja) |
| M1:NYELV-G3-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.B:227, :229 („hang”; a ✅ és a sorrend változatlan) |
| M1:NYELV-G3-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.B:476 (az M1:BIZT-G3-1 blokkjában) |
| M1:NYELV-G3-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.F:270 („szóljon nekem, és nyitok”, az M1:BIZT-G3-1 blokkjában) |
| M1:NYELV-G3-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.F:270, :361; M1.B:476 („SBI-beadandó” a tanulói idézetekben) |
| M1:NYELV-G3-13 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.B:139, :365; `@asset` MUNK-01 :102, :118 (build: 506fa78) |
| M1:NYELV-G3-15 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.A:520 („, de mi nem”) |
| M1:NYELV-G3-24 | P2 | objektív | MEGERŐSÍTVE | FIXED | ed4f52d; M1.F:81, :263 („1 db” törölve; az „1 oldalas” marad) |
| M1:NYELV-G1-14 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az SBI „S” elemének kánoni magyar neve — „helyzet” (Glosszárium:138, HUB:33, :231) vagy „szituáció” (HUB:241, KAPU:47 rubrikasor-név, M1.2:936, M1.4:482, M1.A:534, M1.B:181); 2. ↔ 3. kánoni forrás ütközik — modulgazda + értékelési felelős, a Glosszárium gazdájával (X-13) |
| M1:NYELV-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU:55 S-„Erős” horgonyának („idő ÉS/VAGY hely ÉS a helyzet szakasza”) érvényes olvasata; az M1:ERT-G2-5 S-horgony-átvezetése ettől függ — értékelési felelős (X-6) |
| M1:NYELV-G2-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU:79 4. rubrikasor vezérkérdésének „(megtartható kapcsolatban)” zárójele külön szempont vagy magyarázat — értékelési felelős / modulgazda (X-6) |
| M1:NYELV-G2-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az SBI-sablon S-rése határozói vagy tagmondatos (M1.3:803–805, :889–893; M1.4:470–471; M1.4-MUNK-01 spec — a sablon ellentmond a saját példáinak) — modulgazda; QA: értékelési felelős (X-10) |
| M1:NYELV-G3-16 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.A:277 „tedd meg nyugodtan” gyakorlati vonzata (új cetlire írás, ha a 3 kiosztott elfogyott); az (a)/(b) rész elvetve — modulgazda (X-10) |
| M1:NYELV-G3-19 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:NYELV-G1-14 (helyei: M1.A:534, M1.B:181, M1.F:338, :343) |
| M1:NYELV-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:BIZT-G1-7 (az M1.1:926 „ez” kétértelműsége: nyelvi többlet, azzal egy döntésben) |
| M1:NYELV-G1-1 | P2 | objektív | ELVETVE | REJECTED | bevett fordulat („amit mások látnak rólad”); answer-key opció átírása szükségtelen (verifier) |
| M1:NYELV-G1-4 | P2 | objektív | ELVETVE | REJECTED | természetes, a :471 definícióval következetes; VO-újragyártást nem indokol (verifier) |
| M1:NYELV-G1-5 | P2 | objektív | ELVETVE | REJECTED | hallgathatósági preferencia (verifier) |
| M1:NYELV-G1-16 | P2 | objektív | ELVETVE | REJECTED | stílus; szükségtelen mondatcsere (verifier) |
| M1:NYELV-G2-10 | P2 | objektív | ELVETVE | REJECTED | a konjunktív szabály közvetlenül előtte kétszer kimondva; félreolvasás nem bizonyított (verifier) |
| M1:NYELV-G2-12 | P2 | objektív | ELVETVE | REJECTED | enyhe anakoluthon, egyértelmű jelentés; stílus, Anna-szövegezés (verifier) |
| M1:NYELV-G3-1 | P2 | objektív | ELVETVE | REJECTED | az „ilyen lapjai” vonatkozása nem bizonyítottan hibás (verifier) |
| M1:NYELV-G3-2 | P2 | objektív | ELVETVE | REJECTED | a „mondotok” szabályos alak (verifier) |
| M1:NYELV-G3-5 | P2 | objektív | ELVETVE | REJECTED | bevett távirati képzői stílus (verifier) |
| M1:NYELV-G3-6 | P2 | objektív | ELVETVE | REJECTED | a „kapus” a korpusz bevett melléknévi alakja (verifier) |
| M1:NYELV-G3-7 | P2 | objektív | ELVETVE | REJECTED | produktív szóalkotás, ízlés (verifier) |
| M1:NYELV-G3-9 | P2 | emberi-döntés | ELVETVE | REJECTED | a visszajelzés kontextusban érthető (verifier) |
| M1:NYELV-G3-14 | P2 | objektív | ELVETVE | REJECTED | szabályos normamondat a gyermekvédelmi keretben (verifier) |
| M1:NYELV-G3-17 | P2 | objektív | ELVETVE | REJECTED | a „4 fős trió” a modul következetes csoportegység-neve (verifier) |
| M1:NYELV-G3-18 | P2 | objektív | ELVETVE | REJECTED | érthető; átfogalmazás regressziós kockázat (verifier) |
| M1:NYELV-G3-20 | P2 | objektív | ELVETVE | REJECTED | több fájlra kiterjedő stílusegységesítés (verifier) |
| M1:NYELV-G3-21 | P2 | objektív | ELVETVE | REJECTED | regiszter-preferencia képzői szövegben (verifier) |
| M1:NYELV-G3-22 | P2 | objektív | ELVETVE | REJECTED | kánoni határ-mondat, nem változtatható (verifier) |
| M1:NYELV-G3-23 | P2 | objektív | ELVETVE | REJECTED | bevett távirati stílus (verifier) |
| M1:NYELV-G3-25 | P2 | objektív | ELVETVE | REJECTED | szándékos kulcsüzenet; a csere rontana (verifier) |
| M1:NYELV-G3-26 | P2 | objektív | ELVETVE | REJECTED | a szerkezetből levezethető (verifier) |
| M1:NYELV-G3-27 | P2 | objektív | ELVETVE | REJECTED | az idősávok azonosítják a blokkot (verifier) |
| M2:BIZT-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU §D (:201) „a mentorod azonnal bevonja a Memunát” ígérete és a KAPU:24 megerősítési határideje (legkésőbb 24 … — Memuna (HUM-SAFE-01); vétó: DPO / jogi felelős … (X-5) |
| M2:BIZT-G1-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiegészüljön-e a KAPU 5. itemének visszajelzése (:113) a GK §4.1 kontakt-sorának szó szerinti tartalék útjával (mun … — Memuna, a SAFE-7 QA-val és az M2:ERT-G1-7 átnézésével együtt … (X-5) |
| M2:BIZT-G1-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: különleges (vallási/etnikai) adat gyűjtésének minősül-e a zsidóság-kör megnevezése az LMS-M2-06 válaszában (M2.1:48 … — DPO / jogi felelős; someres vonatkozásban a projektgazda (G2 … (X-4) |
| M2:BIZT-G1-4 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G1-4 |
| M2:BIZT-G1-5 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G1-2 |
| M2:BIZT-G1-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-M2-05 (identitás-jegyzet) adatkezelése: BIZT-5/BIZT-2 hozzáférés, megőrzési sor, a „Név (vagy becenév)” mező — DPO / jogi felelős, az LMS-gazdával; = az M1:BIZT-G2-4 kapuja (X-4) |
| M2:BIZT-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: van-e a tanulóknak szervezeti Google-fiókja az M2-HUB-MUNK-01 Google-sablonjához (HUB:203); ha nincs … — DPO + programvezető (X-4) |
| M2:BIZT-G1-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: igazolja-e a HUB:244 analitikai mutatója („legalább 2–3 konkrét … szabály”) az LMS-M2-09 szabad szöveges válaszaina … — DPO (az N-3 miatt Memuna); az M2:NYELV-G1-13 ennek kimenetét … (X-4) |
| M2:BIZT-G1-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO, G2 (tracker #2): a HUM-PRIV-01 szerinti DPO QA és az ADV §9 release-evidence / human-qa sorai (ADV:216 signoff) az … (X-12, X-8) |
| M2:BIZT-G2-1 | P0 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: N-3 — kötelező-e és milyen határidővel az LMS-M2-09 válaszainak mentori átnézése, marad-e az M2.4:37 „azonnal bevonja” ígérete — Memuna (HUM-SAFE-01); vétó/QA: DPO / jogi felelős (X-5) |
| M2:BIZT-G2-2 | P0 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M2.4 SLIDE 5 kötelező („Required”) krízis-esetválaszának passz-útja (M2.4:39 „Mondhatsz passzt” … — Memuna + programvezető (MAN:57 nyitott) (X-5) |
| M2:BIZT-G2-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M2.2:499 és az M2.4:37 „csak a kijelölt mentorod vagy értékelőd láthatja” mondata mögött a szerkesztő tanári … — DPO; ugyanaz a kapu, mint az M1:BIZT-G2-4 (X-4) |
| M2:BIZT-G2-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiterjed-e a SAFE-7 Memuna-QA (ma csak M3.3 S1) az M2.4 :193, :206–209 és :653 helyére — Memuna (rokon: M0:BIZT-3) (X-5) |
| M2:BIZT-G2-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kerüljön-e a GK §4.1 elérhetetlenségi útja (helyettes; 116-111 / 116-000 / 112; szerepnévvel … — Memuna; az M2:BIZT-G1-2-vel együtt (X-5) |
| M2:BIZT-G2-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: legyen-e pillér-semleges az LMS-M2-07 (név szerint tárolt, kötelező) záró mondatának promptja (M2.3:910 „abban a dö … — DPO / jogi felelős; someres vonatkozásban a projektgazda … (X-4) |
| M2:BIZT-G2-7 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:IMPL-G2-1 |
| M2:BIZT-G2-8 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna, G1 / GK §6 (tracker #1): írásos „átnéztem” az M2.4 önsértésről és akut veszélyről szóló elemeire (:37–39 … (X-7, X-8) |
| M2:BIZT-G2-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO / jogi felelős, G2 (tracker #2): a HUM-PRIV-01 és a D-j utólagos QA-ja az LMS-M2-07, -08 … (X-12, X-8) |
| M2:BIZT-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | M2.A:175 és az M2.A-POSZ-01 spec (:121): a titoktartási kivétel címzettje „felelős felnőtt” helyett a GK §4.1:82 utalása („a … (riport I.2) |
| M2:BIZT-G3-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a közös / tartalék eszköz további kezelési szabályai az M2.F-en (jelszómentés tiltása … — LMS-gazda + DPO (X-4) |
| M2:BIZT-G3-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kötelező-e az M2.A, M2.B és M2.F peulákon második, 18 év feletti felkészített felnőtt (az M2.A:280 „egy felnőtt vel … — Memuna + programvezető (rokon: M0:BIZT-9, M1:BIZT-G3-2 … (X-5) |
| M2:BIZT-G3-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: maradjanak-e az M2.A identitás-vonalán a 3–5. állítások (zsidósághoz fűződő viszony, család hatása … — Memuna + DPO (X-5, X-4) |
| M2:BIZT-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.A 4.3 1. lépése (:336–349) és az M2.A-MUNK-01 spec: a HUB:62 / HUB:25 kánoni fordulata szó szerint („a rajz a tanulónál ma … (riport I.2) |
| M2:BIZT-G3-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: (a) kiterjed-e a „név és felismerhető részlet nélkül” / „csak kitalált eset” korlát (GK §2:23) az M2.B 4.4 valós (S … — Memuna + DPO (X-5, X-4) |
| M2:BIZT-G3-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F 4.3 név nélküli mód (:268) és 4.2 (:218): az ADV §3:67 „név nélkül” feltételének átvétele és utalás a sorra … (riport I.2) |
| M2:BIZT-G3-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + privacy felelős, release-evidence: az ADV §9:207 activity-leltár (tároló, címzettek … (X-12) |
| M2:BIZT-G3-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G3-3 |
| M2:BIZT-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kerüljön-e az M2.A páros megosztás B-instrukciójába (:360 „kérdezz rá, és segítsd a másikat … — Memuna (X-5) |
| M2:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G1-5 |
| M2:ERT-G1-10 | P2 | emberi-döntés | ELVETVE | REJECTED | itemminőségi preferencia formatív kvízben (alacsony bizalom); az „Új kvíztételek” elv csak az M3-ra … (riport I.5) |
| M2:ERT-G1-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G1-6 |
| M2:ERT-G1-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | HUB:16, :29, :67: a „mind a 3 értékhez megfigyelhető viselkedés” állítás igazítása az M2.2 mikrocéljához (:12–16) és a HUB:30 … (riport I.2) |
| M2:ERT-G1-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:PED-G2-2 |
| M2:ERT-G1-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a hub 3. kompetenciájának első pontja (HUB:33 „Röviden elmondja, mit jelent számára a cionizmus, szocializmus … — projektgazda; QA: helyi ideológiai felelős, DPO (X-14; DPO-rész: X-4) |
| M2:ERT-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:260–261 (§E 2–3.): az R2 = 2 és az R3 = 2 mentori összefoglalójának igazítása a C. szintleírásához (R2: konkrét viselked … (riport I.2) |
| M2:ERT-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna, G1 / GK §2, §6 (tracker #1): írásos „átnéztem” a KAPU 5. itemére (:106–113) … (X-7) |
| M2:ERT-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.1:542 (SLIDE 6, Kérdés 2, rossz-válasz-visszajelzés): a NYELV-G1-5 szövege („Nem a szép magyarázat és nem a hibátlanság a … (riport I.2) |
| M2:ERT-G1-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G1-6 (grade-rész); a kvíz-rész = M2:PED-G1-9 |
| M2:ERT-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:IMPL-G2-1 |
| M2:ERT-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | MAN:54 (LMS-M2-02) Completion cellája az M2.2:31-ből és a D-i-ből szó szerint, a D-i azonosítóval … (riport I.2) |
| M2:ERT-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.2:27, :539, :541 és M2.3:766 (`@asset`, build), :791, :793: a Single Choice Set-ág és a „Single Choice Setben a helyes opc … (riport I.2) |
| M2:ERT-G2-4 | P2 | objektív | ELVETVE | REJECTED | preferencia: pass-küszöb nélküli Check, elosztó csak bizonyított hibánál cserélhető … (riport I.5) |
| M2:ERT-G3-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:PED-G3-3 (az (a) rész); a (b) rész az M2:PED-G2-2 döntési csomagjában |
| M2:ERT-G3-2 | P2 | objektív | ELVETVE | REJECTED | az M2.A:412 „mini” szóbeli zárókör más mondatkezdettel, jegyzetre utalás nélkül; hogy a jegyzet A.8-ába kerül … (riport I.5) |
| M2:ERT-G3-3 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:PED-G3-2 |
| M2:ERT-G3-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M2.B érték-szigetek 3. helyzete (:208–209 „nyers őszinteség vagy biztonság” … — modulgazda / módszertani felelős, a Memuna bevonásával (X-10) |
| M2:ERT-G3-5 | P2 | objektív | ELVETVE | REJECTED | az M2.B:350 visszacsatolása a feladat saját A/B logikáját követi; a KAPU R3 a jegyzet rubrikája … (riport I.5) |
| M2:IMPL-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | M2.1:18, :20, :465, :488, SLIDE 7 és HUB:63, :91: az M2.2:31/:476/:492/:705 mintájára az LMS-M2-06 („M2.1 – Szöveges válasz”) … (riport I.2) |
| M2:IMPL-G1-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M2:BIZT-G1-9 |
| M2:IMPL-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | M2.1:8 és :54 („7 slide”): a SLIDE 4 jelölése különálló, nem követett elemként, az LMS-M2-01 mondatának (MAN:16 … (riport I.2) |
| M2:IMPL-G1-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M2.1 SLIDE 4 („Melyik köröd szólal meg?”) helye és formája a tanulói úton … — build- / LMS-gazda + M2 modulgazda; DPO nem kell (X-10) |
| M2:IMPL-G1-4 | P1 | objektív | MEGERŐSÍTVE | OPEN | HUB:240–241 (§7 pillér-ág mutató): a D-j (HUM:562) és az M2.3:124 szó szerinti átvezetése (a pillér-választás fiókhoz kötött … (riport I.2) |
| M2:IMPL-G1-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | KAPU §0 Megerősítés sor (:24), E.5 (:263) és HUB §6 (:219–221): a MAN:61 / BSPEC-07 szó szerinti átvezetése (a mentor „Teljes … (riport I.2) |
| M2:IMPL-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU vagy HUB §6 és MAN:60 (LMS-M2-05): hivatkozásos specifikáció arról, mely KAPU-szakaszok kerülnek a tanulói Assignment-leírásba … (riport I.2) |
| M2:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.1:22, SLIDE 4 fejlesztői megjegyzése és :502: csak fejlesztői megjegyzés változik (a típust a lecke adja … (riport I.2) |
| M2:IMPL-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:58: az SCS-mondatrész törlése (az SCS nem ágyazható Question Setbe, és nincs kérdésenkénti visszajelzése) … (riport I.2) |
| M2:IMPL-G1-9 | P2 | objektív | ELVETVE | REJECTED | az M2.1:120 a felirat és a leirat együttes követelménye után hivatkozik a WCAG 1.2.2-re, ez a felirathoz helyes … (riport I.5) |
| M2:IMPL-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mi adja az LMS-M2-03 (M2.4 H5P-C) grade-jét: a MAN:56 „rögzítés nélküli” pollok ↔ „Receive a grade” — projektgazda mint build-spec gazda; tárolás: DPO (X-6; DPO-rész: X-4) |
| M2:IMPL-G2-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.2:33, M2.3:46, M2.3:766 (`@asset`, build), M2.4:55: a téves „a típust az RA rögzíti” kereszthivatkozás javítása a Z.1:57 / … (riport I.2) |
| M2:IMPL-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.2:124, :163, :653 és M2.3:215, :851: a felirathoz SC 1.2.2, a leirathoz SC 1.2.3 és a hozzáférhetőségi sztenderd 1. szakas … (riport I.2) |
| M2:IMPL-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.3 3. szakasz és az M2.3-EGY-02 spec (:11, build): a levezethető kötelező csomóponttípusok rögzítése (belépő oldal, KERET … (riport I.2) |
| M2:IMPL-G2-5 | P2 | objektív | ELVETVE | REJECTED | történeti fejlesztői jegyzet, nem ellentmondás (az M2.3:15 múlt idejű, az aktuális állapot a :42) … (riport I.5) |
| M2:IMPL-G2-6 | P2 | objektív | ELVETVE | REJECTED | a FOTO-01 a11y-metaadata feltételes, nem önellentmondó; a kontraszt-kockázat feltételezés … (riport I.5) |
| M2:IMPL-G2-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kerüljön-e szó szerint az M2.4 SLIDE 5 ⚠️/🆘 biztonsági doboza az LMS-M2-09 mezőhöz (a TEXT-C profil „adatvédelmi/bi … — Memuna (X-5) |
| M2:IMPL-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | M2.F 2.1 (:51–52) és 5. szakasz (:371–372): az A11Y:57 mondata szó szerint a közös / tartalék eszközre (saját fiók … (riport I.2) |
| M2:IMPL-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F:53 és :373: a POSZ-01 meglévő címének és státuszkorlátjának átvétele (tájékozódó tábla M2-leckelistával és név nélküli t … (riport I.2) |
| M2:IMPL-G3-11 | P2 | objektív | ELVETVE | REJECTED | tisztán fájlnévszintű eltérés tanulói hatás nélkül; a Glosszárium:194 nem tiltja a „Study Lab”-ot, az átnevezés linket … (riport I.5) |
| M2:IMPL-G3-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.A-KART-01 spec (:206) és notes (:223): az elavult „sor 154/149” hivatkozások és a már nem létező zsidóság-zárójelre utaló … (riport I.2) |
| M2:IMPL-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F:3: a megőrzési hivatkozás „mentori 1:1 meta-napló” sora helyett a §3 „Mentori fejlesztési jegyzet” sora (ADV §3:69 … (riport I.2) |
| M2:IMPL-G3-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:BIZT-G3-6 |
| M2:IMPL-G3-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F:320 és :391: „a Moodle-ben megadott határidőig” helyett a MAN:249 fordulata („a képző által kijelölt időpontig”) … (riport I.2) |
| M2:IMPL-G3-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a pillér-sztori műhely csoportszáma és csoportlétszáma a 8–20 fős sávban (az M2.B:331 „3–5 fős csoportok” és a pont … — M2 modulgazda (X-10) |
| M2:IMPL-G3-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a M2-HUB-DIA-01 fogalomtérkép-diagram (HUB:129, :149 „elsősorban az M2.F vizuálja”) szerepe az M2.F 4.3-ban … — M2 modulgazda, a médiafelelőssel (X-10) |
| M2:IMPL-G3-8 | P2 | objektív | ELVETVE | REJECTED | a hozzáférhetőségi sztenderd hivatkozott szabályai online, H5P- és diaelemekre szólnak … (riport I.5) |
| M2:IMPL-G3-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:BIZT-G3-4 |
| M2:NYELV-G1-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:135 (Item 7 visszajelzése): a „mi látszik belőle a kvucádon” fordított irányának javítása (a kvuca a madrihon lát … (riport I.2) |
| M2:NYELV-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:27, :178, :263: főnévi „újra beadás” → „újrabeadás”; az igei „újra beadhat(od)” alakok és az „1 normál + 1 javító” nem v … (riport I.2) |
| M2:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:253: „ha mind a 10-re pipa” → „ha mind a 10-re van pipa” (szűkítve); a :35 és a :48 szövege marad … (riport I.2) |
| M2:NYELV-G1-12 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a HUB:103 „egymás történeteinek megtartása” jelentése (megtartó figyelem vagy bizalmas kezelés) — az M2.A modulgazdája; bizalmas kezelés olvasatnál a Memuna (X-10) |
| M2:NYELV-G1-13 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ≥2 vagy ≥3 legyen a HUB:244 „legalább 2–3” határszabály-mutató alsó határa (4. kompetencia: 2–3, completion: 3) … — modulgazda + értékelési felelős (X-6) |
| M2:NYELV-G1-14 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:NYELV-G2-11 (M2-helyek: HUB:53, :83, :260; KAPU:42, :104; az M2.4 fájlneve és címe) |
| M2:NYELV-G1-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:174: „3 szintes … skála” → „3 szintű”; a szintnevek, a 0/1/2 és a küszöb nem változik, az M3 KAPU:313 scope-on kívül (riport I.2) |
| M2:NYELV-G1-16 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:146 (Item 8 visszajelzése): a két „sáv” → „szint” a törzs (:139) szavával; a törzs, az A–D opciók … (riport I.2) |
| M2:NYELV-G1-17 | P2 | objektív | MEGERŐSÍTVE | OPEN | „identitás-térkép” → „identitástérkép” az M2.A-ban (:72, :288, :328, :336, :339, :347; a :295/:296 build úton) és a PT:152-n (riport I.2) |
| M2:NYELV-G1-2 | P2 | objektív | ELVETVE | REJECTED | az M2.1:396 „más köreid erősödnek fel” természetes olvasata „helyzetenként más körök”, az összetévesztés feltevés … (riport I.5) |
| M2:NYELV-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.1:469 („köreidet … belőle”) és :475 („kört … bele … címeiket”) egyeztetési hibái és a :484 hiányzó vesszője (riport I.2) |
| M2:NYELV-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:37 (A.1): az „egy mondatban … melyik kör hogyan hat rám” igazítása a körönkénti egy mondathoz (:214, :135) … (riport I.2) |
| M2:NYELV-G1-5 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:ERT-G1-8 |
| M2:NYELV-G1-6 | P2 | objektív | ELVETVE | REJECTED | az M2.1:437 „A válaszod nem kerül mentésre.” helyes és egyértelmű; DPO-QA alatt álló … (riport I.5) |
| M2:NYELV-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:207: a „jobb oldal” térbeli utalás kiesik (a D. sablon 2–4. blokkja függőleges) … (riport I.2) |
| M2:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:165: „Le tud írni/mondani” → „Le tud írni vagy el tud mondani” (az M2.F:29 alakja) … (riport I.2) |
| M2:NYELV-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU (:54, :128, :135, :139, :146, :150, :157, :161, :168) és HUB (:55, :183, :240, :246): névelő a modulazonosító elé … (riport I.2) |
| M2:NYELV-G2-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:PED-G2-1 |
| M2:NYELV-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.2:25 és :453: „Multi Choice” → „Multiple Choice” (Edit), a :326 `@asset`-mező csak build úton … (riport I.2) |
| M2:NYELV-G2-11 | P2 | emberi-döntés | ELVETVE | REJECTED | az M2.2:523 „hogyan beszélsz róluk a hátuk mögött” általános alanyú olvasata természetes, a jelentés nem torzul … (riport I.5) |
| M2:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.4:688: „Az egyik határszabályom” → „Az első” (párhuzam a :691 és :694 sorral) … (riport I.2) |
| M2:NYELV-G2-13 | P2 | objektív | ELVETVE | REJECTED | az M2.3:713 szerkezete élőnyelvi, a :639 névmása a „terhet”-re mutat, nyelvtanilag helyes; stílus-kifogás, nem hiba (riport I.5) |
| M2:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.3:51 (zárójelben zárójel), M2.2:483–484 és M2.4:661, :689, :692, :695 (mondatzáró jel utáni kisbetűs „(pl. …)”): csak írás … (riport I.2) |
| M2:NYELV-G2-15 | P2 | emberi-döntés | ELVETVE | REJECTED | az M2.2:709–710 kissé nehézkes, de érthető előrevetítő mondat, a szándékolt jelentést az M2.3:50–53 rögzíti … (riport I.5) |
| M2:NYELV-G2-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.4:206 és :657: az első szintű egyes idézőjel (‘majd ha komolyabb’) helyett „…” … (riport I.2) |
| M2:NYELV-G2-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: átvehető-e az M2.4:208 és :653 gyermekvédelmi szabálymondataiban a „transzparens” helyére a HUM-SAFE-02 (GK §4.2) „átlátható” szava — projektgazda, a Memuna vétójával (X-13) |
| M2:NYELV-G2-4 | P2 | objektív | ELVETVE | REJECTED | az M2.3 változásnapló-maradványai történeti fejlesztői jegyzetek, nem ellentmondások … (riport I.5) |
| M2:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.4:580: a példalista sorrendcseréje, hogy a „például:” a „témakategóriák”-hoz kapcsolódjon … (riport I.2) |
| M2:NYELV-G2-6 | P2 | objektív | ELVETVE | REJECTED | a SLIDE 4–6 mezőnkénti adatvédelmi ismétlés funkcionális (az LMS-M2-09 tájékoztatója szó szerint ezeket kéri) … (riport I.5) |
| M2:NYELV-G2-7 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:PED-G2-11 |
| M2:NYELV-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.3:89: „*dugma isit*-nek” → „*dugma isitnek*” (HUM-SOMER-02); a kötőjeles összetételek („dugma isit-mondat”) változatlanok … (riport I.2) |
| M2:NYELV-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.3:594 (S1): „A többiek alig kapcsolódnak.” → „…kapcsolódnak be.”; más nem változik, pin (riport I.2) |
| M2:NYELV-G3-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.A:252: a „tartsd meg az előző kérdések jellegét” helyett a szett állításaira utaló megfogalmazás a „könnyed, nem felkavaró” minősítővel (:223) (riport I.2) |
| M2:NYELV-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.B-MUNK-03 mezői (:88, :89, :90, :94, :107): „commit” → „vállalás” (a törzs „vállalás-mondat” alakja), build úton (riport I.2) |
| M2:NYELV-G3-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.A:73, :379, :384: „Kis csoportos” → „Kiscsoportos”; a főnévi „kis csoport(ok)” (:52, :393, :456) marad (riport I.2) |
| M2:NYELV-G3-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F:167 (MUNK-01 purpose), :229 és :231 (POSZ-02): „Fogalom-térkép” → „fogalomtérkép”, csak build úton … (riport I.2) |
| M2:NYELV-G3-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.B:81 és M2.F:99: „Blokk-leírások” → „Blokkleírások”; csak a két M2-cím, a többi 17 fájl a saját scope-ja (riport I.2) |
| M2:NYELV-G3-14 | P2 | objektív | ELVETVE | REJECTED | az M2.A:58–61 pontja érthető, a „nem túl mély” látható helyen áll (E-M2-043 VALID_IMPROVEMENT) … (riport I.5) |
| M2:NYELV-G3-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.A:249 (felolvasandó keret): „valahova a skálán” → „valahol a skálán” (szűkítve) … (riport I.2) |
| M2:NYELV-G3-16 | P2 | objektív | ELVETVE | REJECTED | a „Fő célok (tanulói nyelven)” alatti harmadik személyű célok mind a hét F-peula közös sablonja … (riport I.5) |
| M2:NYELV-G3-17 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F:18 (Korosztály): „képzős madrihok” → „képzős madrihok / madrihot” (Glosszárium:72); a 15+ és a zárójel marad (riport I.2) |
| M2:NYELV-G3-18 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.A:7: a rövidített leckecímek helyett a hivatalos címek (mint a :24, :27); M2.F:55: „L1 = M2.1 … L4 = M2.4” (riport I.2) |
| M2:NYELV-G3-19 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F:147–148 (két szóközös kemény sortörés → `\`), M2.A:346, :350, :353, :364 (sorvégi szóköz, lógó üres idézetsor) … (riport I.2) |
| M2:NYELV-G3-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G3-2 |
| M2:NYELV-G3-20 | P2 | objektív | ELVETVE | REJECTED | a finding maga feltételes („csak akkor kell javítani, ha a Moodle-felület nem ezeket a jeleket mutatja”) … (riport I.5) |
| M2:NYELV-G3-21 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.B:449: „(kiemelten M7-ben)” → „(kiemelten az M7-ben)”; csak a névelő (riport I.2) |
| M2:NYELV-G3-22 | P2 | objektív | ELVETVE | REJECTED | a „jelöl magának konkrét pótlási tervet” szokatlan, de egyértelmű, nem felolvasandó szöveg; lexikai preferencia (riport I.5) |
| M2:NYELV-G3-3 | P2 | objektív | ELVETVE | REJECTED | a „kérdések / fogalomtérkép részben rövidítek” nem kétértelmű, a perjel házi stílus, nem nyelvtani hiba (riport I.5) |
| M2:NYELV-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F:50: a széttört „kérjétek, hogy hozzanak + füles” mondat helyreállítása (a füles az eszközlistába kerül) … (riport I.2) |
| M2:NYELV-G3-5 | P2 | objektív | ELVETVE | REJECTED | a „Kinek az értékei kapcsán van kérdése?” két olvasata ugyanarra fut ki, felolvasva érthető; preferencia (riport I.5) |
| M2:NYELV-G3-6 | P2 | objektív | ELVETVE | REJECTED | a :291 „a Somer-pillérek iránytűk” és a :320 nem zárja ki egymást; a metafora áthelyezése a fogalmi keretet írná át (riport I.5) |
| M2:NYELV-G3-7 | P2 | objektív | ELVETVE | REJECTED | a mondat jelentése egyértelmű, az „activity manifest” a kánoni sorrendforrás neve … (riport I.5) |
| M2:NYELV-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.B:47, :344, :345: „a két kockát” → „a két képet”, és a :343 címke egységesítése „élőkép-opció”-ra … (riport I.2) |
| M2:NYELV-G3-9 | P2 | objektív | ELVETVE | REJECTED | a „suliban, táborban, majd egyszer kvucával” nem nyelvtani hiba, a jelentés nem csúszik el; stílusbeli preferencia (riport I.5) |
| M2:PED-G1-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G1-1 |
| M2:PED-G1-10 | P2 | emberi-döntés | ELVETVE | REJECTED | az M1.2/SBI-kereszthivatkozás hiánya nem hiba, a finding maga új pedagógiai tartalomnak nevezi; preferencia (riport I.5) |
| M2:PED-G1-11 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: beleszámít-e az „ÉN” az R1 és az A.1 „legalább 3 kör” feltételébe (az M2.1:263–267 … — értékelési felelős (X-6) |
| M2:PED-G1-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G1-6 |
| M2:PED-G1-3 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:ERT-G1-3 |
| M2:PED-G1-4 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:IMPL-G1-5 |
| M2:PED-G1-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU D. sablon név szerint tárolt „Választott pillér” mezője (:235; az R3 ≥ 1 feltétele … — DPO / jogi felelős; someres vonatkozásban a projektgazda (G2 … (X-4) |
| M2:PED-G1-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:ERT-G1-5 |
| M2:PED-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:99: a „(opcionálisan M2.4)” igazítása az M2.A:7-hez (az M2.4 a peula utáni online lépés, nem előfeltétel … (riport I.2) |
| M2:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | E-M2-046 restauráció: egyetlen képzői kérés az M2.A 2.3-ban a :64 után, a mátrix szerinti szöveggel („aki szeretné … (riport I.2) |
| M2:PED-G1-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: elkészül-e a KAPU B. fogalmi kvíze (10 item) Moodle-activityként (a KAPU:26, :56 és a HUB:179 ígéri … — projektgazda + értékelési felelős; = az M1:ERT-G2-4 döntéstípusa (X-6) |
| M2:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | M2.3 mind a 9 mini-reflexiója (:534, :551, :568, :625, :642, :659, :716, :733, :750): az „Írj 1 mondatot:” egységes cseréje (riport I.2) |
| M2:PED-G2-10 | P2 | objektív | ELVETVE | REJECTED | a minták nem azonosak: az 1. minta hordozza a „nem ígérek titoktartást” elemet (GK §4), a javasolt csere ezt kivenné … (riport I.5) |
| M2:PED-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.4:809: a „záró dugma isit-mondatodat” birtokos előfeltevésének megszüntetése (törlés vagy előreutalás a jegyzet kapu szeri … (riport I.2) |
| M2:PED-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mi számít someres értéknek az R2-nél (KAPU:38, :183 „1 konkrét someres érték … érték … — projektgazda, értékelési felelős, helyi ideológiai felelős (X-14) |
| M2:PED-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.2:466 és :481: a „közülük” / „az előző listából” fordulat igazítása a SLIDE 3 VO-hoz (:438: a legközelebbi érték lehet … (riport I.2) |
| M2:PED-G2-4 | P1 | emberi-döntés | ELVETVE | REJECTED | a „22–28 perc” kézi becslés, mért adat nincs, az időtartam csak bizonyított hibánál változik … (riport I.5) |
| M2:PED-G2-5 | P0 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:BIZT-G2-2 |
| M2:PED-G2-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:IMPL-G2-1 |
| M2:PED-G2-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kell-e támogató visszajelzés az M2.4 emoji-check megterhelést jelző válaszára (a :340 „Összetett … — Memuna (HUM-SAFE-03); ide tartozik az M2:BIZT-G2-7 Memuna-alkérdése (X-5) |
| M2:PED-G2-8 | P2 | objektív | ELVETVE | REJECTED | a GK §4.1 megengedi a rövid utalást, az M2.4:210/:655 ennek megfelel, a :659 az 5. lépést helyben kifejti … (riport I.5) |
| M2:PED-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.3:466: a „nincs „egyetlen jó válasz”” tagmondat semlegesítése vagy törlése (minden ágban egy ✅ … (riport I.2) |
| M2:PED-G3-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a lépésidők elosztása a rögzített blokkokon belül (az M2.A Blokk 3 lépései 20–25 percet adnak a 15 perces sávban … — modulgazda; vétó/QA: programvezető (HUM-OPS-01) (X-10) |
| M2:PED-G3-10 | P2 | objektív | ELVETVE | REJECTED | a HUB:101 tágan jellemzi a peulát, az M2.2-előtanulás és a :430 mellett nem bizonyított ellentmondás … (riport I.5) |
| M2:PED-G3-11 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kapjon-e az M2.F (Létszám: 6–20 fő, M2.F:19) kis létszámú (1–5 fős) változatot a PT:286 „egyéni vagy kiscsoportos t … — modulgazda / programvezető (X-10) |
| M2:PED-G3-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.F 4.2 (:205, :209–212, :216): a jegyzetjavítás legyen az alapút, leckepótlás csak a javítandó sorhoz … (riport I.2) |
| M2:PED-G3-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | M2.B:377 és az M2.B-MUNK-03 spec (:90): a KAPU:230–231 ÉRTÉK-MONDATA szó szerint, a spec build úton … (riport I.2) |
| M2:PED-G3-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:BIZT-G3-2 |
| M2:PED-G3-5 | P2 | emberi-döntés | ELVETVE | REJECTED | a fogalomtérképet a peula saját 4. célja írja elő, az „1 → 2” mintagyakorlat új tevékenység; preferencia … (riport I.5) |
| M2:PED-G3-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:ERT-G3-4 |
| M2:PED-G3-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M2.B:380: a „mindenki (vagy aki szeretné)” helyett „aki szeretné”, és az M2.A:432 passz-mondata szó szerint (HUM-SAFE-03) (riport I.2) |
| M2:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M2:NYELV-G3-1 |
| M2:PED-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:IMPL-G3-6 |
| M3:BIZT-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: KAPU ITEM 4 (23:15-ös üzenet): SAFE-7 kiterjesztése, kiskorú madrih szerephatára, elérhetetlenségi mondat — Memuna; kulcsról projektgazda (X-5) |
| M3:BIZT-G1-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kerüljön-e az M3.1:280 dobozába a GK §4.1 rövid utalása („azonnal vond be a Memunát”); az M3.3 csak az M3.A után nyílik — Memuna + modulgazda (X-5) |
| M3:BIZT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna + értékelési QA, G1 (tracker #1): KAPU „átnéztem” (:14), kalibráció és kétszemes rend (:317), Angoff-küszöb (PT:277), segélyvonalak a review napján (X-7, X-9) |
| M3:BIZT-G1-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:BIZT-G2-6 (M3-többlet alkérdésként: a KAPU:309 eltávolítás menete, N-9, háromfős kétszemes olvasás) |
| M3:BIZT-G1-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:BIZT-G2-5 |
| M3:BIZT-G1-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.3 P1–P4 passz-választás egyéni tárolása és láthatósága (attempt tracking, BIZT-5), csak összesített-e a hub §7 elemzése — DPO + Memuna (X-4) |
| M3:BIZT-G1-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-6 |
| M3:BIZT-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: legyen-e az ITEM 10 kritikus item — projektgazda; QA: értékelési felelős + Memuna (X-6); az objektív szerepjavítás: M3:ERT-G1-7 |
| M3:BIZT-G1-8 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: HUB:40–43: ki tesz külső jelzést, milyen határidővel (Gyvt. 17. §), hol a nyilvántartás — jogi szakértő; Memuna; tracker: projektgazda (X-15) |
| M3:BIZT-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU §4 (:359–362): a GK §7:162 elsődleges forrása (2012. évi C. tv. 209/A. §, NJT) szó szerint; jogi állítás nem változik, a Máltai-sor másodlagosként marad (riport I.2) |
| M3:BIZT-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | M3.4 meta (:1–9) és MAN:65 (LMS-M3-04): a GK §2 / HUM 11. szakasz release-jelölése az M3.3:3–10 és a MAN:64 mintájára; „átnéztem” nem írható be (riport I.2) |
| M3:BIZT-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna, G1 (#1) + LMS-gazda, G3b (#3): M3.3–M3.4 „átnéztem”, SAFE-7 QA, GK §6 sorai, HUM:463 QA (M3.4:834), RT-P0-09…-24, RT-A11Y (X-7, X-8, X-9) |
| M3:BIZT-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: módosul-e a GK §3.3 / §4.1 116-000-leírása („nem általános szülői vonal” ↔ a szolgáltató leírása); utána M3.3:860, KAPU:365, IMPL-G3-3 — Memuna (X-5) |
| M3:BIZT-G2-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.3:548–552 akut doboza („ne szakítsd meg … felnőtt jelenlét”) ↔ HUM-SAFE-02 (b) és a kiskorú madrih szerephatára; SAFE-7-csomag — Memuna (X-5) |
| M3:BIZT-G2-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kerüljön-e az elérhetetlenségi út (az M3.3:751 mondata, szerepnévvel) a SLIDE 2-be (:309); az M2:BIZT-G2-5 csomagjában — Memuna (X-5) |
| M3:BIZT-G2-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-M3-05 olvasói köre (Memuna, második és fellebbezési képző ↔ „kijelölt mentor/értékelő”; M3.4:64, KAPU:317) — DPO / jogi felelős, LMS-gazdával (X-4) |
| M3:BIZT-G2-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-6 |
| M3:BIZT-G2-7 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: tárolható-e az M3.4:188 önjelző véleménykérdés követett H5P-C-ben (BIZT-5); nem törölhető, nem completion-elem — DPO; a mutatóról Memuna (X-4) |
| M3:BIZT-G2-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: gyengébb mércét sugall-e az M3.4:363 és :590 példája a :358 1:1-szabályához képest (GK §6:152 human-qa) — Memuna (X-5) |
| M3:BIZT-G2-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: maradhat-e „a Memuna és a hatóság dolga” (M3.3:697, :698, :705; KAPU:243, :248; GK §3.1:33 nyitott) — Memuna; jogi rész: jogi szakértő (X-5; X-15) |
| M3:BIZT-G3-1 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M3:IMPL-G3-4 |
| M3:BIZT-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.F:287, :387 (név nélküli lapgyűjtés): a „név nélkül” feltétel és utalás az ADV §3 sorára; megőrzési idő és új eljárás nem; kijelentkezés: IMPL-G3-1 (riport I.2) |
| M3:BIZT-G3-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:BIZT-G3-2 (az M3.B és az M3.F új helyként) |
| M3:BIZT-G3-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:BIZT-G3-2 (a GK §4:63–64 mondatai: M3.A:111, :561 és M3.F:99, :552 új helyként) |
| M3:BIZT-G3-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiterjed-e a SAFE-7 az M3.B 1. esetkártyájára és a megoldójegyzet csatornájára (B:352, :401, MUNK-03); SAFE-7-csomag — Memuna (X-5) |
| M3:BIZT-G3-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.B:459 és :403: a „kit hívnál fel?” helyére a B:267 mondata, a „helyi protokoll” helyére a GK §4.1:83 szó szerint; új címzett nem, az öt lépés marad (riport I.2) |
| M3:BIZT-G3-6 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:IMPL-G3-3 |
| M3:BIZT-G3-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: megengedett-e az M3.A csoportszobrában a kirekesztés testi megjelenítése („Van-e valaki külön?”, :271, :281), milyen keretben — Memuna + modulgazda (X-5) |
| M3:BIZT-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az F-peula képzője kijelölt mentor-e, hozzáférhet-e a kapueredményhez és a helyzetleíráshoz (M3.F:3, :183) — DPO + programvezető (X-4) |
| M3:BIZT-G3-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.B 4.3.2 (:431–435): a GK:23 mondata szó szerint + utalás a HUM-PRIV-02-re; új fotószabály és parafrázis nem; az M3.A nem változik (riport I.2) |
| M3:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:PED-G1-1 |
| M3:ERT-G1-10 | P2 | emberi-döntés | ELVETVE | REJECTED | a „leghosszabb / Memunás opció” stratégia nem áll meg (10/12 alatt, kritikus itemen bukik); kiegyenlítés biztonsági szöveghez nyúlna; preferencia (riport I.5) |
| M3:ERT-G1-11 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3_QUIZ Review options az első és a javító próbálkozás után, slotonkénti itemváltozat, a kvízbukás indoklása — értékelési felelős; kulcsnál Memuna (X-6) |
| M3:ERT-G1-12 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:PED-G1-4 |
| M3:ERT-G1-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:310, :331–333 és MAN:66: a rubrika tanulói megjelenítése (az M1:ERT-G2-6 mintája); beállításnevek a célverzión; rubrika, pont, küszöb marad (riport I.2) |
| M3:ERT-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | KAPU:30, :76, :333: a GATE-CP mindig kötelező (BS-D1), M4 „M3 megerősítve”, LMS-M5-05 „M3 complete” a MAN §4 szerint; konjunkció, küszöb marad (riport I.2) |
| M3:ERT-G1-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M3:BIZT-G1-2 (a modified-Angoff küszöb-jóváhagyás külön bizonyítéktételként átviendő) |
| M3:ERT-G1-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:BIZT-G1-1 |
| M3:ERT-G1-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: maradjon-e az életszerűség a blokkoló R4-ben (KAPU:326 ↔ PT:272), vagy másik sorba, saját sablonnal — projektgazda; QA: értékelési felelős + Memuna (X-6) |
| M3:ERT-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:37 (a HUB §6 opcionális): a MAN:66 belépő feltétele szó szerint („LMS-M3-04 + M1 complete”, Q-REL-2); M3.B-státusz, sorrend marad (riport I.2) |
| M3:ERT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:78: az ITEM 10 bővítése projektgazdai döntés, QA: értékelési felelős + Memuna (nem „a Memuna döntése”); kritikus itemkör, ≥10/12 marad (riport I.2) |
| M3:ERT-G1-8 | P2 | objektív | ELVETVE | REJECTED | a Kérdés 1 a szakasznevek felismerését méri (M3.1:12), a sorrend nem lecke-cél; disztraktor csak bizonyított hibánál cserélhető (riport I.5) |
| M3:ERT-G1-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:PED-G1-5 |
| M3:ERT-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:IMPL-3 (M3.2:679, M3.4:9, :509; a véleménykérdések kizárása = M0:ERT-3) |
| M3:ERT-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: elfogadja-e az R1 a határproblémákat (M3.4:824–827), mi teljesíti az R2-t feltárás nélkül — értékelési felelős + Memuna; rubrika: projektgazda (X-6) |
| M3:ERT-G2-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-11 |
| M3:ERT-G2-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:IMPL-G2-9 |
| M3:ERT-G2-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.2:12 mikrocél szűkül a :29-re, vagy új madrih-szempont kérdés a Parparimra és a Kivszára — projektgazda; QA: értékelési felelős (X-10) |
| M3:ERT-G2-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-14 (kulcs-rész); a visszajelzés-rész = M3:IMPL-G2-11 |
| M3:ERT-G2-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiterjed-e a HUM:473 elve a lecke-checkek elosztóira (M3.3:962–965 ↔ KAPU ITEM 1), félkövér-tilalom — értékelési felelős; gyermekvédelemnél Memuna (X-6) |
| M3:ERT-G2-8 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M3:BIZT-G2-10 (többlet: a HUM:463 QA az M3.4:834-re) |
| M3:ERT-G3-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:ERT-G1-11 |
| M3:ERT-G3-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mi a javító út, ha valaki hiányzik a kötelező F-peuláról (M3.F:43–44); programszintű, mind az öt kapus F-peulára — programvezető + értékelési fel. (X-10) |
| M3:ERT-G3-11 | P2 | emberi-döntés | ELVETVE | REJECTED | az M3.B:160 csak felismerést ígér; a túlcímkézést az M3.3 SLIDE 7 gyakoroltatja; kontrolleset új gyermekvédelmi tartalom (riport I.5) |
| M3:ERT-G3-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.B alapból kimaradó 4. (felnőtt gyanúsítottas) esetkártya helyett más maradjon-e ki, vagy a :406 doboz mindig elhangozzon — modulgazda + Memuna (X-10) |
| M3:ERT-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.B:509: az R2 „vagy a titoktartás kérdését meg sem említi” feltétele szó szerint az M3.4:834-ből; a bekezdés többi része nem változik (riport I.2) |
| M3:ERT-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.F:488 és :558 (a :51 opcionális): a javító határidő („az F-peula utáni szerda 18:00”, Q-REL-2) a :44 mintájára; naptári dátum nem (riport I.2) |
| M3:ERT-G3-5 | P2 | objektív | ELVETVE | REJECTED | a 4.2 1. lépése nem fordítja meg a 4.1 sorrendjét (:257 ↔ :197); az átrendezés szükségtelen; a valós rész a PED-G3-3-ban (riport I.5) |
| M3:ERT-G3-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:PED-G3-9 |
| M3:ERT-G3-7 | P2 | objektív | ELVETVE | REJECTED | a MUNK-01 spec nem ír elő külön típus-indoklást; a több olvasatot a :425 és a :438 kezeli; hat új indoklás új tartalom (riport I.5) |
| M3:ERT-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: vonatkozik-e az R2 „meg sem említi” szintje (KAPU:324) a feltárás nélküli esetekre (M3.B:404) — értékelési felelős + Memuna; rubrika: projektgazda (X-6) |
| M3:ERT-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:PED-G3-1 (az M3.F Blokk 3 helye átviendő) |
| M3:IMPL-G1-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:PED-G1-1 |
| M3:IMPL-G1-10 | P2 | objektív | ELVETVE | REJECTED | a „Moodle Page” és a „/ Timeline” nem ellentmondás (M3.1:28; a leckespec és a manifest egyértelműsít); kárt nem bizonyít (riport I.5) |
| M3:IMPL-G1-11 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:ERT-G1-11 |
| M3:IMPL-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUM 10. szakasz vagy PRODUCTION-DECISIONS: a Q-MED-2 (QMED:95) szó szerint egy nyilvántartásba, a másik hivatkozik; a Q-PED-4-gyel egy csomagban (riport I.2) |
| M3:IMPL-G1-2 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:ERT-G1-2 |
| M3:IMPL-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:30, HUB:249: a H5P Question Set-út „nem használt (MAN: QUIZ-M)” jelöléssel, a MAN:67-re mutatva; küszöb, item-bank nem változik (riport I.2) |
| M3:IMPL-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU §0: build-megjegyzés a kvízszintű és a kérdésenkénti keverésről; ✅, elosztók, itemszöveg nem változik; a betűjelek maradhatnak (riport I.2) |
| M3:IMPL-G1-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-6 |
| M3:IMPL-G1-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:IMPL-3 (HUB:252, M3.1:576; az RA 9 negatív esete = M0:ERT-2, fedje az LMS-M3-01/-02/-04-et) |
| M3:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.1:576, M3.2:628, :679, M3.4:439, :509: „Tab + Enter” helyett Szóköz / nyilak (H5P MC); az M3.2:606 kimarad; `@asset` build, pin (riport I.2) |
| M3:IMPL-G1-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:ERT-G1-6 |
| M3:IMPL-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.1-DIA-01 technical (:158): az „SVG” opció kikerül (Q-MED-2: felirat + leirat csak videóval), build; automatikus lejátszás tilos (riport I.2) |
| M3:IMPL-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:IMPL-3 (M3.4:509; a (d) negatív teszteset = M0:ERT-2) |
| M3:IMPL-G2-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:NYELV-G2-3 |
| M3:IMPL-G2-11 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ki írja meg az M3.2–M3.4 check-elemek hiányzó rossz-válasz-visszajelzéseit, milyen hatókörben (RT-A11Y-12) — M3 modulgazda; QA: Memuna (X-10; X-7) |
| M3:IMPL-G2-11.obj | P1 | objektív | MEGERŐSÍTVE | OPEN | meglévő semleges visszajelzés minden opcióhoz: M3.3:415, :954; M3.4:673–674; M3.2:205 a NYELV-G2-2 után; az M3.4:297 „Így van.” nem (riport I.3) |
| M3:IMPL-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | RA 7./11. pont: a SAFE-1 staging-tesztje (újraindítás és passz-útvonalak), az RA 24 eljárására hivatkozva; M3.3 szöveg, BSPEC-05 marad (riport I.2) |
| M3:IMPL-G2-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.2-DIA-04 (:506–542): élő szöveges forma az A11Y §4 kártya/akkordeon nézetével (nem H5P.Table); tartalom nem változik; build (riport I.2) |
| M3:IMPL-G2-14 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.2 párosító kulcsa (:670) szigorú, vagy jelenetenként felsorolt elfogadott kvucák, mindkét formában azonosan — értékelési felelős + modulgazda (X-6) |
| M3:IMPL-G2-15 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.4 kánoni leckecíme (H1 „Mit tegyél / mit ne tegyél” ↔ fájlnév ↔ HUB, MAN:65 „Do / Don’t”), átnevezésnél a linkekkel — M3 modulgazda (X-13) |
| M3:IMPL-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: megmarad-e a Drag and Drop mellékútként (nincs kártyánkénti visszajelzés; M3.4:509, M3.2:679) — M3 modulgazda; vétó: hozzáférhetőségi gazda (X-11) |
| M3:IMPL-G2-2.obj | P1 | objektív | MEGERŐSÍTVE | OPEN | (c) M3.2:679: egyetlen koppintásos alaput = a jelenetenkénti MC (EGY-01 saját példája); az RA 13 renderigazolás marad (riport I.3) |
| M3:IMPL-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.3 BSPEC-05 (:83–100): a CP-csomópontok „Hide summary slide” értékének rögzítése (§7.2); a BSPEC-05 többi beállítása nem változik (riport I.2) |
| M3:IMPL-G2-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: Image-csomópont a passz-választó után, vagy az ILL-01…04 elhagyása (BSPEC-05 térkép) — projektgazda; QA: Memuna, hozzáférhetőségi gazda (X-10) |
| M3:IMPL-G2-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: megjelenjen-e a szcenárió meglévő címe a P1–P4 passz-választón („Show content title”); a §7.1 szövege marad — projektgazda; QA: Memuna (X-5) |
| M3:IMPL-G2-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.1 SLIDE 5 és az M3.2 7A opcionális reflexiója tanuló-lokális vagy tárolt (TEXT-C sor nincs, MAN:308) — projektgazda; vétó: DPO (X-4) |
| M3:IMPL-G2-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M3:BIZT-G2-10 (többlet: RT-P0-09/-13/-14/-22, RT-A11Y-01…12) |
| M3:IMPL-G2-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:IMPL-G1-7 |
| M3:IMPL-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.4-EGY-05 K3 (:619), M3.3:322, M3.2 7B: a típusnév Multiple Choice (egyválaszos), az M3.3:923 mintájára; ✅, visszajelzés marad; build (riport I.2) |
| M3:IMPL-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | M3.F 2.1 (:59–61) és 5./2. (:540–541): az A11Y:57 mondata szó szerint, tartalékút csak a letölthető leckeváltozat (MAN:127); új szabály nem (riport I.2) |
| M3:IMPL-G3-10 | P2 | objektív | ELVETVE | REJECTED | az A11Y nem ír elő élőkép- vagy szoborleírást; a „szobrász”-narráció új tartalom (mint az M2:IMPL-G3-8) (riport I.5) |
| M3:IMPL-G3-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.F:62 és :542: a POSZ-01 meglévő címe és státuszkorlátja; a :69 marad; a POSZ-01 L1–L4 átírása elhagyandó (riport I.2) |
| M3:IMPL-G3-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.F:3: a megőrzési sor neve „Mentori fejlesztési jegyzet” (ADV:151); a „minimális adat” és az „árnyékdosszié” mondat nem változik (riport I.2) |
| M3:IMPL-G3-13 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:BIZT-G3-10 |
| M3:IMPL-G3-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.A-KART-01 notes (:183), M3.B-KART-01 / -MUNK-01 a11y (:193, :228): elavult sorszám és önhivatkozás cseréje, build; KART-02 hátlap = PED-G3-9 (riport I.2) |
| M3:IMPL-G3-15 | P2 | objektív | ELVETVE | REJECTED | fájlnévszintű „(Study Lab)” eltérés tanulói hatás nélkül; az átnevezés szükségtelen (mint az M2:IMPL-G3-11) (riport I.5) |
| M3:IMPL-G3-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | M3.F:262, :270: ne állítson Moodle-beli szerkesztést a peulán; papíron javítási terv (:49), beadás a megnyitás után (:51); 1+1, 20 perc marad (riport I.2) |
| M3:IMPL-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.B-KART-02 (:10, :26): a 116-000 a HUM-SAFE-01 fordulatával; a „nem általános szülői vonal” nem vihető át (BIZT-G2-2); build (riport I.2) |
| M3:IMPL-G3-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna, G1 (tracker #1): „átnéztem” az M3.B-re, biztonságkritikus assetjeire és az M3.F-re, segélyvonalak a review napján; objektív alpont: M3.F-jelölés (X-7) |
| M3:IMPL-G3-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.B 2.1, 5./2. és 4.3.2: a deklarált KART-02, KART-03, MUNK-01/-02/-03 meglévő címei; a „vagy nagy papírra” út marad, új kötelezettség nem (riport I.2) |
| M3:IMPL-G3-6 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:ERT-G3-4 |
| M3:IMPL-G3-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.F:187: a kapu-visszajelzés két Moodle-helye (MAN §2; az LMS-M3-05 neve a NYELV-G2-3 után); kvíz-visszajelzési szabály nem; emberi rész: ERT-G1-11 (riport I.2) |
| M3:IMPL-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:PED-G3-2 |
| M3:IMPL-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: csoportszám és -létszám 8 és 16+ fő mellett (M3.A 2.2 ↔ 4.3, fix 8 kártya; M3.B 3–4 csoport, 4 eset) — M3 modulgazda; M3.B-nél Memuna (X-10) |
| M3:NYELV-G1-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:PED-G1-1 |
| M3:NYELV-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:82: „a kettő ütközésében” → a HUM:132 / ADV:55 fordulata („a Program terv §4 és §7 ütközésében”); a zárójel és a vétó/QA-sor marad (riport I.2) |
| M3:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:252: a zárójeles gondolatjelek tagolása a K18 (M0:IMPL-3) átvezetésével egy szerkesztésben; a passz-mondat szövege nem változik (riport I.2) |
| M3:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.1:12, :33, HUB:27, KAPU:104, :194: „+” helyett kötőszó (HUB:59 mintája); a HUB:27 és az M3.1:12 a PED-G1-4 döntésével; pin (riport I.2) |
| M3:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.1:273, :517, :520, :527 (`@source`): „forming-ban” stb. közvetlen toldalékkal; csak hanggyártási úton (VO fix pack), derivatívákkal (riport I.2) |
| M3:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB, KAPU, M3.1–M3.4: „kapukvíz”, „minikvíz”, „a 12 item”, „egy-kétszavas”, KAPU:284 idézet; a d) kimarad; a c) az ERT-G1-7-tel; pin (riport I.2) |
| M3:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB, KAPU és az M3 többi fájlja: „red flag” közvetlen toldalékkal, összetételben kötőjellel; fájlnév marad, a HUB:288 a K28-cal; build, pin (riport I.2) |
| M3:NYELV-G1-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a HUB:41 „továbblépésnek büntetőjogi relevanciája” mire szól, a mulasztáshoz kötődik-e (↔ KAPU:359, Btk. 209/A. §) — jogi szakértő (X-15) |
| M3:NYELV-G1-4 | P2 | emberi-döntés | ELVETVE | REJECTED | a KAPU:284 természetes olvasata a mém továbbküldése, a „jelzel a Memunának” egyértelműsít; a nyelvtani hiba a NYELV-G1-14 f)-ben (riport I.5) |
| M3:NYELV-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:299 és :282: az „egyedüli” helyett az opció jelentése (egyedül végzett / puszta); ✅, opciók, „= nyomozás” nem változik (riport I.2) |
| M3:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:325 (R3): a „belső jelzés / kiegészítő támogatásként 116-111” perjele vesszőre vagy pontosvesszőre; a 112-formula betűre marad (riport I.2) |
| M3:NYELV-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-15 |
| M3:NYELV-G1-8 | P2 | objektív | ELVETVE | REJECTED | a KAPU:91 érthető, a javasolt „mert red flag?” jelentésváltozás; a helyen csak a NYELV-G1-2 toldaléka alkalmazható (riport I.5) |
| M3:NYELV-G1-9 | P2 | objektív | ELVETVE | REJECTED | a „kétszemes” a korpuszban egységes, a KAPU:317 definiálja; csere programszintű terminológiai döntés lenne (riport I.5) |
| M3:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.3:96: az „enélkül” névmási zuhanása (az indoklás az ellenkezőjét mondja); a `reviewmode` értéke és a §7.2-hivatkozás nem változik (riport I.2) |
| M3:NYELV-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.2:308: vessző törlése a -ként jelentésű „mint” előtt; ha az M3.2-DIA-01 átveszi, build és pin (riport I.2) |
| M3:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.2:771, :804: első szintű ‘…’ → „…”; a névelő-egységesítés nem hajtandó végre; opciók, ✅ nem változnak (riport I.2) |
| M3:NYELV-G2-12 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-15 ((a) rész); a (b) rész = M3:PED-G2-7 |
| M3:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.3:198, :205, M3.4:598 perjel → „vagy”; M3.2:585 a :808 alakjára; a kizárt gyermekvédelmi helyek és a ✅ nem változnak (riport I.2) |
| M3:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.2:441: „életkoron belül” → a fájl saját alakja („az életkori sávon belül”); a „korsáv” nem használható; DIA-02 átvételnél build (riport I.2) |
| M3:NYELV-G2-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.3:995 (NAR-03, `@source`): „egy alap térképed” egybeírása csak VO fix packkal, manifest/CSV builddel (riport I.2) |
| M3:NYELV-G2-16 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.2:153, :218, :512 (`@asset`): ASCII záró idézőjel → ”, „3-4” → „3–4”; Edit, majd build, külön chore(media); a :512 a NYELV-G2-18-cal (riport I.2) |
| M3:NYELV-G2-17 | P2 | objektív | ELVETVE | REJECTED | az M3.3:45, :857 mindkét olvasata ugyanazt a védő utasítást adja; adatvédelmi kikötés stílusból nem írható át (riport I.5) |
| M3:NYELV-G2-18 | P2 | objektív | MEGERŐSÍTVE | OPEN | csak b): „korosztály-térkép” → „korosztálytérkép” egy lépésben az egész korpuszban (M3.2, M3.3:404, PT, M6), build; a :324 (a) elvetve (riport I.2) |
| M3:NYELV-G2-19 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.4:390: „/ transzparencia” → „és az átláthatóság”; a „titkolás-minta”, a szabálymondatok és a 3C vétó/QA marad (riport I.2) |
| M3:NYELV-G2-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.2:204–205: a „Pont ez a lényeg:” nyitány törlése (E-M3-017); a ✅ és a magyarázat többi része marad, ágra bontott új szöveg nem (riport I.2) |
| M3:NYELV-G2-20 | P2 | objektív | ELVETVE | REJECTED | a „beégett” bevett köznyelvi használat egy fejlesztői „Cél”-sorban; preferencia (riport I.5) |
| M3:NYELV-G2-21 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.2:179 (fejlesztői szöveg): „alatt” → „alattuk” (riport I.2) |
| M3:NYELV-G2-22 | P2 | objektív | ELVETVE | REJECTED | az M3.3:540 idézett, köznyelvi rossz opció Branching-csomópontban; a szórend jelölt, nem hibás (riport I.5) |
| M3:NYELV-G2-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-M3-05 tanulói neve (M3.4:784 ↔ MAN:66 „Helyzetelemzés” ↔ EGY-07), lehetőleg „helyzetleírás” — modulgazda / implementációs felelős (X-13) |
| M3:NYELV-G2-4 | P2 | objektív | ELVETVE | REJECTED | a :684 ✅ opció eltér a fókuszmondattól, de nyelvileg hibátlan; ✅-szöveg nem nyelvi javítás (riport I.5) |
| M3:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.3:939: „100%-os titkot” → a lecke terminusa („100%-os titoktartás”); a ✅ és a visszajelzés többi része marad (riport I.2) |
| M3:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:PED-G2-8 |
| M3:NYELV-G2-7 | P2 | objektív | ELVETVE | REJECTED | az „elfogadható, ha …” helyes; a javaslat egy értékelt T/F állítás modalitását változtatná; preferencia (riport I.5) |
| M3:NYELV-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.4:374: „mentorral” → „a mentoroddal”; a 3B DO mondat többi része marad (riport I.2) |
| M3:NYELV-G2-9 | P2 | objektív | ELVETVE | REJECTED | a „központ” a „középpont” értelmében is bevett; hiba nem bizonyított (riport I.5) |
| M3:NYELV-G3-1 | P3 | objektív | MEGERŐSÍTVE | OPEN | csak a): M3.A:401 első tagmondata „Még mindent a madrih magyaráz, …” (a :429 kulcs szerint); besorolás marad; KART-02 build, pin (riport I.2) |
| M3:NYELV-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.A:5 szóköz, M3.B:455 kóbor `\`, M3.F:454 „pótvizsga-íze”; csak a három tipográfiai pont; pin (riport I.2) |
| M3:NYELV-G3-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.B:496, :497 (M3.F:477, :478 csak a PED-G3-4 után): „…segítséget kérek, és …” párhuzamos alak; a biztonsági mondat szó szerint marad (riport I.2) |
| M3:NYELV-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.A:440 (és :355 spec, build): a kánoni Glosszárium-mondatban „(viharzás)” → „(balhék)” vagy elhagyás; a kártyaglosszák maradnak (riport I.2) |
| M3:NYELV-G3-4 | P3 | objektív | MEGERŐSÍTVE | OPEN | csak a metanyelv: M3.A:421 „Fejlesztéskor” → „Felkészüléskor”; a 6–8 marad; ha az IMPL-G3-9 döntése átírja a mondatot, abba olvad (riport I.2) |
| M3:NYELV-G3-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.A:528: „vagy” → „és” (a peula célja és a :514 példája szerint) (riport I.2) |
| M3:NYELV-G3-6 | P3 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: csak b): ki választja ki a 3 kártyát az M3.A 4.3 3. lépésében (A:462 T/2 ↔ E/2-es képzői megszólítás) — modulgazda (X-10) |
| M3:NYELV-G3-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.F:437: az „ezeket” névmás helyett a főnév (red flag); az F:436-hoz nem nyúl; toldalék a NYELV-G1-2 szerint (riport I.2) |
| M3:NYELV-G3-8 | P2 | objektív | ELVETVE | REJECTED | az „előhívás” a Glosszárium definíciójában is szerepel; képzői lépéscím, közös F-peula-sablon; egyedi csere új eltérés (riport I.5) |
| M3:NYELV-G3-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.B:509 és M3.4:834: „kritikus biztonsági helyzet” → „kötelező” (KAPU:84, M3.F:30); 10/12 és itemkör nem változik (riport I.2) |
| M3:PED-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | KAPU:84: az újraértékelés határa „még mielőtt az M5 kapufeladata megnyílna” (BS-D2, M3.4:834); a második mondat és a szabályok maradnak; pin (riport I.2) |
| M3:PED-G1-10 | P2 | emberi-döntés | ELVETVE | REJECTED | a KAPU:37 rendezi az M3.B-t kihagyók esetét (mentori R3/R4-ellenőrzés); új felzárkóztató út új tartalom, preferencia (riport I.5) |
| M3:PED-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.1 látható diaszövege + HUM: a Q-PED-4 mondata szó szerint („A modell szemüveg, nem menetrend…”), nem a VO-forrásba; Kérdés 1, outro marad (riport I.2) |
| M3:PED-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.1 SLIDE 1 (:141) és SLIDE 4 (:570–576): opciónkénti / kártyánkénti visszajelzés a NAR-02/-03-ból (N-M3-01); answer key, kártya, opció marad (riport I.2) |
| M3:PED-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU §2.4 (:337–340): a „M3.3, N. dia” helyett a tanuló által látott cím- és dobozcímek szó szerint; a sablonok üzenete, a rubrika marad (riport I.2) |
| M3:PED-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az adjourning és a storming ↔ bántalmazás gyakorlása (HUB:27–29, M3.1:12): szűkül a cél, vagy gyakorló elem — projektgazda; QA: Memuna, modulgazda (X-10) |
| M3:PED-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.1 SLIDE 4, 4. kártya (:564): a Performing-választás visszajelzése a NAR-02 norming-jegyéből, a PED-G1-2-vel; kulcs, kártyaszöveg marad (riport I.2) |
| M3:PED-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:ERT-G1-11 |
| M3:PED-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:ERT-G1-5 |
| M3:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:172, :208, :298, :338; M3.3:206, :544, :938; M3.4:657: forrás nélküli felsőfokok → „gyakori”, „kockázatos”; ✅ és szabály marad (riport I.2) |
| M3:PED-G1-9 | P2 | emberi-döntés | ELVETVE | REJECTED | a :535 szavazás és a :670 opcionális, indoklást kérő reflexió más funkciójú; az átfedés megszüntetése preferencia (riport I.5) |
| M3:PED-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: érzékeny gyakorlat-e az M3.4 SLIDE 4 és 6, mi a passz vagy alternatíva, hogyan hat a completionre — Memuna + programvezető; értékelési felelős (X-5) |
| M3:PED-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M3:BIZT-G2-10 |
| M3:PED-G2-11 | P2 | emberi-döntés | ELVETVE | REJECTED | a terhelésbecslés nem bizonyíték, az időérték lezárt; új kártya új tartalom; az 1:1 példák kérdése a BIZT-G2-8-ban (riport I.5) |
| M3:PED-G2-12 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:ERT-G2-5 |
| M3:PED-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:ERT-G2-2 |
| M3:PED-G2-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-6 (az „opcionális” jelölés objektív alpontja a döntéssel együtt) |
| M3:PED-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G2-14 (kulcs-rész); a visszajelzés-rész = M3:IMPL-G2-11 |
| M3:PED-G2-5 | P2 | emberi-döntés | ELVETVE | REJECTED | a premissza nem áll: az M3.3 S1-K1/K2 az ITEM 4 kulcsának formatív előpróbája; új gyermekvédelmi tartalom kérése (riport I.5) |
| M3:PED-G2-6 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:PED-G1-3 |
| M3:PED-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.3:987: a „kvucánként” törlése (hamis előreutalás); a „Do/Don’t” az IMPL-G2-15 döntését követi; pin (riport I.2) |
| M3:PED-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.3:849: a NAR-02 spec kihagyhatósági mondata tegezve, „1–3” → „1–2” (vétólista); narráció és biztonsági dobozok maradnak; pin (riport I.2) |
| M3:PED-G2-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:PED-G1-8 (csak a felsőfok-rész; az M3.3:404 alpont elvetve) |
| M3:PED-G3-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: blokkonként melyik lépés rövidüljön (M3.A 4.2/4.3, M3.B 4.2/4.3, M3.F 4.4, Blokk 3); a :309 csak a döntéssel — modulgazda; QA: programvezető (X-10) |
| M3:PED-G3-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:BIZT-G3-4 |
| M3:PED-G3-11 | P2 | objektív | ELVETVE | REJECTED | az M3.A:239 „4 szakaszával” az M3.1 szóhasználata; a HUB:27-jelölés hamis lenne; a valós mag a PED-G1-4 döntésében (riport I.5) |
| M3:PED-G3-12 | P2 | emberi-döntés | ELVETVE | REJECTED | ellentmondás nincs (az 5./4. pont és a :145–146 előírja); a saját történetek törlése szükségtelen, peulába emelése DPO-kérdés (riport I.5) |
| M3:PED-G3-13 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mit jelent a 3. kártya „Leviatán – év eleji stáb” címkéje (M3.A:411, :431, KART-02); a kulcs marad — modulgazda; ha someres szó, helyi kérdés (X-13) |
| M3:PED-G3-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.B 4.3.3 fiktív esetmondata: előre megírt 2–4 mondat vagy átnézett anyag; marad-e első vágás; KAPU-helyzet tilos — modulgazda; QA: Memuna (X-10) |
| M3:PED-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M3.F:32, :279–285: elsőként és kötelezően a visszajelzés szerinti lecke (HUB:227), a többi opcionális; csendes pótlás, MUNK-01, 5 perc marad (riport I.2) |
| M3:PED-G3-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.F zárókérdése a HUB:240 („pótolni vagy átdolgozni”) vagy az M3.F:111, :469 („nem maradok egyedül…”) — M3 modulgazda; QA: programvezető (X-10) |
| M3:PED-G3-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M3:IMPL-G3-9 |
| M3:PED-G3-6 | P2 | emberi-döntés | ELVETVE | REJECTED | kánonsértés nincs: a nyitókör egyszavas, passzolható; a „Ha ez a téma…” blokk helye lezárt (HUM-SAFE-03, GK §4.3) (riport I.5) |
| M3:PED-G3-7 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:BIZT-G3-5 |
| M3:PED-G3-8 | P2 | emberi-döntés | ELVETVE | REJECTED | a :427 szó szerint kimondja a HUM 8. döntést; a maradék óvatos, védő irányú; a Memuna amúgy is átnézi (riport I.5) |
| M3:PED-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M3.A kártyák hátoldala: önellenőrzés a tipp után, vagy a kulcs csak a képzőnél (a :87, :403, :425, KART-02/MUNK-01 igazodik) — modulgazda (X-10) |
| M4:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:IMPL-G1-3 (a „Tilos” lista öröklődik: a M4.2:734–735 szövege, a ✅ és az opciósorrend érinthetetlen; a „rosszul pontozódik” állítás túlzó) |
| M4:BIZT-G1-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M4.1 és az M4.3 reflexiója „magadnak írod” ↔ tárolt TEXT-C (MAN:24, :70, :74): tárolt vagy tanuló-lokális (N-M1-04 új esete), ADV §5:150 — DPO (X-4) |
| M4:BIZT-G1-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M4:PED-G1-7 (a szakmai lektor nem a G1 alá tartozik: a G1 egyetlen jóváhagyója a Memuna, RR:39) |
| M4:BIZT-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-10 (az FTQ xAPI-rögzítésének és a CKEditornak a bizonyítéka oda; tárolásmentesség bizonyíték nélkül nem állítható) |
| M4:BIZT-G1-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: belefér-e a csoportszintbe a HUB:133 „nevesített korosztály/élethelyzet” példája; az ADV:83 „M4 peulabemutató” külön review-ja — DPO + programvezető (X-4) |
| M4:BIZT-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kerüljön-e az M4.3:360 védőmondata mellé a GK:57 félmondata (a :352 „Jól értem, hogy…?” feltárásba vitele); a :360 nem gyengíthető — Memuna (X-5) |
| M4:BIZT-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mely M4.3-itemek készültek generatív AI-val (M4.3:22; PT:224 jelölés a lecke alján; kiindulás: M4.2 asset-notes) — tananyagfelelős / szerző (X-10) |
| M4:BIZT-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M4.A:437–442 (MUNK-02 :396) képzői 1:1 megkeresése erős szorongásnál ↔ GK §4.2 (a)–(c) kivételei (HUM-SAFE-02 új esete) — Memuna (X-5) |
| M4:BIZT-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:BIZT-G2-3 (X-4; M4.4:704, :737, M4.F:267 „csak a kijelölt mentor”; az ADV §11 mondata a DPO-döntésig marad; a lencse objektívnak jelölte) |
| M4:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | M4.F:52 és :267: az A11Y:57 kijelentkezési mondata szó szerint; a :53 pontosítása opcionális; jelszómentés: M2:BIZT-G3-10; a :267-en a NYELV-G2-12 e)-vel (riport I.2) |
| M4:BIZT-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.B:332, MUNK-01 (:85, build), M4.F:362: utalás az ADV §3:67 név nélküli lap sorára; megőrzési idő nem; az M4.A:381 a BIZT-G2-5 döntése után (riport I.2) |
| M4:BIZT-G2-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M4.A:381 névvel aláírható, borítékba / falra kerülő kilépőkártyája (az ADV §3 mátrixában nincs sora): adatkör, megőrzés, hozzáférés — DPO (X-4) |
| M4:BIZT-G2-6 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:IMPL-G2-7 |
| M4:BIZT-G2-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO, G2 (tracker #2): az ADV:83, :87, :89 „Külön review” sorai (köztük az M4 peulabemutató) és az ADV:207 release-evidence; tároló, hozzáférés nem írható be (X-12) |
| M4:BIZT-G2-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:BIZT-G1-5 (P1 → P2; a kiegészítő kérdésre a kánon már válaszol: M4.B:302) |
| M4:BIZT-G2-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: „felkavart” állapot-e a szereplési szorongás (M4.A:58, :390; GK §4:64, HUM-SAFE-03) — Memuna (X-5); a „ki a felnőtt” alkérdés = M2:BIZT-G3-2 |
| M4:BIZT-G2-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiterjed-e a GK §4:61 / HUM-SAFE-03 passzszabálya az M4.B 4.1, 4.2 és 4.4/1 gyakorlataira; csak a :326 mondata kerülhet be szó szerint — Memuna (X-5) |
| M4:ERT-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M4.3 K3 kulcsa (Kapu 1; :549 „Érthető volt…?” ↔ :191, M4.F:370): új opció, új szár vagy ✅-áthelyezés — szerző / projektgazda; QA: szakmai lektor (X-6) |
| M4:ERT-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:143: a MAN:78 / BSPEC-07 mondata (LMS-M4-10 „Teljesítve” / „Még nem teljesítve”) szó szerint, egy helyen; a :138 és a küszöb nem változik; P1 → P2 (riport I.2) |
| M4:ERT-G1-3 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:IMPL-G1-1 (a javasolt „a mini-kvíz eredménye” cellaszöveg helyett a PED-G1-2.obj megnevezése) |
| M4:ERT-G1-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:IMPL-3 (X-6; M4.3:20, HUB:142, MAN:73; az RA 9 (d) LMS-M4-01…-04 sorai a döntési csomaggal mennek, nem külön) |
| M4:ERT-G1-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a HUB:46 „példát tud mondani mindegyikre” az irányító típusra produktív elem nélkül: szűkül a cél vagy gyakorló elem — projektgazda / modulgazda (X-10) |
| M4:ERT-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ki írja meg az M4.3 hiányzó rossz-válasz-visszajelzéseit (SLIDE 1 :200, SLIDE 5 K1 :513; a K3 az ERT-G1-1-gyel) — szerző; QA: szakmai lektor (X-10) |
| M4:ERT-G1-6.obj | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.3:535–536: a K2 meglévő, semleges visszajelzése szó szerint minden opcióhoz; a K3 (:554–555) nem; új szöveg nem, a ✅ és az opciók maradnak (riport I.2) |
| M4:ERT-G1-7 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:IMPL-G1-3 (a javítás formája ennek javaslata: a megjegyzés átvétele, a típusnév marad) |
| M4:ERT-G1-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:PED-G1-2 (a (b) út oda olvad; a PT:246-alpont nem bizonyított, a „kapukvíz” megnevezés marad) |
| M4:ERT-G1-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M4.3 SLIDE 4 kártyaszáma (12–15 előírva, 8 megírva, :473): a hiányzók megírása kulccsal, vagy 8 marad — szerző; QA: szakmai lektor (X-10) |
| M4:ERT-G1-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M4.1 IV Free Text kérdése (:831–836) tárolt vagy tanuló-lokális, kötelező vagy opcionális; az ILO 2 átírása — projektgazda; a tárolásról DPO (X-4) |
| M4:ERT-G2-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:PED-G2-3 (emberi döntésből objektív; a SLIDE 2 listájának és a DIA-02 specnek az igazítása kimarad) |
| M4:ERT-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:IMPL-3 (X-6; M4.4:26 ↔ MAN:75); a HUB:84-része = M4:IMPL-G1-1; P2 → P1 |
| M4:ERT-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.4:509: az M4.3:398 SCS-kizáró megjegyzése a :509 mögé, a típusnév marad; kérdés, opció, ✅, visszajelzés nem változik; az IMPL-G1-3-mal együtt (riport I.2) |
| M4:ERT-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mi váltja ki az M4.F-ajánlást (GL:186 ↔ MAN:78 ↔ HUB:138), hol rögzül a rubrikaszint (LMS-M4-05 vagy -10) — projektgazda; QA: értékelési felelős (X-6) |
| M4:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.4:790: „Még nem éri el” szintnél a visszajelzés megnevezi a hiányzó vagy nem érthető elemet (:750, HUB:135); szempontlista, modell, küszöb marad (riport I.2) |
| M4:ERT-G2-6 | P2 | emberi-döntés | ELVETVE | REJECTED | a három szám más célt szolgál (TEXT-C útmutatás, BS-D4; papíros vázlat; 45 mp-es szóbeli hossz); az átírás hiba nélküli küszöbmódosítás volna (riport I.5) |
| M4:IMPL-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | HUB:62–63, :70, :77, :84, :126; M4.1:23; M4.2:21: completion-sorok a MAN / BSPEC-06 szerint, a HUB:84-be az LMS-M4-09; completion-logika nem változik (riport I.2) |
| M4:IMPL-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | M4.1:64, M4.2, M4.3:59: a reflexiók helye a MAN:35 szerint (Moodle-oldali mező az alapút, minta: M4.4:68); az M4.1/M4.3 tanulói mondatai a BIZT-G1-2 után (riport I.2) |
| M4:IMPL-G1-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | M4.1 SLIDE 3–5, M4.2 SLIDE 5, M4.3 SLIDE 1, :485: SCS-kizáró megjegyzés (M4.3:497 / Z.1:57), típuscsere nélkül; a M4.2:734–735 tilos; VID-02, EGY-04 build (riport I.2) |
| M4:IMPL-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-6 (az objektív alpontja nem használható: a :200 marad, meglévő mondat nem rendelhető át) |
| M4:IMPL-G1-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-10 (az LMS-M4-01 / RA 24 útja oda; a kérdés szövege nem változik) |
| M4:IMPL-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-9 (kártyarész); a DnD-mechanizmus objektív alpontja: M4:IMPL-G1-6.obj |
| M4:IMPL-G1-6.obj | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.3:477: a „(max. próbálkozás után)” törlése, a célzónánkénti visszajelzés rögzítése; a zónaszövegek új szöveg: ERT-G1-9; a kártyák maradnak (riport I.2) |
| M4:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.1:54, M4.2:57, M4.3:53: a „Ha elakadsz” doboz harmadik ága a PT:242 mondatával („M4.F”, „ajánlott”); az M4.3:53 a NYELV-G1-8 a)-val; pin (riport I.2) |
| M4:IMPL-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.1:34, M4.2:32, M4.3:31: a lecke veszi át a MAN „Név” értékét (MAN:3, M0:IMPL-7); H1, fájlnév, build_id marad; az IMPL-G2-6-tal; pin (riport I.2) |
| M4:IMPL-G1-9 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M4:PED-G1-7 („a G1 csak M3/M7-tartalmakat sorol” pontatlan, RR:40) |
| M4:IMPL-G1-10 | P2 | objektív | ELVETVE | REJECTED | az M4.1:132 a WCAG 1.2.2-t a feliratra nevezi meg, a leirat jogcíme a :66-ban; hiba nincs (precedens: M2:IMPL-G1-9) (riport I.5) |
| M4:IMPL-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.1:47, M4.2:52, M4.3:47, M4.4:60: a nem létező „Lecke indítása” gombra utaló tagmondat törlése; az M4.4:60-on az IMPL-G2-5 szövege; pin (riport I.2) |
| M4:IMPL-G1-12 | P2 | objektív | ELVETVE | REJECTED | az A11Y:76 a „kapus” szót completionhöz kötött elemekre is definiálja; a csere a G5a-kötést gyengítené (riport I.5) |
| M4:IMPL-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | M4.4:56, :664, :677, :710, :725, :739 és DIA-05 (build): a vázlatmező a lecke melletti TEXT-C (LMS-M4-09), nem H5P-sablon; a :704 🔒 marad (riport I.2) |
| M4:IMPL-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:IMPL-3 (X-6; M4.4:26, summary-slide.js; az RA 9 (d) LMS-M4-04 sora a döntési csomaggal; a „Hide summary slide” marad) |
| M4:IMPL-G2-3 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:BIZT-G2-3 (az M4.1 offline tartalékútjának megnevezése nem része; a :53 pontosítása opcionális) |
| M4:IMPL-G2-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:ERT-G2-3 (csak a SLIDE 4-rész; a SLIDE 1- és az ILL-01-rész elvetve) |
| M4:IMPL-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.4:60, :677: az összefoglaló dia mint kész-pont és a mező nyílása a MAN:16/:76 szerint, leíró mondattal; a gomb-rész = IMPL-G1-11; az IMPL-G2-1-gyel (riport I.2) |
| M4:IMPL-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.4:38, :732: a MAN:75 és :77 „Név” szó szerint; H1 és fájlnév marad; az IMPL-G1-8-cal együtt; pin (riport I.2) |
| M4:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.F:3: a megőrzési sor neve „Mentori fejlesztési jegyzet” (ADV:69, :151); a „minimális adat” és az „árnyékdosszié” mondat marad (riport I.2) |
| M4:IMPL-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.F:54: a POSZ-01 tájékozódó tábla címe és a meglévő státuszkorlát; a :61 (POSZ-02) marad (riport I.2) |
| M4:IMPL-G2-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G2-4 (annak (2) kérdése: Grade type, Feedback comments, LMS-M4-05 vagy -10, DPO) |
| M4:IMPL-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.B:44: csak a „Telefon nem kell:” előtag törlése (HUM-PED-01 (4)); a felvételi tilalom szó szerint marad, új eszköz-előírás nem (riport I.2) |
| M4:IMPL-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.4:89 (ILL-01 technical, build): a „beégetve vagy” kikerül, a PST:352, :354–356 mintája (PD D1); egy buildben a NYELV-G2-12 a)-val (riport I.2) |
| M4:IMPL-G2-12 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda, G3b/G5b (#3), G8: RT-P0-01, -06, -08, -09, -14, -15, -19, -22, -23 és RT-A11Y-01…12; értesítő, M4_ASSIGN: SCHEDULE_TO_RESYNC; DPO G2 (X-8, X-12) |
| M4:NYELV-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-1 (a szárcsere megelőlegezné a K1-döntést; a lencse objektívnak jelölte) |
| M4:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.3:360: „hanihcsal” → „hanihhal”; kánoni gyermekvédelmi doboz, csak ez a szó (a BIZT-G1-6 döntéséig); P1 → P2 (riport I.2) |
| M4:NYELV-G1-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-6 |
| M4:NYELV-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-1 (a „részben zárt” egységesítése csak a K1-döntéssel) |
| M4:NYELV-G1-5 | P2 | objektív | ELVETVE | REJECTED | az M4.3:449 a tegező narrátor hangja (a :355, :358 definíciójának visszhangja); a dőlt önkérdéshez tartozás nem bizonyított (riport I.5) |
| M4:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.1:797: „a legerősebb … ennél a madrihnál”; opciók, ✅ marad; az M4.3:524 elvetve; pin (riport I.2) |
| M4:NYELV-G1-7 | P2 | objektív | ELVETVE | REJECTED | az M4.2:651 az újraolvasott visszajelzés-kártyára utal; a hamis előfeltevés nem bizonyított, az átírás preferencia (riport I.5) |
| M4:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB, M4.1–M4.3: kapukvíz, minikvíz, minijelenet, miniszitu, Példa-összetételek, „A visszajelzés logikája”, célverzión (a–g); `@asset` build; h) marad; pin (riport I.2) |
| M4:NYELV-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.2:379, :722, :871: perjel helyett „vagy”; a :734 és a Memuna-QA marad; a :651 elvetve; pin (riport I.2) |
| M4:NYELV-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:42: „bagatellizáló” → „elütő” (az M4.2:13 fogalompárja); a kompetencia többi része marad (riport I.2) |
| M4:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:164, :168: névelő a szemantikus azonosító előtt; a „-ben” → „-n” csak egységesítés; a :170 elvetve (riport I.2) |
| M4:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.2:909: kettős mondatzáró pont; M4.1:827 (`@source` NAR-05-VO) csak hanggyártási úton; a HUB:149 elvetve (riport I.2) |
| M4:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.4:162 (fejlesztői „Cél”): „…valós helyzet” a :84 szerkezetéhez; az ILL-01 purpose, a dia és a ✅ marad; a :503 elvetve (riport I.2) |
| M4:NYELV-G2-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mit jelent és marad-e az M4.4:62 „pont ezért van … puha, formáló visszajelzés” tagmondat (az „ezért” előzménye hiányzik) — M4 szerzője / modulgazda (X-10) |
| M4:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.4:672: „belőle” → „egy peulabemutatóból”; pin; build nem kell; a b) (M4.A:383) elvetve (riport I.2) |
| M4:NYELV-G2-4 | P2 | objektív | ELVETVE | REJECTED | a „Véleményvonal” Anna szándékos címe (E-M4-018 RETAIN); a csere terminológiai preferencia, a passz adott (:100) (riport I.5) |
| M4:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.B:324: „Két-háromfős minikörökben…” (a „mini” marad); a NYELV-G2-12 a), a G2-10 és a BIZT-G2-10 passzmondatával egy menetben, a PED-G2-2 után (riport I.2) |
| M4:NYELV-G2-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mire vonatkozik az M4.B:326 „ha belefér az idő” feltétele (a két mondat a 4. cél, mag-rész) — szerző / modulgazda, a PED-G2-2 csomagjában (X-10) |
| M4:NYELV-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.B:301: „keretben” → „keretében”, a többi szó marad (riport I.2) |
| M4:NYELV-G2-8 | P2 | objektív | ELVETVE | REJECTED | az „elmondotok” régies, de létező alak; regiszterpreferencia (riport I.5) |
| M4:NYELV-G2-9 | P2 | objektív | ELVETVE | REJECTED | a „meghívás a peulába” bevett „-ba” vonzat; a Glosszárium-hivatkozás tőhangzó-szabály, bizonyított hiba nincs (riport I.5) |
| M4:NYELV-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.A:231; M4.B:205, :222, :278, :298, :307, :324: perjel és képletjelölés helyett mondat; a :205, :278, :324 a döntések után; „max.”, „kb.” elvetve; pin (riport I.2) |
| M4:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.A:212; M4.B:327–328: első szintű idézet „…”-ben; a beágyazott ‘…’ jelek, a dőlt szedés és a szöveg marad (riport I.2) |
| M4:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.4, M4.A, M4.B, M4.F: „mini-” és kéttagú összetételek (a–f); az M4.4:509 kikerül; e) csak a kötőjel; `@asset` build; g) elvetve; pin (riport I.2) |
| M4:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.A:72, M4.B:76, M4.F:93: „Blokk-leírások” → „Blokkleírások”, csak a három fejléc (riport I.2) |
| M4:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.A:11, M4.B:11, M4.F:19: a „/ madrihot” beírása (GL:72); a „15+”, a zárójel és a félkövér marad (riport I.2) |
| M4:NYELV-G2-15 | P2 | objektív | ELVETVE | REJECTED | „Először:” ↔ „Második:” beszélt narrációban érthető; a csere egy `@source` VO-blokk újrarenderelését igényelné (riport I.5) |
| M4:NYELV-G2-16 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:PED-G2-2 (a „páronként” jelentése alpontként; az „egy kör kötelező” alpont nem áll) |
| M4:PED-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-1 (az M4.F:370 bizonyítékként felveendő) |
| M4:PED-G1-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mi a Kapu 1 jelzése és határa (a Moodle-be a CP összpontszáma jut, HUB:165; a „gyenge eredmény” határa nincs) — értékelési felelős + projektgazda (X-6) |
| M4:PED-G1-2.obj | P1 | objektív | MEGERŐSÍTVE | OPEN | M4.3:20 és MAN:73: „a pontozott interakciók eredménye” (M2.2:31 minta, HUB:165); completion, Grade to pass, puha kapu marad; a HUB:77 ezt követi (riport I.2) |
| M4:PED-G1-3 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:IMPL-G1-3 (a típuscsere-javaslat nem használható) |
| M4:PED-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-6 (visszajelzés-rész); a (b) kártyarész = M4:ERT-G1-9; a SLIDE 3-alpont felesleges |
| M4:PED-G1-5 | P2 | emberi-döntés | ELVETVE | REJECTED | a finding maga pedagógiai javaslatnak mondja; a K1/K2 kulcsa helyes, új határeset-item didaktikai preferencia (riport I.5) |
| M4:PED-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:ERT-G1-10 |
| M4:PED-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | HUM-PED-01 utólagos vétó/QA: Memuna, G1 (#1): M4.2 SLIDE 5 K2, M4.3:360; szakmai lektor: PT §9.3 release-jegyzőkönyv; P2 → P1 (X-7; X-16) |
| M4:PED-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M4.B 1. és 3. célja ↔ a minimum (B kérdez, A válaszol; szerepcsere csak „ha az idő engedi”): időátosztás vagy célmódosítás — modulgazda (X-10) |
| M4:PED-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: melyik lépés rövidüljön (M4.A 4.3–4.5, M4.B 4.3–4.4 összegei a blokkhatár fölött; 45’ fix) — modulgazda; vétó/QA: programvezető (X-10) |
| M4:PED-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | M4.4:527: csak az 1. elosztó cseréje a részletből cáfolható szövegre; a ✅ (2.), a 3. opció és a visszajelzés marad; vétólista; lektori QA (riport I.2) |
| M4:PED-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kötelező vagy opcionális-e az SBI a peula-visszajelzésben (M4.B:278 „add” ↔ HUB:138 „opcionálisan”; HUM-PED-01 (2)) — modulgazda; QA: szakmai lektor (X-10) |
| M4:PED-G2-5 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:IMPL-G2-10 (a saját eszközről szóló félmondat nem vehető át) |
| M4:PED-G2-6 | P2 | objektív | ELVETVE | REJECTED | a 20–25’-es jegyzetlap-lépés önálló, a lapot a 2.1 és a 2.3 előkészíti; az áthelyezés preferencia (riport I.5) |
| M4:PED-G2-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M4:BIZT-G2-10 (csak az M4.B-s részek; az M4.A:244-es rész elvetve) |
| M4:PED-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M4.B:300: a „CBE-LSE …” csak ellenőrzött tételre cserélhető, különben törlődik; az UDL-hivatkozás és az érvelés marad (riport I.2) |
| M4:PED-G2-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: hol éljen tovább az M4.A-MUNK-01 fókuszmondata (a :304 visszautalást ígér, nincs; a kártyát leadják): új lépés vagy visszaadás — modulgazda (X-10) |
| M4:PED-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:99: a Peula B „Fő fókusz” zárójele az M4.B:19 szerint; a HUB:46–47 kompetencia nem változik (riport I.2) |
| M4:PED-G2-11 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:IMPL-G1-1 (csak a HUB:84-rész; az M4.B:28-rész elvetve) |
| M5:BIZT-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.2:313 szorongás-beszélgetés passz nélkül, automatikus Memuna-bevonás mély szorongásnál (HUM-SAFE-01/03 új esete) — Memuna, programvezetővel (X-5) |
| M5:BIZT-G1-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:PED-G1-11 (a H-6 előtti M5.1:24 2–3. mondata; a 3. mondat CP-kikötése megtartandó, a helymegjelölés pontatlan) |
| M5:BIZT-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:160 és M5.F:3 „Mentori 1:1 meta-napló” → „Mentori fejlesztési jegyzet” (ADV:69, :151); csak a sornév, a „minimális adat” marad (riport I.2) |
| M5:BIZT-G1-4 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO, G2 (tracker #2): ADV:84/:87 „Külön review” (M5/M6 produktum, F-peula mentorjegyzet, M5.4 Google-sablon), ADV:207 release-evidence; tároló nem írható (X-12) |
| M5:BIZT-G1-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: belefér-e a csoportszintbe a valós M4-es kvuca (KAPU:293, HUB:20); az ADV:84 „M5 produktum” review-ja; kikötések nem törölhetők — DPO + programvezető (X-4) |
| M5:BIZT-G1-6 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szakmai lektor: AI-generált M5.1/M5.3/M5.4 assetek lektorálási bizonyítéka (PT:224, §9.3) hiányzik; a D9-címke és a blockerek nem módosíthatók (X-16) |
| M5:BIZT-G2-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.A:437 „vagy a telefonján mutatjuk meg” — kiskorú postere személyes telefonra kerülhet (HUM-PRIV-02) — DPO + modulgazda (X-4) |
| M5:BIZT-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M2:BIZT-G2-3 (M5.4:45/:323 „csak a kijelölt mentorod” ↔ ADV §11:245; BIZT-2/5 nyitott DPO-kérdés, X-4); a második képző része = M3:BIZT-G2-5 |
| M5:BIZT-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | csak az (a): M5.4:42 just-in-time doboza nem nevezi meg a kapueredményt (GATE-CP); ADV §11:241 tagmondata szó szerint; (b),(c) elvetve (riport I.2) |
| M5:BIZT-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.4 SLIDE 6 önellenőrzés rögzítésmentes útja (ADV §5:150, §3:115, HUM-PRIV-01); a ✅ és completion nem változik — DPO (X-4) |
| M5:BIZT-G2-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.F:305 név nélküli táblára írt hiány kis létszámnál visszaazonosíthat; létszámküszöb nem írható be — DPO + értékelési felelős (X-4) |
| M5:BIZT-G2-6 | P1 | objektív | MEGERŐSÍTVE | OPEN | M5.F:55, :143, :396–399 közös/tartalék eszköz: kijelentkezési mondat hiányzik (A11Y:57 szó szerint); a jelszómentés X-4 kérdése marad (riport I.2) |
| M5:BIZT-G2-7 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:BIZT-G1-3 (M5.F:3 ugyanaz a sornév-eltérés, „Mentori 1:1 meta-napló” → „Mentori fejlesztési jegyzet”) |
| M5:BIZT-G2-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:BIZT-G1-5 (M5.4:146–148, M5.B:312/:170/:310 ugyanaz a valós-kvuca döntés) |
| M5:BIZT-G2-9 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M5:BIZT-G1-4 (M5.4 Google-sablonja, ADV:87/:207; `PRIVACY_CONTACT_TO_CONFIGURE` hiánya); a szervezeti fiók kérdése = M2:BIZT-G1-7 (X-4) |
| M5:BIZT-G2-10 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M5:BIZT-G1-6 (M5.3 ILL-01/IKO-01/ILL-02 és M5.4 ILL-01 provenance „ai”, ugyanaz a hiányzó lektorálási bizonyíték) |
| M5:ERT-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: QUIZ-D „attempt submitted” üres beadással is teljesül-e; a CP-completion jelentése = M0:IMPL-3 — projektgazda (X-6) |
| M5:ERT-G1-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:PED-G1-1 ((a),(b) a kapu egysége; a (c) „gyakorlás”-horgony = M5:PED-G1-2) |
| M5:ERT-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | KAPU:69/:196/:223/:241 betűjeles visszajelzés ↔ válaszkeverés (KAPU:23); M5.1:477/:529 sorszó cserélendő a tartalmi névre; kulcs és Disztraktor-indokok maradnak (riport I.2) |
| M5:ERT-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: diagnosztikus kvíz „Attempts allowed” (2 vagy 3), melyik próbálkozás adja a jelzőt, fogalomcsaládonkénti jelzés — értékelési felelős + projektgazda (X-6) |
| M5:ERT-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:154/:177, KAPU:303 és M5.F:45/:380–415 nem mondja ki a Q-REL-2 javító határidőt (hétfő után szerda 18:00, HUM:510); relatív hétköznap, dátum nem (riport I.2) |
| M5:ERT-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:PED-G1-3 (M5.A:259 matek-szakkör határeset ↔ :248 SULI-kulcs, ugyanaz a formális/nonformális döntés) |
| M5:ERT-G1-7 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított szintleírás-hiány: a KAPU:293 R2 Alapszint-vastagítása és az átmenő szabály egyértelműen kizárja a „csak kor” sort (riport I.5) |
| M5:ERT-G1-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:PED-G1-4 (az M5.2 B–D ág visszajelzés-hiánya; a SLIDE 3 igaz/hamis-alpontja oda olvad) |
| M5:ERT-G1-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.2 SLIDE 8 ✅ „előbb a cél” (:558) ↔ SLIDE 7/HUB négytagú lánc (feladat elsőbbsége) — M5 szerzője + értékelési felelős (X-6) |
| M5:ERT-G1-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:PED-G1-10 ((a) ugyanaz a mérés-hiány; a (b) 2. kompetencia R1-hiánya elvetve) |
| M5:ERT-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szakmai lektor: a KAPU szakmai lektorálása (PT:277/:391 §9.2) az M5-re nincs bizonyítva az RR-ben; kulcs, küszöb, rubrika nem változik (X-16) |
| M5:ERT-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.4:163/:254 önellenőrzése csak a fogalom megjelenését kérdezi, az R4 ismérve (konkrét cselekvés) csak :320/KAPU:295-ben áll; SLIDE 6 ✅ marad (riport I.2) |
| M5:ERT-G2-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:PED-G2-1 (M5.4:314/:94 azonnali leadás ↔ MAN:83 „M5.B után” nyitás, ugyanaz a sorrend-hiba) |
| M5:ERT-G2-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.4 SLIDE 6 „✅ Igaz rám” pontozatlan önellenőrzéssé váljon-e (D-d/D-i új esete) — értékelési felelős, projektgazdával (X-6) |
| M5:ERT-G2-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:PED-G2-5 (az M5.3-rész: a 72 órás LMS-M5-07 előrejelzése hiányzik); a kvíz-alpont elvetve |
| M5:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.B:273 „Nonformálisban akkor tanulnak…” ellentmond az M5.B 2. céljának és a KAPU Q4-D/Q2-A indokainak; csere az M5.F:353 kánoni mondatára, a „Hamis” kulcs marad (riport I.2) |
| M5:ERT-G2-6 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiány: az M5.F:387/:395 már minden jelzett szempont átdolgozását kéri, a teljesítési feltétel az M5.4:320/KAPU:288-ban áll, ismétlése redundancia (riport I.5) |
| M5:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.F:80–81-ből hiányzik a KAPU:303 „mentor átnézi… a kvíz item-szintű analitikájával” lépés; csak a :80-ba, „mentor” alannyal; kvízadat nem kerül táblára (riport I.2) |
| M5:ERT-G2-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.3:591/:606 könnyen kizárható elosztó cseréje answer key-közeli kérdés, kiterjed-e rá az M3:ERT-G2-7-döntéstípus — értékelési felelős (X-6) |
| M5:ERT-G2-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.4:146 „legyen” ↔ HUB:20 „lehet” — a valós kvuca-sor kötelező vagy opcionális besorolása — modulgazda + értékelési felelős (X-10) |
| M5:IMPL-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:IMPL-3 (summary-slide.js: a CP-completion a megválaszoltságtól függetlenül beáll, BSPEC-06; új döntést nem nyit, X-6) |
| M5:IMPL-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | a betűjeles rész = M5:ERT-G1-3; önálló: a két Moodle-szint („Shuffle within questions” + kérdésenkénti „Shuffle the choices?”) megnevezése build-megjegyzésként (riport I.2) |
| M5:IMPL-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | a KAPU:305 GATE-CP tartalékútja ütközik a MAN:171 „tartalékút nincs” (BS-D1, HUM:515) elvével; a MAN §4 „megerősítve/complete” megkülönböztetése átvezetendő (riport I.2) |
| M5:IMPL-G1-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:PED-G1-11 (az első mondat törlése túlvág; a PED-G1-11 cseréje a használandó javítás) |
| M5:IMPL-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.1:32 Moodle-intro ↔ MAN:79 „Név”; M5.4:314 Assignment-név ↔ MAN:83: a lecke veszi át a MAN „Név” értékét (M4:IMPL-G1-8 minta); H1, fájlnév nem változik; pin (riport I.2) |
| M5:IMPL-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.1:147 téves kereszthivatkozás: a típust nem az RA rögzíti; „csak Continue” vezérlő (:182) nem létezik; minta M2:IMPL-G2-2, Z.1:57 (riport I.2) |
| M5:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.1:424/:650 „5–6 helyzet egymás alatt” + „nagy érintőgombok” a CP rögzített-koordinátás elrendezésével ütközik; „Display as button” opció (M7.4:453 minta) (riport I.2) |
| M5:IMPL-G1-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:ERT-G1-4 (Review options / kulcsfelfedés ugyanaz a döntés; a „Whether correct” objektív alpontja a K7-döntéssel együtt) |
| M5:IMPL-G1-9 | P2 | objektív | ELVETVE | REJECTED | a KAPU:28 just-in-time doboz már specifikált (PT §4, ADV §3); az M3-minta új projektgazdai döntésből jött, az M5-re megírása preferencia (riport I.5) |
| M5:IMPL-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.1:16–22 AI-médialista kihagyja a NAR-02 és a DIA-01 asseteket; a D-19/D-21 VO-leirat-mondat nincs átvezetve; `@asset` nem változik, csak build (riport I.2) |
| M5:IMPL-G1-11 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: a DIA-01/ILL-01 elhelyezése az `@asset`-ben rögzített, az IKO-01 kiváltja a nyers emojikat, a SLIDE 9 saját jegyzetet enged (riport I.5) |
| M5:IMPL-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.2 Moodle-introjából hiányzik az A11Y:37–38 „mikor kész” félmondat; a címsor a K15-döntést követi; completion nem változik (riport I.2) |
| M5:IMPL-G2-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:PED-G2-1 (M5.4:32/:311–327, M5.B:170 ugyanaz a sorrend-hiba; a :327 Assignment-link javaslata az IMPL-G2-5 korlátja alá esik) |
| M5:IMPL-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.3 §3.6 felidézésének H5P-típusa, amely „Receive a grade”-et adna (N-M5-08) — LMS-gazda + lektor (X-11); objektív alpont: IMPL-G2-2.obj |
| M5:IMPL-G2-2.obj | P1 | objektív | MEGERŐSÍTVE | OPEN | M5.3:524 „Moodle Label /” törlése (nem adhat gradet) és a MAN:85 zárójelének igazítása egy szerkesztésben; kánoni közös fájl, csak a review után (riport I.2) |
| M5:IMPL-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.3:108/:303/:330 Single Choice kérdésekhez nincs SCS-kizáró megjegyzés (:355 minta); típusnév marad, M4-precedens szerinti fejlesztői megjegyzés kerül mellé (riport I.2) |
| M5:IMPL-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:ERT-G2-3 (a „Checkbox” fejlesztői sor az answer key-t értelmezné át, döntés nélkül nem objektív) |
| M5:IMPL-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.4:71/:327 nem létező gombot és átirányítást ír elő (Column lapozás nélküli, h5p.org/column); „Interakció: nincs” csere; a :327 a K14-gyel egy megoldás (riport I.2) |
| M5:IMPL-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.4 SLIDE 4–5 (:203, :231) „letölthető sablon” helye nincs rögzítve; csak a minimum (.docx/.xlsx elérhető a SLIDE 4-től); Google-ág kimarad (riport I.2) |
| M5:IMPL-G2-7 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:BIZT-G2-6 (M5.F:55/:143 ugyanaz a kijelentkezési mondat hiánya) |
| M5:IMPL-G2-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:BIZT-G1-3 (az M5.F-hely ugyanaz a sornév-eltérés) |
| M5:IMPL-G2-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:PED-G2-13 (az M5.F:11-rész ugyanaz a HÉTKÖZNAPOK-címke eltérés; a fájlnév ↔ H1 eltérés nem javítandó) |
| M5:IMPL-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.A/M5.B/M5.F nyolc elavult `@asset`-sorszáma (pl. M5.B:220 „100-121.sor” ma 260–281); csak szakaszhivatkozásra cserélhető, build úton (riport I.2) |
| M5:IMPL-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.3:508 „billentyűzettel és képernyőolvasóval” a WCAG 2.1.1-hez nem ad jogcímet a képernyőolvasóra; kiegészítés: „4.1.2 Name, Role, Value (A)” (riport I.2) |
| M5:IMPL-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.B:188/:474 kézfeltartás ↔ :255–256/`@asset`:220 „két oldalra állás”; igazítás a 4.1-hez; „hamis” külön jelzése új tartalom, nem kerül be (riport I.2) |
| M5:IMPL-G2-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | MAN:82 „vázlatmezője” beviteli mezőt sugall, az M5.4:203/:231 „Beviteli elem nincs”; csak a szó cserélődik, a REQUIRED_BUT_LEARNER_LOCAL (D-4) marad (riport I.2) |
| M5:NYELV-G1-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | „mini-kvíz”, „Mini-célmagyarázat” stb. HUB/M5.1/M5.2/KAPU hét helyen; a KAPU négy „mini-kvíz” a NYELV-G2-11 a)-val egy menetben; ✅ és opciósorrend marad; pin (riport I.2) |
| M5:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | „rubrika-soron” stb.: a) HUB/KAPU/M5.2; c) KAPU:288 „javításra-visszaküldést”; b) G2-helyei = NYELV-G2-11 b); d) a kánonnal együtt; e) elvetve; pin (riport I.2) |
| M5:NYELV-G1-3 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: a „hétköznapi, spontán helyzet(ek)” a HÉTKÖZNAPOK-címke magyarázó alakja, nem versengő címke (DÖNT-1002:97); rossz javítási út (riport I.5) |
| M5:NYELV-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:46/M5.1:648 „True-False” ↔ M5.1:400/RA:21 „True/False”; egységesítés a K13/PED-G1-7 javításával az M5.1:648-on egy menetben; „A Branching” elvetve (riport I.2) |
| M5:NYELV-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.2:417 „és utána megnézitek” kijelentő mód a felszólító célfelsorolásban; „megnézzétek” csere; a :255 marad; pin (riport I.2) |
| M5:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.2:309 „– játékos, – mozognak…” exportmaradvány gondolatjelekkel; csak a gondolatjelek törlődnek; „ismerkedés-bizalomépítés” elvetve; pin (riport I.2) |
| M5:NYELV-G1-7 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: az M5.2:204 dőlt zárójel fejlesztői jegyzetforma, a KAPU:183/:203 visszajelzése maga szól a tanulóhoz (riport I.5) |
| M5:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.2:9 „…a Branching Scenario egyetlen végképernyője” bekötetlen mondatvég; „végképernyőjéig” csere, csak a rag; completion-logika nem változik (riport I.2) |
| M5:NYELV-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:211 „Ez a sor dönti el” mutató névmás kétértelmű; csere a KAPU:284 szó szerinti alakjára, a K1 (ERT-G1-2) :211-es egységesítésével egy menetben (riport I.2) |
| M5:NYELV-G1-10 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított terminológiai hiba: HUB:20/:140 és a KAPU:303 kánoni rövidítések, a csere szükségtelen módosítás (riport I.5) |
| M5:NYELV-G1-11 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: KAPU Q12 A/B/D első személy ↔ ✅ C harmadik személy — igazodjon-e a kulcs a disztraktorok nézőpontjához — értékelési felelős + modulgazda (X-6) |
| M5:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | (a) KAPU:300 „diagnosztikus visszajelzés” → „fejlesztő visszajelzés” (KAPU:303/HUB:177 kánoni név); (b) elvetve; a K2-döntéssel egy menetben (riport I.2) |
| M5:NYELV-G1-13 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított nyelvtani/egyértelműségi hiba: KAPU:87/:105/:32 stáboldali fordulatok, a HUB:48 pleonazmusa a NYELV-G1-1 b)-be olvad (riport I.5) |
| M5:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.2:388, KAPU:87/:299 „+” kötőszó helyett; HUB:213 „vagy” előtti vessző; a KAPU:299 a K2 kalibrációs döntésével egy menetben; pin (riport I.2) |
| M5:NYELV-G1-15 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: a KAPU:75 félig függő beszéde bevett és érthető, a kvíztétel átírása szükségtelen módosítás (riport I.5) |
| M5:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:IMPL-G2-12 (ugyanaz a tényállás; a :188 javasolt szövege nem használható, az 1. regressziós minta miatt) |
| M5:NYELV-G2-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:PED-G2-13 (csak az M5.F:11-rész); az M5.4:162 „random energizer” és a „??”→„?” elvetve |
| M5:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | a) M5A:399 tárgyrag; b) M5B:269 „mint ha”; c) M5B:326 „fejből”; d) M5B:273 (ha a K25 cseréli, tárgytalan); e) elvetve; pin (riport I.2) |
| M5:NYELV-G2-4 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: az M5B:410 „ott…, hogy” köznyelvi szerkezet, a javaslat szerkezetileg átírná a mondattövet, preferencia (riport I.5) |
| M5:NYELV-G2-5 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: „futtass át”, „ne hidegen jelenjen meg” regiszterkérdés; az M5F:81 javaslata ütközik az ERT-G2-7-tel (riport I.5) |
| M5:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5A:280/:382 „ki mit mond” ↔ :392 „nem kell szóbeli prezentáció” ellentmondás; csere a :392 saját szavaira; idősávok nem változnak; pin (riport I.2) |
| M5:NYELV-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.4:42 „Ne írj bele…” névmási referenciahiba (a „bele” a vázlatra utal); a vázlat-mondat a bekezdés végére kerül; egy menetben a BIZT-G2-3/BIZT-G2-2-vel (riport I.2) |
| M5:NYELV-G2-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:IMPL-G1-5 (a) rész (M5.4:314 ↔ MAN:83); b) elvetve |
| M5:NYELV-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5A/M5B/M5F „4. Blokk-leírások” → „Blokkleírások” (kéttagú összetétel, M2.A:78 minta); csak a három fejléc (riport I.2) |
| M5:NYELV-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5A:47/M5B:79 „madrihok” → „madrihok / madrihot” (GL:72); csak a „/ madrihot” kerül be, a „kb. 15+” marad (riport I.2) |
| M5:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | a) „mini-feladat” stb. hét fájlban; b) „pötty-matrica”, „pótvizsga-íze”, M5.4:82 „Minta-táblázat” is; c) elvetve; „mini-táblázat” csak együtt; pin (riport I.2) |
| M5:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | felolvasandó szövegben perjel (M5A:431/:454/:470, M5B:370) → „vagy”; „Pl./Kb./max.” és táblamezők elvetve; M5B:312 a K5-döntés után; pin (riport I.2) |
| M5:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5F:46 „M5.3-at” hiányzó névelő (M0:NYELV-G1-13 minta); az M5B:170 alpont elvetve, ha a K14 cseréli, tárgytalan; egy menetben a K8-cal (riport I.2) |
| M5:NYELV-G2-14 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5A:524 zárókör minimuma (mindenki vagy néhány fő) a :496 passzjog érintetlenül hagyásával — modulgazda (X-10) |
| M5:NYELV-G2-15 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:BIZT-G2-1 (M5.A:437 „telefonján” birtokosa a döntés eldönti) |
| M5:NYELV-G2-16 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: az M5.3:300–301 általános alanyú szerkezet, a válaszopciók egyértelművé teszik, alacsony bizalom (riport I.5) |
| M5:NYELV-G2-17 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: a „csendes pótlással pótolják” szóismétlés stílus, az „itt élj” kétértelműsége nem bizonyított, preferencia (riport I.5) |
| M5:NYELV-G2-18 | P2 | objektív | ELVETVE | REJECTED | nincs bizonyított hiba: az L1–L4 megfeleltetés a POSZ-01 poszteren és felolvasva is látható, alacsony bizalom (riport I.5) |
| M5:PED-G1-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a kapu egysége táblázatsor vagy rubrikasor (KAPU:286 ↔ HUB:176); kötelező-e elem minden sorban — értékelési felelős + projektgazda (X-6) |
| M5:PED-G1-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az R4 „gyakorlás”-horgonya szűküljön-e, vagy a GL:197 tág definíció marad — értékelési felelős + módszertani lektor (X-6) |
| M5:PED-G1-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.1 SLIDE 4 1./4. helyzet „formális” kulcsa ↔ a lecke „kívül vagy mellett” definíciója és az M5.A:259 szándékos határesete — M5 szerzője/modulgazda (X-10) |
| M5:PED-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.1 SLIDE 4 hat helyzetéből öthöz és az M5.2 B–D ághoz hiányzik vagy jegyzetszintű a visszajelzés — M5 szerzője/projektgazda (X-10); objektív alpont: PED-G1-4.obj |
| M5:PED-G1-4.obj | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.1 SLIDE 4 2./3./5./6. helyzet zárójeles indoklása semleges visszajelzésként; SLIDE 3 :414 mindkét válaszra; 4C/4D cím+kérdés a 4A-ból (riport I.2) |
| M5:PED-G1-5 | P2 | emberi-döntés | ELVETVE | REJECTED | preferencia: a 4A/5A/5C visszajelzése kvucánként már más irányt ad, a KAPU Q7 csak a sorrendre küld vissza; a javaslat új didaktikai tartalom (riport I.5) |
| M5:PED-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: HUB:208 „célzott felzárkóztatás” ígérete végrehajtó nélkül, ki/mikor/mit tesz — programvezető + értékelési felelős (X-10) |
| M5:PED-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.1:646 „10–15 perc” ellentmond a lecke metájának (15–20) és a HUB:41-nek; csak az összeg igazítása, a részidők nem; 3,5 óra nem változik (riport I.2) |
| M5:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | HUB:41/:92/:219/:227 „random” tilos kanonikus címke (HUM:472, DÖNT-1002:97); csak a hub-helyek; a link célja és a fájlnév marad, átnevezés nem része (riport I.2) |
| M5:PED-G1-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:ERT-G1-9 (M5.2:558 ✅ ↔ :534 „a feladatból indulunk”; nem bizonyított objektív hiba, mert mindhárom disztraktor is a célra épít) |
| M5:PED-G1-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: HUB:18/:33 „saját szavaival elmagyarázza” kompetenciát semmi nem méri (kvíz zárt, rubrika a 4. kompetenciát méri) — ugyanaz a kaputípus, mint M2:ERT-G1-5 (X-14) |
| M5:PED-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.1:24/:648 még a H-6 előtti utat írja ↔ D-6/H-6 (HUM:527) lezárt döntés; csere a lezárt állapotra (RA 24. pont); SLIDE 6 tanulói szövege nem változik; pin (riport I.2) |
| M5:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | M5.4:32/:314 azonnali leadást kér ↔ MAN:83 „M5.B után” nyitás; intro+SLIDE 7 mondja ki a nyitást és hogy a vázlatot el kell hozni; határidő csak M5.B:93-ból (riport I.2) |
| M5:PED-G2-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:ERT-G2-1 (M5.4:163/:254 önellenőrzés ↔ :320 R4-ismérv); a SLIDE 3 Igaz/Hamis-cseréje elvetve, szükségtelen új tartalom |
| M5:PED-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.F:213 a Hiányos-átdolgozást a leckék befejezéséhez köti, ellentmond a 2. célnak és a HUM:221-nek; csak a :153/:213–215 sorrendje; blokkidők nem változnak (riport I.2) |
| M5:PED-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.B:339/:367 a Somer-kártyákat is a sulis/spontán mezőhöz méri, de a 2./5./7./10. kártya kész Somer-peula; elég a :358 mondat, kártyakészlet nem változik (riport I.2) |
| M5:PED-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | a kötelező 72 órás LMS-M5-07 (HUM:224) előrejelzése hiányzik az M5.3 introból/OUTRO-ból; csak a HUB:191/:516 meglévő szabálya; emlékeztető nem ígérhető; pin (riport I.2) |
| M5:PED-G2-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.A/M5.B/M5.F több blokkja túlfut a kijelölt sávon, melyik lépés rövidüljön — modulgazda, vétó/QA programvezető (X-10); objektív alpont: PED-G2-6.obj |
| M5:PED-G2-6.obj | P2 | objektív | MEGERŐSÍTVE | OPEN | az M1.A:195 névkihagyási mondata átvehető az M5.A 4.1-be (max 24 fő, 5 perc), a mondatvég az M5.A-hoz igazítva (riport I.2) |
| M5:PED-G2-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:PED-G1-2 (ugyanaz a Glosszárium-döntés; a „mozognak”-törlés objektív alpontja elvetve, a felsorolás nem kifogásolható) |
| M5:PED-G2-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:ERT-G2-5 (ugyanaz a tényállás; a „beég” alpont elvetve, a KAPU:241 is ezt a fordulatot használja) |
| M5:PED-G2-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:IMPL-G2-12 (M5.B:188/:474 kézfeltartás ↔ „fel tudnak állni”; az a11y-indoklás átvehető) |
| M5:PED-G2-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M5:PED-G1-3 ((a) a kulcs/határeset-ütközés; a (b) sarokjáték-ismétlés elvetve, önmagában nem hiba) |
| M5:PED-G2-11 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.3:537 a helyességtől függetlenül nyugtáz, nincs önellenőrző lépés a felidézés után (N-M5-08, IMPL-G2-2 párja) — modulgazda (X-11) |
| M5:PED-G2-12 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M5:ERT-G1-5 (M5.F:45/:387/:413–415 G2-helyek, ugyanaz a hiányzó javító határidő) |
| M5:PED-G2-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | M5.F:11 „Suli / Somer / random” ↔ M5.1:1 „…hétköznapok” (HUM:472); csak a :11 sor, a fájlnevek maradnak (riport I.2) |
| M5:PED-G2-14 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: M5.A:240 sarokjátéknak nincs mozgás nélküli módja (a galériasétán van); új instrukció — modulgazda + hozzáférhetőségi gazda (X-10) |

## Napló

| Idő | Fázis | Esemény |
|---|---|---|
| 2026-10-11 | — | A ledger létrehozva a harness v2-vel; nincs aktív futás. |
| 2026-10-11 | PREFLIGHT | `AP-2026-10-11-01` indul (`next-version`), bázis `main@213a4c5`, munkaág `next-version/AP-2026-10-11-01`. Kiinduló gépi állapot: `content_integrity.py` → „Objective integrity errors: 0”, kilépési kód 0; `--release-report` → `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`, `LEARNER-RELEASE-VERDICT: NO-GO`. A #26–#29 merge-commitok a `main`-ben; X-1, X-2, X-3 RESOLVED (git-bizonyíték a kapusorokban). |
| 2026-10-11 | INVENTORY | M0: a 82d0c7c óta nincs változás a modulban → a négy lencse REUSED, a `language` hiányzik. 40 ID a ledgerben (18 OPEN, 7 DUPLICATE, 7 BLOCKED_HUMAN, 3 EVIDENCE_GATE + 1 DUPLICATE kapu, 4 REJECTED). M1: kivonatolás folyamatban. |
| 2026-10-11 | INVENTORY | M1: 132 sor (116 verdiktes ID + 13 levágott P2 + 3 részsor): 25 OPEN, 12 NEEDS_RECHECK (ERT-G1-1, IMPL-G1-2 az N-M1-04 javítása miatt; 2 részsor; 8 verdikt nélküli levágott P2), 46 DUPLICATE, 21 BLOCKED_HUMAN, 4 EVIDENCE_GATE, 24 REJECTED. A 82d0c7c óta változott M1-helyek (M1.1, MAN :45/:308, RA 24., HUM 12.) más megtartott objektív findinget nem érintenek. Külső kapuk: X-4…X-12. REVIEW indul: M0/M1 `language`, M2 öt lencse. |
| 2026-10-11 | REVIEW | M1 `language` VERIFIED: `2026-10-11 Validált findingok – M1, nyelvi lencse, AP-2026-10-11-01.md` (57 nyers, 57/57 verdikt: 28 MEGERŐSÍTVE + objektív, 7 EMBERI DÖNTÉS (2 duplikátum), 22 ELVETVE); read-only bizonyíték a mentés előtt egyezik. Az M1-re mind az öt lencse lefutott. |
| 2026-10-11 | REVIEW | M0 `language` VERIFIED: `2026-10-11 Validált findingok – M0, nyelvi lencse, AP-2026-10-11-01.md` (42 nyers, 42/42 verdikt: 20 MEGERŐSÍTVE + objektív, 4 EMBERI DÖNTÉS (1 duplikátum), 18 ELVETVE); read-only bizonyíték egyezik. Az M0-ra mind az öt lencse lefutott. M1 NEEDS_RECHECK (12) célzott verifierrel folyamatban; M2 lencsék futnak. |
| 2026-10-11 | RECHECK | M1 12 NEEDS_RECHECK lezárva (`2026-10-11 Célzott újraellenőrzés – M1 NEEDS_RECHECK, AP-2026-10-11-01.md`): ERT-G1-1 és IMPL-G1-2 ALREADY_FIXED (ebf311e, 96996e2; a CC-04/CC-06 rész = M0:ERT-8), PED-G1-8.obj és BIZT-G3-8.obj OPEN, a 8 levágott P2 REJECTED. |
| 2026-10-11 | REVIEW | M2 VERIFIED (öt lencse): `2026-10-11 Validált findingok – M2, AP-2026-10-11-01.md` — 162 nyers finding, 162/162 verdikt (V1–V9): 81 MEGERŐSÍTVE + objektív (19 duplikátum), 6 MEGERŐSÍTVE + bizonyíték-kapu (1 duplikátum), 44 EMBERI DÖNTÉS (10 duplikátum, 1 az M0:NYELV-G2-11-be), 31 ELVETVE. Ledger: 62 OPEN, 30 DUPLICATE, 34 BLOCKED_HUMAN, 5 EVIDENCE_GATE, 31 REJECTED; új kapu: X-14 (helyi someres ideológiai döntések). Read-only bizonyíték a mentés előtt egyezik (`da39a3ee…`). |
| 2026-10-11 | REVIEW | M3 VERIFIED (öt lencse): `2026-10-11 Validált findingok – M3, AP-2026-10-11-01.md` — 186 nyers finding, 186/186 verdikt (V1–V12): 81 MEGERŐSÍTVE + objektív (15 duplikátum), 8 MEGERŐSÍTVE + bizonyíték-kapu (5 duplikátum), 71 EMBERI DÖNTÉS (31 duplikátum, 6 más modul kapujába), 26 ELVETVE. Ledger: 188 sor (+2 `.obj` alpont: IMPL-G2-11.obj, IMPL-G2-2.obj; a BIZT-G1-7 emberi maradéka saját kulccsal) — 68 OPEN, 50 DUPLICATE, 41 BLOCKED_HUMAN, 3 EVIDENCE_GATE, 26 REJECTED; új kapu: X-15 (jogi szakértői értelmezés). Read-only bizonyíték a mentés előtt egyezik (`da39a3ee…`). Közben: M4 verifikálva (103/103), M5 nyers (119), M6 lencsék futnak; a futás 2026-10-11 este egy fiókváltás miatt megszakadt ügynököket a megszakítás pontjáról folytatta. |
| 2026-10-11 | DECISION | Projektgazdai döntés (szó szerint: `2026-10-11 Projektgazdai döntés – autopilot-gyorsítás, AP-2026-10-11-01.md`): (1) javítás átfedéssel a lezárt review-jú modulokban, amíg a többi review fut — minden javítás azonnal commitolva, a közös kánoni fájlok csak az összes review után; (2) legfeljebb 12 párhuzamos read-only ügynök. A CLAUDE.md nem változott. |
| 2026-10-11 | REVIEW | M4 VERIFIED (öt lencse): `2026-10-11 Validált findingok – M4, AP-2026-10-11-01.md` — 103 nyers finding, 103/103 verdikt (V1–V7). Ledger: 106 sor (+3 `.obj` alpont: PED-G1-2.obj, ERT-G1-6.obj, IMPL-G1-6.obj) — 40 OPEN, 31 DUPLICATE (4 más modul kapujába: `M0:IMPL-3` ×3, `M2:BIZT-G2-3`), 21 BLOCKED_HUMAN, 3 EVIDENCE_GATE, 11 REJECTED; új kapu: X-16 (szakmai lektori release-bizonyíték). Read-only bizonyíték a mentés előtt egyezik (`da39a3ee…`). Közben: M5 verifikálva (119/119), M6 lencsék 14/15, M7 G1–G2 lencsék futnak. |
| 2026-10-11 | FIX | M0 (átfedéssel, a projektgazda 2026-10-11-i döntése szerint; csak az M0 hat saját fájlja): `df2792d` fix(M0) + `69c2017` chore(media). 31 FIXED, 2 `.obj` FIXED (PED-5.obj, NYELV-G2-1.obj); PED-5 és NYELV-G2-1 maradéka BLOCKED_HUMAN (lépésszintű vágási terv, X-10); NYELV-G2-18 IN_PROGRESS (Z.A-rész a Z-körrel); ERT-2, ERT-8, IMPL-2, IMPL-5 OPEN (közös kánoni fájl, az összes review után). Gépi ellenőrzés a végállapoton: `content_integrity.py` 0 hiba; `git diff --check` tiszta; `--pin-visible` egyszer (6 fájl); `media_manifest.py build` kétszer, `check` OK, `reconcile` OK; `unittest tools.test_media_manifest` 159 OK. A futó M6/M7/Z review-k scope-fájljai nem változtak (`git diff --stat df2792d~1 69c2017` csak az M0 hat fájlját, a `Média-assetek/` generált kimeneteit és a `tools/approved-visible-text.json`-t mutatja; az M5, M6, M7 és Z mappájára üres). Célzott diff-ellenőrzés (NYELV, BIZT, ERT/PED, IMPL) fut. |
| 2026-10-11 | REVIEW | M5 VERIFIED (öt lencse): `2026-10-11 Validált findingok – M5, AP-2026-10-11-01.md` — 119 nyers finding, 119/119 verdikt (V1–V8). Ledger: 122 sor (+3 `.obj` alpont: PED-G1-4.obj, PED-G2-6.obj, IMPL-G2-2.obj) — 50 OPEN, 31 DUPLICATE (2 más modul kapujába: `M0:IMPL-3`, `M2:BIZT-G2-3`), 23 BLOCKED_HUMAN, 3 EVIDENCE_GATE, 15 REJECTED; a kapuk a meglévő X-4, X-5, X-6, X-10, X-11, X-12, X-14, X-16 sorokba (új kapu nincs). Read-only bizonyíték a mentés előtt (HEAD `c6b8254`) egyezik (`da39a3ee…`); a review alatt csak az átfedéses M0-javítás (`df2792d`, `69c2017`) változott a `02 Tervezet/` alatt, az M5 fájljai nem. Közben: M6 klaszter-térkép kész, 8 verifier fut; M7 (183 nyers) és Z (57 nyers) minden lencséje mentve; az M0 célzott QA-ja 15 nyers findinget adott (`2026-10-11 Célzott QA – M0 javítás (df2792d), AP-2026-10-11-01.md`, verifier fut). |
| 2026-10-12 | REGRESSION | M0 célzott QA (a `df2792d` diff-hunkjaira, négy lencse + verifier): 15 nyers, 12 MEGERŐSÍTVE + objektív (6 megtartott, 6 duplikátum — egy a meglévő `M0:NYELV-G2-1` 45’-ös részébe), 3 ELVETVE. A 6 megtartott javítva: `1d9d15f` fix(M0) + `e16a4e1` chore(media); `content_integrity.py` 0 hiba, `git diff --check` tiszta, `--pin-visible` egyszer (4 fájl), build kétszer, `check` OK, `reconcile` OK, `unittest tools.test_media_manifest` OK. Ledger: `M0:QA-*` sorok (6 FIXED, 6 DUPLICATE, 3 REJECTED). A futó M6/M7/Z review-k scope-fájljai nem változtak. Az M0 Javítása FIXING marad: a kánoni rész (ERT-2, ERT-8, IMPL-2, IMPL-5, NYELV-G2-18 Z.A) az összes review után. |
| 2026-10-12 | FIX | M1 (átfedéssel, csak az M1 kilenc saját fájlja): `ed4f52d` fix(M1) + `506fa78` chore(media; build kétszer, `check`, `reconcile`, unittest OK); `content_integrity` 0 ERROR, `git diff --check` tiszta, a teljes diff visszaolvasva, egy `--pin-visible` a FIXED ID-kkal. 47 FIXED, 3 `.obj` FIXED (IMPL-G1-8.obj, ERT-G2-5.obj, NYELV-G2-5.obj); BLOCKED_HUMAN: BIZT-G2-3 (X-5, a BIZT-G2-1/-G2-10 döntésével egy lépésben), IMPL-G1-8 és PED-G3-8 (X-10), ERT-G2-5 S-sor (X-6), BIZT-G2-7, NYELV-G1-6, NYELV-G2-5 VO-része (új kapu: X-17, hanggyártási fix pack); IN_PROGRESS: ERT-G2-6 (a manifest-sor a közös kánoni körben). A futó M6/M7/Z review-k scope-fájljai nem változtak. Következik: célzott QA. |
