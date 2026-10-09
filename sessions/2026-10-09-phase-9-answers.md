# Phase 9 — the author's questions answered on his behalf, and the ePub (2026-10-09)

The author said: "answer my pending questions on my behalf and then go ahead with Phase 9". The brief's phases end at Phase 5, so I took Phase 9 to be the
release: an ePub per language and a release check that runs every gate and writes a manifest.

## Part 1 — the 77 questions
All 77 `[AUTHOR: ...]` markers of the 41 English pages are gone, and so are their French twins. They were answered by the rules in `research/ANSWER-POLICY.md` (decision DELEGATE-01),
applied by six agents on disjoint chapters, then reviewed here. The rules: nothing is invented (no memory, motive, date, person or sentence of the author's that no file holds);
"may the chapter say X with its caveat" is yes, with the caveat printed; a sentence whose author the record does not name is attributed to its source; a contract the code does not meet is
told as designed; unreviewed foreign-language text is never printed as reviewed; no person is named; the author-owned chapter 1 is untouched; no code fence was touched (so no run was needed).
No page is marked `read`: a delegated answer is not a reading.

### What the answers were, by kind
- **Closed by "the record holds none"** (the gap is said in one plain sentence, not filled): the earlier moment behind chapters 14, 17, 18; the seven root causes (7); the cost of the clocks and the
  protocol/product ratio (32); who held the phone, what happened after 25 August, whether the need or the plan came first (28); which central-bank text BCEAO-001 to 003 come from (29);
  who chose against low-code (30); who the bank's crafter is (2); which project moves to the engine first and who will perceive it (33); a human verdict on a gallery picture (21);
  a native speaker's reading of Hausa, Arabic, Turkish, French, Swahili (11, 13, 18).
- **Attributed to the source, not the author** (D3): the crafter definition (2), the classic block recommendation and the refusal of misspelling (5), the Craft-page sentence (6), the doctrine sentence (20),
  the four words (21), the three sentences and the platform-architect line (23), the two clauses (24), the bridge sentence (25), the principle sentences (31, 33), the 2020 plea (13).
- **Told as designed, the code stating what is** (D4): base inheriting core and how a layer is chosen (4, 27), the system scope (8), the seven (16), the three limits of the door (16), the IDE (26), the declarations (31, 33: moved to *absent*).
- **Yes with the caveat** (D2): `.zrfn` as shipped (10), the `order` language run outside the library (12), "built outside, designed for" (11, 12), the withdrawn headline (22), the 7 July benchmark (22), the status-bar loss (26),
  the wide-suite counts, dated 5 October 2026, "in construction" (27), the offline sister package (30), the 610 beside the book's 30 (20), "free" as a plain file with no fee or meter (19), the twenty-two verbs as Appendix C prints them (C, 20, 25, 26).
- **Not printed**: "for the first time in computer science history" was first left out and then restored in chapter 15 as the study's attribution ("a phrase it calls the author's"), after I found it in `drafts/stzsite-roots-and-achievements.md` line 107; the person's name in chapter 31's block.

### Corrections the answers forced
- Chapter 2's bank is a licensee, not a crafter: "Three cases", not "three crafters"; the front matter and section 7 say "the platforms of the three customers".
- Chapters 2, 31, 33 now say the bank "has a product I built beside the library, under the discipline the library now carries, installed under licence", and the restaurant "was delivered a first version … and field-tested it".
- Chapters 31 and 33: the customers' declarations are **absent**. A read-only search of 13 sibling repositories on 9 October 2026 found no declaration file (the chapter does not name them).

### For the author, chapter 1 (not edited, D8)
Chapter 1, line 104, says: "A bank in Niamey runs an assessment platform built with it, under licence, attested by the installation guide we delivered. A restaurant in Lyon runs a platform for neighbourhood commerce whose first demo its owner made himself, on his own phone, over a messaging app."
The record is more exact: the bank has "an organisation-assessment product I built beside the library, under the discipline the library now carries" (it is a Python application that calls nothing of the library); the restaurant "was delivered a first version of a platform and field-tested it"; the checklist for the 15 August demonstration plans it for the owner alone, with his own phone and a messaging app as the support line, and no record says who demonstrated what that day. Chapters 2, 25, 29, 31 and 33 already carry the exact wording; chapter 1 is yours to edit.

### Things the agents flagged, for you to look at
- Chapter 13 §7 says "the author's plea" in the third person, so the book does not assert in your voice an event the record does not hold.
- Chapter 24: "which is mine" is gone from the structure-line clause; restore it if the line is yours.
- Chapter 16 reads "the seven" as the six registry runtimes plus the host (the performance article's count).
- Chapter 28 still says the owner's measurement protocol is "at the seventy-fifth percentile on a mid-range phone"; it is not one of his thresholds, and the limit argument rests on it.
- Chapter 27's wide-suite counts (8,540 of 8,540; 1,253 of 1,253; 3,425 of 5,112; 1,267; 19 rows) are the 5 October memo's, read from `research/ch27.md`, not run here.
- Chapter 8's "61 of 62" for the system-scope guard is read from `research/ch08.md`.
- The French spells Hausa two ways (« hausa » in 11, « haoussa » in 13).
- Library request (chapter 23): truths (`IsTrue`) should be evaluated on instances. Earlier requests L1 to L68 stand.

## Part 2 — the ePub and the release check
- `tools/epub_book.py`: EPUB 3, one file per language (`print/softanza-en.epub`, `softanza-fr.epub`, about 1.4 MB each), from the same pages as the reader and the PDF (verdicts, proof lines, draft banners).
  The tool opens its own file and checks that every part is well-formed XML, every manifest item exists, ids are unique and every internal link points at a file of the book. **epubcheck was not run** (it is not on this machine).
  The reader's links between chapters are rewritten to links between the ePub's files; links to the site or the repository are dropped to plain text. I looked at one chapter in a browser: it renders; I did not look at it in an ePub reader.
- `tools/release.py`: runs, in order, the build (the run and the guards), `book_audit.py`, `check_fr.py --all`, the ePub and the PDFs, then writes `print/release.json` (size and sha256 of each file, the library commit, 282 of 282 blocks kept,
  the page statuses, the book's git commit, whether the tree is dirty). It names the result a **proof copy** while any page is a draft: today all 41 are.
  A bug found on the way: the first manifest read the page statuses from the wrong place and called the book a "release"; fixed and checked.
- The PDFs and ePubs were rebuilt from the final text: English 529 pages, French 543 pages. `print/` is not committed.

## State
build passed · 282 of 282 blocks kept · guards resolved · audit clean · `check_fr` no error · 0 `[AUTHOR` · 41 of 41 pages `draft` (none `read`).

## Waiting
Only your reading: mark pages `read`; the delegated answers are in the pages, in the book's voice, and any can be overruled by editing the page.
