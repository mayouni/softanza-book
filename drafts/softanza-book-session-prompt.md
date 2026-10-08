# Session prompt · Make the Softanza book

**Repository.** The one the author names when starting this session; if none is named, propose a new `softanza-book` repository and wait for the author's yes before creating it. Every path below marked `book/` is relative to that repository's root.

**Attached files.** The author attaches four files to this session's first message, or places them at `book/drafts/` before it starts: `softanza-book-structure.md`, `book-00-preface.md`, `book-01-change-arrives-faster-than-trust.md`, `stzsite-roots-and-achievements.md`. If any is missing, ask for it before Phase 0.

You are opening the session that builds the Softanza book. Read this whole prompt before touching a file. It carries the book's cover, structure, chapter shape, method, voice, format, pipeline, rules and working order, all settled with the author in a previous session on 2026-10-07 and 2026-10-08. Where this prompt and the repository disagree, the repository is right; report the divergence rather than forcing the prompt.

## 0. What you are making

A book that is the third medium of Softanza. The site shows what is; the course teaches how; **the book says why**: the argument behind Softanza, one thesis carried across every plane, with the record as evidence and the reader as judge. It is not the site in print and not the course. Its distinguishing content is the element the site cannot carry: **the decision taken at each rethink, and what was refused.**

The cover, exact and final:

```
Softanza
The Software Makers Platform of the AI Age
Rethinking programming, languages and intelligence, from first principles
```

Back cover: `Born in Africa. Useful to the World!` and `Declare, then govern.`

Series: **the second of the AYOUNI books**, ruled by the author on 2026-10-08. The first is *Refinement-Oriented Programming*. Place the series line on the cover, the title page and the reader's header exactly where the Refine book places its own, with the number changed; record where that is in `book/FORMAT.md`.

French edition, same lines: `Softanza · La plateforme des makers du logiciel à l'ère de l'IA · Repenser la programmation, ses langages et son intelligence depuis les premiers principes`. The site keeps the English word "makers" in French; so does the book.

## 1. Read first, in this order

1. `book/drafts/softanza-book-structure.md`: the final structure, thirty-three chapters and a preface in seven parts, the chapter shape, the appendices, the method. Treat it as the contract.
2. `book/drafts/book-00-preface.md` and `book/drafts/book-01-change-arrives-faster-than-trust.md`: the preface and chapter 1, drafted in the author's voice and corrected against the record. They are your model for voice and for the chapter shape. The author owns them; you may propose edits, never silently change them.
3. `book/drafts/stzsite-roots-and-achievements.md`: the study of twenty-eight rulings the book is built from. Each ruling names the record's files, numbers, guards and the author's decisions for one subject. Every chapter has one or more rulings behind it; read the ruling before writing the chapter.
4. **The Refine book**, in the refine repository (`/ayouni/refine` as the author gives it; `D:\GitHub\refine` on the author's machine). The previous session could not reach that repository, so its files are not named here: you find them. The manuscript is *Refinement-Oriented Programming, a manifesto for software in the agentic era*, by Mansour Ayouni, eighteen chapters and a coda, version 0.1, 2026, which the site calls "first of the AYOUNI books". Find the HTML reader that renders it. Read its page structure, navigation, typography, colour variables, light and dark themes, how a chapter is laid out, how code and figures are shown, how the reader moves between chapters, any language toggle, any progress or print affordance. **Reproduce that reading experience for this book**, not its content. Record what you took from it in `book/FORMAT.md`, file by file, so the lineage is checkable.
5. The site repository `stzsite`: `content/en/*.md`, `content/fr/*.md`, `tools/build.py`, `tools/narrations_run.py`, `tools/build_narration_pages.py`, `data/narrations-run.json`, `agents/index.json`, `llms.txt`. The site's runner is the model for the book's runner; the site's honesty lines are the model for the book's.
6. The library `stzlib/libraries/stzlib`: `base/doc/narrations/` (135 articles, the book's sources), `base/doc/design/` (the design documents the rulings cite), `base/test/` (the guards the chapters name).
7. The vision corpus in the Central repository: `vision/01-KERNEL.md` to `08-NORTH-STAR.md`, `REFERENCE_DESIGN.md`, and the memos the rulings cite for the author's decisions.

If a path does not resolve, the Central protocol's `PATHS.md` is the authority.

## 2. The structure (the contract)

Seven parts, thirty-three chapters, a preface written last, six appendices and a seventh for agents. About 110,000 words. A spine of nine chapters carries the whole argument alone: the four of Part I, the three law chapters (5, 11, 17), the two of Part VII.

- **I. The age, the maker, the method.** 1 Change arrives faster than trust · 2 The software maker · 3 The method, from first principles · 4 The platform in one picture.
- **II. Programming, rethought.** 5 Law: the code adheres to the way a person thinks, and the court judges it whoever wrote it · 6 The mental model, and the metaphors · 7 The writing style, and the seven goals · 8 Functions as linguistic expressions, and scope · 9 Patterns of thought: the Softanzuter, Reaxis and the engines · 10 Programming becomes refinement.
- **III. Languages, rethought.** 11 Law: a language is declared and closed, and whatever speaks it, person or model, is judged by it · 12 A language, declared · 13 Natural, and executable: two directions, one discipline · 14 Knowledge programming · 15 Pattern languages · 16 Seven languages, one door.
- **IV. Intelligence, rethought.** 17 Law: programmatic by default, the model last, admission over generation · 18 The five registers, and conversations that ask · 19 The domain language model · 20 Agents that cannot hurt you · 21 The court: promises, perception, security and performance · 22 Compared, honestly.
- **V. The platform, assembled.** 23 A world, a constellation, a platform, and the architect · 24 Rehearse, then commit · 25 Your users keep their medium · 26 The environment · 27 The engine beneath: three layers, one engine, Haro.
- **VI. Software makers, forged.** 28 A restaurant in Lyon · 29 A bank in Niamey · 30 An organisation in the field · 31 What the projects did not prove.
- **VII. What is owed.** 32 Many minds on one body of work · 33 The one line still owed · the preface.
- **Appendices.** A the register of innovations (46 rows) · B the fourteen house rules · C the twenty-two verbs and the constitution · D the glossary, words name states, never people · E the guards and fixtures cited, by chapter · F the narrations the book argues from · G the book as data, for the agent that reads it.

Each law chapter opens by answering, on its first page, **what the AI age changes in this movement**, and states how its movement depends on the others (the record's logic runs languages first; the cover's order runs from the familiar to the new; say the dependency aloud).

## 3. The shape of every chapter (strict)

1. **The concept, as the field holds it today**, two paragraphs.
2. **The first principle**, one sentence.
3. **The Softanza form**: one running block per claim, each block followed by its promise line `#--> …`, run on a named date at a named commit.
4. **The decision, and what was refused**, from the record's own rulings and memos. Never invented. If the record holds no decision for a chapter, say so and ask the author.
5. **The court**: the guard that proves the chapter, by name and assertion count, read from the test tree at build time, never typed from memory.
6. **The field, and where it leads**: two or three tools, cited and dated, the loss beside the win.
7. **The limit**, in stage words: built, designed, absent.
8. **Six doors**, one line each: the programmer, the analyst, the designer, the decision-maker, the educator, the agent.
9. **The exercise**, one, judged by the tutor's rule: never answered first.

Each chapter links to the site's area and narration for the court's full evidence. The book's code is the argument's minimum; the site's is the court's maximum.

## 4. The method (eight decisions, settled)

1. **The book runs.** Every code block carries its promise; no output is stored in the source; every block is run inside the library at build, block after block in one process per chapter, judged against its `#-->` lines the way `tools/narrations_run.py` judges a narration; a chapter whose promises are not kept **fails the build**. The proof line on every page: run date, commit, blocks kept.
2. **One law per part**, stated, shown, doubted: law chapter first, evidence chapters after, each ending on its limit.
3. **The author's hand.** The author writes the argument and the law of each part; you draft from the record and the rulings, in the author's voice, and mark every draft `DRAFT · not yet read by the author`. A chapter loses that mark only when the author says so. You never present a draft as the author's final word.
4. **Six doors per chapter**, as above.
5. **The narrations are the sources.** Each chapter cites the one to five narrations it argues from, by file name. The narration tells; the book argues; the book never copies a narration.
6. **Writing order by evidence.** Phase order below. Parts II, IV and VI first, Part VII next, Part I last, the preface last of all.
7. **English and French from the first draft.** Chapters 13 and 18 run examples in Arabic and Hausa as well.
8. **The names.** The language is **Haro**; the former host language is named only where history is told, as history. Code is shown in Haro: the name is changed and nothing else; data strings that carry the old name are renamed with their promise and re-run; names the library owns (`load "stzlib.ring"`, the `ring:` skill prefix, `stzRingCodeGraph`) are shown as the library ships them. **The product "Zin" is never named in the book**; its designs are told as "the estate's product designs". No other repository's product is named without the author's ruling.

## 5. The voice (read the two drafts, then hold to this)

First person singular, addressed to "you". Plain words a non-native reader parses; no idiom. Short paragraphs. Examples before explanations, "by example". Bold for a key phrase, at most one or two per section. One exclamation per chapter at most. Precise numbers only when read from the code with their date, otherwise none. Every chapter ends on its limit; every comparison prints the loss. The warmth is in the stories (the wife's song lyrics, two phones and a messaging app, a nine-year-old answering in Hausa) and never in adjectives. When you cannot source a sentence in the author's voice from the record, write `[AUTHOR: …]` and ask, rather than inventing a memory or a feeling.

## 6. The format experience (from the Refine book)

Reproduce the Refine book's reader for this book: same kind of page, navigation, typography family, theme handling, chapter layout and movement between chapters. Then add what this book needs and the Refine book may not have:

- a code cell shows the block as written, its promise lines, and under it the verdict of the build's run (kept · printed something else, shown · raised, shown · not run, why), in the site's exact wording;
- a proof line per chapter: `Run on <date> inside the library at commit <sha>: <k> of <n> blocks kept their promise`;
- a stage word rendered as a badge: built · designed · absent;
- a "decision" block, visually distinct, for element 4;
- a "court" line with the guard name linked to its file and its assertion count;
- the six doors as a compact table;
- a language toggle EN · FR per chapter, each chapter a page in both;
- the spine marked in the navigation (the nine chapters) so a reader can read it alone;
- a reading-progress and a print stylesheet, if the Refine reader has them; if not, add the print stylesheet only;
- `book.json` and `llms-book.txt` for agents: every chapter with its law, its promises, its guards, its stage words, its doors.

Single-file and no-build constraints: follow the Refine reader's choice. Whatever it is, no CDN, no framework, every colour behind a CSS variable, light and dark as first-class themes, the page opens from the file system.

## 7. The pipeline

- Source: one Markdown file per chapter per language, `book/src/en/NN-slug.md` and `book/src/fr/NN-slug.md`, with front matter: `id`, `part`, `number`, `title`, `law` (for law chapters), `spine: true|false`, `narrations: [...]`, `guards: [...]`, `stage`, `status: draft|read|final`, `rulings: [...]` (the study's section numbers).
- Builder: `book/tools/build_book.py`, modelled on the site's `tools/build.py` and `build_narration_pages.py`; produces `book/en/*.html`, `book/fr/*.html`, the reader shell, `book/book.json`, `book/llms-book.txt`.
- Runner: `book/tools/book_run.py`, modelled on the site's `tools/narrations_run.py`; runs every block of every chapter inside the library, records verdicts to `book/data/book-run.json`, and **exits non-zero when any chapter's promises are not all kept**. A block that touches files, the network, input, the clock or chance is marked and its recorded output shown with its run date, never silently skipped.
- Guard reading: `book/tools/book_guards.py` reads each chapter's named guards from the library's test tree and records their assertion counts at build; a guard that does not exist fails the build.
- A status page: `book/status.html`, every chapter with its status, its run verdict, its guard counts, its word count, its FR presence. Regenerated at every build.

## 8. Working order

- **Phase 0, the skeleton.** Read everything in §1. Copy the Refine reader's experience into `book/` with the preface and chapter 1 as its first two pages; wire the runner on chapter 1's two blocks; build; show the author the result and `FORMAT.md`. Stop for the author's verdict on the format before writing a third chapter.
- **Phase 1, the spine.** Chapters 2, 3, 4, 5, 11, 17, 32, 33 in English, drafted from their rulings, each marked DRAFT; run; status page.
- **Phase 2, the evidence with the most built behind it.** Parts II, IV and VI.
- **Phase 3, the rest.** Parts III and V; the appendices A to F generated from the record (the register from the study's 12.19; the house rules from `base/meta/stzCodeRules.ring`; the verbs from the Zui constitution; the guards from the front matter).
- **Phase 4, French.** Every chapter, from the English the author has marked `read`, never from a draft.
- **Phase 5, the agents' form.** `book.json`, `llms-book.txt`, Appendix G.
- The preface is rewritten last, from the book that exists.

A chapter is **done** only when: its code runs on the build; its guards resolve; its FR exists; and the author has read it and said so. The status page prints which of the four each chapter has.

## 9. Rules that override everything above

- **Outputs are never stored in a source file.** The runner writes them to data; the page shows them. A page that restyles an output lies.
- **Never rewrite library code** beyond the name change of §4.8. Never rewrite a narration.
- **Every number is read, never composed.** A count, a date, a commit, an assertion figure comes from a file or a run at build time, with its source. A number you cannot read is written `null` and said so.
- **Never claim a perception.** "The author read it" is a status set by the author, not by you.
- **Stamps from the clock.** Every memo `by:` time, every proof line, every filename date is read from the clock at the moment of writing, never composed.
- **Losses beside wins.** Every comparison in element 6 prints where the field leads.
- **No new rulings by you.** Where the record is silent on a decision, a fact, a name or a date, write `[AUTHOR: …]` in the draft and put the question in your memo's `waiting:`. Three such questions per chapter at most; batch them.
- **The Central protocol applies** if this repository is in the estate: open your mailbox first, read `protocol/README.md` and `QUEUE.md`, speak in the memo style, file your memo, append your cost line at close. Never edit a sibling repository; what a chapter needs from the library (a guard renamed, a promise made judgeable) goes in your memo as a request, never as an edit.

## 10. Report at the end of each phase

A memo: `by / subject / why / did / state / waiting / next / note`. `state:` lists every chapter with its status line from the status page. `waiting:` lists the `[AUTHOR: …]` questions, batched by chapter. `did:` names the files written and the build's verdict (blocks run, kept, failed; guards resolved; chapters done). Nothing is reported as done that the build did not prove.

## 11. Open questions for the author, to ask in your first memo

- Which repository holds the book, and is it public from the first commit or private until a named phase?
- Does the book share the Refine reader's code (copied, with its lineage recorded) or only its experience (rebuilt)?

Begin with Phase 0. Your first message is the memo of what you read, the ref you read it at (branch and commit, for each repository), the Refine reader's files you will reproduce, and the two questions above.
