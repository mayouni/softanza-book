#!/usr/bin/env python3
"""Read each chapter's named guards from the library's test tree, and count their assertions.

A guard is named in a chapter's front matter (`guards: [...]`) by its file stem. This script finds
`<name>.ring` under the test tree of the library snapshot the runner used, and counts the assertion
calls in it: the calls to the shared helper Then, to the helpers the house writes in its guards
(chk, Chk, ChkEq, Check, Expect, Assert, Verify), and to any function the guard itself defines that
counts a pass or a failure, and the promise lines of the house's classic form (`#--> value`), which a
runner judges against the output. A definition (`func chk`) is not an assertion; only calls are counted.

The count is read from the file, not from a run: it says how many assertions the guard holds, not
that they passed. A guard that does not exist fails the build: exit status 1.

    python tools/book_guards.py
"""
import re, sys
from book_common import sources, load_json, save_json, snapshot, GH_BLOB, stamp, now

HELPERS = {"then", "chk", "chkeq", "check", "expect", "assert", "verify"}


def counting_helpers(text):
    """The functions this guard defines that count a pass or a failure."""
    names = set()
    for m in re.finditer(r"(?mis)^\s*func\s+(\w+)[^\n]*\n(.*?)(?=^\s*(?:func|class)\s|\Z)", text):
        if re.search(r"\$?n(Pass|Fail|Ok|Failed|Passed)\w*\s*(\+\+|\+=)", m.group(2), re.I):
            names.add(m.group(1).lower())
    return names


def count_assertions(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    helpers = HELPERS | counting_helpers(text)
    by = {}
    for line in text.split("\n"):
        s = line.strip()
        if not s or s.startswith("#") or re.match(r"(?i)(func|def)\s", s):
            continue
        m = re.match(r"(\w+)\s*\(", s)
        if m and m.group(1).lower() in helpers:
            by[m.group(1)] = by.get(m.group(1), 0) + 1
    # the house's classic form asserts by promise: a line `#--> value` under the expression it judges
    promises = len(re.findall(r"(?m)^[ \t]*(?:#|//)[ \t]*-->|\S[ \t]+#-->", text))
    if promises:
        by["#-->"] = promises
    return sum(by.values()), by


def main():
    run = load_json("book-run.json", None)
    commit = run["run"]["library"]["commit"] if run else None
    lib, prov = snapshot(commit)
    tests = [p for p in lib.rglob("*.ring") if "test" in p.relative_to(lib).parts[:-1]]
    index = {}
    for p in tests:
        index.setdefault(p.stem.lower(), []).append(p)
    out = {"read": stamp(now()), "commit": prov["commit"], "guards": {}, "chapters": {}}
    missing = []
    for lang in ("en", "fr"):
        for path, meta, body in sources(lang):
            names = meta.get("guards") or []
            out["chapters"][f"{lang}/{path.stem}"] = names
            for name in names:
                if name in out["guards"]:
                    continue
                hits = index.get(name.lower(), [])
                if not hits:
                    missing.append(f"{lang}/{path.stem}: {name}")
                    out["guards"][name] = {"exists": False}
                    continue
                f = hits[0]
                rel = f.relative_to(lib).as_posix()
                n, by = count_assertions(f.read_text(encoding="utf-8", errors="replace").replace("\r", ""))
                out["guards"][name] = {"exists": True, "path": rel, "assertions": n, "by_helper": by,
                                       "url": GH_BLOB.format(sha=prov["commit"], path=rel),
                                       "also_found": [h.relative_to(lib).as_posix() for h in hits[1:]]}
                print(f"{name}: {n} assertions  ({rel})")
    save_json("guards.json", out)
    if missing:
        print("MISSING GUARDS:\n  " + "\n  ".join(missing))
        sys.exit(1)


if __name__ == "__main__":
    main()
