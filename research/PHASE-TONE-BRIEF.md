# Brief: take the self-undermining wording out of one chapter (VOICE-04)

The author's standing rule, repeated many times and confirmed on 2026-10-14: **do not hurt our work in the name of transparency or critical balance.** Softanza is not a research project, although it rests on deep research. It has been used to solve real problems in several situations, and the feedback shaped its design. Parts of it are in production and parts are in development, which is normal for a platform this new and this ambitious. It is a professional foundation aimed at professional decision-makers: a bank's IT director must not read "weak" about it.

Your chapter: `src/en/<file>.md` and the same-named `src/fr/<file>.md`. Read first: this brief; the book's `CLAUDE.md` "Standing rules"; `DECISIONS.md` VOICE-04; `FRENCH.md`. Then read your chapter whole.

## What to change
Find each sentence where **the book undersells Softanza itself**: "weak", "weaker", "weakness", "falls short", "falls short of", "short of", "poor", "crude", "toy", "still only", an apology ("unfortunately", "I must admit"), "nothing runs", "none of it runs in production", "not in production", "owes you", a limit told as a deficiency of Softanza rather than as a stage. Rewrite it in the register of **stage and direction**: "in development", "to come", "built, designed or absent" (the book's three stage words, unchanged), "the field leads here today", "this is the next step", "what the field does better today". The fact stays: you remove the apology and the weakness, not the information. Where the chapter says a part is absent, keep the word *absent* (a stage word) and say what exists beside it.

Examples of the move: "Softanza is weaker than the field at X" → "At X the field leads today; Softanza's answer to X is in development"; "falls short of the vision" → "the vision goes further than what is built today, and the limit section says how far"; "the guard is weak" → "the guard covers N cases; the rest is the next step".

## What not to change
- A **quotation** of a source (the site, a memo, a study, the library's own message): never.
- A technical sense of the word that is not about Softanza ("weak typing", "a weak reference", "weakly typed" about a language the book describes, "a weak signal"): leave it.
- Any stage word (built, designed, absent), any count, any guard name, any date, any claim of fact: leave it. **Never write that something is in production, or in use, unless the chapter's own page or the record already says so.** Do not invent a project, a user or a number. If a sentence says a thing is absent or unrun, keep that fact and change only the register.
- Code fences, `#-->` lines, front matter, other chapters. Chapters 1, 31 and 33 (and the preface) are not yours.
- The framework's rule C3 stays: the loss is printed beside the win, in this register.
If a chapter has no sentence that undersells Softanza, change nothing and say so.

## French
Make the same edits in `src/fr/` in the French of `FRENCH.md` (« en développement », « à venir », « le terrain mène aujourd'hui », « c'est l'étape suivante »); same paragraph, heading, list-item and table-row counts as the English.

## Rules
Edit only your chapter's two files. Run `python -I tools/check_fr.py <number>` and `python -I ../../writing-framework/tools/style_lint.py src/en/<file>.md` (and `src/fr/<file>.md --lang fr`) and fix what they report. Do not run the build or the printers. Edit with small scripts (read bytes, normalise CRLF to LF, replace an exact string asserted to occur once, write bytes back; `python -I`; put long scripts in a file in your scratchpad to avoid shell escape trouble).

## Report (your final message, under 250 words)
Each change as `before → after` (quote both, under 30 words each), then the count, then anything you left because it is a quotation, a technical sense or a fact you could not soften without changing the claim.
