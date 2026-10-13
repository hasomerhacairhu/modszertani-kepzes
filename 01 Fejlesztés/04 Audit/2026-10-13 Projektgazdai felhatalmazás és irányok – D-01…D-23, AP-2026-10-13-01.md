# Projektgazdai felhatalmazás és irányok – D-01…D-23 rendezése, AP-2026-10-13-01

> **Audit trail, nem kánon.** A projektgazda 2026-10-13-i üzenete szó szerint, ahogy a sessionbe érkezett
> (a `next-version/AP-2026-10-11-01` ágon, a `3dfc451` állapotból). A benne álló irányok projektgazdai
> irányok; ahol az illetékes jóváhagyó más szerepkör, az irány a szöveg szerint sem helyettesíti az ő
> döntését vagy írásos jóváhagyását. A kánoni rögzítés helye: `02 Tervezet/Emberi jóváhagyás szükséges.md`
> 15. szakasz.

---

Folytasd a `hasomerhacairhu/modszertani-kepzes` repository fejlesztését a `next-version/AP-2026-10-11-01` ágon, a legutóbb ellenőrzött `3dfc451` commitból. Először ellenőrizd az aktuális HEAD-et.

## Cél

A 2026-10-13-i „Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md” dokumentumban szereplő D-01–D-23 döntési csomagok rendezése, a feloldható problémák tényleges kijavítása és a szükséges szakértői jóváhagyások előkészítése.

A korábban elfogadott 125 döntést NE nyisd újra. Ne indíts új teljes M0–Z auditot.

## Projektgazdai irányok

Az alábbi megoldási irányokat projektgazdaként támogatom. Ahol az illetékes jóváhagyó más szerepkör, ez nem helyettesíti az ő döntését vagy írásos jóváhagyását.

**Gyermekvédelem**
- D-01: egységes peula-megállítási protokoll, helyszíni helyettesítés, érzékeny foglalkozásoknál két felkészített 18+ felelős.
- D-02: a meglévő, kiskorúakra is kötelező védelmi keret megtartása.
- D-03: meglévő esetkártyák duplikálása, a negyedik eset megtartása.
- D-04: a meglévő kétlépcsős eszkaláció alkalmazása, egyértelmű címzettekkel és közvetlen veszély esetén azonnali biztonsági intézkedéssel.
- D-05: sürgősen készítsd elő a 116 111 és 116 000 segélyvonalak félrevezető leírásának javítását, aktuális elsődleges források alapján. A Memuna formális jóváhagyása szükséges.
- D-08: valódi passzjog, egyenértékű fiktív tudásdemonstrációval és előzetes témajelzéssel.
- D-09: a 24 órás kapuértékelési határidőt különítsük el a gyermekvédelmi bejelentések kezelésétől. A meglévő határidőt csak az illetékesek döntésével változtasd.

**Adatvédelem**
- D-10: incidensnyilvántartás, hozzáférés-korlátozás, dokumentált megőrzés/törlés és feltárásmentes pótlási út.
- D-11: a „Separate groups” elv terjedjen ki az Assignment, H5P, Quiz és GATE-CP elemekre, megfelelő jogosultságokkal és negatív hozzáférési tesztekkel. Ne feltételezd, hogy a csoportmód önmagában elegendő.
- D-12: név és egyéni eredmény nélküli, csoportszintű visszajelzés.
- D-13: egységes közöseszköz-protokoll, adattakarékosság, felesleges névmezők megszüntetése. Megőrzési időt csak DPO-jóváhagyással rögzíts.
- D-14: a nem igazolt AI-adatfolyam maradjon inaktív. A naplózás, megőrzés, adattovábbítás és a képző által közvetített AI-használat dokumentálása szükséges. A no-AI út maradjon egyenértékű.

**Értékelés és LMS**
- D-07: biztonságkritikus rubrikák és itemek közös szakértői kalibrációja, előzetesen nem közölt bukási feltételek nélkül.
- D-15: a dokumentum hat meglévő build-spec javaslatát fogadom el tervezési alapként. Az M3 megerősített kapu, a Z.3 tanuló-lokális útja, az M4 rubrika, az M6 pontozás, az M2.1 reflektív diája és a fórum új kohorszokra vonatkozó feltétele külön-külön legyen konzisztens és tesztelhető.
- D-16: a Z.4-nél a teljes beadás értelmezhetősége számítson, a passz maradjon lehetséges; az üres kötelező beküldés negatív tesztje legyen egyértelmű.
- D-17: rubrikakalibráció indokolatlan küszöbemelés nélkül. A pedagógiai pontozást és az adatvédelmi stopot külön kezeljük.
- D-18: az itemkulcsok a ténylegesen tanított tartalomhoz igazodjanak; a kulcsokat kizárólag az illetékes szakmai jóváhagyással változtasd.
- D-19: a tanulási kimenetek ne ígérjenek magasabb kompetenciaszintet, mint amit a tananyag gyakoroltat és mér.
- D-23: az M7 kapukvíznél a hibázott kompetenciát a mentor közölje a GATE-CP-n. Ne legyen automatikus kvízszintű zárás. A helyes válaszok és a megoldókulcsot felfedő visszajelzések semelyik automatikus review-ablakban ne jelenjenek meg, a lezárás után sem. Ezt cél-Moodle-ben is tesztelni kell.

**Program**
- D-06: a JOG-1 jogászi ellenőrzésének elsődleges nyilvántartása a G1 GitHub #1 issue legyen, a HUM megfelelő hivatkozásával.
- D-20: modulonkénti, lépésszintű vágási tervek, a védett gyermekvédelmi és kötelező feldolgozó lépések megtartásával.
- D-21: közös 1–5 fős F-peula keret, modulspecifikus kiegészítésekkel. Készíts hozzá konkrét `/course-develop` tervet. A terv külön projektgazdai elfogadásáig ne indíts új tartalomgyártást.
- D-22: az „átjárás” logisztikai értelemben, másik helyszínre történő átvonulást jelent.

## Végrehajtási szabályok

1. A projektgazdai hatáskörben eldönthető kérdéseket rögzítsd a megfelelő kánoni döntési helyen. Ahol a fenti irány önmagában elegendő, nincs szükség újabb általános kérdésre.

2. A Memuna, DPO, jogász, értékelési felelős, modulgazda vagy más jogosult döntési hatáskörét ne vedd át. Ezekhez készíts konkrét, előre kitöltött elfogadási javaslatokat, pontos szövegekkel, érintett fájlokkal és jóváhagyási feltételekkel. Jóváhagyás nélkül ne változtass védett szabályt, értékelési kulcsot vagy küszöböt.

3. Implementálj minden olyan módosítást, amelyet a fenti felhatalmazás és a korábbi lezárt döntések megengednek. Ne módosíts olyan részt, amely valódi, még hiányzó szakértői jóváhagyástól függ.

4. A 23 csomagot, a fennmaradó 119 emberi és 52 bizonyíték-tételt konszolidáld. Az átfedő findingokat vond össze. Ne kezeld őket 171 független új kérdésként, és ne állítsd, hogy bármelyik lezárult, ha ehhez nincs meg a szükséges bizonyíték.

5. Az M7 válaszszivárgási javítását ne nyisd újra. A még hiányzó review-options konfigurációt és runtime-tesztet készítsd elő.

6. Az LMS-2 technikai módosítását külön, kontrollált change setben végezd el, amennyiben ezt a repository szabályai és a jelen felhatalmazás megengedik. A TECH-2, felhasználói terminált igénylő átnevezéshez készíts ellenőrzött parancsokat és regressziós tervet, de ne kerüld meg a végrehajtási korlátozást.

7. Készíts jóváhagyásra kész szerepköri csomagokat a Memunának, DPO-nak, jogásznak, értékelési felelősnek, modulgazdáknak és médiafelelősnek. A VO fix pack minden szükséges módosítását egyetlen csomagban készítsd elő.

8. A módosításokra fusson célzott QA, verifier, regresszió, content-integrity és médiaellenőrzés. Új, teljes alapreview vagy önmagát ismétlő auditkör nem szükséges. Új QA-findingot csak validált, valódi hiba esetén vegyél fel.

9. A javításokat commitold és pushold a next-version ágra. Frissítsd a ledgert és a lefedettségi jelentést. Sem a sikeres teszt, sem a TERMINAL ledger nem helyettesítheti a runtime- vagy szerepköri bizonyítékot.

## Korlátok

- A `main` és a futó M0/M1 pilot érintetlen.
- CC-04 freeze változatlan.
- PR #30 marad draft.
- Nincs merge, staging deployment vagy learner release.
- Nincs automatikus szakértői jóváhagyás.
- Nincs kitalált runtime-eredmény, jogi állásfoglalás vagy tesztbizonyíték.

## Elvárt végeredmény

A munka végén rövid, döntésorientált jelentést kérek:

- Mi került ténylegesen kijavításra és tesztelésre?
- A D-01–D-23 csomagok közül melyik lezárt, melyik implementált, melyik vár szerepköri jóváhagyásra?
- Mely kérdésekhez kell még az én konkrét döntésem?
- Milyen kész jóváhagyási anyagot kell továbbítanom a Memunának, DPO-nak és a többi felelősnek?
- Mi szükséges még a staging buildhez és a learner release-hez?

A cél nem egy újabb kutatási vagy auditciklus, hanem a képzés következő, ténylegesen használható, kontrolláltan tesztelhető verziójának előkészítése, a valódi szakértői kapuk tiszteletben tartásával.

Ne állj meg az első külső függőségnél. Minden függetlenül elvégezhető munkát fejezz be, és csak a ténylegesen blokkolt tételeket hagyd nyitva.
