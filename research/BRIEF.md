# Research brief for one chapter of the Softanza book (Phase 1)

You are gathering the evidence for ONE chapter of a book. You do not write the chapter. You write a research
file that the chapter's writer will draft from. Everything you report must be read from a file or from a run,
with its path. Never invent a fact, a date, a number, a decision or a quotation. Where the record is silent,
say "the record is silent" and propose an `[AUTHOR: ...]` question.

## Read first

1. `D:\GitHub\ayouni\books\softanza-book\drafts\softanza-book-session-prompt.md` — the method (§3 chapter shape,
   §4 method, §5 voice, §9 rules). Read §3, §4, §5, §9 at least.
2. `D:\GitHub\ayouni\books\softanza-book\drafts\softanza-book-structure.md` — the contract.
3. `D:\GitHub\ayouni\books\softanza-book\src\en\01-change-arrives-faster-than-trust.md` — the model chapter
   (the author's voice and the nine-part shape).
4. `D:\GitHub\ayouni\books\softanza-book\drafts\stzsite-roots-and-achievements.md` — the study of rulings.
   Read the sections named in your task in full; skim the rest by heading.

## Where the record lives (read only; NEVER edit any of these)

- The library, pinned: `D:\GitHub\ayouni\books\softanza-book\.cache\stzlib-93d7a39bd\libraries\stzlib`
  (origin/main, the commit the book runs at; see the book's CLAUDE.md). Prefer it for code, design documents (`base/doc/design/`), narrations
  (`base/doc/narrations/`) and guards (`base/test/`).
- The library's live checkout `D:\GitHub\stzlib` (may differ; only if the snapshot lacks something; say so).
- The site: `D:\GitHub\stzsite` (`content/en/*.md`, `content/fr/*.md`, `llms.txt`).
- The Central repository: `D:\GitHub\softanza` (`vision/01-KERNEL.md` … `08-NORTH-STAR.md`,
  `REFERENCE_DESIGN.md`, `protocol/`, `memos/`, `CLAUDE.md`). `protocol/PATHS.md` resolves paths.
- Other estate repositories exist under `D:\GitHub\` (stz, bangalo, harobanda, harobase, …).

## Running code (the book's blocks must run)

The book shows code in Haro (the language's name; the library's files keep `.ring`, and the executable is
`ring`). Every block you propose must be run, and you report its exact output. Run ONLY inside the snapshot:

```
cd "D:/GitHub/ayouni/books/softanza-book/.cache/stzlib-93d7a39bd/libraries/stzlib/base/test"
mkdir -p _probe_<chapter-number> && cd _probe_<chapter-number>
# write probe.ring whose first line is:   load "../../../max/stzMax.ring"
ring probe.ring
cd .. && rm -rf _probe_<chapter-number>
```

- Use your OWN folder name `_probe_<chapter-number>` (other researchers run at the same time).
- Run in the foreground, one process at a time, never in the background (a hook refuses it; this machine
  freezes under load). Never run `zig build`. Never run a whole test suite; one guard at a time at most.
- The `WARNING: ... not found` lines do not appear in the snapshot; if they do, report it.
- A block's promise is its `#-->` lines; the book's judge compares them with what the block prints
  (whitespace ignored, TRUE/FALSE as 1/0; a list printed item by item equals the bracketed form).
  So propose blocks as `? expression` lines each followed by `#--> exact output`.
- Prefer blocks taken from a narration (`base/doc/narrations/`) or a guard, cited by file, over invented ones.
  Keep each block short (2 to 10 lines). One block per claim of the chapter.
- A block must not touch files, the network, the clock or chance unless the chapter's claim is about that.
- Library-owned names are shown as shipped (`load "stzlib.ring"`, `ring:` prefixes, `stzRingCodeGraph`).
  Data strings carrying the former language's name: rename to "Haro" and re-run so the promise is the run's.

## What to write

Write `D:\GitHub\ayouni\books\softanza-book\research\chNN.md` (NN = two-digit chapter number) with these
sections, in this order:

1. **Sources read** — every file, with path.
2. **The concept as the field holds it** — what programmers and tools mean by it today; two or three named
   tools or practices, each with a citable source and date (prefer the record's own field studies, by file and
   date; general knowledge only when well established, marked "general knowledge").
3. **The first principle** — the one sentence the record returns to, quoted, with its path.
4. **The Softanza form: verified blocks** — each block exactly as the book should show it (Haro), its exact
   output from your run, the claim it supports, and its source (narration or guard file). Say which ran.
5. **The decision, and what was refused** — only from the record's rulings, memos, design documents, charters,
   with path and a short quote (under 25 words each). Distinguish the author's own words from a session's.
6. **The court** — guard file names (stem) that prove the chapter, with path; say what each asserts.
7. **The field, and where it leads** — the loss beside the win, from the record's own honest sections
   ("what the field has that Softanza lacks"), with path and date.
8. **The limit** — what is built, designed, absent, in those words, with evidence.
9. **Six doors** — one line each for: the programmer, the analyst, the designer, the decision-maker, the
   educator, the agent, as the record supports.
10. **The exercise** — one exercise idea, judged by the tutor's rule (never answered first).
11. **Narrations to cite** — one to five article file names from `base/doc/narrations/`, with one line each.
12. **Rulings** — the study's section numbers the chapter rests on.
13. **[AUTHOR] questions** — at most three, only where the record is silent.
14. **Hazards** — anything that would break a rule: a product name of another repository (never name "Zin";
    avoid naming other products, describe them), a number you could not read, a promise that did not run.

Be thorough and exact. Short quotes only. Report at the end, in your final message, the path of your file and
the list of blocks with run status (kept / not).

---

# Phase 2 addendum (read this before the sections above are applied)

**The library the book runs at is `origin/main` (93d7a39bd).** Use the snapshot `.cache/stzlib-93d7a39bd/...`
(the paths above say so). A guard you name in the front matter must exist in that snapshot's `base/test/` tree, and a
block you propose must run THERE. Several things measured in the study (written at 93d7a39) are present now, among
them `base/security/SOFTANZA_THREAT_MODEL.md`, `threat_model_narrated`, `containment_drill_narrated` and
`base/test/testoor/testoor_promises_narrated.ring`.

**Nine chapters are already drafted: read them first** in `D:\GitHub\ayouni\books\softanza-book\src\en\` (1, 2, 3, 4, 5, 11,
17, 32, 33). Do not repeat their blocks; build on them. Their voice is the model: first person, the author's, plain
words, short paragraphs, "you" for the reader, one exclamation per chapter at most, the loss printed beside the win.
A chapter runs about 2,000 words with 3 to 10 blocks; the shape is the nine elements of §3 of the prompt.

**What the drafts already established, so you can point to it and not re-tell it:** the first principle of the method
(declare, then govern; ch3); the six doors and the three makers in a page each (ch2); the platform in one picture
(ch4); the discipline of thinking and writing and the court judging whoever wrote it (ch5); the closed language and the
model judged by it (ch11); programmatic by default, the model last (ch17); the protocol of many minds (ch32); the one
line still owed (ch33).

**Known defects of the library at main: do not build a block on them (a request has been filed).** The 2022 slide's
`CharsQR` does not exist; `ReplaceNth(2, "x", :With = "y")` panics the engine (the positional form runs);
`ReplaceNextOccurrence` does not exist (`ReplaceNextNthOccurrence` does); a list literal in a natural sentence reaches
host code; the Hausa pack cannot read the letter ɗ (use plain `dauke`, `maida`); the domain model answers a reworded
question with the type; `stx*` classes (max) are loaded by no entry file; `stkString` raises; `Some/Most/Few` draw at
random; `AreGreaterThan` is spelled `AreGreaterThen`; the history narration's promise (it prints the initial value first).

**Names the book does not use** (describe them): Zin and everything of its notation; the bank's, the restaurant's and the
organisation's product names and their customers' persons; Harobanda, HaroBase, Aïcha, Makeen, Bangalo Studio, Zing,
Zui (say "the interface constitution"), RingPad, Takamba. The harness may be described, not named. The author's own
first book, *Refinement-Oriented Programming*, may be named (it is the book this one follows). "Refine" the product is
another repository's: say "the refinement layer" or "the library verb". Never the word "substrate".

**A block that does not run on main is evidence, not a block**: put it in §8 as a limit with the failure you saw, and
propose the nearest block that runs. Report requests for the library in your hazards; never edit it.

**Do not run more than one `ring` process at a time, and never any `zig` command.** Put your probe in a folder named for
your chapter (`_probe_NN`) and remove it when done. If a guard leaves a file beside itself, remove it and say so.

**Be economical**: you have no need to read every file the study cites; read the sections named in your task, the
narrations and guards you will use, and the sources for the decision and the limit. Write the research file as
specified. Short quotes only (under 25 words each), always with path. Report your file path and the block table.

**Two corrections, 2026-10-08 22:10.** (1) The author ruled that the book says **crafter**, not "maker": the cover is
"The Software Crafters Platform of the AI Age", chapter 2 is "The software crafter", Part VI is "Software crafters, forged".
The structure and the prompt in `drafts/` still say "makers" (they are the author's, untouched): treat "crafter" as current
in anything you write; "decision-maker" is a door's name and stays. (2) The library is pinned by commit, not by branch:
`origin/main` has moved since (five fix branches merged at 21:34 to 21:43) and it changes the max layer; the snapshot
`.cache/stzlib-93d7a39bd` is the only library the book runs at. Never look at the live checkout for a block.
