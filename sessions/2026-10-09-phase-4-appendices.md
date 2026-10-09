# 2026-10-09 · Phase 4, the appendices

```yaml
by:        softanza-book · claude-sonnet-5-5 · 2026-10-09 02:50 UTC+01:00

subject:   Appendices A to G built and running; a working preface; the readers carry the appendices

why:       the author asked for Phase 4 ("Go ahead with Phase 4"); the Phase 3 memo named it as the appendices

did:
  - taught the builder to carry appendices: a source with an `appendix:` letter becomes a page, with its own sidebar
    group, contents rows, a row on the status page, and a place in book.json and llms-book.txt
  - A, the register of innovations: the study's forty-six rows (12.19) with a column of this book's own, the chapter that
    tells each; seven rows are not told, and the appendix says so
  - B, the fourteen house rules: read from the library's own list, three fired live; the other fourteen (the rules of
    writing) set beside them with their state, because the book has two fourteens
  - C, the twenty-two verbs and the constitution: printed from the constitution's `rules.json` (version 3.11, 16 August 2026),
    repository unnamed; seven articles, six families of verbs, six rights, set 31, the forbidden patterns
  - D, the glossary: forty-odd words, each tied to the chapter that shows it; two senses where the record has two
    (door, facet, register)
  - E, F and G generated at every build: 114 distinct guards and their assertions by chapter; 49 distinct narrations checked
    against the library's folder; the chapters as the build reads them, for an agent
  - found, while doing it, that chapters 7, 12, 13 and 25 had one section too many and broke the nine-element shape (the
    decision box, the court box and the doors table fell on the wrong sections); folded the extra section into the form
    section of each and renumbered; every chapter's doors now parse into book.json
  - drafted a working preface from the book that exists, marked for the author to keep or replace

state:
  library:         origin/main 93d7a39bd; engine binaries from the worktree at that commit, built 2026-10-05 20:27
  runtime:         the former host language, version 1.27
  build:           41 source files (preface, 33 chapters, 7 appendices); every runnable block kept its promise; build passes
  words:           about 94,700 (the structure plans 110,000)
  appendix A:      draft · no code · 1,493 words · 0 open questions
  appendix B:      draft · 2 of 2 kept · 1 guard · 859 words
  appendix C:      draft · no code · 982 words · 1 open question
  appendix D:      draft · no code · 1,375 words
  appendix E:      draft · generated · 217 words of its own
  appendix F:      draft · generated · 159 words of its own
  appendix G:      draft · generated · 533 words of its own
  preface:         draft (working page) · written from the book, not from the author's draft
  french:          none; see waiting

waiting:
  - APP-C:  may the twenty-two verbs and the constitution's lists be printed while the repository is not public (the same
            question as chapter 26's)
  - PREFACE: keep this working preface, or replace it with the one you drafted
  - FRENCH: by the structure and the prompt the French is written from the English that the author has marked `read`, never
            from a draft. No chapter is marked read, so no French has been written. Say which chapters to read first, or tell
            me to translate from drafts and mark every French page as such
  - the questions of Phases 1 to 3, unchanged

next:
  - you:  read, and mark `status: read` in a chapter's front matter when it is read; the build then shows it on the status page
  - me:   the French, from the chapters you mark read; the agents' form is already built (book.json, llms-book.txt, Appendix G)

note:      Phases 1 to 4 of the English are drafted. What remains is not writing but reading: the author's, chapter by chapter.
```

## Requests for the library

None new. The appendices read the record and found nothing that is not already a request. One note: Appendix B shows that the rule names come back with hyphens or underscores by rule (request L8, Phase 1).

## What I could not settle

- The register's evidence counts are the study's of 7 October 2026 and I re-counted none; Appendix A says so.
- Appendix C prints another repository's content with the repository unnamed. If the author does not want it printed, the appendix goes and the sentence in chapter 26 stays.
- The preface is mine and not the author's. It says nothing of why the book was written.
