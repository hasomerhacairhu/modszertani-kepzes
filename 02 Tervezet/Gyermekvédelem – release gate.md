# Gyermekvédelem – release gate

## 1. Mire szolgál ez a kapu?

Ez a dokumentum három külön réteget tart szét:

1. **jogi kötelezettség**, amit hatályos jogszabály alapoz meg;
2. **safeguarding szakmai minimum**, amit a képzés akkor is követ, ha egy konkrét jogi minősítés még nyitott;
3. **szervezeti policy**, amit a Hasomer Hacair magyarországi szervezetének kell jóváhagynia.

A három réteget nem nevezzük egymás helyett „törvényi kötelezettségnek”.

## 2. Release-szabály

M3.3, M3.B, az M3-kapu, valamint minden olyan tananyagelem, amely bántalmazásra, önsértésre, groomingra, szexuális/romantikus határátlépésre, súlyos veszélyeztetettségre vagy külső jelzésre tanít, **nem nyitható meg valódi madrichoknak gyermekvédelmi szakértő írásos jóváhagyása nélkül**.

Zárt Moodle-stagingben, szintetikus tesztadatokkal és csak szerkesztői/QA hozzáféréssel ezek az elemek felépíthetők és technikailag tesztelhetők.

A jelen repo biztonságos szakmai alapértelmezése: súlyos helyzeteket **harmadik személyű esetelemzéssel**, nem traumatikus szerepjátékkal dolgozunk fel.

## 3. Jogi keret, amit a szakértőnek a szervezet konkrét jogállására kell alkalmaznia

### 3.1. Gyvt. 17. §

A hatályos 1997. évi XXXI. törvény 17. § (1) a gyermekvédelmi jelzőrendszer résztvevői között **egyesületeket, alapítványokat és egyházi jogi személyeket is nevesít**. A 17. § (2) a felsorolt intézmények és személyek számára veszélyeztetettség esetére jelzést, súlyos esetekben hatósági eljárás kezdeményezését írja elő.

**Nyitott jogi alkalmazási kérdés:** a képzést ténylegesen működtető szervezeti jogalany, a madrichok és az egyes önkéntes szerepkörök pontosan hogyan esnek a törvényi kötelezettségek alá. Ezt a repository nem minősíti önállóan.

### 3.2. Btk. 209/A. §

A Btk. 209/A. § **nem általános „elmulasztott gyermekvédelmi jelzés = bűncselekmény” szabály**. A tényállás kifejezetten a Gyvt. 17. § **(4a)–(4c)** bekezdéseiben meghatározott, kiemelt veszélyeztető okra utaló körülménnyel összefüggő kötelezettség megszegésére hivatkozik.

Ezért learner-facing tananyagban nem használunk olyan mondatot, amely minden red flagre automatikus büntetőjogi következményt állít. A konkrét jogi kötelezettséget szakértő igazolja a szerepkör és a helyzet alapján.

### 3.3. Akut veszély

Közvetlen életveszély vagy azonnali sürgősségi helyzet esetén a **112** sürgősségi út. Ez nem helyettesíti a szervezet jóváhagyott gyermekvédelmi jelzési láncát.

A Kék Vonal jelenlegi szolgáltatásleírása szerint:
- **116-111**: gyerekek és fiatalok Lelkisegély-vonala, és gyerek érdekében telefonáló felnőttek hívását is fogadja;
- **116-000**: az eltűnt és bántalmazott gyerekek segélyvonala, nem általános „szakember-vonal”;
- **116-123**: felnőtt lelki elsősegély.

A telefonszámokat learner release előtt újra ellenőrizni kell.

## 4. Safeguarding szakmai minimum

Ezek a szabályok a tananyagban akkor is maradnak, ha a konkrét szervezeti/jogi minősítés még nyitott:

- nincs 100%-os titoktartási ígéret;
- a madrich meghallgat, de **nem nyomoz**, nem tesz rávezető kérdésekkel „kihallgatást”;
- a madrich nem konfrontál feltételezett elkövetőt;
- a madrich nem vállal egyedüli felelősséget gyermekvédelmi ügyben;
- a 15–17 éves madrichot nem pozicionáljuk egyedüli „felnőttként”;
- súlyos vagy személyesen érintő gyakorlatnál mindig lehet **passzolni**, szünetet vagy egyenértékű alternatívát kérni;
- a résztvevőnek nem kell saját traumát vagy érzékeny történetet megosztania;
- ha a képzés közben saját érintettség kerül elő, a facilitátor nem folytat nyilvános feldolgozást, hanem biztonságos támogatási útra terel;
- a tananyag nem ír elő automatikus négyszemközti félrevonulást;
- diszkrét beszélgetés csak **átlátható helyzetben**, a jóváhagyott helyi safer-working szabály szerint; amíg ez nincs lezárva, másik képző bevonása az alapértelmezett fallback.

## 5. Szervezeti döntések

A konkrét értékeket az **Emberi jóváhagyás szükséges.md** tartja nyilván. Itt nem ismételjük meg őket külön placeholderként.

- **HUM-SAFE-01:** helyi gyermekvédelmi felelős, elérhetőség, helyettes/külső út, akut-eszkaláció, dokumentálás;
- **HUM-SAFE-02:** négyszemközti / safer-working szabály;
- **HUM-SAFE-03:** a madrich saját érintettsége, passz/alternatíva, kiskorú madrich felügyelete;
- **HUM-SAFE-04:** alkohol- és dohányzási policy;
- **HUM-SAFE-05:** a programban dolgozó felnőttek szerepkörönkénti alkalmassági ellenőrzése, dokumentált safeguarding-felkészítése és felülvizsgálata.

## 6. Tartalmi acceptance

Learner-facing release előtt mindegyik legyen igazolt:

- [ ] M3.3, M3.B, M3-kapu és M7 gyermekvédelmi kapuelemek szakértő által átnézve;
- [ ] HUM-SAFE-01–05 lezárva;
- [ ] a learner-facing kontakt ténylegesen látható a Moodle-ben;
- [ ] nincs 100%-os titoktartási ígéret;
- [ ] nincs nyomozásra, konfrontációra vagy otthoni „lerendezésre” utasítás;
- [ ] akut veszély útja és a segélyvonalak a review napján ellenőrizve;
- [ ] saját érintettségre van rövid, szégyenítés nélküli kilépési/támogatási út;
- [ ] a négyszemközti helyzetek tananyaga a jóváhagyott helyi szabállyal egyezik;
- [ ] az alkohol- és dohányzási példák csak a HUM-SAFE-04 szerint jóváhagyott helyi policy-t állítják;
- [ ] a valódi résztvevőkkel dolgozó stáb alkalmassági ellenőrzése és safeguarding-felkészítése HUM-SAFE-05 szerint dokumentált;
- [ ] a jogszabályi állításoknál külön látszik, mi jogi kötelezettség, mi safeguarding-jógyakorlat, és mi helyi policy;
- [ ] jóváhagyás dátuma és következő felülvizsgálat dátuma rögzítve.

## 7. Elsődleges források a szakértői review-hoz

- **1997. évi XXXI. törvény 17. §**, Nemzeti Jogszabálytár.
- **2012. évi C. törvény 209/A. §**, Nemzeti Jogszabálytár.
- **Kék Vonal Gyermekkrízis Alapítvány**, 116-111 és 116-000 aktuális szolgáltatásleírás.
- **Lelki Elsősegély Telefonszolgálatok Szövetsége**, 116-123.
- Az éles review napján elérhető aktuális állami/ágazati gyermekvédelmi módszertani útmutató.

A repository nem dönthet a szervezet konkrét jogállásáról, jelzési láncáról vagy egyedi ügy jogi minősítéséről szakértő helyett.
