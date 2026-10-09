# How the author's open questions are answered on his behalf (2026-10-09)

The author said: "answer my pending questions on my behalf". Every `[AUTHOR: ...]` marker in `src/en/` is a question the record could not answer.
They are answered by the rules below. An answer taken this way is a DELEGATED decision: it is recorded as one, the page is not marked
`read`, and the author can overrule any of them by editing the page. Nothing here lets anyone write a sentence and call it the author's.

## The rules

**D1. The record decides; nothing is invented.** Never put in the author's mouth a memory, a motive, a fact about a person, a date or a feeling that no file holds.
When a question asks for one ("is there an earlier moment", "what did it cost you", "who held the phone", "which project goes first", "who will perceive it"), the answer is
*the record does not hold it*: the chapter says what the record holds, in one plain sentence where the gap is, and does not fill it. The marker goes. The gap stays visible in the text.

**D2. "May the chapter say / print X, with its caveat?" is yes, with the caveat printed in the same place.** A loss, a gap or a "not run" is printed beside the claim.

**D3. "Is this sentence yours?" cannot be answered for him.** Print the sentence attributed to its source (the site, the design document, the memo, the study), by name and date, never as his
own words. A principle the chapter states in its own bold sentence stays the chapter's principle, in the book's voice.

**D4. A contract that the code does not meet is amended in the book's account, not hidden.** Where a question is "realised, or amended to match the code", the chapter states what the code does now
and labels the other as *designed*, with the stage word. Never write that something is built that the code does not do.

**D5. Unreviewed foreign-language text is never printed as reviewed.** Print the library's sentences in Arabic, Hausa and the others only with the line "no native speaker has read this, in the code's
words", or do not print them. Never write a sentence in these languages yourself to fill a gap.

**D6. People are not named.** A person named in a record (an owner, a bank officer, a reviewer) is not named in the book. The chapter says "the record names the person" and prints the date and the sentence.

**D7. Content of a repository not yet public (the interface constitution's verbs, rules) is printed as Appendix C already prints it** (APPENDIX-03: read from the rules file, the repository unnamed).
Do not add more of it than the chapter needs.

**D8. The author-owned chapter 1 is not edited.** Where a question asks to correct chapter 1, the answer is: chapter 1 keeps his wording; the other chapter says in one sentence what the record shows
more exactly, and the exact wording is listed once in `sessions/2026-10-09-phase-9-answers.md` under "for the author, chapter 1" so he can edit it himself.

**D9. A question that offers a choice between "show it as a running block" and "describe it", between "open on X" and "open on Y"** is answered by the option that keeps the chapter's runs
unchanged: the current text stays and the other option is dropped. **Do not touch any code fence** (a fence change needs a re-run, and the runner is not yours to start). If an answer would need a code change, do not make it:
write the need in your report.

**D10. A question whose answer is a name, a title, a number or a label** (which of three names, which date, which seven): choose the option that is already in the text or that the record supports most directly, say so in your report,
and print the alternative nowhere.

**D11. The preface stays a working page** (`status: draft`); the marker in it goes and the preface keeps its own sentence that it was written by the session from the book that exists.

## What you do for each marker
1. Read the marker and the paragraph around it, and the chapter's section 4 (the decision) and 7 (the limit) if the answer touches them.
2. Pick the answer by the rules above. Make the smallest edit that states it: usually delete the marker and, where the answer changes the claim, adjust the sentence or add one sentence.
3. Make the same edit in `src/fr/<same file>.md`, in the French of `FRENCH.md`. The French page must keep the same number of paragraphs, headings and list items as the English.
4. After your edits no `[AUTHOR` may remain in your files, in either language.

## What you do not do
- Do not edit a code fence, a front matter key other than `stage:` text (and only if an answer changes a stage claim), or any file outside your list.
- Do not run `build_book.py`, `book_run.py`, `book_guards.py` or `print_book.py` (they share a working directory). You may run `python tools/check_fr.py <number>` and `python tools/book_audit.py`.
- Do not mark a page `read` or `final`.
- Never write: substrate, maker (outside "decision-maker"), the names of other repositories' products. Write "crafter" / « artisan du logiciel ».

## Report
For each marker, one line: `chapter · short question · answer (rule) · what you changed`. Then anything that needs a code change or a run, and anything you could not settle by the rules.
