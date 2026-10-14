# Group H, read as a reader: appendices E, F, G, H and the map

Read on 2026-10-14 as the AI agent the book addresses, from the files as published to that agent, then as the author. Totals recomputed from the tables; cross references followed; `python tools/book_audit.py` run once (clean). Nothing changed.

## agents/app-e-the-guards-and-fixtures-cited.md

**1. What I remember.** A guard is a test file the build finds at the pinned commit and counts; a missing guard breaks the build. Thirty-three tables, one per chapter, 114 distinct guards and 3,359 assertions, and the warning that a count is a reading of the file, not a run. I could restate the opening paragraph without looking.

**3. Where I doubted.** The totals: I summed the tables myself and got 114 distinct guards and 3,359 assertions, the figures the page prints. "The few I ran myself are named in the chapters that rely on them" (opening): true where I checked (chapter 27), but on this page a reader cannot tell a run guard from a counted one; a mark would end the doubt. The title promises "guards and fixtures" and the page lists no fixture: one paragraph says what they are and no table names one. Either the title loses "fixtures" or the page gains them.

**6. Errors of fact or form.** Every path ends in `.ring`, 114 times. The page is right to print the library's names, but Appendix H opens with "This is the one page of the book that names the language". One sentence here ("the extension is the former runtime's, until Haro runs the library") would keep H's claim true in spirit. One guard name is the library's own truncation, `466_keeping_the_history_of_updates_of_a_softanza_objec` (chapter 5); a reader will report it as the book's typo unless told it is the file's. "Nothing in it is typed" sits two lines above "The few I ran myself": say "no figure in it is typed".

**Would a reader open it; does every entry point to a page that exists.** The agent opens it: it is the index from a claim to its proof, and chapter 31's rule ("quote any cell") needs it. Every section heading is a chapter 1 to 33 that exists in `agents/`; every path was checked by the build at the pin.

**8. Verdict.** `ready after the items above`: the figures hold; the title and the extension need a sentence each.

## agents/app-f-the-narrations-the-book-argues-from.md

**1. What I remember.** A narration is one of the author's articles in the library's documentation folder, not a test; 135 exist and the book argues from 50; the word "narration" was later taken by the executable guards and chapter 21 refused that. Each chapter runs its own blocks, not the article's.

**3. Where I doubted.** "There are about a hundred and thirty-five of them": I counted the folder at the pin and there are 135 exactly, and chapter 21 prints 135. "About" hedges a number the build could read. The column "In the library at the pin" says "yes" fifty times out of fifty: the summary already says "Every name is a file", so the column carries nothing, and the sentence "Where a name is not a file of that folder, this appendix says so" promises a case the page never has. Either drop the column or keep it only when a name is missing. Chapter 1 has no table and no sentence says why, while Appendix E gives chapter 1 three guards; the agent that compares the two appendices will ask.

**6. Errors of fact or form.** The third paragraph repeats the first almost word for word: "A narration is the author's article; its code is the old surface, and several of its blocks no longer run at the pin" after "The code in them is the old surface" and "Several no longer run at that commit". One of the two should go. Three names carry the former language in their file name (`stznatural-vs-ring-naturallib.md`, four chapters; `stzexcis-polyglot-programming-in-ring.md`; `stz-pycode-bridging-ring-and-python-narration.md`), and two carry the library's own typos (`stzwalker-beyond-loops-the -walker-metaphor.md` with a space, `stztablex-pattern-langauge-for-tables.md.md`). They are right as printed, and the audit is clean; "names are printed as the library spells them" would stop a reader from reporting them as the book's errors. The cross reference lands: chapter 21, "I refused the word for the thing it was not".

**Would a reader open it; does every entry point to a page that exists.** Less than E. The agent opens it once to learn that the articles can drift and the guards cannot, which the opening says; the fifty rows after are file names with no path and no link. Every heading is a chapter 2 to 33 that exists; every name is a file at the pin (checked in the snapshot).

**8. Verdict.** `ready after the items above`: a dead column, a doubled paragraph, a hedge on an exact number.

## agents/app-g-the-book-as-data.md

**1. What I remember.** Six files beside the reader, regenerated at every build; what a promise is (`haro` block, `#-->` lines, four verdicts, `TRUE` read as 1); five rules for an agent, of which "You may not turn an absent cell into a present one" is the one I will keep; a table of 34 rows, every page draft, every block kept, six doors per chapter.

**3. Where I doubted.** "Absent means that I looked, and say how far" (What an AI agent may do): the sentence does not parse; who says how far? The map, `llms-book.txt`, has the same rule in other words ("the record was searched, and the chapter says how far"). Two texts for one rule, and the agent will read both. "The book says so in chapter 31": it does, under "The agent." at chapter 31's close, "will find your sentence and the missing file side by side". The sentence that lists what `book.json` holds (What there is, first bullet) runs twenty clauses on semicolons; I read it twice and could not say whether "its stage words" was one field or three. A list would do what the sentence cannot. The table, "The chapters, as the build reads them", holds no appendix, while the first bullet says `book.json` has "an appendix" too: eight rows fewer than the file holds.

**6. Errors of fact or form.** The "Doors" column reads 6 on thirty-three rows and 0 on one; the "Spine" column is blank where it is not "yes"; the "Part" column is a digit with no part name anywhere on the page. The six files named exist at the root, and the 34 slugs match the 34 files in `agents/`. "`TRUE` and `FALSE` as 1 and 0" is the one place where the judge's leniency is written down; good that it is.

**Would a reader open it; does every entry point to a page that exists.** The agent opens this first, and it is the right first page: the contract is five bullets long. The person who gives the book to an agent opens it too. Every row points to a page that exists.

**8. Verdict.** `ready after the items above`: one broken sentence in the rules, one sentence that should be a list, a table short of its appendices.

## src/en/H-the-projects-history.md

**1. What I remember.** Softanza was born on Ring, which the author taught, promoted and wrote a book about. Real projects showed three limits (performance, typing, build), the language's direction could not be influenced, Ring++ did not take, and governance turned out to be a design property, so the project built its own engine in Zig and declares Haro as the destination. The library still runs on the first runtime, 1.27, and the test of the promise is that Haro runs the narrated tests. I can restate it in one breath: it is 414 words, and every one carries.

**2. Where I lost the thread.** "The direction of a language belongs to its owner, and ours could not be influenced" (What real projects taught): "ours" reads as "our direction" and means "our language's", and the sentence holds the two meanings for a beat. "Three things, and they are the reasons": reasons for what has not been said yet on this page; the first paragraph only said the platform "is going where that language cannot follow". "Under all three sits the engine in Zig, which does the computation once" (The path): Ring the language does not sit on Softanza's engine; the library does, under all three syntaxes. And "once" is chapter 27's word ("implemented once, in the engine") and arrives here unexplained.

**3. Where I doubted.** "Real projects showed that Ring was not suited to the challenges of modern applications" followed by "The project's own sessions measured them": the one sentence a reader from that community will contest, and the page gives no number and no chapter. Chapter 27 has numbers for the engine, not for the limits of the former runtime; if a measurement exists, name where; if it does not, say "showed" without "measured". The particulars are the author's own: "nine months", "published by Apress in 2020", "In 2021 I described", "In 2022 the first presentation", and the quoted "a best friend of existing Ring programmers". I could check none of them; the author can, in a minute. "Ring's simplicity and its multiparadigm expressiveness are two things Softanza keeps, because they were never the problem" is the best-judged sentence on the page: the former language gets its due and the move is not undersold.

**4. Where it moved me.** The close: "Softanza says thank you to the language it grew up on, and goes where its users' sovereignty requires." And the four fragments of the third lesson: "An open core. Charters ratified in public. Every decision in a dated record. Every claim linked to its proof." Nothing to skip.

**5. The code.** None, rightly.

**6. Errors of fact or form.** "Ring++ is the bridge, in construction": a calque of *en construction*; English says "under construction". "The library's narrated tests are the test of that promise": the book's word is guard, and Appendix F has just spent a paragraph taking "narration" away from the executable files; "narrated test" here hands it back (chapter 30 uses the phrase once, too). "This is the one page of the book that names the language": in letter, E names its extension 114 times, F names it in three file names, and chapter 10 runs `stzRingCodeGraph`. The claim is true of the prose and the audit agrees; "the one page that tells of the language" would be true of everything. "version 1.27" matches the build line of the map. The chapter 27 reference lands.

**7. The door.** There is none: `book.json` gives this page `doors: {}`. This is the one appendix that reads like a chapter, and the decision-maker's two lines are already inside it ("fails the due diligence that regulated domains require"). If any appendix earns doors, this one does; if none does, that is a rule and it holds.

**8. Verdict.** `ready after the items above`: one claim without its measure, one calque, one word returned to the wrong thing, and the particulars for the author to confirm.

## llms-book.txt

**Does the map tell a reader what the book is, in order?** It tells what each page is and in what order, with its status, guards, run and principle, and all 42 paths under `agents/` exist. What it does not tell is the shape. The book has seven parts (`book.json` numbers them, Appendix G prints the digit), and the map shows 33 chapters flat, with `[spine]` the only structure. A reader who stops at the map does not know that chapters 5 to 10 are one part, or that 28 to 31 are the projects. Seven headings would do it.

**Does every summary match its title?** Mostly, with these exceptions, which are the items for the author.

- Chapters 5 and 7 carry the same principle: "what you think is what you write." and "What you think is what you write." One of the two pages has lost its own sentence; the map shows which.
- Chapters 25 and 26 end on the same clause, "renderings, never verbs"; a reader cannot tell the two pages apart from the map.
- Chapter 1's principle is its title again ("change arrives faster than trust."); chapter 28's ("deliver small, fast and useful...") and chapter 30's ("the AI agent proposes, and a person decides.") do not say that the page is a restaurant or an organisation: neither title nor principle says what the reader will find.
- The preface and the eight appendices have no summary line at all.
- The principles start in lower case on nine lines (1, 2, 3, 4, 5, 10, 28, 30, 32) and in upper case on the rest.

**Errors of form.** The tagline line has a double period: "The AI model comes last.. By Mansour Ayouni" (the tagline ends in a period and the build adds another). "Haro does not run the library yet" is said in the header and again as rule six. Rule three's wording of "absent" differs from Appendix G's. Otherwise clean, and "You may not turn an absent cell into a present one" appears here, in G and in chapter 31 in the same words, which is what a rule should do.

**Verdict.** `ready after the items above`: the parts, the two shared principles, the double period.

## The group

**The thread.** E, F, G, H is the right order: the proofs, the sources, the data contract, the history; E is what G's "quote any cell" is for. But no page hands to the next: each opens cold, and only H's first sentence knows the rest of the book exists. The group does not feel like a part and need not; it is a back matter. The one seam that shows is between G and the map: the same five rules in two wordings, and the agent will read both.

**The author at his best, three sentences.** "You may not turn an absent cell into a present one." (G.) "A guard that is not there fails the build." (E.) "Softanza says thank you to the language it grew up on, and goes where its users' sovereignty requires." (H.)

**The passage least like him.** "Real projects showed that Ring was not suited to the challenges of modern applications. [...] The project's own sessions measured them." (H, What real projects taught.) Everywhere else in these pages a number is read and dated; here the one judgment that will be contested is asserted and the measure is pointed at without a name.

**What a reader who stops here takes away.** That the book's proofs are counted and the count is reproducible (114 guards, 3,359 assertions, 50 of 135 articles, every total found as printed); that an AI agent has a five-line contract it can keep; and that the platform changed its language for reasons it names, and thanks the old one on its way out.
