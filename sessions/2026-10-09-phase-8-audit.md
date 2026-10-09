# Phase 8 — the editorial audit (2026-10-09)

The brief's phases end at Phase 5. Phase 6 was the French, Phase 7 the press edition. Everything left is the author's reading, so I took Phase 8 to be
a check of the whole book against the rules it states, and a settling of the French terms the translators left varying.

## What was done
- `tools/book_audit.py` (changes nothing; exit 1 on an error) checks, in both languages: words the book never writes (substrate, Zin, other repositories' products,
  "maker" outside the decision-maker and the chapter that refuses it); every `chapter N` / `appendix X` reference points at a page that exists; at most three
  [AUTHOR] questions per chapter; no repeated long paragraph; a sentence that names one guard and an assertion count agrees with `data/guards.json`;
  the glossary's cited chapters use the word; stage keys; no TODO left; no date after today; every narration a page cites exists in the library at the pin, and
  every site page it cites exists in both languages.
- It found, and I fixed: four [AUTHOR] questions in each of chapters 2, 18 and 31 (merged to three, English and French; no question was dropped); two glossary entries that cited
  a chapter that never uses the word (candidate: chapter 17 removed; spine: now "the preface").
- Counted against the appendices and found right: 14 house rules (two fourteens, 28 rows), 46 innovations in 7 families, 22 verbs, 33 chapters, 7 parts, 9 on the spine.
- French terms settled in `src/fr/` and `FRENCH.md`: plane = volet (it had been plan, volet, plan sonore); estate = « domaine de projets » (24 bare « domaine » made exact);
  ledger = registre; git commit = commit, the governed act = valider.
- Build passes; `check_fr.py --all` shows no error; audit clean.

## What it cannot check (the author's, or a reader's)
- That a claim is true to the record: every claim was checked by the research sessions at the time; the audit does not re-read the library.
- That the prose is good. No page is marked `read`.

## Waiting
- The questions of Phases 1 to 4, now at most three per chapter (see the five memos and `[AUTHOR` in each page).
