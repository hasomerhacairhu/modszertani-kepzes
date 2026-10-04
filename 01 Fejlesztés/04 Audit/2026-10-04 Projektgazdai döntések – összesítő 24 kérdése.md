# Projektgazdai döntések — az összesítő 24 nyitott kérdése (2026-10-04)

> **Audit trail, nem tananyag.** A projektgazda válasza a `2026-10-04 Kérdések és döntések – összesítő.md` I. részének
> 24 nyitott kérdésére (Q-REL-1…4, Q-GH-1…4, Q-PED-1…7, Q-LEG-1…5, Q-MED-1…4). A projektgazda a választ beillesztett
> szövegként adta át a munkamenetben, majd külön kérdésre (AskUserQuestion) megerősítette: **„Igen, mind a 24”** — „Ezek
> az én döntéseim; rögzítsd szó szerint, és frissítsd az összesítőt (projektgazdai döntésre váró kérdés: 0).” A
> megerősítő kérdés kikötése: a jogi és adatvédelmi pontoknál (Q-LEG-1, -2, -4, -5) operatív projektgazdai döntés, a
> jogi és DPO-átnézés bizonyíték-kapu marad; a CODEOWNERS-be csak valódi GitHub-fiókok kerülnek, amelyeket a projektgazda
> ad meg.

**Jóváhagyta:** projektgazda · **Dátum:** 2026-10-04

**Utólagos ellenőrzés (vétó/QA), szerepenként:** jogi felelős (Q-LEG-1), Memuna + DPO (Q-LEG-2), DPO (Q-LEG-3…5),
módszertani felelős (Q-PED-2, -4, -5), modulgazda (Q-PED-3), Memuna + programvezető (Q-PED-6), hozzáférhetőségi felelős
(Q-MED-2, -3), release-felelős (Q-REL-1…3). Vétónál a tétel újranyílik.

**A munkamenetben ellenőrizve (2026-10-04):** az #6 issue `CLOSED` (2026-10-02T19:41:47Z), a #12-re (`cfeef1e`)
hivatkozó lezáró kommenttel — a Q-GH-3 tehát nem volt nyitott kérdés, az összesítő tévesen tartotta nyitottnak.

---

## A projektgazda válasza, szó szerint

A 24 tételt végigellenőriztem a csatolt összesítővel, a jelenlegi `main` ággal, git history-val, issue-kkal, korábbi projektgazdai döntésekkel, a releváns levelezéssel/naptárral és a jogi/technikai pontoknál külső forrásokkal. Az összesítőben felsorolt kérdések itt vannak egyben. 2026-10-04 Kérdések és dönt…

**Ezekkel a projektgazdai döntési kérdések lezárhatók.** Néhány tételről közben kiderült, hogy valójában már korábban eldőlt vagy végrehajtódott.

### A. Program és release

| ID | Végső válasz |
|---|---|
| **Q-REL-1** | **Legyen külön `CONTROLLED_PILOT`.** Állapotmodell: `INTERNAL_STAGING → CONTROLLED_PILOT → GENERAL_RELEASE → PROGRAM_TRANSFER_VALIDATED`. A **6 valós terepi peula nem release előtti kapu**, hanem a második féléves programtranszfer utólagos validációja. A kontrollált pilot az első valódi tanulói release, utána a pilot-findingok javítása és újratesztelése kell a general release-hez. Az issue #9 és a `content_integrity.py` ehhez igazítandó. |
| **Q-REL-2** | **Nem kell pufferhét.** Bukott éles kapu után a következő modul **tanulási része megnyílhat**, de a következő éles kapu lezárása és minden, a hiányzó kompetenciára épülő magas tétű előrehaladás blokkolt marad. A már elfogadott út marad: F-peula a megerősítés utáni hétfőn, javító határidő szerda 18:00. |
| **Q-REL-3** | **Igen, bontsuk fel a `LEZÁRVA` állapotot.** Kánoni lánc: `PROPOSED → OWNER_DECIDED → EXPERT_QA → IMPLEMENTED → RUNTIME_VERIFIED → RELEASE_APPROVED`. Legyen még `SUPERSEDED` és `REOPENED`. Az `OWNER_DECIDED` tehát nem jelent release-ready állapotot. |
| **Q-REL-4** | **Péntek 18:00, Europe/Budapest.** Ez legyen a kanonikus kezdési idő. Nem találtam ezzel ellentétes időpontot sem a repóban, sem a releváns levelezésben/naptárban, és pontosan konzisztens a már elfogadott „csütörtök 18:00 = legalább 24 órával a következő fix alkalom előtt” szabállyal. |

A Q-REL-1 fontos szemantikai javítás: a pilot nem „release előtti nem-release”, hanem **egy korlátozott release állapot**. Így megszűnik a jelenlegi körkörös logika.

### B. GitHub és repó

| ID | Végső válasz |
|---|---|
| **Q-GH-1** | **Végrehajtandó, a döntés már megszületett.** `git filter-repo` az összes érintett névre és refre, force push, GitHub Supporttal cache/PR-ref tisztítás ahol szükséges, majd minden aktív clone újraklónozása. **Ezt kell megcsinálni a ruleset aktiválása előtt.** |
| **Q-GH-2** | **Main ruleset kötelező.** PR kötelező, legalább 1 approval, CODEOWNER approval, `content-integrity` + `media-manifest` kötelező check, unresolved conversation tiltás, branch deletion és force push tiltás. Squash/rebase kikapcsolható, a korábbi döntés szerint merge commit marad. CODEOWNERS: default `@heymarcell`; safeguarding → Memuna + helyettes/Ros Hinuh; privacy/AI → DPO/jogi felelős; media → producer + szükség szerint a11y-felelős; `tools/` és `.github/` → repo-admin + projektgazda. A még nem létező GitHub team/user handle-eket nem szabad kitalálni, ezeket a tényleges accountokkal kell kitölteni. A live ellenőrzés szerint a `main` **jelenleg nem protected és nincs ruleset**. GitHub támogatja a required PR-t, code-owner review-t, required checks-et és force-push tiltást rulesetben. [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets?utm_source=chatgpt.com) |
| **Q-GH-3** | **Már lezárt, törlendő a nyitott listából.** A #6 issue 2026-10-02 óta `CLOSED`, és már van rajta korrekt lezáró komment, amely a #12 merge-re és a projektgazdai döntésekre hivatkozik. **Nem kell utólag hamisan kipipálni a régi AC-ket és nem kell újranyitni.** |
| **Q-GH-4** | **Igen mindháromra.** Rövid `SECURITY.md`, rövid `CONTRIBUTING.md`, Dependabot. A repóban jelenleg nincs package/requirements lockfile, ezért a Dependabot elsődlegesen `github-actions` heti frissítést kapjon. A workflow `actions/checkout@v7` és `actions/setup-python@v7` hivatkozásait teljes commit SHA-ra kell pinelni, mert GitHub szerint ez az egyetlen immutable action-referencia. Az `openpyxl` CI-dependency kapjon tesztelt, fix verziót. [GitHub Docs](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/auto-update-actions?learn=dependency_version_updates&utm_source=chatgpt.com) |

### C. Értékelés és pedagógia

| ID | Végső válasz |
|---|---|
| **Q-PED-1** | **Nem nyitjuk újra a HUM-GOV-01-et.** Marad a 2026-10-02-i döntés: mind a 6 terepi alkalom számít, az **egyéni kötelező minimum kizárólag a „biztonság és határtartás” soron ≥1**. Az 1,6/2 átlag program-KPI, nem egyéni bukási feltétel. Nem vezetünk be utólag „minden sor ≥1” követelményt. |
| **Q-PED-2** | **A soronkénti 0/1/2 leírás legyen az alábbi rubric.** Lásd közvetlenül a táblázat után. |
| **Q-PED-3** | **2 + 8 + 5 perc = 15 perc.** A korábbi döntésből a 3 kártya már kánon. A fennmaradó időhibát úgy zárjuk, hogy a kiscsoportos munka 10 → **8 perc**, a közös átbeszélés pedig fix **5 perc, 3 kártyával**. |
| **Q-PED-4** | **Igen.** Kerüljön be: „**A modell szemüveg, nem menetrend: egy valódi csoport visszaléphet, átugorhat szakaszt, és egy helyzet többféleképpen is olvasható.**” |
| **Q-PED-5** | **Igen, kell forrásjegyzék.** Minimum Dunlosky et al. 2013 a retrieval practice + distributed practice összegzésére, Cepeda et al. 2006 az elosztott gyakorlásra, Rowland 2014 a testing/retrieval effectre. A „kutatások szerint” mondat ezekre mutasson, ne legyen forrás nélküli általánosítás. [Sage Journals](https://journals.sagepub.com/doi/pdf/10.1177/1529100612453266?utm_source=chatgpt.com) |
| **Q-PED-6** | **Ne nevezzük modified Angoffnak.** Új név: **„strukturált szakértői küszöb-megállapítás (Angoff-elemekkel)”**. Maradhat a két szakértő, Memuna + módszertani lektor, majd a pilot itemadatai alapján utólagos kalibráció. |
| **Q-PED-7** | **Igen, az `M1.1-NAR-05` is D-17.3 hatálya alá tartozik.** A mért narrációs idő és a tanuló gondolkodási/reflexiós ideje két külön időtétel. A VO-mérés csak a hangsáv slotját módosíthatja, a gondolkodási időt nem eheti meg. |

#### Q-PED-2: terepgyakorlati rubrika

A jelenlegi 9 rubrikasorhoz ezt rögzíteném:

| Sor | 0 = Még nem | 1 = Rendben | 2 = Erős |
|---|---|---|---|
| **Cél és alignment** | A cél nem világos vagy a tevékenység nem ezt szolgálja. | A cél világos, a fő lépések ehhez kapcsolódnak. | A cél, a tevékenység és a lezárás tudatosan egymásra épül. |
| **Instrukció / keretezés** | A kvuca nem tudja biztosan, mit és hogyan kell csinálni. | Érthető feladat, szabályok és keretek. | Rövid, pontos instrukció, megértésellenőrzéssel és tiszta átmenetekkel. |
| **Kvuca-reakciók megfigyelése** | Lényeges reakciókat nem vesz észre vagy címkékkel értelmez. | Észreveszi a releváns reakciókat és szükség esetén reagál. | A halkabb résztvevőket is olvassa, megfigyelésből dolgozik és ezek alapján adaptál. |
| **Facilitálás és kérdezés** | Dominálja vagy szétesni hagyja a folyamatot. | Érthető kérdésekkel és megfelelő részvétellel vezeti. | Tudatos kérdéssorral mélyít, több hangot behoz, kényszerítés nélkül. |
| **Idő / tér adaptáció** | Az idő vagy tér problémája miatt sérül a cél vagy a keret. | Szükség esetén módosítja a tempót vagy elrendezést. | Előre érzékeli és rugalmasan kezeli a helyzetet a cél elvesztése nélkül. |
| **Inkluzivitás** | Elkerülhető részvételi akadály vagy kirekesztő helyzet marad. | Van reális részvételi alternatíva és figyel a különböző igényekre. | Proaktívan úgy tervez és adaptál, hogy többféle részvételi mód működjön stigmatizálás nélkül. |
| **Biztonság és határtartás** | Biztonsági minimum sérül, vagy nem tartja a madrih szerephatárát. | Betartja a biztonsági szabályokat, felismeri, mikor kell megállítani vagy továbbjelezni. | Előre keretez, megelőzhető kockázatokat csökkent, és magabiztosan alkalmazza a megfelelő jelzési utat. |
| **Visszajelzés felhasználása** | A korábbi visszajelzés nem jelenik meg a következő alkalomban. | Legalább egy konkrét korábbi pontot láthatóan átvezet. | Átvezeti, majd azt is értékeli, hogy a változtatás milyen hatást hozott. |
| **Reflektív javítás** | A reflexió általános, konkrét következő lépés nélkül. | Megnevez egy konkrét erősséget, fejlesztendő pontot és következő lépést. | A tervet összeveti a megfigyelt hatással és konkrét, ellenőrizhető következő próbát fogalmaz meg. |

A 0 pont nem „nem tetszett a stílusa”, hanem **megfigyelhető kompetenciahiány** legyen.

### D. Jog, adatvédelem, AI

| ID | Végső válasz |
|---|---|
| **Q-LEG-1** | **A „csak deployer” állítást töröljük.** Operatív besorolás: a Somer **legalább deployer** az OpenAI rendszerével kapcsolatban, de a saját néven működtetett, saját Moodle/backendbe integrált Somer AI-segéd esetében **provider/downstream provider szerep is felmerül**. Az AI Act definíciója szerint provider az is, aki AI-rendszert saját néven fejlesztet és szolgálatba állít, downstream provider pedig az idegen AI-modellt saját AI-rendszerbe integráló provider. Addig a szigorúbb, kettős szerepet feltételező compliance legyen az alap, amíg a jogi felelős ezt le nem zárja. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng?utm_source=chatgpt.com) |
| **Q-LEG-2** | **V1 tartalmi kapu is, és a VO D-08 nem fedi le.** D-08 az AI-transzparencia címkézését rendezi. A V1-nek külön, tényleges gondviselői tájékoztatást kell tartalmaznia a szintetikus narráció természetéről, céljáról, arról, hogy tanulói hang nem kerül a hangszolgáltatóhoz, milyen harmadik fél vesz részt a gyártásban, és kihez lehet fordulni kérdéssel. Nem szabad olyan jogtisztasági állítást beleírni, amelyhez a bizonyíték még hiányzik. Memuna + DPO QA kell. |
| **Q-LEG-3** | **Igen.** A V2 hozzájárulásban legyen külön nyilatkozat: „nagykorú vagyok / a 18. életévemet betöltöttem és jogosult vagyok e hozzájárulást megadni”. A központi nyilvántartás továbbra is csak `ellenőrizve: igen/nem + dátum + ellenőrző szerepe` adatot tartson. Születési dátum vagy igazolványmásolat ne kerüljön bele. |
| **Q-LEG-4** | A **név nélkül begyűjtött papír munkalapnál** és a **név nélküli hanih-visszajelzésnél** nincs GDPR 6. cikk szerinti jogalap, **ha ténylegesen anonimak**, mert a GDPR nem vonatkozik valóban anonim információra. Ha a digitális megoldás accounttal, IP-vel vagy más adattal visszaazonosítható, akkor nem anonim, és a projekt meglévő alaplogikája szerint **jogos érdek + DPO érdekmérlegelés** legyen. A mentori fejlesztési jegyzet jogalapja továbbra is jogos érdek. [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?toc=OJ%3AL%3A2016%3A119%3A&uri=uriserv%3AOJ.L_.2016.119.01.0001.01.ENG&utm_source=chatgpt.com) |
| **Q-LEG-5** | **Moodle Feedback legyen a QR-kilépőkártya szolgáltatója**, ne új külső SaaS. `Record user names = Anonymous`, **ne legyen completion-feltétel**, a tanulói tájékoztató pedig ne nevezze valóban anonimnak, mert Moodle bejelentkezett használatnál az adatbázisban továbbra is rögzítheti a userid-t. A nyers válaszokat **90 napig**, utána törlés, csak aggregált eredmény maradjon. A QR mellett mindig legyen szöveges URL. Moodle saját dokumentációja is külön figyelmeztet arra, hogy az „Anonymous usernames” mód nem valódi technikai anonimitás. [Moodle Docs](https://docs.moodle.org/401/en/Feedback_FAQ?utm_source=chatgpt.com) |

A Q-LEG-1 esetében ez **operatív projektgazdai döntés, nem végleges jogi szakvélemény**. A jogi QA továbbra is release-bizonyíték.

### E. Média és hang

| ID | Végső válasz |
|---|---|
| **Q-MED-1** | **Elfogadjuk az A/B/C média-MVP-t.** **A fázis, release-kötelező:** tanulói szöveg, natív H5P, szükséges segédlet, pedagógiai diagram/grafika és valamennyi szükséges alt/szöveges ekvivalens. **B fázis:** csak pedagógiailag indokolt narráció, minden esetben a szükséges leirattal/felirattal. **C fázis:** videó, avatar, karakterjelenet, márkás polish csak ott, ahol bizonyított tanulási funkciója van. A C fázis jogfüggő eleménél A/B-s statikus vagy szöveges fallback legyen. **Nem a 415 asset vagy a 903 deliverable teljes legyártása a release-feltétel.** A manifeszt kapjon `release_phase: A/B/C` mezőt, és onnantól az legyen a scope-freeze. |
| **Q-MED-2** | **Besorolás:** `M1.1-NAR-03` = animáció hangsávja; `M1.2-NAR-02` = animáció hangsávja; `M1.2-NAR-03` = storyboard/animáció hangsávja; `M3.1-NAR-02` = animált Tuckman-ábra hangsávja. Ezekhez **felirat + leirat** kell. `M4.1-NAR-02` a jelenlegi spec alapján **önálló slide-narráció**, nincs időzítési/szinkron-kontraktusa az animált DIA-01-gyel, ezért VO D-19 szerint mellette látható leirat kell. Ha később ténylegesen az animációhoz szinkronizáljuk, akkor átkerül a hangsáv kategóriába. |
| **Q-MED-3** | **Igen.** Mobilos gombcímke: **„Kérdés: melyik az SBI-mondat?”** Ne generikus „Kérdés” vagy „Open” legyen. A hozzáférhető névnek az interakció célját kell azonosítania és megkülönböztetnie. |
| **Q-MED-4** | **A képleírás 5. része alatt a második, SBI-s verzió záróképe maradjon, és az S/B/I megfeleltetés villanjon fel újra.** A háttér enyhén visszafogható, majd sorban: `S → „amikor ma a játék közben”`, `B → „háromszor félbeszakítottad…”`, `I → „nagyon nehéz volt…”`. Nem új jelenet, hanem vizuális recap. Ezután áll meg a videó és jön a kérdés. |

Az M6-ban már eldöntött **„médiaelem mellett látható leirat”** szabály ezzel konzisztens, és valóban korpuszszintű, nem csak M6-os követelmény. 2026-10-04 Projektgazdai dönte…

### Mit kell átírni az összesítő státuszában

A 24 sorból néhányat már **most téves nyitottként tart nyilván**:

| Tétel | Új státusz |
|---|---|
| Q-GH-1 | `OWNER_DECIDED / IMPLEMENTATION_PENDING` |
| Q-GH-3 | `RELEASE_APPROVED/CLOSED`, issue #6 már lezárt |
| Q-PED-1 | `OWNER_DECIDED`, HUM-GOV-01 marad, nem nyitjuk újra |
| Q-PED-3 | `OWNER_DECIDED`, véglegesítve 2+8+5 percre |
| Q-REL-1..4 | `OWNER_DECIDED` |
| Q-PED-2,4..7 | `OWNER_DECIDED`, implementáció/QA következik |
| Q-LEG-1..5 | `OWNER_DECIDED`, ahol jelöltem, DPO/jogi QA még kötelező |
| Q-MED-1..4 | `OWNER_DECIDED` |

Vagyis **projektgazdai döntésre váró kérdés ezek után: 0**. Ami marad, az implementáció, runtime-validáció, szakértői QA vagy külső bizonyíték, tehát nem szabad ismét „nyitott projektgazdai kérdésként” visszahozni.

---

## Függelék — a 24 eredeti kérdés (az összesítő 2026-10-04-i első változatából)

| ID | Kérdés | Forrás |
|---|---|---|
| Q-REL-1 | Mi a release, a pilot és a programátadás viszonya? A 6 valós terepi peula release előtti kapu, vagy release utáni program-teljesítési tétel? Legyen-e külön `CONTROLLED_PILOT` állapot? | külső audit 2026-10-03 #2; 2026-10-04 P0.1; `RELEASE-READINESS.md:86–87`; issue #9 |
| Q-REL-2 | Mi történik egy bukott „éles” kapu után, ha a következő modul már másnap indul? Nyílhat-e ideiglenesen a következő modul tanulási része, vagy minden éles kapu után puffer hét kell? | külső audit 2026-10-04 P0.2 |
| Q-REL-3 | Bontsuk-e fel a „LEZÁRVA” jelölést állapotokra? | külső audit 2026-10-03 #3; 2026-10-04 P1.4 |
| Q-REL-4 | Mikor kezdődik a pénteki fix alkalom (óra:perc, Europe/Budapest)? | külső audit 2026-10-04 P1.6 |
| Q-GH-1 | A hangforrás-nevek kitisztítása a git-előzményekből (végrehajtás). | külső audit 2026-10-03 #1; 2026-10-04 P0.4; HUM-MEDIA-02 |
| Q-GH-2 | `main` ruleset, és ki legyen a CODEOWNERS az egyes útvonalakon? | külső audit 2026-10-04 P0.3 |
| Q-GH-3 | Az #6 issue lezárásának módja. | külső audit 2026-10-03 #11; 2026-10-04 P1.5 |
| Q-GH-4 | Kell-e `SECURITY.md`, `CONTRIBUTING.md`, Dependabot, függőség-rögzítés? | külső audit 2026-10-04 |
| Q-PED-1 | Legyen-e a terepgyakorlatnak egyéni kompetencia-minimuma? | külső audit 2026-10-03 #4; 2026-10-04 P1.1 |
| Q-PED-2 | A terepgyakorlat rubrikájának soronkénti szintleírásai. | 2026-10-02 3. válasz, maradék |
| Q-PED-3 | M3.A 4.3: 17–19 perc egy 15 perces blokkban — melyik lépés rövidüljön? | külső audit 2026-10-03 #6 |
| Q-PED-4 | M3.1: kerüljön-e be, hogy a Tuckman-modell „szemüveg, nem menetrend”? | külső audit 2026-10-03 #5 |
| Q-PED-5 | M5.3: kerüljön-e be forrásjegyzék a „kutatások szerint” állításhoz? | külső audit 2026-10-03 #7 |
| Q-PED-6 | A „modified-Angoff panel” átnevezése vagy a panel bővítése? | külső audit 2026-10-03 #9 |
| Q-PED-7 | UE-PED-4: az `M1.1-NAR-05` is a VO D-17.3 körébe tartozzon? | VO 2. fázis course-fix napló |
| Q-LEG-1 | AI Act: elég-e a „deployer” minősítés, vagy provider / downstream provider? | külső audit 2026-10-04 P1.2 |
| Q-LEG-2 | UE-BIZT-1: a V1 tartalmi kérdés is — lefedi-e a VO D-08? | VO 2. fázis course-fix napló |
| Q-LEG-3 | A nagykorúság igazolása a V2 hozzájárulás része-e? | `ELEVENLABS-VOICE-TEST.md` 1.0.; K6 |
| Q-LEG-4 | A két új megőrzési sor jogalapja. | 2026-10-02 3. válasz, maradék |
| Q-LEG-5 | Az M7 QR-kilépőkártya szolgáltatója és megőrzése. | 2026-10-02 3. válasz, maradék |
| Q-MED-1 | Média-MVP és scope-freeze. | külső audit 2026-10-03 #10 |
| Q-MED-2 | Öt narráció besorolása (csak hang vagy animáció/videó hangsávja). | VO 2. fázis utóellenőrzés |
| Q-MED-3 | UE6-PED-1: beszédes címke a mobilos M1.3 kérdésgombra? | VO 2. fázis, 6. csomag napló |
| Q-MED-4 | UE6-PED-2: mit mutasson a kép a képleírás 5. része alatt? | VO 2. fázis, 6. csomag napló |
