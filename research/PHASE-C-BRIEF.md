# Brief: phase C, a defect left in the reader's hands (one agent per chapter)

The author said, on 2026-10-13: "Go ahead with Phase C, pick the defects on my behalf". Framework commitment C2: every chapter hands the reader something real and unfinished, **named as such**: a bug left on purpose, a correct listing rejected for taste with the reason, an answer the chapter refuses to give, a question the record cannot answer. The Ring book did it everywhere ("Correct it please", "this is your penalty", "I left a subtle bug I want you to discover"). The plan's phase C proposed two candidates per chapter; you pick one.

Your chapter: the English `src/en/<file>.md` and the French `src/fr/<file>.md`. The candidates are in `research/voice/REPORTS-2026-10-11.md`, in your chapter's report, section "2. Two candidate defects for phase C". Read first: `../../writing-framework/FRAMEWORK.md` §2 C2, C3, C4; `research/ANSWER-POLICY.md` D1, D4, D9; `FRENCH.md`; this book's `CLAUDE.md` "The voice". Read your chapter whole, and especially its `## 9. Exercise` and `## 7. The limit`.

## How to choose (on the author's behalf)
Pick the candidate whose **answer the page, the run data or the record already holds**, so the book never asserts an output nobody ran. Prefer, in this order: (1) a defect the chapter's own limit section already admits (the page says the thing fails; the exercise hands the reader the failing case); (2) a block the chapter ran, handed over with one named change, whose consequence the chapter's prose already explains elsewhere (the reader runs it and finds out; you print neither the output nor a prediction); (3) a listing the decision section already rejects, with its reason. Reject a candidate that needs you to state an output that `data/book-run.json` and the chapter do not hold. If neither candidate qualifies, write the defect from the chapter's limit section instead and say so.

## What you write
Rewrite `## 9. Exercise` (keep its number and its fixed heading, English and French; the build reads the number) so that it ends on the defect, in the first person, plainly named as left on purpose:
- keep the exercise's existing task if it has one (shorten if needed; never remove a task the reader needs); then add the defect as the last paragraph(s): "I left this one in your hands." / « Je vous laisse celui-ci. » — what to run, what to change, what to look for, and **where the page says why** (a section number), never the answer itself;
- if code is needed, use a fence tagged `haro exercise` (not run by the build, shown as an exercise), copied from a block of the chapter with the one change; never add a runnable fence; never add a `#-->` line to it; never print the output it would give;
- one sentence says what the reader will know when they have solved it ("When the court answers, you will know why a declared constraint is not an enforced one" only if that is what the page says);
- no new fact, no name, no date, no number, no metaphor, no stake; the stage words and the losses stay as they are;
- the chapter's bridge sentence (the last paragraph after the exercise, added by phase D) stays last.

## French
The same in `src/fr/` (the exercise keeps the heading « Exercice »), same paragraph count and the same fences as the English (the fence must be byte-identical).

## Rules
Edit only your chapter's two files. Never edit another section, front matter or any non-exercise fence. Never touch chapter 1 or the preface. Run `python -I tools/check_fr.py <number>` and `python -I ../../writing-framework/tools/style_lint.py src/en/<file>.md` (and `src/fr/<file>.md --lang fr`). Do not run the build or the printers. Edit with small scripts (read bytes, normalise CRLF to LF, replace an exact string asserted to occur once, write bytes back; `python -I`).

## Report (your final message, under 250 words)
`chapter N · chosen: <candidate, one line> · why (which rule 1/2/3 and the page's own evidence, with the section number) · the rejected candidate and why · what you wrote (quote the last paragraph in English) · an exercise fence added: yes/no`.
