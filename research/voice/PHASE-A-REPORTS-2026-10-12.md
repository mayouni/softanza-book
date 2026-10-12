# Phase A rulings applied, 2026-10-12: one report per agent (chapter 1, forge, stakes 2..33)

Chapter 4 got one stake owned, in English and in French. `check_fr.py 4` reports ok and the style lint has no calques, no forbidden words and no hedge stacks. The paragraph count is unchanged in both files.

**Changed, §6 "The field, and where it leads", last paragraph:**
- EN: "I hold this as a view, not a result: a map that prints its weak areas is the only kind worth reading."
- FR: « Je tiens cela pour une vue, non pour un résultat : une carte qui imprime ses zones faibles est la seule sorte qui vaille la peine d'être lue. »

No reason was added. The page already lists the Atlas's weak areas (binary, extensibility, system) in the sentence just before, so that stands behind the view.

**Left alone:**
- "defensible only while the debt is visible" (§4): it is framed by "I say so", and chapter 27 gives the debt with its numbers.
- "The engine is the product" and "Build on the strong lanes": each is a design decision or an instruction, not an unproved claim about the field, and the report named neither.
- "three unrelated places" (crafters): a particular for the author's next answers.
- The exclamation "Four letters, not eight!": the author's call.
- The report's phase C candidates (the layers block, the constellation block): not part of this task.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\04-the-platform-in-one-picture.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\04-the-platform-in-one-picture.md

=====

Chapter 7 had one unowned stake. I added one owning clause to it in both languages, and `check_fr.py 7` and the style lint report no problems.

**What I changed (§2, "The first principle"):**
The sentence was "a software architecture that is goal-oriented is the only way one architect masters a project of this size". It is a conviction stated as fact, and the page carries it only "as the study reports it".

- **EN:** I appended "I hold this as a view, not a result. What stands behind it on this page is one case: the 2022 matrix served as a skeleton for one architect over about three hundred thousand hand-written lines (section 6)."
- **FR:** I appended « Je tiens cela pour une vue, non pour un résultat. Ce qui la soutient sur cette page est un seul cas : la matrice de 2022 a servi de squelette à un architecte pour environ trois cent mille lignes écrites à la main (section 6). »

The backing is §6's own sentence about the matrix and the 300,000 lines. I added no reason of my own. The paragraph count is unchanged, and I kept the English file's CRLF line endings.

**What I left and why:**
- **§4, first refusal** ("I refused a style that was changed when AI became the main writing tool", and the demand that follows): it is reported through the study, and the voice report lists it as the author's own words owed. It is a source matter, not mine to touch.
- **§3, Flexibility:** the free-order parameters question is already marked as a decision the record does not hold.
- **§6 "Where I think the style stands apart…":** already marked as belief.
- **§6 enforcement and "first look" claims, and the §8 door sentences:** these are field observations or already backed on the page, so I judged them not stakes.

**Files:**
- D:\GitHub\ayouni\books\softanza-book\src\en\07-the-writing-style-and-the-seven-goals.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\07-the-writing-style-and-the-seven-goals.md

=====

Chapter 6 (stakes): I added two ownership clauses, in English and in French. `check_fr 6` reports ok, and the style lint is clean in both languages with no calques or forbidden words. I did not run the build or the printers. Paragraph count is unchanged.

**Changed**
1. In §6, after "A table with no loss on it is the shape of a brochure.":
   - EN: "This is my view, held on this table: thirteen rows, none with a loss."
   - FR: « C'est mon point de vue, tenu sur cette table : treize lignes, aucune avec une perte. »
   - The thirteen rows come from the page itself, which says the library's table has thirteen rows, all in the walker's favour.
2. In §4, after "A goal is what makes a feature justifiable or refusable.":
   - EN: "I hold this as a view, not a result." The next sentence now begins "So I did not leave the metaphors as a nicety…".
   - FR: « Je tiens cela pour une vue, non pour un résultat. » The next sentence now begins « Alors je n'ai pas laissé… ».
   - The page gives no proof for this conviction, so nothing follows the clause.

**Left, and why**
- §4 "I let the edge rule be a design principle": the report lists it, but it concerns whether the record dates a ruling. That is a particular for the author's next answers, not a stake.
- "The field leads in…" in §6: these are comparisons already balanced by a stated loss, so I did not touch them.
- Every code fence, `#-->` line and front-matter key.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\06-the-mental-model-and-the-metaphors.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\06-the-mental-model-and-the-metaphors.md

=====

I added two ownership clauses to chapter 3, in English and French, and left everything else alone. `check_fr 3` reports ok. The style lint is unchanged from the 2026-10-11 voice-pass report: hedge stacks stay at 2 in English and 0 in French, and the one forbidden-word hit in French is "développeurs" inside the quoted article. The English lint now shows forbidden 0 where that report showed 1; I did not check why.

**New clauses (EN, then FR)**
1. §4, "I refused to add a feature without a need": "First principles without that rule produce a museum. **That is my view, not a result.** With it, a rethink has to earn its place…"
   FR: « …produisent un musée. **C'est mon point de vue, non un résultat.** Avec elle, … »
2. §6, "Where I think Softanza stands apart": "…the rethink is carried all the way down. **I hold this as a view, not a result.** The decision is written, the redesign runs, the promise is judged at build…"
   FR: « …mené jusqu'au bout. **Je tiens cela pour une vue, non pour un résultat.** La décision est écrite, … »
   This is the stake the voice report names for chapter 3. The sentences after the clause already say what stands behind the view, so I added no reason.

Paragraph counts are unchanged, and no code fence, `#-->` line or front matter was touched.

**Left alone**
- "A reader who sees only those grids is right to discount them": the page backs it with the grids where Softanza's column wins almost every row.
- "A court can only judge a sentence of a language it knows": it is a design statement the chapter argues.
- "A verdict … that cannot say why is not admitted in this house": the `modality_narrated` guard proves it.
- The quoted article's missing date and the unnamed internal memo: these are the author's next answers.

Files edited:
- `D:\GitHub\ayouni\books\softanza-book\src\en\03-the-method-from-first-principles.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\03-the-method-from-first-principles.md`

=====

Chapter 8 had one unowned stake. I added one owning clause to it in each language, with no paragraph added.

**Changed**

The stake is the sentence in §3 that opens the scope half: "The same fault shows up everywhere in programming: behaviour with an invisible governing frame."

English clause, added right after it:
"I hold this as a view, not a result; what stands behind it here is three instances: the regex verbs, the system and the placement of a deployment."

French clause, same place:
« Je tiens cela pour une vue, non pour un résultat ; ce qui la soutient ici, ce sont trois instances : les verbes de l'expression régulière, le système et le placement d'un déploiement. »

The three instances are the ones §3 itself walks through and §7 lists as built. I added no reason beyond those.

**Checks**
- `check_fr.py 8` returns ok.
- `style_lint.py` is clean for both files, with no new calque and no new hedge stack. It reports 1 absolute in each language, which I take to be "everywhere". That word is the stake, now owned, and I left it in.
- Both files already used LF line endings.
- I touched no code fence, `#-->` line or front-matter key.

**Left alone**
- The §2 bold principle ("A function's name is a sentence…") is the chapter's own principle (D3), restated in the roadmap and the bridge.
- "The scope decides, not the operation" is proved by the `Spawn` run.
- "That mode is the antipattern this paradigm was founded against" is a verdict the design document records.
- The door line "a review can see it" is a mild design claim, not a conviction about the field or the future.
- The three "places that need the author" in the chapter 8 report are a trace, a recorded run and a question of attribution. They are not stakes, so I did not touch them.

**Files**
- D:\GitHub\ayouni\books\softanza-book\src\en\08-functions-as-linguistic-expressions-and-scope.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\08-functions-as-linguistic-expressions-and-scope.md

=====

Chapter 5: two stakes owned, in English and French. `check_fr 5` says ok and the style lint reports 0 flags in both languages. Paragraph counts are unchanged, no code fence was touched, and both files were already LF.

**Changed**

EN §3, before the court block:
- "A rule a person must remember is folklore; I hold this as a view, not a result. The library turns its house rules into validators…"
- The next sentence, already on the page, is the support: the validators, five of the fourteen.

EN §8, The decision-maker:
- "I hold this as a view, not a result: a style a machine can be held to can be reviewed goal by goal, not line by line, which is the only reading one person can give to hundreds of thousands of lines."
- The page offers nothing that proves this, so nothing follows the clause.

FR, same two places:
- « Une règle qu'une personne doit retenir est du folklore ; je le tiens pour une vue, non pour un résultat. La bibliothèque… »
- « **Le décideur.** Je tiens cela pour une vue, non pour un résultat : un style auquel une machine peut être tenue peut être relu… »

**Left, and why**
- **Already owned or proved:**
  - "Where I think Softanza stands apart" is marked as belief.
  - "A style that lives in one person's habits dies…" is backed by the promise counts of 98.9 / 75.1 / 52.5 / 0.7.
  - "A style that is not shown is not learned" follows the site finding.
  - The refusals in §4 are already in "I refused…" form.
- **Left for the author's next answers:**
  - The study's recommendation on the one test form, which has "no ruling of mine".
  - Whether the refusal of the three features is his.
  - The lost `CharsQRT` link and the request to restore it, which is a stake to own or drop.
- **Limit of two:** I stopped at two, as the brief says.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\05-law-the-code-adheres-to-the-way-a-person-thinks.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\05-law-the-code-adheres-to-the-way-a-person-thinks.md

=====

Chapter 9 had two unowned stakes, and I added one clause to each in both languages. `check_fr 9` passes, and the lint flags nothing on either page. The 3 and 4 "absolutes" counts it prints are "to judge" items that were already there ("never", "nothing"). No code fence, `#-->` line or front-matter key was touched, no paragraph was added, and line endings stay LF.

The chapter's section in `research/voice/REPORTS-2026-10-11.md` names no stake. Its "places that need the author" list only the images ("reflex arc", "intelligence of a place") and the 46-word definition, which the brief tells me to leave. I found the two stakes by reading the page.

**Changed (EN / FR)**
1. §1, after "a rule engine does not have a vocabulary that a person would use to say a thought." I added: "I hold this as a view, not a result." / « Je tiens cela pour une vue, non pour un résultat. »
2. §4, after "borrowed from plumbing, telephony and publishing, and not from the problem." I added: "This is my view of those words, not a result." / « C'est mon point de vue sur ces mots, non un résultat. »

Neither clause carries a reason, because the page gives no proof for either claim. The overflow audit and the settle block show how Reaxis behaves, not that its words are better.

**Left alone, and why**
- "I would rather show you the block that fails to cascade": already marked as my preference.
- "the Regexuter, a reflex arc", "Time is a workspace, not a number" and "a word you do not need a diagram to understand": design images, definitions or mild wording, not convictions about the field or the future. The reflex arc is kept by the rulings.
- "I will not call it more": already a limit statement.
- §6, where the field's rule engines and reactive libraries lead: already marked as general knowledge and conceded.
- The report's other places (the 46-word definition and the two images): not stakes, and for the author's next answers.

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\09-patterns-of-thought.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\09-patterns-of-thought.md`

=====

I added one first-person clause to each of two unowned stakes in chapter 2, in English and French, and left everything else alone. `check_fr.py 2` reports ok with 1 warning; the warning is the old 'maker' one, which is the refused word. The style lint reports nothing new.

**What I changed**

1. In §2, "The first principle", the conviction that skill is not part of what a crafter is now ends with:
   - EN: "I hold this as a view, not a result."
   - FR: « Je tiens cela pour une vue, non pour un résultat. »
2. In §6, "The field, and where it leads", the sentence "The messaging apps lead where the crafters already are." is now followed by:
   - EN: "This is my view, not a result."
   - FR: « C'est mon point de vue, non un résultat. »
   - The sentences after it already say what stands behind the claim: the spreadsheet, the option label, and no conversational medium being a target yet. I added no reason of my own.

Paragraph counts are unchanged, and the files stay LF. I touched no code fence, `#-->` line or front matter. Each replacement was an exact string asserted to occur once.

**What I left**
- Passages already marked as belief or as general knowledge: "Neither says what I think programming is", "I held that agents do not make programmers obsolete", and the "(General knowledge…)" lines in §1 and §4.
- "Coding agents lead in hands", "Low-code leads in installed base" and "The crafter's platform sits beside the field's tools": these are marked, factual, or backed by the page.
- The other places the report lists for the author's next answers: who at the bank declared anything, what the cover image carries, and the "Coding agents lead in hands" image.
- The English lint shows "hedge stacks 2". These are the two "kind of" classifications the voice pass noted, not my clauses, so I left them.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\02-the-software-crafter.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\02-the-software-crafter.md`.

=====

Chapter 10: I added an ownership clause to two stakes in each language and left everything else alone. The French check (`check_fr 10`) passes, and the style lint is clean in both languages (0 calques, 0 forbidden, 0 hedge stacks). I did not run the build or the printers.

**What I changed (§1 and §4, same paragraphs, same paragraph count in both languages)**

1. §1, the field's answer to a change:
   - EN: "It is a weak instrument when most changes arrive from agents, in volume; I hold this as a view, not a result."
   - FR: « C'est un instrument faible quand la plupart des changements arrivent d'agents, en volume ; je tiens cela pour une vue, non pour un résultat. »
2. §4, "I refused to govern the intelligence":
   - EN: "The change is the thing that stays, and it is the thing that reaches the world: this is my view."
   - FR: « Le changement est ce qui reste, et c'est lui qui atteint le monde : c'est mon point de vue. »

I added nothing after either clause. The page offers no count, project or guard behind these two claims, so I followed your rule and left it at that.

**What I left, and why**

- Sentences already marked "(General knowledge…)" in §1, §4 and §6, the "I refused…" decisions, and "the first principle" (already "I have not found a better one").
- "A learner can try without fear because every step keeps its prior value" is proved on the page by the reversal block.
- The `research/verify/ch10.md` items (the "three refusals" credit, "third law", the `.rfn` / `.zrfn` wording and the other overclaims) and the reading problems are factual corrections, not stakes. They belong to the author's next answers.
- The voice report's open question (whether the unknown-posture rank is a bug or a stance) is also for the author.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\10-programming-becomes-refinement.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\10-programming-becomes-refinement.md

=====

Chapter 18 had two unowned stakes. I added one owning clause to each, in English and in French. `check_fr 18` returns ok, with the same 61 paragraphs in each language. The style lint reports no flags in either file. I did not run the build or the printers.

**What I changed**

1. §3, fifth register (silence):
   - EN: "It is silence, and I hold silence to be the worse answer, as a view and not a result: the reader who offered the examples is not told they were not understood."
   - FR: « C'est le silence, et je tiens le silence pour la pire réponse, comme une vue et non comme un résultat : le lecteur qui a offert les exemples n'est pas informé qu'ils n'ont pas été compris. »
   - What stands behind it is already on the page: the `[ ]`, `[ ]`, `pursuing` and zero-checkpoint block. I added no reason.
2. §4, "I refused a different gate…":
   - EN: "The form does not buy trust, and I hold this as a view, not a result. All five registers go through one door."
   - FR: « La forme n'achète pas la confiance, et je tiens cela pour une vue, non pour un résultat. Les cinq registres passent par une seule porte. »
   - I added nothing after the clause. The sentence that follows is the page's own.

**What I left**
- "Where I think the record stands apart" (§6) is already marked as his belief.
- "The raise is the law working" is a design-document quote and a fact of the record.
- §2 (why five registers, and when he set wise coding against vibe coding) and the dates "to be checked before print" are the report's author-places, kept for his next answers.
- The 12 July 2026 / 13 July 2026 style particulars are untouched.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\18-the-five-registers.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\18-the-five-registers.md

=====

Chapter 13 (stakes): I added two ownership clauses in each language and changed nothing else. `check_fr.py 13` returns ok. Both style lints report 0 flags, with no hedge stacks and no calques.

**What I changed (§4, "What I refused")**
1. In "I refused markers on reference", after "…and language itself never marks reference this way."
   - EN: "That is my view of language, not a result."
   - FR: « C'est mon point de vue sur le langage, non un résultat. »
2. In "I refused the ungrammatical chain", after "…an ungrammatical chain that runs is a bug."
   - EN: "I hold this as a view, not a result."
   - FR: « Je tiens cela pour une vue, non pour un résultat. »

I added no reason after either clause, because the page gives none for them. The paragraph count is the same in both languages. Both files keep their CRLF line endings, as before. I did not touch any code fence, `#-->` line or front matter.

**What I left, and why**
- The three "places that need the author" from the chapter's report are not stakes, so I left them for his next answers. They are the count of promises in "I built it without a model", the sense of "thin doors", and the private memo of 30 August 2026.
- The "ch13.md" verification report's items (dates, counts, attributions) are facts of the record, so I left them too.
- Sentences already marked or attributed, or proved on the page, stay as they are:
  - the first principle, a stated principle;
  - "The record says the winning case is regulated or sovereign work", attributed to the record;
  - the "fourth promise: accountability", which belongs to the design review;
  - "the human's job", which the page presents as doctrine and then proves in §7.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\13-natural-and-executable.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\13-natural-and-executable.md`.

=====

Chapter 17: I added two ownership clauses in each language, so four sentences in all. `check_fr.py 17` reports ok. The style lint is clean in both languages (calques 0, forbidden 0, hedge stacks 0).

**What I changed**

1. In section 3, after the first block's refusal:
   - EN: "A refusal that names its boundary is worth more than a fluent answer that has none. This is my view."
   - FR: « … qui n'en a pas. C'est mon point de vue. »
   - What stands behind it is the block just above, which prints the refusal `I know 1 entities and 1 relations`. I added no reason.

2. In section 7, after the rephrased-question limit:
   - EN: "I show it here rather than hide it, because a law is only as good as the page that prints where it is broken. I hold this as a view, not a result."
   - FR: « … la page qui imprime où elle est brisée. Je tiens cela pour une vue, non pour un résultat. »
   - The page already backs it with the printed counter-example, so I added nothing after the clause.

Paragraph counts are unchanged in both files. No code fence, `#-->` line or front matter was touched. I kept each file's line endings (both are LF now).

**What I left**

- Section 4, "Pretending would be easier, and it would make every other refusal in this chapter worth less". It is a third conviction, but the brief caps stakes at two per chapter.
- Section 4, "The industry's loop is a special case of this design". It reads as a design claim, not a belief about the future or people.
- Section 1, "some of it is very good". The report lists it as an opinion to keep or cut, which is the author's call.
- Section 4, the two readings of "last" (local or remote), and whether the rephrased question is the chosen defect. Both are the author's rulings, so I left them.
- Section 6, "where I think the law stands apart": it is already marked as belief.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\17-law-programmatic-by-default.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\17-law-programmatic-by-default.md

=====

No unowned stake in chapter 14, so I changed nothing in either language. Both files are untouched. I did not edit the line endings, and the French file is still CRLF.

**Checks, both unchanged and clean:**
- `python -I tools/check_fr.py 14` returns `14-knowledge-programming: ok`.
- The style lint on the English reports 0 calques, 0 forbidden words and 0 superlatives.
- The style lint on the French reports the same zeros.
- The lint also shows `abs 9` (English) and `abs 10` (French). I read them. They are technical universals ("every fact needs its provenance", "every declared course is a folder"), not convictions, so I left them.

**What I read as a candidate and why I left it:**
- **§2, the bold principle** ("A system is a file…"). It is the chapter's own principle, and the §3 blocks run it: `not derivable` becomes `proved: …` after one added line.
- **§3, "A refusal is as certain as a proof".** The page scopes it ("about what is recorded and declared… not 'false'") and cites the library's comment on `Prove`.
- **§3, "a real limit"** (one edge per node pair). The run and the code's own "known limitation" back it.
- **§4, the four "I decided / I refused" lines.** They are already in the first person as his choices.
- **§6, "Where I think this stands apart".** Already marked as belief, and it ends "with the measured limits beside it". The sentence "None of that needs a store, a server, a model or a training run" sits inside that paragraph, so it needs no extra clause.
- **§6, "the fair summary of the loss".** The comparison table backs it.
- **§8, the manager and educator doors.** They state record or design facts, not convictions.

**Left for the author, as the report lists them:**
- The `EnableAutoDerive` line ("I did not run it").
- The 2022 founding dialog.
- The silent designer door.

I touched none of them.

Files, unchanged:
- `D:\GitHub\ayouni\books\softanza-book\src\en\14-knowledge-programming.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\14-knowledge-programming.md`

=====

Chapter 15 had two unowned stakes. I added one owning clause to each, in English and in French, and nothing else. `check_fr.py 15` reports ok. The style lint is unchanged from before my edits: EN hedge stacks 2 and superlatives 1 were already there, FR superlatives 1.

**Changes**

1. Section 4, the refusal to reinvent the notation for text:
   - EN: "…kept as history, for educational value, which I hold, as a view and not a result, to be the right way to retire a mechanism."
   - FR: « …ce que je tiens, comme une vue et non comme un résultat, pour la bonne façon de mettre à la retraite un mécanisme. »
   - The page gives nothing behind it, so I added nothing.

2. Section 7, the unknown-word finding, which the report named as "a stake to own":
   - EN: "…as a finding of the court, and not as a debt of mine; I hold that as my view, and the run above, on this commit, is what stands behind it."
   - FR: « …et non comme une dette de moi ; je le tiens pour mon point de vue, et l'exécution ci-dessus, à ce commit, est ce qui le soutient. »
   - What stands behind it is already on the page: the `@Banana` run and "I reproduced it on this commit".

**Left alone**
- "That is rare, and I say it" (section 6): a comparative claim about the field's headers, not named by the report. It is a stake, but I stayed within the two-per-chapter limit and the report's list.
- Section 2, "for the first time in computer science history": already his, done earlier.
- The verification report's wrong and overclaim items, the reading problems, and the exercise's unanswered questions. These are not stakes, and the exercise is the author's call under the beats rule.
- No code fence, `#-->` line or front matter key was touched. The paragraph count is unchanged.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\15-pattern-languages.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\15-pattern-languages.md

=====

Chapter 19 had one unowned stake, and I added one clause to it in each language. I ran `python -I tools/check_fr.py 19`, which returned `19-the-domain-language-model: ok`. The style lint is clean on both files: long sentences 0.0%, calques 0, forbidden 0.

**Changed (§6, "The field, and where it leads", last sentence of the last paragraph)**
- EN: "…that is what a bank, a ministry or a school can sign. I hold that as a view, not a result."
- FR: « …voilà ce qu'une banque, un ministère ou une école peut signer. Je tiens cela pour une vue, non pour un résultat. »

I added nothing after the clause. The page's own support, the why each answer carries and the refusal kept on record, is already in the preceding sentence. Paragraph count is unchanged in both files.

**Left, and why**
- §4 "free to the users of its domain": already narrowed on the page ("I tell 'free' as the ruling's word"), and the record holds no licence text. The report assigns it to the author's next answers.
- §4 "one of the estate's products" and "the earlier product": unnamed particulars, for the author's next answers.
- §6 "for a customer the plausible thing is often more useful": a concession against the thesis, not a conviction in its favour. I kept it as the second stake slot's only candidate and left it alone.
- §6 "Where I think this stands apart…": already marked as belief.
- The two phase C candidate defects in the report, which are not stakes.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\19-the-domain-language-model.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\19-the-domain-language-model.md

=====

Chapter 20 had two unowned stakes, both in §4. I added one first-person clause to each, in English and French. Paragraph counts are unchanged. `check_fr.py 20` reports ok, and the style lint reports 0 calques and 0 forbidden words on both files.

**What I changed** (the same places in `src/en/20-agents-that-cannot-hurt-you.md` and `src/fr/20-agents-that-cannot-hurt-you.md`)

1. **"I refused safe agents."** The doctrine's reason, that the field's safety "tries to make a fundamentally unpredictable actor trustworthy", was stated as fact. I added right after it:
   - EN: "I hold this reason as a view, not a result."
   - FR: « Je tiens cette raison pour une vue, non pour un résultat. »
2. **"I refused a second workbench for machines."** "Everything designed to liberate one is exactly what is needed to contain an artificial one" was stated as fact. I added right after it:
   - EN: "I hold this as a view, not a result."
   - FR: « C'est mon point de vue, non un résultat. »

Both clauses follow the wording already used in chapters 10 and 13. I added no reason, because the page offers none behind these two sentences. The next sentence ("That is the doctrine's claim, and section 6 gives its limits") still follows the first one.

**What I left, and why**
- The chess-engine analogy and the "tool surface contains no operation that touches the disk" sentence are attributed to the doctrine and carry their limits already.
- The principle sentence in §2 is the doctrine's, quoted and dated by its first commit, so it is proved on the page.
- The §3 ledger paragraph and Appendix D's definition of *ledger* (the report's other item for the author) are not stakes. I left them for his answers.
- Nothing else in the chapter states a conviction as fact without proof.

I did not touch code fences, `#-->` lines or front matter. I did not run the build or the printers. The English file was already LF.

=====

Chapter 21 (stakes): I added two ownership clauses, one per stake, in both languages. `python -I tools/check_fr.py 21` reports `21-the-court: ok`, and the paragraph counts are unchanged.

**Changed**

Both edits are in section 4, "The decision, and what I refused".

1. Stake: "A runner that folds unjudged or unperceived into pass or fail is wrong."
   - EN: added "I hold this as a view, not a result."
   - FR: added « Je tiens cela pour une vue, non pour un résultat. »
2. Stake: "A tool that verifies, warns, and then analyses anyway teaches its users to ignore the warning."
   - EN: added "This is my view."
   - FR: added « C'est mon point de vue. »

Both clauses stand alone, with no reason attached. The page gives no count, guard or project behind either claim, so I added nothing after them.

**Left, and why**

- "Rightness is a person." and the perception law: proved on the page by the bar-plot case and already attributed to the law.
- "A claim is only as good as the court that can refuse it": the page backs it with the threat model and the perception law.
- The detection-feedback-loops clause and the performance-study claims: attributed to the record.
- The unmarked "general knowledge" lines about the field (verify-report note, lines 251 and 253 in its numbering): that is a source mark, not a stake.
- "Far from being qualified": already owned as the author's verdict.
- The verify report's WRONG, OVERCLAIM and UNSUPPORTED items (hours, dates, quotation marks, "redacted" and the like): not in this task type, so I did not touch them.
- Code fences, `#-->` lines and front matter: untouched.

**Lint:** EN has 0 absolutes or superlatives. Its 1 hedge stack and 2 colon lead-ins were already there; the lead-ins sit before the limit's lists. The FR lint reports nothing new.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\21-the-court.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\21-the-court.md

=====

**Chapter 22, stakes: two clauses added, in English and French.** `check_fr 22` returns ok. The lint is unchanged from the 2026-10-11 report: no new flags, and the one hedge stack in English was already there. Paragraph counts are unchanged and the files stay LF.

**Changed** (`src/en/22-compared-honestly.md` and `src/fr/22-compared-honestly.md`):
1. §3, block four, after "An operation either honours the culture it was given, or refuses.":
   - EN: "I hold this as a view, not a result, and the culture plan's law says the same."
   - FR: « Je tiens cela pour une vue, non pour un résultat, et la loi du plan de culture dit la même chose. »
   - The report's named stake ("no facades") now owns the conviction. The only support named is the culture plan's law, which the page already cites.
2. §4, "I refused a retraction that deletes its evidence", after "Printing losses is not the rule.":
   - EN: "This is my view, and the two withdrawals the record holds, a win and a loss, are what stand behind it."
   - FR: « C'est mon point de vue, et les deux retraits que garde le dossier, un gain et une perte, sont ce qui le soutient. »
   - The support named is the two withdrawals stated in the sentence just before.

**Left, and why:**
- **Quoted or attributed:** the "a platform that shows its gaps is believed on its strengths" sentence in §2 is the site's page, attributed. The "culture plan … fake progress bar" line is the plan's own.
- **Proved on the page:** "the loss most worth printing" is argued in the next sentences (the method returns the wrong answer silently).
- **Imperatives, not stakes:** the six-doors advice to the decision-maker and the analyst, and the §9 exercise.
- **Only two allowed per chapter:** two was the cap, and the two above were the clearest unowned convictions.
- **Not mine to touch (for the author's next answers):**
  - §9 "five lines of block three's other side", where §3 shows three other-side runs.
  - §7 "my note of the night".
  - §6 the unlocated compass file.

=====

Chapter 23: two stakes owned, one clause each, in English and French. `check_fr.py 23` says ok, and `style_lint.py` finds no calque, forbidden word or emoji in either file.

**English** (`D:\GitHub\ayouni\books\softanza-book\src\en\23-a-world-a-constellation-a-platform.md`)
- Section 1, end of "The shared shape" paragraph: "This is my reading of the three, not a survey of the field." The page already says the three habits come from general knowledge, not from a study of the record. That is all that stands behind the clause.
- Section 3, "The architect, and the three scopes": after "the profile, the worlds, the governance." I added "I hold this as a view, not a result." This is the stake the 11 October report names. The page already marks the application as mine, but not "the architect is not a rank" as a belief. The estate protocol's definition of a role is already in the preceding sentence, so I added no reason.

**French** (`D:\GitHub\ayouni\books\softanza-book\src\fr\23-a-world-a-constellation-a-platform.md`)
- « C'est ma lecture des trois, non une enquête sur le terrain. »
- « Je tiens cela pour une vue, non pour un résultat. »
- Paragraph count is unchanged. The English file kept its CRLF line endings; the French file has LF only and I left it that way.

**Left untouched**
- The "I refused…" decisions in section 4. They are the author's own choices, not claims about the field.
- The sentence on isolation as a declared meaning rather than a black-box machine, which is attributed to the design.
- The comparisons with the field in section 6, which the page proves with counts, code or the Atlas.
- The architect sentences on the certification date, the withdrawn memo, the school and the site read of 9 October 2026. They are particulars for the author's next answers.

The lint reports "hedge stacks 2" on the English page ("kind of"), which was already there and which I did not touch.

=====

Chapter 29: no unowned stake, so I changed nothing in `src/en/29-a-bank-in-niamey.md` or `src/fr/29-a-bank-in-niamey.md`.

**The stake the report names.** Section 6 reads "Where I think this stands apart is that the chart is the data and the court is a rule over it." It is already marked as belief ("I think", « je pense »). Section 3's seven-regime block, section 6's limit block and section 7's built/designed/absent lists stand behind it. The brief says not to touch a sentence already marked as belief, so I left it, and adding "This is my view" would only repeat the "I think" already there.

**Other sentences I checked and left.**
- Section 1, "A bank is judged on its structure as much as on its numbers": a field claim the page frames as the field's account.
- Section 1, the governance tools "usually do not read the structure": already flagged "(General knowledge, not a study of the record.)".
- Section 4, "a rule applied to a text is something a person can read before it runs": a statement of what the chapter's own text form does, not a conviction about the field or the future. The decision it justifies is already owned in "I refused".
- Section 2, the first principle: proved by the blocks.

**Left for the author.** The report's other "needs the author" items for this chapter (the licence and installation guide, reconciling chapter 1's "built with Softanza" with the record, a delivery date) are particulars, not stakes, so I did not touch them.

`check_fr.py 29` returns ok. The style lint reports 0 calques, 0 hedge stacks and 0 forbidden words in both languages.

=====

Chapter 25 had two unowned stakes. I added one clause to each, in English and French, and `check_fr 25` returns ok. The style lint reports no calques, forbidden words or hedge stacks in either language. Its "abs" count is 9 in English and 10 in French; I did not look at what it flags. Paragraph counts are unchanged.

**Changed**

1. §3, after the "2" block, on the reader of the medium: "The reading is where a user's culture lives, the digits, the words, a local "OUI". **I hold this as a view, not a result.**" The French adds « **Je tiens cela pour une vue, non pour un résultat.** » The page proves only digits for this claim, so nothing follows the clause.
2. §8, The designer: "...should be a red cell, and not a silent omission. **I hold this as a view, not a result.** That is designed and not built, since the matrix does not exist." The French is the same. The existing "designed, not built" stays as the stage marker.

**Left untouched**

- **§4 refusals** ("Refuse, never substitute", "Voice is not a paradigm", "No inferred meaning"): the chapter already says they are the record's, "not rulings of mine". A first-person "my view" there would contradict that.
- **"A constitutional amendment wearing a library's clothes"**: the report calls it the record's image, and it is for the author to keep or cut.
- **§2 constitution quote** ("The record is silent on whether the wording is mine"): already marked. Whether the sentence is his wording is a question for the author.
- **§3, "The restaurant's medium"** (the chapter 1 sentence on the messaging-app demonstration): a particular, for the author.
- **§4 "gate" → « barrière »**: a wording choice, not a stake, so I did not touch it.

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\25-your-users-keep-their-medium.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\25-your-users-keep-their-medium.md`

=====

Chapter 24 had two unowned stakes. I added one owning clause to each, in English and in French, and left every other sentence as it was.

**What I changed (§4, "The decision, and what I refused")**
1. The agreeable fake. The sentence "An agreeable fake is more dangerous than no fake at all." is now followed by "I hold this as a view, not a result." The page's own support comes next, unchanged: "Silence is the worst answer: the lenient mode answers 501, because a miss must never be mistakable for success."
2. The gate that fails open. It now reads "A gate that fails open is worse than no gate: this is my view." The page's own account follows unchanged: the registry once kept its state in attributes, and the state now sits in a table keyed by identity.
3. French, same paragraph count:
   - « Un faux complaisant est plus dangereux que pas de faux du tout. Je tiens cela pour une vue, non pour un résultat. »
   - « Une barrière qui échoue en laissant passer est pire que pas de barrière : c'est mon point de vue. »

I added no reason that was not already on the page. I did not touch code fences, `#-->` lines or front matter.

**What I left, and why**
- The §7 engine-in-a-browser sentence, which the voice report lists. It is a fact of the record (the guard was not run, the page is not in the tree, nobody named has seen it), not a conviction. The chapter already says so in plain words, so it needs no owning clause.
- "Where I think the record stands apart is the coupling" is already marked as his view.
- "Anything that governs others must survive being copied" and "Frontier-model quality cannot be virtualized" follow from the two stakes above or from the record, so I left them. Neither would be a third stake.
- The report's other place that needs the author is whether the service plan's "user's question" of 23 July 2026 was his. It is a person or source question for his next answers, so I did not touch it.

**Checks**
- `python -I tools/check_fr.py 24` reports ok, with one warning that was there before: the number "07" is in the English and not the French.
- The style lint on both files shows no new noise: 0 calques, 0 forbidden words, 0 emoji. The English page keeps its one hedge-stack warning from before.

Files edited:
- `D:\GitHub\ayouni\books\softanza-book\src\en\24-rehearse-then-commit.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\24-rehearse-then-commit.md`

=====

Chapter 28 (stakes): two stakes owned, in English and French. Paragraph counts are unchanged. `check_fr 28` returns ok and both lints are clean (0 calques, 0 hedge stacks). I did not run the build or the printers.

**Changed (EN, `D:\GitHub\ayouni\books\softanza-book\src\en\28-a-restaurant-in-lyon.md`)**
1. §3 "The speed budget": "…so speed had to be a promise judged by something, not an aspiration. **I hold this as a view, not a result.** The budget has three numbers…"
2. §4 "I refused silent drift": "…drifts without anyone deciding to. **That is my view.** A second change of course…"

**Changed (FR, `D:\GitHub\ayouni\books\softanza-book\src\fr\28-a-restaurant-in-lyon.md`)**
1. « …pas une aspiration. **Je tiens cela pour une vue, non pour un résultat.** Le budget a trois nombres… »
2. « …sans que personne ne l'ait décidé. **C'est mon point de vue.** Un second changement de cap… »

I added no reason after either clause. The page has nothing behind them beyond what it already says.

**Left untouched, and why**
- The §3 sentence that a double answering with an empty string gives "a test that passes for the wrong reason": it follows from the plan and the sandbox's states, which the page proves.
- "The owner stops following at milestones and phasing" and the "how to ask" lesson: these are project facts from the record.
- The §6 and §7 field-leads claims: they are sourced, or marked as general knowledge or "I found nothing".
- The report's four "needs the author" items: they are for his next answers.
  - the last door versus the delivery gate
  - the state after 25 August 2026
  - who held the phone
  - "a novel of narrations"

=====

Chapter 26 had two unowned stakes. I added one clause to each, in English and French, with no other change. `check_fr 26` reports ok. The lint is clean in both languages: forbidden 0, calques 0, hedge stacks 0, and long sentences 0.0% in English and 1.3% in French. Paragraph counts are unchanged, and no code fence, `#-->` line or front matter key was touched.

**Changed** (`D:\GitHub\ayouni\books\softanza-book\src\en\26-the-environment.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\26-the-environment.md`, section 1 and section 6)

1. Section 1, after "A bar that was green by default would be the field's usual lie.":
   - EN: "That is my view."
   - FR: « C'est mon point de vue. »
2. Section 6, the status-bar bet:
   - EN: "That is a bet, and I hold it as a view, not a result; the record's own corpus argues the field's side in the same breath."
   - FR: « C'est un pari, et je le tiens pour une vue, non pour un résultat ; le corpus propre du dossier plaide pour le côté du terrain dans le même souffle. »
   - The page's own counter-evidence (the corpus arguing the field's side) was already in that sentence, so I added no reason.

**Left, and why**
- The "Places that need the author" item on `ShellStatus` gaining the specification's *unchecked* state is a design call, not a stake, so it stays for the author's next answers.
- The "(General knowledge.)" tags the verification report suggested at lines 25, 306 and 310 are a different class of item, so I did not touch them.
- Two sentences read as stakes but I left them alone:
  - "Who decides the ribbon is the author" is the author's own ruling, recorded on the page.
  - "A status bar that tells the truth" is already a stated mark of the pattern, proved by the blocks in section 3 and the strip reading in section 5.

=====

Chapter 27 had two unowned stakes. I added one clause to each, in English and in French, with no change to paragraph count. `python -I tools/check_fr.py 27` returns ok, and the style lint on both files reports no flags.

**Changed, §4 "I chose safe optimisation" (EN, `src/en/27-the-engine-beneath.md`)**
- Before: "a clean panic beats silent memory corruption, and here it costs nothing."
- After: "Not the fastest mode, and not the unoptimised one. I hold it as a view, not a result, that a clean panic beats silent memory corruption, and that here it costs nothing."
- FR (`src/fr/27-the-engine-beneath.md`): « Je tiens pour une vue, non pour un résultat, qu'une panique propre vaut mieux qu'une corruption silencieuse de la mémoire, et qu'ici cela ne coûte rien. »
- I added no reason after the clause. The page measures optimised against unoptimised, not safe against fast, so it holds nothing behind this claim.

**Changed, §8 "The decision-maker" (EN)**
- Before: "A record that prints its loss is the only kind to trust."
- After: "This is my view: a record that prints its loss is the only kind to trust."
- FR: « C'est mon point de vue : un dossier qui imprime sa perte est le seul genre à croire. »

**Left alone**
- "The surface is the promise, and the runtime is the part you measure" is already sourced to the record's design rule and the field examples.
- "A layer is a decision about what you ship, and not about taste" is a third, weaker stake. I stayed at the two-per-chapter limit.
- The three places the voice report assigns to the author: which count the site should print (the 752 that can't be reproduced), whether the runtime repository's notes are his to correct, and the unread charter section 15.

Edit script: `C:\Users\ASUSV3~1\AppData\Local\Temp\claude\D--GitHub-ayouni\88992b14-3a52-43bb-a199-d50e9b5ab27a\scratchpad\ch27_stakes.py`.

=====

Chapter 1 is corrected in both languages. `check_fr.py 1` reports ok. The lint is clean: the English calque is gone (it was "the answer may be an example", line 96), and the French is clean. I did not run the build or the printers. The English file had CRLF line endings and now has LF. Code fences and front matter are untouched, and paragraph counts match between the two files.

All 14 items are confirmed against the cited paths. These are the new clauses (French mirrors each):

1. **Haro stage:** "is being replaced by one we own, written in Zig, a charter and a spike so far, wearing the old surface so that every line I wrote can keep running". Chapter 27 lists "Haro running the library" as absent.
2. **Five registers:** "It was a proposer beside the registers of answer. Three of them… are built today… two more, a formula written and an example shown, are not yet built (Chapter 18)."
3. **"Five commitments":** "one of the commitments I made". I found no list of five, so "of five" and "that summer" are gone.
4. **Restaurant guard:** "Take a restaurant as the illustration:…", and the guard "rehearses in a twin of the files, plans, and lets an actor commit… none of them about a restaurant". Two other claims in that paragraph went with it. The commit now "is recorded with its actor and its outcome", not "its reasons". The workbench records "every operation it would perform", not "every message it would send".
5. **Watch it run:** "the site shows a recorded run of the same mechanism". The site links the decision-makers' demo and `virtual_system_twin_narrated`, not `safeworld_narrated`, so I did not follow the report's "links the guard".
6. **Second guard's plane:** "`governance_crossing_narrated`, in the system plane".
7. **Published the loss:** "I recorded the loss in the estate memo of 13 September."
8. **Court caught me:** "the study of the record caught me… the court for the layers is still only proposed". The follow-on line needed the second clause, from chapter 27.
9. **One door:** "one door, to be governed".
10. **Seven languages:** "The record's seven languages… and Chapter 16 counts them."
11. **Never compete:** "does not compete with them… will be checked by a grammar".
12. **Court born with it:** "whose court is meant to be born with it, so that, for the languages whose grammar is compiled today, an invalid sentence cannot be spoken".
13. **Platform built with it:** "whose building shaped Softanza".
14. **Generator that cannot drift:** "a verifier that refuses what a machine can check".

I used "can be" instead of "maybe" for the calque. In "the answer may be an example", "maybe" would mean "perhaps" and break the sentence.

**Left alone:**
- The front-matter `figures` line names "Luau", while chapter 27 says "I name no peer". It is a front-matter value, so the author or the build owner should reconcile the two.
- The report's reading problems are untouched: "the old surface" and "the language I was born on" are never named, "register" and "plane" come before they are defined, and line 40's list differs from the registers in line 56. They are outside the 14 items.

Files changed: `D:\GitHub\ayouni\books\softanza-book\src\en\01-change-arrives-faster-than-trust.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\01-change-arrives-faster-than-trust.md`.

=====

Chapter 30: one stake owned, in English and French. `check_fr.py 30` reports ok. The style lint is unchanged from the 2026-10-11 report on both files: no flags, and the one English "absolute" is "never" in a quoted library message. The paragraph count is the same in both languages.

**Changed.** The stake is in section 3, in the paragraph after the first dead-rule lead-in. The sentence says the library answers "the worst thing that can go wrong when a non-programmer edits a rule: a rule that quietly governs nothing." That is a conviction stated as fact. I added one sentence right after it:

- EN: "I hold that as a view, not a result."
- FR: « Je tiens cela pour une vue, non pour un résultat. »

I added nothing after the clause, because the page gives no reason beyond the block that follows it, and I did not add one.

**Left, and why.**
- Section 4, "That is the price of letting a non-programmer touch a rule": the same conviction. The clause above now owns it where it first appears. A second clause on the same belief would repeat it, so I kept to one clause.
- "The court has to tell 'nothing was wrong' from 'nothing was looked at'": the dead-rule block just above proves it on the page.
- "Authority is not permission": proved by the authority block.
- "Read this block as a limit and not as a win" and the principle "the agent proposes, and a person decides": already marked as the author's stance, or attributed to the organisation.
- The three places the 2026-10-11 report lists for the author's next answers: who chose the retained offer, whether study version 1.2 was validated, and the sister browser-side package's outbox. They are a name, a date and a source, not stakes.

**Files.**
- D:\GitHub\ayouni\books\softanza-book\src\en\30-an-organisation-in-the-field.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\30-an-organisation-in-the-field.md

=====

Chapter 31 had one unowned stake. I added one clause to it in each language. `check_fr 31` reports ok, and both lints are clean: 0 calques, 0 forbidden words, 0 superlatives.

**What I changed**

The stake is in section 8, "The designer": "A feature that no person has seen or heard ships shut, and says so. The stage is a state of the design and not an apology." It states a conviction about the craft as fact. The new clause follows it in the same paragraph, so the paragraph count is unchanged:

- EN: "I hold this as a view, not a result. What stands behind it on this page is the sound plane, where `Sing` refuses until a person has heard the voice."
- FR: « Je tiens cela pour une vue, non pour un résultat. Ce qui la soutient sur cette page, c'est le volet du son, où `Sing` refuse tant qu'une personne n'a pas entendu la voix. »

The support is only what the page already says: block 4 of section 3, and `sound_mu5_narrated` in section 5.

**What I left, and why**

- The chapter's bold principle in section 2. The chapter already presents it as its own sentence, drawn from the site's two sentences, and section 5 applies it.
- "Where I think the record stands apart" in section 6. It is already marked as belief.
- The "most often skipped when the reader is a buyer" remark in section 1. The page already marks that section as "General knowledge, not a study of the record."
- The advice lines in the other doors, and "unperceived is a state, not a failure". These are the book's own stage vocabulary and rules, not unproved convictions.
- The places in the report's section 3: whether to print the person's name beside the verdict, chapter 1's "runs" and "built with" wording, and the tutor's closing question in the exercise. They belong to the author's next answers.

Files changed:
- `D:\GitHub\ayouni\books\softanza-book\src\en\31-what-the-projects-did-not-prove.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\31-what-the-projects-did-not-prove.md`

=====

Chapter 32: I added two ownership clauses in each language. Both lints and `check_fr.py 32` report nothing to fix, and paragraph counts are unchanged. Edited files are `D:\GitHub\ayouni\books\softanza-book\src\en\32-many-minds-on-one-body-of-work.md` (CRLF kept) and `D:\GitHub\ayouni\books\softanza-book\src\fr\32-many-minds-on-one-body-of-work.md` (LF).

**Changed**
1. Section 4, "I refused to let a coordinator grade its legislator". After "A coordinator that judged its own rules would be the one part of the system nothing could fix." I added: "I hold this as a view, not a result."
   - French: « Je tiens cela pour une vue, non pour un résultat. »
   - I added nothing after it. The page already gives the structure (the Observer corrects Central, the doctrine binds it), and that sentence sits right before.
2. Section 7, "What is designed". The watcher "which is the right replacement for the clocks" now reads "which, in my view, is the right replacement for the clocks and is not written."
   - French: « ce qui est, à mon avis, le bon remplacement des horloges et n'est pas écrit. »
   - I added no reason. The page already says the clocks were stopped on 27 August and that the watcher is unwritten.

**Left, and why**
- Section 7, "the author should watch the ratio". It is already marked as the study's words, and the report says only he can own or reject it. I did not add a stance for him.
- Section 8, the educator's "at two in the morning". That is a particular; the report flagged it for his next answers.
- The §3 exclamation ("the code is clean!"), which is his to keep or cut.
- "The best sentence in the protocol", "Where I think the record stands apart", "the first principle" and "the words we use about work are part of the work". Each is either already marked as a view, attributed to a session, or tied to the page's own evidence.
- `verify/ch32.md` items other than stakes (the wrong, overclaim and unsupported lists). They are outside this task type.
- The CRLF convention of the EN file, which I preserved.

=====

Chapter 33 had two unowned stakes. I added one clause to each, in English and French. `check_fr 33` reports ok. The lint on both files shows 0 calques, forbidden words and hedge stacks, and 1 colon lead-in (the same count as before, from the five-step list). No code fence, `#-->` line or front-matter key was touched. The English file was CRLF and is now LF. Paragraph counts are unchanged.

**Changed, §4 "What I refused"**
1. Under "I refused to move a platform by rewriting it":
   - EN: "I hold this as a view, not a result: rewriting would be faster to announce and slower to trust."
   - FR: « Je tiens cela pour une vue, non pour un résultat : réécrire serait plus rapide à annoncer et plus lent à croire. »
   - The page gives nothing behind this stake, so nothing follows the clause.
2. Under "I refused an instrument as proof of a perception":
   - EN: "The counter is a result. The person is the verdict. This is my view, and the sound plane above, with its hundreds of passing assertions and its broken sound, is what stands behind it."
   - FR: « C'est mon point de vue, et le volet sonore plus haut, avec ses centaines d'assertions réussies et son son cassé, en est le fondement. »
   - The backing is already on the page in §3: the sound plane that held hundreds of passing assertions while it was, "to my ear", broken.

**Left, and why**
- §6 "Where I think the record stands apart": already marked as belief.
- The rest of the §3 sound-plane passage, the §7 limit, and the NASA readiness-levels sentence in §1: either a fact of the record, proved on the page, or the field's own position.
- The "Places that need the author" items in the report: the unnamed Principal who heard the drum, the §7 sentence about no project moving to the engine first, and the "last door" naming. These are for his next answers, not stakes to mark.

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\33-the-one-line-still-owed.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\33-the-one-line-still-owed.md`

=====

The forge work is done in both languages, and `check_fr` passes for 0, 11, 12, 16 and D. Chapter 16 has one warning, `'ring'`, which was already there. The lint is clean on every file except one false positive in the glossary. I did not run the build or the printers. The files were already LF, so there was nothing to normalise.

**(a) factory to forge.**
- Chapter 11: the stage text, the chapter-12 summary and the limit section now say forge. The French says « forge ».
- Chapter 12: the heading is now "The forge, outside the library", and every other "factory" is "forge". The French changes « usine » to « forge », including « La forge, hors de la bibliothèque ».
- Preface: it already said forge, so I left it unchanged.
- Kept in chapter 16, both languages: "factory" at line 200 ("the factory constructs and forwards") and line 270 ("Factories exist for Python, R, Julia and Prolog"). They name the library's code factories, not the forge. The French « fabrique » stays.

**(b) The mapping sentence.**
- Chapter 11: "the forge (the machinery that produces a language's parser, court, printer and grammar from its declaration alone)".
- Chapter 12: "the forge, the machinery that turns a language's declaration alone into its court and its grammar".

**(c) Chapter 16, "Which seven?".** The paragraph now begins "I ruled on 12 October 2026 which one: the six foreign runtimes of the registry above and the host". The model is excluded. The other counts are compressed into one sentence beginning "The record counts it differently elsewhere". The French says « j'ai tranché le 12 octobre 2026 ».

**(d) Appendix D.** I added the forge entry after "floor" and its French « forge. » after « étage ». Both files now have 53 entries.

**(e) Stakes owned.**
- Chapter 11, "that is a bet": "I hold that bet as a view, not a result." The French is « Je tiens ce pari pour une vue, non pour un résultat. »
- Chapter 11, the court as the core of a declared language: "This is my view."
- Chapter 12, "its power and not its poverty": "This is my view."
- Chapter 12, "the court is the core and not an accessory": "I hold this as a view, not a result."
- Chapter 16, "takes them without leaving": "I hold this as a view, not a result: section 3 shows the door carrying two runtimes in one pipeline, and nothing on this page runs numpy or pandas."
- The French clauses are « C'est mon point de vue. » and « Je tiens cela pour une vue, non pour un résultat. ».

**Left alone.**
- The chapter-12 faces question "mine, and unanswered": it is an open question, not a conviction, and the report lists it for the author.
- The bet sentence in chapter 12: it is already named as a bet.

**The lint hit.** The glossary entry "a special kind of node" (commons) trips the hedge-stack rule. It is a false positive, so I left it.

Files, all under D:\GitHub\ayouni\books\softanza-book\src: en and fr versions of 11-law-a-language-is-declared-and-closed.md, 12-a-language-declared.md, 16-seven-languages-one-door.md and D-the-glossary.md. The preface is unchanged.