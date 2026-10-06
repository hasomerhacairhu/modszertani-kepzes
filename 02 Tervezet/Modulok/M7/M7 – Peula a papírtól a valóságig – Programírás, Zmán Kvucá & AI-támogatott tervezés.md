# M7 – „Peula a papírtól a valóságig” – Programírás, Zmán Kvucá & AI-támogatott tervezés

<!-- @asset
{
  "id": "M7-HUB-DIA-02",
  "kind": "diagram",
  "mode": "generate",
  "title": "Kétlépcsős félévzáró idővonal: v1 első vázlat → köztes fejlesztés → v2 teljesítési kapu",
  "purpose": "Vizuálisan érthetővé teszi az időben elosztott, két menetben érő félévzáró logikát (v1 = próba, v2 = vállalható verzió), amit a szöveg kétszer is fontosnak tart kifejteni; csökkenti a „mikor mit adok le\" bizonytalanságot.",
  "spec": "Idővonal/folyamatábra a félévzáró feladat két lépcsőjéről, időben szétterítve: (1) v1 – elsővázlat-ellenőrzési pont az M7 1. hetének végén, az M7.A után (formatív, alacsony tét, NEM buktat, újrapróbálható, M7.4 Assignment; a kijelölt mentor a v2 előtt rubrikára épülő visszajelzést ad rá); (2) a kvíz (felkészültségi kapu) a v1 leadása után nyílik – ajánlott még az M7.B előtt teljesíteni –, és a megerősített eredménye a v2 leadásának feltétele; ~1 hét köztes fejlesztési idő, csiszolás az M7.B peula-műhelyben és otthon; (3) v2 – teljesítési kapu az M7 2. hetének végén, az M7.B után (éles kapu: v2-rubrika ÉS a v2 előtt teljesített kvíz). Jelölje a két határidő helyét a központi ütemezési kulcsokkal: `M7_V1_DUE` és `M7_V2_DUE`; a renderelt változatban ezek értékeit a HUM-OPS-01 szerinti központi schedule tölti ki.",
  "provenance": "ai",
  "provenance_note": "AI-generált",
  "technical": {
    "note": "Vektoros, vízszintes idővonal/sávos időrend, magyar feliratokkal; 16:9 kivetíthető és A4/A3 nyomtatható; két dátummezővel, amelyeket rendereléskor a HUM-OPS-01 központi ütemezésből kell kitölteni. Üres dátummezővel nem publikálható."
  },
  "a11y": {
    "visual": "informative",
    "alt_note": "a lecke előírja az alt-szöveget, de a végleges szöveget a legyártott vizuál alapján kell megírni",
    "note": "Alt-szöveg kötelező: M7-HUB-DIA-02::ALTTEXT (a három állomás sorrendje, tétje és időzítése szövegesen)."
  },
  "derivatives": [
    "alt-text"
  ],
  "production_rules": [
    "R1",
    "R5"
  ],
  "blockers": [],
  "notes": "Hub-szintű folyamatábra; a részletes értékelő (item-bank, rubrika) az „M7 – KAPU\" fájlban él, ide csak az idővonal logika kell.",
  "legacy": {
    "alt-text": [
      "M7-HUB-ALT-02"
    ],
    "asset": [
      "M7-HUB-DIA-02"
    ]
  }
}
-->

<!-- @asset
{
  "id": "M7-HUB-DIA-03",
  "kind": "diagram",
  "mode": "generate",
  "title": "Portfólió-átkötés / félévzáró összegzés: M1 SBI … M6 játéklap → 1 Peula v2",
  "purpose": "Vizuálisan üzeni, hogy a félévzáró feladat nem nulláról indul, hanem a portfólió korábbi produktumait köti egybe; megerősíti a §6 PORTFÓLIÓ-BEMENET végén álló „Üzenet a madrihnak” mondatot.",
  "spec": "Konvergencia-/tölcsérdiagram, amely megmutatja, hogy a hat korábbi modul kész produktuma hogyan táplálja az egyetlen Peula v2-t: M1 megfigyelés és konkrét visszajelzés (utóreflexió, javító visszajelzés), M2 saját érték / dugma isit (SMART cél kötése), M3 gyermekvédelem + kvuca-profil (Zmán Kvucá-biztonság), M4 kérdezéstechnika (élmény-/feldolgozó-blokk, visszatükrözés), M5 módszer-logika (cél↔módszer↔kvuca), M6 játéklap (élmény-blokk, biztonság/inkluzivitás). Hat bemenet → egy vállalható Peula v2.",
  "provenance": "ai",
  "provenance_note": "AI-generált",
  "technical": {
    "note": "Vektoros tölcsér/konvergencia-ábra, magyar feliratokkal; 16:9 kivetíthető és A4/A3 nyomtatható."
  },
  "a11y": {
    "visual": "informative",
    "alt_note": "a lecke előírja az alt-szöveget, de a végleges szöveget a legyártott vizuál alapján kell megírni",
    "note": "Alt-szöveg kötelező: M7-HUB-DIA-03::ALTTEXT (a hat bemenet és a Peula v2 célpont szöveges felsorolása)."
  },
  "derivatives": [
    "alt-text"
  ],
  "production_rules": [
    "R1",
    "R5"
  ],
  "blockers": [],
  "notes": "A részletes félévzáró szintézis-átkötés-tábla az „M7 – KAPU\" §PORTFÓLIÓ-ÁTKÖTÉS-ban él; ez a hub-ábra annak vizuális, ezen a fájlon belül is használt összefoglalója.",
  "legacy": {
    "alt-text": [
      "M7-HUB-ALT-03"
    ],
    "asset": [
      "M7-HUB-DIA-03"
    ]
  }
}
-->

<!-- @asset
{
  "id": "M7-HUB-MUNK-01",
  "kind": "worksheet",
  "mode": "generate",
  "title": "1 perces kilépőkártya-munkalap (M7.A/M7.B/M7.F utáni offline visszajelzés)",
  "purpose": "Gyors offline visszajelzés-gyűjtés a három peula után a learning analyticshez; méri a Peula v2-hez közeledést és feltárja a maradék bizonytalanságokat (Zmán Kvucá / AI).",
  "spec": "Egylapos, 1 perc alatt kitölthető kilépőkártya-sablon két kérdéssel: (1) 1–5 skála „Mennyire érzed, hogy most közelebb kerültél egy valódi Peula v2-höz?\"; (2) nyitott kérdés „Mi az, ami még bizonytalan benned a Zmán Kvucával / AI-használattal kapcsolatban?\". Helyhagyás a peula azonosítására (M7.A / M7.B / M7.F). Készüljön egy QR-kódos digitális kitöltési variáns is (§7, Offline visszajelzések); ennek elején a Program terv §7 adatvédelmi tájékoztató sablonja áll, és a válaszokhoz csak a legszűkebb szükséges hozzáférés adható (HUM-PRIV-01).",
  "provenance": "mixed",
  "provenance_note": "vegyes",
  "technical": {
    "note": "A6/A5 nyomtatható lap, magyar nyelvű; opcionális QR-kódos online űrlap-variáns ugyanazzal a két kérdéssel."
  },
  "a11y": {
    "note": "Olvasható, nagy kontrasztú nyomtatás; a QR-kód mellett szöveges URL feltüntetése azoknak, akik nem tudják beolvasni."
  },
  "derivatives": [
    "print-pdf"
  ],
  "production_rules": [
    "R1",
    "R5"
  ],
  "blockers": [],
  "notes": "Modul-szintű mérőeszköz; mindhárom offline alkalom (M7.A, M7.B, M7.F) után használható.",
  "legacy": {
    "asset": [
      "M7-MUNK-01"
    ]
  }
}
-->

## 1. Modul meta

* **Időtartam:** 2 hét
* **Heti offline:** péntek 2. sáv – Peula A (1. hét) és Peula B (2. hét; a dátumokat a központi naptár adja), **45’ + 45’**
* **Online terhelés:** kb. **4 db mikrolecke** H5P-magja: az M7.1, az M7.3 és az M7.4 egyenként **15–20’**, az M7.2 **30–35’**, mert az elején kb. 15 perces **AI-jártassági blokk** van (össz. ~**75–95’**; V1 tervezési értékek: a későbbi pilot finomíthatja őket, de nem élesítési feltétel); ehhez jön **M7.3 Moodle Checklist (5–10’)** és **M7.4 Moodle Assignment-kitöltés (5–10’)** külön lépésként → online összterhelés **~85–115 perc**.
* **Félévzáró szintézis-produktum (önálló írásmunka – külön, reális becslés):** a **véglegesített Peula v2 + Zmán Kvucá** NEM fér bele a fenti percekbe – ez a félév **szintézis-produktuma**, ezért külön tervezett munkaidőt igényel. **Reális becslés (madrih-óra, otthoni / védett munkaidő):**
  * **Peula v1 első vázlat** (M7.4 Assignment): **~30–45 perc** (kvuca-meta + SMART cél + 3–4 pont + operációs mini-tábla).
  * **Felkészültségi kvíz a v1 leadása után** (ajánlott még az M7.B előtt, a v2 leadása előtt kötelező; 14 item, esetleg egy javító próbálkozással): **~15–25 perc**.
  * **v1 → v2 véglegesítés** (a kijelölt mentor rubrikára épülő v1-visszajelzése és az M7.B peula-műhely után, önállóan): **~60–90 perc** – SMART-cél csiszolása, 3–4 Peula-pont kidolgozása, **biztonsági rész** (R4 blokkoló), **inkluzivitás** (R5), Zmán Kvucá-operációs tábla pufferrel, az AI-javaslatok kritikus átdolgozása (ha használt AI-t), és a **portfólió-átkötések tényleges behozása** (M1 SBI · M2 érték · M3 biztonsági keret/kvuca-profil · M4 kérdezéstechnika · M5 módszer · M6 játéklap).
  * → **A szintézis-produktum önálló írás-/véglegesítő terhelése reálisan kb. 105–160 perc (kb. 1,75–2,7 óra; a fenti három tétel összege)**, az online leckéken és a peulákon **felül**. Ezt **előre kommunikáld** a madrihoknak (a ténylegesnél kisebbnek ígért, majd nagyobbnak bizonyuló terhelés lemorzsolódási kockázat), és adj hozzá **védett munkaidőt** (pl. az M7.B-műhely). Ha a kapu nem teljesül, a kötelező M7.F **felzárkóztató peula (F-peula)** ad facilitált, strukturált javítási alkalmat a javító próbálkozás előtt – nem általános pótlásra szolgál.
* **Teljes terhelés (V1 tervezési érték): 4–5,5 óra** a félévzáró kapuig – kontaktidő kb. **175–205 perc (2,9–3,4 óra; online mikroleckék ~85–115 perc + 2 × 45’ peula)** + kb. **105–160 perc önálló szintézis-produktum-munka: Peula v1, kvíz, Peula v2 véglegesítés** (a részidők összege ~280–365 perc, kb. 4,7–6,1 óra; a V1 tervezési érték a projektgazdai döntés szerint 4–5,5 óra).

**Modulközponti kérdés**

> „Hogyan lesz egy someres ötletből olyan **Peula és Zmán Kvucá**, ami biztonságos, korosztály-illeszkedő – és ahol a **szervezetileg jóváhagyott generatív AI-eszköz** csak segít, nem helyettesít?”

**Kulcsfogalmak (első említés)**

* **SMART nevelési cél:** olyan cél, ami **Specifikus, Mérhető, Achievable (elérhető), Releváns és Time-bound (időhöz kötött)** – someres nyelven: pontosan megfogalmazott, látszik, hogy megtörtént-e, reális, Somer-értékhez kapcsolódik, és tudjuk, *mikorra* szeretnénk, hogy megvalósuljon. (M7.1, M7.A, M7.4)
* **Peula 11 pontja (modernizált):** a peula „csontváza” a céltól a feldolgozáson át a biztonságig; ahol a résztvevő választja és a szervezeti feltételek engedik, AI opcionális támogató eszköz lehet. (M7.2, M7.A, M7.4)
* **Zmán Kvucá:** a kvuca **fix, rendszeres foglalkozás-idősávja** (pl. heti kvuca-idő a kenben), ahol peula, beszélgetés, játék történik – **nevelési céllal**, tervezetten, biztonságos keretben. (M7.3, M7.B, M7.F)
* **AI mint opcionális eszköz:** ötletelésre, fogalmazásra, kérdésgenerálásra használható **hanih-adatok nélkül**; a használata nem teljesítési feltétel, és a döntés/felelősség minden esetben a madrihnál marad. Saját AI-fiókra nincs szükség: a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj. (M7.1–M7.4, M7.B)

**Modulcél röviden**

A madrih a modul végére rendelkezik **1 db Peula v2-vel** egy konkrét kvucára (pl. Parparim/Kivsza), amelyet a **modernizált Peula 11 pont** szerint írt meg; érti és használja a **Zmán Kvucá-checklistet**, és képes megítélni, hogyan vonható be **opcionálisan, etikusan egy szervezetileg jóváhagyott generatív AI-eszköz** a tervezésbe. A no-AI út teljes értékű; a döntések minden esetben a madrih kezében maradnak. (M7.1–M7.4, M7.A, M7.B)

**Kétlépcsős félévzáró – a Peula v2 nem egy ülésben készül el**

> **Üzenet a madrihnak:** a félévzáró feladat **két lépcsőben** érik be – szándékosan **időben szétterítve**, hogy a peuládat ne egy lélegzetre, hanem két menetben csiszold:
>
> * **v1 – elsővázlat-ellenőrzési pont (az M7 1. hetének vége, az M7.A után):** leadod a **Peula v1 első vázlatot** (M7.4 Assignment). Ez **alacsony tét**: NEM buktat, **újrapróbálható**, és a v2 előtt a **kijelölt mentorod** a v2-rubrika alapján visszajelzést ad rá – a célja, hogy lásd, hova tartasz, és hol kérsz segítséget. (A pontos dátumot a Moodle-ben látod.)
> * **kvíz – felkészültségi kapu (a v1 után, a v2 előtt):** a „SMART & Zmán Kvucá kvíz (felkészültségi)” a v1 leadása után nyílik. Érdemes még az M7.B előtt kitöltened: így már a v2 csiszolása előtt kiderül, megvan-e a tudásalap (a gyermekvédelmi lépésekkel együtt). A v2-t csak a sikeres kvíz után adhatod le.
> * **~1 hét köztes fejlesztési idő:** a v1 visszajelzései után, **az M7.B peula-műhelyben és otthon** csiszolod a vázlatot – nem aznap, hanem a két hét közti időben érik be a gondolat.
> * **v2 – teljesítési kapu (az M7 2. hetének vége, az M7.B után):** leadod a **véglegesített Peula v2 + Zmán Kvucá-operációt** – ez a tényleges, éles teljesítési kapu (rubrika + kvíz, lásd „M7 – KAPU”). (A pontos dátumot a Moodle-ben látod.)
>
> A v1 és a v2 **ugyanaz a peula**, két érettségi fokon: a v1 a próba, a v2 a vállalható, megtartható verzió. A portfólió-átkötés (M1 SBI … M6 játéklap → v2) ezt táplálja – részletesen a §6 PORTFÓLIÓ-BEMENET és az „M7 – KAPU” §PORTFÓLIÓ-ÁTKÖTÉS.

***

## 2. Kimeneti kompetenciák

A modul végére a madrih…

1. **SMART nevelési cél írása (someres kontextusban)**
   * 2–3 „szétfolyó” célt át tud írni **SMART nevelési céllá** egy adott kvucára (M7.1, M7.A).
   * Érti, hogyan kapcsolódik a cél Somer-értékhez / kvuca-állapothoz (M7.1, M7.4).
2. **„Peula 11 pontja” – modern, AI-támogatott verzió**
   * **Azonosítja a Peula 11 pontjának fázisait egy adott peulavázban** (1. Téma & modul, 2. Háttér & altémák, 3. Kvuca + idő + helyszín, 4. Nevelési cél/SMART, 5. Módszerek & élmény-blokk, 6. Felépítés, 7. Realitás-check, 8. Kelléklista, 9. Biztonság & gyermekvédelem, 10. Visszajelzés és finomhangolás, 11. Utóreflexió & továbbfejlesztés) (M7.2).
   * Képes ezek mentén **Peula v2-t írni**, és ha az AI utat választja, AI-t használni ötleteléshez vagy nyelvi finomításhoz anélkül, hogy átadná neki a szerzői/szakmai döntést (M7.2, M7.4, M7.A).
3. **Zmán Kvucá & operáció**
   * Érti, mit jelent a **Zmán Kvucá** mint időkeret, felelősség és gyermekvédelmi kontextus (M7.3).
   * Tud használni egy **Zmán Kvucá-checklistet** (helyszín, létszám, anyagok, B-terv, hozzáférhetőség, gyermekvédelem, szerepek) saját peulájára (M7.3, M7.4, M7.B).
4. **AI-etikusság & adatbiztonság**
   * Tudja, hogy a hanih neve, képe, elérhetősége, pontos helye, egészségügyi/mentális állapota, családi háttere, vallási/etnikai vagy más érzékeny identitása és beazonosítható eseménye **nem kerülhet promptba** (a lista forrása: `Adatvédelem – tanulói adatok és AI.md` §7), és gyermekvédelmi ügyben mindig a kijelölt Memuna (a Somer gyermekvédelmi felelőse) a kontakt (M7.2–M7.4).
   * Különbséget tesz „AI segít ötletelni / fogalmazni” és „AI megírja helyettem az egész peulát” között; az utóbbit nem használja (M7.2, M7.4, M7.B).
5. **Peula v2 + Zmán Kvucá produktum**
   * Elkészíti és leadja a modul produktumát:
     * 1 db **Peula v2** (Peula sablon + 11 pont),
     * 1 db **Zmán Kvucá-checklist** ugyanarra a programra. (M7.4, M7.B, modulkapu)

***

## 3. Online mikroleckék (L1–L4)

### M7.1 – „Ez még csak vágy, nem cél” – SMART nevelési cél someres módra (15–20’)

* **Cél:**
  Megkülönböztetni a „szétfolyó” kívánságszintű célokat a **SMART nevelési céltól**, és 1 saját peula-ötlethez SMART célt írni.
* **Programírás-fókusz:**
  „Ha nem tudom pontosan, mit szeretnék, nem tudom jól megtervezni a peulát sem.”
* **Eszközök:** H5P **Course Presentation** (**7 slide**) + beépített **Single Choice Set** + **Fill in the Blanks**; a záró SLIDE 7 saját SMART céljának mezői a lecke melletti Moodle-oldali szövegmezőben (`LMS – activity manifest.md`, LMS-M7-10).
* **Tartalom röviden:**
  * „Szétfolyó vágyak” vs. mérhető célok (kvuca-szituációkra írva).
  * SMART definíció **madrih-nyelven** + 2 someres minta (pl. szolidaritás / biztonság).
  * Gyakorló feladat: hiányzó SMART-elemek beírása 2 célmondatba.
  * Mini AI-blokk: hogyan kérsz segítséget AI-tól egy meglévő cél átírásához – **hanih-adat nélkül**.
  * Zárás: 1 saját peula-ötlethez SMART cél megírása (alap egy későbbi Peula v2-hez).

***

### M7.2 – „Nemcsak játék, hanem peula” – 11 tervezési pont & AI-támogatás (30–35’)

* **Cél:**
  Megismerni a modernizált **Peula 11 pontját**, és látni egy-egy AI-használati példát (ötletelés, kérdésgenerálás, nyelvi egyszerűsítés).
* **Programírás-fókusz:**
  „Nem elég a játék – a peulának *szerkezete* és *biztonsági kerete* van.”
* **Eszközök:** **Moodle-oldal** az AI-jártassági blokkhoz (beágyazott H5P Multiple Choice ellenőrző kérdéssel) + H5P **Course Presentation** (**7 slide**) + **húzásmentes párosító feladat** (a megvalósítási típust a runtime acceptance rögzíti).
* **Tartalom röviden:**
  * **AI-jártassági blokk a lecke elején (kb. 15’):** mi az AI, mire jó és mire nem; hallucináció; adatvédelem; emberi ellenőrzés; a promptba nem írható adatok (`Adatvédelem – tanulói adatok és AI.md` §7). Saját AI-fiókra nincs szükség; az AI továbbra is opcionális, a no-AI út teljes értékű.
  * A 11 pont nevei és someres példái (pl. Kvuca + idő + helyszín, Módszerek & élmény-blokk, Felépítés, Realitás-check, Biztonság & gyermekvédelem).
  * Minden ponthoz 1 rövid magyarázat; fázisonként 1 ajánlott **AI-prompt**-példa. Gyermekvédelmi döntést, red flag minősítést vagy kríziskezelést **nem delegálunk AI-nak**: ilyen ügyben azonnal a Memunát kell bevonni (M7.2, kötelező AI-keret).
  * Párosító feladat (koppintással / kattintással, húzás nélkül): pont → leírás.
  * Önellenőrzés (SLIDE 7): egy hiányos példa-peulavázról kérdés arról, melyik pont hiányzik belőle, és 1 mondatos mini-reflexió.

***

### M7.3 – „Zmán Kvucá-checklist” – idő, tér, felelősség (15–20’)

* **Cél:**
  Érteni, mitől lesz egy Zmán Kvucá **vállalható és biztonságos**, és használni a hozzá tartozó **checklistet** saját programokra.
* **Programírás-fókusz:**
  „A Zmán Kvucá nemcsak egy játékidő – hanem *idő + helyszín + kvuca + cél + felelősség* tudatos kerete.” A madrih a saját szerepében figyel és jelez, a gyermekvédelmi felelősség pedig a jelen lévő, 18 év feletti felnőtté.
* **Eszközök:** H5P **Course Presentation** (kb. 6 slide) + **Moodle Checklist** külön aktivitásként.
* **Tartalom röviden:**
  * Mini-sztori(k) széteső Zmán Kvucáról (nincs B-terv, kevés madrih, bizonytalan terek).
  * A Zmán Kvucá 5 fő területe:
    * Idő & helyszín,
    * Létszám & madrih–hanih arány,
    * Anyagok, technika & B-terv,
    * Hozzáférhetőség & inkluzivitás,
    * Gyermekvédelem & határok.
  * Checklist egy **mintaprogramra** (pl. „Péntek esti Zmán Kvucá a kenben”): mi oké / mi kérdéses.
  * Zárás: 1 közelgő saját Zmán Kvucára jelöli, melyik 2 checklist-pont az, amire extra figyelnie kell.

***

### M7.4 – „Peula v1 + AI” – első modulproduktum-vázlat (15–20’)

* **Cél:**
  Előkészíteni a modul produktumát: 1 **Peula v1 vázlatot** és a hozzá tartozó **Zmán Kvucá-operáció** alapjait.
* **Programírás-fókusz:**
  „A végén legyen egy peula, amit **tényleg meg tudnál tartani** – nem csak papíron néz ki jól.”
* **Eszközök:** H5P **Course Presentation** + Moodle **Assignment** („Peula v1 – első vázlat” – formatív, még nem kapu).
* **Tartalom röviden:**
  * Felidézés: 3 építőkocka összekapcsolása (SMART cél – Peula 11 pontja – Zmán Kvucá-checklist).
  * Vezetett kérdések a saját Peula v1-hez:
    * kvuca-típus, korosztály, kvuca-meta,
    * SMART nevelési cél,
    * 3–4 fókuszpont a Peula 11 pontja közül (pl. Módszerek & élmény-blokk, Felépítés, Biztonság & gyermekvédelem).
  * Mini AI-blokk: hogyan kérj AI-tól ötleteket feldolgozó kérdésekre úgy, hogy nem viszel be hanih-adatokat, és **te döntöd el**, mi illik a kvucádhoz.
  * Moodle Assignment: „Peula v1 – első vázlat” beadása minimum elvárásokkal (kitöltött meta, 3–4 peula-pont részletezve, mini Zmán Kvucá-táblázat).

***

## 4. Offline peulák

### Peula A (M7.A) – „Célból peula” – SMART & 11 pont élőben (45’)

* **Kapcsolódás:** elsősorban **M7.1–M7.2** élményesítése (SMART cél + Peula 11 pontja).
* **Fő cél:**
  * A résztvevő jobban látja, mitől „szétfolyó” egy cél, és mitől SMART egy konkrét kvucára.
  * 1 saját peula-ötletből **félkész vázlatot** formál (SMART cél + néhány kijelölt peula-pont).
* **Fókusz-mondat:**
  „Ha jól megfogalmazom a célt, a peula fele már kész.”
* **Rövid váz:**
  * Ráhangolódás: „Mitől jó egy Zmán Kvucá hanih-szemmel?”
  * Játék: vágy kontra SMART cél – sarokválasztás, rövid megbeszélés.
  * Mini-műhely: 1 ötlet → SMART cél + 3–4 kijelölt peula-pont (a Peula 11 pontjából).
  * Megosztás és társas visszajelzés: kvuca-meta, SMART cél, 2 kidolgozott pont rövid bemutatása.
  * Zárókör: „Peula-tervezésnél legközelebb mire fogsz leginkább figyelni?”

***

### Peula B (M7.B) – „Peula v2 & Zmán Kvucá – amikor a papír találkozik a valósággal” (45’)

* **Kapcsolódás:** elsősorban **M7.3–M7.4** alkalmazása (Zmán Kvucá-checklist + Peula v1-váz).
* **Hol áll a kétlépcsős ívben:** ez a **2. hét** peulája – a **v1 elsővázlat-ellenőrzési pont** (1. hét vége) és a **v2 teljesítési kapu** (2. hét vége) **közti** csiszoló alkalom. A műhelyben a résztvevők **a már leadott Peula v1-et** fejlesztik tovább; a véglegesített v2-t **nem itt, aznap** adják le, hanem a műhely utáni munkával, a 2. hét végén.
* **Fő cél:**
  * 1 már leadott **Peula v1 vázlat** továbbfejlesztése a **v2 felé** Zmán Kvucá-szempontból (idő, tér, létszám, eszköz/B-terv, inkluzivitás, gyermekvédelem).
  * Átélni, hogy nem az a jó peula, ami papíron a legkreatívabb, hanem amit a madrih **biztonságban meg is tud tartani** a saját kvucájának.
* **Fókusz-mondat:**
  „Nem az a jó peula, ami papíron nagyon kreatív, hanem amit **biztonságban meg is tudsz tartani**.”
* **Rövid váz:**
  * Gyors felidézés / élő kvíz: Zmán Kvucá & AI-határok.
  * Peula-műhely kiscsoportban:
    * 1 kiválasztott Peula v1-re végigpörgetik a checklistet,
    * beírják a hiányzó biztonsági / operatív elemeket,
    * opcionálisan kipróbálnak 1–2 AI-promptot (pl. alternatív helyszín-ötlet, B-terv, feldolgozó kérdések; saját AI-fiók nem kell: a kurzus AI-segédjét a Somer szervere közvetíti, vagy a képző küldi el a promptot); aki nem használ AI-t, ugyanazt saját ötleteléssel, mentorral vagy nyomtatott promptkártyával végzi.
  * Galériaséta: „előtte–utána” – a checklist hatása a kész vázlatokon (mi lett biztonságosabb, valóságközelibb).
  * Zárókör: „A következő Zmán Kvucá tervezésénél mire fogsz külön figyelni?”

***

## 5. Felzárkóztató peula (M7.F) – „Peula & Zmán Kvucá” (45’)

<!-- @asset
{
  "id": "M7-HUB-DIA-01",
  "kind": "diagram",
  "mode": "generate",
  "title": "Modul-fogalomtérkép: SMART – Peula 11 pont – Zmán Kvucá – Peula v2",
  "purpose": "Az M7.F F-peula résztvevőinek egységes mentális térkép a modul négy fő fogalmáról; vizuálisan rögzíti a cél→tervezés→operáció→produktum ívet, amelyre a javító próbálkozás épülhet (§5, Fő cél).",
  "spec": "A modul négy kulcsfogalmát összekötő fogalomtérkép: SMART nevelési cél → Peula 11 pontja → Zmán Kvucá-checklist → Peula v2 logikai egymásra épülése, irányított nyilakkal (cél táplálja a tervezést, a tervezés az operációt, ezekből áll össze a Peula v2). A legyártandó verzió egy KIINDULÓ/alap-térkép, amelyet az M7.F F-peulán élőben, közös beszélgetéssel egészítenek ki (§5, Rövid váz), ezért hagyjon helyet a kézi kiegészítésnek.",
  "provenance": "ai",
  "provenance_note": "AI-generált",
  "technical": {
    "note": "Vektoros diagram, magyar feliratokkal; nyomtatható A3/flipchart-méretben és kivetíthető 16:9 arányban; üres kiegészítő-mezőkkel a közös munkához."
  },
  "a11y": {
    "visual": "informative",
    "alt_note": "a lecke előírja az alt-szöveget, de a végleges szöveget a legyártott vizuál alapján kell megírni",
    "note": "Alt-szöveg kötelező: M7-HUB-DIA-01::ALTTEXT (négy csomópont + irányított kapcsolatok szöveges leírása)."
  },
  "derivatives": [
    "alt-text"
  ],
  "production_rules": [
    "R1",
    "R5"
  ],
  "blockers": [],
  "notes": "Modul- (hub-) szintű asset. A lecke-szintű H5P-vizuálok (Course Presentation slide-ok, párosító feladat) az M7.1–M7.4 fájlokban élnek, nem itt.",
  "legacy": {
    "alt-text": [
      "M7-HUB-ALT-01"
    ],
    "asset": [
      "M7-HUB-DIA-01"
    ]
  }
}
-->

* **Kapcsolódás:** **F-peula** – facilitált, strukturált javítási alkalom azoknak, akiknek az M7 kapuja nem teljesült (meghatározása: Program terv, Glosszárium): a kapun kapott visszajelzésre (Megfigyelés → Hatás → Következő lépés) építve a nem teljesült kapuelemek javítását készíti elő, és ehhez rögzíti az **M7.1–M7.4** blokk fogalmait; **kötelező, ha az M7 éles kapuja nem teljesült**. Időpontja a kapueredmény megerősítése után, a javító próbálkozás előtt van; a képző jelöli ki a központi naptár szerint: a Z utáni hét hétfőjén, 18:00-tól. A javító próbálkozás az F-peula után nyílik meg (a képző nyitja meg, vagy az F-peula jelenléti completionje a feltétele). Aki csak lemaradt a leckékkel, csendes pótlással pótol.
* **Fő cél:**
  * Segíteni azoknak, akiknek az M7 kapuja nem teljesült, hogy a kapun kapott visszajelzés alapján **előkészítsék a nem teljesült kapuelemek javítását** (a kvíz, a Peula v2 + Zmán Kvucá vagy mindkettő), és ehhez **értsék a fő fogalmakat** (SMART, Peula 11 pont, Zmán Kvucá-checklist, Peula v2 + AI),
  * valódi, védett időt adni a javító próbálkozás előkészítésére és a hiányzó leckék pótlására,
  * egy egyszerű **fogalomtérképet** adni a modulhoz, amelyre a javító próbálkozás épülhet.
* **Hangnem:** támogató, nem büntető – F-peula, nem pótvizsga.
* **Rövid váz:**
  * Ráhangolódás: **privát** önellenőrzés – mindenki magának nézi meg a Moodle-ben a kapun kapott visszajelzést és azt, hol tart az M7.1–M7.4 leckékkel, és kiválasztja, melyik nem teljesült kapuelemmel foglalkozik. **Név szerinti haladási státusz nem kerül közös táblára**; ha a képzőnek kell a kép, azt a Moodle-ben vagy a saját, nem nyilvános mentorjegyzetében nézi meg (ebben csak minimális, a fejlődéstámogatáshoz szükséges adat lehet, „árnyékdosszié” nélkül; megőrzése: `Adatvédelem – tanulói adatok és AI.md` §3, „Mentori 1:1 meta-napló” sor). A közös falra legfeljebb **név nélküli témakérés** kerül („miben kérsz ma segítséget?”).
  * Csendes online munka fülessel: mindenki a saját tempójában újranézi azt az 1–2 leckét, amelyhez a visszajelzésben jelzett hiány kapcsolódik; aki leckét hagyott ki, itt pótolja a javító próbálkozás előtt.
  * Fogalomtérkép: SMART – Peula 11 pont – Zmán Kvucá – Peula v2 összekötése közös beszélgetéssel, a név nélkül összegyűjtött kérdésekre és a visszajelzésekben jelzett hiányokra fókuszálva.
  * Zárás – híd a javító próbálkozás felé: 1 mondat arról, mire figyel majd leginkább a javító próbálkozásban (a kvízben, a Peula v2-ben vagy mindkettőben), plusz saját mini javítási terv (melyik visszajelzési pontot veszi elő, melyik leckét nézi újra).

***

## 6. Kapuk

* **Kaputípus:**
  **Éles teljesítési kapu**, mert peula- és gyermekbiztonság-fókuszú modulról van szó – itt nem elég a „kb. értem”.

> **Hol történik a tényleges Peula v2 teljesítési leadása? (kétlépcsős, időben szétterítve)**
> A félévzáró feladat **két lépcsőben** érik be:
> – **v1 – elsővázlat-ellenőrzési pont (1. hét vége, M7.A után):** az M7.4 Assignment („Peula v1 – első vázlat”) **fejlesztő** (0/1 completion; üres sablon nem completion), **alacsony tét, újrapróbálható, NEM buktat**; a **kijelölt mentor** a v2 előtt rubrikára épülő, Megfigyelés → Hatás → Következő lépés szerkezetű visszajelzést ad rá – ez a kapu **bemenete**, a **váz** (Peula v1), NEM maga a kapu. (Határidő: `M7_V1_DUE` = az M7.B előtti szerda 18:00, a mentori visszajelzés az M7.B előtti csütörtök 18:00-ig – a V1 központi naptárból levezetett pontok, nem külön megadott dátumok; a Moodle-ben előre beállítva és előre közölve.)
> – **kvíz – felkészültségi kapu (a v1 leadása után nyílik; ajánlott még az M7.B előtt teljesíteni, a v2 leadása előtt kötelező):** a „SMART & Zmán Kvucá kvíz (felkészültségi)” (lásd lent, 2. pont) a v1 leadása után nyílik, és a megerősített eredménye a v2 leadásának feltétele (`LMS – activity manifest.md` LMS-M7-07); a kapu ettől még kétrészes marad: a kvíz ÉS a v2-rubrika.
> – **~1 hét köztes fejlesztési idő:** a v1 visszajelzései után a finomítás az **M7.B peula-műhelyben és otthon** történik, nem aznapi v1→v2, hanem külön fejlesztési szakaszban.
> – **v2 – teljesítési kapu (2. hét vége, M7.B után):** a **véglegesített Peula v2 + Zmán Kvucá** leadása az **éles kapu**. (Határidő: `M7_V2_DUE` = szerda 18:00 a V1 központi naptár szerint, a kapueredmény megerősítése legkésőbb csütörtök 18:00; a Moodle-ben előre beállítva és előre közölve.)
> A részletes értékelőt (item-bank, 8 soros rubrika, blokkoló biztonsági sor, ponthoz kötött ≥70%) az **[M7 – KAPU – értékelő (item-bank + rubrika)](./M7%20–%20Kapu%20–%20értékelő%20%28item-bank%20+%20rubrika%29.md)** fájl tartalmazza.
> **Horgonyzás:** a végleges Peula v2-t a **félév végén, mentor / képző** zárja le ezen az éles kapun – ez NEM csúszik a modulon kívülre, és a Z modul completion-alapú reflexiója **nem helyettesíti** ezt a teljesítési értékelést.

1. **Moodle Assignment – „Peula v2 + Zmán Kvucá” (modulproduktum)**
   * **Beadás:**
     * kitöltött **Peula v2 sablon** a modernizált Peula 11 pontja alapján,
     * kitöltött **Zmán Kvucá-checklist** ugyanarra a programra.
   * **Valós vagy kitalált kvuca:** a Peula v2 tervezhető valós kvucára, de csak nem azonosító, csoportszintű információval: nevek, egyéni érzékeny történetek, diagnózisok és hasonlók nem kerülhetnek bele. Akinek nincs saját kvucája, kitalált profilt kap.

   > **PORTFÓLIÓ-BEMENET – a Peula v2 nem nulláról indul.**
   > A félév szintézis-produktuma a korábbi modulok kész produktumaira épít (tükrözve az „M7 – KAPU” portfólió-átkötési tábláját):
   >
   > * **M1 – megfigyelés, értelmezés, konkrét fejlesztő visszajelzés:** az M7.A/M7.B műhelyben a társas visszajelzés konkrétumokra épül, nem címkékre. A 11. pontban ugyanez a fegyelem tér vissza: a megtartás után a madrih előbb azt rögzíti, mi történt és mit figyelt meg, csak utána értelmezi a hatást, és dönt a változtatásról.
   > * **M2 – identitás / érték** (identitás-jegyzet, dugma isit – személyes példamutatás): a SMART nevelési cél / kvuca-illeszkedés a madrih saját someres értékéhez, dugma isitjéhez kötődik – nem „bárki” peulája, hanem az övé.
   > * **M3 – gyermekvédelem + kvuca-profil** (Parparim/Kivsza/Leviatán + jelzési lánc): a Zmán Kvucá biztonsági része és a kvuca-illeszkedés a korábban tanult gyermekvédelmi keretre és a someres kvuca-profilra támaszkodik.
   > * **M4 – kérdezés & kapcsolódás** (aktív hallgatás, nyitott/tisztázó kérdés, rövid peulabemutató): a Peula 11 pontjának **élmény- és feldolgozó-blokkja** (5–6. pont) és a **Visszajelzés és finomhangolás** (10. pont) és az élő levezetés erre épül – a feldolgozó kérdések és a visszatükrözés az M4-ben tanult kérdezéstechnikából jönnek.
   > * **M5 – módszer-logika** (feladat–cél–kvuca–módszer + tanulástan): a cél ↔ módszer ↔ kvuca tudatos illesztését a Peula v2 indokolja meg.
   > * **M6 – játéklap** (cél, kvuca, leírás, biztonság, inkluzivitás, variációk): a peula konkrét élmény-blokkja egy kész M6-játéklapból emelhető be; a biztonsági és inkluzivitási mezők itt élnek tovább.
   >
   > Üzenet a madrihnak: „Hozd be az M1-ből a konkrét megfigyelésre épülő visszajelzési szemléletet, az M2-ből a saját értékedet, az M3-ból a biztonsági keretet, az M4-ből a kérdezéstechnikádat (feldolgozó kérdések, visszatükrözés), az M5-ből a módszer-logikádat és az M6-ból egy játéklapot – itt **egy** vállalható peulává kötöd össze őket.” (Részletes átkötés-tábla: „M7 – KAPU” §PORTFÓLIÓ-ÁTKÖTÉS.)

   * **Rubrika-minimum (példa):**
     1. SMART cél – egyértelmű, someres értékhez kötött.
     2. Kvuca-illeszkedés – korosztály, energiaszint, **életkori / korosztályi sajátosságok**.
     3. Struktúra – a Peula 11 pontja felismerhetően jelen van.
     4. Biztonság & gyermekvédelem – átgondolt biztonsági rész a Zmán Kvucá-checklist alapján.
     5. AI-használat – emberi, érthető szöveg; nincs „robotnyelv”, nincsenek beazonosítható hanih-sztorik.
   * **Követelmény:**
     * **„Teljesítve” = (összpont ≥70% = ≥17/24) ÉS (R1, R5, R6 mindegyike ≥2 = „Megfelelő”) ÉS (R4 – Gyermekvédelem & biztonság ≥2, blokkoló)** – zárt **ÉS**-logika; a kritikus sorok ≥2 minimuma a ponthatártól **függetlenül mindig kötelező**, a blokkoló biztonsági sor (R4) pedig, ha 2 pont alatt marad, a %-tól függetlenül buktat (a pontos szabály: „M7 – KAPU” §B).
2. **Moodle Quiz – „SMART & Zmán Kvucá kvíz (felkészültségi)”** **(kötelező 2. rész a kétrészes teljesítési kapuban – ≥80%; fogalmi belépő, vagyis felkészültségi kapu: a v1 leadása után nyílik, ajánlott még az M7.B előtt teljesíteni, a Peula v2 leadása előtt kötelező; a teljesítése is feltétel, mindkét részt teljesíteni kell)**
   * **14 item**: definíciók, szituációk, checklist-elemek felismerése (M7.1–M7.4 tartalma) **+ gyermekvédelem: az ötlépéses jelzési út és az 1:1 helyzetek szabálya (Q13–Q14, az M3.3, az M3.B és az M7.3 alapján – a blokkoló R4-sor tudásalapja)** (a részletes item-bank: „M7 – KAPU” §A).
   * **Követelmény:** **≥80% (14 itemből ≥12 jó)** **és a gyermekvédelmi Q13 helyes** (a blokkoló konstruktum külön kötelező), **1 normál + 1 javító próbálkozás** (a javító a kötelező F-peula után nyílik: a képző nyitja meg felhasználói felülbírálással, vagy az F-peula jelenléti completionje a feltétele; további próbálkozást a képző nyit; a legjobb megerősített eredmény számít), kérdés- és válasz-randomizálással.

* **Javítás / támogatás:**
  * ha valaki nem éri el a küszöböt:
    * rövid, konkrét **fejlesztő visszajelzés** Megfigyelés → Hatás → Következő lépés szerkezetben (legfeljebb három konkrét javaslatban),
    * **kötelező felzárkóztató peula (F-peula)** mentorral / képzővel (egyéni támogatás; kettesben csak a safer-working szabály szerint: indokolt esetben, átlátható módon, egy másik felelős tudtával – online is) a kapueredmény megerősítése után, a javító próbálkozás előtt; az időpontot a képző jelöli ki a központi naptár szerint: a Z utáni hét hétfőjén, 18:00-tól,
    * utána lehetőség javított Peula v2 leadására (egy javító leadás jár, amely az F-peula után nyílik meg: a képző nyitja meg, vagy az F-peula jelenléti completionje a feltétele; továbbit a képző nyit).

***

## 7. Tanulási analitika a modul szintjén – mit nézzen a stáb az M7-nél?

**Activity completion (online)**

* M7.1–M7.4 completion arány, külön figyelve:
  * **M7.1 – SMART cél:** ha sok a hibás válasz / félbehagyott lecke → a célfogalmazást érdemes erősíteni.
  * **M7.2 – Peula 11 pontja:** ha sokan félbehagyják → lehet, hogy túl hosszú / túl bonyolult; érdemes rövidítő verziót vagy extra magyarázatot betenni.
  * **M7.3 – Zmán Kvucá-checklist:** ahol sok kérdést írnak, ott érdemes több példát / tisztázást adni.

**H5P analitika**

* Hol lépnek ki a Course Presentationből?
* Melyik AI-tipp slide-nál töltenek több időt (érdekli-e őket az AI-támogatás)?

**Assignment-rubrika adatok (Peula v2 + Zmán Kvucá)**

* A rubrika-sorok átlagpontszáma:
  * ha az R4 („Gyermekvédelem & biztonság”) vagy az R2 („Kvuca-illeszkedés & kvuca-meta”) sor gyenge sokaknál, az jelzi, hogy több **Zmán Kvucá- és biztonság-fókuszú** támogatás kell (pl. extra M7.B-szerű peula-műhely).
  * ha az R8 („Etikus AI-használat & emberi szöveg”) sor gyenge, érdemes külön mini-anyagot csinálni AI & gyermekvédelem témában.

**Quiz-eredmények (SMART & Zmán Kvucá)**

* Kérdés-szintű statisztika:
  * hol értik félre a SMART definíciót,
  * a Zmán Kvucá-checklist melyik pontját látják „feleslegesnek”.

**Offline visszajelzések (M7.A, M7.B, M7.F után)**

* 1 perces „kilépőkártya” (papíron vagy QR-kóddal; a QR-kérdőív elején a Program terv §7 adatvédelmi tájékoztató sablonja áll, és a válaszokhoz csak a legszűkebb szükséges hozzáférés adható, HUM-PRIV-01):
  * „Mennyire érzed, hogy most közelebb kerültél egy valódi Peula v2-höz?” (1–5 skála).
  * „Mi az, ami még bizonytalan benned a Zmán Kvucával / AI-használattal kapcsolatban?”

**Küszöbök / beavatkozási pontok**

* ha a résztvevők **>30%-a nem fejezi be** az M7.2-t vagy M7.3-at → a lemaradóknak **csendes pótlás** (önálló elmaradás-pótlás) ajánlott; az **M7.F F-peula** a nem teljesült kapu utáni, kötelező javítási alkalom, nem általános pótlás.
* ha a Peula v2 rubrika szerint a csoport kevesebb mint **60%-a** kap „Teljesítve” eredményt (az „M7 – KAPU” §B zárt ÉS-szabálya szerint) → sablon-finomhangolás, plusz támogatás cél- és biztonsági szinten (a kaput nem teljesítőknek a modul utáni **F-peula** ettől függetlenül is kötelező).



[M7.1 – „Ez még csak vágy, nem cél” – SMART nevelési cél someres módra](./Online%20leckék/M7.1%20–%20Ez%20még%20csak%20vágy,%20nem%20cél%20–%20SMART%20nevelési%20cél%20someres%20módra.md)

[M7.2 – „Nemcsak játék, hanem peula” – 11 tervezési pont & AI-támogatás](./Online%20leckék/M7.2%20–%20Nemcsak%20játék,%20hanem%20peula%20–%2011%20tervezési%20pont%20&%20AI-támogatás.md)

[M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség](./Online%20leckék/M7.3%20–%20Zmán%20Kvucá-checklist%20–%20idő,%20tér,%20felelősség.md)

[M7.4 – „Peula v1 + AI” – első modulproduktum-vázlat](./Online%20leckék/M7.4%20–%20Peula%20v1%20+%20AI%20–%20első%20modulproduktum-vázlat.md)

[M7.A – Célból peula – SMART & 11 pont élőben](./Peulák/M7.A%20–%20Célból%20peula%20–%20SMART%20&%2011%20pont%20élőben.md)

[M7.B – Peula v2 & Zmán Kvucá – amikor a papír találkozik a valósággal](./Peulák/M7.B%20–%20Peula%20v2%20&%20Zmán%20Kvucá%20–%20amikor%20a%20papír%20találkozik%20a%20valósággal.md)

[M7.F – Felzárkóztató peula – Peula & Zmán Kvucá](./Peulák/M7.F%20–%20Felzárkóztató%20peula%20–%20Peula%20&%20Zmán%20Kvucá%20%28Study%20Lab%29.md)
