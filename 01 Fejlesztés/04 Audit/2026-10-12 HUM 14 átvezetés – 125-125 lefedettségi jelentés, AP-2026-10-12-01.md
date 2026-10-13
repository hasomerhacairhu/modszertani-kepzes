# HUM 14. szakasz átvezetése – 125/125 lefedettségi jelentés, AP-2026-10-12-01

| | |
|---|---|
| Run-ID | `AP-2026-10-12-01` (változat: `next-version`) |
| Ág | `next-version/AP-2026-10-11-01` |
| Bázis | `beaea60` (a döntések: `aa126a5`, `Emberi jóváhagyás szükséges.md` 14. szakasz) |
| A tananyag utolsó változása, záró ellenőrzés | `33aec89` |
| Dátum | 2026-10-12 |
| Felhatalmazás | `2026-10-12 Projektgazdai felhatalmazás – a HUM 14. szakasz átvezetése, AP-2026-10-12-01.md` (szó szerint) |
| Ledger | `AUTOPILOT-LEDGER.md` (Run AP-2026-10-12-01) |
| Állapot | a futás záró jelentése; **nem release-jóváhagyás** |

A `main`, a futó M0/M1 pilot és a CC-04 freeze érintetlen. A PR #30 draft; merge, staging deployment és learner release nem történt. A 16 bizonyíték-kapu nyitva van (9. szakasz).

## 1. Összegzés

- **125 döntés** (53 `A`, 72 `F`), mindegyikhez egy sor a 13. szakasz táblájában: implementáció (hely + commit), blokkállapot, tesztelés, fennmaradó külső függőség.
- **IMPLEMENTED: 41** · **QA-RA VÁR: 17** · **KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ: 67**.
- **Besorolási szabály:**
  - IMPLEMENTED: a döntés tartalma a fájlokban van, a célzott QA lefutott, és a G1–G8 szerepköri bizonyítékon túl nincs nyitott emberi döntés vagy külső feltétel.
  - QA-RA VÁR: az átvezetés megtörtént, de a célzott QA egy szerepköri döntést vagy kalibrációt nyitott, amely a döntés hatókörét érinti (6. szakasz).
  - KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ: a döntés maga nevez meg külső feltételt vagy bemenetet (runtime-teszt, szerepkiosztás, DPO/jogász, Memuna, VO-render, `tools/`-változás, `/course-develop`, felhasználói átnevezés, új itemdöntés), vagy szándékosan csak részben alkalmazható. Az `F` döntéseknél addig az óvatos alapértelmezés él a fájlokban.
- Az IMPLEMENTED sem release-jóváhagyás: a G1–G8 kapuk szerepköri bizonyítéka és a go/no-go döntés hiányzik (`RELEASE-READINESS.md`).
- A bizonyíték forrása: a fájlok végállapotának visszaolvasása (három független ellenőrző ügynök döntésenként, a fő session hat saját visszaolvasása, és a 4. szakasz gépi blokk-nyomkövetése), a commitok és a parancskimenetek. A ledger és a riportok csak hivatkozások.

## 2. Záró validáció (a végállapoton)

Ellenőrzött commit: `33aec89` (a tananyag utolsó változása; utána csak audit-fájlok változnak). A `/release-check` skill (külön subagentben fut) kétszer is üres eredményt adott vissza („Skill execution completed”). Ezért az ellenőrzőlistáját (CLAUDE.md „Ellenőrzés és release”, a skill 1–5. pontja) a fő session futtatta, ugyanazokkal a parancsokkal. Minden parancs 0-s kilépési kóddal futott le, kivéve a sandbox-próbát: annak a bukása a várt eredmény.

| Ellenőrzés | Parancs | Eredmény (szó szerint) |
|---|---|---|
| Python | `python3 -X pycache_prefix=… -m py_compile tools/*.py` | hiba nélkül |
| Integritás, selftest | `python3 tools/content_integrity.py --selftest` | `Selftest: 57/57 eset rendben.` |
| Integritás | `python3 tools/content_integrity.py` | `Objective integrity errors: 0` |
| Release-riport | `python3 tools/content_integrity.py --release-report` | `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` · `LEARNER-RELEASE-VERDICT: NO-GO` (alias: `RELEASE-VERDICT: NO-GO`) |
| Média-baseline | `git cat-file -e a8629732…^{commit}` | megvan |
| Média, selftest | `python3 tools/media_manifest.py --selftest` | `--- selftest OK (0 hiba) ---` |
| Média, validate | `python3 tools/media_manifest.py validate` | `OK — 416 asset, 903 deliverable, 123 forrásblokk, 84 fájl.` |
| Média, check | `python3 tools/media_manifest.py check` | `OK — 10 generált kimenet naprakész, 747 történeti sor egyeztetve.` |
| Média, reconcile | `python3 tools/media_manifest.py reconcile` | `Történeti sor: 747 · diszpozícionálva: 747 · nem egyeztetett: 0` |
| Média, lint | `python3 tools/media_manifest.py lint --high-only` | `1 jelzés, ebből 0 HIGH.` |
| Regressziós tesztek | `python3 -m unittest tools.test_media_manifest` | `Ran 159 tests` · `OK`, skip nélkül |
| Whitespace | `git diff --check`; `git diff --check origin/main...HEAD` | tiszta; a PR-tartomány az öt QA-riport fájlvégi üres sorának javítása (`596c699`) után |
| Munkafa | `git status --short` | csak a lezárás alatt álló `AUTOPILOT-LEDGER.md` (a záró audit-commitban kerül be) |
| Governance | settings-JSON, `bash -n` a két hookra, guard-selftest, ledger-selftest, workflow-selftest és -futás | `--- selftest OK ---` (guard: 303 must-block, 158 must-pass); `workflows read-only OK (1 fájl)` |
| Sandbox | `touch .sandbox-probe` | `Operation not permitted`: a sandbox aktív (ez a várt eredmény) |
| Ledger | `python3 tools/autopilot_ledger.py validate`, `check` (a lezárt ledgeren) | `AUTOPILOT-LEDGER: VALID`; `AUTOPILOT-LEDGER: TERMINAL`, kilépési kód 0; `AUTOPILOT-RESULT: OPEN_ITEMS_REMAIN` |

A `READY_FOR_STAGING_BUILD` nem release-jóváhagyás. A learner-verdiktet blokkoló sorok (a build-verdiktet nem blokkolják), szó szerint:

```
POST-BUILD: CHECKLIST 14 open (SAFEGUARDING 1, PRIVACY 2, A11Y 10, RELEASE-READINESS 1)
RELEASE-EVIDENCE: CHECKLIST 8 open (SAFEGUARDING 2, PRIVACY 4, A11Y 2)
FINAL-RELEASE-QA: CHECKLIST 15 open (SAFEGUARDING 6, PRIVACY 1, A11Y 8)
SIGNOFF: CHECKLIST 4 open (SAFEGUARDING 3, RELEASE-READINESS 1)
POST-BUILD: BUILD-OUTPUT 75 unresolved BUILD_OUTPUT values
POST-BUILD: ENVIRONMENT-RECORD 19 unresolved RUNTIME_OUTPUT values
POST-BUILD: RUNTIME-TESTS 38 not RUNTIME_VERIFIED
MEDIA-RELEASE: MEDIA-ASSETS 1 on fallback: M0.3-FOTO-01
MEDIA-INFO: MEDIA-PHASE-UNASSIGNED 412 asset (release_phase hiányzik; alapértelmezés: voiceover → B, video → C, minden más → A)
MEDIA-INFO: PRODUCTION-RULES 2 open: R2, R3 (asset-szinten értékelve)
MEDIA-INFO: RIGHTS-SUBGATES 4 HIÁNYZIK: J1, J2, V1, V3
LIFECYCLE: PROGRAM-TRANSFER 1 open (RELEASE-READINESS 1) — release utáni validáció (Q-REL-1), nem kapu
```

## 3. Munkafolyamat és commitok

Modulonként: fix-terv (ellenőrzött OLD/NEW blokkok) → alkalmazás (`fix(<modul>)`) → `media_manifest.py build` (`chore(media)`) → célzott QA a diff-hunkokra (biztonság-jog, értékelés, nyelv, ahol kellett implementáció; verifier) → QA-javítás. A modulok közös kánoni blokkjai (DEFER_CANON) a kánoni körbe kerültek, ugyanilyen QA-val. Új teljes alapreview nem indult.

| Modul | Átvezetés | Média | Célzott QA-riport | QA-javítás |
|---|---|---|---|---|
| M0 | `5484b02` | `0eeb225` | `2026-10-12 Célzott QA – M0 átvezetés (5484b02)` | `a2445ff (+media 68dc5e9)` |
| M1 | `eb4fa6d` | `42635db` | `2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)` | `7a69b9d (+media 7de9164)` |
| M2 | `147f3c3` | `d473ab6` | `2026-10-12 Célzott QA – M2 átvezetés (147f3c3)` | `db724db` |
| M3 | `ce04b9c` | `8602d2a` | `2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)` | `e0d69d4` |
| M4 | `dd64825` | `adf1f41` | `2026-10-12 Célzott QA – M4 átvezetés (dd64825); … nyelvi lencse és verifier` | `64a60d1 (+media b409d02)` |
| M5 | `aadf41b` | `50f2891` | `2026-10-12 Célzott QA – M5 átvezetés (aadf41b)` | `9764987` |
| M6 | `fbebec0` | `ac49d8b` | `2026-10-12 Célzott QA – M6 átvezetés (fbebec0)` | `511d9e0 (+media b409d02)` |
| M7 | `f6e9c6e` | `ae63490` | `2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)` | `0b76212 (+media 7d833d3)` |
| Z | `c5bc2c4` | `56c0f6b` | `2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)` | `a0c0c83` |
| Kánon | `bdb94ab` | `–` | `2026-10-12 Célzott QA – kánoni kör (bdb94ab)` | `35a9ddd` |
| Kánon (ERT-26) | `33aec89` | `–` | `célzott értékelési ellenőrzés a 3 cellára: nincs finding (ledger, Napló)` | `–` |

Minden átvezetés és QA-javítás után: `content_integrity` 0 ERROR, a ✅-szám változatlan (kivétel: 12.3), `git diff --check` tiszta, látható-szöveg pin a döntés- vagy finding-azonosítókkal. A riportok importja: `3704938`, `4d1583f`, `31ef0f2`, `a89bba9`, `a3aadf9`; az öt QA-riport fájlvégi üres sora: `596c699`. Az ERT-26 kánoni részét (PT:183, MAN:83, :86) a 125/125 visszaolvasás találta kimaradtnak (nem volt rá kánoni blokk); átvezetve `33aec89`.

## 4. Blokkszintű nyomkövetés (gépi, a HEAD-en)

A kilenc fix-terv **728 blokkja** a HEAD-en (a futás commitjain végigkövetve, `beaea60..HEAD`):

- **576** blokk új szövege szó szerint a fájlban van;
- **98** blokk bekerült, majd egy QA-javítás finomította (`35a9ddd` 18, `511d9e0` 16, `9764987` 11, `0b76212` 11, `e0d69d4` 10, `64a60d1` 9, `7a69b9d` 7, `db724db` 7, `a0c0c83` 7, `a2445ff` 2) — a finomítás oka a QA-riportokban;
- **39** blokk a saját commitjában módosított alakban került be (4.1);
- **15** blokk szándékosan nincs alkalmazva (4.2).

### 4.1 Módosított alakban alkalmazott blokkok

| Ok | Blokkok |
|---|---|
| ADV-11 közös eszköz: „nem hoz létre” (a „nem hagy rajta” helyett; a döntés: „ne hozzon létre … munkapéldányt”) | M1#98, M2#9, M2#10, M3#125, M3#126, M6#5, M7#129, M7#130, M7#131 |
| GYV-5 létszámszabály: a döntés szó szerinti teljes szövege (két felnőtt VAGY helyettes + kötelező megállítási protokoll; egyszemélyes működés csak dokumentált alacsony kockázatnál) | M2#65, M2#66, M3#116, M6#60, M6#61, M6#62 |
| ADV-1: a kánoni összevont szöveg (csoportszűkítés a beadásokra; a H5P-C/QUIZ/GATE-CP kiterjedés nyitott emberi döntés, CANON:QA-BIZT-1; átmeneti szöveg `35a9ddd`) | M1#2, M1#4, M2#1, M2#2, M2#3, M2#4, M2#5, M2#6 |
| Átfedő kánoni blokkok összevonva a kánoni körben (egy cellába, mindkét döntés szövegével) | M0#33, M0#36, M1#64, M2#42, M7#91, M7#107, Z#55, Z#56, Z#57, Z#61, Z#63 |
| A saját commitban pontosítva (GYV-1 M2.4:37; ADV-2 M3.4 hozzáférési mondat; ERT-1 M3.4 completion-mondatok) | M2#46, M3#2, M3#25, M3#26, M3#27 |

Mindegyiknél a döntés szövegrésze a fájlban van; a pontos hely a 13. szakasz Implementáció oszlopában.

### 4.2 Szándékosan nem alkalmazott blokkok

| Döntés | Blokkok | Ok | Feloldja |
|---|---|---|---|
| LMS-2 (M3.4-rész) | M3#55–#62, #64, #65, #67 | az M3.4-EGY-03 Drag & Drop-mellékút megszüntetése a `tools/test_media_manifest.py` név szerinti párját is módosítaná; `tools/` ebben a futásban nem változik | X-10: projektgazda / build-felelős, egy change setben (vétó: hozzáférhetőségi gazda) |
| ERT-28 | M5#22–#24 | a döntés sorrendje („feladat–kvuca–módszer–cél”) eltér a tanított lánctól (feladat → cél → kvuca → módszer, M5.2 SLIDE 7); a ✅-opció átírása így a döntés szerint „explicit új itemdöntés” | az M5 szerzője + értékelési felelős |
| ERT-38 (manifest) | Z#58 | az LMS-Z-08 „Teljesítve”-mércéje a célzott QA szerint nyitott (Z:QA-NYELV-1 = Z:QA-ERT-1, Z:QA-ERT-2) | értékelési felelős (+ DPO a passz jelzéséhez) |

Ezeken kívül terv-blokk nélkül, szándékosan: GYV-9, GYV-14, TERM-1, ERT-7, ERT-19, ERT-30, ERT-32, ERT-36, ERT-42, ERT-43, PRG-4, PRG-17, LMS-7, TECH-2 (az okuk és a feloldó szerep a 13. szakaszban), valamint a TECH-1, amelynél a döntés szerint nincs szövegváltozás.

## 5. IMPLEMENTED (41)

| Döntés | A/F | Implementáció | Tesztelés |
|---|---|---|---|
| GYV-6 | A | M1.A, M1.B („megállhat vagy passzolhat”), M1.F, M7.A:56, M7.F:89, Z.A:56 + eb4fa6d, f6e9c6e, c5bc2c4 | QA-riport M1, M3, M4, M5; QA-riport M7, Z |
| GYV-12 | A | M1.3:913 (ADV §11 mondat), M2.4:665 (a biztonsági doboz a Moodle-mezőnél) + eb4fa6d/7a69b9d, 147f3c3 | QA-riport M1, M2; kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| GYV-13 | A | a formula 37 fájlban 77-szer (pl. M2.4, M4.3:360, M6.2:783) + a modul-commitok | QA-riport M0–M6; QA-riport M7, Z |
| GYV-20 | F | M2.A:225 („nincs nyilvános kiállás: fejben vagy a saját papírjukon”) + 147f3c3 | QA-riport M2 |
| GYV-22 | A | M1.1:926 („nem elvárás, és nem feltétele a jó madrihságnak … általános vagy kitalált példát”) + eb4fa6d | QA-riport M1 |
| ADV-9 | A | M4.4, M4.B, M5.4, M5 KAPU:283, M6.1, M6 KAPU, M6.B (korosztály/létszám, nincs diagnózis) + dd64825, aadf41b, fbebec0 | QA-riport M4, M5, M6; kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| ADV-13 | A | a „2–3 konkrét szabály” KPI az M2-ben 0 találat (kikerült; 12. blokk) + 147f3c3 | QA-riport M2 |
| TERM-3 | A | „transzparens” az M2-ben 0 találat + 147f3c3 | QA-riport M2 |
| TERM-5 | A | M3.4:692, :699, :787, :796; MAN:66 („M3 – Helyzetleírás”) + ce04b9c | M3 QA-riport + verifier |
| TERM-6 | F | M3.A:413 („kvuca – év eleje”), :433 („Leviatán – év eleji kvuca”) + ce04b9c, e0d69d4 | M3 QA (QA-NYELV-5 javítva) |
| ERT-2 | A | MAN:16 (általános szabály), MAN:39 (M0_L1); M0.1:13 + 5484b02, bdb94ab | M0, M6, M7, Z QA-riport; kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| ERT-4 | F | M1 KAPU:28, :132, :314; M2 KAPU:56; M2 HUB:179 + eb4fa6d, 147f3c3 | M1 QA (QA-ERT-7), M2 QA |
| ERT-6 | A | M5 HUB:180; M5 KAPU:24; M6 KAPU:74, :440; MAN:92 + aadf41b, fbebec0, bdb94ab | M5 és M6 QA-riport; kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| ERT-11 | A | M0 HUB:222–230, :255, :261 + 5484b02, a2445ff | M0 QA (QA-ERT-3, HUB:181) |
| ERT-16 | F | M1.4:490, :592 + eb4fa6d, 7a69b9d | M1 QA (QA-ERT-6) |
| ERT-17 | A | M1 KAPU:79 („A kapcsolat megtartása ennek a pedagógiai oka, nem külön pontozott szempont.”) + eb4fa6d | M1 QA-riport (eb4fa6d); fő session visszaolvasás |
| ERT-20 | F | M2 hub:245 („a stáb a szabad szöveges válaszokat programanalitikai célból nem olvassa újra, és ehhez nincs külön mutató”) + 147f3c3 | M2 QA-riport (147f3c3); fő session visszaolvasás |
| ERT-24 | F | M4 HUB:128 („összesített téma-visszajelzés”) + dd64825, 64a60d1 | M4 QA (QA-NYELV-4) |
| ERT-25 | F | M4.3:542 (K3 szár: „új vita nyitása nélkül ellenőrizni, hogy a kvuca érti-e, mi volt a mai peula célja”); ✅ változatlan + dd64825 | M4 QA-riport (dd64825); fő session visszaolvasás |
| ERT-27 | A | M5 KAPU:295–300 (az R4 nem szűkül a felidézésre/elosztott gyakorlásra; a terv 20–21. blokkja) + aadf41b | M5 QA-riport (aadf41b); fő session visszaolvasás |
| ERT-29 | A | M5.4:9, :247 + aadf41b, 9764987 | M5 QA (QA-IMPL-1); kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| ERT-31 | A | M6 KAPU:412 + fbebec0, 511d9e0 | M6 QA (QA-ERT-1) |
| ERT-33 | A | M6 HUB:218; M6 KAPU:390; PT:288 + fbebec0, bdb94ab | M6 QA (QA-NYELV-9); kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| ERT-35 | A | M6.4:961; M6 KAPU:165 + fbebec0, 511d9e0 | M6 QA (QA-NYELV-1) |
| ERT-37 | A | M6.B:261, :348 („önállóan véglegesít”) + fbebec0 | M6 QA-riport |
| ERT-39 | A | Z HUB:197; Z.4:283; Z.4:402 (Z:QA-ERT-3 javítva); MAN:165 a Z.A-t nem sorolja + c5bc2c4, a0c0c83 | QA-riport Z (nincs nyitott ERT-39 tétel); kánoni QA: riport (bdb94ab), javítás 35a9ddd (CANON:QA-IMPL-5: a MAN LMS-Z-04 és a Z.A-hoz kötött nyitás jelenléti feltétel nélkül) |
| ERT-41 | A | M7 KAPU:260 (QA-fix: „a madrih”), :263, :426, :427; MAN:103 (kánoni 39. blokk) + f6e9c6e, 0b76212, bdb94ab | QA-riport M7 (K8 javítva); kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| ERT-44 | F | M7 KAPU:297 („Mit mér”), :302 (QA-fix: „egyes elemei”), :303 + f6e9c6e, 0b76212 | QA-riport M7 (M7:QA-ERT-4 javítva) |
| ERT-45 | A | M7 KAPU:211, :350 („a 45 perc csak példa”); M7.2:709 + f6e9c6e | M7 QA (nincs nyitott tétel) |
| ERT-46 | F | M7.1:8, :324, :333 (pontozatlan, ERT-46), :349 (QA-fix: IMPL-1) + f6e9c6e, 0b76212 | QA-riport M7 (M7:QA-IMPL-1 javítva) |
| ERT-47 | A | M7 KAPU:385 ((a)/(b) alpont) + f6e9c6e | QA-riport M7 |
| ERT-48 | A | M7.2:9, :88, :131; MAN:96 (kánoni 58. blokk) + f6e9c6e, bdb94ab | QA-riport M7; kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| ERT-49 | A | M7 KAPU:386; az „eltérő létszám” az M7-ben sehol nem maradt + f6e9c6e | QA-riport M7 |
| ERT-50 | A | M7.4:74, :698, :776, :817; M7 KAPU:351 + f6e9c6e | QA-riport M7 |
| PRG-6 | F | M7 KAPU:27; M7 HUB:383; M7.4:703 („indokolt esetben”); Z.4:339; MAN:222 (M0, kánoni), :252 (Z, kánoni), :102 + f6e9c6e, 0b76212, c5bc2c4, a0c0c83, bdb94ab | QA-riport M7 (K1 javítva); kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| PRG-7 | A | M5 HUB:208; M6 HUB:242, :247 + aadf41b, fbebec0 | M5/M6 QA-riport |
| PRG-8 | A | MAN:120, :121 („Peulák” leíróelem, F-peula-szakasz, csak az új verzió) + bdb94ab | kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| PRG-10 | A | M4.B:278 (SBI opcionális, Megfigyelés → Hatás → Következő lépés), M4 hub (kötelező szerkezet); M5 KAPU:283 (kitalált kvucaprofil egyenértékű); ADV §3 M5/M6 (kánon) + dd64825, aadf41b, bdb94ab | M4/M5 QA-riport; kánoni QA: riport (bdb94ab), javítás 35a9ddd |
| PRG-13 | A | M5.A:243; M6.A:381, :549 + aadf41b, fbebec0 | M5/M6 QA-riport |
| LMS-6 | A | M7.4:14, :543 (pontozatlan saját jegyzetes lista, nem completion-elem) + f6e9c6e | M7 verdiktek (NYELV-11 ELVETVE) |
| TECH-1 | A | nincs szövegváltozás: a „mini-jelenet” forma marad (M4.1, M5.3); a kivétel dokumentálva: HUM 14. szakasz TECH-1 sora és bevezetője (:610, :747); a ledger ALREADY_FIXED sorai | content_integrity (gyermekvédelmi tiltóőr) 0 hiba |

## 6. QA-RA VÁR (17)

Az átvezetés a fájlokban van; a nyitott tétel a célzott QA szerepköri döntése vagy kalibrációja. Addig a fájlban álló óvatos szöveg él.

| Döntés | A/F | Nyitott döntés (mit, kitől) |
|---|---|---|
| GYV-1 | F | M2:QA-BIZT-5, kiterjed-e a KAPU:24 24 órás határidejére (projektgazda, Memuna-QA) |
| GYV-8 | F | Z:QA-BIZT-2, 112-utalás (Memuna + programvezető) |
| GYV-17 | A | M6:QA-BIZT-5, a „kiskorúakra is térjen ki” tartalma (Memuna + tartalomfelelős) |
| GYV-19 | A | M2:QA-BIZT-3 és M4:QA-BIZT-3, címzett: „képzőnek és Memunának” vagy a GK §4.1 szerint csak Memuna (Memuna) |
| GYV-21 | A | M2:QA-BIZT-7, „felismerhető részlettel sem” (Memuna + DPO) |
| GYV-23 | F | M0:QA-BIZT-3 (DPO + LMS-gazda), M0:QA-NYELV-3 (programvezető + Memuna) |
| ADV-7 | A | M4:QA-BIZT-5 (DPO + Memuna), Z:QA-BIZT-3 (DPO/jogi) |
| ADV-11 | F | M0:QA-BIZT-4, kiterjed-e a nem F-peulás tartalék eszközre (projektgazda; QA: LMS-gazda + DPO); a kivételhez LMS + DPO teszt (opcionális) |
| ERT-9 | A | –; kánoni QA: CANON:QA-ERT-2 emberi döntés — az LMS-M3-05 SUBMITTED completionje és a kapukvíz-ablak (build-spec gazda; QA: értékelési felelős); a többi ASSIGN-M sor és a profil javítva (35a9ddd) |
| ERT-14 | A | M1:QA-ERT-3, a rubrika jóváhagyása az értékelési felelőstől (bizonyíték-kapu) |
| ERT-21 | F | M3:QA-BIZT-2 (Memuna + értékelési felelős) |
| ERT-22 | A | az értékelési felelős és a Memuna ítélete a befogadó sorról |
| ERT-26 | A | M5:QA-ERT-1 kalibráció (értékelési felelős; QA: módszertani lektor) |
| ERT-38 | A | értékelési felelős (+ DPO a passz jelzéséhez): szakaszonkénti vagy egész beadásra szóló „Teljesítve”-mérce |
| ERT-40 | F | értékelési felelős: a kézi megerősítés menete eltérő Highest grade esetén; a minden-vagy-semmi kérdéstípus validálása: LMS-gazda (X-4) |
| PRG-12 | F | M3 modulgazda + Memuna: M3:QA-NYELV-13 (a 4.3.3 esete négy csoportnál) |
| PRG-16 | F | a döntés szerinti rövid szerzői szándék-QA modulonként (modulgazdák; M2 bizalmas olvasatnál Memuna; M6: hub tartalomfelelőse; Z: modulgazda vagy projektgazda); az M7.B „átjárás” (M7:NYELV-G3-12) nyitott |

## 7. KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ (67)

A döntés külső feltételt nevez meg; az `F` döntéseknél addig az óvatos alapértelmezés áll a fájlokban (a 13. szakasz Implementáció oszlopa).

| Döntés | A/F | Fennmaradó külső függőség |
|---|---|---|
| GYV-2 | F | az M3/M4-kör Memuna- és completion-QA-ja (a döntés nevezi meg; M3:IMPL-G2-5, PED-G2-1, M4:BIZT-G2-10 nincs átvezetve); M2:QA-BIZT-4 egyenértékű demonstráció (Memuna + programvezető, értékelési felelős) |
| GYV-3 | F | helyenkénti Memuna-verdikt a 7 helyre (a döntés szerint addig él az alapértelmezés) |
| GYV-4 | F | a számok és órák kiadáskori Memuna-ellenőrzése; a 116 000 pontosítása (GYV-14) |
| GYV-5 | F | végleges létszámnorma és a megállítási protokoll tartalma (Memuna + programvezető; M0:QA-BIZT-2, M2:QA-BIZT-2, M6:QA-BIZT-4); M2.B/M2.F/M3.F besorolás |
| GYV-7 | F | az M0 csoportchat-küszöbét a Memuna külön ellenőrzi (a döntés nevezi meg, az M0-ban nincs átvezetve); M6:QA-BIZT-1/2, M7:QA-BIZT-6 (Memuna) |
| GYV-9 | F | a rubrikahorgony és a Q9/(C) formális jóváhagyása (Memuna + értékelési felelős; rubrikaszint: projektgazda) |
| GYV-10 | F | igazolt adatkezelési és kríziskezelési út (Memuna + DPO/jogi + programvezető); CANON:QA-BIZT-3 (b) emberi döntés — kell-e és milyen szöveggel a képző által közvetített AI-út a tanulói tájékoztatóban (ADV §11) — programvezető + Moodle-adminisztrátor; vétó/QA: DPO / jogi felelős |
| GYV-11 | F | dokumentált Memuna-eljárás és DPO-jóváhagyott törlési/megőrzési rend; M1:QA-BIZT-5, Z:QA-BIZT-1; CANON:QA-BIZT-4 emberi döntés — „kikerül a Moodle-ből” vs GYV-11 törlési rend (Memuna + DPO) |
| GYV-14 | F | kiadás előtti egyeztetés a Kék Vonal és az NMHH leírásával; formális Memuna-újranyitás |
| GYV-15 | F | a külső jelzés címzettjei (jogász/JOG-1 + Memuna); M3:QA-BIZT-1 |
| GYV-16 | F | Memuna szakmai döntése (a döntés nevezi meg; M3.A-nál a modulgazdával) |
| GYV-18 | F | a 12. item új szára és kulcsa (értékelési felelős + Memuna, kulcs: projektgazda; M6:QA-BIZT-3); az M6.2-NAR-05 VO-render (VO-gazda) |
| ADV-1 | F | staging role-matrix (LMS-gazda) + DPO; BIZT-5 csoportszűkítés; CANON:QA-BIZT-1 emberi döntés — kiterjed-e a csoportszűkítés a H5P-C, QUIZ, GATE-CP nézetre (projektgazda; DPO-vétó); a staging role-matrix utáni RBAC-igazítás |
| ADV-2 | F | az F-peula szereposztás és a vészhozzáférés dokumentálása, valós csoport-hozzáférési teszt (DPO + LMS-gazda, programvezető) |
| ADV-3 | F | RT-P0-24 (LMS-gazda), DPO adatkör-aláírás (M4:BIZT-G1-2), az M4.1 ILO 2 szövege (az IV-kérdés opcionális lett; modulgazda / projektgazda, X-5), VO_PACK; CANON:QA-IMPL-7 (b) emberi döntés (X-11) — a Z.3 5. dia besorolása (projektgazda) |
| ADV-4 | F | a tárolásmentes technika célverziós visszaolvasása (H5P-verzió, próbálkozás-riport, xAPI, mentett állapot, szerepkörök; RA 24) – LMS-gazda + DPO, M3-nál Memuna |
| ADV-5 | F | GDPR 9. cikk szerinti minősítés (jogi/DPO); M7 R1; M2:QA-ERT-2 |
| ADV-6 | F | cél, hozzáférési kör, DPO által elfogadott megőrzés, tájékoztató (DPO/jogi); M0:QA-ERT-1 (build-spec gazda + LMS-gazda) |
| ADV-8 | F | a mentori adatkör/megőrzési sor kijelölése (DPO, ADV-E2) |
| ADV-10 | F | külső eszköz csak a szolgáltató, adatkör, megőrzés és harmadik fél ismerete után (DPO/jogi); szervezeti fiók (programvezető); M7 (c) megőrzési sor |
| ADV-12 | F | provider-, proxy-, hibalog-, backup- és admincsatorna-felmérés, megőrzés (DPO/jogi); CANON:QA-BIZT-5 emberi döntés — az AI-végpont metaadatainak jogalapja és megőrzése az ADV §3-ban (DPO) |
| ADV-14 | F | hozzájárulási folyamat, törlési út, feltöltés előtti ellenőrzés, kiskorú jogalapja (DPO + jogász) |
| ADV-15 | A | az anonim mód és a back-end hozzáférés tényleges működésének vizsgálata (runtime, LMS-gazda) |
| JOG-1 | F | a Gyvt. 17. § címzettjei és határidői (jogász); Memuna; nyilvántartás helye (projektgazda) |
| TERM-1 | F | terminológiagazda (ken-vezető/mozgalmi felelős) megerősítése; átnevezés (TECH2) a felhasználótól |
| TERM-2 | A | NAR-02 VO-render (VO_PACK, VO-gazda) |
| TERM-4 | F | a fájlnév-átnevezést a felhasználó futtatja (git mv + linkek); a végleges szerzői címet az M3 modulgazdája adja |
| TERM-7 | F | az M5-részben választani kell a formatív demonstráció és a célmegfogalmazás szűkítése között (M5 modulgazda + értékelési felelős) |
| TERM-8 | F | a top 3-ban hiányzó someres értékhez előre rögzített támogatás új tartalom, PRG-4 csomag (/course-develop) |
| ERT-1 | A | RA 9 negatív teszt, és soronként igazolni, hogy a CP-nek van összefoglaló diája (LMS-gazda / build-spec gazda) |
| ERT-3 | F | a „kiürítés” staging-tesztje (RA 16); nyitott Z:QA-IMPL-3 a „kiürítés” jelentéséről (build-spec gazda) |
| ERT-5 | A | a Review options célverziós visszaolvasása (LMS-gazda) |
| ERT-7 | A | itemek újraírása PRG-4 csomagban (szerző + értékelési felelős + Memuna) |
| ERT-8 | A | az értékelés helyének és hozzáférésének dokumentálása (build-spec gazda + DPO; M4:ERT-G2-4 EXTERNAL) |
| ERT-10 | F | küszöbhatás-vizsgálat (értékelési felelős) és Memuna szakmai állásfoglalás |
| ERT-12 | A | a NAR-05 VO fix pack; DPO-vétó |
| ERT-13 | A | a NAR-03 hang (VO-render) |
| ERT-15 | F | a két horgony példáinak egységesítése és kalibrációja (értékelési felelős + módszertani lektor) |
| ERT-18 | F | runtime-próba a cél-Moodle-ön (LMS-gazda); a tárolásról a DPO dönt |
| ERT-19 | F | a módosított követelményt a modulgazda és az értékelési felelős írja alá |
| ERT-23 | F | itemenkénti validálás (M3 modulgazda + értékelési felelős) |
| ERT-28 | F | új item-döntés (M5 szerzője + értékelési felelős) |
| ERT-30 | F | a C mondat jóváhagyása (szakmai szerző / értékelési felelős + modulgazda) |
| ERT-32 | F | kalibráció (értékelési felelős + Memuna); a rubrikaszint a projektgazdáé |
| ERT-34 | F | új Kivsza-item és validálása (értékelési felelős, PRG-4) |
| ERT-36 | F | GYV-18 döntés és M6:QA-BIZT-3 (értékelési felelős + Memuna); PRG-4 |
| ERT-42 | F | értékelési felelős + DPO formális döntése a rubrikáról és a kapuhatásról |
| ERT-43 | F | projektgazdai jóváhagyás + előzetes tanulói tájékoztató (értékelési felelős) |
| PRG-1 | A | tételes vágási terv modulonként (modulgazdák; M3.B-nél a Memuna bevonásával); az M5.1 részidőinek újrabecslése (modulgazda); vétó: programvezető |
| PRG-2 | A | az M5-rész (M5:PED-G1-10, TERM-7) EXTERNAL |
| PRG-3 | A | az M1-poszter rész (M1:IMPL-G3-5): modulgazda + médiafelelős; PRG-4-jelölés opciója: modulgazda |
| PRG-4 | F | `/course-develop` csomag (a felhasználó indítja, X-8); a csomagterv a projektgazdáé; QA: Memuna, értékelési felelős |
| PRG-5 | F | 1–5 fős változatok (PRG-4, modulgazda); kapacitás és pótlási felelős (programvezető) |
| PRG-9 | F | b) M2.1 „CP-ben integrált” forma: build-/LMS-gazda + M2 modulgazda (M2:IMPL-G1-3 EXTERNAL; az M2.1:8 ma „különálló, nem követett elem”) |
| PRG-11 | A | eset- és kártyadarabszám, valamint egyenlőrészvétel-sor az M3.B, M4, M7 specekben (modulgazdák; M3.B: + Memuna) |
| PRG-14 | F | a tényleges médiaeredet igazolása (szerző / médiafelelős; M4:BIZT-G1-7 EXTERNAL); a nyomtatható változat legyártása |
| PRG-15 | F | b) az M5.1 SLIDE 4 1./4. kulcsa: szakmai lektor / M5-szerző (M5:PED-G1-3) |
| PRG-17 | F | pilot-visszajelzés (X-9); projektgazda / modulgazda |
| LMS-1 | F | cél-Moodle beállítás- és a11y-ellenőrzés (LMS-gazda + DPO + hozzáférhetőségi gazda); M2- és M5-rész EXTERNAL |
| LMS-2 | A | `tools/test_media_manifest.py` cseréje (projektgazda / fő session); a11y pre-flight |
| LMS-3 | F | valós H5P + az LMS-M5-07 teszt (LMS-gazda + lektor); jóváhagyott önellenőrző tartalom (PRG-4, modulgazda) |
| LMS-4 | F | a Grade type / Maximum grade / rubrikaminimum értéke (LMS-gazda + értékelési felelős; RT-P0-01) |
| LMS-5 | F | a NAR-05 hangszöveg VO_PACK (médiafelelős / VO-gazda) |
| LMS-7 | F | a hozzáférhetőségi gazda ellenőrzi az alt + kísérőszöveg együttes funkcióját |
| LMS-8 | F | krízis-, adatkezelési, jogosultsági és no-AI parity review a közvetlen úthoz (programvezető + Moodle-adminisztrátor; DPO-vétó; RT-5); CANON:QA-BIZT-3b emberi döntés — a közvetített AI-út a tanulói tájékoztatóban (programvezető + Moodle-adminisztrátor; DPO) |
| VO-1 | F | egyetlen VO fix pack, újrarender és meghallgatás (médiafelelős / VO-gazda; felhasználói kérés, X-6) |
| TECH-2 | F | a felhasználó saját terminálban futtatja a `git mv`-t (X-7); projektgazda (`tools/` két sora, baseline-sor) |

## 8. Tudatos eltérések és részleges átvezetések

- **LMS-2, ERT-28, ERT-38 (manifest):** 4.2.
- **ERT-26 kánoni része:** az M5 terv a PT:183 és a MAN:83, :86 igazítását „a kánoni körre” hagyta, de kánoni blokkot nem írt rá, ezért a kánoni kör kihagyta. A 125/125 visszaolvasás találta meg; átvezetve `33aec89` (célzott értékelési ellenőrzés: nincs finding). Az ERT-26 az M5:QA-ERT-1 kalibrációja miatt QA-ra vár.
- **ADV-1:** a csoportszűkítés a beadásokra él; a H5P-C, QUIZ és GATE-CP mentori nézetére való kiterjedése emberi döntés (CANON:QA-BIZT-1; projektgazda, vétó/QA: DPO / jogi felelős). A „csak a mentorod látja” ígéret a staging role-matrixig a technikai adminisztrátor hozzáférését is kimondja.
- **GYV-4 (M6):** az M6.2:783, M6.3:749 és a 6D/ZÁRÓ veszélydoboza a terv szerint a rövid Memuna-utalásnál maradt (GK §4.1 megengedi; a 6D/ZÁRÓ a 2026-10-05-i döntés szerint Memuna-QA alatt).
- **VO-1 és a VO-érintett nyelvi tételek:** a kimondott szöveg csak egyetlen VO fix packkel javítható (X-6); a kurzusoldali `@source`-szövegek nem változtak ott, ahol a narráció eltérne.
- **TECH-2:** az M6.1/M6.2 átnevezését a felhasználó futtatja (X-7). **PRG-4:** `/course-develop` csomag (X-8). **PRG-17:** pilot-visszajelzéssel (X-9).
- **Z:QA-NYELV-11** („18+” → „18 év feletti”): elvetve; a korpusz alakja marad.
- **Nyitott megfigyelés (nem validált finding), ERT-5, M7:** az M7 kapukvíz itemjeinek „Visszajelzés” szövegei közlik a helyes választ (pl. KAPU:72, :83). A KAPU:51 a „helyes választ és a teljes, opciónkénti visszajelzést csak a javító próbálkozás lezárása után” szabállyal ezt fedi, de az M3 kapujával ellentétben nem nevezi meg külön az általános visszajelzést (Moodle Review options: General feedback). Nem javítottuk: a következő célzott QA-ban kell validálni, addig a célverziós Review options-visszaolvasás (X-4) során a build-spec gazda ellenőrzi.

## 9. Nyitott bizonyíték-kapuk (16) — nem teljesültek, nem jelöltük teljesítettnek

| ID | Mit kell bizonyítani | Szerep | Ledger |
|---|---|---|---|
| GYV-24 | Egyazon végleges SHA-ra szóló, datált „átnéztem” G1; SAFE-7 és valamennyi 1:1-kulcs explicit verdikt; akut út/segélyvonal friss ellenőrzése; tracker #1 lezárása linkkel | Memuna | X-1 |
| ADV-E1 | Activitynkénti DPO G2 QA: pontos adatmezők, hozzáférési szerepek (mentor/editor/manager/admin), megőrzés, export, xAPI/LRS, saved-state, backup, esetenkénti tartalékút. M0/M1-re prioritás | DPO/jogi felelős | X-2 |
| ADV-E2 | Teljes activity-szintű adatleltár, külső Google/papír/mentori jegyzet folyamatokkal, adatfeldolgozói és törlési renddel, „külön review” helyek rögzítése | DPO/jogi és programvezető | X-2 |
| ADV-E3 | HUM-PRIV-04 AI-kapcsolat tényellenőrzése: API, közvetítő, provider, naplózás, retention, hozzáférés, továbbítás, no-AI egyenértékű út; formális QA | DPO/jogi | X-2 |
| SIG-1 | M0 hét belépőkvíz-itemjének független értékelési QA-ja; az 1–2. itemnél gyermekvédelmi kontroll, dátummal és SHA-val | Értékelési felelős, 1–2.: Memuna | X-3 |
| SIG-2 | M3 ≥10/12 és kritikus Q2/Q4/Q7/Q9, M7 Q13 szakértői item- és küszöbmegállapítás (korábbi Q-PED-6 Angoff-elv átvezetése); 1–2 közös referenciaminta; kétszemes blokkoló döntési rend | Szakmai lektor, assessment, Memuna a gyermekvédelmi résznél | X-3 |
| SIG-3 | M3.4 kritikus követelmény megnevezése kulcsfelfedés nélkül; szöveg és valós tanulói review-options QA | Értékelési felelős + Memuna | X-3 |
| SIG-4 | M4 kvíz/rubrika/sablon és M5 kapu független lektori QA-ja az összes függő döntés alkalmazása után | Kijelölt szakmai lektor; M5 assessment QA | X-3 |
| SIG-5 | M5 AI-generált media assetenkénti emberi szakmai és eredetjelölési ellenőrzés; release-record referencia | Szakmai lektor | X-3 |
| SIG-6 | M6 média jogosultságok: J3, H-11, AI Act minősítés, J2, V1, V3/E-8, R2/R3 és minden releváns RIGHTS-EVIDENCE kontroll; az érintett asset addig fallbacken | Jogi jogosult, Memuna, DPO, szerző | X-3 |
| RT-1 | Valódi technikai/program/mentor/Memuna kontakt, ügyfél- és tanulói nézetben helyesen megjelenik; nyitvatartás, szerepcímke, elérhetőség | LMS-gazda + programvezető | X-4 |
| RT-2 | M0/M1 completion/unlock/attempt/GATE_CP, védett és hibás negatív esetek; N-M1-04 saját jegyzetes/no-input alapút; H5P saved-state, xAPI/LRS és jogosultsági visszaolvasás a célverzión | Moodle/LMS-gazda, a11y szerep, DPO a saját részén | X-4 |
| RT-3 | M4 kész kapu/completion/a11y és notification teszt; tényleges M4_ASSIGN dátum és az elkülönített learner-scope | LMS-gazda + programvezető + a11y | X-4 |
| RT-4 | M6.4 Branching Scenario A → B → opcionális C → D → 6D → ZÁRÓ valós bejárása; kizárólag végponti completion, passz és érintés/húzásmentes működés | LMS-gazda + a11y | X-4 |
| RT-5 | M7 AI „store=false” és esetleges proxy/provider naplózások auditja, API és ZDR jogcím; no-AI út feladat-, grade- és completion-paritása | LMS-gazda + DPO | X-4 |
| RT-6 | M7.2/M7.3 minden párosítás billentyűzettel és egyérintéses kattintás/koppintás útján egyenértékű, azonos visszajelzéssel; mobil portrait teszt | LMS-gazda + független hozzáférhetőségi QA | X-4 |

## 10. A célzott QA emberi döntései (40 tétel; ledger: X-11, a VO-tételek X-6, az LMS-2-tétel X-10)

A riport-azonosító a QA-riportoké; a ledger kulcsa `<modul>:QA14-<…>` (a kánoni körnél `KANON:`). Javasolt szöveg nélkül: mit kell eldönteni, kitől. Addig a fájlban álló szöveg változatlan.

| Riport-ID | Súly | Döntési igény |
|---|---|---|
| M0:QA-BIZT-2 | P1 | GYV-5 — a „kötelező megállítási protokoll” tartalma, a 2.4 miniprotokoll ennek számít-e, az alacsony kockázat dokumentálása az M0.A-ban — Memuna + programvezető |
| M0:QA-BIZT-3 | P2 | GYV-23 — ki láthatja alapból a belépőkvíz egyéni válaszait (Responses report), rögzítés az ADV §3-ban, staging-igazolás — DPO + LMS-gazda |
| M0:QA-BIZT-4 | P2 | ADV-11 — kiterjed-e a közös eszköz-protokoll a nem F-peulás tartalék eszközre (M0.A) — projektgazda; vétó/QA: LMS-gazda + DPO |
| M0:QA-NYELV-3 | P2 | GYV-23 — mit jelent „a két item nyilvános visszajelzése” — programvezető + Memuna; adatkör: DPO |
| M0:QA-ERT-1 | P2 | ADV-6 — a fórum megnyitásának visszamenőleges hatása az M0 completionre és az LMS-M1-01 feloldására; a „zárt” állapot Moodle-mechanizmusa — build-spec gazda + LMS-gazda |
| M1:QA-BIZT-1 | P1 | VO fix pack (X-6) — az M1.3-NAR-05 `@source` mondata ütközik az ERT-12-vel; csak a VO-úton javítható — médiafelelős / VO-gazda |
| M1:QA-BIZT-5 | P2 | GYV-11 — a Memuna-eljárás, a korlátozás/helyesbítés, a törlés/megőrzés és a feltárásmentes pótlási út mechanikája — Memuna + DPO; a kapueredményre az értékelési felelős |
| M2:QA-BIZT-2 | P1 | GYV-5 — a megállítási protokoll tartalma, az M2.A kockázati besorolása, a :281–283 viszonya — Memuna + programvezető |
| M2:QA-BIZT-3 | P1 | GYV-19 — „képzőnek és Memunának” vs a GK §4.1 kizárólagos Memuna-címzettje (M2.A:362; az M4:QA14-BIZT-3-mal együtt) — Memuna |
| M2:QA-BIZT-4 | P1 | GYV-2 — mi egyenértékű tudásdemonstráció az M2.4 passz-útján — Memuna + programvezető; értékelési felelős |
| M2:QA-BIZT-5 | P2 | GYV-1 — kiterjed-e a KAPU:24 24 órás megerősítési határidejére — projektgazda, Memuna-QA |
| M2:QA-BIZT-7 | P2 | GYV-21 — „és felismerhető részlettel sem” a csoportos titoktartási normában (M2.A:177, :410) — Memuna + DPO |
| M2:QA-ERT-2 | P2 | ADV-5 — változzon-e a HUB:34 kimeneti célja a fiktív R3-út miatt — projektgazda + értékelési felelős (someres QA: helyi ideológiai felelős) |
| M3:QA-BIZT-1 | P2 | GYV-15 — az M3.3 S3-SAFE doboz és a KAPU ITEM 9 a GYV-15 alá tartozik-e — Memuna; jogi kérdésben a jogi szakértő |
| M3:QA-BIZT-2 | P1 | ERT-21 — a „titoktartási ígéret” lefedi-e a hanih titoktartás-kérését; határhelyzetnél mi az R3 Alapszintje (öt hely együtt) — Memuna + értékelési felelős; rubrikaszintnél a projektgazda |
| M3:QA-IMPL-1 | P2 | LMS-2 M3.4-rész — az M3.4-EGY-03 törlése és a ♿ doboz igazítása a `tools/test_media_manifest.py` párjának cseréjével egy change setben (a tools/ ebben a futásban nem változhat) — projektgazda / build-felelős; vétó: hozzáférhetőségi gazda |
| M3:QA-NYELV-13 | P2 | PRG-12 — az M3.B 4.3.3 esete négy csoportnál — M3 modulgazda + Memuna |
| M4:QA-BIZT-3 | P2 | GYV-19 — „a képzőnek és a Memunának” az M4.3 képzésen kívüli hanih-helyzetére is vonatkozik-e — Memuna + projektgazda |
| M4:QA-BIZT-4 | P2 | VO fix pack (X-6) — „magadnak” az M4.1-NAR-07 és az M4.3-NAR-03 hangszövegében — médiafelelős / VO-gazda |
| M4:QA-BIZT-5 | P2 | ADV-7 — az M4.A/M4.B fókuszmondat-kártyája személyes önfeltáró cetli-e — DPO / jogi felelős, Memuna-QA-val |
| M5:QA-ERT-1 | P2 | ERT-26 — a „soronként látható módszertani indok” kalibrációja a meglévő R3 szinteken belül — értékelési felelős; QA: módszertani lektor |
| M6:QA-BIZT-1 | P1 | GYV-7 — vonatkozik-e a kétlépcsős küszöb az M6.3:749 és az M6.4 6D/ZÁRÓ dobozára — Memuna |
| M6:QA-BIZT-2 | P1 | GYV-7 — ki adja a „támogató mentorálást” a madrih–hanih viszonyban, kell-e konzultációs út — Memuna |
| M6:QA-BIZT-3 | P1 | GYV-18 — a KAPU 12. item új szára és ✅-ja; a narráció a VO fix packkal — értékelési felelős + Memuna; a kulcs: projektgazda; VO: médiafelelős |
| M6:QA-BIZT-4 | P2 | GYV-5 — a 4.3.2/B négy lépése az M6.A megállítási protokollja-e; az egyszemélyes kivétel alkalmazhatósága — Memuna + programvezető |
| M6:QA-BIZT-5b | P2 | GYV-17 — mit jelent a keretben „a kiskorúakra is térjen ki” — Memuna + a peula tartalomfelelőse |
| M7:QA-ERT-1b | P2 | ERT-40 — a kézi megerősítés menete, ha a Moodle „Highest grade” szerinti próbálkozása eltér a darabszám szerint teljesítőtől — értékelési felelős; QA: programvezető; platform: LMS-gazda |
| M7:QA-BIZT-6 | P2 | GYV-7 — az M7.B:480 AI-tiltó mondatában a „komoly szorongás” a Memunához vagy a mentorhoz (veszélyeztetettség gyanújánál azonnal a Memunához) menjen — Memuna |
| Z:QA-NYELV-1 | P1 | ERT-38 — a „Teljesítve” alsó határa: mindhárom szakaszban kell-e értelmezhető tartalom, vagy elég a beadás egészének értelmezhetősége (Z.4:98, :329, :343, :347, :353, HUB:185, manifest LMS-Z-08 együtt) — értékelési felelős; vétó/QA: programvezető |
| Z:QA-ERT-2 | P2 | ERT-38 — hogyan jelzi a tanuló a passzt, mi a mentor első lépése üres szakasznál — értékelési felelős, a DPO-val |
| Z:QA-BIZT-1 | P1 | GYV-11 — kiterjed-e a megőrzési kivétel a Z.4 Feedback nyers válaszaira, szabad-e visszakeresni a válaszadót, kell-e tájékoztató mondat a :370-be — Memuna + DPO |
| Z:QA-BIZT-2 | P2 | GYV-8 — kerüljön-e a Z.3 terepi mintamondatába „közvetlen veszélyben előbb a biztonság és a 112” — Memuna + programvezető |
| Z:QA-BIZT-3 | P2 | ADV-7 — személyes önfeltáró cetlinek számít-e a Z.A egyszavas szófelhő-cetlije — DPO / jogi felelős |
| Z:QA-IMPL-3 | P2 | ERT-3 — mit jelent a „kiürítés” (az RA 16 tesztje ezután végrehajtható) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| CANON:QA-ERT-2 | P1 | ERT-9 — hogyan kap az LMS-M3-05 SUBMITTED completiont úgy, hogy a kapukvíz (LMS-M3-06) csak a megerősített rubrika után nyíljon (külön GATE-CP vagy M3-kivétel) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| CANON:QA-IMPL-7b | P2 | ADV-3 — a Z.3 5. dia célmondata kötelező vagy opcionális tanuló-lokális lépés — projektgazda (X-11) |
| CANON:QA-BIZT-1 | P1 | ADV-1 — kiterjed-e a (c) csoportszűkítés a H5P-C, a QUIZ és a GATE-CP mentori nézetére; addig átmeneti szöveg (35a9ddd, ADV §3 :104, :109, §11 :232) — projektgazda; vétó/QA: DPO / jogi felelős |
| CANON:QA-BIZT-3b | P2 | GYV-10/LMS-8 — kell-e és milyen szöveggel kerüljön a tanulói tájékoztatóba (ADV §11) a képző által közvetített AI-út — programvezető + Moodle-adminisztrátor; vétó/QA: DPO / jogi felelős |
| CANON:QA-BIZT-4 | P2 | GYV-11 — a „kikerül a Moodle-ből” (HUM-PRIV-01) a GYV-11 szerinti jóváhagyott korlátozást/törlést jelenti-e, az incidensnyilvántartásba mentés után — Memuna + DPO |
| CANON:QA-BIZT-5 | P2 | ADV-12 — az AI-végpont technikai metaadatainak jogalapja és megőrzési ideje az ADV §3 táblában — DPO / jogi felelős; QA: programvezető |

## 11. Külső kapuk (ledger)

| Kulcs | Típus | Tétel | Kell (mit, kitől) | Állapot |
|---|---|---|---|---|
| X-1 | EVIDENCE_GATE | G1: a Memuna írásos „átnéztem” bejegyzése (GYV-24) | Memuna: egyazon végleges SHA-ra szóló, datált „átnéztem” (PT §9.3), SAFE-7 és az 1:1-kulcsok verdiktje, segélyvonalak review-napi ellenőrzése, tracker #1 lezárása | OPEN |
| X-2 | EVIDENCE_GATE | G2: a DPO írásos release-QA-ja (ADV-E1, ADV-E2, ADV-E3) | DPO / jogi felelős: activitynkénti jóváhagyás (adatmezők, szerepek, megőrzés, export, xAPI/LRS, saved-state, backup), teljes adatleltár, HUM-PRIV-04 AI-kapcsolat QA-ja; tracker #2 | OPEN |
| X-3 | SIGNOFF | Szerepköri jóváhagyások (SIG-1…SIG-6) | értékelési felelős, szakmai lektor, Memuna, jogi jogosult, DPO, szerző: a döntési csomag SIG-bejegyzései szerint | OPEN |
| X-4 | RUNTIME | Célkörnyezeti runtime-bizonyíték (RT-1…RT-6) | LMS-gazda / build-felelős, hozzáférhetőségi gazda, DPO a saját részén: RA 1–26. pont, RT-P0-xx és RT-A11Y sorok | OPEN |
| X-5 | HUMAN_DECISION | Szerepköri bemenetek és vétó/QA az `F` döntésekhez | a döntésben megnevezett szerep (Memuna, DPO, jogász, értékelési felelős, modulgazda, programvezető, LMS-gazda); tételesen: `2026-10-12 HUM 14 átvezetés – 125-125 lefedettségi jelentés, AP-2026-10-12-01.md` „Külső bizonyítéktól függő” szakasza és a Findingok BLOCKED_HUMAN sorai | OPEN |
| X-6 | HUMAN_DECISION | VO-1: egyetlen VO fix pack | médiafelelős / VO-gazda: a kimondott szöveget módosító blokkok újrarenderelése, a többi kiejtési azonosságának igazolása; kurzusoldali alkalmazás fix packként | OPEN |
| X-7 | HUMAN_DECISION | TECH-2: az M6.1/M6.2 átnevezése | a felhasználó futtatja az átnevezési commitot a saját termináljában; utána a hivatkozások, a két `tools/` útvonalkulcs, a baseline-sor, a pin és a média egy change setben | OPEN |
| X-8 | HUMAN_DECISION | PRG-4: célzott `/course-develop` csomag | a felhasználó indítja; a csomagtervet a projektgazda hagyja jóvá; új biztonsági vagy értékelési item csak Memuna- / értékelési jóváhagyással | OPEN |
| X-9 | HUMAN_DECISION | PRG-17: az M0.1 SLIDE 5 kérdése | a pilot-visszajelzéssel együtt dönt a projektgazda / modulgazda (CC-04, HUM 13. és 14. szakasz) | OPEN |
| X-10 | HUMAN_DECISION | LMS-2 M3.4-rész: az M3.4-EGY-03 Drag & Drop-mellékút megszüntetése | projektgazda / build-felelős: a `tools/test_media_manifest.py` `M3.4-EGY-03` párjának cseréje (`M3.4-EGY-04`) egy change setben a terv 55–62., 64–65. és 67. blokkjával; vétó: hozzáférhetőségi gazda | OPEN |
| X-11 | HUMAN_DECISION | A célzott QA emberi döntései (a QA14-kulcsú BLOCKED_HUMAN sorok) | a sorban megnevezett szerep: Memuna, DPO / jogi felelős, értékelési felelős, programvezető, build-spec gazda, modulgazda | OPEN |

## 12. Vétólista

Answer key, küszöb, ponthatár, időtartam, rubrikaszint, kapu-típus, completion-feltétel és kötelező/opcionális besorolás minden változása, a döntési vagy finding-bizonyítékkal. Utólagos vétó/QA: a döntésben megnevezett szerep.

### 12.1 A fix-tervek vétólistái (szó szerint)

A tervek „Vétólista” szakaszai, modulonként. A szándékosan nem alkalmazott blokkok (4.2) sorai nem léptek életbe: az M3 LMS-2 sorában a #55–#62, #64, #65, #67; az M5 ERT-28 sorai (M5.2 SLIDE 8, HUB:207/KAPU:312); a Z „Teljesítve”-sorában a MAN LMS-Z-08 (#58). A QA-javítás által finomított helyek a 12.2-ben.

#### M0

| Hely | Előtte → utána | Döntés és előíró szövegrész |
|---|---|---|
| M0.1:13, M0.2:13, M0.3:14, M0.4:14 (#9, #10, #11, #13); MAN:16, :39 (#29–31); RA:72 (#36) | **completion-feltétel:** „a … választók / választós interakciók / négy MC kérdés megválaszolása” → „az összefoglaló dia elérése, nem minden beágyazott kérdés megválaszolása”; a pontozatlan vélemény- és önjelző választók (M0.1 SLIDE 3–5, M0.2 SLIDE 2, M0.3 SLIDE 1, M0.4 SLIDE 1/2/5/7) nem completion-elemek | ERT-1: „az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését”; ERT-2: „általánosan ne legyen önálló completion-elem … M0.1-nél ezt kifejezetten rögzítsük”. A QA-nak tudatosan el kell fogadnia: az M0.2 SLIDE 3 biztonsági helyzetfeladata megválaszolás nélkül is teljesít (döntési csomag). |
| HUB:169 (#4); MAN:155 (#34); MAN:43 (#32) | **M0 completion:** „Bemutatkozó fórum: 1 poszt + 1 komment” feltétlen → csak a fórum megnyitása után feltétel | ADV-6: „maradjon valódi tanulóknak zárva, amíg …”, „Addig szóbeli/nem rögzített bemutatkozás a biztonságos alternatíva” – zárt fórum nem lehet teljesítési feltétel (az LMS-M1-01 „M0 complete” unlockja különben elakadna), a nem rögzített alternatíva pedig nem Moodle-completion. A kvíz-feltétel (mind a 7 item, eredménytől függetlenül) nem változik. |
| HUB:41 (#2) | 3. kompetencia: feltétlen → a fórum megnyitásához kötött | ADV-6 + PRG-2: „ahol nincs ilyen [gyakoroltatott teljesítmény], inkább szűkítsük a hub-ígéretet”. |
| HUB:223, :254, :260 (#5–7) | belépőkvíz 4. és 7. itemtörzse, a 7. item **✅ C opciójának szövege** („completion-státusszal” → „completion-állapottal”) | ERT-11: „javíthatók a kérdések helyességének és a ✅ elhelyezésének változtatása nélkül”. A ✅ helye, a kulcs, a disztraktorok tartalma változatlan. |
| MAN:220 (#35) | M0 „Megerősítés”: `SCHEDULE_TO_RESYNC` 18:00 → „nincs” | PRG-6: „ne kapjon kitalált formális megerősítési kaput”. Completion/unlock (M1 ← „M0 complete”) és a kapu-beadás célideje változatlan. |
| M0.A:347 (#24) | csoportösszevonási feltétel: „vagy páratlan a létszám” törölve | PRG-11: „8–20 főnél alapból 3–5 fős csoportokat … Ez működési alapjavaslat, nem új kánoni létszámkorlát.” Létszámsáv (8–20) és darabszám nem változik. |
| M0.A 2.3 (#20); GK §4 (#41) | új képzői személyzeti szabály (szigorítás) | GYV-5 szó szerint; a HUM-SAFE-03 „legalább egy” felnőttje az érzékeny peulákra szigorodik (a HUM 14 döntése kifejezetten így rendelkezik). |
| M0.A 4.5 (#26) | új adatvédelmi eszköz-protokoll (szigorítás) | ADV-11 szó szerint (kereszt). |
| HUB §6 (#8) | az egyéni utánkövetés korlátja (szigorítás) | GYV-23 szó szerint. |

Answer key: egyik blokk sem ad hozzá, töröl vagy helyez át ✅-t; elosztó nem cserélődik. Küszöb, ponthatár, időtartam (perc),
rubrikaszint, kapu-típus és kötelező/opcionális besorolás egyik blokkban sem változik.

---

#### M1

| Hely | Előtte → utána | Döntés és szövegrész |
|---|---|---|
| KAPU:28, :132, :309 (#31–#33) | Az item-bank „Moodle Quiz / H5P Question Set, formatív / completion(-only)” → „szerzői itempool, külön Moodle-activity és manifest-sor nélkül”. A MAN-ban sor sosem volt; az M1 complete (HUB:248, MAN:156) nem változik; ✅ és itemek változatlanok. | ERT-4: „szerzői itempoolhoz ne hozzunk létre új tárolt aktivitást … Az M1 nyitott szöveges itemjei maradjanak szerzői pool”. |
| KAPU:47; M1.4:490, :571, :584; HUB:241 (#85, #28, #90, #91, #84) | Rubrikasor-név „Szituáció (S) konkrétsága” → „Helyzet (S) konkrétsága”; szint, pont, horgony változatlan. | TERM-2: „A rubrikacím is ehhez igazodjon úgy, hogy az értékelt kompetencia és a pontozás ne változzon.” |
| KAPU:55; M1.4:490, :593 (#27–#29) | S „Erős”: „idő ÉS/VAGY hely ÉS a helyzet szakasza” → „az idő vagy a hely (vagy mindkettő) ÉS a helyzet releváns szakasza” + zárójeles pontozói példák; a tanulói másolat „mikor, hol és melyik helyzetben” → „mikor vagy hol (vagy mindkettő), és a helyzet melyik szakaszában”. Pont, küszöb változatlan. | ERT-16: „idő VAGY hely (mindkettő lehet) ÉS a helyzet releváns szakasza. Kerüljön zárójelezett, pontozói példákkal megadott szabály a rubrikába”. |
| KAPU:79 (#30) | A 4. sor vezérkérdéséből a „(megtartható kapcsolatban)” kikerül, utána magyarázatként áll; nem pontozott szempont. | ERT-17: „magyarázó cél legyen, ne új … külön pontozási dimenzió”. |
| KAPU:81 (#26) | Új értékelői szabály: egy enyhe minősítő szóért egy levonás, a B-sor viseli; a hangnem csak önálló kommunikációs hibánál. Szintleírás, pont, küszöb változatlan. | ERT-15: „Ugyanazért az enyhe minősítő szóért csak egyszer járjon levonás. … a hangnem külön csak önállóan igazolt kommunikációs hibánál módosulhat.” |
| KAPU §5 (#24) | Új értékelői szabály a minta bemásolására. Szint, pont, küszöb, ✅ változatlan. | ERT-14: „kimondott értékelői szabályt a mintaválasz szó szerinti visszaadására”. |
| KAPU §5 (#34); MAN:50 (#35, DEFER_CANON) | Az Assignment saját completionje: „leadva + megerősített kapueredmény” → SUBMITTED („Make a submission”); CONFIRMED a `GATE_CONFIRMED_M1`-en (LMS-M1-06). A küszöb (soronként ≥1 ÉS ≥5/8; Grade to pass 5; Maximum grade 8) és a downstream unlock (MAN §4, GATE-CP) változatlan. | ERT-9: „ASSIGN-M saját completion = SUBMITTED … a tényleges szakmai CONFIRMED állapot külön GATE-CP-n álljon be … A korábbi pontküszöb nem változik.” |
| HUB:30, :93 (#56, #58) | A „4/5” formatív, nem kapuzott célérték kikerül (sehol nem mérik; az M1.2-ben 6 kártya van). | PRG-2: „Kimeneti kompetenciának csak a ténylegesen gyakoroltatott/mérhető teljesítményt nevezzük; … szűkítsük a hub-ígéretet”. |
| M1.2 SLIDE 5 és meta (#67–#81) | A Drag & Drop forma kikerül, a húzásmentes rádió-/kattintásos út az egyetlen. A kártyák és a besorolási kulcs (:754–:759), a visszajelzések és a completion változatlan; a billentyűzet-, fókusz- és 24×24 px-követelmény nem gyengül. | PRG-9: „M1.2 SLIDE 5 Drag & Drop: nem szükséges, legyen csak húzásmentes, rádió-/kattintásos út.” |
| M1.1:204 (#5) | A rögzítő választós H5P tartalékút kikerül; a szöveg + Tovább az út. A választó eddig sem volt completion-elem (:344). | ADV-4: „M1.1-ben a szöveg + Tovább út az alap”, „lehetőleg ne rögzítsük”. |
| M1.3:913–915 (#38); M1.4:514–515 (#39) | Biztonsági szöveg (nem invariáns, jelzem): az egyedi „ha nagyon nehéz helyzet” felszólítás helyére az ADV §11:241 mondata (M1.3), illetve az elhagyása (M1.4). A Memuna-mondat (M1.4:516) és a HUM-SAFE-03 blokk (M1.3:917, M1.4:518) változatlan; védelem nem törlődik. | GYV-12: „az ADV §11 már elfogadott, adattakarékos mondata kerüljön az önfeltárást sugalló egyedi felszólítás helyére”; GK §4.3:102. |
| M1.4:10, :426, :450; M1.3:45; M1.B:359 (#16–#20, #23) | Mondatszám-útmutatás „1–2” → „2–3”; nem küszöb (a KAPU:21 kimondja, #15). A darabszám (min. 1, max. 2 SBI) változatlan. | ERT-13: „kánoni hossza 2–3 mondat … A mondatszám csak instrukció, ne váljon pontozott küszöbbé.” |

#### M2

| # | Hely | Előtte → utána | Döntés és az előíró szövegrész |
|---|---|---|---|
| 1 | HUB:183, :190 (54–55.); MAN:57 (57., 48.) | completion: „a fiktív eset szakmai válasza … érdemben rögzítve” → „… (vagy a passz és egy mondat arról, kit vonna be)”; a mező „Required” marad | GYV-2: „a teljesítés nem függhet önfeltárástól … M2.4 kötelező mezője így biztosan módosítandó” |
| 2 | MAN:56 (21.), MAN:16 (20.), M2.4:55 (19.), HUB:183 (54.) | LMS-M2-03 completion: H5P-C profil („Receive a grade”, attempt tracking Yes) → megtekintés („View”), attempt tracking ki, nincs grade; a „Kötelező = igen” és az unlock-lánc nem változik | ERT-18: „ne generáljanak fantom „grade”-et. A továbblépést … a megtekintéshez kell kötni”; runtime-próba nélkül nem kész |
| 3 | KAPU:261 (17.), :41 (15.), :206 (16.) | R3 alkalmazása: a kitalált madrih példája egyenértékű a saját példával; a rubrikaszintek szövege változatlan | ADV-5: „engedjünk semleges, fiktív vagy válasz nélküli egyenértékű utat pontlevonás nélkül” |
| 4 | KAPU:178 (82.) | R2 elfogadási kritériuma kimondva (Ideológiai Kézikönyv; érték ≠ hangulat; nincs világnézeti vallomás); szintek változatlanok | TERM-8: „A rubrika nyitott, leírt kritérium alapján fogadja el az érték és hangulat közti különbséget” |
| 5 | 17 M2-hely (25–41.), HUB:129 (77.), GL:188, :194, PT:242, :286 (42–45.) | „ha a kapu nem teljesült/teljesül” → „ha a jegyzet a kapu küszöbe alatt maradt/marad”; kaputípus, küszöb, 1+1 beadás, GATE-CP címkék változatlanok | ERT-8: „a gyenge, de értelmezhető munka formatív F-peula-javaslatot váltson ki, ne „nem teljesült” bukást” |
| 6 | KAPU:26, :56, HUB:179 (22–24.) | az opcionális kvíz → szerzői itempool, activity csak két feltétellel; ✅, elosztók, keverés változatlan; manifest-sor eddig sem volt (nem completion-változás) | ERT-4: „az M2 zárt formatív gyakorló csak akkor activity, ha a tanulói út követeli és DPO által elfogadott” |
| 7 | HUB:33 (81.) | kimeneti kompetencia „Röviden elmondja …” → nem pontozott reflektív cél (mérőelem eddig sem volt) | TERM-7: „M2-ben a személyes ideológiai viszonyulás legyen nem pontozott reflektív cél” |
| 8 | M2.B:45, :56, :231, :264, :331–335, :400, :431, :435 (67–74.) | fix 3 csoport/lap/asztal → a létszámhoz igazodó csoportszám; „3–5 fős” alapból marad; időkeret változatlan | PRG-11: „a csoportszámot és kártyakészletet a létszámhoz igazítva” |
| 9 | M2.A:250, :265, :224 (58–60.) | a 2., 3., 5. állításnál nyilvános kiállás → fejben/papíron, passzal; a 8 állítás és az idő változatlan | GYV-20: „Privát, papíros vagy fejben végzett út, passz és nem érzékeny közös reflexió legyen a default” |

Answer key: egyik blokk sem ad, töröl vagy mozgat ✅-t, és elosztót sem cserél (a 62. blokk a KAPU Item 5 visszajelzéséhez
fűz mondatot, a ✅ B és az opciók szövege érintetlen). Küszöb, ponthatár, időtartam, kapu-típus és kötelező/opcionális
besorolás nem változik.

#### M3

| # | Hely | Előtte → utána | Melyik döntés, melyik szövegrésze írja elő |
|---|---|---|---|
| 1 | HUB:252; M3.4:12; M3.1:586; M3.2:675 és EGY-02; M3.4:512 és EGY-04 (#21, #22, #23, #24, #25, #26, #27) | completion: „érdemi kitöltéssel … nem csak a slide-ok végigléptetésével” / „a H5P-interakciók megválaszolva” / „a válasz nélküli végigléptetés nem ad completiont” → a CP összefoglaló diájának elérése, a kitöltés nem kikényszerített, negatív teszt kötelező; M3.3 (BS) változatlan | ERT-1: „az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését … az üres/kihagyott interakciós negatív teszt kötelező” |
| 2 | KAPU:78 (#28) | a kritikus itemkör bővítésének jóváhagyói rendje: „projektgazdai döntés; vétó/QA: értékelési felelős + Memuna” → egyszerre írásos projektgazdai kapudöntés és Memuna-jóváhagyás, értékelési kalibráció; az ITEM 10 nem kritikus (a kritikus itemek 2, 4, 7, 9 és a ≥10/12 változatlan) | ERT-10: „egyszerre kell írásos projektgazdai kapudöntés és Memuna-jóváhagyás … Az ITEM 10-et addig ne emeljük kritikusnak” |
| 3 | KAPU §2.1 (új pont), R1 Alapszint/0, R2 0-cella; M3.4:837; M3.B:512 (#29, #30, #31, #32, #33) | R1: csak „valódi red flag” → biztonsági/határhelyzet is; R2 0: „meg sem említi” minden helyzetben → csak feltárást vagy titoktartási ígéretet tartalmazó helyzetben; feltárás nélkül legalább Alapszint (1) | ERT-21: „R1 fogadjon el … releváns biztonsági/határhelyzetet … R2-t … ahol nincs feltárás vagy titoktartási ígéret, ne büntető mechanikával alkalmazzuk” |
| 4 | KAPU R4 és R1 sor (#30, #34) | R4 „Nem nyomoz / nem konfrontál + életszerű helyzet” → „Nem nyomoz / nem konfrontál”; az életszerűség három szintje az R1-be (nem blokkoló sor); 4 sor, max. 8, ≥1 szabály, pontsáv változatlan | ERT-22: „R4 sorban csak gyermekvédelmi eljárási kritérium … Az életszerűség kerüljön egy nem blokkoló minőségi sorba” |
| 5 | M3.A 4.3, 1. lépés (#68) | kiscsoport: 3–4 fő → 3–5 fő, a csoportszám a létszámból | PRG-11: „8–20 főnél alapból 3–5 fős csoportokat képezzünk, a csoportszámot … a létszámhoz igazítva” |
| 6 | M3.F 1. szakasz (#93) | a kötelező F-peula hiányzás esetén: (nincs út) → dokumentált pótidőpont vagy jóváhagyott, rövid egyéni mentoros út, a javító próbálkozás előtt | PRG-5: „Hiányzásnál dokumentált pótidőpont vagy jóváhagyott, rövid egyéni mentoros út legyen, mindig a javító próbálkozás előtt” |
| 7 | M3.4-EGY-03 (törlés), M3.2-EGY-01, ♿ dobozok, „Mit lát/látunk?” (a teljes LMS-2-blokklista: #45, #46, #47, #48, #49, #50, #51, #52, #53, #54, #55, #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #66, #67) (#45, #46, #53, #54, #56, #61, #62) | a kapus belépő lecke interakciós útjai: húzásmentes + Drag & Drop → csak húzásmentes; kártyák, kulcs, ✅ változatlan | LMS-2: „Az M3.2/M3.4 Drag & Drop mellékutakat hagyjuk el” |

Nem invariáns, de értékelési közelségű (tájékoztatásul): ERT-5 (visszanézés tartalma; kulcs, küszöb, próbálkozásszám változatlan), ERT-23 (a kulcs a validálásig változatlan), TERM-6 (kártyacímke; a kulcs változatlan).

#### M4

| Hely | Előtte → utána | Döntés és az előíró szövegrész |
|---|---|---|
| M4.1 SLIDE 3 IV, 3. kérdés (2–6. blokk; VID-02 spec, notes) | beágyazott Free Text beviteli mező (státusza rögzítetlen) → beviteli elem nélküli, opcionális, tanuló-lokális gondolkodtató kérdés; a kérdés szövege és a completion (CP összefoglaló dia + LMS-M4-06) nem változik | ADV-3: „opcionális reflexió saját jegyzetben, beviteli elem és completion nélkül” |
| M4.3 SLIDE 5 K3 szár (23. blokk) és visszajelzés (24. blokk) | „…és ellenőrizni, hogy nagyjából egy oldalon vagytok.” → „…és új vita nyitása nélkül ellenőrizni, hogy a kvuca érti-e, mi volt a mai peula célja.”; „Egy egyszerű, részben zárt kérdés…” → „A lezárásban az a kérdés segít, amely konkrétan a mai peula céljára kérdez rá…”; **a ✅ (3. opció), az opciók, a K1, a K2 és a SLIDE 1 változatlan** | ERT-25: „elsőként a kérdésszár pontosítása és a meglévő helyes válasz megtartása preferált” |
| HUB:128 Kapu 1 „Következmény” (22. blokk) | gyenge eredménynél egyéni jelzés és mentori M4.F-ajánlás (határ nélkül) → nincs egyéni küszöb, összesített téma-visszajelzés; új küszöb nem kerül be; completion, Grade to pass, puha kapu változatlan | ERT-24: „ne állítsuk be önkényes P/F küszöbként. Addig személyre nem szabott, összesített téma-visszajelzés legyen” |
| HUB:104, :108, :159, :170; M4.1:53, M4.2:57, M4.3:52, M4.4:62; M4.F:37; GL:188 (25–34. blokk) | az F-peula kiváltója „a kapu nem teljesült” → a vázlat a Kapu 2 küszöbe alatt (formatív javaslat); kaputípus, „alapszint / rendben” küszöb, „Teljesítve / Még nem teljesítve” címke, 1+1 beadás változatlan | ERT-8: „a gyenge, de értelmezhető munka formatív F-peula-javaslatot váltson ki, ne „nem teljesült” bukást” |
| M4.B:278 (44. blokk), HUB:138 (43. blokk) | **kötelező ↔ opcionális:** az SBI a peula-visszajelzésben kötelező („add”) → opcionális; a Megfigyelés → Hatás → Következő lépés szerkezet kötelező | PRG-10: „az SBI forma legyen opcionális, de Megfigyelés → Hatás → Következő lépés szerkezet kötelező” |
| M4.3:20, M4.4:26; MAN:73, :75 (49–52. blokk) | „a puszta végignézés nem elég” → „a completion az összefoglaló dia elérését jelenti, nem minden beágyazott kérdés kötelező kitöltését”; a completion-beállítás (Receive a grade, Hide summary slide = No) és a TEXT-C kötelező mezői változatlanok | ERT-1: „az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését” |
| HUB:133 Kapu 2 rubrika, „Fejlettebb” szint példája (20. blokk) | „pl. nevesített korosztály/élethelyzet” → „pl. nevesített korosztály, hozzávetőleges létszám, a csoport általános energiája vagy hangulata”; a szintlogika és a küszöb változatlan | ADV-9: „korosztály, hozzávetőleges létszám, általános energia/hangulat igen; név, diagnózis, konkrét azonosítható eset nem” |
| HUB:46 (46. blokk); M4.B:19, :21 (47–48. blokk) | kompetencia- és célígéret szűkül (példamondás: nyitott, tisztázó; kérdező vagy válaszoló szerep; visszajelzés a peulabemutatóra és a nyitó kérdésre); Kapu 1 itemei és ✅ változatlan | PRG-2: „Kimeneti kompetenciának csak a ténylegesen gyakoroltatott/mérhető teljesítményt nevezzük” |
| M4.4:759 (53. blokk) | fájlszám nincs megadva → legfeljebb 1 fájl (build-paraméter) | LMS-1: „alapból legfeljebb 1 fájl” |

#### M5

| hely | előtte → utána | döntés (szövegrész) |
|---|---|---|
| HUB:180; KAPU:24; KAPU:313; MAN:84 (DEFER) | „2–3 próbálkozás” → „3 próbálkozás”; a jelzést az első, visszajelzés előtti próbálkozás adja (eddig nem volt rögzítve) | ERT-6 („M5-ben 3 próbálkozást”; „az első, visszajelzés előtti próbálkozás a mérvadó”) |
| KAPU:286, :288; HUB:211; HUB:176; KAPU:26 | kapuegység: „minden sorban … mind a 4 kritériumon” (táblázatsor × kritérium) → rubrikakritérium a teljes táblázat alapján; küszöb (≥ Alapszint), szintek, R4 kritikus: változatlan | ERT-26 („elsődleges pontozási egysége a rubrikakritérium a teljes táblázat alapján”) |
| HUB:35 | 4. kompetencia: „minden sorban látszik, milyen tanulástan-logika” → „minden sorban látható a módszertani indok, és legalább egy sorban konkrét tanulástan-elem” | ERT-26 („egy tanulástani eszköz nem feltétlenül kell minden sorba”) |
| M5.4 SLIDE 6 (4 opciósor) | „✅ Igaz rám / ✅ Igen” → „☐ Igaz rám / ☐ Igen” (answer key megszűnik); Checkbox → pontozatlan, beviteli elem nélküli önellenőrzés | ERT-29 („ne legyen pontozott helyes–hibás kérdés”); ADV-4 („lehetőleg ne rögzítsük”) |
| M5.4:9; MAN:82 (DEFER) | completion: a SLIDE 6 kifejezetten nem completion-feltétel (eddig a Checkbox a Column gradejébe számított) | ERT-29 („a completion a lecke megtekintésén vagy más semleges eseményen alapuljon”) |
| M5.4 SLIDE 6 zárószöveg; 4. állítás | „a legtöbb állításra” → „mind a négy állításra”; a 4. állítás az R4-ismérvvel (KAPU:295) | ERT-29 (csomag (a): „a zárószöveg igazodik”), ERT-G2-1 HOLD |
| M5.2 SLIDE 8 ✅ opció | „Először a nevelési célt találom ki, és ahhoz választok módszert…” → „Először a feladatból indulok ki: megfogalmazom belőle a nevelési célt, megnézem, milyen kvucával dolgozom, és ehhez választok módszert…”; a ✅ helye és a disztraktorok változatlanok | ERT-28 („a helyes opciója … a tanított döntési utat méri”) |
| HUB:185 | completion: „érdemi kitöltéssel, nem csak a slide-ok végigléptetésével” → CP-nél az összefoglaló dia elérése | ERT-1 („az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését”) |
| HUB:187; MAN:84; MAN:160 (DEFER) | QUIZ-D completion: „kitöltés elég” / „kitöltve” → „a beküldés ténye elég” / „beküldve” | ERT-3 („a beküldés ténye elegendő completionhez”) |
| MAN:83, :160 (DEFER) | ASSIGN-M saját completion: „leadva + megerősített kapueredmény” → SUBMITTED; a CONFIRMED az LMS-M5-08 GATE-CP | ERT-9 („ASSIGN-M saját completion = SUBMITTED”) |
| MAN:85 (DEFER) | LMS-M5-07 profil: „H5P-C (rövid H5P …)” → „H5P-C vagy PAGE-C (rövid, adatminimalista …)”; completion-cella: nyitott | LMS-3 |
| M5.4:146 | „Az egyik sorod legyen …” (kötelező M4-es/valós kvuca-sor) → „lehet” + kitalált profil egyenértékű | PRG-10 („a valós kvuca-adat nem kötelező: fiktív profil egyenértékű”) |
| M5.A, M5.B ellenőrző lista (zárókör) | „minimum 1–2 mondat mindenkitől / pár embertől”, „minimum 2–3 ember” → mindenki kap lehetőséget, a passz teljes értékű | PRG-10 („Zárókörben mindenki kapjon lehetőséget megszólalni”) |
| KAPU:299–300 | kalibrációs megjegyzés: „+” → „és”; „diagnosztikus visszajelzés” → „fejlesztő visszajelzés”; szint és szabály változatlan | ERT-27 (b) |
| HUB:207; KAPU:312 | elemzési címke „cél az első” → „nem a játék az első” | ERT-28 (következmény) |
| HUB:208 | „célzott felzárkóztatást kapnak a produktum beadása előtt” → támogató, nem kötelező mentori ajánlás; formatív státusz változatlan | PRG-7 |

**Biztonsági és adatvédelmi szöveg (semmi nem törlődik, nem gyengül):** M5.2:317 eszkalációs küszöb (GYV-7: automatikus
Memuna → kétlépcsős, a Memuna választható marad; + passz, GYV-2) · M5.F:88 GK §4:63–64 (GYV-6) · M5.F begyűjtés és tábla
(ADV-8: szigorodik) · M5.A:439 telefonos út kimarad, a felvétel nélküli út marad (ADV-7) · HUB:20, KAPU:283, M5.4:146, ADV:84
adatszabály (ADV-9: szigorodik) · M5.4:45, :323 technikai admin (ADV-1: a tájékoztató pontosodik) · M5.4:203, MUNK-01
(ADV-10: szigorodik) · M5.F:55, :400 (ADV-11: szigorodik) · M5.F meta hiányzási út, 1:1 csak HUM-SAFE-02 szerint (PRG-5).

#### M6

| # | Hely | Előtte → utána | Melyik döntés, melyik szövegrész írja elő |
|---|---|---|---|
| #16, #17 | HUB:222, :226 | „két feltétel (1–2.)”, a kvíz „nem feltétel” → „három feltétel (1–3.)”, a kvíz **beküldése** feltétel (eredménye nem) | **completion-feltétel** – ERT-31: „beküldése legyen kötelező completion, de az eredmény ne blokkolja …”; a MAN:92/:161 már így |
| #18 | KAPU:38 | – → „A kvíz beküldése … az M6 teljesítésének kötelező eleme” | **completion** – ERT-31 (uaz) |
| #54–#56 | M6.1:9, M6.2:9, M6.3:9 | „a lecke választós interakciói megválaszolva” → „az összefoglaló dia elérése …; a SLIDE 1 pontozatlan választója nem completion-elem” | **completion-leírás** – ERT-1: „az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését”; ERT-2: „ne legyen önálló completion-elem” |
| #57 | HUB:224 | „érdemi kitöltéssel, nem végiglapozással” → „az M6.1–M6.3-nál az összefoglaló dia elérésével (BSPEC-06)” | **completion-leírás** – ERT-1 (uaz) |
| #58, #59 | KAPU:388, MAN:91 | „a completion ehhez kötött” / „leadva + mentor által megerősített kapueredmény” → GATE-CP-hez kötött / SUBMITTED + CONFIRMED a GATE-CP-n | **completion** – ERT-9 (D-h minta: SUBMITTED = leadás, CONFIRMED = GATE-CP); küszöb, R4/R5 változatlan |
| #30 | KAPU:72 | – → Review options sor; „az első, visszajelzés előtti próbálkozás számít” | **diagnosztikus jelzés / Moodle-beállítás** – ERT-6: „az első, visszajelzés előtti próbálkozás a mérvadó … A gradebook és az analitika e két szerepét el kell választani”; a Review options a csomag szerint objektív alpont; korlátlan próbálkozás, ≥10/12 változatlan |
| #31, #52, #53 | KAPU:438, HUB:242, :247 | „pár próbálkozás után” → „az első, visszajelzés előtti próbálkozáson”; beavatkozás gazdája | **jelzőszabály** – ERT-6 (uaz), PRG-7; a >30% / 80% szám nem változik |
| #33 | MAN:92 | „korlátlan újrapróbálás” → + első próbálkozás mint diagnosztikus adat | ERT-6 (uaz) |
| #20–#23, #19, #24 | KAPU:388, :390, :400, :422; HUB:218; PT:288 | „társas pontozás / társ–stáb kalibráció” → pontozás nélküli társas visszajelzés, képzői végső rubrika, stáb-kalibráció | **értékelési eljárás (ki pontoz)** – ERT-33: „formatív, pontozás nélküli …; a végső rubrikával a képző értékel, a stáb egymás között kalibrál … pontosítsuk a projektgazda engedélyével”; szintek, küszöb, R4/R5 változatlan |
| #39 | KAPU:386 | – → „A kapudöntést a rubrikasorok … és a GATE-CP hordozza, nem a … normalizált összpont” | **kapu-megállapítás** – LMS-4 (első és utolsó mondata); 1/2/3 és küszöb változatlan |
| #40 | RA:55 | – → pozitív teszteset (csupa „Oké” = 10/15 → teljesül) | LMS-4: „a 10 pontos „csupa Oké” negatív/pozitív teszt legyen dokumentálva” |
| #25 | KAPU:60 | „Parparim 6–9 / Kivsza 10–12 / Leviatán 13–17” → Kivsza-item nincs, a lefedettség nem teljes | **lefedettségi állítás** – ERT-34: „addig a meglévő kvízt ne hirdessük teljes korosztályi lefedettségűnek”; itemszám, küszöb, kulcs változatlan |
| #27 | KAPU:163 | 4. item visszajelzésének forrása „(M6.4, D. szcenárió)” → „(M6.4, záró oldal; részletesen: a D. szcenárió)” | ERT-35 (kötelező forrás); ✅ és szár változatlan |
| #26 | M6.4 ZÁRÓ | – → a 4. item elvének minimális változata | ERT-35: „kerüljön az összes tanuló által garantáltan látott kötelező forrásba”; D-e topológia, ✅-ok változatlan |
| #28, #29 | M6.B:261, :347 | a közös páros lap → vázlat; egyéni véglegesítés és leadás | **leadási szabály** – ERT-37: „az éles LMS-M6-05 kapun minden résztvevő önállóan véglegesít és nyújt be egyéni játéklapot”; profil, R1–R5 változatlan |
| #44–#51 | HUB:53, :62, :84, :97, :122; M6.1:15; M6.2:15; M6.4:55–56 | kimondott kompetencia / mikrocél → a gyakorolthoz szűkítve (pl. „3–4” → „2 nyitott kérdést”) | PRG-2: „Kimeneti kompetenciának csak a ténylegesen gyakoroltatott/mérhető teljesítményt nevezzük; … inkább szűkítsük a hub-ígéretet”; kapu, ✅, rubrika változatlan |
| #35 | M6.A:460 | opcionális tiltott-zóna megjegyzés → kötelező, kimondott keret | **kötelező ↔ opcionális** – GYV-17: „rövid, kötelezően kimondott biztonsági keretek a gyakorlat előtt” |
| #36, #37 | HUB:98, M6.2:606 | „nálatok” mintakérdés → opcionális, passzolható | GYV-18: „a „nálatok” önfeltáró kérdés opcionális és passzolható” (a KAPU 12. item kulcsa nem változik) |
| #38 | M6.2:783 | a jelzési út kiváltója „friss seb, bántalmazás” → zaklatás, bántalmazás, önsértés, veszélyeztetettség; gyász: támogatás | **gyermekvédelmi küszöb** – GYV-7: „Kétlépcsős küszöb …”; védelmi elemek megmaradnak |
| #34 | M6.4 5D-J | – → az M6.1 biztonsági minimuma szó szerint | GYV-16 óvatos alapértelmezése; védelem bővül |
| #61, #62, #60 | M6.A 2.3, 5. lista, spec | – → két felkészített 18+ felelős vagy azonnal elérhető helyettes | GYV-5 óvatos alapértelmezése; felügyeleti minimum nem gyengül |
| #1, #2 | M6.3:550, HUB:14 | külső eszköz feltétel nélkül / szervezeti fiókkal → jóváhagyásig papír, felülvizsgálat után | ADV-10 óvatos alapértelmezése |

Answer key (✅), opciók, elosztók, küszöbszámok (≥10/12, 80%, >30%, >25%, minden sor ≥2), időtartamok (45’, 15–20’),
rubrikaszintek (1/2/3), kaputípus (éles) és a kötelező F-peula egyik blokkban sem változik.

#### M7

Minden tétel a lezárt HUM 14-es döntés szó szerinti előírása; a ✅-ok helye, az opciók száma, a 12/14, a 17/24, a
kritikus és blokkoló sorok, a 0–3 / 0–2 skálák és az 1+1 próbálkozás sehol nem változik.

| Hely | Előtte | Utána | Döntés és szövegrész |
|---|---|---|---|
| KAPU:21, :48, :52, :216, :411; HUB:382, :384; M7.4:704, :843; MAN:101, :102, :104; PT:112, :203, :275; RA:57 (18–33.) | „≥80% (14 itemből ≥12 jó)” mint döntő formula; a részpont sorsa kimondatlan | „legalább 12 teljesen helyes item a 14-ből”; a Multi-Select csak teljes ponttal számít; kézi megerősítés, negatív teszt 11+2; a „Grade to pass = 12” önmagában nem elég | ERT-40: „a kapuküszöb darabszám-alapú (legalább 12 teljesen helyes item / 14), ne átszámított részpontszázalék … Ne engedjen át „Grade to pass 12” önmagában.” |
| KAPU:259, :262, :422, :423; M7.4:789–790; MAN:103 (34–39.) | „completion-szinten … veszi figyelembe / elvárt … nem blokkol” | az érdemi leadást nézi; hiányzó/üres mezőnél pótláskérés, nem értékelő visszajelzés; nem buktat, a v2 értékelését nem akadályozza (nem pontozott, 24 pont változatlan) | ERT-41: „kérjünk kitöltési pótlást és értelmezhető, nem értékelői visszajelzést, de ne buktassuk a kaput és ne tiltsuk a szakmai v2 értékelését” |
| KAPU R3 (:294–300), HUB:162 (40–41.) | 0–2. szint: a 11 pont fázisai és az ív együtt; az 1-es szint az élmény-blokkot „fázisnak” hívja | „Mit mér”: egyetlen konstruktum, a belső ív; a fázisok bizonyítékok; a 0–2. szint az ívet írja le (3-as szint, skála, nem kritikus státusz változatlan) | ERT-44: „Az M7 R3 egyetlen konstruktuma a peula koherens belső íve legyen; a három fázis … ne külön még egyszer pontozott dimenzió.” |
| KAPU:347 (R7/1), :210 (Q12 visszajelzés), M7.2:708 (42–44.) | „túllépik a 45 percet”; „belefér-e 45 percbe”; „Működni fog ez 45 percben” | a tervezett időkeret túllépése / betarthatósága, a 45 perc csak példa (a Q12 kulcsa és opciói változatlanok) | ERT-45: „a … tervezett időkeret betarthatóságát pontozzuk; a 45 perc csak példa lehet” |
| M7.1 SLIDE 4 (:324–358), M7.1:8, :45, HUB:185 (45–53.) | pontozott Fill in the Blanks, „add meg az összes reális számot … elfogadott válaszként” | pontozatlan, formatív feladat saját jegyzetben, elfogadott számlista nélkül; a visszajelzés-szövegek maradnak | ERT-46: „Ha a „reális” szabad mérlegelést jelent, legyen pontozatlan, formatív visszajelzéses feladat; semmilyen numerikus varázsküszöböt ne gyártsunk.” |
| KAPU:382 ((C) 1. sor, 2-es szint) (54.) | „+ átláthatóság (sötétedés, hazaút) megnevezve” | két alpont: (a) ki tud a felügyeletről / kockázatról; (b) a helyszín, sötétedés, hazajutás feltételeinek közlése | ERT-47: „bontsuk két ellenőrizhető alpontra …” |
| KAPU:383 ((C) 2. sor, 1–2. szint) (59.) | „vagy a „mi van, ha többen/kevesebben jönnek””; „+ „mi van eltérő létszámnál” átgondolva” | az „eltérő létszám” elvárás kikerül mindkét szintből | ERT-49: „a legkisebb helyes változás a rubrika szűkítése” |
| KAPU:348 (R7/2); M7.4:74, :619 (SLIDE 5 ✅ opció), :698, :776, :817 (63–68.) | „min. 3–4 soros / 3–4 sor” | „legalább 3 sor (4 ajánlott, de nem kötelező)”; a ✅ helye változatlan | ERT-50: „minimális terjedelme 3 értelmes sor legyen; 4 sor ajánlott, de nem kötelező” |
| M7.4:14 (lecke-completion) (92., 132.) | „a választós interakciók érdemi megválaszolása … SLIDE 3 kvuca-típus-választó … a SLIDE 4 AI-biztonsági Multiple Choice completion-elem marad” | „az összefoglaló dia elérése (BSPEC-06)”; a SLIDE 3 választó nem completion-elem; a SLIDE 4 fókuszlista nem H5P-interakció | ERT-1 („az összefoglaló dia elérését jelentse”), ERT-2 („ne legyen önálló completion-elem”), LMS-6 („a Completiont az oldal vagy összefoglaló dia biztosítja”) |
| M7.4 SLIDE 4 (:514, :532, :543–545, :872) (93–96.) | „nem pontozott fókuszválasztó lista”, H5P-útja nyitott | pontozatlan, saját jegyzetes lista, interakció nélkül | LMS-6: „legyen pontozatlan, saját jegyzetes lista, nem minden választ „helyessé” programozó H5P Multiple Choice” |
| M7.2:8 (új lecke-completion sor), :87, :130; MAN:96 (55–58.) | completion-sor nincs; az ellenőrző kérdés „külön H5P-activityként” is futhat | a befogadó oldal completionje; beágyazott, nem külön pontozott kérdés, külön activity és gradebook-nyom nélkül | ERT-48: „a kötelező tanulási tartalom megtekintését a befogadó activity completionje jelölje … külön H5P gradebook-nyom ne keletkezzen” |
| M7.2 SLIDE 7 (:913, :947, :953, :975), M7.B:29 (8–12.) | opcionális szöveges mező / Moodle-reflexió | saját jegyzetes, beviteli elem nélküli opcionális reflexió (completion-feltétel nem volt és nem lesz) | ADV-3: „opcionális reflexió saját jegyzetben, beviteli elem és completion nélkül” |
| M7.3 (:7–8, :53–54, :780–881), HUB:116, :217, :401; MAN:97 (79–91.) | külön „Moodle Checklist” activity, tárolt komment | core oldal / CP + letölthető munkalap, tanuló-lokális; completion a befogadó lecke (LMS-M7-03); az 5–10’ időtartam marad | LMS-5: „Moodle core Page/CP + letölthető munkalap formában, tanuló-lokálisan …, külön tárolt komment és plugin nélkül; a completiont a befogadó tanulási szakasz viszi” |
| MAN:103 (completion-cella) (133.) | „leadva + megerősített rubrika” | SUBMITTED a v2 leadása; CONFIRMED a GATE-CP-n (LMS-M7-08); küszöb változatlan | ERT-9: „ASSIGN-M saját completion = SUBMITTED …; a … CONFIRMED állapot külön GATE-CP-n álljon be” |
| M7.1:529 (LMS-M7-10), M7.4:310, KAPU:405, HUB:372, M7.B:457 (13–17.) | az R elem „kötődjön” a saját M2-értékhez | kötődhet; semleges vagy kitalált érték egyenértékű, pontlevonás nélkül; az LMS-M7-10-ben a megnevezés kihagyható (az R1 nem változik) | ADV-5: „Ne legyen kötelező azonosítható vallási önbesorolás; engedjünk semleges, fiktív vagy válasz nélküli egyenértékű utat pontlevonás nélkül.” |
| KAPU:25, :27; HUB:144; M7.4:702; M7.F:35; MAN:102 (123–128.) | a függő kvízeredmény és a v2-határidő viszonya kimondatlan; a kvízen bukott v2-jének javító helye nyitott | egyéni határidő-hosszabbítás függő eredménynél; a meglévő M7.F utáni 1 + 1 v2-leadás (dátum nélkül) | PRG-6: „a függőben lévő kvízeredmény ne szorítsa ki a v2 határidejét: indokolt egyéni hosszabbítás és meglévő F-peula utáni 1+1 javítás” |
| KAPU §A (:51), QA-lista (:412), MAN:101 (60–62.) | Review options rögzítetlen | első próbálkozás után pontszám és hibázott kompetencia; kulcs és opciónkénti visszajelzés csak a javító lezárása után | ERT-5: „ne jelenjen meg a helyes kulcs és a teljes opció-visszajelzés a javító lezárása előtt” |
| HUB:159 (1. kompetencia) (113.) | „2–3 „szétfolyó” célt át tud írni SMART nevelési céllá” | a ténylegesen gyakoroltatott lépések (megkülönböztetés, SMART-elem pótlása, saját SMART cél) | PRG-2: „Kimeneti kompetenciának csak a ténylegesen gyakoroltatott/mérhető teljesítményt nevezzük” |
| HUB §7 kilépőkártya, HUB-MUNK-01 (1–2.) | kétkérdéses kártya (1–5 skála) mindhárom peula után, QR-változattal; legyártandó print-pdf | az M7.B egykérdéses papírkártyája; az asset `reuse` (külön print-pdf nem készül) | PRG-3: „a hub/meta/kártya-spec azzal egyezzen”; ADV-10: „Moodle és papír legyen az alap … ne engedjük az opcionális külső eszközt” |
| M7.F:392, MUNK-02 (4) (77–78.) – gyermekvédelmi szöveg | „ha valakit mélyen érint egy gyermekvédelmi téma, a Memunát vonom be” | veszélyeztetettség gyanújánál azonnal Memuna; pusztán érzelmi érintettségnél mentor, választható Memunával | GYV-7: „zaklatás, feltárás, önsértés vagy más veszélyeztetettség gyanújánál azonnali Memuna-jelzés; pusztán nem veszélyeztető nehéz érzelemnél támogató mentorálás, választási lehetőséggel” |
| Gyermekvédelmi, AI- és adatvédelmi hozzáadások (törlés nincs): M7.A:56, :479, :518; M7.B:93; M7.F:89 (GYV-6, GYV-13); HUB:133, :282, M7.1:413, M7.2:24, :68, :114, :990, M7.4:82, :878, M7.B:75, :478, :588, :627, ADV §7, RA 20, MAN:94, :98, :119, PT:250 (GYV-10, LMS-8, ADV-12); M7.4:820 (ADV-10); M7.F:49, :350, :380 (ADV-11); M7.F:81 (ADV-2) | – | szigorítás vagy pontosítás; a HUM-PRIV-04 szó szerinti tanulói mondata és a „ne AI-t kérdezz” mondatok változatlanok | GYV-6, GYV-13, GYV-10, LMS-8, ADV-12, ADV-10, ADV-11, ADV-2 |

#### Z

| Hely | Előtte | Utána | Döntés és szövegrész |
|---|---|---|---|
| Z.1:13 (#8) – completion | a SLIDE 1, 3 és 4 választós interakcióinak megválaszolása | az összefoglaló dia elérése; feladatelem a SLIDE 4 (a négy ✅ változatlan); a SLIDE 1/3 nem completion-elem | ERT-1 „az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését”; ERT-2 „ne legyen önálló completion-elem” |
| Z.2:13 (#10) + MAN LMS-Z-02 (#55) – completion | a SLIDE 1, 3 és 4 Single Choice megválaszolása | az összefoglaló dia elérése; a három választó nem completion-elem; a dia megléte igazolandó | ERT-1, ERT-2 (ua.) |
| Z.3:59 (#13) + MAN LMS-Z-03 (#56) – completion | (a lecke completion-sort nem ír; a profil szerint az interakciók) | a választók nem completion-elemek; az összefoglaló dia megléte igazolandó | ERT-1, ERT-2 |
| HUB:198 (#7) – completion | a Z.A a „Minimális teljesítés” 2. pontja | ajánlott, nem kötelező feltétel; a hiányzás nem akadályoz | ERT-39 „ne a Moodle program completion kötelező feltétele … Hiányzó jelenlét ne akadályozzon” |
| HUB:186 (#6), Z.4:343 (#40), Z.4:345–353 (#41), MAN LMS-Z-08 (#58) – a „Teljesítve” mércéje | a hármas minimum („Minimum elvárás”) a „Teljesítve” feltétele; „Ha nagyon hiányos / alibi” → „Még nem teljesítve” | a „Teljesítve” alsó határa a tényleges, minimálisan értelmezhető beadás; a hármas szerkezet formatív; érzékeny rész passzolható; „Még nem teljesítve” csak értelmezhető tartalom nélkül | ERT-38 „a három részes ideális reflektív szerkezet legyen formatív útmutató, ne új, rejtett bukási küszöb. Az adatvédelmi szempontból szenzitív részek passzolhatók” |
| Z.4:374, :399 (#44, #46), :370 (#43), MAN LMS-Z-05 (#59) – completion | egyik Feedback-kérdés sem „Required” (üres beküldés teljesít) | az 1. kérdés „Required”, a többi kihagyható | ERT-3 „legalább egy nem érzékeny, értelmezhető Required válasz, a személyes kérdéseknél passz” |
| Z.4:359 (#42) – értékelés | (a kapueredményről nem szól) | a „Teljesítve” nem függ a feltárástól; feltárásmentes pótlási út | GYV-11 „a kapueredmény ne függjön a feltárástól” |
| Z.4:336 (#38) – beállítás (nem invariáns, átláthatóság miatt) | File submissions ON (opcionális videós út) | OFF, a videós út a feltételekig kikapcsolva | ADV-14 „A Z.4 videóopció legyen alapból kikapcsolva” |

Answer key (✅), opció, elosztó, küszöb, ponthatár, időtartam, rubrikaszint, kapu-típus (puha) és kötelező/opcionális besorolás egyik
blokkban sem változik. A Z.3 SLIDE 5 tanuló-lokálissá válik (#18), a besorolása nem (a terv nem állítja sem kötelezőnek, sem
opcionálisnak; az LMS-Z-06 három kötelező kérdése változatlan). Az 1 normál + 1 javító beadás, a két állapot (BSPEC-07), a
címkepár és a 90 napos megőrzés változatlan.

### 12.2 A QA-javítások vétótételei

A célzott QA-javítások (és a 125/125 visszaolvasás utáni ERT-26-átvezetés) közül azok, amelyek kulcsot, küszöböt, rubrikaszintet, completion-feltételt vagy kötelező/opcionális besorolást érintenek. Mindegyik a verifier által megerősített, objektív finding (a pontos előtte/utána és a bizonyíték a QA-riportok B. mellékletében), a döntés szövegrésze szerint.

| Hely | Változás | Finding (döntés) | Commit |
|---|---|---|---|
| M5.4 SLIDE 6 | a ✅ eltávolítása után megmaradt ☐ jelölők is kikerültek a beviteli elem nélküli diáról; answer key nincs | M5:QA-IMPL-1 (ERT-29) | `9764987` |
| M5 HUB:186 | a „minden sor ≥ Alapszint” alanya a rubrikasor, nem a táblázatsor | M5:QA-ERT-2 (ERT-26) | `9764987` |
| M2 KAPU, R2 | az „értékítélet” szó kikerül az R2 kritériumából: a `147f3c3` tette be, és szigorúbbá tette az R2-t a szintleírásoknál | M2:QA-ERT-1 (TERM-8) | `db724db` |
| M3 KAPU, R2 Alapszint | a cellába kerül a 2.1 szabálya: ahol a leírt helyzetben nincs feltárás vagy titoktartási ígéret, a titoktartás említésének hiánya is Alapszint | M3:QA-ERT-1 (ERT-21) | `e0d69d4` |
| M4 HUB:138 | az F-peula kiváltója a leadott, de gyenge vázlat; a be nem adott vázlat a lemaradás-szabály alá tartozik | M4:QA-ERT-1 (ERT-8) | `64a60d1` |
| M7 KAPU:48, :217 | a Q14 csak teljesen helyes válasz esetén számít a 12-es küszöbbe (a pontalapú maradvány kikerült) | M7:QA-ERT-1 (ERT-40) | `0b76212` |
| M7 KAPU:302 | a rubrika 1. szintjének szövege a négyelemű ívhez igazodik (az átvezetés regressziója) | M7:QA-ERT-4 (ERT-44) | `0b76212` |
| MAN:20, ASSIGN-M profil | „beadvány leadva és megerősített kapueredmény” → két állapot: SUBMITTED (a leadás) és CONFIRMED (külön GATE-CP-n); a §4 M1/M6/M7 sorai ehhez igazodnak, az M3-é emberi döntésig nem | CANON:QA-ERT-1 (ERT-9) | `35a9ddd` |
| PT:263 | az M7 14 itemes kapuja: ≥12/14 teljesen helyes item, darabszám-alapú, nem átszámított részpont-százalék | CANON:QA-ERT-3 (ERT-40) | `35a9ddd` |
| RA:57, negatív teszt | „11 teljesen helyes + 2 részpontos Multi-Select item, ahol a két részpont összege legalább 1 (nyers pont ≥12)” | CANON:QA-ERT-5 (ERT-40) | `35a9ddd` |
| MAN:167, kurzusteljesítés | az LMS-M0-05 csak akkor activity-kritérium, ha a fórum az ADV-6 feltételeivel megnyílt | CANON:QA-IMPL-1 (ADV-6) | `35a9ddd` |
| MAN, új LMS-M7-12 sor (PAGE-C) | az M7.2 AI-jártassági oldala saját completion-sort kap (megtekintés); az LMS-M7-02 unlockjának átkötése a build-spec gazdáé | CANON:QA-IMPL-2 (ERT-48) | `35a9ddd` |
| MAN:85, LMS-M5-07 | „a forrás szerinti felidézési interakció elvégzése” → a választott profil szerint; üres CP-re hamis „Receive a grade” completion nem állítható | CANON:QA-IMPL-4 (LMS-3) | `35a9ddd` |
| PT:183; MAN:83 (LMS-M5-05), :86 (LMS-M5-08) | „minden sor ≥ Alapszint” → „minden rubrikasor ≥ Alapszint” (a PT-ben és az LMS-M5-05-nél: „a teljes táblázat alapján”); érték, R4, szintek, completion változatlan | ERT-26 („a PT és HUB ugyanezt írja”); precedens: M5:QA-ERT-2 | `33aec89` |

### 12.3 Gépi diff-ellenőrzés (`beaea60..HEAD`, `02 Tervezet`)

- **✅-szám:** a futás 84 változott `.md` fájljából kettőben változott. (1) M0 hub 7 → 8: a többlet prózai említés („a ✅ helye és a kulcs változatlan”, M0:QA-ERT-3, ERT-11), nem kulcsjelölés. (2) M5.4 12 → 8: a SLIDE 6 önellenőrzés négy ✅-jelölése megszűnt, mert a dia pontozatlan, beviteli elem nélküli önellenőrzés lett (ERT-29: „ne legyen pontozott helyes–hibás kérdés”; ADV-4). A zárószöveg „a legtöbb állításra” → „mind a négy állításra” (ERT-29; az M5 terv vétólistáján).
- **Számok:** 21 fájlban változott szám jellegű token (küszöb, idő, pont, nap). A küszöbök és pontok a tervek vétólistáján (12.1) vagy a 12.2-ben szerepelnek. Az M1 hub „4/5” formatív célértéke a PRG-2 szerint kikerült (M1 vétólista, HUB:30, :93); az M1.A percbontása a hubban a peulafájl §3-át követi (PRG-3, M1 terv 60. blokk). A „90 nap” tokenek az ADV-6 szó szerinti mondata („a „képzés vége + 90 nap” nem automatikus jogszerű alapérték”) és már meglévő megőrzési mondatok átfogalmazott sorai: a „legfeljebb 90 nap / 90 napig” előfordulások száma az ADV-ben (7) és a Z.4-ben (2) a `beaea60` óta változatlan. A média-CSV-k és a médiamanifest „1 perc” sorai a `chore(media)` buildek kimenetei.
- **Szemantikus azonosítók és fájlnevek:** nincs átnevezés és nincs törölt fájl a futásban (a TECH-2 átnevezése a felhasználóé, X-7).
- **Tartalomvesztés:** egyetlen fájl sem lett 10%-nál rövidebb.
- **Félbehagyott szöveg:** új `TODO`/`FIXME` nincs.
- **Látható-szöveg pinek:** a `tools/approved-visible-text.json` 81 új indoklássora mind döntés- vagy finding-azonosítót nevez meg (HUM 14 döntés-ID-k, illetve `<modul>:QA-…` és `CANON:QA-…`).

## 13. A 125 döntés tételesen

Hely-rövidítések: HUB = modulhub, KAPU = kapu-értékelő, MAN = `LMS – activity manifest.md`, RA = `LMS – H5P runtime acceptance.md`, ADV = `Adatvédelem – tanulói adatok és AI.md`, GK = `Gyermekvédelem – release gate.md`, PT = `Program terv.md`, GL = Glosszárium, HUM = `Emberi jóváhagyás szükséges.md`. A sorszámok az átvezetéskori állapotra utalnak; a későbbi commitok eltolhatták őket.

| Döntés | A/F | Kategória | Implementáció (hely + commit) | Blokkok (terv → HEAD) | Tesztelés | Fennmaradó külső függőség / döntési igény | Megjegyzés |
|---|---|---|---|---|---|---|---|
| GYV-1 | F | QA-RA VÁR | M2.4:37 („senki nem figyeli folyamatosan … ne egy tanulási feladatban tedd”), M2 KAPU:203 (külön akut út az LMS-M2-05-nél) + 147f3c3/db724db | 3 blokk (M2): 2 szó szerint; 1 módosított alakban (4.1) | QA-riport M2 (147f3c3); kánoni QA: riport (bdb94ab), javítás 35a9ddd | M2:QA-BIZT-5, kiterjed-e a KAPU:24 24 órás határidejére (projektgazda, Memuna-QA) | a „mentorod azonnal bevonja” ígéret eltűnt az M2-ből; a KAPU:24 határideje változatlan |
| GYV-2 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M2.4:663 (passz + „kit vonnál be”, „teljes értékű válasz”), M2.4:665 + 147f3c3 | 4 blokk (M2): 4 szó szerint | QA-riport M2 | az M3/M4-kör Memuna- és completion-QA-ja (a döntés nevezi meg; M3:IMPL-G2-5, PED-G2-1, M4:BIZT-G2-10 nincs átvezetve); M2:QA-BIZT-4 egyenértékű demonstráció (Memuna + programvezető, értékelési felelős) | az M5 passz-részt az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban |
| GYV-3 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M4.A:397, :440 („automatikus négyszemközti … nélkül”), M3.4:593, M5.F:89 + dd64825/ce04b9c | 3 blokk (M3, M4): 3 szó szerint | QA-riport M3, M4 | helyenkénti Memuna-verdikt a 7 helyre (a döntés szerint addig él az alapértelmezés) | kulcs érintetlen |
| GYV-4 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M2 KAPU:113 és M2.4:209 (a QA-fix után előbb biztonság és 112), M2.4:659, M3.3:4/478/708–709 + 147f3c3/db724db, ce04b9c | 4 blokk (M2, M3): 0 szó szerint; 4 a QA-javítás után finomítva (db724db, e0d69d4) | QA-riport M2 (QA-BIZT-1 javítva), M3 | a számok és órák kiadáskori Memuna-ellenőrzése; a 116 000 pontosítása (GYV-14) | az M6 veszélydobozai (M6.2:783, M6.3:749, 6D/ZÁRÓ) a terv szerint szándékosan a rövid Memuna-utalásnál maradtak (GK §4.1 megengedi; a 6D/ZÁRÓ a 2026-10-05-i döntés szerint Memuna-QA alatt): a helyek, számok és órák Memuna-ellenőrzése nyitott (nem implementációs hiba) |
| GYV-5 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M0.A:94, M3.B:275, Z.A:59, M2.A (2 találat), M6.A (3 találat) + 5484b02, ce04b9c, c5bc2c4 | 9 blokk (M0, M2, M3, M6, Z): 2 szó szerint; 1 a QA-javítás után finomítva (35a9ddd); 6 módosított alakban (4.1) | QA-riport M0, M2, M3, M6; QA-riport Z | végleges létszámnorma és a megállítási protokoll tartalma (Memuna + programvezető; M0:QA-BIZT-2, M2:QA-BIZT-2, M6:QA-BIZT-4); M2.B/M2.F/M3.F besorolás | szó szerinti óvatos alapértelmezés |
| GYV-6 | A | IMPLEMENTED | M1.A, M1.B („megállhat vagy passzolhat”), M1.F, M7.A:56, M7.F:89, Z.A:56 + eb4fa6d, f6e9c6e, c5bc2c4 | 16 blokk (M1, M3, M4, M5, M7, Z): 10 szó szerint; 6 a QA-javítás után finomítva (64a60d1, 7a69b9d) | QA-riport M1, M3, M4, M5; QA-riport M7, Z | – | a szorongás-küszöb Memuna-jóváhagyása G1-szerepbizonyíték |
| GYV-7 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M5.2:317, M6.2:783 („pusztán nehéz érzés … nem jelzési ügy”), M7.F:350 + aadf41b, fbebec0, f6e9c6e | 4 blokk (M5, M6, M7): 3 szó szerint; 1 a QA-javítás után finomítva (0b76212) | QA-riport M5, M6; QA-riport M7 | az M0 csoportchat-küszöbét a Memuna külön ellenőrzi (a döntés nevezi meg, az M0-ban nincs átvezetve); M6:QA-BIZT-1/2, M7:QA-BIZT-6 (Memuna) | az M6.3:749 jelzési listájában még ott a „friss seb”; a QA emberi döntésre küldte |
| GYV-8 | F | QA-RA VÁR | Z.3:310 („akut kockázatot látok, a Memunát is azonnal bevonom”) + c5bc2c4/a0c0c83 | 1 blokk (Z): 1 szó szerint | QA-riport Z | Z:QA-BIZT-2, 112-utalás (Memuna + programvezető) | az M6-ban nincs változás |
| GYV-9 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | szándékosan nincs átvezetve (az M7 R4-ben nincs változás; csak HUM:632) | nincs terv-blokk | QA-riport M7 | a rubrikahorgony és a Q9/(C) formális jóváhagyása (Memuna + értékelési felelős; rubrikaszint: projektgazda) | – |
| GYV-10 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M7.2:25 („közvetlen tanulói AI-segéd … addig nem nyílik”) + f6e9c6e | 5 blokk (M7): 5 szó szerint | QA-riport M7 | igazolt adatkezelési és kríziskezelési út (Memuna + DPO/jogi + programvezető); CANON:QA-BIZT-3 (b) emberi döntés — kell-e és milyen szöveggel a képző által közvetített AI-út a tanulói tájékoztatóban (ADV §11) — programvezető + Moodle-adminisztrátor; vétó/QA: DPO / jogi felelős | – |
| GYV-11 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M1 KAPU:27, M3 KAPU:309, M3.4:835, Z.4:359 + eb4fa6d, ce04b9c, c5bc2c4 | 6 blokk (M1, M3, Z): 3 szó szerint; 3 a QA-javítás után finomítva (a0c0c83, e0d69d4) | QA-riport M1, M3; QA-riport Z; kánoni QA: riport (bdb94ab), javítás 35a9ddd | dokumentált Memuna-eljárás és DPO-jóváhagyott törlési/megőrzési rend; M1:QA-BIZT-5, Z:QA-BIZT-1; CANON:QA-BIZT-4 emberi döntés — „kikerül a Moodle-ből” vs GYV-11 törlési rend (Memuna + DPO) | – |
| GYV-12 | A | IMPLEMENTED | M1.3:913 (ADV §11 mondat), M2.4:665 (a biztonsági doboz a Moodle-mezőnél) + eb4fa6d/7a69b9d, 147f3c3 | 4 blokk (M1, M2): 4 szó szerint | QA-riport M1, M2; kánoni QA: riport (bdb94ab), javítás 35a9ddd | – | IMPLEMENTED a kánoni QA (35a9ddd) után |
| GYV-13 | A | IMPLEMENTED | a formula 37 fájlban 77-szer (pl. M2.4, M4.3:360, M6.2:783) + a modul-commitok | 8 blokk (M1, M2, M3, M7): 7 szó szerint; 1 a QA-javítás után finomítva (e0d69d4) | QA-riport M0–M6; QA-riport M7, Z | – | a helyek Memuna-megerősítése G1 |
| GYV-14 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3 KAPU:367/371, M3.B:76, M2.4:659 (nincs változás, M3:BIZT-G2-2 EXTERNAL) | nincs terv-blokk | QA-riport M2, M3 | kiadás előtti egyeztetés a Kék Vonal és az NMHH leírásával; formális Memuna-újranyitás | az M3 „bántalmazott vagy eltűnt gyermek ügyében 116-000”-t ír, a döntés „eltűnt gyermekek vonalá”-t; a KAPU:371 Kék Vonal-forrása a tágabb leírást támasztja alá |
| GYV-15 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3.3:546, :547, :554 („a Memuna és – ahol indokolt – a hivatalos szervek feladata”) + ce04b9c | 3 blokk (M3): 3 szó szerint | QA-riport M3 | a külső jelzés címzettjei (jogász/JOG-1 + Memuna); M3:QA-BIZT-1 | – |
| GYV-16 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3.A („csak önként vállalhatja”), M6.4 és M6.1 („nem osztotok kirekesztett … szerepet”) + ce04b9c, fbebec0 | 2 blokk (M3, M6): 1 szó szerint; 1 a QA-javítás után finomítva (e0d69d4) | QA-riport M3, M6 | Memuna szakmai döntése (a döntés nevezi meg; M3.A-nál a modulgazdával) | óvatos alapértelmezés |
| GYV-17 | A | QA-RA VÁR | M6.A:462–466 (kötelező tiltott zóna: identitás, kirekesztés, önfeltárás, „kiskorú résztvevőkkel sem”) + fbebec0/511d9e0 | 1 blokk (M6): 0 szó szerint; 1 a QA-javítás után finomítva (511d9e0) | QA-riport M6 | M6:QA-BIZT-5, a „kiskorúakra is térjen ki” tartalma (Memuna + tartalomfelelős) | a kapukvízre vonatkozó részt az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban |
| GYV-18 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | az M6 #36/#37-et az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban + fbebec0 | 2 blokk (M6): 2 szó szerint | QA-riport M6 | a 12. item új szára és kulcsa (értékelési felelős + Memuna, kulcs: projektgazda; M6:QA-BIZT-3); az M6.2-NAR-05 VO-render (VO-gazda) | – |
| GYV-19 | A | QA-RA VÁR | M2.A:362, M4.3:360 („hallgasd meg, de ne nyomozz”) + 147f3c3, dd64825 | 2 blokk (M2, M4): 2 szó szerint | QA-riport M2, M4 | M2:QA-BIZT-3 és M4:QA-BIZT-3, címzett: „képzőnek és Memunának” vagy a GK §4.1 szerint csak Memuna (Memuna) | az M2.A „képzőnek, aki bevonja a Memunát” alakú |
| GYV-20 | F | IMPLEMENTED | M2.A:225 („nincs nyilvános kiállás: fejben vagy a saját papírjukon”) + 147f3c3 | 3 blokk (M2): 2 szó szerint; 1 a QA-javítás után finomítva (db724db) | QA-riport M2 | – (a nyilvános változat csak opcionális, későbbi Memuna/DPO-mérlegelés) | a többi M2-hely állapota a „Blokkok” oszlopban (gépi blokk-nyomkövetés) |
| GYV-21 | A | QA-RA VÁR | M1.3, M1.4 (GYV-21/visszaazonosíthatóság, 1–1 találat) + eb4fa6d; az M2 #61-et az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban | 4 blokk (M1, M2): 2 szó szerint; 2 a QA-javítás után finomítva (7a69b9d, db724db) | QA-riport M1, M2; kánoni QA: riport (bdb94ab), javítás 35a9ddd | M2:QA-BIZT-7, „felismerhető részlettel sem” (Memuna + DPO) | – |
| GYV-22 | A | IMPLEMENTED | M1.1:926 („nem elvárás, és nem feltétele a jó madrihságnak … általános vagy kitalált példát”) + eb4fa6d | 1 blokk (M1): 1 szó szerint | QA-riport M1 | – | a Memuna- és lektor-QA G1 |
| GYV-23 | F | QA-RA VÁR | M0 hub:283 (csoportszintű, nem megbélyegző korrekció; egyéni utánkövetés csak DPO-jóváhagyással) + 5484b02 | 1 blokk (M0): 1 szó szerint | QA-riport M0 | M0:QA-BIZT-3 (DPO + LMS-gazda), M0:QA-NYELV-3 (programvezető + Memuna) | – |
| ADV-1 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | „rendszergazdája is hozzáférhet” 12 fájlban (M1.4, M2 KAPU, M2.4, M3.4, M4.x, M5.4, Z.4) + modul-commitok és bdb94ab | 13 blokk (M1, M2, M5, Z): 4 szó szerint; 1 a QA-javítás után finomítva (35a9ddd); 8 módosított alakban (4.1) | QA-riport M1–M5; QA-riport Z; kánoni QA: riport (bdb94ab), javítás 35a9ddd | staging role-matrix (LMS-gazda) + DPO; BIZT-5 csoportszűkítés; CANON:QA-BIZT-1 emberi döntés — kiterjed-e a csoportszűkítés a H5P-C, QUIZ, GATE-CP nézetre (projektgazda; DPO-vétó); a staging role-matrix utáni RBAC-igazítás | a „csak mentorod” ígéret a role-matrixig változatlan |
| ADV-2 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | Adatvédelem:247, M1.F, M3.F, M7.F (aggregált/hiánylista) + eb4fa6d, ce04b9c, f6e9c6e | 9 blokk (M1, M3, M7): 7 szó szerint; 1 a QA-javítás után finomítva (7a69b9d); 1 módosított alakban (4.1) | QA-riport M1, M3; QA-riport M7; kánoni QA: riport (bdb94ab), javítás 35a9ddd | az F-peula szereposztás és a vészhozzáférés dokumentálása, valós csoport-hozzáférési teszt (DPO + LMS-gazda, programvezető) | – |
| ADV-3 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | ADV-3-hivatkozás M4.1, M3.1, M3.2, M7.2, M7.B, Z.3 + ce04b9c, dd64825, f6e9c6e, c5bc2c4 | 42 blokk (M3, M4, M7, Z): 38 szó szerint; 3 a QA-javítás után finomítva (35a9ddd, 64a60d1, a0c0c83); 1 módosított alakban (4.1) | QA-riport M3, M4; QA-riport M7, Z; kánoni QA: riport (bdb94ab), javítás 35a9ddd | RT-P0-24 (LMS-gazda), DPO adatkör-aláírás (M4:BIZT-G1-2), az M4.1 ILO 2 szövege (az IV-kérdés opcionális lett; modulgazda / projektgazda, X-5), VO_PACK; CANON:QA-IMPL-7 (b) emberi döntés (X-11) — a Z.3 5. dia besorolása (projektgazda) | – |
| ADV-4 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | ADV-4-hivatkozás M1.1, M3.4, M5.1, M5.4, M6.1–6.3, Z.1–Z.3 + modul-commitok | 10 blokk (M1, M3, M5, M6, Z): 7 szó szerint; 3 a QA-javítás után finomítva (511d9e0) | QA-riport M1, M3, M5, M6; QA-riport Z | a tárolásmentes technika célverziós visszaolvasása (H5P-verzió, próbálkozás-riport, xAPI, mentett állapot, szerepkörök; RA 24) – LMS-gazda + DPO, M3-nál Memuna | – |
| ADV-5 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M2 KAPU (1 ADV-5-hivatkozás) + 147f3c3; az M2.3 és az M7 blokkokat az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban | 11 blokk (M2, M7): 11 szó szerint | QA-riport M2; QA-riport M7; kánoni QA: riport (bdb94ab), javítás 35a9ddd | GDPR 9. cikk szerinti minősítés (jogi/DPO); M7 R1; M2:QA-ERT-2 | – |
| ADV-6 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | ADV-6-hivatkozás M0.4 (4), M0 hub (2), M0.A (1) + 5484b02 | 19 blokk (M0): 16 szó szerint; 3 a QA-javítás után finomítva (35a9ddd, a2445ff) | QA-riport M0; kánoni QA: riport (bdb94ab), javítás 35a9ddd | cél, hozzáférési kör, DPO által elfogadott megőrzés, tájékoztató (DPO/jogi); M0:QA-ERT-1 (build-spec gazda + LMS-gazda) | a fórum zárva maradásának szövegét szó szerint nem idéztem |
| ADV-7 | A | QA-RA VÁR | M1.A (2), M2.A, Z.A (fotó/kifüggesztés-szabály) + eb4fa6d, 147f3c3, c5bc2c4 | 10 blokk (M1, M2, M4, M5, Z): 10 szó szerint | QA-riport M1, M2, M4, M5; QA-riport Z; kánoni QA: riport (bdb94ab), javítás 35a9ddd | M4:QA-BIZT-5 (DPO + Memuna), Z:QA-BIZT-3 (DPO/jogi) | az M4/M5 blokkokat az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban |
| ADV-8 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M6.F („nem anonim/névtelen”, 1 találat) + fbebec0; az M1.F, M2, M5 blokkokat az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban | 8 blokk (M1, M2, M5, M6): 5 szó szerint; 3 a QA-javítás után finomítva (511d9e0, 9764987) | QA-riport M1, M2, M5, M6 | a mentori adatkör/megőrzési sor kijelölése (DPO, ADV-E2) | – |
| ADV-9 | A | IMPLEMENTED | M4.4, M4.B, M5.4, M5 KAPU:283, M6.1, M6 KAPU, M6.B (korosztály/létszám, nincs diagnózis) + dd64825, aadf41b, fbebec0 | 11 blokk (M4, M5, M6): 9 szó szerint; 2 a QA-javítás után finomítva (35a9ddd, 9764987) | QA-riport M4, M5, M6; kánoni QA: riport (bdb94ab), javítás 35a9ddd | – | IMPLEMENTED a kánoni QA (35a9ddd) után |
| ADV-10 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | ADV-10 M2 hub:203, M3.4:801, M5.4:204/:280, M7.4:820, M7 hub:86/96/417 + modul-commitok | 11 blokk (M2, M3, M4, M5, M6, M7): 8 szó szerint; 3 a QA-javítás után finomítva (35a9ddd, 511d9e0, 64a60d1) | QA-riport M2–M6; QA-riport M7 | külső eszköz csak a szolgáltató, adatkör, megőrzés és harmadik fél ismerete után (DPO/jogi); szervezeti fiók (programvezető); M7 (c) megőrzési sor | – |
| ADV-11 | F | QA-RA VÁR | jelszó/munkapéldány-szabály 11 fájlban (M0.A, M1.F–M7.F) + modul-commitok | 18 blokk (M0, M1, M2, M3, M4, M5, M6, M7): 5 szó szerint; 4 a QA-javítás után finomítva (511d9e0, 64a60d1, 9764987); 9 módosított alakban (4.1) | QA-riport M0–M6; QA-riport M7; kánoni QA: riport (bdb94ab), javítás 35a9ddd | M0:QA-BIZT-4, kiterjed-e a nem F-peulás tartalék eszközre (projektgazda; QA: LMS-gazda + DPO); a kivételhez LMS + DPO teszt (opcionális) | a „személyes munkapéldányt nem hoz létre” a „tilos” szónak felel meg, nem eltérés |
| ADV-12 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M7.2 (2), M7.4 (1) store=false/naplózás + f6e9c6e, bdb94ab | 3 blokk (M7): 0 szó szerint; 3 a QA-javítás után finomítva (0b76212, 35a9ddd) | QA-riport M7; kánoni QA: riport (bdb94ab), javítás 35a9ddd | provider-, proxy-, hibalog-, backup- és admincsatorna-felmérés, megőrzés (DPO/jogi); CANON:QA-BIZT-5 emberi döntés — az AI-végpont metaadatainak jogalapja és megőrzése az ADV §3-ban (DPO) | – |
| ADV-13 | A | IMPLEMENTED | a „2–3 konkrét szabály” KPI az M2-ben 0 találat (kikerült; 12. blokk) + 147f3c3 | 1 blokk (M2): 1 szó szerint | QA-riport M2 | – | DPO QA = G |
| ADV-14 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | Z.4:303 („videós út … alapból kikapcsol[va]”) + c5bc2c4 | 14 blokk (Z): 10 szó szerint; 2 a QA-javítás után finomítva (a0c0c83); 2 módosított alakban (4.1) | QA-riport Z; kánoni QA: riport (bdb94ab), javítás 35a9ddd | hozzájárulási folyamat, törlési út, feltöltés előtti ellenőrzés, kiskorú jogalapja (DPO + jogász) | – |
| ADV-15 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | Z.4:398 („Show analysis page”, „Enable notification of submissions”) + c5bc2c4 | 3 blokk (Z): 1 szó szerint; 1 a QA-javítás után finomítva (a0c0c83); 1 módosított alakban (4.1) | QA-riport Z; kánoni QA: riport (bdb94ab), javítás 35a9ddd | az anonim mód és a back-end hozzáférés tényleges működésének vizsgálata (runtime, LMS-gazda) | – |
| JOG-1 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3.3:484, M3 KAPU:360–364, M3 hub:41 (Gyvt. 17. §/Btk. 209/A); általános „három munkanap” állítás 0 találat + ce04b9c | 1 blokk (M3): 1 szó szerint | QA-riport M3 | a Gyvt. 17. § címzettjei és határidői (jogász); Memuna; nyilvántartás helye (projektgazda) | – |
| TERM-1 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | szándékosan nincs átvezetve; „dugma isit vagy” még az M0.4-ben és az M0 hubban (1–1) | nincs terv-blokk | QA-riport M0, M2, M3 | terminológiagazda (ken-vezető/mozgalmi felelős) megerősítése; átnevezés (TECH2) a felhasználótól | – |
| TERM-2 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M1.4:472, :529 („S – Helyzet”) + eb4fa6d | 10 blokk (M1): 10 szó szerint | QA-riport M1 | NAR-02 VO-render (VO_PACK, VO-gazda) | a szöveges rész kész, a hangrész szándékosan nincs átvezetve |
| TERM-3 | A | IMPLEMENTED | „transzparens” az M2-ben 0 találat + 147f3c3 | 2 blokk (M2): 2 szó szerint | QA-riport M2 | – | Memuna vétó = G |
| TERM-4 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3.4:1, :9; M3 HUB:122, :288; M3.B:151; M3.F:16 + ce04b9c, e0d69d4 | 10 blokk (M3): 10 szó szerint | M3 QA-riport (a verifier a QA-NYELV-9-et elvetette: a linkek frissek) | a fájlnév-átnevezést a felhasználó futtatja (git mv + linkek); a végleges szerzői címet az M3 modulgazdája adja | a tanulói cím mindenütt „Mit tegyél, mit ne tegyél madrihként?”, de a fájlnév még „M3.4 – Do és Don’t madrihként…”. |
| TERM-5 | A | IMPLEMENTED | M3.4:692, :699, :787, :796; MAN:66 („M3 – Helyzetleírás”) + ce04b9c | 6 blokk (M3): 6 szó szerint | M3 QA-riport + verifier | – | a kód (LMS-M3-05) nem változott. |
| TERM-6 | F | IMPLEMENTED | M3.A:413 („kvuca – év eleje”), :433 („Leviatán – év eleji kvuca”) + ce04b9c, e0d69d4 | 3 blokk (M3): 2 szó szerint; 1 a QA-javítás után finomítva (e0d69d4) | M3 QA (QA-NYELV-5 javítva) | – | az óvatos alapértelmezés él; „stáb” csak modulgazdai igazolással térhet vissza, ez vétó, nem feltétel. |
| TERM-7 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M2 HUB:33 („nem pontozott, reflektív cél”) + 147f3c3 | 1 blokk (M2): 1 szó szerint | M2 QA-riport | az M5-részben választani kell a formatív demonstráció és a célmegfogalmazás szűkítése között (M5 modulgazda + értékelési felelős) | az M5 HUB:18, :33 nincs átvezetve (a terv szerint szándékosan, EXTERNAL). |
| TERM-8 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M2 KAPU:180 + 147f3c3, db724db | 1 blokk (M2): 0 szó szerint; 1 a QA-javítás után finomítva (db724db) | M2 QA (QA-ERT-1 javítva) | a top 3-ban hiányzó someres értékhez előre rögzített támogatás új tartalom, PRG-4 csomag (/course-develop) | a világnézeti vallomás tilalma és az Ideológiai Kézikönyvhöz kötés benne van. |
| ERT-1 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | MAN:16; RA:72; M0.1:13; M4.3:20; M6.1:9 + 5484b02, bdb94ab | 26 blokk (M0, M3, M4, M5, M6, M7, Z): 16 szó szerint; 5 a QA-javítás után finomítva (511d9e0, 9764987, a0c0c83); 5 módosított alakban (4.1) | M0 (QA-IMPL-1), M6 (QA-IMPL-1), Z (QA-IMPL-2) QA-riport; kánoni QA nincs; kánoni QA: riport (bdb94ab), javítás 35a9ddd | RA 9 negatív teszt, és soronként igazolni, hogy a CP-nek van összefoglaló diája (LMS-gazda / build-spec gazda) | a döntés maga írja elő a negatív tesztet. |
| ERT-2 | A | IMPLEMENTED | MAN:16 (általános szabály), MAN:39 (M0_L1); M0.1:13 + 5484b02, bdb94ab | 3 blokk (M0): 3 szó szerint | M0, M6, M7, Z QA-riport; kánoni QA: riport (bdb94ab), javítás 35a9ddd | – (ha egy CP-nek a célverzión nincs összefoglaló diája, a build-spec gazda rögzíti a legitim completion-alapot: a kánonban szabályként rögzítve) | IMPLEMENTED a kánoni QA (35a9ddd) után |
| ERT-3 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M5 HUB:187; Z.4:374, :400 + aadf41b, c5bc2c4 | 4 blokk (M5, Z): 4 szó szerint | M5 és Z QA-riport | a „kiürítés” staging-tesztje (RA 16); nyitott Z:QA-IMPL-3 a „kiürítés” jelentéséről (build-spec gazda) | – |
| ERT-4 | F | IMPLEMENTED | M1 KAPU:28, :132, :314; M2 KAPU:56; M2 HUB:179 + eb4fa6d, 147f3c3 | 6 blokk (M1, M2): 6 szó szerint | M1 QA (QA-ERT-7), M2 QA | – (DPO csak akkor, ha mégis activity készül) | az óvatos alapértelmezés (szerzői itempool) teljes. |
| ERT-5 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3 KAPU:35; M7 KAPU:51, :415; MAN:18 + ce04b9c, f6e9c6e | 4 blokk (M3, M7): 3 szó szerint; 1 a QA-javítás után finomítva (e0d69d4) | M3 QA (QA-ERT-2), M7 QA-riport | a Review options célverziós visszaolvasása (LMS-gazda) | az M3 KAPU az itemenkénti általános visszajelzést is visszatartja, az M7 KAPU:51 nem; a fő session visszaolvasta: az M7 itemek „Visszajelzés” szövegei közlik a kulcsot (pl. KAPU:72, :83), ezért az általános visszajelzést is a javító próbálkozás utánra kell állítani; a KAPU:51 ezt a „helyes választ … csak a javító próbálkozás lezárása után” szabállyal fedi, de külön nem nevezi meg (nyitott megfigyelés, 8. szakasz). |
| ERT-6 | A | IMPLEMENTED | M5 HUB:180; M5 KAPU:24; M6 KAPU:74, :440; MAN:92 + aadf41b, fbebec0, bdb94ab | 8 blokk (M5, M6): 5 szó szerint; 3 a QA-javítás után finomítva (35a9ddd, 9764987) | M5 és M6 QA-riport; kánoni QA: riport (bdb94ab), javítás 35a9ddd | – (a Moodle-beállítás rögzítése az LMS-gazda build-feladata) | IMPLEMENTED a kánoni QA (35a9ddd) után |
| ERT-7 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | az M5-ben már korábban megvolt; M0/M3/M6 → PRG4 | nincs terv-blokk | modul-QA-riportok | itemek újraírása PRG-4 csomagban (szerző + értékelési felelős + Memuna) | az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban (szándékosan nincs szövegváltozás). |
| ERT-8 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M2-ben 17 „küszöbe alatt” hely; Gl:188, :194; PT:242, :286; M4 HUB:138 + 147f3c3, dd64825, bdb94ab | 31 blokk (M2, M4): 26 szó szerint; 4 a QA-javítás után finomítva (35a9ddd, 64a60d1); 1 módosított alakban (4.1) | M2 és M4 QA (M4:QA-ERT-1, -4) | az értékelés helyének és hozzáférésének dokumentálása (build-spec gazda + DPO; M4:ERT-G2-4 EXTERNAL) | – |
| ERT-9 | A | QA-RA VÁR | M1 KAPU:309; MAN:50, :83, :91, :101, :103 + eb4fa6d, fbebec0, bdb94ab | 7 blokk (M1, M5, M6, M7): 6 szó szerint; 1 a QA-javítás után finomítva (35a9ddd) | QA-riport M1; kánoni QA: riport (bdb94ab), javítás 35a9ddd | –; kánoni QA: CANON:QA-ERT-2 emberi döntés — az LMS-M3-05 SUBMITTED completionje és a kapukvíz-ablak (build-spec gazda; QA: értékelési felelős); a többi ASSIGN-M sor és a profil javítva (35a9ddd) | a kánoni QA-javítás (35a9ddd) a MAN:20 és a §4 M1/M6/M7 sorát átvezette; az M3 sora emberi döntésig változatlan |
| ERT-10 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3 KAPU:78 + ce04b9c | 1 blokk (M3): 1 szó szerint | M3 QA-riport | küszöbhatás-vizsgálat (értékelési felelős) és Memuna szakmai állásfoglalás | az ITEM 10 a döntés szerint addig nem kritikus; a 2/4/7/9 és a ≥10/12 változatlan. |
| ERT-11 | A | IMPLEMENTED | M0 HUB:222–230, :255, :261 + 5484b02, a2445ff | 3 blokk (M0): 3 szó szerint | M0 QA (QA-ERT-3, HUB:181) | – | a ✅ és a kulcs nem változott. |
| ERT-12 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | MAN (1 ERT-12-találat) + eb4fa6d | 6 blokk (M1): 6 szó szerint | M1 QA (QA-BIZT-1) | a NAR-05 VO fix pack; DPO-vétó | az M1.3:885-öt a QA-riportból; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| ERT-13 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | „2–3 mondat” 16 helyen 7 M1-fájlban + eb4fa6d | 9 blokk (M1): 8 szó szerint; 1 a QA-javítás után finomítva (7a69b9d) | M1 QA (QA-ERT-2, QA-NYELV-5) | a NAR-03 hang (VO-render) | az M1.4:450 „nem pontozzuk” megjegyzését csak a QA-riportból ismerem. |
| ERT-14 | A | QA-RA VÁR | M1 KAPU:305 + eb4fa6d | 2 blokk (M1): 2 szó szerint | M1 QA-riport | M1:QA-ERT-3, a rubrika jóváhagyása az értékelési felelőstől (bizonyíték-kapu) | – |
| ERT-15 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M1 KAPU:83; M1.4:628 + eb4fa6d, 7a69b9d | 1 blokk (M1): 1 szó szerint | M1 QA (QA-ERT-5) | a két horgony példáinak egységesítése és kalibrációja (értékelési felelős + módszertani lektor) | a QA-ERT-4 elvetése maga mondja ki, hogy a kalibráció nyitott. |
| ERT-16 | F | IMPLEMENTED | M1.4:490, :592 + eb4fa6d, 7a69b9d | 3 blokk (M1): 3 szó szerint | M1 QA (QA-ERT-6) | – | eltérő konstruktumot csak kivételként hagyhat jóvá az értékelési felelős. |
| ERT-17 | A | IMPLEMENTED | M1 KAPU:79 („A kapcsolat megtartása ennek a pedagógiai oka, nem külön pontozott szempont.”) + eb4fa6d | 1 blokk (M1): 1 szó szerint | M1 QA-riport (eb4fa6d); fő session visszaolvasás | – | a fő session ellenőrizte a fájlban (a „megtartható” szó helyett a magyarázó mondat áll) |
| ERT-18 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M2.4:55 („követésmentes”); M2 HUB:183; MAN:16 + 147f3c3 | 3 blokk (M2): 3 szó szerint | M2 QA-riport | runtime-próba a cél-Moodle-ön (LMS-gazda); a tárolásról a DPO dönt | a döntés szerint runtime-próba nélkül nem kész. |
| ERT-19 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | szándékosan nincs (NO_CHANGE) | nincs terv-blokk | – | a módosított követelményt a modulgazda és az értékelési felelős írja alá | – |
| ERT-20 | F | IMPLEMENTED | M2 hub:245 („a stáb a szabad szöveges válaszokat programanalitikai célból nem olvassa újra, és ehhez nincs külön mutató”) + 147f3c3 | az ADV-13 blokkjában (M2#12), szó szerint a HEAD-en | M2 QA-riport (147f3c3); fő session visszaolvasás | – (ha a DPO később engedélyezné a rendszeres olvasást, a programvezető rögzít ≥2-es formatív célértéket) | az óvatos alapértelmezés: a „2 vagy 3” mutató megszűnt |
| ERT-21 | F | QA-RA VÁR | M3 KAPU:318, :324, :325; M3.4:837; M3.B:513 + ce04b9c, e0d69d4 | 5 blokk (M3): 3 szó szerint; 2 a QA-javítás után finomítva (e0d69d4) | M3 QA (QA-ERT-1, QA-NYELV-2, -3) | M3:QA-BIZT-2 (Memuna + értékelési felelős) | – |
| ERT-22 | A | QA-RA VÁR | M3 KAPU:324 (R1), :327 (R4) + ce04b9c | 1 blokk (M3): 1 szó szerint | M3 QA-riport | az értékelési felelős és a Memuna ítélete a befogadó sorról | az életszerűség az R1-be került; az R1 a rubrika szóhasználatában nem blokkoló, de a „minden sor ≥1” szabály miatt (KAPU:331–332) az irreális, de biztonságos válasz így is bukik; a terv 1. megjegyzése ezt ítéletként jelezte, a QA nem zárta le. |
| ERT-23 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3.2:666 + ce04b9c | 1 blokk (M3): 1 szó szerint | M3 QA-riport | itemenkénti validálás (M3 modulgazda + értékelési felelős) | a kulcs addig változatlan. |
| ERT-24 | F | IMPLEMENTED | M4 HUB:128 („összesített téma-visszajelzés”) + dd64825, 64a60d1 | 1 blokk (M4): 0 szó szerint; 1 a QA-javítás után finomítva (64a60d1) | M4 QA (QA-NYELV-4) | – (a programvezető csak akkor kell, ha egyéni jelzést kér) | – |
| ERT-25 | F | IMPLEMENTED | M4.3:542 (K3 szár: „új vita nyitása nélkül ellenőrizni, hogy a kvuca érti-e, mi volt a mai peula célja”); ✅ változatlan + dd64825 | 2 blokk (M4): 2 szó szerint | M4 QA-riport (dd64825); fő session visszaolvasás | – (✅-változás csak külön lektori és projektgazdai döntéssel; nem kellett) | a döntés első, preferált útja |
| ERT-26 | A | QA-RA VÁR | M5 KAPU:288 + aadf41b, 9764987; PT:183, MAN:83, :86 („minden rubrikasor ≥ Alapszint”, a teljes táblázat alapján) + 33aec89 | 7 blokk (M5): 6 szó szerint; 1 a QA-javítás után finomítva (9764987) | M5 QA (QA-ERT-2, QA-NYELV-4); a kánoni részre célzott értékelési ellenőrzés (33aec89): nincs finding | M5:QA-ERT-1 kalibráció (értékelési felelős; QA: módszertani lektor) | a PT- és manifest-rész kánoni blokk nélkül maradt; a 125/125 visszaolvasás után átvezetve (33aec89) |
| ERT-27 | A | IMPLEMENTED | M5 KAPU:295–300 (az R4 nem szűkül a felidézésre/elosztott gyakorlásra; a terv 20–21. blokkja) + aadf41b | 2 blokk (M5): 2 szó szerint | M5 QA-riport (aadf41b); fő session visszaolvasás | – | – |
| ERT-28 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | nincs átvezetve: az M5 terv 22–24. blokkja (M5.2 SLIDE 8 ✅-opció szövege, HUB:207, KAPU:312) szándékosan kimaradt az aadf41b-ből; a régi szöveg áll | 3 blokk (M5): 0 szó szerint; 3 szándékosan nincs alkalmazva (M5#22, M5#23, M5#24) | M5 QA-riport (aadf41b); blokk-nyomkövetés: a 3 blokk OLD-szövege a HEAD-en | új item-döntés (M5 szerzője + értékelési felelős) | a döntés sorrendje („feladat–kvuca–módszer–cél”) eltér a tanított lánctól (feladat → cél → kvuca → módszer, M5.2 SLIDE 7); a döntés szerint ilyenkor „explicit új itemdöntés” kell, nem kozmetikai szövegezés |
| ERT-29 | A | IMPLEMENTED | M5.4:9, :247 + aadf41b, 9764987 | 10 blokk (M5): 6 szó szerint; 4 a QA-javítás után finomítva (9764987) | M5 QA (QA-IMPL-1); kánoni QA: riport (bdb94ab), javítás 35a9ddd | – (célverziós visszaolvasás: RA 9, 24 – G3) | IMPLEMENTED a kánoni QA (35a9ddd) után |
| ERT-30 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | nincs átvezetve (EXTERNAL) | nincs terv-blokk | – | a C mondat jóváhagyása (szakmai szerző / értékelési felelős + modulgazda) | a ✅ C változatlan. |
| ERT-31 | A | IMPLEMENTED | M6 KAPU:412 + fbebec0, 511d9e0 | 3 blokk (M6): 3 szó szerint | M6 QA (QA-ERT-1) | – | – |
| ERT-32 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | szándékosan nincs | nincs terv-blokk | – | kalibráció (értékelési felelős + Memuna); a rubrikaszint a projektgazdáé | – |
| ERT-33 | A | IMPLEMENTED | M6 HUB:218; M6 KAPU:390; PT:288 + fbebec0, bdb94ab | 6 blokk (M6): 5 szó szerint; 1 a QA-javítás után finomítva (511d9e0) | M6 QA (QA-NYELV-9); kánoni QA: riport (bdb94ab), javítás 35a9ddd | – | IMPLEMENTED a kánoni QA (35a9ddd) után |
| ERT-34 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M6 KAPU:60 + fbebec0 | 1 blokk (M6): 1 szó szerint | M6 QA-riport | új Kivsza-item és validálása (értékelési felelős, PRG-4) | az óvatos alapértelmezés (nem hirdetjük teljes korosztályi lefedettségűnek) benne van. |
| ERT-35 | A | IMPLEMENTED | M6.4:961; M6 KAPU:165 + fbebec0, 511d9e0 | 2 blokk (M6): 0 szó szerint; 2 a QA-javítás után finomítva (511d9e0) | M6 QA (QA-NYELV-1) | – | – |
| ERT-36 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | szándékosan nincs (PRG4) | nincs terv-blokk | M6 QA (QA-BIZT-3) | GYV-18 döntés és M6:QA-BIZT-3 (értékelési felelős + Memuna); PRG-4 | az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| ERT-37 | A | IMPLEMENTED | M6.B:261, :348 („önállóan véglegesít”) + fbebec0 | 2 blokk (M6): 2 szó szerint | M6 QA-riport | – | – |
| ERT-38 | A | QA-RA VÁR | Z.4:329, :343, :347; Z HUB:185 + c5bc2c4, QA-fix a0c0c83 | 6 blokk (Z): 5 szó szerint; 1 szándékosan nincs alkalmazva (Z#58) | QA-riport Z (Z:QA-NYELV-1 = ERT-1, Z:QA-ERT-2 emberi döntés) | értékelési felelős (+ DPO a passz jelzéséhez): szakaszonkénti vagy egész beadásra szóló „Teljesítve”-mérce | a Z.4:343 („a három szakaszban”) és a :347 („ha egy eleme hiányzik … akkor is Teljesítve”) közti feszültség a nyitott döntés tárgya. |
| ERT-39 | A | IMPLEMENTED | Z HUB:197; Z.4:283; Z.4:402 (Z:QA-ERT-3 javítva); MAN:165 a Z.A-t nem sorolja + c5bc2c4, a0c0c83 | 2 blokk (Z): 2 szó szerint | QA-riport Z (nincs nyitott ERT-39 tétel); kánoni QA: riport (bdb94ab), javítás 35a9ddd (CANON:QA-IMPL-5: a MAN LMS-Z-04 és a Z.A-hoz kötött nyitás jelenléti feltétel nélkül) | – | – |
| ERT-40 | F | QA-RA VÁR | M7 KAPU:48, :53, :217 (QA-fix: „12-es küszöbbe számít”), :414; MAN:101–102 (kánoni kör) + f6e9c6e, 0b76212, bdb94ab | 16 blokk (M7): 14 szó szerint; 2 a QA-javítás után finomítva (0b76212, 35a9ddd) | QA-riport M7 (M7:QA-ERT-1 RÉSZBEN) | értékelési felelős: a kézi megerősítés menete eltérő Highest grade esetén; a minden-vagy-semmi kérdéstípus validálása: LMS-gazda (X-4) | az óvatos alapértelmezés (kézi ellenőrzés, a „Grade to pass = 12” önmagában nem elég, 11 + 2 negatív eset) a fájlban van; a kánoni QA a RA 8 negatív tesztjét pontosította (nyers ≥12, 35a9ddd) |
| ERT-41 | A | IMPLEMENTED | M7 KAPU:260 (QA-fix: „a madrih”), :263, :426, :427; MAN:103 (kánoni 39. blokk) + f6e9c6e, 0b76212, bdb94ab | 6 blokk (M7): 4 szó szerint; 2 a QA-javítás után finomítva (0b76212, 35a9ddd) | QA-riport M7 (K8 javítva); kánoni QA: riport (bdb94ab), javítás 35a9ddd | – | IMPLEMENTED a kánoni QA (35a9ddd) után |
| ERT-42 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | nincs változás; M7 KAPU:356–362 (R8) a régi szöveg (f6e9c6e: NO_CHANGE) | nincs terv-blokk | – | értékelési felelős + DPO formális döntése a rubrikáról és a kapuhatásról | az R8 0. szintje (:360) ma is „AI-másolat … és/vagy beazonosítható hanih-adat” együtt. A szétválasztás rubrikaváltozás, a döntés szerint formális döntéshez kötött. |
| ERT-43 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | nincs változás; M7 KAPU:279 (R1 2. szint: „mérhető jelet VAGY időkeretet”) | nincs terv-blokk | – | projektgazdai jóváhagyás + előzetes tanulói tájékoztató (értékelési felelős) | a döntés kifejezetten feltételhez köti a hatálybalépést. |
| ERT-44 | F | IMPLEMENTED | M7 KAPU:297 („Mit mér”), :302 (QA-fix: „egyes elemei”), :303 + f6e9c6e, 0b76212 | 2 blokk (M7): 1 szó szerint; 1 a QA-javítás után finomítva (0b76212) | QA-riport M7 (M7:QA-ERT-4 javítva) | – | – |
| ERT-45 | A | IMPLEMENTED | M7 KAPU:211, :350 („a 45 perc csak példa”); M7.2:709 + f6e9c6e | 3 blokk (M7): 3 szó szerint | M7 QA (nincs nyitott tétel) | – | – |
| ERT-46 | F | IMPLEMENTED | M7.1:8, :324, :333 (pontozatlan, ERT-46), :349 (QA-fix: IMPL-1) + f6e9c6e, 0b76212 | 9 blokk (M7): 7 szó szerint; 2 a QA-javítás után finomítva (0b76212) | QA-riport M7 (M7:QA-IMPL-1 javítva) | – | a pontozott (b) ág csak RA-igazolás után nyílna, de ez nem az alapértelmezés része. |
| ERT-47 | A | IMPLEMENTED | M7 KAPU:385 ((a)/(b) alpont) + f6e9c6e | 1 blokk (M7): 1 szó szerint | QA-riport M7 | – | a Memuna-ellenőrzés G1–G8. |
| ERT-48 | A | IMPLEMENTED | M7.2:9, :88, :131; MAN:96 (kánoni 58. blokk) + f6e9c6e, bdb94ab | 4 blokk (M7): 3 szó szerint; 1 a QA-javítás után finomítva (35a9ddd) | QA-riport M7; kánoni QA: riport (bdb94ab), javítás 35a9ddd | – | IMPLEMENTED a kánoni QA (35a9ddd) után |
| ERT-49 | A | IMPLEMENTED | M7 KAPU:386; az „eltérő létszám” az M7-ben sehol nem maradt + f6e9c6e | 1 blokk (M7): 1 szó szerint | QA-riport M7 | – | – |
| ERT-50 | A | IMPLEMENTED | M7.4:74, :698, :776, :817; M7 KAPU:351 + f6e9c6e | 6 blokk (M7): 6 szó szerint | QA-riport M7 | – | az M7-ben nem maradt „min. 3–4”. Az M5-beli „3–4 soros” más tábla. |
| PRG-1 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M0.A:153, :155 (blokkcímkék) + 5484b02, a2445ff | 5 blokk (M0, M4): 5 szó szerint | M0 QA-riport | tételes vágási terv modulonként (modulgazdák; M3.B-nél a Memuna bevonásával); az M5.1 részidőinek újrabecslése (modulgazda); vétó: programvezető | az M5.1:7, :34, :657 ma is „15–20 perc”. |
| PRG-2 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M1 HUB:30, :97; M6 HUB:53; M7 HUB:152 + eb4fa6d, fbebec0, f6e9c6e | 24 blokk (M1, M3, M4, M6, M7, Z): 22 szó szerint; 2 a QA-javítás után finomítva (511d9e0) | M1/M6 QA-riport, M7 verdiktek | az M5-rész (M5:PED-G1-10, TERM-7) EXTERNAL | az M3-, M4- és Z-rész az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| PRG-3 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M7 HUB:207; M7.B:18; M2 HUB:129; M1 HUB (a régi M1.A-percbontás eltűnt) + f6e9c6e, 147f3c3, eb4fa6d | 25 blokk (M1, M2, M3, M7): 25 szó szerint | M1/M2 QA-riport, M7 verdiktek | az M1-poszter rész (M1:IMPL-G3-5): modulgazda + médiafelelős; PRG-4-jelölés opciója: modulgazda | az M3- és M4-BUILD-rész az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| PRG-4 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | nincs (minden modulban PRG4) | nincs terv-blokk | – | `/course-develop` csomag (a felhasználó indítja, X-8); a csomagterv a projektgazdáé; QA: Memuna, értékelési felelős | ismert, nem indult. |
| PRG-5 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M1.F:66 (hiányzási út, HUM-SAFE-02) + eb4fa6d | 3 blokk (M1, M3, M5): 2 szó szerint; 1 a QA-javítás után finomítva (e0d69d4) | M1 QA-riport | 1–5 fős változatok (PRG-4, modulgazda); kapacitás és pótlási felelős (programvezető) | az M3- és M5-hiányzási út az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| PRG-6 | F | IMPLEMENTED | M7 KAPU:27; M7 HUB:383; M7.4:703 („indokolt esetben”); Z.4:339; MAN:222 (M0, kánoni), :252 (Z, kánoni), :102 + f6e9c6e, 0b76212, c5bc2c4, a0c0c83, bdb94ab | 15 blokk (M0, M7, Z): 12 szó szerint; 3 a QA-javítás után finomítva (0b76212, a0c0c83) | QA-riport M7 (K1 javítva); kánoni QA: riport (bdb94ab), javítás 35a9ddd | – (konkrét dátum csak a tényleges naptárból; a Z.3:217 és a Z hub:95 javítva: a0c0c83) | IMPLEMENTED a kánoni QA (35a9ddd) után |
| PRG-7 | A | IMPLEMENTED | M5 HUB:208; M6 HUB:242, :247 + aadf41b, fbebec0 | 3 blokk (M5, M6): 3 szó szerint | M5/M6 QA-riport | – | – |
| PRG-8 | A | IMPLEMENTED | MAN:120, :121 („Peulák” leíróelem, F-peula-szakasz, csak az új verzió) + bdb94ab | 2 blokk (M0, M1): 0 szó szerint; 2 módosított alakban (4.1) | kánoni QA: riport (bdb94ab), javítás 35a9ddd | – | IMPLEMENTED a kánoni QA (35a9ddd) után |
| PRG-9 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M1.2:803 (csak húzásmentes út); M1 HUB:97; M3.3: az ILL-01–04 assetek kikerültek + eb4fa6d, ce04b9c | 22 blokk (M1, M3): 22 szó szerint | M1/M3 QA-riport | b) M2.1 „CP-ben integrált” forma: build-/LMS-gazda + M2 modulgazda (M2:IMPL-G1-3 EXTERNAL; az M2.1:8 ma „különálló, nem követett elem”) | – |
| PRG-10 | A | IMPLEMENTED | M4.B:278 (SBI opcionális, Megfigyelés → Hatás → Következő lépés), M4 hub (kötelező szerkezet); M5 KAPU:283 (kitalált kvucaprofil egyenértékű); ADV §3 M5/M6 (kánon) + dd64825, aadf41b, bdb94ab | 5 blokk (M4, M5): 5 szó szerint | M4/M5 QA-riport; kánoni QA: riport (bdb94ab), javítás 35a9ddd | – (az M4.B rész a fő session visszaolvasásával igazolva: M4.B:278, M4 hub) | IMPLEMENTED a kánoni QA (35a9ddd) után |
| PRG-11 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M0.A:645 (egyenlő részvétel); a „páratlan a létszám” kikerült + 5484b02 | 14 blokk (M0, M2, M3, Z): 14 szó szerint | M0 QA-riport | eset- és kártyadarabszám, valamint egyenlőrészvétel-sor az M3.B, M4, M7 specekben (modulgazdák; M3.B: + Memuna) | az M2, M3.A és Z rész az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| PRG-12 | F | QA-RA VÁR | M3.B:186, :467 (előre megírt fiktív 4. esetkártya, „ne rögtönözz”) + ce04b9c | 3 blokk (M3): 3 szó szerint | M3 QA-riport | M3 modulgazda + Memuna: M3:QA-NYELV-13 (a 4.3.3 esete négy csoportnál) | a konkrét forgatókönyv Memuna-review-ja G-kapu. |
| PRG-13 | A | IMPLEMENTED | M5.A:243; M6.A:381, :549 + aadf41b, fbebec0 | 3 blokk (M5, M6): 3 szó szerint | M5/M6 QA-riport | – | – |
| PRG-14 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M7.1:371 (letölthető, nyomtatható promptkártya, PRG-14) + f6e9c6e | 3 blokk (M7): 3 szó szerint | M7 verdiktek | a tényleges médiaeredet igazolása (szerző / médiafelelős; M4:BIZT-G1-7 EXTERNAL); a nyomtatható változat legyártása | – |
| PRG-15 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M2.B:212 (önkéntes reflektáló kérdés) + 147f3c3 | 1 blokk (M2): 0 szó szerint; 1 a QA-javítás után finomítva (db724db) | M2 QA-riport | b) az M5.1 SLIDE 4 1./4. kulcsa: szakmai lektor / M5-szerző (M5:PED-G1-3) | a c) rész a bemenet szerint ALREADY_DONE, az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| PRG-16 | F | QA-RA VÁR | M6 HUB:228 („fiktív esetet használunk…”); M7.4 (112. blokk) és M1.3 SBI-S sablon az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban + fbebec0, f6e9c6e, eb4fa6d | 11 blokk (M1, M2, M3, M4, M6, M7, Z): 11 szó szerint | modul-QA-riportok | a döntés szerinti rövid szerzői szándék-QA modulonként (modulgazdák; M2 bizalmas olvasatnál Memuna; M6: hub tartalomfelelőse; Z: modulgazda vagy projektgazda); az M7.B „átjárás” (M7:NYELV-G3-12) nyitott | – |
| PRG-17 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | szándékosan nincs változás (M0:ERT-8) | nincs terv-blokk | – | pilot-visszajelzés (X-9); projektgazda / modulgazda | az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| LMS-1 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M1 KAPU:300; Z.4:336 (File submissions ON, videó csak DPO-profilon; Z:QA-IMPL-1 javítva) + eb4fa6d, a0c0c83 | 4 blokk (M1, M3, M4): 3 szó szerint; 1 a QA-javítás után finomítva (64a60d1) | M1 QA-riport, QA-riport Z | cél-Moodle beállítás- és a11y-ellenőrzés (LMS-gazda + DPO + hozzáférhetőségi gazda); M2- és M5-rész EXTERNAL | az M3- és M4-rész az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| LMS-2 | A | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M3.2:595, :623, :636, :675 („Drag & Drop mellékút nincs, LMS-2”) + ce04b9c | 23 blokk (M3): 12 szó szerint; 11 szándékosan nincs alkalmazva (M3#55, M3#56, M3#57, M3#58, M3#59, M3#60, M3#61, M3#62, M3#64, M3#65, M3#67) | M3 QA-riport (M3:QA-IMPL-1) | `tools/test_media_manifest.py` cseréje (projektgazda / fő session); a11y pre-flight | ismert eltérés. Az M3.4-rész blokkjai szándékosan nincsenek alkalmazva (X-10). |
| LMS-3 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M5.3:529 (adatminimalista út, LMS-3) + aadf41b | 4 blokk (M5): 4 szó szerint | M5 QA-riport | valós H5P + az LMS-M5-07 teszt (LMS-gazda + lektor); jóváhagyott önellenőrző tartalom (PRG-4, modulgazda) | – |
| LMS-4 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | M6 KAPU:388; RA:55 (pozitív és negatív eset, kánoni) + fbebec0, bdb94ab | 2 blokk (M6): 2 szó szerint | M6 QA-riport; kánoni QA: riport (bdb94ab), javítás 35a9ddd | a Grade type / Maximum grade / rubrikaminimum értéke (LMS-gazda + értékelési felelős; RT-P0-01) | – |
| LMS-5 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | MAN:97 (LMS-5, kánoni) + f6e9c6e, 0b76212, bdb94ab | 13 blokk (M7): 10 szó szerint; 2 a QA-javítás után finomítva (0b76212); 1 módosított alakban (4.1) | QA-riport M7 (IMPL-2, IMPL-3) | a NAR-05 hangszöveg VO_PACK (médiafelelős / VO-gazda) | az M7.3:53, :732, :825 QA-javításai az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| LMS-6 | A | IMPLEMENTED | M7.4:14, :543 (pontozatlan saját jegyzetes lista, nem completion-elem) + f6e9c6e | 5 blokk (M7): 5 szó szerint | M7 verdiktek (NYELV-11 ELVETVE) | – | – |
| LMS-7 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | szándékosan nincs változás (M7:IMPL-G2-12) | nincs terv-blokk | – | a hozzáférhetőségi gazda ellenőrzi az alt + kísérőszöveg együttes funkcióját | az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| LMS-8 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | MAN:94, :96, :98, :119 (képző által közvetített út, közvetlen tanulói AI-segéd nincs) + f6e9c6e, bdb94ab | 12 blokk (M7): 10 szó szerint; 1 a QA-javítás után finomítva (35a9ddd); 1 módosított alakban (4.1) | QA-riport M7 (BIZT-1, BIZT-2); kánoni QA: riport (bdb94ab), javítás 35a9ddd | krízis-, adatkezelési, jogosultsági és no-AI parity review a közvetlen úthoz (programvezető + Moodle-adminisztrátor; DPO-vétó; RT-5); CANON:QA-BIZT-3b emberi döntés — a közvetített AI-út a tanulói tájékoztatóban (programvezető + Moodle-adminisztrátor; DPO) | az alapértelmezés a feltétel teljesüléséig él. Az M7.4:801, KAPU:263 és M7.F:307 QA-javításai az ellenőrző ügynök nem olvasta vissza; a terv blokkjainak állapota a „Blokkok” oszlopban. |
| VO-1 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | a kurzusoldal: az M1.2-NAR-04, az M1.3-NAR-04 és az M1.3-NAR-06 `@asset` specifikációja a VO-pack célállapotát írja (eb4fa6d, 7a69b9d); a hangszöveg újrarenderelése a VO fix packban (VO_PACK minden modulban) | 3 blokk (M1): 2 szó szerint; 1 a QA-javítás után finomítva (7a69b9d) | – | egyetlen VO fix pack, újrarender és meghallgatás (médiafelelős / VO-gazda; felhasználói kérés, X-6) | ismert. |
| TECH-1 | A | IMPLEMENTED | nincs szövegváltozás: a „mini-jelenet” forma marad (M4.1, M5.3); a kivétel dokumentálva: HUM 14. szakasz TECH-1 sora és bevezetője (:610, :747); a ledger ALREADY_FIXED sorai | nincs terv-blokk | content_integrity (gyermekvédelmi tiltóőr) 0 hiba | – | a fő session ellenőrizte; a (D) „rövid jelenet” csere nem kellett |
| TECH-2 | F | KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ | nincs; az M6.1 és M6.2 fájlnév a régi | nincs terv-blokk | – | a felhasználó saját terminálban futtatja a `git mv`-t (X-7); projektgazda (`tools/` két sora, baseline-sor) | ismert. |

## 14. Amit ez a jelentés nem állít

- Nem release-jóváhagyás, és nem igazol runtime-, szerepköri vagy QA-bizonyítékot: a 16 bizonyíték-kapu és a G1–G8 nyitott, a `LEARNER-RELEASE-VERDICT` NO-GO.
- A `0 ERROR` és a zöld tesztek a gépi invariánsokat igazolják, nem a tananyag minőségét; a minőségi ellenőrzés a célzott QA-riportokban van, és csak a diff-hunkokra terjedt ki (teljes új alapreview nem volt).
- A ledger és ez a jelentés hivatkozás; a bizonyíték a fájlok, a commitok és a parancskimenetek.
