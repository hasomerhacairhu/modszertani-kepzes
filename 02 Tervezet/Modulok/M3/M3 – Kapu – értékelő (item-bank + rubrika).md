# M3 – KAPU – értékelő (item-bank + rubrika)

<!-- @asset-free
{
  "reason": "Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)"
}
-->

← Vissza a modul-hubhoz: **[M3 – „Kvuca, red flag, felelősség” – Csoportdinamika, korosztályok és gyermekvédelem](M3%20–%20Kvuca,%20red%20flag,%20felelősség%20–%20Csoportdinamika,%20korosztályok%20és%20gyermekvédelem.md)**

> ⚠️ **Az élesítés előtt a Memuna (gyermekvédelmi felelős) ellenőrzése szükséges.**
> Ez egy biztonságkritikus (gyermekvédelmi) kapu. Az éles használat előtt a kijelölt **Memuna** (a Somer gyermekvédelmi felelőse) olvassa át, és ellenőrizze a **helyi adatokat** (lásd a következő bekezdést). **Projektgazdai döntés (2026-10-02):** a gyermekvédelmi jóváhagyó a Memuna, operatív társdöntő a programvezető, jogi kérdésben a jogi szakértő dönt; a jelzési út az ötlépéses út (a Gyermekvédelmi működési standard v1.0 része, `Gyermekvédelem – release gate.md` §4.1), a jelzés címzettje a Memuna. **Utólagos ellenőrzés (vétó/QA):** a Memuna; a helyettes (a Ros Hinuh). A hívószámok és jogszabályi hivatkozások a magyar gyakorlatot tükrözik – ellenőrizd, hogy időközben nem változtak-e.
> **Helyi adatok és alternatív eszkalációs út (HUM-SAFE-01, projektgazdai döntés, 2026-10-02):** a Memuna a Somer mindenkori, a `somer.hu/kapcsolat` oldalon publikált Memunája; a helyettese a Ros Hinuh (oktatási vezető). A jelenlegi neveket a HUM-SAFE-01 rögzíti (`Emberi jóváhagyás szükséges.md`); az elérhetőséget a kurzus „Segítség és kapcsolatok” blokkja adja (a Somer központi száma, +36 70 42 76 637, a kapcsolati oldal szerint hétköznap 10–18 óra között hívható; ez nem ügyeleti vonal: munkaidőn kívül és közvetlen veszélyben a 112, illetve a Kék Vonal az út). Ha a gyanú épp a Memunára vonatkozik, vagy összeférhetetlenség áll fenn, a jelzés nem állhat meg az érintett személynél: a helyetteshez megy, ha pedig a helyettes érintett, a Memunához. Ha mindketten érintettek vagy nem elérhetők: Kék Vonal **116-111**, bántalmazott vagy eltűnt gyermek ügyében **116-000**, közvetlen veszélyben **112**. Közvetlen veszélynél előbb a biztonság és a **112**, utána a belső jelzés. Az incidensnyilvántartás külön, korlátozott hozzáférésű tár (Google Workspace Shared Drive → `Restricted / Safeguarding / Incidents`; hozzáférés csak a Memunának, a helyettesnek és a szervezeti vezetőnek), nem Moodle és nem GitHub. A tananyag nem határozza meg, hogy egy adott ügyben pontosan melyik külső szervhez és milyen jogcímen kell fordulni.
> **A safeguarding-tartalom (és ez a kapu) nem élesedik a Memuna ellenőrzése (vétó/QA) nélkül.**
>
> | Mező | Érték |
> |---|---|
> | **Lektor (Memuna – gyermekvédelmi felelős):** | a Somer mindenkori, a `somer.hu/kapcsolat` oldalon publikált Memunája; a jelenlegi nevét a HUM-SAFE-01 rögzíti (`Emberi jóváhagyás szükséges.md`) |
> | **Jóváhagyás dátuma:** | projektgazdai döntés: 2026-10-02 (HUM-SAFE-01); a Memuna utólagos ellenőrzésének (vétó/QA) dátuma a `RELEASE-READINESS.md` G1 kapujához tartozó #1 issue-ban rögzítendő |
> | **Következő felülvizsgálat:** | a Memuna utólagos ellenőrzésekor a `RELEASE-READINESS.md` G1 kapujához tartozó #1 issue-ban rögzítendő dátum |

---

## 0. A kapu adatai (fejlesztőnek / stábnak)

| Mező                           | Érték                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Modul**                      | M3 – „Kvuca, red flag, felelősség” – Csoportdinamika, korosztályok és gyermekvédelem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Kapu típusa**                | **Éles teljesítési kapu** (biztonságkritikus, gyermekvédelmi)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Komponens A – tudásmérés**   | Szcenárió-alapú kvíz – **Moodle Quiz** (Gradebook-súly; a „Grade to pass” **csak az összpont-komponens**). A kapu feltétele **konjunkció**: **≥10/12 ÉS a 2., 4., 7., 9. item mind helyes** – ezt **item-szintű/összetett feltétellel automatikusan csak akkor** szabad kikényszeríteni, ha a cél-környezet ezt **runtime acceptance-teszten igazoltan tudja**; egyébként a négy kritikus item helyességét **kézzel kell ellenőrizni**, mielőtt a kapu „megfelelt”-re kerül és a továbblépés megnyílik (lásd 1.2). **H5P Question Set csak akkor**, ha a Moodle-beli completionje **grade-alapú** (≥80% completionre állítva, **nem** attempt-/megtekintés-alapú) ÉS a kritikus itemek külön, **igazoltan** kikényszerítve – különben a kaput Moodle Quiz adja (vö. M7 KAPU minta).                                            |
| **Komponens B – produktum**    | **Moodle Assignment + rubrika** (modulproduktum: helyzetleírás)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Küszöb (A)**                 | **≥ 80%** → 12 itemből **legalább 10 helyes** (lásd 1.2 pontozás)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Kötelező (kritikus) itemek** | **2., 4., 7., 9.** item **helyes válasza kötelező** a 80% mellett is (lásd 1.2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Küszöb (B)**                 | Rubrika 1–4. sora mind legalább **„Alapszint (1)”**, az **R2 (titoktartás)** és **R4 (nem nyomoz / nem konfrontál)** sor **blokkoló**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Próbálkozások**              | **1 normál + 1 javító próbálkozás** automatikusan (kvíz: 2 automatikus próbálkozás, „Highest grade” értékelési mód; Assignment: a második, javító beadás után további csak kézzel); további próbálkozást a képző nyithat kézzel (elsajátításig tartó tanulás). A completionhöz **a legjobb megerősített eredmény** számít; egy már megszerzett teljesítés nem romolhat vissza önkéntes, gyakorló újrabeadástól, a legfrissebb próbálkozás visszajelzésként megmaradhat. Ha a kapu nem teljesül, a javító próbálkozás előtt az **M3.F (F-peula)** kötelező: a kapueredmény megerősítése után, a képző által a központi naptár szerint kijelölt időpontban. 2 sikertelen próbálkozás után **mentor bevonása (támogatás, nem büntetés)**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Újraértékelés**              | A madrich kérheti, hogy **az eredeti értékelőtől eltérő második képző** nézze át a beadást és a kapudöntést, még az M4 feloldása előtt; biztonságkritikus vitánál a **Memunát is be kell vonni** (Program terv §5). |
| **Belépő feltétel**            | M3.1–M3.4 activity completion. Az M3.B peula **nem formális előfeltétele** a leadásnak (a hub §6 belépő feltétele is csak az L1–L4 completion + Komponens B), de a modulproduktum (Komponens B) minőségi alapjához **erősen ajánlott az M3.B peulán való részvétel** (élő red-flag-felismerés, az első lépés és a lépéstérkép gyakorlása). Ajánlott sorrend: **M3.1–M3.2 → M3.A → M3.3–M3.4 → M3.B → produktum-leadás → kapu-kvíz**. **Aki kihagyta az M3.B-t, annál a mentor az átnézéskor kötelezően ellenőrzi az R3/R4 sort** a rubrika blokkoló-logikája szerint: az R4 (nem nyomoz / nem konfrontál) **blokkoló**, tehát itt is ugyanúgy buktat, ha 0; az R3-nál (kit von be) a leírásnak azt kell megneveznie, hogy a madrich **azonnal a kijelölt Memunát vonja be** (összeférhetetlenség esetén a név szerint kijelölt helyettesét). Ez nem enyhébb mérce a kihagyóknál – csak az élő gyakorlás hiányát pótolja átnézéssel. |
| **Item-randomizálás**          | **Kötelező:** a válaszlehetőségek sorrendjének keverése, mert a bankban szerkesztési okból a helyes válasz mindig a B vagy a C (lásd §1). **Ajánlott:** a kérdéssorrend keverése – ekkor a kritikus itemeket stabil kérdésnév azonosítsa (lásd 1.2). Próbálkozásonként cserélt item-pool csak slotonként validált, egyenértékű változatokkal használható; kritikus slotba csak a Memuna által jóváhagyott változat kerülhet. A jelenlegi bank 12 itemből áll, változatok nélkül, és több item a leckék interakcióihoz közeli helyzetre épül.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

**Miért éles és nem puha ez a kapu?** A gyermekvédelem és a red flag-felismerés **biztonsági kérdés** – itt nem elég a részvétel, mérhető megértés kell. Ezért: produktív Assignment + valódi ≥80% küszöb + kötelező kritikus itemek.

**Mit mér élesen ez a kapu, és mit nem?** A program-mátrix három kompetenciaterülete közül (Tuckman-szakaszok, 3 aktuális someres kvuca-profil, gyermekvédelem & red flag) **éles, küszöbös méréssel csak a harmadikat** – a gyermekvédelmi minimumot – ellenőrizzük; az item-bank (1–12) és a rubrika **szándékosan kizárólag** ezt méri. A **Tuckman- és a kvuca-profil-kompetencia formatív / completion-alapú**: az M3.1–M3.2 beágyazott H5P-kvízei (Drag & Drop, koppintásos párosítás, minikvíz) és az M3.A peula gyakoroltatják, és az **activity completion** fedi le – ezek nem buknak külön a kapun. Ez nem hiányosság, hanem a program **kapu-filozófiájával** összhangban álló döntés: „tisztán kvíz-kapu csak ott éles, ahol a biztonsági minimum-tudás konvergens ellenőrzése indokolt – ez gyakorlatilag az M3 gyermekvédelmi reflexei” (lásd Program terv §5). Így a program-mátrix három kompetenciát ígér, a kapu szándékosan egyet mér éles kapuval, a másik kettőt completion-szinten.

### Miért 12 item és miért így van a küszöb?
A kapu-validitási szempont fontos itt: az 5–8 itemes kvíznél a 80% durva ugrásokat ad (egy hiba még átmegy, a második már bukás), biztonságkritikus témánál ez nem védhető. **12 item** mellett a 80% = **10/12** helyes – ez egy hiba (11/12 ≈ 92%) és két hiba (10/12 ≈ 83%) esetén is átenged, három hiba (9/12 = 75%) esetén nem. Így a küszöb nem billen át egyetlen bizonytalan itemnél, **de** a négy legkritikusabb biztonsági állítást (titoktartás határa, akut önveszély, a gyanúsított figyelmeztetésének tilalma madrich vagy felnőtt elleni gyanúnál, meghallgatás ≠ nyomozás) **külön, kötelezően** is helyesen kell tudni – ezek tévesztése akkor is bukás, ha az összpontszám egyébként meglenne.

---

## 1. KOMPONENS A – Szcenárió-alapú item-bank (12 item)

> **Hangnem:** tegező, someres-barát. **Forma:** rövid szituáció + 4 opció + jelölt helyes válasz (✅) + miért jó/rossz minden opció + tanulói visszajelzés.
> A helyes válasz pozícióját az éles kvízben **keverd meg** – itt szerkesztési okból a helyes válasz mindig a B vagy a C.

### 1.1 Lefedettség (konstruktumvaliditás)
Az itemek pontosan az M3.3–M3.4-ben **ténylegesen tanított** elemeket mérik:

| Tanított elem (forrás) | Item |
|---|---|
| Red flag felismerése (M3.3 SLIDE 3) | 1 |
| Online zaklatás mint red flag (M3.3 SLIDE 4 – sértő mém szcenárió) | 11 |
| Nincs 100% titoktartás, mit ígérhetsz (M3.3 SLIDE 1, 4) | **2**, 8 |
| Akut önveszély sürgőssége – 112 / 116-111 (M3.3 SLIDE 4 ⚠️ doboz) | **4** |
| Meghallgatás ≠ nyomozás (M3.3 SLIDE 5 ✅ doboz) | **9** |
| Madrich vagy felnőtt elleni gyanú: ne konfrontáld, azonnal és közvetlenül a Memunának (M3.3 SLIDE 5 ⚠️ doboz) | **7** |
| Bizonytalanság esetén is jelezz; a red flag ritkán 100%-ig egyértelmű (M3.3 SLIDE 1 T/F2, SLIDE 3) | 12 |
| Jelzési út: **azonnal a kijelölt Memuna** (az ötlépéses jelzési út 4. lépése), NEM egyedül, NEM csoportchat (M3.3 SLIDE 2, 4) | 3, 5 |
| Madrich–chanich párkapcsolat = súlyos red flag (M3.3 SLIDE 5; M3.4 SLIDE 3–4) | 10 |
| Online határ / kedvenc chanich / Do-Don’t (M3.4 SLIDE 3–4) | 6 |

*(Félkövér = kötelező kritikus item.)*

### 1.2 Pontozás és küszöb
- 12 item, itemenként 1 pont. **Átmenő: ≥ 10/12 (≥ 80%).**
- **Kötelező kritikus itemek: 2, 4, 7, 9.** Ha ezek bármelyike rossz → **nem átmenő**, akkor is, ha az összpont ≥ 10. A feltétel **konjunkció**: „**összpont ≥ 10/12 ÉS a 2., 4., 7., 9. item mind helyes**”.
  - ⚠️ **Pontsúlyozás ezt NEM helyettesíti.** Semmilyen skalár pontküszöb nem kódolja a konjunkciót. Példa: ha a négy kritikus itemet 2 pontra súlyoznánk (4×2 + 8×1 = **16** a maximum), akkor „**mind a négy kritikus helyes + 2 egyéb hibás**” = 8 + 6 = **14**, és „**egy kritikus hibás + minden más helyes**” = 6 + 8 = **14** – **ugyanaz a pontszám, ellentétes kapu-eredmény**. Ezért a súlyozott pontozás tartalékmegoldásként **nem megengedett**.
  - **A két megengedett megvalósítás:** (a) a cél-Moodle **acceptance-teszten igazolt** item-szintű / összetett feltétele, **vagy** (b) **kézi ellenőrzés**: a négy kritikus item helyességét a kapu „megfelelt”-re állítása és a továbblépés megnyitása **előtt** valaki (mentor / kurzusfelelős) visszanézi; ehhez a kritikus itemeket a Moodle-ben stabil kérdésnév azonosítsa, ne a próbálkozásban megjelenő sorszám (kérdéskeverésnél ez próbálkozásonként más). A továbblépés a **megerősített, összetett kapueredményhez** kötődik (a kvíznél: összpont ÉS a négy kritikus item), nem a nyers összpontszámhoz.
  - Ha nincs igazolva, hogy a cél-konfiguráció a konjunkciót automatikusan ki tudja kényszeríteni, a (b) **kézi ellenőrzés kötelező**; nem ekvivalens helyettesítő (pl. súlyozott pontozás) ilyenkor sem használható. A konkrét mechanizmus **runtime acceptance-kérdés**, lásd [`LMS – H5P runtime acceptance.md`](../../LMS%20–%20H5P%20runtime%20acceptance.md).
- **Miért épp ez a négy a kritikus, és nem pl. a madrich–chanich párkapcsolat (ITEM 10) vagy az online zaklatás (ITEM 11)?** A kötelező négy item az a **konvergens, eljárásban is egyedi reflexnégyes**, amit elrontva a tanuló *aktívan árthat* (titoktartást ígér → 2; halaszt akut önveszélynél → 4; figyelmezteti a gyanúsított madrichtársat → 7; nyomoz a meghallgatás helyett → 9). Az ITEM 10 (madrich–chanich párkapcsolat) és az ITEM 11 (online zaklatás) **ugyanúgy súlyos red flag** (ld. §1.1), de jelenleg nem kritikus itemek. Az összpont-küszöb (≥ 10/12) **nem** garantálja a helyességüket: két nem kritikus item tévesztését megengedi, így például az ITEM 10 „A” és az ITEM 12 „A” válasza mellett is át lehet menni, ha minden más helyes, és ugyanez igaz az általános jelzési reflexet mérő ITEM 3/5/12-re is. Az ITEM 10 saját indoklása ráadásul madrich elleni gyanúként kezeli a helyzetet, a D opciója pedig a gyanúsított megszólítása, vagyis ugyanabba a hibaosztályba esik, mint a 7. item A opciója. Ezért ITEM 10/11 a **lefedettségben** kötelező (szerepel a bankban, méri a rubrika R1 sora is), a **kötelező kritikus** körben viszont jelenleg nem szerepel – ha a stáb a Gyermekvédelmi működési standard v1.0 alapján szigorítani akar, ITEM 10 bevonható ötödik kritikus itemként (5/12 még védhető arány a 12-item mellett), de ez **a Memuna döntése** az élesítés előtti ellenőrzéskor.

### 1.3 Tanulói bevezető (a Moodle Quiz leírásába)

*Fejlesztőnek:* a bevezető elé a Program terv §4 és §7 szerinti „just-in-time” adatkezelési tájékoztató kerül; a kettő ütközésében a szigorúbb, kisebb hozzáférést engedő szabály érvényes (a zárt kvíz pontszámát az értékelő látja). A címzetteket, a jogalapot és a megőrzést a HUM-PRIV-01 adatkezelési mátrixa adja (`Adatvédelem – tanulói adatok és AI.md` §3) – itt nem másoljuk; a kapcsolattartási utat itt nem töltjük ki. A bevezető megnevezi a kötelező biztonsági helyzetek témáit (titoktartás, akut veszély, jelzési út, meghallgatás), a kvíz konkrét kulcsát viszont nem. *(Projektgazdai döntés, 2026-10-02. Utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős; a kritikus témák megnevezésénél az értékelési felelős és a Memuna.)*

> Ez a kvíz az M3 éles, kétrészes kapujának egyik része, a másik a helyzetleírásod (modulproduktum). 12 rövid helyzetet kapsz: legalább 10-re kell jól válaszolnod, és a kötelező biztonsági helyzetek mindegyikére is helyesen kell felelned. Ha ezek közül bármelyik nem sikerül, akkor is újra kell próbálkoznod, ha az összpontod meglenne. A kötelező helyzetek négy témát érintenek: a titoktartást, az akut veszélyt, a jelzési utat és azt, hogyan hallgatod meg a chanichot, ha valami nehezet mond el. Ha elsőre nem sikerül, a visszajelzésed alapján a felzárkóztató peulán (F-peula, M3.F) dolgozol – ez ilyenkor kötelező –, utána van egy javító próbálkozásod; további próbálkozást a képződ nyithat. A teljesítéshez a legjobb megerősített eredményed számít. Az M4 akkor nyílik meg, amikor mindkét rész eredményét megerősítették; a még meg nem erősített eredmény nem bukás. Ha nem értesz egyet a kapudöntéssel, kérheted, hogy egy másik képző is átnézze, még mielőtt az M4 megnyílik.
>
> *A kérdésekben szereplő kijelölt **Memuna** a Somer gyermekvédelmi felelőse.*

---

### ITEM 1 – Red flag felismerése (mi számít red flag-nek)
**Szituáció:** Négy dolgot látsz a héten a kvucádban. Melyik az, amire **biztosan red flag-ként** kell felkapnod a fejed?

- A) Az egyik chanich elfelejtette, hánykor kezdődik a péntek esti peula.
- B) Egy chanich karján több régebbi vágásnyomot látsz, és „viccesen” söpri le, amikor szóba kerül. ✅
- C) A kvuca fele hangosan nevet egy bennfentes poénon.
- D) Egy chanich azt mondja, nem szereti a csoportos játékokat, jobban szeret rajzolni.

**Miért ez a jó / miért rossz a többi:**
- ✅ **B** – Az önsértésre utaló jel (vágásnyom) + bagatellizáló magyarázat tipikus, a leckében is szereplő red flag. Komolyan kell venni és jelezni.
- A – Feledékenység normál kamaszviselkedés, nem biztonsági jel.
- C – Egy belső poén önmagában csoportélet, nem red flag (akkor lenne az, ha valakit megaláznának vele).
- D – Eltérő preferencia (introverzió) nem red flag; a sokszínűség normális.

**Tanulói visszajelzés:** „A red flag nem a furcsa vagy csendes viselkedés, hanem a **biztonságot fenyegető** jel: bántalmazás, önsértés, zaklatás, határátlépés. A vágásnyom + lekicsinylés pont ilyen.”

---

### ITEM 2 – Mit ígérhetsz a titoktartásról *(KRITIKUS)*
**Szituáció:** Egy chanich peula után odajön: „Mondok valamit, de **esküdj meg, hogy soha senkinek nem mondod el**, jó?” Mit válaszolsz felelős madrichként?

- A) „Megígérem, esküszöm, ez köztünk marad, bármi is az – tudod, hogy bízhatsz bennem, nem mondom el senkinek.”
- B) „Fontos, amit mondasz, de teljes titoktartást nem ígérhetek – elmondom, kinek és miért szólok, és nem hagylak egyedül.” ✅
- C) „Inkább most ne mondd el, mert ha komoly, úgyis tovább kell adnom, és nem akarlak ezzel kínos helyzetbe hozni.”
- D) „Oké, megígérem a titoktartást, de csak ha nem valami nagy dolog – és ha kiderül, hogy mégis komoly, akkor majd utólag szólok neked, hogy visszavonom.”

**Miért ez a jó / miért rossz a többi:**
- ✅ **B** – Ez a tananyag (és a nemzetközi gyermekvédelmi gyakorlat) magja: **nem ígérsz teljes titoktartást**, de átláthatóan elmondod, kinek és miért szólsz, és hogy nem hagyod egyedül.
- A – Veszélyes: nem tudhatod előre, mi jön; lehet, hogy azonnal be kell vonnod a Memunát. A titoktartás-ígéret csapdába visz.
- C – Elhárítás: a chanich épp segítséget keres, ne riaszd el.
- D – Ez is titoktartás-ígéret, csak feltétellel és utólagos visszavonással; a chanich így nem fog beszélni a nagy dologról – pont a lényeg veszik el.

**Tanulói visszajelzés:** „Soha ne ígérj 100% titoktartást. Amit ígérhetsz: komolyan veszem, elmondom, **kinek és miért** szólok, és **nem hagylak egyedül**.”

---

### ITEM 3 – Jelzési út: kihez fordulsz
**Szituáció:** Biztos vagy benne, hogy egy chanichhal kapcsolatban red flag helyzet áll fenn, és jelezni akarsz. **Kihez** fordulsz elsőként a someres keretben?

- A) A kvuca csoportchatjébe írom ki, hogy mindenki figyeljen oda.
- B) Azonnal a Memunához fordulok. ✅
- C) Megírom a chanich szüleinek privátban, és rájuk bízom.
- D) Előbb a chanich barátait kérdezem meg, mit tudnak, hogy pontos részleteket vihessek, és csak utána szólok a Memunának.

**Miért ez a jó / miért rossz a többi:**
- ✅ **B** – Nem neked kell rögtönözni, hogy „kinek szólj”. Gyermekvédelmi ügyben az ötlépéses jelzési út szerint **azonnal a kijelölt Memunát** vonod be (összeférhetetlenség esetén a név szerint kijelölt helyettesét); a további lépésekről (szülő, szakember bevonása) innentől nem te döntesz egyedül. Te nem maradsz egyedül a helyzettel.
- A – A csoportchatbe kiírni súlyos adatvédelmi és bizalmi határsértés, megalázhatja az érintettet.
- C – A szülő bevonása nem a madrich önálló döntése; lehet, hogy épp otthon a baj. Ez a Memuna és a szakemberek mérlegelése.
- D – A barátok kikérdezése már nyomozás, ami nem a te dolgod, és csak késlelteti a jelzést; ráadásul az érintett ügye így mások előtt is kitudódhat. A Memunát azonnal kell bevonni, nem „bizonyítékokkal” később.

**Tanulói visszajelzés:** „A jelzés **azonnal a kijelölt Memunához** megy (összeférhetetlenség esetén a név szerint kijelölt helyetteséhez), nem a kvucának és nem saját döntésből közvetlenül a szülőnek. Nem te nyomozol, és nem te találod ki egyedül a következő lépést.”

---

### ITEM 4 – Akut önveszély sürgőssége *(KRITIKUS)*
**Szituáció:** Este 23:15. Egy chanich privát üzenetben azt írja, hogy **most, ma este úgy érzi, kárt tenne magában**, és egyedül van otthon. Mi a felelős reakció?

- A) Megírom, hogy beszéljük meg holnap a peulán, addig próbáljon aludni, és felírom magamnak, hogy reggel rákérdezek, hogy van.
- B) Nem hagyom egyedül, és azonnal bevonom a Memunát; közvetlen veszélynél előbb a 112-t hívom. Gyerek/fiatal lelki krízisében a 116-111 Kék Vonal kiegészítő támogatás lehet. ✅
- C) Megnyugtatom, hogy ez biztosan csak egy nehéz este, átbeszéljük chaten a problémáit, és megígérem neki, hogy ez kettőnk titka marad.
- D) Megkérem a hozzá legközelebb lakó, vele jóban lévő chanichot, hogy menjen át és maradjon vele éjszakára, és reggel szólok a Memunának.

**Miért ez a jó / miért rossz a többi:**
- ✅ **B** – Az **akut, aznapi** önveszély **sürgős**. Ne maradjon egyedül, és azonnal vond be a kijelölt Memunát; **közvetlen veszélynél előbb a biztonság és a 112**, utána a belső jelzés. A **116-111 Kék Vonal** gyerekek és fiatalok számára kiegészítő lelki támogatás lehet, de nem helyettesíti a sürgősségi utat és a belső jelzést.
- A – A halasztás („majd holnap”) közvetlen veszélynél elfogadhatatlan.
- C – A „biztosan elmúlik” bagatellizál, a titoktartás-ígéret pedig itt különösen veszélyes.
- D – Jó szándékú, de veszélyes: egy akut önveszélyes helyzet felelőssége **nem hárítható egy másik gyerekre**, és a Memuna bevonása **nem várhat reggelig**. A kortárs nem tud (és nem is szabad neki) egy krízist kezelni; ettől a chanich is és a „kirendelt” társa is magára marad.

**Tanulói visszajelzés:** „Akut önveszélynél a kulcs: **ne maradjon egyedül, azonnal vond be a Memunát, közvetlen veszélynél pedig előbb a biztonság és a 112, utána a belső jelzés**. Ez nem várhat másnapig. Gyerek/fiatal lelki krízisében a **116-111 Kék Vonal** kiegészítő támogatás lehet.”

---

### ITEM 5 – Az „egyedül megoldom”-csapda
**Szituáció:** Egy chanich nehéz dolgot oszt meg veled, és nagyon bízik benned. Azt érzed, „nem akarom elárulni a bizalmát”. Mit teszel?

- A) Megtartom magamnak, és igyekszem egyedül, chaten átsegíteni rajta, mert megbízott bennem.
- B) Komolyan veszem, azonnal bevonom a Memunát, és elmagyarázom a chanichnak, hogy ez nem árulás, hanem azért van, hogy igazi segítséget kapjon. ✅
- C) Megmondom neki, hogy ez túl nagy dolog nekem, és inkább ne meséljen ilyet.
- D) Megígérem, hogy senkinek nem mondom el, különben nem bízik meg bennem többé; majd ha ő is készen áll, együtt szólunk a Memunának.

**Miért ez a jó / miért rossz a többi:**
- ✅ **B** – A bizalom megtartása **nem** azt jelenti, hogy egyedül cipeled. A madrich láncszem, nem terapeuta; a kijelölt Memuna bevonása a chanich érdeke.
- A – Az „egyedül megoldom” épp a leggyakoribb és legkockázatosabb hiba; nem vagy sem terapeuta, sem nyomozó.
- C – Elutasítás: a chanich így megtanulja, hogy nincs kihez fordulnia.
- D – A titoktartás-ígéret csapdába visz: lehet, hogy azonnal be kell vonnod a Memunát, és akkor vagy megszeged az ígéreted, vagy magára hagyod a chanichot. A „majd ha készen áll” halogatás pedig a kockázatot növeli.

**Tanulói visszajelzés:** „Nem az a jó madrich, aki mindent egyedül megold, hanem aki tudja, **mikor kér segítséget**. A bevonás a chanich védelme, nem árulás.”

---

### ITEM 6 – Online határ (Do / Don’t)
**Szituáció:** Melyik viselkedés **OK** madrichként az online térben?

- A) Minden este külön, privátban írsz az egyik chanichnak, hogy „jóéjt ❤️”.
- B) Privátban kérsz egy chanichtól képet magáról, mert kíváncsi vagy, hogy néz ki most.
- C) A kvucával közösen alakítotok ki chat-szabályokat (pl. este 10 után nem írunk), és a csoportos kommunikációt részesíted előnyben. ✅
- D) A személyes profilodról privátban küldözgetsz egy chanichnak éjszakai üzeneteket, hogy közelebb kerüljetek.

**Miért ez a jó / miért rossz a többi:**
- ✅ **C** – A közös, átlátható chat-szabály és a csoportos kommunikáció a tanított jó gyakorlat: véd téged és a chanichot is.
- A – A rendszeres, intim hangvételű privát éjszakai üzenet határátlépés és „kedvenc chanich” irányába visz.
- B – Kép kérése egy chanichtól súlyos határsértés, soha nem OK.
- D – Az éjszakai privát közeledés tipikus „grooming”-jellegű határátlépés.

**Tanulói visszajelzés:** „Online a jó keret: **közös szabály + csoportos csatorna**. A rendszeres privát éjszakai üzengetés és a képkérés nem fér bele.”

---

### ITEM 7 – Madrichtárs elleni gyanú: ne figyelmeztesd a gyanúsítottat *(KRITIKUS)*
**Szituáció:** Észreveszed, hogy **egy másik madrich** feltűnően sokat van négyszemközt egy chanichhal, sok az ölelés, és „ezt ne mondjuk el senkinek” mondatok mennek. Mit teszel **először**?

- A) Odamegyek a másik madrichhoz, négyszemközt szóvá teszem, amit látok, és megkérem, hogy hagyja abba.
- B) Azonnal és közvetlenül a Memunának jelzek, a gyanúsított madrichot pedig nem figyelmeztetem. ✅
- C) Diszkréten kikérdezem a chanichot a részletekről, hogy legyen elég konkrétumom, mielőtt bárkit bevádolok.
- D) Várok és diszkréten tovább figyelem őket néhány napig, hátha csak félreértem a helyzetet, és csak akkor szólok a Memunának, ha egészen biztosat tudok.

**Miért ez a jó / miért rossz a többi:**
- ✅ **B** – Ha a gyanú egy madrichtársra, kollégára vagy más felnőttre vonatkozik, **ne konfrontáld** a gyanúsítottat, mert ezzel figyelmeztetheted őt, és veszélyeztetheted a későbbi kivizsgálást. **Azonnal és közvetlenül a kijelölt Memunának** jelezz (összeférhetetlenség esetén a név szerint kijelölt helyettesének).
- A – A gyanúsított konfrontálása a legveszélyesebb hiba: riasztod, és tönkreteheted a kivizsgálást.
- C – A chanich kikérdezése = nyomozás, ami nem a te dolgod (meghallgatni szabad, kihallgatni nem).
- D – A halogatás itt is kockázatos; a jelzés akkor is helyes, ha utóbb kiderül, hogy félreértés volt.

**Tanulói visszajelzés:** „Ha a gyanú **egy madrichtársra, kollégára vagy más felnőttre** vonatkozik: **ne beszéld meg vele, ne konfrontáld**. Azonnal a kijelölt Memunának jelezz – ha a gyanú őt érinti, a név szerint kijelölt helyettesének.”

---

### ITEM 8 – Mit ígérhetsz / mit nem (a pontos mondat)
**Szituáció:** Egy chanich megosztott veled valami nehezet. Melyik mondat a **felelős** és pontos?

- A) „Ígérem, ez kettőnk titka marad, senki nem fogja megtudni.”
- B) „Megígérem, hogy megoldom a problémádat, ne aggódj.”
- C) „Komolyan veszem. Lehet, hogy segítséget kell kérnünk, ezért elmondom, kinek és miért szólok – de nem hagylak egyedül ezzel.” ✅
- D) „Ez túl nagy, szólok rögtön mindenkinek, aki csak eszembe jut.”

**Miért ez a jó / miért rossz a többi:**
- ✅ **C** – Két dolgot ígér, amit szabad: komolyan veszem + nem hagylak egyedül; és átláthatóan jelzi a megosztás határát (kinek/miért).
- A – Titoktartás-ígéret: tilos.
- B – A megoldás megígérése irreális és nem a te szereped (nem vagy terapeuta).
- D – A „mindenkinek szólok” a másik véglet: a jelzés **csak ahhoz** megy, aki segíteni tud (a Memunához), nem fűnek-fának – ez a bizalom és az adatvédelem megsértése.

**Tanulói visszajelzés:** „A jó mondat **nem** ígér titoktartást és **nem** ígér megoldást, de megígéri: komolyan veszem, elmondom, **kinek és miért** szólok, és **nem maradsz egyedül**. A jelzés célzott (a Memunának szól), nem szétkürtölés.”

---

### ITEM 9 – Meghallgatás ≠ nyomozás *(KRITIKUS)*
**Szituáció:** Egy chanich **magától** kezd mesélni arról, hogy otthon bántják. Hogyan hallgatod meg helyesen?

- A) Részletesen kikérdezem: pontosan ki, mikor, hányszor, mivel – hogy minél több konkrét infóm legyen a jelzéshez, és a Memunának könnyebb dolga legyen.
- B) Nyugodtan, ítélkezés nélkül meghallgatom, hagyom a saját szavaival mesélni, és csak nyílt kérdést teszek fel – nem nyomozok. ✅
- C) Óvatosan megkérdőjelezem, amit mond, hogy lássam, biztosan igaz-e, és nehogy valakit utóbb alaptalanul mártsak be egy komoly üggyel.
- D) Gyorsan megnyugtatom, hogy „biztos nem olyan vészes”, és témát váltok, hogy ne legyen kínos egyikünknek se a beszélgetés.

**Miért ez a jó / miért rossz a többi:**
- ✅ **B** – A gyermekvédelem alapelve: **meghallgatni szabad, kihallgatni / nyomozni nem.** Nyugodt, ítélkezésmentes, a gyermek saját szavaival – a részletek kiderítése a Memuna és a hatóság dolga.
- A – A részletes kikérdezés = nyomozás; árthat a gyereknek és a későbbi hivatalos eljárásnak.
- C – A kétségbe vonás („biztosan igaz-e”) eltántorítja a gyereket; nem a te dolgod eldönteni, igazat mond-e.
- D – A bagatellizálás és témaváltás elnémítja; pont az ellenkezője a komolyan vételnek.

**Tanulói visszajelzés:** „**Meghallgatni szabad – nyomozni nem.** Nyugodtan, ítélkezés nélkül, a gyerek saját szavaival; a részletek a Memuna és a hatóság dolga. Amit hallasz, a **gyerek szavaival** add tovább.”

---

### ITEM 10 – Madrich–chanich párkapcsolat
**Szituáció:** Egy madrich elmondja neked négyszemközt, hogy „összejött” egy chanichhal, de kéri, hogy tartsd titokban. Hogyan értékeled ezt?

- A) Ha mindketten akarják, magánügy, és nem kell beleszólni.
- B) Kínos, de mivel a madrich idősebb és tapasztaltabb nálad, jobb nem ütközni vele.
- C) Ez súlyos red flag – madrich nem lehet párkapcsolatban chanichhal –, és mindig azonnal be kell vonni a Memunát. ✅
- D) Megmondom a madrichnak, hogy ez gáz, és ezzel le is van tudva a dolog.

**Miért ez a jó / miért rossz a többi:**
- ✅ **C** – A madrich–chanich párkapcsolat **elfogadhatatlan határátlépés, önmagában súlyos red flag**; itt a kijelölt Memuna azonnali bevonása kötelező (és madrich elleni gyanúként kezelendő: ne a kvucának, hanem a Memunának jelezz).
- A – A „magánügy / kölcsönös beleegyezés” érv itt nem érvényes: a felelősségi és hatalmi különbség miatt elfogadhatatlan.
- B – A „ne ütközz a tapasztaltabbal” a hallgatás csapdája; a védelem fontosabb a kínos érzésnél.
- D – A puszta „ez gáz” megjegyzés **nem** jelzés; a Memunához kell vinni (és a gyanúsítottat nem a te dolgod konfrontálni).

**Tanulói visszajelzés:** „Madrich–chanich párkapcsolat = **súlyos red flag, mindig azonnali jelzés a kijelölt Memunának**. Nem magánügy, és nem oldódik meg egy odavetett ‘ez gáz’-zal.”

---

### ITEM 11 – Online zaklatás a csoportchatben
**Szituáció:** A kvuca csoportchatjében valaki egy **megalázó mémet** küld egy másik chanichról; többen nevetnek, az érintett nem ír semmit. Mit lépsz madrichként?

- A) Semmit, mert nem akarok belekeveredni egy poénba.
- B) Privátban ráírok a küldőre, hogy törölje a mémet, és ennyivel le is zárom – nem viszem tovább, hogy ne legyen még nagyobb ügy belőle.
- C) Kiállok a chatben: leírom, hogy ez bántó, és nálunk ilyet nem küldünk, majd külön jelzem a Memunának, mi történt. ✅
- D) Privátban megírom az érintettnek, hogy ne foglalkozzon vele, biztos csak vicc.

**Miért ez a jó / miért rossz a többi:**
- ✅ **C** – Ez online zaklatásgyanú: a madrich a helyszínen kiáll a keretért **és** jelez a Memunának. Két lépés együtt.
- A – A „csak poén” elbagatellizálás; a hallgatás a bántalmazónak ad teret.
- B – Csábító „elintéztem”-érzés, de fél megoldás: a privát törlési kéréssel **nem állsz ki nyilvánosan a keretért** (a kvuca azt látja, hogy ez következmény nélkül maradt), és **kihagyod a Memunának szóló jelzést**. Az érintett chanich így továbbra is támogatás nélkül marad – a „ne legyen nagy ügy” pont a hallgatás csapdája.
- D – Az érintett egyedüli „ne foglalkozz vele” lerázása nem védi meg, és nem szünteti meg a zaklatást.

**Tanulói visszajelzés:** „Online zaklatásnál **a helyszínen is kiállsz** (ezt nálunk nem küldünk) **és jelzel** a Memunának. A ‘csak poén’ és a továbbküldés nem opció.”

---

### ITEM 12 – Bizonytalanság: szóljak vagy ne?
**Szituáció:** Valami **gyanús**, de nem vagy 100%-ig biztos benne, hogy red flag. Félsz, hogy „túlreagálod”. Mit teszel?

- A) Inkább nem szólok, nehogy feleslegesen pánikot keltsek vagy valakit megvádoljak.
- B) Jelzek a Memunának, mert bizonytalanságban is biztonságosabb kérdezni, mint egyedül cipelni – ha kiderül, hogy nem red flag, akkor sem baj, hogy szóltam. ✅
- C) Addig figyelek és gyűjtök bizonyítékot egyedül, amíg 100%-ig biztos nem leszek, és csak utána szólok a Memunának.
- D) Megkérdezem a kvuca többi tagját, mit gondolnak róla.

**Miért ez a jó / miért rossz a többi:**
- ✅ **B** – A red flag **ritkán 100%-ig egyértelmű**; a tananyag is mondja: bizonytalanságban is fontosabb segítséget kérni, mint egyedül maradni. A „felesleges” jelzés sem baj.
- A – A „túlreagálás”-tól való félelem a leggyakoribb ok a végzetes hallgatásra.
- C – Az egyedüli „bizonyítékgyűjtés” = nyomozás, ami nem a te dolgod, és időveszteséggel jár.
- D – A kvuca bevonása pletykát szül és sérti az érintettet; a jelzés a Memunához megy.

**Tanulói visszajelzés:** „A red flag ritkán teljesen biztos. **Bizonytalanságban is jelezz** a Memunának – ha kiderül, hogy semmi, az sem baj. Nem te nyomozol, és nem a kvucától kérsz tanácsot.”

---

## 2. KOMPONENS B – Assignment-rubrika a modulproduktumhoz

> **Modulproduktum (M3.4 SLIDE 7):** rövid, **kitalált, de életszerű helyzetleírás** (max. 8–10 mondat), amelyben a tanuló leírja, hol játszódik és milyen kvucában, mi történik; megnevez **legalább egy red flaget**; leírja **a felelős madrich első lépését** (mit mond / mit NEM ígér) és azt, **kit von be**.
> **Csak kitalált eset:** kapuproduktumba csak kitalált, életszerű eset kerülhet; valós eset névtelenítve sem, mert kis közösségben könnyen visszaazonosítható. Valós gyermekvédelmi eset soha nem pedagógiai feladat: ha egy beadás mégis valós esetre utal, az gyermekvédelmi ügy, és az ötlépéses jelzési út szerint azonnal a Memunát kell bevonni; a beadás kikerül a Moodle-ből, és az incidensfolyamatba kerül (`Adatvédelem – tanulói adatok és AI.md` §3).
> **LMS-eszköz:** Moodle Assignment + alábbi analitikus rubrika.

### 2.1 Hogyan használd
- A rubrika **4 sorból** áll, mindegyik **3 szintes**: **Nem megfelelő (0) / Alapszint (1) / Magabiztos (2)**.
- A szintek **megfigyelhető szövegjegyre** épülnek (mi olvasható a beadványban), nem általános „jó/rossz” benyomásra.
- **Átmenő (pass):** mind a 4 sor legalább **Alapszint (1)**, **ÉS** az **R2 (titoktartás)** és **R4 (nem nyomoz / nem konfrontál)** sor **blokkoló** → ha bármelyik 0, a beadvány **nem mehet át** a többi sortól függetlenül (gyermekvédelmi tét).
- **Bukásnál:** rövid fejlesztő visszajelzés a **Megfigyelés → Hatás → Következő lépés** modell szerint (mi hiányzik, melyik leckéhez térjen vissza) + újraleadás (elsajátításig tartó tanulás). Az újraleadás (javító próbálkozás) előtt az **M3.F (F-peula)** kötelező: ez a facilitált javítási alkalom, amely erre a visszajelzésre épít. Nincs kizárás.
- **Kalibráció és kétszemes döntés (Program terv §5):** a kapu-szezon előtt az értékelők közösen átbeszélik a rubrikát, és 1–2 referenciamintát együtt pontoznak. Az R2 és az R4 blokkoló sornál a „javításra megy / blokkol” döntés kétszemes – mentor + második képző + a Memuna –, nem egyetlen értékelő döntése. A kapu csak akkor élesedhet, ha a kalibráció és a kétszemes döntési rend rögzítve van.

### 2.2 A rubrika (4 sor × 3 szint)

| Kritérium (mit nézünk) | Nem megfelelő (0) | Alapszint (1) | Magabiztos (2) |
|---|---|---|---|
| **R1 – Red flag megnevezése** *(megfigyelhető: a szövegben néven nevezi a biztonsági jelet)* | Nem nevez meg valódi red flaget, vagy ártalmatlan dolgot címkéz red flagnek (pl. „csendes a chanich”). | **Legalább 1 valódi** red flaget pontosan megnevez (pl. önsértésgyanú, online zaklatás, madrich–chanich határátlépés, bántalmazásgyanú) és röviden indokolja, miért az. | Több releváns red flaget azonosít vagy egyet mélyebben elemez (mire kell figyelni, miért nem egyértelmű), és megkülönbözteti a „lassú” red flaget az **akut** veszélytől. |
| **R2 – Titoktartás kezelése** *(BLOKKOLÓ)* *(megfigyelhető: mit ígér / nem ígér a leírt madrich)* | A leírt első lépésben **titoktartást ígér** (pl. „megígérem, hogy nem szólok senkinek”), vagy a titoktartás kérdését meg sem említi. | A leírt madrich kimondja, hogy **nem ígér 100% titoktartást**, és jelzi, hogy bevonhat mást. | A leírt madrich pontosan megfogalmazza a felelős mondatot: komolyan veszem + elmondom, **kinek és miért** szólok + **nem hagylak egyedül**; a megosztást a **Memunára** korlátozza (nem „mindenkinek”). |
| **R3 – Felelős első lépés + kit von be** *(megfigyelhető: megnevezi, hogy a madrich azonnal a Memunát vonja be)* | Nincs konkrét lépés, vagy egyedül „megoldja”, vagy a kvucának / csoportchatnek / közvetlenül a szülőnek „jelez”. | Megnevezi, hogy a leírt madrich **azonnal a kijelölt Memunát vonja be** (összeférhetetlenség esetén a név szerint kijelölt helyettesét). | A bevonás illeszkedik a helyzet **súlyosságához és típusához**: akut önveszélynél azonnal a Memuna, közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés / kiegészítő támogatásként 116-111; madrich vagy felnőtt elleni gyanúnál közvetlenül a Memuna; és van utánkövetés-elem („nem tűnik el a levegőben”). |
| **R4 – Nem nyomoz / nem konfrontál + életszerű helyzet** *(BLOKKOLÓ)* *(megfigyelhető: a leírt viselkedés)* | A leírt madrich **nyomoz / kikérdez** (ki, mikor, hányszor), **vagy konfrontálja** a gyanúsított madrichot vagy felnőttet, **vagy** a helyzet nem életszerű / nem értelmezhető. | A leírt madrich **meghallgat, de nem nyomoz**, és madrich vagy felnőtt elleni gyanú esetén **nem konfrontálja** a gyanúsítottat; a helyzet életszerű, konkrét (hely + kvuca + esemény). | Tudatosan jelzi a „meghallgatni szabad, nyomozni nem” elvet (pl. nyílt, nem rávezető kérdés, a gyerek saját szavainak pontos továbbadása), madrich vagy felnőtt elleni gyanúnál a diszkrét, közvetlen jelzést a Memunának; a helyzet konkrét és reflektált. |

### 2.3 Pontozás-összegzés (stábnak)
- **Maximum:** 8 pont (4 sor × 2).
- **Átmenési feltétel:** minden sor ≥ 1 **ÉS** R2 ≥ 1 **ÉS** R4 ≥ 1 (a két blokkoló sor 0-ja önmagában bukás).
- **Átmenő pontsáv:** 4–8 pont, **feltéve, hogy mind a 4 sor ≥ 1** (tehát minden sor legalább Alapszint). Ha **bármely sor 0** (köztük a blokkoló R2 vagy R4) → fejlesztő visszajelzés + újraleadás. (A 4/8 csak akkor átmenő, ha tényleg minden sor ≥ 1; egyetlen 0-s sor – akár nem blokkoló – is bukás, mert a „minden sor ≥ 1” feltétel sérül.)
- A pontszám **másodlagos** a két blokkoló kritériumhoz képest: ez biztonsági, nem „pontvadász” értékelés.
- **Továbblépés (unlock):** a 4–8 pontsáv **nem „Grade to pass”**. A Moodle natívan az összpontot látja, a „minden sor ≥ 1” feltételt és a blokkoló R2/R4 sort nem, így egy 2/0/2/0 = 4 pontos beadvány (a leírt madrich titoktartást ígér és nyomoz) a nyers határt elérheti, miközben a kapun megbukik. Az M4 a **megerősített, összetett kapueredmény** után nyílik (Komponens A és B együtt), nem a nyers pontszám alapján; ha az összetett feltétel Moodle-ben nem kódolható bizonyítottan, a továbblépés feltételét az [`LMS – activity manifest.md`](../../LMS%20–%20activity%20manifest.md) §4 szerinti `GATE_CONFIRMED_M3` stáb-checkpointhoz kell kötni.
- **Megerősítési határidő:** a kapueredményt legkésőbb 24 órával a következő fix alkalom (az M4.A) előtt meg kell erősíteni; pénteki A-peulánál a beadás szerda 18:00-ig, az első értékelés csütörtök délután, a megerősítés legkésőbb csütörtök 18:00-ig történik. A függőben lévő (még nem megerősített) eredmény nem bukás.

### 2.4 Kész visszajelzés-sablonok (a stáb gyorsításához)
- **R1 hiány (nincs valódi red flag):** „A leírásban nem látszik valódi red flag. A red flag nem a furcsa vagy csendes viselkedés, hanem a biztonságot fenyegető jel: bántalmazás, önsértés, zaklatás, határátlépés. Nevezz meg legalább egyet, és röviden indokold, miért az. (Vissza: M3.3, 3. dia.)”
- **R2 hiány (titoktartást ígért):** „Itt a leírt madrich megígérte a titoktartást – ez a leggyakoribb csapda. Írd át úgy, hogy *nem* ígér teljes titoktartást, de elmondja, kinek-miért szól, és hogy nem hagyja egyedül. (Vissza: M3.3, 1. és 4. dia.)”
- **R3 hiány (nincs jelzés a Memunának):** „A red flaget jól látod, de a leírásból hiányzik, hogy a madrich **azonnal bevonja a kijelölt Memunát**. Az ötlépéses jelzési út (M3.B lépéstérkép) alapján nevezd meg. (Vissza: M3.3, 2. dia.)”
- **R4 hiány (nyomoz / konfrontál):** „A leírt madrich kikérdez / szembesít – ez már nyomozás. Cseréld le: meghallgat, de nem faggat, és madrich vagy felnőtt elleni gyanúnál közvetlenül a Memunának jelez, nem a gyanúsítottnak. (Vissza: M3.3, 5. dia.)”

---

## 3. Mentor bevonása (2 sikertelen próbálkozás után)

A mentor a tanulási analitika alapján nézze át, **mely red flag típust** nem ismeri fel a tanuló (kvíz item-szintű adat), és melyik rubrikasor gyenge. Tipikus fókuszok: **titoktartás határa (item 2, 8 / R2)**, **akut önveszély (item 4)**, **madrich vagy felnőtt elleni gyanú / a gyanúsított figyelmeztetése (item 7 / R4)**, **meghallgatás vs. nyomozás (item 9 / R4)**. A beszélgetés **támogató, nem büntető** – a cél a biztonságos szemlélet megszilárdítása, nem a „megbuktatás”. Az egyéni beszélgetés – online is – előre egyeztetett mentorbeszélgetés, vagyis a safer-working szabály egyik engedélyezett 1:1 kivétele (`Gyermekvédelem – release gate.md` §4.2): legfeljebb 30 percig tart, hivatalos csatornán vagy fizikailag átlátható térben zajlik, és egy másik felelős tud róla; nincs zárt privát szoba, személyes közösségimédia-fiók, eltűnő üzenet vagy felvétel. A naplóba csak dátum, résztvevők, időtartam, célkategória és utánkövetés kerül, a beszélgetés tartalma nem; ha gyermekvédelmi ügy lesz belőle, külön incidens-azonosítóra vált, és azonnal a Memunát kell bevonni. További próbálkozást ezután a képző nyithat kézzel. (Az **M3.F (F-peula)** a sikertelen kapu után, a javító próbálkozás előtt kötelező – lásd §0, Próbálkozások.)

---

## 4. Források (webkereséssel ellenőrizve, 2026-06)

**Nemzetközi safeguarding alapelvek** (ne ígérj teljes titoktartást; ne nyomozz, hallgasd meg a gyermek saját szavaival; felnőtt-gyanúnál ne konfrontáld a gyanúsítottat, közvetlenül a kijelölt gyermekvédelmi felelősnek – nálunk a Memunának, nemzetközi terminológiával: DSL, *Designated Safeguarding Lead* – jelezz):
- NSPCC Learning – *Recognising and responding to abuse* / *Safeguarding example scenarios* – https://learning.nspcc.org.uk/child-abuse-and-neglect/recognising-and-responding-to-abuse
- Safeguarding Network – *Dealing with a disclosure* – https://safeguarding.network/content/dealing-with-a-disclosure
- British Council – *Guidance on handling a disclosure from a child* (PDF) – https://www.britishcouncil.org/sites/default/files/handling_disclosure_from_a_child_0.pdf
- CSA Centre – *Key messages: identifying and responding to disclosures of child sexual abuse* (PDF) – https://www.csacentre.org.uk/app/uploads/2019/09/Key-messages-CSA-disclosures.pdf
- NCVO – *Recognise, respond and report* / *Managing concerns* (ne konfrontáld a gyanúsított felnőttet) – https://www.ncvo.org.uk/help-and-guidance/safeguarding/steps-safer-organisation/recognise-respond-and-report/

**Magyar jogi háttér:** a Gyvt. 17. § (1) a jelzőrendszeri szereplők között egyesületeket és alapítványokat is felsorol, a (2) bekezdés pedig jelzési, súlyos esetben kezdeményezési kötelezettséget ír elő. A Btk. 209/A. § **csak** a Gyvt. 17. § (4a)–(4c) szerinti, kiemelt veszélyeztető okhoz kapcsolódó kötelezettség megszegésére épül; nem szabad úgy tanítani, mintha minden red flag elmulasztott jelzése automatikusan ezt a tényállást valósítaná meg. A szervezet és az egyes szerepek konkrét jogi helyzetét szakértő zárja le. A madrich számára a viselkedési szabály marad: **észlelj, ne nyomozz, és azonnal vond be a kijelölt Memunát**; a lépéseket részletesen az ötlépéses jelzési út (M3.B lépéstérkép) mutatja.
- 1997. évi XXXI. törvény a gyermekek védelméről és a gyámügyi igazgatásról (Gyvt.) – Nemzeti Jogszabálytár – https://njt.hu/jogszabaly/1997-31-00-00
- Gyvt. – Hatályos Jogszabályok Gyűjteménye (net.jogtar.hu) – https://net.jogtar.hu/jogszabaly?docid=99700031.tv
- 2024.09.01-i módosítás / büntetőjogi felelősség (Btk. 209/A. §) – jelzőrendszeri összefoglaló – https://modszertan.maltai.hu/

**Akut önveszély / krízis – hívószámok** (112 segélyhívó; 116-111 Kék Vonal Lelkisegély-vonal gyerekeknek és fiataloknak, valamint gyerek érdekében telefonáló felnőtteknek; 116-123 Lelki Elsősegély felnőtteknek; **116-000 a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért**):
> **A számok szétválasztása (stáb/mentor):** a **116-111** a Kék Vonal Lelkisegély-vonala gyerekeknek és fiataloknak; **gyerek érdekében telefonáló, aggódó felnőtt** is hívhatja. A **116-000** a Kék Vonal Segélyvonala a Bántalmazott és Eltűnt Gyerekekért: eltűnt, szökésben lévő vagy szökést fontolgató, illetve bántalmazott gyerek ügyében hívható, felnőttek is hívhatják; nem általános „szülői vonal”. **Felnőtt saját lelki krízisében** a 116-123 Lelki Elsősegély érhető el. **Közvetlen életveszélynél 112.** A belső jelzést (a Memuna bevonását) egyik segélyvonal sem helyettesíti.
- A Rendőrség hivatalos honlapja – *Tájékoztató a Lelki Elsősegély Telefonszolgálatokról* – https://www.police.hu/hu/hirek-es-informaciok/bunmegelozes/aktualis/tajekoztato-a-lelki-elsosegely-telefonszolgalatokrol
- Magyar Lelki Elsősegély Telefonszolgálatok Szövetsége (LESZ) – 116-123 (ingyenes, 0–24, mindenkinek) – https://sos116-123.hu/
- Kék Vonal Gyermekkrízis Alapítvány – 116-111 (gyermek- és ifjúsági lelkisegély, ingyenes, 0–24, 24 év alatt) – https://kek-vonal.hu/
- Kék Vonal Gyermekkrízis Alapítvány – 116-111 Lelkisegély-vonal; 116-000 Segélyvonal az eltűnt és bántalmazott gyerekekért – https://interaktiv.kek-vonal.hu/index.php/hu/component/content/category/15-szakmai-szolgaltatasok
- Egészségvonal (NNGYK) – *Lelkisegély-szolgálatok és kríziskezelés* (112 közvetlen veszélynél) – https://egeszsegvonal.gov.hu/maradj-egeszseges/lelki-egeszseg/lelkisegely/lelkisegely-szolgalatok.html

> A hívószámok és a helyi gyermekvédelmi szabályok (Gyermekvédelmi működési standard v1.0) ellenőrzése az élesítés előtt a **Memuna** feladata (utólagos ellenőrzés: vétó/QA).
