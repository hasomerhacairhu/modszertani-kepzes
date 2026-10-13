# Jóváhagyási csomag – jogi szakértő (AP-2026-10-13-01)

> **Audit trail, nem kánon.** Előre kitöltött elfogadási javaslat a 2026-10-13-i futásból. A projektgazda irányait a
> `02 Tervezet/Emberi jóváhagyás szükséges.md` 15. szakasz rögzíti; ahol a döntés vagy a jóváhagyás a címzett szerep hatásköre, az irány **nem helyettesíti** az ő
> döntését. A javasolt szövegek tervezetek: a tananyagba csak az írásos elfogadás után kerülnek, `/course-fix`-szel.
> A tervezeteket read-only szakértői ügynökök készítették, a fő session ellenőrizte; a sorszámok a `8bb4d7d` körüli
> állapotra vonatkoznak, átvezetéskor újra ellenőrizzük őket.

Címzett: a szervezet által felkért jogi szakértő. A kérdések írásos szakvéleményt kérnek; a repó jogi minősítést nem állít. A JOG-1 ellenőrzésének elsődleges nyilvántartása a G1 tracker-issue (#1; projektgazdai döntés, 2026-10-13, D-06); az issue nyilvános, ezért személyes adat oda nem kerül.

## Hogyan válaszolj

- Tételenként: **VÁLASZ / PONTOSÍTÁS / NEM ALKALMAZHATÓ**, dátummal és szerepnévvel. A repó nyilvános: személynév,
  személyes adat ne kerüljön a válaszba vagy az issue-ba.
- Elfogadásnál a javasolt szöveg (a „DPO tölti ki”, „Memuna dönt” mezők kitöltésével) a következő engedélyezett javítási körben
  kerül be; vétónál a mostani szöveg marad, és az érintett 14. szakaszbeli sor `REOPENED`.
- Az elfogadás nem release-jóváhagyás: a G1–G8 kapuk bizonyítéka és a go/no-go döntés külön lépés (`02 Tervezet/RELEASE-READINESS.md`).
- A válasz helye: a G1 (#1) tracker-issue a JOG-1-nél, a G2 (#2) a GDPR-kérdéseknél; a hosszabb vélemény tárolási helyéről a DPO dönt.

## Tételek

| Tétel | Mit kérünk | Kapcsolódó ledger-kulcsok / kapu |
|---|---|---|
| B1 – JOG-1 | a Gyvt. 17. § címzettjei és határidői, a (4a)–(4c) és a Btk. 209/A. § viszonya; a belső jelzési modell megfelelősége | M3:BIZT-G1-8; BK-04 |
| B2 – D-10 | a tárolt feltárás korlátozása, kézi törlése jogi felülvizsgálat után; a Z.4 Feedback válaszadójának visszakeresése | Z:QA14-BIZT-1, KANON:QA14-BIZT-4 |
| B3 – ADV-5 | a GDPR 9. cikk szerinti minősítés és kivétel a someres érték megnevezésénél | M7:BIZT-G1-6; BK-11 |
| B4 – ERT-42 | harmadik személy azonosítható adata a beadásban: incidens-e, kell-e bejelentés | M7:BIZT-G1-1 |

## Részletes javaslatok

### B) Jogászi jóváhagyási és szakvélemény-csomag (csak kérdések)

### B1 — JOG-1: Gyvt. 17. § és Btk. 209/A. §

**Érintett helyek és mostani szöveg:**
- **M3 hub :41**: „A Gyvt. 17. § a gyermekvédelmi jelzőrendszer résztvevői között szervezeteket és személyeket is nevesít, és veszélyeztetettség esetén jelzési / kezdeményezési kötelezettséget ír elő. A Btk. 209/A. § nem valamennyi jelzéskésés általános büntetőszabálya, hanem a Gyvt. 17. § (4a)–(4c) szerinti speciális kötelezettségekhez kötődik.”
  - Fájl: `02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md`
- **M3 hub :42**: „Azt, hogy az adott szervezeti jogállás mellett ki tesz külső jelzést, az éles használat előtt rögzíteni kell, és a Memunának jóvá kell hagynia; a szervezet nevében a jogi tanács alapján kijelölt felnőtt dönt a külső jelzésről, anélkül, hogy az akut védelem késne; a külső jelzés jogi kérdésében jogi szakértő dönt.”
- **GK §3.1:31**: „…17. § (1) a gyermekvédelmi jelzőrendszer résztvevői között **egyesületeket, alapítványokat és egyházi jogi személyeket is nevesít**.”
- **GK §3.1:33**: „**Nyitott jogi alkalmazási kérdés:** … Ezt a repository nem minősíti önállóan.”
- **GK §3.2:37**: „…kifejezetten a Gyvt. 17. § **(4a)–(4c)** bekezdéseiben meghatározott, kiemelt veszélyeztető okra utaló körülménnyel összefüggő kötelezettség megszegésére hivatkozik.”
- **GK §5:121**: „…jogi szakértő csak a jogi minősítésnél.”
- **HUM:662 (JOG-1)**: „Ne állítsunk általános három munkanapos büntetőjogi határidőt jogi vélemény nélkül.”

**Jogszabályszöveg:**
- Az njt.hu kétszer ECONNRESET hibát adott. Az njt.jog.gov.hu betöltött (hatály: 2026.10.01), de csak összegző eszközön át, és két lekérés eltérő kimenetet adott. Az alábbi kivonat ezért **nem ellenőrzött szó szerinti szöveg**, a jogásznak a hivatalos szöveggel kell összevetnie:
  - (1) j): „az egyesületek, az alapítványok és az egyházi jogi személyek”
  - (4a): „…kiemelt veszélyeztető okra utaló körülmény észlelése esetén haladéktalanul, de legkésőbb három munkanapon belül köteles azt a szerv vezetőjénél vagy a kijelölt személynél kezdeményezni. A szerv vezetője vagy az arra kijelölt személy a kezdeményezést követő három munkanapon belül teljesíti … amelynek elmulasztása büntetőjogi felelősségre vonással jár.”
  - Az eszköz által „(4c)”-ként adott szöveg „A (4a)–(4c) bekezdés alkalmazásában kiemelt veszélyeztető okra utaló körülmények: …” kezdetű. Ez a bekezdés-számozást kétségessé teszi.
- **Btk. 209/A. §**: az njt.jog.gov.hu oldal a 209. §-nál csonkult, a szöveget **nem olvastam**.

**Kérdések a jogásznak (írásos megerősítés kell):**
1. A képzést ténylegesen működtető jogalany a Gyvt. 17. § (1) melyik pontja alá esik, ha egyáltalán alá esik? A j) pont („egyesületek, alapítványok…”) erre a jogalanyra vonatkozik? Pontos-e a hub :41 „szervezeteket és személyeket is nevesít” fordulata?
2. Kinek kell címezni a 17. § (2) szerinti jelzést (gyermekjóléti szolgálat, gyámhatóság, rendőrség stb.), és milyen határidővel?
3. A (4a) „alkalmazottja” fogalma kiterjed-e az önkéntes madrihokra, mentorokra és képzőkre, különösen a 15–17 éves önkéntesre?
4. Megfelel-e a (4a)-nak a belső modell (madrih → Memuna/helyettes → a szervezet által kijelölt felnőtt dönt a külső jelzésről)? A Memuna vagy a „kijelölt felnőtt” a (4a) szerinti „kijelölt személy”? Kell-e írásbeli kijelölés, és hol kell rögzíteni?
5. Pontosan melyik bekezdésekhez és melyik alanyi körhöz kötődik a Btk. 209/A. §? Igaz-e a hub :41 második mondata és a GK §3.2:37 a mai hatályos szöveg szerint?
6. Kell-e a tananyagban megjelennie a (4a) belső határidejének („haladéktalanul, de legkésőbb három munkanapon belül”), és kinek szólna: a madrihnak, a Memunának vagy a kijelölt felnőttnek? A JOG-1 jogi vélemény nélkül ezt tiltja.
7. Összeegyeztethető-e a (4a) határidejével a hub :42 „anélkül, hogy az akut védelem késne” fordulata?

**Mit változtatnánk a válasz szerint:**
- a hub :41 első mondata (a címzetti kör pontosítása);
- a hub :42 kijelölt felnőttjének megnevezési módja;
- a GK §3.1:33 „nyitott jogi alkalmazási kérdés” sorának lezárása a jogász hivatkozásával;
- a GK §3.2 esetleges pontosítása.

A bizonyíték helye a projektgazdai irány szerint a G1 GitHub #1 issue, HUM-hivatkozással (D-06). Típus: `bizonyíték-kapu` (BK-04, G1).

### B2 — D-10: feltárás a tárolt beadásban és a Feedback-válaszban

**Érintett helyek és mostani szöveg:**
- **Z.4:359** (Assignment): „…jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük.”
- **Z.4:401** (Feedback): „…ezt a választ jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük; a korlátozáshoz, a helyesbítéshez és a törlési vagy megőrzési döntéshez dokumentált, jogosult Memuna-eljárás és adatvédelmileg jóváhagyott rend kell…”
- **Z.4:370 és :403**: „A válaszok név nélkül jelennek meg a feldolgozásban.”
- **ADV:153** és **ADV:198**: „…a felhasználó azonosítója az adatbázisban marad…”
- **M1 KAPU:27**
- **M7 KAPU:360** (R8 0-s szint): „…az kikerül a Moodle-ből…”

**GDPR-hivatkozások:** a G4 kutató a 17. cikk (3) e), a 18. cikk (1) c) és (2), valamint a (38) preambulumbekezdés szövegét **másodlagos forrásból (gdpr-info.eu)** vette. Ebben a futásban az EUR-Lex HU szövege kétszer üresen jött vissza. Szó szerinti GDPR-idézetet ezért nem adok.

**Kérdések (DPO + jogi felelős, a visszakeresésnél a jogi felelős is):**
1. Mi a jogalapja annak, hogy a gyermekvédelmi feltárást tartalmazó tárolt beadás a Moodle-ben maradjon, miután a szükséges tartalom az incidensnyilvántartásba került? A 18. cikk szerinti korlátozás-e a jogi megőrzési felülvizsgálatig a megfelelő eszköz?
2. Kire alkalmazható a 17. cikk (3) e) kivétele (jogi igények előterjesztése, érvényesítése, védelme): egy ifjúsági szervezet safeguarding-nyilvántartására vagy a Moodle-példányra? Vagy más jogalap kell, például a Gyvt. 17. §-ból fakadó kötelezettség?
3. Ki dönthet a végleges kézi törlésről, milyen dokumentálással, és mennyi ideig őrizhető az incidensnyilvántartásba mentett példány?
4. A HUM-PRIV-01 „kikerül a Moodle-ből” mondata (és az M7 R8) korlátozásként olvasható-e, amely csak jogi felülvizsgálat után fordul törlésbe, összhangban a GYV-11-gyel?
5. Szabad-e a Moodle-ben név nélküli megjelenítéssel rögzített Z.4 Feedback-válasz írójának azonosítóját visszakeresni, ha a válasz gyermekvédelmi feltárást tartalmaz?
   - A Moodle dokumentációja szerint a felhasználó azonosítója ilyenkor is az adatbázisban marad.
   - Ha szabad: milyen feltétellel (csak súlyos veszélynél? a Memuna kérésére? megnevezett adminisztrátor? dokumentáltan?).
   - Ha nem szabad: mit tehet a Memuna egy azonosítatlan feltárással?
6. Ha a visszakeresés megengedett, kell-e a Z.4:370 mellé tájékoztató mondat (13. cikk, átláthatóság)? A HUM-PRIV-03 „név nélkül jelennek meg” mondata nem változhat.

**Mit változtatnánk a válasz szerint:**
- az ADV §3 (megőrzési kivétel) és §5:153;
- a GK §4.1 incidensnyilvántartási pontja;
- a Z.4:359, :370 (esetleges tájékoztató mondat) és :401;
- az M1 KAPU:27 pótlási útja;
- az M7 R8 „kikerül” fordulata.

A pótlási mechanika (külön, kézzel nyitott próbálkozás; beszámít-e) nem jogi kérdés, hanem az értékelési felelősé.

### B3 — ADV-5: GDPR 9. cikk szerinti minősítés és kivétel

**Érintett helyek és mostani szöveg:**
- **LMS – activity manifest.md:59 (LMS-M2-07, M2.3 záró mondat)** és **:95 (LMS-M7-10, M7.1 SMART cél R eleme)**: „…különleges vagy érzékeny világnézeti információként kezeljük; … nyitott: a GDPR 9. cikk szerinti minősítés és kivétel, csak jogi/DPO-jóváhagyással…”
- **HUM:651 (ADV-5)**

**Kérdések (DPO / jogi felelős; someres vonatkozásban a projektgazda):**
1. Különleges kategóriájú adatnak minősül-e a 9. cikk (1) szerint (vallási vagy világnézeti meggyőződés) az a névhez kötött, tárolt tanulói válasz, amely a Somer egyik pillérével vagy egy someres értékkel való azonosulásra enged következtetni?
2. Ha igen: maga a mozgalmi tagság már ilyen adat-e?
3. Melyik 9. cikk (2) szerinti kivétel alkalmazható?
   - a) kifejezett hozzájárulás: kiskorúnál alkalmazható-e, és milyen életkortól;
   - d) politikai, világnézeti, vallási vagy szakszervezeti célú nonprofit szervezet tagjaira vonatkozó kivétel: megfelel-e neki a szervezet, és teljesül-e a kívülre továbbítás tilalma.
4. Elég-e a már beépített semleges, kitalált vagy válasz nélküli egyenértékű út ahhoz, hogy a kötelező mező ne kényszerítsen különleges adat kezelésére? Kell-e ehhez külön tájékoztatás?

A 9. cikk szövegét az EUR-Lexen nem tudtam lekérni. A cikkhivatkozásokat a jogász vesse össze a hivatalos szöveggel.

**Mit változtatnánk a válasz szerint:**
- a manifest :59 és :95 „nyitott” tagmondatának lezárása vagy pontosítása;
- az ADV-dokumentum adatkör-táblája;
- a RELEASE-READINESS G2 sora;
- szükség esetén tájékoztató mondat a mezők mellé.

Típus: `bizonyíték-kapu` (BK-11, G2).

### B4 — ERT-42: harmadik személy azonosítható adata a beadásban

**Érintett hely és mostani szöveg:**
- **M7 KAPU:360 (R8, 0 pont)**: „…beazonosítható hanih-adat (név, konkrét sztori) szerepel benne. **(Adatszivárgás esetén jelzés a mentornak; ha gyermekvédelmi feltárás jelenik meg benne, az kikerül a Moodle-ből…)**”
- **HUM:712 (ERT-42 `F`)**: „…legyen DPO-jóváhagyott korlátozás, incidensértékelés, adateltávolítás és javító leadás.”

**Kérdések (DPO; QA: DPO + programvezető):**
1. Adatvédelmi incidens-e a 4. cikk 12. pontja szerint, ha a tanuló a saját beadásába egy hanih azonosítható adatát írja?
   - Az incidens a biztonság olyan sérülése, amely jogosulatlan közléshez vagy hozzáféréshez vezet.
   - Vagy jogalap nélküli, illetve adattakarékossági elvet sértő adatkezelésről van szó?
   - Számít-e, hogy a beadást csak a jogosult mentor vagy értékelő látja?
2. Ki az adatkezelő a beadásba írt harmadik személyes adat tekintetében: a szervezet, vagy a (gyakran kiskorú) tanuló?
3. Ha incidens: mi alapján kell eldönteni, hogy 72 órán belül be kell-e jelenteni a hatóságnak, mert kockázattal jár (33. cikk (1)), és értesíteni kell-e az érintett hanihot, illetve a gondviselőjét (34. cikk)?
4. Ha nem incidens: elég-e az adateltávolítás és a javító leadás belső dokumentálással?
5. Mi legyen a „jelzés a mentornak” fordulat helyén: DPO-hoz forduló incidensértékelés?

A 4., 33. és 34. cikk szövegét nem olvastam elsődleges forrásból.

**Mit változtatnánk a válasz szerint:**
- az M7 R8 kettéválasztása (D-17 b: pedagógiai pont és külön adatvédelmi stop);
- a 0-s szint „Adatszivárgás … jelzés a mentornak” mondatának cseréje a DPO-jóváhagyott eljárásra;
- a javító leadás útja;
- az ADV-dokumentum incidens-szakasza.

A rubrikaszintet és a kapuhatást ez nem érinti; az projektgazdai és értékelési döntés, VÉTÓLISTÁS.

---

### (1) Amit nem tudtam ellenőrizni
- **GDPR (EUR-Lex HU)**: a szöveg kétszer üresen jött vissza, ezért szó szerinti GDPR-idézet nincs.
- **Gyvt. 17. §**: csak összegző eszközön át jött, egymásnak ellentmondó kivonatokkal, a (4c) számozása kétséges. Az njt.hu ECONNRESET hibát adott.
- **Btk. 209/A. §**: nem olvastam, az oldal csonkult.
- **Európai Bizottság, 116-os oldal**: 404. Az EU-s 116 111 feltételsort nem kaptam meg szó szerint.
- **NMHH díjsor**: valószínűleg félreolvasás, nem használtam fel.
- **Kék Vonal-oldalak**: összegző eszközön át, szó szerinti kérésre jöttek. A rövid mondatok megbízhatók, az S5 „kérdéseit” szava valószínűleg eszközhiba.
- **Pinek**: nem ellenőriztem, hogy az M3 KAPU:366–371 tartalmaz-e pinnelt látható szöveget.
- **M2.4 `@source` blokk**: a :463-ban kezdődő blokk végét soronként nem néztem meg.

### (2) Ellentmondások a kánonban és a forrásokban
- **A Kék Vonal régi és mai oldala ellentmond egymásnak.** A kánon a régit (S6) követi, ma ez a félrevezető. A 116-000-ról a GK:47, az M3.3:709 és az M3 KAPU:367 állítja, hogy „nem általános szülői vonal”, ezt az S3 cáfolja. A 116-111-ről a GK:46, az M3.3:709, az M3 KAPU:366–367, az M2.4:659 és az M3.B:10 állítja, hogy felnőtt is hívhatja, ezt a mai oldalak nem erősítik meg.
- **A GYV-14 `F` és a GYV-4 `F` fordulata** („116 000 eltűnt gyermekek vonala”, „elsődlegesen az eltűnt gyermekek forróvonala”) a hatósági névvel egyezik. Szűkebb viszont a HUM-SAFE-01 szövegénél (GK:87: „bántalmazott vagy eltűnt”) és a szolgáltató mai leírásánál. Hogy melyik az irányadó, arról a Memuna dönt (D-05 (b) vagy (c)).
- **Az M3.3:709 doboz** a 15–17 éves madrihot is megszólítja, de a 116-000 felnőtteknek szól. A kiskorú madrih útvonala nyitott emberi döntés.
- **Az M7 R8 „kikerül a Moodle-ből”** és a GYV-11 „ne töröljünk automatikusan” között feszültség van; ez a D-10 (f) pontja.

Érintett fájlok (abszolút úttal):
- 02 Tervezet/Gyermekvédelem – release gate.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md
- 02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md
- 02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md
- 02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépéstérkép.md
- 02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md
- 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md
- 02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md

Sources:
- [Kék Vonal – 116-111 (fiataloknak)](https://kek-vonal.hu/fiataloknak/116-111)
- [Kék Vonal – főoldal](https://kek-vonal.hu/)
- [Kék Vonal – 116-000 (szülőknek)](https://kek-vonal.hu/szuloknek/116-000)
- [Kék Vonal – 116-000 (szakembereknek)](https://kek-vonal.hu/szakembereknek/116-000)
- [Kék Vonal tudástár – 116 000, szakembereknek is](https://kek-vonal.hu/tudastar/116-000-segelyvonal-a-bantalmazott-es-eltunt-gyerekekert-szakembereknek-is)
- [Kék Vonal – régi szolgáltatási oldal](https://interaktiv.kek-vonal.hu/index.php/hu/component/content/category/15-szakmai-szolgaltatasok)
- [NMHH – 116-os harmonizált számok](https://nmhh.hu/cikk/115/A_116_kezdoszamu_harmonizalt_kozerdeku_szolgaltatasok_szamainak_hasznalata_es_kijelolese)
- [EUR-Lex – 2007/116/EK, egységes szerkezetben (2023-03-06)](https://eur-lex.europa.eu/legal-content/HU/TXT/?uri=CELEX:02007D0116-20230306)
- [EUR-Lex – 2007/116/EK](https://eur-lex.europa.eu/legal-content/HU/TXT/?uri=CELEX:32007D0116)
- [Nemzeti Jogszabálytár – Gyvt. (njt.jog.gov.hu)](https://njt.jog.gov.hu/jogszabaly/1997-31-00-00)
- [Nemzeti Jogszabálytár – Btk. (njt.jog.gov.hu, csonkult)](https://njt.jog.gov.hu/jogszabaly/2012-100-00-00)
