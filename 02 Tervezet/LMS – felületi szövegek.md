# LMS – felületi szövegek

> **Állapot:** projektgazdai és szerzői döntés, 2026-11-08 (`Emberi jóváhagyás szükséges.md` 22. szakasz; a
> projektgazda a tananyag szerzője, D-097). A szövegek a vak tanulói és mentori tesztek (2026-10-26 – 2026-11-08)
> visszajelzéséből születtek, és a tesztelt kurzusváltozatban így szerepeltek.

Ez a fájl a Moodle-felület azon szövegeit rögzíti, amelyeket a leckék nem tartalmaznak, de a beépített kurzus a
tanulónak vagy a mentornak megmutat: a kérdőívre mutató sorokat, a válaszok visszajelzésének első szavait, a mentori
címkéket és a képek alt-szövegét. A kurzus építése ezeket innen, szó szerint veszi át; új felületi szöveg csak ide
kerülhet. A szögletes zárójeles rész („[kérdések]”, „[címke]”) helyére az építés a kérdőív nevét, illetve a lecke
saját címkeszavát írja.

## 1. Tanulói felületi szövegek

### 1.1 A lecke utáni kérdőívre mutató sorok

- **UI-KÉRDŐÍV-1** (ahol a lecke egy kérdését a lecke utáni kérdőív kérdezi): ➜ Erre a kérdésre a lecke után következő kérdőívben válaszolsz (a kurzusoldalon, közvetlenül a lecke alatt találod).
- **UI-KÉRDŐÍV-2** (ugyanez, ha a kérdés szövege a sor után következik): ➜ Erre a kérdésre nem itt, hanem a lecke után következő kérdőívben válaszolsz (a kurzusoldalon, közvetlenül a lecke alatt találod):
- **UI-KÉRDŐÍV-3** (a lecke „A következő lépésed” diáján, ha a leckéhez kérdőív tartozik): ➜ A kérdőív kérdéseire a kurzusoldalon, közvetlenül a lecke alatt álló „[kérdések]” kérdőívben válaszolsz; amit a lecke csak magadnak kér, azt nem kell beadnod. A fenti következő lépés a kérdőív után jön.

### 1.2 Az önellenőrző kérdések visszajelzésének első szavai

- **UI-JÓ-1** (az egyetlen jó válasz visszajelzése előtt): ✅ Igen, ez a jó válasz.
- **UI-JÓ-2** (több jó válasz közül egy visszajelzése előtt): ✅ Igen, ez is a jó válaszok közé tartozik.
- **UI-NEM-1** (egy nem jó válasz visszajelzése előtt, ha az maga nem mondja ki): ✗ Nem ez a jó válasz.
- **UI-NEM-2** (ugyanez, ha több jó válasz van): ✗ Ez nem tartozik a jó válaszok közé.
- **UI-TÖBB-1** (a több jó választ kérő önellenőrzés fölött): Több jó válasz is van. Döntsd el magadban, melyeket jelölnéd, aztán nyisd ki mindegyiket: így látod, igazad volt-e.

### 1.3 A címkekereső (M1.2) mondatonkénti visszajelzése

- **UI-CÍMKE-1** (minden címkét megtalált): ✔ Pontosan. Ebben a mondatban a címke: [címke].
- **UI-CÍMKE-2** (nem minden címkét talált meg): Ebben a mondatban a címke: [címke].
- **UI-CÍMKE-3** (az 5. mondat, amelynek saját visszajelző sora van): ✔ Pontosan.

### 1.4 Egyéb felületi szövegek

- **UI-ÚJRA-1** (a lecke szövegét másképp elmondó narráció leiratának lenyitható címe): A történet még egyszer, másképp elmondva
- **UI-KÁRTYA-1** (a párbeszédkártyák kör végi összesítője): Helyes kártyák ebben a körben:
- **UI-KÁRTYA-2**: Még gyakorlandó kártyák ebben a körben:
- **UI-KÁRTYA-3**: Végleg megtanult kártyák (@max-szor egymás után helyesen):

## 2. Mentori szövegek

A mentori sorok a tanulónak rejtve maradnak; a mentor a kapupont („megerősítés”) leírásában látja őket.

### 2.1 Címkék

- **UI-MENTOR-1** (a kapupont „Teljesítve” feltétele előtt): Mentori szempont – a „Teljesítve” feltétele:
- **UI-MENTOR-2** (a visszajelzés módja előtt): Mentori szempont – a visszajelzésben:
- **UI-MENTOR-3** (a döntéshozók előtt): Mentori szempont – ki dönt:
- **UI-MENTOR-4** (a mentornak szóló forrásmondat előtt egy beadandó leírásában): Mentori szempont:

### 2.2 Hol találja a mentor a kritikus kérdést

- **UI-MENTOR-5** (LMS-M7-09): A Q13 a kvíz „Értékelések” jelentésében a „K. 13” oszlop, a próbálkozás saját kérdéssorrendjétől függetlenül.
- **UI-MENTOR-6** (LMS-M3-07): A Q2, Q4, Q7 és Q9 a kapukvíz „Értékelések” jelentésében a „K. 2”, „K. 4”, „K. 7” és „K. 9” oszlop; a próbálkozás áttekintésében ugyanez a 2., 4., 7. és 9. kérdés.

### 2.3 Átvételi szabályok

- A kapupont leírásában a manifest „Teljesítve =” cellája áll, szó szerint, két eltéréssel: a sorazonosítók
  (`LMS-…`) helyén az activity manifest szerinti neve áll, és a fejlesztői dokumentumokra mutató zárójeles hivatkozások
  kimaradnak.
- Egy kapu vagy egy beadandó mentornak szóló forrásmondata (a kapufájlból vagy a manifest megjegyzés-cellájából) szó
  szerint, egy sorban áll a 2.1 címkéje alatt.

## 3. A képek alt-szövege

Ahol a kép leírása nem a lecke saját szövege, a képernyőolvasó ezt az alt-szöveget olvassa fel. A dekoratív kép
alt-szövege üres.

- **M0.4-ILL-01**: Egy madrih telefonnal a kezében; körülötte a négy online felület: csoportchat-buborékok, insta-sztori kör, privát üzenet és Moodle-komment.
- **M0.4-POSZ-01**: Nyomtatható poszter: „3 egyszerű szabály – dugma isit online”: 1. „Amit nem olvasnék fel nagykörben, azt nem írom le privátban.” 2. „Gyermekvédelmi red flag online is red flag.” 3. „Nem vagyok éjjel-nappali ügyelet.”
- **M1.1-IKO-01**: dekoratív kép, üres alt-szöveg.
- **M1.1-ILL-02**: dekoratív kép, üres alt-szöveg.
- **M1.2-IKO-03**: dekoratív kép, üres alt-szöveg.
- **M1.3-EGY-01**: Két verziócímke: „1. verzió – címke” (címke-ikonnal) és „2. verzió – SBI-szerű” (S, B, I betűjelekkel).
- **M1.3-VID-01**: A videó állóképe: két fiatal madrih áll egymással szemben egy világos teremben; a lány magyaráz, a fiú elgondolkodva hallgatja. Mellette a cím: „Bunkó voltál” vs. „Amikor ma…”, alatta a két verzió felirata: „1. verzió – címke”, „2. verzió – SBI-szerű”.
- **M2.2-IKO-01**: dekoratív kép, üres alt-szöveg.
- **M2.4-VID-01**: Videó-nyitókép: „Mit érzel? Mit csinálsz?” Három doboz a narráció kulcsmondataival, a hanih üzenetétől a „segítő madrih lenni” gondolatig; a narráció a kép alatt olvasható.
- **M3.1-IKO-01**: dekoratív kép, üres alt-szöveg.
- **M3.2-IKO-01**: Három kvuca-ikon felirattal: pillangó – Parparim, bárány – Kivsza, bálna – Leviatán.
- **M3.2-DIA-01**: Két profilkártya: Parparim (kb. 6–9 év) és Kivsza (kb. 10–12 év), pontokba szedve, egy-egy tipikus jelenettel. A szöveg a kép alatt is olvasható.
- **M3.2-DIA-02**: Leviatán profilkártya (kb. 13–17 év), pontokba szedve, egy fiatalabb és egy idősebb tipikus jelenettel. A szöveg a kép alatt is olvasható.
- **M3.2-DIA-03**: Három kulcsszókártya a kvucák ikonjával: Parparim – JÁTÉK & BIZTONSÁG, Kivsza – STÁTUSZ & POÉN, Leviatán – IDENTITÁS & FELELŐSSÉG.
- **M3.3-VID-01**: Videó-nyitókép: „Mit ígérhetek egy hanihnak?” Két doboz a narráció mondataival: egy hanih titoktartást kér, és a lecke célja (felelős lépés, red flag).
- **M3.4-IKO-01**: Ikon: egy madrihot jelző figura és egy kvucát jelző csoportfigura, köztük szaggatott határvonal.
- **M3.4-DIA-01**: Három témablokk DO és DON’T dobozzal: Kommunikáció & online; Kapcsolatok & kedvencek; Dohány & alkohol – ken kontra magánélet. A szöveg a dián is olvasható.
- **M3.4-VID-01**: Videó-nyitókép: „Meddig mehetek el madrihként?” Két doboz: hol a határ a bizalmi kapcsolat és a „nem oké” között, és „Azzal is tanítasz, amit nem csinálsz.”
- **M4.1-DIA-01**: Három ikon egymás alatt, vonallal összekötve: álló alak – Testtartás, szem – Tekintet, helyjelölő tű – Térfoglalás.
- **M4.1-VID-02**: A videó állóképe: ugyanaz a fiatal madrih háromféle kiállásban egymás mellett: papírjába nézve, idegesen összekulcsolt kézzel, egyik lábát emelve, végül lazán és egyenesen állva. Mellette a kérdés: „Melyik madrihra figyelnél szívesebben?”, és a három felirat: 1. Jegyzetbe bújó madrih, 2. Ideges topogó madrih, 3. Nyitott, stabil madrih.
- **M4.2-ILL-01**: Chatbuborék egy személyikon mellett: „Nagyon ideges vagyok, hogy holnap peulát kell tartanom…”, alatta gépelést jelző három pont.
- **M4.2-ILL-02**: Két fogalomdoboz három-három kulcsmondattal: Aktív hallgatás (fejhallgató) és Visszatükrözés (körkörös nyíl), alul a „Nem terapeuta vagy…” zárómondat.
- **M4.2-ILL-03**: Pipás lista „Ha idáig eljutottál, már:” címmel: lezáró és támogató reakciók, a visszatükrözés gyakorlása, a saját szereped átgondolása.
- **M4.2-IKO-01**: dekoratív kép, üres alt-szöveg.
- **M4.3-ILL-01**: Rajz: egy madrih áll a székeken ülő kvuca előtt, buborékban: „Na, értitek?” A csoport tagjai szótlanul, értetlen arccal néznek vissza.
- **M4.3-DIA-01**: Négy színkódolt doboz definícióval és példával: Nyitott, Zárt, Tisztázó és Irányító kérdés. A szöveg a dián is olvasható.
- **M4.4-ILL-01**: Rajz: egy madrih áll a körben ülő kvuca előtt, gondolatbuborékban: „Oké, 45 mp-em van, hogy ne veszítsem el őket…” A hanihok őt figyelik.
- **M4.4-DIA-02**: „Peulabemutató =” öt ponttal: rövid (max. 45 mp) bevezető; miről szól; miért pont ennek a kvucának; mit fogtok csinálni; mit vigyenek haza. Kiemelve: érthető, rövid meghívás a peulába.
- **M4.4-DIA-03**: Peulabemutató-sablon öt számozott kérdéssel és egy-egy példamondattal: Kihez beszélsz? Miről szól a peula? Miért fontos ez nekik? Mit fogtok csinálni? Mit szeretnél, hogy hazavigyenek?
- **M4.4-DIA-05**: Pipás összefoglaló három ponttal, majd két lépés: az első vázlat a szövegmezőbe, a finomított változat az M4.B peula után a Moodle-beadandóba.
- **M5.1-IKO-01**: dekoratív kép, üres alt-szöveg.
- **M5.3-ILL-01**: Két rajz. A) Éjjel egy fiatal ásítozva magol egy hosszú listát. B) Nappal ugyanő becsukott könyvvel, ujjain számolva felidéz; a naptáron három nap kipipálva.
- **M5.3-IKO-01**: Három ikon: 1. Gyakorlás (kéz), 2. Aktív felidézés (becsukott füzet visszakanyarodó nyíllal), 3. Időben elosztott gyakorlás (három különálló blokk).
- **M5.3-ILL-02**: Három jelenet: Gyakorlás – peulán (labdajáték), Aktív felidézés – következő péntek (beszélgetés körben), Időben elosztott gyakorlás – tábor előtt („3–4× röviden”).
- **M5.4-ILL-01**: Mintatáblázat három kártyán (1–3. helyzet): Feladat / cél, Kvuca (kor / hangulat), Módszer / forma, Tanulástan-szemlélet. A minta a kép alatt olvasható.
- **M6.1-ILL-01**: Két játékkártya: „Névkör labdával” (ismerkedős, 6–9 és 10–12, inkluzív variációkkal) és „Szobor-játék” (energizer, 6–9 és 10–12). A szöveg a dián is olvasható.
- **M6.1-ILL-02**: Játékkártya: „Csukott szemű vezetés” (bizalom- és kontaktjáték, párban), korosztályi kiindulóponttal és figyelmeztetéssel a fizikai és érzelmi kockázatra.
- **M6.1-ILL-03**: Két játékkártya: „Beszélgetőkártyák” (reflexiós, 10–12 és 13–17) és „Fiktív eset kirekesztésről” (mélyebb élményjáték, biztonsági minimummal). A szöveg a dián is olvasható.
- **M6.2-IKO-01**: Négy ikon a négy okkal: szív (érezzenek is), szem (konkrét helyzet), pajzs (biztonságosabb), tükör kérdőjellel (tükröt tart a kvucának).
- **M6.2-DIA-01**: Kétoszlopos ábra: „Nem minden téma és nyelv jó minden korosztálynak” – Oké és Figyelj rá példákkal. A példák a dián szövegként is olvashatók.
- **M6.3-DIA-01**: „Három kérdés minden kézműves feladat előtt”: Cél – Mit tanít? Inkluzivitás – Kinek nehéz? Variációk – Hogyan vonok be mindenkit?
- **M6.3-IKO-01**: dekoratív kép, üres alt-szöveg.
- **Z.1-IKO-01**: Napló-ikon: jegyzetfüzet ceruzával.
- **Z.2-ILL-01**: Rajz: egy fiatal az állát fogva, mosolyogva gondolkodik; feje fölött felvillanó villanykörte és egy „aha” gondolatbuborék.
- **Z.3-IKO-01**: Két ikon: egy figura egyetlen nagy ugrással próbál átjutni egy szakadék fölött, és egy figura apró lépésekkel halad fel a lépcsőn.
