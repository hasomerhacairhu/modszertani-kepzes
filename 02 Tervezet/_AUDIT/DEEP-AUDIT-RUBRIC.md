# DEEP-AUDIT RUBRIC — Hasomer Hacair madrichképzés

> **Scope:** blended (Moodle + H5P online mikrolecke + offline peula), nonformális, mastery-kapus, magyar nyelvű, 15+ célcsoport, gyerekvédelmi tartalommal.
> **Cél:** egy auditor-ügynök fájlonként, modulonként és program-szinten, *megalapozottan és reprodukálhatóan* végig tudjon menni minden tananyagelemen, és minden megállapítás visszavezethető legyen egy kutatott keretrendszerre.
> **Verzió:** 1.0 · **Felülvizsgálandó:** ~évente, vagy ha a curriculum-ív érdemben változik.

---

## Hogyan használd (auditor-ügynök protokoll)

**1. Egység szintű pontozás (fájlonként).**
Minden tananyagfájlt (egy online mikrolecke VAGY egy peula) végig kell vinni mind a 10 dimenzión. Egy dimenzión belül minden kritérium **háromállapotú**:

| Jelölés | Jelentés |
|---|---|
| ✅ **PASS** | A kritérium teljesül, bizonyíték a fájlból idézhető. |
| ⚠️ **PARTIAL** | Részben teljesül / gyenge / nem explicit (idézd, mi hiányzik). |
| ❌ **FAIL** | Nem teljesül vagy ellentmond (idézd a sértő részt vagy a hiányt). |
| ➖ **N/A** | A kritérium erre a fájltípusra nem értelmezhető (indokold — pl. „nincs videó”). |

**Minden megállapításhoz kötelező: (a) konkrét idézet vagy sorhivatkozás a fájlból, (b) a forrás-keretrendszer rövidneve (lásd dimenziónként), (c) javaslat.**

**2. Súly és kapuzás.**
- 🔴 **kritikus** kritérium bármelyikének FAIL-je → a fájl **nem build-ready**, blokkoló hiba.
- 🟡 **fontos** FAIL → javítandó az élesítés előtt, de nem blokkol egyedül.
- 🟢 **nice-to-have** → backlog.

**3. Dimenzió-pontszám.** Dimenziónként adj egy 0–100 readiness-számot: `(PASS + 0.5·PARTIAL) / (értékelhető kritériumok száma) · 100`. Az N/A nem számít a nevezőbe. A 🔴 FAIL **felülírja**: ha bármely kritikus bukik, a dimenzió maximum **„BLOKKOLT”** státuszt kap, szám nélkül.

**4. Modul-szint.** Aggregáld a modul összes fájlját. Külön jelöld:
- **online↔offline koherencia** (D4) a modul szintjén él, nem egy fájlban.
- **mastery-kapu validitása** (D3) a modul kvíz+rubrika együttesére.

**5. Program-szint.** Húzd össze a 10 dimenziót egy hőtérképbe (modul × dimenzió). Külön jelentés a **review-igényes** dimenziókról (D6 ideológiai mélység, D7 gyerekvédelem) — ezeket az ügynök **nem zárja le**, hanem eszkalálja emberhez.

**6. Auto-fix vs. review.** Lásd a dimenzió-fejlécek `autoFixable` jelölését. Az auto-fixálható hibákat (tördelés, alt-szöveg, linkszöveg, célmegfogalmazás, glosszárium) az ügynök javaslattal javíthatja; a review-igényeseket csak **megjelöli és eszkalálja**, soha nem írja át önállóan.

---

## D1 — Tartalmi pontosság & forráshűség & AI-provenance
**autoFixable: részben** (provenance-címke, forráshivatkozás igen; szakmai tényhelyesség → review)
**Forrás-keretrendszerek:** ai-ethics-data, safeguarding, assessment-validity

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D1.1 | **Tényszerű helyesség** — a modellek (Johari, SBI, Kolb), a gyerekvédelmi protokoll és a héber/mozgalmi fogalmak szakmailag korrektül szerepelnek, nincs hallucinált vagy elcsúszott definíció. | 🔴 | Minden kulcsfogalom definíciója egyezik az elfogadott szakirodalommal? | ai-ethics-data (human-in-the-loop) |
| D1.2 | **Emberi szakmai lektorálás nyoma** — az érzékeny (gyerekvédelmi, krízis-) tartalomnál van lektor/dátum/verziónyom vagy review-jelölés. | 🔴 | Van megerősített emberi jóváhagyás a magas tétű tartalmon? | ai-ethics-data |
| D1.3 | **AI-provenance jelölés** — ahol generatív AI-t használtak (szöveg, ábra, kvíz-item, példa), van ember által olvasható címke vagy nyilatkozat. | 🟡 | Minden AI-gyanús elemnél van provenance VAGY „100% emberi” állítás? | ai-ethics-data (3.3.2) |
| D1.4 | **Torzítás-, sztereotípia- és gyűlöletbeszéd-mentesség** — a példák, szituációk, distraktorok mentesek nemi/etnikai/vallási torzítástól; kisebbségi/identitás-érzékenység rendben. | 🔴 | Átment-e bias-ellenőrzésen (checklist/rubrika)? | ai-ethics-data (4.1) |
| D1.5 | **Forrás-/hivatkozás-épség** — a beágyazott linkek, hivatkozott sablonok és külső anyagok léteznek és helyesek (nincs törött vagy rossz célra mutató link). | 🟡 | Minden link él és a helyes célra mutat? | elearning-qa (navigáció) |

---

## D2 — Pedagógiai illeszkedés (constructive alignment)
**autoFixable: részben** (célok újrafogalmazása igen; tevékenység-tervezés → emberi)
**Forrás-keretrendszerek:** id-alignment, elearning-qa, nonformal-youth

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D2.1 | **Mérhető, ige-alapú tanulási cél a fájl elején** — legalább 1 explicit ILO, megfigyelhető cselekvő igével (revideált Bloom: felidéz/megért/alkalmaz/elemez/értékel/alkot), NEM „megérti / tudatosul / érzi”. Témacím önmagában nem cél. | 🔴 | Van célblokk a tartalom ELŐTT, minden cél „ige + tartalom” párként? | id-alignment, elearning-qa (QM 2.1/2.3), nonformal-youth |
| D2.2 | **Cél↔tevékenység ige-egyezés** — minden célhoz van olyan lecke-/peula-aktivitás, amely UGYANAZT a kognitív szintet aktiválja (ha a cél „alkot”, a gyakorlat ténylegesen alkottat, nem csak olvastat). | 🔴 | Minden cél ige-szinten aktiválva van legalább egy tevékenységben? | id-alignment, elearning-qa (QM 5.1) |
| D2.3 | **Nincs árva tevékenység / lefedetlen cél** — nincs olyan aktivitás, amely egyetlen kimondott célhoz sem kötődik; nincs olyan cél, amelyhez se tevékenység, se értékelés. | 🟡 | Kitölthető-e hiánytalan cél↔tevékenység tábla? | id-alignment, elearning-qa (QM 4.1) |
| D2.4 | **Bloom-szint nem esik a cél alá** — az értékelő item nem alacsonyabb kognitív szinten kér, mint a cél (elemzés-célt nem puszta felidézéssel mér). | 🟡 | Item Bloom-szintje ≥ cél Bloom-szintje? | id-alignment |
| D2.5 | **Gyerekvédelmi cél viselkedés-szinten + mérve** — ahol gyerekvédelmi tartalom van, ott megjelenik viselkedés-szintű célként („felismer jelzésköteles helyzetet”, „megnevezi a jelentési lépést”) ÉS van hozzá alkalmazási/elemzési értékelési mozzanat, nem marad puszta információ. | 🔴 | A gyerekvédelmi tartalom célhoz kötött ÉS mért? | id-alignment, safeguarding |

---

## D3 — Értékelés-validitás & mastery-kapu & rubrika/item minőség
**autoFixable: részben** (item-flaw javítás, rubrika-újraírás javaslat igen; cut-score indoklás → review)
**Forrás-keretrendszerek:** assessment-validity, elearning-qa, id-alignment

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D3.1 | **Item↔cél illeszkedés (construct validity)** — minden kvíz-item és peula-feladat tanított, kimondott célhoz vezethető vissza; nincs konstruktum-irreleváns mérés (nyelvi trükk, általános műveltség), és minden mastery-kulcscélnak van legalább egy itemje. | 🔴 | Kitölthető cél→item tábla alul-/túl-reprezentáció nélkül? | assessment-validity, id-alignment |
| D3.2 | **Egy védhető helyes válasz** — minden feleletválasztósnak pontosan egy szakmailag védhető helyes/„legjobb” válasza van; nincs két egyformán védhető opció. | 🔴 | Egy hozzáértő olvasó nem tud két opciót helyesnek minősíteni? | assessment-validity |
| D3.3 | **Tiltott globális opciók hiánya** — nincs „minden fenti / egyik fenti sem / A és C” gyűjtő-opció ítéletes kérdéseknél; nincs fókuszálatlan „melyik állítás helyes / KIVÉVE” típus. | 🟡 | Szöveges keresés ezekre üres? | assessment-validity (NBME) |
| D3.4 | **Testwise-cueing flaw-k hiánya** — nyelvtani illeszkedés (zárt lead-in); nincs abszolút kvantor a distraktorokban; helyes válasz nem hosszabb; nincs clang-clue; nincs konvergencia; nincs homályos gyakorisági szó a pontozás eldöntésére. | 🟡 | Az opciónkénti flaw-checklist tiszta? | assessment-validity (NBME) |
| D3.5 | **Plauzibilis, homogén distraktorok** — minden distraktor valós tévhitet képvisel, azonos kategóriájú és nyelvtani szerkezetű, nincs „töltelék” / vicc-opció. | 🟢 | Minden distraktor logikusan illik a lead-inre? | assessment-validity |
| D3.6 | **Szcenárió-alapú, autentikus kompetenciamérés** — a vezetés/konfliktus/gyerekvédelem/csoportdinamika feladata realisztikus madrich-helyzet, cselekvést/döntést kér (nem definíció-felmondás), dokumentált best-response kulccsal. | 🟡 | Van szituáció-leírás ÉS szakértői megoldókulcs? | assessment-validity (SJT) |
| D3.7 | **Megfigyelhető viselkedést leíró rubrika** — minden rubrika-kritérium külső megfigyelő által, interpretáció nélkül eldönthető viselkedés/produktum („SBI-struktúrában: helyzet–viselkedés–hatás megnevezve”), NEM belső jelző („elkötelezett”, „jól érti”). | 🔴 | Minden kritérium-szint demonstrálható viselkedés? | assessment-validity, id-alignment, nonformal-youth |
| D3.8 | **Explicit cut-score + megkülönböztető szintek + korrektív hurok** — a mastery-küszöb a tanuló számára a lecke elején kimondott, kritérium-referenciás indoklású (nem „kerek szám”); a szomszédos rubrika-szintek kölcsönösen kizáróak; van leírt remediáció (mi történik, ha nem éri el). | 🔴 | Van indokolt küszöb + nem átfedő szintek + újratanulási út? | assessment-validity (Angoff), elearning-qa (QM 3.2/3.3), id-alignment (mastery) |

---

## D4 — Curriculum-koherencia & blended ív
**autoFixable: részben** (kereszt-link, „kezdd itt / következő lépés” igen; ívtervezés → emberi)
**Forrás-keretrendszerek:** id-alignment, elearning-qa, nonformal-youth

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D4.1 | **Getting Started / belépés** — a fájl megmondja, hogyan kezdjen hozzá a tanuló és hol a következő lépés („kezdd itt”, „mielőtt továbblépsz a peulára”). | 🟡 | Van indító és tovább-mutató utasítás? | elearning-qa (OSCQR #1, QM 1.1) |
| D4.2 | **A lecke helye az íven** — tisztázott, mi előzte meg és mi következik; nincs kontextus nélkül, hidegen induló mikrolecke. | 🟡 | Be van pozicionálva a moduláris ívben? | elearning-qa (QM 1.2) |
| D4.3 | **Online↔offline folytonosság** — az online mikrolecke kimenete explicit input a párosított peulának (és viszont); a fájl hivatkozik a párjára, a célok építkeznek, nincs szakadás vagy duplikáció. | 🔴 | A blended pár célrendszere egy ívet alkot? | id-alignment (ADDIE), nonformal-youth |
| D4.4 | **Cél-modszer-idő illeszkedés** — minden tanított célhoz konkrét módszer/aktivitás; a peulánál az időkeret arányos a célokhoz és a résztvevőszámhoz. | 🟡 | Minden cél kap módszert + reális időt? | nonformal-youth (COE) |
| D4.5 | **Nincs cél-szakadás a modulon belül** — az online és offline szegmens NEM fut külön célrendszerrel; a verbális cél a teljes íven aktiválódik. | 🟡 | A modul egy közös célrendszerre fűzött? | id-alignment |

---

## D5 — Akadálymentesség & UDL & multimédia kognitív terhelés
**autoFixable: nagyrészt igen** (alt-szöveg, felirat-flag, kontraszt, célméret, szemantikus struktúra, glosszárium)
**Forrás-keretrendszerek:** accessibility-udl, multimedia-cog, elearning-qa

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D5.1 | **Felirat / narráció-lefedettség** — minden videóhoz/hanghoz magyar felirat VAGY a leckeszöveg szó szerint lefedi a narrációt; a tanulási cél nem érhető el kizárólag hang útján. | 🔴 | Minden A/V-nek van szöveges ekvivalense? | accessibility-udl (WCAG 1.2.2 A), elearning-qa (OSCQR #35), nonformal-youth |
| D5.2 | **Alt-szöveg érdemi képeknél** — minden információt hordozó ábra (Johari, SBI-folyamatábra) ekvivalens alt-szöveget kap; a dekoratív kép üres/rejtett alttal van jelölve. Kulcsszöveg nincs képbe égetve. | 🔴 | Minden tartalmi kép szöveges megfelelővel? | accessibility-udl (WCAG 1.1.1 A), elearning-qa (QM 8.3) |
| D5.3 | **Szemantikus szövegstruktúra** — valódi címsor-hierarchia (H1>H2>H3), listák listaelemként, táblázat fejlécsorral, leíró linkszöveg („SBI-sablon”, nem „kattints ide”); nem csak vizuálisan formázott, szemantikailag lapos szöveg. | 🟡 | A struktúra szemantikus, nem csak vizuális? | accessibility-udl, elearning-qa (QM 8.2/8.3, OSCQR #16-28/#34) |
| D5.4 | **Kontraszt 4.5:1 (AA)** — törzsszöveg ≥ 4.5:1; nagy/félkövér ≥ 3:1; a kiemelőkártyák/idézetdobozok/smiley-skálák halvány szövege sem esik a küszöb alá. | 🟡 | A színkódok kielégítik a kontraszt-küszöböt? | accessibility-udl (WCAG 1.4.3 AA) |
| D5.5 | **Célméret ≥ 24×24 px + billentyűzet-operálhatóság + látható fókusz** — a H5P-elemek/linkek érintőfelülete ≥ 24px (vagy ráhagyás); minden interaktív feladat csak billentyűzettel is végigvihető, egérrablás nélkül, látható fókusszal. | 🔴 | Mobil/billentyűzet-felhasználó is teljesíti a kapus feladatot? | accessibility-udl (WCAG 2.5.8 / 2.1.1 / 2.4.7) |
| D5.6 | **Több reprezentációs csatorna (UDL)** — minden kulcsfogalom legalább két modalitásban (szöveg + ábra/példa/videó); az absztrakt fogalmakhoz (vakfolt, megfigyelés vs. értelmezés) konkrét illusztráció. | 🟡 | Nincs kizárólag folyó-prózás kulcsfogalom? | accessibility-udl (UDL 1.2/2.5), elearning-qa (QM 5.2) |
| D5.7 | **Diszlexia-barát tördelés + chunking** — sans-serif, ~12-14pt/16-19px, ~1.5 sorköz, balra zárt (NEM sorkizárt), ~60-70 karakter sorhossz, alcímekkel tagolt; felsorolás falanszöveg helyett; egy mikrolecke = egy cél. | 🟡 | A tördelés a BDA paramétereit követi? | accessibility-udl (BDA 2023, UDL 3.2) |
| D5.8 | **Koherencia — nincs csábító zaj (seductive details)** — nincs célhoz nem kötött dekoráció (háttérzene, hangulati kép, vicc-gif, díszítő ikon, irreleváns sztori); minden vizuális elemhez rendelhető konkrét tanulási cél. | 🟡 | Minden képhez/animációhoz/zenéhez van cél? | multimedia-cog (Coherence) |
| D5.9 | **Redundancia + modalitás** — narrált videónál a képernyőn nem fut szó szerinti teljes narráció (felirat KAPCSOLHATÓ, nem ráégetett); komplex ábra magyarázata hang, nem egyidejűleg olvasandó szövegblokk. | 🟢 | Nincs >~30% szó szerinti hang↔képernyő átfedés / split-modalitás? | multimedia-cog (Redundancy, Modality) |
| D5.10 | **Szegmentálás + signaling + contiguity** — a lecke tanulói tempóban léptethető (nem egy auto-folyam); a 2-3 kulcspont vizuálisan jelölt (címsor, számozott lépés, „amit vigyél el” doboz); az összetartozó szöveg+kép egymás mellett van (nincs split-attention görgetés). | 🟢 | Tagolt + jelölt + térben közeli? | multimedia-cog (Segmenting, Signaling, Contiguity) |
| D5.11 | **Pre-training (kulcsfogalmak előre) + worked example** — minden szakszó használat ELŐTT definiált (glosszárium/fogalomkártya); magas elem-interaktivitású készségnél van minta/sablon/demonstráció a tanuló önálló gyakorlása előtt (nincs minta nélküli „adj most SBI-visszajelzést”). | 🟡 | Fogalmak előre + minta a nyílt feladat előtt? | multimedia-cog (Pre-training, CLT), accessibility-udl (UDL 5.3/6.4) |

---

## D6 — Nonformális / someres pedagógiai hűség → **REVIEW-IGÉNYES**
**autoFixable: NEM** (Kolb-fázis kiegészítés javasolható; ideológiai/értékmélység emberi döntés)
**Forrás-keretrendszerek:** nonformal-youth, multimedia-cog, elearning-qa

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D6.1 | **Teljes Kolb-ciklus a peulában** — mind a négy fázis explicit: (1) konkrét tapasztalat/játék/szituáció, (2) strukturált reflexió/debrief kérdésekkel, (3) fogalmi összekötés/általánosítás, (4) transzfer/kipróbálás új helyzetben. A debrief sosem hiányzik élményalapú aktivitás után. | 🔴 | Megvan mind a 4 Kolb-fázis? | nonformal-youth (Kolb) |
| D6.2 | **Aktív részvétel és választás (nem frontális fogyasztás)** — van döntési/választási pont, saját tapasztalat behozása, pár-/csoportmunka vagy alkotás; nem csak passzív videó/szöveg + tudásmérő kvíz. Minden tisztán frontális blokk megjelölve. | 🟡 | Van aktív, interaktív, választást adó elem? | nonformal-youth (EU 9 alapelv), elearning-qa (QM 5.2, OSCQR #29-30/#41-42) |
| D6.3 | **Megfigyelés vs. értelmezés/címkézés szétválasztása** — a feedback-anyagok (SBI, Johari) mintái és rubrikái leíró viselkedést írnak le („kétszer félbeszakítottad”), nem címkét/szándékot („agresszív voltál”). | 🔴 | Minden minta/rubrika-sor megfigyelhető tény, nem címke? | nonformal-youth, assessment-validity |
| D6.4 | **Résztvevő-középpontúság & 15+ kontextus-illeszkedés** — a példák, nyelvezet, szituációk a 15+ Hasomer-élményvilághoz kötöttek, a résztvevő előzetes tapasztalatára építenek; nincs absztrakt/felnőtt-munkahelyi példa elszakadva a célcsoporttól. | 🟡 | A tartalom a célcsoport élményvilágához kötött? | nonformal-youth (youth-centredness) |
| D6.5 | **Értékelés a tanulási folyamatra** — van participatív önreflexió/csoportos kiértékelés a folyamatról (nem csak végeredmény-kvíz), és van follow-up/transzfer pont; az értékelés kimenete a célokhoz illeszkedik. | 🟡 | Van folyamat-szintű, részvételi értékelés + follow-up? | nonformal-youth (ETS 8., COE) |
| D6.6 | **Emberi jogi / mozgalmi érték-dimenzió beágyazva** — az érték- és jogi tartalom (mlachomut, szolidaritás, méltóság, egyenlőség) a tevékenységbe/módszerbe/légkörbe ágyazott („learning about, through and for”), nincs külön moralizáló záróblokként; a reflexió saját identitásra/értékre kérdez. | 🟡 | Az értékdimenzió aktivitásba ágyazott, nem ráma­zolt? | nonformal-youth (COE) |
| D6.7 | **Személyes, beszélt nyelvű hangnem** — közvetlen megszólítás (te/ti/mi), aktív első/második személy; nem személytelen „a madrich köteles…” regiszter. | 🟢 | Dominálnak a megszólító, aktív mondatok? | multimedia-cog (Personalization), nonformal-youth |

> **Eszkaláció:** D6.1, D6.3, D6.6 és minden ideológiai mélységet/mozgalmi hitelességet érintő megállapítás → **szakértői (someres) review**, az ügynök nem zárja le.

---

## D7 — Gyerekvédelem & biztonság → **REVIEW-IGÉNYES (kötelező emberi jóváhagyás)**
**autoFixable: NEM** (hiányt megjelöli és eszkalálja; tartalmat nem ír át önállóan)
**Forrás-keretrendszerek:** safeguarding, nonformal-youth

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D7.1 | **Disclosure-protokoll: a 4 tilalom mind szerepel** — (1) NE ígérj titoktartást, (2) NE nyomozz / NE tegyél fel rávezető kérdéseket, (3) NE beszélj az ügyről a gyanúsítottal, (4) rögzítsd a gyerek szó szerinti szavait, tényt és véleményt elkülönítve. Bármelyik hiánya = bukás. | 🔴 | Mind a 4 NSPCC-szabály jelen van? | safeguarding (NSPCC) |
| D7.2 | **Eszkalációs lánc nevesített lépésekkel** — madrich → szervezet kijelölt gyerekvédelmi felelőse (focal point/DSL, szerep megnevezve) → hatóság/gyermekvédelem; közvetlen veszélynél külön 112/rendőrség ág. „Szólj valakinek” nem elég. | 🔴 | Van belső felelős + külső hatóság + azonnali-veszély ág? | safeguarding (KCS+NSPCC) |
| D7.3 | **Magatartási kódex konkrét, megfigyelhető tiltásokkal** — minimum: (a) kettős felügyelet (ne legyen egy felnőtt egyedül gyerekkel), (b) fizikai kontaktus szabálya, (c) magán/online kontaktus tilalma személyes fiókról; mindegyik MIT tegyen/ne tegyen szinten, nem „légy felelős”. | 🔴 | A kódex megfigyelhető viselkedést ír le? | safeguarding (KCS People, NSPCC) |
| D7.4 | **Online/digitális kontaktus szabályai (blended-specifikus)** — (a) csak hivatalos fiók/eszköz, soha személyes fiókról; (b) moderált, rendszeresen ellenőrzött fórum/üzenet; (c) egyetlen moderátorra épülő függőség kerülendő. Az online modult leíró fájlban jelen. | 🔴 | Mind a 3 digitális szabály a Moodle/online fájlban? | safeguarding (NSPCC online) |
| D7.5 | **15+ önkéntes vezetők kettős státusza kezelve** — (a) 18 alatti soha nem felügyel egyedül és nem számít a felnőtt-gyerek arányba; (b) korának megfelelő safeguarding-tréning és bejelentési út; (c) bizalmi pozíció/hatalmi egyenlőtlenség tudatosítva. | 🔴 | Mind a 3 pont a vezetői szerepleírásnál? | safeguarding (NSPCC young volunteers) |
| D7.6 | **Madrich ≠ terapeuta — szereptisztázás** — kifejezett „mit NEM csinál a madrich” szakasz a gyerekvédelmi kontextusban: figyel/biztonságot ad/jelez, de nem diagnosztizál, nem terápiáztat, nem old meg egyedül feltárt esetet. | 🔴 | Van explicit határ-szakasz? | safeguarding (KCS People, NSPCC), nonformal-youth |
| D7.7 | **Biztonságos tér & visszavonulási mechanizmus** — minden önfeltárást kérő/érzelmileg expono aktivitásnál: önkéntesség / „pass” joga, bizalmasság, határok, ÉS kihez fordulhat a résztvevő, ha rosszul érinti (segítségkérési útvonal). | 🔴 | Van „pass” + bizalmasság + eszkalációs út minden expono feladatnál? | nonformal-youth (secure environment), safeguarding |
| D7.8 | **Bizalmas adatkezelés & rögzítés** — konkrét utasítás: mit/hogyan/mikor rögzíts (gyerek szavai, dátum, tények vs. vélemény) ÉS a megosztás határai (need-to-know, csak a felelősnek). | 🟡 | Van rögzítési + megosztás-korlát utasítás? | safeguarding (NSPCC) |
| D7.9 | **Kódexszegés következménye + safeguarding-küszöb elkülönítve** — fokozatos következménysor (figyelmeztetés → dokumentálás/szülő értesítése → eltávolítás), és kimondva: ha a viselkedés ártalom/veszély jele, AZONNAL a safeguarding-eljárás indul, nem a fegyelmi. | 🟡 | Van következménysor ÉS elkülönített safeguarding-küszöb? | safeguarding (NSPCC) |
| D7.10 | **Accountability / felülvizsgálati nyom** — a gyerekvédelmi anyagon van felülvizsgálati dátum vagy nevesített felelős; jelzi a rendszeres felülvizsgálatot és a valós esetek visszacsatolását. | 🟢 | Van review-dátum/felelős a safeguarding-tartalmon? | safeguarding (KCS Accountability) |

> **Eszkaláció:** D7 minden FAIL és PARTIAL **kötelezően** emberi gyerekvédelmi felelőshöz megy; az ügynök a modult `BLOKKOLT (safeguarding)` státuszúra állítja, amíg ember nem hagyja jóvá.

---

## D8 — AI-etika & adatvédelem (GDPR / ICO Children's Code / UNESCO)
**autoFixable: részben** (adatminimalizálási flag, plain-language tájékoztató sablon, AI-címke igen; jogi/korhatár-döntés → review)
**Forrás-keretrendszerek:** ai-ethics-data

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D8.1 | **Adatminimalizálás a naplóknál/kvízeknél** — a reflexiós napló / kvíz / H5P csak a tanulási célhoz szükséges személyes adatot kéri; nincs felesleges gyűjtés, nincs bundling, nincs „adj meg többet” nudge; opcionális mezők elkülönítve. | 🔴 | Csak a szükséges minimum adat, bundling/nudge nélkül? | ai-ethics-data (GDPR 5(1)(c), ICO #8) |
| D8.2 | **Gyermek-hozzájárulás & korhatár az AI-/adat-elemeknél** — ahol önálló külső GenAI-interakció van, dokumentált a minimum korhatár (≥13), és 16 alatt szülői/gondviselői hozzájárulás a reflexiós/kvíz-adatokra; a fájl jelzi, hogy 16 alatt a szülő erősíti meg. | 🔴 | Korhatár + szülői hozzájárulás kezelve a 15+ határvonalon? | ai-ethics-data (GDPR Art.8, UNESCO 3.3) |
| D8.3 | **Informált, gyermek-nyelvű tájékoztatás** — a naplót/kvízt indító ponton rövid, plain-language tájékoztató: milyen adat, mire, meddig, kihez fordulhat; a hozzájárulás célonként külön kérhető (alapfunkció vs. extra). | 🟡 | Van érthető, célonkénti tájékoztató/hozzájárulás? | ai-ethics-data (GDPR átláthatóság, ICO) |
| D8.4 | **Tárolási korlát & törlés** — a napló-/kvíz-/mastery-haladási adat megőrzési ideje meghatározott, van törlési/anonimizálási folyamat lejáratkor/képzés végén; a kapuhoz tárolt adat valóban szükséges a kapu funkciójához. | 🟡 | Van megőrzési idő + törlési folyamat + szükségesség? | ai-ethics-data (GDPR 5(1)(e), ICO) |
| D8.5 | **AI-túltámaszkodás megelőzése a feladatokban** — a feladatok nem ösztönöznek puszta AI-másolásra; ahol AI megengedett, kötelező a kritikus értékelés és saját reflexió („értékeld, mi pontatlan az AI-válaszban”). | 🟡 | A feladat védi az emberi gondolkodást (nem usurp)? | ai-ethics-data (UNESCO 4.2) |
| D8.6 | **AI-literacy a curriculumban** — van legalább egy elem, amely fejleszti a kritikus AI-értékelést (hallucináció, torzítás), az adatbiztonság-tudatosságot és a magyarázat-jog ismeretét. | 🟢 | Jelen van-e AI-műveltség-fejlesztő elem? | ai-ethics-data (UNESCO AI Competency, 4.4) |

---

## D9 — Hozzáférhetőség / LMS build-readiness & tanulói támogatás
**autoFixable: nagyrészt igen** (eszközmegnevezés, support-link, technikai utasítás, adatvédelmi megjegyzés)
**Forrás-keretrendszerek:** elearning-qa, accessibility-udl

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D9.1 | **Interakció minden online leckében** — minden mikrolecke kínál legalább egy aktív elemet (H5P-interakció, reflexiós prompt, fórum-hozzászólás), nem csak passzív olvasás/videó. | 🟡 | Van legalább 1 aktív elem leckénként? | elearning-qa (QM 5.2, OSCQR #29) |
| D9.2 | **Higher-order + peer-interakció a peulában** — a peulák tartalmaznak tanuló–tanuló interakciót és alkalmazási/elemzési (nem felidéző) feladatot. | 🟡 | Van peer-interakció + higher-order feladat? | elearning-qa (OSCQR #30/#41-42) |
| D9.3 | **Eszköz-/hozzáférés-megnevezés** — a fájl megnevezi a szükséges eszközöket/hozzáféréseket (Moodle, H5P, fórum) és hogy mire valók a célok szempontjából. | 🟡 | Az eszközök a célokhoz kötve megnevezve? | elearning-qa (QM 6.1) |
| D9.4 | **Technikai & tanulási támogatás elérhető** — van link/utalás technikai és tanulási segítségre (kihez fordulj, ha elakadsz). | 🟢 | Van support-utalás? | elearning-qa (QM 7.2-7.4, OSCQR #5/#11-13) |
| D9.5 | **Adatvédelmi / biztonságos megosztási megjegyzés** — gyerekvédelmi/érzékeny tartalomnál a fájl jelzi, mit oszt meg a tanuló és hol (biztonságos megosztás). | 🟡 | Van biztonságos-megosztási megjegyzés érzékeny tartalomnál? | elearning-qa (QM 6.4, OSCQR #14), ai-ethics-data |
| D9.6 | **Reakció-/visszacsatolási pont (L1 + iteráció)** — a lecke/modul tartalmaz legalább egy beépített reakció/relevancia-visszajelzést (záró reflexió, bemutatkozó/visszajelző fórum, rövid értékelés), amely a tananyag iteratív javításához felhasználható. | 🟢 | Van beépített visszacsatolási mozzanat? | id-alignment (Kirkpatrick L1, SAM) |

---

## D10 — Hangnem / nyelv / inklúzió / olvashatóság
**autoFixable: nagyrészt igen** (szókincs-feloldás, plain-language átírás, inkluzív megfogalmazás)
**Forrás-keretrendszerek:** accessibility-udl, multimedia-cog, nonformal-youth

| # | Kritérium | Súly | Check (igen/nem) | Forrás |
|---|---|---|---|---|
| D10.1 | **Szókincs- és rövidítés-tisztázás** — minden szakkifejezés, héber/jiddis fogalom (madrich, peula, dugma ishit) és rövidítés (SBI, H5P) első előfordulásakor feloldva/definiálva. | 🟡 | Minden új terminushoz tartozik magyarázat? | accessibility-udl (UDL 2.1, BDA plain language) |
| D10.2 | **Plain language & aktív igék** — rövid mondatok, hétköznapi szavak, aktív igék; kerüli a felesleges zsargont és a bürokratikus passzívot. | 🟢 | Plain-language, aktív szerkezet dominál? | accessibility-udl, multimedia-cog |
| D10.3 | **Inkluzív, nem kirekesztő megfogalmazás** — a nyelvezet mentes a kirekesztő/sztereotip megfogalmazástól; identitás-/kisebbség-érzékeny (Hasomer-kontextus). | 🟡 | A megfogalmazás inkluzív, nem sztereotip? | ai-ethics-data, nonformal-youth |
| D10.4 | **Olvashatóság / readability (QM 8.2)** — a kurzusdizájn megkönnyíti az olvasást: tagolt, jelölt, nem szövegfal; konzisztens formázás. | 🟡 | A fájl olvasásra optimalizált? | elearning-qa (QM 8.2), accessibility-udl |
| D10.5 | **Big-idea kiemelés / chunking** — a kulcsüzenet explicit kiemelt (összefoglaló doboz, „amit vigyél el”, tanulási-cél fejléc); egy mikrolecke egy fő gondolat köré szervezett. | 🟢 | A nagy-kép vizuálisan kiemelt + chunkolt? | accessibility-udl (UDL 3.2), multimedia-cog (Signaling) |

---

## Auto-fix vs. review összefoglaló

| Dimenzió | autoFixable | Megjegyzés |
|---|---|---|
| D1 Tartalmi pontosság & AI-provenance | részben | Provenance-címke, link-épség auto; szakmai tényhelyesség → emberi lektor. |
| D2 Pedagógiai illeszkedés | részben | Cél-újrafogalmazás auto-javaslat; tevékenység-redesign emberi. |
| D3 Értékelés-validitás & kapu | részben | Item-flaw és rubrika-átírás javaslat auto; cut-score indoklás → review. |
| D4 Curriculum-koherencia | részben | Kereszt-link, belépő/tovább auto; ívtervezés emberi. |
| D5 Akadálymentesség & UDL & multimédia | **nagyrészt igen** | Alt, felirat-flag, kontraszt, célméret, struktúra, tördelés gépiesíthető. |
| D6 Nonformális/someres hűség | **NEM** | Kolb-kiegészítés javasolható; ideológiai mélység → someres review. |
| D7 Gyerekvédelem & biztonság | **NEM** | Csak megjelöl + eszkalál; kötelező emberi jóváhagyás. |
| D8 AI-etika & adatvédelem | részben | Adatminimalizálás-flag, tájékoztató-sablon auto; korhatár/jogi → review. |
| D9 LMS build-readiness & support | **nagyrészt igen** | Eszköz/ support/adatvédelmi megjegyzés gépiesíthető. |
| D10 Hangnem/nyelv/inklúzió | **nagyrészt igen** | Szókincs-feloldás, plain-language átírás auto-javaslat. |

**Kötelező emberi eszkaláció (az ügynök NEM zár le):** D6.1 / D6.3 / D6.6 (someres/ideológiai), és **a teljes D7** (gyerekvédelem). Ezeknél a modul `BLOKKOLT` marad jóváhagyásig.

---

## FORRÁSOK

- https://www.qualitymatters.org/qa-resources/rubric-standards/higher-ed-rubric
- https://www.qualitymatters.org/sites/default/files/PDFs/QM-Higher-Ed-Sixth-Edition-Specific-Review-Standards-Accessible.pdf
- https://www.qualitymatters.org/sites/default/files/PDFs/StandardsfromtheQMHigherEducationRubric.pdf
- https://www.qualitymatters.org/qa-resources/rubric-standards
- https://educationaldevelopment.uams.edu/qualitymatters/qm-rubric
- https://oscqr.suny.edu/
- https://oscqr.suny.edu/standard1/
- https://oscqr.suny.edu/standard15/
- https://oscqr.suny.edu/standard35/
- https://oscqr.suny.edu/standard50/
- https://oscqr.suny.edu/about/about-oscqr/
- https://www.buffalo.edu/catt/teach/develop/evaluate/evaluating-course-design/oscqr-rubric.html
- https://www.qmul.ac.uk/queenmaryacademy/educators/resources/curriculum-design/constructive-alignment/
- https://en.wikipedia.org/wiki/Constructive_alignment
- https://www.researchgate.net/profile/John-Biggs-3/publication/255583992_Aligning_Teaching_for_Constructing_Learning/links/5406ffe70cf2bba34c1e8153/Aligning-Teaching-for-Constructing-Learning.pdf
- https://www.eiu.edu/instructional_design/blooms_revised_taxonomy_2001_for_action_verbs.php
- https://teaching.uic.edu/cate-teaching-guides/syllabus-course-design/blooms-taxonomy-of-educational-objectives/
- https://quincycollege.edu/wp-content/uploads/Anderson-and-Krathwohl_Revised-Blooms-Taxonomy.pdf
- https://www.kirkpatrickpartners.com/the-kirkpatrick-model/
- https://www.devlinpeck.com/content/kirkpatrick-model-evaluation
- https://www.td.org/content/newsletter/all-about-addie
- https://www.devlinpeck.com/content/addie-instructional-design
- https://elmlearning.com/blog/iterative-design-models-addie-vs-sam/
- https://learn.alleninteractions.com/services/custom-learning/sam/elearning-development
- https://www.ascd.org/el/articles/lessons-of-mastery-learning
- https://files.eric.ed.gov/fulltext/ED490412.pdf
- https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/principles-for-reducing-extraneous-processing-in-multimedia-learning-coherence-signaling-redundancy-spatial-contiguity-and-temporal-contiguity-principles/CD5B7AE1279A9AB81F8EEBB53DBEC86E
- https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/principles-for-managing-essential-processing-in-multimedia-learning-segmenting-pretraining-and-modality-principles/DD24C2F48B9B1277CE59F78276110258
- https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/redundancy-principle-in-multimedia-learning/448A5532008EB4B4BA17DBEB5A421920
- https://teaching.pitt.edu/wp-content/uploads/2023/03/multimedia-principles-checklist.pdf
- https://www.digitallearninginstitute.com/blog/mayers-principles-multimedia-learning
- https://link.springer.com/article/10.1186/s40561-022-00200-2
- https://journals.sagepub.com/doi/10.1177/0963721420922183
- https://www.sciencedirect.com/science/article/abs/pii/S2211368121000231
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/WCAG22/quickref/
- https://www.w3.org/WAI/WCAG22/Understanding/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- https://udlguidelines.cast.org/
- https://udlguidelines.cast.org/more/about-guidelines-3-0/
