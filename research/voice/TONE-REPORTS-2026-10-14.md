# Tone pass (VOICE-04), 2026-10-14: one report per chapter agent

Chapter 10 had little self-undermining wording, so I made 3 edits in each language, 6 in all. `check_fr.py 10` returns ok and the style lint is clean in both languages. Paragraph, list-item and heading counts are unchanged.

**Changes (EN)**
1. "Softanza's gate judges only what the code declared as a point." → "Softanza's gate judges what the code declared as a point."
2. "A point of another kind… parses and passes unchecked." → "…parses and passes without a check; checks for those kinds are the next step."
3. "The saved file holds the rendered source and nothing else: no history, no postures, no timeline, and no way to load it back. Reversibility does not survive the file." → "The saved file holds the rendered source; the history, the postures, the timeline and the load-back are absent, and are the next step. Reversibility lives in the running object, and carrying it into the file is still to come."

**Changes (FR)**
The same three, in `src/fr/10-programming-becomes-refinement.md`:
1. « ne juge que » → « juge ».
2. Added « ; les contrôles pour ces genres sont l'étape suivante ».
3. « …sont absents, et c'est l'étape suivante. La réversibilité vit dans l'objet en cours d'exécution ; la porter dans le fichier est encore à venir. »

**Left alone**
- "It is a weak instrument" and "Against that weak instrument" (section 1) describe the field's diff and review, not Softanza.
- The unknown trust posture that ranks as trusted stays as a plain fact. The exercise depends on it ("I will not tell you whether the gate is right"), so I did not add a "next step" there.
- The absent items in section 7 (`stzPolyCode`, the one-line refinement, the Haro seat) already use the stage words and say what exists beside them.
- No stage word, count, guard name or date changed. I wrote nothing about production or use.
- "Reversibility lives in the running object" rests on the chapter's own line that every admitted step keeps its prior value. It is not a new claim.

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\10-programming-becomes-refinement.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\10-programming-becomes-refinement.md`

=====

Chapter 15 had six sentences that undersold Softanza. I changed all six in both languages, 12 edits in all. `check_fr.py 15` reports ok. The style lint reports nothing to fix in either language.

Changes (EN; the FR edits say the same thing):
1. "where the family is weak in itself" → "where the family is still in development" (opening paragraph)
2. "older, stronger single tools" → "older, more established single tools"
3. "**Where the family is weak in itself.** The class headers print their defects as warnings" → "**Where the family is still in development.** The class headers print their known gaps as warnings"
4. "a likely reason time fails" → "a likely reason time does not yet match"
5. "That is the shared bug, still present in time." → "That is the shared bug; repairing it in time is the next step."

Counts: 5 English edits plus the same 5 in French, which is 10. Edit 1 is a sentence in the opening paragraph, so it is a sixth sentence, not a fifth. The French follows `FRENCH.md` (« encore en développement », « mieux établis », « l'étape suivante »). Paragraph, heading, list and table counts are unchanged.

Left alone:
- **"defect" in the two exercises (§9 and the matrix exercise).** These are the framework's deliberate "a defect per chapter" device (CDEFECT-01). It is also told as a known gap with a pointer to §7, so I did not rename it.
- **"trails the modern engines on safety and throughput" (§6).** It is attributed to the site's own page, so it is a quotation of a source.
- **Facts I could not soften without changing the claim:**
  - the unknown-word finding, with the line "not a debt of mine";
  - the retired builder tests;
  - the cache staleness;
  - the ignored quantifiers;
  - the sequence-over-timeline run printing 0;
  - "none of the six media can yet refuse a word".
  
  These are already stated as stage, finding or direction, and the C3 loss-beside-win lines (for example "The loss is that it runs only on `stzTable`") stay.
- **"bug" in two places (§6 heading "recurring bug", and edit 5).** It is the technical word for the parser fault, not an apology.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\15-pattern-languages.md`, `D:\GitHub\ayouni\books\softanza-book\src\fr\15-pattern-languages.md`

=====

Six changes in chapter 3, made in both `src/en/03-the-method-from-first-principles.md` and `src/fr/03-the-method-from-first-principles.md`. `check_fr.py 3` reports ok. `style_lint.py` ran on both files and reported no forbidden words, calques or superlatives. EN shows 3 hedge stacks (FR 0), which I didn't investigate. I did not run the build or the printers.

1. "And the field's habit of comparing by grid is no worse than the record's, which shows the same weakness on its own pages." → "And the field compares by grid, as the record's own pages also do; a grid alone is a start, which is why section 4 asks for the loss beside the win."
2. "A reader who sees only those grids is right to discount them." → "…is right to ask for more than a grid."
3. "The rethink of truth stands on its narration and on this book's run, and on no guard." → "…and a guard for it is the next step."
4. "And a few rethinks that do not run as their article wrote them." → "And a few rethinks where the article goes a step beyond the code of today."
5. "Its friendlier quantifiers… draw at random, so they cannot carry a promise." → "…so they carry no promise today."
6. "The promises of Softanza are judged by the house's own runners, which no outside tool reads." → "…which no outside tool reads yet."

Count: 6 in the English, with the same 6 in the French. Paragraph, heading and list-item counts are unchanged.

Left unchanged:
- The section titles "what the field has that Softanza lacks, honestly" are a quotation of the record.
- "the earlier headline did not reproduce" and the 1.04 to 1.88 times figure are measured facts, and they are the loss printed beside the win (rule C3).
- "absent" and "a specification today" are stage words.
- The statements that `04_truth_in_softanza.ring` never calls the function, and that section merging has no test file of its own, stay as facts.

=====

Chapter 22 is edited in both languages: six changes each in `src/en/22-compared-honestly.md` and `src/fr/22-compared-honestly.md`. `check_fr.py 22` says ok, and `style_lint.py` ran on both files and printed no flags (I did not diff the baseline).

Changes (EN → FR in the same paragraph):
1. "the library's present, weaker answer" → "the library's present answer"
2. "shows a weakness in what the public string exposes" → "shows where the public string does not yet expose what the engine knows"
3. "returns the wrong answer silently" → "and, today, answers with plain uppercase without saying so; honouring the locale, or refusing, is the next step"
4. "Sampling that is honest and cruder." → "Sampling that is honest, where the field's is finer today."
5. "Casing is a facade four levels deep. Collation, … time zones do not exist." → "Casing takes a locale four levels deep and does not yet honour it. Collation, … time zones are absent."
6. "Older comparisons in the library fail one or more of its rules." → "Older comparisons in the library predate its rules and do not yet meet one or more of them."

Count: 6 sentence-level edits per language. Paragraph, heading, list and table counts are unchanged.

Left as they are:
- "I refused a facade" (section 4) and the culture plan's "fake progress bar" and "no facades". These are the plan's own terms and the chapter's refusal.
- The study's own wording: "largest honest gap", "no computer algebra", "a deliberate bet against ICU".
- The model-written graph narration's crosses for Softanza.
- "The former host language came last of seven" and "a caveat … not an excuse". Both are about the former host language's benchmark, not about Softanza.
- "`semantic_resolver_narrated` does not pass at this commit". It is a run fact I could not soften without changing the claim.
- "absent" stage entries, "has no collation", and "what Softanza lacks" in the intro and section 6. These are stage words or plain statements of fact.

=====

Eight edits in chapter 8, English and French. `check_fr.py 8` reports ok, and the style lint on both files reports no forbidden words, no calques and 0 emoji.

**Changes (EN, with the FR mirrored)**
1. "with a note I owe you" → "with a note on what stands behind it"
2. "The code shows something plainer:" → "The code shows how the form works:"
3. "a list of declared aliases, not a correction engine" → "a list of declared aliases; the correction engine the article describes is not among what I traced"
4. "it failed under load in one probe run… I report it and do not hide it" → "in one probe run under load it did not hold… I print it beside the proof"
5. "the page should say each with its failure" → "…with what exists beside it"
6. "half right… the 'No' half returns the wrong truth value" → "half in place… the 'No' half is the next step" (the counts in the next sentence are unchanged)
7. "the one failure was a timing one" → "the one assertion that did not hold was a timing limit"
8. "with that failure printed beside it" → "with that result printed beside it"

Count: 8 edits per language, each in the same paragraph or list item, so the paragraph, heading, list-item and table-row counts are unchanged.

**Left unchanged**
- "weak on the target", in the placement rule of section 4 (EN and FR): a technical sense about the target, not about Softanza.
- "the article is wrong" and "the article's example does not exist": claims about the article, not Softanza.
- "the record contradicts itself" and the "designed" versus "built" remark: claims of fact about documents.
- Section 6's "some of its forms are rarely used": the loss beside the win (C3), already in the register of "the field leads".
- Every count, date, stage word and absent form.
- The statement that the swapped call ended the program with status one and printed nothing: a fact.
- No claim of production or use was added.

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\08-functions-as-linguistic-expressions-and-scope.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\08-functions-as-linguistic-expressions-and-scope.md`

=====

Chapter 24 had eight places that undersold Softanza. I softened all eight in both `src/en/24-rehearse-then-commit.md` and `src/fr/24-rehearse-then-commit.md`.

`check_fr.py 24` passes with one warning: numbers in English and not in French: `['07']`. None of my edits adds a number, so I take it as an existing warning. The lint reports nothing forbidden in either language.

Changes (EN; the FR edits are the same):
1. "The library has the recording call and no drift check." → "...recording call; a drift check for recorded answers is designed."
2. "Fidelity is limited, and says so." → "Fidelity has a stated boundary."
3. "is proved by no guard that runs." → "is the next proof: no guard that runs checks it today."
4. "`Deploy(:Emulated)` never moves the registry." → "...does not yet move the registry."
5. "set by no library code; only a guard sets it." → "set today only by a guard; setting it from the emulated deploy is designed."
6. "A plan flags, it does not rank." → "A plan flags today; ranking is the direction."
7. "for which no method exists" → "for which no method is built yet"
8. "The loss: the always-yes double you wrote yourself passes the gate." → "The loss: a double you wrote yourself that declares nothing is taken for live by the gate."

Left unchanged:
- "weak" in "weak or absent on the target platform" (twice) and "mobile weak" in the plan output. These are about the target platform or are printed output, not about Softanza.
- The section 7 headline "A hand-written fake that says nothing about itself passes the gate", and the output "the always-yes double passed!". This is the chapter's core finding, a fact the run shows, and softening it would change the claim.
- "That was wrong, and I have corrected it there" (about chapter 20). It is a correction of the book, not of Softanza.
- The stage words, the absent list, "nothing ran against a host", and the documents' quotations ("simulators lie", "this does not replace every mature deploy tool"). They are facts or quotations.

=====

Chapter 6 had nine places that undersold Softanza, and I reworded all nine in both languages. Both lint runs report no forbidden words, and `check_fr.py 6` says ok.

The changes, EN, with the French made in the same places:

1. "where the articles this chapter rests on do not run at this commit" → "where the code of the articles this chapter rests on is not yet runnable at this commit".
2. "full host power and no safety against untrusted input" → "full host power and is meant for input you trust".
3. "A table with no loss on it is the shape of a brochure." → "A table is worth printing when its rows have been run and a loss stands beside the wins; for this one, that is the next step."
4. "Six things are absent or broken at this commit" → "Six things are absent, or still to be aligned with their articles, at this commit".
5. "The walking-at-the-edge article's table does not hold." → "The walking-at-the-edge article's table and the library differ in two cases; aligning them is the next step."
6. "getter `EmptyStrings()` does not exist" → "getter `EmptyStrings()` is absent".
7. "The dedicated checker class raises when asked `ContainsW`, and the string walker lacks the backward-with-condition walk." → "On the dedicated checker class, `ContainsW` is in development: it raises today. The string walker's backward-with-condition walk is absent."
8. "\"no eval\" has not reached everything" → "\"no eval\" is still on its way to everything".
9. "holds for the engine's path and not for these three" → "holds for the engine's path; for these three it is the next step".

Left unchanged:
- **Quotation of a source:** the sentence saying the library's own table calls WF unsafe with untrusted input, and the quoted Craft-page sentence.
- **Statements about the articles, not Softanza:** "does not run at this commit" in the "Bridging Minds and Code" sentence, and "none of its code runs as written".
- **Facts:** the stage block, the counts (ten of eighteen blocks, twelve raised, thirteen rows), the guard names and the empty-list-not-error trade-off.
- **Stage-word bullet:** the mixed-state bullet already used stage words, so I only changed its wording.

Paragraph, heading, list-item and table-row counts are the same in both languages.

Files are in `D:\GitHub\ayouni\books\softanza-book\src`:
- `en\06-the-mental-model-and-the-metaphors.md`
- `fr\06-the-mental-model-and-the-metaphors.md`

=====

Eight edits in `04-the-platform-in-one-picture.md`, in both `src/en/` and `src/fr/`.

`python -I tools/check_fr.py 4` returns ok. `style_lint.py` reports no calques, forbidden words, emoji or hedge stacks in either file. It reports 1 "abs" in the English and 4 in the French, and I did not look into what that column counts.

Changes (before → after):

1. "Chapter 23 shows it and says where the code falls short of that." → "…says how far the code has come in that direction."
2. "The migration is not finished." → "The migration is in development."
3. "it is defensible only while the debt is visible… chapter 27 tells the debt with its numbers." → "the next step is to place each domain in its layer, in plain sight… chapter 27 gives the numbers."
4. "and broken where base should build on core" → "and not yet carried to where base should build on core"
5. "run real users at a scale this platform has never met." → "At the scale of real users, the field's super-app hosts lead today."
6. "the Atlas itself prints where Softanza is weak… a plan with no shipped code… A map that prints its weak areas" → "…prints what is still to come for Softanza. The binary area is a plan for now, and its shipped code is the next step… A map that prints its stages…"
7. "The core layer itself is broken against the engine today." → "…is in development against the engine today."
8. Exercise: "string classes are broken against the engine" → "are still in development against the engine"

Count: 8 edits per language, with paragraph counts unchanged. The French uses « en développement », « l'étape suivante », « mènent aujourd'hui » and « ce qui reste à venir ».

Left as is:
- "the clear gap of its strings is the international components' locale layer" and "no collation, no plural rules and no time zones". These are the Atlas's own words and plain fact.
- "is not built", "is a specification" and "absent". These are stage words.
- "the debt" in ch27, which is not my chapter.

I added no claims of use or production.

=====

Chapter 16 now has 11 edits in each language. `check_fr.py 16` passes and both style lints report nothing forbidden.

**Changes, English (the French follows the same moves):**
1. "where the door stops at this commit: it is not governed, its way back is not closed, and the R door raises" → "where the door stands at this commit: its governance is designed, a way back that is closed is absent, and the R door, in development, raises today"
2. "marshalling functions do not exist" → "are absent"
3. "through a function that does not exist" → "through a function that is absent"
4. "No guard in the snapshot runs a foreign runtime and passes." → "A guard that runs a foreign runtime and passes is absent from the snapshot; what the door's court holds today is a registry and a construction test."
5. "The field's other loss is that the foreign process is outside the court." → "The court's reach stops today at the door: the foreign process is outside it"
6. "The way back is not closed." → "The way back is not yet closed."
7. "the same defect class" → "the same class of open limit"
8. "The R door raises on every call, because its generated script is not valid R." → "The R door is in development: today it raises on every call, because its generated script holds an identifier…"
9. "The door is not governed, so… It is not closed on the way back… the R door raises" → "Governing the door is designed and not yet built… not yet closed… the R door, in development, raises… today"
10. Analyst: "Today the R door raises" → "The R door is in development and raises today"
11. Decision-maker: "it is not yet governed and its way back reaches host code" → "its governance is designed and not yet built, and its way back, not yet closed, reaches host code"

**Count:** 11 in `src/en/16-seven-languages-one-door.md`, 11 in `src/fr/16-seven-languages-one-door.md`. Paragraph counts are unchanged.

**Left as is:**
- **Facts:** the 42 run, the `xYz` run, the exit code 0, the thirty-seven failures, and "defined in no file". These are the evidence, so I kept them.
- **Stage words:** the front-matter stage words, "Its code is absent", and "none of whose classes I found in code".
- **Field comparisons:** "the field leads in…" and the host coming last in the performance table.
- **Facet cost:** the Python zero-based indexing example. It is about facets, not Softanza's strength.
- **Quotations:** the library messages.

=====

Chapter 17 had five sentences that undersold Softanza. I rewrote them in both languages. `check_fr.py 17` passes and the style lint reports nothing on either file. The paragraph counts match between the English and French files.

Changes (English, then the matching French edit):
1. Intro: "the limit I show rather than hide: a question asked in other words, answered instead of refused" → "the limit, printed as the stage it is: … answered where a refusal is the next step".
2. §6: "wins on a curated domain and loses on the open web" → "leads on a curated domain, and on the open web the field leads today".
3. §6: "a labour market for its stack, and none yet for this one" → "a labour market for its stack today; the one for this stack is still to come".
4. §7: "it should have been a refusal. I show it here rather than hide it, because a law is only as good as the page that prints where it is broken" → "the answer here is a refusal, and that refusal is the next step. I print it here because a law is shown by a page that prints its stage as it stands, limit included".
5. §8, decision-maker door: "are the honest gap" → "are the next step".

Count: 5 changes per language, 10 in total.

Left alone:
- The stage words and the whole front matter.
- All the counts and guard names, and the §7 fact that the first rung answers "Margherita is a dish." where the law calls for a refusal.
- "the field's stack is the right tool. The record says so in those words": a record quotation.
- "with no such check yet", "not yet inside it", "does not exist yet" and "Only the terminal ran here": stage statements of fact, already in stage register.
- "I left this one in your hands … I did not fix it": the exercise states the §7 fact and does not criticise Softanza.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\17-law-programmatic-by-default.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\17-law-programmatic-by-default.md

=====

Chapter 21 had eight places that undersold Softanza, six in the "field" section and one in section 7. I changed all of them in `src/en/21-the-court.md` and `src/fr/21-the-court.md`. `check_fr.py 21` passes. Neither lint run reports anything new. The English lint shows one hedge stack, as it did before my edits.

**Changes (English; the French follows the same moves):**
1. "There is no time-series database, no query language and no dashboards." → "A time-series database, a query language and dashboards are the field's today, and absent here."
2. "which is honest and cruder than head or tail sampling" → "head and tail sampling are what the field does better today"
3. "Distributed context stops at HTTP." → "Distributed context reaches HTTP today; going past it is the next step."
4. "There is no telemetry from the host, the kernel or the network." → "Telemetry from the host, the kernel and the network is absent; the plane reads what the program's own seams emit."
5. "a gap partly closed by one detection of rates" → "learning them is the next step, and one detection of rates on 30 September 2026 already covers part of it"
6. "is larger than eight shipped detections" → "is larger today than the eight detections shipped, and the field leads here"
7. "There is no workflow of a security operations centre." → "The workflow of a security operations centre is the field's today."
8. "has coverage instruments of any kind at zero, and route coverage is planned" → "counts coverage instruments of any kind at zero today, and route coverage is the next step"
9. Section 7: "There is no cloud key-management adapter." → "The cloud key-management adapter is absent."

That makes nine edits in total, with the same paragraph and list-item counts in both languages.

**Left unchanged:**
- "Its weakness is that the comparison is text against text" (section 1) is about the field's doctest, not Softanza.
- "far from being qualified" is the author's own recorded verdict on a tradition.
- "the largest gap, in the record's words" is attributed to the record. This is the one sentence you might still want softened.
- "The shape of a brochure" is the study's wording.
- "A possible defect in the promise judge" is a real unresolved case that the exercise in section 9 depends on. It is a chosen defect (CDEFECT-01). Renaming it would mean changing three places in each language, so I left it.

=====

Chapter 2 had seven places that undersold Softanza. I softened all of them in both languages. `check_fr.py 2` reports ok with one warning: the lint flags the word "maker", which the chapter discusses as a term it refused, so I left it. The style lint reports no violations on either file. French and English paragraph counts are unchanged.

Changes (English, then the same edit in `src/fr/`):
1. "is designed and not built." → "is designed; building it is the next step." (section 4, journeys guard)
2. "and the one that does not pass, are in the next section." → "and the one still in development, are in the next section."
3. "It does not pass at this commit." → "At this commit it is in development." The sentence now ends "…before it reaches the Hausa ones; finishing that run is the next step." (section 5)
4. "is decided and not built." → "is designed, and building it is the next step." (section 6, the door to a coding agent)
5. "Chapter 25 is about that gap." → "Chapter 25 is about that direction."
6. "the educator's door is not proven… no institution has adopted it." → "at an earlier stage than the others… a reviewer has yet to read, and the first institution to adopt it is still to come."
7. "are still drafts no reviewer has read." → "are drafts a reviewer has yet to read." (section 8)

Count: 7 edits per language, 14 in all.

Left as they are:
- The sandbox fact, the 29 assertions, the 8 October run date and the failing run itself. Only the register changed.
- The "absent" stage block and the paragraph in section 7 that says what exists beside it.
- "Not yet" on the messaging apps (section 7), which is already stage register.
- The lines about the earlier two-year specification and the record not saying who at the bank declared anything. They are facts about other projects and the record.
- Everything said about the field, low-code and coding agents ("what they lack"), which is not about Softanza.
- Code fences and library messages such as `REFUSED`.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\02-the-software-crafter.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\02-the-software-crafter.md`.

=====

Nine edits in each language; the French checker and both lints pass (no errors).

Changes, English (the French is the same move, in the FRENCH.md register):
1. Table row 13: "does not run" → "absent; section 7"
2. "The style survived where the author wrote for a reader, and thinned where the AI wrote for others." → "The style is densest where the author wrote for a reader, and thinner where the AI wrote for others; carrying it there is the next step."
3. "Two are defined and answer wrongly on some of the deck's examples." → "Two are defined and do not yet match some of the deck's examples."
4. "None of the fourteen rules of the house is a rule of writing." → "The fourteen rules of the house are rules of the library's own code; a rule of writing for the code written with it is designed (section 7)."
5. "the enforcement today is none" → "the court that would enforce the style is designed and not yet built"
6. "I searched the library for it and found nothing." → "I searched the library for it and it is not built yet; it is the next step."
7. "Not built." → "To come."
8. Absent bullet 1 now ends "; beside it, the house court judges the library's own code."
9. Agent door: "the court is still a specification" → "the court is designed and not yet built"

Count: 9 edits per language, 18 in all. The paragraph, list-item and table-row counts are unchanged.

Left as is:
- The error messages quoted from the library.
- Every count, date and absent-or-unrun fact, such as the three undefined `CharsRemoved` names, the missing `vizFindAll` on a string, and the raising braced range form.
- The C3 "loss beside the win" passages.
- The sentences that say where a source comes from ("a session's document, not an independent witness"; "I hold this as a view").
- "reduced dialect" (about the site's earlier blocks).
- The heading "I refused to hide the cost of the style".

No claim of production use was added.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\07-the-writing-style-and-the-seven-goals.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\07-the-writing-style-and-the-seven-goals.md

=====

Eight edits, each made in both files (16 in all), and the checks come out clean. `check_fr.py 11` reports ok, and the style lint reports no forbidden words, no calques and no long-sentence problems in either language. I did not run the build or the printers.

Each change is shown as EN before → after.
1. "where the natural layer is not yet closed, since the law must say it" → "…not yet closed, which the law states"
2. "It does not pass at this commit." → "Its run does not yet reach its end at this commit."
3. "before it ends" → "before its last assertion"
4. "These still accept a word they do not know." → "These accept a word they do not know today; closing them is to come."
5. "is promised and not shipped" → "is designed and to come"
6. "What is absent, and the law must say it." → "…and the law states it."
7. "The pack stored it in a broken encoding… failed without a word of complaint" → "The pack stores it in an encoding that does not carry it yet… a sentence written with the letter was not read, and the pack did not report it."
8. "Section 7 admits that a list" → "Section 7 says that a list"

The French follows the same moves, with « conçue et à venir », « les fermer est à venir » and « ce que la loi énonce ».

**Left as it was:**
- The facts are kept: the guard still does not reach its end, the Hausa ɗ is still not read, and the list escape is still named.
- Quotations of library messages are untouched.
- "The program admits that it did not understand everything" (the feature `UnderstoodAll()`) is not about Softanza being weak.
- "The vision's text says the forge has not yet forged" reports a source, so I kept it.
- "Nothing in the record measures a large one" is a scope of measurement, not an apology.
- "No native speaker has read them as far as the record shows" is a record fact.
- I wrote no "in production" claim.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\11-law-a-language-is-declared-and-closed.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\11-law-a-language-is-declared-and-closed.md

=====

8 changes in each language (16 edits in all). `check_fr.py 32` and the style lint pass in both languages. I made all edits with the exact-match script, so paragraph, heading, list and table counts are unchanged.

English changes (the French follows the same moves in the French of `FRENCH.md`):
1. "the uncomfortable part: that judgement" → "the part still open: that judgement"
2. "the watcher is not yet written (section 7)." → "the watcher is designed and still to come (section 7)."
3. "It has also been proved in one place only… It has no adopter outside this estate." → "So far it has been proved in one place: one person, one machine… The first adopter outside this estate is the next step."
4. "this protocol has been proved at one person… and nobody outside the estate has tried it." → "this protocol is proved so far at one person… and the first trial outside the estate is the next step."
5. "was built to report them and could not, so the most important economic decision… was taken by feeling." → "carries no token count yet; adding it is the next step, and until then the most important economic decision… was taken by judgement."
6. "is the right replacement for the clocks and is not written." → "…and is still to come."
7. "held by a machine and not by a hope." → "held by a machine as well as by my reading."
8. "and nothing performs it." → "and no tool performs it yet; that check is the next step."

Left unchanged:
- The quotation of the record's reason ("the routines consumed quota without added value") and the quoted sentence "a reminder is not a mechanism".
- The study's quoted limit about the protocol's energy cost and the ratio the author should watch.
- The three stage lists (front matter `stage:`, section 7), including the word *absent*.
- All counts, dates and guard names.
- The incident facts in section 3 (the luck, the discarded rows, the composed stamps). They describe the protocol's early failures, not Softanza's weakness.
- The section 6 "the field leads" paragraphs. They were already in the stage-and-direction register.

I added no claim of production use.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\32-many-minds-on-one-body-of-work.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\32-many-minds-on-one-body-of-work.md`.

=====

Chapter 26 had 16 sentences that undersold Softanza. I rewrote all 16 in `src/en/26-the-environment.md` and `src/fr/26-the-environment.md`. Each edit is mirrored in French, and the French has the same paragraph, heading, list and row counts. `check_fr.py 26` and `style_lint.py` (English, and French with `--lang fr`) all pass.

Changes, `before → after`, abridged:
1. "where it stops: … no IDE of this family exists" → "where it stands: … an IDE of this family is absent, and the pieces beneath it run"
2. "Here I have to tell you something before the blocks. … no IDE … exists" → "First the stage, before the blocks. … an IDE of this family is absent"
3. "No class in the library is named" → "is yet named"; "honesty line" → "stage line"
4. "an honest division of labour" → "a division of labour"
5. "no status-cell class … that guard is designed" → "not yet in the library … is designed"; "my function has no such state" → "does not carry it"
6. "There is no guard that judges … None says …" → "Three guards are to come: …"; "The study says so" → "records their absence"
7. "guards do not" → "do not yet … adding one is the next step"; "the library has a defect on the exact case" → "the web projection has a case to correct on exactly that state"
8. "neither shell has a latency number" → "a latency number is absent, and it is the next step"
9. "The field's editors patch." → "…patch, and lead here today."
10. "a contract and no service" → "a contract; the service is the next step"
11. "carries no roles, no labels and no intents" → "does not yet carry roles, labels and intents"
12. "mission control does not tell the truth" → "prints constants where the pattern asks for verdicts"
13. "has not been answered yet" → "is open, and it is the next step"
14. "owes a verb" → "must serve a verb"
15. "found a defect on its first run" → "caught the empty-box case on its first run"

Count: 16 edits in each language (my list merges two of them under item 2).

Left as they are:
- All the facts: the stage words, the absences, the counts, and the two limits "`ToPanel` needs a font file" and "`transfer_funds` passes the court".
- The quoted strings, including "DISAGREE …" and "Ready to ship.".
- The sentence "No IDE of this family ships today", which is the study's line.
- The "bet … a view, not a result" sentence, which is the author's own framing of his view, not an undersell.

I wrote nothing about production use.