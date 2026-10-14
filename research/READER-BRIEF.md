# Brief: read the book as a reader, on the author's behalf

The author, on 2026-10-14: "Read the book on my behalf, after getting step back from your role as a writer to embrace the profile of a reader." You did not write this book. You are not editing it. You are reading it the way its author would read it before letting it go: whole pages, in order, at reading speed, as one of the six readers it addresses (the programmer, the analyst, the designer, the decision-maker, the educator, the AI agent), and as the author himself, who wants to know one thing: **is each page ready to be marked read, and if not, what stops it.**

Read nothing about how the book was made (no `research/chNN.md`, no `sessions/`, no `DECISIONS.md`, no brief but this one and the cover of `CLAUDE.md`'s "The voice" paragraph). You judge the page, not the record. Read the English pages in `src/en/` whole, your group in order, and keep going until you have read every page of your group once without stopping to take notes; then read each again with the questions below in hand.

## What you report, per page

1. **What you remember after closing it.** Two or three sentences in your own words: the point, the proof, the limit. If you cannot say them, say so: that is the first finding.
2. **Where you lost the thread.** The paragraph (quote under 20 words and the heading it sits under) where you had to read twice, or stopped understanding what the code was for. A term used before it was defined, a figure that does not match its text, a "we have seen" that you had not seen.
3. **Where you doubted.** A claim that sounds larger than the page shows; a number you could not find in the code or the court; a sentence that sounds like an advertisement, or one that sells the work short. Quote it.
4. **Where it moved you,** if anywhere: a run, a reveal, a refusal, a sentence. Quote it. And where it bored you: a stretch you would skip on a second reading, named by its heading.
5. **The code.** Did you understand each block from the sentence before it? Was its `#-->` output what the sentence promised? Any block you would cut or move.
6. **Errors of fact or form you are sure of:** a wrong cross reference (chapter number, appendix letter, guard name that another page spells differently), a typo, a broken list or table, a heading out of order, a French word in the English, an English word that reads as a calque.
7. **The door that is yours.** Pick the one of the six doors you walked in by for this page and say whether its two lines were worth the walk.
8. **Verdict.** `ready` / `ready after the items above` / `not ready`, one line of reason. "Ready" means: you would put your name on it as the author.

Then, **for the group**: the thread between the pages (does each bridge land where the next page starts? does a part feel like a part?), three sentences that are the author at his best, one passage least like him, and what a reader who stops at the end of your group takes away.

## Rules
- You change nothing. Do not edit a file, do not run the build, the runner or the printers. You may run `python tools/book_audit.py` if an item needs it; nothing else.
- Quotes under 20 words; headings named exactly; page named by its file.
- No praise without a quote; no generality without a place. "The chapter is clear" is not a finding; "I could restate section 3 without looking" is.
- Write the report to `research/read/<group>.md` (the group letter you were given), under 2,500 words, in the order above, one `## <file>` per page, then `## The group`. Your final message: the verdict line per page and the three items that most need the author, under 200 words.
