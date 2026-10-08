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

- The library, pinned: `D:\GitHub\ayouni\books\softanza-book\.cache\stzlib-b9d5cd1e4\libraries\stzlib`
  (the commit the book runs at). Prefer it for code, design documents (`base/doc/design/`), narrations
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
cd "D:/GitHub/ayouni/books/softanza-book/.cache/stzlib-b9d5cd1e4/libraries/stzlib/base/test"
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
