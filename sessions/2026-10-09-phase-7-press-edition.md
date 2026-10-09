# Phase 7 — the press edition (2026-10-09)

The brief's phases end at Phase 5, and Phase 6 was the French. I took Phase 7 to be what the Refine book's last phase was: the PDF.

## What was done
- `tools/print_book.py` composes each language's pages (the same `build_pages` the reader uses) into `print/<lang>.html` and has headless Chrome lay it out.
  Output: `print/softanza-en.pdf` (528 pages) and `print/softanza-fr.pdf` (544 pages), about 11 MB each.
- Cover full bleed (page 1), half title, title page, colophon (proof-copy line, draft count, run commit, blocks kept), contents with real page numbers
  (the PDF is laid out, the first page of each chapter is found in its text, and it is laid out again), part dividers with the part's law, 41 chapters with
  running heads, folios, the back cover. Code cells keep their verdict; the decision, the court and the doors stay whole.
- The reader's own style block is reused, with the code colours turned light for paper. Found and fixed on the way: a table wider than the page made Chrome shrink the whole
  document to 65% (the first PDF came out at 320 pages with a small cover); long file names now wrap.

## Decisions (DECISIONS.md): PRINT-01, PRINT-02, PRINT-03
Format and tool; the proof-copy colophon; the back cover holds only the two lines already in `structure.yaml`.

## What is not done
- A blurb for the back cover and a French line for it (the author's).
- The licence and ISBN lines of a copyright page (not in the record; the colophon says only "© Mansour Ayouni · AYOUNI").
- Fonts are the system's (Georgia, Arial, Consolas). A pinned font set is a choice for the press stage.
- Not checked on paper; I looked at sample pages of both PDFs only.

## For the author
1. Read the English; mark pages `read`; rerun `python tools/print_book.py` and the colophon counts follow.
2. Say whether 528 pages at 6.5 x 8.5 in is the size you want, or whether chapters 24 and 27 (the longest) should be cut for print.
