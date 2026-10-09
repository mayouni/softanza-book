# Softanza — the book

*Softanza · The Software Crafters Platform of the AI Age · Rethinking programming, languages and intelligence,
from first principles.* By Mansour Ayouni. The second of the AYOUNI books.

This book runs. Every code block is run inside the Softanza library at a named commit and judged against the
`#-->` promise lines it carries. A chapter whose promises are not kept fails the build.

## Build

```bash
python tools/build_book.py
```

This runs every block (`tools/book_run.py`), reads every named guard (`tools/book_guards.py`), then writes
`en/index.html`, `fr/index.html`, `status.html`, `book.json` and `llms-book.txt`. It exits 1 when a promise is
not kept, a block changed since its last run, a guard does not exist, or a fence still uses the former name.
To re-render from `data/` without running: `python tools/build_book.py --render-only`.

The first run exports the library at its current commit into `.cache/` (334 MB with the engine binaries, measured 2026-10-08;
ignored by git). It needs: Python 3 with PyYAML, `git`, `tar`, the `ring` executable on the PATH, and the
library at `D:/GitHub/stzlib` with its engine built (`tools/book_common.py`, `LIB_REPO`).

## Layout

| Path | What |
|---|---|
| `drafts/` | the files the author handed over: the session prompt, the structure, chapter drafts. Author-owned |
| `src/structure.yaml` | the contents: parts, chapters, spine, cover lines |
| `src/en/NN-slug.md`, `src/en/A-slug.md`, `src/fr/...` | one chapter or appendix per file, with front matter (`appendix: A` for an appendix; `generated:` for one read from the build) |
| `assets/cover/` | the cover, made by `tools/make_cover.py` from the two images in `source/` |
| `tools/` | the builder, the runner, the guard reader, the judge (copied from the site, lineage in its header) |
| `reader/shell.refine.html` | the Refine reader's shell, unchanged; see `FORMAT.md` |
| `data/` | what the runs and the guard reading recorded; pages show outputs from here, never from a source |
| `book.schema.json` | the schema of `book.json`; the build validates against it (`tools/book_schema.py`) |
| `en/`, `fr/`, `index.html`, `status.html`, `book.json`, `llms-book.txt`, `llms-full-book.txt`, `agents/` | built; do not edit by hand |

Open `index.html` from the file system, or serve the folder (`python -m http.server`).
