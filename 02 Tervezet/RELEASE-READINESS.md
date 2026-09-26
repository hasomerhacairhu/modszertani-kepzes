# Release readiness – staging és élesítés

## Jelenlegi állapot

- **Moodle staging:** **READY WITH NAMED HUMAN GATES** – a tartalmi specifikáció zárt, szerkesztői stagingben felépíthető és tesztelhető. A staginghez tesztfiókot és tesztadatot használunk; valódi madrich nem kap hozzáférést.
- **Learner-facing release:** **NO-GO** – az alábbi emberi, szervezeti és futtatási kapuk bizonyíték nélkül nem zárhatók le.

A két állapotot nem szabad összemosni. A staging célja éppen az, hogy a Moodle/H5P megvalósítást, a completiont, a kapukat és a hozzáférhetőséget bizonyítsuk. A szervezeti döntések hiánya ettől még változatlanul blokkolja az éles megnyitást.

## Élesítés előtti globális kapuk

| Gate | Követelmény | Állapot típusa | Bizonyíték |
|---|---|---|---|
| **G1 Gyermekvédelem** | HUM-SAFE-01–04 lezárva; M3 és kapcsolódó biztonsági tartalmak szakértői jóváhagyása | `HUMAN_DECISION_REQUIRED` + `EXPERT_SIGNOFF_REQUIRED` | `Gyermekvédelem – release gate.md` |
| **G2 Adatvédelem és kiskorúak** | HUM-PRIV-01–04 lezárva, activity-szintű adatleltár, notice, hozzáférés, retention/törlés | `HUMAN_DECISION_REQUIRED` + `EXPERT_SIGNOFF_REQUIRED` | `Adatvédelem – tanulói adatok és AI.md` |
| **G3 Moodle/H5P célkörnyezet** | pontos verziók + kritikus runtime tesztek | `IMPLEMENTATION_REQUIRED` | `LMS – H5P runtime acceptance.md` |
| **G4 Learner-facing nyitott mező = 0** | nincs `KITÖLTENDŐ`, ismeretlen kontakt, bizonytalan határidő vagy törött link a madrich által látható felületen | `IMPLEMENTATION_REQUIRED` | staging visszaaudit |
| **G5 Hozzáférhetőség** | mobil, billentyűzet, képernyőolvasó, zoom/reflow, felirat/leirat a tényleges renderen | `IMPLEMENTATION_REQUIRED` + `RUNTIME_VERIFIED` | a11y tesztjegyzőkönyv |
| **G6 Mozgalmi tartalom** | HUM-SOMER-01–03 lezárva az érintett részekhez | `HUMAN_DECISION_REQUIRED` | `Emberi jóváhagyás szükséges.md` |
| **G7 Regresszió** | repository tesztek, content integrity, média-manifeszt, helyi linkek és diff ellenőrzése zöld | `IMPLEMENTATION_REQUIRED` | CI / release-check |
| **G8 Ütemezés és support** | HUM-OPS-01–02 + HUM-A11Y-01 lezárva | `HUMAN_DECISION_REQUIRED` | központi schedule + „Segítség és kapcsolatok” blokk |

## Staging-szabály

A staging buildben:

1. **nem találunk ki** gyermekvédelmi, privacy-, support- vagy mozgalmi adatot;
2. emberi döntés helyén **belső build-jelölő** maradhat, de ez nem kerülhet learner-facing nézetbe;
3. személyes adat helyett szintetikus tesztadatot használunk;
4. minden tényleges Moodle activity kap stabil build-ID-t és a létrehozás után rögzített Moodle `cmid`-t;
5. minden runtime-bizonyítást `IMPLEMENTATION_TEST_REQUIRED` állapotból csak tényleges teszteredmény mozdíthat `RUNTIME_VERIFIED` állapotba.

## Modul-specifikus élesítés

Egy modul szakmai jóváhagyása lehet moduláris, de a hozzá tartozó globális kapukat nem lehet megkerülni. Például az M1 stagingben teljesen felépíthető, miközben HUM-PRIV-01 még nyitott; valódi madrichnak viszont az M1 Assignment csak a jóváhagyott adatkezeléssel nyitható meg.

A safeguarding-tartalomra külön szabály vonatkozik: M3.3, M3.B és az M3/M7 gyermekvédelmi kapuelemek **éles használatához** HUM-SAFE-01/02 és szakértői jóváhagyás kötelező.

## Legkisebb értelmes staging pilot

**M0 + M1**, belső tesztfiókokkal.

Miért ez a minimum:
- M0 bizonyítja a kurzusnavigációt, H5P completiont, fórumot és a puha completion-logikát;
- M1 hozzáadja az Assignmentet, rubrikát, javítás/újrabeadás folyamatot és az összetett mastery-feltételt;
- együtt már tesztelhető a modulok közötti unlock, a mobil/a11y viselkedés és a `moodle-ai-mcp` build-visszaolvasás;
- M3 safeguarding-kockázata és az M7 capstone összetettsége nélkül ad valódi technikai szeletet.

**A pilot nem learner release.** A tesztelők szerkesztői/QA tesztfiókok.

## Program-transzfer

- [ ] A félév végi `Peula v2` után működik a `Terepgyakorlat – 2. félév.md` szerinti hat valós, 60–90 perces peula + mentorfeedback ciklus.
- [ ] Learner pilot megtörtént kis csoporttal, a findingek javítva és újratesztelve.
- [ ] A médiaregiszter a tartalmi freeze után újragenerálva és auditálva.

## Merge ≠ staging ≠ release

A GitHub merge technikai esemény. A Moodle staging egy zárt megvalósítási és tesztkörnyezet. Az éles learner release külön, dátummal, jóváhagyókkal és runtime-bizonyítékokkal rögzített Go/No-Go döntés.
