"""Compare a French page with its English source and say what a translation must keep.

Usage:  python tools/check_fr.py <file stem or number prefix> [...]      (e.g. 12 or 12-a-language-declared or A)
        python tools/check_fr.py --all

Errors (the build would break, or the page would not be the same page): front matter keys and fixed values, the code fences
(identical, in order), the headings and their numbers, the table row counts, the bullet counts, the [AUTHOR markers.
Warnings (read them): numbers of two digits or more that are in one text and not the other, backtick spans that differ,
the words a French page must never carry (the former language's name as a language, 'substrate', 'maker').
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FENCE = re.compile(r"(?ms)^```([^\n]*)\n(.*?)^```")
FIXED = ("id", "part", "number", "spine", "narrations", "site", "guards", "rulings", "research", "appendix", "generated", "law", "figures", "status")


def split(path):
    text = path.read_text(encoding="utf-8").replace("\r", "")
    _, fm, body = text.split("---\n", 2)
    return yaml.safe_load(fm) or {}, body


def prose(body):
    return FENCE.sub("", body)


def numbers(text):
    out = set()
    for m in re.finditer(r"\d[\d,.   ]*\d|\d", text):
        s = re.sub(r"[,.   ]", "", m.group(0))
        if len(s) >= 2:
            out.add(s)
    return out


def tables(body):
    rows, cur = [], 0
    for line in prose(body).split("\n"):
        if line.strip().startswith("|"):
            cur += 1
        elif cur:
            rows.append(cur); cur = 0
    if cur:
        rows.append(cur)
    return rows


def check(en_path, fr_path):
    errs, warns = [], []
    me, be = split(en_path)
    mf, bf = split(fr_path)
    if set(me) != set(mf):
        errs.append(f"front matter keys differ: en-only {sorted(set(me) - set(mf))}, fr-only {sorted(set(mf) - set(me))}")
    for k in FIXED:
        if k in me and me.get(k) != mf.get(k):
            errs.append(f"front matter '{k}' differs: {me.get(k)!r} / {mf.get(k)!r}")
    if isinstance(me.get("stage"), dict) and isinstance(mf.get("stage"), dict) and set(me["stage"]) != set(mf["stage"]):
        errs.append("stage keys differ")
    fe, ff = FENCE.findall(be), FENCE.findall(bf)
    if len(fe) != len(ff):
        errs.append(f"{len(fe)} code fences in English, {len(ff)} in French")
    for i, (a, b) in enumerate(zip(fe, ff), 1):
        if a[0].strip() != b[0].strip():
            errs.append(f"fence {i}: info string differs ({a[0].strip()!r} / {b[0].strip()!r})")
        if a[1].strip("\n") != b[1].strip("\n"):
            errs.append(f"fence {i}: the code differs (it must be byte-identical)")
    he = re.findall(r"(?m)^(#{2,4}) (\d+)?", prose(be))
    hf = re.findall(r"(?m)^(#{2,4}) (\d+)?", prose(bf))
    if he != hf:
        errs.append(f"headings differ: English {he} / French {hf}")
    if tables(be) != tables(bf):
        errs.append(f"table row counts differ: {tables(be)} / {tables(bf)}")
    bul = lambda b: len(re.findall(r"(?m)^[-*] ", prose(b)))
    if bul(be) != bul(bf):
        errs.append(f"bullets: {bul(be)} / {bul(bf)}")
    ordl = lambda b: len(re.findall(r"(?m)^\d+\. ", prose(b)))
    if ordl(be) != ordl(bf):
        errs.append(f"numbered items: {ordl(be)} / {ordl(bf)}")
    if be.count("[AUTHOR") != bf.count("[AUTHOR"):
        errs.append(f"[AUTHOR markers: {be.count('[AUTHOR')} / {bf.count('[AUTHOR')}")
    bold = lambda b: len(re.findall(r"(?m)^\*\*[^*]+\*\*", prose(b)))
    if bold(be) != bold(bf):
        warns.append(f"paragraphs that open in bold: {bold(be)} / {bold(bf)}")
    ne, nf = numbers(prose(be)), numbers(prose(bf))
    if ne - nf:
        warns.append(f"numbers in English and not in French: {sorted(ne - nf)}")
    if nf - ne:
        warns.append(f"numbers in French and not in English: {sorted(nf - ne)}")
    se = set(re.findall(r"`([^`\n]+)`", prose(be)))
    sf = set(re.findall(r"`([^`\n]+)`", prose(bf)))
    if se - sf:
        warns.append(f"backtick spans in English and not in French: {sorted(se - sf)[:8]}")
    if sf - se:
        warns.append(f"backtick spans in French and not in English: {sorted(sf - se)[:8]}")
    low = bf.lower()
    for w in ("substrate", "substrat ", "maker", "faiseur", " ring ", "zin "):
        if w in prose(bf).lower().replace("`", " "):
            warns.append(f"a word to look at: {w.strip()!r}")
    if len(prose(bf)) < 0.8 * len(prose(be)):
        warns.append("the French is much shorter than the English; is something missing?")
    return errs, warns


def main():
    args = sys.argv[1:]
    en_files = sorted((ROOT / "src" / "en").glob("*.md"))
    if "--all" in args:
        picks = en_files
    else:
        def match(p, a):
            if a.isdigit():
                return p.stem.startswith(f"{int(a):02d}-")
            return p.stem == a or p.stem.startswith(a + "-")
        picks = [p for p in en_files if any(match(p, a) for a in args)]
    bad = 0
    for p in picks:
        fp = ROOT / "src" / "fr" / p.name
        if not fp.exists():
            print(f"{p.stem}: no French page")
            bad += 1
            continue
        errs, warns = check(p, fp)
        print(f"{p.stem}: {'ok' if not errs else str(len(errs)) + ' error(s)'}" + (f", {len(warns)} warning(s)" if warns else ""))
        for e in errs:
            print("   ERROR  " + e)
        for w in warns:
            print("   warn   " + w)
        bad += bool(errs)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
