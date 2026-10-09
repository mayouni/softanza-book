#!/usr/bin/env python3
"""Audit the whole book against its own rules. Reads src/ and data/; changes nothing.

    python tools/book_audit.py            # report; exit 1 if any error
    python tools/book_audit.py --notes    # also print the notes (things to look at, not rules)

Errors (the book breaks a rule it states):
  names      a word the book never writes (substrate, Zin, another repository's product), in prose
  refs       a chapter or appendix reference to a page that does not exist
  author     more than three [AUTHOR: ...] questions in a chapter
  dup        the same long paragraph in two pages of one language
  assert     a sentence names a guard and a number of assertions that is not the guard's count in data/guards.json
  glossary   Appendix D cites a chapter that never uses the entry's word
  stage      a stage word other than built, designed, absent
  future     a date after today written as something that happened
  todo       TODO / TBD / lorem left in a page

Notes: chapters with no stage section content, French pages whose reference list differs from the English, very long paragraphs.
"""
import re, sys, json
from datetime import date
from collections import defaultdict
from book_common import ROOT, sources, structure, load_json, now

NAMES = [r"substrate", r"substrat", r"\bzin\b", r"\bzui\b", r"stzzui", r"sonibank", r"organizium", r"bangalo", r"harobanda",
         r"restolean", r"ringface", r"\bzing\b", r"stzos", r"microring", r"vizcode", r"zimcode", r"\bdiko\b", r"stznarrations"]
# "maker" is the word the crafter replaced; "decision-maker" is a door's name and stays
MAKER = re.compile(r"(?<!decision-)(?<!decision )\bmakers?\b", re.I)
FR_MAKER = re.compile(r"\bfabricants?\b|\bcréateurs?\b", re.I)

WORDNUM = {w: n for n, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
FR_WORDNUM = {w: n for n, w in enumerate(
    "zéro un deux trois quatre cinq six sept huit neuf dix onze douze treize quatorze quinze seize dix-sept dix-huit dix-neuf".split())}
FR_TENS = {"vingt": 20, "trente": 30, "quarante": 40, "cinquante": 50, "soixante": 60}


def number_words(s):
    """The first number written in words or digits at the end of s, or None. Handles up to the hundreds in English."""
    s = s.lower().strip()
    m = re.search(r"(\d[\d , ]*)\s*$", s)
    if m:
        return int(re.sub(r"\D", "", m.group(1)))
    toks = re.findall(r"[a-zé-]+", s)
    total, cur, seen = 0, 0, False
    for t in toks[-6:]:
        for part in t.split("-"):
            if part in WORDNUM:
                cur += WORDNUM[part]; seen = True
            elif part in TENS:
                cur += TENS[part]; seen = True
            elif part == "hundred":
                cur = max(cur, 1) * 100; seen = True
            elif part == "and" and seen:
                pass
            elif seen:
                cur = 0 if part not in ("and",) else cur
    return cur if seen and cur else None


def prose(body):
    """The page without its fenced code (and without the generated tables)."""
    return re.sub(r"```.*?```", "", body, flags=re.S)


def main():
    notes_on = "--notes" in sys.argv
    st = structure()
    guards = load_json("guards.json", {}).get("guards", {})
    today = now().date()
    errors, notes = [], []
    langs = {l: sources(l) for l in ("en", "fr")}
    chapter_numbers = {m["number"] for _, m, _ in langs["en"] if not m.get("appendix") and m["number"]}
    letters = {str(m["appendix"]) for _, m, _ in langs["en"] if m.get("appendix")}

    paras = defaultdict(list)
    for lang, srcs in langs.items():
        for path, m, body in srcs:
            tag = f"{lang}/{path.stem}"
            text = prose(body)

            # names
            for pat in NAMES:
                for mm in re.finditer(pat, text, re.I):
                    ln = text[:mm.start()].count("\n") + 1
                    errors.append(f"names  {tag}: '{mm.group(0)}' near prose line {ln}")
            maker = FR_MAKER if lang == "fr" else MAKER
            for mm in maker.finditer(text):
                ctx = text[max(0, mm.start() - 40):mm.end() + 40].replace("\n", " ")
                if lang == "en" and ("refused" in ctx or '"maker"' in ctx or "“maker”" in ctx or "'maker'" in ctx or "word" in ctx):
                    continue          # chapter 2 tells the refusal of the word
                errors.append(f"names  {tag}: '{mm.group(0)}' in: …{ctx}…")

            # references
            ref_en = re.compile(r"\b[Cc]hapters?\s+((?:\d+(?:\s*(?:,|and|to|et|à|–|-)\s*)?)+)")
            ref_fr = re.compile(r"\b[Cc]hapitres?\s+((?:\d+(?:\s*(?:,|and|to|et|à|–|-)\s*)?)+)")
            for mm in (ref_fr if lang == "fr" else ref_en).finditer(text):
                for n in re.findall(r"\d+", mm.group(1)):
                    if int(n) not in chapter_numbers and int(n) != 0:
                        errors.append(f"refs   {tag}: chapter {n} does not exist (…{text[max(0, mm.start() - 20):mm.end()].replace(chr(10), ' ')}…)")
            for mm in re.finditer(r"\b(?:Appendix|Appendices|Annexes?)\s+([A-G](?:\s*(?:,|and|et|to|à)\s*[A-G])*)\b", text):
                for l in re.findall(r"\b[A-G]\b", mm.group(1)):
                    if l not in letters:
                        errors.append(f"refs   {tag}: appendix {l} does not exist")

            # author markers
            nq = len(re.findall(r"\[AUTHOR", body))
            if nq > 3 and not m.get("appendix"):
                errors.append(f"author {tag}: {nq} [AUTHOR] questions (three at most)")

            # stage words
            for k in (m.get("stage") or {}):
                if k not in ("built", "designed", "absent"):
                    errors.append(f"stage  {tag}: front matter stage key '{k}'")

            # todo
            for mm in re.finditer(r"\b(TODO|TBD|FIXME|lorem ipsum|XXX)\b", text):
                if text[max(0, mm.start() - 3):mm.start()].rstrip('   ')[-1:] in ('"', "“", "«", "'", "`"):
                    continue          # a quoted marker is a citation of someone else's page
                errors.append(f"todo   {tag}: {mm.group(0)}")

            # dates after today, written as past events
            for mm in re.finditer(r"\b(20\d\d)-(\d\d)-(\d\d)\b", text):
                try:
                    d = date(int(mm.group(1)), int(mm.group(2)), int(mm.group(3)))
                except ValueError:
                    errors.append(f"future {tag}: invalid date {mm.group(0)}"); continue
                if d > today:
                    errors.append(f"future {tag}: {mm.group(0)} is after today")

            # guard + assertion claims, in one sentence
            for sent in re.split(r"(?<=[.;!?])\s+", text.replace("\n", " ")):
                if "assertion" not in sent and "assertions" not in sent:
                    continue
                named = re.findall(r"`([a-z0-9_]+_narrated|[a-z0-9_]+_guard)`", sent)
                if len(named) != 1:
                    continue          # with two guards in one sentence the number's owner is not decidable here
                for gname in named:
                    g = guards.get(gname)
                    if not g or not g.get("assertions"):
                        continue
                    # a number directly before 'assertion(s)' in the sentence
                    for mm in re.finditer(r"([\w\d,\- ]{1,40}?)\s+(?:assertions?)\b", sent):
                        n = number_words(mm.group(1))
                        if n is not None and n != g["assertions"] and n > 3:
                            notes.append(f"assert {tag}: `{gname}` has {g['assertions']}, sentence says {n}: {sent[:140]}")

            # paragraphs repeated verbatim
            for para in re.split(r"\n\s*\n", text):
                p = re.sub(r"\s+", " ", para).strip()
                if len(p) >= 140 and not p.startswith(("|", "#", "---")):
                    paras[(lang, p)].append(tag)

            if notes_on:
                for para in re.split(r"\n\s*\n", text):
                    if len(para) > 1800:
                        notes.append(f"long   {tag}: a paragraph of {len(para)} characters: {para[:60]!r}")

    for (lang, p), tags in paras.items():
        if len(set(tags)) > 1 or len(tags) > 1:
            errors.append(f"dup    {sorted(set(tags))}: {p[:90]!r}")

    # the evidence each page points at must exist: the site's pages (both languages) and the narrations at the pin
    short = load_json("book-run.json", {}).get("run", {}).get("library", {}).get("short")
    narr_dir = ROOT / ".cache" / f"stzlib-{short}" / "libraries" / "stzlib" / "base" / "doc" / "narrations"
    site_dir = (ROOT / "en" / st.get("site_base", "../../../../stzsite/")).resolve()   # relative to en/, as the reader reads it
    for path, m, body in langs["en"]:
        for n in m.get("narrations") or []:
            if narr_dir.exists() and not (narr_dir / n).exists():
                errors.append(f"evidence en/{path.stem}: narration {n} is not in the library's narration folder at the pin")
        for pg in m.get("site") or []:
            for lg in ("en", "fr"):
                if site_dir.exists() and not (site_dir / lg / f"{pg}.html").exists():
                    errors.append(f"evidence en/{path.stem}: site page {lg}/{pg}.html does not exist in {site_dir}")
    if not narr_dir.exists():
        notes.append("evidence narrations not checked: the snapshot folder is missing")
    if not site_dir.exists():
        notes.append(f"evidence site pages not checked: {site_dir} is missing")

    # the glossary cites chapters; each must use the word
    en = {m["number"]: (m, body) for _, m, body in langs["en"]}
    gl = [b for _, m, b in langs["en"] if m.get("id") == "the-glossary"]
    if gl:
        for entry in re.finditer(r"^\*\*([^.*]+)\.\*\*\s*(.*?)$", gl[0], re.M):
            term, rest = entry.group(1).strip().lower(), entry.group(2)
            cited = re.search(r"\bChapters?\s+([\d, and]+)\.?\s*$", rest)
            if not cited:
                continue
            term_base = re.sub(r"\s*\(.*\)", "", term)
            stem = term_base[:-1] if term_base.endswith("s") and len(term_base) > 4 else term_base
            stem = re.sub(r"(ed|ing|e)$", "", stem) if len(stem) > 6 else stem
            for n in re.findall(r"\d+", cited.group(1)):
                n = int(n)
                if n not in en:
                    errors.append(f"glossary '{term}' cites chapter {n}, which does not exist")
                    continue
                if stem not in en[n][1].lower():
                    errors.append(f"glossary '{term}' cites chapter {n}, which never uses '{stem}'")

    print(f"audited {sum(len(s) for s in langs.values())} pages (en {len(langs['en'])}, fr {len(langs['fr'])})")
    if errors:
        print(f"\n{len(errors)} error(s):")
        for e in errors:
            print("  " + e)
    if notes and (notes_on or True):
        print(f"\n{len(notes)} note(s):")
        for n in notes[:80]:
            print("  " + n)
    if not errors:
        print("audit clean")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
