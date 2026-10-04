# Projektgazdai döntések — M6 nyelvi review (2026-10-04)

> **Audit trail, nem tananyag.** A projektgazda válaszai a `2026-10-04 Nyelvi review – M6, Anna-baseline
> összevetés.md` emberi döntést igénylő tételeire, a munkamenetben feltett kérdésekre (AskUserQuestion). A kérdés és a
> választott opció szó szerint áll. Átvezetés: `/course-fix`-szel, a validált finding-listával együtt.

**Jóváhagyta:** projektgazda · **Dátum:** 2026-10-04

## 1. kör — gyermekvédelem

Utólagos ellenőrzés (vétó/QA): Memuna. Vétónál a tétel újranyílik.

### M6-NY-D1 — NYELV-501 (M6.4, 826–828. ↔ 1014. sor)

- **Kérdés:** „NYELV-501 (M6.4): Ha egy gyerek a peulán láthatóan „kibillen”, de nem tár fel semmit, ez önmagában
  elindítja-e az ötlépéses jelzési utat? Az M6.4 egyik helyen nemet mond (826–828. sor), a másikon igent (1014. sor). A
  két blokk utána szó szerint egyezni fog.”
- **Válasz:** „Nem, csak feltárás” — „A jelzési utat a feltárás indítja. A kibillenést a meglévő M0.A mini-protokoll
  kezeli. Ez egyezik az M6.2-vel és az M6.3-mal.”
- **Átvezetés:** az M6.4 1014. sori blokkja a 826–828. sori változathoz igazodik (a „vagy láthatóan kibillen” nem
  kiváltó feltétel); a két blokk szó szerint egyezik. A blokkok védelmi elemei (jelzési út, a teljes titoktartás
  ígéretének tilalma, a Memuna azonnali bevonása, az elérhetőség) nem változnak.

### M6-NY-D2 — NYELV-301 / NYELV-406 (M6.2:778, M6.3:743, M6.4 „Fontos” dobozai)

- **Kérdés:** „NYELV-301/406 (M6.2, M6.3, M6.4 „Fontos” dobozai): A doboz most a jelzési útnak csak néhány lépését
  sorolja fel („többek között…”), és hivatkozik az M3.B lépéstérképre. Maradhat-e így, vagy kerüljön be az öt lépés szó
  szerint?”
- **Válasz:** „Utalás marad” — „Marad a rövid utalás és az M3.B-hivatkozás; csak nyelvileg javítjuk: kikerül a
  „nyugodtan”, és mondatokra bontjuk. Minden védelmi elem megmarad.”
- **Átvezetés:** NYELV-301 (a „nyugodtan” törlése), NYELV-406 (mondatokra bontás, minden elem szó szerint), és az M6.4
  dobozainak ugyanilyen nyelvi igazítása.

### M6-NY-D3 — NYELV-101 (M6 kapu, P1-es pool-item, 364. sor)

- **Kérdés:** „NYELV-101 (M6 kapu, P1-es kérdés visszajelzése): A kvíz szerint a Memunát még a peula alatt mindig be
  kell vonni. Az M6.A peulában ugyanez feltételes: „ha valaki erősen érintett”. Melyik legyen?”
- **Válasz:** „Feltételes (M6.A)” — „A kvíz is az M6.A-t követi: „…bevonod a Memunát, ha valaki erősen érintett”.”
- **Átvezetés:** KAPU:364 `…bevonod a Memunát, ha valaki erősen érintett – nem maradsz egyedül a helyzettel, és nem
  halasztod a peula utánra` (az M6.A:496 szó szerinti átvétele); a ✅ az A opción marad.

### M6-NY-D4 — NYELV-602 (M6.B:565, a 523. sori MUNK-06 spec)

- **Kérdés:** „NYELV-602 (M6.B 565. sor): „Tudod, kit hívsz oda / kinek jelzel, ha valaki nagyon elbizonytalanodik.”
  Milyen helyzetre szól ez a képzői ellenőrzőpont?”
- **Válasz:** „Érzelmi megterhelődés” — „Gyermekvédelmi helyzetre szól. Ide is az M6.A:180 mondata kerül: a kijelölt
  Memunának jelzel (a Somer gyermekvédelmi felelősének).”
- **Átvezetés:** az M6.A:180 kánoni mondata szó szerint (HUM-SAFE-01) a B:565-be és a MUNK-06 spec-be (523).

## 2. kör — értékelés

Utólagos ellenőrzés (vétó/QA): értékelési felelős.

### M6-NY-D5 — NYELV-103 (M6 kapu, R1)

- **Kérdés:** „NYELV-103 (M6 kapu, R1 rubrikasor): Az „Oké” szint ellenőrzőlistája „pontosan 1” célt kér, a
  rubrikatábla „1 konkrét célt”, a többi sor „legalább 1”-et. Melyik a szabály?”
- **Válasz:** „Legalább 1 cél” — „Két konkrét céllal is „Oké” a lap; a lista „pontosan 1” alakja „legalább 1”-re
  változik.”
- **Átvezetés:** KAPU:403 „pontosan **1**” → „legalább **1**”; a 393. sor rubrikacellája ugyanezt a kvantort használja.
  Küszöb és kapu-logika (minden sor ≥ 2) nem változik.

### M6-NY-D6 — NYELV-104 (M6 kapu, R2; hub 211)

- **Kérdés:** „NYELV-104 (M6 kapu, R2 rubrikasor): A 3-kvucás migráció óta az „Oké” szint kötelező korosztálya és az
  „Erős” szint kvuca-típus bónusza ugyanaz a címkesor (Parparim 6–9 / Kivsza 10–12 / Leviatán 13–17). Mi különböztesse
  meg a két szintet?”
- **Válasz:** „Erős = indoklás” — „Oké: megnevezi a korosztályt (név vagy évszám). Erős: ezen felül legalább 1, az
  M3.2-ben tanult korosztály-jellemzővel indokol (a hub meglévő megfogalmazása).”
- **Átvezetés:** a KAPU:394/404 R2 „Erős” cellája és a hub §6.2 (211) R2-összefoglalója ugyanezt mondja; a
  típusnév-bónusz mint külön feltétel kikerül; a cella végig harmadik személyben áll. A küszöb és a blokkoló logika nem
  változik.

### M6-NY-D7 — NYELV-115 (M6 kapu, 38. sor)

- **Kérdés:** „NYELV-115 (M6 kapu, 38. sor): „A kvíz diagnózisa kötelezően becsatornázódik: … célzott ismétlés +
  mentori egyeztetés ajánlott”. Mi kötelező a gyenge biztonsági/inkluzivitási kvízeredmény után?”
- **Válasz:** „Stáb figyel, egyeztetés ajánlott” — „A stábnak kötelező figyelembe vennie az eredményt; a célzott
  ismétlés és a mentori egyeztetés ajánlott.”
- **Átvezetés:** a 38. sor mondata ezt a két részt különíti el; kötelező ↔ opcionális besorolás egyéb helyen nem
  változik.

### M6-NY-D8 — NYELV-410 (M6.3 Check, 1. és 2. kérdés)

- **Kérdés:** „NYELV-410 (M6.3 záró kérdések): A 2. kérdésben csak a helyes opció szól tegező második személyben, a
  többi nem, így a nyelvtan elárulhatja a kulcsot. Egységesíthető-e az opciók személye? (A ✅ helye és az opciók
  tartalma nem változik.)”
- **Válasz:** „Igen, egységesítsd” — „Csak a személyrag egységesül, a hozzá tartozó visszajelzéssel együtt; tartalom,
  ✅ és elosztó változatlan.”
- **Átvezetés:** az M6.3 1149–1157. és 1167–1175. sor opcióinak személyraga és a hozzá tartozó visszajelzés; a ✅ helye,
  az opciók tartalma és az elosztók nem változnak.

## 3. kör — someres terminológia és tartalom

Utólagos ellenőrzés (vétó/QA): someres tartalomgazda (D9, D10), a lecke tartalomfelelőse (D11), Memuna (D12).

### M6-NY-D9 — *dugma isit* (NYELV-105, NYELV-401, NYELV-603)

- **Kérdés:** „Dugma isit (NYELV-105, -401, -603; hub 155, M6.3 727, M6.B 87/473/491): A Glosszárium szerint a dugma
  isit a madrih élőben látható személyes példamutatása, és a „Dugma Isitnek lenni” forma kerülendő. Az M6-ban viszont
  egy játékra vagy eszközre („a saját játékom … dugma isit legyen”), illetve a hanihra vonatkozik. Mi legyen?”
- **Válasz:** „Csak a madrihra” — „Glosszárium szerint: a vállalás így szól: „Miben szeretnék a saját játékommal …
  személyes példát (dugma isit) mutatni?”; az M6.3 hanih-felsorolásából a dugma isit kikerül.”
- **Átvezetés:** hub 155 és M6.B 87/473/491 a NYELV-105 javaslata szerint (a 87. sor végén kérdőjel); az M6.3:727
  felsorolásából a *dugma isit* és a hozzá tartozó magyarázat kikerül, a sor egalitásról szóló része marad.

### M6-NY-D10 — NYELV-404 (M6.3, 934/938. sor) — Somer zászló- és színhagyomány

- **Kérdés:** „NYELV-404 (M6.3, 934/938. sor): A lecke a „Somer saját zászló- és színhagyományára” hivatkozik („a
  mozgalmi identitás vállalt jelképe”), de ennek a korpuszban nincs más forrása. Van ilyen hivatkozható hagyomány?”
- **Válasz:** „Van, maradjon” — „A hivatkozás marad (nyelvileg rövidebb, párhuzamos ponttal).”
- **Átvezetés:** a hivatkozás tartalma marad; a pont nyelvileg rövidül és a felsorolás párhuzamához igazodik, új indoklás
  nélkül. Az, hogy a 939. sor érzékenységi szabálya a mozgalmi jelképekre is vonatkozik: M6-NY-D23.

### M6-NY-D11 — NYELV-214 (M6.1, SLIDE 6, B kártya)

- **Kérdés:** „NYELV-214 (M6.1, SLIDE 6 „Kategória-kártya 3”): A B kártya („Összetettebb, érzékenyebb téma” – fiktív
  eset kívülről elemezve) nem az 5. kategória („Mélyebb élményjátékok”) nevén szerepel, és nem is élményjáték. Mi legyen
  a B kártya?”
- **Válasz:** „Az 5. kategória példája” — „A kártya az 5. kategória nevét kapja; a biztonsági minimum (1061–1064)
  változatlan, kirekesztést szimuláló példa nem kerül be.”
- **Átvezetés:** a 928., 1055. és 1075. sor megnevezése az 5. kategória nevéhez igazodik („Mélyebb élményjátékok”, a
  modulhub 84. sora szerint); a fiktív eset és a biztonsági minimum nem változik (M6-invariáns).

### M6-NY-D12 — NYELV-601 (M6.A:176, játékválasztási szűrő)

- **Kérdés:** „NYELV-601 (M6.A 176. sor, játékválasztási szűrő „Kerüli” pontja): „a kiesés-alapú (vesztes-csináló)
  játékot tét nélkül”. Melyik a szabály?”
- **Válasz:** „Csak tét nélkül” — „Csak a tét nélküli kiesős játék kerülendő; téttel bíró kiesős játék megengedett.
  Ekkor az 572. sort kell pontosítani.”
- **Átvezetés:** a 176. sor feltételes olvasata a kánon; a „vesztes-csináló” magyarosítandó. Az 572. sor („A kieséses /
  felállásra kényszerítő verzió a rossz minta.”) pontosítása a döntéssel összhangban, új szabály nélkül; ha a pontos
  megfogalmazás nem vezethető le, a `/course-fix` jelzi, és nem talál ki szöveget. A szűrő másik két eleme (kötelező
  fizikai kontaktus; identitásra, testre, családi-anyagi helyzetre építő állítás) nem változik.

## 4. kör — szerzői szándék (M6.3, M6.4)

Utólagos ellenőrzés (vétó/QA): a lecke tartalomfelelőse. (A kérdésekben a „karkotő” elírás; helyesen „karkötő”.)

### M6-NY-D13 — NYELV-402 (M6.3:734)

- **Kérdés:** „NYELV-402 (M6.3 734. sor, karkotő-feladat, a szorongó vagy nyelvi nehézséggel küzdő hanih két másik
  lehetősége mellett): „az mondhatja csak a viselő nevét” – a karkotőt maga a hanih viseli, ezért értelmezhetetlen. Mi
  legyen ezzel az első lehetőséggel?”
- **Válasz:** „Kerüljön ki” — „Ez az egy lehetőség kikerül; marad a párban súgás, a szó nélküli felmutatás és a „ne
  legyen kötelező” kitétel.”
- **Átvezetés:** a 734. sorból az „az mondhatja csak a viselő nevét” tag törlődik; a „**ne legyen kötelező**” és a másik
  két lehetőség szó szerint marad.

### M6-NY-D14 — NYELV-405 (M6.3:529)

- **Kérdés:** „NYELV-405 (M6.3 529. sor, közös plakát, „Cél: mit tanít?”): „közösségi identitás (mi van rajtunk, mi
  nincs)”. Mit jelentsen?”
- **Válasz:** „Mi kerül rá, mi nem” — „A plakát tartalmáról szól, a 932. sor párhuzamos fordulatával: „közösségi
  identitás (mi kerül rá, mi nem)”.”
- **Átvezetés:** 529: „közösségi identitás (mi kerül rá, mi nem);”.

### M6-NY-D15 — NYELV-411 (M6.3:1185)

- **Kérdés:** „NYELV-411 (M6.3 1185. sor, záró mini-reflexió): „mit változtatnál rajta (cél, kérdések, inkluzivitás)” –
  a lecke alapkerete viszont „cél – inkluzivitás – variációk”. A „kérdések” elírás?”
- **Válasz:** „Elírás: variációk” — „Az alapkeret hármasa kerül ide: „(cél, inkluzivitás, variációk)”.”
- **Átvezetés:** 1185: „(cél, inkluzivitás, variációk)”.

### M6-NY-D16 — NYELV-503 (M6.4:660–664, 5C-T)

- **Kérdés:** „NYELV-503 (M6.4 660–664. sor, 5C-T napzárás történettel): „ami egy hasonló összegzésről szól” és „nektek
  mi volt ma ilyen pillanat?” – mindkettő előzmény nélküli utalás. Mi legyen?”
- **Válasz:** „Jó pillanat” — „„…rövid történet egy csoportról, amely a nap végén összegzi, mi volt jó” és „Nektek mi volt
  ma egy jó pillanat?””
- **Átvezetés:** 661: „…rövid történet egy csoportról, amely a nap végén összegzi, mi volt jó”; 664: „„Nektek mi volt ma
  egy jó pillanat?””. A két pont szerkezete marad.

## 5. kör — szerzői szándék (M6.A, M6.B; NYELV-610 b–e)

Utólagos ellenőrzés (vétó/QA): a peula tartalomfelelőse.

### M6-NY-D17 — NYELV-610 (b) (M6.A:569)

- **Kérdés:** „NYELV-610 (b) (M6.A 569. sor): „identitás-sérüléshez” – nem világos, mit jelent. Mire cseréljük?”
- **Válasz:** „Identitást sértő megjegyzés” — „„…identitást sértő megjegyzéshez” – egy másik gyerek vagy a játék
  állítása sérti valaki identitását.”
- **Átvezetés:** 569: „identitás-sérüléshez” → „identitást sértő megjegyzéshez”.

### M6-NY-D18 — NYELV-610 (c) (M6.B:63, 373; 86)

- **Kérdés:** „NYELV-610 (c) (M6.B 63. és 373. sor): „félplénum” – a percbontás (86. sor) „plénumban”-t ír. Mit
  jelent?”
- **Válasz:** „A csoport fele” — „Két félcsoport párhuzamosan: „a csoport felének”; a 86. sori percbontás is ehhez
  igazodik.”
- **Átvezetés:** a 63. és a 373. sor „félplénum” szava „a csoport fele” értelmű magyar fordulatra cserélődik; a 86. sori
  percbontás ehhez igazodik. Időtartam nem változik.

### M6-NY-D19 — NYELV-610 (d) (M6.B:226)

- **Kérdés:** „NYELV-610 (d) (M6.B 226. sor): „(ha van, 2–3 perc)” – hiányzik, mi „van”. A 2.3 és az 5.3 kötelezően
  kéri a mintát.”
- **Válasz:** „Ha van idő” — „„(ha van rá idő, 2–3 perc)” – a lépés időfüggő; a minta kötelezősége máshol nem változik.”
- **Átvezetés:** 226: „(ha van rá idő, 2–3 perc)”.

### M6-NY-D20 — NYELV-610 (e) (M6.B:575–577)

- **Kérdés:** „NYELV-610 (e) (M6.B 575–577. sor): „az élő műhelyen pedig egymásnak is tudnak visszajelzést adni”. A
  QA-ban még ez állt: „Workshopban pedig egymásnak is tudnak majd visszajelzést adni” (a Moodle Workshop társértékelő
  tevékenysége). Melyik a helyes?”
- **Válasz:** „Moodle Workshop” — „Az eredeti értelem: a Moodle Workshop-tevékenységben (online társértékelés) adnak
  egymásnak visszajelzést; a szöveg ezt mondja ki.”
- **Átvezetés:** 575–577: a Moodle Workshop-tevékenység megnevezése visszakerül (Moodle UI-elem, ezért angolul marad).
- **Következmény (nem új döntés, jelzés):** a „Workshop → műhely” csere ezen a helyen a Moodle-tevékenység nevét is
  lecserélte. Ha a korpuszban máshol is történt ilyen csere, az ugyanilyen hiba; a további modulok nyelvi review-jában
  külön figyelendő.
- **Felülírva (2026-10-04, M6-NY-D24):** a Workshopra vonatkozó rész, a fenti „Következmény” jelzéssel együtt. A kérdés
  nem mutatta meg a 2026-09-29-i konszolidáció kánonját (`Program terv.md:193, :248`; `LMS – activity manifest.md:75,
  :160`: az M6 első kiadása nem függ a Moodle Workshoptól).

## 6. kör — cím, leirat, jelképek

Utólagos ellenőrzés (vétó/QA): a peula tartalomfelelőse (D21), a hozzáférhetőségi felelős (D22), a someres
tartalomgazda (D23).

### M6-NY-D21 — NYELV-613 (M6.A:239)

- **Kérdés:** „NYELV-613 (M6.A 239. sor): A 4.2.1 címe „Biztonsági keret + Játék-labor magyarázata”, de a lépésben nincs
  biztonsági keret (az a 4.3.1-ben van). Ez már Anna szövegében is így volt. Mi legyen?”
- **Válasz:** „Címből töröld” — „A címből kikerül a „Biztonsági keret +”; a keret a 4.3.1-ben marad, ahol most is van.”
- **Átvezetés:** 239: „#### 4.2.1. Lépés 1 – Játék-labor magyarázata (kb. 2–3 perc)”; az időtartam nem változik. A
  4.3.1 biztonsági kerete változatlan.

### M6-NY-D22 — NYELV-403 és UE-IMPL-4 (leirat láthatósága)

- **Kérdés:** „NYELV-403 (M6.3 hat leirat-sora, M6.1 és M6.2 azonos sorai): „Teljes szöveges leirat a dián vagy a
  médiaelem mellől elérhető szövegként”. A VO D-19 szerint „a médiaelem mellett látható” leirat kell. Ez összefügg a
  nyitott UE-IMPL-4-gyel: számít-e láthatónak a gombbal megnyitható leirat?”
- **Válasz:** „Mellett látható” — „A VO D-19 szó szerint: a leirat a médiaelem mellett látható; a gombbal megnyitható
  leirat nem elég (UE-IMPL-4 is lezárul: nem).”
- **Átvezetés:** a leirat-sor „mellől elérhető szövegként” → „mellett látható szövegként” (VO D-19 szó szerint) az M6.1,
  az M6.2 és az M6.3 minden ilyen során. **Az UE-IMPL-4 ezzel lezárult** (a gombbal megnyitható leirat nem minősül
  láthatónak). A döntés nem csak az M6-ra szól: ahol a korpuszban ugyanez a leirat-sor áll, ugyanígy átvezetendő
  (külön, a modulonkénti javításokban).

### M6-NY-D23 — NYELV-404 második része (M6.3:938–939)

- **Kérdés:** „NYELV-404 második része (M6.3 938–939. sor): A következő pont érzékenységi szabálya (vallási/politikai
  jelkép ne legyen senkire nézve bántó) vonatkozik-e a Somer mozgalmi jelképeire is?”
- **Válasz:** „Igen, rájuk is” — „Az érzékenységi szabály a mozgalmi jelképekre is vonatkozik; a szöveg ezt egyértelműen
  kimondja.”
- **Átvezetés:** a 938. sor zárómondata („Az alábbi érzékenységkezelés ezt nem váltja ki, hanem kiegészíti”) helyett a
  szöveg egyértelműen kimondja, hogy az érzékenységi szabály a mozgalmi jelképekre is vonatkozik (M6-NY-D10-zel együtt).

## 7. kör — a course-fix célzott újraellenőrzése (UE7)

A `2026-10-04 course-fix napló – M6 nyelvi review.md` nyitott UE7-tételeire. A projektgazda a választ a munkamenetben
írásban adta meg, és megerősítette, hogy az ő döntése és utasítása (AskUserQuestion: „Igen, mind így”). A válaszok
szó szerint állnak.

Utólagos ellenőrzés (vétó/QA): a peula tartalomfelelőse (D25, D26), a Memuna (D27), a DPO (D24: nem nyílik új
adatfolyam).

### M6-NY-D24 — UE7-BIZT-1 / UE7-PED-1 (M6.B:576; a D20 részleges felülírása)

- **Kérdés (a course-fix jelentéséből):** a D20 szerint visszaírt „Moodle Workshop-tevékenység” ütközik a `Program
  terv.md:193, :248` és az `LMS – activity manifest.md:75, :160` kánonjával, és új tanulói adatfolyamot nyitna. (a) A
  Workshop bekerül az első kiadásba, vagy (b) a 576. sor a kánonhoz igazodik, Workshop nélkül.
- **Válasz:** „(b). Az M6 első kiadásába **nem kerül Moodle Workshop**. A D20-at ebben a részében felülírom, mert a
  döntéshez nem volt megadva a 2026-09-29-i konszolidáció és az LMS-manifest releváns kánonja. Az M6.B:576 igazodjon a
  jelenlegi kánonhoz, Workshop nélkül. Használható például: „A mai élő peulán kapott visszajelzéseket a játéklap
  véglegesítésekor is felhasználhatják.” Ne nyissunk emiatt új adatfolyamot, ne módosítsuk a Program tervet,
  LMS-manifestet vagy Adatvédelem §5-öt.”
- **Átvezetés:** M6.B 575–577: a Workshop-tagmondat helyett a válasz mintamondata. A Program terv, az LMS-manifest és
  az `Adatvédelem` §5 nem változik.

### M6-NY-D25 — UE7-PED-3 (M6.A:574; a D12 második fele)

- **Válasz:** „Javítsd az M6.A:574-et erre: „Ennél a játéknál a tét nélküli, kiesésre vagy felállásra kényszerítő
  verzió a rossz minta.” Így a mondat lokális marad, és pontosan összhangban van a D12 hatókörével.”
- **Átvezetés:** M6.A:574 szó szerint a válasz mondatára.

### M6-NY-D26 — UE7-PED-2 (M6.B:86, :373, 4.4.1–4.4.2; a D18 következménye)

- **Válasz:** „A második félcsoportot **előre kijelölt felnőtt stábtag** vezeti ugyanazzal a facilitátori sablonnal.
  Ha van második képző, ő legyen az elsődleges választás. Résztvevő ne vezesse a félcsoportot. Vezesd ezt
  következetesen át az M6.B:86, :373 és a 4.4.1–4.4.2 lépések között.”
- **Átvezetés:** M6.B 86, 373, a 4.4 blokk szervezése, a 4.4.1 instrukciója és a 4.4.2 lépései. Az időtartam nem
  változik. A bemutatók száma (2–3) félcsoportonként értendő, mert mindkét félcsoport ugyanazt a 8–10 percet kapja
  (4.4.2); az időszelep (569) ugyanígy.

### M6-NY-D27 — UE7-PED-4 (M6.4:826 és :1014)

- **Válasz:** „Igen, kerüljön mindkét érintett blokkba rövid utalás az M6.A négy lépéses eljárására. Fontos: ez csak
  a látható kibillenés esetén követendő teendőt tegye egyértelművé. **A D1 kiváltó feltétele és a Memuna bevonásának
  küszöbe ne változzon.** A kibillenés önmagában ne váljon automatikus gyermekvédelmi feltárási triggerré.”
- **Átvezetés:** a két blokk végére ugyanaz a rövid utalás kerül az M6.A 4.3.2/B négy lépésére. A Memuna bevonásának
  küszöbe az M6.A:498 szavaival áll („ha valaki erősen érintett”). A D1 kiváltó feltétele (csak a feltárás indítja az
  ötlépéses jelzési utat) és a blokkok védelmi elemei nem változnak.

## Összesítés

23 kérdés, 23 lezárt döntés (M6-NY-D1…D23); egyik sem „később döntök”. Lezárult velük a korábban nyitott **UE-IMPL-4**
is (M6-NY-D22). Az átvezetés a `/course-fix`-é, a validált finding-listával együtt
(`2026-10-04 Nyelvi review – M6, Anna-baseline összevetés.md`).

A 7. kör négy további döntése (M6-NY-D24…D27) a course-fix célzott újraellenőrzésének nyitott tételeit zárja le. A
D24 a D20 Workshopra vonatkozó részét felülírja.
