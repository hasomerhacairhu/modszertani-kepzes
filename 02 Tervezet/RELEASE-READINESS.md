# Release readiness – staging és élesítés

## Jelenlegi állapot

- **Moodle staging:** **READY WITH NAMED HUMAN GATES** – a tananyag szerkesztői stagingben felépíthető és tesztelhető. A tartalmi specifikáció **nem tekinthető zártnak**, amíg kötelező tanulói médiaasset nyitott jogi vagy gyermekvédelmi médiakapun áll (lásd: **Médiakapuk**). A staginghez tesztfiókot és tesztadatot használunk; valódi madrih nem kap hozzáférést.
- **Learner-facing release:** **NO-GO** – az alábbi kapuk bizonyíték nélkül nem zárhatók le. A HUM-tételek 2026-10-02 óta lezártak (projektgazdai döntések, `Emberi jóváhagyás szükséges.md`), ezért a NO-GO a futtatási és build-ellenőrzéseken (runtime acceptance, Moodle build), valamint a gyermekvédelmi, adatvédelmi és hozzáférhetőségi átvételi listák és a program-transzfer még nyitott pontjain áll. **READY** csak akkor lehet, ha a G1–G8 zárt, és minden release-hatókörű médiakapu is zárt, vagy az érintett assetet eltávolították, illetve helyettesítették. Ha már csak médiakapu nyitott, az állapot **CONTENT_READY / MEDIA_PENDING**.

A két állapotot nem szabad összemosni. A staging célja éppen az, hogy a Moodle/H5P megvalósítást, a completiont, a kapukat és a hozzáférhetőséget bizonyítsuk. A szervezeti döntések 2026-10-02 óta lezártak, de a futtatási és átvételi bizonyítékok hiánya ettől még változatlanul blokkolja az éles megnyitást.

## Élesítés előtti globális kapuk

| Gate | Követelmény | Állapot típusa | Bizonyíték |
|---|---|---|---|
| **G1 Gyermekvédelem** | HUM-SAFE-01–05 lezárva; M3 és kapcsolódó biztonsági tartalmak írásos gyermekvédelmi jóváhagyása (jóváhagyó: a Memuna – lásd a táblázat alatt) | `HUMAN_DECISION_REQUIRED` + `EXPERT_SIGNOFF_REQUIRED` | `Gyermekvédelem – release gate.md` |
| **G2 Adatvédelem és kiskorúak** | HUM-PRIV-01–04 lezárva, activity-szintű adatleltár, adatvédelmi tájékoztató, hozzáférés, megőrzés/törlés | `HUMAN_DECISION_REQUIRED` + `EXPERT_SIGNOFF_REQUIRED` | `Adatvédelem – tanulói adatok és AI.md` |
| **G3 Moodle/H5P célkörnyezet** | pontos verziók + kritikus runtime tesztek | `IMPLEMENTATION_REQUIRED` | `LMS – H5P runtime acceptance.md` |
| **G4 Learner-facing nyitott mező = 0** | nincs `KITÖLTENDŐ`, ismeretlen kontakt, bizonytalan határidő vagy törött link a madrih által látható felületen | `IMPLEMENTATION_REQUIRED` | staging visszaaudit |
| **G5 Hozzáférhetőség** | mobil, billentyűzet, képernyőolvasó, zoom/reflow, felirat/leirat a tényleges renderen | `IMPLEMENTATION_REQUIRED` + `RUNTIME_VERIFIED` | a11y tesztjegyzőkönyv |
| **G6 Mozgalmi tartalom** | HUM-SOMER-01–03 lezárva az érintett részekhez | `HUMAN_DECISION_REQUIRED` | `Emberi jóváhagyás szükséges.md` |
| **G7 Regresszió** | repository tesztek, content integrity, média-manifeszt, helyi linkek és diff ellenőrzése zöld | `IMPLEMENTATION_REQUIRED` | CI / release-check |
| **G8 Ütemezés és support** | HUM-OPS-01–02 + HUM-A11Y-01 lezárva | `HUMAN_DECISION_REQUIRED` | központi schedule + „Segítség és kapcsolatok” blokk |

**Projektgazdai döntések a kapukhoz (2026-10-02).** A G1, G2, G6 és G8 HUM-feltétele (a „… lezárva” rész) teljesült: a tételek lezártak (`Emberi jóváhagyás szükséges.md`), a megnevezett szerepek későbbi ellenőrzése vétó / minőségellenőrzés (QA), nem új döntési kapu. A kapuk ettől még nem zártak: mindegyik csak a táblázat „Bizonyíték” oszlopa szerinti bizonyítékkal és a tracker-issue-ban rögzített lezárással zárul (lásd: GitHub release-tracker).

- **G1 – jóváhagyói rend:** a gyermekvédelmi jóváhagyás egyetlen felelős jóváhagyója a **Memuna** (a Somer gyermekvédelmi felelőse); a programvezető operatív társdöntő, jogi szakértő csak jogi kérdésben dönt. A képzés elsődleges normatív gyermekvédelmi dokumentuma a **Gyermekvédelmi működési standard v1.0** (a HUM-SAFE-01…05 együtt; `Gyermekvédelem – release gate.md` §5.1).
- **G5/G8 – hozzáférhetőségi felelős (HUM-A11Y-01):** külön szerep; a szerző nem hagyja jóvá a saját anyagát. A felelős (accountable) hozzáférhetőségi gazda a **Ros Hinuh** (jelenleg Lili); az élesítés előtti, független második ellenőrző (pre-flight) **Marci**. A pre-flight ellenőrzőnek ismernie kell a WCAG- és H5P-követelményeket, és nem lehet az ellenőrzött anyag szerzője. Utólagos ellenőrzés (vétó/QA): a programvezető.
- **G8 – ütemezés és support (HUM-OPS-01–02):** a program 2026-11-06-án (péntek) indul, és 2027-03-05-én (péntek) zárul; a teljes központi naptár (péntekek, kapu-beadások, megerősítések, téli szünet) az `LMS – activity manifest.md` §7-ében (Központi ütemezés) él. A „Segítség és kapcsolatok” blokk négy, szerep szerinti kontaktot ad (technikai segítség, tanulási/programkontakt, a kijelölt mentor, és ettől külön a Memuna); a mentori kapacitás kemény plafonja 1:8. Utólagos ellenőrzés (vétó/QA): a programvezető.

### Médiakapuk

**Projektgazdai döntés (2026-10-02):** a jogi és gyermekvédelmi médiakapuk blokkolják az általuk érintett tanulói asset release-ét. A teljes release csak akkor **READY**, ha minden release-hatókörű médiakapu zárt, vagy az érintett assetet eltávolították, illetve helyettesítették. Külön állapot lehet: **CONTENT_READY / MEDIA_PENDING**. „Specifikáció zárt” nem igaz, amíg kötelező asset nyitott jogi kapun áll. Utólagos ellenőrzés (vétó/QA): a release owner és a jogi/adatvédelmi felelős.

Ilyen kapuk: a **HUM-MEDIA-02** (hangjogosultság; alkapui: J1, J2, V1, V3) és a **HUM-MEDIA-03** (avatar- és médiajogok; gyermekvédelmi vagy krízis-HOOK-ban nincs készlet-AI-beszélőfej). A két döntés 2026-10-02-án lezárult (`Emberi jóváhagyás szükséges.md`), de a médiakapuk a bizonyítékig nyitva maradnak: az alkapuk állapotát a `Média-assetek/RIGHTS-EVIDENCE.md` 1/A.5. pontja tartja nyilván, a D11 a hangjogosultsági bizonyítékig blokkolt, az E-9 jogi felülvizsgálaton van (`LEGAL_REVIEW_REQUIRED`). A felelős- és bizonyíték-mezők (a bizonyíték megléte és nem személyes hivatkozása): `Média-assetek/RIGHTS-EVIDENCE.md`; a valódi név, a szerződés vagy hozzájárulás, a hatókör és a dátum a korlátozott hozzáférésű jogosultsági nyilvántartásba tartozik, nem a repóba. A hangjogosultsági nyilvántartás helye: Google Workspace Shared Drive → `Restricted / Rights / Voice`, `VOICE-RIGHTS-REGISTER`; valódi név nem kerül a Gitbe.

A **vizuális rendszer** (HUM-MEDIA-01; a `Média-assetek/PRODUCTION-DECISIONS.md` D1 döntése) nem jogi vagy gyermekvédelmi médiakapu, hanem gyártási feltétel. **Projektgazdai döntés (2026-10-02):** a D1 lezárva – a hivatalos Somer-paletta, a 2022-es arculati kézikönyv és a hivatalos SVG színgenerációja a kánon; a produkciós rendszer a B változat (Source Sans 3 + produkciós semleges skála); a szín soha nem önálló jelentéshordozó. Ezzel az R5 nyitott értéke (a paletta) eldőlt; a produkciós szabály kitöltése, az asset-szintű R5-blokkolók kivezetése és a médiaállapot darabszámai a média-build után frissülnek. Utólagos ellenőrzés (vétó/QA): a kreatív/márkafelelős.

## GitHub release-tracker

A repository-specifikáció és a tényleges lezárási munka külön réteg. A nyitott kapukat ezek az issue-k követik:

| Kapu / döntés | Tracker |
|---|---|
| **G1 / HUM-SAFE-01–05** | [#1 – Gyermekvédelmi release gate és szakértői jóváhagyás](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/1) |
| **G2 / HUM-PRIV-01–04** | [#2 – Adatvédelem, kiskorúak, reflexiók, felvétel és külső AI](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/2) |
| **G3 + G5** | [#3 – Moodle/H5P célverziók és runtime acceptance](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/3) |
| **G4 + G8 / HUM-OPS-01–02 + HUM-A11Y-01** | [#4 – Moodle build, dátumok, kontaktok és előfeltételek](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/4) |
| **G6 / HUM-SOMER-01–03** | [#6 – Mozgalmi tartalom jóváhagyása](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/6) |
| **G7** | GitHub Actions + release-check az élesítendő commiton |
| **Program-transzfer** | [#9 – Terepgyakorlat és learner pilot](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/9) |
| **HUM-GOV-01** *(nem P0 release-gate; projektgazdai döntés, 2026-10-02 – lezárva; utólagos ellenőrzés (vétó/QA): a programvezető és a módszertani felelős)* | [#7 – Terepgyakorlat rubrika és KPI skálájának összehangolása](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/7) |

Az issue-k **nem helyettesítik a jóváhagyási bizonyítékot**. Lezáráskor az issue-ba a tényleges döntést, dátumot, jóváhagyót és bizonyítékot kell linkelni/rögzíteni; csak ezután tekinthető az adott gate zártnak. A HUM-tételek döntése, dátuma, jóváhagyója és bizonyítéka 2026-10-02 óta az `Emberi jóváhagyás szükséges.md`-ben áll (**projektgazdai döntések**); ezt kell az issue-kba átvezetni. A megnevezett szerepek későbbi ellenőrzése vétó / minőségellenőrzés (QA): vétó esetén a tétel újranyílik.

## Staging-szabály

A staging buildben:

1. **nem találunk ki** gyermekvédelmi, privacy-, support- vagy mozgalmi adatot;
2. emberi döntés helyén **belső build-jelölő** maradhat, de ez nem kerülhet learner-facing nézetbe;
3. személyes adat helyett szintetikus tesztadatot használunk;
4. minden tényleges Moodle activity kap stabil build-ID-t és a létrehozás után rögzített Moodle `cmid`-t;
5. minden runtime-bizonyítást `IMPLEMENTATION_TEST_REQUIRED` állapotból csak tényleges teszteredmény mozdíthat `RUNTIME_VERIFIED` állapotba.

## Modul-specifikus élesítés

Egy modul szakmai jóváhagyása lehet moduláris, de a hozzá tartozó globális kapukat nem lehet megkerülni. Például az M1 stagingben akkor is teljesen felépíthető, ha egy rá vonatkozó adatkezelési döntés (pl. a HUM-PRIV-01) még nyitott; valódi madrihnak viszont az M1 Assignment csak a jóváhagyott adatkezeléssel nyitható meg.

A safeguarding-tartalomra külön szabály vonatkozik: M3.3, M3.B és az M3/M7 gyermekvédelmi kapuelemek **éles használatához** az adott tartalomhoz közvetlenül szükséges **HUM-SAFE-01/02** döntések és az írásos gyermekvédelmi jóváhagyás (jóváhagyó: a Memuna, lásd G1) kötelező, **de ez nem szűkíti a globális G1-et**: learner-facing release csak akkor lehet, ha a teljes **HUM-SAFE-01–05** csomag lezárt.

## Legkisebb értelmes staging pilot

**M0 + M1**, belső tesztfiókokkal.

Miért ez a minimum:
- M0 bizonyítja a kurzusnavigációt, H5P completiont, fórumot és a puha completion-logikát;
- M1 hozzáadja az Assignmentet, rubrikát, javítás/újrabeadás folyamatot és az összetett teljesítési feltételt;
- együtt már tesztelhető a modulok közötti unlock, a mobil/a11y viselkedés és a `moodle-ai-mcp` build-visszaolvasás;
- M3 gyermekvédelmi kockázata és az M7 összegző feladat összetettsége nélkül ad valódi technikai szeletet;
- az első staging **nem vár narrációra, AI-videóra vagy arculati grafikára**; a média-fallbackeket a `Média-assetek/RELEASE-MEDIA-STATUS.md` rögzíti.

**A pilot nem learner release.** A tesztelők szerkesztői/QA tesztfiókok.

## Program-transzfer

- [ ] A félév végi `Peula v2` után működik a `Terepgyakorlat – 2. félév.md` szerinti hat valós, 60–90 perces peula + mentori visszajelzési ciklus.
- Learner pilot kis csoporttal: későbbi mérés, **nem release-kapu** (projektgazdai döntés, 2026-10-02). A V1 időkereteket finomíthatja, de nem kell rá várni.
- [x] A médiaregiszter a tartalmi freeze után újragenerálva és auditálva. **Bizonyíték:** determinisztikus `media_manifest.py build/check/reconcile` + sikeres teljes media CI (`36605020566`, 417 asset / 902 deliverable / 143 teszt).

## Merge ≠ staging ≠ release

A GitHub merge technikai esemény. A Moodle staging egy zárt megvalósítási és tesztkörnyezet. Az éles learner release külön, dátummal, jóváhagyókkal és runtime-bizonyítékokkal rögzített Go/No-Go döntés.
