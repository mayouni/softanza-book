#!/usr/bin/env python3
"""The release check: every gate, then the artefacts, then a manifest of what was made.

    python tools/release.py              # build, audit, French check, PDF and ePub per language, manifest
    python tools/release.py --no-pdf     # everything but the PDFs (they take about four minutes each)
    python tools/release.py --manifest   # only (re)write the manifest from the files as they are

The gates, in order; the first that fails stops the release:
  1. tools/build_book.py       the run, the guards, the reader, the agents' files
  2. tools/book_audit.py       the book's own rules
  3. tools/check_fr.py --all   the French against the English
  4. tools/epub_book.py        the ePub files (checked by their own tool)
  5. tools/print_book.py       the PDF files (unless --no-pdf)

Writes print/release.json: for each file its size and sha256, the library commit the book ran at, the blocks kept, the number
of pages that are drafts and that are read, and the book's own git commit. A release of a book with unread pages is named
a proof copy in that manifest, and the colophon of the PDF says the same.
"""
import hashlib, json, subprocess, sys
from pathlib import Path
from book_common import ROOT, load_json, now, stamp

OUT = ROOT / "print"
T = ROOT / "tools"
LINT_OK = []   # gate 4's verdicts (English, French), written to the manifest


def run(*args):
    print("\n$ python " + " ".join(args), flush=True)
    r = subprocess.run([sys.executable, *args], cwd=ROOT)
    if r.returncode != 0:
        raise SystemExit(f"release stopped: {' '.join(args)} exited {r.returncode}")


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def manifest():
    runs = load_json("book-run.json", {})
    lib = runs.get("run", {}).get("library", {})
    from book_common import sources
    pages = [m for _, m, _ in sources("en")]
    status = {}
    for m in pages:
        st = {"read": "review", "final": "published"}.get(m.get("status", "draft"), m.get("status", "draft"))
        status[st] = status.get(st, 0) + 1
    chapters = runs.get("chapters", {})
    kept = sum(c.get("kept", 0) for k, c in chapters.items() if k.startswith("en/"))
    runnable = sum(c.get("runnable", 0) for k, c in chapters.items() if k.startswith("en/"))
    files = {}
    for p in sorted(OUT.glob("softanza-*.*")):
        if p.suffix in (".pdf", ".epub"):
            files[p.name] = {"bytes": p.stat().st_size, "sha256": sha256(p)}
    dirty = bool(git("status", "--porcelain"))
    m = {
        "made": stamp(now()),
        "kind": "proof copy" if (status.get("published", 0) != len(pages) or not pages) else "release",
        "pages": len(pages), "pages_by_status": status,
        "blocks_kept": kept, "blocks_runnable": runnable, "library_commit": lib.get("commit"), "library_short": lib.get("short"),
        "book_commit": git("rev-parse", "HEAD"), "book_tree_has_uncommitted_changes": dirty,
        "files": files,
        "lint_strict_passed": {"en": LINT_OK[0], "fr": LINT_OK[1]} if len(LINT_OK) == 2 else None,
        "note": "epubcheck, the W3C validator, was not run; the ePub is checked by its own tool for well-formedness, its manifest and its links.",
    }
    OUT.mkdir(exist_ok=True)
    (OUT / "release.json").write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nwrote print/release.json: {m['kind']}, {len(files)} files, book commit {str(m['book_commit'])[:9]}"
          f"{' (uncommitted changes in the tree)' if dirty else ''}")
    return m


def main():
    if "--manifest" in sys.argv:
        manifest()
        return
    run("tools/build_book.py")
    run("tools/book_audit.py")
    run("tools/check_fr.py", "--all")
    lint = ROOT.parent.parent / "writing-framework" / "tools" / "style_lint.py"
    if lint.exists():
        # gate 4 reports and is recorded in the manifest; it does not stop a proof copy, since the author's own
        # chapter is linted too and only he edits it
        for args in (("src/en", "--strict"), ("src/fr", "--lang", "fr", "--strict")):
            print("\n$ python " + str(lint) + " " + " ".join(args), flush=True)
            r = subprocess.run([sys.executable, str(lint), *args], cwd=ROOT)
            LINT_OK.append(r.returncode == 0)
    else:
        print("\n(the writing framework's lint is not beside this repository; gate 4 skipped)")
    run("tools/epub_book.py")
    if "--no-pdf" not in sys.argv:
        run("tools/print_book.py")
    manifest()


if __name__ == "__main__":
    main()
