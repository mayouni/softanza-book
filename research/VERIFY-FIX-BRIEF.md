# Applying a verification report to a chapter

A fresh reader checked one chapter against the record and the library and wrote a report: `research/verify/chNN.md`. Its items are claims of the form *wrong*, *unsupported*, *overclaim*, plus reading problems.
The reader is a model like you; it can be wrong. You decide each item yourself, from the evidence.

## For each item
1. Open the evidence it cites (the library at `.cache/stzlib-93d7a39bd/libraries/stzlib/`, the site at `D:\GitHub\stzsite\`, the drafts, `data/book-run.json`, `data/guards.json`). Spend a few minutes on each, not more.
2. If you **confirm** it: make the smallest edit to the English page that makes the sentence true to the evidence, in the book's voice (first person, plain words, short sentences). Prefer *narrowing* a claim to what the evidence says over deleting it. Where a claim is general knowledge, mark it "(General knowledge, ...)" as the chapter already does.
3. If you **cannot confirm** it (the evidence says the book was right, or you find nothing either way): leave the text and say so in your report with what you looked at.
4. Make the same edit in the same-named file in `src/fr/`, in the French of `FRENCH.md`. The French page keeps the same number of paragraphs, headings, list items and table rows.
5. Reading problems: fix them only when the fix is one sentence (define a term where it first appears, split a long paragraph into two ONLY if you add the same split in French). Skip the rest and say so.

## Rules (they bind you)
- `research/ANSWER-POLICY.md` rules D1 to D6 still hold: invent nothing; attribute a sentence to its source; stage words are the book's (*built* = code, a guard and a run; *designed* = a document and no code; *absent* = nothing in the record); no person named; no other repository's product named; never "substrate", never "maker" (outside "decision-maker"); say "crafter" / « artisan du logiciel ».
- **Do not edit any code fence**, and do not edit chapter 1. Front matter: you may change the text of `stage:` values and add/remove names in `guards:` / `narrations:` / `site:` only when an item requires it and the named file exists; change no other key.
- A number printed in prose beside a guard must equal `data/guards.json`; if you add one, read it there.
- The site has changed since the chapter was drafted (it now says "crafter" and "seven doors", for instance): where the report shows the site changed, either state the present reading with its date (read from the site, 9 October 2026) or state what the page said when the chapter was drafted, with the date. Prefer the present reading.
- Do NOT run `build_book.py`, `book_run.py`, `book_guards.py`, `print_book.py`, `epub_book.py`, `release.py`, `ring` or `zig`. You may run `python tools/check_fr.py <number>` and `python tools/book_audit.py` and must fix any error they report in your files.
- Edit only your chapter's two files (English, French). Use small python scripts: read bytes, replace an exact string asserted to occur once, write bytes back (files use LF).
- Do not mark a page `read`.

## Report (your final message, under 500 words)
`item · confirmed/not confirmed · what you changed (or why not)`, one line each; then the count `confirmed C · not confirmed N · reading problems fixed R`, then anything you could not settle.
