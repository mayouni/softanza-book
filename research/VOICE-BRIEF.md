# Brief: bring one chapter's voice in line with the AYOUNI Writing Framework (phases B, D, E, G of the plan)

You edit one chapter of the Softanza book, English (`src/en/<file>.md`) and French (`src/fr/<file>.md`), and nothing else. Read first, whole: `../../writing-framework/FRAMEWORK.md` §2 and §4, this book's `CLAUDE.md` section "The voice", `FRENCH.md` (the French style sheet), and the rows of `research/METAPHORS.md` that name your chapter. Then read your chapter whole, and the first lines of the next chapter (its title and its bold principle under "## 2") for the bridge.

The book keeps its discipline (the court, the limit, the loss beside the win, the counts) exactly as it is. You add the beats and the shape the framework asks for, and you add **nothing that is not already on the page or in the next chapter's title and principle**: no name, date, place, memory, feeling, opinion, metaphor, fact or number. If a sentence you want to write needs a particular only the author can give, do not write it.

## What you do, in this order

**1. The roadmap (D).** Before `## 1`, after the front matter, add one paragraph of three to five sentences in the first person that says what this chapter does, built only from its headings, its bold principle and its decision: "In this chapter I …". It ends on the chapter's principle or on a true particular the chapter already holds (a date, a project, a guard), never on a new one. Chapter 1 is the author's text: if your chapter is chapter 1, stop and report.

**2. The bridge (D).** At the end of the chapter, after the exercise, one or two sentences that hand over to the next chapter, naming only what its title and principle say. No summary of what was just read.

**3. The beats (B).** Where a code block follows, you may turn the lead-in sentence into a question the block answers ("What does the court answer when the fake is asked in production? Run it:") — only where the recorded output (the `#-->` lines of the block) answers it. Where the prose paraphrases what a block printed, let the tool speak: quote the `#-->` text verbatim ("the court answers: `REFUSED …`"). An exclamation is allowed only in the sentence that directly follows a block or states a reveal the page has just shown; at most two in the chapter; none on an abstract sentence; delete none that already obey this. After a long explanatory sentence (over 35 words) that ends on its point, split the point into a short verdict sentence or its own one-sentence paragraph. No question is left unanswered on the page. No "isn't it?" tags.

**4. The metaphor mapping (E).** If `research/METAPHORS.md` says a ruling metaphor first appears in your chapter, make sure the place where it first appears maps it in one paragraph, term by term, in the book's own words (the glossary's definition in Appendix D, the chapter's own sentences); if the chapter already does this, leave it. Do not add a sustained metaphor. If you find a decorative metaphor (deletable without loss of meaning), delete it and say so in your report.

**5. The noise (G).** From the lint of your chapter: "developer(s)" → "programmer(s)" unless inside a quotation of a source; "may be" (for maybe) → rephrase; "a hole" → "a whole"; a hedge stack ("kind of" as a hedge, "more or less", "in a way") → the plain statement, but leave "a kind of X" when it is a classification; sentences over 40 words → split, aiming at no more than one in twenty-five; a colon that ends a paragraph before a prose paragraph → a full sentence. Keep the forbidden words out (substrate; maker outside "decision-maker"; leverage, utilize, best practice, stakeholders).

**6. The French.** Make the same edits in `src/fr/`, in the French of `FRENCH.md` (the nine headings have fixed French names; the roadmap is « Dans ce chapitre, je … »; the exclamation and question rules are the same). The French page must keep the same number of paragraphs, headings, list items and table rows as the English after your edits (so a paragraph you add in English, you add in French). "développeur" → "programmeur".

## Rules (they bind you)
- Never edit a code fence or a `#-->` line. Never change front matter. Never touch chapter 1 or any other chapter's files.
- Never invent: every word you add is derived from the page, the next chapter's title and principle, or Appendix D. Never write "I remember", "I feel", "I believe" unless the sentence already exists.
- Never set `status`. Never add an `[AUTHOR` marker; if you see a place that needs the author, list it in your report instead.
- Run `python tools/check_fr.py <number>` and `python ../../writing-framework/tools/style_lint.py src/en/<file>.md` (and `src/fr/<file>.md --lang fr`) and fix what they report in your files. Do not run the build, the runner, the printers or the release.
- Edit with small scripts: read bytes, replace an exact string asserted to occur once, write bytes back (files use LF). Use `python -I`.

## Report (your final message, under 400 words)
1. What you added: the roadmap (quote it), the bridge (quote it), the beats (count: questions added, exclamations added or kept, verdict sentences split, tool-quotes), the mapping (which term, where), the noise fixed (counts).
2. **Two candidate defects for phase C**, for the author to choose, derived from the chapter: a block the reader could be given broken on purpose (name the block and the line), a correct listing the decision section already rejects and why, a chart or answer the chapter could refuse to give, a question the record cannot answer. Do NOT write them into the page.
3. Places that need the author (a particular, a stake to own), one line each with the heading.
4. The lint's last line for each of your two files, and `check_fr`'s verdict.
