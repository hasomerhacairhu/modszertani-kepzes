---
paths:
  - "02 Tervezet/**/*.md"
---

# Tananyag-invariánsok

Ez aktív tananyag. Minden szerkesztés alapszabálya: **a jelentés nem változhat véletlenül.**
Ha nem tudod bizonyítani, hogy a jelenlegi állapot hibás, ne írd át.

## Számszerű és értékelési invariánsok — csak bizonyított objektív hibánál

- **Answer key**: a `✅` és bármely más helyesmegoldás-jelölés hozzáadása, törlése,
  áthelyezése tilos. Elosztó (distractor) sem cserélhető „stílusból".
- **Küszöbök, ponthatárok, százalékok, időtartamok** (`45’`, `70%`, `3 próbálkozás`)
  változatlanok. Egy szám átírása mindig külön, indokolt finding.
- **Rubrikaszintek, kapu-típus (puha/éles), completion-feltétel** logikája változatlan.
- **Kötelező ↔ opcionális** besorolás nem cserélhető.

## Fix megnevezések — nem „fordítandók", nem „szépítendők"

- Terméknevek és futtatókörnyezet: Moodle, H5P, és a konkrét H5P content type nevek.
  Nem létező típust ne nevezz meg (a repóban ez már megtörtént: nincs „Short Answer").
- Szemantikus azonosítók: `M3.2`, `M7.4`, `Z.4`, `M1.B`, `M6.F`. Ezek **azonosítók**,
  nem listasorszámok — átszámozni, sorrendbe rendezni, „elgépelésként" javítani tilos.
- Fájlnevek és a rájuk mutató relatív linkek együtt mozognak, vagy sehogy.

## Amit egy szerkesztés soha nem törölhet

- gyermekvédelmi instrukció, feltárás-kezelés, jelzési lánc, a kiskorú madrih szerephatárai
- kötelező „in-the-moment" képzői utasítás — ha bürokratikus, a **mondatot** javítsd, ne a védelmet
- adattakarékossági korlát, AI-adatkezelési kikötés, és a **nem-AI alternatíva**
- érzékeny helyzetek szimulációs korlátai (M3: harmadik személyű esetelemzés, nem szerepjáték;
  M6: nincs kirekesztés-szimuláció)
- akadálymentesítési követelmény (WCAG-hivatkozás, alt-szöveg, felirat, kontraszt,
  billentyűzet, érintőfelület-méret)
- H5P/Moodle valós képességére vonatkozó pontosítás és megvalósíthatósági kikötés

## Kereszthivatkozások

Egy átnevezés vagy áthelyezés **soha nem elég önmagában.** Nézd meg a hivatkozó helyeket is:
modulhub link-címkék, `02 Tervezet/Program terv.md` leírások, kapu-fájlok, Study Lab (F-peula)
zárómondatok, `02 Tervezet/LMS – activity manifest.md`,
`02 Tervezet/Emberi jóváhagyás szükséges.md`,
és a média-regiszter forrás-útvonalai.

## Generált tartalom

A `02 Tervezet/Média-assetek/` generált kimeneteit (CSV, XLSX, `_build/*.json` és a
`Média-assetek/README.md` „Mi generált?” táblájában felsorolt Markdown-fájlok) kézzel ne
szerkeszd: a `python3 tools/media_manifest.py build` állítja elő őket, külön `chore(media)`
commitban. A `.gitattributes` szándékosan tiltja a sorvég-normalizálást.

## Látható szöveg, Markdown és átnevezés

- Látható szöveg változásakor a `tools/test_media_manifest.py` pinjei buknak, amíg
  változtatáskészletenként egyszer újra nem pinneled:
  `python3 tools/test_media_manifest.py --pin-visible "<finding-/HUM-ID-k>: <miért>"`.
  A `tools/approved-visible-text.json`-t kézzel soha ne szerkeszd.
- Kemény sortörés: sor végi `\`, nem két szóköz — a CI a teljes PR-tartományon futtatja a
  `git diff --check`-et.
- Átnevezés külön commitban, tartalmi szerkesztés nélkül (lásd 450fef7); a szerkesztés a
  következő commitba kerül. 50% hasonlóság alatt a git törlés + új fájlként látja, és a CI
  a fájl minden sorvégi szóközét jelzi.
