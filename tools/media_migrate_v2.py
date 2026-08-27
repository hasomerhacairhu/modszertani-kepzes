#!/usr/bin/env python3
"""ONE-TIME migration: frozen v1 media registry → v2 declarations in the Markdown.

This script is **not** part of the daily workflow and is **not** the compiler.
`tools/media_manifest.py` is the canonical compiler; this file exists so the
one-time seeding of ~750 historical rows into the current curriculum is a
reviewable, deterministic, re-runnable transformation instead of hand editing.

Contract
--------
* The CURRENT Markdown wins. The frozen registry supplies the *inventory*
  (which asset, which type, which production intent) — never the current copy.
  Narration, alt text and captions are wrapped where they already stand in the
  lesson, so the compiler reads them live.
* Only HTML comments are inserted. No existing line is modified, reordered or
  deleted. Each inserted block is `block_lines + ['']`; stripping a block plus
  the single blank line after it restores the file byte-for-byte, which is what
  `tools/test_media_manifest.py` asserts against `main @ a862973`.
* Nothing is guessed silently. Rows whose anchor, parent or source text cannot
  be resolved are reported, not invented.

Usage
-----
    python3 tools/media_migrate_v2.py plan   [--out plan.json]
    python3 tools/media_migrate_v2.py apply  [--plan plan.json]
    python3 tools/media_migrate_v2.py strip  # remove every v2 metadata block
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import media_manifest as mm  # noqa: E402

ROOT = mm.ROOT
ACTIVE_ROOT = mm.ACTIVE_ROOT
DEFAULT_PLAN = ROOT / "02 Tervezet" / "Média-assetek" / "_build" / "migration-plan.json"

# --------------------------------------------------------------------------
# v1 → v2 vocabulary
# --------------------------------------------------------------------------

TYPE_TO_KIND: dict[str, tuple[str, str]] = {
    "narráció": ("voiceover", "narration"),
    "beszélőfej-videó": ("video", "ai-talking-head"),
    "interaktív-videó": ("video", "interactive"),
    "animált-diagram": ("diagram", ""),
    "illusztráció": ("illustration", ""),
    "ikon-készlet": ("icon-set", ""),
    "fotó-kép": ("photo", ""),
    "print-munkalap": ("worksheet", ""),
    "print-kártya": ("card-set", ""),
    "print-poszter": ("poster", ""),
}

DERIVATIVE_TYPES = {
    "felirat": "captions",
    "leirat-transzkript": "transcript",
    "alt-szöveg": "alt-text",
}

PROVENANCE_PATTERNS: tuple[tuple[str, str], ...] = (
    ("ai-asszisztált", "mixed"),
    ("vegyes", "mixed"),
    ("ai-generált", "ai"),
    ("stock", "stock"),
    ("szöveges-ekvivalens", "human"),
    ("emberi", "human"),
)

#: The R1–R8 production conventions live in the frozen dataset; v2 references
#: them by ID instead of copying their text onto hundreds of rows. Three of them
#: carry an explicit ⟬KITÖLTENDŐ⟭ organisational decision and therefore *block*
#: production: R2 (AI avatar/voice licence evidence), R3 (narrator voice or TTS
#: engine) and R5 (icon/character batch lock, which is where the Somer hex
#: palette is still open). R8 blocks anything with real people or third-party
#: imagery. R7 is a gated dependency: assets it names cannot be produced before
#: the Moodle course is finalised.
RULE_FOR_AI_AVATAR = ("R1", "R2")
RULE_FOR_VOICE = ("R3",)
RULE_FOR_PALETTE = ("R5",)
RULE_FOR_AI_LABEL = ("R1",)
RULE_FOR_IMAGERY_RIGHTS = ("R8",)
RULE_FOR_TRADEMARK = ("R4",)
#: R4 names the platforms whose visual language must not be imitated.
TRADEMARK_RE = re.compile(r"Messenger|WhatsApp|Discord|Insta|chat-buborék|"
                          r"sztori-kör|LMS-felület", re.I)

#: A printed template that the corpus also asks for as a fillable digital form is
#: TWO produced files, not one. Losing the second one lost its accessibility
#: requirement (labelled form fields, tab order) from the production list.
EDITABLE_RE = re.compile(
    r"szerkeszthető verzió|szerkeszthető változat|kitölthető PDF|digitálisan is kitölthető|"
    r"form-?field|űrlapmező|Google/Word sablon|doc/sheet|digitális.{0,24}kitölthető", re.I)

#: Physical items that are bought, not produced: the register has to keep them
#: (a peula cannot run without them) but they carry no production spec.
CONSUMABLE_RE = re.compile(
    r"post-?it|matric|filc|marker|ragaszt|blu-?tack|irodaszer|gyurmaragasztó|"
    r"papír\b|A4-es lap|ceruz|toll\b", re.I)

#: Phrases the repository's own integrity checker forbids from the module corpus.
#: They appear in a handful of frozen spec fields as historical runtime drift; a
#: declaration carrying one of them would (correctly) fail CI, so the seeder
#: refuses to emit it and records the trim instead of quietly rewriting meaning.
FORBIDDEN_SUBSTRINGS = (
    "Short Answer", "short answer", "Short answer",
    "miniszínház", "Miniszínház", "mini-színház",
    "minijelenet", "fórum-színház", "de-roling",
    "megbízható felnőtt", "biztonságos felnőttként",
    "te leszel az a felnőtt", "felirat VAGY",
)

#: Files the v1 inventory verified as carrying no media, each with the reason the
#: discovery lint needs in order to tell "nothing to produce here" apart from
#: "somebody forgot to declare it". Paths are relative to `02 Tervezet/`.
ASSET_FREE_FILES: dict[str, str] = {
    'Modulok/M0/M0 – Kickoff, keret, technika.md':
        'Modul-áttekintő fájl: a benne említett médiát a modul saját leckéi és peulái deklarálják; itt nincs önálló legyártandó anyag. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
    'Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md':
        'Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
    'Modulok/M2/M2 – Kapu – értékelő (item-bank + rubrika).md':
        'Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
    'Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md':
        'Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
    'Modulok/M4/M4 – Hallható és érthető vagyok – Kiállás, kapcsolódás & kérdezéstechnika.md':
        'Modul-áttekintő fájl: a benne említett médiát a modul saját leckéi és peulái deklarálják; itt nincs önálló legyártandó anyag. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
    'Modulok/M5/M5 – Kapu – értékelő (item-bank + rubrika).md':
        'Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
    'Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md':
        'Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
    'Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md':
        'Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
    'Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzés feedback.md':
        'Moodle Assignment + Feedback lecke: a tartalmat a tanuló állítja elő (reflexiós szöveg vagy videó), a beállítás a `02 Tervezet/LMS – activity manifest.md`-ben él. Nincs legyártandó média-anyag. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.)',
}


# --------------------------------------------------------------------------
# Explicit reuse, carried over from the v1 dedup analysis
# --------------------------------------------------------------------------

#: The v1 register's ID space collided between a module overview (hub) file and
#: the lesson/peula it summarised: the same identifier named two different rows.
#: The merge kept only one of them, so several dedup tags that meant "the hub's
#: row equals this one" ended up pointing at the DETAILED file's own, unrelated
#: asset. The signature is mechanical: member and canonical live in the SAME
#: non-hub file, while the group's reason explains the match by referring to the
#: overview file. v2's unit namespace (`M1-HUB-` vs `M1.A-`) removes the
#: collision, so those rows are separately produced assets, not reuse.
OVERVIEW_HINT = re.compile(r"áttekintő|\bhub\b", re.I)

COLLISION_NOTE = (
    "a v1 dedup-tag a modul-áttekintő fájl azonos azonosítójú sorára mutatott, "
    "nem erre az assetre; a v2 egység-névtér elválasztja a kettőt. A jelenlegi "
    "fájlban ez a sor önálló, külön legyártandó anyag.")

#: Hand-written evidence for the rows the v1 README itself flagged as unresolved.
NOT_ACTUALLY_REUSE: dict[str, str] = {
    "M3.F-MUNK-01": (
        "a v1 dedup-tag a HUB-fájl azonos ID-jű sorára mutatott; a v2 egység-névtér "
        "(M3-HUB- vs. M3.F-) elválasztja őket. Ez a sor a peula saját jegyzetlapja "
        "(„1 gondolat / 1 kérdés leckénként”), nem a fogalom-térkép alaplap "
        "(M3.F-POSZ-02) — külön nyomtatandó anyag."),
    "M3.F-MUNK-02": (
        "a v1 dedup-tag a HUB-fájl azonos ID-jű sorára mutatott; ez a sor a peula "
        "képzői checklistje (1 A4), nem a haladás-követő check-in tábla "
        "(M3.F-POSZ-01) — külön nyomtatandó anyag."),
    "Z.A-POSZ-01": (
        "a v1 dedup-tag a HUB-fájl azonos ID-jű sorára mutatott; ez a sor a peula "
        "„Mit viszek magammal?” szó-felhő fejléc-posztere, nem a „Híd a terepre” "
        "kétoszlopos plakát (Z.A-MUNK-01) — külön nyomtatandó anyag."),
}

#: Reuse the v1 dedup analysis recorded and the current sources confirm, but
#: which only becomes expressible once the hub has its own namespace.
#: Reuse the v1 dedup asserted but the two specs contradict on a safeguarding
#: point: the hub's poster draws a FOUR-step disclosure path, the canonical
#: worksheet a FIVE-node one whose missing node carries the non-negotiable
#: instruction not to promise confidentiality. Which one is canonical is a
#: child-protection question, not a compiler question.
#: Two v1 spec fields still asserted wording the current M5.1 lesson replaced.
#: The live narration was already correct — `source_ref` reads it — but the hidden
#: production spec contradicted it, which is the same drift class in a new place.
#: Both replacements are summaries built from the CURRENT narration's own words,
#: and neither repeats the script: that text lives in the source block.
STALE_SPEC_REWRITES: dict[str, tuple[str, str]] = {
    "M5.1-VID-01": (
        "AI beszélő fej videó, 16:9 arányban, max. 40 mp. Személyes ráhangolással "
        "bevezeti a három tanulási kategóriát (suli / Somer / random élet), és "
        "felveti, mi számít formális, nonformális és informális tanulásnak, "
        "illetve hol van ebben a Somer. A felmondandó szöveg a hivatkozott "
        "forrásblokkban él, itt nem ismételjük.",
        "A v1 spec a HOOK-narráció régi megfogalmazását idézte („random "
        "pillanatok”); a jelenlegi lecke „teljesen más pillanatok”-at mond. A spec "
        "leíróvá vált, és nem duplikálja a felmondandó szöveget."),
    "M5.1-NAR-02": (
        "Kb. 60 mp hangnarráció a három tanulási forma definíciójával: formális "
        "(suli – tanterv és intézményi keret, jeggyel/bizonyítvánnyal hitelesítve, "
        "jellemzően kötelező jelenléttel, tanár–diák szerepben), nonformális "
        "(Somer – a suli rendszerén kívüli, szervezett, megtervezett program, "
        "amelynek van nevelési célja, csak nem dolgozatban, hanem játékban, "
        "beszélgetésben és közös élményekben jelenik meg; a Somerbe ráadásul "
        "önként jössz), és informális (random élet – spontán, előre tervezett "
        "nevelési cél nélkül). A választóvonal a tudatos nevelési cél, nem az "
        "önkéntesség. A felmondandó szöveg a hivatkozott forrásblokkban él.",
        "A v1 spec azt állította, hogy a nonformális ÉS az informális tanulás is "
        "önkéntes, és ez választja el a formálistól. A jelenlegi M5.1 narráció ezt "
        "kifejezetten cáfolja: a választóvonal a tudatos nevelési cél, az "
        "önkéntesség pedig a Somer sajátja."),
}

#: Narrations whose script is the slide's own text, because the lesson says so in
#: as many words. The region is addressed by its first and last LINE TEXT, not by
#: a line number — the v1 notes still carry line references that drifted, which is
#: exactly what v2 exists to stop relying on.
SLIDE_TEXT_NARRATIONS: dict[str, tuple[str, str, str]] = {
    "M5.3-NAR-01": (
        "**1. Gyakorlás**",
        "> hanem három külön napon, rövidebb időkre osztva.",
        "a lecke a három fogalom-blokk után kimondja: „(Opcionális 20–30 mp-es "
        "narráció ugyanezzel a szöveggel.)” — a felmondandó szöveg tehát a dia "
        "három blokkja, nem külön szkript"),
    "M7.1-NAR-02": (
        "> Válaszd ki **1 saját peula-ötletedet** (lehet olyasmi, amit már úgyis "
        "tervezel a kvucáddal).",
        "> – „1–2 konkrét dolgot meg tudnak nevezni arról, hogy …”",
        "a lecke a dia-szöveg után kimondja: „(Opcionális narráció, 15–20 mp-ben "
        "ugyanez hangban.)” — a felmondandó szöveg tehát a dia szövege"),
}

#: The Interactive Video container has no script of its own: its sound is the
#: three scene narrations played in sequence, and the manifest has no way to say
#: "composed of". Who owns the caption file is a production decision, not a
#: compiler one, so it is recorded rather than guessed.
CONTAINER_DECISIONS: dict[str, str] = {
    "M4.1-VID-02": (
        "Az Interactive Video hangsávja a három jelenet narrációjából áll össze "
        "(M4.1-NAR-03/04/05), önálló szkriptje nincs; a v1 leltár viszont ehhez a "
        "konténerhez rendelte a felirat- és leirat-sort (M4.1-FEL-03 / M4.1-LEI-02), "
        "és a jelenetek jegyzete is ide mutat. El kell dönteni, hogy a felirat- és "
        "leiratfájlt a konténer kapja-e (a három szkript összefűzésével), vagy "
        "jelenetenként készül — addig a konténer felirata nem gyártható. A három "
        "szkript szövege a regiszterben megvan."),
}

#: An alt the lesson DOES state, but which cannot be wrapped in a source block:
#: the prescription puts two alts in one blockquote paragraph, and a marker
#: between them would split that paragraph visibly. Production reads the text
#: from the lesson; the compiler cannot verify it stays in sync.
UNWRAPPABLE_ALT_NOTES: dict[str, str] = {
    "M6.3-FOTO-01": (
        "az alt-szöveg meg van írva a leckében („Bal kép alt: …”), de nem fogható "
        "@source blokkba: a prescription egyetlen bekezdésben ad meg két alt-ot, "
        "és a köztük elhelyezett jelölő kettévágná a bekezdést. A szöveget a "
        "leckéből kell átvenni — az élő ellenőrzés erre az egy altra nem terjed ki."),
}

#: Spoken assets whose script already exists in the current lesson, under a
#: different asset. Linking the SAME source block keeps one copy of the text and
#: stops the video from looking producible without a script. Keyed by v1 ID.
SPOKEN_SOURCE_LINKS: dict[str, tuple[str, str]] = {
    "M4.1-VID-03": ("M4.1-NAR-03-VO",
                    "az M4.1 SLIDE 3 „Jelenet 1” blokkja alatt a „Narráció "
                    "(15–20 mp, a kép közben)” idézett szkript ennek a jelenetnek "
                    "a hangja"),
    "M4.1-VID-04": ("M4.1-NAR-04-VO",
                    "az M4.1 „Jelenet 2” narrációja; a v1 spec maga is "
                    "„Narrációval (M4.1-NAR-04)”-ként hivatkozik rá"),
    "M4.1-VID-05": ("M4.1-NAR-05-VO",
                    "az M4.1 „Jelenet 3” narrációja, a jelenet képe alatt futó "
                    "idézett szkript"),
}

#: Videos the current lesson describes as picture-only material. Declaring this
#: removes no requirement: the narration they run under is its own asset and
#: carries the captions and the transcript.
#: Once a video is resolved as silent, its own note may not stay conditional: the
#: alt it calls "recommended" is now a required deliverable.
SILENT_VIDEO_A11Y_NOTES: dict[str, str] = {
    "M1.1-VID-02": ("Némán fut a narráció alatt, ezért a felirat és a leirat "
                    "kötelezettsége azé a narrációé, amely alatt megy "
                    "(M1.1-NAR-04). A képi tartalomhoz viszont alt-szöveg "
                    "kötelező: a jeleneteket rövid leírás írja le."),
}

SILENT_VIDEOS: dict[str, str] = {
    "M1.1-VID-02": (
        "A saját akadálymentesítési jegyzete mondja ki: „Ha némán fut a narráció "
        "alatt, a kapcsolódó NAR feliratai fedik”. A lecke kizárólag képi anyagként "
        "írja le („1× mini storyboard / B-roll (példákhoz)”, illetve „Storyboard: "
        "kvuca-szitu (körben ülő fiatalok, madrich jelenlét)”), párbeszéd és saját "
        "narráció nélkül, a v1 spec szerint a narrációk ALÁ vágott anyagként. A v1 "
        "leltár sem rendelt hozzá felirat- vagy leirat-sort. A feliratot és a "
        "leiratot az a narráció adja, amely alatt fut; a képi tartalomhoz viszont "
        "alt-szöveg jár."),
}

#: Keyed by the v1 identifier, like every other migration table here.
SAFEGUARDING_DECISIONS: dict[str, str] = {
    "M3.B-POSZ-01": (
        "A modul-áttekintő NÉGY lépéses gyermekvédelmi lépés-térkép posztert ír le "
        "(észreveszem → jelzek → nem maradok egyedül → bevonás), a peula kanonikus "
        "sablonja viszont ÖT csomópontosat, amelynek 2. eleme a nem alkudható "
        "instrukció: „Meghallgatom röviden, biztonságosan (nem ígérek 100% "
        "titoktartást)”. A v1 leltár a kettőt ugyanannak a médiának vette. "
        "Gyermekvédelmi felelős döntse el, hány lépéses a kanonikus lépés-térkép, "
        "és igazítsa hozzá a hub összefoglaló mondatát — addig ez a poszter nem "
        "gyártható."),
}

EXTRA_REUSE: dict[str, tuple[str, str]] = {
    "Z.A-POSZ-02": ("Z.A-POSZ-01",
                    "a Z hub „Lezáró rituálé” blokkja és a Z.A peula ugyanazt az egy "
                    "közös „felhő” felületet írja le (hub: „egy közös »felhőbe« rakják”; "
                    "Z.A eszközlista: „1 nagyobb papír / flipchart lap vagy falfelület "
                    "a »Mit viszek magammal?« felhőnek”) — egy fizikai média."),
}

PAREN_SUFFIX = re.compile(r"\s*\((.*?)\)\s*$")


def _dedup_base(value) -> str:
    return PAREN_SUFFIX.sub("", str(value or "")).strip()


def _dedup_scope(value) -> str | None:
    match = PAREN_SUFFIX.search(str(value or ""))
    if not match:
        return None
    qualifier = match.group(1).strip().lower()
    if qualifier.startswith("hub"):
        return "hub"
    if qualifier.startswith("al-lecke"):
        return "online-lecke"
    return None


def build_reuse_map(legacy: dict) -> dict[str, tuple[str, str]]:
    """old_id -> (canonical old_id, justification), using the v1 dedup groups.

    Same base-ID and file-scope rules the v1 renderers used, so the set matches
    the 14 rows the frozen register itself classified as reuse — minus the three
    the ID collision mislabelled, plus the one the collision hid.
    """
    rows = {r["assetId"]: r for r in legacy["assets"]}
    out: dict[str, tuple[str, str]] = {}
    for bucket in legacy.get("dedup", []):
        for group in bucket.get("groups", []):
            canonical = _dedup_base(group.get("canonicalId"))
            reason = (group.get("reuseNote") or group.get("reason") or "").strip()
            for member in group.get("memberIds", []):
                base = _dedup_base(member)
                if not base or base == canonical or base in out:
                    continue
                scope = _dedup_scope(member)
                row = rows.get(base)
                if scope and row is not None and row.get("kind") != scope:
                    continue
                if base in NOT_ACTUALLY_REUSE or canonical not in rows:
                    continue
                canonical_row = rows.get(canonical)
                if (row is not None and canonical_row is not None
                        and row["file"] == canonical_row["file"]
                        and row.get("kind") != "hub"
                        and OVERVIEW_HINT.search(reason)):
                    NOT_ACTUALLY_REUSE.setdefault(base, COLLISION_NOTE)
                    continue
                out[base] = (canonical, reason)
    for old_id, (canonical, reason) in EXTRA_REUSE.items():
        out[old_id] = (canonical, reason)
    return out


# --------------------------------------------------------------------------
# Markdown structure helpers
# --------------------------------------------------------------------------

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
BOLD_LABEL_RE = re.compile(r"^\s*\*{2}(?P<label>[^*]+?)\*{2}\s*:?\s*$")
SLIDE_RE = re.compile(r"\bSLIDE\s*(\d+)", re.I)
BLOCK_RE = re.compile(r"\bBLOKK\s*(\d+)|\b(\d+)\.\s*[Bb]lokk", re.I)

NARRATION_MARKERS = (
    "narráció", "mit hallunk", "felmondandó", "narrációs szöveg",
    "hangalámondás", "narrátor", "videó dialóg", "videó-dialóg",
)
#: Lines that sit between a narration label and the script itself: an italic tone
#: direction, or a bolded / quoted accessibility reminder. They are instructions
#: about the narration, never the narration, so the source block starts after them.
A11Y_NOTE_RE = re.compile(r"♿|akadálymentes|wcag|felirat \+ teljes", re.I)
ALT_MARKERS = ("alt-szöveg", "alt szöveg", "javasolt alt", "alt-szöveg-előírás")

QUOTED_RE = re.compile(r"„(?P<text>[^„”]*)”", re.S)
STAGE_DIRECTION_RE = re.compile(r"^\*\(.*\)\*$|^\*_?\(.*\)_?\*$")


def strip_accents(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.lower())
    return "".join(ch for ch in text if not unicodedata.combining(ch))


def tokens(text: str) -> set[str]:
    return {t for t in re.split(r"[^a-z0-9]+", strip_accents(text)) if t}


class Doc:
    """A parsed view of one current Markdown file."""

    def __init__(self, path: Path):
        self.path = path
        self.rel = path.relative_to(ROOT).as_posix()
        self.text = path.read_text(encoding="utf-8")
        self.lines = self.text.split("\n")
        self.unit, self.module, self.file_kind = mm.file_identity(path)
        self.fences = self._fence_map()
        self.headings = self._headings()
        self.sections = self._sections()

    def _fence_map(self) -> list[bool]:
        inside = False
        out = []
        for line in self.lines:
            if line.lstrip().startswith("```"):
                inside = not inside
                out.append(True)
                continue
            out.append(inside)
        return out

    def _headings(self) -> list[tuple[int, int, str]]:
        out = []
        for idx, line in enumerate(self.lines, 1):
            if self.fences[idx - 1]:
                continue
            match = HEADING_RE.match(line)
            if match:
                out.append((idx, len(match.group(1)), match.group(2)))
        return out

    def _sections(self) -> list[dict]:
        out = []
        for pos, (start, level, title) in enumerate(self.headings):
            end = len(self.lines)
            for later_start, later_level, _ in self.headings[pos + 1:]:
                if later_level <= level:
                    end = later_start - 1
                    break
            out.append({"start": start, "end": end, "level": level, "title": title})
        return out

    def section_at(self, line: int) -> dict | None:
        best = None
        for section in self.sections:
            if section["start"] <= line <= section["end"]:
                if best is None or section["level"] > best["level"]:
                    best = section
        return best

    def slide_sections(self) -> list[dict]:
        return [s for s in self.sections if SLIDE_RE.search(s["title"])]


# --------------------------------------------------------------------------
# Quote-run detection
# --------------------------------------------------------------------------

def quote_run(doc: Doc, start: int) -> tuple[int, int] | None:
    """Extent of the blockquote run beginning at or just after line ``start``.

    Consecutive `>` paragraphs separated by a single blank line belong to one
    spoken passage in this corpus (the narration is written as several short
    quoted paragraphs), so the run continues across blank lines as long as the
    next non-blank line is another `>` line. It stops at any other block: a
    heading, a thematic break, an italic stage direction, a list.
    """
    idx = start
    # Skip what sits between a narration label and the script: blank lines, the
    # italic tone direction ("*(Tegező, barátságos hang…)*"), and accessibility
    # reminders — which appear both as bold prose and as their own ♿ blockquote.
    # An earlier pass wrapped such a reminder as if it were the spoken text.
    limit = start + 8
    while idx <= len(doc.lines) and idx < limit:
        line = doc.lines[idx - 1].strip()
        if not line or STAGE_DIRECTION_RE.match(line):
            idx += 1
            continue
        if line.startswith(">") and A11Y_NOTE_RE.search(line):
            while idx <= len(doc.lines) and doc.lines[idx - 1].strip().startswith(">"):
                idx += 1
            continue
        if line.startswith("**") and A11Y_NOTE_RE.search(line):
            idx += 1
            continue
        break
    if idx > len(doc.lines) or not doc.lines[idx - 1].lstrip().startswith(">"):
        return None
    first = idx
    last = idx
    while idx <= len(doc.lines):
        line = doc.lines[idx - 1]
        if line.lstrip().startswith(">"):
            last = idx
            idx += 1
            continue
        if not line.strip():
            look = idx + 1
            while look <= len(doc.lines) and not doc.lines[look - 1].strip():
                look += 1
            if look <= len(doc.lines) and doc.lines[look - 1].lstrip().startswith(">"):
                # An accessibility reminder often follows the script as its own ♿
                # blockquote. It describes the narration; it is not spoken.
                if A11Y_NOTE_RE.search(doc.lines[look - 1]):
                    break
                idx = look
                continue
            break
        # A lazy continuation line belongs to the quoted paragraph.
        if last == idx - 1 and not HEADING_RE.match(line) and not line.startswith("***") \
                and not re.match(r"^\s*[-*+]\s", line) and not re.match(r"^\s*\d+\.\s", line):
            last = idx
            idx += 1
            continue
        break
    return (first, last)


def find_marker_blocks(doc: Doc, markers: tuple[str, ...]) -> list[dict]:
    """Lines that introduce narration/alt copy, with the quote run that follows."""
    out = []
    for idx, line in enumerate(doc.lines, 1):
        if doc.fences[idx - 1]:
            continue
        stripped = line.strip()
        if not stripped or stripped.startswith(">"):
            # A line inside a blockquote is content, not a label. The accessibility
            # notes quote the word "narráció" while describing caption duties; an
            # earlier pass wrapped those as if they were the script itself.
            continue
        is_heading = bool(HEADING_RE.match(stripped))
        is_label = bool(BOLD_LABEL_RE.match(stripped)) or stripped.startswith("**")
        # Z.1 writes the label as plain prose ending in a colon:
        # "Opcionális narráció (30–40 mp), egyszerűen felolvasva…:"
        is_plain_label = stripped.endswith(":") and len(stripped) < 160
        if not (is_heading or is_label or is_plain_label):
            continue
        label = strip_accents(re.sub(r"^[#*>\s-]+", "", stripped))
        # The marker word has to open the label, but the corpus qualifies it in
        # several ways — "Rövid narráció", "Opcionális narráció (40–60 mp)",
        # "Rövid, közös narráció a slide elején". Requiring the marker inside the
        # first few words covers all of them without an ever-growing word list,
        # and still rejects prose that merely mentions narration later on.
        opening = " ".join(label.split()[:4])
        if not any(strip_accents(m) in opening for m in markers):
            continue
        run = quote_run(doc, idx + 1)
        out.append({"marker_line": idx, "marker_text": stripped,
                    "run": list(run) if run else None,
                    "section": doc.section_at(idx)})
    return out


#: An alt prescription writes the alt itself right after its label:
#: `**Alt-szöveg (kötelező):** „…”` or `**Javasolt alt:** **„…”**`. A quotation
#: that merely illustrates the label ("adj rövid alt-szöveget, pl. „Testtartás”")
#: is NOT the alt, so only a quote that follows the colon directly counts.
ALT_QUOTE_RE = re.compile(
    r"(?:javasolt\s+alt|alt-?\s?sz[öo]veg[^:\n]{0,90}|(?:^|[\s*_])alt)"
    r"\s*:\s*[*_\s]{0,6}„([^„”]*)”",
    re.I | re.M)


LIST_MARKER = re.compile(r"^(\s*)([-*+]|\d+[.)])(\s+)")
QUOTE_PREFIX = re.compile(r"^(\s*(?:>\s?)+)")


def content_indent(line: str) -> str:
    """The column a continuation of ``line`` has to start at to stay inside it."""
    match = LIST_MARKER.match(line)
    if match:
        return " " * (len(match.group(1)) + len(match.group(2)) + len(match.group(3)))
    return line[:len(line) - len(line.lstrip())]


ALT_LABEL_RE = re.compile(r"javasolt\s+alt|alt-?\s?sz[öo]veg|(?:^|[\s*_>])alt\s*:", re.I)


#: A line that begins its own block: another list item, a heading, a thematic
#: break — optionally inside a blockquote.
BLOCK_START_RE = re.compile(r"^\s*(?:>\s?)*(?:[-*+]\s|\d+[.)]\s|#{1,6}\s|\*\*\*|---)")


def starts_block(line: str) -> bool:
    return not line.strip() or bool(BLOCK_START_RE.match(line))


def _marker_prefix(neighbour: str, own: str, closing: bool = False) -> str:
    """What a marker must carry to stay inside the block it borders.

    Empty at a blank-line boundary: there the plain contract is correct and any
    indentation would change list tightness. Otherwise the surrounding
    blockquote's `>` prefix, or the indentation that keeps the marker inside the
    list item it is written into.
    """
    if not neighbour.strip():
        return ""
    quote = QUOTE_PREFIX.match(own if closing else neighbour)
    if quote and QUOTE_PREFIX.match(neighbour):
        return quote.group(1)
    if LIST_MARKER.match(neighbour) or neighbour[:1] in (" ", "\t"):
        return content_indent(own if closing else neighbour)
    return ""


def find_alt_blocks(doc: Doc) -> list[dict]:
    """The minimal region around each stated alt text, with safe marker prefixes.

    A source block that also swallows an unrelated „…” quotation forces the
    reference to select positionally, and a later edit can silently rebind it to
    the wrong quote. So the block is narrowed to the line (or lines) that carry
    the alt itself, and the markers get whatever prefix keeps them inside the
    surrounding list item or blockquote — an unprefixed marker between two list
    items ends the list, and between two quoted lines splits the quote box.
    """
    out: list[dict] = []
    idx = 1
    while idx <= len(doc.lines):
        line = doc.lines[idx - 1]
        # The window has to START on the label line, or a later window could
        # sweep two unrelated bullets in and wrap the wrong region.
        if doc.fences[idx - 1] or not ALT_LABEL_RE.search(line):
            idx += 1
            continue
        # A marker may only land on a block boundary. Dropped between two lines of
        # the SAME paragraph — two sentences of one quote box, say — it splits that
        # paragraph in two and the reader sees the gap. So the window grows until
        # BOTH ends sit on a boundary while still holding exactly one quotation; if
        # no such window exists the alt keeps its prescription in the lesson but
        # gets no live source.
        before = doc.lines[idx - 2] if idx >= 2 else ""
        if not (starts_block(before) or starts_block(line)):
            idx += 1
            continue
        end = None
        for window in range(1, 6):
            last = idx + window - 1
            if last > len(doc.lines):
                break
            text = mm.normalise_source_text("\n".join(doc.lines[idx - 1:last]))
            quotes = len(QUOTED_RE.findall(text))
            if quotes > 1:
                break
            after = doc.lines[last] if last < len(doc.lines) else ""
            if (ALT_QUOTE_RE.search(text) and quotes == 1
                    and (starts_block(after) or last >= len(doc.lines))):
                end = last
                break
        if end is None:
            idx += 1
            continue
        after = doc.lines[end] if end < len(doc.lines) else ""
        last_line = doc.lines[end - 1]
        prefix_open = _marker_prefix(before, line)
        prefix_close = _marker_prefix(after, last_line, closing=True)
        out.append({"start": idx, "end": end, "used": False, "emitted": False,
                    "prefix_open": prefix_open, "prefix_close": prefix_close,
                    "section": doc.section_at(idx)})
        idx = end + 1
    return out


# --------------------------------------------------------------------------
# Legacy row classification
# --------------------------------------------------------------------------

ID_RE = re.compile(r"\b((?:M[0-7]|Z)(?:[.\-][0-9A-ZÁÉÍÓÖŐÚÜŰ]+)*-[A-ZÁÉÍÓÖŐÚÜŰ]{3,4}-\d{2})\b")


_AUDIT_DECISIONS: dict[str, str] | None = None


def open_decision_for(old_id: str) -> str:
    """An unresolved authoring decision the v1 audit recorded against this row.

    The audit marked them with ⟬SZERZŐI DÖNTÉS⟭ / ⟬KITÖLTENDŐ⟭. They are open
    questions about the curriculum, not defects the migration may close, so they
    move into the asset's `decision` field and surface in the register.
    """
    global _AUDIT_DECISIONS
    if _AUDIT_DECISIONS is None:
        _AUDIT_DECISIONS = {}
        legacy = mm.load_legacy() or {}
        for dimension in legacy.get("audit", []):
            for finding in dimension.get("findings", []):
                fix = finding.get("fix", "") or ""
                asset_id = finding.get("assetId", "")
                if asset_id and "⟬" in fix and "PÓTOLVA" not in fix:
                    _AUDIT_DECISIONS[asset_id] = (
                        f"{finding.get('issue', '').strip()} — {fix.strip()}")
    return _AUDIT_DECISIONS.get(old_id, "")


def normalise_provenance(raw: str) -> str:
    low = (raw or "").lower()
    for needle, value in PROVENANCE_PATTERNS:
        if needle in low:
            return value
    return "unknown"


#: `KITÖLTENDŐ` is the repository's marker for an unresolved decision, and
#: `content_integrity --release-report` counts every occurrence inside a module
#: file as a release blocker. A declaration only *describes* a decision that is
#: already tracked in its own file, so copying the token would mint duplicate
#: blockers. The description is kept; only the marker token is replaced.
PLACEHOLDER_RE = re.compile(r"⟬\s*KITÖLTENDŐ[^⟭]*⟭|„?⟬?\s*KITÖLTENDŐ\s*⟭?”?|KITÖLTENDŐ")


def replace_placeholders(text: str) -> tuple[str, bool]:
    if not text or "KITÖLTENDŐ" not in text:
        return text, False
    cleaned = PLACEHOLDER_RE.sub("nyitott döntés", text)
    cleaned = re.sub(r"\(\s*([0-9]+\. sor)\s*[–-]\s*nyitott döntés\s*\)", r"(\1)", cleaned)
    cleaned = re.sub(r"\s{2,}", " ", cleaned).strip()
    return cleaned, True


#: The v1 specs named a concrete H5P free-text content type. The current lessons
#: deliberately do NOT: every one of them carries the rule that a free-text field
#: inside a Course Presentation slide must not be assumed, and that the actual
#: element is decided and tested per
#: `02 Tervezet/LMS – H5P runtime acceptance.md` point 6. Carrying the v1 wording
#: into a lesson file would hand production a runtime decision the curriculum has
#: not made, so the type name is replaced by the lessons' own term — "szabad
#: szöveges mező" — with Hungarian morphology preserved case by case. The original
#: v1 wording stays readable in _legacy/media-merged.json.
RUNTIME_FIELD_REWRITES: tuple[tuple[str, str], ...] = (
    ("H5P Essay / Moodle szöveges mező",
     "Moodle-oldali vagy H5P szabad szöveges mező, a runtime acceptance 6. pontja "
     "szerint"),
    ("Két kötelező H5P Essay (szövegmező) interakció",
     "Két kötelező szabad szöveges mező interakció"),
    ("2× H5P Essay (Course Presentationön belül)",
     "2× szabad szöveges mező (a befoglaló elemet a runtime acceptance 6. pontja "
     "dönti el)"),
    ("H5P Essay x2", "2× szabad szöveges mező"),
    ("H5P Essay nyitott kérdés", "Szabad szöveges mező, nyitott kérdés"),
    ("H5P Essay, nyitott, magyar", "szabad szöveges mező, nyitott, magyar"),
    ("H5P Essay-vel; az Essay", "szabad szöveges mezővel; a mező"),
    ("Slide 5 Essay sablon-vizuál", "Slide 5 sablon-vizuál"),
    ("Essay-sablon vizuálhoz", "sablon-vizuálhoz"),
    ("Essay prompt verbatim", "a szabad szöveges mező promptja verbatim"),
    ("Essay promptban", "szabad szöveges mező promptjában"),
    ("reflektív Essay-hez", "reflektív szabad szöveges mezőhöz"),
    ("reflektív Essay kérdést", "reflektív szabad szöveges kérdést"),
    ("Essay reflektív kérdéssel", "szabad szöveges reflektív kérdéssel"),
    ("Essay reflektív mező", "szabad szöveges reflektív mező"),
    ("Essay reflexióhoz", "szabad szöveges reflexióhoz"),
    ("Essay mezőben", "szabad szöveges mezőben"),
    ("Essay mezők", "szabad szöveges mezők"),
    ("Essay mező", "szabad szöveges mező"),
    ("Essay –", "Szabad szöveges mező –"),
    ("H5P Essay", "szabad szöveges mező"),
    ("Essay", "szabad szöveges mező"),
)

RUNTIME_ARTICLE_FIX = ((" az szabad", " a szabad"), ("Az szabad", "A szabad"),
                       ("az szabad", "a szabad"))

RUNTIME_REVIEW = (
    "A v1 spec konkrét H5P content type-ot nevezett meg a szabad szöveges mezőre; "
    "a jelenlegi leckék ezt kifejezetten a `LMS – H5P runtime acceptance.md` 6. "
    "pontjára bízzák, és kikötik, hogy a Course Presentation dián belüli szabad "
    "szöveges mező nem feltételezhető. A megnevezés ezért kikerült a specből; az "
    "eredeti v1 szöveg a _legacy/media-merged.json-ban olvasható.")


def rewrite_runtime_claim(text: str) -> tuple[str, bool]:
    if not text or "Essay" not in text:
        return text, False
    for needle, replacement in RUNTIME_FIELD_REWRITES:
        text = text.replace(needle, replacement)
    for needle, replacement in RUNTIME_ARTICLE_FIX:
        text = text.replace(needle, replacement)
    # A replacement that lands at the start of a sentence has to keep sentence case.
    text = re.sub(r"(^|(?<=[.!?])\s+)szabad szöveges",
                  lambda m: m.group(1) + "Szabad szöveges", text)
    return text, True


def sanitize(text: str) -> tuple[str, bool]:
    """Drop sentences carrying phrases the repository forbids in module files.

    The frozen spec fields still name runtime details the lessons dropped (an
    H5P content type that does not exist, a peula format that was replaced).
    Copying them into a lesson file would reintroduce a documented regression
    and fail `content_integrity`. The offending SENTENCE is removed and the trim
    is recorded — the compiler never rewrites it into a new claim.
    """
    if not text:
        return "", False
    if not any(bad in text for bad in FORBIDDEN_SUBSTRINGS):
        return text, False
    parts = re.split(r"(?<=[.!?])\s+", text)
    kept = [p for p in parts if not any(bad in p for bad in FORBIDDEN_SUBSTRINGS)]
    cleaned = " ".join(kept).strip()
    return cleaned, True


def classify(rows: list[dict]) -> dict:
    """Split one file's legacy rows into primaries and derivative claims."""
    primaries: list[dict] = []
    derivatives: list[dict] = []
    for row in rows:
        role = DERIVATIVE_TYPES.get(row["assetType"])
        if role:
            derivatives.append({"row": row, "role": role})
        else:
            primaries.append(row)
    return {"primaries": primaries, "derivatives": derivatives}


def referenced_ids(row: dict) -> set[str]:
    blob = " ".join(str(row.get(field, "")) for field in
                    ("a11y", "contentSpec", "notes", "provenance", "title", "location"))
    return set(ID_RE.findall(blob))


def link_derivatives(primaries: list[dict], derivatives: list[dict]) -> tuple[dict, list]:
    """Attach caption/transcript/alt rows to the primary asset they belong to.

    Preference order, most explicit first:
      1. a primary whose own text names the derivative row's ID;
      2. the derivative's own text naming a primary's ID;
      3. same location prefix (same slide/block) and a compatible kind.
    Anything still unattached is reported, never guessed.
    """
    by_id = {row["assetId"]: row for row in primaries}
    claims: dict[str, list[tuple[str, str]]] = defaultdict(list)
    unresolved = []

    forward: dict[str, list[str]] = defaultdict(list)
    for primary in primaries:
        for ref in referenced_ids(primary):
            forward[ref].append(primary["assetId"])

    def location_key(row: dict) -> str:
        loc = row.get("location") or ""
        slide = SLIDE_RE.search(loc)
        if slide:
            return f"SLIDE{slide.group(1)}"
        block = BLOCK_RE.search(loc)
        if block:
            return f"BLOCK{block.group(1) or block.group(2)}"
        return strip_accents(loc.split("/")[0].strip())[:40]

    visual_kinds = {"animált-diagram", "illusztráció", "ikon-készlet", "fotó-kép"}

    for item in derivatives:
        row, role = item["row"], item["role"]
        candidates = forward.get(row["assetId"], [])
        if not candidates:
            candidates = [rid for rid in referenced_ids(row) if rid in by_id]
        if not candidates:
            key = location_key(row)
            pool = [p for p in primaries if location_key(p) == key]
            if role == "alt-text":
                pool = [p for p in pool if p["assetType"] in visual_kinds
                        or p["assetType"] in ("beszélőfej-videó", "interaktív-videó")]
            else:
                pool = [p for p in pool if p["assetType"] in
                        ("narráció", "beszélőfej-videó", "interaktív-videó")]
            candidates = [p["assetId"] for p in pool]

        if not candidates:
            unresolved.append({"old_id": row["assetId"], "role": role,
                               "reason": "nincs azonosítható szülő asset"})
            continue

        # When several primaries name the same derivative, the derivative's own
        # wording decides: `M5.1-ALT-03` is titled "Alt (rejtett/üres) – oszlop-
        # ikonok", so it belongs to the icon set, not to the diagram that merely
        # mentions it. Type order first, then descriptive overlap, then ID.
        own_words = tokens(f"{row.get('title', '')} {row.get('location', '')} "
                           f"{row.get('contentSpec', '')}")

        def rank(candidate_id: str) -> tuple[int, int, str]:
            candidate = by_id[candidate_id]
            if role in ("captions", "transcript"):
                order = {"beszélőfej-videó": 0, "interaktív-videó": 0, "narráció": 1}
            else:
                order = {"animált-diagram": 0, "illusztráció": 0, "ikon-készlet": 0,
                         "fotó-kép": 0, "beszélőfej-videó": 1, "interaktív-videó": 1}
            overlap = len(own_words & tokens(f"{candidate.get('title', '')} "
                                             f"{candidate.get('location', '')}"))
            return (order.get(candidate["assetType"], 5), -overlap, candidate_id)

        best = sorted(set(candidates), key=rank)[0]
        claims[best].append((role, row["assetId"]))
        item["parent"] = best

    return claims, unresolved


def fold_narration(primaries: list[dict], claims: dict) -> tuple[dict, dict]:
    """A narration attached to a video becomes that video's `voiceover` derivative.

    The historical registry listed the talking-head video and its narration as two
    separate rows even though production makes them together: one script, one
    recording, one render. v2 keeps ONE semantic asset (the video) whose narration
    source feeds the voiceover, captions and transcript deliverables.
    """
    by_id = {row["assetId"]: row for row in primaries}
    videos = [r for r in primaries if r["assetType"] in ("beszélőfej-videó", "interaktív-videó")]
    narrations = [r for r in primaries if r["assetType"] == "narráció"]
    folded: dict[str, str] = {}

    def location_key(row: dict) -> str:
        loc = row.get("location") or ""
        slide = SLIDE_RE.search(loc)
        return f"SLIDE{slide.group(1)}" if slide else strip_accents(loc.split("/")[0])[:40]

    for video in videos:
        refs = referenced_ids(video)
        target = next((n for n in narrations
                       if n["assetId"] in refs and n["assetId"] not in folded), None)
        if target is None:
            same = [n for n in narrations
                    if location_key(n) == location_key(video) and n["assetId"] not in folded]
            target = same[0] if len(same) == 1 else None
        if target is not None:
            folded[target["assetId"]] = video["assetId"]
            claims[video["assetId"]].append(("voiceover", target["assetId"]))
            for role, old_id in list(claims.get(target["assetId"], [])):
                claims[video["assetId"]].append((role, old_id))
            claims.pop(target["assetId"], None)
    return folded, by_id


# --------------------------------------------------------------------------
# Anchor resolution
# --------------------------------------------------------------------------

def resolve_anchor(doc: Doc, row: dict) -> tuple[dict | None, str]:
    """Which current section a legacy row belongs to, and how confident we are."""
    loc = row.get("location") or ""
    slide = SLIDE_RE.search(loc)
    if slide:
        number = slide.group(1)
        for section in doc.sections:
            match = SLIDE_RE.search(section["title"])
            if match and match.group(1) == number:
                return section, "slide"
    block = BLOCK_RE.search(loc)
    if block:
        number = block.group(1) or block.group(2)
        for section in doc.sections:
            found = BLOCK_RE.search(section["title"])
            if found and (found.group(1) or found.group(2)) == number:
                return section, "block"

    head = loc.split(" / ")[0].strip()
    head = re.sub(r"\(sorok? [^)]*\)", "", head)
    head = re.sub(r"\(\d+[^)]*\)", "", head)
    want = tokens(head)
    best, score = None, 0.0
    if want:
        for section in doc.sections:
            have = tokens(section["title"])
            if not have:
                continue
            overlap = len(want & have) / len(want)
            if overlap > score:
                score, best = overlap, section
    if best is not None and score >= 0.5:
        return best, f"fuzzy:{score:.2f}"

    title_want = tokens(row.get("title", ""))
    if title_want:
        for section in doc.sections:
            have = tokens(section["title"])
            if have and len(title_want & have) / len(title_want) >= 0.5:
                return section, "title"

    top = [s for s in doc.sections if s["level"] <= 2]
    return (top[0] if top else (doc.sections[0] if doc.sections else None)), "fallback"


def insertion_point(doc: Doc, section: dict | None) -> int:
    """First safe insertion index inside ``section`` (1-based line number).

    Immediately after the heading and its blank line, so the declaration reads as
    a property of the section. The insertion contract requires the *previous*
    line to be blank or the file start; a heading is always followed by a blank
    line in this corpus, and the caller asserts it.
    """
    if section is None:
        return len(doc.lines) + 1
    idx = section["start"] + 1
    while idx <= len(doc.lines) and not doc.lines[idx - 1].strip():
        idx += 1
    return min(idx, len(doc.lines) + 1)


# --------------------------------------------------------------------------
# Declaration construction
# --------------------------------------------------------------------------

def v2_asset_id(unit: str, old_id: str) -> str:
    """Old ID re-homed into the file's unit namespace.

    Historical IDs are preserved verbatim whenever the row already lives in its
    own unit's file. Hub and gate files re-used lesson/peula identifiers for
    *different* rows — the collision the v1 register documented but could not
    resolve — so those move into `M1-HUB-…` / `M1-KAPU-…`.
    """
    match = re.match(r"^(.*?)-([A-ZÁÉÍÓÖŐÚÜŰ]{3,4}-\d{2})$", old_id)
    if not match:
        return f"{unit}-EGY-99"
    prefix, tail = match.groups()
    if prefix == unit:
        return old_id
    return f"{unit}-{tail}"


_V2_ID_CACHE: dict[str, str] | None = None


def v2_id_of_legacy(old_id: str) -> str:
    """The v2 identifier a legacy row gets, wherever that row lives."""
    global _V2_ID_CACHE
    if _V2_ID_CACHE is None:
        legacy = mm.load_legacy() or {"assets": []}
        _V2_ID_CACHE = {}
        for row in legacy["assets"]:
            unit, _module, _kind = mm.file_identity(ACTIVE_ROOT / row["file"])
            _V2_ID_CACHE[row["assetId"]] = v2_asset_id(unit, row["assetId"])
    return _V2_ID_CACHE.get(old_id, old_id)


#: old asset ID -> (v2 asset ID, role). Built by replaying the same
#: classification/linking the plan uses, so a human-readable reference to a v1
#: identifier can be rewritten to the v2 asset or deliverable it became. Without
#: this the production workbook would print identifiers that resolve to nothing.
_ROLE_MAP: dict[str, tuple[str, str]] | None = None
#: Deliverable IDs the first planning pass actually produced.
_DELIVERABLES: set[str] = set()
_REWRITE_REFS = False

LEGACY_REF_RE = re.compile(
    r"\b((?:M[0-7]|Z)[.\-][0-9A-ZÁÉÍÓÖŐÚÜŰ]*-[A-ZÁÉÍÓÖŐÚÜŰ]{3,4}-\d{2})\b")


def legacy_role_map() -> dict[str, tuple[str, str]]:
    global _ROLE_MAP
    if _ROLE_MAP is None:
        _ROLE_MAP = {}
        for _path, rows in legacy_rows_by_file().items():
            split = classify(rows)
            claims, _ = link_derivatives(split["primaries"], split["derivatives"])
            folded, _ = fold_narration(split["primaries"], claims)
            for asset_id, items in claims.items():
                target = v2_id_of_legacy(asset_id)
                for role, old_id in items:
                    _ROLE_MAP[old_id] = (target, role)
            for row in split["primaries"]:
                if row["assetId"] not in folded:
                    _ROLE_MAP[row["assetId"]] = (v2_id_of_legacy(row["assetId"]), "asset")
    return _ROLE_MAP


def rewrite_legacy_refs(text: str) -> str:
    """Point a human-readable reference at what the v1 row actually became."""
    if not _REWRITE_REFS or not text:
        return text

    def replace(match):
        old_id = match.group(1)
        entry = legacy_role_map().get(old_id)
        if entry is None:
            return old_id
        target, role = entry
        if role == "asset":
            return target
        deliverable = f"{target}::{mm.DERIVATIVE_SUFFIX[role]}"
        return deliverable if deliverable in _DELIVERABLES else target

    return LEGACY_REF_RE.sub(replace, text)


def kind_for(row: dict) -> tuple[str, str]:
    mapped = TYPE_TO_KIND.get(row["assetType"])
    if mapped:
        return mapped
    # 'egyéb' rows: split by what they actually are.
    aid = row["assetId"]
    title = row.get("title", "")
    if "-VID-" in aid:
        return ("video", "explainer")
    if row["category"] == "print-fizikai":
        # Two very different things live under "print-fizikai": office supplies to
        # buy, and printed material to produce. Only the first is `external`.
        blob = f"{title} {row.get('contentSpec', '')}"
        if CONSUMABLE_RE.search(blob):
            return ("print", "consumable")
        if re.search(r"kártya", blob, re.I):
            return ("card-set", "")
        if re.search(r"poszter|plakát|flipchart", blob, re.I):
            return ("poster", "")
        return ("worksheet", "")
    if re.search(r"Moodle (Assignment|Label|oldal)", title):
        return ("other", "moodle-activity")
    if re.search(r"H5P|Single Choice|Matching|Drag|Dialog Cards|Question Set|Essay|True/False|"
                 r"Branching|Sorting|poll|kvíz|interakció|szöveges", title, re.I):
        return ("other", "h5p-interaction")
    if re.search(r"provenance|címke|iframe|fókusz", title, re.I):
        return ("other", "ui-text")
    return ("other", "")


#: Asset IDs R7 names explicitly as depending on the finalised Moodle course.
_R7_TARGETS: set[str] | None = None


def r7_targets() -> set[str]:
    global _R7_TARGETS
    if _R7_TARGETS is None:
        rules = {r["id"]: r["text"] for r in (mm.load_legacy() or {}).get("productionRules", [])}
        text = rules.get("R7", "")
        _R7_TARGETS = set(re.findall(r"\b(?:M[0-7]|Z)[.\-][0-9A-ZÁÉÍÓÖŐÚÜŰ]*-[A-ZÁÉÍÓÖŐÚÜŰ]{3,4}-\d{2}\b",
                                     text))
    return _R7_TARGETS


def production_rules_for(kind: str, subtype: str, provenance: str, row: dict) -> list[str]:
    rules: list[str] = []
    if row["assetId"] in r7_targets():
        rules.append("R7")
    if TRADEMARK_RE.search(f"{row.get('contentSpec', '')} {row.get('techSpec', '')}"):
        rules.extend(RULE_FOR_TRADEMARK)
    if provenance in ("ai", "mixed"):
        rules.extend(RULE_FOR_AI_LABEL)
    if kind == "video" and subtype == "ai-talking-head":
        rules.extend(RULE_FOR_AI_AVATAR)
    if kind in ("voiceover", "audio") or (kind == "video" and subtype != "screen-recording"):
        rules.extend(RULE_FOR_VOICE)
    if kind in ("diagram", "illustration", "icon-set", "poster", "card-set", "worksheet"):
        rules.extend(RULE_FOR_PALETTE)
    if kind == "photo" or provenance == "stock":
        rules.extend(RULE_FOR_IMAGERY_RIGHTS)
    seen: list[str] = []
    for rule in rules:
        if rule not in seen:
            seen.append(rule)
    return seen


DECORATIVE_RE = re.compile(r"üres\s*/?\s*rejtett|rejtett\s*/?\s*üres|dekorat", re.I)

#: Whether a visual carries information is stated by the lesson itself, in the
#: accessibility note the v1 row copied from it. Reading only the linked ALT rows
#: got it wrong in both directions: a freeze-frame whose note says "érdemi
#: alt-szöveg kell" was marked decorative, and icon sets whose note says
#: "tisztán DEKORATÍVAK" produced pointless alt deliverables.
NEEDS_ALT_RE = re.compile(
    r"alt-?\s?sz[öo]veg (kell|jár|kötelező|szükséges)|kell alt|kötelező alt|"
    r"érdemi alt|rövid alt|tartalmi (kép|ábra|ikon|vizuál|illusztrác)|"
    r"tartalmat hordoz|információt hordoz|jelentést hordoz|"
    r"nem dekorat|dekorat\w* NEM|szöveges ekvivalens kötelező", re.I)
IS_DECORATIVE_RE = re.compile(
    r"dekorat|üres alt|alt=\"\"|rejtett a felolvasó|nem kell (külön )?alt", re.I)


def visual_role(text: str) -> str | None:
    """"informative" / "decorative" / None, from the lesson's own wording.

    Conflicting or conditional wording ("dekoratív kísérő; ha tartalmi, akkor
    rövid alt") resolves to *informative*: adding an alt requirement that turns
    out unnecessary costs a line of copy, dropping one that was needed makes the
    slide unusable with a screen reader.
    """
    if NEEDS_ALT_RE.search(text):
        return "informative"
    if IS_DECORATIVE_RE.search(text):
        return "decorative"
    return None


#: The project rule is that every video carries captions; a narration over a
#: slide needs only a transcript (SC 1.2.1). When the lesson's own note demands
#: captions for an audio asset, that is the lesson speaking, and it wins.
NEEDS_CAPTIONS_RE = re.compile(r"felirat", re.I)


def build_declaration(row: dict, doc: Doc, roles: list[tuple[str, str]],
                      rows_by_id: dict[str, dict], source_ref: str,
                      alt_source_ref: str, trims: list[str],
                      reuse_map: dict[str, tuple[str, str]]) -> dict:
    """One v2 `@asset` declaration from one legacy primary row plus its claims."""
    kind, subtype = kind_for(row)
    provenance = normalise_provenance(row.get("provenance", ""))
    aid = v2_asset_id(doc.unit, row["assetId"])

    runtime_rewritten = False

    def clean(field: str) -> tuple[str, bool]:
        nonlocal runtime_rewritten
        value, trimmed = sanitize(row.get(field, ""))
        value, _replaced = replace_placeholders(value)
        value, rewritten = rewrite_runtime_claim(value)
        runtime_rewritten = runtime_rewritten or rewritten
        return rewrite_legacy_refs(value), trimmed

    spec, t1 = clean("contentSpec")
    if row["assetId"] in STALE_SPEC_REWRITES:
        spec = STALE_SPEC_REWRITES[row["assetId"]][0]
    purpose, t2 = clean("purpose")
    notes, t3 = clean("notes")
    a11y_note, t4 = clean("a11y")
    title, t5 = clean("title")
    tech_note, t6 = clean("techSpec")
    if t1 or t2 or t3 or t4 or t5 or t6:
        trims.append(row["assetId"])

    legacy: dict[str, list[str]] = {"asset": [row["assetId"]]}
    for role, old_id in roles:
        legacy.setdefault(role, []).append(old_id)

    derivatives: list[str] = []
    a11y: dict[str, str] = {}

    alt_rows = [rows_by_id[i] for i in legacy.get("alt-text", []) if i in rows_by_id]
    alt_decorative = bool(alt_rows) and all(
        DECORATIVE_RE.search(f"{r.get('title', '')} {r.get('contentSpec', '')}")
        for r in alt_rows)

    if kind == "video":
        # A video is "silent" only when nothing in the record points at speech:
        # no narration source, no caption/transcript/voiceover row, no mention of
        # sound in its own spec. Defaulting the other way would quietly delete a
        # caption requirement, so silence has to be provable — which is why the
        # one picture-only case is an explicit, evidence-carrying entry.
        speech_signals = any(role in legacy for role in ("captions", "transcript", "voiceover"))
        mentions_sound = bool(re.search(r"felirat|narrác|hang|beszél|dialóg|szinkron",
                                        f"{spec} {a11y_note} {row.get('title', '')}", re.I))
        spoken = bool(source_ref) or speech_signals or mentions_sound
        if row["assetId"] in SILENT_VIDEOS:
            spoken = False
        a11y["audio"] = "spoken" if spoken else "silent"
        stated = visual_role(f"{row.get('title', '')} {a11y_note} {notes}")
        if stated is not None:
            a11y["visual"] = stated
        elif not spoken:
            # A silent video cannot be "decorative because the captions cover it":
            # it has none. Absent an explicit statement, treat its picture as
            # carrying information — the direction that never drops a requirement.
            a11y["visual"] = "informative"
        else:
            a11y["visual"] = "decorative" if (alt_decorative or not alt_rows) else "informative"
        if spoken:
            derivatives.extend(["captions", "transcript"])
            # A borrowed source belongs to a narration asset that already produces
            # the recording; only an asset that OWNS its script also owns the voice.
            owns_script = row["assetId"] not in SPOKEN_SOURCE_LINKS
            if owns_script and (source_ref or "voiceover" in legacy):
                derivatives.insert(0, "voiceover")
        if a11y["visual"] == "decorative":
            a11y.setdefault("alt_note",
                            "a videóelem dekoratív: a tartalmat a felirat és a leirat "
                            "szó szerint lefedi" if spoken else
                            "a lecke dekoratívként jelöli, önálló szöveges tartalmat "
                            "nem hordoz")
        else:
            derivatives.append("alt-text")
            if not alt_source_ref:
                a11y.setdefault("alt_note", UNWRAPPABLE_ALT_NOTES.get(
                    row["assetId"], "a lecke előírja az alt-szöveget, de a végleges "
                                    "szöveget a legyártott vizuál alapján kell megírni"))

    elif kind in mm.AUDIO_KINDS:
        derivatives.append("transcript")
        if "captions" in legacy or NEEDS_CAPTIONS_RE.search(a11y_note):
            derivatives.insert(0, "captions")

    elif kind in mm.VISUAL_KINDS:
        stated = visual_role(f"{row.get('title', '')} {a11y_note} {notes}")
        decorative = stated == "decorative" if stated is not None else alt_decorative
        if decorative:
            a11y["visual"] = "decorative"
            a11y["alt_note"] = ("a lecke akadálymentesítési jegyzete dekoratívként "
                                "jelöli (üres / rejtett alt)")
        else:
            a11y["visual"] = "informative"
            derivatives.append("alt-text")
            if not alt_source_ref:
                a11y.setdefault("alt_note", UNWRAPPABLE_ALT_NOTES.get(
                    row["assetId"], "a lecke előírja az alt-szöveget, de a végleges "
                                    "szöveget a legyártott vizuál alapján kell megírni"))

    if kind in mm.PRINT_KINDS or kind in mm.DOC_KINDS:
        derivatives.append("print-pdf")
        if EDITABLE_RE.search(f"{spec} {tech_note} {a11y_note}"):
            derivatives.append("editable")

    if alt_source_ref and a11y.get("visual") == "informative":
        a11y["alt_source_ref"] = alt_source_ref
    elif a11y.get("visual") == "informative":
        a11y.setdefault("alt_note", "a lecke előírja az alt-szöveget, de a végleges "
                                    "szöveget a legyártott vizuál alapján kell megírni")
    if row["assetId"] in SILENT_VIDEO_A11Y_NOTES:
        a11y["note"] = SILENT_VIDEO_A11Y_NOTES[row["assetId"]]
    elif a11y_note:
        a11y["note"] = a11y_note

    mode = "generate"
    reuse_of = ""
    reuse_reason = ""
    decision = ""
    external: dict[str, str] = {}
    if row["assetId"] in CONTAINER_DECISIONS:
        decision = CONTAINER_DECISIONS[row["assetId"]]
    if row["assetId"] in SAFEGUARDING_DECISIONS:
        mode = "human-decision"
        decision = SAFEGUARDING_DECISIONS[row["assetId"]]
        derivatives = []
    elif row["assetId"] in reuse_map:
        canonical_old, reuse_reason = reuse_map[row["assetId"]]
        reuse_of = v2_id_of_legacy(canonical_old)
        mode = "reuse"
        derivatives = []
    elif row["category"] == "print-fizikai" and subtype == "consumable":
        mode = "external"
        external = {"source": "beszerzendő irodaszer (post-it / matrica / filc / marker)",
                    "owner": "képzés-logisztika"}
        derivatives = []
    elif provenance == "stock" and mode == "generate":
        mode = "external"
        external = {"source": "stock-kép beszerzés",
                    "licence": "nyitott: licenc, attribúció és felhasználási jogcím "
                               "igazolása hiányzik (R8 produkciós szabály)"}

    rules = production_rules_for(kind, subtype, provenance, row)
    unique: list[str] = []
    for role in derivatives:
        if role in mm.DERIVATIVES and role not in unique:
            unique.append(role)

    declaration: dict = {"id": aid, "kind": kind, "mode": mode,
                         "title": title.strip() or (row.get("title") or "").strip()}
    if subtype:
        declaration["subtype"] = subtype
    if purpose.strip():
        declaration["purpose"] = purpose.strip()
    if spec.strip():
        declaration["spec"] = spec.strip()
    if source_ref:
        declaration["source_ref"] = source_ref
    declaration["provenance"] = provenance
    raw_provenance = (row.get("provenance") or "").strip()
    if raw_provenance and raw_provenance.lower() != provenance:
        declaration["provenance_note"] = raw_provenance
    if tech_note.strip():
        declaration["technical"] = {"note": tech_note.strip()}
    if a11y:
        declaration["a11y"] = a11y
    if unique:
        declaration["derivatives"] = unique
    if decision:
        declaration["decision"] = decision
    if reuse_of:
        declaration["reuse_of"] = reuse_of
    if external:
        declaration["external"] = external
    if rules and mode != "reuse":
        declaration["production_rules"] = rules
        open_rules = [r for r in rules if r in ("R2", "R3", "R5", "R7", "R8")]
        if open_rules:
            declaration["blockers"] = open_rules
    combined_notes = notes.strip()
    if reuse_reason:
        combined_notes = (f"Újrahasznosítás indoklása (v1 dedup): {reuse_reason} "
                          f"{combined_notes}").strip()
    if combined_notes:
        declaration["notes"] = combined_notes
    reviews = []
    if row["assetId"] in SLIDE_TEXT_NARRATIONS:
        reviews.append("A felmondandó szöveg forrása a dia saját szövege: "
                       + SLIDE_TEXT_NARRATIONS[row["assetId"]][2] + ".")
    if row["assetId"] in STALE_SPEC_REWRITES:
        reviews.append(STALE_SPEC_REWRITES[row["assetId"]][1])
    if row["assetId"] in SPOKEN_SOURCE_LINKS:
        reviews.append("A felmondandó szöveg forrása a leckében már megvan: "
                       + SPOKEN_SOURCE_LINKS[row["assetId"]][1] + ".")
    if row["assetId"] in SILENT_VIDEOS:
        reviews.append(SILENT_VIDEOS[row["assetId"]])
    if row["assetId"] in NOT_ACTUALLY_REUSE:
        reviews.append(NOT_ACTUALLY_REUSE[row["assetId"]])
    if runtime_rewritten:
        reviews.append(RUNTIME_REVIEW)
    if reviews:
        declaration["review"] = " ".join(reviews)
    audit_decision = open_decision_for(row["assetId"])
    if audit_decision and not declaration.get("decision"):
        declaration["decision"], _ = replace_placeholders(audit_decision)
    declaration["legacy"] = {k: sorted(set(v)) for k, v in sorted(legacy.items())}
    return enforce_forbidden(declaration, row)


def scrub_title(text: str, hits: list[str]) -> str:
    """Drop a retired term from a title without rewriting what it names.

    "Képzői safety- & de-roling gyorskártya (triage + leállító- + de-roling
    mondatok)" → "Képzői safety-gyorskártya". A trailing parenthetical that is
    built on the retired term goes with it; the remaining words are the legacy
    author's, only the dangling connector is tidied.
    """
    trailing = re.search(r"\s*\([^()]*\)\s*$", text)
    if trailing and any(bad in trailing.group(0) for bad in hits):
        text = text[:trailing.start()]
    for bad in hits:
        text = text.replace(bad, "")
    text = re.sub(r"-\s*&\s*", "-", text)
    text = re.sub(r"\s*&\s*(?=$|\))", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip(" -–—&/,+")


def enforce_forbidden(declaration: dict, row: dict) -> dict:
    """Last line of defence: a declaration may not reintroduce a retired claim.

    `content_integrity` forbids a handful of phrases anywhere under `Modulok/`
    because each marks a defect the curriculum already removed — a runtime that
    does not exist, a peula format replaced on safeguarding grounds. When a legacy
    spec still carries one, the asset is not silently reworded into something new:
    the offending sentence is dropped and the row becomes an explicit human
    decision, because the current lesson no longer supports the requirement.
    """
    blob = json.dumps(declaration, ensure_ascii=False)
    hits = sorted({bad for bad in FORBIDDEN_SUBSTRINGS if bad in blob})
    if not hits:
        return declaration

    def scrub(value):
        if isinstance(value, str):
            cleaned, _ = sanitize(value)
            for bad in hits:
                cleaned = cleaned.replace(bad, "").replace("  ", " ")
            return re.sub(r"\s*[&/,]\s*(?=[)\]]|$)", "", cleaned).strip(" -–—&/,")
        if isinstance(value, dict):
            return {k: scrub(v) for k, v in value.items()}
        if isinstance(value, list):
            return [scrub(v) for v in value]
        return value

    declaration["title"] = scrub_title(declaration.get("title", ""), hits)
    for field in ("purpose", "spec", "notes", "technical", "a11y",
                  "provenance_note", "external"):
        if field in declaration:
            declaration[field] = scrub(declaration[field])
    if not declaration["title"]:
        declaration["title"] = f"Emberi döntésre váró produkciós tétel ({row['assetId']})"
    declaration["mode"] = "human-decision"
    declaration.pop("reuse_of", None)
    # The decision text must not name the retired phrases either: the repository
    # forbids them anywhere under Modulok/, including in metadata.
    declaration["decision"] = (
        "A v1 leltárban szereplő spec olyan foglalkozásformára épült, amit a "
        "jelenlegi tananyag már nem tartalmaz, és a jelenlegi peula-szöveg nem "
        "hivatkozik erre a segédanyagra. Emberi döntés kell arról, hogy szükség "
        "van-e rá, és ha igen, milyen tartalommal — a témáért felelős szakmai/"
        "gyermekvédelmi jóváhagyóval. Az eredeti v1 megfogalmazás a befagyasztott "
        f"leltárban változatlanul megvan ({row['assetId']}).")
    declaration["review"] = (
        "A migráció eltávolította a visszavont megfogalmazást a spec-mezőkből, "
        "mert a repository integritás-ellenőrzése tiltja a Modulok/ alatt; "
        "a v1 szöveg a befagyasztott leltárban (_legacy/media-merged.json) "
        "olvasható.")
    return declaration


# --------------------------------------------------------------------------
# Rendering declarations back into Markdown
# --------------------------------------------------------------------------

def render_asset_free_block(reason: str) -> list[str]:
    payload = json.dumps({"reason": reason}, ensure_ascii=False, indent=2)
    return ["<!-- @asset-free"] + payload.split("\n") + ["-->"]


def render_asset_block(declaration: dict) -> list[str]:
    payload = json.dumps(declaration, ensure_ascii=False, indent=2)
    if "-->" in payload:
        raise SystemExit(f"a(z) {declaration['id']} deklarációja `-->` sorozatot tartalmaz")
    return ["<!-- @asset"] + payload.split("\n") + ["-->"]


def render_source_open(source_id: str, kind: str) -> list[str]:
    payload = {"id": source_id, "kind": kind}
    return ["<!-- @source " + json.dumps(payload, ensure_ascii=False) + " -->"]


SOURCE_CLOSE = ["<!-- @endsource -->"]


# --------------------------------------------------------------------------
# Planning
# --------------------------------------------------------------------------

def plan_file(doc: Doc, rows: list[dict], report: dict,
              reuse_map: dict[str, tuple[str, str]]) -> list[dict]:
    """Every insertion for one file, as (line, block) records."""
    rows_by_id = {row["assetId"]: row for row in rows}
    split = classify(rows)
    claims, unresolved = link_derivatives(split["primaries"], split["derivatives"])
    folded, _ = fold_narration(split["primaries"], claims)
    for item in unresolved:
        report["unlinked_derivatives"].append({"file": doc.rel, **item})

    narration_blocks = [b for b in find_marker_blocks(doc, NARRATION_MARKERS) if b["run"]]
    alt_blocks = find_alt_blocks(doc)
    used_narration: set[int] = set()
    used_alt: set[int] = set()

    insertions: list[dict] = []

    def take_block(blocks, used, section):
        pool = [b for b in blocks if id(b) not in used]
        if section:
            pool = [b for b in pool
                    if section["start"] <= b.get("marker_line", b.get("start", 0))
                    <= section["end"]]
        if not pool:
            return None
        pool.sort(key=lambda b: b.get("marker_line", b.get("start", 0)))
        chosen = pool[0]
        used.add(id(chosen))
        return chosen

    def take_alt_quote(blocks, section):
        """Next unused alt block inside ``section`` (or None)."""
        pool = [b for b in blocks if not b["used"]]
        if section:
            pool = [b for b in pool if section["start"] <= b["start"] <= section["end"]]
        if not pool:
            return None
        pool.sort(key=lambda b: b["start"])
        chosen = pool[0]
        chosen["used"] = True
        return chosen

    def close_line(end: int) -> int:
        """First non-blank line after ``end`` — keeps the marker off a quote line."""
        line = end + 1
        while line <= len(doc.lines) and not doc.lines[line - 1].strip():
            line += 1
        return line

    primaries = [r for r in sorted(split["primaries"], key=lambda r: mm.natural_key(r["assetId"]))
                 if r["assetId"] not in folded]

    for row in primaries:
        section, confidence = resolve_anchor(doc, row)
        if confidence == "fallback":
            report["weak_anchors"].append({"file": doc.rel, "old_id": row["assetId"],
                                           "location": row.get("location", "")})
        roles = claims.get(row["assetId"], [])
        kind, _subtype = kind_for(row)
        aid = v2_asset_id(doc.unit, row["assetId"])

        if row["assetId"] in reuse_map and row["assetId"] not in SAFEGUARDING_DECISIONS:
            # A reuse row produces nothing new, so it gets no source block and no
            # derivatives: it points at the canonical asset's deliverables.
            declaration = build_declaration(row, doc, roles, rows_by_id, "", "",
                                            [], reuse_map)
            insertions.append({"line": insertion_point(doc, section), "kind": "asset",
                               "block": render_asset_block(declaration), "indent": "",
                               "order": 1, "id": declaration["id"], "anchor": confidence})
            report["assets"].append({"file": doc.rel, "v2_id": declaration["id"],
                                     "old_id": row["assetId"], "kind": declaration["kind"],
                                     "roles": sorted({r for r, _ in roles})})
            report["reuse"].append({"file": doc.rel, "v2_id": declaration["id"],
                                    "reuse_of": declaration.get("reuse_of", "")})
            continue

        source_ref = ""
        if row["assetId"] in SLIDE_TEXT_NARRATIONS:
            first_text, last_text, _why = SLIDE_TEXT_NARRATIONS[row["assetId"]]
            span = _text_region(doc, first_text, last_text)
            if span:
                start, stop = span
                source_id = f"{aid}-VO"
                insertions.append({"line": start, "kind": "source-open",
                                   "block": render_source_open(source_id, "narration"),
                                   "indent": "", "order": 0, "id": source_id})
                insertions.append({"line": stop + 1, "kind": "source-close",
                                   "block": list(SOURCE_CLOSE), "indent": "",
                                   "order": 0, "id": source_id})
                source_ref = source_id
            else:
                report["narration_without_source"].append(
                    {"file": doc.rel, "old_id": row["assetId"], "v2_id": aid})
        elif row["assetId"] in SPOKEN_SOURCE_LINKS:
            source_ref = SPOKEN_SOURCE_LINKS[row["assetId"]][0]
        elif kind in ("video", "voiceover", "audio") and row["assetId"] not in SILENT_VIDEOS:
            block = take_block(narration_blocks, used_narration, section)
            if block:
                source_id = f"{aid}-VO"
                indent = leading_space(doc.lines[block["run"][0] - 1])
                insertions.append({"line": block["run"][0], "kind": "source-open",
                                   "block": render_source_open(source_id, "narration"),
                                   "indent": indent, "order": 0, "id": source_id})
                insertions.append({"line": close_line(block["run"][1]), "kind": "source-close",
                                   "block": list(SOURCE_CLOSE), "indent": indent,
                                   "order": 0, "id": source_id})
                source_ref = source_id
            else:
                report["narration_without_source"].append(
                    {"file": doc.rel, "old_id": row["assetId"], "v2_id": aid})
        elif row["assetId"] in SILENT_VIDEOS:
            report["silent_videos"].append({"file": doc.rel, "old_id": row["assetId"]})

        alt_source_ref = ""
        alt_ids = [old_id for role, old_id in roles if role == "alt-text"]
        alt_informative = bool(alt_ids) and not all(
            DECORATIVE_RE.search(f"{rows_by_id[i].get('title', '')} "
                                 f"{rows_by_id[i].get('contentSpec', '')}")
            for i in alt_ids if i in rows_by_id)
        if alt_informative and kind in mm.VISUAL_KINDS:
            block = take_alt_quote(alt_blocks, section)
            if block:
                source_id = f"{aid}-ALT"
                insertions.append({"line": block["start"], "kind": "source-open",
                                   "block": render_source_open(source_id, "alt-text"),
                                   "indent": block["prefix_open"], "order": 0,
                                   "id": source_id})
                insertions.append({"line": block["end"] + 1, "kind": "source-close",
                                   "block": list(SOURCE_CLOSE),
                                   "indent": block["prefix_close"], "order": 0,
                                   "id": source_id})
                alt_source_ref = f"{source_id}#1"
            else:
                report["alt_without_source"].append(
                    {"file": doc.rel, "old_id": row["assetId"], "v2_id": aid})

        trims: list[str] = []
        declaration = build_declaration(row, doc, roles, rows_by_id, source_ref,
                                        alt_source_ref, trims, reuse_map)
        for trimmed in trims:
            report["trimmed_specs"].append({"file": doc.rel, "old_id": trimmed})
        insertions.append({"line": insertion_point(doc, section), "kind": "asset",
                           "block": render_asset_block(declaration), "indent": "",
                           "order": 1, "id": declaration["id"], "anchor": confidence})
        report["assets"].append({"file": doc.rel, "v2_id": declaration["id"],
                                 "old_id": row["assetId"], "kind": declaration["kind"],
                                 "roles": sorted({r for r, _ in roles})})

    overlaps = _overlapping_sources(insertions)
    for dropped in overlaps:
        report["dropped_overlapping_source"].append({"file": doc.rel, "id": dropped})
    if overlaps:
        insertions = [i for i in insertions if i["id"] not in overlaps]
        for insertion in insertions:
            if insertion["kind"] == "asset":
                _drop_source_ref(insertion, overlaps)
    return insertions


def _overlapping_sources(insertions: list[dict]) -> set[str]:
    """Source IDs whose ranges nest or cross — the parser cannot represent those."""
    spans: dict[str, list[int]] = {}
    for insertion in insertions:
        if insertion["kind"] == "source-open":
            spans.setdefault(insertion["id"], [0, 0])[0] = insertion["line"]
        elif insertion["kind"] == "source-close":
            spans.setdefault(insertion["id"], [0, 0])[1] = insertion["line"]
    ordered = sorted(spans.items(), key=lambda kv: kv[1])
    dropped: set[str] = set()
    last_end = -1
    for source_id, (start, end) in ordered:
        if start <= last_end:
            dropped.add(source_id)
            continue
        last_end = end
    return dropped


def _drop_source_ref(insertion: dict, dropped: set[str]) -> None:
    """Rewrite a declaration whose source block had to be dropped."""
    payload = json.loads("\n".join(insertion["block"][1:-1]))
    changed = False
    if payload.get("source_ref", "").split("#")[0] in dropped:
        payload.pop("source_ref")
        changed = True
    a11y = payload.get("a11y") or {}
    if a11y.get("alt_source_ref", "").split("#")[0] in dropped:
        a11y.pop("alt_source_ref")
        a11y.setdefault("alt_note", "a lecke előírja az alt-szöveget, de a végleges "
                                    "szöveget a legyártott vizuál alapján kell megírni")
        changed = True
    if changed:
        insertion["block"] = render_asset_block(payload)


def _text_region(doc: Doc, first_text: str, last_text: str) -> tuple[int, int] | None:
    """Line range between two exact anchor lines, if both ends sit on a boundary."""
    try:
        start = next(i for i, line in enumerate(doc.lines, 1) if line.strip() == first_text)
        stop = next(i for i, line in enumerate(doc.lines, 1)
                    if i > start and line.strip() == last_text)
    except StopIteration:
        return None
    before = doc.lines[start - 2] if start >= 2 else ""
    after = doc.lines[stop] if stop < len(doc.lines) else ""
    if before.strip() or after.strip():
        return None
    return start, stop


def leading_space(line: str) -> str:
    return line[:len(line) - len(line.lstrip())]


UNSAFE_PREV = re.compile(r"^\s*\|")
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s")


def apply_insertions(doc: Doc, insertions: list[dict]) -> tuple[str, list[str]]:
    """Insert every block as ``block + ['']`` so stripping is exactly invertible.

    An HTML comment is an HTML block that may interrupt a paragraph, so a marker
    placed directly after a quoted line still renders identically. Two positions
    genuinely are unsafe and are reported instead of written: inside a table and
    inside a fenced code block.
    """
    problems: list[str] = []
    grouped: dict[int, list[dict]] = defaultdict(list)
    for insertion in insertions:
        grouped[insertion["line"]].append(insertion)

    out: list[str] = []
    for idx in range(1, len(doc.lines) + 2):
        if idx in grouped:
            previous = out[-1] if out else ""
            ids = [i["id"] for i in grouped[idx]]
            following = doc.lines[idx - 1] if idx <= len(doc.lines) else ""
            if UNSAFE_PREV.match(previous) or UNSAFE_PREV.match(following):
                problems.append(f"{doc.rel}:{idx} táblázatba eső beszúrás ({ids})")
            if idx <= len(doc.lines) and doc.fences[idx - 1]:
                problems.append(f"{doc.rel}:{idx} kódblokkba eső beszúrás ({ids})")
            # An UNPREFIXED comment between two quoted lines splits one quote box
            # into two, and between two list items it ends the list. A marker that
            # carries the surrounding block's own prefix stays inside it and
            # changes nothing the reader sees.
            prefixes = {i.get("indent", "") for i in grouped[idx]}
            quoted_marker = all(pfx.lstrip().startswith(">") for pfx in prefixes)
            indented_marker = all(pfx and pfx.strip() == "" for pfx in prefixes)
            if (previous.lstrip().startswith(">") and following.lstrip().startswith(">")
                    and not quoted_marker):
                problems.append(f"{doc.rel}:{idx} idézetblokkot kettévágó beszúrás ({ids})")
            if (LIST_ITEM.match(previous) and LIST_ITEM.match(following)
                    and not indented_marker and not quoted_marker):
                problems.append(f"{doc.rel}:{idx} listát kettévágó beszúrás ({ids})")
            for insertion in sorted(grouped[idx], key=lambda i: (i["order"], i["id"])):
                indent = insertion.get("indent", "")
                out.extend(indent + line if line else line for line in insertion["block"])
                # A prefixed marker lives inside a list item or a blockquote; a
                # blank line after it would end that block and change the layout.
                # Only column-0 markers get the separating blank line.
                if not indent:
                    out.append("")
        if idx <= len(doc.lines):
            out.append(doc.lines[idx - 1])
    return "\n".join(out), problems


# --------------------------------------------------------------------------
# Stripping (the inverse operation, also used by the content-invariant test)
# --------------------------------------------------------------------------

def strip_metadata(text: str) -> str:
    """Remove every v2 metadata block plus the single blank line each added."""
    lines = text.split("\n")
    out: list[str] = []
    idx = 0
    while idx < len(lines):
        match = mm._OPEN_RE.match(lines[idx])
        if match and match.group("tag") in ("asset", "asset-free",
                                            "source", "endsource"):
            start_line = idx
            end = idx
            while end < len(lines) and not lines[end].rstrip().endswith("-->"):
                end += 1
            prefixed = not lines[start_line].startswith("<!--")
            idx = end + 1
            # Mirror of the insertion contract: only an unprefixed marker was
            # written with a separating blank line, so only that one takes it back.
            if not prefixed and idx < len(lines) and not lines[idx].strip():
                idx += 1
            continue
        out.append(lines[idx])
        idx += 1
    return "\n".join(out)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def legacy_rows_by_file() -> dict[str, list[dict]]:
    legacy = mm.load_legacy()
    if legacy is None:
        raise SystemExit("nem található a történeti media-merged.json")
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in legacy["assets"]:
        grouped[row["file"]].append(row)
    return grouped


def plan_asset_free(doc: Doc, reason: str) -> list[dict]:
    """A single file-level `@asset-free` marker, placed under the title."""
    line = 2
    while line <= len(doc.lines) and not doc.lines[line - 1].strip():
        line += 1
    return [{"line": line, "kind": "asset-free", "block": render_asset_free_block(reason),
             "indent": "", "order": 0, "id": doc.unit + "-ASSET-FREE"}]


def make_plan() -> dict:
    already = [path.relative_to(ROOT).as_posix() for path in mm.discover_sources()
               if "<!-- @asset" in path.read_text(encoding="utf-8")
               or "<!-- @source" in path.read_text(encoding="utf-8")]
    if already:
        raise SystemExit(
            "A korpusz már tartalmaz v2 metaadatot — a tervezés csak tiszta forráson "
            f"futhat ({len(already)} fájl, pl. {already[0]}). "
            "Futtasd előbb: python3 tools/media_migrate_v2.py strip")
    grouped = legacy_rows_by_file()
    reuse_map = build_reuse_map(mm.load_legacy() or {"assets": []})
    for rel in ASSET_FREE_FILES:
        grouped.setdefault(rel, [])
    report = {"assets": [], "weak_anchors": [], "unlinked_derivatives": [],
              "narration_without_source": [], "alt_without_source": [],
              "trimmed_specs": [], "insert_problems": [], "dropped_overlapping_source": [], "reuse": [], "silent_videos": [],
              "files": []}
    plan: dict[str, list[dict]] = {}
    # First pass discovers which deliverables exist, so the second pass can
    # rewrite v1 identifiers to something that actually resolves.
    global _REWRITE_REFS, _DELIVERABLES
    if not _REWRITE_REFS:
        _REWRITE_REFS = False
        _DELIVERABLES = _collect_deliverables(grouped, reuse_map)
        _REWRITE_REFS = True
    for legacy_path, rows in sorted(grouped.items()):
        path = ACTIVE_ROOT / legacy_path
        if not path.exists():
            report["insert_problems"].append(f"HIÁNYZÓ FÁJL {legacy_path}")
            continue
        doc = Doc(path)
        if legacy_path in ASSET_FREE_FILES:
            insertions = plan_asset_free(doc, ASSET_FREE_FILES[legacy_path])
        else:
            insertions = plan_file(doc, rows, report, reuse_map)
        _, problems = apply_insertions(doc, insertions)
        report["insert_problems"].extend(problems)
        plan[doc.rel] = insertions
        report["files"].append({"file": doc.rel, "unit": doc.unit,
                                "rows": len(rows), "insertions": len(insertions)})
    return {"plan": plan, "report": report}


def _collect_deliverables(grouped, reuse_map) -> set[str]:
    """Deliverable IDs a dry planning pass produces (no files are written)."""
    out: set[str] = set()
    throwaway = defaultdict(list)
    for legacy_path, rows in sorted(grouped.items()):
        path = ACTIVE_ROOT / legacy_path
        if not path.exists():
            continue
        doc = Doc(path)
        if legacy_path in ASSET_FREE_FILES:
            continue
        for insertion in plan_file(doc, rows, throwaway, reuse_map):
            if insertion["kind"] != "asset":
                continue
            payload = json.loads("\n".join(insertion["block"][1:-1]))
            out.add(payload["id"])
            for role in payload.get("derivatives", []):
                out.add(f"{payload['id']}::{mm.DERIVATIVE_SUFFIX[role]}")
    return out


def cmd_plan(args) -> int:
    result = make_plan()
    out = Path(args.out) if args.out else DEFAULT_PLAN
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    report = result["report"]
    print(f"fájl: {len(result['plan'])}  asset: {len(report['assets'])}")
    for key in ("weak_anchors", "unlinked_derivatives", "narration_without_source",
                "alt_without_source", "trimmed_specs", "dropped_overlapping_source",
                "reuse", "silent_videos", "insert_problems"):
        print(f"  {key:26s} {len(report[key])}")
    print(f"terv: {out}")
    return 0


def cmd_apply(args) -> int:
    result = json.loads(Path(args.plan).read_text(encoding="utf-8")) \
        if args.plan else make_plan()
    problems: list[str] = []
    changed = 0
    for rel, insertions in sorted(result["plan"].items()):
        path = ROOT / rel
        doc = Doc(path)
        text, file_problems = apply_insertions(doc, insertions)
        problems.extend(file_problems)
        if text != doc.text:
            path.write_text(text, encoding="utf-8")
            changed += 1
    for problem in problems:
        print(f"PROBLÉMA {problem}", file=sys.stderr)
    print(f"{changed} fájl módosítva, {len(problems)} probléma")
    return 1 if problems else 0


def cmd_strip(_args) -> int:
    changed = 0
    for path in mm.discover_sources():
        text = path.read_text(encoding="utf-8")
        stripped = strip_metadata(text)
        if stripped != text:
            path.write_text(stripped, encoding="utf-8")
            changed += 1
    print(f"{changed} fájlból eltávolítva a v2 metaadat")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Egyszeri v1 → v2 asset-migráció.")
    sub = parser.add_subparsers(dest="command", required=True)
    plan_parser = sub.add_parser("plan")
    plan_parser.add_argument("--out")
    apply_parser = sub.add_parser("apply")
    apply_parser.add_argument("--plan")
    sub.add_parser("strip")
    args = parser.parse_args(argv)
    return {"plan": cmd_plan, "apply": cmd_apply, "strip": cmd_strip}[args.command](args)


if __name__ == "__main__":
    raise SystemExit(main())
