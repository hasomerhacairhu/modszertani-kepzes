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
- EU AI Act 50. cikk (2) provider-, (4) deployer-kötelezettség: artificialintelligenceact.eu / EUR-Lex.
- H5P Documentation Tool – content state saving nincs implementálva (h5p.org fejlesztői válasz).
- WCAG 2.2 SC 1.2.2 (Captions, Prerecorded).
- GDPR 8. cikk hatálya (információs társadalommal összefüggő szolgáltatás, hozzájárulás-alapú kezelés).

## Nem automatizálható P0

A `RELEASE-READINESS.md` globális kapui. Ezeket issue-ként is nyitni kell, felelőssel és bizonyítékkal kell lezárni. A repository **nem** pótolja és nem helyettesíti ezeket.

## Tanulság a folyamatra

Az egyszeri, önmagát futás közben módosító, tartalmat mutáló CI-automatizmus **nem alkalmas** tananyag-javításra: a „0 regresszió / validált” állítás olyan assertekből származott, amelyeket a futtató környezet előtte kikapcsolt. Ehelyett: read-only integritás-ellenőrzés CI-ban, tartalmi javítás emberi/ügynöki review-val, és minden kész-jelentés a **végállapoton** ellenőrizve.
