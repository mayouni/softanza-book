# 2026-10-09 · Phase 5, the agents' form

```yaml
by:        softanza-book · claude-sonnet-5-5 · 2026-10-09 03:05 UTC+01:00

subject:   the book as data, for the agent that reads it: book.json v2, its schema, the full text, one file per page

why:       the author asked for Phase 5 ("Go ahead with Phase 5"); the prompt's Phase 5 is book.json, llms-book.txt and Appendix G

did:
  - book.json is now schema "softanza-book/2": one entry for each of the 41 pages (preface, 33 chapters, 7 appendices), each
    with its slug, kind, first principle, stage words, guards with their counts, promises (the code, the lines it promised,
    what the last run printed, the verdict, what it touches), narrations, rulings, six doors, sections, open questions, words,
    whether a French edition exists, and where its text is; at the head, seven rules for an agent and the runtime
  - book.schema.json describes it, tools/book_schema.py validates it, and the build fails if book.json does not match
  - llms-book.txt gives the rules and one line per page with its principle; llms-full-book.txt holds every page as text with the
    verdict under each block (about 730 KB); agents/<slug>.md holds one page each
  - the reader's overview now links to the agents' files; Appendix G describes them
  - the runtime is named in book.json for what it is ("the former host language", version 1.27), not by its former name

state:
  build:           41 source files; every runnable block kept its promise; book.json validates against its schema
  not changed:     no chapter text, no run

waiting:
  - the questions of Phases 1 to 4, unchanged (see the five memos)
  - FRENCH: still blocked on the author's reading; tell me which chapters to read first, or to translate from the drafts
    with every French page marked as such

next:
  - you:  read; mark `status: read` in a chapter's front matter; book.json, the status page and the agents' files then show it
  - me:   the French, from the chapters you mark read
```

No library requests, and nothing new that I could not settle. One thing to know: `book.json` is 415 KB and `llms-full-book.txt` 730 KB, so they are the book's whole text and every run's output, and they change at every build; a commit of them is a commit of the build.
