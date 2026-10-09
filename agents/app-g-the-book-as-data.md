# The book as data, for the agent that reads it

Source: Appendix G. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

This appendix is for an agent that reads the book, and for the person who gives it the book to read. It says what the book offers in a form a machine can take, and what an agent may do with it.

### What there is

Files sit beside the reader, and each is regenerated at every build.

- **`book.json`** holds, for each page of the book, a chapter, the preface or an appendix: its number, identifier and slug; its kind; its part; the law it states, if it is a law chapter; the first principle it states, in one sentence; whether it is on the spine; its status; its stage words, built, designed and absent; its guards, each with its path and its assertion count; its promises, which are its blocks of code with the lines they promised, what the last run printed, and the verdict; its narrations; the study's rulings it rests on; its six doors; its sections; its open questions, which are the places the record could not answer; its word count; whether it has a French edition; and where its text is. A chapter that is a draft says so in its status.
- **`book.schema.json`** describes `book.json`, and the build validates the file against it. A build that produces a `book.json` that does not match its schema fails.
- **`llms-book.txt`** is a short text: the rules for an agent, then one line per page with its status, its guards and the count of blocks that kept their promise, and its principle.
- **`llms-full-book.txt`** is every page as text, one after the other, with the verdict of the last run written under each block of code. **`agents/<slug>.md`** is the same, one page per file; the slug is in `book.json`.
- **`status.html`** is the page for a person: every chapter with its status, its run, its guards, its words, its open questions and whether it has a French edition.

### What a promise is

A block of code that begins with the tag `haro` is run inside the library at the commit named under the chapter's title. The lines that begin with `#-->` are the block's promise: what the block printed when the author wrote it. The judge compares the promise with the run, ignoring spacing, and reading `TRUE` and `FALSE` as 1 and 0. A promise is kept, or it differs, or the block raised, or it stopped. A block that is marked as an exercise is not run, and a block that touches files, the clock or chance says so, and shows the output that was recorded on its date.

An agent that quotes a promise should quote its verdict with it.

### What an agent may do, and may not

- **You may quote any cell.** A table of this book is data. A row that says "absent" is a row you may repeat as absent.
- **You may not turn an absent cell into a present one.** The record will find your sentence and the missing file side by side, and the book says so in chapter 31.
- **You may rely on the stage words.** Built means the code, a guard and a run. Designed means a document and nothing that runs. Absent means that I looked, and say how far.
- **You may rely on a promise only with its verdict, and only at the commit it names.** A number that the book prints is a number read from a file or a run, at the date the page gives.
- **A draft is a draft.** A chapter marked as a draft is not the author's final word, and "the author read it" is a status that only the author sets.

### The chapters, as the build reads them

The table below is generated at every build from the same data as `book.json`.

| # | Id | Part | Status | Spine | Blocks kept | Guards | Doors |
|---|---|---|---|---|---|---|---|
|  | `preface` | 0 | draft | yes | no code | 0 | 0 |
| 1 | `change-arrives-faster-than-trust` | 1 | draft | yes | 1 of 1 | 3 | 6 |
| 2 | `the-software-crafter` | 1 | draft | yes | 9 of 9 | 5 | 6 |
| 3 | `the-method-from-first-principles` | 1 | draft | yes | 5 of 5 | 3 | 6 |
| 4 | `the-platform-in-one-picture` | 1 | draft | yes | 8 of 8 | 5 | 6 |
| 5 | `law-the-code-adheres-to-the-way-a-person-thinks` | 2 | draft | yes | 7 of 7 | 4 | 6 |
| 6 | `the-mental-model-and-the-metaphors` | 2 | draft |  | 7 of 7 | 6 | 6 |
| 7 | `the-writing-style-and-the-seven-goals` | 2 | draft |  | 10 of 10 | 10 | 6 |
| 8 | `functions-as-linguistic-expressions-and-scope` | 2 | draft |  | 13 of 13 | 5 | 6 |
| 9 | `patterns-of-thought` | 2 | draft |  | 8 of 8 | 6 | 6 |
| 10 | `programming-becomes-refinement` | 2 | draft |  | 9 of 9 | 3 | 6 |
| 11 | `law-a-language-is-declared-and-closed` | 3 | draft | yes | 11 of 11 | 7 | 6 |
| 12 | `a-language-declared` | 3 | draft |  | 8 of 8 | 5 | 6 |
| 13 | `natural-and-executable` | 3 | draft |  | 17 of 17 | 7 | 6 |
| 14 | `knowledge-programming` | 3 | draft |  | 13 of 13 | 3 | 6 |
| 15 | `pattern-languages` | 3 | draft |  | 13 of 13 | 5 | 6 |
| 16 | `seven-languages-one-door` | 3 | draft |  | 10 of 10 | 5 | 6 |
| 17 | `law-programmatic-by-default` | 4 | draft | yes | 8 of 8 | 6 | 6 |
| 18 | `the-five-registers` | 4 | draft |  | 15 of 15 | 4 | 6 |
| 19 | `the-domain-language-model` | 4 | draft |  | 7 of 7 | 5 | 6 |
| 20 | `agents-that-cannot-hurt-you` | 4 | draft |  | 9 of 9 | 5 | 6 |
| 21 | `the-court` | 4 | draft |  | 7 of 7 | 9 | 6 |
| 22 | `compared-honestly` | 4 | draft |  | 5 of 5 | 4 | 6 |
| 23 | `a-world-a-constellation-a-platform` | 5 | draft |  | 10 of 10 | 5 | 6 |
| 24 | `rehearse-then-commit` | 5 | draft |  | 11 of 11 | 7 | 6 |
| 25 | `your-users-keep-their-medium` | 5 | draft |  | 11 of 11 | 6 | 6 |
| 26 | `the-environment` | 5 | draft |  | 10 of 10 | 6 | 6 |
| 27 | `the-engine-beneath` | 5 | draft |  | 9 of 9 | 4 | 6 |
| 28 | `a-restaurant-in-lyon` | 6 | draft |  | 5 of 5 | 5 | 6 |
| 29 | `a-bank-in-niamey` | 6 | draft |  | 6 of 6 | 6 | 6 |
| 30 | `an-organisation-in-the-field` | 6 | draft |  | 7 of 7 | 6 | 6 |
| 31 | `what-the-projects-did-not-prove` | 6 | draft |  | 5 of 5 | 7 | 6 |
| 32 | `many-minds-on-one-body-of-work` | 7 | draft | yes | 3 of 3 | 3 | 6 |
| 33 | `the-one-line-still-owed` | 7 | draft | yes | 3 of 3 | 3 | 6 |
