# Release readiness – staging és élesítés

## Jelenlegi állapot

- **Moodle staging:** **READY WITH NAMED HUMAN GATES** – a tartalmi specifikáció zárt, szerkesztői stagingben felépíthető és tesztelhető. A staginghez tesztfiókot és tesztadatot használunk; valódi madrich nem kap hozzáférést.
- **Learner-facing release:** **NO-GO** – az alábbi emberi, szervezeti és futtatási kapuk bizonyíték nélkül nem zárhatók le.

A két állapotot nem szabad összemosni. A staging célja éppen az, hogy a Moodle/H5P megvalósítást, a completiont, a kapukat és a hozzáférhetőséget bizonyítsuk. A szervezeti döntések hiánya ettől még változatlanul blokkolja az éles megnyitást.

## Élesítés előtti globális kapuk

| Gate | Követelmény | Állapot típusa | Bizonyíték |
|---|---|---|---|
| **G1 Gyermekvédelem** | HUM-SAFE-01–05 lezárva; M3 és kapcsolódó biztonsági tartalmak szakértői jóváhagyása | `HUMAN_DECISION_REQUIRED` + `EXPERT_SIGNOFF_REQUIRED` | `Gyermekvédelem – release gate.md` |
| **G2 Adatvédelem és kiskorúak** | HUM-PRIV-01–04 lezárva, activity-szintű adatleltár, adatvédelmi tájékoztató, hozzáférés, megőrzés/törlés | `HUMAN_DECISION_REQUIRED` + `EXPERT_SIGNOFF_REQUIRED` | `Adatvédelem – tanulói adatok és AI.md` |
| **G3 Moodle/H5P célkörnyezet** | pontos verziók + kritikus runtime tesztek | `IMPLEMENTATION_REQUIRED` | `LMS – H5P runtime acceptance.md` |
| **G4 Learner-facing nyitott mező = 0** | nincs `KITÖLTENDŐ`, ismeretlen kontakt, bizonytalan határidő vagy törött link a madrich által látható felületen | `IMPLEMENTATION_REQUIRED` | staging visszaaudit |
| **G5 Hozzáférhetőség** | mobil, billentyűzet, képernyőolvasó, zoom/reflow, felirat/leirat a tényleges renderen | `IMPLEMENTATION_REQUIRED` + `RUNTIME_VERIFIED` | a11y tesztjegyzőkönyv |
| **G6 Mozgalmi tartalom** | HUM-SOMER-01–03 lezárva az érintett részekhez | `HUMAN_DECISION_REQUIRED` | `Emberi jóváhagyás szükséges.md` |
| **G7 Regresszió** | repository tesztek, content integrity, média-manifeszt, helyi linkek és diff ellenőrzése zöld | `IMPLEMENTATION_REQUIRED` | CI / release-check |
| **G8 Ütemezés és support** | HUM-OPS-01–02 + HUM-A11Y-01 lezárva | `HUMAN_DECISION_REQUIRED` | központi schedule + „Segítség és kapcsolatok” blokk |

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
| **HUM-GOV-01** *(nem P0 release-gate; nyitott, jóváhagyásra vár)* | [#7 – Terepgyakorlat rubrika és KPI skálájának összehangolása](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/7) |

Az issue-k **nem helyettesítik a jóváhagyási bizonyítékot**. Lezáráskor az issue-ba a tényleges döntést, dátumot, jóváhagyót és bizonyítékot kell linkelni/rögzíteni; csak ezután tekinthető az adott gate zártnak.

## Staging-szabály

A staging buildben:

1. **nem találunk ki** gyermekvédelmi, privacy-, support- vagy mozgalmi adatot;
2. emberi döntés helyén **belső build-jelölő** maradhat, de ez nem kerülhet learner-facing nézetbe;
3. személyes adat helyett szintetikus tesztadatot használunk;
4. minden tényleges Moodle activity kap stabil build-ID-t és a létrehozás után rögzített Moodle `cmid`-t;
5. minden runtime-bizonyítást `IMPLEMENTATION_TEST_REQUIRED` állapotból csak tényleges teszteredmény mozdíthat `RUNTIME_VERIFIED` állapotba.

## Modul-specifikus élesítés

Egy modul szakmai jóváhagyása lehet moduláris, de a hozzá tartozó globális kapukat nem lehet megkerülni. Például az M1 stagingben teljesen felépíthető, miközben HUM-PRIV-01 még nyitott; valódi madrichnak viszont az M1 Assignment csak a jóváhagyott adatkezeléssel nyitható meg.

A safeguarding-tartalomra külön szabály vonatkozik: M3.3, M3.B és az M3/M7 gyermekvédelmi kapuelemek **éles használatához** az adott tartalomhoz közvetlenül szükséges **HUM-SAFE-01/02** döntések és szakértői jóváhagyás kötelező, **de ez nem szűkíti a globális G1-et**: learner-facing release csak akkor lehet, ha a teljes **HUM-SAFE-01–05** csomag lezárt.

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
- [ ] Learner pilot megtörtént kis csoporttal, a findingek javítva és újratesztelve.
- [x] A médiaregiszter a tartalmi freeze után újragenerálva és auditálva. **Bizonyíték:** determinisztikus `media_manifest.py build/check/reconcile` + sikeres teljes media CI (`36605020566`, 417 asset / 902 deliverable / 143 teszt).

## Merge ≠ staging ≠ release

A GitHub merge technikai esemény. A Moodle staging egy zárt megvalósítási és tesztkörnyezet. Az éles learner release külön, dátummal, jóváhagyókkal és runtime-bizonyítékokkal rögzített Go/No-Go döntés.
