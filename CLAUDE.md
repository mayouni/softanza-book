# CLAUDE.md — Softanza (the book)

**Read this first.** This repository holds the Softanza book, the first of the AYOUNI books.

```
Softanza
The Governed Software Platform of the AI Age
Declare what you know. A court keeps it. The AI model comes last.
```

**Author:** Mansour Ayouni · **Imprint:** AYOUNI · **Series:** first of the AYOUNI books; *Refinement-Oriented Programming* (`../refinement-book/`) follows it, and is to be rewritten on Softanza's foundation.

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

## The voice (the AYOUNI Writing Framework, `../../writing-framework/FRAMEWORK.md`, v0.1)

This book follows the framework's twelve commitments; its own shape is the nine elements. In prose: first person, "you" at the keyboard, the tool as "it";
a question is a beat answered on the page, an exclamation comes only after a run or a reveal (one or two per thousand words; VOICE-01 replaces the brief's
"one per chapter"); long sentence then short verdict; the colon, not the dash; no particular (name, date, place, memory, sentence of the author's) that the record
or the author did not give; one metaphor at a time, the ruling ones mapped once where they first appear (`research/METAPHORS.md`). The lint:
`python ../../writing-framework/tools/style_lint.py src/en` (and `src/fr --lang fr`); it is a gate of `tools/release.py`.

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
- Phase 2 (the evidence) drafted 2026-10-08: chapters 6 to 10, 18 to 22, 28 to 31, all `status: draft`, all blocks kept
  at 93d7a39bd. Memo, open questions and library requests L15 to L41: `sessions/2026-10-08-phase-2-evidence.md`.
- Phase 3 (the languages and the platform) drafted 2026-10-09: chapters 12 to 16 and 23 to 27, all `status: draft`, all blocks
  kept at 93d7a39bd; the cover (`assets/cover/`, made by `tools/make_cover.py` from the author's two images). Memo, open
  questions and library requests L42 to L68: `sessions/2026-10-09-phase-3-languages-and-platform.md`.
- Phase 4 (the appendices) done 2026-10-09: appendices A to G as pages with an `appendix:` letter (E, F, G generated at build),
  a working preface, the nine-element shape restored in chapters 7, 12, 13 and 25. Memo: `sessions/2026-10-09-phase-4-appendices.md`.
- Phase 5 (the agents' form) done 2026-10-09: `book.json` v2 validated against `book.schema.json` at every build, `llms-full-book.txt`, `agents/<slug>.md`.
  Memo: `sessions/2026-10-09-phase-5-agents-form.md`.
- Phase 6 (the French) done 2026-10-09: all 41 pages in `src/fr/`, translated from the English drafts and bannered as such (FRENCH-01); style sheet
  `FRENCH.md`, checker `tools/check_fr.py`. Memo: `sessions/2026-10-09-phase-6-french.md`.
- Phase 7 (the press edition) done 2026-10-09: `python tools/print_book.py` writes a 6.5 x 8.5 in PDF per language (`print/`, not committed). Memo: `sessions/2026-10-09-phase-7-press-edition.md`.
- Phase 8 (the editorial audit) done 2026-10-09: `python tools/book_audit.py` (clean), four [AUTHOR] questions merged to three in chapters 2, 18, 31, glossary citations fixed,
  French terms plane / estate / ledger settled. Memo: `sessions/2026-10-09-phase-8-audit.md`.
- Phase 9 done 2026-10-09: the author's 77 questions answered on his behalf by `research/ANSWER-POLICY.md` (DELEGATE-01; no open question left in the pages, all still `draft`), the ePub (`tools/epub_book.py`),
  the release check (`tools/release.py`). Memo: `sessions/2026-10-09-phase-9-answers.md`.
- Phase 10 done 2026-10-09: the spine verified by fresh readers (513 claims, 124 flagged, fixed in 2, 3, 4, 5, 11, 17, 32, 33; chapter 1 reported to the author), VERIFY-01.
  Memo: `sessions/2026-10-09-phase-10-verification.md`. Chapters outside the spine are not yet verified this way.
- Phase 11 done 2026-10-09: the preface, chapters 6 to 31 outside the spine and appendices A to C verified and fixed the same way (about 3,180 statements checked in the book, 624 flagged and fixed except chapter 1).
  Memo: `sessions/2026-10-09-phase-11-verification-rest.md`. Chapter 1 still carries its flagged statements for the author.
- The AYOUNI Writing Framework (`../../writing-framework/`, v0.1, 2026-10-11) now governs the voice; this book keeps its discipline (C1, C3, C8, C11, C12) and lacks its warmth
  (C2, C4, C6, C9, C10). The plan to bring it in line, phase by phase, with the author's three rulings first: `sessions/2026-10-11-writing-framework-plan.md`.
- The voice pass of 2026-10-11 (plan phases G, E, B, D) is done: roadmaps, bridges, beats, the metaphor register (`research/METAPHORS.md`) and its mappings,
  the noise, in both languages, chapters 2 to 33 and the preface; chapter 1 untouched. Memo: `sessions/2026-10-11-voice-pass.md`; the phase C candidates and
  the places that need the author: `research/voice/CANDIDATES.md`.
- Phase A's rulings (PHASEA-01: the crafter, forge, the seven, chapter 1 corrected, stakes owned; VOICE-01 confirmed by the author on 2026-10-12) and Phase B, the beats
  (`sessions/2026-10-13-phase-b-beats.md`), are done; the 15 particulars of Phase A are answered "the record holds none" (PHASEA-02) and stay open.
- Phase C (a defect per chapter, picked on his behalf, CDEFECT-01) is done: `sessions/2026-10-13-phase-c-defects.md`.
- 2026-10-14: the standing rules below, the type scale (TYPE-01), the cover ruling (COVER-02), the terminology pass (VOICE-05), the pending calls closed on delegation (CLOSE-01), the book read on his behalf by eight fresh readers and fixed (READ-01, `sessions/2026-10-14-reading.md`). Next: the author reads the English and marks pages `read`; the French is then re-checked page by page. Method per chapter
  for any new evidence: a research session writes `research/chNN.md` from the record (brief: `research/BRIEF.md`; its snapshot paths must name
  the current `.cache/stzlib-<sha>`), runs every block it proposes; then the chapter is drafted in one voice from it, built, and committed.
- Session notes: `sessions/YYYY-MM-DD-topic.md`.
- **Public since 2026-10-14** (PUBLISH-01): origin https://github.com/mayouni/softanza-book; the readers at https://mayouni.github.io/ayouni/books/softanza/en/ and /fr/, served by the house repository (`mayouni/ayouni`), which pins one commit. **A push to origin publishes everything pushed: tell the house desk before pushing**, commit locally as before. Only the author gives the go for a push.

## How this session reports (2026-10-15)

A substantive report to the author is a **memo** in Bangalo's style (`D:\GitHubangalo\CLAUDE.md`, "Talk in the memo style"): by / subject / why / did / state / waiting / next / note, and each memo is appended to `D:\GitHub\softanza\memos\YYYY-MM-DD.md`. The author confirmed it to this session directly.

## Standing rules the author has repeated (VOICE-04, RING-01, CODEWRAP-01, TYPE-01, VOICE-05)

- **Never undersell Softanza** in the name of transparency or balance. It is not a research project; parts are in production and parts in development; it is a professional foundation for professional decision-makers. Say stage and direction, never "weak", "falls short", "nothing runs in production".
- **Ring is named only in Appendix H** (the project's history). The language is Haro (for now it uses the syntax of its first facet); the former runtime is "the former host language". The audit enforces it.
- **No horizontal scrollbar in a code block**: long lines wrap.
- **"AI model" and "AI agent" where the bare word is ambiguous** (VOICE-05): first use in a page and wherever another sense of model/agent is near; never in every sentence; Softanza's own terms (domain language model, programmatic agent) keep their names. French: modèle d'IA, agent d'IA.
- **Type size follows semantic level** (TYPE-01): book > part > chapter > section > body; a heading is larger than the text it heads; no label under 12px. One scale, `TYPE` in `tools/build_book.py`, checked at build. Never give a new component a size of its own.
