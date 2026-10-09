---
id: the-book-as-data
appendix: G
number: 107
title: The book as data, for the agent that reads it
status: draft
generated: agents
---

This appendix is for an agent that reads the book, and for the person who gives it the book to read. It says what the book offers in a form a machine can take, and what an agent may do with it.

### What there is

Three files sit beside the reader, and each is regenerated at every build.

- **`book.json`** holds, for each chapter, its number and identifier; its part; the law it states, if it is a law chapter; whether it is on the spine; its status; its stage words, built, designed and absent; its guards, each with its path and its assertion count; its promises, which are its blocks of code with the verdict of the last run; its narrations; the study's rulings it rests on; its six doors; and the run's date and counts. A chapter that is a draft says so in its status.
- **`llms-book.txt`** is the same in a short text: one line per chapter, with its status, its guards and the count of blocks that kept their promise.
- **`status.html`** is the page for a person: every chapter with its status, its run, its guards, its words, its open questions and whether it has a French edition.

The appendices are in the same files, each with its letter.

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
