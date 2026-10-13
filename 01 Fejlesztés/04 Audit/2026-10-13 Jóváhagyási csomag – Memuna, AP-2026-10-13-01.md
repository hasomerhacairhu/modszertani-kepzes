# Jóváhagyási csomag – Memuna (és ahol a döntés előírja, a programvezető) (AP-2026-10-13-01)

> **Audit trail, nem kánon.** Előre kitöltött elfogadási javaslat a 2026-10-13-i futásból. A projektgazda irányait a
> `02 Tervezet/Emberi jóváhagyás szükséges.md` 15. szakasz rögzíti; ahol a döntés vagy a jóváhagyás a címzett szerep hatásköre, az irány **nem helyettesíti** az ő
> döntését. A javasolt szövegek tervezetek: a tananyagba csak az írásos elfogadás után kerülnek, `/course-fix`-szel.
> A tervezeteket read-only szakértői ügynökök készítették, a fő session ellenőrizte; a sorszámok a `8bb4d7d` körüli
> állapotra vonatkoznak, átvezetéskor újra ellenőrizzük őket.

Címzett: a Somer gyermekvédelmi felelőse (Memuna), összeférhetetlenség esetén a név szerint kijelölt helyettese; a GYV-5, GYV-6 és GYV-8 tételeknél a programvezetővel együtt.

## Hogyan válaszolj

- Tételenként: **ELFOGADOM** / **MÓDOSÍTOM: …** / **VÉTÓ**, dátummal és szerepnévvel. A repó nyilvános: személynév,
  személyes adat ne kerüljön a válaszba vagy az issue-ba.
- Elfogadásnál a javasolt szöveg (a „DPO tölti ki”, „Memuna dönt” mezők kitöltésével) a következő engedélyezett javítási körben
  kerül be; vétónál a mostani szöveg marad, és az érintett 14. szakaszbeli sor `REOPENED`.
- Az elfogadás nem release-jóváhagyás: a G1–G8 kapuk bizonyítéka és a go/no-go döntés külön lépés (`02 Tervezet/RELEASE-READINESS.md`).
- A válasz helye: a G1 tracker-issue (#1) és a release-jegyzőkönyv (`Program terv.md` §9.3); a GYV-24 „átnéztem” bejegyzés egyazon végleges SHA-ra szól.

## Tételek

| Tétel | Mit kérünk | Kapcsolódó ledger-kulcsok / kapu |
|---|---|---|
| D-05 (sürgős) | a HUM :471 „Segélyvonalak” sor formális újranyitása és a 116-111 / 116-000 új leírása (elsődleges források 2026-10-13) | M3:BIZT-G2-2; X-1 |
| D-01 | egységes peula-megállítási protokoll (GK §4.4 tervezet), peulánkénti kockázati besorolás, létszámnorma (+ programvezető) | M0:QA14-BIZT-2, M2:QA14-BIZT-2, M6:QA14-BIZT-4, M2:BIZT-G3-2, M4:BIZT-G2-9 |
| D-04 | az eszkalációs küszöb és címzett hat helyen; a Z.3 veszélydoboz 112-mondata (+ programvezető) | M6:QA14-BIZT-1, M6:QA14-BIZT-2, M7:QA14-BIZT-6, Z:QA14-BIZT-2, M4:QA14-BIZT-3, M0:BIZT-5, M6:BIZT-G1-1 |
| D-08 (a) | az M2.4 passz-útja egyenértékű, fiktív tudásdemonstrációval (+ programvezető) | M2:QA14-BIZT-4 |
| D-09 | a KAPU-M2:24 24 órás határideje kapuértékelési megerősítés, külön a gyermekvédelmi úttól (DPO vétó/QA) | M2:QA14-BIZT-5 |
| D-10 | a jogosult Memuna-eljárás lépései a feltárást tartalmazó tárolt beadásnál (+ DPO) | M1:QA14-BIZT-5, KANON:QA14-BIZT-4, Z:QA14-BIZT-1, Z:BIZT-G1-2 |
| D-13 (d) | az M2.A csoportnorma: „és felismerhető részlettel sem” (+ DPO) | M2:QA14-BIZT-7 |
| D-07 | biztonságkritikus rubrika- és itemkalibráció (az értékelési felelőssel; szövegek az értékelési csomagban) | M3:QA14-BIZT-2, M6:QA14-BIZT-3, M7:BIZT-G1-2, M7:PED-G2-4 |
| GYV-3 | a hét 1:1 kockázati hely és a SAFE-7 helyenkénti verdiktje | M0:BIZT-3, M2:BIZT-G2-4, M3:BIZT-G1-1, M3:BIZT-G2-3, M3:BIZT-G3-4, M4:BIZT-G2-1 |
| GYV-6, PRG-12, JOG-1, GYV-24 | az M4 küszöb; az M3.B 4. esetkártya reviewja; a JOG-1 jóváhagyás a jogász után; a G1 „átnéztem” | X-1; BK-01, BK-04, BK-12 |
| Vétó/QA (megvalósítva) | D-02 (M6.A keret), D-03 (M3.A/M3.B kártyák), D-08 (b) (M3.3 csomópontcím megterhelő-e), D-12 (M0 belépőkvíz visszajelzés) | HUM 15; 8bb4d7d |

## Részletes javaslatok

### D-05 – a 116-111 és a 116-000 leírása (elsődleges források, kész szövegek)

### A) D-05: a 116-111 és a 116-000 leírása

### Elsődleges források (mind lekérve 2026-10-13-án)

**S1 – kek-vonal.hu/fiataloknak/116-111** (TÉNY)
- „Hívd a 116-111-et, ha jól esne valakivel megosztani, mi jár a fejedben!”
- „A Kék Vonalnál 24 éves korig fogadjuk a hívásokat.”
- „A 116 111-es hívószámon az egész országból, bármelyik vezetékes vagy mobiltelefon hálózatról, éjjel-nappal ingyen hívhatsz minket!”
- Az oldal sehol nem mondja, hogy egy gyerek érdekében telefonáló felnőtt is hívhatja.

**S2 – kek-vonal.hu (főoldal)**
- A 116-111-nél: „Hívj minket, ha beszélgetni szeretnél! Anonim, ingyenes, 0-24.”
- A 116-000-nál: „Hívj minket, ha aggódsz egy gyerekért! Anonim, ingyenes, non-stop.”
- A célcsoportok: „Fiataloknak: 116-111”, „Szülőknek és szakembereknek: 116-000”.

**S3 – kek-vonal.hu/szuloknek/116-000** (szó szerinti kérésre adott kimenet)
- „HÍVJ MINKET, ha aggódsz egy gyerekért!”
- „Beszéld át aggodalmaidat, kérdéseidet, kétségeidet képzett ügyelőinkkel.”
- „Fontos, hogy amennyiben egy gyermek akut és súlyos veszélyben van, személyes ne késlekedj, hívd a 112-es segélyhívó számot!”
- „Amennyiben egy gyermek bántalmazását tapasztalod, vagy sejted, bíztatunk arra, hogy felelős felnőttként Te magad tégy jelzést írásban vagy telefonon a területileg illetékes gyermekjóléti szolgálat felé.”
- Az eszköz szerint az „eltűnt” és a „szökés” szó nem szerepel az oldalon.

**S4 – kek-vonal.hu/szakembereknek/116-000**
- „Szakemberként is konzultálhatsz velünk olyan esetekről, amiben bizonytalan vagy, ami nagyon megterhelő a számodra, vagy amelyben különböző érvek feszülnek egymásnak, hívj minket bizalommal, gondolkozzunk együtt!”

**S5 – kek-vonal.hu/tudastar/116-000-segelyvonal-a-bantalmazott-es-eltunt-gyerekekert-szakembereknek-is** (2023. október 4.)
- „A 116 000 Segélyvonalon várjuk azoknak a felnőtteknek a hívásait, akik aggódnak egy gyermekért, akiknek kérdéseit, kételyeit vannak egy gyerek biztonsága kapcsán, akik bizonytalanok, hogy kihez fordulhatnának segítségért.”
- A „kérdéseit” valószínűleg az eszköz hibája.

**S6 – interaktiv.kek-vonal.hu/…/15-szakmai-szolgaltatasok** (régi oldal, dátum nélkül; ma ezt hivatkozza az M3 KAPU:371)
- 116 111: „…a segítségre szoruló gyerekek, fiatalok számára és olyan felnőttek hívásait is fogadjuk, akik gyerekek érdekében telefonálnak.”
- 116 000: „A Segélyvonalunk az Eltűnt és Bántalmazott Gyerekekért a 116 000-s telefonszámon a szökésben lévő vagy szökést fontolgató gyerekek, fiatalok és gyermekeltűnéssel kapcsolatban segítséget kérő felnőttek hívásait fogadja.”

**S7 – nmhh.hu/cikk/115/A_116_kezdoszamu_harmonizalt_kozerdeku_szolgaltatasok_szamainak_hasznalata_es_kijelolese** („Legutóbb frissítve: 2024. július 11.”)
- 116000: „Eltűnt gyermekek felkutatására fenntartott forróvonal”.
- 116111: „Gyermekek segélyvonala”.
- Mindkettőnél a szolgáltató: „Kék Vonal Gyermekkrízis Alapítvány”.
- Az eszköz percdíjat is visszaadott (vezetékesről 4,37 Ft/perc). Ez ellentmond a Kék Vonal „ingyenes” állításának, és valószínűleg félreolvasás. Nem használtam fel.

**S8 – EUR-Lex, 2007/116/EK határozat, egységes szerkezetben (2023-03-06)**
- 116 000: „Eltűnt gyermekek felkutatására fenntartott forróvonal”, és „Folyamatosan (azaz a nap 24 órájában, a hét minden napján, az ország egész területén) rendelkezésre álló szolgáltatás.”
- 116 111: „Gyermekek segélyvonala”. A feltételsor szövegét nem kaptam meg szó szerint.
- Az Európai Bizottság oldala (digital-strategy.ec.europa.eu/en/policies/116-helplines) 404-es hibát adott.

### Mit mutatnak a források

**TÉNY:** a Kék Vonal két saját oldala ellentmond egymásnak.
- A régi oldal (S6) igazolja a kánon mostani állításait: a 116-111-et a gyerek érdekében telefonáló felnőtt is hívhatja, a 116-000 pedig szökés és eltűnés esetére szól.
- A jelenlegi oldalak (S1–S5) mást mondanak. A 116-111 a fiatalok vonala, 24 éves korig. A 116-000 a gyerekért aggódó felnőttek, a szülők és a szakemberek vonala.
- Emiatt a kánon „nem általános szülői vonal” fordulata ma közvetlenül ellentmond az S3 „Szülőknek” oldalának.

**PROJEKT-DÖNTÉS:**
- A GYV-14 `F` sora szerint a 116 000 az „eltűnt gyermekek vonala”. Ez az NMHH (S7) és az EU (S8) hivatalos szolgáltatásnevét követi, a szolgáltató mai leírásánál viszont szűkebb.
- A HUM:471 a 8. szakasz lezárt sora, a „Projektgazdai döntések HUM-azonosító nélkül (2026-10-02)” alatt. Újranyitását maga a GYV-14 írja elő.

**EMBERI JÓVÁHAGYÁS KELL (Memuna):**
- melyik szolgáltatói leírás az irányadó;
- melyik vonalat ajánljuk a 15–17 éves madrihnak, ha egy hanihért aggódik (a 116-000 felnőtteknek szól);
- rákérdez-e a Memuna közvetlenül a Kék Vonalnál.

### Érintett helyek (Grep a teljes `02 Tervezet/` alatt, a `_build` és a `_legacy` mappa nélkül)

A vitatott fordulatok („gyerek érdekében … felnőtt”, „nem általános szülői vonal”, „24 év alatt”) pontosan ezeken a helyeken állnak:
- GK:46 és :47
- M3.3:709
- M3 KAPU:366, :367 és :370
- M2.4:659
- M3.B:10, ez `@asset` spec, belőle generálódik az `assetek.csv:533`

`@source` blokkban egyik előfordulás sincs:
- M3.3: a `@source` blokkok a :169, :314, :717 és :841 sorban kezdődnek, a :709 tehát nem blokkban áll.
- M2.4: a blokkok a :168, :320, :463 és :797 sorban kezdődnek. A :463-as blokk végét soronként nem ellenőriztem, de a :659 jóval utána áll.
- A VOICE-BIBLE:168 szerint a segélyvonalak a narrációban nem hangzanak el.

Ezek a helyek nem félrevezetők, nem kell változtatni rajtuk: GK:87 és :89, HUM:30, Program terv:251, M3 KAPU:13, M3.B:76 / `assetek.csv:536` („bántalmazott vagy eltűnt gyermek ügyében 116-000”), M3.3:4, :478, :480 és :708, M3 KAPU:62, :148, :153, :158 és :326, M2 KAPU:113, M2.4:209.

### Szövegterv

Minden telefonszám változatlan marad. A számok írásmódja a kánon mostani formája („116-111”, „116-000”).

### D05-1 — GK §3.3: a 116-111 leírása
- Fájl: 02 Tervezet/Gyermekvédelem – release gate.md:46
- Alap: GYV-14 `F`; projektgazdai irány D-05; források: S1, S2, S7
- Hatáskör: SZEREP: Memuna (jóváhagyási feltétel: a HUM:471 formális újranyitása és a Memuna írásos jóváhagyása)
- OLD: `- **116-111**: a Kék Vonal Lelkisegély-vonala gyerekeknek és fiataloknak; gyerek érdekében telefonáló, aggódó felnőtt is hívhatja;`
- NEW: `- **116-111**: a Kék Vonal vonala gyerekeknek és fiataloknak (a szolgáltató szerint 24 éves korig), ingyenes, éjjel-nappal hívható; a hatósági nyilvántartásban „Gyermekek segélyvonala”;`
- Együtt mozgó helyek: D05-3…D05-7
- Címkék: governance/gate-szöveg; nem VO-PACK; nem vétólistás
- Indoklás: A felnőtt hívóra vonatkozó állítást csak a régi oldal (S6) támasztja alá, a mostani oldalak (S1, S2, S5) a felnőtteket a 116-000-ra irányítják. Ez információs állítás, nem védelmi kikötés, ezért a törlése nem gyengíti a védelmet.

### D05-2 — GK §3.3: a 116-000 leírása
- Fájl: 02 Tervezet/Gyermekvédelem – release gate.md:47
- Alap: GYV-14 `F`, GYV-4 `F`; projektgazdai irány D-05; források: S2, S3, S4, S5, S7
- Hatáskör: SZEREP: Memuna (mint D05-1)
- OLD: `- **116-000**: a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért: eltűnt, szökésben lévő vagy szökést fontolgató, illetve bántalmazott gyerek ügyében, felnőttek is hívhatják; nem általános „szülői vonal”;`
- NEW: `- **116-000**: a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért; a szolgáltató jelenlegi leírása szerint a gyerekért aggódó felnőttek – szülők és gyerekekkel foglalkozó szakemberek – vonala (ingyenes, anonim, éjjel-nappal), bántalmazott vagy eltűnt gyerek ügyében is; a hatósági nyilvántartásban „Eltűnt gyermekek felkutatására fenntartott forróvonal”. Ha egy gyerek akut és súlyos veszélyben van, a 112 az út;`
- Együtt mozgó helyek: D05-3…D05-7
- Címkék: governance/gate-szöveg; nem vétólistás
- Indoklás: Az S3 „Szülőknek” oldala közvetlenül cáfolja a „nem általános szülői vonal” fordulatot. A hatósági név (S7) megmarad, így a GYV-14 „eltűnt gyermekek vonala” fordulata is teljesül, a szolgáltató tágabb leírása mellett. A 112-es mondat az S3 saját utasítását veszi át.
- **Választási pont a Memunának:** a D-05 (c) opciója, vagyis a GYV-14 szó szerinti szűk fordulata („116-000: eltűnt gyermekek vonala”) is választható. Kockázata: egy bántalmazás miatt aggódó felnőtt nem ismerné fel, hogy ez az ő vonala.

### D05-3 — GK §7: forrássor
- Fájl: 02 Tervezet/Gyermekvédelem – release gate.md:165
- Alap: GYV-14 („a Kék Vonal és az NMHH aktuális szolgáltatásleírása alapján”)
- Hatáskör: SZEREP: Memuna (ugyanabban a változtatáskészletben)
- OLD: `- **Kék Vonal Gyermekkrízis Alapítvány**, 116-111 és 116-000 aktuális szolgáltatásleírás.`
- NEW: `- **Kék Vonal Gyermekkrízis Alapítvány**, 116-111 és 116-000 aktuális szolgáltatásleírás (kek-vonal.hu/fiataloknak/116-111; kek-vonal.hu/szuloknek/116-000; kek-vonal.hu/szakembereknek/116-000; lekérve: 2026-10-13); **NMHH**, a 116-os harmonizált számok nyilvántartása (nmhh.hu/cikk/115).`
- Együtt mozgó helyek: nincs
- Címkék: governance
- Indoklás: A forrás visszakereshetővé válik. A GK §6:151 release-napi ellenőrzését ez nem helyettesíti.

### D05-4 — M3.3: a 📞 doboz (TANULÓI LÁTHATÓ SZÖVEG)
- Fájl: 02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md:709
- Alap: GYV-14, GYV-4; D-05
- Hatáskör: SZEREP: Memuna (jóváhagyási feltétel: az újranyitás után jóváhagyott leírás; a kiskorú madrihra vonatkozó mondatról külön dönt)
- OLD: `a **116-111 Kék Vonal Lelkisegély-vonal** gyerekek és fiatalok mellett olyan felnőttek hívását is fogadja, akik **egy gyerek érdekében** telefonálnak. A **116-000** a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért: eltűnt, szökésben lévő vagy szökést fontolgató, illetve bántalmazott gyerek ügyében felnőttek is hívhatják, de nem általános szülői vonal.`
- NEW, A változat: `a **116-000** a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért: azoknak a felnőtteknek szól, akik aggódnak egy gyerekért – szülőknek és gyerekekkel foglalkozó szakembereknek is. A **116-111 Kék Vonal** a gyerekek és fiatalok vonala, 24 éves korig.`
- NEW, B változat (az A szöveg, a végén egy plusz mondattal): `Ha 24 éves vagy fiatalabb vagy, és téged is nyomaszt a helyzet, a 116-111-et te is hívhatod.`
- Együtt mozgó helyek: a doboz többi mondata (116-123, 112, „nem helyettesítik a Memuna bevonását”) változatlan. A végén álló „(Forrás: Kék Vonal aktuális szolgáltatásleírás; LESZ 116-123.)” maradhat.
- Címkék: LÁTHATÓ SZÖVEG (pin kell: `--pin-visible "D-05/GYV-14: …"`); nem VO-PACK; nem vétólistás
- Indoklás: A doboz címe („Ha madrihként vagy mentorként aggódsz egy hanihért”) a 15–17 éves madrihot is megszólítja, a 116-000 viszont a szolgáltató szerint felnőtteknek szól. Az, hogy a kiskorú madrih melyik vonalat hívja, új útvonal-szabály, ezért **EMBERI JÓVÁHAGYÁS KELL**. A B változat az S1 „szinte bármiről, ami téged személyesen foglalkoztat” leírására épül, de a Memuna nélkül nem építhető be.

### D05-5 — M3 KAPU: a hívószám-fejléc
- Fájl: 02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md:366
- Alap: GYV-14; D-05
- Hatáskör: SZEREP: Memuna
- OLD: `116-111 Kék Vonal Lelkisegély-vonal gyerekeknek és fiataloknak, valamint gyerek érdekében telefonáló felnőtteknek;`
- NEW: `116-111 Kék Vonal gyerekeknek és fiataloknak (24 éves korig);`
- További csere ugyanezen a soron. OLD: `**116-000 a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért**` → NEW: `**116-000 a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért, a gyerekért aggódó felnőtteknek**`
- Együtt mozgó helyek: :367, :370, :371
- Címkék: képzői/értékelői forrásszakasz. A pin-állapotot nem ellenőriztem, a fő session nézze meg a `--pin-visible` igényét.
- Indoklás: ugyanaz, mint a D05-1-nél és a D05-2-nél.

### D05-6 — M3 KAPU: „A számok szétválasztása” doboz
- Fájl: 02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md:367
- Alap / Hatáskör: mint a D05-5-nél
- OLD: `a **116-111** a Kék Vonal Lelkisegély-vonala gyerekeknek és fiataloknak; **gyerek érdekében telefonáló, aggódó felnőtt** is hívhatja. A **116-000** a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért: eltűnt, szökésben lévő vagy szökést fontolgató, illetve bántalmazott gyerek ügyében hívható, felnőttek is hívhatják; nem általános „szülői vonal”.`
- NEW: `a **116-111** a Kék Vonal vonala gyerekeknek és fiataloknak (24 éves korig). A **116-000** a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért: a szolgáltató leírása szerint a gyerekért aggódó felnőttek – szülők és gyerekekkel foglalkozó szakemberek – vonala, bántalmazott vagy eltűnt gyerek ügyében is.`
- Együtt mozgó helyek: a doboz 116-123-as, 112-es és „belső jelzés” mondata változatlan.
- Címkék: képzői szöveg; a pin-állapot ellenőrizendő

### D05-7 — M3 KAPU: forrássorok
- Fájl: 02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md:370 és :371
- Alap / Hatáskör: mint a D05-5-nél
- OLD (:370): `116-111 (gyermek- és ifjúsági lelkisegély, ingyenes, 0–24, 24 év alatt) – https://kek-vonal.hu/`
- NEW: `116-111 (gyerekeknek és fiataloknak, ingyenes, éjjel-nappal; a szolgáltató szerint 24 éves korig) – https://kek-vonal.hu/fiataloknak/116-111`
- A :371-es sor (a régi interaktiv oldal, S6) helyett vagy mellé:
  - `- Kék Vonal Gyermekkrízis Alapítvány – 116-000, szülőknek és szakembereknek – https://kek-vonal.hu/szuloknek/116-000; https://kek-vonal.hu/szakembereknek/116-000`
  - `- NMHH – a 116-os harmonizált számok nyilvántartása (116000: „Eltűnt gyermekek felkutatására fenntartott forróvonal”; 116111: „Gyermekek segélyvonala”) – https://nmhh.hu/cikk/115/A_116_kezdoszamu_harmonizalt_kozerdeku_szolgaltatasok_szamainak_hasznalata_es_kijelolese`
- Indoklás: A „24 év alatt” nem pontosan egyezik a szolgáltató „24 éves korig” fordulatával; a szolgáltató szövegét vettem át, és nem értelmeztem. A régi oldal a 116-111 felnőtt-hívó állításának egyetlen forrása. Hogy megmarad-e, arról a Memuna dönt.

### D05-8 — M2.4 SLIDE 5: 🆘 doboz (TANULÓI LÁTHATÓ SZÖVEG)
- Fájl: 02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md:659
- Alap: GYV-14, GYV-4; D-05
- Hatáskör: SZEREP: Memuna
- OLD: `a Kék Vonal Lelkisegély-vonala gyerekeknek és fiataloknak (0–24, ingyenes; gyerek érdekében aggódó felnőtt is hívhatja)`
- NEW: `a Kék Vonal vonala gyerekeknek és fiataloknak (24 éves korig, éjjel-nappal, ingyenes)`
- Opcionális, Memuna-döntés, mert új tanulói mondat: a mondat után `Ha felnőttként egy gyerekért aggódsz, a Kék Vonal **116-000**-s száma neked szól.`
- Együtt mozgó helyek: nincs (a :209 nem érintett)
- Címkék: LÁTHATÓ SZÖVEG (pin); nem VO-PACK
- Indoklás: A zárójeles „0–24” a mondatban életkorként is olvasható, pedig a nyitvatartást jelenti. Az S1 mindkettőt külön kimondja.

### D05-9 — M3.B-KART-02: kártya-spec (BUILD-INPUT)
- Fájl: 02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépéstérkép.md:10
- Alap / Hatáskör: mint a D05-1-nél
- OLD: `116-111 – a Kék Vonal Lelkisegély-vonala gyerekeknek és fiataloknak (gyerek érdekében telefonáló, aggódó felnőtt is hívhatja), bántalmazott vagy eltűnt gyermek ügyében 116-000`
- NEW: `116-111 – a Kék Vonal vonala gyerekeknek és fiataloknak (24 éves korig), 116-000 – a Kék Vonal vonala a gyerekért aggódó felnőtteknek, bántalmazott vagy eltűnt gyermek ügyében is`
- Együtt mozgó helyek: az `assetek.csv:533`-at és a `_build`-et csak a `python3 tools/media_manifest.py build` írja, külön `chore(media)` commitban.
- Címkék: BUILD-INPUT (@asset); nem VO-PACK

### D05-10 — Csak ha a Memuna a §4.1 külső útját is pontosítja
- Fájl: GK:87, és szó szerint vele együtt HUM:30, Program terv:251, M3 KAPU:13, M3.B:76 (`@asset`, ebből `assetek.csv:536`)
- OLD (GK:87): `Kék Vonal **116-111**, bántalmazott vagy eltűnt gyermek ügyében **116-000**, közvetlen veszélyben **112** (§3.3)`
- NEW (tervezet): `Kék Vonal: **116-111**, ha 24 éves vagy fiatalabb vagy; **116-000**, ha felnőttként aggódsz egy gyerekért (bántalmazott vagy eltűnt gyermek ügyében is); közvetlen veszélyben **112** (§3.3)`
- Hatáskör: **EMBERI JÓVÁHAGYÁS KELL**. A szöveg a HUM-SAFE-01 lezárt projektgazdai döntésének szövege (HUM:30). A GYV-14 a célcsoport javítását írja elő, de egy LEZÁRVA HUM-SAFE-sor átírása a Memuna jóváhagyásán túl a projektgazda tudomásulvételét is kívánja.
- Indoklás: A mostani szöveg nem hamis. Egy 24 év feletti felnőtt viszont, akinek a gondja nem bántalmazás vagy eltűnés, a fiatalok vonalára jutna. Ez gyenge hiba, ezért P2. Ha a Memuna nem kéri, a sor marad.

### A HUM:471 formális újranyitásának tervezete (a Memuna saját aktusa, nem a repó írja be)

> **Memuna-újranyitás (GYV-14, <dátum>, REOPENED → új leírás):**
>
> **Mit nyitok újra:** az `Emberi jóváhagyás szükséges.md` 8. szakaszának „Segélyvonalak” sorát (:471), vagyis a `Gyermekvédelem – release gate.md` §3.3 116-111- és 116-000-leírását. A telefonszámok nem változnak.
>
> **Miért:**
> - A Kék Vonal jelenlegi oldalai szerint a 116-111 a fiatalok vonala 24 éves korig (kek-vonal.hu/fiataloknak/116-111: „A Kék Vonalnál 24 éves korig fogadjuk a hívásokat.”).
> - A 116-000 a gyerekért aggódó felnőttek, a szülők és a szakemberek vonala (kek-vonal.hu/szuloknek/116-000: „HÍVJ MINKET, ha aggódsz egy gyerekért!”; tudástár, 2023-10-04: „A 116 000 Segélyvonalon várjuk azoknak a felnőtteknek a hívásait, akik aggódnak egy gyermekért…”).
> - Az NMHH nyilvántartásában (frissítve: 2024-07-11) a 116000 neve „Eltűnt gyermekek felkutatására fenntartott forróvonal”, a 116111-é „Gyermekek segélyvonala”.
> - A kánon mostani állításait („a 116-111-et a gyerek érdekében telefonáló felnőtt is hívhatja”; „a 116-000 nem általános szülői vonal”) csak a Kék Vonal régi oldala (interaktiv.kek-vonal.hu) támasztja alá.
>
> **Új leírás:** a D05-1 és a D05-2 NEW szövege. A 15–17 éves madrihra vonatkozó útvonalról (D05-4, B változat) külön döntök: igen / nem.
>
> **Ellenőrzés:** forrásoldalak és dátum; a GK §6 release-napi ellenőrzése ettől független marad.
>
> **Jóváhagyta:** Memuna, <dátum>.

A repóba ezt csak a Memuna írásos aktusa után lehet bevezetni. Addig a mostani szöveg marad (D-05 „Addig”).

---

### D-01, D-04, D-09, D-10, GYV-3, GYV-6, PRG-12, JOG-1, GYV-24

### Memuna (és programvezető) jóváhagyási csomag: tervezet, AP-2026-10-13-01


Az ebben a csomagban álló minden javaslat **SZEREP** hatáskörű. A projektgazda 2026-10-13-i iránya egyiket sem hagyja jóvá (felhatalmazási jegyzőkönyv :21). Elfogadás csak a megnevezett szerep írásos nyilatkozatával lehetséges. Elutasításnál mindenhol a mostani, szó szerinti szöveg marad (a HUM:612 szerint az `F` sor óvatos alapértelmezése).

---

### 1. D-01 (GYV-5): megállítási protokoll, besorolás, létszámnorma

**Ki dönt:** Memuna + programvezető (HUM:628; GK §5:121).

**Mit jelent az elfogadás:** az (a)–(e) pont szövege az alábbi formában bekerülhet. **Elutasításnál:** marad a szó szerinti GYV-5 (M0.A:94, M2.A:65, :466, M3.B:275, M6.A:182, :712, Z.A:59). Protokoll-tartalom és besorolás nem kerül be.

### D01-a — GK §4.4, új alpont: a peula-megállítási protokoll
- Fájl: `02 Tervezet/Gyermekvédelem – release gate.md`, a :99 (a §4.2 vége) és a :101 (`### 4.3.`) után, a §4.3 blokkja (:107) mögé.
- Alap: projektgazdai irány, D-01; GYV-5. Az elemek kánoni helye lépésenként szögletes zárójelben áll.
- Hatáskör: SZEREP, Memuna + programvezető. Jóváhagyási feltétel: írásos jóváhagyás. A protokoll egésze **új elem — Memuna-szövegezés/jóváhagyás kell**. A GK maga is kánoni gate-dokumentum.
- OLD (beszúrási horgony, a §5 előtt): `## 5. Szervezeti döntések`
- NEW (a horgony elé):
  ```
  ### 4.4. Peula-megállítási protokoll (GYV-5)

  Ahol egy peula a „kötelező megállítási protokollra” hivatkozik, ezt a sorrendet követi:

  1. **Állítsd le a kört egy semleges mondattal – ne állítsd az érintettet a figyelem középpontjába.** Például: „Álljunk meg egy pillanatra, legyen egy kis levegő.” [M6.A:492–493]
  2. **Ajánld fel a kilépést, szünetet – nyíltan, mindenkinek, ne csak az érintettnek.** [M6.A:496; M0.A:133]
  3. **Felkavart kiskorút nem küldünk ki egyedül:** legyen kijelölt biztonságos hely és egy felnőtt, aki vele van [§4:64]. A beszélgetés diszkrét, de átlátható helyzetben zajlik; kettesben csak indokolt esetben, átlátható módon és egy másik felelős tudtával [§4.2].
  4. **Hívd a helyettest.** A helyettes ugyanazon a helyszínen azonnal elérhető [§4:60 mintája]; a telefonos elérhetőség nem elég. A kör csak akkor folytatódik, ha a második felelős megérkezett. [ÚJ ELEM, G1 1(a) és 2.]
  5. **Gyermekvédelmi aggálynál azonnal vond be a kijelölt Memunát** – összeférhetetlenség esetén a név szerint kijelölt helyettesét [§4.1, 4. lépés]; **közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés** [§4.1, 5. lépés; §3.3].

  A 15–17 éves madrih nem számít a felelősök közé: soha nem ő az egyetlen felelős felnőtt [§4:60; HUM-SAFE-03].
  ```
- Együtt mozgó helyek: a D01-b hivatkozó helyei; a §5.1 táblájának 6. sora („a kiskorú madrih felnőtt felügyelete”). Ez utóbbi bővíthető „§4.4”-gyel, de az is új elem.
- Címkék: nem VÉTÓLISTÁS (kulcs, küszöb és completion nem érintett), nem VO-PACK, governance-szöveg (nem tanulói).
- Indoklás: a lépések az M6.A 4.3.2/B, a GK §4:60, :64, a §4.1 és a §4.2 meglévő mondatai. Új elem a 4. lépés „ugyanazon a helyszínen” alkalmazása erre a helyzetre, valamint a „csak a második felelős érkezése után” feltétel (G1, nyers kimenet :48–57).

### D01-b — A peulák hivatkozó mondata
- Fájlok és OLD horgonyok:
  - `M0/Peulák/M0.A…md:94` · `M3/Peulák/M3.B…md:275` · `Z/Peulák/Z.A…md:59`, mindhárom: `vagy azonnal elérhető helyettes és kötelező megállítási protokoll. Egyszemélyes`
  - `M2/Peulák/M2.A…md:65`: `vagy azonnal elérhető helyettes és kötelező megállítási protokoll. Egyszemélyes`
  - `M6/Peulák/M6.A…md:182`: `vagy azonnal elérhető helyettes és kötelező megállítási protokoll. Egyszemélyes`
- NEW (mindegyikben): `vagy azonnal elérhető helyettes és kötelező megállítási protokoll (`Gyermekvédelem – release gate.md` §4.4). Egyszemélyes`. Az M6.A-ban a G1 ajánlása szerint: `… megállítási protokoll (4.3.2/B; `Gyermekvédelem – release gate.md` §4.4). Egyszemélyes`.
- Együtt mozgó helyek: M2.A:466 és M6.A:712 ellenőrzőlista („és a kötelező megállítási protokoll” → „… (§4.4)”); a spec-sor M6.A:10 (BUILD-INPUT, csak `media_manifest.py build` úton).
- Hatáskör: SZEREP, Memuna + programvezető (a D01-a elfogadásától függ). Címkék: nem tanulói felület (képzői peulaszöveg). M0.A: **CC-04 freeze**, ezért csak freeze-kivétellel.
- Indoklás: a képzői szövegben van precedens GK-útvonal-hivatkozásra (M3.B:344, „`Gyermekvédelem – release gate.md` §4.2”).

### D01-c — Peulánkénti kockázati besorolás (javasolt kánoni hely: a GK §4.4 táblája; ez is új elem)

| Peula | Önbesorolás a szövegben | G1 ajánlása | Verdikt |
|---|---|---|---|
| M0.A | :94 „erős érzelmet vagy súlyos tartalmat is előhívhat”; :130 | érzékeny, nem egyszemélyes | Memuna + programvezető erősítse meg |
| M2.A | :279 „Ez az egész peula önfeltáró” | érzékeny, nem egyszemélyes | erősítse meg |
| M2.B | csak a GK:64-minimum (:57) | **nyitott** | Memuna dönt |
| M2.F | csak a GK:64-minimum (:73, :380) | **nyitott** | Memuna dönt |
| M3.A | – | nem vizsgálta | Memuna dönt |
| M3.B | :275 GYV-5-sor; GK §2 release-hatókör | érzékeny, nem egyszemélyes | erősítse meg |
| M3.F | – | listázta, ajánlás nélkül | Memuna dönt |
| M4.A | :58 „szereplési szorongás önmagában nem … krízis” | **nem érzékeny** (GYV-6); a :58 minimum marad | erősítse meg vagy vétózza |
| M4.B | :63 GYV-6-minimum | nem vizsgálta | Memuna dönt |
| M5.A, M5.B, M5.F | – | nem vizsgálta | Memuna dönt |
| M6.A | :182 „Érzékeny peula” | érzékeny, nem egyszemélyes; protokoll = 4.3.2/B | erősítse meg |
| M6.F | – | nem vizsgálta | Memuna dönt |
| M7.A | – | nem vizsgálta | Memuna dönt |
| M7.B | :93 minimum | nem vizsgálta | Memuna dönt |
| M7.F | – | listázta, ajánlás nélkül | Memuna dönt |
| Z.A | :59 GYV-5-sor | érzékeny, nem egyszemélyes | erősítse meg |

- Kivételes esetre a G1 ajánlása: a programvezető írásos kockázatfelmérése. A képző önminősítése nem javasolt (KCS Standard 3). Mindkettő új elem.
- Hiány: a feladatlistából kimaradt az M1.A, M1.B, M1.F, M4.F és M6.B. Az M1 a CC-04 freeze alatt áll. Besorolásukat a Memunának ugyanígy meg kell adnia, vagy ki kell mondania, hogy nem releváns.

### D01-d — Létszámnorma-javaslat (új elem, Memuna + programvezető)
- Javasolt szöveg (GK §4.4, a protokoll alá): `Érzékeny peulán legalább két, a HUM-SAFE-05 szerint ellenőrzött és felkészített, 18 év feletti felelős (képző vagy mentor) van jelen, 20 fős létszámig. A 15–17 éves madrih ebbe nem számít bele.` 20 fő felett a G1 nem adott értéket: **Memuna + programvezető dönt.**
- Források a G1 szerint (nyers kimenet :25–35). Én nem nyitottam meg őket újra: az idézetek a G1 kimenetéből valók.
  - NSPCC Learning: „13 - 18 years - one adult to ten children”; „We recommend having at least two adults present, even with smaller groups.”; „only people aged 18 or over should be included as adults when calculating adult to child ratios.” Ez ajánlás, nem jogszabály.
  - KCS Standard 3: „Child safeguarding risk assessments and mitigation strategies are incorporated into existing risk assessment processes at all levels.”
  - **Hatályos magyar létszámnormát nem találtunk.** A 6/2025. (II. 25.) BM rendeletet a G1 csak nem hivatalos forrásból (net.jogtar.hu) olvasta, és ott sincs számszerű arány. Az NJT nem töltött be, a Gyvt.-t nem olvasta végig. A Scouting America szabálya nem ellenőrzött, ezért nem használható.

### D01-e — Feltételes alak: M0.A:134 és M2.A:281–283
- **M0.A:134**
  - OLD: `3. **Tereld vissza a kört egy kész mondattal**, és menj tovább a strukturált blokkal (a kör/feladat folytatódik mással).`
  - NEW: `3. **Tereld vissza a kört egy kész mondattal.** Ha van a peulán második felelős, aki az érintettel marad, menj tovább a strukturált blokkal (a kör/feladat folytatódik mással); ha nincs, a megállítási protokoll szerint állj meg (`Gyermekvédelem – release gate.md` §4.4).`
  - Együtt mozgó helyek: :135. A „Most haladunk tovább a körrel” mondat csak az első ágon érvényes, ezért Memuna-szövegezés kell. Ugyancsak együtt mozog a M0.A-KART-01 spec, :105 „3) tereld vissza a kört…” (BUILD-INPUT, újragenerálandó kártya).
  - Címkék: CC-04 freeze, nem VO.
- **M2.A:281**
  - OLD: `**Egy rövid mondattal jelezd, hogy ez rendben van, ne állítsd meg miatta a csoportot:**`
  - NEW: `**Egy rövid mondattal jelezd, hogy ez rendben van:**`
- **M2.A:283**
  - OLD: `3. **A kört folytasd mással**, hogy ne maradjon rajta minden szem`
  - NEW: `3. **Ha van a peulán második felelős, aki az érintettel marad, a kört folytasd mással**, hogy ne maradjon rajta minden szem`
  - A mondat végére: ` Ha nincs második felelős, a megállítási protokoll szerint állj meg (`Gyermekvédelem – release gate.md` §4.4).`
- Hatáskör: SZEREP (Memuna szövegez, G1 5. pont). Nem VÉTÓLISTÁS.

---

### 2. D-04 (GYV-7, GYV-8, GYV-4, GYV-19): eszkalációs küszöb és címzett

**Ki dönt:** Memuna. A (e) részben a programvezetővel. Ha egy ✅-szöveg változna: értékelési felelős + projektgazda. A (d) részben a projektgazdával.

### D04-a1 — M6.3:749 (M6:QA14-BIZT-1/-2)
- Fájl: `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:749`. A doboz nincs `@source`-ban (a NAR-04 a :757-en kezdődik).
- Alap: GYV-7; kánoni mondat: M6.2:783, M6.A:502, M3.3:416.
- Hatáskör: SZEREP, Memuna. Jóváhagyási feltétel: a GYV-7 kiterjesztése erre a dobozra (új alkalmazási eset).
- OLD: `valós, nehéz saját helyzetet (friss seb, bántalmazás, önsértés) hoz fel.`
- NEW: `valós, nehéz saját helyzetet (zaklatás, bántalmazás, önsértés vagy más veszélyeztetettség) hoz fel.`
- Második OLD: ` **Madrih vagy, nem terapeuta.**`
- NEW: ` Ha valaki pusztán nehéz érzésről beszél (például friss gyászról), és veszélyeztetettség nem merül fel, az nem jelzési ügy: támogatást ajánlasz neki, és ő választja meg, él-e vele („Itt vagyok, ha beszélni szeretnél – de nem kötelező.”). Ha bizonytalan vagy, ezzel se maradj egyedül: sokszor pont az a nehéz, hogy bizonytalan vagy, és ilyenkor is fontosabb segítséget kérni, mint egyedül maradni vele – [KONZULTÁCIÓS ÚT: a helyszíni 18+ felelős / a Memuna; ÚJ ELEM, a Memuna dönti el]. **Madrih vagy, nem terapeuta.**`
- Együtt mozgó helyek: D04-a2, D04-a3.
- Címkék: LÁTHATÓ SZÖVEG (pin), nem VO.
- Indoklás: a felsorolás és a második lépcső szó szerint az M6.2:783-ból jön; a két idézett mondat az M6.A:502 és az M3.3:416 alakja (G2, :202). A konzultációs út címzettje új szabály.

### D04-a2 — M6.4 6D (:933) és ZÁRÓ (:1028)
- **Korlát.** A 2026-10-05-i jegyzőkönyv (:31): „the 6D/ZÁRÓ safeguarding repetition remains Memuna QA; do not change it now.” Az M6-NY-D27: „A D1 kiváltó feltétele és a Memuna bevonásának küszöbe ne változzon.” A D27 **lezárt projektgazdai döntés**. A „friss seb” kivétele ezért a Memuna-verdikten túl **projektgazdai feloldást is igényel**.
- Hatáskör: SZEREP, Memuna (QA), a D27 miatt + projektgazda.
- OLD (:933): `> hanem valós, súlyos témát (bántalmazás, önsértés, friss seb) tár fel,`
- NEW: `> hanem valós, súlyos témát (bántalmazás, önsértés vagy más veszélyeztetettség) tár fel,`
- OLD (:1028, egyedi rész): `hanem valós, súlyos témát (bántalmazás, önsértés, friss seb) tár fel, az már **nem játék**`
- NEW: `hanem valós, súlyos témát (bántalmazás, önsértés vagy más veszélyeztetettség) tár fel, az már **nem játék**`
- Megfigyelés: a 6D (:938–) és a ZÁRÓ már tartalmazza a „kibillen, de ilyen témát nem tár fel” ágat az M6.A négy lépésével, a 4. lépésben a Memunával. Az M6.2:783 második lépcsőjét ide **nem** javaslom betenni, mert ütközne a D27-tel zárolt „erősen érintett → Memuna” küszöbbel.
- Címkék: LÁTHATÓ SZÖVEG. Nem VO (a fájlban nincs `@source`).
- Ajánlott alapértelmezés: marad, ha a projektgazda a D27-et nem oldja fel.

### D04-a3 — M6.2:783
- OLD: `az nem jelzési ügy: támogatást ajánlasz neki, és ő választja meg, él-e vele.`
- NEW: `az nem jelzési ügy: támogatást ajánlasz neki („Itt vagyok, ha beszélni szeretnél – de nem kötelező.”), és ő választja meg, él-e vele. Ha bizonytalan vagy, ezzel se maradj egyedül: ilyenkor is fontosabb segítséget kérni, mint egyedül maradni vele – [KONZULTÁCIÓS ÚT: ÚJ ELEM, Memuna dönt].`
- Nem `@source` (a NAR-06 a :789-en kezdődik; a „nem jelzési ügy” csak a :783-ban fordul elő).
- Címkék: LÁTHATÓ SZÖVEG. Hatáskör: SZEREP, Memuna (a kiskorú madrih szerepe).

### D04-b — M7.B:480 (M7:QA14-BIZT-6)
- Fájl: `02 Tervezet/Modulok/M7/Peulák/M7.B – Peula v2 & Zmán Kvucá – amikor a papír találkozik a valósággal.md:480`. Nincs `@source`.
- OLD: `> – Ha olyasmire kerestek választ, ami **gyermekvédelemmel, bántalmazással, komoly szorongással** kapcsolatos, arra ne AI-tól kérjetek tanácsot, hanem **a Memunától**.`
- NEW: `> – Ha olyasmire kerestek választ, ami **gyermekvédelemmel vagy bántalmazással** kapcsolatos, arra ne AI-tól kérjetek tanácsot, hanem **a Memunától**. **Komoly szorongásnál** se AI-tól kérjetek tanácsot, hanem a mentorotoktól vagy a képzésfelelőstől; ha veszélyeztetettség gyanúja merül fel, azonnal a Memunától.`
- Alap: a modul saját :93 szerkezete („mentor / képzésfelelős”; „gyermekvédelmi jelzés … azonnal a Memuna”).
- Az AI-tilalom mindhárom esetre megmarad.
- Címkék: AI-kikötés (nem gyengül), LÁTHATÓ SZÖVEG.

### D04-c — M0 csoportchat-szívatás (M0:BIZT-5)
- **A Memuna kérdése (GYV-7, F):** a kvuca-csoportchatben zajló szívatás mindig Memuna-jelzés, vagy csak zaklatásnál vagy veszélyeztetettségnél? A G2 ajánlása: kétlépcső, az ismétlődő csúfolás zaklatásnak számít; a minősítés a Memunáé.
- **M0.2:271 — javaslat: marad.** Az ✅ opció („és **jelzek** a Memunának”) a kétlépcsős olvasatban is helyes, ha a Memuna a kvuca-chatben induló szívatást zaklatásnak minősíti. Ha átírnánk, VÉTÓLISTÁS lenne (kulcsopció szövege), és a :281 visszajelzéssel is széttartana.
- **M0.4:328 (az 1. helyzet jó-válasz visszajelzése)**
  - OLD: `> „Igen: **nem mész bele a csúfolódásba / nem hagyod magára az érintettet**.”`
  - NEW: `> „Igen: **nem mész bele a csúfolódásba / nem hagyod magára az érintettet**. Ha a csúfolás ismétlődik, vagy zaklatássá, bántalmazássá válik, azonnal vond be a Memunát.”`
  - Alap: GYV-7 első lépcsője + a Memuna minősítése (ÚJ alkalmazás).
  - A :332 téves-válasz visszajelzése ugyanígy mozog.
- A kvízkulcs (✅ :310, :271) nem változik.
- Címkék: LÁTHATÓ SZÖVEG, **CC-04 freeze** (futó M0-pilot), a hub belépőkvíz-itemje a projektgazdáé (hub :180).

### D04-d — M4.3:360: javaslat, hogy marad
- A mostani szöveg: „**Ha egy hanihhal folytatott beszélgetésben gyermekvédelmi aggály merül fel,** … **azonnal vond be a kijelölt Memunát** …”
- Indok:
  - Ez terepi hanih-helyzet, ahol nincs képző. A címzett a GK §4.1:82 szerint „mindig a Memuna … nem „egy felnőtt””.
  - A GYV-19 GK §4:57-része (meghallgat, nem nyomoz) már teljesül.
  - A „képző” beírása új címzettet vezetne be a terepen. A helyszíni 18+ felelős (GYV-8) beírása szintén új címzett az M4-ben (G2, :284).
- A Memuna (a projektgazdával) azt erősíti meg, hogy a GYV-19 „képző” eleme csak a képzés közbeni feltárásra (M2.A) szól.
- Elfogadás után az `M4:BIZT-G1-6` a „képző” részig zárható.

### D04-e — M6 KAPU P1, visszajelzés (:367); a ✅ :355 nem változik
- Fájl: `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:367`
- OLD: `és nem halasztod a peula utánra. (M6.A peula;`
- NEW: `és nem halasztod a peula utánra. Nem te vagy az egyetlen felelős: a peulán ott van a felkészített, 18 év feletti felnőtt is, és a gyermekvédelmi felelősség az övé. Ha a Memuna nem érhető el vagy érintett, a helyettesét vond be; ha egyikük sem érhető el (például munkaidőn kívül), érzelmi támogatásra a Kék Vonal 116-111 az út – az elérhetőségeket a kurzus „Segítség és kapcsolatok” blokkjában találod. (M6.A peula;`
- Alap: GK §4:60 (tanulói átfogalmazás, Memuna-szövegezés) és az M2.4:209 szó szerint.
- Hatáskör: SZEREP, Memuna + programvezető. Ha az értékelési felelős a visszajelzést kulcsrésznek tekinti, ő is.
- Címkék: kapu-item visszajelzése, LÁTHATÓ SZÖVEG. A ✅ és az opciók nem változnak.
- **D-05-függés:** az M2.4:209 csak a 116-111-et nevezi meg, a GK §4.1:87 bántalmazásra a 116-000-t is. A 116-os leírás a D-05 Memuna-döntéséig nyitott.
- **M6.B játéklap, „kit hívsz” rovat** (:48, :216; a spec :244 BUILD-INPUT): a G2 (a) opciója szerint **nem változik**. Ha a Memuna kiegészítést kér (például „kit hívsz: a helyszíni 18+ felelőst és a Memunát”), az az R4 blokkoló sor új eleme, és értékelési felelős + projektgazda is kell hozzá (VÉTÓLISTÁS).
- A GYV-4 (c) alkérdése G1-bizonyíték (BK-13), nem döntés.

---

### 3. D-09 (GYV-1 `F`): ellenőrzési kérdés és nyilatkozat

**Ki dönt:** Memuna. Vétó/QA: DPO / jogi felelős.

- **A kérdés a Memunának:** „A GYV-1 ‚határidős átnézés’ fordulata vonatkozik-e a KAPU-M2:24 mentori megerősítésére (‚A mentor a kapueredményt legkésőbb 24 órával a következő fix alkalom előtt megerősíti.’)? Vagy az kapuértékelési megerősítés, és a gyermekvédelmi jelzés útja külön, a KAPU-M2:203 akut útja?”
- **Az elfogadási nyilatkozat tervezete (Memuna):** „Megerősítem, hogy a KAPU-M2:24 24 órás határideje kapuértékelési megerősítés (HUM:220), nem gyermekvédelmi átnézés vagy bejelentés-kezelés. A GYV-1 feltételét az M2-ben a KAPU-M2:203 külön akut jelzési útja teljesíti, és a ‚mentorod azonnal bevonja’ ígéret az M2-ből kikerült. A határidő nem változik. Dátum, név, a vizsgált SHA: ….”
- **DPO / jogi QA:** „Nem emelek vétót: az M2 tárolt szöveges válaszaira nem keletkezik rendszeres, határidős biztonsági olvasási cél.”
- **Elutasításnál:** a (b) olvasat lép életbe. Ekkor az M2-ben SLA-bizonyíték kell, vagy a KAPU-M2:24 és a MAN:57 módosul. Ez a HUM:220-at érinti, ezért **projektgazdai döntés** kell hozzá, és VÉTÓLISTÁS (időtartam, completion).
- **Kapcsolódó kérdés ugyanebben az ülésben:** a Z.4:201 („a beadást látó mentornak vagy értékelőnek azonnal be kell vonnia”) garancia-jellegű. Hasonló-e a GYV-1 által az M2-ben tiltott ígérethez? Ha a Memuna szerint igen, az külön döntés (Memuna + DPO).

---

### 4. D-10, Memuna-rész (GYV-11): az eljárás lépései a G4 (1)+(i) opciója szerint

Ez **teljes egészében új elem — Memuna + DPO-szövegezés/jóváhagyás kell.** A szerepek egy része repóból nem nevezhető meg; ezeket helyőrző jelöli.

1. **Észlelés:** a beadást látó mentor vagy értékelő a GK §4.1 szerint azonnal bevonja a Memunát. A Moodle-be nem ír az esetről (GK:85).
2. **Átmentés:** a Memuna vagy a helyettese a szükséges tartalmat az incidensnyilvántartásba menti (`Restricted / Safeguarding / Incidents`, GK:86).
3. **Korlátozás:** a Moodle-példányt [KIJELÖLT JOGOSULT: LMS-gazda / manager szerep? — Memuna + DPO nevezi meg] korlátozza: elrejti, és elvonja az értékelői hozzáférést. Ez a HUM-PRIV-01 „kikerül a Moodle-ből” fordulatának olvasata (G4).
4. **Törlés vagy megőrzés:** automatikus törlés nincs. A kézi törlésről jogi megőrzési felülvizsgálat után [DÖNTŐ: Memuna + DPO; a jogi felülvizsgálatot végző szerep: jogi felelős] dönt, és a döntést dokumentálja (ADV §5:153).
5. **Pótlás:** feltárásmentes, kézzel nyitott külön próbálkozás, amely nem számít bele a keretbe (a Z.4:359 mintája). Erről az **értékelési felelős** dönt; ez nem Memuna-hatáskör, és VÉTÓLISTÁS.

**Z.4 Feedback-válaszok:**
- A G4 ajánlása a (2) vagy a (3) opció:
  - (2) a Memuna átmenti a választ, a Moodle-válasz a 90 napos sor szerint megy (ADV §3:70 változatlan), és a Z.4:401 GYV-11-tagmondata kikerül;
  - (3) átmentés után kézi, dokumentált törlés a `mod/feedback:deletesubmissions` jogú szereppel. A G4 szerint ez az editingteacher és a manager szerepé (`mod/feedback/db/access.php`); ezt én nem ellenőriztem újra.
- Addig a Z.4:359, :370 és :401 marad.

**Amit a DPO-tól kell kérni (külön csomag):**
- az (a)/(b) megőrzési rend;
- az ADV §3:70 sor sorsa;
- a Feedback-válaszadó felhasználónévvel való visszakeresése: tiltott, vagy csak súlyos veszélynél, a Memuna kérésére, megnevezett adminisztrátor által, dokumentáltan. Ez jogi minősítés, a jogi felelős is kell hozzá;
- a Z.4:370 tájékoztató mondata. A HUM-PRIV-03 „név nélkül jelennek meg” mondata nem változhat.

A GDPR-idézeteket a G4 másodlagos forrásból (gdpr-info.eu) vette. A hivatalos magyar szöveggel össze kell vetni.

---

### 5. GYV-3: helyenkénti Memuna-verdikt lap (7 hely)

Forrás: a döntési csomag :230. Lehetséges verdiktek minden helyen: **(M)** megfelel a HUM-SAFE-02-nek; **(N)** nem felel meg, Memuna-szövegezés kell; **(K)** megfelel, kiegészítéssel.

A kritikus itemek kulcsa nem változik. Az ITEM 4 kulcsa csak projektgazdai döntéssel változhat.

| # | Kulcs | Hely (ma) | A mostani szöveg (rövid idézet) | A Memuna kérdése |
|---|---|---|---|---|
| 1 | M0:BIZT-3 | M0.4:312–317, 2. helyzet | „Késő este ír egy hanih: ‚Nagyon sz\*rul vagyok…’” → ✅ B: „…bevonom a Memunát, mert ő tud segíteni. Nem a hátad mögött teszem…” | Megfelel-e a privát, esti válaszüzenet a §4.2-nek (szervezeti csatorna, nincs 1:1 elmélyítés)? CC-04 freeze. |
| 2 | M2:BIZT-G2-4 | M2.4:193–198, :206–209, :653 | poll: „Azonnal visszaírok, és addig chatelek vele…” („mind elfogadható”); :207 „nem nyitsz éjszakai privát 1:1 chatet” | Elfogadható-e a poll „mind elfogadható” keretezése a :207 tiltásával együtt? |
| 3 | M3:BIZT-G1-1 | M3 KAPU ITEM 4, :145–148 (KRITIKUS) | „23:15 … privát üzenetben” → ✅ B „Nem hagyom egyedül, és azonnal bevonom a Memunát…” | (a) SAFE-7-megfelelés; (b) a „Nem hagyom egyedül” a kiskorú madrih szerepén belül van-e. A kulcs nem változik. |
| 4 | M3:BIZT-G2-3 | M3.3:549–554 | „Ha ő magától kezd beszélni – így hallgasd meg” | A feltárási beszélgetés a §4.2 (b) kivétele-e, átláthatósági feltétellel? |
| 5 | M3:BIZT-G3-4 | M3.B:356 (1. kártya), :405 (megoldójegyzet), MUNK-03 spec :108 | „ezt csak neked mondhatom el”; a megoldójegyzet csatornát nem nevez meg | Kell-e a megoldójegyzetbe a csatorna (szervezeti, nem 1:1)? |
| 6 | M3:BIZT-G2-8 | M3.4 3A (régi :363, :590 ↔ :358); ma :361, valószínűleg :564 | :361 már a teljes §4.2-szabály; :564 „kettesben csak a három engedélyezett kivételnél” | Erősítse meg, hogy megfelel. A régi sorhivatkozás eltolódott. |
| 7 | M4:BIZT-G2-1 | M4.A:438–444, MUNK-02 | „automatikus négyszemközti félrevonulás nincs … egy másik felelős tudtával” | Erős szorongásnál a képzői 1:1 a (b) kivétel-e? |

- A **SAFE-7** (M3.3 S1, 23:15-ös bejövő privát üzenet és ✅ első válasz) önálló, nyitott QA (HUM:569, GK §6:154). A GYV-3 7 helyével együtt, de külön sorban kell verdiktet adni rá.
- **Eltérés a megbízástól:** a megbízás 7. helyként a „SAFE-7 helyeit” nevezte meg, a kánoni csomag (:230) viszont az M3:BIZT-G2-8-at. Mindkettőt felvettem.

---

### 6. Kisebb tételek

### GYV-6 küszöb (M4), Memuna + programvezető
- **Kérdés:** jóváhagyja-e a Memuna a küszöböt?
  - M4.A:58 és M4.B:63: „A szereplési szorongás önmagában nem gyermekvédelmi krízis, de bárki bármikor megállhat és passzolhat.”
  - Saját érintettségnél nincs nyilvános feldolgozás; GK:64-minimum.
- **Ha a Memuna körönkénti passz-bejelentést kér:** az M4.B:326 mondata szó szerint a 4.1, a 4.2 (3. lépés) és a 4.4/1 instrukcióba kerül (G3, :543).
- **Elutasításnál:** a sor REOPENED.

### PRG-12 review-lap (M3 modulgazda + Memuna)
- Vizsgálandó:
  - M3.B:359 (4. kártya: „sok külön töltött idő, ölelkezés, titkolózás: ‚Ezt ne mondjuk el senkinek.’”);
  - :408 megoldójegyzet;
  - :410 „Fontos különbség”;
  - :465–471 (4.3.3, „Valós gyermekvédelmi történetet ne rögtönözz”).
- Ellenőrzőpontok:
  - fiktív és nem visszaazonosítható-e;
  - harmadik személyű-e (:361–362);
  - nem megterhelő-e;
  - a kulcskülönbség időhiánynál is elhangzik-e (:471).
- Verdikt: (M) / (N + Memuna-szövegezés).
- A D-03 kérdése (az „új” szó a címben, négy csoport) külön döntés.

### JOG-1 — Memuna-jóváhagyási nyilatkozat (a jogászi ellenőrzés után)
„A jogi szakértő [név, dátum] írásos ellenőrzése alapján jóváhagyom:
- a madrih azonnal a kijelölt Memunának vagy a helyettesének jelez;
- a külső jelzésről a szervezet nevében a jogi tanács alapján kijelölt felnőtt, [szerep] dönt, anélkül hogy az akut védelem késne;
- a Gyvt. 17. § címzettjeit és határidőit a jogász ellenőrizte; a tananyag nem állít általános három munkanapos büntetőjogi határidőt.
Nyilvántartás: G1 tracker #1 [link] (D-06 projektgazdai irány). SHA: ….”

A kijelölt felnőtt megnevezése szervezeti aktus. A repó nem tölti ki.

### GYV-24 — G1 „átnéztem” ellenőrzőlista (csak a Memuna)
- [ ] Egyetlen végleges SHA, dátummal; minden alábbi verdikt erre szól.
- [ ] SAFE-7 explicit verdikt (HUM:569).
- [ ] A 7 GYV-3-hely mindegyike explicit verdikttel (5. pont).
- [ ] Akut út és segélyvonalak a review napján ellenőrizve (GK §6:151). A D-05 116-111/116-000-leírás döntése előtte szükséges.
- [ ] A GK §2 hatókörébe eső elemek átnézve (M3.3, M3.B, M3-kapu, az M7 gyermekvédelmi részei).
- [ ] Tracker #1 lezárása a bejegyzés linkjével (RELEASE-READINESS :60).

---

### Amit nem ellenőriztem
- Az OLD-horgonyok egyediségét Greppel csak az alábbi szövegeknél néztem meg kifejezetten: M7.B:480, M6.4 „friss seb” (:933, :1028), M6.2:783, M0.2:271 és M0.4:310. A többit Read alapján, egyetlen előfordulásként vettem át.
- Az M3.4 régi :590-es hivatkozásának mai megfelelője nincs megerősítve.
- A NSPCC-, KCS-, Moodle- és GDPR-idézeteket nem nyitottam meg újra; mind a G1 és a G4 nyers kimenetéből származik.
- Az M3.A, M5.x, M6.F és M7.A/B önbesorolását nem olvastam végig.

### Ellentmondások a kánonban
1. A GK §3.3:46 szerint a 116-111-et a felnőtt is hívhatja, a G2 szerint a szolgáltató ezt nem erősíti meg. Közben az M2.4:209-re épülő D04-e csak a 116-111-et nevezi meg. Mindkettő a D-05-től függ.
2. Az M6-NY-D27 (lezárt) zárolja az M6.4 6D/ZÁRÓ küszöbét, miközben a GYV-7 kiterjesztése a „friss seb” kivételét kívánná. Ehhez projektgazdai feloldás is kell, nem csak Memuna.
3. Az M0.A:94 GYV-5-mondata és a :133–134 („felnőtt legyen vele” + „a kör folytatódik”) egy képzővel együtt nem teljesíthető. Ezt a D01-e oldja fel.

### Érintett fájlok (abszolút úttal)
- 02 Tervezet/Gyermekvédelem – release gate.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md
- 01 Fejlesztés/04 Audit/2026-10-13 Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md
- 01 Fejlesztés/04 Audit/2026-10-13 Nyers kutatási, verifier- és QA-kimenetek, AP-2026-10-12-02.md
- 01 Fejlesztés/04 Audit/2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md
- A javasolt szerkesztések helyei: a `02 Tervezet/Modulok/` alatt az M0.A, M0.2, M0.4, M2.A, M6.2, M6.3, M6.4, M6 KAPU, M7.B, továbbá M3.B, Z.A, M6.A (hivatkozó mondat) fájl.

### Kiegészítő kész szövegek (a független ellenőrzés ezeket szerepköri jóváhagyáshoz sorolta)

### D-04 (f) – Z.3 biztonsági doboz

### D04f-1 — 112 a :303 dobozba
- Fájl: 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md:303
- Alap: HUM 14 GYV-4 `F` („közvetlen veszélyben 112” a veszélyt bemutató dobozokban); a kánoni mondat: `Gyermekvédelem – release gate.md`:79 (§4.1 5. lépés); irány D-04
- Hatáskör: PROJEKTGAZDA (szó szerinti kánoni átvezetés; vétó/QA: Memuna és helyettese (GYV-4), Memuna + programvezető (GYV-8)). Ha a hívó új alkalmazási esetnek minősíti (G2 így sorolta), akkor SZEREP: Memuna + programvezető.
- OLD: `ha pedig gyermekvédelmi aggályod van, azonnal bevonod a kijelölt Memunát.`
- NEW: `ha pedig gyermekvédelmi aggályod van, azonnal bevonod a kijelölt Memunát. **Közvetlen veszélynél előbb a biztonság és a 112**, utána a belső jelzés.`
- Együtt mozgó helyek: nincs. A :310 mintamondat és a :316 (LMS-Z-07 elfogadási kritériuma) NEM változik.
- Címkék: LÁTHATÓ SZÖVEG. A Z.3-ban nincs `@source` blokk, ezért nem VO-PACK.
- Indoklás: a GK §4.1:79 pontos szövege kiemeléssel együtt: „**Közvetlen veszélynél előbb a biztonság és a 112**, utána a belső jelzés.” Ezt vettem át változtatás nélkül.

---

### D08-1 — M2.4 SLIDE 5 passz-út
- Fájl: 02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md:663
- Alap: HUM 14 GYV-2 `F` („M2.4 kötelező mezője így biztosan módosítandó”); D-08 (a), G3 (b) opció; irány D-08
- Hatáskör: PROJEKTGAZDA (vétó/QA: Memuna + programvezető, HUM-SAFE-03)
- OLD: `ilyenkor a mezőbe írd be, hogy „passz”, és egy mondatban azt, kit vonnál be azonnal egy ilyen üzenetnél. Ez is teljes értékű válasz.`
- NEW: `ilyenkor a mezőbe írd be, hogy „passz”, és egy mondatban azt, kit vonnál be azonnal egy ilyen üzenetnél, és mit nem kezdenél el. Ez is teljes értékű válasz.`
- Együtt mozgó helyek: D08-2, D08-3, D08-4. A :665 („a passz lehetősége is”) nem változik.
- Címkék: LÁTHATÓ SZÖVEG. Nem VÉTÓLISTÁS: a „Required” és a completion („beküldve”) nem változik, csak a passz-út tartalma bővül; ha a hívó ezt completion-tartalomnak tekinti, akkor vétólistás. A NAR-04 `@source` (:797) nem tartalmaz passz-szöveget, ezért nem VO-PACK.
- Indoklás: a 3️⃣ kérdés saját eleme (:655). Fiktív esetre vonatkozik (:649), személyes tartalmat nem kér, így a teljesítés nem függ önfeltárástól.

### D08-2 — M2 hub :183
- Fájl: 02 Tervezet/Modulok/M2/M2 – Ki vagyok madrihként – Identitás, Somer-értékek és dugma isit.md:183
- Alap / Hatáskör: mint a D08-1-nél
- OLD: `(vagy a passz és egy mondat arról, kit vonna be)`
- NEW: `(vagy a passz és egy mondat arról, kit vonna be és mit nem kezdene el)`
- Együtt mozgó helyek: D08-1
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: tükörszöveg.

### D08-3 — M2 hub :190
- Fájl: ugyanaz:190
- Alap / Hatáskör: mint a D08-1-nél
- OLD: `(vagy passz egy mondattal arról, kit vonna be)`
- NEW: `(vagy passz egy mondattal arról, kit vonna be és mit nem kezdene el)`
- Együtt mozgó helyek: D08-1
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: tükörszöveg.

### D08-4 — MAN LMS-M2-09 (két horgony egy sorban)
- Fájl: 02 Tervezet/LMS – activity manifest.md:57
- Alap: GYV-2 (jobb oszlop: „MAN:57 … projektgazda (build-spec gazda), QA: Memuna”)
- Hatáskör: PROJEKTGAZDA (QA: Memuna)
- OLD-a: `(vagy a passz és egy mondat arról, kit vonna be: HUM 14. szakasz, GYV-2)` → NEW-a: `(vagy a passz és egy mondat arról, kit vonna be és mit nem kezdene el: HUM 14. szakasz, GYV-2)`
- OLD-b: `a „passz” és egy mondat arról, kit vonna be, teljes értékű válasz` → NEW-b: `a „passz” és egy mondat arról, kit vonna be és mit nem kezdene el, teljes értékű válasz`
- Együtt mozgó helyek: D08-1
- Címkék: BUILD-INPUT (manifest)
- Indoklás: a manifest a lecke passz-szövegét idézi.

### D-13 (d) – csoportos titoktartási norma

### D13d-1 — M2.A :177
- Fájl: 02 Tervezet/Modulok/M2/Peulák/M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md:177
- Alap: HUM 14 GYV-21 `A`; mérce: M2.B:370 („Ne írj nevet (elég a szerep), és olyan részletet se, amelyből felismerhető, kiről van szó.”); irány D-13 (adattakarékosság)
- Hatáskör: PROJEKTGAZDA (vétó/QA: Memuna + DPO)
- OLD: `* „Amit itt hallunk, az **nem kerül ki** névvel a teremből – kivéve`
- NEW: `* „Amit itt hallunk, az **nem kerül ki** névvel a teremből, és felismerhető részlettel sem – kivéve`
- Együtt mozgó helyek: D13d-4 (a :123 spec szó szerint idézi)
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: csak szigorítás. A Memuna-kivétel érintetlen.

### D13d-2 — M2.A :410
- Fájl: ugyanaz:410
- Alap / Hatáskör: mint a D13d-1-nél
- OLD: `Senki más történetét ne vigyétek ki névvel.”`
- NEW: `Senki más történetét ne vigyétek ki névvel, és felismerhető részlettel sem.”`
- Együtt mozgó helyek: D13d-3
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: GYV-21 („ténylegesen nem visszaazonosítható”).

### D13d-3 — M2.A :409 képzői megjegyzés
- Fájl: ugyanaz:409
- Alap / Hatáskör: mint a D13d-1-nél
- OLD: `(**fontos: senki más történetét ne vigyék ki névvel**)`
- NEW: `(**fontos: senki más történetét ne vigyék ki névvel, és felismerhető részlettel sem**)`
- Együtt mozgó helyek: D13d-2
- Címkék: LÁTHATÓ SZÖVEG
- Indoklás: a képzői utasítás és a kimondott mondat ne térjen el egymástól (7. regressziós minta).

### D13d-4 — M2.A-POSZ-01 spec
- Fájl: ugyanaz:123 (`@asset` „spec”)
- Alap / Hatáskör: mint a D13d-1-nél
- OLD: `„Amit itt hallunk, az nem kerül ki névvel a teremből – kivéve`
- NEW: `„Amit itt hallunk, az nem kerül ki névvel a teremből, és felismerhető részlettel sem – kivéve`
- Együtt mozgó helyek: D13d-1; generált kimenetek (build)
- Címkék: BUILD-INPUT (@asset)
- Indoklás: a spec szó szerint idézi a :177-et.

---

### D-09 – a 24 órás határidő és a gyermekvédelmi út elválasztása

**Megállapítás:** a mostani szöveg nem mondja ki egyértelműen az elválasztást. A KAPU:24 a 24 órás határidőt a „Teljesítve” tartalmi kritériumához köti, tehát kapuértékelési megerősítésként írja le. A KAPU:203 külön akut utat ad a tanulónak: „Ha egy valós gyermekvédelmi helyzetet jelezned kell, azt ne ebben a jegyzetben tedd: azonnal vond be a Memunát”. Sehol nem áll viszont, hogy a 24 órás átnézés nem gyermekvédelmi figyelés. Az LMS-M2-05 manifest-sorában (MAN:60) nincs olyan mondat, mint az LMS-M2-09-nél (MAN:57: „nem folyamatosan figyelt gyermekvédelmi jelzőcsatorna”). Ezért vetette el a verifier a B7-ben. A tisztázó mondat kell; a határidő nem változik.

### D09-1 — KAPU §0 „Megerősítés” sor
- Fájl: 02 Tervezet/Modulok/M2/M2 – Kapu – értékelő (item-bank + rubrika).md:24
- Alap: HUM 14 GYV-1 `F` („egyébként ott is világos, külön akut jelzési út legyen”); HUM:220 (a 24 órás határidő, változatlan); irány D-09
- Hatáskör: PROJEKTGAZDA (irány D-09; a határidő változatlan; vétó/QA: Memuna (HUM-SAFE-01), DPO / jogi felelős; a GYV-1 Memuna- és DPO-QA-ja bizonyíték-kapu, BK-13). Ha a hívó új GYV-1-alkalmazásnak minősíti, akkor SZEREP: Memuna.
- OLD: `a puha kapu rubrika-küszöbe formatív, nem feltétel (Program terv §5). |`
- NEW: `a puha kapu rubrika-küszöbe formatív, nem feltétel (Program terv §5). A 24 órás határidő a kapuértékelés megerősítésére szól, nem gyermekvédelmi figyelésre: a jegyzet nem gyermekvédelmi jelzőcsatorna, és a határidő a gyermekvédelmi jelzések kezelésére nem vonatkozik. Valós gyermekvédelmi helyzetben a külön akut út érvényes: azonnal a Memuna (D. szakasz bevezetője). |`
- Együtt mozgó helyek: D09-2. A tanulói :203 nem változik, mert már tartalmazza az akut utat.
- Címkék: nem VÉTÓLISTÁS (határidő, completion és küszöb változatlan). Stábszöveg, a tanulói Assignment-leírásba nem kerül (§0 kimarad, :26).
- Indoklás: új mentori kötelezettséget vagy ígéretet nem tesz. A GYV-1 mintája szerint garancia jellegű mondatot az M2-ben nem írunk.

### D09-2 — MAN LMS-M2-05
- Fájl: 02 Tervezet/LMS – activity manifest.md:60
- Alap / Hatáskör: mint a D09-1-nél
- OLD: `(M2 KAPU C.: „ne mutasd osztályzatként”; a rejtés Moodle-beállításának nevét stagingben kell igazolni) |`
- NEW: `(M2 KAPU C.: „ne mutasd osztályzatként”; a rejtés Moodle-beállításának nevét stagingben kell igazolni); a KAPU §0 24 órás megerősítési határideje kapuértékelési megerősítés, nem gyermekvédelmi figyelés: az LMS-M2-05 nem gyermekvédelmi jelzőcsatorna, valós gyermekvédelmi helyzetben a KAPU D. szakaszának külön akut útja érvényes (azonnal a Memuna); a határidő változatlan (HUM 14. szakasz, GYV-1; vétó/QA: Memuna, DPO/jogi felelős) |`
- Együtt mozgó helyek: D09-1
- Címkék: BUILD-INPUT (manifest)
- Indoklás: ugyanaz a minta, mint az LMS-M2-09-nél (MAN:57).

---

## Kiegészítés a célzott QA után (`9788c05`)

A `8bb4d7d` célzott QA-ja (QA17; riport: `2026-10-13 Célzott QA – D-csomagok átvezetése (8bb4d7d), AP-2026-10-13-01.md`) után ehhez a szerephez került tételek. A javasolt szöveg helyett itt a döntési kérdés áll; a javító commit nem implementálta őket.

- **KANON:QA17-BIZT-7 (a programvezetővel; adatkör: DPO):** láthatja-e a mentor a pontkönyvben a saját csoportja egyéni LMS-M0-06-pontszámát (GYV-23)? Ma a runtime acceptance 15. pontja ezt nyitott várt eredményként jelöli; a döntés után a várt eredmény beírható. Bizonyíték: a pontkönyv a kurzus csoportmódja szerint szűr, a `moodle/grade:viewall` a nem szerkesztő tanári szerepnek alapból megvan.
- **M3:QA17-IMPL-1 (QA a projektgazda döntéséhez):** a D-08 (b) címmegjelenítése a h5p-branching-scenario forrása szerint Branching Question-csomópontnál nem működik a `showContentTitle`-lel. Ha a projektgazda más megjelenítési módot választ (például a szitu meglévő címe a megelőző csomóponton, vagy külön címcsomópont), a Memuna QA-ja: a cím ott sem megterhelő-e. A §7.1 kérdése és a két opció nem változik.
- **KANON:QA17-BIZT-6 (bizonyíték):** a D-11 mechanizmusa most kimondja az ADV-2 szerinti „Memuna szükség esetén” hozzáférést (Adatvédelem :139, RA 15). A Memuna szerepéről a Memuna dönt (ADV-2); ehhez a G1-ellenőrzésben elég az „egyetértek / módosítás kell”.
