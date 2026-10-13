# 2026-10-12 Modulközi konzisztencia-ellenőrzés (FINAL QA), AP-2026-10-11-01

> **Audit trail — nem kánon, nem tanulói tartalom.** A `/course-autopilot` FINAL QA modulközi konzisztencia-lépése: a futás
> által egységesített alakok (kvíznév, mentorjegyzet-sor, SCS-megjegyzés, „csak hangot tartalmazó narráció”, „Multiple
> Choice”, „kvuca-infó”, „korosztálytérkép”, „fogalomkvíz”, „részvételalapú”, „a kapu nem teljesül”, Assignment- és
> Feedback-nevek) maradékainak keresése a teljes tananyag-korpuszban (a generált kimenetek nélkül), majd adverzális
> verifikáció.
>
> - **Bemenet:** HEAD `0f4f673` (a kánoni kör után); a kereső: `scratchpad/xmod_scan.py`.
> - **Állapot:** VALIDÁLT — 3/3 ID verdikttel (B. melléklet): 3 MEGERŐSÍTVE + objektív, 0 ELVETVE, 0 emberi döntés. Javítva:
>   `c299aab` fix(xmod) + `a16b00d` chore(media). A ledgerben `Z:XMOD-1`, `M0:XMOD-2`, `M5:XMOD-3` kulccsal.
> - **Szerkezet:** A. térkép · B. verdiktek · C. jelöltek.

---

# A. melléklet – verifier-kontextus

# A. Térkép

Három önálló jelölt, klaszter nincs: XMOD-1 (Z hub, mentorjegyzet-sor ↔ ADV:151; az M7:QA-BIZT-1 párja), XMOD-2 (M0.1, M0.4
„Multi Choice” ↔ H5P Multiple Choice; a Z:NYELV-G1-8 és az M2:NYELV-G2-10 maradéka), XMOD-3 (PT:257 „részvétel-alapú” ↔
GL:178, M5.1; az M5:NYELV-G1-2 d) maradéka).

---

# B. melléklet – verifier-verdiktek

# B. Verdiktek

## verifier (3 ID)

XMOD-1 · MEGERŐSÍTVE · objektív · P2 · Az idézet egyezik a fájllal. A Z HUB:206 szövege: „megőrzése … §3 szerint a mentori jegyzet sorát („Mentori 1:1 meta-napló”) követi”. Ezzel ütközik az ADV:69 „Mentori fejlesztési jegyzet (… a terepi megfigyelési jegyzet is)” sora és az ADV:151 „Megőrzése a §3 mátrixának „Mentori fejlesztési jegyzet” sora szerint; ide tartozik a terepi megfigyelési jegyzet is.” mondata. Ugyanezt a mintát javította az M7 QA-BIZT-1 (MEGERŐSÍTVE), és a verifier kifejezetten külön Z-tételként jelölte („A Z HUB:206 … ugyanez a minta … külön Z-tétel”). A javítás a kánoni sornév szó szerinti átvétele, nem új adatvédelmi szabály: mindkét ADV-sor „az utolsó mentorálás + 6 hónap”. Baseline ismeretlen. · Használható szöveg: Z HUB:206-ban csak a zárójeles sornév cserélődik, „(„Mentori 1:1 meta-napló”)” → „(„Mentori fejlesztési jegyzet”)”. A „mentori jegyzet sorát”, az adatminimalitás, a hanih érzékeny adatára vonatkozó kizárás, az incidensnyilvántartás-mondat és a HUM-SAFE-01 változatlan marad. Látható szöveg változik, ezért a pin-tesztet le kell futtatni.

XMOD-2 · MEGERŐSÍTVE · objektív · P2 · Az idézetek egyeznek: M0.1:11 „…nem a Single Choice Set), Multi Choice;”, M0.1:13 „SLIDE 5 Multi Choice”, M0.1:336 és M0.4:156 „Beágyazott kérdés – Multi Choice”, M0.4:11 „Beágyazott kérdéstípusok: Multi Choice, …”. A M0.4:71 egy `@asset` blokk „purpose” mezője („a Multi Choice opcióknál”). Elsődleges forrás a h5p/h5p-multi-choice `semantics.json`, megnyitva: a „Question Type” mező opciói „Multiple Choice (Checkboxes)” (multi) és „Single Choice (Radio Buttons)” (single), „Multi Choice” nevű típus nincs. Két validált precedens van: M2:NYELV-G2-10 (a „Multi Choice” 7 fájlos maradékát scope-on kívülinek jelölte) és Z:NYELV-G1-8. Baseline ismeretlen. · Használható szöveg:
- M0.1:11 és M0.4:11: „Multi Choice” → „Multiple Choice többválaszos (jelölőnégyzetes) módban”. Ez a semantics „multi” címkéjének fordítása, és megkülönbözteti az egyválaszos módtól.
- M0.1:13: „SLIDE 5 Multi Choice” → „SLIDE 5 Multiple Choice”. A completion-feltétel tartalma nem változik.
- M0.1:336 és M0.4:156: „Beágyazott kérdés – Multiple Choice”. Az „Opciók (több válasz lehetséges)” és a „pipa-típus” sor marad.
- M0.4:71: csak build úton (`@asset`), külön `chore(media)` commitban.
- Korlát: ✅, opciók, completion és a „Single Choice” jelölések (M0.1:11, :13) nem változnak.
- Látható szöveg változik, pin kell.

XMOD-3 · MEGERŐSÍTVE · objektív · P2 (a finding-formátumban nincs P3; a súly nem emelkedik, alacsony prioritású helyesírási maradék) · Az idézet egyezik: PT:257 „A program nonformális, élmény- és részvétel-alapú nevelést hirdet”. A kánoni párok már egybeírva állnak: GL:178 „élmény-, részvétel- és kapcsolatalapú”, M5.1:478 és :504 „élmény- vagy részvételalapú”. A PT így a korpusszal ellentétes írásmódot őriz. Az AkH szerint a kéttagú összetétel egybeírandó; ugyanez a minta van a KAPU:78 „élményalapú” alakjában. Az M5:NYELV-G1-2 d) korlátja („csak a PT-vel és a GL-lel együtt javítható, vagy sehol”) a kánon és a lecke együttmozgását írja elő. A GL és az M5.1 már átállt, ezért a PT:257 javítása ezt a korlátot teljesíti, nem sérti. Nem regresszió, hanem kimaradt hely: a d) helylistája a PT-t a „részvétel-alapú” alaknál nem nevezte meg. · Használható szöveg: PT:257-ben csak „élmény- és részvétel-alapú” → „élmény- és részvételalapú”. A mondat többi része, a §2-idézet és a kapu-filozófia változatlan.

Összesítés: MEGERŐSÍTVE 3 (XMOD-1, XMOD-2, XMOD-3) · ELVETVE 0 · EMBERI DÖNTÉS 0 · ebből bizonyíték-kapu 0 · duplikátum nincs. Az XMOD-1 a M7 QA-BIZT-1 Z-beli párja: ugyanaz a minta, de más hely, ezért nem duplikátum. Az XMOD-2 az M2:NYELV-G2-10 és a Z:NYELV-G1-8 M0-beli maradéka: más helyek, nem duplikátum.

---

# C. melléklet – nyers lencse-kimenetek (szó szerint)

# C. Modulközi konzisztencia-jelöltek (FINAL QA, fő munkamenet, 2026-10-12)

A futás által egységesített alakok maradékai a teljes korpuszban (`scratchpad/xmod_scan.py`, a generált kimenetek nélkül).
Szándékosan nem jelölt: az M7 KAPU:21, :44 régi fejlesztői kvízcíme (az M7 implementációs QA-lencse szerint a verifier-korlát
megengedi); a PRODUCTION-DECISIONS:507 „csak hangos narrációk a11y-jegyzete (K2)” (lezárt döntés szövege); az ADV:68 „Mentori
1:1 meta-napló” mátrixsor (létező, külön ADV-sor).

**XMOD-1** · P2 · objektív (jelölt)
- Hely: `02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md:206`
- Probléma: a terepi megfigyelési jegyzet megőrzésére a Z hub a „Mentori 1:1 meta-napló” ADV-sort nevezi meg; az ADV:69 és :151 szerint a megfigyelési jegyzet a „Mentori fejlesztési jegyzet” sorába tartozik. Ugyanezt az M7 HUB:335-ben a 2026-10-12-i M7 célzott QA (QA-BIZT-1, MEGERŐSÍTVE) javította; a verifier ott jelezte: „a Z HUB:206 … ugyanez a minta … külön Z-tétel”.
- Bizonyíték: Z HUB:206 „megőrzése az `Adatvédelem – tanulói adatok és AI.md` §3 szerint a mentori jegyzet sorát („Mentori 1:1 meta-napló”) követi” ↔ ADV:151 „Megőrzése a §3 mátrixának „Mentori fejlesztési jegyzet” sora szerint; ide tartozik a terepi megfigyelési jegyzet is.”
- Javaslat: csak a sornév: „(„Mentori fejlesztési jegyzet”)”. A megőrzési idő (mindkét sorban „az utolsó mentorálás + 6 hónap”), a minimalitás és az incidensnyilvántartás-mondat változatlan.

**XMOD-2** · P2 · objektív (jelölt)
- Hely: `02 Tervezet/Modulok/M0/Online leckék/M0.1 – Üdv a képzésben! – Éves útiterv & mi köze hozzám.md:11`, `:13`, `:336`; `02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md:11`, `:71` (`@asset`?), `:156`
- Probléma: a „Multi Choice” nem H5P content type-név (a típus megjelenített neve „Multiple Choice”; gépi neve H5P.MultiChoice). A Z-ben ugyanezt a Z:NYELV-G1-8 (validált, 5fcf2b0) „Multiple Choice”-ra javította; a Z.1 többválaszos esetre „H5P **Multiple Choice** (pipálhat többet is…)” alakot használ.
- Bizonyíték: M0.1:11 „…Multiple Choice egyválaszos (rádiógombos) módban, nem a Single Choice Set), Multi Choice; …”; M0.4:11 „Beágyazott kérdéstípusok: Multi Choice, Multiple Choice egyválaszos (rádiógombos) módban …”.
- Kérdés a verifiernek: objektív-e (H5P-típusnév), és ha igen, mi a minimális alak ott, ahol a „Multi Choice” a többválaszos módot különbözteti meg az egyválaszostól (pl. „Multiple Choice többválaszos (jelölőnégyzetes) módban”); a :71 `@asset`-e (akkor build úton).

**XMOD-3** · P3 · objektív (jelölt)
- Hely: `02 Tervezet/Program terv.md:257`
- Probléma: a kánoni körben az M5:NYELV-G1-2.obj d) „részvétel-alapú” → „részvételalapú” átírást az M5.1-ben és a GL:178-ban elvégeztük; a PT:257 „élmény- és részvétel-alapú” alakja a finding helylistáján kívül maradt, így a PT-n belül két írásmód él (a PT:110, :183, :273 „fogalomkvíz” is egybeírt lett).
- Bizonyíték: PT:257 „A program nonformális, élmény- és részvétel-alapú nevelést hirdet”.
- Kérdés: objektív helyesírási maradék-e (AkH: kéttagú összetétel egybeírva), és a validált M5:NYELV-G1-2 d) korlátja („csak a PT-vel és a GL-lel együtt javítható, vagy sehol”) alapján ide tartozik-e.
