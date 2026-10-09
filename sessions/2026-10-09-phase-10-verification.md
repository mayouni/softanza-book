# Phase 10 — an independent verification of the spine (2026-10-09)

The brief's phases end at Phase 5. Phases 6 to 9 were the French, the PDF, the audit, and the answers with the ePub. Phase 10 I took to be what none of them was: a read of the nine spine chapters by readers
who did not write them and who were given the evidence, not my conclusions (`research/VERIFY-BRIEF.md`). They changed nothing; they reported.

## What was done
1. Nine fresh agents, one per spine chapter (1, 2, 3, 4, 5, 11, 17, 32, 33), each checked every checkable claim against the library at the pin (read-only), the run and guard data, the drafts and the site, and
   classified it: verified / wrong / unsupported / overclaim. Their reports are in `research/verify/chNN.md`.
2. Eight fixer agents (chapter 1 excepted) re-checked each finding against its cited evidence before touching the text, applied the smallest fix in English and French, and reported
   (`research/verify/FIXERS-REPORTS.md`, brief `research/VERIFY-FIX-BRIEF.md`). I made two small fixes myself (chapter 4's last sentence; the areas figure's label).

## The count
| chapter | claims | verified | wrong | unsupported | overclaim |
|---|---|---|---|---|---|
| 1 (author's, not edited) | 43 | 29 | 2 | 1 | 11 |
| 2 | 64 | 45 | 6 | 4 | 9 |
| 3 | 56 | 39 | 3 | 2 | 12 |
| 4 | 61 | 47 | 3 | 3 | 8 |
| 5 | 52 | 40 | 2 | 1 | 9 |
| 11 | 55 | 39 | 2 | 5 | 9 |
| 17 | 62 | 54 | 0 | 2 | 6 |
| 32 | 62 | 47 | 3 | 3 | 9 |
| 33 | 58 | 49 | 1 | 3 | 5 |
| **total** | **513** | **389 (76%)** | **22** | **24** | **78** |

124 statements were flagged. In the eight chapters I could edit, the fixers confirmed all but five against the evidence (three in chapter 2, one each in chapters 4 and 11, which stood as written) and narrowed the claim, corrected it or marked it as general knowledge. Nothing was deleted
that a narrower sentence could keep. No code fence changed, so no block needed a new run; the build re-ran every block and all 282 kept their promise.

## What the readers found, by kind
- **The site moved under the chapter.** Chapter 2 said the site had six doors and used "maker"; the site now says seven doors and "crafter". Dated readings of 9 October 2026 now stand. The journey pages exist (nine of them), so
  chapter 2's stage for them changed from designed to built, with only "each step run in order under a guard" still designed. The site now has an innovations page (47 rows; the book's Appendix A has 46), and chapter 3's "absent" is narrowed to "each concept with a run proof".
- **A design said as built.** Chapter 4's "the layer contract's rule that base inherits core" is the author's convention, not the contract's text (the contract says "inheritance or delegation"); "every feature implemented once, in the engine" is the engine's design rule with a migration still pending;
  64 of 334 atlas lanes have no proof line, so "each rated with its proof line" became "most".
- **A guard credited with more than it proves.** `00_orgchart_narrated` covers positions, reporting lines and vacancies, not the BCEAO rules; the Hausa assertions of `semantic_resolver_narrated` are its last scenario and the guard stops before them; the "four blocks on two guards" of chapter 3 are three.
- **A claim the evidence does not make.** "Published the same day" (an internal memo), "the court caught me" (the study did), "a year" (a week), "for years" (no duration in the record), "a few neighbours" (nowhere), "every exercise is checked by running" (beside "0 of 35 reviewed").
- **Unmarked general knowledge**: marked as such.

## For the author: chapter 1 (not edited; the report is `research/verify/ch01.md`)
Two statements are wrong, one unsupported, eleven overclaim. The ones that matter most:
1. **Line 76**: "the runtime beneath Softanza is now one we own, written in Zig, wearing the old surface…, under a new name, Haro" says built what the record holds as in construction: Haro does not run the library (chapter 27 says so). Proposed: "is being replaced by one we own, in Zig, a charter and a spike so far; the old surface is kept so that the code I wrote keeps running (in construction)". Same line: "the first of five commitments I made that summer" has no source for five.
2. **Line 56**: "one register of answer among five, and the other four, an option chosen, a data structure given, a formula written, a sentence spoken…" mixes the model with the five registers (option, structure, formula, sentence, example). Chapter 18 marks formula and example absent.
3. **Line 54**: "The guard that proves this sequence, `safeworld_narrated`" is about reversibility, the registration gate, the plan and the commit by an actor; it has no restaurant, messages or supplier rules. "You can watch it run on the site": the site shows a recorded run.
4. **Line 104**: "assessment platform built with it" against line 106's "a Python application" (the book's own chapters 2, 25, 29, 31, 33 carry the exact wording).
5. **Lines 78, 80, 94, 96, 114** claim as done: the court that caught the layers (the study did; no layer court exists), "one door, governed" (designed), "every answer is checked by a grammar" (designed), "an invalid sentence cannot be spoken at all" (only for the grammars compiled today), "a generator that cannot drift" (a verifier of what a machine can check).
Each has a proposed fix in the report. Chapter 1 stays your text; edit what you agree with, and the French follows.

## Still open after the fixes
- The areas figure's caption does not say the atlas numbers (28 areas, 334 lanes) come from the site at commit 0e72e2e2c of 30 September 2026, not from the pinned library. One sentence to add in chapter 4.
- Chapter 4: "twelve" names in the core claim comes only from the drafts; left out.
- Chapter 11: "principal" is the estate's term and is not introduced; chapter 32 may be where to define it. Two machine terms in chapter 11 still need a definition from an earlier chapter.
- Chapter 2 §8 repeats §3's six entries almost line for line; fixing it is a restructure, left.
- Chapters 6 to 10, 12 to 16, 18 to 31 were **not** verified this way. The same two briefs apply to them; it is eight more fixer agents' work.

## State
build passed · 282 of 282 blocks kept · audit clean · `check_fr` no error · all 41 pages `draft`. The PDFs and ePubs in `print/` predate these edits; `python tools/release.py` rebuilds them.
