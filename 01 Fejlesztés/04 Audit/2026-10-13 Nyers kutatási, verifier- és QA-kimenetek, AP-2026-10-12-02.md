# Nyers kutatási, verifier- és QA-kimenetek – AP-2026-10-12-02

> **Audit trail, nem kánon.** A `next-version/AP-2026-10-11-01` ágon futó AP-2026-10-12-02 célzott kör read-only ügynökeinek szó szerinti kimenetei (a helyi útvonal-előtag repó-relatívra rövidítve). A kutatói „LEZÁRHATÓ” javaslat nem javítás: csak a verifier MEGERŐSÍTVE verdiktje után, a fő session bizonyításával került a tananyagba (commitok: 3b160fc, 958bced, 16a9ad9, 11a89b4, 93da996). A döntési javaslatok összevont változata: `2026-10-13 Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md`; az állapot: `AUTOPILOT-LEDGER.md`.

## G1 – Peula-biztonsági keret (GYV-5, GYV-6, GYV-17, PRG-12)

## G1: peula-biztonsági keret (GYV-5, GYV-6, GYV-17, PRG-12). Kutatás és döntési javaslat, read-only

Semmit nem szerkesztettem. A sorszámok a HEAD `10b5d76` állapotára vonatkoznak.

**Röviden:** a „kötelező megállítási protokoll” tartalma sehol nincs rögzítve a kánonban. Lezárt szöveg csak a GYV-5 szó szerinti átvétele (GK:65). Ezért a protokollt egyik peulánál sem lehet szó szerinti átvezetéssel kitölteni. Öt tétel egyetlen emberi döntésbe vonható össze (D-GYV5). Egy apró kísérő LEZÁRHATÓ javítást találtam (M6.A:182). Egy tétel objektív része már átvezetve.

### Előzetes megállapítás: van-e a „megállítási protokoll” tartalma más néven a kánonban?
- **Lezárt kánonban nincs.** A kifejezés csak a GYV-5 szövegében és annak átvételeiben fordul elő: HUM:628, GK:65, M0.A:94, M2.A:65, :466, M3.B:275, M6.A:10, :182, :712, Z.A:59. A GK §4 (:56–67), a §4.1 (az ötlépéses jelzési út), a §4.2 és a HUM-SAFE-03 (HUM:72–73) nem ír le megállítási lépéseket. A GK:64 csak annyit mond: „felkavart kiskorút **nem küldünk ki egyedül**: legyen kijelölt biztonságos hely és egy felnőtt, aki vele van”.
- **A modulok saját lépéssorai eltérnek egymástól.** Egyik sem lezárt döntés, és kettő kifejezetten nem állítja meg a kört:
  - M0.A:134: „**Tereld vissza a kört egy kész mondattal**, és menj tovább a strukturált blokkal (a kör/feladat folytatódik mással).”
  - M2.A:281: „ne állítsd meg miatta a csoportot”; :283: „**A kört folytasd mással**”.
  - M3.B:340–346 (4.2.1): „ne várd meg a blokk végét”, a csoport rövid feladatot kap.
  - M6.A:492: „**1. Állítsd le a kört egy semleges mondattal**”. Ez az egyetlen valódi megállítás; a KAPU P1 (:347, :367) pontozott itemként kéri számon.
- **Az előző kör egyszer már elvetette a protokoll kijelölését.** A korábbi M3-vázlat ezt írta be: „(a 4.2.1 „Ha valakit megérint a téma” lépései és a 4.2.4 leállító mondata)” (scratchpad `impl/m3_blocks.txt:550`). A QA után ez kikerült, az M3.B:275 mai szövege már nem tartalmazza (lefedettségi jelentés, `35a9ddd`). Precedens tehát: a kijelölés új alkalmazási eset.
- **A „dokumentált alacsony kockázatra” nincs lezárt szabály.** Egyetlen kánoni hely sem mondja meg, ki, hol és mi alapján dokumentálja. Az incidensnyilvántartás (GK:86) ügyekre szól, a release-jegyzőkönyv (GK:19) a Memuna „átnéztem” bejegyzésére.
- **Mit jelent az `F` jelölés a HUM:612 szerint:** „A sorban megnevezett feltétel a döntés része: amíg nem teljesül, a sorban megnevezett óvatos alapértelmezés érvényes.” Formálisan tehát a mostani szó szerinti GYV-5-szöveg az óvatos alapértelmezés. Két kiskapuja (a protokoll és a dokumentált alacsony kockázat) azonban tartalom nélkül áll.

### Kutatás (külső normák)
- **NSPCC Learning, „Recommended adult to child ratios for working with children”** (https://learning.nspcc.org.uk/research-resources/briefings/recommended-adult-child-ratios-working-with-children, 2026. szeptemberi változat). Ajánlás, nem jogszabály.
  - „13 - 18 years - one adult to ten children”
  - „We recommend having at least two adults present, even with smaller groups.”
  - „If young people are helping to supervise younger children only people aged 18 or over should be included as adults when calculating adult to child ratios.”
  - „Carry out a risk assessment of the activities you are planning … This will help you decide how many adults you need and what skills and experience they should have.”
- **Keeping Children Safe, International Child Safeguarding Standards** (https://www.keepingchildrensafe.global/wp-content/uploads/2023/09/KCS-CS-Standards-ENG-200218.pdf).
  - 22. o., Standard 3: „Child safeguarding risk assessments and mitigation strategies are incorporated into existing risk assessment processes at all levels.”
  - 27. o., mintatáblázat. Kockázati tényező: „Levels of contact with children are high in the programmes and often with one staff only”. Teendő: „Assign additional member of staff to meet with children on a regular basis”.
  - Következtetés: a kockázatbesorolás szervezeti folyamat, nem a helyszíni képző egyéni ítélete.
- **Magyar jog, másodlagos forrás alapján, óvatosan.** A hivatalos NJT-oldal (njt.hu/jogszabaly/2025-6-20-0A) nem töltött be (ECONNRESET). A nem hivatalos net.jogtar.hu szerint a 6/2025. (II. 25.) BM rendelet hatálya a „csoportos, többnapos táboroztatásban … részt vevő 18 év alatti személyekre” terjed ki, és számszerű felnőtt–gyerek arányt nem ír elő. A Gyvt. 17. § a GK §3.1 szerint jelzési kötelezettség, nem felügyeleti norma. A Gyvt.-t nem olvastam végig. Hatályos magyar létszámnormát nem találtam, tehát a kérdés szervezeti döntés.
- **Scouting America** („two registered adult leaders 21 years of age or over are required at all Scouting activities”): ezt csak keresési találat mutatta, az elsődleges oldal 403-at adott. **Nem ellenőrzött**, ezért nem támaszkodom rá.

---

### M0:QA14-BIZT-2 — EMBERI DÖNTÉS [ÖSSZEVONVA: M0:QA14-BIZT-2, M2:QA14-BIZT-2, M6:QA14-BIZT-4, M2:BIZT-G3-2, M4:BIZT-G2-9 „ki a felnőtt” alkérdése → „D-GYV5”]
- **Mostani állapot:**
  - M0.A:94: „… vagy azonnal elérhető helyettes és kötelező megállítási protokoll. Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben lehet; felkavart kiskorú nem maradhat egyedül. A végleges létszámnormát a Memuna és a programvezető határozza meg.”
  - Vele szemben M0.A:133: „a kijelölt biztonságos helyen egy felnőtt legyen vele”, és :134: „a kör/feladat folytatódik mással”. Egy képzővel a kettő együtt nem teljesíthető.
  - Az M0.A ellenőrzőlistájában (:636–641) nincs GYV-5-pont. Az M2.A:466-ban és az M6.A:712-ben van. Ezt csak megfigyelésként jelzem: új pont felvétele új tartalom lenne.
- **Lezárt döntés / kánon:** a GYV-5 (HUM:628, GK:65) szó szerint átvezetve. A protokoll tartalma, az „azonnal elérhető” jelentése és az alacsony kockázat dokumentálása nincs eldöntve (lásd az előzetes megállapítást). A GK:60 / HUM:72 („fizikailag ott van, vagy ugyanazon a helyszínen azonnal elérhető”) a 15–17 éves madrih terepi felügyeletére vonatkozik. Hogy erre a helyzetre is alkalmazható-e, az új alkalmazási eset.
- **Kutatás:** lásd fent (NSPCC, KCS, magyar jog).
- **Javaslat, D-GYV5.** Ki dönt: a Memuna és a programvezető (GYV-5; GK §5:121). Öt kérdés:
  1. **Mi a „kötelező megállítási protokoll”?**
     - (a) Egyetlen közös protokoll a GK §4-ben, amelyre a peulák hivatkoznak. Csak meglévő elemekből épülne:
       - a kört semleges mondattal megállítod (M6.A:492);
       - mindenkinek felkínálod a szünetet (M6.A:496, M0.A:133);
       - a felkavart kiskorúval egy felnőtt marad a kijelölt, átlátható biztonságos helyen (GK:64, §4.2), például látótávolságban a csoporttól;
       - hívod a helyettest, és a kör csak akkor folytatódik, ha megérkezett a második felelős;
       - gyermekvédelmi aggálynál azonnal a Memuna, közvetlen veszélynél előbb a biztonság és a 112 (§4.1).
     - (b) Peulánként a meglévő lépéssor lesz a protokoll (M0.A 2.4, M2.A 4.2, M3.B 4.2.1, M6.A 4.3.2/B). Ez a legolcsóbb, de az M0.A:134 és az M2.A:281/:283 ellentmondását nem oldja fel.
     - (c) Érzékeny peulán nincs protokoll-ág, két 18+ felelős kötelező. Ez a legszigorúbb, és megfelel az NSPCC „at least two adults present” ajánlásának.
     - **Ajánlásom:** az (a). Az M6.A-nál elég a 4.3.2/B-re hivatkozni, mert az már megállítja a kört. Indok: egy képzővel csak a megállítás oldja fel a „felnőtt vele van” és a „kör folytatódik” ütközését.
  2. **Mit jelent az „azonnal elérhető helyettes”?** Ajánlás: a GK:60 mintája, „ugyanazon a helyszínen azonnal elérhető”. A telefonos elérhetőség nem elég.
  3. **Ki, hol és mi alapján dokumentálja az „alacsony kockázatot”, és mely peulák érzékenyek** (M0.A, M2.A, M2.B, M2.F, M3.B, M3.F, M4.A, M6.A, M7.F, Z.A)?
     - (i) A Memuna és a programvezető előre, peulánként besorol, kánoni helyen.
     - (ii) A programvezető alkalmanként írásos kockázatfelmérést készít (például csak felnőttekből álló csoportnál).
     - (iii) A képző maga dokumentál. Nem javaslom: önminősítés lenne.
     - **Ajánlásom:** az (i), kivételes esetre a (ii). Az önmagukat érzékenynek nevező peulák alapból ne legyenek egyszemélyesen vezethetők (M0.A:94, M2.A:279 „az egész peula önfeltáró”, M6.A:182 „Érzékeny peula”, M3.B, Z.A). Forrás: KCS Standard 3.
  4. **Végleges létszámnorma.** Ajánlás: érzékeny peulán legalább két, a HUM-SAFE-05 szerint felkészített 18+ felnőtt, 20 főig. Ez illeszkedik az NSPCC 1:10-es arányához (13–18 év) és „legalább két felnőtt” ajánlásához. A 15–17 éves madrih nem számít bele: NSPCC, illetve a HUM-SAFE-03 („soha nem ő az egyetlen felelős felnőtt”).
  5. **Az M0.A:134 és az M2.A:281–283 viszonya az egyszemélyes ághoz.** Ajánlás: feltételes mondat („ha van második felelős, a kört folytasd mással; ha nincs, a megállítási protokoll szerint állj meg”). Ezt a Memuna szövegezze.
- **Mi marad addig a fájlban:** a szó szerinti GYV-5. Az `F`-szemantika szerint ez az óvatos alapértelmezés, de a kiskapui tartalom nélkül állnak. Óvatosabb átmeneti olvasat lehetne: „amíg a protokoll és a dokumentálás nincs rögzítve, csak a kétfelnőttes ág teljesíthető”. Ez azonban szűkítő új szabály, ezért nem LEZÁRHATÓ; a döntéshozók mondják ki, ha akarják.
- **Vétó-érintettség:** gyermekvédelmi szabály (új), a kiskorúak felügyelete. Kulcs, küszöb és completion nem érintett. Az M6 KAPU P1 kulcsa (:367) nem változik.

### M2:QA14-BIZT-2 — EMBERI DÖNTÉS [ÖSSZEVONVA → D-GYV5]
- **Mostani állapot:**
  - M2.A:65: „… vagy azonnal elérhető helyettes és kötelező megállítási protokoll. Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben lehet; felkavart kiskorú nem maradhat egyedül. (A végleges létszámnormát a Memuna és a programvezető rögzíti.)”
  - M2.A:279: „Ez az egész peula önfeltáró”; :281: „ne állítsd meg miatta a csoportot”; :282: „egy felnőtt veled lesz”; :283: „**A kört folytasd mással**”.
  - M2.A:466: „Megvan a második felkészített 18+ felelős, vagy egy azonnal elérhető helyettes és a kötelező megállítási protokoll.”
- **Lezárt döntés / kánon:** ugyanaz, mint a D-GYV5-nél. Az M2.A önfeltáró besorolása a saját szövegéből következik, de hogy kizárja-e az egyszemélyes kivételt, az új alkalmazás.
- **Kutatás:** lásd fent.
- **Javaslat:** a D-GYV5 1., 3. és 5. kérdése. Az M2.A-ra ajánlott: nincs egyszemélyes kivétel (3/i), és az M2.A:281–283 feltételes alakot kap (5). Addig a :65, a :281–283 és a :466 nem változik.
- **Vétó-érintettség:** gyermekvédelmi in-the-moment utasítás (M2.A:281–283). Csak döntés után változhat.

### M6:QA14-BIZT-4 — EMBERI DÖNTÉS [ÖSSZEVONVA → D-GYV5] + kísérő LEZÁRHATÓ javítás
- **Mostani állapot:**
  - M6.A:182: „**Érzékeny peula (a 4.3 játéka érzelmileg érzékeny lehet, lásd 4.3.2/B), ezért előre:** legyen legalább két … vagy azonnal elérhető helyettes és kötelező megállítási protokoll. Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben lehet; felkavart kiskorú nem maradhat egyedül.”
  - M6.A:712: „… és a kötelező megállítási protokoll (2.3).”
  - A 4.3.2/B négy lépése az M6.A:492–505-ben áll.
- **Lezárt döntés / kánon:** hogy a 4.3.2/B négy lépése-e az M6.A protokollja, és alkalmazható-e itt az egyszemélyes kivétel, az a verifier szerint új alkalmazás (M6 QA-riport :55; a NYELV-6 javasolt NEW-ja elvetve, :85).
- **Kutatás:** lásd fent.
- **Javaslat:** D-GYV5, 1. kérdés (b), csak az M6.A-ra: a 4.3.2/B legyen a protokoll, mert az 1. lépése már megállítja a kört, és a KAPU P1 ugyanezt kéri számon. 3. kérdés: az M6.A-n ne legyen egyszemélyes kivétel, mert a peula maga nevezi magát érzékenynek. Addig 4.3.2/B-azonosítás nem kerül be.
- **Kísérő LEZÁRHATÓ javítás (GYV-5, szó szerinti átvezetés):** az M6.A:182-ből hiányzik a GYV-5 záró feltétele („Végleges létszámnorma a Memuna és programvezető hatásköre”, HUM:628; GK:65: „a végleges létszámnorma a Memuna és a programvezető hatásköre”). Az M0.A:94, az M3.B:275 és a Z.A:59 tartalmazza, az M2.A:65 zárójelben.
  - Fájl: `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md`, 182. sor
  - OLD: `Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben lehet; felkavart kiskorú nem maradhat egyedül.`
  - NEW: `Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben lehet; felkavart kiskorú nem maradhat egyedül. A végleges létszámnormát a Memuna és a programvezető határozza meg.`
  - Miért nem új szabály: a lezárt GYV-5 utolsó mondata, az M0.A:94 / M3.B:275 / Z.A:59 szó szerinti alakjában. Az OLD a fájlban egyedi; a :10-es spec más szövegű, és nem változik.
  - Vétó: gyermekvédelmi megfogalmazás, de csak szó szerinti hozzáadás; semmi nem törlődik. Látható szöveg, ezért szükség esetén `--pin-visible "GYV-5: …"`.
- **Vétó-érintettség (a fő tételnél):** gyermekvédelmi. A KAPU P1 kulcsa nem változik.

### M6:QA14-BIZT-5b — EMBERI DÖNTÉS (megerősítés jellegű; az objektív rész MÁR RENDBEN)
- **Mostani állapot:**
  - M6.A:462: „**Tiltott zóna (kötelező, a játék indítása előtt mondd ki röviden):**”
  - M6.A:464: „Ezekről a témákról nem mondunk állítást: identitás, test, család, pénz, szexualitás. Nem mondunk olyat, ami valakit kirekeszt, és senkinek nem kell érzékeny dolgot elárulnia magáról – a felállás bármikor passzolható.”
  - M6.A:466: „*(Ez a keret soha nem maradhat el, kiskorú résztvevőkkel sem.)*”
  - A verifier átmeneti NEW-ja tehát már bent van. Az identitás, a kirekesztés és az önfeltárás szerepel a keretben.
- **Lezárt döntés / kánon:** GYV-17 (HUM, 14. szakasz): „a kiskorúakra, identitásra, kirekesztésre és önfeltárásra is térjen ki”. A döntési csomag kérdése (Projektgazdai döntési csomag :355): „Legyen-e kötelező … in-the-moment lépés **kiskorú résztvevőkkel** az M6.A:459 ma opcionális tiltott-zóna kimondása”. A csomag kérdéséből úgy olvasható, hogy a „kiskorúakra kitérés” az alkalmazási kört jelenti, és ezt a :466 teljesíti. A szöveg azonban kétértelmű, és a verifier a Memunához és a peula tartalomfelelőséhez utalta.
- **Kutatás:** nem kell, belső értelmezési kérdés.
- **Javaslat.** Kérdés: mit jelent a keretben „a kiskorúakra is térjen ki”? Ki dönt: a Memuna és a peula tartalomfelelőse.
  - (a) Az alkalmazási kört jelenti, és a :466 ezt már teljesíti. Nincs további szöveg.
  - (b) Tartalmi elem kell: kiskorúakat, illetve életkort érintő állítás is tiltott zóna. Ez új tartalom.
  - (c) Korosztályi igazítás (kivsza). A :460 erről csak a fizikai biztonság kapcsán szól.
  - **Ajánlásom:** az (a), mert a csomag kérdésének szó szerinti kerete ez. Megerősítés után a tétel MÁR RENDBEN.
  - Addig a :462–466 marad. Ez az óvatos alapértelmezés: a keret mindig kötelező.
- **Vétó-érintettség:** gyermekvédelmi keret (szimulációs korlát). A KAPU :221 és :233 kulcsa nem változik.

### M3:QA14-NYELV-13 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - M3.B:465: „### 4.3.3. Gyors alkalmazás – új eset kívülről (5–8’)”
  - M3.B:467: „Adj a kiscsoportoknak előre megírt fiktív esetként **a 4. esetkártyát** …”
  - M3.B:354: „Alapból 3 csoporttal számolj; 4. csoportot csak nagyobb létszámnál indíts.”
  - M3.B:383: „Ha 4 csoport van, rövidítsd a megbeszélést esetenként két kérdésre”
  - M3.B:186 (asset-spec): „alapból ez a 4.3.3 gyors alkalmazásának előre megírt, fiktív esete.”
  - M3.B:471: „Ha az idő szűk, ezt a lépést hagyd el először, de a 4.2.4 „Fontos különbség” dobozát … ekkor is mondd el.”
- **Lezárt döntés / kánon:** PRG-12: „Az M3.B 4. esetkártyáját használjuk előre megírt fiktív példaanyagként … Memuna review szükséges a konkrét forgatókönyvre.” A szöveg feltétel nélküli, a négycsoportos esetről nem szól; a verifier szerint ez új alkalmazási eset. Más eset írása új gyermekvédelmi tartalom volna (PRG-4, GK:23).
- **Kutatás:** nem kell.
- **Javaslat.** Kérdés: mi a 4.3.3 esete 4 csoportnál? Ki dönt: az M3 modulgazdája a Memunával.
  - (a) A 4. kártya marad, a címből kikerül az „új” szó („Gyors alkalmazás – eset kívülről”). A PRG-12 szó szerinti olvasata; a 4.3.3 feladata (lépéstérkép) más, mint a 4.2-es négypontos elemzés.
  - (b) Ötödik, előre megírt, a Memuna által átnézett eset. Új tartalom.
  - (c) Négy csoportnál a lépés elmarad, és a :471 szerint a „Fontos különbség” akkor is elhangzik. Nincs új tartalom, a négy csoport amúgy is időszűkös.
  - **Ajánlásom:** az (a), mert a legkisebb, döntéshű változtatás. A (c) elfogadható alternatíva.
  - Döntés után a :186-os spec „alapból” szava `media_manifest.py build` úton igazítható.
  - Addig sem a cím, sem saját eset nem változik.
  - A PRG-12 Memuna-reviewja külön BIZONYÍTÉK-KAPU (G1, RELEASE-READINESS:24).
- **Vétó-érintettség:** gyermekvédelmi esetanyag (szimulációs korlát: harmadik személyű elemzés, M3.B:361–362). Kulcs nem érintett, a megoldójegyzet (:401–410) nem változik.

### M2:BIZT-G3-2 — EMBERI DÖNTÉS [ÖSSZEVONVA → D-GYV5]
- **Mostani állapot:**
  - Az M2.A-ban a `147f3c3` óta szó szerinti GYV-5 áll (:65, :466).
  - Az M2.B-ben és az M2.F-ben nincs GYV-5-mondat, csak a GK:64-minimum:
    - M2.B:57: „felkavart résztvevőt nem küldünk ki egyedül, ott is egy felnőtt van vele”;
    - M2.F:73 és :380 hasonlóan.
- **Lezárt döntés / kánon:** a GYV-5 csak az „érzékeny, potenciálisan felkavaró peulára” szól. Az M2.B és az M2.F besorolása új alkalmazás. A „ki lehet a másik felelős” kérdésre a HUM-SAFE-05 (GK:119: 18+ képző, mentor; ellenőrzés és gyermekvédelmi képzés) és a GK:60 („jóváhagyott, felkészített, 18 év feletti”) ad mintát, de ezek alkalmazása erre a helyzetre is döntés.
- **Kutatás:** NSPCC, csak a 18+ számít felnőttnek.
- **Javaslat:** D-GYV5, 3–4. kérdés. A „másik felelős” legyen HUM-SAFE-05 szerint ellenőrzött és felkészített 18+ személy (képző vagy mentor). Az M2.B és az M2.F besorolását a Memuna és a programvezető végezze el. Addig az M2.B és az M2.F nem kap GYV-5-mondatot.
- **Vétó-érintettség:** gyermekvédelmi, a kiskorú résztvevők felügyelete.

### M4:BIZT-G2-9 — EMBERI DÖNTÉS [ÖSSZEVONVA → D-GYV5; a GYV-6-rész MÁR RENDBEN, a küszöb-QA BIZONYÍTÉK-KAPU]
- **Mostani állapot:**
  - M4.A:58: „… A szereplési szorongás önmagában nem gyermekvédelmi krízis, de bárki bármikor megállhat és passzolhat. Ha valakinél saját érintettség kerül elő, a képző nem folytat nyilvános feldolgozást … felkavart kiskorút nem küldünk ki egyedül: legyen kijelölt biztonságos hely és egy felnőtt, aki vele van.”
  - Ugyanez áll az M4.B:63-ban, és a minimum az M4.F:80-ban.
- **Lezárt döntés / kánon:** a GYV-6 („A meglévő GK §4:63–64 védelmi minimum szerepeljen röviden minden releváns peula képzői instrukciójában … A szereplési szorongás nem automatikusan gyermekvédelmi krízis, de legyen szabad megállni és passzolni; a Memuna hagyja jóvá a küszöböt.”) szó szerint teljesül. Ez a rész MÁR RENDBEN. A „Memuna hagyja jóvá a küszöböt” rész szerepköri utólagos QA: BIZONYÍTÉK-KAPU (G1). Nyitott marad a „ki a felnőtt, aki vele van” kérdés, és hogy az M4.A érzékeny peula-e a GYV-5 szerint (GYV-5, `plan-M4` :1068).
- **Kutatás:** lásd fent.
- **Javaslat:** D-GYV5, 3. kérdés. Az M4.A-t a Memuna és a programvezető sorolja be. Ajánlás: nem érzékeny, mert a szereplési szorongás a GYV-6 szerint nem automatikusan krízis, így a GYV-5 nem kötelező rá. Ez a kijelölt szerepek ítélete. A :58, :63 és :390 mentori útja nem törölhető, felügyeleti arányt nem írunk be.
- **Vétó-érintettség:** gyermekvédelmi; semmi nem változik.

---

### Összesítő

| Kulcs | Besorolás | Egysoros indok |
|---|---|---|
| M0:QA14-BIZT-2 | EMBERI DÖNTÉS (D-GYV5) | a protokoll tartalma, az „azonnal elérhető”, az alacsony kockázat dokumentálása és a létszámnorma nincs a kánonban; Memuna + programvezető |
| M2:QA14-BIZT-2 | EMBERI DÖNTÉS (→ D-GYV5) | ugyanaz, plusz az M2.A:281–283 feltételes alakja |
| M6:QA14-BIZT-4 | EMBERI DÖNTÉS (→ D-GYV5) + kísérő LEZÁRHATÓ | a 4.3.2/B kijelölése új alkalmazás; az M6.A:182-ből hiányzó GYV-5 zárómondat szó szerint pótolható |
| M6:QA14-BIZT-5b | EMBERI DÖNTÉS (megerősítés) | a :466 átmeneti javítás bent van; a „kiskorúakra kitérés” jelentését a Memuna és a tartalomfelelős erősítse meg; ajánlás: alkalmazási kör, és akkor MÁR RENDBEN |
| M3:QA14-NYELV-13 | EMBERI DÖNTÉS | a PRG-12 nem szól a négycsoportos esetről; ajánlás: a 4. kártya marad, a címből kikerül az „új”; Memuna-review: G1-kapu |
| M2:BIZT-G3-2 | EMBERI DÖNTÉS (→ D-GYV5) | az M2.B/M2.F besorolása és a „másik felelős” (HUM-SAFE-05 minta) a kijelölt szerepeké |
| M4:BIZT-G2-9 | EMBERI DÖNTÉS (→ D-GYV5) | a GYV-6-rész teljesül (M4.A:58, M4.B:63, M4.F:80); a küszöb-QA G1-kapu; az M4.A besorolása nyitott |

Források:
- [NSPCC Learning – Recommended adult to child ratios for working with children](https://learning.nspcc.org.uk/research-resources/briefings/recommended-adult-child-ratios-working-with-children)
- [Keeping Children Safe – International Child Safeguarding Standards (PDF)](https://www.keepingchildrensafe.global/wp-content/uploads/2023/09/KCS-CS-Standards-ENG-200218.pdf)
- [6/2025. (II. 25.) BM rendelet – net.jogtar.hu (nem hivatalos, másodlagos)](https://net.jogtar.hu/jogszabaly?docid=a2500006.bm); a hivatalos [NJT-oldal](https://njt.hu/jogszabaly/2025-6-20-0A) nem volt elérhető
- [Scouting America – Youth Protection and Adult Leadership](https://www.scouting.org/health-and-safety/gss/gss01/) (403, nem ellenőrzött, nem támaszkodtam rá)

## G2 – Eszkalációs út, küszöb és címzett

## G2 — eszkalációs út, küszöb és címzett (AP-2026-10-12-02, read-only)

Minden tételt végigvittem, levágás nincs. A tananyag sorszámai elcsúsztak: az M0.2 kérdéses sora ma `:271`, a M3.3 régi `:697/:698/:705` sorai ma `:546/:547/:554`.

**A kutatás forrásai és korlátai:**
- **Gyvt.** A hivatalos njt.hu nem volt elérhető (ECONNRESET). A Gyvt.-t a net.jogtar.hu-ról (Wolters Kluwer) olvastam, ez **másodlagos** forrás. Ráadásul összegző eszközön át kaptam meg, ezért a szó szerinti idézeteket az átvétel előtt az njt.hu-n újra kell olvasni.
- **Kék Vonal.** Az oldalakat szintén összegző eszközön át értem el. A döntő mondatokat a `2026-10-11 Validált findingok – M3` verifier-idézetéből veszem át, amely elsődleges forrásból készült (2026-10-11).
- **NMHH, europa.eu.** Ezek elsődleges hatósági, illetve uniós források.

---

### M6:QA14-BIZT-1 — EMBERI DÖNTÉS [ÖSSZEVONVA: M6:QA14-BIZT-1, M6:QA14-BIZT-2 — egy Memuna-döntés a GYV-7 M6-os alkalmazásáról]
- **Mostani állapot:**
  - Az M6.2 már tartalmazza a második lépcsőt. `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:783`: „Ha valaki pusztán nehéz érzésről beszél (például friss gyászról), és veszélyeztetettség nem merül fel, az nem jelzési ügy: támogatást ajánlasz neki, és ő választja meg, él-e vele.”
  - Az M6.3 a „friss seb”-et az ötlépéses jelzési útra küldi. `…/M6.3 – Kézműves, ami tanít is.md:749`: „valós, nehéz saját helyzetet (friss seb, bántalmazás, önsértés) hoz fel … az **ötlépéses jelzési utat** követed”.
  - Az M6.4 két helyen ugyanígy. `…/M6.4 – Döntési szcenáriók – mit választanál.md:933–934` (6D) és `:1028` (ZÁRÓ): „valós, súlyos témát (bántalmazás, önsértés, friss seb) tár fel, az már **nem játék**: az **ötlépéses jelzési utat** követed”.
- **Lezárt döntés / kánon:**
  - GYV-7 (HUM:630): „pusztán nem veszélyeztető nehéz érzelemnél támogató mentorálás, választási lehetőséggel”.
  - A GYV-7 döntési csomagja M6-helyként csak az M6.2:777–779-et sorolja fel (`2026-10-12 Projektgazdai döntési csomag…:266`). Az M6.3/M6.4 dobozokra tehát nem szól.
  - A 2026-10-05-i jegyzőkönyv (`2026-10-05 Projektgazdai döntés – M6.4 elfogadás és Command 5 hatókör.md:31`): „the 6D/ZÁRÓ safeguarding repetition remains Memuna QA; do not change it now.”
  - M6-NY-D27 (`2026-10-04 Projektgazdai döntések – M6 nyelvi review.md:290`): „A D1 kiváltó feltétele és a Memuna bevonásának küszöbe ne változzon.”
  - A GYV-7 kiterjesztése ezért új alkalmazási eset.
- **Kutatás:** nem külső tényen múlik.
- **Javaslat:**
  - **Kérdés:** a GYV-7 kétlépcsős küszöbe vonatkozik-e az M6.3:749 és az M6.4 6D/ZÁRÓ dobozára, és ha igen, ki adja a „támogató mentorálást” a madrih–hanih viszonyban?
  - **Ki dönt:** a Memuna (HUM-SAFE-01/03).
  - **Opciók:**
    - (a) A „friss seb” kikerül a kiváltó felsorolásból, és az M6.2:783 utolsó mondata szó szerint bekerül az M6.3/M6.4 dobozba. Ezzel a modul egységes lesz.
    - (b) A „friss seb” marad, de pontosítva: „veszélyeztetettséggel járó”.
    - (c) Marad a mostani állapot (túleszkaláció). Ez ütközik a GYV-13 elvével: puszta érzelmi megosztás miatt nem sugallunk kötelező jelentést.
  - **Ajánlásom:** az (a), a QA14-BIZT-2 kiegészítésével. A „támogatást ajánlasz” mondat a már kánoni M6.A:502 mintájára maradjon („Itt vagyok, ha beszélni szeretnél – de nem kötelező.”). Mellé kerüljön az M3.3:416 meglévő mondata: „Sokszor pont az a nehéz, hogy bizonytalan vagy. Ilyenkor is fontosabb segítséget kérni, mint egyedül maradni vele.” Így a kiskorú madrih nem marad egyedül a „nem jelzési ügy” minősítéssel (GK §4:59–60). Hogy bizonytalanság esetén a helyszíni 18+ felelős vagy a Memuna a konzultációs út, az új szabály, ezt is a Memuna dönti el.
  - **Addig:** egyik doboz sem változik. A mostani szöveg védelmi szempontból óvatos (túleszkalál), nem gyengít.
- **Vétó-érintettség:** gyermekvédelmi megfogalmazás és a kiskorú madrih szerepe. Kulcsot, küszöböt és completiont nem érint.

### M6:QA14-BIZT-2 — EMBERI DÖNTÉS [ÖSSZEVONVA az M6:QA14-BIZT-1-gyel]
- **Mostani állapot:** M6.2:783 (lásd fent): „az nem jelzési ügy: támogatást ajánlasz neki”. Felnőtt vagy mentor nincs megnevezve.
- **Lezárt döntés / kánon:**
  - GYV-7: „támogató mentorálás”. Ez a mentor–tanuló viszonyra szól. A HUM-SAFE-03 (HUM:73) bizalmas kontaktja („a mentor vagy … a Memuna”) a madrih saját ügyére vonatkozik, nem a hanihéra.
  - GK §4:60: „a gyermekvédelmi felelősség az övé [a 18+ felnőtté]; a madrih a saját szerepében figyel és jelez”.
  - A madrih–hanih viszonyra a döntés nem szól, ezért ez új alkalmazási eset.
- **Javaslat:** a Memuna döntse el, ki mentorál, és van-e konzultációs út. Az ajánlásomat lásd fent.
  - **Addig:** a mondat marad. Nem óvatos alapértelmezés, de védelmi elemet nem töröl.
- **Vétó-érintettség:** a kiskorú madrih szerepe.

### M7:QA14-BIZT-6 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - `02 Tervezet/Modulok/M7/Peulák/M7.B – Peula v2 & Zmán Kvucá – amikor a papír találkozik a valósággal.md:480`: „Ha olyasmire kerestek választ, ami **gyermekvédelemmel, bántalmazással, komoly szorongással** kapcsolatos, arra ne AI-tól kérjetek tanácsot, hanem **a Memunától**.”
  - Ugyanebben a fájlban, `:93` (képzői felkészülés, már kétlépcsős): „ha … valakit láthatóan nagyon megérint egy téma (mentor / képzésfelelős), vagy ha gyermekvédelmi jelzés jön (azonnal a Memuna …)”.
- **Lezárt döntés / kánon:** a GYV-7 a „komoly szorongás” esetét nem dönti el, ezért ez új alkalmazási eset. A meglévő „GYV-13, GYV-7 (QA) | Memuna” sorhoz tartozik.
- **Javaslat:**
  - **Kérdés:** a :480 tanácskérési szabályában a „komoly szorongás” a Memunához menjen, vagy a mentorhoz, veszélyeztetettség gyanújánál azonnal a Memunához?
  - **Ki dönt:** a Memuna.
  - **Opciók:**
    - (a) marad;
    - (b) a :93 szerkezete szerint: gyermekvédelmi, bántalmazási ügyben a Memuna; komoly szorongásnál a mentor, veszélyeztetettség gyanújánál azonnal a Memuna;
    - (c) „a Memunától vagy a mentorodtól”.
  - **Ajánlásom:** a (b), mert a modul saját :93 sorával egyezik, és a GYV-7-et követi.
  - **Addig:** a mondat marad. Ez óvatos alapértelmezés. Az AI-tilalom egyik opcióban sem gyengülhet.
- **Vétó-érintettség:** gyermekvédelmi megfogalmazás és AI-kikötés (nem törölhető).

### Z:QA14-BIZT-2 — EMBERI DÖNTÉS (nem blokkoló; a mostani szöveg teljesíti a GYV-8-at)
- **Mostani állapot:**
  - `02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md:310`: „… nem vezetek éles foglalkozást, hanem jelzem a képzőnek; ha pedig akut kockázatot látok, a Memunát is azonnal bevonom.”
  - A :301–316 dián nincs 112. A mintamondat az LMS-Z-07 elfogadási tárgya (:316).
- **Lezárt döntés / kánon:**
  - GYV-8 (HUM:631): „Pusztán hiányzó felnőtt felügyelet operatív ügyét a képző/programvezető rendezi, akut kockázatnál Memuna is.” Ez szó szerint át van vezetve.
  - GK §4.1:83: „Ahol a teljes felsorolás nem a hely feladata, elég az utalás: … „azonnal vond be a Memunát””.
  - A 112 bevitele új alkalmazás.
- **Kutatás:** europa.eu (https://europa.eu/youreurope/citizens/travel/security-and-emergencies/emergency/index_hu.htm): „Aki ezt a számot tárcsázza, annak hívása azonnal a segélyszolgálatokhoz – a mentőkhöz, a rendőrséghez, illetve a tűzoltósághoz – fut be.”
- **Javaslat:**
  - **Kérdés:** kerüljön-e a Z.3 biztonsági lépésébe a GK §4.1 5. lépése („Közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés.”)?
  - **Ki dönt:** a Memuna és a programvezető.
  - **Opciók:**
    - (a) marad;
    - (b) az 5. lépés szó szerint a :303 magyarázó dobozba kerül, a mintamondat érintetlen;
    - (c) a mintamondatba kerül.
  - **Ajánlásom:** a (b). Így a „jelzem a képzőnek” és az „akut kockázatnál Memuna is” tagmondat, valamint az LMS-Z-07 kritériuma nem változik.
  - **Addig:** marad. Kánonkonform.
- **Vétó-érintettség:** gyermekvédelmi megfogalmazás. A (c) az LMS-Z-07 elfogadási kritériumát érintené.

### M2:QA14-BIZT-3 — LEZÁRHATÓ (eltér a verifier besorolásától, indoklás lent)
- **Mostani állapot:** `02 Tervezet/Modulok/M2/Peulák/M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md:362`: „Ha aggasztót hallasz, hallgasd meg, de ne nyomozz, és ne kérdezz rá a részletekre: ezzel ne maradj egyedül, azonnal szólj a képzőnek, aki a kijelölt úton bevonja a Memunát.”
- **Lezárt döntés / kánon:**
  - GYV-19 (HUM:642) **név szerint az M2.A-ra** szól: „Mind az M2.A, mind az M4.3 gyakorlat-instrukciója kapjon … határmondatot: … a képzőnek és a Memunának a kijelölt úton jelezni kell.”
  - A döntési csomag (a) opciója is kifejezetten az M2.A-ra adja a képzőt: „az M2.A-ban és „azonnal szólj a képzőnek”” (`…döntési csomag…:375`).
  - A mostani szöveg ezzel szemben a képzőtől teszi függővé a Memuna-jelzést. Eltér az M2-n belüli többi helytől is: M2.4:209 „(3) **azonnal bevonod a Memunát**”, valamint az M2.B, a KAPU és az M2.4:37.
- **Miért nincs ütközés a GK §4.1:82-vel:**
  - A GK §4.1:82 szerint a címzett „mindig a Memuna …, nem „egy felnőtt””. Ez azt tiltja, hogy valaki a Memuna *helyett* kapja a jelzést. Az „és” szerkezetben a Memuna címzett marad.
  - A képző az élő peulán a helyszíni 18+ felelős (GK §4:60).
  - A GYV-8 ugyanezt a modellt rögzíti: „ez nem két alternatív, egymást helyettesítő címzett”.
- **Javaslat (szerkesztés):**
  - Fájl: `02 Tervezet/Modulok/M2/Peulák/M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md`, 362. sor
  - OLD: `azonnal szólj a képzőnek, aki a kijelölt úton bevonja a Memunát.”`
  - NEW: `azonnal szólj: a képzőnek és a Memunának a kijelölt úton jelezni kell.”`
  - Miért nem új szabály: a GYV-19 utolsó tagmondatának szó szerinti átvétele azon a helyen, amelyet a döntés megnevez. Az „azonnal szólj” a mostani szövegből marad.
  - Ha a fő session a GK §4.1:82-ütközést mégis valósnak ítéli, a tartalék besorolás EMBERI DÖNTÉS (Memuna), és addig a mondat marad.
- **Vétó-érintettség:** gyermekvédelmi megfogalmazás (vétólista, Memuna QA). Kulcsot és completiont nem érint.

### M4:QA14-BIZT-3 — EMBERI DÖNTÉS
- **Mostani állapot:** `02 Tervezet/Modulok/M4/Online leckék/M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md:360`: „**Ha egy hanihhal folytatott beszélgetésben gyermekvédelmi aggály merül fel,** az már nem kérdezésgyakorlás: hallgasd meg, de ne nyomozz, ne folytass rávezető kérdésekkel „kihallgatást”, és ne próbáld egyedül megoldani; **azonnal vond be a kijelölt Memunát** …”
  - A GK §4:57 része **megvan**. Csak a „képző” hiányzik.
- **Lezárt döntés / kánon:**
  - A GYV-19 szó szerint az M4.3-ra is „képzőt” ír.
  - A :360 viszont terepi hanih-helyzet, ahol nincs képző. Ott a GK §4:60 / GYV-8 szerint a helyszíni 18+ felelős cselekszik, a címzett a Memuna (GK §4.1:82).
  - A szó szerinti átvétel tehát egy terepi helyzetben új címzettet vezetne be. Két lezárt szöveg ütközik, és ez új alkalmazási eset.
- **Javaslat:**
  - **Kérdés:** a GYV-19 „képző” eleme csak a képzés közbeni feltárásra (M2.A) szól, vagy az M4.3 terepi hanih-helyzetére is?
  - **Ki dönt:** a Memuna, a projektgazdával.
  - **Opciók:**
    - (a) csak az M2.A-ra szól, az M4.3 kész (a GK §4.1:82 szerint);
    - (b) az M4.3-ba a helyszíni 18+ felelős kerül (a GYV-8 szerint), képző nélkül;
    - (c) a szó szerinti „képző”.
  - **Ajánlásom:** az (a). A terepen nincs képző, a GK §4.1:82 nem gyengül. A (b) új címzett lenne az M4-ben.
  - **Addig:** a mostani szöveg marad, ez az óvatos alapértelmezés. Az `M4:BIZT-G1-6` nem jelölhető FIXED-nek a „képző” részig.
- **Vétó-érintettség:** gyermekvédelmi megfogalmazás.

### M3:QA14-BIZT-1 — MÁR RENDBEN
- **Mostani állapot:**
  - `02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md:554` (az S3 „Vágásnyomok” ágának S3-SAFE doboza): „A részletek kiderítése a Memuna és – ahol indokolt – a hivatalos szervek feladata, nem a tiéd.” Ugyanez áll a :546 és :547 sorban.
  - Az M3 KAPU ITEM 9 („otthon bántják”), `02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md:243`, `:248`: „a részletek … a Memuna és a hatóság dolga.”
- **Lezárt döntés / kánon:**
  - A GYV-15 döntési kérdése (`…döntési csomag…:337`) kifejezetten ezeket a helyeket nevezi meg: „Maradhat-e ez a fordulat (M3.3:697, :698, :705; KAPU:243, :248) az önsértés-esetnél is”.
  - A forrás-finding helye (`2026-10-11 Validált findingok – M3…:2878`): „M3.3 > S3 visszajelzések (:697, :698) és az S3-SAFE doboz (:705)”.
  - A régi :697/:698/:705 ugyanazzal a 8 soros eltéréssel a mai :546/:547/:554. Az idézett régi :705 szöveg („Meghallgatni szabad – kihallgatni / nyomozni nem. A részletek kiderítése a Memuna és a hatóság dolga, nem a tiéd.”) megegyezik a mai :554-gyel, csak a GYV-15-ös csere tér el. Git-historyt nem futtattam.
  - Az S3-SAFE doboz tehát a GYV-15 eldöntött kérdésének része, nem új alkalmazás.
  - A KAPU ITEM 9 bántalmazási eset, kívül esik a GYV-15 „önsértési eseteknél” hatókörén. A döntés szerint marad.
- **Javaslat:** nincs szerkesztés. Ha a lecke és a kapu egységesítése kívánatos, az **külön, opcionális** új alkalmazás, Memuna és jogász döntése (JOG-1/X-15). A kulcs, a ✅ és a :546–547 nem változik.
- **Vétó-érintettség:** nincs változás.

### M0:BIZT-5 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - `02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrih, nem terapeuta – szerepek és elvárások.md:271`: „A) A csoportchatben leállítom a szívatást, figyelek az érintettre, és **jelzek** a Memunának ✅”
  - `…/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md:310`: „B) „Srácok, ez már nem vicces, álljunk meg. …” ✅” (Memuna nélkül)
  - `02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md:242`: „… szükség esetén hivatalos segítségi utat használni. ✅”
- **Lezárt döntés / kánon:** a GYV-7 maga a Memunára hagyja: „A csoportchatbántalmazás M0-specifikus küszöbét a Memuna külön ellenőrizze; a kvízkulcs nem módosul vélelmezésből.”
- **Javaslat:**
  - **Kérdés:** a kvuca-csoportchatben zajló szívatás minden esetben Memuna-jelzés, vagy csak zaklatás vagy veszélyeztetettség jele esetén?
  - **Ki dönt:** a Memuna. A belépőkvíz itemszövege a projektgazdáé (hub :180).
  - **Opciók:**
    - (a) mindig jelzés (az M0.2 mintája; GK §4.1:81: a Memuna felel a „sértéssel, bántalmazással, zaklatással kapcsolatos ügyekben”);
    - (b) GYV-7-es kétlépcső: zaklatásnál a Memuna, alkalmi beszólásnál beavatkozás a chatben és a mentor;
    - (c) helyenként eltérő.
  - **Ajánlásom:** a (b), azzal, hogy az ismétlődő csúfolás „zaklatásnak” minősül. A minősítés a Memunáé. Utána az eltérő hely visszajelzése objektív átvezetés. A kulcs nem változik.
  - **Addig:** marad. Mindkét minta beavatkozást tanít.
- **Vétó-érintettség:** gyermekvédelmi küszöb. A kvízkulcs védett.

### M6:BIZT-G1-1 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:355` (P1 ✅ A): „… és ha valaki erősen érintett, még a peula alatt bevonom a kijelölt Memunát …”
  - Visszajelzés, `:367`: „(4) **még a peula alatt bevonod a Memunát**, ha valaki erősen érintett – nem maradsz egyedül a helyzettel”.
  - Helyszíni 18+ felelős és munkaidőn kívüli út nincs benne.
  - Az M6.B játéklap „kit hívsz” rovata, `…/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:48`, `:216`, `:244` (spec).
- **Lezárt döntés / kánon:**
  - A küszöb lezárt (M6-NY-D3: „…bevonod a Memunát, ha valaki erősen érintett”).
  - GYV-8: „Terepi veszélynél a helyszíni 18+ felelős cselekszik azonnal, és a szervezeti Memuna-jelzés külön megtörténik”.
  - A GYV-4 a (b) alkérdést név szerint felsorolja (`…döntési csomag…:239`). Az egységes elsődleges mondat az M2.4:209-ben áll: „Ha a Memuna nem érhető el vagy érintett, a helyettesét vond be; ha egyikük sem érhető el (például munkaidőn kívül), érzelmi támogatásra a Kék Vonal 116-111 az út …”.
  - Hogy egy *játékbeli felkavarodás* „terepi veszély”-e (GYV-8), vagy a GYV-7 második lépcsője, az új alkalmazás. Ráadásul feszül a D3-mal.
- **Javaslat:**
  - **Kérdés:** a P1 és a játéklap nevezze-e meg elsőként a helyszíni 18+ felelőst a Memuna mellett, és kerüljön-e a P1 visszajelzésébe az M2.4:209 elérhetetlenségi mondata?
  - **Ki dönt:** a Memuna és a programvezető. A ✅-szöveg változásánál az értékelési felelős és a projektgazda is.
  - **Opciók:**
    - (a) csak a visszajelzés kap két szó szerinti kánoni elemet: a GK §4:60-at és az M2.4:209-et; a ✅ opció szövege nem változik;
    - (b) a ✅ opció szövegébe is bekerül;
    - (c) marad.
  - **Ajánlásom:** az (a).
  - A (c) alkérdés (G1 hatókör) a GK §2 és a HUM 11. szakasz „A Memuna-átnézés hatóköre” sora alapján G1-bizonyíték-kapu, nem döntés.
  - **Addig:** marad. Nem teljesen óvatos (munkaidőn kívül elérhetetlen utat tanít), de védelmi elemet nem töröl.
- **Vétó-érintettség:** kulcsszöveg (✅ A), R4 blokkoló sor (játéklap), gyermekvédelmi megfogalmazás.

### M3:BIZT-G2-2 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - `02 Tervezet/Gyermekvédelem – release gate.md:47`: „**116-000**: … felnőttek is hívhatják; nem általános „szülői vonal”;”
  - Ugyanezt követi az M3.3:709 (📞 doboz) és a KAPU:367.
  - Az M3.3:709 és a GK:46 azt is állítja, hogy a 116-111 a „gyerek érdekében telefonáló” felnőttet is fogadja.
- **Lezárt döntés / kánon:**
  - HUM 8. „Segélyvonalak” (HUM:471) → GK §3.3. Vétó/QA: a Memuna.
  - GYV-14 (`F`): „Ha a kánon félrevezető, a Memuna formálisan nyissa újra a konkrét tájékoztató sort; ne változtassunk telefonszámot igazolás nélkül.” A feltétel tehát Memuna-aktus.
  - A GYV-14 saját fordulata („116 000 eltűnt gyermekek vonala”) szűkebb, mint a HUM-SAFE-01 („bántalmazott vagy eltűnt gyermek ügyében 116-000”) és a szolgáltató leírása. Szó szerint nem vezethető át.
- **Kutatás:**
  - Kék Vonal (kek-vonal.hu/tudastar/116-000-segelyvonal-a-bantalmazott-es-eltunt-gyerekekert-szakembereknek-is; az idézet a 2026-10-11-i verifiertől): „A 116 000 Segélyvonalon várjuk azoknak a felnőtteknek a hívásait, akik aggódnak egy gyermekért”.
  - kek-vonal.hu/szuloknek/116-000: „HÍVJ MINKET, ha aggódsz egy gyerekért!”
  - kek-vonal.hu/fiataloknak: a 116-111 a gyerekek és fiatalok vonala. Arra, hogy felnőtt hívót is fogad, megerősítést nem találtam (összegző eszközön át).
  - NMHH (https://nmhh.hu/cikk/115/A_116_kezdoszamu_harmonizalt_kozerdeku_szolgaltatasok_szamainak_hasznalata_es_kijelolese): a 116000 neve „Eltűnt gyermekek felkutatására fenntartott forróvonal”, amely „fogadja az eltűnt gyermekekkel kapcsolatos hívásokat és közvetíti azokat a rendőrség felé”. A 116111 neve „Gyermekek segélyvonala”.
  - europa.eu: a 116 000 a „gyermekek eltűnésének bejelentésére szolgáló európai forródrót”.
- **Javaslat:**
  - **Kérdés:** a Memuna újranyitja-e a HUM:471 sort, és milyen 116-111/116-000-leírást hagy jóvá a GK §3.3-ba és a §4.1-be?
  - **Ki dönt:** a Memuna.
  - **Opciók:**
    - (a) nincs újranyitás;
    - (b) újranyitás, és a leírás a szolgáltató szerint: 116-111 a gyerekeknek és fiataloknak; 116-000 bántalmazott és eltűnt gyerekek ügyében, a gyermekért aggódó felnőtteknek (szülőknek, szakembereknek) is; a „nem általános szülői vonal” és a 116-111 felnőtt-állítás törlése;
    - (c) a GYV-14 szűk fordulata.
  - **Ajánlásom:** a (b), a release-napi ellenőrzéssel (GK §6) egy lépésben. Telefonszám nem változik.
  - **Addig:** a mostani szöveg marad, mert repóból nem írható át. Nem óvatos alapértelmezés: egy aggódó felnőttet rossz vonalra küldhet. Ezért a Memuna-döntés P1.
- **Vétó-érintettség:** gyermekvédelmi tájékoztató sor (HUM:471 → REOPENED).

### M3:BIZT-G1-8 — BIZONYÍTÉK-KAPU (egy kapcsolódó LEZÁRHATÓ szerkesztéssel)
- **Mostani állapot:** `02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md:41–42`.
  - A Btk.-mondat már a JOG-1 szerint áll (ce04b9c): „A Btk. 209/A. § nem valamennyi jelzéskésés általános büntetőszabálya, hanem a Gyvt. 17. § (4a)–(4c) szerinti speciális kötelezettségekhez kötődik.”
  - A :42 vége: „Azt, hogy az adott szervezeti jogállás mellett ki tesz külső jelzést, az éles használat előtt rögzíteni kell, és a Memunának jóvá kell hagynia; a külső jelzés jogi kérdésében jogi szakértő dönt.”
- **Lezárt döntés / kánon:** JOG-1 (HUM:662): „a szervezet nevében a jogi tanács alapján kijelölt felnőtt dönt a külső jelzésről, anélkül hogy az akut védelem késne. A Gyvt. 17. § konkrét címzettjeit/időhatárait jogász ellenőrizze”. Jóváhagyás: Memuna; a nyilvántartás helyéről a projektgazda dönt.
- **Kutatás (másodlagos forrás, net.jogtar.hu):**
  - Gyvt. 17. § (1): a jelzőrendszer tagjai között „az egyesületek, az alapítványok és az egyházi jogi személyek”.
  - (2): „kötelesek a) jelzéssel élni a gyermek veszélyeztetettsége esetén …, b) hatósági eljárást kezdeményezni …”.
  - (4a): „Ha az (1) bekezdésben meghatározott személy vagy szerv alkalmazottja kiemelt veszélyeztető okra utaló körülményt észlel, és haladéktalanul, de legkésőbb három munkanapon belül nem tesz eleget … büntetőjogi felelősségre vonásának van helye.”
  - (4b) a szervezeten belüli láncot szabályozza: a jelzés a vezető vagy „arra kijelölt személy” útján megy, mindkét lépésre három munkanap.
  - A szöveg „alkalmazottról” szól. Hogy egy önkéntes madrihra vonatkozik-e, az jogi minősítés, nem a repóé.
- **Mi hiányzik:**
  - A jogász írásos ellenőrzése (címzettek, határidők, a (4b) alkalmazhatósága) és a Memuna jóváhagyása: G1-bizonyíték.
  - A kijelölt felnőtt megnevezése: szervezeti aktus.
  - A nyilvántartás helye: kis projektgazdai döntés, a JOG-1 szerint („G1 #1 issue vagy új HUM-sor”).
- **Kapcsolódó LEZÁRHATÓ szerkesztés (a JOG-1 szó szerinti átvétele):**
  - Fájl: `02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md`, 42. sor
  - OLD: `; a külső jelzés jogi kérdésében jogi szakértő dönt.`
  - NEW: `; a szervezet nevében a jogi tanács alapján kijelölt felnőtt dönt a külső jelzésről, anélkül hogy az akut védelem késne.`
  - Miért: a mostani mondat azt sugallhatja, hogy a jogász dönt a jelzésről, és ez késleltethet. A JOG-1 a kijelölt felnőttet nevezi meg, és kimondja, hogy az akut védelem nem késhet. A madrih nem kap külső jelzési feladatot. A hub mondata nem törlődik, csak a döntő szerep pontosodik.
- **Vétó-érintettség:** gyermekvédelmi és jogi megfogalmazás. Jogi és Memuna QA.

---

## Összesítő

| Kulcs | Besorolás | Indok |
|---|---|---|
| M6:QA14-BIZT-1 | EMBERI DÖNTÉS (+QA14-BIZT-2) | A GYV-7 csak az M6.2-re szól; a 6D/ZÁRÓ 2026-10-05 óta Memuna-QA, a D27 zárolja a küszöböt |
| M6:QA14-BIZT-2 | EMBERI DÖNTÉS (összevonva) | A „támogató mentorálás” a madrih–hanih viszonyban új alkalmazás, és a kiskorú madrih szerepét érinti |
| M7:QA14-BIZT-6 | EMBERI DÖNTÉS | A „komoly szorongás” a GYV-7 két lépcsője között; ajánlás: a modul :93 szerkezete |
| Z:QA14-BIZT-2 | EMBERI DÖNTÉS (nem blokkoló) | A GYV-8 szó szerint át van vezetve; a 112 bevitele új alkalmazás, ajánlás: a :303 dobozba |
| M2:QA14-BIZT-3 | LEZÁRHATÓ | A GYV-19 név szerint az M2.A-ra adja „a képzőnek és a Memunának” szöveget; az „és” nem sérti a GK §4.1:82-t |
| M4:QA14-BIZT-3 | EMBERI DÖNTÉS | Terepi hanih-helyzetben a „képző” új címzett lenne; ajánlás: csak az M2.A-ra szól |
| M3:QA14-BIZT-1 | MÁR RENDBEN | Az S3-SAFE doboz (régi :705) a GYV-15 eldöntött kérdésében név szerint szerepelt; az ITEM 9 bántalmazás, kívül esik |
| M0:BIZT-5 | EMBERI DÖNTÉS | A GYV-7 kifejezetten a Memunára hagyja az M0 csoportchat-küszöbét |
| M6:BIZT-G1-1 | EMBERI DÖNTÉS | A helyszíni 18+ felelős játékbeli felkavarodásnál új alkalmazás; a (b) az M2.4:209-cel, a (c) G1-bizonyíték |
| M3:BIZT-G2-2 | EMBERI DÖNTÉS | A GYV-14 feltétele a HUM:471 Memuna-újranyitása; a Kék Vonal és a kánon eltér |
| M3:BIZT-G1-8 | BIZONYÍTÉK-KAPU (+1 LEZÁRHATÓ szerkesztés) | Jogászi ellenőrzés és Memuna-jóváhagyás hiányzik; a hub :42 a JOG-1-gyel szó szerint pontosítható |

**Átfedés:** az M6:QA14-BIZT-1 és -2 egy döntés. Az M0:BIZT-5, az M7:QA14-BIZT-6 és az M6-os tételek egy Memuna GYV-7-csomagba kérdezhetők, de külön kérdések. Az M2- és az M4-tétel a GYV-19-ből ered, de külön zárul: az M2 LEZÁRHATÓ, az M4 döntést kér.

## G3 – Gyermekvédelmi tartalmú értékelés

## G3: gyermekvédelmi tartalmú értékelés. Kutatási és döntési javaslat (read-only)

Hét tételt vittem végig: ezekben idéztem a mostani szöveget, és ellenőriztem a lezárt döntéseket. A két M7-es tételt nem értem el, ezek a lista végén LEVÁGVA alatt szerepelnek. Webes forrásom nem volt, ezért H5P-, Moodle- és jogi tényt nem állítok. Ahol ilyen tényen múlik valami, kutatási hiányként jelölöm.

Rövidítések:
- KAPU-M2 = `02 Tervezet/Modulok/M2/M2 – Kapu – értékelő (item-bank + rubrika).md`
- KAPU-M3 = `02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md`
- KAPU-M6 = `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md`
- M2.4, M3.3, M3.4, M3.B, M4.B, M6.2 = a megfelelő lecke- vagy peulafájl a `02 Tervezet/Modulok/` alatt
- HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`
- MAN = `02 Tervezet/LMS – activity manifest.md`
- GK = `02 Tervezet/Gyermekvédelem – release gate.md`
- CSOMAG = `01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`

---

### M3:QA14-BIZT-2 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - KAPU-M3:318: „Ahol a leírt helyzetben nincs feltárás vagy titoktartási ígéret, az R2-t nem büntető módon alkalmazzuk: a titoktartás említésének hiánya ilyenkor nem 0, hanem legalább Alapszint (1); a titoktartás megígérése viszont mindig 0.”
  - KAPU-M3:325, az R2 0-s cellája: „vagy – feltárást vagy titoktartási ígéretet tartalmazó helyzetben – a titoktartás kérdését meg sem említi”. Ugyanitt az Alapszint cella: „ahol a leírt helyzetben nincs feltárás vagy titoktartási ígéret, a titoktartás említésének hiánya is Alapszint”.
  - KAPU-M3:326, R3 Alapszint: „Megnevezi, hogy a leírt madrih **azonnal a kijelölt Memunát vonja be**”.
  - A tükörmondat a tanulói szövegben is áll: M3.4:837 és M3.B:513, mindkettőben „ha a helyzetben feltárás vagy titoktartási ígéret szerepel”.
- **Lezárt döntés / kánon:**
  - ERT-21 (HUM:691): „R2-t az olyan helyzetekben, ahol nincs feltárás vagy titoktartási ígéret, ne büntető mechanikával alkalmazzuk. A rubrika ne buktassa meg a saját sablonját követő résztvevőt; kalibráció Memuna + értékelési felelős.” A döntés nem mondja meg, hogy a hanih kérése „titoktartási ígéret”-nek számít-e.
  - A kánon központi helyzetként tanítja a kérést. M3.3:187: „Ha egy hanih azt kéri, hogy **senkinek ne mondd tovább** … megígérheted a 100%-os titoktartást” (hamis állítás). M3.3:177: „Megígéred, hogy **senkinek** nem mondod el?”
  - A sablon maga is kérdez a titoktartásra. M3.4:832: „mit NEM ígérne és mit NEM tenne (pl. teljes titoktartás, nyomozás, konfrontáció)”. Aki a sablont követi, az tehát említi a titoktartást.
  - A kétlépcsős küszöb: GYV-7 (HUM:630) és GYV-8 (HUM:631: „Pusztán hiányzó felnőtt felügyelet operatív ügyét a képző/programvezető rendezi, akut kockázatnál Memuna is”).
  - Biztosíték: KAPU-M3:317: „A kapu csak akkor élesedhet, ha a kalibráció és a kétszemes döntési rend rögzítve van.” A SIG-2 (HUM:759) nyitott bizonyíték-kapu.
- **Kutatás:** nem kell; a kérdés belső kalibráció. A KAPU-M3 §4 forráslistája (NSPCC, Safeguarding Network) a „ne ígérj teljes titoktartást” elvet támasztja alá, a rubrikahatárt nem.
- **Javaslat:** EMBERI DÖNTÉS. Kalibrál: Memuna + értékelési felelős. A rubrikaszintről a projektgazda dönt.
  - **(1) Lefedi-e a „titoktartási ígéret” a hanih titoktartás-kérését?**
    - (a) Igen, a kérés is beletartozik. Ekkor a feltételnek önálló tartalma van; ha a madrih maga ígér, az az első tagmondat miatt amúgy is 0. A kérés az M3.3 tanított esete, és a sablont követő tanulót nem buktatja, mert az 5. kérdés titoktartást kérdez.
    - (b) Nem, csak az elhangzott ígéret. Ekkor egy „ne mondd el senkinek” helyzetben a blokkoló R2 nem buktat akkor sem, ha a leírás a titoktartást meg sem említi.
    - **Ajánlás: (a).** Jóváhagyás után az öt hely együtt változik (KAPU-M3:318, :325 két cellája, M3.4:837, M3.B:513): „feltárás vagy titoktartási ígéret” → „feltárás, titoktartás-kérés vagy titoktartási ígéret” (a ragozott alakokban is).
  - **(2) Mi az R3 Alapszintje határhelyzetben?**
    - (a) Marad: Alapszinten mindig a Memuna bevonása áll. A túleszkaláció nem veszélyes, és a sablon az „ötlépéses jelzési út”-ra utal.
    - (b) Alapszint: a helyzet típusának megfelelő felnőtt. Gyanúnál a Memuna, pusztán operatív, nem veszélyeztető határhelyzetnél a képző vagy a programvezető (GYV-8), akut kockázatnál a Memuna is.
    - (c) Mindkettő elfogadott Alapszinten.
    - **Ajánlás: (c).** Nem bünteti sem a Memunához forduló, sem a GYV-8 szerint helyes operatív címzettet megnevező tanulót.
  - **Átmeneti szöveg:** változatlan. Az óvatos értékelői olvasat a széles (a kérés beletartozik). A szöveg a döntésig maradhat, mert a kalibráció nélkül a kapu nem élesedhet (KAPU-M3:317).
- **Vétó-érintettség:** rubrikaszint, blokkoló R2, gyermekvédelmi megfogalmazás, látható tanulói szöveg (pinelés kell). A pontsáv, a „minden sor ≥1” szabály és az R4 nem változik.

### M2:QA14-BIZT-5 — MÁR RENDBEN
- **Mostani állapot:**
  - KAPU-M2:24: „A mentor a kapueredményt legkésőbb 24 órával a következő fix alkalom előtt megerősíti. … „Teljesítve” = … tényleges, minimálisan értelmezhető tartalom”. Ez kapuértékelési megerősítés, nem gyermekvédelmi átolvasás.
  - KAPU-M2:203: „Ha egy valós gyermekvédelmi helyzetet jelezned kell, azt ne ebben a jegyzetben tedd: azonnal vond be a Memunát”.
  - MAN:57 (LMS-M2-09): „kötelező, határidős mentori átnézés nincs”.
- **Lezárt döntés / kánon:**
  - A 24 órás határidő önálló, lezárt döntés: HUM:201–203 („Lezárva: 2026-10-02”, „Jóváhagyta: projektgazda”) és HUM:220: „A kapu eredményét legkésőbb 24 órával a következő fix alkalom előtt meg kell erősíteni.” Ez programszintű, minden kapura szól (M1–M7 KAPU).
  - A GYV-1 kérdése (CSOMAG:211) két külön dolgot választ szét: „Kötelező-e (és milyen határidővel) az M2 tárolt szabad szöveges válaszainak mentori átolvasása …, és maradhat-e … „a mentorod azonnal bevonja a Memunát” ígérete **a KAPU:24 megerősítési határideje mellett**?” A „határidős átnézés” tehát az (a) opció biztonsági célú átolvasása (CSOMAG:213), nem a KAPU:24.
  - A GYV-1 „egyébként” ága (külön akut jelzési út) teljesül: KAPU-M2:203.
- **Kutatás:** nem kell.
- **Javaslat:** nincs szerkesztés. A verifierrel szemben nem tartom nyitott hatóköri kérdésnek. Ha a projektgazda mégis tágan olvasná a GYV-1-et, az a HUM:220 lezárt döntését írná felül csak az M2-ben (projektgazdai újranyitás, vétólistás időtartam/completion). Ez nem következik a GYV-1 szövegéből. Ami nyitott: a GYV-1 Memuna- és DPO-QA-ja, ez bizonyíték-kapu (G1/G2).
- **Vétó-érintettség:** nincs, mert nincs változás.

### M2:QA14-BIZT-4 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - M2.4:663: „ilyenkor a mezőbe írd be, hogy „passz”, és egy mondatban azt, kit vonnál be azonnal egy ilyen üzenetnél. Ez is teljes értékű válasz.”
  - M2.4:655 (3️⃣): „**Kit vonnál be azonnal** … és mit nem kezdenél el (pl. nyomozás, konfrontáció, diagnózis, teljes titoktartás ígérete)?”
  - M2.4:649: „Ez **fiktív eset**”.
  - MAN:57: completion = „beküldve” (a SLIDE 5-nél „a „passz” egy mondattal teljes értékű válasz; … a terjedelmet a Moodle nem ellenőrzi”). A mező nem kapu.
- **Lezárt döntés / kánon:** GYV-2 (HUM:625): „a passzhoz ekvivalens tudásdemonstráció járjon, ne automatikus kapuátengedés. M2.4 kötelező mezője így biztosan módosítandó”. Ez megtörtént. Az egyenértékűség tartalmát a döntés nem rögzíti. Párhuzam: a SAFE-1 (HUM:566–567) az M3.3-ban tudásdemonstráció nélküli, completion-semleges passzt enged, de csak ott.
- **Kutatás:** nem kell.
- **Javaslat:** EMBERI DÖNTÉS. Kérdés: mi számít egyenértékűnek az M2.4 SLIDE 5 passz-útján? Dönt: Memuna + programvezető (HUM-SAFE-03). A HUM-sor a kapus belépőnél az értékelési felelőst is megnevezi, de az M2.4 nem kapus belépő.
  - (a) Marad az egy mondat a bevonandó személyről. A mező nem kapu; az üzenet magja: „a Memuna bevonása nem feltételes” (M2.4:657). A titoktartás tilalmát az M3 éles kapuja méri elsajátításig (R2 blokkoló, 2. és 8. item).
  - (b) A passz-mondat kiegészül a 3️⃣ saját szavával: „…kit vonnál be azonnal egy ilyen üzenetnél, és mit nem kezdenél el.” Mindkét biztonsági felet lefedi, és nem kér személyes tartalmat.
  - (c) A „teljes értékű válasz” minősítés elhagyása, új tartalom nélkül.
  - **Ajánlás: (b).** Ez a legkisebb lépés a „ekvivalens” szó felé, és a passz továbbra is valódi marad. A javítás együtt mozog a MAN:57-tel és a hub két passz-sorával (a QA szerint HUB:183, :190; ezeket nem ellenőriztem).
  - **Átmeneti szöveg:** a mostani maradhat. Nem automatikus átengedés (a mező „Required”, biztonsági mondatot kér), és a feladat nem kapu.
- **Vétó-érintettség:** gyermekvédelmi megfogalmazás, látható szöveg. A „Required” besorolás és a completion-lánc nem változik.

### M6:QA14-BIZT-3 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - KAPU-M6:328: „Tudod, hogy a kvucában nemrég valakit tényleg kicsúfoltak.”
  - KAPU-M6:331: „A) „Láttál-e már olyat, hogy egy beszólás miatt valaki kívül érezte magát? (Nem kell nevet mondani.)” ✅”
  - KAPU-M6:338 („főleg friss seb mellett”) és :343 („megengedi a saját élményt”) együtt mozog az itemmel.
  - A lecke diaszövegét már átvezették. M6.2:606: „opcionálisan: „Milyen hasonló helyzet volt már nálatok? (Nem kell nevet mondani, és bárki indoklás nélkül passzolhat.)””
  - A narráció még a régi: M6.2:631–632, a `M6.2-NAR-05-VO` blokkban: „‘Milyen hasonló helyzet volt már nálatok? / Nem kell nevet mondani.’”
- **Lezárt döntés / kánon:**
  - GYV-18 (HUM:641): „fiktív, szereplőközpontú kérdés és biztonságos válasz legyen; a „nálatok” önfeltáró kérdés opcionális és passzolható. A megváltozott disztraktor/✅ szöveg értékelési felelős + Memuna jóváhagyását igényli.” A kulcsról a projektgazda dönt.
  - ERT-36 (HUM:706): „azonos gondolkodási elvet más, fiktív helyzeten kérjen számon, ne szó szerinti leckememóriát … biztonsági veto megtartandó.”
- **Kutatás:** nem kell.
- **Javaslat:** EMBERI DÖNTÉS. Kérdés: mi a 12. item új szára, ✅-ja és disztraktora? Dönt: értékelési felelős + Memuna; a kulcsról a projektgazda.
  - (a) Új fiktív helyzet (nem a Lili-történet), a „friss seb” mondat nélkül. A ✅ szereplőközpontú; a disztraktorok ugyanazt a három hibatípust hordozzák (megnevezés/szégyenítés, álkérdés, áldozathibáztatás).
  - (b) A Lili-keret marad, csak a „friss seb” mondat törlődik, és a ✅ szereplőközpontú lesz. Ez ütközik az ERT-36-tal, mert a lecke ✅-ja (M6.2:655) szó szerint ugyanez lenne.
  - (c) A mostani ✅ marad, passz-formulával kiegészítve. Ez nem teljesíti a GYV-18 „szereplőközpontú” előírását.
  - **Ajánlás: (a).** Illusztratív tervezet a jóváhagyóknak, nem implementálandó: szár „Elmesélsz egy kitalált történetet egy hanihról, akit a csapatválasztásnál mindig utolsónak hívnak…”; ✅ „Szerinted mit érezhetett ő, és mit tehetett volna a csapat?”; disztraktorok: „Ki szokott nálatok utolsó maradni? Mondjuk ki!”, „Ugye mindannyian egyetértünk, hogy mi ilyet sosem csinálunk?”, „Szerintetek nem csinált ebből túl nagy ügyet?”. A :338 és a :343 vele együtt változik.
  - **Narráció:** ez nem döntés, mert a GYV-18 erről már döntött. VO-fix pack kérés a médiafelelősnek, az M6.2:606 diaszövegével mint forrással. A `@source` blokk a lecke-kódban nem változik.
  - **Átmeneti szöveg:** az item és a kulcs változatlan. Ez nem az óvatos alapértelmezés, de a ✅ jóváhagyás nélkül nem érinthető. Az M6 learner release a G1 nélkül amúgy is zárt, ezért a next-version ágon maradhat.
- **Vétó-érintettség:** kulcs (projektgazda), disztraktor, kapu-item, látható szöveg, VO.

### M3:IMPL-G2-5 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - A passz-választók: M3.3:58, :63, :67, :70. Mindegyiken csak ez áll: „Mit szeretnél tenni ezzel a helyzettel?”.
  - Az INSTR-12 nem nevezi meg a témát. M3.3:431–432: „Most két rövid helyzetet fogsz látni. / Minden ponton válassz egy lehetőséget…”
  - Meglévő címek: M3.3:434 „1. szitu: késő esti privát üzenet”, :530 „3. szitu: vágásnyomok, „vicces” magyarázattal”, :559 „4. szitu: madrih–hanih kapcsolat (párkapcsolat-gyanú)”.
- **Lezárt döntés / kánon:**
  - §7.1 (HUM:567): „Minden S1–S4 szcenárió előtt ugyanaz a pass-choice csomópont: kérdés „Mit szeretnél tenni ezzel a helyzettel?” … egyik opció sem preferált”. A címről nem rendelkezik.
  - GYV-2 (HUM:625): „M3/M4-es kör Memuna- és completion-QA”. A sor jobb oldala: „az M3.3 §7.1: projektgazda (build-spec gazda), QA: Memuna”.
  - A CSOMAG:223 ajánlása („a passzjog tájékozott választást feltételez, a cím meglévő szöveg … QA: a cím maga ne legyen megterhelő”) a kérdés háttere, nem a döntés szövege.
- **Kutatás:** KUTATÁSI HIÁNY. A H5P Branching Scenario `showContentTitle` működését a finding a semantics.json-ból idézi („the user will see the content title in the top bar above this content”), de ezt nem ellenőriztem. Azt sem, hogy a csomópont saját címe jelenik-e meg, vagy a következő tartalomé. Stagingben kell igazolni (RT).
- **Javaslat:** EMBERI DÖNTÉS. Kérdés: megjelenjen-e a szcenárió meglévő címe a P1–P4 csomóponton? Dönt: projektgazda (build-spec); QA: Memuna.
  - (a) A meglévő cím megjelenik, új szöveg nélkül.
  - (b) Status quo: a passz vakon történik.
  - (c) Téma-előjelzés az INSTR-12/34-ben. Ez új szöveg, gyermekvédelmi tartalom.
  - **Ajánlás: (a).** A tájékozott passz a HUM-SAFE-03 célja. A Memuna nézze meg, nem megterhelő-e maga a cím (például „vágásnyomok”).
  - **Átmeneti szöveg:** status quo. A passz és a biztonsági csomópontok megvannak, ezért elfogadható.
- **Vétó-érintettség:** build-spec (BSPEC-05). A §7.1 szövege, a completion és a pontozás nem változik.

### M3:PED-G2-1 — BIZONYÍTÉK-KAPU [ÖSSZEVONVA: M3:PED-G2-1, M4:BIZT-G2-10 — közös Memuna-verdikt]
- **Mostani állapot:**
  - M3.4:12: „a beágyazott kérdések kitöltését a CP nem kényszeríti ki … A SLIDE 4 besorolója … kötelező tanulási lépés; a kapus belépő ennek a leckének a completionje (LMS-M3-04).”
  - M3.4:63: „Mondhatsz passzt”.
  - MAN:65–66: az LMS-M3-05 unlockja az LMS-M3-04 („profil”).
- **Lezárt döntés / kánon:**
  - ERT-1 (HUM:671): „a CP completionje … az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését”. Ebből közvetlenül következik, hogy a SLIDE 4/6 passza nem zárja el a kapus belépőt. A completion-rész tehát a kánonból megválaszolt.
  - A SLIDE 4 és a SLIDE 6 harmadik személyű, önfeltárás nélküli elem, így a „teljesítés nem függhet önfeltárástól” (GYV-2) teljesül.
  - A GYV-2 az M3/M4-re csak „Memuna- és completion-QA”-t ír elő, szövegváltozást nem.
- **Kutatás:** nem kell.
- **Javaslat:** nincs szerkesztés. Két dolog hiányzik:
  1. Memuna-verdikt arról, hogy az M3.4 SLIDE 4 és 6 érzékeny gyakorlat-e. Kérdés az is, hogy a „kötelező tanulási lépés” címke engedjen-e a passznak (az M3.3-ban a SAFE-1 így döntött). Ez a G1-hez tartozik (GYV-24, HUM:754).
  2. A megválaszolatlan interakció negatív tesztje (runtime acceptance 9. pont): RT, LMS-gazda.

  Ha a Memuna alternatív feladatot kér, az új tartalom: a tétel újranyílik (REOPENED).
- **Vétó-érintettség:** nincs, mert nincs változás.

### M4:BIZT-G2-10 — BIZONYÍTÉK-KAPU [ÖSSZEVONVA: M3:PED-G2-1, M4:BIZT-G2-10]
- **Mostani állapot:**
  - M4.B:63, a képzői felkészülésben: „A szereplési szorongás önmagában nem gyermekvédelmi krízis, de bárki bármikor megállhat és passzolhat.” A ledger szerint ez a dd64825 commitban került be.
  - A körökben a passz nincs kimondva: M4.B:120, :124–135, :199–203, :323–324. Csak a zárókörben van kimondva, M4.B:326: „Ha valaki nem szeretne megszólalni, mondhatja azt is, hogy **passzol** – ez is rendben van.”
- **Lezárt döntés / kánon:** GYV-6 (HUM:629, `A`): „A szereplési szorongás nem automatikusan gyermekvédelmi krízis, de legyen szabad megállni és passzolni; a Memuna hagyja jóvá a küszöböt.” A feltétel nélküli rész az M4.B:63-ban teljesül, a finding kérésénél tágabban („bárki bármikor”). A GYV-2 az M4-re Memuna-QA-t ír elő.
- **Kutatás:** nem kell.
- **Javaslat:** a Memuna küszöb-jóváhagyása (GYV-6) és az M4-es GYV-2 QA a G1 bizonyítéka. Ha a Memuna körönkénti bejelentést kér, kész a szerkesztés: a :326 mondata szó szerint a 4.1, a 4.2 (3. lépés) és a 4.4/1 instrukciójába kerül. A körök, a mondattövek, az időkeretek és a 4.1 „Nem tudom, még keresem” kiútja nem változik (verifier-korlát).
- **Vétó-érintettség:** nincs. Offline peula, completion nincs.

---

| Kulcs | Besorolás | Egysoros indok |
|---|---|---|
| M3:QA14-BIZT-2 | EMBERI DÖNTÉS | Az ERT-21 kalibrációja (a kérés lefedettsége; az R3 Alapszintje határhelyzetben); ajánlás: (1)(a), (2)(c); a kapu kalibráció nélkül nem élesedhet (KAPU-M3:317) |
| M2:QA14-BIZT-5 | MÁR RENDBEN | A 24 órás megerősítés a HUM:220 lezárt döntése; a GYV-1 kérdése (CSOMAG:211) a biztonsági átolvasástól külön kezeli; az akut út megvan (KAPU-M2:203) |
| M2:QA14-BIZT-4 | EMBERI DÖNTÉS | Az egyenértékű passz tartalma (Memuna + programvezető); ajánlás: „…és mit nem kezdenél el”; átmenetileg maradhat |
| M6:QA14-BIZT-3 | EMBERI DÖNTÉS | Új 12. item (értékelési felelős + Memuna; kulcs: projektgazda); ajánlás: új fiktív helyzet az ERT-36 szerint; a narráció VO-fix pack (már eldöntött) |
| M3:IMPL-G2-5 | EMBERI DÖNTÉS | Cím a passz-választón (projektgazda, build-spec; QA: Memuna); a `showContentTitle` működését stagingben kell igazolni |
| M3:PED-G2-1 | BIZONYÍTÉK-KAPU | A completion-rész az ERT-1-ből megválaszolt; az érzékenységről a Memuna G1-verdiktje és az RA 9. pont negatív tesztje kell |
| M4:BIZT-G2-10 | BIZONYÍTÉK-KAPU | A GYV-6 alapja az M4.B:63-ban teljesül; hiányzik a Memuna küszöb-jóváhagyása (G1); a :326 mondata kész javítás, ha a Memuna kéri |

Összevonás: az M3:PED-G2-1 és az M4:BIZT-G2-10 egy Memuna-verdikttel zárható. Az M2:QA14-BIZT-4 jóváhagyói ugyanők (Memuna + programvezető), ezért egy ülésben kezelhetők.

LEVÁGVA: 2 tétel: M7:BIZT-G1-2, M7:PED-G2-4. Az M7 KAPU mostani szövegét nem olvastam be. Hiányzik az R4 2–3. szintje (a CSOMAG szerint KAPU:311–312), a (C) 5. sora (:386), a Q9 (:164, :171), az M7.4 mintatáblája (:769–778) és a MUNK-01 spec (:808) szó szerinti idézete. A CSOMAG:282–289 alapján a két tétel egy döntés (GYV-9), és valószínűleg EMBERI DÖNTÉS: a rubrikaszintről a projektgazda dönt, a rubrikahorgonyt és a Q9/(C) szabályt a Memuna és az értékelési felelős hagyja jóvá összehangoltan. Ezt a fájlban nem ellenőriztem.

## G4 – Tanulói adatok: láthatóság, megőrzés, önfeltárás, közös eszköz

## G4 – tanulói adatok: kutatás és döntési javaslat (read-only, HEAD 10b5d76)

**Forrásokról.** Az EUR-Lex (HU HTML, PDF és ELI) nem töltött be, ezért a GDPR szövegét **másodlagos forrásból** idézem: gdpr-info.eu, a hivatalos angol szöveg másolata. A magyar hivatalos szöveggel össze kell vetni. NAIH-iránymutatást nem kerestem. A Moodle-tények elsődleges forrásból valók: `MOODLE_405_STABLE` forráskód (`raw.githubusercontent.com/moodle/moodle/...`) és docs.moodle.org (4.5).

---

### M0:QA14-BIZT-3 — EMBERI DÖNTÉS [ÖSSZEVONVA: M0:QA14-BIZT-3 + az ADV §3 nyitott BIZT-5-je, az ADV-1 kiterjedése a QUIZ profilra]
- **Mostani állapot:**
  - HUB `02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md:283`: „Egyéni mentoros utánkövetés csak indokolt pedagógiai cél, célhoz kötött válaszhozzáférés és DPO-jóváhagyás mellett lehet (projektgazdai döntés, 2026-10-12, GYV-23)”.
  - `Adatvédelem – tanulói adatok és AI.md:116` (QUIZ-D sor): „a kvízriportot és az értékelést (`mod/quiz:viewreports`, `mod/quiz:grade`): nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5)”.
  - ADV:109: „A nem beadás jellegű profilok (H5P-C, QUIZ) és a GATE-CP csoport szerinti szűkítése nincs rögzítve … a döntés kiterjedéséről a projektgazda dönt … (BIZT-5)”.
- **Lezárt döntés / kánon:**
  - Részben válaszol rá, teljesen nem.
  - HUM:132 (HUM-PRIV-01): „Mindenhez a legszűkebb szükséges hozzáférés: zárt kvíz pontszáma – az értékelő”.
  - ADV §11:247: „A kvízek és a kapuk eredményét az értékelőd látja.”
  - GYV-23 (HUM:646): „célhoz kötött válaszhozzáférés és DPO-jóváhagyás”.
  - Nincs rögzítve, hogy ki az M0 diagnosztikus kvíz „értékelője”, és hogy a mentor (nem szerkesztő tanár) alapból lássa-e a tételszintű válaszokat. Ez az ADV:109 szerint nyitott projektgazdai kérdés.
- **Kutatás:**
  - `mod/quiz/db/access.php` (4.5): `'mod/quiz:viewreports'` → `'riskbitmask' => RISK_PERSONAL … 'archetypes' => ['teacher' => CAP_ALLOW, 'editingteacher' => CAP_ALLOW, 'manager' => CAP_ALLOW]`.
  - docs.moodle.org/405/en/Quiz_responses_report: „The quiz responses report allows the teacher to see a table of answers for a quiz, with a row for each student.”
  - `quiz/statistics:view` (`mod/quiz/report/statistics/db/access.php`): `'clonepermissionsfrom' => 'mod/quiz:viewreports'`, vagyis külön capability. Hogy a statisztika a Responses report nélkül is elérhető-e, azt stagingben kell kipróbálni; nem állítom.
  - `mod/quiz/report/responses/report.php` csoportot kezel: „This option is only available to users who can access all groups in groups mode”.
  - GDPR 25. cikk (2) (másodlagos): „by default, only personal data which are necessary for each specific purpose of the processing are processed. That obligation applies to … their accessibility.”
- **Javaslat:**
  - **Kérdés:** a belépőkvízen (QUIZ-D) ki láthatja alapból a tételszintű egyéni válaszokat (Responses report), és ezt szerepbeállítással kell-e kikényszeríteni?
  - **Ki dönt:** a projektgazda (az ADV-1 kiterjedése, BIZT-5), DPO-val. A beállítást az LMS-gazda rögzíti és stagingben visszaolvassa (RT-P0-15, ADV-E1).
  - **Opciók:**
    - (a) Moodle-alapérték, csoportmód „Separate groups”. A mentor csak a saját csoportját látja, a GYV-23-at eljárási szabály védi. Ez technikailag nem „célhoz kötött” hozzáférés.
    - (b) Activity-szintű role override: a QUIZ-D-n a nem szerkesztő tanártól elvonjuk a `mod/quiz:viewreports`-t. A csoportszintű korrekcióhoz a privacy felelős által kijelölt szerep összesítést lát. Egyéni utánkövetéshez a DPO-jóváhagyás után dokumentált, ideiglenes override jár.
    - (c) Csak összesítés mindenkinek: a statisztikai riport igen, a Responses report senkinek. A megvalósíthatósága runtime-kérdés.
  - **Ajánlás:** a (b). Ez a GYV-23 „célhoz kötött válaszhozzáférés” szövegét és a GDPR 25. cikk (2) alapértelmezését technikailag is teljesíti. A (c) csak akkor jöhet szóba, ha a staging bizonyítja, hogy a két riport szétválasztható.
  - **Addig:** a HUB:283 és az ADV:116 szövege marad. Ez szövegszinten az óvatos alapértelmezés, beállításként viszont nem az. Repóból javítható szöveg nincs.
- **Vétó-érintettség:** adatvédelmi hozzáférés. Kulcs, küszöb és completion nem érintett.

### M0:QA14-NYELV-3 — EMBERI DÖNTÉS
- **Mostani állapot:** HUB:283: „első körben csoportszintű, nem megbélyegző korrekció és a két item nyilvános visszajelzése jár.” A döntés szövege, HUM:646: „a biztonsági 1–2. item nyilvános visszajelzését ajánlom”.
- **Lezárt döntés / kánon:**
  - Sem a döntés, sem a döntési csomag nem magyarázza. A csomag GYV-23 opciói (`…döntési csomag….md:411`): „(b) csak csoportszintű megerősítés az M0.A-n, összesítés alapján; (c) marad a kvíz saját visszajelzése”.
  - A döntés a (b)-t és egy „nyilvános visszajelzést” kombinál, a jelentését viszont nem mondja ki.
  - A HUB-ban a „két item” a mondat elején álló „1–2. (biztonsági) item”-re mutat vissza, ez nem hiba.
- **Kutatás:** külső tényen nem múlik.
- **Javaslat:**
  - **Kérdés:** a „nyilvános visszajelzés” tartalomszintű-e (a két item helyes válasza és magyarázata mindenkinek), vagy személyhez kötött, csoport előtti visszajelzés?
  - **Ki dönt:** programvezető + Memuna. Az adatkörről a DPO.
  - **Opciók:**
    - (1) A két item helyes válaszát és magyarázatát név és eredmény nélkül mindenki megkapja, szóban az M0.A-n vagy kurzusüzenetben. Adatvédelmileg semleges.
    - (2) A kvíz review-beállítása a beküldés után minden résztvevőnek megmutatja a két item helyes válaszát és általános visszajelzését (build-spec, runtime-teszt).
    - (3) Személyhez kötött, csoport előtti visszajelzés. Ütközik a „nem megbélyegző” kikötéssel, és egyéni eredményt tesz közzé.
  - **Ajánlás:** az (1), szükség esetén a (2)-vel együtt. Csak ez fér össze egyszerre a „csoportszintű, nem megbélyegző” korrekcióval és a célhoz kötött hozzáféréssel.
  - **Addig:** marad a szó szerinti átvezetés, és köztes átírás sincs (a verifier szerint). Ez nem kifejezetten óvatos, de kitalált magyarázatot sem tartalmaz.
- **Vétó-érintettség:** gyermekvédelmi és adatvédelmi megfogalmazás. Kulcs nem érintett.

### M0:QA14-BIZT-4 — EMBERI DÖNTÉS (hatókör-megerősítés)
- **Mostani állapot:**
  - `M0.A – Kickoff & ismerkedés + közös keret.md:604`: „**Tartalék eszköz (közös eszköz-protokoll, ADV-11):** rajta jelszót menteni és személyes munkapéldányt hagyni tilos; használat után jelentkeztesd ki a résztvevőt …”.
  - M0.A:612: „Az M0-ban **szándékoltan csak ez az egy peula (M0.A) van** – … sem felzárkóztató peula (F-peula).”
- **Lezárt döntés / kánon:**
  - A döntés szövege általános, HUM:657: „Egységes közös eszköz-protokoll …”. A csomag kérdése viszont csak az F-peulákról szólt (`…döntési csomag….md:541`: „Közös vagy tartalék eszköz kezelése az F-peulákon”).
  - Az általános olvasat mellett szól a javaslat „Lényeges eltérések” 5. pontja (`…Döntési javaslat….md:307`): „**ADV-11:** közös eszközön inkább adatmentes működés az alap”. HUM:614: ahol a javaslat eltér a csomagtól, „a javaslat érvényes”.
  - Az `LMS – hozzáférhetőségi sztenderd.md:57` is F-peula-szűkítés nélkül vezeti át („a közös eszközön mindenki…”, „Egységes közös eszköz-protokoll (projektgazdai döntés, 2026-10-12 … ADV-11)”).
  - Ez erős támasz, de a verifier új alkalmazási esetnek minősítette (nem F-peula, technikai segítségpont), ezért nem zárom le.
- **Kutatás:** nem szükséges.
- **Javaslat:**
  - **Kérdés:** az ADV-11 a nem F-peulás tartalék eszközre (M0.A technikai segítségpont) is vonatkozik-e?
  - **Ki dönt:** projektgazda (a döntés hatóköre). Vétó/QA: LMS-gazda + DPO.
  - **Opciók:** (a) igen, minden közös vagy tartalék eszközre (a javaslat 5. pontja és az A11Y:57 olvasata); (b) csak az F-peulákra, akkor a #26 visszaáll; (c) M0-ra külön szabály.
  - **Ajánlás:** az (a). A döntés szövege nem szűkít, a javaslat kifejezetten általános, és a tartalék laptop maradványadat-kockázata ugyanaz.
  - **Addig:** az M0.A:604 marad. Ez a szigorúbb, óvatos alapértelmezés.
- **Vétó-érintettség:** adatvédelmi kikötés (csak szigorítás). Completion nem érintett.

### M1:QA14-BIZT-5 — EMBERI DÖNTÉS [ÖSSZEVONVA a GYV-11 csomagba: M1:QA14-BIZT-5, KANON:QA14-BIZT-4, Z:QA14-BIZT-1, Z:BIZT-G1-2]
- **Mostani állapot:**
  - `M1 – Kapu – értékelő (item-bank + rubrika).md:27`: „… A kapueredmény nem függhet a feltárástól: a tanuló biztonságos, feltárásmentes pótlási utat kap. Bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan. |”. A „szükség szerinti korlátozás” hiányzik.
  - ADV §5:153 viszont teljes: „… a Memuna-eljárást, a szükség szerinti korlátozást vagy helyesbítést és az adatvédelmileg jóváhagyott törlést vagy megőrzést dokumentálni kell (projektgazdai döntés, 2026-10-12, GYV-11).”
- **Lezárt döntés / kánon:**
  - A GYV-11 (HUM:634, `F`) a követelményt rögzíti, az eljárást nem.
  - A csomag (`:304`): „A kivétel módjáról, a megőrzésről és törlésről, valamint a kapueredményről ajánlás nincs”.
- **Kutatás (GDPR, másodlagos forrás):**
  - 18. cikk (1) c): „the controller no longer needs the personal data …, but they are required by the data subject for the establishment, exercise or defence of legal claims”.
  - 18. cikk (2): „Where processing has been restricted …, such personal data shall, with the exception of storage, only be processed with the data subject's consent or for … legal claims or for the protection of the rights of another natural … person …”.
  - 17. cikk (3) e): törlés nem jár, ha az adat „for the establishment, exercise or defence of legal claims” szükséges.
  - (38) preambulumbekezdés: „Children merit specific protection with regard to their personal data”.
- **Javaslat:**
  - **Kérdés:**
    - a) ki és hogyan korlátozza vagy veszi ki a feltárást tartalmazó beadást a Moodle-ből;
    - b) mi a törlés és a megőrzés rendje;
    - c) mi a feltárásmentes pótlás mechanikája (M1-ben a javító próbálkozás az F-peula után nyílik);
    - d) beszámít-e a feltárást tartalmazó próbálkozás.
  - **Ki dönt:** Memuna + DPO (a, b); értékelési felelős (c, d).
  - **Opciók (a, b):**
    - (1) A Memuna vagy a helyettese az incidensnyilvántartásba menti a szükséges tartalmat (GK:85–86). A Moodle-példányt egy kijelölt jogosult korlátozza: rejtés, az értékelői hozzáférés elvonása. A végleges törlés kézi, jogi megőrzési felülvizsgálat után.
    - (2) A Moodle-példány a normál megőrzési sor szerint marad, megjelölve.
    - (3) Az átmentés után azonnali kézi törlés.
  - **Opciók (c, d):** (i) kézzel nyitott, külön próbálkozás, amely nem számít bele a keretbe (a Z.4:359 mintája: „ha kell, a képző kézzel nyit hozzá próbálkozást”); (ii) a próbálkozás beszámít.
  - **Ajánlás:** az (1) és az (i). A megőrzés helye a már szabályozott incidensnyilvántartás (ADV §3:73: „jogi visszatartás esetén tovább”). Így az LMS nem elsődleges nyilvántartás, és nincs automatikus törlés. A tanulót a feltárás nem bünteti.
  - **Addig:** a KAPU:27 marad, és nem kerül bele kitalált eljárás.
  - **Külön LEZÁRHATÓ alpont (szó szerinti átvezetés, mert a tárolt kapubeadvány a GYV-11 közvetlen hatóköre):**
    - Fájl: `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:27`
    - OLD: `Bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan. |`
    - NEW: `Bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan; a Memuna-eljárást, a szükség szerinti korlátozást vagy helyesbítést és az adatvédelmileg jóváhagyott törlést vagy megőrzést dokumentálni kell (projektgazdai döntés, 2026-10-12, GYV-11). |`
    - Ez az ADV §5:153 kánoni mondata szó szerint, eljárás nélkül. Az M3 KAPU:309 és az M3.4:835 párhuzamos helyét nem olvastam vissza: alkalmazás előtt ellenőrizni kell, hogy megvan-e bennük a korlátozás.
- **Vétó-érintettség:** gyermekvédelmi és adatvédelmi megfogalmazás (csak bővítés). A pótlás és a beszámítás próbálkozási, completion-kérdés, ezért értékelési felelős dönt róla.

### Z:QA14-BIZT-1 — EMBERI DÖNTÉS [ÖSSZEVONVA: Z:BIZT-G1-2; a GYV-11 csomag része]
- **Mostani állapot:**
  - `Z.4 – Záró reflexió + képzési visszajelzés.md:401` (Feedback, Megőrzés): „… és ezt a választ jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük; a korlátozáshoz, a helyesbítéshez és a törlési vagy megőrzési döntéshez dokumentált, jogosult Memuna-eljárás és adatvédelmileg jóváhagyott rend kell (projektgazdai döntés, 2026-10-12, GYV-11).”
  - Z.4:370: „A válaszok név nélkül jelennek meg a feldolgozásban. Ha veszélyről van szó, azt ne csak ebbe az űrlapba írd: azonnal vond be a Memunát.”
- **Lezárt döntés / kánon:**
  - A GYV-11 a „tárolt beadandó”-ról szól (HUM:634), a Feedbackről nem.
  - Ütközés: ADV §3:70 „Z visszajelzés nyers válaszai | jogos érdek | 90 nap, utána csak összesítve”, illetve HUM-PRIV-03 (HUM:174).
  - Kánoni, nem törölhető rész: GK:85 (dokumentáció az incidensnyilvántartásban), GK §4.1 (Memuna).
- **Kutatás:**
  - Feedback FAQ (docs.moodle.org/405): „the username of the user who took the Feedback is still recorded in the database just as with non-anonymous Feedbacks, but the name is not show to anyone on screen.”
  - Viewing Feedback responses: „Individual responses may be Deleted if required.”
  - `mod/feedback/db/access.php`: `mod/feedback:deletesubmissions` → editingteacher, manager.
  - A GDPR 17. cikk (3) e) és 18. cikke, mint fent.
- **Javaslat:**
  - **Kérdés:**
    - (a) kiterjed-e a GYV-11 megőrzési kivétele a Feedback nyers válaszaira, és hogyan módosul az ADV §3:70;
    - (b) szabad-e, és ki által, az adatbázisban tárolt felhasználónévvel visszakeresni a válaszadót;
    - (c) kell-e a :370-be a :201 mintájára tájékoztató mondat.
  - **Ki dönt:** Memuna + DPO. A (b)-nél a jogi felelős is.
  - **Opciók (a):**
    - (1) Igen: a feltárást tartalmazó válasz a 90 napos összesítés alól kivétel, korlátozva.
    - (2) Nem: a Memuna az incidensnyilvántartásba menti, a Moodle-válasz a 90 napos sor szerint megy. Ilyenkor a :401 GYV-11-tagmondata kikerül.
    - (3) Átmentés után kézi törlés a Moodle-ből (a `deletesubmissions`-szerep, dokumentáltan).
  - **Ajánlás (a):** a (2) vagy a (3). A megőrzés helye az incidensnyilvántartás (ADV §3:73), így az ADV §3:70 változatlan maradhat.
  - **Opciók (b):** tiltott; csak súlyos veszélynél, a Memuna kérésére, megnevezett adminisztrátor, dokumentáltan.
  - **Ajánlás (b):** a második, de ez jogi minősítés. A HUM-PRIV-03 tanulói ígérete („név nélkül jelennek meg”) a megjelenítésről szól. Ha a visszakeresés megengedett, a tájékoztató ezt nem tagadhatja (az ADV-1 mintája).
  - **Addig:** a :401 szövege marad, egyik irányba sem írandó át (a verifier szerint). Gyermekvédelmi szempontból a megőrzés felé óvatos, a tárolás korlátozása felé nem.
- **Vétó-érintettség:** gyermekvédelmi és adatvédelmi megfogalmazás, megőrzés. A HUM-PRIV-03 kanonikus mondata nem változhat.

### KANON:QA14-BIZT-4 — EMBERI DÖNTÉS [ÖSSZEVONVA a GYV-11 csomagba]
- **Mostani állapot:** ADV §5:153: „Ha a feltárásban különleges adat jelenik meg, az kikerül a Moodle-ből, és az incidensfolyamatba kerül (§3). … bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan …”. Ugyanez a §11:243-ban és az ADV:75-ben.
- **Lezárt döntés / kánon:**
  - Két lezárt döntés áll egymás mellett. A HUM-PRIV-01 (HUM:133) a különleges adatról: „kikerül a Moodle-ből”. A GYV-11 a tárolt beadandóba került gyermekvédelmi feltárásról.
  - Egyik sem rögzíti a sorrendet és a hatáskört. Az illesztés értelmezés, nem szó szerinti átvezetés.
- **Kutatás:** a GDPR 18. cikk (2) szerint korlátozott adattal a tároláson kívül csak szűk célból lehet műveletet végezni. Ez a „kikerül” korlátozásként vagy átmentés utáni törlésként is olvasható.
- **Javaslat:**
  - **Kérdés:** a „kikerül a Moodle-ből” jelentése: (1) az incidensnyilvántartásba mentés utáni korlátozás; (2) az átmentés utáni, jogi felülvizsgálathoz kötött kézi törlés; (3) azonnali törlés.
  - **Ki dönt:** Memuna + DPO.
  - **Ajánlás:** az (1), amely a felülvizsgálat után a (2)-be fordul. Ez mindkét lezárt mondatot teljesíti: kikerül az elsődleges használatból, és nincs automatikus törlés. A (3) ütközik a GYV-11-gyel.
  - **Addig:** nincs szövegváltozás és nincs sorrendi szabály.
- **Vétó-érintettség:** gyermekvédelmi és adatvédelmi kanonikus mondat (nem törölhető).

### M4:QA14-BIZT-5 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - `M4.A – Állj oda! – Kiállás & jelenlét a térben.md:381`: „Írd rá ugyanezt az egy mondatot, név nélkül. Ha szeretnéd, tedd a közös ‘M4 – kiállás’ borítékba / falra … El is viheted magaddal emlékeztetőnek.”
  - M4.A:382: „A név nélkül bent hagyott kártyák kezelése: `Adatvédelem…` §3, „Név nélkül begyűjtött papír munkalap” sor.”
  - `M4.B…md:332–333` ugyanez a minta (a sorszám a riport óta nem változott).
- **Lezárt döntés / kánon:**
  - ADV-7 (HUM:653): „személyes önfeltáró cetli a résztvevőnél marad vagy hozzá visszakerül; névvel nem függesztjük ki és nem gyűjtjük”.
  - Hogy a fókuszkártya önfeltáró-e, azt a döntés nem mondja meg.
  - A csomag elfogadott (a) opciója (`:508`) megkülönböztet: „az önfeltáró cetli és kártya a madrihnál marad …; a név nélküli lapokra az ADV §3:67 vonatkozik”.
  - ADV-8 (HUM:654): „Visszaazonosítható kis csoportos produktumot ne minősítsünk anonimnak” (kézírás).
- **Kutatás:** külső tényen nem múlik.
- **Javaslat:**
  - **Kérdés:** az M4.A és M4.B fókuszmondat-kártyája személyes, önfeltáró cetli-e?
  - **Ki dönt:** DPO / jogi felelős, Memuna-QA-val.
  - **Opciók:** (a) nem önfeltáró, a mostani szöveg marad; (b) önfeltáró, a boríték- és faliopció kikerül; (c) a kártya csak a résztvevőnél marad, a képző szóban összesít (az ADV-8 elsődleges útja).
  - **Ajánlás:** az (a). A mondat szakmai fejlődési szándék („amire legközelebb figyelni szeretnék, amikor a kvucám előtt állok”), nem az ADV §2:29 érzékeny kategóriája. Az elhelyezés önkéntes és név nélküli, a szöveg nem nevezi anonimnak.
  - **Addig:** a szöveg marad (a verifier szerint). Ez nem a legóvatosabb változat, az a (b) lenne.
- **Vétó-érintettség:** adatvédelmi kikötés.

### Z:QA14-BIZT-3 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - `Z.A – Mit viszek magammal – Záró kvuca-peula.md:40`: „Szükséges csoportproduktumról (például a „Híd a terepre” poszterről vagy a szófelhőről) csak előre rögzített céllal … készülhet fotó”.
  - Z.A:41: „a személyes, önfeltáró cetli a résztvevőnél marad … (a szófelhő cetlijére nem kerül név, 4.4.2)”.
  - Z.A:464: „írj rá **1 szót** … Lehet érzés, érték, gyakorlat … Nevet ne írj rá.”
  - Z.A:467: a cetlik a közös felületre kerülnek. Hogy utána mi lesz velük, azt a szöveg nem mondja meg.
- **Lezárt döntés / kánon:**
  - ADV-7 (HUM:653).
  - HUM-PRIV-02 (HUM:151): „A kézírásos plakátot lehetőleg fizikailag őrizzük meg.”
  - ADV §3:67 (név nélküli papír: 30 napon belül megsemmisítés).
  - Egyik sem sorolja be a szófelhő-cetlit.
- **Javaslat:**
  - **Kérdés:** az egyszavas szófelhő-cetli csoportproduktum vagy személyes, önfeltáró cetli, és mi a sorsa a peula után?
  - **Ki dönt:** DPO / jogi felelős.
  - **Opciók:** (a) csoportproduktum, fizikai megőrzés a HUM-PRIV-02 szerint, a megőrzési időt a DPO adja meg; (b) csoportproduktum, a peula után a résztvevők elvihetik a szavukat, vagy az ADV §3:67 szerint megsemmisül; (c) önfeltáró, a résztvevőhöz kerül vissza, a felhőről nincs fotó.
  - **Ajánlás:** a (b). A Z.A:40 már csoportproduktumnak tekinti, és így nem keletkezik megőrzési idő nélküli papír.
  - **Addig:** a szöveg marad. A „nincs fotó”, a HUM-PRIV-02-feltétel, a „Nevet ne írj rá” és a saját telefonra vonatkozó tilalom nem gyengülhet.
- **Vétó-érintettség:** adatvédelmi kikötés.

### M2:QA14-BIZT-7 — EMBERI DÖNTÉS
- **Mostani állapot:**
  - `M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md:177`: „„Amit itt hallunk, az **nem kerül ki** névvel a teremből – kivéve, ha valaki veszélyben van: ilyenkor azonnal bevonjuk a Memunát.””
  - M2.A:409–410: „Lehet egy felismerés, egy közös minta, akár valami nehézség is. Senki más történetét ne vigyétek ki névvel.”
  - A minta ma a `M2.B…md:370` sorban áll (nem a :368-ban): „Ne írj nevet (elég a szerep), és olyan részletet se, amelyből felismerhető, kiről van szó.”
- **Lezárt döntés / kánon:**
  - GYV-21 (HUM:644): „A „név nélkül” nem egyenlő anonim jelleggel egy kis kvucában. Gyermekvédelmi és érzékeny példából csak fiktív, illetve ténylegesen nem visszaazonosítható, általánosított változatot kérjünk szóban is.”
  - A „kérjünk” arra vonatkozik, amit a képző kér. A :410 plenáris kérés („akár valami nehézség is”) ehhez közel áll. A :177 csoportos titoktartási norma viszont új alkalmazási eset.
- **Javaslat:**
  - **Kérdés:** kerüljön-e a :177-be és a :410-be „és felismerhető részlettel sem”?
  - **Ki dönt:** Memuna + DPO.
  - **Opciók:** (a) mindkét helyre; (b) csak a :410-be (képzői kérés, a GYV-21 hatóköréhez legközelebb); (c) marad.
  - **Ajánlás:** az (a). Ugyanaz a modul (M2.B:370) már ezt a mércét használja, és a GYV-21 első mondata kifejezetten a kis kvuca visszaazonosíthatóságára figyelmeztet.
  - **Addig:** a :177 és a :410 marad, a Memuna-kivétel érintetlen.
- **Vétó-érintettség:** gyermekvédelmi és adatvédelmi megfogalmazás (csak szigorítás).

### Z:BIZT-G1-2 — EMBERI DÖNTÉS [ÖSSZEVONVA: Z:QA14-BIZT-1]
- **Mostani állapot:**
  - Az objektív alpont kész (`.obj`, 5fcf2b0).
  - A Z.4:359 (Assignment) az óvatos alapértelmezést tartalmazza („feltárásmentes változatot adhat be; ha kell, a képző kézzel nyit hozzá próbálkozást”).
  - Nyitott a Feedback-ág (:370, :401), lásd Z:QA14-BIZT-1.
  - Mellékmegfigyelés, nem ebben a csoportban: a Z.4:201 „a beadást látó mentornak vagy értékelőnek azonnal be kell vonnia” garancia-jellegű. A GYV-1 mintája ilyet tiltott az M2-ben. Érdemes a GYV-1 gazdájával egyeztetni.
- **Lezárt döntés / kánon, kutatás, javaslat:** mint a Z:QA14-BIZT-1-nél. Egy Memuna + DPO döntés (a)–(c) zárja; a pótlási útról az értékelési felelős dönt.
- **Vétó-érintettség:** gyermekvédelmi és adatvédelmi megfogalmazás.

### M3:BIZT-G1-5 — BIZONYÍTÉK-KAPU (utána DPO + Memuna technikaválasztás)
- **Mostani állapot:**
  - `M3.3 – Gyermekvédelem 101…md:96`: „„Enable attempt tracking” = Yes”. A P1–P4 passz-választók: :58, :63, :67, :70.
  - Az M3 hub §7 (`M3 – Kvuca, red flag, felelősség…md:264–276`) csak összesített kérdéseket tesz fel („mely red flag típusokat **nem ismerik fel**”, „átlag **<80%**”, „>30%-a”).
- **Lezárt döntés / kánon:**
  - ADV-4 (HUM:650): „M3 SAFE-1 ágnál a konkrét H5P verzió, próbálkozás-riport, xAPI/LRS, mentett állapot és szerepkörök visszaolvasása után dönthető el a tárolásmentes technika.” A sorrendet a döntés maga adja, ezért ami hiányzik, az a runtime-bizonyíték.
  - A hub §7 alkérdésére az ADV §11:245 lezárt tanulói mondata válaszol: „A program fejlesztéséhez csak összesített, beazonosíthatatlan adatot használunk.” A §7 szövege ezt már követi, ez az alpont rendben van.
- **Javaslat:**
  - **G3b runtime:** az LMS-gazda visszaolvassa az RT-2 sort (HUM:765: „H5P saved-state, xAPI/LRS és jogosultsági visszaolvasás a célverzión”), a runtime acceptance 15. pontját és az ADV-E1-et (HUM:755).
  - Utána a DPO + Memuna választ technikát. A SAFE-1 csomópontjai nem változnak.
- **Vétó-érintettség:** adatvédelem. A completion és a SAFE-1 szerkezete nem érintett.

### M3:BIZT-G2-7 — BIZONYÍTÉK-KAPU
- **Mostani állapot:**
  - `M3.4 – Do és Don’t madrihként…md:191`: „🔥 „Nagyon, ez most nagyon aktuális nekem.””
  - A spec, M3.4:95: „Érzelmi önjelzés (ADV-4): nem pontozott, nem completion-elem, és lehetőleg nem rögzül a követett próbálkozásban; hogy rögzül-e, azt a célverzión … vissza kell olvasni”.
- **Lezárt döntés / kánon:** ADV-4 (HUM:650). Az óvatos alapértelmezés a specben megvan.
- **Javaslat:** G3b runtime-visszaolvasás (LMS-gazda: RT-2, 15. pont), utána a DPO dönt a technikáról, a mutatóról a Memuna. A kérdés nem törölhető, és nem köthető completionhöz.
- **Vétó-érintettség:** adatvédelem.

### M3:BIZT-G2-5 — BIZONYÍTÉK-KAPU
- **Mostani állapot:**
  - M3.4:67: „a kijelölt értékelőd elolvassa; egy második vagy fellebbezési értékelő csak konkrét eljárásnál láthatja …, a Memuna pedig csak szükség esetén; technikai okból a Moodle rendszergazdája is hozzáférhet.”
  - Ugyanez a M3.4:33 specben.
  - A kánon átvezetve: ADV §5:148 és §11:247.
  - ADV-10: M3.4:801 „.docx; Google Doc csak szervezeti fiókkal, adatfeldolgozói és hozzáférési felülvizsgálat után (ADV-10)”.
- **Lezárt döntés / kánon:** ADV-2 (HUM:648): „Az F-peula szereposztást és a vészhozzáférést dokumentálni kell; csoport-hozzáférés ténylegesen tesztelendő.”
- **Javaslat (szöveg kész, hiányzó bizonyítékok):**
  - a csoport-hozzáférés stagingtesztje (LMS-gazda, RT-P0-15, runtime acceptance:86);
  - az F-peula szereposztásának és a vészhozzáférésnek a dokumentálása (programvezető);
  - a Memuna szerepének megerősítése (Memuna);
  - DPO G2 (ADV-E1, ADV-E2: HUM:755–756);
  - a szervezeti Google-fiók megléte (programvezető, ténykérdés).
- **Vétó-érintettség:** nincs új. A kétszemes rend és a „valós eset névtelenítve sem” érintetlen.

### M3:BIZT-G3-8 — BIZONYÍTÉK-KAPU
- **Mostani állapot:**
  - `M3.F…md:3`: „a képző a kapueredményekből csak összesített vagy minimális hiánylistát lát … az F-peula szereposztását és a vészhozzáférést dokumentálni kell (ADV-2).”
  - M3.F:184: „a képző a peula előtt **privát módon** nézze át az F-peulához kapott összesített vagy minimális hiánylistát”.
- **Lezárt döntés / kánon:** ADV-2 (HUM:648). A szöveg a döntést teljesíti.
- **Javaslat:** a programvezető írásos szereposztás- és vészhozzáférés-dokumentációja (ADV-E2, G2), és az LMS-gazda hozzáférési tesztje (RT-P0-15).
- **Vétó-érintettség:** nincs.

---

## Összesítő

| Kulcs | Besorolás | Indok |
|---|---|---|
| M0:QA14-BIZT-3 | EMBERI DÖNTÉS (+BIZT-5) | A QUIZ-D tételszintű hozzáférése nincs rögzítve; a Moodle-alapérték szerint a nem szerkesztő tanár látja (RISK_PERSONAL). Ajánlás: activity-szintű override, DPO-jóváhagyott, célhoz kötött hozzáférés. |
| M0:QA14-NYELV-3 | EMBERI DÖNTÉS | A „nyilvános visszajelzés” jelentése nem dönthető el. Ajánlás: tartalomszintű, név és eredmény nélküli visszajelzés. |
| M0:QA14-BIZT-4 | EMBERI DÖNTÉS | Az ADV-11 hatóköre a nem F-peulás eszközre. Erős támasz: javaslat :307, HUM:614, A11Y:57. Az M0.A:604 a szigorúbb alap. |
| M1:QA14-BIZT-5 | EMBERI DÖNTÉS (+ LEZÁRHATÓ alpont) | Az eljárás, a pótlás és a beszámítás szerepköri döntés; a KAPU:27-be szó szerint átvezethető az ADV §5:153 korlátozási mondata. |
| Z:QA14-BIZT-1 | EMBERI DÖNTÉS | A GYV-11 Feedback-ágra alkalmazása ütközik az ADV §3:70-nel; a visszakeresés és a tájékoztatás nyitott. |
| KANON:QA14-BIZT-4 | EMBERI DÖNTÉS | A HUM-PRIV-01 „kikerül” és a GYV-11 sorrendje. Ajánlás: átmentés, korlátozás, jogi felülvizsgálat, kézi törlés. |
| M4:QA14-BIZT-5 | EMBERI DÖNTÉS | A fókuszkártya besorolása; ajánlás: nem önfeltáró (csomag (a) opció, ADV §3:67). |
| Z:QA14-BIZT-3 | EMBERI DÖNTÉS | A szófelhő-cetli csoportproduktum; a sorsa a peula után nincs rögzítve. |
| M2:QA14-BIZT-7 | EMBERI DÖNTÉS | A GYV-21 új alkalmazási esete; ajánlás: „és felismerhető részlettel sem” (M2.B:370 mintája). |
| Z:BIZT-G1-2 | EMBERI DÖNTÉS (= Z:QA14-BIZT-1) | Egy Memuna + DPO döntés zárja. |
| M3:BIZT-G1-5 | BIZONYÍTÉK-KAPU | Az ADV-4 a runtime-visszaolvasáshoz köti (G3b, RT-2); a hub §7 alpontja rendben (ADV §11:245). |
| M3:BIZT-G2-7 | BIZONYÍTÉK-KAPU | A spec kész (M3.4:95); a runtime-visszaolvasás hiányzik. |
| M3:BIZT-G2-5 | BIZONYÍTÉK-KAPU | A szöveg kész; hiányzik a dokumentálás (programvezető), a teszt (RT-P0-15), a Memuna- és a DPO-bizonyíték (ADV-E1/E2). |
| M3:BIZT-G3-8 | BIZONYÍTÉK-KAPU | A szöveg kész; a szereposztás és a vészhozzáférés dokumentálása hiányzik. |

**Egyetlen döntéssel zárható összevonás:** GYV-11 csomag = M1:QA14-BIZT-5, KANON:QA14-BIZT-4, Z:QA14-BIZT-1, Z:BIZT-G1-2. Egy Memuna + DPO ülés dönt a korlátozásról, a törlés és megőrzés rendjéről, a Feedback-ágról és a visszakeresésről; az értékelési felelős külön a pótlásról és a beszámításról.

**Ami nincs ellenőrizve:**
- Az M3 KAPU:309 és az M3.4:835 GYV-11-sorát nem olvastam vissza: hiányzik-e belőlük is a „korlátozás”.
- Nem ellenőriztem, hogy a kvízstatisztika a Responses report nélkül elérhető-e (runtime-kérdés).
- A GDPR-t csak másodlagos forrásból idéztem, és NAIH-forrást nem néztem.

Mindegyik tételt végigvittem, levágott tétel nincs.

## G5 – Hozzáférési modell, AI-út, fórum

## G5: hozzáférési modell, AI-út, fórum (read-only; HEAD 10b5d76)

A kért formában adom le, azzal, amit eddig ellenőriztem. Fájlt nem módosítottam.

**A legfontosabb**
- Az ADV-1 kiterjedése továbbra is a projektgazda döntése. Moodle 4.5 alatt mindhárom érintett profilnál műszakilag megoldható a csoportszűkítés.
- Új kockázat az Assignment értékelői nézetében: a csoportba nem sorolt mentor minden beadást láthat. Ez a TEXT-C BIZT-3 párja, ezért runtime-tesztlépést javaslok rá.
- Négy tétel zárható a lezárt döntésekből: két AI-szöveg és két M7-es ADV-5-maradvány. A KANON:QA14-BIZT-3b (b) részénél eltérek a korábbi verifier-verdikttől (indok lent).

### KANON:QA14-BIZT-1 — EMBERI DÖNTÉS [ÖSSZEVONVA: a hozzáférési részük: M1:BIZT-G2-4, M2:BIZT-G2-3, M2:BIZT-G1-6]
- **Mostani állapot:** az átmeneti szöveg a három helyen már bent van.
  - `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:109`: „A nem beadás jellegű profilok (H5P-C, QUIZ) és a GATE-CP csoport szerinti szűkítése nincs rögzítve: … a döntés kiterjedéséről a projektgazda dönt, utólagos ellenőrzés (vétó/QA): a DPO / jogi felelős (BIZT-5).”
  - Ugyanitt `:104`: „nyitott: az ADV-1 kiterjedése, BIZT-5”; `:232`: „a nem beadás jellegű profilok szűkítése nyitott: az ADV-1 kiterjedése (BIZT-5)”.
  - Maradvány: a `:115` (H5P-C sor) cellája még ez: „nincs rögzítve: DPO-kérdés (BIZT-5)”. Ugyanaz a pontatlanság, amelyet a verifier a :109-nél kijavíttatott.
- **Lezárt döntés / kánon:**
  - A HUM `:647` (ADV-1) szó szerint csak ennyit mond: „mentor csak saját csoportjának lássa a beadást”.
  - A döntési csomag ADV-1 kérdése (`01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md:452`) mind a négy profilt felsorolja: „ASSIGN-S/M, GATE-CP, H5P-C, QUIZ”. A választott (c) opció (`:454`) így szól: „a mentorokat csoport szerint szűkítik”.
  - A GATE-CP a manifest szerint „Moodle Assignment beadási típus nélkül … a tanuló semmit nem tud beadni” (`LMS – activity manifest.md:25`). Szó szerint tehát nem „beadás”.
  - Az ADV-1 hatóköre ezért a kánonból nem dönthető el.
- **Kutatás (TÉNY, a moodle/moodle `MOODLE_405_STABLE` forrása):**
  - **H5P (`mod/h5pactivity/classes/local/manager.php`, `get_active_users_join()`):** „if ($currentgroup === 0 && $coursemodule->effectivegroupmode == SEPARATEGROUPS && !has_capability('moodle/site:accessallgroups', $context)) { return new sql_join('', '1=2', [], true); }”. Egyéni riportnál a `get_report()` ezt hívja: „if (!groups_user_groups_visible($course, $user->id, $this->coursemodule)) { return null; }”.
    - A korábbi hibát (MDL-80501, „H5P attempts report did not respect activity group settings”) a 4.3.3/4.2.6/4.1.9 javította. Ezt csak a moodle.org keresési összefoglalójából látom, a bejelentés oldala 403-at adott (másodlagos forrás).
  - **Kvíz (`mod/quiz/classes/local/reports/report_base.php`, `get_current_group()`):** „if ($groupmode == SEPARATEGROUPS && !$currentgroup && !has_capability('moodle/site:accessallgroups', $context)) { $currentgroup = self::NO_GROUPS_ALLOWED; }”.
  - **Assignment / GATE-CP (`mod/assign/gradingtable.php`):** a táblázat ezt hívja: „$currentgroup = groups_get_activity_group(…, true); … list_participants($currentgroup, true)”.
    - A `lib/grouplib.php` `_group_verify_activegroup()` megjegyzése: „this happen when user not assigned into group in SEPARATEGROUPS mode … mod authors must add extra checks for this when SEPARATEGROUPS mode used”. Ilyenkor az aktív csoport 0.
    - A `list_participants()`-ben ilyen extra ellenőrzést nem találtam: 0-s csoporttal a `get_enrolled_sql` szűrés nélkül fut.
    - Következtetés, óvatosan: a csoport nélküli mentor az Assignment értékelői nézetében minden beadást láthat. Ezt runtime-ban kell eldönteni.
  - **Capability-oldal (docs.moodle.org/405, moodle/site:accessallgroups):** a szerkesztő tanári szerepnél ez a jog alapból engedélyezett, a nem szerkesztő tanárinál nem.
- **Javaslat:**
  - *Kérdés:* kiterjed-e az ADV-1 (c) csoportszűkítése a H5P-C, a QUIZ-D/M és a GATE-CP mentori nézetére?
  - *Ki dönt:* a projektgazda; vétó/QA: a DPO / jogi felelős; a szerepkiosztást az LMS-gazda rögzíti.
  - *Opciók:*
    - (A) Mindhárom profilra kiterjed, „Separate groups” csoportmóddal. A HUM-PRIV-01 „legszűkebb szükséges hozzáférés” elvéhez ez illik, a csomag (c) opciója sem szűkít profilra, és a fenti kód szerint core-ban megvalósítható.
    - (B) Csak az ASSIGN-S/M-re, ahogy a döntés betűje szól. Ilyenkor a „Ki látja?” szövegnek ki kell mondania, hogy a kvíz- és a H5P-eredményt minden tanári szerep látja.
    - (C) A P2-t rögzítő H5P-C-re és a QUIZ-ra igen, a GATE-CP-re nem, mert az P1 kapueredmény. Hátránya: a kétszemes rend miatt a második képzőnek amúgy is csoporton kívüli hozzáférés kell.
  - *Ajánlás:* az (A), csoport nélküli mentorral mint negatív tesztesettel.
  - *Addig:* a mostani „nincs rögzítve / nyitott” szöveg marad. Ez az óvatos alapértelmezés, mert nem ígér szűkítést.
  - *Különálló LEZÁRHATÓ javítás (a verifier saját következmény-szabálya szerint):*
    - Fájl: `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:115`
    - OLD: `nincs rögzítve: DPO-kérdés (BIZT-5)`
    - NEW: `nincs rögzítve; nyitott: az ADV-1 kiterjedése (BIZT-5)`
- **Vétó-érintettség:** adatvédelmi megfogalmazás. Szigorít, nem gyengít; a „nincs rögzítve” cella marad.

### M1:BIZT-G2-4, M2:BIZT-G2-3, M2:BIZT-G1-6 (hozzáférési rész) — BIZONYÍTÉK-KAPU [ÖSSZEVONVA]
- **Mostani állapot:** a döntés feltétel nélküli része, hogy a tájékoztató nem tagadja a rendszergazda hozzáférését, már bent van.
  - `M1.4 …:510`: „…technikai okból a Moodle rendszergazdája is hozzáférhet.”
  - `M2.2 …:499`: ugyanez.
  - `M2 – Kapu …:203`: „A beadásodat csak a kijelölt mentorod vagy értékelőd látja és értékeli; technikai okból a Moodle rendszergazdája is hozzáférhet.”
- **Lezárt döntés:** ADV-1: „A „csak mentorod látja” ígéretet a tényleges RBAC-hoz kell igazítani a staging role-matrix után.”
- **Mi hiányzik:**
  - A staging role-matrix (LMS-gazda), a G2 POST-BUILD kapu: ADV §9 `:212` „mentor/képző hozzáférések tesztfiókkal ellenőrizve”, RT-P0-15.
  - Utána igazodik a szerkesztő tanárt és a menedzsert is érintő tanulói szöveg.
- **LEZÁRHATÓ következmény (az ADV-1 eldöntött részének átvezetése a tesztbe):** az RT 15. pontja a csoportszűkítést ma csak a TEXT-C-re írja elő.
  - Fájl: `02 Tervezet/LMS – H5P runtime acceptance.md:86`. Az OLD egyediségét javítás előtt ellenőrizni kell.
  - OLD (a pont vége): `1. szakasz 2. pont).`
  - NEW: `1. szakasz 2. pont). Az ASSIGN-S és az ASSIGN-M beadásainál ugyanígy két mentorral és két elkülönített tanulói csoporttal kell visszaolvasni, hogy a mentor az értékelői nézetben csak a saját csoportja beadásait látja, és hogy csoportba nem sorolt mentorfiók sem lát más csoporthoz tartozó beadást (projektgazdai döntés, 2026-10-12, ADV-1; `Adatvédelem – tanulói adatok és AI.md` §3).`
  - Indok: az ADV `:104` szerint „a csoportmód beállítását stagingben vissza kell olvasni”. A negatív esetet a fenti grouplib-tény indokolja. Új szabály nincs benne, csak a tesztlépés.
- **Vétó-érintettség:** nincs kulcs, küszöb vagy completion; adatvédelmi teszt.

### M2:BIZT-G1-6 (megőrzési sor és a „Név (vagy becenév)” mező) — EMBERI DÖNTÉS
- **Mostani állapot:** `M2 – Kapu …:214`: „Név (vagy becenév): ______”. Az LMS-M2-05-nek nincs saját §3-sora.
- **Lezárt döntés:** az ADV-1 ezt az alkérdést nem válaszolja meg (csomag `:453`). A HUM 14 az LMS-M2-05-öt csak a GYV-1-nél említi.
- **Javaslat:**
  - *Kérdés:* „Assignment / peulatervek” (+12 hónap) vagy „Szabad szöveges reflexió” (+90 nap) sor vonatkozik-e az identitás-jegyzetre? Kell-e a fájlba a név?
  - *Ki dönt:* a DPO / jogi felelős, az LMS-gazdával.
  - *Opciók:* (1) +90 nap, a Z.4 reflektív beadandó precedense szerint (ADV `:65`); (2) +12 hónap, Assignmentként; (3) a névmező törlése (a fiók már azonosít; ADV §2, adatminimalizálás).
  - *Ajánlás:* (1) + (3).
  - *Addig:* a fájl változatlan, megőrzési sort nem találgatunk (BS-D6-minta).

### KANON:QA14-BIZT-5 (ADV-12) — EMBERI DÖNTÉS
- **Mostani állapot:**
  - ADV `:183`: „csak a feltétlenül szükséges technikai metaadat marad, rövid, dokumentált megőrzéssel”.
  - A §3 tábla (`:60–73`) nem tartalmaz AI-sort. Az ADV `:58` szerint pedig „A jogalap és a megőrzés kanonikus helye ez a tábla”.
- **Kutatás (OpenAI, developers.openai.com/api/docs/guides/your-data):**
  - „By default, abuse monitoring logs are generated for all API feature usage and retained for up to 30 days, unless longer retention is required by law…”
  - „the Responses API has a 30 day Application State retention period by default, or when the `store` parameter is set to `true`.”
  - ZDR / Modified Abuse Monitoring: „subject to prior approval by OpenAI and acceptance of additional requirements.”
  - Következmény: `store=false` mellett a tartalom a szolgáltató visszaélés-naplójában akár 30 napig megmaradhat, hacsak nincs jóváhagyott ZDR. Ez alátámasztja az ADV-12 „store=false önmagában nem bizonyít” mondatát.
- **Javaslat:**
  - *Kérdés:* mi az AI-végpont technikai metaadatának jogalapja és megőrzési ideje? Hogyan kerül a „harmadik fél” mezőbe a szolgáltató 30 napos naplója?
  - *Ki dönt:* a DPO / jogi felelős (QA: programvezető).
  - *Opciók:*
    - (a) Jogos érdek (üzembiztonság), rövid megőrzés, például legfeljebb 30 nap, a szolgáltatói naplóhoz igazítva.
    - (b) Somer-oldalon nincs naplózás, csak a szolgáltatói napló marad, harmadik félként dokumentálva.
    - (c) Inaktív marad a csatornafelmérésig.
  - *Ajánlás:* (c) most, utána (a), DPO-rögzítette időtartammal, és ZDR-kérelemmel.
  - *Óvatos átmeneti javítás (LEZÁRHATÓ):* a BS-D6-minta szerint új pont a „Külön review” listában, időtartam nélkül.
    - Fájl: `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:86`
    - OLD: `saját kvuca hiányában a tanuló kitalált profilt kap;`
    - NEW: `saját kvuca hiányában a tanuló kitalált profilt kap;` + új sor: `- az AI-végpont technikai metaadata: a tartalom naplózása alapból kikapcsolva, csak a feltétlenül szükséges technikai metaadat, rövid, dokumentált megőrzéssel (projektgazdai döntés, 2026-10-12, ADV-12; §7); a jogalap és a megőrzési idő nincs rögzítve: nyitott (ADV-12), a repository nem dönti el;`
- **Vétó-érintettség:** adatvédelmi megfogalmazás. Időtartamot nem ír be.

### KANON:QA14-BIZT-3b — (a) MÁR RENDBEN; (b) LEZÁRHATÓ [GYV-10/LMS-8 a specben: MÁR RENDBEN]
- **(a) állapot:** ADV `:247`: „Az F-peula képzője a kapueredményekből csak összesített vagy minimális hiánylistát lát.” Megegyezik a §5 `:148` szövegével.
- **GYV-10/LMS-8 a specben már bent van:**
  - ADV §7 `:183`;
  - RA 20. pont `:102`: „…közvetlen tanulói AI-hozzáférés nincs, csak a képző által közvetített út (ADV-12, GYV-10, LMS-8)”;
  - manifest `:120`.
- **(b) állapot:** ADV `:264`: „Saját AI-fiókra nincs szükség: a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj.” A közvetített utat nem mondja ki, az „ide se írj” pedig közvetlen tanulói használatot sugall, ami a GYV-10 alatt ki van kapcsolva.
- **Kánon (b):**
  - A lezárt formula az M7 tanulói szövegében: `M7.4 …:82`, `M7.2 …:69, :115`: „Az AI-segédet egyelőre a képző kezeli: ha AI-ötletet kérnél, a promptot ő küldi el.”
  - Az M7 célzott QA verifiere (`2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)…:95`) ezt „a lezárt GYV-10 / LMS-8 formula”-ként erősítette meg.
  - A korábbi „(b) emberi” verdikt idején ez a validált formula még nem szerepelt érvként.
- **Javaslat (b):**
  - Fájl: `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:264`
  - OLD: `közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj.` A `:194` is tartalmazza, ezért a teljes `:264` sort kell OLD-ként venni.
  - NEW: `… Személyes adatot ide se írj. Az AI-segédet egyelőre a képző kezeli: ha AI-ötletet kérnél, a promptot ő küldi el.`
  - Nem új szabály: szó szerinti átvezetés.
  - Ha a fő session verifiere nem fogadja el, EMBERI DÖNTÉS lesz belőle: programvezető + Moodle-adminisztrátor, vétó: DPO; addig a `:264` változatlan.
- **Vétó-érintettség:** tanulói AI- és adatvédelmi szöveg; látható szöveg, ezért pin kell. Az ADV §1 DPO-jóváhagyási feltétele változatlan.

### M0:QA14-ERT-1 (ADV-6) — EMBERI DÖNTÉS [a (b) rész feltétel-oldala MÁR RENDBEN]
- **Mostani állapot:**
  - HUB `M0 – Kickoff…:170`: „csak ha a fórum valódi tanulóknak megnyílt (ADV-6…); addig ez nem teljesítési feltétel.”
  - Manifest `:43`: „addig nem completion-feltétel”; `:158`, illetve `:168`: „(az LMS-M0-05 csak akkor, ha a fórum az ADV-6 feltételeivel valódi tanulóknak megnyílt)”.
  - A (b) részből tehát a „kimarad-e az LMS-M1-01-ből és a kurzusteljesítésből” kérdésre a zárt állapotban a kánon „igen”-t mond.
  - Nyitott: a zárt állapot mechanizmusa (nem készül el vagy rejtett) és a visszamenőleges hatás (a).
- **Kutatás (TÉNY):**
  - `availability/condition/completion/classes/condition.php` `is_available()`: a pillanatnyi completionből számol (a QA forrása).
  - `lang/en/completion.php` `err_settingslocked`: „One or more students have already completed a criterion so the settings have been locked. Unlocking the settings will delete user completion data and may cause confusion.”
  - Következmény: ha a kohorsz közben új kritérium kerül be, (1) az LMS-M1-01 feltételébe téve azonnal elveszi az M1.1-et azoktól, akiknek nincs posztjuk; (2) kurzus-kritériumként csak a teljesítési adatok törlésével adható hozzá.
- **Javaslat:**
  - *Kérdés:* futó kohorszban a fórum megnyitása módosíthatja-e az M0 completionjét és az LMS-M1-01 feloldását?
  - *Ki dönt:* a projektgazda (build-spec gazda) + LMS-gazda.
  - *Opciók:*
    - (1) Csak a megnyitás után induló kohorszban feltétel; futó kohorszban a fórum opcionális. Ez megőrzi az M0.4:570 ígéretét, és nem jár adattörléssel.
    - (2) Visszamenőleges, türelmi idővel. Hozzáférés-elvonás és adattörlés jár vele.
    - (3) A fórum véglegesen opcionális. Ez kötelező/opcionális-váltás, tehát projektgazdai döntés.
  - *Ajánlás:* (1), zárt állapotban pedig az activity ne készüljön el, vagy rejtett legyen úgy, hogy egyetlen feltétel sem hivatkozik rá.
  - *Addig:* a mostani szöveg az óvatos alapértelmezés. Saját időbeli szabályt nem írunk be.
- **Vétó-érintettség:** completion és kötelező/opcionális besorolás. Csak döntéssel változhat.

### M7:BIZT-G1-6 (ADV-5) — (a) LEZÁRHATÓ; (b) EMBERI DÖNTÉS; (c) BIZONYÍTÉK-KAPU
- **Mostani állapot:**
  - Az f6e9c6e már átvezette: `M7.1 …:526` („…de ezt nem kötelező itt leírnod: választhatsz semleges vagy kitalált értéket is, vagy kihagyhatod a megnevezését.”), `M7 – Kapu …:408` („…semleges vagy kitalált someres érték is elfogadott, pontlevonás nélkül”), valamint M7.4:310 és M7.B:457.
  - Kimaradt a finding saját „Hely” mezőjének `M7.1:236` sora: „A SMART célod **R eleme erre épüljön** – tehát egy *konkrét, általad megnevezett* someres értékre…”.
  - Kimaradt az `M7.4 …:487–488` is: „Kösd ide az **M2-ben kiemelt someres értékedet** … nem „bárki” peulája lesz, hanem a tiéd.*”.
  - A manifest `:95` (LMS-M7-10) és a `RELEASE-READINESS.md:25` (G2) az ADV-5-öt nem említi; a G2 csak az LMS-M2-07-et.
- **Lezárt döntés:** HUM `:651`: „Ne legyen kötelező azonosítható vallási önbesorolás; engedjünk semleges, fiktív vagy válasz nélküli egyenértékű utat pontlevonás nélkül. GDPR 9. cikk szerinti minősítés és kivétel csak jogi/DPO jóváhagyással.”
- **(a) LEZÁRHATÓ.** Szó szerinti átvezetés az M7.4:310 mondatából, mindkettő a @source-blokkon kívül van. A javítás előtt ellenőrizni kell, hogy az OLD egyedi.
  - `…/M7.1 – … .md:236`
    - OLD: `Így a célod tényleg a te iránytűdhöz kapcsolódik.`
    - NEW: `Így a célod tényleg a te iránytűdhöz kapcsolódik. Ha nem szeretnéd a sajátodat leírni, semleges vagy kitalált érték is jó.`
  - `…/M7.4 – … .md:488`
    - OLD: `peulája lesz, hanem a tiéd.*`
    - NEW: `peulája lesz, hanem a tiéd. Ha nem szeretnéd a sajátodat leírni, semleges vagy kitalált érték is jó.*`
  - `02 Tervezet/LMS – activity manifest.md:95`
    - OLD: `elég a korosztály.” (M7.1, SLIDE 7) |`
    - NEW: `elég a korosztály.” (M7.1, SLIDE 7); a SMART cél R elemében a saját someres érték megnevezése nem kötelező: semleges vagy kitalált érték is választható, vagy a megnevezés kihagyható (projektgazdai döntés, 2026-10-12, HUM 14. szakasz, ADV-5); nyitott: a GDPR 9. cikk szerinti minősítés és kivétel, csak jogi/DPO-jóváhagyással (`RELEASE-READINESS.md` G2) |`
  - `02 Tervezet/RELEASE-READINESS.md:25`
    - OLD: `(BIZT-R5; someres vonatkozásban a projektgazda)`
    - NEW: `(BIZT-R5; someres vonatkozásban a projektgazda), és ugyanez az LMS-M7-10 (M7.1 saját SMART cél) mezőjénél (ADV-5)`
  - Vétó: adatvédelmi; szigorít. Az R1 szintleírása nem változik. Látható szöveg, ezért pin kell.
- **(b) EMBERI DÖNTÉS.**
  - *Kérdés:* kiterjed-e a „válasz nélküli” út a v2 R1 2-es szintjére („Somer-értékhez kötve”, KAPU:279)?
  - *Ki dönt:* az értékelési felelős + a projektgazda (rubrikaszint), az ERT-43-mal egy menetben.
  - *Opciók:* (1) Az R1 marad: a semleges vagy kitalált someres érték teljesíti, és ezt a KAPU:408 már kimondja. (2) Az R1 2-es szintje kifejezetten elfogadja a megnevezés nélküli, a kvuca helyzetéhez kötött relevanciát is (az M7.1:229 „vagy a kvucátok helyzetéhez” mintájára). (3) Az értékkötés kikerül az R1-ből.
  - *Ajánlás:* az (1). Addig az R1 változatlan.
- **(c) BIZONYÍTÉK-KAPU:** a GDPR 9. cikk szerinti minősítés a DPO / jogi felelős írásos jóváhagyása (G2, FINAL_RELEASE_QA).

### Összesítő

| Kulcs | Besorolás | Indok |
|---|---|---|
| KANON:QA14-BIZT-1 | EMBERI DÖNTÉS (+ LEZÁRHATÓ :115) | az ADV-1 kiterjedése a kánonból nem dönthető el; mindhárom profilnál műszakilag szűkíthető; a :115 cella még „DPO-kérdés” |
| M1:BIZT-G2-4, M2:BIZT-G2-3, M2:BIZT-G1-6 (hozzáférés) | BIZONYÍTÉK-KAPU (+ LEZÁRHATÓ RT 15) | az óvatos tájékoztató-szöveg már bent van; a staging role-matrix hiányzik; az ASSIGN-S/M csoportteszt átvezethető, csoport nélküli mentorral |
| M2:BIZT-G1-6 (megőrzés, névmező) | EMBERI DÖNTÉS | az ADV-1 nem válaszolja meg; DPO |
| KANON:QA14-BIZT-5 | EMBERI DÖNTÉS (+ óvatos LEZÁRHATÓ pont) | jogalap és megőrzés DPO-kérdés; az OpenAI 30 napos visszaélés-naplója ZDR nélkül is megmarad |
| KANON:QA14-BIZT-3b | (a) MÁR RENDBEN; (b) LEZÁRHATÓ | a :247 kész; a :264-be a validált M7-es GYV-10/LMS-8 formula kerül |
| M0:QA14-ERT-1 | EMBERI DÖNTÉS | a visszamenőleges hatás és a zárt állapot mechanizmusa nyitott; Moodle-tény: kritérium-zárolás, pillanatnyi kiértékelés |
| M7:BIZT-G1-6 | (a) LEZÁRHATÓ; (b) EMBERI DÖNTÉS; (c) BIZONYÍTÉK-KAPU | M7.1:236, M7.4:488, MAN:95, RR:25 átvezetése; R1 „válasz nélküli”; GDPR 9. cikk |

**Ami hiányzik:**
- Az Assignment csoport nélküli mentoros viselkedését kódból csak részben vezettem le; nem kerestem extra ellenőrzést a `view.php`/`grading` útvonalán. Ezért marad runtime-tesztlépés.
- A moodle.org MSA-24-0003 bejelentését nem tudtam megnyitni (403); erre a pontra csak keresési összefoglalóm van.

Források:
- [moodle/moodle MOODLE_405_STABLE – mod/h5pactivity/classes/local/manager.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/h5pactivity/classes/local/manager.php)
- [moodle/moodle MOODLE_405_STABLE – mod/quiz/classes/local/reports/report_base.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/classes/local/reports/report_base.php)
- [moodle/moodle MOODLE_405_STABLE – mod/assign/gradingtable.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/assign/gradingtable.php)
- [moodle/moodle MOODLE_405_STABLE – lib/grouplib.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/lib/grouplib.php)
- [moodle/moodle MOODLE_405_STABLE – lang/en/completion.php](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/lang/en/completion.php)
- [Moodle Docs 4.5 – moodle/site:accessallgroups](https://docs.moodle.org/405/en/Capabilities/moodle/site:accessallgroups)
- [Moodle Docs 4.5 – Groups](https://docs.moodle.org/405/en/Groups)
- [MSA-24-0003 (másodlagos, 403)](https://moodle.org/mod/forum/discuss.php?d=455636)
- [OpenAI – Data controls in the OpenAI platform](https://developers.openai.com/api/docs/guides/your-data)

## G6 – Értékelés és build-spec

## G6 — értékelés és build-spec: kutatás és döntési javaslat (read-only, HEAD 10b5d76)

Rövidítések (repó-relatív): MAN = `02 Tervezet/LMS – activity manifest.md`; RA = `02 Tervezet/LMS – H5P runtime acceptance.md`; HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`; M5 HUB/KAPU = `02 Tervezet/Modulok/M5/M5 – Ez most játék vagy tanulás – ….md` / `…/M5 – Kapu – értékelő (item-bank + rubrika).md`; M7 KAPU = `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md`; Z.3, Z.4 = `02 Tervezet/Modulok/Z/Online leckék/Z.3 – …md`, `…/Z.4 – Záró reflexió + képzési visszajelzés.md`; Z HUB = `02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md`; CSOMAG = `01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`.

---

### M5:QA14-ERT-1 (ERT-26) — EMBERI DÖNTÉS
- **Mostani állapot:** M5 HUB:35: „amelyben minden sorban látható a módszertani indok, és legalább egy sorban konkrét tanulástan-elem … is megjelenik”. M5 KAPU:286: „mind a 4 kritérium (rubrikasor) legalább **„Alapszint”**, a teljes táblázat alapján értékelve, nem táblázatcellánként”. A soronkénti indokról itt nincs szó. KAPU:294 R3: Alapszint „A módszer **megfelel** a célnak és a kvucának”, Erős „Az illeszkedés **indokolt is**: 1 mondatban kiderül, *miért*”. A tanulói oldalon M5.4:140: „A 4. mezőben mindig legyen 1 mondat arról, **hogyan segíti a tanulást** az adott módszer”.
- **Lezárt döntés / kánon:** HUM:696 ERT-26: „Soronként legyen látható módszertani indok, de egy tanulástani eszköz nem feltétlenül kell minden sorba. Értékelési kalibráció.” CSOMAG:963: „küszöb, szintek, az R4 kritikus státusza változatlan.” A döntés maga mondja ki, hogy ez kalibráció, de nem mondja meg, melyik rubrikaszintre esik. A HUB:35 a döntés szó szerinti átvezetése; a kérdés csak a KAPU-oldali leképezés.
- **Kutatás:** külső tényen nem múlik.
- **Javaslat:** Kérdés: a „soronként látható módszertani indok” az R3 Alapszintjén vagy csak az Erős szinten követelmény? Dönt: az értékelési felelős és a projektgazda; QA: a módszertani lektor.
  - (a) Kalibrációs mondat a KAPU:286 után, szintváltozás nélkül. Alapszinten az indok abból látszik, hogy a sorban a cél, a kvuca és a módszer illeszkedése felismerhető (vagy kiolvasható az M5.4:140 szerinti 4. mezőből). A kifejezett „miért”-mondat továbbra is az Erős szint.
  - (b) Átmenéshez minden sorba kifejezett indokmondat kell. Ez emeli a lécet, vagyis rubrikaváltozás, és ütközik a CSOMAG:963 következményével.
  - (c) Nincs kalibrációs mondat.
  - **Ajánlás: (a).** Megtartja a szinteket, a küszöböt és az R4 státuszát, és nem teremt rejtett bukási feltételt. Átmenetileg a fájl változatlan marad; ez az óvatos alapértelmezés.
- **Vétó-érintettség:** rubrikaszint-értelmezés. Szintleíróhoz, küszöbhöz, R4-hez nem nyúlunk.

### M7:QA14-ERT-1b (ERT-40) — LEZÁRHATÓ
- **Mostani állapot:**
  - A pontalapú maradványt már javították. M7 KAPU:48: „teljesen helyes válasz esetén a 12-es küszöbbe számít”; KAPU:217: „(teljesen helyes válasz esetén a 12-es küszöbbe számít, de nem kötelezően helyes)”. Ez a rész MÁR RENDBEN.
  - Nyitva maradt a :53: „addig a kvíz megerősítése (LMS-M7-09) előtt a képző kézzel ellenőrzi, hogy a két Multi-Select csak teljes ponttal számított-e.” A KAPU:50 szerint az értékelési mód „Highest grade”.
- **Lezárt döntés / kánon:**
  - HUM:710 ERT-40: „…egyébként manual GATE-CP megerősítés…”.
  - Kánoni build-szerződés, MAN:103 (LMS-M7-09): „„Teljesítve” = egy próbálkozásban **≥12/14 teljesen helyes item ÉS a Q13 helyes** … a „Highest grade” szerinti próbálkozásban a Q13 hibás is lehet: 19. pont”.
  - RA:96 (19. pont): „A konjunkciós kvízeknél (M3, M7) a „Highest grade” szerinti legmagasabb pontszámú próbálkozásban a kritikus item hibás is lehet, ezért ott a továbblépés a 8. pont szerinti megerősített eredményhez kötött.”
  - Hogy melyik próbálkozás számít, arra tehát a kánon már felel: bármely egyetlen próbálkozás, amelyben mindkét feltétel teljesül. A KAPU:53 ezt egyszerűen nem mondja ki.
- **Kutatás:** docs.moodle.org/405/en/Quiz_settings: „Highest grade - the final grade is the highest (best) grade in any attempt”. docs.moodle.org/405/en/Multiple_Choice_question_type: „Each answer may carry a positive or negative grade…”. A core tehát részpontot ad, így a legmagasabb nyers pontszámú próbálkozás eltérhet a darabszám szerint teljesítőtől (például 11 teljes + 2 részpont = 12,33 > 12 teljes = 12,0). A minden-vagy-semmi plugin ugyanott: „a respondent gets 100%” csak pontos egyezésnél.
- **Javaslat:** `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md`:53
  - OLD: `addig a kvíz megerősítése (LMS-M7-09) előtt a képző kézzel ellenőrzi, hogy a két Multi-Select csak teljes ponttal számított-e.`
  - NEW: `addig a kvíz megerősítése (LMS-M7-09) előtt a képző kézzel ellenőrzi, hogy a két Multi-Select csak teljes ponttal számított-e. A „Teljesítve” feltétele, hogy egy próbálkozásban legyen meg a legalább 12 teljesen helyes item ÉS a helyes Q13 (`LMS – activity manifest.md` LMS-M7-09); a „Highest grade” szerinti, részpontot is beszámító próbálkozás ettől eltérhet (runtime acceptance 19. pont).`
  - **Miért nem új szabály:** a MAN:103 és az RA 19 kánoni mondatát vezeti át szó szerint. Nem ír elő új lépést (például „azt a próbálkozást erősíti meg”), és nem nevez meg új szerepet.
  - Ami ezen túl van (hol és hogyan rögzíti a megerősítő a számolást), az az értékelési felelős külön döntése maradhat; ennél nem kell kevesebb.
- **Vétó-érintettség:** a completion-feltétel szövegét érinti (szó szerinti átvezetés), az értékét nem. Küszöb, kulcs, próbálkozásszám és Q13-szabály nem változik.

### Z:QA14-NYELV-1 (ERT-38, „Teljesítve” alsó határ) — EMBERI DÖNTÉS [ÖSSZEVONVA: Z:QA14-NYELV-1, Z:ERT-G1-1]
- **Mostani állapot:**
  - Z.4:343 (Completion rule): „ha a beadás előírt részeiben (a három szakaszban; a videós útnál a videóban mindhárom kérdésre kitérve) **tényleges, minimálisan értelmezhető tartalom** van”.
  - Z.4:347: „ha egy eleme hiányzik, de a beadás értelmezhető, akkor is „Teljesítve” jár”.
  - A tanulói szöveg, Z.4:98 és :329: „A „Teljesítve”-hez tényleges, értelmezhető beadás kell; a 3 kérdés szerinti részletes szerkezet (például a legalább 3 pillanat) útmutató, nem bukási feltétel”.
  - Z HUB:185: „tényleges, minimálisan értelmezhető beadás kell”.
  - MAN:112 (LMS-Z-08): „az LMS-Z-04 legutóbb leadott reflexiójának előírt mezőiben tényleges, minimálisan értelmezhető tartalom van”.
- **Lezárt döntés / kánon:** HUM:708 ERT-38: „a tartalom legyen minimálisan értelmezhető, tényleges beadás, de a három részes ideális reflektív szerkezet legyen formatív útmutató, ne új, rejtett bukási küszöb … a tanulói követelmény előre ismert.” HUM:457: „completion csak tényleges, minimálisan értelmezhető tartalommal”. A CSOMAG:1069 elfogadott (b) opciója az M2/M4 „előírt mezőkben” mintájára utal. A két olvasat egyike sem következik szó szerint.
- **Kutatás:** nem külső tény.
- **Javaslat:** Kérdés: a „Teljesítve” alsó határa (i) mindhárom szakaszban értelmezhető tartalom (érzékeny rész passzolható), vagy (ii) a beadás egészének értelmezhetősége? Dönt: az értékelési felelős; vétó/QA: a programvezető.
  - (i) A Completion rule és a MAN:112 marad. Átvehető a Z célzott QA-riport Z:QA-ERT-1 három OLD → NEW cseréje (:347, :353, valamint :98/:329/HUB:185). Mellette szól az M2/M4 precedens (MAN:61, :78) és az ASSIGN-S profil (MAN:19).
  - (ii) A Z.4:343 zárójele („a három szakaszban; …”) és a MAN:112 „előírt mezőiben” fordulata módosul.
  - **Ajánlás: (ii).**
    - A döntés szövege a háromrészes szerkezetet formatívnak mondja.
    - Ugyanezt már ígéri a tanulónak látható :98/:329 („előre ismert” követelmény).
    - Az átadás tartalmát a Z.3 már szigorúan, mentori elfogadással méri: MAN:110 LMS-Z-07 (mikor + melyik kvuca + ha–akkor; kinek mondja el). Egy üres 3. szakasz miatt tehát nem vész el bizonyíték.
  - Átmenetileg egyik hely sem írható át, nyelvi alapon sem. A mostani kettősség nem óvatos alapértelmezés, de a feloldása küszöbdöntés.
- **Vétó-érintettség:** completion-feltétel / küszöb (vétólista).

### Z:QA14-ERT-2 (ERT-38, passz jelzése) — EMBERI DÖNTÉS [a K1-gyel együtt döntendő]
- **Mostani állapot:** Z.4:329: „adatvédelmi szempontból érzékeny részt kihagyhatsz”. Z.4:355: „**„Még nem teljesítve”** státusz + rövid visszajelzés …, hogy mivel egészítse ki”. A passz jelzése sehol nincs leírva. Védő mondat, Z.4:167: „nem kell intim vagy érzékeny részletet megosztanod. Használj általánosított helyzetet…”.
- **Lezárt döntés / kánon:** ERT-38: „Az adatvédelmi szempontból szenzitív részek passzolhatók”. A jelzés módját nem rendezi.
- **Kutatás:** nem külső tény.
- **Javaslat:** Kérdés: hogyan jelzi a tanuló a passzt, és mi a mentor első lépése üres szakasznál? Dönt: az értékelési felelős a DPO-val.
  - Ajánlás: opcionális „passz” jelölés a szakaszcím alatt. Üres szakasznál a mentor első lépése a rákérdezés vagy a passz és a Z.4:167 szerinti általánosított változat felajánlása, nem a kiegészítés kérése.
  - A (ii) olvasatban a kérdés nagyrészt tárgytalan: ott üres szakasz miatt nincs „Még nem teljesítve”.
  - Átmenetileg a :355 marad. Csak a teljesen üres beadásra vonatkozik (:353), ez elfogadható átmenet.
- **Vétó-érintettség:** értékelési eljárás; adatvédelem. A Z.4:167 és a GYV-11 nem gyengülhet.

### Z:QA14-IMPL-3 (ERT-3, „kiürítés”) — EMBERI DÖNTÉS
- **Mostani állapot:** Z.4:400: „A „kiürítés” valós működését stagingben tesztelni kell (`LMS – H5P runtime acceptance.md` 16. pont).” RA:87: „stagingben a „kiürítés” valós működését is tesztelni kell (ERT-3; … a „kiürítés” pontos jelentését a build-spec gazda rögzíti).” MAN:113: az 1. kérdés „Required”, a többi kihagyható.
- **Lezárt döntés / kánon:** HUM:673 ERT-3 csak idézőjelben hozza a szót, a repóban sehol nincs meghatározva. A CSOMAG:749–754 kontextusa („Üres beküldés a kötelező, nem pontozott activityknél”; következmény: „RA 16. pont tesztje”) az üres beküldés olvasatát erősíti, de nem mondja ki.
- **Kutatás:**
  - Moodle 4.5 forrás, `mod/feedback/item/multichoicerated/lib.php` (MOODLE_405_STABLE): a „Not selected” opció `0` értékű, és Required elemnél `return empty($values[$inputname]) ? array(… get_string('required')) : true;`. Kód szerint tehát a Required Likert „Not selected”-del nem küldhető be. Ezt stagingben igazolni kell.
  - Törlés: docs.moodle.org/405/en/Viewing_Feedback_responses: „Individual responses may be Deleted if required.” Kurzus-resetnél a `feedback_reset_userdata` meghívja a `feedback_delete_all_completeds($feedback)`-et (`mod/feedback/lib.php`, MOODLE_405_STABLE).
  - Időzített, automatikus 90 napos törlést a core Feedbackben nem találtam. Ez következtetés, nem dokumentált állítás.
- **Javaslat:** Kérdés: a „kiürítés” a Required kérdés üres vagy „Not selected” beküldésének elutasítása, vagy a nyers válaszok törlése (Z.4:401, 90 nap)? Dönt: a projektgazda mint build-spec gazda; QA: az értékelési felelős.
  - (a) Üres beküldés negatív tesztje: a Required 1. kérdés üresen vagy „Not selected”-del nem küldhető be, és completion nem áll be. Ez a CSOMAG szerinti ERT-3-kérdés tárgya.
  - (b) Törlési teszt: egyedi törlés vagy reset. Ez megőrzési kérdés, az ADV §3 sora, a gazdája a DPO.
  - **Ajánlás: (a)** az ERT-3 alá; a (b) külön megőrzési tétel.
  - Átmenetileg az RA 16 nyitott zárójele marad. Ez az óvatos alapértelmezés.
- **Vétó-érintettség:** tesztlépés. Completion és adatvédelmi szöveg nem változik.

### KANON:QA14-ERT-2 (ERT-9, M3) — EMBERI DÖNTÉS
- **Mostani állapot:**
  - MAN:66 (LMS-M3-05): „leadva + megerősített rubrika”.
  - MAN:67 (LMS-M3-06): „az LMS-M3-05 megerősített rubrikája (§7: az M3 kapuablaka)”.
  - MAN:20 ASSIGN-M már nyitottnak jelöli: „A kétkomponensű M3 kapunál a kapukvíz az Assignment-komponens megerősített rubrikája után nyílik; ennek kódolása az ERT-9 mellett nyitott (build-spec gazda).”
  - M3 KAPU:37: „a kapukvíz (`M3_QUIZ`) csak a **megerősített rubrika után** nyílik”.
  - MAN:254: kapuablak.
- **Lezárt döntés / kánon:** HUM:679 ERT-9: „ASSIGN-M saját completion = SUBMITTED … CONFIRMED állapot külön GATE-CP-n álljon be.” Az M3-ban a kvíznyitáshoz nincs külön GATE-CP (az LMS-M3-07 mindkét komponens után töltődik). Ez új alkalmazási eset.
- **Kutatás:** docs.moodle.org/405/en/Activity_completion_settings: „Student must submit to this activity to complete it”. docs.moodle.org/405/en/Restrict_access_settings, Grade: „either a minimum value (at least percentage), a maximum value (less than percentage), both, or neither”. A MAN:172 ugyanezt a „határ nélküli Grade-feltétel” mintát használja az „Mx megerősítve”-hez.
- **Javaslat:** Kérdés: hogyan kap az LMS-M3-05 SUBMITTED completiont úgy, hogy az LMS-M3-06 csak a megerősített rubrika után nyíljon? Dönt: a projektgazda (build-spec gazda); QA: az értékelési felelős.
  - (a) Új GATE-CP sor az Assignment-komponens megerősített rubrikájára. Precedens: LMS-M7-09, egy komponens megerősített eredménye GATE-CP-n. A kvíz nyitása Grade-feltétel erre a sorra: határ nélkül (bármely megerősített érték, a KAPU:37 „megerősített” szava szerint), vagy alsó határ 50%.
  - (b) Határ nélküli Grade-feltétel közvetlenül az LMS-M3-05 grade itemjére, a marking workflow „Released” állapotával mint megerősítéssel. Ehhez runtime-bizonyíték kell (G3b).
  - (c) Kifejezett M3-kivétel („Receive a grade” completion). Ez ellentmond az ERT-9 szövegének, és csak formális eltérési döntéssel járható.
  - **Ajánlás: (a), határ nélküli Grade-feltétellel.** Determinisztikus, a BSPEC-01 mintáját követi, és nem kell kivétel.
  - Átmenetileg a MAN:66/67/20 marad. Ez óvatos: a nyitottság jelölve van.
- **Vétó-érintettség:** completion és unlock (build-spec). Küszöb és rubrika nem változik.

### KANON:QA14-IMPL-7b (ADV-3, Z.3 5. dia) — EMBERI DÖNTÉS
- **Mostani állapot:**
  - A BSPEC-02 kiegészítés már bekerült, ez a rész MÁR RENDBEN. MAN:312: „a Z.3 5. dia célmondata (LMS-Z-03; ADV-3) és az M7.3 Zmán Kvucá-checklist (LMS-M7-03; LMS-5) tanuló-lokális, külön sor nélkül”.
  - Z.3:266: „Beviteli elem nincs … nem tárolt, nem completion-feltétel”. Besorolás nincs.
  - Ellentétes jelek: Z.3:15 mikrocél „**1–2 konkrét következő lépésed**”, illetve Z.3:337 és Z.4:207 „mindkét célmondatod”.
- **Lezárt döntés / kánon:** HUM:649 ADV-3: „a kötelező/opcionális besorolás: lásd X-6”, vagyis nyitott.
- **Kutatás:** nem külső tény.
- **Javaslat:** Kérdés: kötelező tanulási lépés (tanuló-lokális) vagy opcionális? Dönt: a projektgazda.
  - (a) Kötelező, de tanuló-lokális. Precedens: Z.1 SLIDE 5–6 és Z.2 SLIDE 5–7 (D-2/D-3, MAN:312). A Z.3:337 és a Z.4:207 változatlan marad.
  - (b) Opcionális. Az ADV-3 alapértelmezés szövege és a „1–2” mikrocél mellette szól. Ekkor a Z.3:337 és a Z.4:207 „mindkét” fordulata igazítandó.
  - **Ajánlás: (a).** Beviteli elem és completion nélkül a tanulóra nem jelent kikényszerítést, és nem kell szöveget módosítani.
  - Átmenetileg a semleges „tanuló-lokális lépés” marad. Ez az óvatos alapértelmezés.
- **Vétó-érintettség:** kötelező/opcionális besorolás (vétólista).

### M4:BIZT-G1-2 (ADV-3, M4 tárolt reflexiók) — BIZONYÍTÉK-KAPU
- **Mostani állapot:**
  - A tanulói ígéret már igaz. M4.1:1206: „ebben a két válaszban csak a saját minivállalásodat rögzíted. A válaszaidat csak a kijelölt mentorod láthatja, és csak akkor, ha ténylegesen szükséges; technikai okból a Moodle rendszergazdája is hozzáférhet.” M4.3:650 ugyanígy.
  - A tárolt TEXT-C marad: MAN:70 (LMS-M4-06), MAN:74 (LMS-M4-08).
  - A narrációban még „magadnak” áll: M4.1:1199 „Most írd le magadnak ezt a két dolgot –”, M4.3:644 „Most írd le magadnak röviden:”.
- **Lezárt döntés / kánon:** ADV-3: „Az M4 már tárolt TEXT-C-ként deklarált helyein csak formális completion-/build-spec döntéssel lehet adatmentesre átállni; ha … tárolt marad, a tanulói ígéret legyen igaz és a DPO írja alá az adatkört.” Az alapértelmezett út (tárolt marad) teljesítve. Hiányzik a DPO adatkör-aláírása.
- **Kutatás:** —
- **Javaslat:** G2-kapu (`02 Tervezet/RELEASE-READINESS.md`), DPO / jogi felelős: az LMS-M4-06/-08 adatkörének aláírása.
  - A két narrációs sor csak hanggyártási fix packon át változik (VO-gazda), ebben a repóban nem.
  - Az adatmentes átállás nem kötelező. Ha a projektgazda mégis akarja, az külön build-spec döntés.
- **Vétó-érintettség:** adatvédelem. Szövegszerkesztés nincs.

### M4:ERT-G1-10 (ADV-3 / X-10, M4.1 ILO 2) — EMBERI DÖNTÉS
- **Mostani állapot:** M4.1:19: „**megfogalmazza 1 mondatban**, mit üzen egy adott kiállás a kvucának”. M4.1:12 (mikrocél): „**megfogalmazod 1 mondatban**”. A SLIDE 3 IV-kérdése most opcionális és tanuló-lokális, MAN:69: „beviteli elem nélkül fut, nem tárolt, nem completion-feltétel”. A mért szint a SLIDE 3–4 Single Choice (felismerés).
- **Lezárt döntés / kánon:** ADV-3: „Az ILO 2 átírása: lásd X-10”, vagyis nyitott.
- **Kutatás:** —
- **Javaslat:** Kérdés: hogyan szóljon az ILO 2? Dönt: a modulgazda vagy a projektgazda.
  - (a) Szűkítés: „**felismeri**, mit üzenhet egy adott kiállás a kvucának”, a mikrocélban „felismered”.
  - (b) Marad gyakoroltatott, nem mért célként.
  - (c) Új, mért produktív elem. Ez tárolt adatkör, DPO kell hozzá.
  - **Ajánlás: (a).** A cél így azt állítja, amit a lecke ténylegesen mér.
  - Átmenetileg az ILO marad. Ez nem óvatos alapértelmezés (túlígér), de az átírás pedagógiai döntés.
- **Vétó-érintettség:** kimeneti cél (pedagógiai tartalom).

### M4:ERT-G2-4 (ERT-8) — EMBERI DÖNTÉS
- **Mostani állapot:** A kiváltó-részt az előző kör átvezette (plan-M4 25–34. blokk). A sor maradéka: „Az értékelés helyét és hozzáférését dokumentálni kell”. MAN:77 (LMS-M4-05): „puha kapu, formatív: a mentori „Alapszint / rendben” küszöb … fejlesztő visszajelzés”, de a rubrikaszint Moodle-beli helyét nem nevezi meg. A GATE-CP profilban (MAN:25) „„Feedback comments” = Yes”. Az M4 fájlokat ebben a körben nem olvastam újra.
- **Lezárt döntés / kánon:** HUM:678 ERT-8 utolsó mondata. A CSOMAG:798 szerint „A rubrikaszint helyére ajánlás nincs — build-spec gazda.”
- **Kutatás:** —
- **Javaslat:** Kérdés: hol rögzül az M4 rubrikaszintje? Dönt: a projektgazda (build-spec gazda); a hozzáférésről a DPO.
  - (a) Rubrika az LMS-M4-05-ön. Az M2 precedense (MAN:60 LMS-M2-05): a tanuló a szintleírást és a kommentet látja, pontot nem.
  - (b) Szöveges szint az LMS-M4-10 „Feedback comments” mezőjében.
  - **Ajánlás: (a).** Ugyanaz a minta, mint a másik puha kapunál, és a GATE-CP értéke tisztán CONFIRMED marad.
  - Átmenetileg nincs rögzítve, a hely nincs dokumentálva.
- **Vétó-érintettség:** értékelés helye, adatkör (DPO). Küszöb és kaputípus nem változik.

### M5:ERT-G1-9 (ERT-28) — EMBERI DÖNTÉS
- **Mostani állapot:** az M5.2 SLIDE 8-at ebben a körben nem olvastam be. A CSOMAG:977 szerint a ✅ szöveg: „Először a nevelési célt találom ki…” (M5.2:558). Tanított lánc: MAN:80 „M5.2 – Feladat → cél → kvuca → módszer”. M5 KAPU:312: „a sorrend-üzenet (M5.2 „cél az első”) erősítendő”.
- **Lezárt döntés / kánon:** HUM:698 ERT-28: „…a „feladat–kvuca–módszer–cél” logikát kövesse úgy, hogy a kiválasztás valóban a tanított döntési utat méri. A ✅ pozíció csak akkor maradhat, ha a szemantika ténylegesen helyes; ellenkező esetben explicit új itemdöntés”.
- **Válasz a hívó kérdésére:** valódi itemdöntés. A döntés sorrendje (feladat–kvuca–módszer–cél) eltér a tanított lánctól (feladat → cél → kvuca → módszer, MAN:80), a KAPU:312 pedig harmadik megfogalmazást („cél az első”) hordoz. A ✅ szövege ezért a döntésből nem vezethető le. A szó szerinti sorrend a nem tanított utat kulcsolná; ha a döntés négy elemét halmazként olvassuk, az értelmezés, nem átvezetés.
- **Javaslat:** Dönt: az M5 szerzője és az értékelési felelős.
  - Ajánlás: a ✅ szöveg a tanított láncot kövesse (feladat → cél → kvuca → módszer); a döntés „feladat–kvuca–módszer–cél” fordulatát a négy elem meglétének olvassuk, nem sorrendnek.
  - Utána igazodik a HUB:207 és a KAPU:312 (CSOMAG:981).
  - Átmenetileg a ✅ és a szöveg nem változik.
- **Vétó-érintettség:** answer key (vétólista).

### M2:QA14-ERT-2 (ADV-5, M2 HUB:34) — EMBERI DÖNTÉS
- **Mostani állapot:** a HUB:34-et és a KAPU:239-et ebben a körben nem olvastam újra. A verifier idézete szerint HUB:34: „hogyan akar **személyes példát mutatni** a kvucájának”; az R3 fiktív útja KAPU:209, :264.
- **Lezárt döntés / kánon:** HUM:651 ADV-5: „engedjünk semleges, fiktív vagy válasz nélküli egyenértékű utat pontlevonás nélkül”. Ez a KAPU értékelési útját rendezi, a hub kompetencia-megfogalmazását nem.
- **Javaslat:** Kérdés: változzon-e a HUB:34 kimeneti célja, a betoldás: „(a saját vagy egy kitalált madrih példáján)”? Dönt: a projektgazda és az értékelési felelős; someres QA: a helyi ideológiai felelős (HUM-SOMER-01).
  - Ajánlás: a betoldás igen. Cél és értékelés így nem válik szét, és az R3 szintjei, illetve a küszöb nem változnak.
  - A KAPU:239 sablonsora ugyanazzal a döntéssel mozog (M2-HUB-MUNK-01, build út).
  - Átmenetileg változatlan.
- **Vétó-érintettség:** kimeneti cél; rubrikához és küszöbhöz nem nyúlunk.

---

## Összesítő

| Kulcs | Besorolás | Egysoros indok |
|---|---|---|
| M5:QA14-ERT-1 | EMBERI DÖNTÉS | az ERT-26 maga „értékelési kalibráció”; ajánlás: kalibrációs mondat szintváltozás nélkül |
| M7:QA14-ERT-1b | LEZÁRHATÓ | a :48/:217 már rendben; a :53-ba a MAN:103 „egy próbálkozásban” mondata és az RA 19 szó szerint átvezethető |
| Z:QA14-NYELV-1 + Z:ERT-G1-1 | EMBERI DÖNTÉS (összevonva) | szakaszonkénti vagy egész beadásra szóló mérce; ajánlás: (ii) egész beadás |
| Z:QA14-ERT-2 | EMBERI DÖNTÉS | a passz jelzése és a mentor első lépése; a K1-gyel együtt |
| Z:QA14-IMPL-3 | EMBERI DÖNTÉS | a „kiürítés” jelentése; ajánlás: üres beküldés negatív teszt (4.5-ös kódbizonyítékkal) |
| KANON:QA14-ERT-2 | EMBERI DÖNTÉS | M3 kvíznyitás SUBMITTED mellett; ajánlás: új GATE-CP, határ nélküli Grade-feltétel |
| KANON:QA14-IMPL-7b | EMBERI DÖNTÉS | a BSPEC-02 rész már rendben; a Z.3 5. dia besorolása X-6; ajánlás: kötelező, tanuló-lokális |
| M4:BIZT-G1-2 | BIZONYÍTÉK-KAPU | a szöveg kész, a tárolt út marad; a DPO adatkör-aláírása (G2); narráció: VO-pack |
| M4:ERT-G1-10 | EMBERI DÖNTÉS | ILO 2 (X-10); ajánlás: „felismeri” |
| M4:ERT-G2-4 | EMBERI DÖNTÉS | a rubrikaszint helye (build-spec) és hozzáférése (DPO); ajánlás: M2-minta |
| M5:ERT-G1-9 | EMBERI DÖNTÉS | ERT-28: a döntés sorrendje ≠ a tanított lánc, ezért valódi itemdöntés |
| M2:QA14-ERT-2 | EMBERI DÖNTÉS | a HUB:34 kompetenciacél az ADV-5 szövegén túlmegy |

LEVÁGVA: 3 tétel részben ellenőrizve: M5:ERT-G1-9 (az M5.2 SLIDE 7–8 mostani szövege nincs beolvasva, a ✅ szöveg a CSOMAG:977 idézete), M2:QA14-ERT-2 (a HUB:34 és a KAPU:239/:209/:264 mostani szövege nincs újraolvasva), M4:ERT-G2-4 (az M4 HUB/M4.F mostani szövege nincs újraolvasva, a kiváltó-rész állapota a plan-M4 alapján). A besorolásuk ettől nem függ, a mostani-állapot idézetet a javítás előtt pótolni kell.

## G7 – Az M7 kapukvíz visszajelzéseinek válaszszivárgása (ERT-5)

## G7: az M7 kapukvíz visszajelzéseinek válaszszivárgása (ERT-5), implementációs lencse, read-only

A bemenet tétellistája („A tételek”) üres, ezért egyetlen részletes blokkot adok a feladatban megnevezett ERT-5-kérdésről. Az ERT-40 csak a Q11/Q14 kérdéstípusán keresztül érinti a témát. Az ERT-41-et nem vizsgáltam; futólag annyit láttam, hogy szó szerint átvezetett (KAPU:260, :263; MAN:104).

**Röviden:** van szivárgási kockázat a jelenlegi specben, három helyen. A kért viselkedés core Moodle-ben megvalósítható, de csak a tanulóra érvényes zárási idővel együtt, kvízszintű beállítással önmagában nem.

### G7 / ERT-5 (M7 kapukvíz, Review options): LEZÁRHATÓ (a minimális spec-javítás). Nyitva marad két EMBERI DÖNTÉS (D1, D2) és egy BIZONYÍTÉK-KAPU (RT-P0-19 / G3b). [ÖSSZEVONVA: az M7 KAPU:51 és :415, a manifest QUIZ-M profilja (MAN:18) és LMS-M7-07 sora (MAN:102), valamint a hiányzó RA-lépés]

Finding-mezők: **ID** IMPL-1 · **Súlyosság** P2 (a döntési csomag ERT-5-súlyossága; hatása a kapu validitása) · **Bizalom** magas · **Lencse** implementáció · **Típus** objektív (a maradék: emberi-döntés, bizonyíték-kapu).

#### Mostani állapot

**1. Az itemleltár (Q1–Q14).** Mind a 14 item 4 opciós (A–D). Igaz–Hamis és kétopciós item nincs. Minden itemnek egyetlen itemszintű „Visszajelzés” bekezdése van, ez Moodle-ben természetesen General feedback lesz. Opciónkénti visszajelzés (Specific feedback) egyik itemnél sincs. A Grep 84 találatot ad: 14 cím, 14 „Visszajelzés” és 56 opció.

| Item | Típus | Kulcs | „Visszajelzés” sora | Közli a kulcsot? |
|---|---|---|---|---|
| Q1–Q6 | Single Choice | 1 | :72, :83, :94, :111, :122, :133 | közli |
| Q7 | Single Choice | 1 | :150 | közli (a három disztraktort név szerint kizárja, a kulcsot leírja) |
| Q8–Q10, Q12 | Single Choice | 1 | :161, :172, :187, :211 | közli |
| Q11 | Multi-Select | 3/4 | :198 (+ „Pontozás (képzőnek)” :200, ez nem tanulói szöveg) | közli |
| Q13 (blokkoló) | Single Choice | 1 | :230 | közli |
| Q14 | Multi-Select | 3/4 | :241 (+ „Pontozás (képzőnek)” :243) | közli |

A „Whether correct” hatása az itemtípusonként:
- **Kétopciós item:** az M7-ben nincs. Ha volna, hibás válasznál a jelölés kizárással elárulná a kulcsot.
- **4 opciós Single Choice:** hibás válasznál csak a megjelölt opciót zárja ki.
- **Multi-Select (Q11/Q14):** a megjelölt opciókat egyenként helyesnek vagy hibásnak jelöli. Ha a tanuló mind a négyet bejelölte, a teljes kulcsot látja (lásd Kutatás, renderer).

**2. A szabályszövegek.**
- KAPU:51: „a helyes választ és a teljes, opciónkénti visszajelzést csak a javító próbálkozás lezárása után”. A szabály egy az M7-bankban nem létező elemet (opciónkénti visszajelzés) nevez meg, a ténylegesen kulcsot közlő itemszintű visszajelzést pedig nem.
- KAPU:54: „rövid tanulói visszajelzés”.
- KAPU:415 (QA-lista): „a helyes válasz és a teljes, opciónkénti visszajelzés csak a javító próbálkozás lezárása után; a beállítás a célverzión visszaolvasva.”
- MAN:18 (QUIZ-M): „a helyes kulcs és a teljes, opciónkénti visszajelzés csak a javító próbálkozás lezárása után; … az eltérő Review options célverzión visszaolvasandó”.
- MAN:102 (LMS-M7-07): „a helyes válasz és az opciónkénti visszajelzés csak a javító próbálkozás lezárása után (ERT-5; célverzión visszaolvasandó)”. Itt a „teljes” szó is kimaradt.
- MAN:67 (LMS-M3-06): saját Review options-sora nincs, a QUIZ-M profilt örökli.
- Egyik szöveg sem mondja meg, melyik Moodle-időablakban mi legyen beállítva, és hogyan különül el az első és a javító próbálkozás.

**3. Az M3 összevetése.**
- M3 KAPU:35 (ce04b9c, M3:QA-ERT-2): „a helyes választ, az opciószintű visszajelzést és az itemenkénti tanulói (általános) visszajelzést csak a javító próbálkozás lezárása után”.
- Az M3-ban van opciónkénti és itemszintű visszajelzés is (M3 KAPU:51: „miért jó/rossz minden opció + tanulói visszajelzés”).
- Az M3 itemjei egyválaszos Multiple choice kérdések (KAPU:38), így ott a „Whether correct” nem árulja el a kulcsot.
- A lefedettségi jelentés ugyanezt nyitott megfigyelésként rögzítette: `01 Fejlesztés/04 Audit/2026-10-12 HUM 14 átvezetés – 125-125 lefedettségi jelentés, AP-2026-10-12-01.md:638`.

**4. A runtime acceptance.** A `02 Tervezet/LMS – H5P runtime acceptance.md`-ben nincs ERT-5-lépés, a „Review options” kifejezés nem is szerepel benne. A 19. pont (:90–96) a próbálkozásokról szól, a 8. pont (:71) a kritikus itemek névalapú kézi ellenőrzéséről, a :76 csak az M3.3 BS „Review attempts” beállításáról. A döntés (célverzión vissza kell olvasni) így egyik G3b-tesztben sem jelenik meg.

**5. Időzítési kontextus.**
- A javító próbálkozást a képző az F-peula után, felhasználói felülbírálással nyitja (M7.F:399; KAPU:50).
- Az LMS-M7-09 megerősítési ideje nyitott (MAN:103).
- Az `M7_QUIZ`-nek nincs kimondott „Close the quiz” beállítása (MAN:296). Ennek precedense az M0: „a kvízen nincs „Close the quiz”” (MAN:271).
- A tanuló a kapun kapott visszajelzésből tudja meg, melyik rész nem teljesült (M7.F:26, :144).
- A GATE-CP-n „„Feedback comments” = Yes (ide kerül a módosítás és az elutasítás oka)” (MAN:25).

#### Lezárt döntés / kánon
- **HUM14:675, ERT-5:** „ne jelenjen meg a helyes kulcs és a teljes opció-visszajelzés a javító lezárása előtt … az eltérő Moodle Review options-t célverzión vissza kell olvasni”.
- **HUM:463:** „a kritikus követelményeket megnevezzük, a kvíz kulcsát nem”.
- **HUM14:710, ERT-40:** minden-vagy-semmi kérdéstípus, ha van validált; plugin: LMS-gazda (X-11).
- **A döntési csomag** (`01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md:771`) indoklása: „az első után felfedett kulcs a második próbálkozást érvénytelen bizonyítékká tenné”.
- A javítás ezek szó szerinti, illetve közvetlen technikai átvezetése, nem új szabály: a „General feedback” megnevezése, mert az itemek visszajelzése közli a kulcsot, és az M3 KAPU:35 ugyanezt már rögzíti; a Moodle-jelölőnégyzetek leképezése (precedens: M6 KAPU:73, MAN:84); a zárási idő invariánsa, amely a Moodle-forrásból következik.

#### Kutatás (elsődleges források)

**Időablakok és elemek.** docs.moodle.org/405 Quiz settings, szó szerint:
- „"Immediately after the attempt" means within 2 minutes of the student clicking "submit all and finish".”
- „"Later, while the quiz is still open" means after 2 minutes, but before the close date (if the quiz does not have a close date, this phase never ends).”
- „"After the quiz is closed" means what it says (you never get here for quizzes without a close date).”
- „Right answer – Reveals the correct answer to each question, whether the student answered correctly or not.”
- „General feedback – Displays the general feedback for the whole question as set when adding the question to the quiz.”
- „Users with the capability 'View hidden grades' moodle/grade:viewhidden (typically teachers and administrators) are not affected by these settings and will always by able to review all information about a student's attempt at any time.”

Az 5.0-s dokumentáció: „Marks … is only available when Maximum marks is selected.” Az Overall feedbackről: „The text that is shown can depend on the grade the student got.” Ez sávos összpontszám-visszajelzés, a Q13-at név szerint nem tudja megnevezni.

**Kvízszintű, nem próbálkozásonkénti.**
- `mod/quiz/mod_form.php` (MOODLE_405_STABLE): `self::$reviewfields = [ 'attempt' …, 'correctness' …, 'maxmarks' …, 'marks' …, 'specificfeedback' …, 'generalfeedback' …, 'rightanswer' …, 'overallfeedback' … ]`. Ugyanitt: `$mform->disabledIf('generalfeedback' . $whenname, 'attempt' . $whenname);`. A „Whether correct”, a „Specific feedback”, a „General feedback” és a „Right answer” tehát csak bekapcsolt „The attempt” mellett látszik.
- A felülbírálási űrlap (`mod/quiz/classes/form/edit_override_form.php`) elemei: groupid, userid, password, timeopen, timeclose, timelimit, attempts. Review options-mező nincs benne.
- Quiz FAQ (405): „you will be able to choose one or more users and change quiz dates, times or number of attempts”.

**A felülbírálás tanulónként viszi a visszanézési állapotot.**
- `mod/quiz/classes/quiz_attempt.php`, create_helper (405 és 500 egyaránt): „// Update quiz with override information. $quiz = quiz_update_effective_access($quiz, $attempt->userid);”.
- `mod/quiz/locallib.php`: „} else if ($quiz->timeclose && time() >= $quiz->timeclose) { return display_options::AFTER_CLOSE;”.
- `IMMEDIATELY_AFTER_PERIOD = 2 * MINSECS`.

**A Multi-Select szivárgása.** `question/type/multichoice/renderer.php` (405): „if ($options->correctness && $isselected) { $feedbackimg[] = … $this->feedback_image($this->is_right($ans)) …”. A „Specific feedback” alá tartozik az összesített (combined) visszajelzés és a „toomanyselected” üzenet is.

**Következmény 1 normál + 1 javító próbálkozásnál.**
- Az „Immediately after” és a „Later while open” ablak beállítása mindkét próbálkozás után ugyanaz. Ezekkel az első és a második próbálkozás nem választható szét.
- Szétválasztani csak az „After the quiz is closed” ablakkal lehet, mert ezt a tanulóra érvényes, felülbírálással módosítható zárási idő indítja.
- Ezért core Moodle-ben megvalósítható, hogy a „Right answer”, a „General feedback” és a „Specific feedback” csak „After close” ablakban látsszon, ha ez az ablak a javítási úton lévő tanulónál nem kezdődik a javító határideje előtt.
- Csapda: ha a kvízszintű zárás `M7_V2_DUE`, és a felülbírálás csak az F-peula után készül el (M7.F:399), a bukott tanuló ez alatt az idő alatt „After close” állapotban van, és látja a kulcsot.
- A dokumentáció a négy időablakon kívül nem ír le próbálkozásonkénti vagy kézi visszanézés-engedélyezést; ilyet nem találtam. Külön javító kvíz megvalósítható volna, de új manifest-sort és új bekötést kívánna, és nem szükséges.
- Ha a Q13-at név szerint a tanuló elé akarjuk tenni, az Overall feedbackkel nem megy. Két út van: a „The attempt” + „Marks” együtt itemszintű pontot ad, vagy a mentor írja meg (lásd D1).

#### Javaslat: LEZÁRHATÓ, minimális OLD → NEW

**(1) `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md:51`**

OLD:
> a helyes választ és a teljes, opciónkénti visszajelzést csak a javító próbálkozás lezárása után. A kritikus itemekhez a mentor szabályos javítási útmutatást ad. Az eltérő Review options beállítást a célverzión vissza kell olvasni.

NEW:
> a helyes választ, a teljes, opciónkénti visszajelzést és az itemenkénti tanulói (általános) visszajelzést (az itemek „Visszajelzés” szövegét, amely a helyes választ kimondja) csak a javító próbálkozás lezárása után. Moodle-beállítás (`LMS – activity manifest.md` §1, QUIZ-M): az „Immediately after the attempt” és a „Later, while the quiz is still open” ablakban a „Maximum marks” és a „Marks” = Yes, a „Right answer”, a „Specific feedback” és a „General feedback” = No, és a Q11/Q14 Multi-Select miatt a „Whether correct” is No (a megjelölt opciókat egyenként helyesnek vagy hibásnak jelölné); a „Right answer”, a „Specific feedback” és a „General feedback” legfeljebb az „After the quiz is closed” ablakban kapcsolható be, és ez az ablak a javítási úton lévő madrihnál a felhasználói felülbírálással együtt sem kezdődhet a javító próbálkozás határideje előtt. A kritikus itemekhez a mentor szabályos javítási útmutatást ad. Az eltérő Review options beállítást a célverzión vissza kell olvasni (`LMS – H5P runtime acceptance.md` 19. pont).

**(2) Ugyanez a fájl, :415**

OLD:
> a helyes válasz és a teljes, opciónkénti visszajelzés csak a javító próbálkozás lezárása után; a beállítás a célverzión visszaolvasva.

NEW:
> a helyes válasz, a teljes, opciónkénti visszajelzés és az itemenkénti tanulói (általános) visszajelzés csak a javító próbálkozás lezárása után (az első három ablakban „Right answer”, „Specific feedback”, „General feedback” és – a Q11/Q14 miatt – „Whether correct” = No; az „After the quiz is closed” a javítási úton lévő madrihnál nem kezdődhet a javító határideje előtt); a beállítás a célverzión visszaolvasva (runtime acceptance 19. pont).

**(3) `02 Tervezet/LMS – activity manifest.md:18` (QUIZ-M, 6. oszlop)**

OLD:
> a helyes kulcs és a teljes, opciónkénti visszajelzés csak a javító próbálkozás lezárása után; a kritikus itemekhez (M3, M7) a mentor szabályos javítási útmutatást ad; az eltérő Review options célverzión visszaolvasandó

NEW:
> a helyes kulcs, a teljes, opciónkénti visszajelzés és az itemenkénti tanulói (általános) visszajelzés csak a javító próbálkozás lezárása után: az „Immediately after the attempt” és a „Later, while the quiz is still open” ablakban „Maximum marks” és „Marks” = Yes, „Right answer”, „Specific feedback” és „General feedback” = No, Multi-Select itemet tartalmazó kvíznél (M7 Q11/Q14) a „Whether correct” is No; a „Right answer”, a „Specific feedback” és a „General feedback” legfeljebb az „After the quiz is closed” ablakban kapcsolható be, és ez az ablak a javítási úton lévő tanulónál a felhasználói felülbírálással együtt sem kezdődhet a javító próbálkozás határideje előtt (a Review options kvízszintű, mindkét próbálkozásra azonos; az ablakot a tanulóra érvényes zárási idő adja); a kritikus itemekhez (M3, M7) a mentor szabályos javítási útmutatást ad; az eltérő Review options célverzión visszaolvasandó (runtime acceptance 19. pont)

Az M3-ra ez nem hoz új tartalmat: azonos az M3 KAPU:35-tel, a Multi-Select-mondat pedig ott nem érvényesül.

**(4) Ugyanez a fájl, :102 (LMS-M7-07)**

OLD:
> a helyes válasz és az opciónkénti visszajelzés csak a javító próbálkozás lezárása után (ERT-5; célverzión visszaolvasandó)

NEW:
> a helyes válasz, a teljes, opciónkénti visszajelzés és az itemenkénti tanulói (általános) visszajelzés csak a javító próbálkozás lezárása után (ERT-5; beállítás: §1, QUIZ-M; célverzión visszaolvasandó)

**(5) `02 Tervezet/LMS – H5P runtime acceptance.md:94`**

Alpontként kerül a 19. pontba, így nem kell új RT-sor.

OLD:
> &nbsp;&nbsp;&nbsp;&nbsp;- a normál és a javító próbálkozás után további próbálkozás vagy beadás mindhárom profilnál csak a képző kézi nyitásával lehetséges.

NEW:
> &nbsp;&nbsp;&nbsp;&nbsp;- a normál és a javító próbálkozás után további próbálkozás vagy beadás mindhárom profilnál csak a képző kézi nyitásával lehetséges;
> &nbsp;&nbsp;&nbsp;&nbsp;- a mastery-kvízek (QUIZ-M; M3, M7) Review options-e (ERT-5) a manifest QUIZ-M profilja szerint van beállítva. A tesztet tisztán tanulói szerepű tesztfiókkal kell végezni: a „View hidden grades” (`moodle/grade:viewhidden`) jogú felhasználóra a Review options nem vonatkozik. Negatív esetek: az első próbálkozáson nem teljesítő tesztfiók a beküldés után 2 percen belül („Immediately after the attempt”), 2 perc után („Later, while the quiz is still open”), ha a kvíznek van kvízszintű zárási ideje, annak elmúltával (a felhasználói felülbírálás létrehozása előtt és után), valamint a javító próbálkozás beküldése után, a javító határideje előtt sem lát helyes választ („Right answer”), itemenkénti tanulói visszajelzést („General feedback”), sem opciószintű vagy összesítő visszajelzést („Specific feedback”), az M7 Q11/Q14-nél pedig opciónkénti helyes/hibás jelölést sem. Pozitív esetek: ugyanez a fiók az első próbálkozás után látja a pontszámát, a hibázott kompetenciát vagy kritikus követelményt pedig a QUIZ-M profilban rögzített úton; a javító határideje után az „After the quiz is closed” ablakra beállított elemek megjelennek. Pozitív kontroll: egy tesztkvízen, ahol a „Right answer” és a „General feedback” az „Immediately after the attempt” ablakban Yes, ugyanez a tanulói fiók látja a helyes választ és az általános visszajelzést; enélkül a negatív eset nem bizonyító. A beállítás-mátrixot és az eredményt a tesztelt Moodle-verzióval és a kérdéstípusok verziójával kell rögzíteni; bármelyik változásakor a tesztet meg kell ismételni.

#### Marad, ez nem része a LEZÁRHATÓ javításnak

**D1: EMBERI DÖNTÉS.**
- **Kérdés:** hogyan látsszon az első próbálkozás után a hibázott kompetencia vagy kritikus követelmény kulcsszivárgás nélkül?
- **Ki dönt:** a build-spec gazda (LMS-gazda) és az értékelési felelős, az ERT-5 jóváhagyója.
- **(a) Mentoron keresztül.** Az első három ablakban „The attempt” = No, a tanuló csak a „Marks” értéket látja, opcionálisan az Overall feedbacket. A hibázott kompetenciát a kijelölt mentor/értékelő a megerősítéskor a GATE-CP visszajelzés-mezőjébe írja (LMS-M7-09, illetve az M3-nál LMS-M3-07), a kulcs nélkül. Előnye, hogy nincs szivárgás, és meglévő kánoni csatornát használ (MAN:25; M7.F:26, :144; az ERT-5 mentori tagmondata). Hátránya, hogy nem azonnali.
- **(b) Automatikusan, itemszinten.** „The attempt” + „Marks” = Yes, „Whether correct” = No. Csak akkor, ha a Q11/Q14 célverzión validált minden-vagy-semmi kérdéstípussal épül (ERT-40, X-11), mert részpontos Multi-Select-nél az itemenkénti részpont és a saját jelölés együtt részleges opció-következtetést enged. A kérdésszöveg is látszik, a javító pedig ugyanazt a 14 itemet kapja.
- **(c) „Whether correct” = Yes:** kizárva. A renderer miatt a Q11/Q14-nél bizonyos válaszmintákban a teljes kulcs látszik, ez ellentmond az ERT-5 szövegének.
- **Ajánlás:** most az (a), mert ez az óvatos alapértelmezés. A (b) akkor jöhet szóba, ha az ERT-40 kérdéstípusa és az RT igazolt.
- **Addig a fájlban:** a hibázott kompetencia megjelenítésének módja nincs rögzítve, ez nem óvatos alapértelmezés. Ha a hívó óvatos alapértelmezést akar beírni, ezt a mondatot javaslom a KAPU:51 és a QUIZ-M végére: „Amíg a build-spec gazda és az értékelési felelős másként nem dönt, az első három ablakban a „The attempt” is No, és a hibázott kompetenciát vagy kritikus követelményt a kijelölt mentor/értékelő a megerősítéskor a GATE-CP visszajelzés-mezőjébe írja (LMS-M3-07, LMS-M7-09), a helyes válasz nélkül.” Ez tanulói élményt érint, ezért a vétólistára kerül.

**D2: EMBERI DÖNTÉS.**
- **Kérdés:** milyen mechanizmus biztosítsa, hogy az „After the quiz is closed” ablak a javítási úton lévő tanulónál ne kezdődjön korán?
- **Ki dönt:** a build-spec gazda; a dátumoknál a programvezető (HUM-OPS-01).
- **(1) Nincs kvízszintű zárás** (az M0 mintája, MAN:271). A javítóhoz készülő felülbírálás `timeclose` = a javító határideje. Ha a beállítás elmarad, a kulcs soha nem jelenik meg, vagyis a hiba biztonságos irányba üt. A sikeresen teljesítők automatikusan soha nem látják a kulcsot, így társnak sem adhatják tovább.
- **(2) Kvízszintű zárás `M7_V2_DUE`-ra,** és minden nem teljesítő tanulónak a zárás előtt felülbírálást kell kapnia. Ez kockázatos, mert a megerősítés a zárás után is jöhet (MAN:103), a felülbírálás pedig az F-peula után készül (M7.F:399).
- **(3) Egyik ablakban sem jelenik meg automatikusan a kulcs;** a javító után a mentor beszéli át az itemeket.
- **Ajánlás:** az (1). Ha kötelező kvízzárás kell, akkor a (3).

**Megfigyelés az értékelési felelősnek, nem javítás:** ha a képző egy harmadik próbálkozást kézzel nyit meg, az már a kulcs felfedése után fut. Ezt az ERT-5 nem szabályozza.

**BIZONYÍTÉK-KAPU:** RT-P0-19 (az új alpont) és RT-P0-08 (a Q11/Q14 kérdéstípusa, ERT-40), G3b, felelős a `TEST_OWNER` / LMS-gazda. A `RUNTIME_VERIFIED` állapotot csak dátummal és verzióval rögzített tényleges teszt adhatja. Hogy a felülbírálásban megadott `timeclose` kvízszintű zárás nélkül is „After close” állapotot ad, azt a forráskódból következtettem, ezért a célverzión ezt is igazolni kell.

#### Vétó-érintettség
- Nem változik: kulcs, ✅, küszöb, próbálkozásszám, completion, rubrikaszint, kötelező/opcionális besorolás.
- Változik: a kulcs megjelenítésének időzítése, az ERT-5 szerint. Jóváhagyó az értékelési felelős; mivel a QUIZ-M közös profil, az M3-nál a Memuna QA-ja is él (ERT-5 sor), bár a szöveg azonos az M3 KAPU:35-tel.
- Gyermekvédelmi és adatvédelmi megfogalmazáshoz nem nyúl.
- A `tools/approved-visible-text.json` tartalmaz ERT-5-találatot, ezért a diff visszaolvasása után várhatóan `--pin-visible` kell a finding-ID-val.

### Összesítő

| Kulcs | Besorolás | Indok |
|---|---|---|
| G7/ERT-5: a General feedback, az ablakmátrix és a Multi-Select „Whether correct” (KAPU:51, :415; MAN:18, :102) | LEZÁRHATÓ | Mind a 14 item „Visszajelzés”-e közli a kulcsot; az ERT-5 tiltja, az M3 KAPU:35 már így rögzíti; a leképezés Moodle-forrásból adódik |
| G7/ERT-5: RA 19. pont, új alpont | LEZÁRHATÓ | Az ERT-5 kifejezetten célverziós visszaolvasást ír elő, de nincs rá tesztlépés |
| D1: hogyan látsszon a hibázott kompetencia | EMBERI DÖNTÉS | Mentoron keresztül, vagy itemszinten minden-vagy-semmi kérdéstípussal; build-spec gazda + értékelési felelős |
| D2: zárási mechanizmus | EMBERI DÖNTÉS | Kvízszintű zárás nélkül és felülbírálással (ajánlott), vagy soha nem automatikusan; build-spec gazda (+ programvezető) |
| RT-P0-19 / RT-P0-08 | BIZONYÍTÉK-KAPU | G3b, célverziós teszt, `TEST_OWNER` / LMS-gazda |

Érintett fájlok: `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md`, `02 Tervezet/LMS – activity manifest.md`, `02 Tervezet/LMS – H5P runtime acceptance.md`; összevetésként `02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md`, `02 Tervezet/Modulok/M7/Peulák/M7.F – Felzárkóztató peula – Peula & Zmán Kvucá (Study Lab).md`.

Sources:
- [Quiz settings – MoodleDocs 4.5](https://docs.moodle.org/405/en/Quiz_settings)
- [Quiz settings – MoodleDocs 5.0](https://docs.moodle.org/500/en/Quiz_settings)
- [Quiz FAQ – MoodleDocs 4.5](https://docs.moodle.org/405/en/Quiz_FAQ)
- [mod/quiz/locallib.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/locallib.php)
- [mod/quiz/classes/quiz_attempt.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/classes/quiz_attempt.php)
- [mod/quiz/classes/quiz_attempt.php (MOODLE_500_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_500_STABLE/mod/quiz/classes/quiz_attempt.php)
- [mod/quiz/mod_form.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/mod_form.php)
- [mod/quiz/classes/form/edit_override_form.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/mod/quiz/classes/form/edit_override_form.php)
- [question/type/multichoice/renderer.php (MOODLE_405_STABLE)](https://raw.githubusercontent.com/moodle/moodle/MOODLE_405_STABLE/question/type/multichoice/renderer.php)

## G8 – Részleges LMS-/build-átvezetések és VO-tételek

## G8 — kutatás és döntési javaslat (read-only, részleges: 3 tételt vittem végig, 6 LEVÁGVA)

Nem szerkesztettem semmit. Minden hely repó-relatív, a sorszámok a HEAD `10b5d76` állapotára vonatkoznak.

### M3:QA14-IMPL-1 + M3:IMPL-G2-2 — LEZÁRHATÓ [ÖSSZEVONVA: M3:QA14-IMPL-1, M3:IMPL-G2-2 (LMS-2, M3.4-rész)]

**Mostani állapot.** Az M3.2-es rész, a hub :84 sora és a KAPU :42 sora már át van vezetve (a terv 49–54., 63. és 66. blokkja). Az M3.4-es rész nincs átvezetve, a 55–62., 64., 65. és 67. blokk nincs alkalmazva. A konkrét helyek, mindegyik az `02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md` fájlban:
- **:405–432:** az M3.4-EGY-03 asset, címe „H5P Drag and Drop (két célzóna) … a húzásmentes alapértelmezett út mellett”.
- **:442:** „per-kártya visszajelzés azonos a húzós verzióval”.
- **:454:** „mellette az M3.4-EGY-03 (Drag and Drop) is elérhető”.
- **:467:** „mellette H5P **Drag & Drop** is, két célzónával”.
- **:512:** „és a per-kártya visszajelzés ugyanaz, mint a húzós verzióban. A két forma egyenértékű – a tanuló választhat”.
- **:12:** „(a húzásmentes alapút vagy a húzós változat)”.
- **:65:** „a besoroló feladat húzása/kattintása”. Ez tanulói szöveg, és a terv kihagyta.
- **:332:** a DIA-01 jegyzete: „Ugyanaz a függés, mint az M3.4-EGY-03-nál:”.

A hubban, az `02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md` fájlban:
- **:130:** „+ H5P Drag & Drop két célzónával – „OK / Nem OK madrihként””.
- **:137:** „(alapból húzásmentes, mellette H5P Drag & Drop két célzónával)”.

A `02 Tervezet/Média-assetek/_legacy/legacy-dispositions.json`-ban nincs M3.4-EGY-03 sor.

**Lezárt döntés.** `02 Tervezet/Emberi jóváhagyás szükséges.md:739`, LMS-2 `A`: „Az M3.2/M3.4 Drag & Drop mellékutakat hagyjuk el, ha a húzásmentes kártyás/rádiógombos út ugyanazt a tanulási célt és visszajelzést adja.”

A feltétel a fájlból bizonyíthatóan teljesül:
- Az EGY-04 (:442) ugyanazt a 10 kártyát adja, „válaszonkénti visszajelzéssel (`chosenFeedback`)”.
- A Drag & Drop kártyánkénti visszajelzést nem is tud adni (lásd a kutatást).

**Kutatás.**
- h5p/h5p-drag-question `semantics.json` (https://raw.githubusercontent.com/h5p/h5p-drag-question/master/semantics.json): a `feedbackOnCorrect` / `feedbackOnIncorrect` mező csak a `dropZones` alatt létezik. Leírása: „Message will appear below the task on "check" if correct droppable is matched.” Az `elements` csoportban nincs visszajelző mező. A :512 egyenértékűségi állítása tehát hamis.
- WCAG 2.2 SC 2.5.7 (https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html): „All functionality that uses a dragging movement for operation can be achieved by a single pointer without dragging, unless dragging is essential…” A törlés után nem marad húzás, így az SC 2.5.7 nem sérülhet.

**A teszt megítélése.**
- Mit véd az őr: a `tools/test_media_manifest.py:1886–1900` (`test_an_org_decision_closed_in_the_register_releases_its_assets`) azt állítja, hogy a lezárt HUM-SAFE-04 után a tőle függő assetek nem hordoznak `decision` mezőt, és nem `pending-human-decision` állapotúak. Ez nem a húzásmentes út meglétét védi.
- Mi lesz a törlés után: az EGY-03 törlésével a `by_id["M3.4-EGY-03"]` KeyError-t dob, a teszt elbukik.
- Miért nem elég csak kivenni: ha az EGY-03-at csak elhagynánk a párból, az őr egyetlen assetre gyengülne.
- Miért a csere a jó: az EGY-04-re cserélve két asset marad ellenőrizve, és az EGY-04 hordozza a HUM-SAFE-04-es 6–8. kártyát (a 60. blokk jegyzete ezt ki is mondja). A `by_id`-keresés ráadásul hallgatólagosan azt is ellenőrzi, hogy a húzásmentes út assetje létezik. Az őr tehát nem gyengül, inkább erősödik.
- A `tools/`-ban nincs más Drag/húzásmentes őr (grep).
- A csere így az LMS-2 közvetlen következménye. A governance nem érintett.

**Javaslat.** Egy változtatáskészletben, OLD → NEW:

*M3.4 lecke:*
1. **:12**
   - OLD `A SLIDE 4 besorolója (a húzásmentes alapút vagy a húzós változat) kötelező tanulási lépés;`
   - NEW `A SLIDE 4 húzásmentes besorolója kötelező tanulási lépés;`
2. **:65** (tanulói szöveg; a terven felüli, közvetlen következmény)
   - OLD `(Moodle, H5P, a besoroló feladat húzása/kattintása)`
   - NEW `(Moodle, H5P, a besoroló feladat)`
3. **:332** (terv, 55. blokk)
   - OLD `Ugyanaz a függés, mint az M3.4-EGY-03-nál:`
   - NEW `Ugyanaz a függés, mint az M3.4-EGY-04-nél:`
4. **:405–433** (56. blokk): a teljes `<!-- @asset { "id": "M3.4-EGY-03" … } -->` blokk és az utána álló üres sor törlése; az EGY-04 blokk közvetlenül a SLIDE 4 címsor utáni üres sor után kezdődik.
5. **:439** (57. blokk)
   - OLD `"title": "Húzásmentes alapértelmezett út – Multiple Choice egyválaszos módban (SLIDE 4)",`
   - NEW `"title": "Húzásmentes besoroló – Multiple Choice egyválaszos módban (SLIDE 4)",`
6. **:441** (58. blokk)
   - OLD `"purpose": "LMS a11y-sztenderd: a kapus completion ne csak drag & drop-pal legyen teljesíthető.",`
   - NEW `"purpose": "LMS a11y-sztenderd: a besorolás húzás nélkül teljesíthető; a Drag & Drop mellékút az LMS-2 döntéssel kikerült.",`
7. **:442**, két szerkesztés:
   - (a) OLD `"spec": "Ugyanaz a 8–10 (ténylegesen 10) helyzetkártya húzás nélkül is teljesíthető formában:` → NEW `"spec": "A 8–10 (ténylegesen 10) helyzetkártya húzás nélkül teljesíthető formában:`
   - (b) OLD `célfelületek ≥24px, per-kártya visszajelzés azonos a húzós verzióval; a lecke completionje` → NEW `célfelületek ≥24px; a lecke completionje`
8. **:449** (59. blokk)
   - OLD `"note": "Ez maga az a11y-megoldás; a visszajelzés-szövegek ugyanazok."`
   - NEW `"note": "Ez maga az a11y-megoldás."`
9. **:454** (60. blokk)
   - OLD `"notes": "A SLIDE 4 alapértelmezett, húzásmentes besorolója; mellette az M3.4-EGY-03 (Drag and Drop) is elérhető; azonos kártyakészlet és visszajelzés.",`
   - NEW `"notes": "A SLIDE 4 egyetlen, húzásmentes besorolója; a Drag & Drop mellékút (korábban M3.4-EGY-03) az LMS-2 döntéssel kikerült. A 6–8. kártya és visszajelzésük a HUM-SAFE-04 projektgazdai döntésén (2026-10-02) alapul; utólagos ellenőrzés (vétó/QA): a szervezeti vezetés és a Memuna; vétó esetén a `decision` mező visszakerül.",`
10. **:467–469** (61. blokk)
    - OLD `* Alapból kártyánként egy húzásmentes, kétopciós rádiógombos kérdés (lásd lent: ♿); mellette H5P **Drag & Drop** is, két célzónával:` / `  * két kategória: …` / `  * alul 8–10 kártya, mind rövid helyzet.`
    - NEW `* Kártyánként egy húzásmentes, kétopciós rádiógombos kérdés (lásd lent: ♿):` / `  * két kategória: **„OK madrihként”** és **„Nem OK / red flag-gyanús”**,` / `  * 8–10 kártya, mind rövid helyzet.`
11. **:512**, a ♿ doboz, két szerkesztés:
    - (a) a 62. blokk szerint
      - OLD `> ♿ **Kötelező húzásmentes út – ez az alapértelmezett forma (LMS a11y-sztenderd, 3. szakasz + kapus pre-flight):** mivel ez a lecke a kapu belépő feltétele (activity completion), és a sztenderd szerint a Drag & Drop kerülendő, a 8–10 helyzetkártya **alapból húzás nélkül teljesíthető** formában szerepel; a húzásmentes forma mellett elérhető Drag & Drop **nem lehet az egyetlen út**.`
      - NEW `> ♿ **Kötelező húzásmentes út – ez az egyetlen forma (LMS a11y-sztenderd, 3. szakasz + kapus pre-flight; LMS-2):** mivel ez a lecke a kapu belépő feltétele (activity completion), és a sztenderd szerint a Drag & Drop kerülendő, a 8–10 helyzetkártya **húzás nélkül teljesíthető** formában szerepel; Drag & Drop mellékút nincs.`
    - (b) OLD `a célfelületek **≥24px**, és a per-kártya visszajelzés ugyanaz, mint a húzós verzióban. A két forma egyenértékű – a tanuló választhat, melyikkel oldja meg. A lecke completionje` → NEW `a célfelületek **≥24px**. A lecke completionje`

A 7b-nél és a 11b-nél szándékosan nem a terv 26–27. blokkjának „minden kártyához saját visszajelzés tartozik” szövegét javaslom. A „Visszajelzés minták” (:499–510) csak az 5., 6., 7., 8. és 10. kártyához ad szöveget, így az a mondat új tartalmi állítás lenne.

*Hub:*
12. **:130** (64. blokk)
    - OLD `egyválaszos módban) + H5P Drag & Drop két célzónával – „OK / Nem OK madrihként”`
    - NEW `egyválaszos módban) – „OK / Nem OK madrihként”`
13. **:137** (65. blokk)
    - OLD `(alapból húzásmentes, mellette H5P Drag & Drop két célzónával)`
    - NEW `(húzásmentes)`

*Legacy-diszpozíció:*
14. **`legacy-dispositions.json`** (67. blokk, kézzel karbantartott fájl, nem build-kimenet):
    - Az M7.1-LEI-02 sor `}`-ja (:129) után `,` és egy új bejegyzés: `old_id` = `M3.4-EGY-03`, `status` = `NO_LONGER_REQUIRED`, `v2_asset_id` és `v2_deliverable_id` üres.
    - A `reason` szó szerint a 67. blokk NEW szövege: „Az M3.4 SLIDE 4 Drag and Drop mellékútja … az M3.4-EGY-04-ben változatlanok.”
    - Enélkül a reconcile `CURRENTLY_UNMAPPED_ERROR`-t ad (`tools/media_manifest.py:2259–2263`).

*Teszt:*
15. **`tools/test_media_manifest.py:1887`**
    - OLD `        """`M3.4-EGY-03` and `M3.4-DIA-01` waited on HUM-SAFE-04 (the ken alcohol and tobacco code).`
    - NEW `        """`M3.4-EGY-04` and `M3.4-DIA-01` carry content decided by HUM-SAFE-04 (the ken alcohol and tobacco code).` + új sor: `        `M3.4-EGY-03`, the Drag and Drop side path that first carried the dependency, left with LMS-2 (2026-10-12); its cards 6–8 live on in `M3.4-EGY-04`.`
16. **`tools/test_media_manifest.py:1897`**
    - OLD `        for asset_id in ("M3.4-EGY-03", "M3.4-DIA-01"):`
    - NEW `        for asset_id in ("M3.4-EGY-04", "M3.4-DIA-01"):`

*Utána:* `python3 tools/media_manifest.py build` (külön `chore(media)` commit), majd `--pin-visible "LMS-2, M3:IMPL-G2-2, M3:QA14-IMPL-1: az M3.4 Drag & Drop mellékút kivezetése"`.

**Nem blokkoló maradványok:**
- A `PRODUCTION-DECISIONS.md:16–17` darabszámai (420/913) már most is eltérnek a generált tervtől (`MEDIA-PRODUCTION-PLAN.md:16` = 416). Ezt a kánoni kör igazítsa.
- A `PRODUCTION-DECISIONS.md:392–398` történeti szövege marad.
- Az M3.1 Drag & Drop-ja marad, mert az LMS-2 nem nevezi meg. A `LMS – hozzáférhetőségi sztenderd.md:34` modulon belüli konzisztencia-szabálya miatt ezt a hozzáférhetőségi gazda nézze meg.

**Vétó-érintettség.**
- Nem változik: a kártyák, a ✅ kulcs, a completion (a CP összefoglaló diája), a kötelező státusz és a HUM-SAFE-04 tartalma.
- Az a11y-kikötés nem törlődik: a húzásmentes út marad, és ez lesz az egyetlen.
- Látható szöveg változik, ezért pin kell.
- Utólagos vétó/QA: a hozzáférhetőségi gazda.

### M5:IMPL-G2-2 — BIZONYÍTÉK-KAPU (LMS-3)

**Mostani állapot.** Az óvatos alapértelmezés bent van:
- M5.3 (`02 Tervezet/Modulok/M5/Online leckék/M5.3 – Hogyan tanulunk tényleg – Gyakorlás, aktív felidézés, időben elosztott gyakorlás.md`):
  - :529: „**Adatminimalista út (LMS-3):** … beviteli elem nem épül hozzá. … Üres Course Presentationre hamis „Receive a grade” completion nem állítható”;
  - :531: „(rövid Course Presentation vagy Moodle-oldal)”, vagyis az IMPL-G2-2.obj szerinti „Moodle Label /” már kikerült;
  - :544: „A válaszodat a saját jegyzetedbe írd le; itt nem kell beírnod sehova.”
- `02 Tervezet/LMS – activity manifest.md:85`, completion-cella: „a választott profil szerint; … a végleges completiont a valós H5P és ennek a sornak a tesztje dönti el (LMS-3; runtime acceptance 4. pont)”.

**Lezárt döntés.** HUM :740, LMS-3 `F`: „a valós H5P és az LMS-M5-07 manifest tesztje dönti el, kell-e más profil.” A HUM :612 szerint az `F` feltétel teljesüléséig az óvatos alapértelmezés érvényes.

**Kutatás.** A h5p-course-presentation `src/scripts/cp.js` szerint az összefoglaló dia csak `(this.showSummarySlide || this.hasAnswerElements)` esetén jön létre. Feladatelem nélküli CP-nek tehát nincs összefoglaló diája, és nem küld gradet. Ez megerősíti az „üres CP-re nincs „Receive a grade”” kikötést. Forrás: https://raw.githubusercontent.com/h5p/h5p-course-presentation/master/src/scripts/cp.js

**Javaslat.** Nincs szerkesztés. A hiányzó elem:
- A `LMS – H5P runtime acceptance.md:40` (4. pont) tesztje: „Mindkét úton tesztelni kell a completiont”.
- Kapu: G3b, tracker #3.
- Kitől: LMS-gazda + módszertani lektor/tananyagfelelős.
- A pontozott önellenőrző item tartalma külön tétel (M5:PED-G2-11 → PRG-4, modulgazda).
- A ledgerben BLOCKED_HUMAN helyett bizonyíték-kapuként szerepeljen.

**Vétó-érintettség:** nincs. A 72 óra, a kötelező státusz és az M6-függetlenség változatlan.

### Összesítő

| Kulcs | Besorolás | Indok |
|---|---|---|
| M3:QA14-IMPL-1 + M3:IMPL-G2-2 | LEZÁRHATÓ (összevonva) | Az LMS-2 `A`; a tesztcsere közvetlen következmény, és nem gyengíti az őrt; 16 szerkesztés, majd build és pin |
| M5:IMPL-G2-2 | BIZONYÍTÉK-KAPU | Az óvatos alapértelmezés bent van; a runtime 4. pont completion-tesztje hiányzik (G3b) |

LEVÁGVA: 6 tétel: M6:IMPL-G1-7, M7:IMPL-G2-12, M2:IMPL-G1-3, M4:BIZT-G1-7, M1:QA14-BIZT-1, M4:QA14-BIZT-4

**Mi hiányzik a levágott tételeknél:**
- **M6:IMPL-G1-7 (LMS-4):** csak a `plan-M6.md`-t olvastam. Eszerint a 39. blokk (KAPU) és a 40. blokk (RA:55) alkalmazva van, nyitott a Grade type / Maximum grade / rubrikaminimum értéke a MAN:91-ben és az RT-P0-01. A mostani fájlt nem olvastam vissza, ezért a besorolás nincs megerősítve; a valószínű besorolás: BIZONYÍTÉK-KAPU + az értékelési felelős értékei.
- **M7:IMPL-G2-12, M2:IMPL-G1-3, M4:BIZT-G1-7:** egyiket sem kezdtem el.
- **M1:QA14-BIZT-1 és M4:QA14-BIZT-4:** a fájlokat nem olvastam. Ellenőrizendő:
  - kurzusoldalon a NAR-05 spec/notes mezői és a `LMS – activity manifest.md:48` „nyitott: kerülhet-e ide valós, névtelenített helyzet” zárójele: ez az ERT-12 `A` alapján valószínűleg LEZÁRHATÓ, de ellenőrizetlen;
  - az M4.1:1199 és az M4.3:644 `@source`-on kívüli látható, illetve `@asset` mezői;
  - a `@source` maga mindkét tételnél VO fix pack marad (VO-1).

Ha folytatást kérsz, ezzel a hat tétellel kezdem.

---

## G8 folytatás: a hat levágott tétel (read-only)

Nem szerkesztettem semmit. A sorszámok a HEAD `10b5d76` állapotára vonatkoznak.

### M1:QA14-BIZT-1 — BIZONYÍTÉK-KAPU (csak a VO_PACK rész nyitott; a kurzusoldal kész) [ÖSSZEVONVA: ERT-12 NAR-része + VO-1]

**Mostani állapot.** A kurzusoldal teljesen átvezetett, csak a `@source` maradt.
- **MAN:48 már javítva.** A régi „nyitott: kerülhet-e ide valós, névtelenített helyzet” zárójel eltűnt. A mostani szöveg a `02 Tervezet/LMS – activity manifest.md:48`-on: „ide csak kitalált, életszerű helyzet kerülhet (projektgazdai döntés, 2026-10-12, ERT-12; … vétó: DPO …); a tájékoztatóba szó szerint a lecke kikötése: „Valós helyzetet – név nélkül sem – ne írj le: …””.
- **A leckeszöveg:** `02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md:885`: „egy kitalált, de életszerű helyzetre. Valós helyzetet – név nélkül sem – ne írj le”.
- **A NAR-spec**, ugyanott :837: „a tanulót saját mini-SBI megfogalmazására biztatja (kitalált, életszerű helyzet)”.
- **A hub:** `02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md:116`: „saját mini-helyzet felvázolása (csak kitalált)”.
- **Egyetlen maradék:** M1.3:901, `@source` M1.3-NAR-05-VO: „Gondolj egy helyzetre, ami eszedbe jut – vagy találj ki egy egyszerű, kisebb sztorit.”

**Lezárt döntés.**
- HUM :682, ERT-12 `A`: „a leckeszöveg, HUB, MAN és érintett NAR-spec egy fix packban igazodik. DPO-vétó és szükséges hanggyártás külön.”
- HUM :746, VO-1: „a valóban kimondott szöveget módosító … blokkot újra kell renderelni és meghallgatni … a kurzusoldali alkalmazást a felhasználó kéri.”

**Javaslat.**
- Most nincs kurzusoldali szerkesztés.
- A VO fix packnek (plan-M1:1461), kimondott szöveg, újrarender kell: :901 OLD „Gondolj egy helyzetre, ami eszedbe jut – vagy találj ki egy egyszerű, kisebb sztorit.” → NEW „Találj ki egy egyszerű, kisebb sztorit.”
- Ki viszi: a médiafelelős / VO-gazda, DPO-vétóval.
- A `RELEASE-READINESS.md`-ben nincs külön VO-sor. A ledgerben VO_PACK / nyitott release-blokkolóként álljon, ne FIXED-ként.
- Az M1.3-NAR-05::TRANSCRIPT leirat a `@source`-ból épül, ezért a pack beérkezéséig a látható leirat is a régi mondatot hordozza.

**Vétó-érintettség:** adatvédelmi kikötés; a DPO-vétó él. Kurzusoldalon nem kell semmit szerkeszteni.

### M4:QA14-BIZT-4 — BIZONYÍTÉK-KAPU (csak VO_PACK; a kurzusoldal kész)

**Mostani állapot.**
- **M4.1** (`02 Tervezet/Modulok/M4/Online leckék/M4.1 – Mit üzen a testem – Nonverbális kiállás.md`):
  - a látható szöveg már „magadnak” nélkül áll: :1182 „Zárásként írd le röviden, mire figyelsz majd …”;
  - a spec semleges: :1126 „felhívás a 2 dolog leírására minivállalásként”;
  - csak a `@source` maradt: :1199 „Most írd le magadnak ezt a két dolgot –”.
- **M4.3** (`…/M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md`):
  - a látható szöveg: :625–628 „Zárásként gondold végig: …”;
  - a spec: :569 „felszólítás, hogy a tanuló írja le …”;
  - csak a `@source` maradt: :644 „Most írd le magadnak röviden:”.

**Lezárt döntés.**
- HUM :649, ADV-3 `F`: „ha pedagógiai bizonyíték nélkül tárolt marad, a tanulói ígéret legyen igaz”.
- VO-1 (HUM :746).

**Javaslat.**
- Kurzusoldalon nincs szerkesztés.
- A VO fix packnek. Ez a javaslatom: a plan-M4:1054 NEW szöveget nem ad, csak a „magadnak” törlését jelöli meg; kimondott változás, újrarender kell.
  - :1199 OLD „Most írd le magadnak ezt a két dolgot –” → NEW „Most írd le ezt a két dolgot –”
  - :644 OLD „Most írd le magadnak röviden:” → NEW „Most írd le röviden:”
- Ki viszi: a médiafelelős / VO-gazda; DPO-vétó az ADV-3 szerint. A ledgerben VO_PACK / nyitott.

**Vétó-érintettség:** adatvédelmi ígéret (ADV-3); kurzusoldalon nem kell semmit szerkeszteni.

### M6:IMPL-G1-7 — EMBERI DÖNTÉS (a beállítási értékek) + utána BIZONYÍTÉK-KAPU (RA 8. pont)

**Mostani állapot.** A döntés elvi része és a teszt bent van:
- `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:388`: „A kapudöntést a rubrikasorok értékelése és a megerősített kapueredmény (GATE-CP, LMS-M6-07) hordozza, nem a Moodle által normalizált összpont; a szintpontokat (1/2/3) értékelői döntés nélkül nem vetítjük át 0/1/2-re.”
- `02 Tervezet/LMS – H5P runtime acceptance.md:55`: „negatív eset: … összesen 11/15; pozitív eset: minden sor = 2, összesen 10/15 – a kapu teljesül …”.

Hiányzik: a `LMS – activity manifest.md:91` (LMS-M6-05) sorában nincs Grade type, Maximum grade és rubrikaminimum („… | M6_ASSIGN | társas visszajelzés élőben, nem Moodle Workshop |”). Más sorokban ez rögzítve van: :50, :60, :66 „Grade type: Point, Maximum grade = 8”, :104 „= 24”.

**Lezárt döntés.** HUM :741, LMS-4 `F`: „Ha megőrizzük az 1/2/3 pontokat, a Grade type / Maximum grade / rubrikaminimum … legyen dokumentálva.” Az értékeket a döntés nem adja meg, a felelős: LMS-gazda + értékelési felelős.

**Kutatás** (Moodle Docs, Rubrics, https://docs.moodle.org/405/en/Rubrics):
- „…the plain sum would be 2 points. But that is actually the lowest possible score so it maps to the grade 0 in Moodle.”
- A beállítás: „Calculate grade based on the rubric having a minimum score of 0”.
- A FAQ: „If you are using a criterion without a 0-points level … should be ticked to avoid unexpected grades.” Az M6 1–3 szintjeinek nincs 0 pontos szintje.

**Eldöntendő:** az LMS-M6-05 Grade type, Maximum grade és rubrikaminimum-beállítása, és hogy a tanuló látja-e a pontot.
- **Ki dönt:** LMS-gazda + értékelési felelős.
- **Opciók:**
  - (A) Point, Maximum grade = 15, a „minimum score of 0” bekapcsolva. A Moodle-pont így a nyers rubrikaösszeg (5–15), ami egyezik a RA:55 „11/15” és „10/15” jelölésével.
  - (B) Point, 15, a „minimum score of 0” kikapcsolva. Normalizált érték: csupa „Oké” = 7,5. Félrevezető.
  - (C) Az A vagy a B, de a pont rejtve a tanuló elől, ahogy az M2 sorában (:60: „a szintpontot és a végső pontszámot nem … a rejtés Moodle-beállításának nevét stagingben kell igazolni”).
- **Ajánlás:** A + C. Az A az elsődleges forrás FAQ-ja szerint a 0 pont nélküli szintekhez való beállítás. A C a „fordított irányú” nyerspontot elrejti, a kapueredményt a GATE-CP adja.
- **Átmeneti állapot:** a MAN:91 változatlan. A KAPU:388 már kimondja, hogy a nyers pont nem kapudöntés, ezért ez az óvatos állapot.
- **Döntés után (LEZÁRHATÓ):**
  - MAN:91 OLD `| M6_ASSIGN | társas visszajelzés élőben, nem Moodle Workshop |`
  - NEW `| M6_ASSIGN | társas visszajelzés élőben, nem Moodle Workshop; Grade type: Point, Maximum grade = <érték>; rubrika: „<a választott minimum-beállítás>” (csak build-paraméter: a küszöb és az R4/R5 blokkoló sor nem kódolható bele; a kapudöntést a GATE-CP hordozza, LMS-4) |`
- **Bizonyíték utána:** RA 8. pont (:55), visszaolvasás stagingben (RT-P0-01); G3b, tracker #3.

**Vétó-érintettség:** az 1/2/3, a küszöb és a blokkoló sorok nem változnak; ezt az értékelési felelős vétózhatja.

### M7:IMPL-G2-12 — BIZONYÍTÉK-KAPU (LMS-7, csak az (a) rész)

**Mostani állapot.**
- A (b), (c) és (d) alt-szöveg már átvezetett: M7.4:245 „Három építőkocka…”, M7.3:535 „Öt ikon…”, M7.4:365 „Kvuca-típus-választó piktogramok…”.
- Nyitott az (a): `02 Tervezet/Modulok/M7/Online leckék/M7.2 – Nemcsak játék, hanem peula – 11 tervezési pont & AI-támogatás.md:401–406`. Itt a részletes alt áll („A Peula 11 pontja három egymást követő fázisra bontva. 1. fázis – … A nyilak a fázisok sorrendjét jelzik …”).
- A Program terv :221 (a) rövid altja: „Három blokk: Előkészítés (4 pont), Megírás (4 pont), Biztonság & továbbfejlesztés (3 pont).”
- A dia látható szövege (:395–399) a 3 fázist és a pontszámokat mutatja. A :405 szerint a dia „mind a 11 pontot szövegesen is megjeleníti”.

**Lezárt döntés.** HUM :744, LMS-7 `F`: a PT-alt csak akkor, „ha a diagram lényegi információját ténylegesen közvetíti. Az akadálymentességi felelős ellenőrizze, hogy a rövid alt és a látható kísérőszöveg együttesen teljes értékű-e”.

**Javaslat.**
- Nincs szerkesztés. Óvatos alapértelmezés: a részletes alt marad, mert az akadálymentesítési szöveg nem gyengülhet.
- A hozzáférhetőségi gazda (HUM-A11Y-01) írásos ellenőrzése kell; G5a/G5b, tracker #3.
- Pozitív verdikt után egyetlen `@source` alt-blokk cseréje következik a PT :221 (a) szó szerinti szövegére, majd build.

**Vétó-érintettség:** akadálymentesítési kikötés; a hozzáférhetőségi gazda vétózhatja.

### M2:IMPL-G1-3 — EMBERI DÖNTÉS (PRG-9 b)

**Mostani állapot.**
- `02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrihként – identitás-körök.md:8`: „a SLIDE 4 kérdése különálló, nem követett elemként … a HUM-PRIV-01 két útja … közül egyik sincs kizárva”.
- Ugyanott :431: „nem lehet attempt trackinggel futó H5P-activity része. Runtime-ellenőrzés: a kitöltés után nincs tárolt próbálkozás.”
- `LMS – activity manifest.md:52` ugyanígy.
- A SLIDE 4 helye a 3 → 4 → 5 úton nincs rögzítve; ez a finding tárgya.

**Lezárt döntés.**
- HUM :729, PRG-9 b `F`: „M2.1 identitáskör: maradjon a CP-ben integrált, nem követett reflexió, tényleges tárolás-ellenőrzéssel.”
- A kánon szerint a követés activity-szintű: RA :104 (21. pont) „Mivel a próbálkozás-rögzítés activity-szintű beállítás …”. A követett M2.1 CP-n belül (H5P-C, „Enable attempt tracking” = Yes, MAN:16) tehát egy beágyazott interakció nem tehető „nem követetté”. A „CP-ben integrált” szó szerinti, interakciós olvasata a mai beállítással nem valósítható meg. (A Moodle-dokumentációból a részkérdésenkénti rögzítést nem tudtam elsődleges forrással igazolni; a RA 21. pont mondata kánoni.)

**Eldöntendő:** a SLIDE 4 helye és formája.
- **Ki dönt:** build-/LMS-gazda + M2 modulgazda (DPO nem kell).
- **Opciók:**
  - (i) A követett CP diáján interakció nélküli reflexió: a kérdés és az opciók listaként, az egységes visszajelzés statikus szövegként, „Check” nélkül. Ez a RT-P0-14 tartalékútja (M2.1:452) is.
  - (ii) Tartalombankos elem a CP activity leírásába ágyazva. A kérdés így a SLIDE 3 jelenete előtt jelenik meg.
  - (iii) A mai, különálló, nem követett elem a CP után. A SLIDE 5 előtti tudatosítás kimarad.
- **Ajánlás:** az (i). Ez szó szerint „CP-ben integrált” és „reflexió”. Megőrzi a 3 → 4 → 5 sorrendet, és nincs mit tárolni, így a tárolás-ellenőrzés triviálisan teljesül. Ára: elvész a kattintós interakció, ezt a modulgazda mérlegeli.
- **Átmeneti állapot:** a mai szöveg (a kérdés nem a követett activityben fut) az adatvédelmileg óvatos alapértelmezés (HUM-PRIV-01), marad.
- **Bizonyíték:** RT-P0-21, RA 21. pont (LMS-gazda), G3b.

**Vétó-érintettség:** adatvédelmi kikötés (HUM-PRIV-01, a nem tárolás) nem gyengülhet. A completion nem érintett.

### M4:BIZT-G1-7 — BIZONYÍTÉK-KAPU (PRG-14 a)

**Mostani állapot.** Az AI-jelölésről mindenhol feltételes ígéret áll, címke sehol:
- M4.3:22: „ahol generatív AI-t használtunk (szöveg, kvíz-item, disztraktor, besorolási példa), azt a tanulónak látható felületen jelöljük.”
- Ugyanígy: M4.2:23, M4.4:29, a hub :16, M4.A:14, M4.B:14.
- A PT:224 a lecke alján egy rövid sort ír elő.

**Lezárt döntés.** HUM :734, PRG-14 `F`: „Generatív AI eredetet csak szerzői/provenance bizonyíték alapján jelöljünk, soha ne tippeljünk. … A tényleges médiaeredetet a szerző vagy médiafelelős igazolja.”

**Javaslat.**
- Nincs szerkesztés: a feltételes mondat nem tippel, szerzői nyilatkozat nincs.
- Hiányzik a szerző / tananyagfelelős (média: médiafelelős) itemenkénti írásos provenance-nyilatkozata az M4.2–M4.4 tételeire.
- Ez után, LEZÁRHATÓ lépésként, a PT:224 szerinti „lecke alján egy rövid sor” csak a nyilatkozatban megnevezett itemekhez kerül ki.
- A `RELEASE-READINESS.md`-ben nincs saját G-sor erre. Legközelebbi: G2 / tracker #2 (AI). Ezt a ledgerben bizonyíték-függésként kell rögzíteni.

**Vétó-érintettség:** AI-átláthatósági kikötés; címkét feltételezésből kitenni vagy elhagyni tilos.

### Összesítő

| Kulcs | Besorolás | Indok |
|---|---|---|
| M1:QA14-BIZT-1 | BIZONYÍTÉK-KAPU (VO_PACK) | A MAN:48, a :837, a :885 és a hub :116 kész; csak a :901 `@source` maradt (VO-1, újrarender; DPO-vétó) |
| M4:QA14-BIZT-4 | BIZONYÍTÉK-KAPU (VO_PACK) | A látható szöveg és a spec kész; csak a :1199 és a :644 `@source` maradt |
| M6:IMPL-G1-7 | EMBERI DÖNTÉS + BIZONYÍTÉK-KAPU | A KAPU:388 és a RA:55 kész; a MAN:91 Grade type / Max / minimum értéke az LMS-gazda + az értékelési felelős döntése; ajánlás: Point, 15, „minimum score of 0” bekapcsolva + rejtett pont; utána RA 8. pont |
| M7:IMPL-G2-12 | BIZONYÍTÉK-KAPU | A (b), (c), (d) kész; az (a) rövid altja a hozzáférhetőségi gazda ellenőrzésére vár, addig a részletes alt marad |
| M2:IMPL-G1-3 | EMBERI DÖNTÉS | A „CP-ben integrált, nem követett” csak interakció nélküli diaként valósítható meg; ajánlás: (i); addig a mai, nem követett elem marad |
| M4:BIZT-G1-7 | BIZONYÍTÉK-KAPU | Szerzői provenance-nyilatkozat nélkül nincs címke; a feltételes ígéret nem tippel |

## G9 – Részleges program- és értékelési átvezetések

## G9 — részleges program- és értékelési átvezetések (22 tétel + 1 kereszt-javítás)

Röviden: a PRG-1 szövege nem adja meg, mit kell vágni, ezért a tíz tétel együtt EMBERI DÖNTÉS marad, modulonkénti vágási javaslattal. Egyetlen biztonságosan lezárható javítást találtam: a PRG-5 hiányzási mondata az M6.F-ből és az M7.F-ből hiányzik (lásd lent). A többi tétel emberi döntés vagy bizonyíték-kapu, egy pedig már rendben van.

Rövid nevek: `M0.A` = `02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md`; a többi peula, lecke és KAPU ugyanígy a `02 Tervezet/Modulok/<modul>/…` alatt van. `HUM` = `02 Tervezet/Emberi jóváhagyás szükséges.md`. A sorszámokat a HEAD `10b5d76`-on olvastam vissza, kivéve ahol jelzem.

### Összesítő tábla

| kulcs | besorolás | egysoros indok |
|---|---|---|
| M0:PED-5 | EMBERI DÖNTÉS (ÖSSZEVONVA: PRG-1) | a PRG-1 a vágás tartalmát a modulgazdára bízza; a 45’-es címkék már rendben (M0.A:153–157) |
| M2:PED-G3-1 | EMBERI DÖNTÉS (PRG-1) | Blokk 3: 20–25’ a 15’-ben, a védett páros megosztással; perc nem vezethető le |
| M3:PED-G3-1 | EMBERI DÖNTÉS (PRG-1) | M3.A/M3.B/M3.F túlfutás; M3.B-nél kell a Memuna is, a PRG-11/12-vel egy menetben |
| M4:PED-G2-2 | EMBERI DÖNTÉS (PRG-1) | öt blokk lóg túl; az M4.A:254-es puffer-mondat csak a tervvel együtt módosulhat |
| M4:NYELV-G2-6 | EMBERI DÖNTÉS (PRG-1 + szerzői szándék) | a „ha belefér az idő” mire vonatkozik: a két mondat a 4. tanulási cél |
| M5:PED-G2-6 | EMBERI DÖNTÉS (PRG-1) | M5.A/M5.B/M5.F túlfutás |
| M5:QA-PED-2 | EMBERI DÖNTÉS (PRG-1) | M5.1: a részidők 9–13 perc, a metaszám 15–20; a döntés tiltja a kitalált „átmeneti” percet |
| M6:PED-G3-1 | EMBERI DÖNTÉS (PRG-1) | M6.A 4.4: a védett reflexiós lépések egyedül is kitöltik a 10 percet |
| M7:PED-G3-1 | EMBERI DÖNTÉS (PRG-1) | M7.A/M7.B túlfutás; az M7.F belépésének helye |
| M7:NYELV-G3-14 | MÁR RENDBEN | az M7.A és az M7.B rész kész; az M7.F-rész a hét F-peula közös sablonja, nem ellentmondás |
| M3:ERT-G3-10 | EMBERI DÖNTÉS | 1–5 fős változat (PRG-4) és a kapacitás (programvezető) |
| PRG-5 kereszt (M6.F, M7.F) | LEZÁRHATÓ | a döntés hiányzási szabálya feltétel nélküli; az M1.F, M3.F, M5.F már tartalmazza, az M6.F és az M7.F nem |
| M3:IMPL-G3-9 | EMBERI DÖNTÉS | M3.A kártyadarabszám, M3.B csoport/eset skálázása (modulgazda + Memuna) |
| M5:PED-G1-3 | EMBERI DÖNTÉS | az M5.1 SLIDE 4 1./4. kulcsa csak szakmai lektori döntés után változhat |
| M7:NYELV-G3-12 | EMBERI DÖNTÉS | az „átjárás” döntés szerinti olvasata nem illik az Idő & helyszín kontextusba; kell a szerzői szándék |
| M5:PED-G1-10 | EMBERI DÖNTÉS (ÖSSZEVONVA: TERM-7, PRG-2) | formatív demonstráció vagy a hub-cél szűkítése |
| M2:PED-G1-11 | BIZONYÍTÉK-KAPU | az ERT-19 tartalma lezárt; hiányzik a modulgazda és az értékelési felelős aláírása, és az előzetes tájékoztató |
| M3:IMPL-G2-14 | EMBERI DÖNTÉS | az elfogadási szabály bent van (M3.2:666); az itemenkénti kulcsvalidálás hiányzik |
| M5:NYELV-G1-11 | EMBERI DÖNTÉS | a C opció szövegét a szerzőnek/értékelőnek jóvá kell hagynia (answer key-közeli) |
| M6:ERT-G1-2 | EMBERI DÖNTÉS (ÖSSZEVONVA: M6:ERT-G3-4) | R4 „Oké”-horgony: rubrikaváltozás kalibrációval |
| M6:ERT-G3-4 | EMBERI DÖNTÉS (→ M6:ERT-G1-2) | ugyanaz a döntés (M6.B mezőlista) |
| M7:BIZT-G1-1 | EMBERI DÖNTÉS | R8 kettéválasztása és kapuhatás: értékelési felelős + DPO |
| M7:PED-G1-1 | EMBERI DÖNTÉS | az új R1 2-es horgony szövege és projektgazdai jóváhagyása, tájékoztatóval |

---

### PRG-1 — tíz tétel együtt (M0:PED-5, M2:PED-G3-1, M3:PED-G3-1, M4:PED-G2-2, M4:NYELV-G2-6, M5:PED-G2-6, M5:QA-PED-2, M6:PED-G3-1, M7:PED-G3-1; az M7:NYELV-G3-14-et külön blokk tárgyalja) — EMBERI DÖNTÉS [ÖSSZEVONVA]
- **Megadja-e a döntés a vágás tartalmát?** Nem. A HUM 14 PRG-1 szövege: „a modulgazdák tételes vágási tervvel csökkentsék a túlcsorduló lépéseket, a védett biztonsági/reflexiós és kötelező feldolgozó lépések rövidítése nélkül”. Az M5.1-re: „a 15–20 perc és a 9–13 percre összegződő részidők tényleges újrabecslése vagy a metaszám visszaigazítása kell, nem kitalált „átmeneti” percek”. Szerepek: a vágási tervet az adott modulgazda írja, M3.B-nél a Memunával; vétó/QA: programvezető. Lépésszintű percet a döntés nem ad, a percek pedig vétólistás időtartamok, ezért egyik tétel sem LEZÁRHATÓ.
- **Ami már kész (ellenőrizve):** M0.A:153–157: a 45’-es címkék a Blokk 2/3-hoz igazodnak, és a „Kihez fordulhatok?” rész védett. M0.A:650: „tartsd meg a zárókört + „Kihez fordulhatok?” részt, és a „Madrih, nem terapeuta” lépést (4.3, 3. lépés) is”.
- **Kutatás:** nem kell, belső tervezési kérdés.
- **Javaslat a modulgazdáknak.** Minden javaslat a 45’ és a blokkhatárok megtartásával, a védett lépések rövidítése nélkül. A percek a meglévő sávokon belül maradnak.
  - **M0.A (60’).** Blokk 2 (10–25’), most 16–21’: :341 biztonsági keret 1–2 (védett) · :344 csoportalakítás 2→1 (előre kijelölt csoportok) · :351 plakát 8–10→8 · :357 kiscsoportos megosztás 3 · :360 körbenézés 2–3→1 (a :349 nagy létszámú módja: csak körbesétálás és olvasás). Összesen 14–15’. Blokk 3 (25–40’), most 13–18’: :421 flipchart 1 (a cím előre felírva) · :425 ötletelés 8 · :442 MNT 3–4 (védett) · :448 közös „igen” 1–2. Összesen 13–15’.
  - **M0.A (45’).** Blokk 2 (10’): keret 1–2, csoport 1, plakát 5, megosztás 2. A plenáris kimarad, a plakátok kint maradnak. Blokk 3 (10’): ötletelés 5, MNT 3–4, „igen” 1. A :651 („gondold át előre, hol rövidítesz”) helyére jöhet ez a terv.
  - **M2.A.** Blokk 2 (10’), most 10,5–12,5’: a tér kijelölése (:245) a peula előtt, a mini-lezárás (:268) egy mondat; a 8 állítás marad. Blokk 3 (15’), most 20–25’: :336 rajzolás 5–7→3 (csak frissítés, ha a M2.1-es térkép megvan: PED-G1-8/E-M2-046) · :353 párok 1 · :356 páros megosztás 2×5 (a saját sávjának alsó értéke, nem rövidítés) · :367 mini-reflexió 1 mondat, vagy beolvad a 4.4.1-be. Összesen 15’. 4.4.2 (most 6–7’ az 5-ben): a 4.4.1 nagykör (:407) 3→2’, így a zárókör 39–45’ lehet. Ez csak a Blokk 4-en belüli 40’-es alhatárt mozdítja; a modulgazda erősítse meg.
  - **M2.B Blokk 4** (most 12’ a 10-ben): a :387 képzői záró üzenet a vállalás-kör utolsó mondata lesz (a képző utolsóként mondja el a saját vállalását és a hidat). Így 5+5 = 10’; a két védett lépés változatlan.
  - **M2.F** (:141 ↔ :203, a finding szerint): a technikai belépés az érkezéskor történjen, a Blokk 2-es lépés ellenőrzéssé szűkül.
  - **M3.A.** 4.2 (most 16–22’): :235 emlékeztető 1–2 · :251 csoportalakítás 1 · :262 szobor 4 · :295 bemutatás 4×2 = 8. Összesen 14–15’. 4.3 (most 17–19’): a kártyák előre az asztalokon (:393, 1’) · :444 párosítás 10→7–8 · :462 a 3 kártyás átbeszélés 5–7 (védett). Összesen 13–16’. A hamis :309-es mondatot („A blokk így marad az 5–20’ keretben.”) a tervvel együtt kell átírni.
  - **M3.B (Memunával).** 4.2 (most 21–24’): :320 keret 2–3 (védett) · :352 csoportalakítás 1 · :372 feldolgozás 5–6 · :381 visszahozás esetenként 3’ (×3 = 9). Összesen 17–19’. 4.3 (most 17–22’): :427 bevezetés 1–2 · :433 lépések 10–11 · :465 a 4.3.3 2–3’-es időszelep. Ha kimarad, a „Fontos különbség” akkor is elhangzik (PRG-12, már bent van).
  - **M3.F** (4.4: 5–7’ az 5-ben; Blokk 3: 15–18’): lépéslistát nem olvastam. Elv: a 20’-es csendes pótlás és a zárókör védett, a fogalomtérkép magyarázó lépései rövidülnek.
  - **M4.A.** 4.3 (most 16–19’): :230 2 + :236 12 + :246 1 = 15’; 16 fő fölött a :254-es triádút az alap. 4.4 (most ≈12’): 1’ instrukció + 3×(2’ próba + 1’ visszajelzés) = 10’. 4.5 (most 5–8’): :374 zárókör 3–4 (védett) · :383 záró üzenet egy mondat a kör végén · :378 kilépőkártya leadása kifelé menet.
  - **M4.B.** 4.3 (most 16–20’): :274 csoportalakítás 1 + felkészülés ≤2 (a 2. lépést nem ellenőriztem) + :285 kör 10–12. 4.4 (most 11–14’): a 4.4/1 (5’) és a két mondat védett; a :334 záró üzenet 1’.
  - **M4.B:326 (M4:NYELV-G2-6):** a szerzőnek javasolt szöveg: „Két mondatot szeretnék hallani tőletek; ha szűk az idő, akár egyben is elmondhatjátok.” Így a két mondat kötelező tartalom marad (4. cél), az idő csak az összevonást engedi. A szerzői szándékot meg kell erősíteni (8. regressziós minta). A mostani sort nem olvastam újra, a plan-M4 idézi.
  - **M5.A/M5.B/M5.F (M5:PED-G2-6).** M5.A 4.1: legfeljebb 24 fő név + 1 példa, a már átvett M1.A:195-ös névkihagyással. M5.B 4.2.1: a :326-os „5 perces” ↔ „1 percben” közül választani kell. M5.B 4.3.1–4.3.2: 3 csoport × 2’ = 6’, a visszajelzés csak a 4.3.2-ben (36–40’), nem minden bemutatás után (:405). M5.F 4.4: zárókör 3’ + híd 2’.
  - **M5.1 (M5:QA-PED-2).** Mostani állapot: M5.1:653–656 „~2–3 / ~2–3 / ~3–4 / ~2–3 perc”, :657 „→ összesen 15–20 perc, megfelel a sablonnak.”, :7 és :34 „15–20 perc”, HUB:7 „4×15–20 perc”. Opciók: (A) a részidők újrabecslése 2–3 15–17 éves próbaolvasóval a kész H5P-vázlaton; a metaszám marad, ha a mért idő belefér. (B) A metaszám visszaigazítása; ekkor a HUB:7 és a 3,5 órás terhelés (HUM-OPS-01) is átszámolandó. Ajánlás: A, mert a 15–20 perc a leckesablon, és az A-nak nincs láncolt következménye. Addig a metaszám túlbecsül, ami a terhelés tervezésénél óvatos; a :657 állítása viszont addig is hamis marad.
  - **M6.A.** 4.2 (most 15–18’): :241 2 + :329 5 + :363 korosztály-sarok időszelepként (csúszásnál elhagyható) + :391 elemzés 5 (mag). Összesen 12–15’. 4.3 (most 18–22’): :431 keret 3–4 (védett) · :472 játék 5 · :519 minikör 3 · :539 szemüveg 4 (a sarokszavazás rövidül, a variációs rész védett). Összesen 15–16’; a 4.3.2/B érintetlen. 4.4 (most 13–16’): a :650 záró üzenet 1’-re rövidül, a híd az M6.B-hez átkerül az M6.B elejére. A páros (:612) és a nagykör (:630) összevonása (pl. 4’+5’) védett lépést érint, ezért ez kifejezetten a modulgazda döntése, programvezetői vétóval.
  - **M6.F:** a 4.3-at nem olvastam. A Blokk 1-es Moodle-kérés miatt a belépés az érkezéskor legyen.
  - **M7.A.** Blokk 2 (most 6–8’): a tér előre kijelölve, :210 1 + :212 3 + :221 1 = 5’. Blokk 3 (most 15–17’): a :358 5’-re, összesen 15’. Blokk 4 (most 17–24’): alapból 2 önkéntes (2×4’), :395 1, :410 1, :416 2. Összesen 12–13’; a harmadik önkéntes csak akkor, ha marad idő. A :403 („2–3 önkéntes fér bele”) a tervvel együtt igazítandó. Másik út: a :423–434-es galéria-változat 13’. Blokk 5 (most 6–7’): a :465 zárómondat a :462 kör utolsó mondata, összesen 5’.
  - **M7.B.** Blokk 2 (most 17–28’): :413 2 · :422 10–11 · :444 5–7 · a :472 AI-tipp csak akkor, ha marad idő. Az opcionális státusz és a nem-AI út nem változik. Összesen 17–20’. Blokk 3 (most 9–12’): 1 + 4 + 4–5 = 9–10’, így a :540 igaz marad. Blokk 4 (most 6–9’): a :574 záró üzenet a kör végén, a :570 kilépőkártya leadása kifelé.
  - **M7.F:** a belépés az érkezéskor; a :50 már „előkészített Moodle / H5P belépéssel” számol.
  - Mi marad addig: minden percszám és a :309, :403, :540, :254 mondat változatlan. Ez a meglévő állapot, nem óvatos alapértelmezés: a túlfutás a terepen a zárókört szorítaná ki.
- **Vétó-érintettség:** minden lépésperc időtartam; a 45’ és a blokkhatárok nem változnak. Védett lépés rövidítését csak az M6.A 4.4 és az M2.A 4.4.2 alhatár-mozgatása vetheti fel; ott a programvezető a vétós.

### M7:NYELV-G3-14 — MÁR RENDBEN
- **Mostani állapot:** az M7.A kész: M7.A:65 „„Kvucám, SMART célom, 2 pontom”” = :385. Az M7.B kész: :500 és :524 „mitől lett alaposabb”. Az M7.F-rész: M7.F:95 „Rövid, privát állapotfelmérés: „Mit jelzett a kapu visszajelzése, és min dolgozol ma?”” ↔ :104 „### 4.1. Blokk 1 – Privát állapotfelmérés: „Hol tartok, miben kérek segítséget?” (0–5’)”.
- **Lezárt döntés / kánon:** a K33 a PRG-1-hez kötötte. A korpusz azonban mutatja, hogy ez sablon. Mind a hét F-peulában ugyanaz a szerkezet: a percbontásban modulspecifikus kérdés, a blokkcímben a közös „Hol tartok, miben kérek segítséget?” (M1.F:115↔124, M2.F:92↔101, M3.F:106↔118, M5.F:95↔104, M6.F:149↔158; M4.F:95). A két alak tehát blokknév és nyitókérdés, nem egy kérdés két változata.
- **Javaslat:** szövegváltozás nincs; a ledgerben „korpusz-sablon, változtatás nélkül” zárással. Ez a reviewer ítélete egy validált finding ellenében; ha a fő session nem fogadja el, az M7.F-rész a PRG-1 M7-es tervével egy menetben a modulgazdáé.
- **Vétó-érintettség:** nincs.

### M3:ERT-G3-10 (PRG-5) — EMBERI DÖNTÉS
- **Mostani állapot:** M3.F:45 „**Ha valaki nem tud részt venni:** a javító próbálkozás előtt dokumentált pótidőpontot vagy jóváhagyott, rövid egyéni mentoros utat kap; …” (kész). M3.F:24 „**Létszám:** kb. 6–20 fő”; 1–5 fős változat nincs.
- **Lezárt döntés:** HUM:725 PRG-5 „Minden kötelező F-peulához legyen 1–5 főre előre leírt, azonos kompetenciát fejlesztő változat. … A programvezető rögzítse a kapacitást és a pótlási felelőst.”
- **Javaslat.**
  - Eldöntendő: az 1–5 fős változat szövege, valamint a kapacitás és a pótlási felelős.
  - Ki dönt: a változatot a modulgazda írja a PRG-4 `/course-develop` csomagban (csak a felhasználó indíthatja); az 1:1 kérdésben a Memuna; a kapacitásról a programvezető.
  - Opciók: (a) F-peulánként külön kis létszámú változat; (b) egy közös, programszintű „kis létszámú F-peula” keret, amelyre minden kötelező F-peula hivatkozik, modulspecifikus tartalmi betéttel. Ajánlás: (b), mert egy szerzői kör, kevesebb redundancia, és a döntést ugyanúgy teljesíti.
  - Addig a „6–20 fő” sor marad; kitalált változat nem kerül be.
- **Vétó-érintettség:** kötelező/opcionális nem változik; 1:1 kiskorúval csak a HUM-SAFE-02 szerint.

### PRG-5 kereszt — M6.F, M7.F hiányzási szabálya — LEZÁRHATÓ
- **Mostani állapot:** a hiányzási út az M1.F:66-ban, az M3.F:45-ben és az M5.F:20-ban szerepel, az M6.F-ben és az M7.F-ben nem. Mindkettő kötelező F-peula: M6.F:40 „Mivel az M6 kapuja éles, a peula ilyenkor **kötelező**.”; M7.F:35 „Az F-peula **kötelező annak, akinek az M7 éles kapuja nem teljesült**”. Az M2.F:20 és az M4.F:37 „ajánlott”, ott a szabály nem alkalmazandó.
- **Lezárt döntés:** HUM:725, a mondat feltétel nélküli: „Hiányzásnál dokumentált pótidőpont vagy jóváhagyott, rövid egyéni mentoros út legyen, mindig a javító próbálkozás előtt; 1:1 kiskorúval csak a meglévő HUM-SAFE-02 kivétel szerint.” Az előző futás plan-M6/M7-je azzal tartotta vissza, hogy „csak akkor ígérhető, ha a programvezető rögzítette a kapacitást”. Ez ellentmond az M1/M3/M5 kezelésének, ahol ugyanez a mondat a kapacitás-mondattal együtt bekerült.
- **Szerkesztés 1:** fájl `02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md`, :41.
  - OLD: `* **Időpont:** a kapueredmény megerősítése után, a javító leadás előtt; a képző jelöli ki a központi naptár szerint: a kapu megerősítését követő hétfőn, 18:00-tól; ha az M6 javítása az M7 útját akadályozza, a képző a Z utáni hét hétfőjére teheti. A javító leadás határideje a központi naptár szerint az F-peula utáni szerda 18:00.`
  - NEW: ugyanez a sor, utána új sor: `* **Ha valaki nem tud részt venni:** a javító leadás előtt dokumentált pótidőpontot vagy jóváhagyott, rövid egyéni mentoros utat kap; kiskorúval 1:1 csak a safer-working szabály egyik meglévő kivétele szerint lehet (`Gyermekvédelem – release gate.md` §4.2). A kapacitást és a pótlás felelősét a programvezető rögzíti.`
- **Szerkesztés 2:** fájl `02 Tervezet/Modulok/M7/Peulák/M7.F – Felzárkóztató peula – Peula & Zmán Kvucá (Study Lab).md`, :36.
  - OLD: `  * Aki csak **lemaradt** egy leckével vagy peulával, **csendes pótlással** pótol; erre a peula 2. blokkja (Csendes pótlás) is helyet ad.`
  - NEW: elé új sor: `  * **Ha valaki nem tud részt venni:** a javító próbálkozás előtt dokumentált pótidőpontot vagy jóváhagyott, rövid egyéni mentoros utat kap; kiskorúval 1:1 csak a safer-working szabály egyik meglévő kivétele szerint lehet (`Gyermekvédelem – release gate.md` §4.2). A kapacitást és a pótlás felelősét a programvezető rögzíti.`, utána változatlanul az OLD sor.
- **Miért nem új szabály:** a M3.F:45 szó szerinti mondata, a lezárt PRG-5 és HUM-SAFE-02 átvezetése.
- **Vétó-érintettség:** a gyermekvédelmi megfogalmazás szó szerint a már lezártból jön. Completion: az M7.F:35 szerint a javító „a képző nyitja meg, vagy az F-peula jelenléti completionje a feltétele”. A mentoros út a „képző nyitja meg” ágon fut, a completion-szabály nem változik. Ha a build csak a jelenléti completiont használja, azt az LMS-gazdának kell jeleznie (manifest-következmény, nem szövegváltozás).

### M3:IMPL-G3-9 (PRG-11) — EMBERI DÖNTÉS [ÖSSZEVONVA az M3.B PRG-1/PRG-12 menettel]
- **Mostani állapot:** kész az M3.A:395 („3–5 fős kiscsoportokat; a csoportok száma a létszámból adódik”), az M3.A:458 és az M3.B:374 (egyenlő részvétel). Nyitott:
  - M3.A:396: „Minden kiscsoport kap **2–3 kvuca-sztori kártyát** (összesen kb. 6–8 kártya…)” egy 8 darabos szettből (:425). 20 főnél 3–5 fős csoportokkal ez 8–21 kártya lenne.
  - M3.B:354: „Oszd a kvucát **3–4 fős csoportokra**. Alapból 3 csoporttal számolj”, és :264 „3–4 fős”. Ez 20 főnél nem hajtható végre (3×4 = 12).
- **Lezárt döntés:** HUM 14 PRG-11 „8–20 főnél alapból 3–5 fős csoportokat … a csoportszámot és kártyakészletet a létszámhoz igazítva … az adott célhoz ténylegesen szükséges eset-/kártyadarabszám”. A darabszám nincs megadva; M3.B-nél kell a Memuna is.
- **Javaslat.**
  - Eldöntendő: a kártya- és esetkészlet a létszámhoz. Dönt: az M3 modulgazda, M3.B-nél a Memunával.
  - Opciók: (a) duplikált, meglévő kártyák: M3.A-nál 4 csoporttól a 8-as szett második példánya, és két csoport ugyanazt kapja; M3.B-nél 3–5 fős csoportok, 4 csoporttól az 1–3. eset duplán, visszahozás esetenként. A 4. kártya a PRG-12 szerint a 4.3.3-é. (b) Új esetkártyák: ez új gyermekvédelmi tartalom, PRG-4 és Memuna. (c) 3 csoport marad nagyobb csoportokkal: ellentmond a PRG-11 3–5 fős alapjának.
  - Ajánlás: (a). Nincs új tartalom, és a duplikált eset összevetése maga is tanulságos. Az M3.A közös átbeszélése marad a képző választotta 3 kártyán (PRG-16).
  - Addig a :354/:264 marad; ez nem óvatos alapértelmezés, csak a mostani állapot.
- **Vétó-érintettség:** kulcs nem érintett; M3.B esetanyag (G1, Memuna).

### M5:PED-G1-3 (PRG-15) — EMBERI DÖNTÉS
- **Mostani állapot:** M5.1:439 „Szavalóverseny az iskolában, zsűri pontoz, oklevelet kapsz.”; :442 „Suli utáni matekszakkör, ahol a tanár plusz feladatokat ad, és dolgozat lesz belőle.”; a kulcs :448 „1. formális (iskolai, pontozott, értékelés)” és :451 „4. formális (suli, tanár, értékelés)”. Ezzel szemben :369 a nonformálisra: „a suli rendszerén **kívül vagy mellett** zajlik”.
- **Lezárt döntés:** PRG-15 b) „csak a formális–nonformális–informális definícióval egybevetett szakmai lektor döntése után módosítsuk”.
- **Kutatás:** ebben a sessionben nincs webes eszközöm, az alábbit nem ellenőriztem élőben.
  - A Tanács 2012. december 20-i ajánlása a nem formális és informális tanulás validálásáról (2012/C 398/01, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32012H1222(01)): a formális tanulás „typically leads to the award of a qualification”; a nonformális „planned activities … where some form of learning support is present”.
  - UNESCO ISCED 2011: a nonformális „addition, alternative and/or complement to formal education”.
  - E szerint a két helyzet inkább nonformális, a „formális” kulcs vitatható.
- **Javaslat.**
  - Eldöntendő: kulcs vagy helyzetszöveg. Dönt: szakmai lektor / M5 szerzője.
  - Opciók: (a) a kulcs marad, a két helyzet szövege egyértelműen formálissá válik (tanóra, tanterv, jegy); (b) a kulcs nonformálisra vált, a visszajelzés a :369-re hivatkozik; (c) mindkét válasz elfogadott, határeset-visszajelzéssel.
  - Ajánlás: (a). A bevezető besorolás célja a tiszta elkülönítés; a határeset a M5.A élő vitájába való (:259 már annak nevezi).
  - Addig a kulcs marad; formatív elem, nem kapu.
- **Vétó-érintettség:** answer key (b, c); az (a) a feladatszöveget érinti, a ✅-t nem.

### M7:NYELV-G3-12 (PRG-16) — EMBERI DÖNTÉS
- **Mostani állapot:** a többi rész kész (a „kattant”, „szerzett javítás” és „Ha fut az idő” már nincs a szövegben). Nyitott: M7.B:434 „– Milyen hosszú (hány perces) a Zmán Kvucá? Hol lesz pontosan? Van-e átjárás másik térbe?”, és a MUNK-01 spec :292 „(1) Idő & helyszín (hossz, pontos hely, átjárás)”.
- **Lezárt döntés:** PRG-16 „M7.B „átjárás” egyértelmű részvételi/álláspontváltási instrukció … A szerző szándékát megerősítő rövid QA kell”. A döntési csomag (:1588) csak „az „átjárás” szándéka” kérdést tette fel. A döntés olvasata az Idő & helyszín sorba nem illik, ezért ez új alkalmazási eset.
- **Javaslat.**
  - Eldöntendő: mit jelent itt az „átjárás”. Dönt: a modulgazda.
  - Opciók: (a) „Kell-e közben átvonulni egy másik helyszínre, és hogyan oldjátok meg?”; (b) „Járnak-e át mások a téren?”; (c) a döntés részvételi olvasata, de az a sarokjátékhoz tartozna, nem ide.
  - Ajánlás: (a), mert logisztikai és felügyeleti pont, illik a sorba.
  - Addig marad; biztonsági szempontból nem félrevezető. A :292 `@asset` spec, ezért változáskor build és pin kell.
- **Vétó-érintettség:** látható szöveg.

### M5:PED-G1-10 (TERM-7, PRG-2) — EMBERI DÖNTÉS [ÖSSZEVONVA]
- **Mostani állapot:**
  - M5 HUB:18 „…és saját szavaiddal **elmagyarázod**, hogyan tanulnak tényleg a hanihok…”
  - :32 „**Elmagyarázza az alap tanulástan-fogalmakat és alkalmazza őket a saját peuláira.**”
  - :33 „Saját szavaival el tudja magyarázni a **gyakorlás, aktív felidézés és időben elosztott gyakorlás** fogalmakat…”
  - A KAPU felismerést és alkalmazást mér (pl. Q12, KAPU:263–277).
- **Lezárt döntés:** TERM-7 „rövid, formatív demonstrációval lehet ellenőrizni; ha nincs erre idő/hely, a hub célmegfogalmazását szűkítsük”; PRG-2 „inkább szűkítsük a hub-ígéretet … mint hogy … új activityt építsünk”.
- **Javaslat.**
  - Eldöntendő: demonstráció vagy szűkítés. Dönt: modulgazda + értékelési felelős, a célkitűzésről a projektgazda.
  - Opciók: (a) egy meglévő élő lépés kijelölése nem pontozott ellenőrzésnek (M5.B 4.3.2 vagy M5.F 4.3.0); de az M5.B 4.3 már most túlfut (PRG-1). (b) Szűkítés: :32 „**Felismeri az alap tanulástan-fogalmakat, és alkalmazza őket a saját peuláira.**”; :33 „Felismeri a **gyakorlás, aktív felidézés és időben elosztott gyakorlás** elemeit egy peulatervben, és 2–3 konkrét ötlete van…”; :18 „…felismered, hogyan tanulnak tényleg a hanihok (…), és ezt a saját peuláidban alkalmazod”.
  - Ajánlás: (b), mert idő nincs rá, és a PRG-2 is a szűkítést preferálja.
  - Addig marad; a kapura nincs hatása.
- **Vétó-érintettség:** kompetencia-megfogalmazás, kulcs és küszöb nem. A Program terv és a manifest tükörszövegét nem ellenőriztem.

### M2:PED-G1-11 (ERT-19) — BIZONYÍTÉK-KAPU
- **Mostani állapot:**
  - M2 KAPU:37 „Megneveztem **legalább 3 identitás-körömet** (pl. ÉN–család–zsidóság–Somer–egyéb közegek)”
  - KAPU:218 „• ÉN – ____”
  - M2.1:477 „Köré rajzolj **3–4 nagyobb kört**”
  - M2.A:343
- **Lezárt döntés:** ERT-19: az ÉN a középpont, a „legalább 3 kör” három további réteg. A szigorítást „előre kommunikálni és a modulgazda/értékelési felelős által aláíratni kell, meglévő beadást visszamenőleg nem büntetünk”.
- **Javaslat:** a tartalom eldőlt. Hiányzik a modulgazda és az értékelési felelős írásos aláírása, és az előzetes tanulói tájékoztató. Ez hatálybalépési feltétel, nem G1–G8-kapu. Az aláírás után LEZÁRHATÓ egy menetben a plan-M2:319–321 listája szerint: az A.1 példájából kikerül az ÉN; az R1 három kört kér az ÉN-en kívül; a D-sablonban az ÉN középpont; a HUB:25 és az M2.1:477 egyeztetése. Addig a mai, enyhébb szöveg marad.
- **Vétó-érintettség:** rubrika/küszöb szigorítás.

### M3:IMPL-G2-14 (ERT-23) — EMBERI DÖNTÉS
- **Mostani állapot:** M3.2:666 „(Az elfogadott párosításokat jelenetenként az M3 modulgazdája és az értékelési felelős validálja: …)” (kész). A kulcs :658–664: 1 Parparim, 2 Kivsza, 3 Leviatán, 4 Leviatán, 5 Kivsza, 6 Leviatán, 7 Leviatán.
- **Lezárt döntés:** ERT-23; a validálás itemenként a modulgazdáé és az értékelési felelősé.
- **Javaslat.**
  - Egyetlen kulcs marad az 1-nél (erős fejlődési jel), a 4-nél és a 7-nél (szó szerinti „idősebb” jel).
  - A 2. és az 5. (bekiabálás, egymás szavába vágás) csoportdinamikai, nem életkori jel: javaslom a Kivsza és a Leviatán elfogadását.
  - A 3. és a 6. az M3.2 korosztálytérképe alapján döntendő; ezt nem ellenőriztem.
  - Addig a kulcs érvényes, a visszajelzés „iránymutató”.
- **Vétó-érintettség:** answer key.

### M5:NYELV-G1-11 (ERT-30) — EMBERI DÖNTÉS
- **Mostani állapot:** M5 KAPU:269 „C) ✅ Először **közösen eléneklik**, a következő pénteken **fejből idézik fel**, és a dal **több héten át röviden visszatér**.” Az A, B és D első személyű (:267, :268, :270).
- **Lezárt döntés:** ERT-30: a C mondatot első személyhez kell igazítani, a ✅ jelentése változatlan, a szerző/értékelő jóváhagyásával.
- **Javaslat.**
  - Opciók: (1) „Először **közösen elénekeljük**, a következő pénteken **fejből idézzük fel**, és a dal **több héten át röviden visszatér**.” (2) A plan-M5 javaslata: „…fejből felidéztetem velük…”.
  - Ajánlás: (1). Ugyanaz a nézőpont, mint az A és a D „mi”-je; a kvuca a felidézés ágense marad, így a :274-es indokkal („a madrih aktív, a kvuca passzív”) nem ütközik, és a :277-es visszajelzés változatlanul igaz. A (2) ágenst vált.
  - Dönt: értékelési felelős + modulgazda. Addig marad.
- **Vétó-érintettség:** kulcsopció szövege; látható szöveg.

### M6:ERT-G1-2 és M6:ERT-G3-4 (ERT-32) — EMBERI DÖNTÉS [ÖSSZEVONVA]
- **Mostani állapot:** M6 KAPU:399, R4 „Oké”: „**Legalább 1 konkrét** fizikai **VAGY** érzelmi / beleegyezéssel kapcsolatos biztonsági megjegyzés…”; :409 „legalább **1** konkrét, eszközspecifikus biztonsági mondat”. A tanított minimum a KAPU:189-ben: „szabad, akadályoktól mentes tér, közös „stop” jelszó, a vezető társ folyamatos hangos jelzése, lassú (séta) tempó. (M6.1 fizikai biztonsági minimum)”.
- **Lezárt döntés:** ERT-32 „ne implementáljuk értékelési/Memuna kalibráció nélkül”; a rubrikaszintről a projektgazda dönt.
- **Javaslat.**
  - Opciók: (A) teljes, eszköztípusonkénti horgony; (B) első lépésben csak a két megnevezett típusra: kontaktjátéknál akadálymentes tér + stop-jelzés + lassú tempó + kísérés, szenzitív helyzetnél passzjog + megnevezett felelős felnőtt; a többi típus a mai horgonyon marad. (C) A horgony marad, csak mentori megjegyzés kerül mellé: ez ellentmond a döntésnek.
  - Ajánlás: (B). Kalibráció 6–10 mintalapon két értékelővel (értékelési felelős + Memuna), előzetes tájékoztatással, visszamenőleges hatás nélkül.
  - Addig a mai, enyhébb horgony marad. Biztonságkritikusan ez nem óvatos, de a döntés tiltja a kalibráció nélküli bevezetést.
  - Az M6.B:219 mezőlistát nem olvastam újra; egy menetben igazítandó.
- **Vétó-érintettség:** rubrikaszint, blokkoló R4.

### M7:BIZT-G1-1 (ERT-42) — EMBERI DÖNTÉS
- **Mostani állapot:** M7 KAPU:360, R8 0: „„robotnyelvű”, sablonos, AI-másolat hatású, **és/vagy** beazonosítható hanih-adat … **(Adatszivárgás esetén jelzés a mentornak; ha gyermekvédelmi feltárás …)**”. Az Adatvédelem doksiban csak promptszabály van (:188).
- **Lezárt döntés:** ERT-42: kettéválasztás; a beadás ne legyen automatikusan elfogadott; DPO-jóváhagyott korlátozás, incidensértékelés, adateltávolítás és javító leadás. „Rubrika és kapuhatás formális döntést igényel.”
- **Kutatás:** élőben nem ellenőriztem. GDPR 4. cikk 12. pont (incidens-definíció), 5. cikk (1) c) (adattakarékosság), 33. cikk (1) (értesítés, kivéve, ha valószínűleg nem jár kockázattal), https://eur-lex.europa.eu/eli/reg/2016/679/oj. Hogy egy beadott hanih-név incidens-e, az DPO-értékelés.
- **Javaslat.**
  - Opciók: (A) az R8 csak pedagógiai (saját hang / AI-másolat), mellette külön, nem pontozott „adatvédelmi stop”: azonosítható harmadik személyes adatnál a beadás pontszámtól függetlenül javításra visszamegy, DPO-folyamat szerint, eltávolítással; (B) az R8 0-s szintje blokkoló lesz: két konstruktumot kever; (C) marad.
  - Ajánlás: (A). Nyitott részkérdés: a javító leadás ne fogyassza a javító próbálkozást, mert jogorvoslat, nem teljesítménybukás.
  - Dönt: értékelési felelős + DPO; QA: programvezető. Addig marad; a gyermekvédelmi ág érintetlen.
- **Vétó-érintettség:** rubrika, kapuhatás, adatvédelmi megfogalmazás.

### M7:PED-G1-1 (ERT-43) — EMBERI DÖNTÉS
- **Mostani állapot:** M7 KAPU:279, R1 2: „…és tartalmaz **legalább egy mérhető jelet VAGY időkeretet** („a peula végére…”, „legalább X hanih…”).”
- **Lezárt döntés:** ERT-43: valóban ellenőrizhető jel vagy kimenet kell, „csak előzetes egyértelmű tanulói tájékoztatóval és projektgazdai jóváhagyással léphet hatályba”. A horgony szövege nincs megadva.
- **Javaslat.**
  - Opciók: (A) „…és tartalmaz **legalább egy ellenőrizhető jelet vagy kimenetet** („legalább X hanih…”, „a peula végére mindenki … tud”); az időkeret önmagában nem elég.” (B) „jel ÉS időkeret”: túlmegy a döntésen. (C) Marad.
  - Ajánlás: (A), az ADV-5 R1-kérdésével, a Q3 visszajelzéssel (KAPU:93) és az M7.1:316–320-szal egy menetben; ezeket nem olvastam újra.
  - Dönt: a szöveget az értékelési felelős írja, a projektgazda hagyja jóvá; QA: módszertani lektor. Addig marad.
- **Vétó-érintettség:** rubrikaszint-szigorítás.

**Hiányzó ellenőrzések** (minden tételt besoroltam, de ezeket nem olvastam újra):
- lépéslisták: M2.A Blokk 2 2. lépése, M3.F 4.4 és Blokk 3, M4.B 4.3 2. lépése, M7.B Blokk 4 2. lépése, M6.F 4.3, M5.A/M5.B belső percei;
- konkrét sorok: M2.F:141/:203, M4.B:326 mostani sora, M6.B:219;
- az M3.2 korosztálytérképe;
- a Program terv és a manifest tükörszövegei (TERM-7, ERT-43);
- webes elsődleges forrás nem volt elérhető (PRG-15, ERT-42).

## VA – Verifier A (A1–A10)

Ellenőrzés: AP-2026-10-12-02, A csomag (A1–A10). Read-only, HEAD 10b5d76. A koordinátor kérésére a munka közben adom le. Az A8–A10 tételt nem vittem végig.

A1 | MEGERŐSÍTVE, egy NEW pontosításával | LMS-2 (M3:QA14-IMPL-1 + M3:IMPL-G2-2) | Mind a 16 OLD szó szerint és egyedien megvan: M3.4 :12, :65, :332, :405–432 (EGY-03 blokk), :439, :441, :442, :449, :454, :467–469, :512; hub :130, :137; `tools/test_media_manifest.py` :1887, :1897. A `legacy-dispositions.json`-ban nincs M3.4-EGY-03 sor, az utolsó bejegyzés az M7.1-LEI-02 (:124–129). Az LMS-2 feltétele a fájlból bizonyítható: az EGY-04 ugyanazt a 10 kártyát adja `chosenFeedback`-kel. A h5p-drag-question `semantics.json` állítását WebFetch-csel ellenőriztem: a feedbackOnCorrect/Incorrect csak a dropZones alatt van, az elements csoportban nincs visszajelző mező. A tesztcsere (EGY-03 → EGY-04) nem gyengíti az őrt: két asset marad; a buildelt manifestben az EGY-04 `decision: ""`, `spec-ready`. Az M3.1 és a hub :65/:70 Drag & Drop-ja marad, mert az LMS-2 csak az M3.2-t és az M3.4-et nevezi meg. Egy pontosítás kell: a legacy `reason` szövegéből (scratchpad `impl/plan-M3.md:867`) a „kártyánkénti visszajelzést adó” kimarad. Visszajelzés-minta csak az 5., 6., 7., 8. és 10. kártyához van, és ezt a kutató maga is kerülte a 7b/11b-nél. Végleges NEW: a 14. pontban a reason ez: „Az M3.4 SLIDE 4 Drag and Drop mellékútja („OK / Nem OK madrihként”). 2026-10-12-i projektgazdai döntés (LMS-2, `Emberi jóváhagyás szükséges.md` 14. szakasz): a mellékút kikerül, mert a húzásmentes besoroló (M3.4-EGY-04) ugyanazt a tanulási célt és visszajelzést adja. Akadálymentesítési rés nem keletkezik: a kártyakészlet, a kulcs és a visszajelzések az M3.4-EGY-04-ben változatlanok.” A többi 15 OLD → NEW az `out-G8.md` 1–13. és 15–16. pontja szerint változatlanul jó. Utána: build (külön `chore(media)` commit), a darabszám-pinek ellenőrzése, majd `--pin-visible`.

A2 | MEGERŐSÍTVE | GYV-5 (M6:QA14-BIZT-4, a kísérő javítás) | Az M6.A:182 végéről valóban hiányzik a GYV-5 zárómondata. Ugyanez a mondat szó szerint áll az M0.A:94-ben, az M3.B:275-ben és a Z.A:59-ben, a HUM:628-ban pedig: „Végleges létszámnorma a Memuna és programvezető hatásköre.” Az OLD az M6.A-ban egyedi, a sor vége. Csak hozzáadás, semmi nem törlődik. OLD `Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben lehet; felkavart kiskorú nem maradhat egyedül.` → NEW `Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben lehet; felkavart kiskorú nem maradhat egyedül. A végleges létszámnormát a Memuna és a programvezető határozza meg.`

A3 | MEGERŐSÍTVE | GYV-11 (az M1:QA14-BIZT-5 alpontja) | Az M1 KAPU:27-ből hiányzik a korlátozás és helyesbítés. Az ADV §5:153 kánoni mondata szó szerint ott van, ahogy a kutató idézi. Az M3 KAPU:309 és az M3.4:835 már tartalmazza: „szükség szerinti korlátozással/helyesbítéssel és adatvédelmileg jóváhagyott törléssel/m[egőrzéssel]”; a Z.4:359 és a :401 is. A tárolt M1 kapubeadvány (Assignment) a GYV-11 közvetlen hatóköre („Tárolt beadandóba kerülő gyermekvédelmi feltárásnál”), ezért ez átvezetés, nem új alkalmazás. A szerkesztés M1-fájlt érint: csak a next-version ágon, a pilot-freeze (CC-04, main@213a4c5) érintetlen. OLD `Bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan. |` → NEW `Bizonyítékot jogi megőrzési felülvizsgálat nélkül nem törlünk automatikusan; a Memuna-eljárást, a szükség szerinti korlátozást vagy helyesbítést és az adatvédelmileg jóváhagyott törlést vagy megőrzést dokumentálni kell (projektgazdai döntés, 2026-10-12, GYV-11). |`

A4 | MEGERŐSÍTVE, egy NEW pontosításával | GYV-19 (M2:QA14-BIZT-3) | Az M2.A:362 idézete pontos. A GYV-19 (HUM:642) név szerint az M2.A-ra adja: „a képzőnek és a Memunának a kijelölt úton jelezni kell”. A GK §4.1:82 („a címzett … mindig a Memuna …, nem „egy felnőtt””) azt zárja ki, hogy más kapja a jelzést a Memuna helyett. Az „és” szerkezetben a Memuna közvetlen címzett marad; a mostani szöveg viszont a képzőtől teszi függővé a jelzést. Így nincs ütközés, a GYV-19 szó szerint megválaszolja a kérdést. A kutató NEW-ja nyelvileg kevert: felszólítás után kettőspont és személytelen szerkezet. Végleges: OLD `azonnal szólj a képzőnek, aki a kijelölt úton bevonja a Memunát.”` → NEW `azonnal szólj a kijelölt úton a képzőnek és a Memunának.”`

A5 | RÉSZBEN | JOG-1 (M3:BIZT-G1-8, a kapcsolódó szerkesztés) | A hub :42 idézete pontos. A JOG-1 sehol máshol nincs átvezetve; a döntési csomag :617–624 kifejezetten erre a hub-helyre („HUB:42 … rögzíteni kell”) kérdezett. Ezért a JOG-1 ideiglenes rendjének szó szerinti átvétele zárható. A javasolt csere viszont törli a „a külső jelzés jogi kérdésében jogi szakértő dönt” tagmondatot, és az nem bizonyítottan hibás. Ez a hub egyetlen kifejezett jogászi szerepe; ezt a JOG-1 „címzettjeit/időhatárait jogász ellenőrizze” része és a GK §5:121 tartja fenn. A csere tehát jogi kikötést gyengítene: a cserés változat ELVETVE, a hozzáadó változat zárható. Végleges: OLD `; a külső jelzés jogi kérdésében jogi szakértő dönt.` → NEW `; a szervezet nevében a jogi tanács alapján kijelölt felnőtt dönt a külső jelzésről, anélkül hogy az akut védelem késne; a külső jelzés jogi kérdésében jogi szakértő dönt.` A kijelölt felnőtt megnevezése, a jogászi ellenőrzés és a Memuna-jóváhagyás bizonyíték-kapu marad (G1).

A6 | MEGERŐSÍTVE, egy NEW pontosításával | ERT-40 (M7:QA14-ERT-1b) | Az M7 KAPU:53 OLD-ja megvan. A MAN:103 (LMS-M7-09): „„Teljesítve” = egy próbálkozásban ≥12/14 teljesen helyes item ÉS a Q13 helyes … a „Highest grade” szerinti próbálkozásban a Q13 hibás is lehet: 19. pont”. Az RA:96 ugyanígy. A kutató második tagmondata („részpontot is beszámító próbálkozás ettől eltérhet”) már nem szó szerinti, és a minden-vagy-semmi ágon pontatlan. A 11+2-es esetet a :53 meglévő negatív tesztje úgyis lefedi, ezért a MAN:103 szövegét veszem át. Küszöb, kulcs és próbálkozásszám nem változik. Végleges: OLD `addig a kvíz megerősítése (LMS-M7-09) előtt a képző kézzel ellenőrzi, hogy a két Multi-Select csak teljes ponttal számított-e.` → NEW `addig a kvíz megerősítése (LMS-M7-09) előtt a képző kézzel ellenőrzi, hogy a két Multi-Select csak teljes ponttal számított-e. A „Teljesítve” feltétele, hogy egy próbálkozásban legyen meg a legalább 12 teljesen helyes item ÉS a helyes Q13 (`LMS – activity manifest.md` LMS-M7-09); a „Highest grade” szerinti próbálkozásban a Q13 hibás is lehet (runtime acceptance 19. pont).`

A7 | RÉSZBEN | ERT-5 (G7) | A négy kérdés:
(i) Igaz. A 14 M7-item mindegyikének egyetlen „Visszajelzés” bekezdése kimondja a kulcsot (például Q1 :72), opciónkénti visszajelzés nincs. A KAPU:51/:415 és a MAN:18/:102 tehát nem létező elemet tilt, a kulcsot közlő általános visszajelzést nem.
(ii) Az általános visszajelzés elrejtése az ERT-5 („ne jelenjen meg a helyes kulcs … a javító lezárása előtt”) közvetlen következménye, és szó szerint egyezik az M3 KAPU:35-tel. Ez a rész zárható. A Moodle-ablakmátrix nem zárható: a „Maximum marks/Marks = Yes”, a „Whether correct = No”, az „After close” és a felhasználói zárási idő invariánsa, valamint az RA 19. pont új alpontja összefonódik a D1-gyel (hogyan látszik a hibázott kompetencia, The attempt be vagy ki) és a D2-vel (zárási mechanizmus). Ez build-spec döntés: build-spec gazda + értékelési felelős, a dátumoknál a programvezető. Ráadásul a kutató maga is forráskódból következtette, célverzión nincs igazolva. A tesztlépés tartalma a mátrixtól függ, ezért döntés előtt nem írható be.
(iii) A QUIZ-M általános visszajelzés-bővítése az M3-on nem változtat, mert az M3 KAPU:35 már így szól.
(iv) A D1 és a D2 valóban külön emberi döntés; az RT-P0-19/08 bizonyíték-kapu (G3b).
Zárható OLD → NEW:
(1) KAPU:51 `a helyes választ és a teljes, opciónkénti visszajelzést csak a javító próbálkozás lezárása után.` → `a helyes választ, a teljes, opciónkénti visszajelzést és az itemenkénti tanulói (általános) visszajelzést csak a javító próbálkozás lezárása után.`
(2) KAPU:415 `a helyes válasz és a teljes, opciónkénti visszajelzés csak a javító próbálkozás lezárása után;` → `a helyes válasz, a teljes, opciónkénti visszajelzés és az itemenkénti tanulói (általános) visszajelzés csak a javító próbálkozás lezárása után;`
(3) MAN:18 `a helyes kulcs és a teljes, opciónkénti visszajelzés csak a javító próbálkozás lezárása után;` → `a helyes kulcs, a teljes, opciónkénti visszajelzés és az itemenkénti tanulói (általános) visszajelzés csak a javító próbálkozás lezárása után;`
(4) MAN:102 `a helyes válasz és az opciónkénti visszajelzés csak a javító próbálkozás lezárása után (ERT-5;` → `a helyes válasz, a teljes, opciónkénti visszajelzés és az itemenkénti tanulói (általános) visszajelzés csak a javító próbálkozás lezárása után (ERT-5;`
Az ablakmátrix, az „After close” invariáns és az RA alpont EMBERI DÖNTÉS (D1/D2), utána bizonyíték-kapu.

A8 | NEM ELLENŐRIZVE | GYV-1 (M2:QA14-BIZT-5) | Hiányzik: a HUM:220 24 órás döntés, a KAPU:24 és a döntési csomag :211 visszaolvasása, és az, hogy a GYV-1 kérdése tényleg csak a biztonsági átolvasásról szól-e. A GYV-1 szövege (HUM:624) az LMS-M2-05-nél határidős átnézést csak bizonyított szolgálati rend és SLA esetén enged, ezért a „MÁR RENDBEN” kétes. Gyermekvédelmi tétel: bizonytalanság esetén EMBERI DÖNTÉS.

A9 | NEM ELLENŐRIZVE | GYV-15 (M3:QA14-BIZT-1) | Csak a kutató blokkját olvastam. Hiányzik: az M3.3 :546/:547/:554 visszaolvasása, a döntési csomag :337 szó szerinti listája, valamint az M3 KAPU :243/:248 (ITEM 9). A GYV-15 szövege (HUM:638, „önsértési eseteknél”) a kutató hatókör-érvelésével összhangban van, de a helyeket nem ellenőriztem.

A10 | NEM ELLENŐRIZVE (részben) | GYV-2, GYV-6, LMS-3, ADV-3, JOG-1 | JOG-1 / M3:BIZT-G1-8: a hub :42-ben a feltétel nélküli rész (az ideiglenes szervezeti rend) ma nincs benne, csak az A5 hozzáadó szerkesztése után lesz. Előtte tehát nem tiszta bizonyíték-kapu; utána a jogászi ellenőrzés, a kijelölt felnőtt és a Memuna-jóváhagyás G1-bizonyíték. Az M5:IMPL-G2-2 (M5.3 :529/:531/:544, MAN:85, RA 4. pont), az M4:BIZT-G1-2 (M4.1:1206, M4.3:650, MAN:70/:74) és az M3:PED-G2-1 + M4:BIZT-G2-10 (Memuna G1, RA 9. pont) visszaolvasása hiányzik. Csak a döntési szövegeket vetettem össze (HUM:625, :629, :649, :740): az LMS-3 és az ADV-3 `F` óvatos alapértelmezése a kutatói idézetek szerint bent van, de ezt a fájlban nem ellenőriztem.

Összesítő: 4 MEGERŐSÍTVE (A1, A2, A3, A4, A6; ebből A1, A4 és A6 pontosított NEW-val), 2 RÉSZBEN (A5, A7), 0 ELVETVE, 3 NEM ELLENŐRIZVE (A8, A9, A10). Az A5 cserés változata és az A7 ablakmátrixa nem implementálható. Duplikátum: az A5 és az A10 JOG-1 része ugyanarra a hub :42-re vonatkozik; a szerkesztés az A5-ben marad, a bizonyíték-kapu az A10-ben.

HÁTRAVAN: A8, A9, A10

Hivatkozott fájlok:
- 02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md
- 02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md
- 02 Tervezet/Média-assetek/_legacy/legacy-dispositions.json
- tools/test_media_manifest.py
- 02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md
- 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/Modulok/M2/Peulák/M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md
- 02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md

## VB – Verifier B (B1–B9)

## Verdikt-sorok (B1–B9)

Kilenc tételből 5 MEGERŐSÍTVE (B1, B2, B6, B8, B9), 1 RÉSZBEN (B5), 3 ELVETVE (B3, B4, B7). Az ELVETVE mindhárom esetben azt jelenti, hogy a javasolt lezárás nem igazolt, a tétel nyitott emberi döntés marad. A B5 egyik eleme (`RELEASE-READINESS.md` G2) NEM ELLENŐRIZVE. Fájlt nem módosítottam.

**B1 | MEGERŐSÍTVE | ADV-1 (KANON:QA14-BIZT-1, :115-ös cella)**
- A cella szövege most „nincs rögzítve: DPO-kérdés (BIZT-5)”. Ez a fájlban egyszer fordul elő, a H5P-C sorában.
- Ugyanebben a fájlban a :109 szerint az ADV-1 kiterjedéséről a projektgazda dönt, a DPO csak vétó/QA. A :104 és a :232 már „nyitott: az ADV-1 kiterjedése” alakú.
- A HUM 14. szakasz jobb oszlopa vétó/QA-szerepeket ad, döntéshozót nem. A „DPO-kérdés” címke tehát belső ellentmondás.
- A „nincs rögzítve” megmarad, szigorítás nincs, új szabály nincs.
- `nincs rögzítve: DPO-kérdés (BIZT-5)` → `nincs rögzítve; nyitott: az ADV-1 kiterjedése (BIZT-5)`

**B2 | MEGERŐSÍTVE | ADV-1 (RT 15. pont, ASSIGN-S/M tesztlépés)**
- Az OLD `1. szakasz 2. pont).` a fájlban egyedi (1 találat, a :86 végén).
- HUM :647, ADV-1: „mentor csak saját csoportjának lássa a beadást”. Az ADV :104 előírja: „a csoportmód beállítását stagingben vissza kell olvasni”. A tesztlépés ennek közvetlen átvezetése; a GATE-CP helyesen kimarad.
- A csoportba nem sorolt mentor negatív esete a döntésből következik: saját csoportja nincs, tehát semmit nem láthat.
- Kulcs, küszöb és completion nem változik; nem tanulói szöveg.
- Az OLD → NEW a kutatói szöveg szerint használható. Egy pontosítás ajánlott, mert csoport nélküli fióknál a „más csoporthoz” kétértelmű: „…és hogy csoportba nem sorolt mentorfiók sem lát más csoporthoz tartozó beadást” helyett „…és hogy egy csoportba nem sorolt mentorfiók egyik tanulói csoport beadását sem látja”. A NEW többi része változatlan.

**B3 | ELVETVE (a KANON:QA14-BIZT-5 EMBERI DÖNTÉS marad) | ADV-12**
- A §3 hiánya valós: az ADV :58 szerint a jogalap és a megőrzés helye a §3 tábla, és abban nincs AI-sor.
- A javasolt pont viszont nem szó szerinti átvezetés. Új besorolást tesz: az AI-végpont metaadatát felveszi a tanulói adatok „Külön review” listájába. A GYV-10/LMS-8 alatt a promptot a képző küldi, így nem igazolt, hogy ez tanulói adat.
- A „nyitott (ADV-12)” jelölés a lezárt ADV-12-t nyitottnak mutatná.
- A szabályt a §7 :183 már szó szerint tartalmazza; a jogalap és az időtartam a DPO / jogi felelős kérdése.
- Adatvédelmi kétségben nem szerkesztünk.

**B4 | ELVETVE (a CANON:QA-BIZT-3 (b) EMBERI DÖNTÉS marad) | GYV-10, LMS-8**
- Az ADV :264 idézete egyezik a fájllal.
- A korábbi verifier (kánoni kör, bdb94ab, :249–250) kifejezetten úgy hagyta nyitva, hogy a szöveg legyen „összhangban … az M7 tanulói szövegeivel”. Az M7-es formulát tehát figyelembe vette, nem új érv.
- A 125/125-ös lefedettségi jelentés (:258, :337) az f6e9c6e után is emberi döntésként vezeti.
- Az M7 célzott QA a formulát az M7-ben validálta, nem az adatvédelmi tájékoztatóban. A tájékoztató DPO-kapus (:232), és a kiegészítés eltérne a §7 :194 kanonikus HUM-PRIV-04-es tanulói szövegétől.
- AI- és adatvédelmi kétség, ezért emberi döntés: programvezető + Moodle-adminisztrátor, vétó/QA a DPO.

**B5 | RÉSZBEN | ADV-5 (M7:BIZT-G1-6 (a))**

Megerősítve:
- A mondat szó szerint az M7.4:310-ből jön: „ha nem szeretnéd a sajátodat leírni, semleges vagy kitalált érték is jó”.
- A ZDR M7.1:236 és az M7.4:487–488 sora is @source-blokkon kívül van; az OLD-ok egyediek az M7-ben.
- Ugyanazt a mezőt (LMS-M7-10, M7.1:526) az f6e9c6e már ADV-5 szerint átvezette és a QA validálta, tehát nem új alkalmazási eset.
- A manifest-kiegészítés szó szerint követi a már bent lévő LMS-M2-07 mintát (MAN :59).

Végleges szerkesztések:
- M7.1: `Így a célod tényleg a te iránytűdhöz kapcsolódik.` → `Így a célod tényleg a te iránytűdhöz kapcsolódik. Ha nem szeretnéd a sajátodat leírni, semleges vagy kitalált érték is jó.`
- M7.4: `peulája lesz, hanem a tiéd.*` → `peulája lesz, hanem a tiéd. Ha nem szeretnéd a sajátodat leírni, semleges vagy kitalált érték is jó.*`
- MAN :95: a kutató OLD → NEW-ja változatlanul.
- Látható szöveg változik, ezért pin kell.

NEM ELLENŐRIZVE: a `RELEASE-READINESS.md:25` (G2) kiegészítése.
- Az LMS-M2-07 precedens az ADV-5-tel összhangban lévő irányt mutat.
- Nem néztem meg, hogy az ADV-5 GDPR 9. cikkes bizonyíték-kapuja nincs-e már bent az RR-ben a HUM 14 alatti 16 bizonyíték-bejegyzés között. Ha bent van, a kiegészítés duplikátum.
- Addig ne implementáljátok. Ha az RR marad változatlan, a manifest NEW végéről a „(`RELEASE-READINESS.md` G2)” hivatkozás is maradhat, mert az LMS-M2-07 sor ugyanígy hivatkozik.

**B6 | MEGERŐSÍTVE | PRG-5 (M6.F, M7.F)**
- HUM :725, PRG-5: „Minden kötelező F-peulához … Hiányzásnál dokumentált pótidőpont vagy jóváhagyott, rövid egyéni mentoros út legyen, mindig a javító próbálkozás előtt; 1:1 kiskorúval csak a meglévő HUM-SAFE-02 kivétel szerint.”
- Mindkét F-peula kötelező: M6.F:40 „Mivel az M6 kapuja éles, a peula ilyenkor **kötelező**”, M7.F:35 „**kötelező annak, akinek az M7 éles kapuja nem teljesült**”.
- A NEW az M3.F:45 szó szerinti mondata. A kapacitás-mondat benne van, a gyermekvédelmi kikötés nem gyengül.
- Az M6.F-ben a „javító leadás” a fájl saját terminusa.
- Completion nem változik: a javítót a fájlok szerint „a képző nyitja meg, vagy az F-peula jelenléti completionje a feltétele”.
- Mindkét OLD egyezik és egyedi; a kutató két OLD → NEW-ja változatlanul használható.

**B7 | ELVETVE (a „MÁR RENDBEN” nem áll; EMBERI DÖNTÉS marad: Memuna, DPO-vétó) | GYV-1**
- A GYV-1 (HUM :624): „Az LMS-M2-05 kapubeadványon csak akkor **maradjon** határidős átnézés, ha … SLA bizonyított”.
- A „maradjon” egy meglévő átnézésre utal. Az LMS-M2-05-nek ma egyetlen határidős mentori átnézése van: a KAPU-M2:24 megerősítése, amely az LMS-M2-05 jegyzetének tartalmát nézi.
- A csomag kérdése (:211) is a KAPU:24 mellett kérdez; a „csak az (a) opció új átolvasása” értelmezés vitatható.
- A HUM :220 programszintű 24 órás döntésével való viszony gyermekvédelmi hatóköri kérdés. A korábbi verifier is így ítélte, és nincs új bizonyíték.
- Az akut út (KAPU-M2:203) bent van.

**B8 | MEGERŐSÍTVE („MÁR RENDBEN”) | GYV-15**
- A döntési csomag GYV-15 kérdése (:337) név szerint megnevezi az S3-SAFE dobozt (régi :705, ma :554), és az az önsértés-szcenárióban áll (SLIDE 5, „Vágásnyomok”, :545 „önsértésre utaló jel”). A :554 ma a GYV-15 formuláját hordozza.
- A KAPU ITEM 9 (:235 „otthon bántják”) bántalmazási eset, a GYV-15 („az önsértési eseteknél”) hatókörén kívül esik, így változatlansága a döntéssel összhangban van.
- Ha valaki egységesíteni akarná, az új alkalmazás lenne (Memuna, jogász); nem blokkol. Szerkesztés nincs.

**B9 | MEGERŐSÍTVE („MÁR RENDBEN”) | PRG-1 (M7:NYELV-G3-14)**
- Az M7.A (:65 = :385) és az M7.B (:500, :524 „alaposabb”) rendben.
- Az M7.F-ben a :95 nyitókérdés és a :104 blokkcím eltérése mind a hét F-peulában ugyanaz a sablon: közös blokkcím „Hol tartok, miben kérek segítséget?”, modulonkénti nyitókérdés. Ellenőrizve: M1.F 115/124, M2.F 92/101, M3.F 106/118, M4.F 86/95, M5.F 95/104, M6.F 149/158.
- A validált finding M7.F-javaslatát a verifier eleve használhatatlannak ítélte. Szerkesztés nincs; a ledgerbe korpusz-sablonként, változtatás nélkül zárandó.

## Részletek

- **B1:** a QUIZ- és GATE-CP-cellák semleges „nincs rögzítve (BIZT-5)” alakja maradhat.
- **B3:** a KANON:QA14-BIZT-5 fő kérdése (jogalap, megőrzési idő, a szolgáltatói napló harmadik félként) a DPO / jogi felelős elé tartozik; a repo nem dönti el.
- **B4:** ha a projektgazda mégis átvezetné, a §7 :194 tanulói szövegét is vele együtt kell igazítani.
- **B5, NEM ELLENŐRIZVE rész:** még hiányzik az RR teljes átnézése (a G2 és a HUM 14 alatti 16 bizonyíték-bejegyzés), hogy kiderüljön, van-e már ADV-5 / GDPR 9. cikk tétel.
- **B6:** az M7.F-ben az új sor alpontként a :36 elé kerül, ugyanazzal a behúzással.

Hivatkozott fájlok:
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- 02 Tervezet/LMS – H5P runtime acceptance.md
- 02 Tervezet/LMS – activity manifest.md
- 02 Tervezet/RELEASE-READINESS.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md (14. szakasz, :601–:745)
- 02 Tervezet/Modulok/M7/Online leckék/M7.1 – Ez még csak vágy, nem cél – SMART nevelési cél someres módra.md
- 02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md
- 02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md
- 02 Tervezet/Modulok/M7/Peulák/M7.F – Felzárkóztató peula – Peula & Zmán Kvucá (Study Lab).md
- 01 Fejlesztés/04 Audit/2026-10-12 Célzott QA – kánoni kör (bdb94ab), AP-2026-10-12-01.md
- 01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md

## VC – Verifier C (C1–C11)

C1 | BIZONYÍTÉK-KAPU | M3:PED-G2-1, M4:BIZT-G2-10 | A GYV-2 az M3/M4-re csak ezt írja elő: „M3/M4-es kör Memuna- és completion-QA”. A completion-kérdésre az ERT-1 felel, és a passz bent van: M3.4:12 „a kapus belépő ennek a leckének a completionje”, M3.4:63 „Mondhatsz passzt”. A GYV-6 feltétel nélküli része is bent van: M4.B:63 „A szereplési szorongás önmagában nem gyermekvédelmi krízis, de bárki bármikor megállhat és passzolhat”, mellette a GK §4:63–64 minimuma („felkavart kiskorút nem küldünk ki egyedül…”). Hiányzik: a Memuna G1-verdiktje (GYV-24, a GYV-6 küszöb-jóváhagyása) és az RA 9. pont negatív tesztje (G3b, LMS-gazda). Ha a Memuna alternatív feladatot vagy körönkénti passz-bejelentést kér, a tétel REOPENED.
C2 | BIZONYÍTÉK-KAPU | M5:IMPL-G2-2 | Az óvatos alapértelmezés bent van. M5.3:529: „beviteli elem nem épül hozzá … Üres Course Presentationre hamis „Rec[eive a grade]”…”; M5.3:544: „itt nem kell beírnod sehova”; MAN:85: „a végleges completiont a valós H5P és ennek a sornak a tesztje dönti el (LMS-3; runtime acceptance 4. pont)”. Az LMS-3 maga mondja ki, hogy a profilról a teszt dönt, ezért a nyitott „CP vagy Moodle-oldal” választás nem tartalmi döntés. Kapu: G3b (RA 4.: „Mindkét úton tesztelni kell a completiont”); igazol: az LMS-gazda és a módszertani lektor vagy tananyagfelelős.
C3 | BIZONYÍTÉK-KAPU | M4:BIZT-G1-2 | Az ADV-3 alapértelmezett ága („ha … tárolt marad, a tanulói ígéret legyen igaz és a DPO írja alá az adatkört”) teljesül. A tárolt TEXT-C marad (MAN:70, :74). Az ígéret igaz: M4.1:1206 és M4.3:650 „…technikai okból a Moodle rendszergazdája is hozzáférhet”. Hiányzik a DPO adatkör-aláírása (G2, ADV-E1). A narrációs maradék (M4.1:1199, M4.3:644 „magadnak”) a C11-gyel azonos.
C4 | RÉSZBEN | M3:BIZT-G1-8 | Előfeltétel: a hub :42-ben az olvasáskor még a régi szöveg állt („…a külső jelzés jogi kérdésében jogi szakértő dönt.”), a JOG-1 hozzáadó mondata még nem volt benne. Úgy ítéltem, mintha a hozzáadó változat bent lenne; ennek a jogászi tagmondatot meg kell tartania (out-VA A5). A JOG-1 többi feltétel nélküli része bent van: a :41 Btk. 209/A-mondata, a :42 „4. Azonnal vond be a kijelölt Memunát – … helyettesét” lépése, és a korpuszban sehol nincs „munkanap”-határidő. Bizonyíték-kapu (G1): a jogász ellenőrzése (Gyvt. 17. § címzettek és határidők) és a Memuna jóváhagyása; a kijelölt felnőtt megnevezése szervezeti aktus, nem repótartalom. Nyitott emberi döntés marad (kicsi, nem tartalmi): a JOG-1 sora szerint „a nyilvántartás helyéről a projektgazda” dönt (G1 #1 issue vagy új HUM-sor); erről a repóban nem találtam döntést.
C5 | RÉSZBEN | M3:BIZT-G1-5, M3:BIZT-G2-7 | A mostani blokk a runtime-visszaolvasás: G3b, RT-2 és RA 15, LMS-gazda. Az ADV-4 azonban csak a visszaolvasás utánra halasztja a döntést („…visszaolvasása után dönthető el a tárolásmentes technika”), ezért utána valódi technikaválasztás jön (DPO, az M3-nál a Memuna is), nem puszta bizonyíték. Mindkét finding láthatósági alrésze (BIZT-5) ráadásul az ADV-1 H5P-C-re való kiterjedése, ami nyitott projektgazdai döntés. Ezt az Adatvédelem :104 és :109 („a döntés kiterjedéséről a projektgazda dönt”) és a :115 is így jelöli; azonos a KANON:QA14-BIZT-1-gyel. Pontosítás: az M3.3:96 csak ennyit tartalmaz: „Enable attempt tracking” = Yes. Az ADV-4 halasztása az Adatvédelem :115-ben és az M3.4:95-ben áll, az M3.3-ban nem.
C6 | BIZONYÍTÉK-KAPU | M3:BIZT-G2-5, M3:BIZT-G3-8 | Az ADV-2 alapértelmezése szó szerint bent van. M3.4:67: „…egy második vagy fellebbezési értékelő csak konkrét eljárásnál láthatja …, a Memuna pedig csak szükség esetén”. M3.F:3: „csak összesített vagy minimális hiánylistát lát … az F-peula szereposztását és a vészhozzáférést dokumentálni kell (ADV-2)”. M3.4:772 (nem :801): „Google Doc csak szervezeti fiókkal, adatfeldolgozói és hozzáférési felülvizsgálat után (ADV-10)”. Hiányzik: a programvezető dokumentációja (szereposztás, vészhozzáférés, a szervezeti fiók megléte), a DPO G2-je (ADV-E1/E2), és a csoport-hozzáférési teszt (RT-P0-15 és RA 15, LMS-gazda). A BIZT-G3-8 kérdésére („hozzáférhet-e nem mentor képző”) az ADV-2 felel, így nem marad tartalmi döntés.
C7 | BIZONYÍTÉK-KAPU | M1:BIZT-G2-4, M2:BIZT-G2-3, az M2:BIZT-G1-6 hozzáférési része | Az ADV-1 feltétel nélküli része bent van: M1.4:510, M2.2:499 és M2 KAPU:203 „…technikai okból a Moodle rendszergazdája is hozzáférhet”. Az érintett activityk mind az ADV-1 eldöntött hatókörében vannak: az LMS-M1-05 és az LMS-M2-05 ASSIGN, az LMS-M2-08 TEXT-C (Adatvédelem :104). Hiányzik a staging role-matrix (G2 POST-BUILD, RT-P0-15; LMS-gazda, DPO); utána a „csak a kijelölt mentorod” fordulat a tényleges szerkesztő tanári és menedzseri szerephez igazodik. Ez közvetlen következmény, nem döntés. Az M2:BIZT-G1-6 megőrzési és névmező-része EMBERI DÖNTÉS marad (DPO).
C8 | BIZONYÍTÉK-KAPU | M7:IMPL-G2-12 | A (b)–(d) alt bent van (M7.4:245, M7.3:535, M7.4:365). Az (a) helyén az M7.2:404 részletes altja áll, a Program terv :221 rövid altja nincs bent. Az LMS-7 feltétele („Az akadálymentességi felelős ellenőrizze…”) szakértői QA-verdikt, nem tartalmi választás; addig a részletes alt az óvatos alapértelmezés. Kapu: G5a/G5b (FINAL_RELEASE_QA), hozzáférhetőségi gazda.
C9 | BIZONYÍTÉK-KAPU | M4:BIZT-G1-7 | A jelölési ígéret feltételes: M4.3:22, M4.2:23, M4.4:29, a hub :16, M4.A:14, M4.B:14 („ahol generatív AI-t használtunk …, azt … jelöljük”). Tanulói címke nincs; a „provenance_note”: „AI-generált” mezők csak média-asset metaadatok. A PRG-14 a) ténybizonyítékot kér („csak szerzői/provenance bizonyíték alapján”), ami a szerző vagy tananyagfelelős írásos nyilatkozata, nem döntés. A RELEASE-READINESS-ben erre nincs G-sor, ezért a ledgerben bizonyíték-függésként kell rögzíteni (a legközelebbi a G2, tracker #2).
C10 | BIZONYÍTÉK-KAPU (SIGNOFF, nem G1–G8) | M2:PED-G1-11 | Az ERT-19 tartalma eldőlt („az „ÉN” a középpont, a „legalább 3 kör” … három további réteg”). A feltétel szerepköri aláírás: „a modulgazda/értékelési felelős által aláíratni kell”. Az értékelési felelős a vétó-oszlopban áll, így ez a definíció szerinti bizonyíték-kapu; elutasítás esetén REOPENED. A C-csomag többi tételétől eltérően itt még semmi nincs átvezetve. M2 KAPU:37 ma is így szól: „legalább 3 identitás-körömet (pl. ÉN–család–…)”, vagyis a teljes átvezetés az aláírásra vár. Az előzetes tájékoztató maga a frissített, előre publikált követelmény, és visszamenőleges hatás nincs. Ezért ez nem új tartalmi döntés, de a ledgerben SIGNOFF / hatálybalépési feltételként álljon, ne G-kapuként.
C11 | BIZONYÍTÉK-KAPU (helyesen: VO_PACK-függőség) | M1:QA14-BIZT-1, M4:QA14-BIZT-4 | Igaz, hogy kurzusoldalon nincs több javítandó. Kész: M1.3:837 „(kitalált, életszerű helyzet)”, :885 „Valós helyzetet – név nélkül sem – ne írj le”, MAN:48 „ide csak kitalált, életszerű helyzet kerülhet (… ERT-12 …)”, hub :116 „(csak kitalált)”, M4.1:1182, M4.3:625–628. A „régi” mondat csak a narrációs `@source` blokkokban maradt: M1.3:901 „Gondolj egy helyzetre, ami eszedbe jut” (NAR-05-VO), M4.1:1199 és M4.3:644 „Most írd le magadnak…” (NAR-07-VO, NAR-03-VO); máshol egyik sincs meg. Ez nem szerepköri bizonyíték és nem emberi döntés, hanem a VO-1 szerinti külső hanggyártási fix pack (médiafelelős vagy VO-gazda; DPO-vétó). A pack beérkezéséig a `@source`-ból épülő leirat is a régi mondatot mutatja, ezért ez nyitott release-blokkoló, nem FIXED.

Összesítés: 7 BIZONYÍTÉK-KAPU (C1, C2, C3, C6, C7, C8, C9), 2 minősített BIZONYÍTÉK-KAPU (C10: SIGNOFF, C11: VO_PACK), 2 RÉSZBEN (C4, C5), 0 EMBERI DÖNTÉS MARAD teljes egészében.

Átfedések:
- C3 narrációs része = C11 M4:QA14-BIZT-4 (M4.1:1199, M4.3:644). A VO-rész a C11-ben marad, a C3-ban csak a DPO G2.
- A C5 BIZT-5 láthatósági alrésze és a C7-ből kizárt hozzáférési kiterjedés ugyanaz a nyitott döntés (KANON:QA14-BIZT-1, az ADV-1 kiterjedése; projektgazda).
- C4 = out-VA A5/A10 JOG-1 része. A szerkesztés az A5-ben, a bizonyíték-kapu itt.

Részletek, amelyekre a fő sessionnek figyelnie kell:
- C4: a :42 hozzáadó mondata az olvasáskor még nem volt bent. Ha bekerül, csak a hozzáadó változat (A5) elfogadható; a „jogi szakértő dönt” tagmondat nem törölhető. A tracker helyéről szóló döntést külön, kis projektgazdai tételként kell rögzíteni.
- C5: a ledgerben EVIDENCE_GATE csak akkor álljon, ha mellette függő emberi lépésként szerepel a visszaolvasás utáni technikaválasztás (DPO, Memuna) és az ADV-1 H5P-C-kiterjedés (projektgazda).
- C6: az M3.4 ADV-10-sora ma a :772-n áll, nem a :801-en.

Hivatkozott fájlok:
- 02 Tervezet/Emberi jóváhagyás szükséges.md (14. szakasz: :625, :629, :647–650, :656, :662, :671, :682, :689, :734, :740, :744, :746, :750–769)
- 02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md (:41–42)
- 02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md (:12, :33, :63, :67, :95, :772)
- 02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md (:96)
- 02 Tervezet/Modulok/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyermekvédelem (Study Lab).md (:3, :184)
- 02 Tervezet/Modulok/M4/Peulák/M4.B – Mit és hogyan kérdezek – Kérdezés & peulabemutató gyakorlása.md (:63, :326)
- 02 Tervezet/Modulok/M4/Online leckék/M4.1 – Mit üzen a testem – Nonverbális kiállás.md (:1182, :1186–1206)
- 02 Tervezet/Modulok/M4/Online leckék/M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md (:22, :625–650)
- 02 Tervezet/Modulok/M5/Online leckék/M5.3 – Hogyan tanulunk tényleg – Gyakorlás, aktív felidézés, időben elosztott gyakorlás.md (:529, :531, :544)
- 02 Tervezet/Modulok/M7/Online leckék/M7.2 – Nemcsak játék, hanem peula – 11 tervezési pont & AI-támogatás.md (:401–406)
- 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md (:837, :885, :898–901)
- 02 Tervezet/Modulok/M2/M2 – Kapu – értékelő (item-bank + rubrika).md (:37, :203)
- 02 Tervezet/LMS – activity manifest.md (:48, :70, :74, :85)
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md (:104, :109, :115–117)
- 02 Tervezet/RELEASE-READINESS.md (:24–34)
- 02 Tervezet/Program terv.md (:221)

## QA15-bizt – Célzott QA a 3b160fc hunkjaira – biztonság-jog

Célzott QA a 3b160fc négy hunkján (QA15, biztonság-jog lencse, csak olvasás). Két P2-es findingot találtam, mindkettő objektív. P0 és P1 nincs.

**Összkép a három kérdésre**
- **M6.A :182 (GYV-5):** a döntést szó szerint követi. A mondat azonos a `Gyermekvédelem – release gate.md` §4 :65 soráéval. Nincs gyengítés, nincs nyelvi regresszió, nincs finding.
- **M2.A :362 (GYV-19):** szó szerint követi a döntést („a képzőnek és a Memunának a kijelölt úton jelezni kell”). A hunk erősíti a láncot: a Memuna korábban csak a képzőn keresztül került be, most közvetlen címzett. Ez megfelel a §4.1 címzett-szabályának (:82, „A jelzés címzettje gyermekvédelmi ügyben mindig a Memuna”), és a GYV-8 szerint a helyszíni felelőst külön is jelezni kell. A „ne nyomozz, ne kérdezz rá a részletekre” határ megmaradt, nincs finding.
- **M3 hub :42 (JOG-1):** tartalmilag szó szerint követi a döntést. A külső jelzésről „felnőtt” dönt, a madrih nem kap jogi döntési szerepet. Az előző mondat („15–17 éves önkéntes madrihnak [nem kell] önálló jogi minősítést … végeznie”) és az ötlépéses út érintetlen. Nyelvi hiba van benne, lásd QA15-BIZT-2.
- **M1 KAPU :27 (GYV-11):** a megőrzési és pótlási kikötések megmaradtak. Egy minősítő kiesett, lásd QA15-BIZT-1.

---

**M1:QA15-BIZT-1**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:27`
- **Probléma:** az átvezetésből kiesett a döntés „jogosult” minősítője a Memuna-eljárás elől.
- **Bizonyíték:**
  - A HUM :634 GYV-11 sora: „Dokumentált, jogosult Memuna-eljárás, szükség szerinti korlátozás/helyesbítés és adatvédelmileg jóváhagyott törlés/megőrzés kell”.
  - Az M1:27 sora: „a Memuna-eljárást, a szükség szerinti korlátozást vagy helyesbítést és az adatvédelmileg jóváhagyott törlést vagy megőrzést dokumentálni kell”.
  - A Z.4:359 ugyanezt a döntést a minősítővel vezeti át: „dokumentált, jogosult Memuna-eljárás”.
  - Az M1 megfogalmazása szó szerint az `Adatvédelem – tanulói adatok és AI.md:153` sorát másolja, és abból is hiányzik a „jogosult”.
- **Hatás:** a jogosultsági kikötés, vagyis hogy csak arra jogosult személy járhat el, a kapufájlban és a kánoni adatvédelmi dokumentumban nem jelenik meg. A GYV-11 két átvezetése (M1/Adatvédelem, illetve Z.4) eltér egymástól. A „kijelölt Memuna” a sor elején részben pótolja a minősítőt, ezért P2.
- **Javaslat (javítási korlát):** a „jogosult” minősítőt kell visszatenni a GYV-11 szó szerinti szövegéből, közvetlen következményként az `Adatvédelem – tanulói adatok és AI.md:153` azonos mondatában is (pl. „a jogosult Memuna-eljárást, …”). Tilos hozzányúlni a megőrzési, pótlási, incidensnyilvántartási és kapueredmény-kikötéshez. A DPO-jóváhagyás meglétét nem szabad állítani: az bizonyíték-kapu, és már a döntés vétó/QA-oszlopában szerepel.
- **Típus:** objektív

**M3:QA15-BIZT-2**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv (biztonság-jog kontextusban)
- **Hely:** `02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md:42`
- **Probléma:** az új tagmondatban hiányzik a kötelező vessző az „anélkül, hogy” kötőszópárban. A mondat így három pontosvesszős tagmondatból és négy cselekvőből (Memuna, kijelölt felnőtt, jogi szakértő, akut védelem) álló láncot alkot a jelzési szerepek szétválasztásánál.
- **Bizonyíték:** „a szervezet nevében a jogi tanács alapján kijelölt felnőtt dönt a külső jelzésről, anélkül hogy az akut védelem késne; a külső jelzés jogi kérdésében jogi szakértő dönt.” A vesszőhiány a döntési szöveg (HUM :662) betű szerinti átvételéből ered.
- **Hatás:** a helyesírási hiba tanulói vagy képzői szövegben jelenik meg. A túlterhelt mondat nehezíti annak megértését, ki dönt miről; a tartalom egyébként helyes.
- **Javaslat (javítási korlát):** az „anélkül, hogy” vesszőjét pótolni kell. Szükség esetén az új tagmondat külön mondatba vágható, szavai változatlanok maradnak. Tilos megváltoztatni a három szerepet (a Memuna jóváhagyja, ki tesz külső jelzést; a kijelölt felnőtt dönt; jogi kérdésben a jogi szakértő dönt), a „dönt” igéket és az „akut védelem nem késhet” kikötést. Új szerephatár-magyarázatot sem szabad hozzáírni.
- **Típus:** objektív

Fájlok, amelyekre a findingok hivatkoznak:
- `02 Tervezet/Emberi jóváhagyás szükséges.md` (:628, :634, :642, :662)
- `02 Tervezet/Gyermekvédelem – release gate.md` (:65, :82)
- `02 Tervezet/Adatvédelem – tanulói adatok és AI.md` (:153)
- `02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md` (:359)

## QA15-impl – Célzott QA a 3b160fc hunkjaira – implementáció

Célzott ellenőrzés: 3b160fc és 4b188cc. Read-only, csak a megnevezett hunkokat néztem. Két P2 findingot találtam, P0 és P1 nincs.

**Rövid válasz a kérdésekre**
- **(a) LMS-2:**
  - Az M3.4 leckében és az M3 hub M3.4-szakaszában (:130, :137) nem maradt Drag & Drop-út. A hub :65 és :70 sora az M3.1-é, a :84 az M3.2 húzásmentes útja.
  - Drag & Drop már csak az LMS-2-történetként szerepel: az EGY-04 `purpose` és `notes` mezőjében, valamint a ♿ dobozban („Drag & Drop mellékút nincs”).
  - Nem maradt „azonos a húzós verzióval” típusú állítás: a spec, az a11y-mező és a ♿ doboz is tiszta.
  - A diff nem nyúl a kártyákhoz (1–10, a → kulcsok), a Mini True/False ✅-jéhez és a completionhöz.
  - Az a11y-kikötés megmaradt a spec, a `technical` és a ♿ helyen is: húzásmentes út, Tab, majd nyílbillentyűk vagy Szóköz, ≥24px.
  - Nem találtam a kapcsolódó dokumentumokban sem M3.4-es D&D-hivatkozást: manifest LMS-M3-04, M3 KAPU :42, hozzáférhetőségi sztenderd, runtime acceptance.
- **(b) Teszt:** a párcsere nem gyengíti az őrt. Ha az EGY-04 eltűnik, a teszt KeyError-ral bukik. A `decision` és a `pending-human-decision` ellenőrzés most azon az asseten fut, amely a 6–8. kártyát ténylegesen hordozza.
- **(c) ERT-40:** a :53 új mondata tartalmilag egyezik a manifest LMS-M7-09 sorával („egy próbálkozásban ≥12/14 … ÉS a Q13 helyes”, a Highest grade-kitétellel együtt) és a runtime acceptance 19. pontjával. Küszöb, kulcs és próbálkozásszám nem változott.
- **(d) ERT-5:** az új elem a négy helyen szó szerint azonos („az itemenkénti tanulói (általános) visszajelzés”), és egyezik az M3 KAPU :35-tel. Eltérés csak ott van, hogy az M3 „opciószintű”, az M7 „teljes, opciónkénti” szót használ.
  - A szöveg nem ellentmondásos, a mostani szöveg kulcsot nem árul el.
  - Egy megjegyzés a nyitott ablakmátrix-döntéshez, nem finding: hogy a tanuló lássa, melyik kompetenciánál hibázott, ahhoz kérdésenkénti „Whether correct” vagy „Marks” kell. A Multi-Select (Q11/Q14) részpontja ebből részleges kulcs-információt adhat.
  - Forrás: MoodleDocs, Quiz settings (docs.moodle.org/405/en/Quiz_settings). Szó szerint: „Whether correct: Displays whether the students response to each question is correct or incorrect.” és „Marks: Reveals the marks awarded to the student and the grade for the quiz”.
- **(e) Nyelv:** lásd a M7:QA15-ERT-1 findingot.

---

**M3:QA15-IMPL-1**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md:412-413` (EGY-04 `purpose`, `spec`), :425 (`notes`); `tools/test_media_manifest.py:1892` (docstring)
- **Probléma:** Az EGY-03 törlésével az egyetlen megmaradt SLIDE 4 asset, az EGY-04 metaadataiból kiesett két dolog:
  - a tanulási cél: a `purpose` most változásnapló;
  - a visszajelzés-szövegek forrásmutatója. A régi EGY-04 spec a visszajelzést „azonos a húzós verzióval” hivatkozással definiálta, a forrást pedig csak az EGY-03 spec nevezte meg. Ma a spec csak annyit mond: „válaszonkénti visszajelzéssel (`chosenFeedback`)”.
- **Bizonyíték:** most: `"purpose": "LMS a11y-sztenderd: a besorolás húzás nélkül teljesíthető; a Drag & Drop mellékút az LMS-2 döntéssel kikerült."` — a törölt EGY-03-ban: `Per-kártya visszajelzés-szövegek az 5., 6., 7., 8., 10. kártyához („Visszajelzés minták”) + instrukció („Instrukció”).`
- **Hatás:**
  - Aki a regiszterből (assetek.csv) gyárt, a SLIDE 4 egyetlen interakciójához nem kap tanulási célt.
  - Nem tudja, mely szövegek a `chosenFeedback` forrásai, és hogy az 1–4. és a 9. kártyához nincs szerzői visszajelzés.
  - A legacy-diszpozíció állítása („a visszajelzések az M3.4-EGY-04-ben változatlanok”) spec-szinten nem követhető vissza.
  - Mellékesen: a `notes` „vétó esetén a `decision` mező visszakerül” mondata és a docstring „goes back on both assets” fordulata olyan mezőre utal, amely az EGY-04-en sosem volt.
- **Javaslat:**
  - Az EGY-04 `purpose` mezőjébe az EGY-03 tanulási célja kerüljön, az „activity completion” kitétel nélkül, mert a completion a CP összefoglaló diája. Javasolt szöveg: „Annak aktív gyakorlása, mit tegyél és mit ne, életszerű helyzetekkel, húzás nélkül teljesíthető formában (LMS a11y-sztenderd).” Az LMS-2-történet maradjon a `notes`-ban.
  - A `spec` kapja vissza az EGY-03 forrásmutatóját: 10 kártya a „Kártyák (ajánlott készlet)” részből, helyes besorolással; visszajelzés-szövegek az 5., 6., 7., 8. és 10. kártyához a „Visszajelzés minták” részből; „Instrukció”.
  - A `notes`-ban „visszakerül” helyett „bekerül”; a docstringben „goes back on” helyett „goes on”.
  - Tilos hozzányúlni: a kártyákhoz, a kulcsokhoz, a meglévő visszajelzés-szövegekhez, a completionhöz és az a11y-kikötéshez.
  - Az 1–4. és a 9. kártyához nem szabad új visszajelzést írni, mert az új pedagógiai tartalom lenne.
- **Típus:** objektív
- **Verdikt:**

**M7:QA15-ERT-1**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** implementáció
- **Hely:** `02 Tervezet/LMS – activity manifest.md:102` (LMS-M7-07); a vessző-minta: ugyanott :18 (QUIZ-M), `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md:51` és :415
- **Probléma:** Az ERT-5 bővítése két olvasási hibát hozott a build-utasításba.
  - Az LMS-M7-07 cellájában a „mit lát az első próbálkozás után” és a „mi marad rejtve” csoportot csak egy vessző választja el, ige vagy pontosvessző nélkül.
  - A rejtett listában a „teljes, opciónkénti” vessző miatt „a teljes” önálló listaelemnek olvasható. Ez a minta négy helyen van.
- **Bizonyíték:** „az első próbálkozás után pontszám és a hibázott kompetencia / kritikus követelmény, a helyes válasz, a teljes, opciónkénti visszajelzés és az itemenkénti tanulói (általános) visszajelzés csak a javító próbálkozás lezárása után”
- **Hatás:**
  - A build-felelős ebből a cellából állítja be a Review options-t.
  - Félreolvasva a pontszám és a hibázott kompetencia is rejtve maradhat a javító próbálkozás lezárásáig, vagy egy nem létező „teljes” kategóriát keres.
  - A QUIZ-M sor pontosvesszővel, az M7 KAPU :415 a „látszik” igével választja el a két csoportot; ez a cella eltér tőlük.
- **Javaslat:**
  - A :102 helyen: „az első próbálkozás után pontszám és a hibázott kompetencia / kritikus követelmény látszik; a helyes válasz, a teljes opciónkénti visszajelzés és az itemenkénti tanulói (általános) visszajelzés csak a javító próbálkozás lezárása után”.
  - A :18, :51 és :415 helyen: „teljes, opciónkénti” helyett „teljes opciónkénti”. Ez a HUM 14. szakasz ERT-5 sorának „teljes opció-visszajelzés” szóhasználatához igazodik.
  - Tilos hozzányúlni: az elemkészlethez, az időzítéshez és a Review options ablakmátrixához (külön emberi döntés).
- **Típus:** objektív
- **Verdikt:**

---

Egy megfigyelés a hunkokon kívülről, nem finding: a `02 Tervezet/Média-assetek/PRODUCTION-DECISIONS.md:385-396` HUM-SAFE-04 blokkja még az `M3.4-EGY-03`-at nevezi a döntéstől függő assetnek („a két assetet”). Ez lezárt, datált nyilvántartás és történetileg pontos; a vétó esetére az átadást ma az EGY-04 `notes` mezője és a teszt docstringje rögzíti.

## QA16-bizt – Célzott QA a 958bced+16a9ad9 hunkjaira – biztonság-jog

## QA16-BIZT: biztonság-jog célzott újraellenőrzés (diff-fix2, AP-2026-10-12-02)

3 finding, mindhárom P2. Nincs olyan változtatás, amely törölne vagy gyengítene gyermekvédelmi, adatvédelmi, AI- vagy a kiskorú madrih szerepére vonatkozó kikötést. Új szakpolitikai szabályt egyik hunk sem talál ki.

---

- **ID:** QA16-BIZT-1
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/LMS – activity manifest.md:95` (LMS-M7-10, utolsó oszlop)
- **Probléma:** Az LMS-M7-10 sorba az ADV-5-ből csak a semleges/kitalált/kihagyható út és a nyitott GDPR 9. cikk került át. Kimaradt az ADV-5 átmeneti kezelési szabálya, és az is, hogy ki a gazdája a nyitott kérdésnek. A minta (LMS-M2-07, ugyanennek a fájlnak az 59. sora) mindkettőt tartalmazza.
- **Bizonyíték:** PROJEKT-DÖNTÉS, HUM 14 ADV-5: „Különleges vagy érzékeny világnézeti információként kezeljük azt a névhez köthető válaszmintát, amely vallási/ideológiai meggyőződésre következtetni enged.” A minta, LMS-M2-07: „(gazdája a DPO/jogi felelős, someres vonatkozásban a projektgazda; ez a HUM-PRIV-01 utólagos ellenőrzése …)”. Az új M7-10 szöveg ezek nélkül zárul: „nyitott: a GDPR 9. cikk szerinti minősítés és kivétel, csak jogi/DPO-jóváhagyással (`RELEASE-READINESS.md` G2)”.
- **Hatás:** A build és a DPO a GDPR-minősítés lezárásáig nem látja a sorban, hogy a tárolt, névhez kötött SMART-cél someres értéke addig is érzékeny adatként kezelendő. Azt sem látja, kié a nyitott kérdés.
- **Javaslat:** A LMS-M2-07 mintájára, szó szerint vedd át az ADV-5 első mondatát a ráillő alakban. Írd hozzá a gazda-zárójelet is („gazdája a DPO/jogi felelős, someres vonatkozásban a projektgazda; ez a HUM-PRIV-01 utólagos ellenőrzése”). Ne nyúlj hozzá: a „nincs” grade-hez, a két „Required” kérdéshez, a M7.1 SLIDE 7 idézethez, a meglévő ADV-5 szöveghez. Ne írj be minősítést vagy jogalapot.
- **Típus:** objektív (egy lezárt tétel szó szerinti átvezetése)
- **Verdikt:**

---

- **ID:** QA16-BIZT-2
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/LMS – activity manifest.md:95` → `02 Tervezet/RELEASE-READINESS.md:25` (G2 sor)
- **Probléma:** Az új LMS-M7-10 szöveg azt mondja, hogy a nyitott GDPR 9. cikkes jogi/DPO-jóváhagyást a G2 kapu tartja nyilván. A G2 sor nyitott DPO-tételei között viszont csak az LMS-Z-06 és az LMS-M2-07 szerepel, az LMS-M7-10 nem.
- **Bizonyíték:** TÉNY (repó), RELEASE-READINESS G2: „nyitott DPO-döntés: az LMS-Z-06 (Z.3 szöveges válaszai) megőrzési sora (BS-D6); az LMS-M2-07 (M2.3 záró mondat) kötelező, név szerinti tárolásának adatkategóriája (BIZT-R5; someres vonatkozásban a projektgazda)”.
- **Hatás:** A DPO/jogi felelős írásos jóváhagyásának hiánya az LMS-M7-10-nél nem jelenik meg a release-kapun. A G2 lezárható úgy, hogy ezt a tételt senki nem nézte meg.
- **Javaslat:** Vedd fel a G2 sor nyitott DPO-listájára az LMS-M7-10-et, az LMS-M2-07 mintájára. Ez a manifest-hivatkozás közvetlen következménye. A DPO/jogi jóváhagyást nem írod be és nem feltételezed. A hiányzó szerepköri bizonyíték a G2-höz és a #2 tracker-issue-hoz tartozik. A G2 többi feltételéhez ne nyúlj.
- **Típus:** bizonyíték-kapu
- **Verdikt:**

---

- **ID:** QA16-BIZT-3
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** biztonság-jog
- **Hely:** `02 Tervezet/LMS – H5P runtime acceptance.md:86` (15. pont, az új utolsó mondat)
- **Probléma:** Az ASSIGN-S/M-re felvett tesztfeltétel két ellenőrzést sorol fel: a mentor csak a saját csoportját látja, a csoport nélküli mentor senkit. A TEXT-C-nél előírt közvetlen URL-es ellenőrzés kimaradt. Az „ugyanígy” szóból nem dönthető el, hogy ez is beleértendő-e.
- **Bizonyíték:** TEXT-C (ugyanebben a pontban): „egyik mentor sem jut közvetlen URL-lel más csoport tanulójának válaszához”. Az új ASSIGN-mondat: „ugyanígy két mentorral és két elkülönített tanulói csoporttal kell visszaolvasni, hogy a mentor az értékelői nézetben csak a saját csoportja beadásait látja, és hogy egy csoportba nem sorolt mentorfiók egyik tanulói csoport beadását sem látja”.
- **Hatás:** Átmehet a teszt úgy, hogy egy másik csoport beadása közvetlen hivatkozással elérhető marad. Ez megsértené az ADV-1-et (PROJEKT-DÖNTÉS: „mentor csak saját csoportjának lássa a beadást”).
- **Javaslat:** Mondd ki az ASSIGN-mondatban a TEXT-C negatív esetének megfelelőjét: egyik mentor sem jut közvetlen URL-lel más csoport tanulójának beadásához. Moodle-specifikus URL-paramétert ne találj ki. Ne nyúlj hozzá: a TEXT-C feltételekhez, a 2026-10-05-ös RT-P0-15 hivatkozáshoz, a BIZT-3 és a BIZT-11 tételhez. Ha a verifier szerint ez a 2026-10-05-ös tesztdöntés új alkalmazási esete, akkor ez kell helyette: EMBERI DÖNTÉS: kiterjed-e az RT-P0-15 közvetlen URL-es feltétele az ASSIGN-S/M-re. Kié: projektgazda, utólagos ellenőrzés a DPO / jogi felelős.
- **Típus:** objektív
- **Verdikt:**

---

### A 10 hunk ellenőrzése

1. **Adatvédelem, H5P-C sor:** a „DPO-kérdés” → „nyitott: az ADV-1 kiterjedése” csere egyezik ugyanennek a fájlnak a 104., 109. és 232. sorával. A 109. sor szerint a projektgazda dönt, a DPO utólag ellenőrzi, tehát a régi címke volt pontatlan. Nincs finding.
2. **Adatvédelem, GYV-11 bekezdés:** a „jogosult” szó szó szerint egyezik a HUM 14 GYV-11 sorával. Semmi nem veszett el. Nincs finding.
3. **Runtime acceptance, 15. pont:** az ASSIGN-tesztfeltétel az ADV-1 közvetlen következménye, és nem töröl semmit. A közvetlen URL-es eset hiányzik (QA16-BIZT-3).
4. **Manifest, LMS-M7-10:** az ADV-5 út átkerült, és egyezik a M7.1 526. sorával (a „kihagyhatod” itt is benne van). Hiányos átvezetés (QA16-BIZT-1), és a G2-hivatkozás nincs a kapun nyilvántartva (QA16-BIZT-2).
5. **M1 kapu, GYV-11 sor:** a „jogosult” beszúrás szó szerint egyezik a HUM 14-gyel. A pilot a next-version ágon nem változik. Nincs finding.
6. **M3 hub, JOG-1 mondat:** csak egy vessző került be („anélkül, hogy”). Ez megengedett írásmód, a tartalom és a szerephatár nem változott. Nincs finding.
7. **M6.F, „Ha valaki nem tud részt venni”:** egyezik a M3.F mintával, a „javító leadás” pedig az M6 saját szóhasználata. A PRG-5 és a HUM-SAFE-02 1:1 korlátja megvan. Nincs finding.
8. **M7.1, R szakasz:** az ADV-5 mondat egyezik a M7.4 310. sorával és a M7.B 457. sorával. A „sajátodat” egyértelműen a someres értékre utal, nyelvi regresszió nincs. Nincs finding.
9. **M7.4, 488. sor:** ugyanez a mondat, ugyanaz a minta. Egyezik a M7 kapu 408. sorával („semleges vagy kitalált someres érték is elfogadott, pontlevonás nélkül”). Nincs finding.
10. **M7.F, „Ha valaki nem tud részt venni”:** egyezik a M3.F mintával, a „javító próbálkozás” az M7 saját szóhasználata, az 1:1 korlát megvan. Nincs finding.

## QA16-impl – Célzott QA a 958bced+16a9ad9 hunkjaira – implementáció

Lencse: implementáció. A vizsgált terület a diff-fix2.txt 9 hunkja (AP-2026-10-12-02). 4 findingot találtam, mindegyik P2. Runtime-, QA- vagy release-bizonyítékot a diff nem állít: az új 15. pontos mondat visszaolvasást ír elő, a „stagingben visszaolvasandó” kitétel megmaradt.

**QA16-IMPL-1**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** implementáció
- **Hely:** 02 Tervezet/LMS – activity manifest.md, LMS-M7-10 sor (új zárórész), valamint 02 Tervezet/RELEASE-READINESS.md:25 (G2)
- **Probléma:** Az új LMS-M7-10 szöveg nyitott GDPR 9. cikk szerinti DPO-tételt jelöl, és a G2-re mutat. A G2 „nyitott DPO-döntés” felsorolásában viszont csak az LMS-Z-06 és az LMS-M2-07 szerepel, az LMS-M7-10 nem. Az LMS-M2-07 mintájából a gazda megnevezése is kimaradt.
- **Bizonyíték:** manifest: „nyitott: a GDPR 9. cikk szerinti minősítés és kivétel, csak jogi/DPO-jóváhagyással (`RELEASE-READINESS.md` G2)”. A G2 sor szövege: „nyitott DPO-döntés: az LMS-Z-06 (…) megőrzési sora (BS-D6); az LMS-M2-07 (M2.3 záró mondat) kötelező, név szerinti tárolásának adatkategóriája”.
- **Hatás:** A G2 kapu lezárásakor az M7.1 SMART-cél R elemének minősítése nem szerepel a nyitott DPO-tételek között. Így DPO-jóváhagyás nélkül csúszhat át.
- **Javaslat:** Vedd fel a G2 „nyitott DPO-döntés” listájába: „az LMS-M7-10 (M7.1 SMART cél R eleme) GDPR 9. cikk szerinti minősítése és kivétele (ADV-5; someres vonatkozásban a projektgazda)”. A manifest-sorban az LMS-M2-07 mintájára egészítsd ki a hivatkozást így: „(gazdája a DPO/jogi felelős, someres vonatkozásban a projektgazda; ez a HUM-PRIV-01 utólagos ellenőrzése, nyilvántartás: `RELEASE-READINESS.md` G2)”. Az ADV-5 tartalmához, a küszöbhöz és a completionhöz nem nyúlsz. Maga a DPO-jóváhagyás bizonyíték-kapu marad, ezt nem írod be.
- **Típus:** objektív
- **Verdikt:**

**QA16-IMPL-2**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:** 02 Tervezet/LMS – H5P runtime acceptance.md > 15. pont, új ASSIGN-S/ASSIGN-M mondat. A hiány helye: LMS – activity manifest.md §1, az ASSIGN-S és ASSIGN-M profilsor (19–20. sor), illetve Adatvédelem – tanulói adatok és AI.md §3, „A mentor-láthatóság mechanizmusa (TEXT-C)” szakasz (125–130. sor).
- **Probléma:** Az új tesztmondat csoportmódon alapuló értékelői szűrést vár el. Azt is elvárja, hogy a csoportba nem sorolt mentorfiók semmit ne lásson. Ehhez a build-specifikáció az Assignmentre nem ír elő beállítást. A „Group mode = Separate groups” és a „mentor csak csoportba sorolás után kap szerepet” szabály csak a TEXT-C-re van rögzítve, az ASSIGN-S/M profil csoportmódot nem említ.
- **Bizonyíték:** Adatvédelem 125. sor: „**A mentor-láthatóság mechanizmusa (TEXT-C).**” 127. sor: „A TEXT-C activity csoportmódja („Group mode”) „Separate groups”…”. Az ASSIGN-S/M profilsorban nincs csoportmód.
- **Moodle-forrás:**
  - A Moodle Docs „Groups FAQ” (4.5/503) cikke szerint: „If this capability is removed from the teacher role (either within a course or globally if appropriate) then they will only see the students they teach when accessing the gradebook for example.”
  - A MoodleDocs dev „Groups access control” oldala szerint: „Teachers without any group membership and access to all groups can not view or display grades of any other user.” Ez az oldal elavult (read-only, utoljára 2021-07-14-én szerkesztették) és a pontkönyvről szól.
  - A `mod/assign` értékelői nézetére vonatkozó elsődleges forrást nem értem el: a tracker (MDL-40367) JavaScript nélkül nem tölt be. A fórumtalálatok szerint ismert eset volt, hogy a csoport nélküli tanár az értékelőtáblában minden tanulót látott. Ezt nem ellenőriztem.
- **Hatás:** A képesség valós (Separate groups mellett, `moodle/site:accessallgroups` nélkül). Ha viszont az építő az Assignmentre nem állít csoportmódot, minden mentor minden P2 beadást lát, ami ellentmond az ADV-1-nek. A csoport nélküli mentor viselkedése az Assignmentnél nincs elsődleges forrással igazolva, ezért a teszt sikere jelenleg csak remény. Ha elbukik, a build-szabály hiányzik.
- **Javaslat:** EMBERI DÖNTÉS (az LMS-gazdának vagy a build-spec gazdának, vétó: DPO / jogi felelős). Döntsenek az ASSIGN-S/M láthatósági mechanizmusáról:
  - Group mode „Separate groups” az Assignmenteken;
  - a mentor a nem szerkesztő tanári szerepet csak csoportba sorolás után kapja, a TEXT-C BIZT-3 mintájára;
  - hogyan fér ehhez hozzá a második értékelő, illetve az F-peula képzője (ADV-2, újraértékelés).

  A döntés után a mechanizmus kerüljön be az ASSIGN-S/M profilsorba és az Adatvédelem §3 mechanizmus-szakaszába. Az ADV-1 egy új alkalmazási esete, ezért nem vezetheted át magadtól.
- **Típus:** emberi-döntés
- **Verdikt:**

**QA16-IMPL-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:** 02 Tervezet/LMS – H5P runtime acceptance.md > 15. pont, új ASSIGN-S/ASSIGN-M mondat
- **Probléma:** Az új mondat „ugyanígy” kezdetű, de a TEXT-C ellenőrzésből csak két esetet visz át: a saját csoport látszik, a csoport nélküli fiók nem lát semmit. Két negatív eset kimaradt. Az egyik, hogy a mentor közvetlen URL-lel sem jut el más csoport tanulójának beadásához. A másik, hogy a tanuló nem látja más tanuló beadását.
- **Bizonyíték:** ugyanez a bekezdés a TEXT-C-nél: „egyik mentor sem jut közvetlen URL-lel más csoport tanulójának válaszához; a tanuló nem látja más tanuló válaszát”. Az ASSIGN-mondat csak ennyit vár el: „csak a saját csoportja beadásait látja, és hogy egy csoportba nem sorolt mentorfiók egyik tanulói csoport beadását sem látja”.
- **Hatás:** Az értékelői felület egyes tanulói nézete URL-paraméterrel is megnyitható. Ha ezt a teszt nem nézi, a csoportszűrés listanézetben átmehet, miközben egyéni nézetben más csoport beadása olvasható. Ez a P2 adatkör ADV-1 szerinti szűkítését sérti.
- **Javaslat:** Egészítsd ki az ASSIGN-mondatot: „…egyik mentor sem jut közvetlen URL-lel más csoport tanulójának beadásához, és a tanuló nem látja más tanuló beadását”. Konkrét URL-paramétert ne írj be elsődleges forrás nélkül. A TEXT-C-feltételek és a 2026-10-05-i döntés szövege nem változik.
- **Típus:** objektív
- **Verdikt:**

**QA16-IMPL-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:** 02 Tervezet/Adatvédelem – tanulói adatok és AI.md:115 (H5P-C sor, „Csoport szerinti szűkítés” oszlop), a 116–117. sorhoz képest
- **Probléma:** A „nyitott: az ADV-1 kiterjedése” jelölés csak a H5P-C sorba került be. A QUIZ-D/M és a GATE-CP sor ugyanerről a nyitott tételről továbbra is csak ezt írja: „nincs rögzítve (BIZT-5)”. A 109. sor mindhárom profilra nyitottnak mondja a kiterjedést.
- **Bizonyíték:** A 109. sor szerint: „A nem beadás jellegű profilok (H5P-C, QUIZ) és a GATE-CP csoport szerinti szűkítése nincs rögzítve: … a döntés kiterjedéséről a projektgazda dönt”. A 116. sorban: „nincs rögzítve (BIZT-5)”.
- **Hatás:** Az építő vagy a DPO a táblából azt olvashatja ki, hogy csak a H5P-C-nél van nyitott ADV-1-kérdés, a QUIZ-nál és a GATE-CP-nél nincs.
- **Javaslat:** A QUIZ-D/M sorban és a 117. sor GATE-CP-részében ugyanez a jelölés álljon: „nincs rögzítve; nyitott: az ADV-1 kiterjedése (BIZT-5)”. A capability-oszlophoz és az ADV-1 tartalmához nem nyúlsz.
- **Típus:** objektív
- **Verdikt:**

**Amit rendben találtam:**
- A manifest LMS-M7-10 sora 12 cellás, `|`-vel zárul, a hozzáadott szövegben nincs új cellaelválasztó. Az Adatvédelem H5P-C sora 5 cellás, szintén lezárt.
- Az Adatvédelem §3 hivatkozás helyes: a „Activity-szintű adatleltár – build-rész (PR-01)” a 3. szakaszban van, a 95. sortól. A `Gyermekvédelem – release gate.md` §4.2 a HUM-SAFE-02 kivételeit tartalmazza.
- Az M6.F és az M7.F új sora a PRG-5-öt és az M3.F/M5.F hivatkozási mintáját követi. A GYV-11 („jogosult Memuna-eljárás”) és a JOG-1 vesszőjavítása a döntés szövegével egyezik.
- Az M7.1 és az M7.4 új mondata egyezik az M7 KAPU 408. sorával és az M7.B-vel. Új azonosító nem keletkezett.

Források:
- [Groups FAQ – MoodleDocs 4.5](https://docs.moodle.org/503/en/Groups_FAQ)
- [Groups access control – MoodleDocs dev (elavult)](https://docs.moodle.org/dev/Groups_access_control)
- [MDL-40367 (nem érhető el JavaScript nélkül)](https://moodle.atlassian.net/browse/MDL-40367)
- [Moodle in English: Moodle 3.1 – Assignment Grader (bug) (csak a találati cím, a tartalmát nem ellenőriztem)](https://moodle.org/mod/forum/discuss.php?d=338038)
