# RT-2 — M0+M1 runtime-ellenőrzőlista (célkörnyezet)

**Állapot:** minden sor `IMPLEMENTATION_TEST_REQUIRED`. Ez a lista egy sort sem igazol.

- `RUNTIME_VERIFIED` csak a célkörnyezetben futtatott, dátummal, pontos verzióval és bizonyítékkal rögzített eredményből lehet (RA:31, :174; RR staging-szabály 5.).
- A teszt az a környezet, amelyben a pilot fut, vagy ugyanazokkal a verziókkal futó másolat.
- Szintetikus tesztadat kell, valódi tanulói adat nem (RR staging-szabály 3.).

**Források:**
- `LMS – H5P runtime acceptance.md` (RA) és `LMS – activity manifest.md` (MAN), a pilot forrásában (`main@213a4c5`).
- A (+) jelű tesztpontok csak a next-version jelöltben (`e67cce5`) vannak meg. Ezek nem tartalomváltozások, a pilotban is futtathatók.
- A döntési csomag RT-2 bejegyzése.

## 0. Előfeltételek

| # | Mit | Bizonyíték |
|---|---|---|
| 0.1 | Environment record kitöltve (RA:5–27), legalább: Moodle; H5P core/plugin; `enablesavestate` és `savestatefreq` értéke; Course Presentation; Multiple Choice; Single Choice Set (ha használt); Drag and Drop (M1.2); böngésző- és eszközmátrix | képernyőkép vagy export, dátum |
| 0.2 | Tesztfiókok: tanuló-A (A csoport), tanuló-B (B csoport), mentor-A (nem szerkesztő tanár, A csoport), mentor-B (B csoport), képző (szerkesztő tanár). Valódi madrih nem. | fióklista szerepekkel és csoportokkal |
| 0.3 | Minden M0/M1 activity build-ID-ja és `cmid`-je rögzítve: LMS-M0-01…06, LMS-M1-01…07 (RR staging-szabály 4.) | táblázat |
| 0.4 | Dátumfüggő activityk: az LMS-M0-03 az „M0.A után nyílik dátummal”, az LMS-M1-03 az „M1.A után nyílik”. A dátum beállítva; tanulói nézetben nincs helykitöltő (PILOT-2, G4b) | képernyőkép tanulói nézetből |

## 1. M0

| ID | Activity | Lépések | Elvárt eredmény | RA / RT |
|---|---|---|---|---|
| M0-1 | LMS-M0-01…04 (H5P-C) | Beállítás-visszaolvasás | „Enable attempt tracking” = Yes; Grade type: Point; „Grade to pass” üres; a completion kizárólag „Receive a grade”; Course Presentationnél „Hide summary slide” = No (MAN §1 H5P-C) | RA 9 · RT-P0-09 |
| M0-2 | LMS-M0-01 | tanuló-A: (a) megnyitás és végiglapozás az összefoglaló dia nélkül; (b) végigvitel az összefoglaló diáig | (a) nincs completion; (b) Moodle Activity completion beáll; az LMS-M0-02 csak (b) után nyílik | RA 9 (a)–(c) · RT-P0-09; RA 1 · RT-P0-01 |
| M0-3 (+) | LMS-M0-01 | tanuló-B: az összefoglaló dia elérése úgy, hogy minden dia megválaszolatlan | rögzítendő verzióval: keletkezik-e grade, beáll-e a completion (negatív eset; `M0:ERT-2`) | RA 9 negatív eset · RT-P0-09 |
| M0-4 | M0.2 SLIDE 3 (2. helyzet) | tanuló-A, képernyőolvasóval is | a válaszonkénti kiemelt visszajelzés megjelenik; elolvasható, mielőtt a feladat továblép (SC 2.2.1) | RA 14 · RT-P0-14 |
| M0-5 | M0.1, M0.3, M0.4 helyes válasz nélküli vélemény- és helyzetkérdései | tanuló-A, minden opció kipróbálva | egyetlen őszinte választ sem jelöl hibásnak; nem torzítja az activity pontszámát | RA 14 · RT-P0-14 |
| M0-6 | LMS-M0-01…04 tanuló-lokális szöveges lépései (MAN:39–42) | tanuló-A: szöveg beírása minden beviteli elembe; átlépés egy nem első diára; várakozás a `savestatefreq`-nél tovább; kijelentkezés; új munkamenet; újranyitás. Utána képző: a próbálkozás-riport. | csak akkor értékelhető, ha bekapcsolt „Save state” mellett az activity az utolsó diánál nyílik; ha nem, ismétlés. Siker: a szöveg nem töltődik vissza, a riportban nincs tanulói szöveg, a completion nem függ tőle. Beviteli elem nélküli lépésnél ezt kell rögzíteni. | RA 24 · RT-P0-24 |
| M0-7 | LMS-M0-05 Bemutatkozó fal (FORUM-C) | ⚠️ **Valódi tanulónak nem nyitható meg az ADV-6 (DPO) döntéséig (PT:228).** Tesztfiókkal: 1 új téma + 1 válasz; a completion beállítása | a completion a manuálisan beállított fórum-feltétellel áll be; rögzítendő, hogy a saját témára adott válasz is beszámít (MAN:43); a láthatóság egyezik a tájékoztatóval (FORUM-C, ADV:120) | MAN:43, :155 |
| M0-8 | LMS-M0-06 (QUIZ-D) | tanuló-A: mind a 7 item megválaszolva, beküldés | completion „attempt submitted”; nincs cut-score; több próbálkozás engedélyezett | MAN:44 |
| M0-9 (+) | LMS-M0-06 | tanuló-B: minden item üresen, beküldés | rögzítendő verzióval: beáll-e a completion (az M0 hub §5 „Beállítás” ágának igazolása) | RA 25 · RT-P0-25 |
| M0-10 | M0 → M1 unlock | tanuló-A: az M0-1…M0-8 után | az LMS-M1-01 csak „M0 complete” után nyílik (MAN:45, :155); hiányzó elemmel (pl. fórumposzt nélkül) zárva marad | RA 1 · RT-P0-01 |

## 2. M1

| ID | Activity | Lépések | Elvárt eredmény | RA / RT |
|---|---|---|---|---|
| M1-1 | **LMS-M1-01 SLIDE 5 — az N-M1-04 alapértelmezése** | Megnézni, van-e beviteli elem a SLIDE 5-ön | **Alapértelmezés: nincs beviteli elem**, saját jegyzetes út (HUM §12; MAN:45; RA 24). Ezt kell rögzíteni (RA 24: „Ha a lépésnek nincs beviteli eleme, ezt kell rögzíteni”). | RA 24 · RT-P0-24 |
| M1-1b | LMS-M1-01, csak ha a build beviteli elemet használ | az M0-6 eljárása, kiegészítve: mentor-A és képző hozzáférése a próbálkozás-riporthoz és a mentett állapothoz | siker csak akkor, ha a szöveg sem a riportban, sem a mentett állapotban nem marad meg, és tanári vagy mentori fiókkal sem érhető el. Ha nem: a beviteli elemet ki kell venni, a lépés a saját jegyzetes úton fut. A DPO QA ettől függetlenül nyitott. | RA 24 · RT-P0-24 |
| M1-2 | LMS-M1-01…04 | tanuló-A: végigvitel az összefoglaló diáig, a SLIDE 5 üresen | a completion a SLIDE 5 nélkül is beáll (nem completion-feltétel); a downstream a Moodle completionhöz kötött | RA 9 · RT-P0-09 |
| M1-3 | M1.1–M1.2 SLIDE 1–2 pontozatlan választói | tanuló-A, minden opció | nem jelöl hibásnak; nem torzítja a pontszámot | RA 14 · RT-P0-14 |
| M1-4 | LMS-M1-02 (M1.2) húzásmentes út | tanuló-B, csak kattintással vagy koppintással, mobil portrait nézetben | végigvihető; ugyanaz a visszajelzés; a completion beáll; a célméret mérve | RA 13 · RT-P0-13 (G5b: a hozzáférhetőségi gazda pre-flightja is) |
| M1-5 | LMS-M1-07 (TEXT-C, mini-SBI) | ⚠️ **Valódi tanulónak az ERT-12 döntése és a DPO-jóváhagyás előtt nem nyitható meg** (PILOT-BLOCKER). Tesztfiókkal: beállítás-visszaolvasás és beküldés | puszta szövegmező, szerkesztő és feltöltés nélkül; a „Required” üres beküldést nem enged; a csak szóközből álló válasz viselkedése rögzítve; újrabeküldésnél felülír, a completion megmarad; „Show analysis page” ki; a tanulói `mod/feedback:viewanalysepage` Prohibit; a just-in-time tájékoztató látszik mobilon és képernyőolvasóval | RA 6 · RT-P0-06 |
| M1-6 | LMS-M1-07 és LMS-M1-05 láthatósága | tanuló-A és tanuló-B beküld; mentor-A, mentor-B, képző olvas; közvetlen URL-próba más csoport válaszára | mentor-A csak az A csoportot látja, mentor-B csak a B-t; URL-lel sem jut át; tanuló nem lát más tanulót; nincs csoport nélküli `mod/feedback:viewreports` mentorfiók; a beküldési értesítés ki. A szerkesztő tanári és menedzseri láthatóság rögzítendő (DPO-kérdés: ADV-1). | RA 15 · RT-P0-15 |
| M1-7 | LMS-M1-05 (ASSIGN-M) beállítások | visszaolvasás | Grade type: Point; Maximum grade = 8; Grade to pass = 5 (MAN:50); a rubrika beállítva | RA 1 · RT-P0-01 |
| M1-8 (+) | LMS-M1-05 rubrika tanulói nézete | tanuló-A: beadás előtt; értékelés után | a rubrika a beadás előtt látható („Allow users to preview rubric…” = 1); értékelés után soronként a szint és az értékelői megjegyzés („Show remarks to those being graded” = 1); a beállított érték és a verzió rögzítve | RA 26 · RT-P0-26 |
| M1-9 | LMS-M1-06 (GATE-CP) negatív eset | tanuló-A rubrikája 0/1/2/2 (= 5/8); a stáb „Még nem teljesítve” értéket ír | az „M1 megerősítve” feltétel teljesül (a következő tanulási rész nyílik), az „M1 complete” nem (a következő éles kapu, LMS-M3-05 zárva); completion „complete, fail” | RA 8 · RT-P0-08 |
| M1-10 | LMS-M1-06 állapotmátrix | két tanulói fiókkal: nincs érték / „Még nem teljesítve” / „Teljesítve” / javítás utáni átírás / önkéntes gyengébb újrapróba / a két feltétel külön / tanulói és stáb-láthatóság | az RA 8 :59–67 szerint; a Grade history-ban visszakereshető; beállítás-visszaolvasás az RA :71 szerint (kételemű skála, sorrend, Grade to pass = 2, marking workflow és anonim beadás ki, Feedback comments be, nem rejtett és nem zárolt, a tanuló nem tud beadni, completion „Receive a grade”) | RA 8 · RT-P0-08 |
| M1-11 | LMS-M1-05 próbálkozások | tanuló-B: első, nem teljesítő beadás; javító beadás az F-peula előtt (negatív); képzői nyitás az F-peula után | a javító beadás az F-peula előtt nem indul; utána a képző nyitja; (+) „Grant attempts” = „Manually”, „Allowed attempts” = „Unlimited” (csak a jelöltben: `M1:QA-IMPL-2`, MAN §1 ASSIGN-M és M1 KAPU; a `main`-ben ez a beállításnév nincs rögzítve, ott a tényleges értéket kell feljegyezni); a legjobb megerősített eredmény számít, a későbbi gyengébb önkéntes beadás nem írja felül; rögzítendő, hogyan kerül az F-peula jelenléte a Moodle-be, és tanulónként állítható-e a javító határidő | RA 19 · RT-P0-19 |

## 3. A pilothoz szükséges, de az RT-2-n kívül eső sor

| ID | Mit | Elvárt | RA / RT |
|---|---|---|---|
| X-1 | „Segítség és kapcsolatok” blokk, tanuló-A nézetből | a négy szerep szerinti kontakt kitöltve (technikai, tanulási/program, mentor, Memuna); a Memuna és a helyettese a többitől külön; nincs helykitöltő (PILOT-3) | RA 17 · RT-P0-17 (RT-1) |

## 4. Rögzítés

- **Soronként rögzítendő:** dátum, tesztelő (szerep), Moodle-, H5P- és content type-verzió, böngésző és eszköz, `cmid`, eredmény (siker / sikertelen / nem értékelhető), bizonyíték (képernyőkép, log vagy issue-link).
- **Az RA „Teszt-állapot” táblája** (RT-P0-01, -06, -08, -09, -13, -14, -15, -17, -19, -24; (+) -25, -26) csak a tényleges eredménnyel frissíthető, külön engedélyezett lépésben.
- **Sikertelen eredménynél** a BSPEC-sor vagy a mechanizmus újranyílik (RA 11, D-g minta), és a sor nem igazolt.
- **A DPO (ADV-E1) és a Memuna (GYV-24)** ezekre az eredményekre hivatkozik; a teszt az ő jóváhagyásukat nem helyettesíti.
