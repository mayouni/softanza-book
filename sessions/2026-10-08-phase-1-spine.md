# 2026-10-08 · Phase 1, the spine

```yaml
by:        softanza-book · claude-opus-5-5 · 2026-10-08 21:41 UTC+01:00

subject:   the nine spine chapters drafted and running; the book pinned to the library's public line

why:       the author delegated the Phase 0 decisions and asked to continue (2026-10-08 20:33)

did:
  - took the Phase 0 decisions on the author's behalf, each with its reason and how to reverse it (DECISIONS.md)
  - sent eight research sessions, one per chapter, each writing research/chNN.md from the record and running every
    block it proposed; drafted every chapter myself from them, in the author's voice, each marked draft
  - drafted chapters 2, 3, 4, 5, 11, 17, 32 and 33 (with chapter 1, the nine chapters of the spine)
  - found that the library's checkout sat on another session's side branch (ringpp/migrate-rule-a, split from main on
    2026-08-22); pinned the book to origin/main (93d7a39bd) and took the engine build of the worktree at that commit
  - made every proof line state the runtime (the former host language's, version 1.27, read from the runtime) and the
    engine build (built at this commit; one engine change committed after the build, test-runner functions only)
  - built chapter 4's figure from the files that hold its numbers, at build, so no number in it is typed
  - corrected my own draft of chapter 2 against its source: the wife's story is told as her narration tells it
  - showed, rather than hid, four defects as limits with running promises: the domain model answering a rephrased
    question with the wrong answer (ch17); a list in a natural sentence reaching host code (ch11); the max layer's
    classes loaded by no entry file (ch4); the 2022 slide's chain no longer running (ch5, shown in prose)
  - build: 10 pages, 55 of 55 runnable blocks kept their promise at 93d7a39bd; 39 guards resolve; build passes

state:
  library:         origin/main 93d7a39bd; engine binaries from the worktree at that commit, built 2026-10-05 20:27
  preface:         missing · placeholder
  chapter 1:       draft · 1 of 1 kept · 3 guards · 2,189 words · 0 open questions · no French
  chapter 2:       draft · 9 of 9 kept · 5 guards · 2,123 words · 3 open questions · no French
  chapter 3:       draft · 5 of 5 kept · 3 guards · 2,062 words · 1 open question · no French
  chapter 4:       draft · 8 of 8 kept · 5 guards · 1,917 words · 1 open question · no French
  chapter 5:       draft · 7 of 7 kept · 4 guards · 2,259 words · 3 open questions · no French
  chapter 11:      draft · 11 of 11 kept · 7 guards · 2,148 words · 1 open question · no French
  chapter 17:      draft · 8 of 8 kept · 6 guards · 2,196 words · 2 open questions · no French
  chapter 32:      draft · 3 of 3 kept · 3 guards · 2,571 words · 2 open questions · no French
  chapter 33:      draft · 3 of 3 kept · 3 guards · 2,034 words · 2 open questions · no French
  length:          19,538 words in ten pages; the drafts run 1,900 to 2,600 words, under the ~3,300 a chapter
                   averages in the structure's 110,000 words
  done:            0 chapters (none read by the author; no French)

waiting:
  - CH02:  is the site's definition of a maker yours? who demonstrated what on 15 August? who at the bank is the maker,
           and what did they declare? -> author [asked here] proceeding
  - CH03:  the forty-six-row register as Appendix A as it stands, or ruled row by row? -> author [asked here] proceeding
  - CH04:  base inherits core, or the contract amended to "two implementations sharing one engine"? -> author [asked here] proceeding
  - CH05:  the classic form as the one form for new test blocks? the refusal of three 2022 features as Haro grammar,
           yours? the discipline's name? -> author [asked here] proceeding
  - CH11:  has a Hausa speaker read the pack's sentences? -> author [asked here] proceeding
  - CH17:  an earlier moment for "programmatic by default"? may "the model last" be a remote model? -> author [asked here] proceeding
  - CH32:  what the clocks cost, in your words; any reading of the protocol-to-product ratio -> author [asked here] proceeding
  - CH33:  the chapter's principle in your words; which project moves to the engine first, and who perceives it -> author [asked here] proceeding
  - LENGTH-01: keep the drafts compact (about 2,000 words) or grow them toward the structure's 110,000? -> author [asked here] proceeding
  - LIBRARY-REQUESTS: the list below, for the library, through its owners; never edited from here -> stzlib [not routed] proceeding

next:
  - you:  read the spine in order, in the reader: python -m http.server 8737 --directory D:\GitHub\ayouni\books\softanza-book
          then open http://localhost:8737/en/index.html and press "Read the spine only"; or open status.html for the table
  - you:  answer the waiting rows inline in the chapters (each question is an [AUTHOR: ...] marker on its page)
  - me:   Phase 2, the evidence with the most built behind it: Parts II, IV and VI (chapters 6 to 10, 18 to 22, 28 to 31),
          same method (run with: claude-opus-5-5 · effort high)

note:      every chapter now prints the limits the record holds, including four the drafting found by running
```

## Requests for the library (found by running; not edits)

| # | Finding | Where | Seen in |
|---|---|---|---|
| L1 | The 2022 slide's chain does not run: no fluent link from a string's characters to a list of strings (`CharsQR` exists only in the archive); `ToStzListOfStrings()` returns a `stzList` | `base/string` | ch5 |
| L2 | `ReplaceNth(2, "haro", :With = "♥")` panics the engine (`@memcpy arguments alias` in `stz_string.dll`, exit 3); the positional form runs | engine string | ch5 research |
| L3 | A list literal in a natural sentence is evaluated as host code (`eval` at `stzNatural.ring` lines 739, 1098, 1120); already routed as HARO-P15-01 | `base/natural` | ch11 |
| L4 | The Hausa pack stores ɗ double-encoded (`stzNatural.ring` lines 98, 101): correct Hausa spelling fails silently | `base/natural` | ch11 |
| L5 | The domain model at rung one answers the type ("Margherita is a dish.") when a question's verb is not a declared relation, instead of refusing | `base/learning/stzDLM.ring` | ch17 |
| L6 | `stzobject-history-narration.md` promises `[ 13000, 11500, 23, 46 ]` and `45`; the run prints the initial value first and `46` | narration | ch5 |
| L7 | The quantifiers narration calls `AreGreaterThan`; the library spells it `AreGreaterThen` (R14) | narration | ch3 |
| L8 | The house rule is listed as `misspelled-name` and reported as `misspelled_name`; its suggestion prints in lower case | `base/meta/stzCodeRules.ring` lines 27, 1012 | ch32 |
| L9 | The `stx*` classes of max are loaded by no entry file; `stzListXT` raises R53 at construction | `max/` | ch4 |
| L10 | `stkString` calls `StkEngine*` names no engine bridge registers (STZLIB-CORE-ENGINE-01, still open) | `core/string` | ch4 |
| L11 | The site's Hausa list sentence for the educator's door raises "Unsupported object type" at main | education vocabulary | ch2 |
| L12 | `service_delivery_narrated` leaves `_p7test.db` beside itself | `base/test/system` | ch33 research |
| L13 | The listex narration's line 54 promises `FALSE` and prints `1`; guard 33's `Code()` prints an extra line | narration, guard | ch11 research |
| L14 | `SOFTANZA_INTELLIGENCE_ARCHITECTURE.md` and two guard labels still use the old format names `.stzconv`, `.stzdlm` | design, guards | ch17 research |
