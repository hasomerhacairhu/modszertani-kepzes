# LMS – activity manifest

Ez a Moodle-build hivatalos kontrolltáblája. A modulok Markdown-specifikációja adja a tartalmat; az éles course build során **minden tényleges Moodle activity** kapjon egy sort és konkrét ID/linket.

| Modul | Activity-csoport | Required? | Előfeltétel | Completion / pass | Mit nyit | Határidő | Megjegyzés |
|---|---|---:|---|---|---|---|---|
| M0 | M0.1–M0.4 online | igen | kurzushozzáférés | activity completion, a konkrét interakció szerint | M0.A / M1 | KITÖLTENDŐ | sorrendet a modulhub szerint |
| M0 | M0.A kickoff | igen | kijelölt online előkészítés | jelenlét / facilitator record | M1 | KITÖLTENDŐ | technikai/help keret |
| M1 | M1.1–M1.2 | igen | M0 complete | activity completion | M1.A | KITÖLTENDŐ | |
| M1 | M1.A | igen | M1.1–M1.2 | jelenlét | M1.3–M1.4 | KITÖLTENDŐ | |
| M1 | M1.3–M1.4 + Assignment gate | igen | M1.A | rubrika-kapu **konjunkcióval**: minden sor ≥1 **ÉS** össz. ≥5/8 | M1.B / M2 – a **megerősített kapu-eredmény** nyitja, nem a nyers pontszám | KITÖLTENDŐ | retry mastery |
| M1 | M1.B | igen | M1.3–M1.4 | jelenlét | M2 | KITÖLTENDŐ | |
| M2 | online + peulák + napló/kapu | igen, a hub szerint | M1 complete | a modulhub/kapu szerint | M3 | KITÖLTENDŐ | identity/privacy review required |
| M3 | M3.1–M3.4 | igen | M2 complete | activity completion | M3 produktum/kapu | KITÖLTENDŐ | safeguarding gate |
| M3 | M3.A/M3.B | igen / protokoll szerint | kijelölt online előtanulás | jelenlét + biztonságos esetanalízis | M3 gate | KITÖLTENDŐ | M3.B specialist signoff |
| M3 | M3 kapu | igen | online + produktum | ≥80% (≥10/12) **ÉS** mind a 4 kritikus item (2., 4., 7., 9.) helyes **ÉS** rubrika | M4 – a **megerősített kapu-eredmény** nyitja, nem a nyers pontszám | KITÖLTENDŐ | biztonságkritikus |
| M4 | online + peulák + pitch/kapu | igen | M3 complete | hub/rubrika szerint | M5 | KITÖLTENDŐ | recording/privacy review |
| M5 | online + peulák + kapu | igen | M4 complete | hub/rubrika szerint | M6 | KITÖLTENDŐ | Dialog Cards runtime test |
| M6 | M6.1–M6.4 | igen | M5 complete | M6.4 legalább 3 eset + activity rules | M6 peulák/gate | KITÖLTENDŐ | H5P branch enforcement test |
| M6 | M6.A/M6.B + játéklap gate | igen | kijelölt online előtanulás | rubrika / mastery | M7 | KITÖLTENDŐ | photo/privacy if used |
| M7 | M7.1–M7.4 | igen | M6 complete | activity completion + **Peula v1** | M7.B | KITÖLTENDŐ | AI optional, approved tool only |
| M7 | M7.B | igen | Peula v1 | workshop/review → **Peula v2** | M7 gate | KITÖLTENDŐ | |
| M7 | final gate | igen | Peula v2 + Zmán Kvucá | kapurubrika | Z | KITÖLTENDŐ | safeguarding contact filled |
| Z | Z.1–Z.3 | igen | M7 complete | activity completion | Z.A | KITÖLTENDŐ | |
| Z | Z.A live close | igen | Z.1–Z.3 | jelenlét / facilitator record | Z.4 | KITÖLTENDŐ | hivatalos sorrendben Z.4 előtt |
| Z | Z.4 Assignment + Feedback | igen | Z.A | Assignment submitted + feedback kitöltve (a válaszok név nélkül jelennek meg; nem GDPR-értelemben anonim, anonimitás-szint: emberi döntés – Z.4 §5) | online félév complete | KITÖLTENDŐ | Moodle draft/resume tested |
| Terep | 6 valódi peula | igen a teljes programkompetenciához | online félév complete | megfigyelés + feedback + revision ciklus | program field-complete | 2. félév | lásd Terepgyakorlat |

## Build acceptance

- A `KITÖLTENDŐ` határidőket **a tanulói hozzáférés megnyitása előtt** konkrét dátum/idő váltja fel.
- Minden `Required` activitynél Moodle-ben ellenőrizni kell, hogy a completion valóban azt méri-e, amit a sor állít.
- **Összetett (konjunkciós) kapuknál a nyers aggregált pontszám önmagában nem nyithat kaput.** Ez az M1-re (minden rubrikasor ≥1 **ÉS** össz. ≥5/8) és az M3-ra (≥10/12 **ÉS** a 2./4./7./9. kritikus item mind helyes) vonatkozik: a downstream feltételt a **megerősített kapu-eredményhez** kell kötni. Hogy ezt a cél-Moodle mivel rögzíti és kényszeríti ki, a runtime acceptance dönti el (`LMS – H5P runtime acceptance.md`).
- A megvalósított course exportból ezt a táblát vissza kell auditálni: spec ↔ activity ID ↔ prerequisite ↔ grade/pass ↔ unlock.
