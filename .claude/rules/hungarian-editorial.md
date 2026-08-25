---
paths:
  - "02 Tervezet/**/*.md"
---

# Magyar szerkesztői szabályok

Ez a korpusz exportált és részben gépi fordítású eredetű, ezért sok mondat nyelvtanilag
szabályos, de **nem magyar**. A cél: természetes, felnőttnek szóló, tegező szakmai magyar.

## Alaphangnem

- **Tegezés, közvetlen, felnőttként kezelő.** Nem bébis, nem céges, nem akadémikus.
- **Tanulói és képzői szövegben nincs AI-/compliance-regiszter**: operacionalizálás,
  validáció, governance, runtime, alignment, mitigáció, release gate, „kanonikus" →
  hétköznapi magyar. Belső fejlesztői dokumentumban ezek maradhatnak.
- **Fejlesztői metanyelv nem szivároghat a tananyagba**: „sebészileg", „artefaktum",
  „gyártási embernap", „bukás-útvonal" — ezek nem tanulói szavak.
- **Töltelék-lelkendezés törlése**, ha nincs pedagógiai funkciója („Szuper!", „Ne aggódj!",
  „Most egy izgalmas utazásra indulunk"). A szándékos mérföldkő-gratuláció marad.
- Angol szó csak akkor marad, ha **valódi terméknév, Moodle/H5P UI-elem, vagy bevett
  someres/pedagógiai szakszó**. Egyesével, kontextusban dönts — soha ne globális cserével.

## Nyelvtan, amit külön nézz meg

- **vonzat** (nem az angol elöljáró tükre): „részt vettetek ezen a peulán", nem „peulába"
- **névelő-egyeztetés** `a`/`az` — átnevezés után újra kell ellenőrizni
- **határozott/alanyi ragozás** egyeztetése a tárggyal
- **szám és személy**: szám után egyes szám; a birtokos lánc rövidítése
- **birtokos szerkezet** és igekötő helye
- **névmási referencia**: minden „ez", „az", „ilyenkor" mutasson egyértelmű előzményre
- **felsorolásban nyelvtani párhuzam**: minden pont ugyanabban a szerkezetben
- **igét főnevesítés helyett**: „a jelzés megtétele" → „jelzel"
- **hosszú beágyazott mondat szétvágása**: két gondolat = két mondat
- **magyar tipográfia**: `„…"` idézőjel, beágyazva `'…'`; számtartományban nagykötőjel
  (`15–20’`), telefonszámban kiskötőjel (`116-111`); `stb.` elé nincs vessző
- **`+`, `/`, rövidítés-halmozás helyett rendes mondat**
- **egy fogalomra egy magyar megnevezés** a teljes tananyagban

## Bizonyított regressziós minták — javítás közben ezeket okozzuk

Ezek a hibák **javítás során keletkeztek** ebben a repositoryban. Minden szerkesztés után
nézd meg, nem ejtetted-e valamelyiket:

1. **Hiányzó alaptag** — a jelzős szerkezetből kiesik a főnév („a három legfontosabb" — mi?).
2. **Elveszett minősítő** — „legalább három", „a peula első felében", „ha egyedül vagy":
   a pontosító félmondat törlése a szabályt más szabállyá változtatja.
3. **Névmási zuhanás** — a lecserélt főnév után az „ez"/„az" már másra mutat.
4. **Főnévtorlódás** — „gyermekvédelmi jelzésfelismerési kompetenciafejlesztés".
   Bontsd mondattá.
5. **Morfológia lexikai csere után** — „red flag"→„gyermekvédelmi jelzés" után a rag,
   a névelő és az egyeztetés is változik. A cserét mindig végigviszed a mondaton.
6. **Szám/személy elcsúszás** — egyes számú alany többes számú állítmánnyal, vagy
   tegezés/magázás keveredése egy bekezdésen belül.
7. **Cím ↔ példa ↔ visszajelzés széttartás** — ha a feladat szövege változik, a hozzá
   tartozó cím, példa, kvízkérdés és feedback-mondat is változik, vagy egyik sem.
8. **Kitalált racionalizálás** — a legveszélyesebb. Egy rossz mondat javítása közben
   ne írj helyette új, hihető pedagógiai vagy szakpolitikai magyarázatot.
   Ha nem érted, mit akart mondani: **hagyd, és írj findingot.**
9. **Tartalomvesztés** — az „egyszerűsítés" közben kiesett mondat, lépés vagy feltétel.
   Szószám-csökkenés önmagában is gyanú.
10. **Szemantikus azonosító listasorszámnak nézve** — `M3.2`, `Z.4` nem elgépelés
    és nem sorszám, nem javítandó, nem újraszámozandó.

## Amit ez a szabály NEM enged

- **Ne mass-rewrite-olj.** Fájlonként, mondatonként, indoklással.
- **A jó mondatot hagyd békén.** „Lehetne szebb" nem indok.
- **Nincs pedagógiai vagy policy-átírás nyelvi javítás címén.**
- Ha a mondat tartalmi jelentése bizonytalan, **ne írd át** — findingot írsz.
- Anna (és bármely korábbi szerkesztő) elgépelései nem követendők, hanem javítandók.
