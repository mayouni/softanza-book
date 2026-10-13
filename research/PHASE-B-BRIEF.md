# Brief: phase B, the beats (a fresh voice reader, then a fixer, per chapter)

Plan of 2026-10-11, phase B. Gate: per chapter, questions at least 1.5 per 1,000 prose words, exclamations 1 to 2.5 per 1,000 words and **none cold** (a cold exclamation is one on an abstract sentence, not after a run or a reveal), long sentences at most 4 %. A chapter whose runs are too few to earn the beats keeps fewer and says so; the beats are never padded.

## The voice reader (stage 1: read, change nothing, write one file)

Read `../../writing-framework/briefs/voice-reader.md` whole and follow it for your chapter, `src/en/<file>.md` (English only). Add to its 12 points the four that phase B needs, each with the line and a quote: (a) **runs without a beat**: every code block whose lead-in is a flat statement where a question the block answers would do, with the `#-->` line that answers it; (b) **paraphrased tool**: a place where the prose retells what a block printed instead of quoting the printed line; (c) **cold exclamations**: every `!` that is not after a run or a reveal; (d) **missing verdicts**: a long explanatory sentence (over 30 words) whose point is buried and would stand as a short sentence or a one-sentence paragraph. Do not write praise. Write your report, under 900 words, to `research/voice/read-NN.md` (NN = the chapter number, two digits); it is the only file you may write. Return it as your final message.

## The fixer (stage 2: edit English and French)

Read, whole: `../../writing-framework/FRAMEWORK.md` §2 (C1, C6, C7), this book's `CLAUDE.md` "The voice", `FRENCH.md`, and the voice reader's report `research/voice/read-NN.md` for your chapter. Then, in `src/en/<file>.md` and `src/fr/<file>.md`:

1. **Beats (a).** Turn the lead-in of a block into a question the block's recorded `#-->` output answers, for the blocks the reader named, until the chapter has about 2 questions per 1,000 words. The question is answered on the page by the block, then by the verdict sentence that follows it. Never a question the page does not answer. Never "isn't it?".
2. **Tool quoted (b).** Where the reader found a paraphrase, quote the printed line verbatim in backticks.
3. **Exclamations (c).** Delete or turn into a full stop every cold exclamation. Add an exclamation only in the sentence that directly follows a block or states a reveal the page has just shown, a refusal, a mismatch, a count that surprises, up to about 1.5 per 1,000 words and **at most five in the chapter**; none in a limit section or a decision section on an abstract claim. The sentence is short and says what happened ("The court refused it!", "Seventy-six assertions, and not one of them mine!" only if the page says so).
4. **Verdicts (d).** Split the buried point into a short sentence or its own one-sentence paragraph. Keep the long sentence's content.
5. **One-sentence paragraphs** at hand-overs, as the plan says, where a section ends and the next begins with no bridge.
6. Intensifiers (very, really, simply, obviously, just as a softener) and any colon lead-in before a prose paragraph, from the reader's list: remove.
7. **French:** the same edits, in the French of `FRENCH.md`; the French page keeps the same number of paragraphs, headings, list items and table rows as the English after your edits (adding a one-sentence paragraph in English means adding it in French).

## Rules (they bind you)
- Never edit a code fence, a `#-->` line, front matter, or any other chapter. Never touch chapter 1 or the preface.
- **Invent nothing.** Every word you add is derived from the page, the block's recorded output, the chapter's own headings or the next chapter's title. No name, date, place, memory, feeling, opinion, number or metaphor that is not already there. No "I remember", "I feel", "I believe" unless the sentence already exists. No new stake: the book's stakes are owned already (PHASEA-01).
- Keep the stage words, the losses beside the wins, the counts and every `[AUTHOR` marker exactly as they are.
- Run `python -I tools/check_fr.py <number>` and `python -I ../../writing-framework/tools/style_lint.py src/en/<file>.md` (and `src/fr/<file>.md --lang fr`) and fix what they report in your files. Do not run the build or the printers.
- Edit with small scripts: read bytes (normalise CRLF to LF), replace an exact string asserted to occur once, write bytes back. Use `python -I`.

## Report (your final message, under 300 words)
Questions added (count), exclamations added / removed (count, quote each added), quotes of the tool added, verdict sentences split, one-sentence paragraphs added; the lint's numbers for questions per 1,000 and exclamations per 1,000 before and after; anything you did not do because a run did not earn it.
