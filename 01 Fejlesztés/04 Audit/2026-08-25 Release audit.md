# Release audit – 2026-08-25

## Scope

Teljes repository- és commit-history alapú stabilizáció Anna 2026.07.20–08.12 közötti kézi auditja után. A vizsgálat kiterjed: konstruktív alignment, modulok/kapuk, safeguarding, kiskorúak/adatvédelem, AI, fejlődéslélektan, Moodle/H5P implementálhatóság, accessibility, repo-integritás, terminológia, program-transzfer és release-governance.

Az audit **két körben** készült. A második kör az elsőt is felülvizsgálta — és több olyan javítást talált, amelyet az első kör **befejezetlenül hagyott**, miközben késznek jelentett.

## Eredmény

**Pedagógiai architektúra: erős. Release: NO-GO a globális kapuk lezárásáig.**

A stabilizáció objektíven javítható regressziókat javít (duplikátumok, törött útvonalak, belső ellentmondások, félrevezető runtime/jogi állítások), de **nem hamisít szakértői aláírást**.

## 1. kör – végrehajtott változások

- M1/M3 duplikált kánoni fájlok eltávolítása és linkkorrekció.
- M1 feedback/alignment és titoktartási keret korrekció.
- M3 jogi szerepleírás pontosítása; kiskorú madrich nem kap önálló hatósági/jogi döntéshozó szerepet.
- M3.2 determinisztikus életkori és „amygdala gáz – PFC fék” állítások helyett fejlődési heurisztika + egyéni/kontextuális variabilitás.
- M2.1 identitástérkép-feltöltés megszüntetése (privacy by design).
- M6.4 cél ↔ completion alignment: legalább 3 ág.
- M6.1 AI Act provider/deployer szétválasztás; C2PA best practice.
- M7 külső AI: szervezetileg jóváhagyott eszköz, kiskorú terms/permission, no-AI alternatíva, sensitive-data tiltás.
- M7.4 átnevezése a v1 szerepnek megfelelően.
- Z.3 minor-role korrekció.
- Accessibility: prerecorded synchronized videónál captions-követelmény egyértelműsítve.
- Release governance, LMS manifest, runtime acceptance, privacy, safeguarding és terepgyakorlati kontrollréteg hozzáadva.

## 2. kör – az 1. kör felülvizsgálata

Az 1. kör automatizálása részben **saját magát írta felül futás közben** (a workflow-k a scriptek assertjeit kikapcsolták, illetve catch-all placeholder-fallbacket iktattak be), ezért több „validált” átalakítás valójában nem futott le. A záró riport ennek megfelelően pontosítva:

| 1. körben késznek jelentve | Tényleges állapot a 2. kör előtt | Javítva |
|---|---|---|
| „M3.B harmadik személyű esetanalízis” | Csak a címek változtak; a 4.2.4 továbbra is „eljátssza a jelenetet” + de-roling volt, a 4.2.5 pedig teljes fórum-színház mikroelem | ✅ |
| — (nem is jelezve) | Az M3 modulhub és az M3.F továbbra is „Miniszínház”-at hirdetett | ✅ |
| „AI Act szerepek szétválasztva” | Csak az M6.1-ben; a Program terv §4 és a §9 7. sora továbbra is univerzális deployer-kötelezettséget állított | ✅ |
| „Z.4 Moodle Assignment draft” | Félkész migráció: a törzs végig Documentation Toolt és „Letöltés / Export” gombot írt le | ✅ |
| „M6.A kiesés/székszerző ellentmondás megszüntetve” | A székszerző-verseny safety-mondata bent maradt, a játékmechanika pedig játszhatatlanná vált | ✅ |
| „M7.4 v1/v2 fogalmi rend” | A fájl neve v1 lett, a törzse 12 helyen továbbra is „Peula v2 vázlatot” kért | ✅ |
| Study Lab privacy-javítás | Mind a hét F-peula bájtazonos sablont kapott, M4-specifikus példákkal minden modulban | ✅ |
| — | Az M2 modulhub négy helyen továbbra is fotófeltöltést írt elő | ✅ |
| — | A README-ből törlődött a közreműködői lista, projektleírás és támogatási szakasz | ✅ |
| — | A média-regiszter 35 sora nem létező forrásfájlra mutatott | ✅ |
| — | `gyerekvédelem` / `gyermekvédelem` keveredés (a main-en is) | ✅ 120 előfordulás |
| — | A terepgyakorlati architektúra sehol nem jelent meg a tanulói úton | ✅ |

Emellett törölve lett öt egyszeri, tartalom-mutáló GitHub workflow és öt hozzájuk tartozó script; marad egy read-only checker + egy CI workflow.

## Külső validáció – ténylegesen konzultált források

- Gyvt. (1997. évi XXXI. tv.) 17. § és a 2024.09.01-i jelzőrendszeri változások: Nemzeti Jogszabálytár (njt.hu), Magyar Máltai Szeretetszolgálat Országos Módszertani Munkacsoport összefoglalója.
- Btk. 209/A. § – „Gyermekvédelmi jelzéssel kapcsolatos kötelezettség megszegése”, vétség, max. 2 év.
- Kék Vonal Gyermekkrízis Alapítvány (kek-vonal.hu): 116-111 (gyermek/ifjúsági), **116-000 (gyerekért aggódó felnőtteknek/szakembereknek)** — a repo állítása ellenőrizve és helyes.
- EU AI Act 50. cikk (2) provider-, (4) deployer-kötelezettség: **artificialintelligenceact.eu** (másodlagos forrás). *Az EUR-Lex hivatalos szövegét ebben a körben NEM sikerült lekérni — lásd a follow-up szakasz forrás-megjegyzését.*
- H5P Documentation Tool – content state saving nincs implementálva (h5p.org fejlesztői válasz).
- WCAG 2.2 SC 1.2.2 (Captions, Prerecorded).
- GDPR 8. cikk hatálya (információs társadalommal összefüggő szolgáltatás, hozzájárulás-alapú kezelés).

## Nem automatizálható P0

A `RELEASE-READINESS.md` globális kapui. Ezeket issue-ként is nyitni kell, felelőssel és bizonyítékkal kell lezárni. A repository **nem** pótolja és nem helyettesíti ezeket.

## Tanulság a folyamatra

Az egyszeri, önmagát futás közben módosító, tartalmat mutáló CI-automatizmus **nem alkalmas** tananyag-javításra: a „0 regresszió / validált” állítás olyan assertekből származott, amelyeket a futtató környezet előtte kikapcsolt. Ehelyett: read-only integritás-ellenőrzés CI-ban, tartalmi javítás emberi/ügynöki review-val, és minden kész-jelentés a **végállapoton** ellenőrizve.

***

## 3. kör – célzott follow-up (független külső audit után)

Egy **független külső audit** a pusholt `01177db` HEAD-en reprodukált 14 maradék ellentmondást. Mindegyiket a tényleges fájlokban ellenőriztük, mielőtt bármit szerkesztettünk volna.

A közös minta: a **modulfájlok már helyesek voltak, a program-szintű dokumentumok viszont még a régi viselkedést írták le.** Az integritás-ellenőrző ezt azért nem fogta meg, mert az M3 szerepjáték-szabály `Modulok/M3`-ra volt szűkítve.

| # | Finding | Állapot | Javítás |
|---|---|---|---|
| F1 | Program terv debrief-elve „fórum-/miniszínház … M3.B” | reprodukálva | valós, aktuális példákra írva |
| F2 | „a madrich **biztonságos felnőttként**” (M3-leírás) | reprodukálva | kiskorú-biztos szerepleírás; az M2 kapu „megbízható felnőtt”-je is |
| F3 | „Emberi jóváhagyás”: fórum-színház + Z.4 Documentation Tool | reprodukálva | mindkettő kivezetve, a kánoni állapot kimondva |
| F4 | „a kapu teljesítése a jogalap” | reprodukálva | a 6. cikk szerinti jogalap meghatározása a DPO/jogi felelősé |
| F5 | univerzális „16 alatti szülői hozzájárulás” | reprodukálva | a 8. cikk alkalmazhatóságának vizsgálatát kéri, nem állít szabályt |
| F6 | „felirat VAGY szöveges ekvivalens” a Program tervben | reprodukálva | SC 1.2.2 szerint javítva; **az ellenőrző talált egy továbbit az M0.3-ban** |
| F7 | abszolút 24px / 4,5:1 pre-flight számok | reprodukálva | SC 2.5.8 kivételei + SC 1.4.3/1.4.11 szétválasztva; a szigorúbb belső cél projekt-célként jelölve |
| F8 | AI Act checklist gépi jelölést írt elő | reprodukálva | provider/deployer szétválasztva a checklistben is |
| F9 | „Short Answer” mint H5P típus (57 hely) | reprodukálva | nem létező típus — magyar funkcionális megnevezés + acceptance-döntés |
| F10 | deep-audit.js `_AUDIT/` útvonal + `checkout -B` | reprodukálva | a harness **véglegesen read-only** lett |
| F11 | checker M3-ra szűkített hatóköre | reprodukálva | ACTIVE-SPEC szabályok az egész `02 Tervezet`-re |
| F12 | általános „négyszemközt” utasítás kiskorúaknál | reprodukálva | „diszkrét, de átlátható”; a szabály a gyermekvédelmi gate-be került |
| F13 | governance-duplikáció | reprodukálva | `Szint` oszlop (GLOBÁLIS/modul); a mátrix csak modul-szintű sorokat visz |
| F14 | Z.4 fejléc, M2 feltöltés-példa, forrás-provenance | reprodukálva | mindhárom javítva |

### Forrás-megjegyzés (őszinte provenance)

- **W3C WCAG 2.2** – elsődleges forrás, közvetlenül lekérve (`w3.org/TR/WCAG22/` + Understanding SC 2.5.8): SC 1.2.2, 1.4.3, 1.4.11, 2.5.8 normatív szövege és kivételei.
- **h5p.org** – elsődleges forrás, közvetlenül lekérve: a hivatalos content type listában nincs „Short Answer”; H5P staff (2025-02-27): *„Essay has not been added to Course Presentation… you add Essay in Interactive Book which can function similarly.”*
- **GDPR 8. cikk** – a hivatalos EUR-Lex oldalról származó szövegrészlet keresőn keresztül; a 6. cikk (1) a)–f) felsorolása `gdpr-info.eu` verbatim reprodukcióból.
- **EU AI Act 50. cikk** – `artificialintelligenceact.eu` (másodlagos).
- ⚠️ **Az EUR-Lex közvetlen lekérése ebből a környezetből nem sikerült:** minden HTML/PDF/cellar végpont ugyanazt a „Todays OJ” nyitóoldalt adta vissza. Ezért **nem állítjuk**, hogy a jogszabályok hivatalos konszolidált szövegét ebben a körben elsődleges forrásból visszaolvastuk. A jogi következtetések ennek megfelelően **óvatosak**: sehol nem döntünk a szervezet helyett jogalapról, 8. cikk alkalmazhatóságáról vagy 9. cikk szerinti feltételről.
