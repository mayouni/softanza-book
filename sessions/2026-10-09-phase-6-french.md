# Phase 6 — the French edition (2026-10-09)

## What was done
- All 41 pages (preface, chapters 1 to 33, appendices A to G) exist in `src/fr/`, same file names as `src/en/`.
- `FRENCH.md` is the style sheet; `tools/check_fr.py` compares each French page to its English one (front matter, code fences
  byte for byte, headings, table rows, list items, `[AUTHOR` markers). `python tools/check_fr.py --all`: no error, a few harmless warnings.
- Code is never translated; the runner reuses the English run when the block hashes match (FRENCH-03). Appendices E, F, G are generated in French.
- French part titles (`title_fr`), French UI strings, French cover (`assets/cover/cover.fr.png`).

## Decisions (DECISIONS.md)
- FRENCH-01: the prompt writes the French only from English marked `read`; none is. I translated the drafts and marked every French
  page "traduit d'un brouillon anglais, pas encore lu par l'auteur". A French page is never `read`/`final` before its English page is.
  The preface sentence that said otherwise was corrected in both languages.
- FRENCH-02: the vocabulary is the site's own French (tribunal, garde, porte, jumeau, monde, raffinement, artisan du logiciel).
- FRENCH-03: French code byte-identical.

## Terms to confirm (the translators varied; normalised where it was safe)
- commit as a git act = « commit / commité »; commit as the governed act = « valider / validation » (ch1, 20, 21, 24, 28, C, D).
- ruling = « décision » (never « arbitrage »); workbench = « atelier »; scope = « portée »; record = « le dossier ».
- Still varying: "plane" (plan / volet / plan sonore); "estate" (le domaine de projets / le domaine); registry and ledger both « registre ».

## For the author
1. Read the English pages, mark them `read`; then each French page is re-checked against the final English.
2. Confirm the terms above and the French line « artisans du logiciel ».
3. The questions in each chapter's memo are unchanged; the French carries the same `[AUTHOR` markers.
