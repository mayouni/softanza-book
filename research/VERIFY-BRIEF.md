# Verification brief: check one chapter against the record and the library

You are a fresh reader. You did not write this chapter and you do not know what its author hoped. Your job is to find what in it is **not true to the evidence**, and what a careful reader would not understand. You change nothing.

## What you have
- The chapter: `src/en/<file>.md` (and its research file `research/chNN.md`, which lists the sources the chapter was drafted from; it is a lead, not proof).
- The library at the pinned commit, read-only: `D:\GitHub\ayouni\books\softanza-book\.cache\stzlib-93d7a39bd\libraries\stzlib\` (tests under `base\test\`, narrations under `base\doc\narrations\`, engine docs, design docs). Never use any other copy of the library; other sessions write it.
- The run and guard data: `data/book-run.json` (what each code block printed), `data/guards.json` (assertion counts per guard).
- The author's drafts and the rest: `drafts/`, `DECISIONS.md`, `CLAUDE.md`. The site, if a claim cites it: `D:\GitHub\stzsite\` (read-only).
- Do NOT run any build or runner tool, `ring`, `zig` or the book's `tools/`. Do not edit any file. Reading and searching only.

## What to check, claim by claim
Read the chapter whole. For every checkable statement (a number, a date, a name of a file/class/method/guard/narration, a quotation, a commit, "the library does X", "the court refuses Y", a stage word built/designed/absent in section 7 or the front matter), find the evidence and decide:
- **verified** (the evidence says it); **wrong** (the evidence says otherwise); **unsupported** (you cannot find evidence either way within a fair search); **overclaim** (true, but the sentence says more than the evidence: a design stated as built, one run stated as general, "always"/"never" without a test, a loss missing beside a win).
- The rule of the book: *built* = the code exists, a guard exists, a block ran; *designed* = a document says so and the code does not; *absent* = the record holds nothing. A sentence in the wrong stage is an error.
- Quotations must match their source word for word (the book may translate or abbreviate only if it says so).
- Statements "as the field holds it" (section 1) are general knowledge and are marked as such in the text; check that they are marked, and flag any that are specific and false in a way you know (e.g. a wrong date for a well-known tool).
- Numbers printed in prose beside a guard name must equal `data/guards.json`.
- Code blocks: you may read what `data/book-run.json` records for each block; check the prose around a block says what the block shows, not more.

## Also report (briefly) what a reader cannot follow
A sentence that needs a term the book has not yet explained, a paragraph whose point you could not state, a section that repeats another. Three at most, concrete, with the line.

## Report (return it as your final message, under 700 words, no files)
1. `chapter · claims checked: N · verified V · wrong W · unsupported U · overclaim O`
2. Each **wrong / overclaim / unsupported** item, one line each: `line N · "the words" · verdict · evidence (path:line, or "none found, searched X") · the smallest fix`.
3. At most three reading problems.
4. Anything in the chapter that names another repository's product or breaks `CLAUDE.md` rules (substrate, "maker", Zin).
Be exact and brief. Do not praise. Do not pad the verified list: give only the count.
