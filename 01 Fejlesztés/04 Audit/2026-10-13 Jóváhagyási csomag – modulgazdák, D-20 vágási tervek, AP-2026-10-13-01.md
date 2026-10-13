# Jóváhagyási csomag – modulgazdák (M0, M2, M3, M4, M5, M6, M7), vétó/QA: programvezető (AP-2026-10-13-01)

> **Audit trail, nem kánon.** Előre kitöltött elfogadási javaslat a 2026-10-13-i futásból. A projektgazda irányait a
> `02 Tervezet/Emberi jóváhagyás szükséges.md` 15. szakasz rögzíti; ahol a döntés vagy a jóváhagyás a címzett szerep hatásköre, az irány **nem helyettesíti** az ő
> döntését. A javasolt szövegek tervezetek: a tananyagba csak az írásos elfogadás után kerülnek, `/course-fix`-szel.
> A tervezeteket read-only szakértői ügynökök készítették, a fő session ellenőrizte; a sorszámok a `8bb4d7d` körüli
> állapotra vonatkoznak, átvezetéskor újra ellenőrizzük őket.

Címzett: az érintett modulgazdák; az M3.B-nél a Memuna bevonásával. A percek vétólistás időtartamok: a jóváhagyásig nem változnak. A lezárt PRG-1 a 45 perces peulablokkokat és a központi naptárt köti; ahol a belső blokkhatár sem tartható a védett lépések rövidítése nélkül, a terv A- és B-változatot ad.

## Hogyan válaszolj

- Tételenként: **ELFOGADOM** / **MÓDOSÍTOM: …** / **VÉTÓ**, dátummal és szerepnévvel. A repó nyilvános: személynév,
  személyes adat ne kerüljön a válaszba vagy az issue-ba.
- Elfogadásnál a javasolt szöveg (a „DPO tölti ki”, „Memuna dönt” mezők kitöltésével) a következő engedélyezett javítási körben
  kerül be; vétónál a mostani szöveg marad, és az érintett 14. szakaszbeli sor `REOPENED`.
- Az elfogadás nem release-jóváhagyás: a G1–G8 kapuk bizonyítéka és a go/no-go döntés külön lépés (`02 Tervezet/RELEASE-READINESS.md`).
- Peulánként: ELFOGADOM (A-változat / B-változat) / MÓDOSÍTOM / VÉTÓ; a nyitott kérdéseket a táblázatok jelölik.

## Tételek

| Tétel | Mit kérünk | Kapcsolódó ledger-kulcsok / kapu |
|---|---|---|
| D-20 | lépésszintű vágási terv: M0.A, M2.A, M2.B, M2.F, M3.A, M3.B, M3.F, M4.A, M4.B, M5.A, M5.B, M5.F, M5.1, M6.A, M7.A, M7.B, M7.F | M0:PED-5, M2:PED-G3-1, M3:PED-G3-1, M4:PED-G2-2, M4:NYELV-G2-6, M5:PED-G2-6, M5:QA-PED-2, M6:PED-G3-1, M7:PED-G3-1 |
| D-21 | a közös 1–5 fős F-peula keret `/course-develop` terve (külön dokumentum; projektgazdai elfogadásra) | M3:ERT-G3-10; X-8 |
| D-03 (vétó/QA) | az M3.A/M3.B kártyaduplikálás (megvalósítva); nyitott: a 8 fős csoportosítás (két csoport = két eset) | M3:QA14-NYELV-13, M3:IMPL-G3-9 |
| D-22 (vétó/QA) | az M7.B „átjárás” logisztikai olvasata (megvalósítva) | M7:NYELV-G3-12 |
| D-19 (a), (c) | kimeneti célok (az értékelési felelőssel; szöveg az értékelési csomagban) | M5:PED-G1-10, M2:QA14-ERT-2 |

## Részletes javaslatok

### D-20 – M0, M2, M3

### D-20 (PRG-1 `A`): lépésszintű vágási terv a modulgazdáknak (M0.A · M2.A · M2.B · M2.F · M3.A · M3.B · M3.F)

Mind a hét peula elkészült. Fájlt nem módosítottam. Minden perc VÉTÓLISTÁS: a modulgazda jóváhagyásáig semmi nem változik.

### Röviden

1. **Hat peula túlcsordul, egy épp határon van.** Hat peula úgy, hogy a védett lépéseket nem rövidítjük, csak a 45’-es (az M0.A-nál a 60’-es) keretbe fér bele. Az M2.F most 44–46’, a terv szerint 44–45’.

2. **Négy esetben a belső blokkhatárokat is mozgatni kell, 1–2 perccel.** Ez az M0.A 45’-es változata, az M2.A, az M2.B és az M3.F. Ezekben a záróblokk védett lépései maguk is túllógnak, ezért a blokkhatárok tartása és a védett lépések érintetlensége egyszerre nem teljesül.
   - A HUM 14 PRG-1 szövege csak a „45 perces peulablokkokat és a központi naptárt” rögzíti.
   - A „blokkhatárok tarthatók legyenek” megkötés a D-20 csomag saját keretezése, nem a döntés szövege.
   - A javasolt határmozgatás mindenhol a kánonban már kijelölt vágási terület terhére megy:
     - M0.A: :648
     - M2.A: :468
     - M2.B: :445
     - M3.F: :556

3. **Eltérések a G9 javaslatától:**
   - **M0.A 45’:** a G9 a 45’-es határokat rendben lévőnek tartotta. Valójában a Blokk 4 csak 13’, a védett lépései viszont 14–15’-et igényelnek. Lásd PED-1.
   - **M2.A:** a G9 a 4.4.1 nagykört (feldolgozó lépés) rövidítené. Én ezt határmozgatással elkerülöm.
   - **M2.B:** a G9 szerint „a képző utolsóként mondja el a saját vállalását”. Ez nincs a mostani szövegben, új elem lenne, ezért nem veszem át.
   - **M3.F:** a G9 ezt a peulát nem olvasta.

| Peula | Keret | Most (lépéspercek összege) | Javasolt | Blokkhatár változik? | Jóváhagyó (vétó/QA: programvezető) |
|---|---|---|---|---|---|
| M0.A | 60’ (45’-es változat) | 58–72’ (45’-nél a Blokk 4 13’, védett igény 14–15’) | 55–60’ / 42–45’ | 60’: nem / 45’: igen | M0 modulgazda |
| M2.A | 45’ | kb. 51,5–59,5’ | 43,5–44,5’ | igen (15→13, 30→28, 40→38) | M2 modulgazda |
| M2.B | 45’ | 47–48’ | 45’ | igen (20→18, 35→33) | M2 modulgazda |
| M2.F | 45’ | 44–46’ (+opció) | 44–45’ | nem | M2 modulgazda |
| M3.A | 45’ | 48–56’ | 42–45’ | nem | M3 modulgazda |
| M3.B | 45’ | 48–56’ | 41–45’ | nem | M3 modulgazda + Memuna |
| M3.F | 45’ | 45–50’ | 43–45’ | igen (40→38) | M3 modulgazda |

Jelölés: **V** = védett lépés, a perce nem csökken. A „sávon belül” azt jelenti, hogy a lépés saját kánoni percsávjának alsó értékét választom, a szöveg változatlan. Ahol egy lépésnek nincs percszáma, ott szószám alapján becsültem (kb. 130 szó/perc); ezt mindenhol jelzem.

---

### D20-M0A — M0.A vágási terv (60’ és 45’)
- Fájl: `02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md`
- Alap: HUM 14 PRG-1; D-20 irány; a kánon vágási sorrendje: :647–650
- Hatáskör: SZEREP: M0 modulgazda (vétó/QA: programvezető)
- Címkék: VÉTÓLISTÁS · LÁTHATÓ SZÖVEG · nincs VO, nincs @asset-módosítás

**Jelenlegi összeg (60’-es változat):**

| Blokk | Keret | Lépéspercek |
|---|---|---|
| B1 | 10’ | nincs lépésperc |
| B2 | 15’ | 16–21’ (:341–360) |
| B3 | 15’ | 13–18’ (:421–448) |
| B4 | 15’ | 15–17’ (4.4.1: 8–10’ a 8’-ben; 4.4.2: 7’-es ablak) |
| B5 | 5’ | 4–6’ |
| **Összesen** | **60’** | **58–72’** |

A 45’-es változatnak (:154–158) nincs lépésszintű bontása, és a Blokk 4-et 13’-re szűkíti.

**Védett lépések** (:650 és PRG-1):
- B2 biztonsági keret
- B3 „Madrih, nem terapeuta”
- a teljes B4: „Kihez fordulhatok?” térkép, mini-reflexió, zárókör az indulószavak rögzítésével

| Lépés | Most | Javasolt 60’ | Javasolt 45’ | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|---|
| B1 Név + 1 szó | 10 | 10 | 6 | 45’: „rövidített kör”, a „miért” mondat nélkül | – | :154 maga írja |
| B2/1 Biztonsági keret | 1–2 | 1–2 | 1–2 | – | V | |
| B2/2 Csoportalakítás | 2 | 1 | 1 | leszámolás, azonnal | – | |
| B2/3 Plakát | 8–10 | 8 | 5 | 45’: kulcsszavak | – | |
| B2/4 Kiscsoportos megosztás | 3–4 | 3 | 2 | – | – | a kánon ezt nevezi meg vágásra (:648) |
| B2/5 Plenáris körbenézés | 2–3 | 1 | 0 → a B3 első mondata | 60’: a :349 nagy létszámú módja (körbesétálás és olvasás) + 1 összegző mondat; 45’: a plakátok kint maradnak, az összegzés a B3 nyitánya | – | :648; a :155 is „gyorsabb plenáris összegzés”-t ír |
| B3/1 Flipchart | 1–2 | 1 | 1 (az összegzéssel együtt) | az M0.A-POSZ-01 sablon már előre kint van | – | |
| B3/2 Ötletelés | 8–10 | 8–9 | 4 | 45’: a :439 kész példáival indul | – | :156 |
| B3/3 „Madrih, nem terapeuta” | 3–4 | 3–4 | 3–4 | – | V | :650 |
| B3/4 Közös „igen” | 1–2 | 1 | 1 | – | – | |
| B4 4.4.1/1 Poszter rajzolása | 1–2 | 0 | 0 | **kérdés:** az M0.A-POSZ-02 sablon kitehető-e a peula előtt? | (V blokk, a lépés logisztikai) | a térkép tartalma és a közös kitöltés változatlan |
| B4 kitöltés + mini-reflexió + zárókör | 5–6 + 2 + 7 | változatlan | változatlan | – | V | PRG-1 |
| B5/1+2 Cetli kiosztása + két kérdés | 1 + 2–3 | 3 | 3 | az instrukció kiosztás közben hangzik el | – | |
| B5/3 Híd | 1–2 | 1–2 | 1 | – | – | |
| **Összesen** | 58–72 | **55–60** | **42–45** | | | |

A 45’-es változat új határai: 0–6 / 6–16 / 16–26 / **26–41 (B4 = 15’)** / 41–45. Ha a modulgazda a poszter előzetes kitételét elveti, a 60’-es Blokk 4 15–16’ lesz; ekkor a B1 0–9’-re rövidül.

**Szövegszintű következmény** (VÉTÓLISTÁS, jóváhagyásig nem változik):

| Sor | OLD (szó szerint) | NEW (tervezet) |
|---|---|---|
| :153 | `rész marad a leghosszabb, csak minimálisan rövidül` | `rész marad a leghosszabb, és nem rövidül` (PRG-1) |
| :154 | `**0–7’** – Ráhangolódás` | `**0–6’** – Ráhangolódás` |
| :155 | `**7–17’** – Blokk 2` | `**6–16’** – Blokk 2` |
| :156 | `**17–27’** – Blokk 3` | `**16–26’** – Blokk 3` |
| :157 | `**27–40’** – Blokk 4` / `(**prioritás, csak minimálisan rövidül**)` | `**26–41’** – Blokk 4` / `(**prioritás, nem rövidül**)` |
| :158 | `**40–45’** – Kilépőkártya` | `**41–45’** – Kilépőkártya` |
| :344 | `2. **Kiscsoportok kialakítása (2 perc)**` | `(1 perc)` |
| :351 | `3. **Plakátkészítés (8–10 perc)**` | `(8 perc)` |
| :357 | `4. **Rövid kiscsoportos megosztás (3–4 perc)**` | `(3 perc)` |
| :360 | `5. **Plenáris „körbenézés” (2–3 perc)**` | `(1 perc)` |
| :421 | `1. **Közös flipchart címmel (1–2 perc)**` | `(1 perc)` |
| :425 | `2. **Közös ötletelés nagykörben (8–10 perc)**` | `(8–9 perc)` |
| :448 | `4. **Közös „igen” (1–2 perc)**` | `(1 perc)` |
| :473 | `1. **Tábla / poszter rajzolása (1–2 perc)**` | modulgazdai döntés után: előkészítési lépés |
| :589 / :591 | `1. **Cetlik kiosztása (1 perc)**` / `2. **Két kérdés a cetlire (2–3 perc)**` | összevonva: `(3 perc)` |
| :651 | `Ha 45 percre kell vágni, gondold át előre, hol rövidítesz.` | ide kerül a jóváhagyott 45’-es lépésterv |

**Kérdés a programvezetőnek:** a HUM-OPS-01 szerint „az M0 sávja 60–80 perc”. Ütemez-e a naptár egyáltalán 45’-es M0.A-t? Ha nem, a 45’-es változat elhagyható.

---

### D20-M2A — M2.A vágási terv
- Fájl: `02 Tervezet/Modulok/M2/Peulák/M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md`
- Alap: PRG-1; kánoni vágási terület: :468 („az identitás-vonalból rövidítek”); a feldolgozó kör vagylagossága: :469
- Hatáskör: SZEREP: M2 modulgazda (vétó/QA: programvezető)
- Címkék: VÉTÓLISTÁS · LÁTHATÓ SZÖVEG

**Jelenlegi összeg:**

| Blokk | Keret | Lépéspercek |
|---|---|---|
| B1 | 5’ | 2–3’ + nem percezett részek, becslés kb. 5’ |
| B2 | 10’ | 10,5–12,5’ |
| B3 | 15’ | 20–25’ |
| B4 | 15’ | 16–17’ (4.4.1: 10’; 4.4.2: 6–7’ az 5’-ben) |
| **Összesen** | **45’** | **kb. 51,5–59,5’** |

**Védett lépések:**
- B1 megosztási szabályok és a „Ha ez a téma téged is érint” keret
- B2 biztonsági keret
- páros megosztás (:469)
- 4.4.1 feldolgozó kör
- zárókör

| Lépés | Most | Javasolt | Mit rövidít | V? | Indok |
|---|---|---|---|---|---|
| B1 (minden) | ~5 | 5 | – | V | |
| B2/1 Tér kijelölése | 1–2 | 1 | a szalag előre lerakva, az instrukció elhangzik | – | |
| B2/2 Keret | 0,5 | 0,5 | – | V | |
| B2/3 Állítások | 8–9 | 5–5,5 | mind a 8 állítás marad; magyarázó kérdés legfeljebb 1–2-re; a 3 GYV-20-as állítás fejben vagy papíron | – | :468 |
| B2/4 Mini-lezárás | 1 | 1 | – | – | |
| B3/1 Rajzolás | 5–7 | 4 (3, ha megvan az M2.1-es térkép) | csak frissítés vagy egyszerű változat | – | |
| B3/2 Párok | 2 | 1 | – | – | |
| B3/3 Páros megosztás | 10–12 | 10 (2×5) | sávon belül | V | |
| B3/4 Mini-reflexió | 3–4 | **kérdés:** 0 vagy 3 | a :469 szerint vagylagos a 4.4.1-gyel; a :377 kapcsolómondat a 4.4.1 elejére kerül | V? | lásd lent |
| B4 4.4.1 (1+6+3) | 10 | 10 | – | V | |
| B4 4.4.2 (1+4–5+1) | 6–7 | 6–7 | – | V | |
| **Összesen** | | **43,5–44,5** | | | |

Új határok: 5–13 / 13–28 / 28–38 / 38–45.

**Kérdés a modulgazdának, programvezetői vétóval:** a :469 („a feldolgozó kört (a mini-reflexiót vagy a 4.4.1 kiscsoportos feldolgozást) … nem hagyom el”) a PRG-1 alatt is megengedi-e a mini-reflexió elhagyását?
- Ha nem: a B2 6’-re szűkül (5–11), a B3 18’ lesz (11–29), a B4 16’ (29–45). Ekkor a 4.4.2 záró üzenete a kör utolsó mondataként hangzik el. 20 fő körül kb. ½’ kockázat marad.

**Szövegszintű következmény** (VÉTÓLISTÁS):

| Sor | OLD | NEW |
|---|---|---|
| :73 | `**5–15’** – Identitás-vonal játék` | `**5–13’**` |
| :74 | `**15–30’** – Identitástérkép frissítése` | `**13–28’**` |
| :75 | `**30–40’** – Kiscsoportos feldolgozás` | `**28–38’**` |
| :76 | `**40–45’** – Zárókör` | `**38–45’**` |
| :199 / :235 | `„Identitás-vonal” játék (5–15’)` / `**Időtartam:** 5–15’` | `5–13’` |
| :245 | `1. **Tér kijelölése (1–2 perc)**` | `(1 perc)` |
| :252 | `3. **Állítások felolvasása (8–9 perc)**` | `(kb. 5 perc)` |
| :290 / :326 | `páros megosztás (15–30’)` / `**Időtartam:** 15–30’` | `13–28’` |
| :336 | `1. **Egyéni rajzolás / frissítés (5–7 perc)**` | `(4 perc; ha megvan az M2.1-es térkép, 3)` |
| :353 | `2. **Párok kialakítása + szerepek (2 perc)**` | `(1 perc)` |
| :356 / :364 | `– 2×5–6 perc (10–12 perc)**` / `5–6 perc után a képző jelzi a cserét` | `– 2×5 perc (10 perc)**` / `5 perc után …` |
| :367 | `4. **Mini-reflexió nagykörben (3–4 perc)**` | a kérdés eldöntése után |
| :381 / :384 / :386 / :414 | `(30–45’)` · `**Időtartam:** 30–45’` · `(30–40’)` · `(40–45’)` | `28–45’` · `28–38’` · `38–45’` |

Ellentmondó mondat: :254 (lásd PED-6). Független objektív javítás, nem perc.

---

### D20-M2B — M2.B vágási terv
- Fájl: `02 Tervezet/Modulok/M2/Peulák/M2.B – Somer-értékek a gyakorlatban – döntések, amelyek tanítanak.md`
- Alap: PRG-1; kánoni vágási terület: :445 („az Érték-szigetek helyzetek számát csökkentem, de a pillér-sztori műhely és a vállalás-kör marad”)
- Hatáskör: SZEREP: M2 modulgazda (vétó/QA: programvezető)
- Címkék: VÉTÓLISTÁS · LÁTHATÓ SZÖVEG · BUILD-INPUT (@asset M2.B-MUNK-02 spec, :402, `media_manifest.py build`)

**Jelenlegi összeg:**

| Blokk | Keret | Lépéspercek |
|---|---|---|
| B1 | 5’ | nincs lépésperc |
| B2 | 15’ | 3 + 10 + 2 = 15’ |
| B3 | 15’ | 3 + 7 + 5 = 15’ (4–5 csoportnál a bemutatás 5–6’ → 15–16’) |
| B4 | 10’ | 5 + 5 + 2 = 12’ |
| **Összesen** | **45’** | **47–48’** |

**Védett lépések:**
- B2/1 biztonsági keret
- B4/1 egyéni reflektív írás
- B4/2 vállalás-kör a kötelező beadandó-infóval (:386)

| Lépés | Most | Javasolt | Mit rövidít | V? |
|---|---|---|---|---|
| B2/1 Szigetek + keret | 3 | 2 | a szigetkártyák előre kint; az instrukció és a keret szövege változatlan | V (szöveg) |
| B2/2 Helyzetek | 10 | 10 | – | – |
| B2/3 Mini-összegzés | 2 | 1 | – (a szöveg kb. 25 mp) | – |
| B3 (3+7+5) | 15 | 15 (4–5 csoportnál 16) | – | – |
| B4/1 Írás | 5 | 5 | – | V |
| B4/2 Vállalás-kör | 5 | 5 | – | V |
| B4/3 Záró üzenet | 2 | 2 (4–5 csoportnál 1) | – | – |
| **Összesen** | 47–48 | **45** | | |

Új határok: 5–18 / 18–33 / 33–45. Négy-öt csoportnál: 18–34 / 34–45.
- Alternatíva, csak 12 fő alatt és a határok tartásával: a :387 záró üzenet szövege változatlanul a vállalás-kör végén hangzik el. Ez 10,5–11’ a 10’-ben.

**Szövegszintű következmény** (VÉTÓLISTÁS):

| Sor | OLD | NEW |
|---|---|---|
| :75–77 | `**5–20’**` · `**20–35’**` · `**35–45’**` | `5–18’` · `18–33’` · `33–45’` |
| :142 / :178 | `gyakorlat 1 (`5–20’`)` / `**Időtartam:** `5–20’`` | `5–18’` |
| :219 / :321 | `(`20–35’`)` / `**Időtartam:** `20–35’`` | `18–33’` |
| :356 / :359 | `(`35–45’`)` / `**Időtartam:** `35–45’`` | `33–45’` |
| :187 | `1. **Szigetek kijelölése + biztonsági keret (kb. 3’)**` | `(kb. 2’)` |
| :213 | `3. **Mini-összegzés (kb. 2’)**` | `(kb. 1’)` |
| :444 | `Blokk-idők: 0–5’ / 5–20’ / 20–35’ / 35–45’` | `0–5’ / 5–18’ / 18–33’ / 33–45’` |
| :402 (@asset) | `(0–5'/5–20'/20–35'/35–45')` | build úton, együtt mozog |

---

### D20-M2F — M2.F vágási terv
- Fájl: `02 Tervezet/Modulok/M2/Peulák/M2.F – Felzárkóztató peula – Identitás, értékek, pillérek, személyes példamutatás (Study Lab).md`
- Alap: PRG-1; G9 (belépés érkezéskor); :388–389 („szent idő”, „a záró üzenetet nem hagyom el”)
- Hatáskör: SZEREP: M2 modulgazda (vétó/QA: programvezető). Ha az érkezéskori belépés naptári időt igényel, az a programvezető kérdése.
- Címkék: VÉTÓLISTÁS · LÁTHATÓ SZÖVEG

**Jelenlegi összeg:**

| Blokk | Keret | Lépéspercek |
|---|---|---|
| B1 | 5’ | nincs lépésperc |
| B2 | 20’ | 5 + 10 + 5 = 20’ |
| B3 | 15’ | 3 + 5 + 4 + 3 = 15’ |
| B4 | 5’ | 2–3 + 2–3 = 4–6’ (+ opció 1–2’) |
| **Összesen** | **45’** | **44–46’** |

**Védett lépések:**
- B2 csendes pótlás
- B4 mini-kör, záró üzenet és híd

| Lépés | Most | Javasolt | Mit rövidít / átrendez | V? |
|---|---|---|---|---|
| (érkezés) Moodle-belépés | – | érkezéskor | a B2/1 belépése előre kerül; **kérdés:** megoldható-e érkezéskor | – |
| B2/1 Belépés + fókusz | 5 | 2 | ellenőrzéssé szűkül | – |
| B2/2 Csendes munka | 10 | 13 | a felszabaduló idő a védett pótlásé | V |
| B2/3 Jegyzetlap | 5 | 5 | – | – |
| B3 | 15 | 15 | – | – |
| B4/1 Mini-kör | 2–3 | 2 | a :318-ban már meglévő „vagy csak 5–6 önkéntes” változat 10 fő fölött | V (a változat kánoni) |
| B4/2 Záró üzenet + híd | 2–3 | 2–3 | – | V |
| B4/3 Opció | 1–2 | csak ha marad idő | – (már most is így szól) | – |
| **Összesen** | 44–46 | **44–45** | | |

Szövegszintű következmény (VÉTÓLISTÁS):
- :203 `1. **Technikai belépés + fókusz választása (kb. 5’)**` → `(kb. 2’)`
- :205 `Mindenki lépjen be a Moodle-be, és` → `Aki még nem lépett be a Moodle-be, most lépjen be, és`
- :208 `2. **Csendes online munka (kb. 10’) – fülessel**` → `(kb. 13’)`
- :314 `(kb. 2–3’)` → `(kb. 2’)`
- :52 `(mindenki a saját fiókjával lép be)` → kiegészítés az érkezéskori belépéssel, modulgazdai döntés szerint

Ellentmondó mondatok:
- :141 ↔ :203 (lásd PED-4).
- Ha a belépés érkezéskor nem oldható meg, alternatíva: a belépés a B1 első 1–2 perce, a B1 privát felmérése ekkor 3’.

---

### D20-M3A — M3.A vágási terv
- Fájl: `02 Tervezet/Modulok/M3/Peulák/M3.A – Találd ki, hol tart a kvuca! – Történetek Tuckman szemüvegén át.md`
- Alap: PRG-1; D-03 irány (meglévő kártyák duplikálása); PRG-11, PRG-16 (közös átbeszélés 3 kártyán)
- Hatáskör: SZEREP: M3 modulgazda (vétó/QA: programvezető)
- Címkék: VÉTÓLISTÁS · LÁTHATÓ SZÖVEG · az M3 hub (:155–162) nem változik

**Jelenlegi összeg:**

| Blokk | Keret | Lépéspercek |
|---|---|---|
| B1 | 5’ | nincs lépésperc |
| B2 | 15’ | 2–3 + 1–2 + 5 + 8–12 = 16–22’ |
| B3 | 15’ | 2 + 10 + 5–7 = 17–19’ |
| B4 | 10’ | 8 + 2 = 10’ |
| **Összesen** | **45’** | **48–56’** |

**Védett lépések:**
- a mini-megbeszélésben a „külön” állás megbeszélése (:276)
- a B3/3 közös átbeszélés a „Storming vagy kortárs bántalmazás?” elhatárolással (:442)
- zárókör és híd

| Lépés | Most | Javasolt | Mit rövidít | V? |
|---|---|---|---|---|
| B2/1 Emlékeztető | 2–3 | 1–2 | az idővonal-poszter előre kint; a 4 sor felolvasása | – |
| B2/2 Csoportok | 1–2 | 1 | – | – |
| B2/3 Szobor | 5 | 4 | – | – |
| B2/4 Bemutatás | 8–12 | 8 (4×2’) | mini-megbeszélés kb. 45 mp, ahogy a :311 már írja | részben V: a „külön” állás megbeszélése nem rövidül |
| B3/1 Kiosztás | 2 | 1 | **kérdés:** a B2 négy kiscsoportja (3–5 fős) maradhat-e? A kártyák előre kiosztva | – |
| B3/2 Párosítás | 10 | 7 | csoportonként 2 kártya (4 csoport × 2 = egy 8-as szett; 5 csoporttól a második példány a D-03 szerint) | – |
| B3/3 Átbeszélés | 5–7 | 5–7 | – | V |
| B4 (8+2) | 10 | 10 | – | V |
| **Összesen** | 48–56 | **42–45** | | |

**Szövegszintű következmény** (VÉTÓLISTÁS):

| Sor | OLD | NEW |
|---|---|---|
| :235 | `#### 1. Rövid emlékeztető Tuckmanre (2–3’)` | `(1–2’)` |
| :251 | `#### 2. Kiscsoportok & szakaszkiosztás (1–2’)` | `(1’)` |
| :262 / :266 | `#### 3. Csoportszobor készítése (5’)` / `„Van 5 percetek, hogy` | `(4’)` / `„Van 4 percetek, hogy` |
| :295 | `(kb. 2–3’ × 4 csoport = 8–12’)` | `(kb. 2’ × 4 csoport = 8’)` |
| :306 | `6. Rövid mini-megbeszélés (1 perc)` | `(kb. 45 mp; a „külön” állás megbeszélése nem rövidül)` |
| :311 | `A blokk így marad az 5–20’ keretben.` | `Így a blokk 14–15 perc (emlékeztető 1–2’, kiscsoportok 1’, szobor 4’, bemutatás 4 × 2’), és belefér az 5–20’ keretbe.` |
| :393 | `#### 1. Kiscsoportok & kártyák kiosztása (2’)` | `(1’)` |
| :396 | `Minden kiscsoport kap **2–3 kvuca-sztori kártyát**` | `**2 kvuca-sztori kártyát**`; a D-03 átvezetésével egy menetben |
| :444 | `#### 2. Kiscsoportos munka – párosítás (10’)` | `(7’)` |
| :566 | `de a zárókört **nem hagyom el** (max. rövidítem a kör hosszát)` | `de a zárókört **nem hagyom el és nem rövidítem**` (PED-5) |

A G9 a :309-es hamis mondatra hivatkozott; ez ma a :311 (PED-2).

---

### D20-M3B — M3.B vágási terv (a Memunával)
- Fájl: `02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépéstérkép.md`
- Alap: PRG-1; :471 (a 4.3.3 az első elhagyható lépés, de a „Fontos különbség” akkor is elhangzik); D-03 irány (a negyedik eset marad a 4.3.3-ban; 4 csoporttól az 1–3. eset duplán, visszahozás esetenként); PRG-12
- Hatáskör: SZEREP: M3 modulgazda + Memuna (vétó/QA: programvezető). A Memuna írásos átnézése külön bizonyíték-kapu (fejléc :133; G1).
- Címkék: VÉTÓLISTÁS · LÁTHATÓ SZÖVEG · biztonságkritikus · az M3 hub (:206–215) nem változik

**Jelenlegi összeg:**

| Blokk | Keret | Lépéspercek |
|---|---|---|
| B1 | 5’ | nincs lépésperc |
| B2 | 20’ | 2–3 + 2 + 5–7 + kb. 12 = 21–24’ |
| B3 | 15’ | 2 + 10–12 + 5–8 = 17–22’ |
| B4 | 5’ | nincs lépésperc; becslésem 20 főnél 4–5,5’, mert a :511–515 kapu-infó kb. 150 szó |
| **Összesen** | **45’** | **48–56’** |

**Védett lépések** (mind a biztonsági réteghez tartozik):
- 4.2.1 keret, szó szerinti felolvasással
- „Ha valakit megérint a téma” (in-the-moment)
- harmadik személyű feldolgozási mód
- 4.2.4 „Fontos különbség”, zárómondat, leállító mondat
- 4.3.2 öt kötött lépés valódi helyi nevekkel
- B4 zárókör, lezáró biztonsági mondat, híd a kapuhoz

| Lépés | Most | Javasolt | Mit rövidít | V? |
|---|---|---|---|---|
| 4.2.1 Keret | 2–3 | 2–3 | – | V |
| 4.2.2 Kiosztás | 2 | 1 | a kártyák csoportonként előkészítve | – |
| 4.2.3 Feldolgozás | 5–7 | 5–6 | sávon belül | – |
| 4.2.4 Visszahozás | kb. 12 | kb. 10 (3 eset × 3–3,5’) | esetenként, nem csoportonként (a D-03 szerint); a duplikált esetnél a második csoport csak az eltérést mondja | részben V: a „Fontos különbség” és a zárómondat teljes |
| 4.3.1 Bevezetés | 2 | 1–2 | – | – |
| 4.3.2 Lépések | 10–12 | 10–12 | – | V |
| 4.3.3 Gyors alkalmazás | 5–8 | 0–3 (időszelep) | **kérdés a Memunának és a modulgazdának:** 2–3’-nél kiscsoport helyett plenáris futtatás a 4. kártyán, vagy elmarad | – |
| B4 | ~5 | ~5 | – | V |
| **Összesen** | 48–56 | **41–45** | | |

20 főnél a B4 akkor is belefér, ha a 4.3.3 elmarad.

Szövegszintű következmény (VÉTÓLISTÁS):
- :352 `### 4.2.2. Kiscsoportok, esetek kiosztása (2’)` → `(1’)`
- :372 `(kb. 5–7’)` → `(kb. 5–6’)`
- :381 `(kb. 3–4 perc / csoport)` → `(kb. 3–3,5 perc / eset)`
- :383 `Alapértelmezés: **3 eset → kb. 12 perc**.` → `**3 eset → kb. 10 perc**`; a „Ha 4 csoport van…” mondat a D-03 átvezetésével együtt változik
- :427 `### 4.3.1. Bevezetés (2’)` → `(1–2’)`
- :465 `### 4.3.3. Gyors alkalmazás – új eset kívülről (5–8’)` → `(legfeljebb 3’, időszelep)`; a címből az „új” a D-03 szerint kerül ki

**Kérdés:** a :364 „2–3 perces eset-összefoglaló” és a négy nagyköri kérdés együtt 3–3,5’-be csak akkor fér, ha az összefoglaló kb. 2’. Kell-e ezt kimondani?

---

### D20-M3F — M3.F vágási terv (a G9 nem olvasta)
- Fájl: `02 Tervezet/Modulok/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyermekvédelem (Study Lab).md`
- Alap: PRG-1; :555–556 („szent idő”; „a fogalomtérképes résznél rövidítek … a záró üzenetet nem hagyom el”); :62 („előkészített Moodle / H5P belépéssel”)
- Hatáskör: SZEREP: M3 modulgazda (vétó/QA: programvezető)
- Címkék: VÉTÓLISTÁS · LÁTHATÓ SZÖVEG · együtt mozog az M3 hub :237 és :239

**Jelenlegi összeg:**

| Blokk | Keret | Lépéspercek |
|---|---|---|
| B1 | 5’ | nincs lépésperc |
| B2 | 20’ | 5 + 10 + 5 = 20’ |
| B3 | 15’ | 2 + 1–2 + 4 + 5–6 + 3–4 = 15–18’ |
| B4 | 5’ | 4–5 + 1–2 = 5–7’ |
| **Összesen** | **45’** | **45–50’** |

**Védett lépések:**
- B2 csendes pótlás
- B4 mondatbefejezés-kör
- a záró üzenet és a híd, a gyermekvédelmi összefoglalóval (:489–495)
- ha a :428-as minta elhangzik, benne a storming/bántalmazás elhatárolás

| Lépés | Most | Javasolt | Mit rövidít | V? |
|---|---|---|---|---|
| B2/1 Belépés + fókusz | 5 | 2 | a belépés érkezéskor, a :62 szerint előkészítve | – |
| B2/2 Csendes munka | 10 | 13 | a felszabaduló idő a védett pótlásé | V |
| B2/3 Jegyzetlap | 5 | 5 | – | – |
| B3/1 Előhívás | 2 | 2 | – (felidézéses gyakorlat) | – |
| B3/2 Kérdésgyűjtés | 1–2 | 1 | cetlikből, a lapok begyűjtése nélkül | – |
| B3/3 Fogalomtérkép | 4 | 3 | az M3.F-POSZ-02 sablon előre kint | – |
| B3/4 Nyilak | 5–6 | 4 | a 3 kérdésből a visszajelzésekben jelzett hiányhoz tartozók | – (az elhatárolás mondata, ha elhangzik, teljes) |
| B3/5 Kérdések | 3–4 | 3 | elsőbbséget a kapu blokkoló biztonsági témái kapnak (:93) | – |
| B4/1 Mondatbefejezés | 4–5 | 4–5 | – | V |
| B4/2 Záró üzenet + híd | 1–2 | 1–2 | – | V |
| **Összesen** | 45–50 | **43–45** | | |

Új határok: 25–38 / 38–45.
- Alternatíva 10 fő alatt, határtartással: a B3 15’ marad (2 + 1 + 4 + 5 + 3), a mondatbefejezés kb. 3’, így a B4 4–5’.

Szövegszintű következmény (VÉTÓLISTÁS):
- :110 `**25–40’** – Kérdések + fogalomtérkép` → `**25–38’**`
- :112 `**40–45’** – Zárókör + híd` → `**38–45’**`
- :292 `fogalomtérkép (25–40’)` → `(25–38’)`
- :449 `zárás + híd (40–45’)` → `(38–45’)`
- M3 hub :237 `**25–40’ – Kérdések + fogalomtérkép:**` → `25–38’`; :239 `**40–45’ – Zárókör + híd:**` → `38–45’`
- :253 `(kb. 5’)` → `(kb. 2’)`
- :258 `Mindenki lépjen be a Moodle-be, és` → `Aki még nem lépett be a Moodle-be, most lépjen be, és`
- :265 `(kb. 10’)` → `(kb. 13’)`
- :384 `(kb. 1–2’)` → `(kb. 1’)`
- :394 `(kb. 4’)` → `(kb. 3’)`
- :416 `(kb. 5–6’)` → `(kb. 4’)`
- :440 `(kb. 3–4’)` → `(kb. 3’)`
- :382 `A két percet a következő kérdésgyűjtés idejéből vedd el, így a blokk nem lesz hosszabb.` → `… vedd el; a blokk így 13 perc (előhívás 2’, kérdésgyűjtés 1’, térkép 3’, nyilak 4’, kérdések 3’).` (PED-3)

Ugyanez a hamis mondat szó szerint megvan az M5.F:296-ban is (hatókörön kívül, az M5-ös tervhez).

---

### Findingok (pedagógia)

**PED-1** — P1 · magas · pedagógia
- Hely: `02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md:153`, `:157`
- Probléma: a 45’-es változat a védett Blokk 4-et 13’-re szűkíti, és kimondja, hogy rövidül. A 60’-es lépésekkel ez a blokk 15–17’, előkészített poszterrel 14–15’; ez ütközik a lezárt PRG-1-gyel. A G9 ezt „már rendben” lévőnek jelölte.
- Bizonyíték: „a zárókör + „Kihez fordulhatok?” rész marad a leghosszabb, csak minimálisan rövidül” · „**27–40’** – Blokk 4”
- Hatás: 45’-ben a „Kihez fordulhatok?” térkép vagy a zárókör csonkul.
- Javaslat: a mondat átvezetése a PRG-1-re („nem rövidül”). A percek csak a D20-M0A terv modulgazdai jóváhagyásával változnak.
- Típus: objektív · Verdikt: —

**PED-2** — P2 · magas · pedagógia
- Hely: `…/M3.A – Találd ki, hol tart a kvuca! – Történetek Tuckman szemüvegén át.md:311`
- Probléma: hamis időállítás. A lépések 16–22’-et adnak a 15’-es blokkban.
- Bizonyíték: „A blokk így marad az 5–20’ keretben.”
- Hatás: a képző megnyugszik, a túlfutás a terepen a zárókört szorítja ki.
- Javaslat: csak a D20-M3A tervvel együtt javítható; addig marad.
- Típus: objektív · Verdikt: —

**PED-3** — P2 · magas · pedagógia
- Hely: `…/M3.F – … (Study Lab).md:382`
- Probléma: hamis állítás. A B3 lépései 15–18’-et adnak a 15’-es keretben.
- Bizonyíték: „A két percet a következő kérdésgyűjtés idejéből vedd el, így a blokk nem lesz hosszabb.”
- Hatás: lásd PED-2; a védett zárókört szorítja.
- Javaslat: a D20-M3F tervvel együtt javítandó.
- Típus: objektív · Verdikt: —

**PED-4** — P2 · magas · pedagógia
- Hely: `…/M2.F – … (Study Lab).md:141` ↔ `:203`
- Probléma: a Blokk 1 a Moodle megnyitását kéri, a belépés viszont csak a Blokk 2 első lépése (5–10’). Az M3.F-ben (:188 ↔ :253) ugyanez a minta, ott a :62 „előkészített belépés” enyhíti.
- Bizonyíték: „Utána nézd meg **magadnak** a Moodle-ben az M2 négy leckéjét” · „1. **Technikai belépés + fókusz választása (kb. 5’)**”
- Hatás: a 0–5’-es privát felmérés nem végezhető el; elvész 5 perc a védett csendes pótlásból.
- Javaslat: EMBERI DÖNTÉS (M2 modulgazda): belépés érkezéskor, vagy a B1 első 1–2 percében.
- Típus: emberi-döntés · Verdikt: —

**PED-5** — P2 · magas · pedagógia
- Hely: `…/M3.A – … .md:566`
- Probléma: a képzői ellenőrzőlista megengedi a zárókör rövidítését, a lezárt PRG-1 tiltja.
- Bizonyíték: „de a zárókört **nem hagyom el** (max. rövidítem a kör hosszát)”
- Hatás: csúszásnál a védett reflexiós kör rövidül.
- Javaslat: „… **nem hagyom el és nem rövidítem**”. A tétel a PRG-1 átvezetése, a percekhez nem nyúl.
- Típus: objektív · Verdikt: —

**PED-6** — P1 · magas · pedagógia
- Hely: `…/M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md:254`
- Probléma: a mondat minden állításnál körbenézést és reflexiót kér. Ez ellentmond a :251 és a :266 GYV-20-nak megfelelő szabályának (a családról, a zsidóságról és a különbözőségről szóló állításoknál nincs kiállás és nincs magyarázó kérdés), és a lezárt GYV-20-nak.
- Bizonyíték: „mindnél hagyj időt, hogy elhelyezkedjenek, körbenézzenek, és legyen 1–2 rövid reflexió”
- Hatás: a képző érzékeny állításnál is nyilvános reflexióra hívhat; a 7’-es időterv sem állja meg.
- Javaslat: a :251 és a :266 szövegével egyeztetni („…a családról, a zsidóságról és a különbözőségről szóló állításoknál fejben vagy a saját papírjukon; néhány más állításnál 1–2 rövid reflexió”). Új szabályt nem tartalmaz. Vétó/QA: Memuna + DPO.
- Típus: objektív · Verdikt: —

---

### (1) Amit nem tudtam ellenőrizni
- A percszám nélküli lépéseket szószám alapján becsültem: minden B1, az M2.A B1-részei és az M3.B B4. A valós időt csak próbapeula adja.
- Nem tudom, ütemez-e a központi naptár 45’-es M0.A-t, mert a HUM-OPS-01 szerint az M0 sávja 60–80 perc.
- Nem tudom, megoldható-e az M2.F és az M3.F belépése érkezéskor, a naptári időn belül.
- A PED-G1-8 / E-M2-046 állapotát nem néztem meg (megmarad-e az M2.1-es térkép).
- Lépésszintű tükröt csak az M3 hubban találtam (:155–240). A Program tervben, az activity manifestben, az M0 és az M2 hubban nincs; ezt Greppel ellenőriztem.

### (2) Ellentmondás a kánonban
- A D-20 csomag „45’ és blokkhatárok” keretezése szigorúbb a HUM 14 PRG-1 szövegénél: az csak a 45’-es peulablokkot és a naptárt rögzíti. Négy peulánál a kettő együtt nem teljesíthető a védett lépések rövidítése nélkül.
- M0.A :153 és :157 ↔ PRG-1 (PED-1).
- M3.A :566 ↔ PRG-1 (PED-5).
- M3.A :311 és M3.F :382: hamis időállítások (PED-2, PED-3); ugyanez a minta az M5.F:296-ban.
- M2.F :141 ↔ :203, illetve M3.F :188 ↔ :253: sorrendi ellentmondás (PED-4).
- M2.A :254 ↔ :251, :266 és GYV-20 (PED-6).
- M2.A :469: a vagylagos feldolgozó kör a PRG-1 „reflexiós lépés” fogalmával ütközhet; ezt a modulgazdának kell eldöntenie, programvezetői vétóval.
- Az M3.A és az M3.B metaadataiból hiányzik az „Időtartam” sor; a hub mindkettőnél 45’-et ír (:147, :166).

### D-20 – M4, M5, M6, M7

### D-20 / PRG-1: lépésszintű vágási terv (M4–M7), a modulgazdák jóváhagyására

**Alap:** a HUM 14 PRG-1 (`02 Tervezet/Emberi jóváhagyás szükséges.md:721`), a projektgazdai irány D-20 (`01 Fejlesztés/04 Audit/2026-10-13 Projektgazdai felhatalmazás és irányok – D-01…D-23, AP-2026-10-13-01.md:50`), kiindulópontként pedig a G9 kutató javaslata (`…Nyers kutatási, verifier- és QA-kimenetek, AP-2026-10-12-02.md:1758–1782`) és a D-20 csomag (`…Döntési javaslatok…, AP-2026-10-12-02.md:445–468`).

**Hatáskör minden tételnél:** a tervet az adott modulgazda hagyja jóvá (M4, M5, M6, M7), vétó/QA: programvezető. **Minden perc VÉTÓLISTÁS.** Az érintett mondatok LÁTHATÓ SZÖVEGEK, változásuk után pin kell. Jóváhagyásig semmi nem változik.

**Olvasási kulcs**
- **V** = védett lépés: gyermekvédelmi és részvételi keret, passz- és megállítási mondat, kötelező feldolgozás, reflexió, zárókör. Ide tartozik az M6.A 4.3.2/B, valamint az M7-ben az AI-kikötések és a nem-AI út.
- **Asztali becslés** = a leírt lépések hosszából számolt saját becslésem, nem mérés. A modulgazda felülírhatja.
- **A-változat:** a 45’ és a belső blokkhatárok is maradnak (ez a D-20 csomag kerete).
- **B-változat:** csak a 45’ és a központi naptár marad, egy-egy belső blokkhatár 1–3’-cel elmozdul. A PRG-1 szövege („Az ütemezett 45 perces peulablokkok és a központi naptár maradjanak”) csak ennyit köt. Ahol az A-változat nem fér bele, kimondom.
- Új tevékenységet nem írtam. A terv csak rövidít, összevon, sorrendet cserél vagy létszámfüggő változatot ad, mindig a fájlban már meglévő szövegrészből.

**Rövid nevek** (a repó gyökere: ``):
- **M4.A** = `02 Tervezet/Modulok/M4/Peulák/M4.A – Állj oda! – Kiállás & jelenlét a térben.md`
- **M4.B** = `02 Tervezet/Modulok/M4/Peulák/M4.B – Mit és hogyan kérdezek – Kérdezés & peulabemutató gyakorlása.md`
- **M5.A** = `02 Tervezet/Modulok/M5/Peulák/M5.A – Suli, Somer vagy random – Hol tanulunk és hogyan.md`
- **M5.B** = `02 Tervezet/Modulok/M5/Peulák/M5.B – Tervezek egy nonformális peula-részletet – hogy tényleg tanuljunk is.md`
- **M5.F** = `02 Tervezet/Modulok/M5/Peulák/M5.F – Felzárkóztató peula – Suli, Somer & tanulástan (Study Lab).md`
- **M5.1** = `02 Tervezet/Modulok/M5/Online leckék/M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md`
- **HUB5** = `02 Tervezet/Modulok/M5/M5 – Ez most játék vagy tanulás – Nonformális nevelés, módszerválasztás & tanulástan.md`
- **M6.A** = `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md`
- **M7.A** = `02 Tervezet/Modulok/M7/Peulák/M7.A – Célból peula – SMART & 11 pont élőben.md`
- **M7.B** = `02 Tervezet/Modulok/M7/Peulák/M7.B – Peula v2 & Zmán Kvucá – amikor a papír találkozik a valósággal.md`
- **M7.F** = `02 Tervezet/Modulok/M7/Peulák/M7.F – Felzárkóztató peula – Peula & Zmán Kvucá (Study Lab).md`
- **PT** = `02 Tervezet/Program terv.md`

Mind a tíz tételt leadom; a vágási táblák összesen kb. 53 sort tesznek ki.

---

### M4.A (keret 45’, 8–20 fő)

**1. Mostani percösszeg**
- **B1 (0–5’):** belső perc csak a kapcsolásnál van („kb. 1 perc”, :102).
- **B2 (5–15’):** keret 1–2 + csoport 1 + szobor 5–7 + összegzés 1–2 = **8–12’**.
- **B3 (15–30’):** instrukció 2–3 + kör 12–13 + miniösszegzés 2–3 = **16–19’**.
- **B4 (30–40’):** 3 fő × (2’ + 2’) + keret + minireflexió ≈ **13–14’** (asztali).
- **B5 (40–45’):** zárókör 3–4 + kilépőkártya 1–2 + záró üzenet 1–2 = **5–8’**.
- **Összesen ≈ 47–58’ a 45’-ben.** A színpadkör 12–13’-e asztali becsléssel (≈70–95 mp beállónként) csak kb. 8–10 főre igaz; a szöveg 12 főre méretez (:255).

**2. Védett lépések:** 4.1 passz; 4.2/1 biztonsági keret; 4.3/1 „most csak figyelek” mondat és a páros szereplés felajánlása; 4.3/3 miniösszegzés; 4.4 hangkímélő keret és minireflexió; 4.5/1 zárókör.

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| 4.2/3 szobor + bemutatás (:200) | 5–7 | 5 | legfeljebb 3 szobor (szerepcímkénként 1); a 2–3 megfigyelés szobronként marad | – | a :74 és a :447 „kevesebb szobor” szelepe |
| 4.3/1 instrukció (:230) | 2–3 | 2 | a sáv alsó értéke, tartalom nem esik ki | a biztonsági mondat V | – |
| 4.3/2 kör (:236) | 12–13 | 11 | a visszatükröző zárás alapból csak 3 beállónál (a :245 szűkösségi szabálya lesz az alap) | – (a beállás nem rövidül) | ~15 mp/fő (:244) |
| 4.3/3 miniösszegzés (:246) | 2–3 | 2 | alsó érték, nem rövidítés | V | – |
| 4.4 Próba 1 (:280) | 2’/fő | 1,5’/fő | 20–30 mp belépő + 2 rövid jelzés | – | asztali: 1,5’ elég |
| 4.4 Próba 2 (:284) | 2’/fő | 1’/fő | a :286 „a második próba páronként rövidíthető” alapból | – | meglévő szelep |
| 4.5/2 kilépőkártya (:378) | 1–2 | 1 | a zárókör ELŐTT írják (ugyanaz a mondat, :381), leadás kifelé menet — **kérdés a modulgazdának** (sorrendcsere) | – | így a mondat előre átgondolt |
| 4.5/3 záró üzenet (:383) | 1–2 | 0,5–1 | a híd (M4.3–M4.4, peulabemutató) marad, az összefoglaló rész rövidül | – | – |

**Új percösszeg (A-változat, legfeljebb 10 fő):** 5 + 8–10 + 15 + 9,5–10,5 + 4,5–6 = **42–46,5’**. A B4 bontása: keret és triádok 1 + 4,5 + 3 + környezeti döntés 0–1 + minireflexió 1. Puffer így sincs.

**Létszámfüggő változatok**
- Legfeljebb 10 fő: közös színpad.
- 11–15 fő: két párhuzamos színpad (:253).
- 16 fő felett: triádút (:254). A 4.3 ekkor 7’ (instrukció 2 + 1–2 mintabeállás 3 + miniösszegzés 2), a 4.4 Próba 1-e egyben a beállás (nonverbális és hangjelzés, 1,5–2’/fő). A 4.3 és a 4.4 együtt ≈ 18–19’ a 25’-ből, a maradék a zárókörre megy (16–20 főnél ez 4–5’). Ez B-változat, mert a 30’-es határ elmozdul.

**4. Érintett mondatok (VÉTÓLISTÁS)**
- :74 „~8–12 fős körre méretezve” és „**Tervezz ~10–15% puffert**”
- :200 „(5–7 perc)”, :230 „(2–3 perc)”, :236 „(12–13 perc)”, :246 „(2–3 perc)”
- :245 „legalább 2–3 beállónál”
- :252 „Nagy létszámnál (kb. 15–20 fő)… 12–13 percbe”
- :254 „a blokk 15 percben tartható”: ki kell mondani, hogy a terhelés átkerül a 4.4-be
- :255 „reálisan 8–12 fős”
- :280 és :284 „(kb. 2 perc/fő)”
- :378 „(1–2 perc)” és a 4.5 lépéssorrendje; :383 „(1–2 perc)”
- Konzisztens marad: :447, illetve az M4.A-MUNK-02 spec (:397, BUILD-INPUT).

---

### M4.B (keret 45’, 8–20 fő)

**1. Mostani percösszeg**
- **B1 (0–5’):** nincs belső perc.
- **B2 (5–20’):** 1–2 + 1 + 1 + 4–5 + [zárt kör 4–5, opcionális] + 4–5 + 2–3 = **13–17’** (zárt körrel 17–22’).
- **B3 (20–35’):** 2 + 2–3 + [gyorsvázlat 3, feltételes] + 10–12 + 2–3 = **16–20’** (19–23’).
- **B4 (35–45’):** 5 + 5–7 + [kilépőkártya 2–3, „ha belefér”] + 1–2 = **11–14’** (13–17’).
- **Összesen 45–56’** (a feltételes lépésekkel legfeljebb 67’) a 45’-ben.

**2. Védett lépések:** 4.1 „Nem tudom…” kimenet; 4.2 körönkénti minireflexiók (lásd PED-2); a :224 gyermekvédelmi zárómondat; 4.3 a részvételi mód választásának felkínálása (:297–301) és a biztonságos megosztás (:302); 4.3/4 miniösszegzés; 4.4/1 kiscsoportos megosztás (reflexió); 4.4/2 zárókör + passz; a két zárómondat (4. cél).

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| 4.2/1 emlékeztető (:192) | 1–2 | 1 | az M4.B-POSZ-01 előre kitéve, élő felírás nélkül | – | az asset jegyzete: „kiváltja vagy gyorsítja” |
| 4.2/2–3 párok + téma (:195, :198) | 1+1 | 1 | összevonva: a párba fordulás alatt hangzik el a téma | – | – |
| 4.2/5 zárt kör (:207) | 4–5 (opc.) | alapból 0 | opcionális marad (a besorolás nem változik), alapból kimarad | – | :70, :208 |
| 4.3/1 csoportalakítás (:274) | 2 | 1 | 3 fős csoport az alap (:275 már engedi) | – | – |
| 4.3/3 peulabemutató-kör (:285) | 10–12 | 8 (3 fő) / 10 (4 fő) | csak a csoportméret változik. Gyorsvázlat-ágnál (:283, +3’) a :295–296 „kevesebb visszajelzés” módja → 7 | mag; a választás V | asztali: ~2,5’/fő |
| 4.3/4 miniösszegzés (:303) | 2–3 | 2 | alsó érték | V | – |
| 4.4/4 záró üzenet + híd (:334) | 1–2 | 0,5–1 | a terepi híd-mondat marad | – | – |

**Új percösszeg (A-változat):** 5 + 12–14 + 13–15 + 10,5–11. **A B4 nem fér bele a 10’-be:** a két védett lépés alsó értéke együtt már 10’ (5 + 5).

**Alternatívák a modulgazdának**
- (a) **B-változat:** B2 5–19’, B3 19–34’, B4 34–45’ (11’). Legfeljebb 14 főnél fér. 15–20 főnél csak akkor, ha a két zárómondat egy körben hangzik el (:326, lásd az 5. pontot).
- (b) A 4.4/1 rövidítése 5’-ről 4’-re: védett lépés, csak modulgazdai döntéssel, programvezetői vétóval.
- (c) A kilépőkártya (:329) „ha belefér” státusza marad; a terv nem számol vele.

**4. Érintett mondatok:** :110 puffer-mondat; :192, :195, :198, :274, :275, :285, :303, :334 percei; B-változatnál a :70–72, :144, :183, :228, :263, :311, :314 sávcímkéi; :395 „interjú-körökből kevesebb reflexió” (PED-2).

**5. A :326 két mondata:** kötelező tartalom marad, lásd a D20-M4B-326 blokkot lent.

---

### M5.A (keret 45’, 8–24 fő)

**1. Mostani percösszeg**
- **A szöveg szerint:** 5 + 5 + 20–22 (:285 „kb. 12–14” a 12’-es sávban) + 10 + 5 = **45–47’**.
- **Asztali becsléssel ≈ 50–60’:**
  - B1: 24 főnél név + két példa 6–8’;
  - B2: 6 szituáció 6–9’ az 5’-ben;
  - 4.3.1: 5,5–7,5’ az 5’-ben;
  - 4.4.1: 6–8’ a 7’-ben, a 4.4.2 négy kérdése 4–5’ a 3’-ben;
  - B5: 24 főnél 5–6’.

**2. Védett lépések:** 4.1 passz; 4.2 helyből jelzés és passz (:243); 4.4.1 inkluzivitás-mondat (:440) és a reagálás két egyenértékű útja; 4.4.2 közös tanulságok (feldolgozás); 4.5 zárókör + passz (:527).

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| 4.1 kör (:134) | – (5) | legfeljebb 14 főnél változatlan; 15 fő felett névsor nélkül (:142 szerint, ha ismerik egymást). Ha a nevek nem ismertek: 1 példa — kérdés | – | passz V | asztali: 12–15 mp/fő |
| 4.2 szituációk (:241, :246) | 6–8 | 4 (+1, ha marad idő) | 2 egyértelmű (1., 3.) 1 indoklással; 2 határeset (4., 5.) 1–2 indoklással és a „mi kellene…” kérdéssel | a befogadó és a passz mondat V | a :267 már engedi |
| 4.3.1 (:281, :331, :350) | 5 (asztali 5,5–7,5) | 5 | kártyák csoportonként előre összekészítve; 2–3 helyett 2 kártya; minifelvezető 2–3 helyett 2 | – | a minifelvezető marad (:350) |
| 4.3.2 poszter (:282, :384) | 12 („kb. 12–14”) | 13 | +1’ a 4.3.3-ból | – | :285 „a poszteridőt tartsd” |
| 4.3.3 felkészülés (:283, :393) | 3 | 2 | a :285 szerinti 1–2’; ide kerül a poszterek kihelyezése (4.4.1/A) | – | – |
| 4.4.1 galériaséta (:414–447) | 7 (asztali 6–8) | 5 | kihelyezés a 4.3.3-ba; séta 3’ (a :447/:526 szelepe alapból); átmenet 1’; instrukció 1’ | inkluzivitás V | – |
| 4.4.2 közös tanulságok (:449) | 3 | **5 (hosszabbítás)** | védett feldolgozás. A 4 kérdés menü vagy mind kötelező? — kérdés | V | 4 kérdés nem fér bele 3’-be |
| 4.5 képző zárása (:501) | – | 0,5 | 20 fő felett csak az M5.3–M5.4 híd-mondata | a zárókör V | 24 főnél a kör maga 5’ |

**Új percösszeg (A-változat):** 5 + 4,5–5 + 20 + 10 + 5 = **45’** legfeljebb 20 főnél. 21–24 főnél a B5 a képző egymondatos zárásával tartható.

**4. Érintett mondatok:**
- szituációk és kártyák száma: :74 „6–8 db a 3 sarok játékhoz”; :241 „Felolvasok 6–8 rövid sztorit.”; :246 „(6–8 db, kb. 1 perc / 2–3 szitu)”; :518;
- a 4.3 idővonala és percei: :281–283; :285 „kb. 12–14 perc”; :331 és :337 „2–3 helyzetkártyát”; :350 „(2–3 perc”; :359, :384–385, :393;
- a 4.4 percei: :414 „(30–37’)”; :418 „(kb. 1 perc)”; :427 „Kb. 3–4 percetek”; :447; :449 „(37–40’)”; :526.

Együtt mozgó hely: HUB5:29 „Legalább 6–8 konkrét példát”. Ez az M5.1 SLIDE 2 (3 példa) és SLIDE 4 (5–6 példa) révén továbbra is teljesül; a modulgazda erősítse meg.

---

### M5.B (keret 45’, 8–20 fő)

**1. Mostani percösszeg**
- **B1 (0–10’):** instrukció + 5 állítás + miniösszegzés ≈ **5–7’** (asztali), vagyis 3–5’ tartalék.
- **B2 (10–30’):** 4.2.1 5 + 4.2.2 12 (instrukció 1–2 + poszter 10–12) + 4.2.3 3 (ebből ~1’ a tényleges munka) = **16–20’**; a tartalék sorírás +5’.
- **B3 (30–40’):** 2–3 csoport × 2–3’ (4–9) + 4.3.2 4 = **8–13’**.
- **B4 (40–45’):** legfeljebb 20 főnél **4–5’**.
- **Összesen 33–45’** (sorírással 38–50’). A túlcsordulást a sorírás és a csoportonként 3’-es bemutatás okozza, nem az alapmenet.

**2. Védett lépések:** 4.2.1 adatvédelmi mondat (:310); 4.3.2 visszajelzés + miniösszegzés (feldolgozás); 4.4 zárókör + passz.

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| 4.2.1 gyors sorírás (:326–327) | „5 perces” / „1 percben” | lásd az 5. pontot (A-opció: 5’, B-opció: 2–3’), mindkettő a B1 végén | elhelyezés: a :326 maga mondja, hogy „a felidézés után” | – | a B1-ben 3–5’ tartalék van |
| 4.3.1 bemutatások (:390, :392, :399) | 2–3 csoport × 2–3’ | 3 × 2’ = 6 (vagy 2 × 3’) | egységesen „max. 2 perc” (:377) | – | a :377 és a :392/:399 eltér |
| 4.3.2 visszajelzés (:401, :405) | 4 | 4 | elhelyezése eldöntendő: mind a 36–40’-ben, vagy bemutatásonként (ekkor a :401 sávcíme változik) | V | a :405 „Minden bemutatás után” és a :401 „(36–40’)” ellentmond |

**Új percösszeg (A-változat):** B1 5–7 (a B-opció sorírásával 7–10) + 16–20 + 10 + 4–5 = **35–45’**.

**4. Érintett mondatok:** :326–327; :377, :390, :392, :399; :401/:405. Ha az A-opció mégis megnyújtja a B1-et: :202, :211, :300, valamint az M5.B-KART-02 purpose sora (:219 „(0–10')”, BUILD-INPUT).

**5. A :326 két fordulata:** lásd a D20-M5B-326 blokkot lent.

---

### M5.F (saját kánoni keret: 50–55’, :17 és HUB5:152; 6–20 fő)

**1. Mostani percösszeg**
- **B1 (0–5’)**
- **B2 (5–25’):** belépés + fókusz 5 + csendes munka 10 + jegyzetlap 5 = **20’**.
- **B3 (25–50’, 20–25’):** 4.3.0 2 + 4.3.1 1–3 + 4.3.2 5 + 4.3.3 7–8 + 4.3.4 4–5 = **19–23’**.
- **B4:** minikör 3–4 + záró üzenet 2–3 = **5–7’**.
- **Összesen 49–55’ az 50–55’-ben.**

Három gond:
- **(i) Sorrendi hiba:** a B1 már a Moodle-ben dolgoztat (:144), a technikai belépés viszont csak a B2 1. lépése (:207).
- **(ii) Számtani hiba:** a :296 a 4.3.0 két percét az 1–3’-es kérdésgyűjtésből vonja le.
- **(iii)** A B4 2’-cel túlcsordul.

**2. Védett lépések:** B1 privát állapotfelmérés; B2 csendes pótlás („szent idő”, :413) és jegyzetlap; 4.3.0 előhívás; B4 minikör + passz; a javító újraleadás határideje.

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| belépés érkezéskor + 4.2/1 (:207) | 5 | 1–2 (csak fókusz + technikai ellenőrzés) | a belépés a 0’ elé kerül, érkezéskorra (a :57 „előkészített … belépéssel” már ezzel számol) | – | sorrendi hiba |
| 4.2/2 csendes munka (:217) | 10 | **13–14 (hosszabbítás)** | a felszabaduló idő a védett munkára megy | V | – |
| 4.3.1 kérdésgyűjtés (:296, :298) | 1–3, „mínusz 2” | nyílt módban 1, név nélküli módban 3 (ekkor a 4.3.3 7–8 helyett 6) | a „vedd el” mondat helyett a 4.3.0 2’-e külön áll | – | számtani ellentmondás |
| 4.4/2 záró üzenet (:381) | 2–3 | 1–2 | a háromelemű összefoglaló (ismétli a :340–345 minikeretet) rövidül; a javító újraleadás és a szerda 18:00 marad | – | redundancia |

**Új percösszeg:** 5 + 20 + 20–23 + 4–6 = **49–54’**, a keretben.

**4. Érintett mondatok:** :207 „(kb. 5’)”; :217 „(kb. 10’)”; :296; :298 „(kb. 1–3’)”; :326 „(kb. 7–8’)” (csak név nélküli módban); :381 „(kb. 2–3’)”. A belépés új helyének egy mondatát (2.3 vagy 4.1) a modulgazda írja meg; nem terveztem.

---

### M5.1 (online lecke, metaszám 15–20’)

**Mostani állapot**
- A metaszám a :7 sorban („**Időtartam:** 15–20 perc”) és a :34 tanulói Moodle-címkében („Ebben a 15–20 perces leckében”, LÁTHATÓ) szerepel.
- A részidők a :653–656 sorokban ~2–3 / ~2–3 / ~3–4 / ~2–3 perc, összesen **9–13’**.
- A :657 állítása („→ összesen 15–20 perc, megfelel a sablonnak.”) ezért hamis.
- Ugyanez a szám jelenik meg: HUB5:7 „4×15–20 perc”; HUB5:8 „a részidők összege 150–180 perc … 3,5 óra”; HUB5:41 „(15–20’)”; PT:70 „M5 | 3,5 óra”.

**(A) Újrabecslés próbaolvasókkal (a G9 ezt ajánlja)**
1. **Feltétel:** kész H5P-vázlat a célverzión, minden diával, visszajelzéssel, felirattal, és végleges vagy időben azonos hanggal (HOOK legfeljebb 40 mp, NAR-02 70–90 mp, OUTRO 20–30 mp; :18–19). A hang tartalma VO-PACK; a mérés nem változtat rajta.
2. **Próbaolvasók:** 2–3 olyan 15–17 éves, aki a leckét még nem látta; legalább egyikük telefonon dolgozik (mobil-first, :8).
3. **Mérés:** egy felnőtt megfigyelő stopperrel méri a négy szakasz határát a :653–656 bontásában (HOOK + minisztorik / Input / Activity / Check + Outro). Külön sorban méri a Moodle-címkét (:28–48) és a SLIDE 6 opcionális lépését (nem completion-feltétel, :626). Segítség és sürgetés nincs.
4. **Adat:** csak időtartam kerül rögzítésre, név nélkül. A kiskorú próbaolvasók bevonásának feltételeiről (hozzájárulás, jelen lévő felnőtt) és minden ezen túli adatról (képernyő- vagy hangfelvétel) a meglévő szabályok szerint a programvezető, adatkezelésnél a DPO, gyermekvédelmi kérdésben a Memuna dönt. A terv ezt nem dönti el.
5. **Kiértékelés:** szakaszonként és összesen min–max, felfelé egész percre kerekítve. A :653–656 a mért értékeket kapja.
6. **Döntési szabály (javaslat):**
   - Ha a mért összeg 15 és 20 perc közé esik, a metaszám marad, a :657 pedig a mért sávot írja.
   - Ha a mért összeg 15 perc alatt marad, a (B) út következik. Kitöltő tartalmat a 15 perc eléréséért nem írunk (az új tartalom /course-develop).
   - Ha a mért összeg 20 perc fölött van, szintén a (B) út következik, felfelé.

**(B) A metaszám visszaigazításának következményei**
- A :7, a :34 (LÁTHATÓ) és a :657 a mért sávra változik, és a HUB5:41 címsora is.
- A HUB5:7 „4×15–20 perc” helyére külön M5.1-érték és „3×15–20 perc (M5.2–M5.4)” kerül.
- A HUB5:8 „150–180 perc” részösszege a különbséggel változik.
- A „3,5 óra” V1 tervezési érték (HUB5:8 és :10; PT:61 és :70) projektgazdai döntés (2026-10-02), és felső tervezési érték: a csökkenés nem érinti, és csak a projektgazda nyúlhat hozzá. Ha a mért érték 20 perc fölött van, a felülvizsgálatáról a projektgazda dönt.
- A központi naptár (HUM-OPS-01, programvezető) nem változik, mert a peulasávok nem mozdulnak. A terhelés kommunikációját a programvezető ellenőrzi.

**Addig:** a :657 hamis marad; a metaszám túlbecsül, ami a terhelés tervezésénél óvatos irány.

---

### M6.A (keret 45’, ideális 8–20 fő)

**1. Mostani percösszeg**
- **B1 (0–5’):** 20 főnél ≈ 4,5’.
- **B2 (5–20’):** 2–3 + 5–7 + 3 + 5 = **15–18’**.
- **B3 (20–35’):** 3–4 + 7–8 + 3–4 + 5–6 = **18–22’**.
- **B4 (35–45’):** 5–6 + 5–6 + 3–4 = **13–16’**.
- **Összesen 51–61’ a 45’-ben.**

**2. Védett lépések:** 4.2.2 biztonság és inkluzivitás játék közben; 4.2.3 kézjel és passz; 4.3.1 a teljes biztonsági keret, a tiltott zóna és az előkeretező mondat; **a 4.3.2/B érintetlen**; 4.3.3 minikör (kötelező feldolgozás, :511); 4.3.4 INKLUZÍV VARIÁCIÓ (:595); 4.4.1 páros beszélgetés (önfeltárás nem kötelező, :626); 4.4.2 nagykör; az M6.B-híd a peula végén (ellenőrzőlista, :719–724).

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| 4.2.2 névkör (:329, :353) | 5–7 | 5 | a második kör (:353 „férjen bele”) alapból elmarad | – | – |
| 4.2.3 korosztály-sarok (:363, :385) | 3 | 2 („2 ember” a 3 helyett), vagy elhagyható, mert a 4.2.4 KVUCA-oszlopa és a 4.3.4 sarka lefedi | – | kézjel és passz V | redundancia a 4.3.4-gyel |
| 4.3.2 játék (:472, :474) | 7–8 (8–10 kör) | 5 (6 kör) | a :594 szelepe alapból | **4.3.2/B ÉRINTETLEN** | ~40 mp/kör |
| 4.3.4 szemüveg (:539) | 5–6 | 4 | sarkonként 1 hozzászóló; a KINEK NEHÉZ és a KIREKESZTÉS oszlop legfeljebb 1–2 hozzászólás (:593) | az INKLUZÍV VARIÁCIÓ V, nem rövidül | – |
| 4.4.3 záró üzenet (:650) | 3–4 | 1 | a négyelemű összefoglaló rövidül; az M6.B-híd (játéklap + Moodle) marad | – | a G9 javaslata (a híd átkerül az M6.B elejére) ütközik a :719–724-gyel (PED-5) |

**Új percösszeg:**
- B2: 2 + 5 + 2 + 5 = 14’ (sarok nélkül 12’);
- B3: 3–4 + 5 + 3 + 4 = 15–16’;
- B4: 5 + 5 + 1 = **11’**. Az A-változatban a B4 nem fér bele.

**Alternatívák a modulgazdának**
- (a) **B-változat:** B2 5–19’, B3 19–34’, B4 34–45’. Akkor fér bele 45’-be, ha a 4.3.1 3’ alatt lefut. Ha 4’ kell neki, a 4.2.3 elmarad (B2 5–17’, B3 17–33’, B4 33–45’).
- (b) A 4.4.1 és a 4.4.2 összevonása (G9: 4’ + 5’), vagy a 4.4.1 rövidítése 5’-ről 4’-re: védett lépést érint, kifejezetten modulgazdai döntés, programvezetői vétóval.
- (c) A kilépőkártya (:680) opcionális marad.

**4. Érintett mondatok:** :189–191; B-változatnál a :227/:230, :418/:421, :599/:602 sávcímkéi; :353; :363 „(kb. 3 perc)” és :385 „3 ember”; :472 „(kb. 7–8 perc)” és :474 „8–10 kört”; :539 „(kb. 5–6 perc)”; :591–594 (PED-2); :650 „(kb. 3–4 perc)”.

---

### M7.A (keret 45’, 8–20 fő)

**1. Mostani percösszeg**
- **B1 (0–5’)**
- **B2 (5–10’):** 1 + 1 + 3–4 + 1–2 = **6–8’**.
- **B3 (10–25’):** 2 + 1 + 7 + 5–7 = **15–17’**.
- **B4 (25–40’):** 1 + 2–3 önkéntes × (2–3 + 2–3) + 2 + 2–3 = **13–24’** (a galéria-változat 15’).
- **B5 (40–45’):** 5 + 1–2 = **6–7’**.
- **Összesen 45–61’.** A :403 állítása (2–3 önkéntes fér bele) 3 önkéntesnél hamis.

**2. Védett lépések:** 4.1 passz; 4.3/1 adatvédelmi mondat (:340); 4.4 a két ítélkezésmentes mondatkezdő; 4.4/4 miniösszegzés; 4.5/1 mondatbefejezés + passz.

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| 4.2/1 és 4.2/4 (:207, :221) | 1 + 1–2 | 0 + 1 | a tér kijelölése az előkészítésbe kerül (a 2.2, :44 már leírja) | – | – |
| 4.2/3 mondatok (:212–213) | 3–4 (4–6 mondat) | 3 (4 mondat) | 2 szétfolyó + 2 SMART-közeli cél. Melyik marad (pl. a „háború”-mondat)? — kérdés | – | – |
| 4.3/4 11 pont (:358) | 5–7 | 5 | szükség esetén 3 pont (:370) | – | – |
| 4.4/1–2 önkéntesek (:395–397) | 2–3 × (2–3 + 2–3) | 2 × (2 + 2) = 8 | a 3. önkéntes csak akkor jön, ha legalább 4’ marad | – | – |
| 4.4/3 visszajelzési struktúra (:410) | 2 | 1 | az M7.A-POSZ-03 előre kitéve | – | – |
| 4.4/4 miniösszegzés (:416) | 2–3 | 2 | alsó érték | V | – |
| 4.5/2 zárómondat + híd (:465) | 1–2 | 0,5–1 | az M7.3–M7.4 híd marad | – | – |

**Új percösszeg:** 5 + 5 + 15 + 12 + 5,5–6 = **42,5–43’**. A B4 3’-es puffere a zárókört védi: ha a sávcímek maradnak, a puffer a 4.4 végén áll; ha nem, B-változat (B4 25–37’, B5 37–45’). A galéria-változat (14 fő felett, :445) esetén a B4 15’, az összesen 45,5–46’, ilyenkor a zárómondat 0,5’.

**4. Érintett mondatok:**
- percek és számok: :207 „(1 perc)”; :212 „(3–4 perc)”; :213 „Olvass fel 4–6”; :221 „(1–2 perc)”; :358 „(kb. 5–7 perc)”; :396 „2–3 önkéntest”; :397; :410 „(2 perc elmagyarázni”; :416 „(2–3 perc)”; :465 „(1–2 perc)”;
- :403, javasolt szöveg: „15 percbe 2 önkéntes fér bele biztosan, a harmadik csak akkor, ha marad idő – nem oszt meg mindenki, és ez így van rendben.”;
- B-változatnál: :65–66, :386, :453.

---

### M7.B (keret 45’, 8–20 fő)

**1. Mostani percösszeg**
- **B1 (0–10’):** 1 + 6–7 + 1–2 = **8–10’**.
- **B2 (10–30’):** 2–3 + 10–12 + 5–7 + ~1 (:465) + [AI-tipp 3–5, opcionális] = **18–23’** (AI-tippel 21–28’).
- **B3 (30–40’):** 1–2 + 4–5 + 4–5 = **9–12’**.
- **B4 (40–45’):** 3–4 + 1–2 + 1–2 + 1 = **6–9’**.
- **Összesen 41–54’** (AI-tippel 44–59’).

**2. Védett lépések:** 4.1 gyermekvédelmi és AI-határ összegzések (:270–272); 4.2/2 a 4. és az 5. terület (:494); adatvédelmi mondatok (:440, :515); **4.2/4 AI-tipp: az opcionális státusz, a négy szabály és a nem-AI egyenértékű út nem változik**; 4.3/3 tanulságkör (feldolgozás); 4.4/1 zárókör + passz; 4.4/2 kipróbálási szándék (benne a 18 év feletti felnőtt mondata, :565).

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| 4.1/1–3 (:255, :258, :273) | 1 + 6–7 + 1–2 | 0 + 6 + 1 | a tér az előkészítésbe kerül (2.2, :80); az 5 állítás marad | az összegzések V | – |
| 4.2/1 kiscsoport (:413) | 2–3 | 2 | alsó érték | – | – |
| 4.2/2 checklist (:422) | 10–12 | 10 | alsó érték. A :494 „3 terület” szelepe csak csúszáskor él, a 4. és az 5. terület nem hagyható el | részben V | – |
| 4.2/3 beírás + előtte–utána (:444, :465) | 5–7 + ~1 | 6 (az előtte–utána benne) | – | – | – |
| 4.2/4 AI-tipp (:472) | 3–5 | 0–2, csak ha marad idő | csak az időzítés változik; a státusz és a nem-AI út marad | V | a 3. cél AI-határait a 4.1 (3. és 5. állítás) és a poszter is hordozza |
| 4.3/1–2 (:519, :522) | 1–2 + 4–5 | 1 + 4 | alsó értékek; a post-it-réteg marad | – | a :541 („fér bele 10 percbe”) igaz marad |
| 4.4/3–4 (:570, :574) | 1–2 + 1 | 1 + 0,5 | a kilépőkártyák felolvasása alapból elmarad; a záró üzenetből a v2 határideje marad | – | a privát kipróbálási jegyzet és a begyűjtött kártya NEM vonható össze |

**Új percösszeg:** 7 + 18 (+0–2) + 9–10 + 6,5–7,5 = **40,5–44,5’**. Az A-változatban a B4 (6,5–7,5’) nem fér bele az 5’-be.

**Alternatívák a modulgazdának**
- **B-változat:** 0–8’ / 8–27’ / 27–37’ / 37–45’; így minden blokk belefér.
- A kilépőkártya opcionálissá tétele: kötelező→opcionális besorolásváltás, VÉTÓLISTÁS, a modulgazda dönt.

**4. Érintett mondatok:**
- a 4.1 és a 4.2 percei: :255 „(1 perc)”; :258 „(6–7 perc)”; :273 „(1–2 perc)”; :413 „(2–3 perc)”; :422 „(10–12 perc)”; :444 „(5–7 perc)”; :465 „(kb. 1 perc)”; :472 „Opcionális AI-tipp (3–5 perc)”;
- a 4.3 és a 4.4 percei: :519 „(1–2 perc)”; :522 „(4–5 perc)”; :571 „ha belefér”; :574 „(1 perc)”;
- a :544 és a :640 „tanulságkör 3 perc” szelepe (PED-2);
- B-változatnál: :99–102, :172/:239, :283/:382, :498/:501, :548/:551.

---

### M7.F (keret 45’, 6–20 fő)

**1. Mostani percösszeg**
- **B1:** 5’.
- **B2:** 5 + 10 + 5 = 20’.
- **B3:** 2 + 1 + 5 + 4 + 3 = 15’.
- **B4:** 2–3 + 2–3 = 4–6’ (az opcióval +1–2’).
- **Összesen 44–46’** (az opcióval 47–48’).

Két gond:
- A B1 már a visszajelzést és a Moodle-t nyittatja (:145), a belépés viszont a B2 első lépése (:208).
- A név nélküli kérdésgyűjtés (begyűjtés, átfutás, táblára írás) nem fér bele 1’-be (:280).

**2. Védett lépések:** B1 privát állapotfelmérés; B2 csendes pótlás („szent idő”, :395) és jegyzetlap; 4.3/1 előhívás; 4.3/5 gyermekvédelmi félreértés tisztázása (:308); B4 minikör + passz; a javító próbálkozás határideje (:336).

**3. Vágási tábla**

| Lépés | Most | Javasolt | Mit rövidít / von össze | V? | Indok |
|---|---|---|---|---|---|
| belépés érkezéskor + 4.2/1 (:208) | 5 | 1–2 | a belépés a 0’ elé kerül (a :51 „előkészített … belépéssel” már ezzel számol) | – | sorrendi hiba |
| 4.2/2 csendes munka (:211) | 10 | **13–14 (hosszabbítás)** | – | V | – |
| 4.3/2 kérdésgyűjtés (:280) | 1 | nyílt módban 1; név nélküli módban 3, ekkor a 4.3/4 4’ helyett 2’ (a :312 minimuma: 4 buborék + 2 nyíl) | – | a 4.3/5 V | – |
| 4.4/2 záró üzenet (:333) | 2–3 | 2 | az első bekezdés (ismétli a :303 minikeretet) rövidül; a második (kvíz → v2, szerda 18:00) marad | – | redundancia |

**Új percösszeg:** 5 + 20 + 15 + 4–5 = **44–45’** legfeljebb 12 főnél. 13–20 főnél a minikör 3–4’, ezért a záró üzenetből csak a második bekezdés marad (1’). Az opcionális javítási terv (:337) „ha belefér” státusza marad.

**4. Érintett mondatok:** :208 „(kb. 5’)”; :211 „(kb. 10’)”; :280 „(kb. 1’)”; :295 „(kb. 4’)” (csak név nélküli módban); :333 „(kb. 2–3’)”.

---

### Konkrét szövegtervek (5. pont)

### D20-M4B-326 — a zárókör két mondata
- Fájl: 02 Tervezet/Modulok/M4/Peulák/M4.B – Mit és hogyan kérdezek – Kérdezés & peulabemutató gyakorlása.md:326
- Alap: HUM 14 PRG-1; D-20; M4:NYELV-G2-6; 4. cél (:22–24)
- Hatáskör: SZEREP: M4 modulgazda (jóváhagyási feltétel: a szerzői szándék megerősítése — az „egyben” azt jelenti, hogy a két mondat egy körben, egymás után hangzik el, vagy hogy egy mondatba sűrítik?); vétó/QA: programvezető
- OLD (Greppel ellenőrizve, egyszer szerepel): `Két mondatot szeretnék hallani tőletek, ha belefér az idő, akár egyben is elmondhatjátok.`
- NEW (a G9 szövege): `Két mondatot szeretnék hallani tőletek; ha szűk az idő, akár egyben is elmondhatjátok.` — ha a szándék az „egy körben”: `Két mondatot szeretnék hallani tőletek; ha szűk az idő, mondjátok el a kettőt egy körben, egymás után.`
- Együtt mozgó helyek: nincs (a :22–24, :72 és :313 a két mondatot változatlanul kéri)
- Címkék: LÁTHATÓ SZÖVEG (képzői instrukció); az M4.B B4 időtervének része
- Indoklás: a mostani „ha belefér az idő” a kötelező két mondatot feltételessé teszi, miközben a 4. cél két mondatot kér. A szerzői szándék nyitott kérdés (8. regressziós minta), ezért kérdésként jelölöm.

### D20-M5B-326 — gyors sorírás: „5 perces” vagy „1 percben”
- Fájl: 02 Tervezet/Modulok/M5/Peulák/M5.B – Tervezek egy nonformális peula-részletet – hogy tényleg tanuljunk is.md:326 (a :327-tel együtt)
- Alap: HUM 14 PRG-1; D-20; M5:PED-G2-6
- Hatáskör: SZEREP: M5 modulgazda (választás az A és a B opció között); vétó/QA: programvezető
- OLD (egyszer szerepel): `**5 perces gyors sorírás (ha van rá 5–10 perced):**`
- NEW, A-opció (5 perces keret, ebből 1 perc írás): `**5 perces gyors sorírás (ebből 1 perc az írás; ha van rá 5–10 perced):**`. A :327 „írj le 1 percben 1 sort” marad. Időterv: a B1 végén; a hiányzó 1–3 percet a 4.2.1 sorválasztása adja, mert a sorírás a táblázat nélkülieknél a sorválasztást váltja ki (kérdés: elfogadható-e).
- NEW, B-opció (rövid lépés): `**Gyors sorírás – 1 perc írás (ha a felidézés után marad 2–3 perced):**`. A :327 marad. Időterv: a B1 végén, a kvíz utáni tartalékban; a 4.2.1 nem változik.
- Együtt mozgó helyek: a :97 és a :469 nem változik
- Címkék: VÉTÓLISTÁS, LÁTHATÓ SZÖVEG
- Indoklás: a címke 5 percet, a szöveg 1 perc írást, a feltétel 5–10 perc tartalékot mond. A B1 asztali becslés szerint 3–5 perc tartalékot hagy.

---

### Findingok (pedagógia)

**PED-1** — F-peulák: a belépés sorrendje
- Súlyosság: P2 · Bizalom: magas · Lencse: pedagógia
- Hely: M5.F:144 ↔ :207; M7.F:145 ↔ :208
- Probléma: a Blokk 1 privát állapotfelmérése már a Moodle-ben dolgoztat, a technikai belépés viszont csak a Blokk 2 első, 5 perces lépése. Így a védett csendes pótlásból 5 perc a belépésre megy el.
- Bizonyíték: M5.F:144 „Nyisd meg **magadnak** a Moodle-ben a visszaküldött M5.4 táblázatodat” · :207 „**Technikai belépés + fókusz választása (kb. 5’)**”
- Hatás: a B1 belépés nélkül csúszik vagy üresen fut; a „szent idő” ténylegesen 10 perc.
- Javaslat: EMBERI DÖNTÉS (M5, M7 modulgazda, a D-20 terv része): belépés érkezéskor, a 4.2/1 1–2 percre, a csendes munka 13–14 percre. A percek VÉTÓLISTÁSAK.
- Típus: emberi-döntés · Verdikt: –

**PED-2** — meglévő időszelepek védett feldolgozó vagy reflexiós lépést rövidítenek
- Súlyosság: P2 · Bizalom: közepes · Lencse: pedagógia
- Hely: M4.B:395; M6.A:592; M7.B:544 és :640
- Probléma: a peulák saját „ha csúszol” szelepei épp azokat a feldolgozó és reflexiós lépéseket rövidítenék, amelyeket a PRG-1 véd.
- Bizonyíték: M6.A:592 „a korosztály-sarkot (4.3.4 eleje) és a minikört (4.3.3) **vond össze** egy gyors körbe” · M7.B:544 „vagy a körbejárás 3 perc + tanulságkör 3 perc”
- Hatás: időszorításban a képző a lezárt döntéssel ellentétes vágást talál a szövegben. Az M6.A-nál a kirekesztésre érzékeny játék utáni feldolgozás szorulna ki (ezt a :511 biztonsági hálója enyhíti).
- Javaslat: EMBERI DÖNTÉS (modulgazdák; vétó: programvezető): védettnek számít-e a lépés. Ha igen, a szelep más lépésre mutasson (M4.B: zárt kör; M6.A: 4.2.3 sarok; M7.B: post-it-réteg). A :395 interjú-minireflexiójának besorolása különösen kérdéses.
- Típus: emberi-döntés · Verdikt: –

**PED-3** — M4.A mini színpad: irreális létszámküszöb
- Súlyosság: P2 · Bizalom: közepes · Lencse: pedagógia
- Hely: M4.A:236, :252–255
- Probléma: a közös színpad 12–13 perce asztali becsléssel (≈70–95 mp beállónként) csak kb. 8–10 főig tartható. A szöveg 8–12 főre méretez, alternatívát csak 15–20 főre ad, a triádút pedig a már túlcsorduló 4.4-be tolja a terhelést.
- Bizonyíték: :255 „A percbontás reálisan 8–12 fős, közös színpadú körre van méretezve.” · :252 „**Nagy létszámnál (kb. 15–20 fő) a kör nem fér bele a 12–13 percbe**”
- Hatás: 11–14 főnél a képző a normál utat választja, és a kör kiszorítja a Hang-létrát vagy a zárókört.
- Javaslat: EMBERI DÖNTÉS (M4 modulgazda): küszöb 10–11 főnél; 11–15 fő között két párhuzamos színpad; 16 fő felett triádút a 4.3 és a 4.4 közös 25 percével (lásd a tervet). A küszöböt próbapeulán érdemes ellenőrizni.
- Típus: emberi-döntés · Verdikt: –

**PED-4** — a védett lépések egyedül kitöltik a záró blokkot; a puffer-utasítás teljesíthetetlen
- Súlyosság: P2 · Bizalom: magas · Lencse: pedagógia
- Hely: M4.B:323–334; M6.A:612–650; M7.B:560–574; M4.A:74; M4.B:110
- Probléma: három záró blokkban a védett lépések alsó értéke együtt eléri vagy meghaladja a blokk hosszát, ezért a blokkhatáron belüli lépésvágással a keret nem érhető el. A G9 javaslata ezt nem mondja ki, és a „~10–15% puffer” egyik M4-peulában sem teljesíthető.
- Bizonyíték: M4.B:323 „**Rövid kiscsoportos (2–3 fős) megosztás (5 perc)**” · :325 „**Nagykörös zárókör – mondatbefejezések (5–7 perc)**” (a 10 perces blokkban) · M4.A:74 „**Tervezz ~10–15% puffert**”
- Hatás: a terepen a záró üzenet vagy a zárókör csonkul, vagyis épp az, amit a PRG-1 véd.
- Javaslat: EMBERI DÖNTÉS (modulgazdák; vétó: programvezető): blokkhatár-eltolás (B-változat, a 45 perc marad) vagy a védett lépés rövidítése; a puffer-mondatot a választott tervhez kell igazítani.
- Típus: emberi-döntés · Verdikt: –

**PED-5** — M6.A: a híd áthelyezése ütközik az ellenőrzőlistával
- Súlyosság: P2 · Bizalom: magas · Lencse: pedagógia
- Hely: M6.A:719–724, összevetve a D-20 csomag G9-javaslatával („a híd az M6.B-hez átkerül az M6.B elejére”)
- Probléma: a G9 javaslata kivenné az M6.A végéről azt a hidat, amelyet az M6.A saját ellenőrzőlistája a peula végére ír elő.
- Bizonyíték: M6.A:720–722 „Tudod, hogy a peula végén / rá kell mutatni: / ez a gondolkodás **közvetlenül belemegy**”
- Hatás: ha a modulgazda a G9-szöveget fogadja el, a blokk és az ellenőrzőlista ellentmond egymásnak, és az M6.B eleje is terhelődik (ezt nem vizsgáltam).
- Javaslat: EMBERI DÖNTÉS (M6 modulgazda): a híd maradjon 1 perces záró üzenetként (a terv így számol), vagy az ellenőrzőlista is változzon.
- Típus: emberi-döntés · Verdikt: –

**PED-6** — az F-peulák kérdésgyűjtésének számtana
- Súlyosság: P2 · Bizalom: magas · Lencse: pedagógia
- Hely: M5.F:284–298; M7.F:280–282
- Probléma: az M5.F a 4.3.0 két percét az 1–3 perces kérdésgyűjtésből vonja le, ami nulla vagy negatív időt ad. Az M7.F 1 percet szán egy olyan név nélküli módra, amely begyűjtést, átfutást és táblára írást kér.
- Bizonyíték: M5.F:296 „A két percet a következő kérdésgyűjtés idejéből vedd el, így a blokk nem lesz hosszabb.” · M7.F:280 „**Kérdésgyűjtés (kb. 1’)**”
- Hatás: a képző vagy kihagyja a kérdésgyűjtést, vagy a fogalomtérkép és a félreértések tisztázása rövidül.
- Javaslat: EMBERI DÖNTÉS (M5, M7 modulgazda; a percek VÉTÓLISTÁSAK): nyílt módban 1 perc, név nélküli módban 3 perc, a térképrész rövidítésével (lásd a tervet).
- Típus: emberi-döntés · Verdikt: –

**PED-7** — M7.F: a név nélküli begyűjtésből hiányzik az M5.F azonosíthatósági feltétele
- Súlyosság: P2 · Bizalom: alacsony · Lencse: pedagógia (a biztonság-jog lencsének továbbítandó)
- Hely: M7.F:219 és :282, összevetve az M5.F:225 és :302 sorával
- Probléma: az M5.F a jegyzetlapok név nélküli begyűjtését ahhoz köti, hogy a lapok „ténylegesen senkihez sem köthetők”. Az M7.F ugyanezt a lépést e feltétel nélkül engedi.
- Bizonyíték: M7.F:219 „A lap maradhat náluk, vagy név nélkül begyűjtheted kérdésgyűjtésnek.” · M5.F:225 „Név nélkül csak akkor gyűjtheted be a lapokat, ha ténylegesen senkihez sem köthetők”
- Hatás: egy 6 fős F-peulán a „név nélküli” lap a kézírásból azonosítható lehet, és két F-peula eltérő szabályt tanít.
- Javaslat: EMBERI DÖNTÉS (DPO: az ADV §3 „Név nélkül begyűjtött papír munkalap” sorának alkalmazása). A feltétel kiterjesztése az M7.F-re új alkalmazási eset, ezért nem objektív javítás.
- Típus: emberi-döntés · Verdikt: –

---

### (1) Amit nem tudtam ellenőrizni
- Minden realitásbecslés asztali; megfigyelt vagy pilotadat nincs.
- Az M5.1 kész H5P-vázlata és a VO-renderek hossza nem állt rendelkezésemre.
- Az M6.B elejét (a G9 hídjának célpontját), valamint az M4.F-et és az M6.F-et nem olvastam; nem voltak a feladatban.
- A belső blokkhatárok kötöttsége értelmezési kérdés: a D-20 csomag megtartaná őket, a HUM 14 PRG-1 szövege csak a 45 percet és a központi naptárt köti. Ezért adok mindenhol A- és B-változatot.
- Az érintett sorok pinjeit és manifesztállapotát nem futtattam. BUILD-INPUT-ként csak az M5.B-KART-02 (:219) és az M4.A-MUNK-02 (:397) érintettségét jelöltem.
- Nyitott, hogy az M4.B interjúköreinek minireflexiói védett reflexiós lépésnek számítanak-e (PED-2).

### (2) Ellentmondások a kánonban
- A PED-1…PED-7 fenti tételei.
- M5.B: a :377 „max. 2 percben” és a :392/:399 „2–3 perc/csoport” eltér; a :405 „Minden bemutatás után” ellentmond a :401 „(36–40’)” külön alsávjának.
- M5.A: a :527 „1–2 mondatra” és a :490 „1 mondatban” kis eltérés.
- M4.A: a :254 „a blokk 15 percben tartható” elfedi, hogy a terhelés átkerül a 4.4-be.
- M7.A: a :403 állítása 3 önkéntesnél hamis. Ez a D-20 „Addig” listáján már szerepel.
- M5.1: a :657 hamis. Ez maga a D-20 tétele (M5:QA-PED-2).

## Kiegészítés a célzott QA után (`9788c05`)

A `8bb4d7d` célzott QA-ja (QA17; riport: `2026-10-13 Célzott QA – D-csomagok átvezetése (8bb4d7d), AP-2026-10-13-01.md`) után ehhez a szerephez került tételek. A javasolt szöveg helyett itt a döntési kérdés áll; a javító commit nem implementálta őket.

- **M3:QA17-NYELV-14 (M3 modulgazda):** az M3.B 4.3.3 címében („Gyors alkalmazás – a 4. eset kívülről”) mire utal a „kívülről” az „új” törlése után (D-03): a 4.2-ben ki nem osztott esetre, vagy másra? Szövegjavaslat nincs.
- **M2:QA17-NYELV-10 (tájékoztatás, M2 modulgazda):** az M2.A :254-ben a „körbenézzenek” lépés visszakerült a nem érzékeny állításokra, mert a :271 lezárása erre épít; a GYV-20 kivétele (család, zsidóság, különbözőség: nincs kiállás) változatlan. Vétónál a :271-et kell igazítani.
