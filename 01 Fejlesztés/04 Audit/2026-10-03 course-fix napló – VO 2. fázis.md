# course-fix napló – VO 2. fázis (2026-10-03)

> **Audit trail, nem kánon.** A `/course-fix` nagy csomagos futásának lépésenkénti naplója
> (`.claude/skills/course-fix/nagy-csomag.md`). A napló a sorrendet és az állapotot rögzíti; bizonyíték a
> fájlok végállapota.

- **Forrás 1:** VO QA-repó fix pack (`reports/phase2/course-fix-pack.md`), CF-01…CF-106, 243 lépés
  (a CF-01 új fájl + 242 szerkesztés), 37 fájl. Döntési alap: projektgazdai döntéscsomag, 2026-10-03
  (VO D-01…D-23, ADDENDUM 2026-10-03-A és -B); a CF-01 ennek kurzusrepó-másolata.
- **Forrás 2:** `01 Fejlesztés/04 Audit/2026-10-03 Külső audit – ellenőrzött megállapítások.md`, AF-01, AF-02.
- **Bázis:** a csomag `cfeef1e`-re készült; a munkaág (`vo/phase2-course-fix`) azóta csak governance-fájlokat
  változtatott, a csomag 36 meglévő célfájlja a bázison azonos.
- **Sorrend:** a csomag „Alkalmazási sorrend” szakasza (CF-01 → CF-02…CF-32 → CF-33…CF-35 → CF-36…CF-98 →
  CF-99…CF-102 → CF-103…CF-106), utána AF-01, AF-02.
- **Köztes állapot:** a csomag szerint a `media_manifest.py check`/`reconcile` és a média-tesztek közben
  tervezetten bukhatnak; fájlcsoportonként csak `content_integrity.py` és `git diff --check` fut.

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| CF-01 | — | 2026-10-03 Projektgazdai döntések – VO 2. fázis.md | alkalmazva | új fájl; 867 sor, sha256 egyezik a csomagéval |
| CF-02 | (a) | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| CF-02 | (b) | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| CF-02 | (c) | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| CF-03 | — | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| CF-04 | (a) | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| CF-04 | (b) | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| CF-05 | (a) | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| CF-05 | (b) | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| CF-05 | (c) | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| CF-06 | — | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| CF-07 | (a) | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | új @asset M1.3-NAR-08 |
| CF-07 | (b) | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | új @source M1.3-NAR-08-VO |
| CF-07 | (c) | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| CF-07 | (d) | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| CF-07 | (e) | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| CF-07 | (f) | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| CF-07 | (g) | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| CF-08 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| CF-09 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| CF-10 | (a) | M1.4 – Miniszituációk – Mondd el SBI-ben.md | alkalmazva | |
| CF-10 | (b) | M1.4 – Miniszituációk – Mondd el SBI-ben.md | alkalmazva | |
| CF-10 | (c) | M1.4 – Miniszituációk – Mondd el SBI-ben.md | alkalmazva | |
| CF-11 | (a) | M1.4 – Miniszituációk – Mondd el SBI-ben.md | alkalmazva | |
| CF-11 | (b) | M1.4 – Miniszituációk – Mondd el SBI-ben.md | alkalmazva | |
| CF-12 | (a) | M2.3 – Somer 3 pillére – mini-kapszula.md | alkalmazva | |
| CF-12 | (b) | M2.3 – Somer 3 pillére – mini-kapszula.md | alkalmazva | |
| CF-12 | (c) | M2.3 – Somer 3 pillére – mini-kapszula.md | alkalmazva | |
| CF-12 | (d) | M2.3 – Somer 3 pillére – mini-kapszula.md | alkalmazva | |
| CF-13 | (a) | M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md | alkalmazva | `replace_all`, 2 előfordulás |
| CF-13 | (b) | M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md | alkalmazva | |
| CF-14 | (a) | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | |
| CF-14 | (b) | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | |
| CF-14 | (c) | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | |
| CF-14 | (d) | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | |
| CF-15 | (a) | M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md | alkalmazva | |
| CF-15 | (b) | M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md | alkalmazva | |
| CF-16 | — | M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md | alkalmazva | `replace_all`, 2 előfordulás |
| CF-17 | (a) | M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md | alkalmazva | csak időkeret |
| CF-17 | (b) | M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md | alkalmazva | |
| CF-17 | (c) | M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md | alkalmazva | |
| CF-18 | (a) | M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md | alkalmazva | csak a11y-jegyzet |
| CF-18 | (b) | M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md | alkalmazva | |
| CF-18 | (c) | M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md | alkalmazva | |
| CF-19 | — | M4.1 – Mit üzen a testem – Nonverbális kiállás.md | alkalmazva | |
| CF-20 | (a) | M4.2 – Aktív hallgatás & visszatükrözés.md | alkalmazva | |
| CF-20 | (b) | M4.2 – Aktív hallgatás & visszatükrözés.md | alkalmazva | |
| CF-20 | (c) | M4.2 – Aktív hallgatás & visszatükrözés.md | alkalmazva | |
| CF-21 | (a) | M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md | alkalmazva | |
| CF-21 | (b) | M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md | alkalmazva | |
| CF-21 | (c) | M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md | alkalmazva | |
| CF-21 | (d) | M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md | alkalmazva | |
| CF-22 | (a) | M5.3 – Hogyan tanulunk tényleg (…).md | alkalmazva | törlés; a horgony a következő sor („**Cél:**”), végállapot azonos |
| CF-22 | (b) | M5.3 – Hogyan tanulunk tényleg (…).md | alkalmazva | törlés; horgony: „**1. Gyakorlás**” |
| CF-22 | (c) | M5.3 – Hogyan tanulunk tényleg (…).md | alkalmazva | |
| CF-23 | (a) | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | |
| CF-23 | (b) | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | |
| CF-23 | (c) | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | |
| CF-24 | — | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | |
| CF-25 | (a) | M6.2 – Történet, mint tükör.md | alkalmazva | |
| CF-25 | (b) | M6.2 – Történet, mint tükör.md | alkalmazva | |
| CF-25 | (c) | M6.2 – Történet, mint tükör.md | alkalmazva | |
| CF-26 | (a) | M6.2 – Történet, mint tükör.md | alkalmazva | |
| CF-26 | (b) | M6.2 – Történet, mint tükör.md | alkalmazva | |
| CF-27 | (a) | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| CF-27 | (b) | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| CF-27 | (c) | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| CF-27 | (d) | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| CF-28 | (a) | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| CF-28 | (b) | M6.3 – Kézműves, ami tanít is.md | alkalmazva | `replace_all`, 5 előfordulás |
| CF-29 | (a) | M7.1 – Ez még csak vágy, nem cél – SMART nevelési cél someres módra.md | alkalmazva | törlés; a horgony a következő sor („**Cél:**”), végállapot azonos |
| CF-29 | (b) | M7.1 – Ez még csak vágy, nem cél – SMART nevelési cél someres módra.md | alkalmazva | törlés; horgony: a dia első sora |
| CF-29 | (c) | M7.1 – Ez még csak vágy, nem cél – SMART nevelési cél someres módra.md | alkalmazva | az adattakarékossági mondat a dián maradt |
| CF-30 | — | M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md | alkalmazva | `replace_all`, 2 előfordulás |
| CF-31 | (a) | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| CF-31 | (b) | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| CF-31 | (c) | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| CF-31 | (d) | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| CF-32 | — | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| CF-33 | — | _legacy/legacy-dispositions.json | alkalmazva | 6 sor; érvényes JSON |
| CF-34 | — | tools/test_media_manifest.py | alkalmazva | py_compile OK |
| CF-35 | — | tools/test_media_manifest.py | alkalmazva | |
| CF-36 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-37 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-38 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-39 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-40 | (a) | VOICE-BIBLE.md | alkalmazva | |
| CF-40 | (b) | VOICE-BIBLE.md | alkalmazva | csak a „Kiejtés” oszlop |
| CF-40 | (c) | VOICE-BIBLE.md | alkalmazva | csak a „Kiejtés” oszlop |
| CF-40 | (d) | VOICE-BIBLE.md | alkalmazva | csak a „Kiejtés” oszlop |
| CF-40 | (e) | VOICE-BIBLE.md | alkalmazva | csak a „Kiejtés” oszlop |
| CF-40 | (f) | VOICE-BIBLE.md | alkalmazva | „Kiejtés” oszlop + a megjegyzés vége |
| CF-40 | (g) | VOICE-BIBLE.md | alkalmazva | |
| CF-41 | (a) | VOICE-BIBLE.md | alkalmazva | horgony: a sor vége |
| CF-41 | (b) | VOICE-BIBLE.md | alkalmazva | |
| CF-42 | — | VOICE-BIBLE.md | alkalmazva | gyermekvédelmi kontextus (112) → vétólista |
| CF-43 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-44 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-45 | — | VOICE-BIBLE.md | alkalmazva | horgony: az első, változatlan pont vége |
| CF-46 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-47 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-48 | (a) | VOICE-BIBLE.md | alkalmazva | |
| CF-48 | (b) | VOICE-BIBLE.md | alkalmazva | voice-ID nem került be (⟬KITÖLTENDŐ⟭) |
| CF-48 | (c) | VOICE-BIBLE.md | alkalmazva | |
| CF-49 | (a) | VOICE-BIBLE.md | alkalmazva | horgony: a címsor |
| CF-49 | (b) | VOICE-BIBLE.md | alkalmazva | |
| CF-49 | (c) | VOICE-BIBLE.md | alkalmazva | |
| CF-50 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-51 | — | VOICE-BIBLE.md | alkalmazva | |
| CF-52 | (a) | ELEVENLABS-VOICE-TEST.md | alkalmazva | horgony: a címsor |
| CF-52 | (b) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-52 | (c) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-53 | (a) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-53 | (b) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-54 | — | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-55 | — | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-56 | — | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-57 | (a) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-57 | (b) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-57 | (c) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-57 | (d) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-57 | (e) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-57 | (f) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-57 | (g) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-58 | — | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-59 | — | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-60 | — | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-61 | (a) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-61 | (b) | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| CF-62 | (a) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-62 | (b) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-62 | (c) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-62 | (d) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-62 | (e) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-62 | (f) | VOICE-PILOT-SCRIPTS.md | alkalmazva | horgony a doboz 2. sorától (az 1. sor változatlan) |
| CF-63 | (a) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-63 | (b) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-64 | (a) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-64 | (b) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-64 | (c) | VOICE-PILOT-SCRIPTS.md | alkalmazva | az `1977-ben` sor változatlan |
| CF-65 | (a) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-65 | (b) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-65 | (c) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-66 | (a) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-66 | (b) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-66 | (c) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-67 | — | VOICE-PILOT-SCRIPTS.md | alkalmazva | horgony az 5. pont első soráig |
| CF-68 | (a) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-68 | (b) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-68 | (c) | VOICE-PILOT-SCRIPTS.md | alkalmazva | |
| CF-69 | — | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-70 | (a) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-70 | (b) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-70 | (c) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-71 | — | PILOT-PRODUCTION-PACK.md | alkalmazva | horgony: a sor középső része (egyedi) |
| CF-72 | (a) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-72 | (b) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-72 | (c) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-72 | (d) | PILOT-PRODUCTION-PACK.md | alkalmazva | horgony az „Export” pontig; a felirat-időzítési pont változatlan |
| CF-72 | (e) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-72 | (f) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-73 | (a) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-73 | (b) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-73 | (c) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-73 | (d) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-74 | (a) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-74 | (b) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-74 | (c) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-75 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-75 | (b) | PRODUCTION-STACK.md | alkalmazva | |
| CF-75 | (c) | PRODUCTION-STACK.md | alkalmazva | |
| CF-76 | — | PRODUCTION-STACK.md | alkalmazva | |
| CF-77 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-77 | (b) | PRODUCTION-STACK.md | alkalmazva | J3 nincs lezártnak jelölve |
| CF-77 | (c) | PRODUCTION-STACK.md | alkalmazva | |
| CF-77 | (d) | PRODUCTION-STACK.md | alkalmazva | |
| CF-78 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-78 | (b) | PRODUCTION-STACK.md | alkalmazva | |
| CF-79 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-79 | (b) | PRODUCTION-STACK.md | alkalmazva | |
| CF-80 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-80 | (b) | PRODUCTION-STACK.md | alkalmazva | |
| CF-80 | (c) | PRODUCTION-STACK.md | alkalmazva | |
| CF-81 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-81 | (b) | PRODUCTION-STACK.md | alkalmazva | |
| CF-82 | — | PRODUCTION-STACK.md | alkalmazva | |
| CF-83 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-83 | (b) | PRODUCTION-STACK.md | alkalmazva | |
| CF-84 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-84 | (b) | PRODUCTION-STACK.md | alkalmazva | |
| CF-84 | (c) | PRODUCTION-STACK.md | alkalmazva | |
| CF-84 | (d) | PRODUCTION-STACK.md | alkalmazva | |
| CF-85 | (a) | PRODUCTION-STACK.md | alkalmazva | |
| CF-85 | (b) | PRODUCTION-STACK.md | alkalmazva | |
| CF-86 | — | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-87 | (a) | PRODUCTION-DECISIONS.md | alkalmazva | D2 → LEZÁRVA (a 2026-10-03-i döntés átvezetése) |
| CF-87 | (b) | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-87 | (c) | PRODUCTION-DECISIONS.md | alkalmazva | voice-ID ⟬KITÖLTENDŐ⟭ marad |
| CF-87 | (d) | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-87 | (e) | PRODUCTION-DECISIONS.md | alkalmazva | az R3 a `blockers`-ben marad |
| CF-87 | (f) | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-87 | (g) | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-87 | (h) | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-87 | (i) | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-88 | — | PRODUCTION-DECISIONS.md | alkalmazva | formális hivatkozás ⟬KITÖLTENDŐ⟭ marad |
| CF-89 | (a) | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-89 | (b) | PRODUCTION-DECISIONS.md | alkalmazva | |
| CF-90 | — | PRODUCTION-DECISIONS.md | alkalmazva | horgony: a D7-sor vége |
| CF-91 | (a) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-91 | (b) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-91 | (c) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-91 | (d) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-91 | (e) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-91 | (f) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-92 | (a) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-92 | (b) | RIGHTS-EVIDENCE.md | alkalmazva | R2-5: RÉSZBEN MEGVAN (nem MEGVAN) |
| CF-92 | (c) | RIGHTS-EVIDENCE.md | alkalmazva | horgony: a bekezdés 2. sora |
| CF-92 | (d) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-92 | (e) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-92 | (f) | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-93 | — | RIGHTS-EVIDENCE.md | alkalmazva | V1 HIÁNYZIK marad |
| CF-94 | — | RIGHTS-EVIDENCE.md | alkalmazva | |
| CF-95 | (a) | Média-assetek/README.md | alkalmazva | |
| CF-95 | (b) | Média-assetek/README.md | alkalmazva | |
| CF-95 | (c) | Média-assetek/README.md | alkalmazva | |
| CF-96 | (a) | ASSET-AUTHORING.md | alkalmazva | a sablon JSON-ja változatlan |
| CF-96 | (b) | ASSET-AUTHORING.md | alkalmazva | |
| CF-96 | (c) | ASSET-AUTHORING.md | alkalmazva | |
| CF-96 | (d) | ASSET-AUTHORING.md | alkalmazva | |
| CF-97 | — | PRODUCTION-STYLE-TOKEN.md | alkalmazva | |
| CF-98 | — | produkcios-szabalyok.json | alkalmazva | érvényes JSON; egy ⟬KITÖLTENDŐ⟭ szándékosan marad |
| CF-99 | — | Program terv.md | alkalmazva | a D9-címke szövege változatlan |
| CF-100 | (a) | LMS – hozzáférhetőségi sztenderd.md | alkalmazva | |
| CF-100 | (b) | LMS – hozzáférhetőségi sztenderd.md | alkalmazva | |
| CF-101 | — | LMS – H5P runtime acceptance.md | alkalmazva | horgony: a 21. pont vége + a címsor; új 22. pont |
| CF-102 | — | Emberi jóváhagyás szükséges.md | alkalmazva | a LEZÁRVA tétel dátuma/jóváhagyója változatlan |
| CF-103 | (a) | LMS – hozzáférhetőségi sztenderd.md | alkalmazva | |
| CF-103 | (b) | LMS – hozzáférhetőségi sztenderd.md | alkalmazva | horgony: a checklist-sor (az üres sor nélkül) |
| CF-104 | (a) | LMS – H5P runtime acceptance.md | alkalmazva | a CF-101 után; horgony: a 22. pont vége + a címsor |
| CF-104 | (b) | LMS – H5P runtime acceptance.md | alkalmazva | |
| CF-105 | (a) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-105 | (b) | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| CF-106 | — | PRODUCTION-STACK.md | alkalmazva | a 36 fájl és a CF-01 bájtra egyezik a csomag végállapotával |
| AF-01 | — | Program terv.md | alkalmazva | a L73 bontásának átvezetése; új összeg nincs |
| AF-02 | — | Emberi jóváhagyás szükséges.md | alkalmazva | a `RELEASE-READINESS.md:23` mondatának átvezetése; státusz és vétó/QA változatlan |

## Összesítés és záró ellenőrzés (2026-10-03)

- **Állapotok:** 245 sor — alkalmazva 245 (CF-01 + 242 csomaglépés + AF-01, AF-02); már alkalmazva 0;
  kihagyva 0; megállva 0. Minden lépés előtt a bizonyíték a fájlban megvolt (1×, ill. a `replace_all`
  lépéseknél 2×/5×), a hozzáadott sorok még nem.
- **Végállapot:** a 36 meglévő célfájl és a CF-01 bájtra egyezik azzal, amit a csomag lépései a bázisra
  alkalmazva adnak (programmal összevetve); a CF-01 sha256-a egyezik a csomagban megadottal.
- **Hangnév-ellenőrzés (2026-10-03-A):** a VO QA-repó push-ellenőrzőjének mintáival a teljes diff
  hozzáadott sorai, a két új fájl és mind a 49 érintett fájl (az xlsx belső XML-jével) — 0 találat.
- **Pin:** egyetlen `--pin-visible`, pontosan 20 fájl (a csomag által várt lista).
- **Build:** kétszer, stabil; 9 generált kimenet változott (a csomag által várt lista).
- **Ellenőrzések:** `py_compile` OK; `media_manifest.py check` OK (10 kimenet naprakész, 747 történeti
  sor egyeztetve); `reconcile` 747/747, 0 nem egyeztetett, `NO_LONGER_REQUIRED` 10; `validate` OK (415
  asset, 903 deliverable, 123 forrásblokk, 84 fájl); `lint --high-only` 0 jelzés; `unittest` 150 teszt OK;
  `content_integrity.py` 0 ERROR; `git diff --check` tiszta.
- **Release-riport:** `RELEASE-VERDICT: NO-GO` (változatlan). Az `A11Y-CHECKLIST` nyitott tételei 19 → 20:
  a CF-103 (b) új, kipipálatlan checklist-sora (nincs automatikus lejátszás) — új követelmény, nem
  regresszió. A PRODUCTION-RULES nyitott tételei: R2, R3 (az R3 egy ⟬KITÖLTENDŐ⟭-je szándékos: a
  voice-ID rögzítési helye).
- **Nem commitolva.** A commit-bontás a csomag javaslata szerint: (1) tartalmi commit (a 38 kézi fájl és a
  `tools/approved-visible-text.json`), (2) külön `chore(media)` commit a 9 generált kimenettel.

## Célzott utóellenőrzés (a diff-hunkokon, lencsénként) — nyitott findingok

A `/course-fix` szerint ezek **nem** kerültek javításra; új fix packhoz vagy döntéshez tartoznak. Teljes szövegük a
futás jelentésében; itt az azonosító, a hely és a lényeg. Előtag: `UE-` (utóellenőrzés), hogy ne ütközzön az
1. fázis azonosítóival.

| ID | Típus | Hely | Lényeg |
|---|---|---|---|
| UE-NYELV-1 / UE-PED-3 | objektív | M1.3:264 ↔ :272 | „a verziócímke … nem hangzik el” — a képleírás (M1.3-NAR-08-VO) viszont felolvassa; hiányzik az „a párbeszédben” minősítő |
| UE-NYELV-2 / UE-PED-2 | objektív | M1.3:278 | a képleírás 4. része kategórianevet mond („az S a szituációnál…”), nem a „Mit látunk?” szerinti szövegrészt |
| UE-NYELV-3 | objektív | M3.1:644, :677; M3.3:812 | az új címkében `—` a magyar `–` helyett; az M1.4 címkéjével nem párhuzamos szerkezet |
| UE-NYELV-4 / UE-IMPL-4 | objektív (+ emberi döntés) | runtime acceptance 22. pont; PRODUCTION-STACK §6; P-NAR lista | a leirat helye háromféle („mellett látható” / „megnyitható” / linkelt oldal); a gombbal nyitható szöveg „látható”-e: projektgazda / hozzáférhetőségi gazda |
| UE-NYELV-5 | objektív | HUM :406 | „bizonyíték-kapu: megvalósítási döntés: …” — két kettőspont; zárójeles formula javasolt |
| UE-PED-1 | objektív | M3.1:621/626/677; M3.3:756/761/812 | írásos reflexiónál a „(a szakasz összesen 20–30 mp)” félrevezető; „saját tempóban, nem része a hangfájlnak” javasolt |
| UE-PED-4 | emberi döntés | M1.1:717/722/778 | az M1.1-NAR-05 ugyanolyan reflexiós felvezető, de nincs a D-17.3 körében — mérés kell |
| UE-IMPL-1 | objektív (P1) | M4.2:460 (P-NAR!), M1.4, M7.2, Z.1 a11y-jegyzetei | csak-hang narrációk még „Felirat … kötelező”-t írnak — a D-19 csak az M3.3-ban van átvezetve (a csomag „Nem eldöntött” 5. pontja tömeges átírásként kihagyta) |
| UE-IMPL-2 | objektív | PRODUCTION-DECISIONS „Lezárt döntések”; HUM | a VO D-04…D-07, D-10, D-11, D-13, D-17, D-19…D-23 és a 2026-10-03-B nincs a döntési nyilvántartásban átvezetve (csak D-01, D-14, D-16, D-18 és a D2/D11 blokkok); a D9 sor nem kapta meg a D-21-et |
| UE-IMPL-3 | objektív | PRODUCTION-DECISIONS :206–209, :234–244; PRODUCTION-STACK :565; RIGHTS-EVIDENCE :96–97, :368 | a módosított sorok melletti mondatokban régi darabszámok maradtak (117, 119, 109/344, 417) |
| UE-IMPL-5 | objektív (+ emberi döntés) | ELEVENLABS-VOICE-TEST :43, :72; PILOT-PRODUCTION-PACK :187 ↔ VOICE-BIBLE :285, README, PRODUCTION-DECISIONS :218, R3 | a voice-ID helye ellentmondóan („nem kerül a repóba” ↔ „ide kerülhet: ⟬KITÖLTENDŐ⟭”); a tárolási hely: projektgazda |
| UE-IMPL-6 | objektív | VOICE-BIBLE :222 | a WebVTT `<v Madrih A>` nem jelenik meg a renderelt feliratban; kiírt beszélőnév kell |
| UE-IMPL-7 | objektív | runtime acceptance 23. pont | a „ki van kapcsolva” kijelentő mód — ellenőrző lépésként kell megfogalmazni |
| UE-IMPL-8 | objektív | VOICE-PILOT-SCRIPTS „Mit NEM dönt el” | a történeti ELEVENLABS-VOICE-TEST pontozólapjára aktuálisként hivatkozik |
| UE-BIZT-1 | emberi döntés (P1) | RIGHTS-EVIDENCE :304–307 | a V1 (szülői/gondviselői tájékoztatás) tartalmi kérdés, nem csak „formális bizonyíték” — lefedi-e a D-08: projektgazda |
| UE-BIZT-2 | objektív | RIGHTS-EVIDENCE 1/A.0 | kimaradt a „hogy a két hangnál hogyan teljesült, csak valós bizonyíték rögzítheti” kikötés |
| UE-BIZT-3 | emberi döntés (P1) | HUM :406; RIGHTS-EVIDENCE :137–146 | a forrás-beszélők nagykorúságának igazolása sehol nincs kötelező mezőként (ElevenLabs ÁSZF 1(a)) — DPO + jogi felelős |
| UE-BIZT-4 | objektív | VOICE-BIBLE :165–170, :218 | a „számjegyenként” általános szabály egy jövőbeli 112-re „egy-egy-kettő”-t írna elő (a D-07 tiltja) |
| UE-BIZT-5 | objektív | RIGHTS-EVIDENCE :81 (R2-3), 1/A.1 cím | a 21 → 18 beszélőfej nem futott végig az R2-3 hatályán és az 1/A.1 címén |
| UE-BIZT-6 | bizonyíték-kapu | HUM :406; RIGHTS-EVIDENCE R2-5, V1; VOICE-BIBLE 112 | `VOICE-RIGHTS-REGISTER` hivatkozás, jogi/privacy minősítés, 50. cikk (4), Memuna-átnézés (G1) — hiányzik, nem tananyag-javítás |
| UE-BIZT-7 | emberi döntés → **eldőlt (K1)** | `2026-10-03 Projektgazdai döntések – VO 2. fázis.md` :857–859 | a félmondat a nyilvános másolatból kimaradt, a fejléc jelzi (commit előtt; ettől a CF-01 sha256-a már nem a csomagé) |

**Projektgazdai döntések az utóellenőrzés után (2026-10-03):** K1–K4 — `2026-10-03 Projektgazdai döntések – VO 2. fázis,
kiegészítés.md`. K2: az UE-IMPL-1 mindre, egységesen; K3: a voice-ID csak a VO QA-repó gyártási konfigurációjában; K4: az
M1.3 Madrih B szerepe már az első körben a második hanggal (a VO D-14 módosítása). Átvezetésük `/course-fix`-szel.
