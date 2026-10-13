# Jóváhagyási csomag – értékelési felelős (és ahol a döntés előírja: Memuna, modulgazda, M5 szerzője, szakmai lektor, DPO) (AP-2026-10-13-01)

> **Audit trail, nem kánon.** Előre kitöltött elfogadási javaslat a 2026-10-13-i futásból. A projektgazda irányait a
> `02 Tervezet/Emberi jóváhagyás szükséges.md` 15. szakasz rögzíti; ahol a döntés vagy a jóváhagyás a címzett szerep hatásköre, az irány **nem helyettesíti** az ő
> döntését. A javasolt szövegek tervezetek: a tananyagba csak az írásos elfogadás után kerülnek, `/course-fix`-szel.
> A tervezeteket read-only szakértői ügynökök készítették, a fő session ellenőrizte; a sorszámok a `8bb4d7d` körüli
> állapotra vonatkoznak, átvezetéskor újra ellenőrizzük őket.

Címzett: a kurzus értékelési felelőse. Kulcs, küszöb, rubrikaszint csak az itt kért jóváhagyással változik; a szigorító változás előzetes tanulói tájékoztatóval, visszamenőleges hatás nélkül lép hatályba.

## Hogyan válaszolj

- Tételenként: **ELFOGADOM** / **MÓDOSÍTOM: …** / **VÉTÓ**, dátummal és szerepnévvel. A repó nyilvános: személynév,
  személyes adat ne kerüljön a válaszba vagy az issue-ba.
- Elfogadásnál a javasolt szöveg (a „DPO tölti ki”, „Memuna dönt” mezők kitöltésével) a következő engedélyezett javítási körben
  kerül be; vétónál a mostani szöveg marad, és az érintett 14. szakaszbeli sor `REOPENED`.
- Az elfogadás nem release-jóváhagyás: a G1–G8 kapuk bizonyítéka és a go/no-go döntés külön lépés (`02 Tervezet/RELEASE-READINESS.md`).
- A rubrikaszint-változásnál a projektgazda jóváhagyása is kell (HUM 14 ERT-21, GYV-9, ERT-32, ERT-43).

## Tételek

| Tétel | Mit kérünk | Kapcsolódó ledger-kulcsok / kapu |
|---|---|---|
| D-07 | ERT-21 (M3 R2/R3, öt hely), GYV-18 (M6 12. item tervezet), GYV-9 (M7 R4 18+ felnőtt), ERT-32 (M6 R4 „Oké”) + Memuna-kalibráció | M3:QA14-BIZT-2, M6:QA14-BIZT-3, M7:BIZT-G1-2, M7:PED-G2-4, M6:ERT-G1-2, M6:ERT-G3-4 |
| D-17 (a)–(c) | ERT-26 kalibrációs mondat (M5); ERT-42 R8 kettéválasztás + adatvédelmi stop (+ DPO); ERT-43 R1 horgony (+ projektgazdai jóváhagyás) | M5:QA14-ERT-1, M7:BIZT-G1-1, M7:PED-G1-1 |
| D-18 | ERT-23 (M3.2 kulcsok), ERT-28 (M5.2 SLIDE 8), ERT-30 (M5 Q12 C), PRG-15 b (M5.1 SLIDE 4) | M3:IMPL-G2-14, M5:ERT-G1-9, M5:NYELV-G1-11, M5:PED-G1-3 |
| D-19 (a), (c) | az M5 hub és az M2 hub kimeneti céljai (+ modulgazda; TERM-7) | M5:PED-G1-10, M2:QA14-ERT-2 |
| ERT-19 | SIGNOFF: az M2 identitáskör-követelmény és az előzetes tájékoztató | M2:PED-G1-11; X-3 |
| D-10 (c), (d) | feltárásmentes pótlás: külön, kézzel nyitott próbálkozás, nem fogy a keretből (+ programvezető, Memuna-vétó) | M1:QA14-BIZT-5 |
| Vétó/QA (megvalósítva) | D-15 (a) LMS-M3-08 (a kvíz bármely rubrikaértékkel nyílik), (c) M4 rubrika helye, (d) M6 pontozás; D-16 Z.4; D-19 (b) M4.1 ILO 2; D-23 M7 Review options | HUM 15; 8bb4d7d |

## Részletes javaslatok

### A1: az értékelési felelős jóváhagyási csomagjának tervezete (D-07, D-17, D-18, D-19 (a)(c), D-16, ERT-19, D-10 (c)(d))


**Három dolog, amit érdemes elsőként tudnod:**
- **Két sorszám elcsúszott:** a kért M3.4:837 ma a 808. sor, a kért M7 KAPU:93 (Q3) ma a 94. sor.
- **Egy kánoni bizonyíték szembemegy a kért iránnyal (3a, ERT-23, 2. item):** az M3.2:328 szinte szó szerint ezt a jelenetet tanítja Kivsza-példaként. Ezért mindkét változatot leírtam, a jóváhagyók választanak.
- **Egy új rés keletkezne (2c, ERT-43):** az R1 2-es szintjének szigorítása után az R1 1-es szint leírása nem fedné le azt a célt, amelyben csak időkeret van. Ezért javaslok egy együtt mozgó :278-as cserét is.

**Rövidítések** (a repó gyökere: ``):
- KAPU-M3/M5/M6/M7 = `02 Tervezet/Modulok/Mx/Mx – Kapu – értékelő (item-bank + rubrika).md`
- M3.4 = `02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md`
- M3.B = `02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépéstérkép.md`
- M3.2 = `02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md`
- M6.B = `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md`
- M7.4 = `02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md`
- M7.1 = `02 Tervezet/Modulok/M7/Online leckék/M7.1 – Ez még csak vágy, nem cél – SMART nevelési cél someres módra.md`
- M5.1 / M5.2 = `02 Tervezet/Modulok/M5/Online leckék/M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md` / `…/M5.2 – Feladat → módszer döntési fa – Mit választok először.md`
- HUB-M5 = `02 Tervezet/Modulok/M5/M5 – Ez most játék vagy tanulás – Nonformális nevelés, módszerválasztás & tanulástan.md`
- HUB-M2 = `02 Tervezet/Modulok/M2/M2 – Ki vagyok madrihként – Identitás, Somer-értékek és dugma isit.md`

**Közös hatálybalépési feltétel minden szigorító tételnél** (D-07 (a)(c)(d), ERT-43, ERT-42, ERT-19):
- a jóváhagyott szöveg előbb a tanulónak látható helyen jelenik meg, és csak utána élesedik;
- az első érintett kohorsz az, amelynek a modulja a közzététel után nyílik;
- a hatálybalépés előtt megkezdett kapuciklusra (a normál és a hozzá tartozó javító leadásra is) a régi horgony érvényes;
- nincs visszamenőleges hatás.

Látható szöveg változik, ezért pin kell (`--pin-visible`, a finding- és HUM-ID-kkal). Jóváhagyást, dátumot vagy nevet sehová nem írtam be.

---

### D-07 (a) – ERT-21: az M3 kapu öt helye + az R3 Alapszintje

### ERT-21-1 – A 2.1 kalibrációs szabálya
- Fájl: KAPU-M3:318
- Alap: HUM 14 ERT-21 (HUM:691), D-07 irány; G3 ajánlása: (1)(a) és (2)(c)
- Hatáskör: SZEREP: értékelési felelős + Memuna (kalibráció); a rubrikaszintről a projektgazda dönt
- OLD (egyedi; a :325-ös párja kisbetűs): `Ahol a leírt helyzetben nincs feltárás vagy titoktartási ígéret, az R2-t nem büntető módon alkalmazzuk:`
- NEW: `Ahol a leírt helyzetben nincs feltárás, titoktartás-kérés vagy titoktartási ígéret, az R2-t nem büntető módon alkalmazzuk:`
- Kiegészítés ugyanebben a sorban:
  - OLD-horgony: `A kalibrációt a Memuna és az értékelési felelős végzi.` (egyediségét nem greppeltem)
  - NEW: `Az R3 Alapszintjén a kijelölt Memuna bevonása mindig elfogadott; ha a leírt helyzet pusztán hiányzó felnőtt felügyelet operatív ügye, a képző vagy a programvezető megnevezése is Alapszint, akut kockázatnál a Memunáé is (GYV-8). A kalibrációt a Memuna és az értékelési felelős végzi.`
- Együtt mozgó helyek: :325 (két cella), :326, M3.4:808, M3.B:513
- Címkék: VÉTÓLISTÁS (rubrikaszint, blokkoló R2) / LÁTHATÓ SZÖVEG (értékelői)
- Indoklás:
  - A hanih kérését a kánon központi esetként tanítja (M3.3:177, :187).
  - A sablon 5. kérdése (M3.4:803) kérdez a titoktartásra, így a sablont követő tanuló nem bukik.
  - A GYV-8-at szűken, a döntés szövege szerint vettem át. A G3 tágabb „operatív határhelyzet” olvasata (pl. „kedvenc hanih”, határtalan chat) új alkalmazási eset lenne: Memuna-kérdés.

### ERT-21-2 – Az R2 0-s cellája
- Fájl: KAPU-M3:325
- OLD: `vagy – feltárást vagy titoktartási ígéretet tartalmazó helyzetben – a titoktartás kérdését meg sem említi.`
- NEW: `vagy – feltárást, titoktartás-kérést vagy titoktartási ígéretet tartalmazó helyzetben – a titoktartás kérdését meg sem említi.`
- Címkék: VÉTÓLISTÁS (blokkoló sor; szigorítás a kérés-esetre, ezért előzetes közlés kell) / LÁTHATÓ SZÖVEG

### ERT-21-3 – Az R2 Alapszint cellája
- Fájl: KAPU-M3:325
- OLD: `ahol a leírt helyzetben nincs feltárás vagy titoktartási ígéret, a titoktartás említésének hiánya is Alapszint`
- NEW: `ahol a leírt helyzetben nincs feltárás, titoktartás-kérés vagy titoktartási ígéret, a titoktartás említésének hiánya is Alapszint`
- Címkék: VÉTÓLISTÁS / LÁTHATÓ SZÖVEG

### ERT-21-4 – Az R3 fejléce és Alapszintje (a (2)(c) opció)
- Fájl: KAPU-M3:326
- Fejléc:
  - OLD: `*(megfigyelhető: megnevezi, hogy a madrih azonnal a Memunát vonja be)*`
  - NEW: `*(megfigyelhető: megnevezi, kit von be azonnal a leírt madrih)*`
- Alapszint:
  - OLD: `Megnevezi, hogy a leírt madrih **azonnal a kijelölt Memunát vonja be** (összeférhetetlenség esetén a név szerint kijelölt helyettesét).`
  - NEW: `Megnevezi, hogy a leírt madrih **azonnal a kijelölt Memunát vonja be** (összeférhetetlenség esetén a név szerint kijelölt helyettesét); ha a leírt helyzet pusztán hiányzó felnőtt felügyelet operatív ügye, Alapszint az is, ha a képzőt vagy a programvezetőt nevezi meg – akut kockázatnál a Memunát is (GYV-8).`
- Együtt mozgó helyek: a :340-es R3-sablon maradhat (a túleszkaláció nem veszélyes)
- Címkék: VÉTÓLISTÁS (rubrikaszint; ez enyhítés, nem szigorítás) / LÁTHATÓ SZÖVEG
- Egyediség: a „azonnal a kijelölt Memunát vonja be” minta a fájlban 2 sorban fordul elő; a teljes OLD a „Megnevezi, hogy a leírt madrih” kezdettel várhatóan egyedi, de ezt Greppel ellenőrizni kell.

### ERT-21-5 – Tanulói tükörmondat az M3.4-ben (ez maga az előzetes tájékoztató)
- Fájl: M3.4:808 (a kért :837 elcsúszott; a sor nincs `@source` blokkban, a NAR-02-VO a :814-nél kezdődik)
- OLD: `vagy – ha a helyzetben feltárás vagy titoktartási ígéret szerepel – a titoktartás kérdését meg sem említi, illetve ha **nyomoz, kikérdez vagy konfrontál**`
- NEW: `vagy – ha a helyzetben feltárás, titoktartás-kérés vagy titoktartási ígéret szerepel – a titoktartás kérdését meg sem említi, illetve ha **nyomoz, kikérdez vagy konfrontál**`
- Címkék: LÁTHATÓ SZÖVEG; a fájlban egyszer szerepel

### ERT-21-6 – Tanulói tükörmondat az M3.B-ben
- Fájl: M3.B:513 (képzői szkript-idézet, nem `@source`)
- OLD: `vagy – ha a helyzetben feltárás vagy titoktartási ígéret szerepel – a titoktartás kérdését meg sem említi, illetve ha nyomoz vagy konfrontál`
- NEW: `vagy – ha a helyzetben feltárás, titoktartás-kérés vagy titoktartási ígéret szerepel – a titoktartás kérdését meg sem említi, illetve ha nyomoz vagy konfrontál`
- Címkék: LÁTHATÓ SZÖVEG; a fájlban egyszer szerepel

**A D-07 (a) jóváhagyási feltételei:**
- Memuna + értékelési felelős írásos kalibrációja, 1–2 referenciamintával, köztük egy „ne mondd el senkinek” esettel és egy operatív felügyeleti esettel (KAPU-M3:317);
- a projektgazda rubrikaszint-jóváhagyása;
- a hatt hely egy menetben változik.

---

### D-07 (b) – GYV-18: az M6 kapu 12. iteme

TERVEZET. Jóváhagyja: Memuna + értékelési felelős; a kulcsról a projektgazda dönt. A ✅ pozíciója (A) marad, a tartalma változik.

### GYV-18-1 – Cím
- Fájl: KAPU-M6:325
- OLD: `## 12. ITEM – Érzékenység a felkavaró tartalmakra: friss seb / biztonságos vs. szégyenítő kérdés`
- NEW: `## 12. ITEM – Érzékenység a felkavaró tartalmakra: szereplőközpontú vs. szégyenítő kérdés`
- Címkék: LÁTHATÓ SZÖVEG

### GYV-18-2 – Szár
- Fájl: KAPU-M6:328
- OLD: `Elmeséled a történetet Liliről, az új lányról (egy újonnan érkezőt egy beszólás kicsit kirekeszt). Tudod, hogy a kvucában nemrég valakit tényleg kicsúfoltak.`
- NEW: `Elmesélsz a kvucának egy kitalált történetet egy hanihról, akit a csapatválasztásnál mindig utolsónak hívnak.`
- A szár második fele (`**Melyik feldolgozó kérdés…**`) marad.
- Címkék: VÉTÓLISTÁS (kapu-item) / LÁTHATÓ SZÖVEG
- Indoklás: a GYV-18 fiktív, szereplőközpontú helyzetet kér; az ERT-36 új helyzetet kér, nem a Lili-leckét.

### GYV-18-3 – Opciók
- Fájl: KAPU-M6:331–334
- A ✅:
  - OLD: `- A) „Láttál-e már olyat, hogy egy beszólás miatt valaki kívül érezte magát? (Nem kell nevet mondani.)” ✅`
  - NEW: `- A) „Szerintetek mit érezhetett ő, amikor megint utolsónak hívták, és mit tehetett volna a csapat?” ✅`
- B (megnevezés, szégyenítés):
  - OLD: `- B) „Ki volt itt a bunkó? Nevezzük meg!”`
  - NEW: `- B) „Ki szokott nálatok utolsó maradni? Mondjuk ki!”`
- C (álkérdés): marad változatlanul.
- D (áldozathibáztatás):
  - OLD: `- D) „Szerintetek Lili túlreagálta?”`
  - NEW: `- D) „Szerintetek nem csinált ebből túl nagy ügyet?”`
  - Alternatíva a jóváhagyóknak: `„Szerintetek nem ő tehet róla, hogy utolsónak választják?”`
- Címkék: VÉTÓLISTÁS (kulcs, disztraktor) / LÁTHATÓ SZÖVEG
- Indoklás: az új ✅ nem azonos a lecke ✅-jával (M6.2:655: „Melyik szereplő nézőpontját érted a legjobban…”), így az ERT-36 teljesül.

### GYV-18-4 – A B disztraktor indoka
- Fájl: KAPU-M6:338
- OLD: `- B – Konkrét emberre mutat → **megszégyenítés**, főleg friss seb mellett veszélyes.`
- NEW: `- B – Valódi, jelen lévő emberre mutat → **megszégyenítés**; megszünteti a kitalált történet védő távolságát.`

### GYV-18-5 – Visszajelzés
- Fájl: KAPU-M6:343
- OLD: `> ✅ A nem szégyenítő kérdés megengedi a saját élményt, de nem mutat rá konkrét emberre, és nem kényszerít egyetlen válaszra – ez teszi a történetet tükörré. (M6.2, 5. dia)`
- NEW: `> ✅ A szereplőről szóló kérdés biztonságos távolságot ad: senkinek nem kell a saját élményéről beszélnie, mégis végig lehet gondolni, mit érezhetett a szereplő, és mit tehetett volna a csoport. Nem mutat rá konkrét emberre, és nem kényszerít egyetlen válaszra – ez teszi a történetet tükörré. A „nálatok” kérdés csak opcionális, és bárki passzolhat. (M6.2, 5. dia)`
- Az „5. dia” hivatkozás ellenőrizve: M6.2 SLIDE 5 = :549.
- Együtt mozgó hely: az M6.2:631–632 narráció → VO-PACK (a médiafelelősnek; forrás: az M6.2:606 diaszövege), nem ebben a csomagban.

---

### D-07 (c) – GYV-9: az M7 R4 és a felelős 18+ felnőtt

A hangolás állapota (most beolvasva):
- A Q9 (KAPU-M7:165, :172) már harmonikus: a szár és a visszajelzés is kimondja, hogy „a 18 év feletti felelős felnőtt végig jelen van”, ezért a D opció nem hiány. A ✅ B marad, nincs változás.
- A (C) 5. sora (:389) 2-es szintje már tartalmazza: „ki a jelen lévő, 18 év feletti felelős felnőtt – megnevezve”. Nincs változás.
- A rés csak az R4-ben van, és a mintatábla nem közli.
- Hatáskör: SZEREP: Memuna + értékelési felelős (a horgony és a Q9/(C) együtt); a rubrikaszintről a projektgazda dönt.

### GYV-9-1 – Az R4 2-es szintje
- Fájl: KAPU-M7:314
- OLD (a fájlban egyszer szerepel; a táblázat sorvégi kitöltő szóközei nélkül): `| **2** | A Zmán Kvucá-checklist alapján **legalább 1 konkrét gyermekvédelmi lépés** szerepel (mit tesz red flag esetén, **kit von be** – a Memunát), és látszik a **B-terv** a kockázatos elemnél.`
- NEW: `| **2** | A Zmán Kvucá-checklist alapján **legalább 1 konkrét gyermekvédelmi lépés** szerepel (mit tesz red flag esetén, **kit von be** – a Memunát), **meg van nevezve a jelen lévő, 18 év feletti felelős felnőtt** (szerepnévvel is elég, pl. „felnőtt C”), és látszik a **B-terv** a kockázatos elemnél.`
- Címkék: VÉTÓLISTÁS (blokkoló, kritikus sor szigorítása) / LÁTHATÓ SZÖVEG

### GYV-9-2 – Az R4 3-as szintje
- Fájl: KAPU-M7:315
- OLD: `+ határhelyzet-mondat („mit nem engedek meg”) + B-terv – mind a saját peulára szabva, nem sablonszöveg.`
- NEW: `+ határhelyzet-mondat („mit nem engedek meg”) + a jelen lévő, 18 év feletti felelős felnőtt megnevezése + B-terv – mind a saját peulára szabva, nem sablonszöveg.`
- Címkék: VÉTÓLISTÁS. Egyediségét nem greppeltem.

### GYV-9-3 – A Q14 visszajelzése (opcionális, a kulcs nem változik)
- Fájl: KAPU-M7:241
- OLD: `és a **megnevezett jelzési út** (azonnal a Memunához) mind kötelező.`
- NEW: `és a **megnevezett jelzési út** (azonnal a Memunához) mind kötelező; a Peula v2-ben azt is meg kell nevezned, ki a jelen lévő, 18 év feletti felelős felnőtt.`
- Címkék: LÁTHATÓ SZÖVEG. A ✅ A/B/C marad; új opció nem kell (az kulcsváltozás lenne).

### GYV-9-4 – Az M7.4 mintatáblája
- Fájl: M7.4:785
- OLD: `*(A neveknél most elég annyi, hogy „madrih A / B” – ez egy gyakorlat, nem éles beosztás.)*`
- NEW: ugyanez, utána új sor: `*A táblázat alá írd oda azt is, ki a jelen lévő, 18 év feletti felelős felnőtt (itt is elég a szerepnév, pl. „felnőtt C”): a Peula v2-ben ez a gyermekvédelmi rész minimumához tartozik.*`
- Együtt mozgó hely: GYV-9-5
- Címkék: LÁTHATÓ SZÖVEG
- Miért mondat és nem példasor: a MUNK-01 sablonba a példasorok nem kerülnek át, így csak mondatként jut el a fájlos úton leadóhoz is (egyenértékű út).

### GYV-9-5 – Az M7.4-MUNK-01 spec
- Fájl: M7.4:817
- OLD: `utána szó szerint a „(A neveknél most elég annyi …)” mondat és az 1:1 helyzetekről szóló dőlt bekezdés;`
- NEW: `utána szó szerint a „(A neveknél most elég annyi …)” mondat, a 18 év feletti felelős felnőttről szóló mondat és az 1:1 helyzetekről szóló dőlt bekezdés;`
- Címkék: BUILD-INPUT (@asset) → build, külön `chore(media)` commit, pin
- Megjegyzés: a spec „Új mező, minta vagy útmutató szöveg nem kerül bele” mondata a forrásszöveg bővülése miatt nem sérül, de ezt a jóváhagyó lássa.

### GYV-9-6 – Előzetes tanulói tájékoztató (közös blokk: GYV-9, ERT-43, ERT-42)
- Fájl: KAPU-M7:408 után (az „Üzenet a tanulónak” blokk a feladatleírásba is beilleszthető), és röviden az M7.4:706 után
- NEW: `> **Mire figyelj a Peula v2-nél ([kohorsz]-tól érvényes):** (1) A SMART célodban legyen legalább egy ellenőrizhető jel vagy kimenet (pl. „legalább X hanih…”, „a peula végére mindenki … tud”); az időpont önmagában nem elég. (2) A biztonsági részben nevezd meg azt is, ki a jelen lévő, 18 év feletti felelős felnőtt (szerepnévvel is elég). (3) Ha a beadásodban mégis szerepel egy hanih vagy más személy azonosítható adata (név, beazonosítható történet), a v2-det a pontszámtól függetlenül javításra visszakapod, és az adatot el kell távolítanod. Ezek a szabályok a korábban leadott munkákra nem vonatkoznak.`
- Hatáskör: (1) ERT-43 → projektgazdai jóváhagyás; (2) GYV-9; (3) ERT-42 → csak a DPO jóváhagyása után kerülhet be
- Címkék: LÁTHATÓ SZÖVEG

---

### D-07 (d) – ERT-32: az M6 R4 „Oké” horgonya, (B) opció

Hatáskör: SZEREP: értékelési felelős (+ Memuna a kalibrációban); a rubrikaszintről a projektgazda dönt.

### ERT-32-1 – A rubrika R4 „Oké” cellája
- Fájl: KAPU-M6:399
- OLD-horgony: `„fiktív esetet elemzünk; nem zárunk ki résztvevőt demonstrációként”).` (egyediségét nem greppeltem)
- NEW: `„fiktív esetet elemzünk; nem zárunk ki résztvevőt demonstrációként”). **Két eszköztípusnál a tanított minimum kell:** bizalom- vagy kontaktjátéknál a szabad, akadályoktól mentes tér, a közös „stop” jelszó, a lassú (séta) tempó és a vezető társ kísérése, folyamatos hangos jelzése (M6.1); szenzitív témájú eszköznél (pl. személyes élményt érintő történet vagy feldolgozás) a passz joga (bárki indoklás nélkül kimaradhat) és a megnevezett felnőtt, akihez a madrih fordul, ha valakinek sok (M6.2, M6.4).`
- Címkék: VÉTÓLISTÁS (blokkoló sor szigorítása) / LÁTHATÓ SZÖVEG
- Indoklás:
  - A kontaktjáték-minimum szó szerint a KAPU-M6:189-ből jön.
  - A „passz és felnőtt” az M6.2:606-ból és az M6.4:938–940-ből: kiülésnél legyen vele egy felnőtt, erős érintettségnél be kell vonni a Memunát.
  - Az ERT-32 „felnőtt” szava kétértelmű; a Memuna mondja ki.

### ERT-32-2 – Az „Oké”-ellenőrzőlista
- Fájl: KAPU-M6:409
- OLD: `- [ ] **R4** *(blokkoló)* – legalább **1** konkrét, eszközspecifikus biztonsági mondat (nem általánosság).`
- NEW: `- [ ] **R4** *(blokkoló)* – legalább **1** konkrét, eszközspecifikus biztonsági mondat (nem általánosság); bizalom- vagy kontaktjátéknál a tér, a „stop” jelszó, a tempó és a kísérés mind, szenzitív témájú eszköznél a passz és a megnevezett felnőtt is.`
- Címkék: VÉTÓLISTÁS / LÁTHATÓ SZÖVEG

### ERT-32-3 – Az M6.B mezőlistája és rubrikafelütése
- Mezőlista, M6.B:216 és :48:
  - OLD: `Biztonsági szempontok (mikor állsz le, kit hívsz, ha valakinek sok)`
  - Ez a szöveg kétszer szerepel; a két sor csak a behúzásban tér el (a :48-ban 2, a :216-ban 3 szóköz), ezért a sor eleji behúzással együtt kell horgonyozni.
  - NEW: `Biztonsági szempontok (mikor állsz le, kit hívsz, ha valakinek sok; kontaktjátéknál tér, „stop”, tempó, kísérés; szenzitív témánál passz és a megnevezett felnőtt)`
- Rubrikafelütés, M6.B:225:
  - OLD: `* R4 Biztonság (blokkoló): legalább 1 konkrét, erre az eszközre vonatkozó biztonsági mondat.`
  - NEW: `* R4 Biztonság (blokkoló): legalább 1 konkrét, erre az eszközre vonatkozó biztonsági mondat; kontaktjátéknál a tér, a „stop” jelszó, a tempó és a kísérés mind, szenzitív témánál a passz és a megnevezett felnőtt is.`
- Asset-spec, M6.B:139 (BUILD-INPUT):
  - OLD: `R4 Biztonság (blokkoló) – legalább 1 konkrét, erre az eszközre vonatkozó biztonsági mondat;`
  - NEW: `R4 Biztonság (blokkoló) – legalább 1 konkrét, erre az eszközre vonatkozó biztonsági mondat, kontaktjátéknál a tér, a „stop” jelszó, a tempó és a kísérés mind, szenzitív témánál a passz és a megnevezett felnőtt is;`
- Címkék: LÁTHATÓ SZÖVEG; a :139 BUILD-INPUT (build, pin)

**Kalibrációs terv (ERT-32):**
- 6–10 kitalált (nem valós tanulói) mintalap: legalább 3 bizalom- vagy kontaktjáték, legalább 3 szenzitív témájú eszköz, 1–2 egyéb (kézműves) kontrollnak.
- Minden típusban legyen határeset (pl. van tér és „stop”, de nincs tempó).
- Két értékelő (értékelési felelős + Memuna) az új horgonnyal egymástól függetlenül pontoz; az eltéréseket megbeszélik, a döntést és az indokot referenciamintaként rögzítik.
- Az egyezési kritériumot az értékelési felelős állapítja meg; számot nem javaslok.
- Hatálybalépés: a közös feltétel szerint, az M6.B 4.2 és az M6 kapu feladatleírása az előzetes közlés helye.

---

### D-17 – Kalibráció és rubrikahorgonyok

### ERT-26 – Kalibrációs mondat az M5 kapuban
- Fájl: KAPU-M5:286 után, új blockquote-sorként (a :286 maga `> `-szel kezdődik; a :287 üres)
- Alap: HUM 14 ERT-26 (`A`), D-17 irány, G6 (a) opció
- Hatáskör: SZEREP: értékelési felelős (a projektgazdai irány megvan); QA: módszertani lektor
- OLD-horgony: a teljes :286-os sor (`> **Átmenő szabály (a kapu):** mind a 4 kritérium (rubrikasor) legalább **„Alapszint”**, …`), utána beszúrás
- NEW: `> **Kalibráció (ERT-26):** a „soronként látható módszertani indok” az R3 sorban így olvasandó: Alapszinten elég, ha a sorban a cél, a kvuca és a módszer illeszkedése felismerhető (vagy kiolvasható a 4. mezőből); a kifejezett, egymondatos „miért” továbbra is az Erős szint jegye. Tanulástan-elem nem kell minden sorba, az R4-et a teljes táblázat alapján értékeljük. A szintek, a küszöb és az R4 kritikus státusza nem változik.`
- Címkék: VÉTÓLISTÁS (rubrikaszint-értelmezés; nem szigorít, ezért tájékoztató nem kell) / LÁTHATÓ SZÖVEG (értékelői)

### ERT-42-1 – Az R8 csak pedagógiai sor lesz
- Fájl: KAPU-M7:360 és :362
- Hatáskör: SZEREP: értékelési felelős + DPO; QA: DPO + programvezető. Az adatvédelmi stop eljárása DPO-hatáskör.
- 0-s szint (:360):
  - OLD: `| **0** | A szöveg „robotnyelvű”, sablonos, AI-másolat hatású, **és/vagy** beazonosítható hanih-adat (név, konkrét sztori) szerepel benne. **(Adatszivárgás esetén jelzés a mentornak; ha gyermekvédelmi feltárás jelenik meg benne, az kikerül a Moodle-ből, és a Memuna bevonásával az incidensfolyamatba kerül.)** |`
  - NEW: `| **0** | A szöveg „robotnyelvű”, sablonos, AI-másolat hatású; nem látszik benne a madrih saját szövege és döntése. *(Azonosítható személyes adat: lásd az alábbi adatvédelmi stopot – ezt nem ez a sor pontozza.)* |`
- 2-es szint (:362):
  - OLD: `| **2** | A szöveg **emberi, érthető**; **nincs** beazonosítható hanih-adat. |`
  - NEW: `| **2** | A szöveg **emberi, érthető**. |`
- Feltétel: csak az ERT-42-2-vel EGY MENETBEN szabad bevinni, különben az adatvédelmi védelem gyengülne.
- Címkék: VÉTÓLISTÁS (rubrika, kapuhatás) / LÁTHATÓ SZÖVEG

### ERT-42-2 – Külön, nem pontozott adatvédelmi stop
- Fájl: KAPU-M7, új blokk az R8 táblázata után, a `### Pontozás & döntési szabály (összefoglaló)` elé
- NEW: `> ⛔ **Adatvédelmi stop (nem pontozott, a rubrikától független; ERT-42):** ha a beadásban egy hanih vagy más harmadik személy azonosítható adata szerepel (pl. név, konkrét, beazonosítható történet), a beadást a pontszámtól és a rubrikasoroktól függetlenül nem fogadjuk el: az értékelő jelzi a mentornak, a beadás javításra visszamegy, és a tanuló az azonosítható adat eltávolításával adja le újra. A korlátozás, az incidensértékelés és az adateltávolítás a DPO által jóváhagyott eljárás szerint történik ([DPO-HATÁSKÖR: az eljárás helye és tartalma – jóváhagyásig nem tölthető ki]). Ha gyermekvédelmi feltárás jelenik meg benne, az kikerül a Moodle-ből, és a Memuna bevonásával az incidensfolyamatba kerül. [NYITOTT RÉSZKÉRDÉS: az adatvédelmi stop miatti újraleadás nem fogyasztja a javító leadást – értékelési felelős + DPO, QA: programvezető.]`
- Az összefoglalóban (:370) a blokkoló sor után:
  - OLD: `* **Blokkoló:** R4 < 2 → **„Még nem teljesítve”**, függetlenül mindentől (a pontszámtól és a többi sortól is).`
  - NEW: ugyanez, utána új sor: `* **Adatvédelmi stop:** azonosítható harmadik személyes adatnál a beadás a pontszámtól függetlenül javításra megy (lásd az R8 alatt); ez nem pontozott szempont.`
- Címkék: VÉTÓLISTÁS / LÁTHATÓ SZÖVEG
- Indoklás: a gyermekvédelmi ág szó szerint megmarad. Hogy egy hanih-név incidens-e, és hogy a GDPR 33. cikk alkalmazandó-e, az DPO-értékelés; jogi minősítést nem írtam.

### ERT-43 – Az M7 R1 2-es szintjének új horgonya
- Hatáskör: SZEREP: az értékelési felelős írja; projektgazdai jóváhagyással lép hatályba (HUM 14 ERT-43 `F`); QA: módszertani lektor
- R1 2-es szint (KAPU-M7:279; a fájlban egyszer szerepel):
  - OLD: `és tartalmaz **legalább egy mérhető jelet VAGY időkeretet** („a peula végére…”, „legalább X hanih…”).`
  - NEW: `és tartalmaz **legalább egy ellenőrizhető jelet vagy kimenetet** („legalább X hanih…”, „a peula végére mindenki … tud”); az időkeret önmagában nem elég.`
- R1 1-es szint (KAPU-M7:278) – új, együtt mozgó csere:
  - OLD: `nincs benne mérhető jel vagy időkeret.`
  - NEW: `nincs benne ellenőrizhető jel vagy kimenet (egy időpont önmagában ezen nem változtat).`
  - Ok: enélkül a csak időkeretet tartalmazó cél egyik szintleírásba sem illene.
- Q3 visszajelzés (KAPU-M7:94; a kért :93 elcsúszott; a ✅ B marad):
  - OLD: `e kettő nélkül a cél ellenőrizhetetlen vágy marad, akkor is, ha specifikus és releváns.`
  - NEW: ugyanez + ` Az időpont önmagában még nem teszi ellenőrizhetővé a célt: kell mellé egy jel, amiből a végén látod, hogy megtörtént.`
- M7.1:320 (H5P visszajelzés, nem `@source`):
  - OLD: `> A következő feladatban a **Mérhető** elemet gyakoroljuk: konkrét számot írsz a célmondatokba.”`
  - NEW: elé új sor: `> Az időpont önmagában még nem elég: kell egy jel is, amiből a végén látod, hogy megtörtént.`
- Tájékoztató: a GYV-9-6 (1) pontja
- Címkék: VÉTÓLISTÁS (rubrikaszint-szigorítás) / LÁTHATÓ SZÖVEG

### ADV-5 R1 – nincs szerkesztés (megerősítés)
- Fájl: KAPU-M7:279 és :408
- Az R1 2-es szintjének „Somer-értékhez kötve” fordulata marad.
- A KAPU:408 kimondja: „semleges vagy kitalált someres érték is elfogadott, pontlevonás nélkül”.
- Hatáskör: DPO / jogi felelős, someres vonatkozásban a projektgazda. Az ERT-43-mal egy menetben kell visszaigazolni.

---

### D-18 – Item- és kulcsdöntések

### ERT-23 – Az M3.2 párosító kulcsa
- Fájl: M3.2:658–666
- Hatáskör: SZEREP: értékelési felelős + M3 modulgazda, itemenként
- Itemenkénti javaslat:
  - 1., 4., 7.: egy kulcs marad (Parparim, Leviatán, Leviatán).
  - 3.: egy kulcs, Leviatán. Ezt a lecke szó szerint tanítja: :448 „Két hanih összeveszik azon, ki kiben bízik…”, :767 minikvíz „ki kiben bízik” → Leviatán.
  - 6.: egy kulcs, Leviatán. A korosztálytérkép (:579) szerint az „identitás… önreflexió” Leviatán-jel; a Kivsza sor (:578) „a beégés érzékeny pont lehet” fordulata inkább a nyílt önfeltárás ellen szól. Ez a határeset: ha a jóváhagyók a Kivsza „kortársak véleménye” jelét is elfogadják, kétkulcsos lesz.
  - 5.: két kulcs.
    - OLD: `5. „A madrih kérdést tesz fel, és két ember mindig egymás szavába vágva, nagy hanggal válaszol, a többiek hallgatnak.” → 🐑 Kivsza`
    - NEW: ugyanez, a végén `→ 🐑 Kivsza vagy 🐋 Leviatán (mindkettő elfogadott)`
  - 2.: ELLENTMONDÁS. A kért irány (G9) két kulcs (`→ 🐑 Kivsza vagy 🐋 Leviatán (mindkettő elfogadott)`). Az én javaslatom viszont egy kulcs, Kivsza:
    - az M3.2:328 szinte szó szerint ezt tanítja Kivsza-példaként („valaki hangos poént mond, a többiek nevetnek, valaki meg kicsit megsértődik, de nem mondja ki”);
    - a :321 „poénok, beszólások, hangos kommentek”;
    - a D-18 szerint a kulcs a ténylegesen tanított tartalomhoz igazodjon.
    - Az OLD (egyedi): `2. „Valaki bekiabál egy poént, amin a fél kvuca röhög, a másik fele pedig kicsit lefagy, de nem szól semmit.” → 🐑 Kivsza`
- Validálási zárójel (:666):
  - OLD: `A validálásig a fenti kulcs érvényes; a visszajelzés legyen iránymutató.)`
  - NEW (csak jóváhagyás után): `A jelenetenkénti validálás (ERT-23) szerint az 5. jelenetnél [és a 2.-nál, ha így döntenek] a Kivsza és a Leviatán is helyes; a többinél egy kulcs marad, mert a jelek egyértelműek. A visszajelzés iránymutató.)`
- Új `chosenFeedback` az 5. item Leviatán-válaszához (tervezet): `„Ez is jó: a hangadók uralta kör bármelyik nagyobb kvucában előfordul; Kivszánál gyakran a státusz és a „ki a menő” áll mögötte.”`
- Címkék: VÉTÓLISTÁS (kulcs) / LÁTHATÓ SZÖVEG / BUILD-INPUT (az M3.2-EGY-01 spec, :595, „az aktualizált megoldókulccsal” hivatkozik rá)
- Runtime-kérdés: működik-e két helyes opció a H5P Multiple Choice „Single Choice (Radio Buttons)” módjában – runtime acceptance, nem állítom.

### ERT-28 – Az M5.2 SLIDE 8 ✅-ja
- Hatáskör: SZEREP: M5 szerzője + értékelési felelős
- Olvasat (értelmezés, nem átvezetés; a jóváhagyó erősítse meg): a döntés „feladat–kvuca–módszer–cél” fordulata a négy elem meglétét jelenti, sorrendjük a tanított lánc (SLIDE 7 :545; MAN:80).
- A ✅ (M5.2:574):
  - OLD: `* **„Először a nevelési célt találom ki, és ahhoz választok módszert, ami elvezet hozzá.”** ✅`
  - NEW: `* **„A feladatból indulok ki: megfogalmazom a nevelési célt, megnézem, milyen a kvucám, és ehhez választok módszert, ami elvezet a célhoz.”** ✅`
  - A pozíció (2. opció) marad, a jelentés változik.
- Visszajelzés (M5.2:581):
  - OLD: `> hanem **célhoz választott módszer** egy konkrét kvucával.”`
  - NEW: `> hanem a feladatból megfogalmazott **célhoz** és a konkrét **kvucához** választott **módszer**.”`
- A disztraktorok és a visszajelzésük maradnak.
- HUB-M5:207:
  - OLD: `erősíteni az M5.2 üzenetét („cél az első”);`
  - NEW: `erősíteni az M5.2 üzenetét („feladat → cél → kvuca → módszer”: a módszer a cél és a kvuca után jön);`
- KAPU-M5:312:
  - OLD: `a sorrend-üzenet (M5.2 „cél az első”) erősítendő;`
  - NEW: `a sorrend-üzenet (M5.2: „feladat → cél → kvuca → módszer”) erősítendő;`
- Címkék: VÉTÓLISTÁS (answer key szemantikája) / LÁTHATÓ SZÖVEG
- Megjegyzés: a SLIDE 7 és a SLIDE 8 így közel azonos láncot mér. Ez nem hiba, de a szerző döntse el.

### ERT-30 – Az M5 kapu Q12 C opciója
- Fájl: KAPU-M5:269
- Hatáskör: SZEREP: értékelési felelős + modulgazda
- OLD: `- C) ✅ Először **közösen eléneklik**, a következő pénteken **fejből idézik fel**, és a dal **több héten át röviden visszatér**.`
- NEW: `- C) ✅ Először **közösen elénekeljük**, a következő pénteken **fejből idézzük fel**, és a dal **több héten át röviden visszatér**.`
- Címkék: VÉTÓLISTÁS (a kulcsopció szövege; a ✅ jelentése változatlan) / LÁTHATÓ SZÖVEG
- Indoklás: azonos nézőpont, mint az A és a D „mi”-alakja. A :274-es indok és a :277-es visszajelzés igaz marad.

### PRG-15 b – Az M5.1 SLIDE 4 1. és 4. helyzete (a kulcs marad: formális)
- Hatáskör: SZEREP: szakmai lektor / M5 szerzője
- Indoklás: a tanított definíció (M5.1:363) szerint a formális „iskola, tanterv, jegy, kötelező”, a nonformális (:369) a „suli rendszerén kívül vagy mellett” zajlik; a mostani két helyzet a „mellett” kategóriába esne.
- Az M5.A határeset-kártyái (:79, :81, :251, :262, :570) szándékosan maradnak.
- Cserék:
  - :439 OLD `1. „Szavalóverseny az iskolában, zsűri pontoz, oklevelet kapsz.”` → NEW `1. „Irodalomórán elszavalod a tanterv szerinti verset, és a tanár jegyet ad rá.”`
  - :442 OLD `4. „Suli utáni matekszakkör, ahol a tanár plusz feladatokat ad, és dolgozat lesz belőle.”` → NEW `4. „Matekórán a tananyagból dolgozatot írtok, és jegyet kapsz rá.”`
  - :448 OLD `1. formális (iskolai, pontozott, értékelés)` → NEW `1. formális (tanóra, tanterv, jegy)`
  - :451 OLD `4. formális (suli, tanár, értékelés)` → NEW `4. formális (tanóra, tanár, jegy)`
  - :430 OLD `(pl. „1. helyzet – Szavalóverseny”)` → NEW `(pl. „1. helyzet – Szavalás irodalomórán”)`
- Hiány: az 1. és a 4. helyzethez nincs visszajelzés-sor (a :455 fejléce csak a 2., 3., 5., 6.-at nevezi). Opcionális pótlás: `* 1. helyzet: „Formális (tanóra, tanterv, jegy).”` és `* 4. helyzet: „Formális (tanóra, tanár, jegy).”`, a fejléc igazításával.
- Címkék: LÁTHATÓ SZÖVEG. A ✅ nem változik, ezért nem vétólistás.

---

### D-19 (a)(c) – Kimeneti célok (TERM-7 `F`: „Modulgazdai/értékelői jóváhagyás”)

### D19a – Az M5 hub célmondatainak szűkítése
- Hatáskör: SZEREP: modulgazda + értékelési felelős; a célkitűzésről a projektgazda (D-19 irány)
- HUB-M5:18:
  - OLD: `és saját szavaiddal **elmagyarázod**, hogyan tanulnak tényleg a hanihok (**gyakorlás, aktív felidézés, időben elosztott gyakorlás**).`
  - NEW: `és **felismered**, hogyan tanulnak tényleg a hanihok (**gyakorlás, aktív felidézés, időben elosztott gyakorlás**), és ezt a saját peuláidban **alkalmazod**.`
- HUB-M5:32:
  - OLD: `3. **Elmagyarázza az alap tanulástan-fogalmakat és alkalmazza őket a saját peuláira.**`
  - NEW: `3. **Felismeri az alap tanulástan-fogalmakat, és alkalmazza őket a saját peuláira.**`
- HUB-M5:33:
  - OLD: `* Saját szavaival el tudja magyarázni a **gyakorlás, aktív felidézés és időben elosztott gyakorlás** fogalmakat, és 2–3 konkrét ötlete van`
  - NEW: `* Felismeri a **gyakorlás, aktív felidézés és időben elosztott gyakorlás** elemeit egy peulatervben, és 2–3 konkrét ötlete van`
- Címkék: LÁTHATÓ SZÖVEG. A kapu, a kulcs és a küszöb nem változik.
- Nem ellenőriztem: a Program terv és a manifest tükörszövegét.

### D19c – Az M2 hub kimeneti célja
- Fájl: HUB-M2:34
- Hatáskör: SZEREP: projektgazda + értékelési felelős; QA: helyi ideológiai felelős (HUM-SOMER-01) és DPO (M2)
- OLD: `hogyan akar **személyes példát mutatni** a kvucájának (a döntési fa egy ágát végigjátszva), a másik kettőt feltáró módon megismeri.`
- NEW: `hogyan akar **személyes példát mutatni** a kvucájának (a saját vagy egy kitalált madrih példáján, a döntési fa egy ágát végigjátszva), a másik kettőt feltáró módon megismeri.`
- Együtt mozgó hely: KAPU-M2:239 sablonsora (M2-HUB-MUNK-01, build út) – NEM OLVASTAM BE, az OLD hiányzik
- Címkék: LÁTHATÓ SZÖVEG. Az R3 szintjei és a küszöb nem változnak.

---

### D-16 – Vétó/QA-kérdés az értékelési felelősnek (ERT-38: a projektgazda a (ii) olvasatot rendelte el)

- Kérdés: „Elfogadja-e az értékelési felelős (vétó/QA: programvezető), hogy a Z.4 »Teljesítve« alsó határa a beadás egészének értelmezhetősége? Ennek megfelelően a Z.4:343 zárójele (»a három szakaszban; …«) és a MAN:112 »előírt mezőiben« fordulata módosul, a háromrészes szerkezet formatív útmutató marad, a passz lehetséges.”
- Vétó esetén a tétel REOPENED.
- A (b) részkérdés (passzjelölés, a mentor első lépése üres szakasznál) az értékelési felelősé a DPO-val; a (ii) olvasatban nagyrészt tárgytalan.
- A Z.4-et nem olvastam be, ezért OLD/NEW nincs.

### ERT-19 – SIGNOFF lap és előzetes tájékoztató (tervezet)

**Aláírási lap mezői:**
- tétel: ERT-19 (HUM:689, `F`);
- tartalom: az ÉN a középpont, a „legalább 3 kör” három további réteg (szigorítás);
- érintett helyek a G9 kimenete szerint, nem friss olvasásból: KAPU-M2:37 és :218, M2.1:477, M2.A:343, HUB-M2:25, és a plan-M2:319–321 listája (az A.1 példájából kikerül az ÉN; az R1 három kört kér az ÉN-en kívül; a D-sablonban az ÉN a középpont);
- aláírók: M2 modulgazda + értékelési felelős; dátum: [üres];
- a tájékoztató közzétételének helye és ideje: [üres];
- hatálybalépés: az első kohorsz, amelynek M2 kapuja a közzététel után nyílik; nem visszamenőleges;
- vétó/QA: értékelési felelős.

**Tájékoztató (LÁTHATÓ SZÖVEG, VÉTÓLISTÁS küszöb):** `Változás az M2 kapufeladatban ([kohorsz]-tól): az identitástérképen az ÉN a középpont; a „legalább 3 identitás-kör” az ÉN körüli három további kört jelenti (pl. család, zsidóság, Somer vagy más közeg). A korábban leadott munkákra ez nem vonatkozik.`

### D-10 (c)(d) – Feltárásmentes pótlás (N-9)

- Hatáskör: SZEREP: értékelési felelős + programvezető, Memuna-vétóval
- Szabálytervezet (helye: M1 KAPU:27 és a GYV-11-es tükörhelyek; ezeket nem olvastam be): `Ha egy beadás gyermekvédelmi feltárást tartalmaz, a tanuló feltárásmentes pótlást adhat le: ezt a képző kézzel nyitott, külön próbálkozásként nyitja meg, és nem számít bele a próbálkozási keretbe; a feltárást tartalmazó próbálkozás a kapueredménybe nem számít bele (GYV-11).`
- Ez a (c) (i) opció, a Z.4:359 mintája; (d): a feltárást tartalmazó próbálkozás nem számít.
- Címkék: VÉTÓLISTÁS (próbálkozásszám, completion)
- Nem része ennek a csomagnak: a tárolt példány korlátozása és törlése (a, b, e, f; Memuna + DPO). A Moodle-mechanika (felhasználói felülbírálás vagy plusz próbálkozás) runtime-bizonyítékot igényel.

---

### (1) Amit nem tudtam ellenőrizni / ami hiányzik
- **Egyediség:** nem greppeltem a KAPU-M3:318 kiegészítés-horgonyát, a KAPU-M3:326 Alapszint teljes horgonyát, a KAPU-M7:315 és :241 horgonyát, a KAPU-M6:399 „fiktív esetet…” horgonyát, a KAPU-M5:286 sorát, az M3.2:666 és az M5.2:581 horgonyát. A beépítés előtt mindet Greppel kell ellenőrizni.
- **D-19 (c):** a KAPU-M2:239 sablonsor szövege; a D-19 (a) Program terv- és MAN-tükörszövegei.
- **ERT-19:** a plan-M2:319–321 és az M2-es helyek friss szövege (G9-idézetből dolgoztam).
- **D-10 (c)(d):** a Z.4:359 mintája és az M1 KAPU:27 mostani szövege.
- **D-16:** a Z.4:343, :347, :353 és a MAN:112 szövege.
- **ERT-32:** az M6.B:48 környezete (melyik blokk), és hogy az M6 hub vagy a Program terv tükrözi-e az R4 „Oké” horgonyát.
- **ERT-23:** hogyan viselkedik két helyes opció a H5P MC radio módban (runtime).
- **ERT-42:** az ADV-ben az adatvédelmi stop eljárásának helye (DPO).

### (2) Ellentmondások a kánonban / a bemenetek között
1. **Sorszám-elcsúszás:** a kért M3.4:837 ma a 808. sor, a kért KAPU-M7:93 (Q3) ma a 94. sor.
2. **ERT-23, 2. item:** a G9 és a kért irány szerint két kulcs, de az M3.2:328 tanított példája egyetlen Kivsza-kulcsot támaszt alá.
3. **ERT-43:** az R1 2-es szint szigorítása után az R1 1-es szint (:278) nem fedi le a csak időkeretet tartalmazó célt; együtt mozgó cserét javasoltam.
4. **ERT-32 „felnőtt” szava:** kétértelmű (a jelen lévő felelős felnőtt vagy a Memuna). Az M6.4:938–940 szerint fogalmaztam; a Memuna erősítse meg.
5. **GYV-8 hatóköre:** a G3 (2)(b) opciója tágabb a GYV-8 szövegénél. Én szűken vettem át; a tágítás Memuna-döntés.
6. **ERT-42:** az R8 2-es szintjéről csak az adatvédelmi stoppal egy menetben vehető ki az adat-kritérium, különben az adatvédelem gyengülne.
7. **M7.4-MUNK-01 spec:** a „nem kerül bele új útmutató szöveg” kikötése miatt a GYV-9 mondat felvétele kifejezett spec-módosítás (BUILD-INPUT).
8. **M5.1 SLIDE 4:** az 1. és a 4. helyzethez ma sincs visszajelzés-sor.

## Kiegészítés a célzott QA után (`9788c05`)

A `8bb4d7d` célzott QA-ja (QA17; riport: `2026-10-13 Célzott QA – D-csomagok átvezetése (8bb4d7d), AP-2026-10-13-01.md`) után ehhez a szerephez került tételek. A javasolt szöveg helyett itt a döntési kérdés áll; a javító commit nem implementálta őket.

- **M7:QA17-ERT-1b:** legyen-e mentori kulcs-átbeszélés az M7 kapukvíz után, és ha igen, mikor: csak a tanuló utolsó próbálkozása után, vagy további kézi próbálkozás csak validált itemváltozattal? A `8bb4d7d` ezt döntés nélkül beírta; a `9788c05` törölte (M7:QA17-ERT-1). A Review options mátrixa, a ≥12/14 küszöb és a Q13 blokkoló státusza nem változik.
- **KANON:QA17-BIZT-3b (a projektgazdával):** a D-16 a lezárt táblában maradjon-e (a 14. szakasz bevezetője szerint az ERT-38/ERT-3 jobb oszlopa utólagos vétó/QA), vagy a nyitott táblába kerüljön (a döntési csomag a D-16 (a)/(b) részét az értékelési felelősnek adta)? A D-16 vétó/QA oszlopába az értékelési felelős visszakerült (KANON:QA17-BIZT-3). Addig a Z.4 mércéje sem nem enyhül, sem nem szigorodik.
- **KANON:QA17-ERT-3 (QA a projektgazda build-spec döntéséhez):** az LMS-M4-05 rubrikájának Grade type-ja, Maximum grade-je és a három szint pontja (rejtve, küszöb- és completion-hatás nélkül; a Moodle-rubrikához pontérték kötelező).
