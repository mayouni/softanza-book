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
The structure is `drafts/softanza-book-structure.md` (seven parts, thirty-three chapters, a preface written
last, appendices A–G). Where the prompt and the repositories disagree, the repositories are right: report
the divergence, do not force the prompt.

In that prompt, a path written `book/...` is relative to **this repository's root**.

## Inputs on disk

| File | State |
|---|---|
| `drafts/softanza-book-session-prompt.md` | present |
| `drafts/softanza-book-structure.md` | present |
| `drafts/book-01-change-arrives-faster-than-trust.md` | present (author-owned; propose edits, never change silently) |
| `drafts/book-00-preface.md` | **missing** — ask the author before Phase 0 |
| `drafts/stzsite-roots-and-achievements.md` | **missing** — ask the author before Phase 0 |

## Sibling repositories (read-only from here)

- The Refine book: `../refinement-book/` (reader: `web/index.html`, built by `web/build.py`).
  Divergence to note: the prompt describes the *manifesto* edition (18 chapters + coda). The live reader is
  now the *Teaching Edition* (13 chapters); the manifesto stays at `manuscript/rop-manifesto.md` and builds
  with `python web/build.py --manifesto`. See `../refinement-book/CLAUDE.md`.
- `D:\GitHub\refine`, `D:\GitHub\stzsite`, `D:\GitHub\stzlib` — named in the prompt §1. Never edit a sibling
  repository; requests go in the phase memo.

## Working state

- Phase 0 (skeleton) not started.
- Sessions leave a note in `sessions/YYYY-MM-DD-topic.md`.
