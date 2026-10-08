# CLAUDE.md — Softanza (the book)

**Read this first.** This repository holds the Softanza book, the second of the AYOUNI books.

```
Softanza
The Software Makers Platform of the AI Age
Rethinking programming, languages and intelligence, from first principles
```

**Author:** Mansour Ayouni · **Imprint:** AYOUNI · **Series:** second of the AYOUNI books, after
*Refinement-Oriented Programming* (`../refinement-book/`).

## The contract

The authoritative brief is `drafts/softanza-book-session-prompt.md`. Read it whole before touching a file.
The structure is `drafts/softanza-book-structure.md`, transcribed as data in `src/structure.yaml`. Where the
prompt and the repositories disagree, the repositories are right: report the divergence, do not force the prompt.

In that prompt, a path written `book/...` is relative to **this repository's root**.

## How the book is built

`python tools/build_book.py` — see `README.md`. `FORMAT.md` records what the reader took from the Refine book.

- **The library is run from a snapshot of `origin/main`**, never from `D:\GitHub\stzlib` itself: other sessions
  write that tree all the time, and its checkout sits on their working branches (it was on `ringpp/migrate-rule-a`,
  a side branch, when the book began). `book_common.snapshot` exports the commit into `.cache/` with `git archive`,
  which writes nothing in the library's repo. `LIB_REF` in `tools/book_common.py` names the line.
- **The engine binaries are taken from a worktree at the same commit** when one exists (`D:\GitHub\_wt*`), else
  from the library's checkout; their build time and any engine commit made after it are printed under every proof
  line, with the runtime's version (the former host language's, until Haro runs the library). A pinned engine
  build (`zig build`) was not run: on this machine that build has frozen the system before (see stzlib's
  `CLAUDE.md`, "This machine stops dead under memory pressure"). Do not run it without the author's word.
- **Never background a heavy command here**; a hook refuses it. Stage files by explicit path; a hook refuses
  `git add -A` / `git add .`.

## Rules that bind every session (from the brief, §9)

- Outputs are never stored in a source file. Every number is read, never composed. Stamps come from the clock.
- A draft is marked `status: draft` and shows "Draft · not yet read by the author". Only the author changes it.
- The author owns `drafts/`. Propose edits in the memo; never change a draft silently. The one mechanical change
  made to chapter 1 on its way to `src/` is the fence tag (`ring` → `haro`, and `haro exercise` for the exercise),
  as §4.8 rules.
- The language is Haro; the build fails on a fence still tagged with the former name. "Zin" is never named.
- Never edit a sibling repository. What the book needs from the library goes in the memo as a request.

## Inputs on disk

| File | State |
|---|---|
| `drafts/softanza-book-session-prompt.md` | present |
| `drafts/softanza-book-structure.md` | present |
| `drafts/book-01-change-arrives-faster-than-trust.md` | present (author-owned) |
| `drafts/stzsite-roots-and-achievements.md` | present (received 2026-10-08, after the first message) |
| `drafts/book-00-preface.md` | **missing**; `src/en/00-preface.md` holds its place with `status: missing` |

## Working state

- Phase 0 (the skeleton) built 2026-10-08; its decisions taken on the author's delegation (`DECISIONS.md`).
- Phase 1 (the spine) drafted 2026-10-08: chapters 1, 2, 3, 4, 5, 11, 17, 32, 33, all `status: draft`, all blocks kept
  at origin/main 93d7a39bd. Memo and library requests: `sessions/2026-10-08-phase-1-spine.md`.
- Next: Phase 2, Parts II, IV and VI. Method per chapter: a research session writes `research/chNN.md` from the
  record (brief: `research/BRIEF.md`; its snapshot paths must name the current `.cache/stzlib-<sha>`), runs every
  block it proposes; then the chapter is drafted in one voice from it, built, and committed.
- Session notes: `sessions/YYYY-MM-DD-topic.md`.
