# Release readiness – staging és élesítés

## Jelenlegi állapot: két verdikt

A gépi állapotot kizárólag a `python3 tools/content_integrity.py --release-report` két verdikt-sora adja (projektgazdai döntés, 2026-10-04; `Emberi jóváhagyás szükséges.md` 10. szakasz). Ez a dokumentum nem ír kézzel állapotot.

- **`MOODLE-BUILD-VERDICT`** (`NOT_READY` / `READY_FOR_STAGING_BUILD`): felépíthető-e a tananyag a zárt, szerkesztői Moodle-stagingben. A buildet meghatározó specnek késznek kell lennie: implementálható activity-definíciók, célkörnyezeti paraméterek, buildet érintő gyermekvédelmi, adatvédelmi és hozzáférhetőségi szabályok, és a release-kötelező médiához asset vagy elfogadott fallback (a „specifikáció zárt” nem igaz, amíg release-kötelező asset fallback nélkül nyitott jogi vagy gyermekvédelmi médiakapun áll; lásd: **Médiakapuk**). Objektív integritási hiba (G7) mellett a verdikt mindig `NOT_READY`. Olyan bizonyíték, amely csak a build vagy a runtime során keletkezhet, ezt a verdiktet nem blokkolja.
- **`LEARNER-RELEASE-VERDICT`** (`NO-GO` / `CONTENT_READY / MEDIA_PENDING` / `READY_FOR_CONTROLLED_PILOT`): odaadható-e a felépített rendszer valódi résztvevőknek kontrollált pilotként. Csak a tényleges build- és runtime-bizonyítékkal, a `FINAL_RELEASE_QA`-val és a go/no-go döntéssel zárható; build-készség nélkül mindig `NO-GO`. Ha már csak release-kötelező médiaasset áll átmeneti fallbackkel nyitott médiakapun, az állapot `CONTENT_READY / MEDIA_PENDING`.

Csupasz `READY` állapot nincs. A régi `RELEASE-VERDICT` sor egy release-ciklusig kompatibilitási alias, az értéke a `LEARNER-RELEASE-VERDICT`. A staginghez tesztfiókot és tesztadatot használunk; valódi madrih nem kap hozzáférést. Tervezési jegyzőkönyv: `01 Fejlesztés/04 Audit/2026-10-04 Release-modell v2 – Moodle build és learner release.md`.

**Életciklus (Q-REL-1):** `INTERNAL_STAGING → CONTROLLED_PILOT → GENERAL_RELEASE → PROGRAM_TRANSFER_VALIDATED`. A fázisváltást a release-jegyzőkönyv rögzíti (`Program terv.md` §9.3). A kontrollált pilot az első valódi tanulói release; a `GENERAL_RELEASE` a pilot-findingok javítása, újratesztelése és a go/no-go döntés után következik, és nem repo-verdikt. A program-transzfer release utáni validáció, nem release-kapu.

**Döntési és QA-lánc (Q-REL-3, módosítva 2026-10-04):** `OWNER_DECIDED → IMPLEMENTED → RUNTIME_VERIFIED → FINAL_RELEASE_QA → RELEASE_APPROVED`. A `SPEC_QA` korai vétó vagy tanácsadó ellenőrzés, nem build-kapu. A `FINAL_RELEASE_QA` release-kapu: ide tartozik a Memuna végső átnézése, a DPO release-ellenőrzése és a független a11y pre-flight. A HUM-tételek `LEZÁRVA` jelölése az `OWNER_DECIDED`-nak felel meg.

A két verdiktet nem szabad összemosni. A staging célja éppen az, hogy a Moodle/H5P megvalósítást, a completiont, a kapukat és a hozzáférhetőséget bizonyítsuk: a staging build ehhez a bizonyítékhoz vezet, nem a feltétele. A szervezeti döntések 2026-10-02 óta lezártak, de a futtatási és átvételi bizonyítékok hiánya ettől még változatlanul blokkolja a tanulói megnyitást.

## Élesítés előtti globális kapuk

A „Besorolás” oszlop a két verdikt szerinti helyet adja (2026-10-04): **BUILD** = a `MOODLE-BUILD-VERDICT` feltétele; **POST-BUILD** = build vagy runtime után keletkező bizonyíték; **FINAL_RELEASE_QA**, **RELEASE-EVIDENCE**, **SIGNOFF** = a `LEARNER-RELEASE-VERDICT` feltétele.

| Gate | Követelmény | Állapot típusa | Bizonyíték | Besorolás |
|---|---|---|---|---|
| **G1 Gyermekvédelem** | HUM-SAFE-01–05 lezárva; az M3 és a kapcsolódó biztonsági tartalmak (köztük M3.3, M3.B, M3-kapu, az M7 gyermekvédelmi részei) élesítés előtti átnézése: a Memuna egyszeri, írásos „átnéztem” bejegyzése a release-jegyzőkönyvben (lásd a táblázat alatt) | `HUMAN_DECISION_REQUIRED` + `EXPERT_SIGNOFF_REQUIRED` | `Gyermekvédelem – release gate.md` | HUM-SAFE és a gyermekvédelmi szabályok a specben: BUILD; a Memuna végső átnézése: FINAL_RELEASE_QA |
| **G2 Adatvédelem és kiskorúak** | HUM-PRIV-01–04 lezárva, activity-szintű adatleltár, adatvédelmi tájékoztató, hozzáférés, megőrzés/törlés; nyitott DPO-döntés: az LMS-Z-06 (Z.3 szöveges válaszai) megőrzési sora (BS-D6); az LMS-M2-07 (M2.3 záró mondat) kötelező, név szerinti tárolásának adatkategóriája (BIZT-R5; someres vonatkozásban a projektgazda) | `HUMAN_DECISION_REQUIRED` + `EXPERT_SIGNOFF_REQUIRED` | `Adatvédelem – tanulói adatok és AI.md` | HUM-PRIV, az adatleltár (Moodle-szerepkör/capability) és a tájékoztató szövege: BUILD; láthatósági és szerepkör-tesztek: POST-BUILD; a DPO release-ellenőrzése: FINAL_RELEASE_QA |
| **G3a Moodle/H5P célkörnyezet – spec** | célkörnyezeti paraméterek: H5P-integráció, content type-lista, plugin-lista, MCP, mechanizmusok tartalékúttal | `IMPLEMENTATION_REQUIRED` | `LMS – activity manifest.md` (nyitott build-spec tételek), `LMS – H5P runtime acceptance.md` | BUILD |
| **G3b Moodle/H5P célkörnyezet – runtime** | pontos verziók (környezeti rekord) + kritikus runtime tesztek | `RUNTIME_VERIFIED` | `LMS – H5P runtime acceptance.md` (Environment record, Teszt-állapot) | POST-BUILD |
| **G4a Learner-facing nyitott mező = 0 – forrás** | nincs `KITÖLTENDŐ`, ismeretlen kontakt, bizonytalan határidő vagy törött link a forrásban | `IMPLEMENTATION_REQUIRED` | `content_integrity.py` | BUILD |
| **G4b Learner-facing nyitott mező = 0 – renderelt felület** | ugyanez a madrih által látható, renderelt felületen | `RUNTIME_VERIFIED` | staging visszaaudit | POST-BUILD |
| **G5a Hozzáférhetőség – spec és build-beállítások** | a hozzáférhetőségi sztenderd; autoplay, Auto continue, iframe-cím, AD-besorolás | `IMPLEMENTATION_REQUIRED` | `LMS – hozzáférhetőségi sztenderd.md` | BUILD |
| **G5b Hozzáférhetőség – renderteszt** | mobil, billentyűzet, képernyőolvasó, zoom/reflow, felirat/leirat a tényleges renderen | `RUNTIME_VERIFIED` | a11y tesztjegyzőkönyv; `LMS – H5P runtime acceptance.md` (Teszt-állapot) | POST-BUILD; a független pre-flight és a hozzáférhetőségi gazda: FINAL_RELEASE_QA |
| **G6 Mozgalmi tartalom** | HUM-SOMER-01–03 lezárva az érintett részekhez | `HUMAN_DECISION_REQUIRED` | `Emberi jóváhagyás szükséges.md` | BUILD (lezárt döntés) |
| **G7 Regresszió** | repository tesztek, content integrity, média-manifeszt, helyi linkek és diff ellenőrzése zöld | `IMPLEMENTATION_REQUIRED` | CI / release-check | BUILD (`ERROR` = 0) |
| **G8 Ütemezés és support** | HUM-OPS-01–02 + HUM-A11Y-01 lezárva | `HUMAN_DECISION_REQUIRED` | központi schedule + „Segítség és kapcsolatok” blokk | a naptár szabályai: BUILD; a `SCHEDULE_TO_RESYNC` dátumok beállítása tanulónak nyitás előtt: RELEASE-EVIDENCE (PILOT-2: a dátumfüggő activity felépíthető, de valódi tanulónak nem nyitható meg, amíg a dátum nincs konfigurálva; `Emberi jóváhagyás szükséges.md` 11. szakasz); a valódi kontaktok: RELEASE-EVIDENCE (stagingben belső build-jelölő megengedett); a blokk megjelenése: POST-BUILD |
| **Go/No-Go a kontrollált pilotra** | dátummal, jóváhagyókkal, a runtime-bizonyítékokra hivatkozó döntés | `RELEASE_APPROVED` | release-jegyzőkönyv (`Program terv.md` §9.3) | SIGNOFF |

**Projektgazdai döntések a kapukhoz (2026-10-02).** A G1, G2, G6 és G8 HUM-feltétele (a „… lezárva” rész) teljesült: a tételek lezártak (`Emberi jóváhagyás szükséges.md`), a megnevezett szerepek későbbi ellenőrzése vétó / minőségellenőrzés (QA), nem új döntési kapu. A kapuk ettől még nem zártak: mindegyik csak a táblázat „Bizonyíték” oszlopa szerinti bizonyítékkal és a tracker-issue-ban rögzített lezárással zárul (lásd: GitHub release-tracker).

- **G1 – jóváhagyói rend:** a gyermekvédelmi jóváhagyás egyetlen felelős jóváhagyója a **Memuna** (a Somer gyermekvédelmi felelőse); a programvezető operatív társdöntő, jogi szakértő csak jogi kérdésben dönt. A képzés elsődleges normatív gyermekvédelmi dokumentuma a **Gyermekvédelmi működési standard v1.0** (a HUM-SAFE-01…05 együtt; `Gyermekvédelem – release gate.md` §5.1).
- **G1 – a Memuna átnézése élesítés előtt:** **projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a Memuna. Élesítés előtti minőségellenőrzési (QA) lépés a gyermekvédelmi tartalmakra (M3.3, M3.B, M3-kapu, az M7 gyermekvédelmi részei, valamint minden olyan tananyagelem, amely bántalmazásról, önsértésről, groomingról, szexuális/romantikus határátlépésről, súlyos veszélyeztetettségről vagy külső jelzésről tanít; `Gyermekvédelem – release gate.md` §2): a Memuna egyszer, írásban rögzíti a release-jegyzőkönyvben (`Program terv.md` §9.3), hogy a kész anyagot átnézte („átnéztem”). Ez nem a policy újradöntése, hanem a kész anyag ellenőrzése (`Gyermekvédelem – release gate.md` §2). A G1 nyitott marad, amíg ez az átnézés meg nem történt.
- **G5/G8 – hozzáférhetőségi felelős (HUM-A11Y-01):** külön szerep; a szerző nem hagyja jóvá a saját anyagát. A felelős (accountable) hozzáférhetőségi gazda a **Ros Hinuh** (jelenleg Lili); az élesítés előtti, független második ellenőrző (pre-flight) **Marci**. A pre-flight ellenőrzőnek ismernie kell a WCAG- és H5P-követelményeket, és nem lehet az ellenőrzött anyag szerzője. Utólagos ellenőrzés (vétó/QA): a programvezető.
- **G8 – ütemezés és support (HUM-OPS-01–02):** a naptár a 2026-10-05-i projektgazdai döntés szerint (`Emberi jóváhagyás szükséges.md` 11. szakasz; a HUM-OPS-01 2026-10-02-i dátumait felülírja): authoring/build 2026-10-06, az első kontrollált pilot cohortjának indulása 2026-10-10; minden további dátum `SCHEDULE_TO_RESYNC` (programvezetői új ütemezés). Az online félév teljesítése bevárja az M6/M7 javítási útját (projektgazdai döntés, 2026-10-02). A teljes központi naptár (péntekek, kapu-beadások, megerősítések, téli szünet) az `LMS – activity manifest.md` §7-ében (Központi ütemezés) él. A „Segítség és kapcsolatok” blokk négy, szerep szerinti kontaktot ad (technikai segítség, tanulási/programkontakt, a kijelölt mentor, és ettől külön a Memuna); a mentori kapacitás kemény plafonja 1:8. A HUM-OPS-01–02 (2026-10-02) utólagos ellenőrzése (vétó/QA): a programvezető; a 2026-10-05-i pilot-ütemezés jegyzőkönyve utólagos ellenőrzőt nem nevez meg.

### Médiakapuk

**Projektgazdai döntés (2026-10-02):** a jogi és gyermekvédelmi médiakapuk blokkolják az általuk érintett tanulói asset release-ét. A teljes release csak akkor **READY**, ha minden release-hatókörű médiakapu zárt, vagy az érintett assetet eltávolították, illetve helyettesítették. Külön állapot lehet: **CONTENT_READY / MEDIA_PENDING**. „Specifikáció zárt” nem igaz, amíg kötelező asset nyitott jogi kapun áll. Utólagos ellenőrzés (vétó/QA): a release owner és a jogi/adatvédelmi felelős.

**2026-10-04 óta** (Q-MED-1, RM-D3, RM-D4): a „READY” itt `READY_FOR_CONTROLLED_PILOT`, és a médiakapu asset-szintű, fallbackkel. Release-kötelező az A fázis (tanulói szöveg, natív H5P, szükséges segédlet, pedagógiai diagram/grafika, alt- és szöveges ekvivalensek). Ha egy A fázisú asset nyitott jogi vagy gyermekvédelmi médiakapun áll, fallback nélkül a buildet blokkolja, átmeneti fallbackkel `CONTENT_READY / MEDIA_PENDING`. A B (narráció) és a C fázis (videó, avatar, karakterjelenet, márkás polish) a Q-MED-1 szerint mindig fallbackkel jár, ezért nem blokkol. Amíg a média-manifest nem viseli a `release_phase` mezőt, a gép a narrációt B-nek, a videót C-nek, minden más assetet A-nak tekint.

Ilyen kapuk: a **HUM-MEDIA-02** (hangjogosultság; alkapui: J1, J2, V1, V3) és a **HUM-MEDIA-03** (avatar- és médiajogok; gyermekvédelmi vagy krízis-HOOK-ban nincs készlet-AI-beszélőfej). A két döntés 2026-10-02-án lezárult (`Emberi jóváhagyás szükséges.md`), de a médiakapuk a bizonyítékig nyitva maradnak: az alkapuk állapotát a `Média-assetek/RIGHTS-EVIDENCE.md` 1/A.5. pontja tartja nyilván, a D11 a hangjogosultsági bizonyítékig blokkolt, az E-9 jogi felülvizsgálaton van (`LEGAL_REVIEW_REQUIRED`). A felelős- és bizonyíték-mezők (a bizonyíték megléte és nem személyes hivatkozása): `Média-assetek/RIGHTS-EVIDENCE.md`; a valódi név, a szerződés vagy hozzájárulás, a hatókör és a dátum a korlátozott hozzáférésű jogosultsági nyilvántartásba tartozik, nem a repóba. A hangjogosultsági nyilvántartás helye: Google Workspace Shared Drive → `Restricted / Rights / Voice`, `VOICE-RIGHTS-REGISTER`; valódi név nem kerül a Gitbe.

A **vizuális rendszer** (HUM-MEDIA-01; a `Média-assetek/PRODUCTION-DECISIONS.md` D1 döntése) nem jogi vagy gyermekvédelmi médiakapu, hanem gyártási feltétel. **Projektgazdai döntés (2026-10-02):** a D1 lezárva – a hivatalos Somer-paletta, a 2022-es arculati kézikönyv és a hivatalos SVG színgenerációja a kánon; a produkciós rendszer a B változat (Source Sans 3 + produkciós semleges skála); a szín soha nem önálló jelentéshordozó. Ezzel az R5 nyitott értéke (a paletta) eldőlt; a produkciós szabály kitöltése, az asset-szintű R5-blokkolók kivezetése és a médiaállapot darabszámai a média-build után frissülnek. Utólagos ellenőrzés (vétó/QA): a kreatív/márkafelelős.

## GitHub release-tracker

A repository-specifikáció és a tényleges lezárási munka külön réteg. A nyitott kapukat ezek az issue-k követik:

| Kapu / döntés | Tracker |
|---|---|
| **G1 / HUM-SAFE-01–05** | [#1 – Gyermekvédelmi release gate és szakértői jóváhagyás](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/1) |
| **G2 / HUM-PRIV-01–04** | [#2 – Adatvédelem, kiskorúak, reflexiók, felvétel és külső AI](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/2) |
| **G3a/G3b + G5a/G5b** | [#3 – Moodle/H5P célverziók és runtime acceptance](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/3) |
| **G4 + G8 / HUM-OPS-01–02 + HUM-A11Y-01** | [#4 – Moodle build, dátumok, kontaktok és előfeltételek](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/4) |
| **G6 / HUM-SOMER-01–03** | [#6 – Mozgalmi tartalom jóváhagyása](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/6) |
| **G7** | GitHub Actions + release-check az élesítendő commiton |
| **Program-transzfer (életciklus, nem release-kapu)** | [#9 – Terepgyakorlat és learner pilot](https://github.com/hasomerhacairhu/modszertani-kepzes/issues/9) |
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

A safeguarding-tartalomra külön szabály vonatkozik: M3.3, M3.B és az M3/M7 gyermekvédelmi kapuelemek **éles használatához** az adott tartalomhoz közvetlenül szükséges **HUM-SAFE-01/02** döntések és a Memuna élesítés előtti, írásos átnézése (QA-lépés a release-jegyzőkönyvben, lásd G1) kötelező, **de ez nem szűkíti a globális G1-et**: learner-facing release csak akkor lehet, ha a teljes **HUM-SAFE-01–05** csomag lezárt.

## Legkisebb értelmes staging-szelet

**M0 + M1**, belső tesztfiókokkal.

Miért ez a minimum:
- M0 bizonyítja a kurzusnavigációt, H5P completiont, fórumot és a puha completion-logikát;
- M1 hozzáadja az Assignmentet, rubrikát, javítás/újrabeadás folyamatot és az összetett teljesítési feltételt;
- együtt már tesztelhető a modulok közötti unlock, a mobil/a11y viselkedés és a `moodle-ai-mcp` build-visszaolvasás;
- M3 gyermekvédelmi kockázata és az M7 összegző feladat összetettsége nélkül ad valódi technikai szeletet;
- az első staging **nem vár narrációra, AI-videóra vagy arculati grafikára**; a média-fallbackeket a `Média-assetek/RELEASE-MEDIA-STATUS.md` rögzíti.

**A staging-szelet nem learner release.** A tesztelők szerkesztői/QA tesztfiókok. A kontrollált pilot (`CONTROLLED_PILOT`, Q-REL-1) ettől külön életciklus-fázis: az első valódi tanulói release, `READY_FOR_CONTROLLED_PILOT` verdikttel és go/no-go döntéssel.

## Program-transzfer (életciklus, nem release-kapu)

A Q-REL-1 szerint a hat valós terepi peula + mentori ciklus release utáni programvalidáció (`PROGRAM_TRANSFER_VALIDATED`). A gépi riport `LIFECYCLE` sorként jelzi; egyik verdiktet sem blokkolja.

- [ ] A félév végi `Peula v2` után működik a `Terepgyakorlat – 2. félév.md` szerinti hat valós, 60–90 perces peula + mentori visszajelzési ciklus. <!-- gate: lifecycle -->
- Learner pilot kis csoporttal: későbbi mérés, **nem release-kapu** (projektgazdai döntés, 2026-10-02). A V1 időkereteket finomíthatja, de nem kell rá várni. (2026-10-04 óta a kontrollált pilot az első valódi tanulói release, Q-REL-1.)
- [x] A médiaregiszter a tartalmi freeze után újragenerálva és auditálva. **Bizonyíték:** determinisztikus `media_manifest.py build/check/reconcile` + sikeres teljes media CI (`36605020566`, 417 asset / 902 deliverable / 143 teszt).

## Learner-release bizonyítékok (gépileg követett)

Az alábbi tételeket a `content_integrity.py --release-report` a jelölésük szerint számolja; a `LEARNER-RELEASE-VERDICT`-et blokkolják, a buildet nem.

- [ ] **G4b:** a renderelt, madrih által látható felület visszaauditja kész: nincs nyitott mező, ismeretlen kontakt, bizonytalan határidő vagy törött link (bizonyíték: a staging visszaaudit jegyzőkönyve). <!-- gate: post-build -->
- [ ] **Go/No-Go a kontrollált pilotra:** dátummal, jóváhagyókkal és a runtime-bizonyítékokra hivatkozva rögzítve a release-jegyzőkönyvben (`Program terv.md` §9.3). <!-- gate: signoff -->

## Merge ≠ staging ≠ release

A GitHub merge technikai esemény. A Moodle staging egy zárt megvalósítási és tesztkörnyezet; a `READY_FOR_STAGING_BUILD` nem release-jóváhagyás. Az éles learner release (`CONTROLLED_PILOT`) külön, dátummal, jóváhagyókkal és runtime-bizonyítékokkal rögzített Go/No-Go döntés.
