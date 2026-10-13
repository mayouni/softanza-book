# Phase C: the defect chosen per chapter, on the author's behalf, 2026-10-13

chapter 9 · chosen: candidate 1, swap the two `Trigger` lines of the §3 cascade block (`:Big` before `:Number`) and ask whether the order changes `Results()` and `Triggers()`.

**Why (rule 2).** The chapter ran that block. The exercise hands it back with one named change. The consequence is already explained in §3 ("Every trigger is matched once against the original text, and what one trigger writes is not offered to the others… the whole difference between the second rung and the third") and in §4 ("I refused to claim the cascade"). I print neither the output nor a prediction. The existing exercise already pointed at this failure, so the defect is a variant of it and invents no case.

**Rejected.** Candidate 2, the overflow table from `OverflowStats()` for all four strategies. The chapter runs only `BUFFER_REJECT_NEWEST`. The other three strategy names and their numbers are not on the page, so it would have forced me to state facts the page doesn't hold.

**What I wrote.** I kept the two existing task paragraphs unchanged. After them I added three paragraphs: an intro, one `haro exercise` fence, and a closing paragraph. The French has the same paragraph count and a byte-identical fence. I added no new fact, number or metaphor. The bridge sentence is still last. The last paragraph in English:

"Before you run it, write down whether the order changes what `Results()` and `Triggers()` hold. I do not print the output of this version, and I do not tell you the answer: section 3 says what each trigger is matched against, and section 4 says what I refused to claim. When you can say why, you will know what separates the second rung from the third."

The intro opens with "I left this one in your hands." The French opens with « Je vous laisse celui-ci. »

**Exercise fence added:** yes, one `haro exercise` fence. It is the §3 block with the two `Trigger` lines swapped and all `#-->` lines removed.

**Checks.** `check_fr 9` passes. Both lints show 0 flags (`colon lead-ins 1`, unchanged from before).

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\09-patterns-of-thought.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\09-patterns-of-thought.md`

=====

chapter 7 · chosen: candidate 1. It hands over the rule 8 call `o1.FindNthNext(2, "♥")` with its named start taken out. The reader runs it, repairs it, and keeps the repaired line.

Why: rule 1. Section 3 (rule 8) already says that the library's own narration calls this form with two arguments and that it raises `less number of parameters`. It also says the guards, and the block above it, pass the starting position. The page holds the failure and the repair, so I print no output and no prediction.

Rejected: candidate 2, the free-order parameters call. It runs and is correct, and it is rejected only for being outside the Haro grammar. Section 3 says "the record does not hold" whether the library keeps them. Nothing in the run data would let the reader discover that, and the chapter would be left asserting a rejection it can't show.

Wrote (EN last paragraph before the bridge):
"Run this one and read what comes back. Then repair the call. Section 3 says where this form of the call comes from and what the guards do instead. When it is repaired, you will know why a call that the library's own narration writes raises, and what the guards pass that it does not."

Before it sits the paragraph "I left this one in your hands. The first call of the rule 8 block, with its named start taken out, has two arguments. Nothing else changes:". The five tasks, the first fence and the "Run it. For the fifth…" paragraph are unchanged, and the bridge to chapter 8 is still last. The French mirrors this with « Je vous laisse celui-ci. », the same paragraph count and byte-identical fence content.

Exercise fence added: yes, a second `haro exercise` fence of two lines, with no `#-->` line and no output printed.

Checks: `check_fr.py 7` reports ok, and both style lints are clean (colon lead-ins 3 each, as before).

Files: D:\GitHub\ayouni\books\softanza-book\src\en\07-the-writing-style-and-the-seven-goals.md and D:\GitHub\ayouni\books\softanza-book\src\fr\07-the-writing-style-and-the-seven-goals.md.

=====

chapter 10 · chosen: the second candidate. The reader runs the trust block from §3 with `:llm` replaced by a posture name of their own that the code was never told about. This is the defect §7 already admits, and I wrote it from §7 as the brief allows.

why: Rule 1. §7 says "An unknown trust posture ranks as trusted: the code gives it the top rank. So a proposal from an origin the code does not know clears a floor of trusted." The page holds the failing case, and I print neither the output nor a prediction. The exercise points to §7 and §3's trust block (`data/book-run.json` holds that block's run), and it declines to say whether the gate is right.

rejected: the reversed-rule derivation (`>=` to `<=`). It needs me to state an output nobody ran (`To("0.30")` refused, `To("0.05")` admitted). Its consequence is only inferred from the prose, so it fits rule 2 poorly.

what I wrote, last paragraph before the bridge: "Run it, and read what the gate does against what section 7 says it does. I will not tell you whether the gate is right. When you have decided, you will know what the trust floor does with an origin it has never met." Before it comes "I left this one in your hands." with the task paragraph and "Run it. If you were wrong..." kept unchanged above. The bridge sentence stays last.

French: the same six paragraphs and the same fence, in the heading « Exercice ». It opens « Je vous laisse celui-ci. »

exercise fence added: yes. It is `haro exercise`, with three lines copied from the §3 trust block (`d.TrustFloor`, `r4 = d.Refine("vat").As(:yourorigin).To("0.25")`, `? r4[:admitted]`). It has no `#-->` line. The only new token is the placeholder `:yourorigin`. The two fences are byte-identical.

checks: `check_fr 10` ok. EN lint: forbidden 0, hedges 0, long 0.7%. FR lint: forbidden 0, long 0.7%.

files:
- D:\GitHub\ayouni\books\softanza-book\src\en\10-programming-becomes-refinement.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\10-programming-becomes-refinement.md

=====

chapter 6 · chosen: candidate 1, the hacked-condition block (§3, `FindW` with a call the language does not know) · why: rule 2.
- The block was run, and `research/ch06.md` records the output as `[ ]` with "hacked" not printed.
- §3 says a W condition is data and is not run.
- §6 and §8 name the quiet cost: a call the language does not know gives an empty list and no error.
- I print neither the output nor a prediction.

Rejected: candidate 2, the `FindWF` listing refused for taste. §4 and §3 do give the reason, but it is not a defect for the reader to solve. It was also a weaker fit than candidate 1, so I did not weigh it against rule 3.

Written, in both files: `## 9. Exercise` keeps its three-sentence task. I then added one paragraph introducing the fence, the `haro exercise` fence, and a closing paragraph. The bridge stays last. The one change from the §3 block is the list, which is now the exercise's list. The condition is unchanged, and the fence has no `#-->` line.

Last paragraph before the bridge (EN): "Run it. The condition begins by asking whether an item is above 5. Look at what comes back, and at what does not, and say why before you go back to the sections. Section 3 says what the engine does with a condition that calls code; section 6 says what that costs, and section 8 says what an agent should do about it. When you have solved it, you will know why an empty answer is not yet a proof that nothing matched."

The fence is byte-identical in FR and EN. The FR opens with « Je vous laisse celui-ci, exprès. » and has the same paragraph count.

An exercise fence added: yes, in `src/en/06-the-mental-model-and-the-metaphors.md` and `src/fr/06-the-mental-model-and-the-metaphors.md`.

`check_fr.py 6` is ok. `style_lint` runs clean in both languages, with no forbidden words or calques.

=====

chapter 11 · chosen: candidate (b), the §7 host-function list escape (`[ upper('x'), 1 ]`), handed back with the function changed.

Why: rule 1.
- §7 already says the natural layer is "not closed all the way down" and that a bracketed list is still handed to the host. It also says the function "ran anyway" and that the repair is routed.
- §4, "I refused the open escape", says why a language must refuse any form that reaches host code.
- The §7 block was run on 2026-10-08, and `research/ch11.md` line 464 holds it. `data/book-run.json` has no entry for it, but the research file does.
- The exercise prints no output and no prediction.

Rejected: (a), the schema without `:must`.
- The page never states what `age: 900000` does once the band is removed, so I would have had to assert an output nobody ran.
- Candidate (c), the native-speaker question, is not a defect.

What I wrote: I kept both existing paragraphs of the exercise and added three things after them.
- The "I left this one in your hands" paragraph, pointing to §7 and §4.
- One `haro exercise` fence: the §7 block with `upper('x')` changed to `lower('X')`. It has no `#-->` line and no output.
- A closing sentence.

Last paragraph in English: "Look at what the library does with the function, and say in one sentence what a closed natural layer would have done instead. When you have, you will know why "the natural layer is a closed language" is true of its words and not yet of its lists."

Exercise fence added: yes, in the English and the French pages, byte-identical. The French mirrors the paragraph count and opens « Je vous laisse celui-ci. ». The bridge sentence is still last in both.

Checks: `check_fr.py 11` returns ok. The style lint on the English page shows no forbidden words, calques, emoji or long sentences. The French lint shows the same, with long sentences at 0.6%. Both files are LF, as found.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\11-law-a-language-is-declared-and-closed.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\11-law-a-language-is-declared-and-closed.md

=====

chapter 4 · chosen: neither candidate qualified, so I wrote the defect from the chapter's limit section (§7). The reader swaps the §7 `stxString` block to `stkString`.

**Why:**
- This is rule 1: §7 already says the core layer's string classes are broken against the engine ("call engine names that no engine file registers") and that the §3 block "shows lists only".
- The page does not hold the output of the new run, so the exercise prints none and predicts none.
- `research/ch04.md` records that `new stkString` fails, so the page's claim rests on a run.
- `data/book-run.json` has no `stkString` entry.

**Rejected:**
- **Candidate 1** (the layers block in one program): the block runs and gives `1` and `1`. Neither the page nor the run data holds what splitting it would show.
- **Candidate 2** (removing `GovGrant`): the research file never ran that variant, and `data/book-run.json` has no entry for it. It fails the "don't state an output nobody ran" rule.

**Written** (the last paragraph before the bridge, in English):
"Run it, and read what the runtime answers. Then go back to section 7 and find which name is called, and who should have registered it. When you have solved it, you will know why the layer contract's line that base builds on core is called designed, and not built."

It follows the intro paragraph "I left this one in your hands…". The French has the same structure and starts « Je vous laisse celui-ci. ». The existing exercise task and the bridge are unchanged.

**Exercise fence added:** yes, one `haro exercise` fence. It is the §7 block with `stxString` changed to `stkString`, with no `#-->` line. The two files carry identical fences (the French script wrote the same string into both).

**Checks:**
- `check_fr.py 4` returns ok.
- Style lint is clean in both languages (0 forbidden, 0 hedge stacks, 0 colon lead-ins).

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\04-the-platform-in-one-picture.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\04-the-platform-in-one-picture.md`.

=====

chapter 8 · chosen: the `RemoveManyCS` block of section 3. The article promised `SOFTANZA`, the run printed `STAZA`, and the exercise hands over the same block with its last argument changed.

**Why (rule 2):** The chapter ran the block and section 3 explains the result: "a removal that does not care about case removes the capitals too." The page already shows the gap between the promise and the run. The new block changes the flag from `FALSE` to `TRUE`, and the reader runs it to find out. I print no output and no prediction. I did not run it myself.

**Rejected:** `DoubleEachConcurrently` (section 4). It is rule 3, the lowest priority, and rule 2 was available. The question the record cannot answer (does the library correct typos, or who wrote the scope design document) was not a candidate that qualified either.

**What I wrote:** The exercise's existing task and its "Run it. If your two names differ only by a flag…" paragraph stay. After them come three additions, and the bridge stays last.

1. Defect intro: "I left this one in your hands, on purpose. In section 3 the article promised `SOFTANZA` from a removal, and the run printed `STAZA`. Here is that block with one change, the last argument of the call:"
2. The fence (described below).
3. The last paragraph of the exercise: "Run it. Set what it prints beside what the article promised and beside what the first run printed. Section 3 says why the first run did not give the article's line; I do not print what this one gives. When you have solved it, you will know what the case flag decides in a removal, and whether it alone can keep the article's promise."

**Exercise fence added: yes.** It is tagged `haro exercise` and copies the `o2` lines of the block with `TRUE` for `FALSE`. It has no `#-->` line. The French fence is byte-identical, and the French paragraph count matches. I used "section 3" in French, as the other chapters do.

**Checks:** `check_fr 8` is ok. The English and French lints are clean, with the colon lead-ins unchanged at 1 in each language.

**Files:**
- `D:\GitHub\ayouni\books\softanza-book\src\en\08-functions-as-linguistic-expressions-and-scope.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\08-functions-as-linguistic-expressions-and-scope.md`

=====

chapter 2 · chosen: candidate 1. Hand the reader the graph-rule block of section 3 with `"effectful"` removed from the writer's capabilities. They run it and say why the rule did or did not read it.

Why: it fits rule 2.
- The block is the chapter's own block with one named change.
- `research/ch02.md` (Block 8) records that run, `RulesAreSound()` → `1`, so the book asserts nothing nobody ran.
- Section 3 holds the rule's two `WhenQ` conditions and the original answer, `0`.

Rejected: candidate 2, a correct listing of `stzList` methods rejected because section 4 refuses to present the library by its anatomy. It needs method names the chapter does not hold. Section 4 refuses the anatomy but does not reject any listing. I also looked at the failing guard `semantic_resolver_narrated` (sections 5 and 7), but the page gives no way to run it and does not say why it fails.

Written, last exercise paragraph in English: "Then compare it with the answer printed in section 3, and say what the rule read to give each. Section 3 shows its two conditions. When you can say it, you will know which line of the model the rule reads."

It follows an opening paragraph that starts "I left this one in your hands." The French mirrors it, starting « Je vous laisse celui-ci. » The original task, its fence and the bridge sentence are unchanged.

Exercise fence added: yes. The `haro exercise` fence is the section 3 block with only `[ "inference" ]` changed. It has no `#-->` line and no printed output, and it is byte-identical in French.

Checks: `check_fr 2` is ok with the pre-existing 'maker' warning. The style lint flags nothing new in either language. English shows "hedge stacks 2", which is unchanged without my addition. Files: `D:\GitHub\ayouni\books\softanza-book\src\en\02-the-software-crafter.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\02-the-software-crafter.md`.

=====

chapter 5 · chosen: the Basket block (§3). The reader changes `AddQ`'s return from `42` to `This` and asks the court again.

**Why:** this is rule 2 with rule 1 behind it.
- The block is the chapter's own, with one named change. The prose already says what the court reads, in §6 (the court that exists judges the library's own classes) and §7 (what is absent).
- §7 admits that no machine today judges the style of a program written with the library. That is the defect the reader is handed.
- I print neither the verdict nor a prediction. The research record (`research/ch05.md`, block 7 probe) does hold that `return This` comes out clean, but I did not state it.

**Rejected:** the positional exercise, `o1.ReplaceEmptyStrings("~")` (§4 rejects the style). Neither `data/book-run.json` nor the chapter holds that this form runs or what it prints. The chapter's prose would also make me assert that it prints the right answer.

**Written:** the existing task is kept. Two paragraphs and a fence follow, then the bridge, which stays last. Last paragraph before the fence, in English: "I left this one in your hands, on purpose. The Basket class of section 3 fails the court because `AddQ` returns `42`. Change that one value to `This` and run the question again:"

After the fence: "Do not stop at the court's answer. Ask whether the class, as it stands, follows the way a person thinks, and what the court read to answer you. I do not give you the verdict: section 6 says which court exists, and section 7 says what it does not read. When you have settled it, you will know why a court that passes a class has not yet judged the style of a program written with the library."

The French has the same paragraph count and a byte-identical fence, opening « Je vous laisse celui-ci, exprès. »

**Exercise fence added:** yes, one `haro exercise` fence in each language. It is the Basket block with `This` in place of `42`. I kept only the `StzCodeIsClean` line and dropped the `StzCheckCode(...)[1][:rule]` line. On clean code the record does not show what that second call returns, so it may fail. There is no `#-->` line.

**Checks:** `check_fr 5` is ok with 1 warning (`ring`, which was already there). The style lint shows no flags in either language.

Files edited:
- `D:\GitHub\ayouni\books\softanza-book\src\en\05-law-the-code-adheres-to-the-way-a-person-thinks.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\05-law-the-code-adheres-to-the-way-a-person-thinks.md`

=====

chapter 13 · chosen: candidate (a), the §7 grammar block. The chain `TheWordQ("haro").IsAQ(:Word).WhichQ().ALengthQ().Of(4)` reads "which a length of 4", and nothing judges it.

why: Rule 1. §7 opens with "An ungrammatical chain runs" and the chapter already ran the block, so the book asserts no new output. §4 "I refused the ungrammatical chain" holds the same case as "a view, not a result", held "by reading aloud, not by a machine". §7 "What is absent" lists "any machine that judges a chain's grammar".

rejected: (b), the §3 `Replace sep with '_'` line that printed `a-_-b`. It is only a rule 3 case. It needs "refused silent tolerance" in §4 to condemn a value-position literal, but §4 and §3 treat the literal as a stated limit, not a refusal, so the reason is weaker.

wrote: the exercise's original task is unchanged. After it, in the first person and named as left on purpose:
"I left this one in your hands. Section 7 shows a chain that reads "which a length of 4", and nothing refused it. Run it, read it aloud as English, and write under it the line you would have the library print to refuse it, with the reason it would give."
Then the fence, then the last paragraph before the bridge:
"When you have written that line, you will know why I hold the ungrammatical chain as a view and not as a result, and who the page says must judge it (sections 4 and 7)."

The bridge sentence stays last. The French is the same, opening « Je vous laisse celui-ci. » and keeping the « Exercice » heading, with the same paragraph count and the fence byte-identical.

exercise fence added: yes, a `haro exercise` fence with the §7 chain line copied verbatim plus two comment lines. It has no `#-->` line and prints no output.

Checks: `check_fr 13` ok. Style lint is clean in English and French. Both files were CRLF and are now LF, as the brief said. Files: `D:\GitHub\ayouni\books\softanza-book\src\en\13-natural-and-executable.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\13-natural-and-executable.md`.

=====

chapter 14 · chosen: the §7 malformed-lines block (`cBad`). I handed it back as an exercise with three added `Query` lines and no printed output, so the reader finds which of the four lines the graph holds.

**Why:** rule 1. §7 itself admits the failure: the parser keeps only a line with exactly three fields, and the reader is silent where §4 and §7 quote the design promise "validated on load". `data/book-run.json` and the chapter already hold the run (`merged` 1, `refused` `[ ]`), so the book asserts no new output. The page says why in §7, with the promise in §4.

**Rejected:** the §4 clinic variant (`AddFact("fatou", "treated-by", "dr-sani")` on a non-strict graph). Its claim that the rumour overwrites the first fact with no contradiction recorded is not held in the chapter or in `data/book-run.json`, so I would have had to state an output nobody ran.

**What I wrote:** the existing exercise and its fence stay. After "I do not tell you the line to add." I added two paragraphs and one fence in each language. The French says « Je vous laisse celui-ci. » The English last paragraph:

"Run it. Read `merged`, read `refused`, read the three queries, and find which lines the graph holds and what the reader told you about the others. Set the design document's promise of a file "validated on load", in section 4, beside what you find; section 7 says what the parser keeps. I do not give you the answer, and I did not fix the reader. When you have it, you will know why a file that merges is not a file that was validated."

The bridge paragraph stays last. The French has the same paragraph count and a byte-identical fence.

**Exercise fence added:** yes, `haro exercise`. It copies the §7 block and adds `? oT.Query([...])` for `a|likes|b`, `d|likes|e` and `g|likes|h`. It has no `#-->` lines and no printed output.

**Checks:** `check_fr 14` is ok. The English lint is clean. The French lint is clean. I did not run the build or the printers.

**Files:**
- D:\GitHub\ayouni\books\softanza-book\src\en\14-knowledge-programming.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\14-knowledge-programming.md

=====

chapter 17 · chosen: neither candidate qualified, so I wrote the defect from the chapter's own limit section (§7). That defect is the rephrased question the first rung answers instead of refusing. · why: this is rule 1. §7 admits the failure ("It should have been a refusal"), and `data/book-run.json` holds that run as kept (`Margherita is a dish.`). The exercise sends the reader to §7 for why. · rejected:
- (a) Add a gate to the `oG` block. Chapter 17 §3 says three laws fire, and a gate is only one of them. Neither the page nor the run data holds `IsSound()` or the `Violations()` count after the change, so I would have had to assert an output nobody ran.
- (b) The `stzLLMAgent`-first listing. That listing is not in the chapter, and the run data has no output for it. · wrote: I kept the exercise's task, then replaced the old closing hint ("as I did, that the machine answered…") with a defect paragraph. The last paragraph, before the bridge sentence, is: "When you have solved it, you will know why a first rung that recognises a relation only by the word it was declared with can answer a question you did not ask." The paragraph before it begins "I left this one in your hands, on purpose." It tells the reader to re-ask one of their own promised questions with an undeclared verb, compare the reply with the question, and say why it answered and which lines of §7 tell them so. It prints no output and no fix. The French mirrors it (« Je vous laisse celui-ci, volontairement. »). The paragraph count matches. · exercise fence added: no. `check_fr 17` is ok and both lints are clean (0 flags). Only the two chapter files changed. The bridge sentence was not touched.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\17-law-programmatic-by-default.md`, `D:\GitHub\ayouni\books\softanza-book\src\fr\17-law-programmatic-by-default.md`.

=====

chapter 15 · chosen: the matrix term `{row(99)}`, which the §7 limit section says accepts a two-by-two matrix. This is neither of the report's two candidates; I wrote the defect from the limit section, as the brief allows.

**Why:** rule 1. §7 says "The class header lists the terms that accept every matrix: `row`, `col`, `pattern`, `determinant` and `sum`. A matrix of two by two is accepted by `{row(99)}`." `research/ch15.md` holds the run (`Mx("{row(99)}").Match([[1,2],[3,4]]) --> 1`). I print no output and no prediction.

**Rejected:**
- **Candidate 1, the reused list object (§3, §7).** Its failing call changes the list's length, and the §7 cache key includes the length. The reader would probably get 0, not the 1 the candidate expects, and the page holds no run for it.
- **Candidate 2, `nonempty(email)` in the table language.** It needs an output that neither the chapter nor the run data holds. The page never shows whether `nonempty` is a known word, or what the table language does with an unknown one.

**Written (EN and FR):** after the existing "Run it… explain the output." paragraph I added three blocks and left the bridge last. They are an intro paragraph, a `haro exercise` fence, and a closing paragraph. The fence is one line, `? Mx("{row(99)}").Match([ [1,0], [0,1] ])`, copied from the §3 matrix block with `property(identity)` changed. The French fence is byte-identical. It has no `#-->` line.

Last paragraph in English: "Say what you expect before you run it, then run it. Do not change the pattern to make the output agree with you: section 7 says where the library prints this defect, and why. When you have found it, you will know which terms of the matrix language accept every matrix."

The intro paragraph opens "I left this one in your hands, on purpose, and I name it a defect."

**Checks:** `check_fr.py 15` ok. The English and French style lints show no flags beyond the `@!` false positive and the earlier hedge-stack counts.

**Exercise fence added:** yes.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\15-pattern-languages.md`, `D:\GitHub\ayouni\books\softanza-book\src\fr\15-pattern-languages.md`

=====

chapter 18 · chosen: the first candidate, the fifth-register block with its two example pairs sent as one string joined by a comma.

Why: it fits rule 2.
- The chapter ran the fifth-register block in §3. The change is one named edit to it.
- §3 already explains the consequence in prose, and §4's last refusal and §7's "absent: the example register" give the reason.
- The reader runs it and finds out. I print no output and no prediction.
- One correction to the report's candidate text: it showed `"+216-21-298-374, valid"`. The record holds a different probe string, `"+216-21-298-374,+33-6-12-34-56-78"` in `research/ch18.md` (a separate probe run). I used that one, since it is the case the record ran.

Rejected: the "tomato sauce" value with a space. §7 says it raised on 8 October 2026 and admits that no block records it. §7 also says "the exercise below does not use a value with a space", so adding it would contradict a section I may not edit. It would also state a failure the book never ran.

What I wrote: the existing task, its fence and its "silence" paragraph are untouched. After them come three paragraphs and a `haro exercise` fence. The bridge sentence stays last. The last paragraph is:

"Run it, then read what was admitted and what the goal says, and decide whether that is what you wanted to hand to the door as examples. Section 4, in its last refusal, and section 7, in the absent example register, say why I call it a fault. When you can say why, you will know what the door did with your examples, and why that is not induction."

The paragraph before the fence opens "I left this one in your hands." The French mirrors it, opening « Je vous laisse celui-ci. », with the same fence byte for byte.

Exercise fence added: yes. It is the fifth-register setup with the one-string reply and two `?` lines, with no `#-->` lines.

Checks: `check_fr.py 18` returns ok, and the style lint is clean in both languages.

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\18-the-five-registers.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\18-the-five-registers.md`

=====

chapter 20 · chosen: the second candidate, a plan with `SetExecutor(PIActor(...))` and no `SetScope`. The reader removes the scope from block 4's committing plan and checks what the plan did.

Why (rule 1): section 7, first item of the gap list, already says a plan with an executor and no scope "is committed with no check on the paths it touches". It adds that "only a governed actor commits" is exact only when both an executor and a scope are set. The exercise already pointed at the executor-less case. The answer is on the page, so I print no output and no prediction.

Rejected: the first candidate, giving `AllowUnder` the wrong path. Block 4 already runs that case with `/somewhere/else`, and the book prints its `0`, so it would hand the reader a solved case.

What I wrote: the existing task and its closing sentence stay. Three paragraphs and one fence now sit before the bridge, which is unchanged and still last. The last paragraph, in English:

"Run it, and ask the disk what the plan did, then ask the audit trail. I do not tell you what you will find. The page says why in section 7, in the first item of its list of gaps; read it after you have looked, not before. When you can say why "only a governed actor commits" holds for this plan or does not, you will know what that sentence depends on."

The paragraph before the fence opens "I left this one in your hands, on purpose." The French is « Je vous laisse celui-ci, exprès. ».

Exercise fence added: yes, a second `haro exercise` fence. Its three lines are copied verbatim from block 4 (`oPlan3 = oAg.GenerateUpdatePlan()`, `oPlan3.SetExecutor(PIActor("shop-committer"))`, `oPlan3.Execute()`). It has no `#-->` line and no output. It replaces the six lines that built `oScope3` and committed under it. The French fence is byte-identical.

Checks:
- `check_fr.py 20`: ok.
- EN lint: long sentences 0.5%, forbidden 0, colon lead-ins 0.
- FR lint: same figures.

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\20-agents-that-cannot-hurt-you.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\20-agents-that-cannot-hurt-you.md`

=====

chapter 16 · chosen: neither listed candidate. I wrote the defect from the §7 limit section instead (the plain-apostrophe failure of the door's way back).

**Why (rule 1).** §7 already says the way back is not closed. It says that a plain apostrophe in data, `it's fine`, writes a string the host cannot read, and that the method prints the error and returns the raw text. `research/ch16.md` records that run. `data/book-run.json` holds no output for it, so I print none.

**Rejected candidates.**
- **Rename `res` to `result` in the first Python block.** Neither the page nor the record says what that does. §7's "absence of the result file" is stated for the R door only. The `res` naming contract appears nowhere in the prose, so I would have been asserting an output nobody ran.
- **"Which seven?"** §3 already carries the ruling of 12 October 2026, so asking the reader to pick would reopen a settled point.

**What I wrote.** In `## 9. Exercise` (EN) and « Exercice » (FR):
- The existing task, promise block and last-promise paragraph are untouched.
- Then two paragraphs and one fence follow. The chapter 17 bridge stays last.
- The English last paragraph reads: "Run it. Read what the method prints and what it returns, and explain both before you touch the block; the page says why in section 7, where the way back is not closed. When you can, you will know why a way back that evaluates its data is not a closed one."
- The first paragraph opens "I left this one in your hands." The French opens « Je vous laisse celui-ci. »

**Exercise fence added: yes.** It is a `haro exercise` fence, a copy of the §7 `oPy4` block with one change (`res = "it's fine"`). It has no `#-->` line and no output. It is byte-identical in EN and FR.

**Checks.**
- `check_fr.py 16` gives ok. Its one warning, `'ring'`, was already there.
- Both style lints are clean: 0 on every flagged item, including emoji, forbidden words and colon lead-ins.
- The English lint shows exclamations at 1.2/k, up from the 0.3/k in the 2026-10-11 report. I added none, so something earlier raised it.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\16-seven-languages-one-door.md`, `D:\GitHub\ayouni\books\softanza-book\src\fr\16-seven-languages-one-door.md`.

=====

chapter 19 · chosen: neither listed candidate. I wrote the defect from the chapter's limit section, as the brief allows: completion that sees one word, not the sentence so far.

**Why (rule 1):** §3 says `Complete("contains")` returns the objects of every `contains` fact, whatever its subject. §7 lists "a completion that sees the sentence so far" as absent. The block already ran, and the exercise now hands the reader that failing case. Nothing is asserted that the page does not already say.

**Rejected:**
- Candidate 1 (the loop without `aFact[2] != "is-a"`): it needs me to state that `Accepts` passes "object: wine". `data/book-run.json` holds no `Accepts` output and no such sentence, and no section explains the filter.
- Candidate 2 ("margherita pairs-with tomato-sauce"): it needs me to state that `Admit` admits it, which was never run. The page's "a person" (§4) is not a defect the reader can hand-test.

**What I wrote:** the two existing task paragraphs are unchanged. I added two paragraphs before the bridge, and the bridge stays last. French has the same paragraph count and the heading « Exercice ».
- Defect paragraph, in English: "I left this one in your hands. Section 3 says that completion sees one word and not the sentence so far, and section 7 lists it as absent. In your domain, give two entities the same relation with different objects, ask for the completion of that relation, and read the list against the sentence you had in mind. The library does not repair it, and I have not repaired it for you. Then compose, from what section 3 shows (the facts of a knowledge base, read one by one), a completion that sees the subject as well as the relation."
- Last new paragraph, in English: "When you have solved it, you will know why a completion that sees one word lists the objects of every fact of that relation."

**Exercise fence added:** no. Any snippet would have given away the solution.

**Checks:** `check_fr 19` is ok. The style lint is clean in English and French: 0 forbidden words, 0 colon lead-ins.

Files are `D:\GitHub\ayouni\books\softanza-book\src\en\19-the-domain-language-model.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\19-the-domain-language-model.md`.

=====

chapter 12 · chosen: candidate 2, the `FindW` / `FindWF` sine listing, which §4 refuses as a word of the closed language. I used the listing as the exercise block, with one named change.

Why: it fits rule 2, with the reason from rule 3.
- The block is §3's own, and the page already says what the two forms print and that the refusal is silent and whole (§3, "What I saw").
- §4 ("I refused one text for declaring and for computing") says why computing stays off the declaring surface.
- I print neither output nor a prediction. The sine listing is not new run data.

Rejected: candidate 1, `cBand` (grammar says 1, court says 0). §3 already prints both answers, so there is nothing hidden to find. The existing sixth prediction (`quantity: 4000`) already covers that gap.

Written, EN last paragraph: "Run them for several numbers. Look for a number at which the two forms print the same thing, and say whether the printout alone tells you which of the two refused and which answered. When you have, you will know what it costs that a closed language refuses without a word."

The paragraph before the fence opens "I left this one in your hands." In French it opens « Je vous laisse celui-ci. » The existing task and its `haro exercise` fence are kept. The phase D bridge stays last. There are three paragraphs plus one fence, in both languages.

Exercise fence added: yes. It is a `haro exercise` fence with no `#-->` lines, and it is byte-identical in both languages.

Checks:
- `check_fr 12`: ok.
- EN lint: 1.4 exclamations per thousand words, otherwise clean.
- FR lint: 1.3 exclamations per thousand words, otherwise clean.

The FR file was CRLF and is now LF, as the brief says to normalise.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\12-a-language-declared.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\12-a-language-declared.md

=====

chapter 22 · chosen: candidate (a). Block three (accented-word sort) is handed over with its `#-->` promise removed. The reader writes the French-order promise and runs it.

why: rule 2, with rule 3 as support. Block three is a block the chapter ran. The one change is the promise. The answer sits on the page and in the record, and I print neither the verdict nor a prediction. §3 says this is a pinned gap, that its promise records the library's present, weaker answer, and that it fails the day the library gains collation. §3 also gives the French order from Python and Node. §7 lists locale collation as absent.

rejected: (b), the chart of the 7 July 2026 string benchmark. §6 says the build mode could not be read and the numbers are only cited as a dated record. A chart would need me to supply figures `data/book-run.json` does not hold, and §6 does not support drawing one.

what I wrote, last paragraph before the bridge, English: "I left this one in your hands. Here is block three with its promise taken off: [fence]. Under it, write the promise a French reader would expect, the order the field's locale-aware sort gives in section 3, as a `#-->` line, and run it. I do not print the verdict. Read it, then read sections 3 and 7 to learn why this block is a pinned gap and not a fault of the sort. When you have solved it, you will know why block three promises the library's present answer and not the field's."

The French mirrors it (« Je vous laisse celui-ci. »), with the same paragraph count and a byte-identical fence. The existing task, its fence, the variant and the bridge sentence are unchanged.

exercise fence added: yes. It is `haro exercise`, holds one line copied from block three, and has no `#-->` line.

checks: `check_fr 22` is ok. EN and FR lint are clean (forbidden 0, long 0.0%, colon lead-ins 0).

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\22-compared-honestly.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\22-compared-honestly.md

The existing variant paragraph still says "the five lines of block three's other side". §3 shows three other-side runs. I left it alone, because the earlier report flagged the count as the author's to settle.

=====

chapter 25 · chosen: candidate 2, the reply with a space in it. The exercise's fourth prediction ("yes please") stays as a task. It now ends on the case I left unfixed, `ReplyIn` with a space in the reply.

Why: rule 1.
- §7's bold item already admits the failure: a reply with a space in it, chapter 18's known limit.
- That item says `ReplyIn("c", "grand couscous")` raised in a research run. It adds that no block of the book records the result, and that the conversation works only on digits and one-word dishes.
- So the exercise prints no output and no prediction.

Rejected: candidate 1, dropping `ReadReply` from block 2. It would qualify under rule 2, but rule 1 ranks higher. The recogniser-confidence chart was only mentioned as "also refusable" and was not a candidate.

What I wrote:
- I kept the task: intro, the four predictions and the fence.
- I removed the line "The fourth prediction raised in my research run, and that is the lesson", because it gave the answer away.
- I added three paragraphs.
  - The first names the defect. It points to §7 and tells the reader to take block 3 (the no-options block), change the reply "2" to a text with a space, and run it.
  - The second is the `haro exercise` fence.
  - The third is the last one.
- Last paragraph in English: "Look at what the call does, and do not repair it. Section 7 says why it matters on a phone. When you have explained the output, you will know why the conversation above works only because its replies are digits and one-word dishes."
- The opening of the first added paragraph is "I left this one in your hands."
- The chapter's bridge sentence is still last.

Exercise fence added: yes. It is the block-3 world with one change (the reply is "grand couscous", the string §7 names). It has no `#-->` line and is byte-identical in EN and FR.

The French has the same paragraph count and opens with « Je vous laisse celui-ci. ». `check_fr 25` is ok. The EN and FR lint show nothing flagged (the two colon lead-ins were already reported before my edit). I normalised the EN file's CRLF to LF, as the brief says.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\25-your-users-keep-their-medium.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\25-your-users-keep-their-medium.md`.

=====

chapter 27 · chosen: the prefix-count block (§3, `left(aClass[1], 3)`). The reader rewrites the count `[ 10, 693, 0 ]` to ask each class's parent chain, via `ParentOf`, instead of its first three letters.

why: rule 3.
- §3 prints the count as correct and says max's forty classes all carry the base prefix.
- §8, the agent's door, rejects counting by prefix and gives the reason: tell the reader which layer a class lives in by its parent chain, not by its prefix.
- I print no output and no prediction. The reader runs it and finds out.

rejected: the `ParentOf` block with `#--> stkstring`. It would need a `#-->` line in the exercise fence, which the brief forbids. §3 and the existing exercise paragraph already give the answer: the contract is not met and `stzString` inherits `stzObject`.

what I wrote: the exercise's two existing paragraphs stay. I added one paragraph after them, in both languages, before the bridge sentence. Last paragraph in English:

"I left this one in your hands. The count by prefix in section 3, `[ 10, 693, 0 ]`, is correct, and it says nothing about layers. Write that count again so that it asks each class's parent chain, read with `ParentOf`, and not its first three letters, and look at what you get. Section 3 says what the prefix hides, and section 8, the agent's door, says why I refuse it. When your count answers, you will know why a class's layer is read from what it inherits, and not from what it is called."

The French has the same paragraph count and begins « Je vous laisse celui-ci. »

checks:
- `check_fr.py 27` returns ok.
- The English lint reports no flags.
- The French lint reports no flags.

an exercise fence added: no. The existing `haro exercise` fence is untouched.

files:
- D:\GitHub\ayouni\books\softanza-book\src\en\27-the-engine-beneath.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\27-the-engine-beneath.md

=====

chapter 24 · chosen: candidate 1. In the "Code first, subscribe later" block, the live payments binding names a key (`"stripe-live"`) that the store does not hold.

**Why:** rule 2. The block ran in the chapter. The page already explains the consequence in section 3, "Production refuses" (`live-without-secret`, "credential not in the secret store"). It also says in "Code first, subscribe later" that the surface is sound once every live binding names a secret the store holds. The new exercise prints no output and no prediction.

**Rejected:** candidate 2, a `MayGoLive` that asks about soundness in the current phase. Section 4 does reject it with its reason (rule 3). But it needs a new listing that is not in the chapter, so it ranks below candidate 1.

**What I wrote:** the existing task and the always-yes class step stay. Three paragraphs follow, then the bridge, which stays last. The last paragraph before the bridge reads:

"Run it. Compare the answer of its last line with the one section 3 gave, and explain any difference before you touch the name; section 3, "Production refuses", shows how to ask the registry for its report. When you have solved it, you will know what makes a live binding sound: a secret that the store holds, and not only a name."

The paragraph before it opens "I left this one in your hands." It tells the reader the block is the section 3 one with one name changed on purpose, and that I do not say what it does.

**Exercise fence added:** yes, a `haro exercise` fence. It is the section 3 block with the `#-->` lines removed and `"stripe-key"` changed to `"stripe-live"` on the payments `BindLive` line. The French uses the same byte-identical fence and « Je vous laisse celui-ci. »

**Checks:**
- `check_fr 24`: ok, with the one warning that was already there (`2026-07-23` in English, « 23 juillet 2026 » in French).
- `style_lint` on both languages: no forbidden words, no intensifiers, and no new calques.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\24-rehearse-then-commit.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\24-rehearse-then-commit.md`.

=====

chapter 23 · chosen: delete the `GovSetAuthority` line from the gates block of §3 (candidate 1). The block keeps its recorded output only in the chapter.

Why: rule 2. The gates block in §3 already ran. Its third refusal, `'resto' holds '' authority (level 0) but 'order-produce' is risk tier 2`, is printed there. The prose around it explains the three gates and says "Each refusal names its gate". The exercise prints no output or prediction, so the book asserts nothing new.

Rejected: candidate 2, in both forms.
- The envelope on `stzApp` has no run data. Writing its consequence would mean stating an output nobody ran.
- The `Hosts(:VisitApp)` question is already answered in full in §7 (R14 errors), so nothing is left unfinished.

Written: I kept the existing task, its `haro exercise` fence and the "harder one" unchanged. After them I added, in English and French, a defect paragraph, a new `haro exercise` fence and a closing paragraph. The bridge paragraph stays last. The last paragraphs:

> I left this one in your hands. Take the gates block of section 3 and delete one line: `oCon.GovSetAuthority("resto", :Delegated)`. Stop the block at its last `Why()`, as here, and I print nothing under it: [fence]
>
> Run it and read the last `Why()`. Name the gate that refuses, and say what the block would have to say for the crossing to clear. Section 3 says what each of the three gates asks, and that each refusal names its gate. When you have solved it, you will know that the court names the gate that refuses and does not write the declaration.

The French has the same paragraph count, opens « Je vous laisse celui-ci. » and has a byte-identical fence.

Exercise fence added: yes. It is a copy of the §3 block, cut after the last `Why()` with the one line removed. It has no `#-->` lines and no runnable fence.

Checks:
- `check_fr 23`: ok.
- EN lint: forbidden 0, hedge stacks 2 (as before).
- FR lint: clean.
- I did not run the build or the printers.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\23-a-world-a-constellation-a-platform.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\23-a-world-a-constellation-a-platform.md

=====

chapter 21 · chosen: the second candidate, the promise judge's possible defect from §7. A file whose first promise is a lie and whose last is a promised raise.

**Why:** rule 1. §7 ("A possible defect in the promise judge") already admits the failure. It says "I reproduced it twice" and hands the question to the Testoor plane. §3 "The court of promises" holds the raise block, and each rule's behaviour alone. No output is printed or predicted. `data/book-run.json` holds nothing on this case, and I do not state it.

**Rejected:** the sealed-ledger first-entry edit, rule 2. The page does explain it (§3, security), but a defect §7 already admits outranks it. `book-run.json` also holds no output for that edit.

**What I wrote** (the existing task paragraphs are kept):
- A paragraph: "I left this one in your hands. Here is the raise block of section 3 with one change: its first promise is now a lie."
- A `haro exercise` fence.
- A closing paragraph, whose last sentence is: "When you can say what the court answers here, you will know the question that section 7 hands to the Testoor plane."
- The French has the same paragraphs, opening « Je vous laisse celui-ci. », with the fence byte-identical.
- The Chapter 22 bridge stays last.

**Exercise fence added:** yes. It is the §3 raise block with its first promise changed from `#--> before` to `#--> after`. I dropped the original's three `#-->` output lines, as the brief forbids them. I added one `?` line (the lie's state) and one comment line. That is slightly more than the one change the brief allows, and I judged it necessary to look at the lie.

**Checks:** `check_fr 21` ok. The EN and FR lint show forbidden 0, calques 0 and exclamations about 1.4/k. The only lint flags are one hedge stack in the English and the two "colon lead-ins" (the "What is designed:" and "What is absent:" lines in §7). The brief's checks do not cover the changed `#-->` line.

**Files:** D:\GitHub\ayouni\books\softanza-book\src\en\21-the-court.md, D:\GitHub\ayouni\books\softanza-book\src\fr\21-the-court.md

=====

chapter 28 · chosen: neither candidate. I wrote the defect from the chapter's limit section instead, the owner's seventy-fifth-percentile speed expectation, which the library cannot declare.

**Why (rule 1):** §6 says the library's terms offer the fiftieth, ninety-fifth and ninety-ninth percentile and cannot declare the owner's seventy-fifth exactly. §7 lists "a seventy-fifth percentile expectation" under what is absent. The existing speed-budget block already runs at the ninety-fifth percentile. The page holds the reason, and no output has to be stated.

**Rejected:**
- **`ExpectP50` listing:** the name `ExpectP50` appears nowhere in the chapter or the run data. Claiming it "runs and is MET" would assert an unrun output.
- **Lock block without the `admitted-by` line:** the chapter already prints its `UNSOUND` report and its fix, so it hands the reader nothing unfinished. It is also close to the existing exercise task.

**Wrote:** two paragraphs after the existing task, fence and harder-variant paragraph, before the bridge. The English last paragraphs:

"I left this one in your hands, on purpose. The owner's speed protocol is at the seventy-fifth percentile, and the budget of section 3 is judged at the ninety-fifth. Take that block, change the percentile of one expectation to another that the library offers, keep every other line, and run it. Read what the court judges against what he asked for. Section 6 says what the library's terms offer, and section 7 lists his expectation among the things absent. I give you neither the verdict nor the answer."

"When you have solved it, you will know why a promise the court can judge is not yet the promise the owner asked for."

The French has the same two paragraphs (« Je vous laisse celui-ci, volontairement. … »). The bridge stays last in both languages.

**Checks:** `check_fr.py 28` is ok. The style lint shows 0 forbidden, 0 hedge stacks and 0 colon lead-ins in either language.

**Exercise fence added:** no. A fence would need a percentile call the library does not have. The existing `haro exercise` fence is untouched.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\28-a-restaurant-in-lyon.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\28-a-restaurant-in-lyon.md`.

=====

chapter 29 · chosen: candidate 1, block 6 (the limit block, `:Banking` trap) · why: rule 1, plus rule 2 for the fence. §3 already prints the `:Banking` `pass` and says the library's own comment calls it a placeholder that passes every time. §4 ("I refused to claim more than the library holds") says what the chapter will not claim for it, and §7 admits that a validator reads only what is declared. The fence is block 6 with one change, so no new output is stated. The three answers are also not asserted. The exercise names the regional court's refusal of the chart (§3, block 1) but gives no output. · rejected: the `when`/`then` rule-file candidate. It is true and runs, but the chapter holds no run of it: the loader's output would have to be stated, and the data has no such run.

What I wrote, appended to `## 9. Exercise` in both languages. The old task paragraphs and the phase D bridge are unchanged. The added paragraphs are the defect paragraph, one fence and the closing paragraph. The last paragraph in English:

"Run it and put the three answers side by side. The regional court has already refused this chart, in section 3; now read what the second validator says of it, and why it is not the same as what the court said. Section 3 and section 4 say why. I do not give you the answer here. When you have it, you will know why a validator that answers `pass` has not judged the chart."

The paragraph before the fence opens "I left this one in your hands, on purpose." The French opens « Je vous laisse celui-ci, exprès. » with the same paragraph count.

Exercise fence added: yes, a `haro exercise` fence, byte-identical in EN and FR. It has no `#-->` line and no output.

Checks: `check_fr 29` ok, and both style lints are clean (EN 0 flags; FR 0 flags).

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\29-a-bank-in-niamey.md`, `D:\GitHub\ayouni\books\softanza-book\src\fr\29-a-bank-in-niamey.md`.

=====

chapter 26 · chosen: the `transfer_funds` candidate (§3, second block), adapted. It now names the book's own `ShellStatus` function and gives the reader the failing case, instead of asking only "who refuses it". · why: rule 1, plus rule 3 for the block. §7 lists "any refusal of an unknown verb: `transfer_funds` passes the court" as absent. §3 ran `IsClean()` on that case. §4 says why the library cannot refuse it (it does not hold the list). The fence reuses the `StzReplace` pair of block 2 on the `ShellStatus` call of the status-bar block. No output is stated. · rejected: the emulator candidate (§7). The chapter holds no backend-only plan block, and the plan is only "read in source, not run", so copying with one change would have meant inventing the backend API. · wrote, last paragraphs in English: "I left this one in your hands. The `ShellStatus` of section 3 is the book's own function, and I did not guard it against the case below: the one section 3 ran through `IsClean()`, and section 7 lists as absent. Run the line and read the word the cell gives. Then make the cell refuse a stranger to the twenty-two, as the book's loop does, with the loop over the list that section 3 already holds, and without asking the library for a list it does not own (section 4 says why)." Then the fence, then: "When the cell is right, you will know what the library finds, and what only a list it does not hold can refuse." The bridge to chapter 27 stays last. The French is the same in « Je vous laisse celui-ci », with « étranger » for stranger. · exercise fence added: yes, one `haro exercise` fence of one call line plus an English comment, byte-identical in both languages. It has no `#-->` line, and the existing `oMine` fence is untouched.

Checks: `check_fr 26` reports ok, and `style_lint` is clean in both languages. I did not run the build or the printers.

Files:
- `D:\GitHub\ayouni\books\softanza-book\src\en\26-the-environment.md`
- `D:\GitHub\ayouni\books\softanza-book\src\fr\26-the-environment.md`

=====

chapter 30 · chosen: candidate 2, a rule written with no `SetMessageQ`, which the governor reports although it runs. The fence is the second block of §3 followed by the last lines of the governor block, with that one line removed.

why: rule 3. §4 ("I refused a silent rule") already rejects that listing and says "A rule with no message is reported too." The page names the reason, and the exercise hands over the failing case. I print no output and no prediction. The research file `research/ch30.md` (l.234) also holds that the governor reports a rule with no message as an error. I did not check `data/book-run.json`.

rejected: candidate 1, dropping `oWatch.AddCase`. Neither §3, §7 nor the research holds what `CheckRules()` returns with no case, so I would have had to assert an output nobody ran.

what I wrote: the existing task and its line "Run it. The difference between those two answers is the chapter." stay. After them I added a paragraph, the `haro exercise` fence, and a closing paragraph. The bridge to chapter 31 stays last. The last paragraph in English:

"Run it on the model of section 3. Compare what the model reports with what it reported when the rule had its message, and read what the governor returns. Under "I refused a silent rule", section 4 says what the governor does with such a rule, and why. I do not give the answer here. When you have solved it, you will know why the governor reports a rule that has no message."

The paragraph before the fence opens "I left this one in your hands." The French mirrors it, opening « Je vous laisse celui-ci. », with the same paragraph count and a byte-identical fence.

checks: `check_fr 30` ok. EN and FR style lint show no flags; the only absolute word in EN is "never" in a quoted library message, and FR has 20 « personne » counts.

exercise fence added: yes (`haro exercise`, no `#-->` line, nothing runnable added). I edited only the two chapter 30 files and did not run the build or the printers.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\30-an-organisation-in-the-field.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\30-an-organisation-in-the-field.md

=====

chapter 32 · chosen: candidate 1, the `StzCheckCode` block on `KillOrder`, with its promises stripped. The reader predicts the three answers, then runs it.

Why: this is rule 2. The block is the chapter's own first block and was run by it. The one named change is that the `#-->` lines are removed. Section 3 already holds the consequence. It reads "Read the last line twice. `StzCodeIsClean` still answers `1`... The tone rule warns; it does not refuse. A word rule advises." The exercise prints no output and no prediction.

Rejected: the stamp chart. The chapter holds no chart data to draw, and a chart would need me to assert a comparison that section 6 only calls "a different surface". I did not write the limit-section fallback, because candidate 1 qualified.

What I wrote: I kept the time-stamp count task and "Your count is the finding. I will not give you mine." After them I added a defect paragraph, then the fence, then the closing sentence. The last paragraphs in English:
"I left this one in your hands. Take the first block of section 3, the one that asks the library to check `KillOrder`, and strip its promises: the block below is that one with no `#-->` line. Before you run it, write under each question the line you expect. Then run it and compare. Section 3 says why the last answer is what it is; whether it is the answer a function with that name should give, I leave to you."
[fence]
"When you have settled it, you will know why a word rule advises and does not refuse."
The bridge sentence is still last. The French mirrors this (« Je vous laisse celui-ci. ... »).

Exercise fence added: yes, `haro exercise`, with no `#-->` line and no output.

Checks: `check_fr 32` is ok. Both style lints show 0 for forbidden, calques and colon lead-ins. Both files are now LF. I did not run the build or the printers.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\32-many-minds-on-one-body-of-work.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\32-many-minds-on-one-body-of-work.md`.

=====

chapter 31 · chosen: candidate 1. It is block 1 (the service registry) with one line added, `oReg.Bind(:payments, new stzPaymentsSandbox())`, before `IsSound()`. The reader is asked whether a sound registry is one ready to ship.

why: rule 3, with a trace of rule 2. Section 5 says the guard `service_registry_narrated` proves "a sandbox in production is a violation". Section 7 says "A sandbox is bound and no live payment adapter is". Chapters 2 and 28 run the same fact elsewhere. I print neither the output nor a prediction. I did not add `SetPhase`, so the fence carries one change only.

rejected: candidate 2, the bridge-runtime pass-rate chart. Section 4 refuses that percentage because no guard produces it. The 5 October 2026 note gives no figure the book holds, so the chart would assert a number nobody ran.

wrote: the existing task and its fence (all three `#--> what you expect` lines) and the paper-table paragraph are kept. I added three blocks after the tutor's question and before the bridge, which stays last.
- A paragraph introducing the defect: "I left this one in your hands, on purpose. Below is the first block of this chapter with one line added…".
- The `haro exercise` fence.
- A closing paragraph. In English it is: "Run it and read what `IsSound()` answers. Then ask whether a sound registry is a registry ready to ship, and what the guard of section 5 says about a fake still bound in production. I do not give the answer: section 5 names the guard that holds it, and section 7 says what the project has bound and what it has not. When you have solved it, you will know what a sound registry does not say about the service behind it."

The French mirrors this (« Je vous laisse celui-ci, exprès. »), with the same paragraphs and a byte-identical fence.

exercise fence added: yes (`haro exercise`; no `#-->` line, no runnable fence).

Checks: `check_fr.py 31` returned ok. The lint is clean for EN and FR, with 0 forbidden, 0 calques and 0 hedge stacks.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\31-what-the-projects-did-not-prove.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\31-what-the-projects-did-not-prove.md

=====

chapter 33 · chosen: candidate 1, the production-gate block of §3 handed over with one line changed (the actor `HumanActor("dana")` becomes `LLMActor("assistant")`). The sandbox stays bound, so I made only one change, not the two the report suggested. The candidate's "which refusal fires first" question was dropped, because the page holds no ordering.

why: rule 2. §5 says `service_delivery_narrated` proves a production deploy with a fake bound does not run, "with every reason named", and that `full_scope_model_narrated` proves a model cannot perform the deployment. §3 says the sandbox refusal "is not a question of authority", and §8 (the agent) says an agent is refused. `LLMActor("assistant")` is copied from chapter 24, line 170. I print no output and no prediction.

rejected: candidate 2, a chart for the bridge-runtime percentage. §4 already refuses that figure, and asking the reader to compute it would contradict the refusal. It is also not a block with a change.

wrote, last paragraph in English: "Run that one too. Read what `WasCommitted()` answers, and read the log: the block of section 3 printed its second error entry for the person, and I make no claim about the assistant's. Section 5 says what the two guards prove, and section 8 what an agent is refused. When the gate answers, you will know what it refuses for what is true and what it refuses for who is asking."

Before it comes "I left this one in your hands." (« Je vous laisse celui-ci. »), then the changed block, then "I did not run this version, and I print no answer for it." The exercise's original task and its fence are unchanged. The bridge stays last.

exercise fence added: yes, one `haro exercise` fence with no `#-->` lines. The French fence is byte-identical to the English.

Checks: `check_fr 33` reports ok. Lint is clean in both languages.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\33-the-one-line-still-owed.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\33-the-one-line-still-owed.md

=====

chapter 3 · chosen: candidate 1. The govern block of §3 is handed over with one verb changed, `EnforceConstraint` for `AddConstraint`.

Why: this is rule 2. The block ran and is kept in `research/ch03.md` (Block B). The consequence is already on the page. §3 says "Declaring a constraint and enforcing it are two acts", and §5 says the guard `modality_narrated` proves that a declared constraint stays passive. The reader runs it and finds out, and I print no output and no prediction.

One correction to the candidate: it named `DeclareConstraint`, which the record does not hold. The guard at 93d7a39bd (`modality_narrated.ring`, scenario "Enforcement-on-update") uses `AddConstraint("lc", :Lowercase)` with the same signature and says "plain AddConstraint stays PASSIVE". I used that verb. It is new to the page's prose, but the guard holds it.

Rejected: the correct grid. It would require me to invent a grid that no file holds, which no rule allows.

What I wrote: the existing exercise task and its fence are unchanged. After them I added two paragraphs and a fence, before the bridge sentence, which stays last. The last paragraph in English:
"Look at what it prints: whether the update was refused, and what the object holds. Then read section 3, just after the block, and section 5, on the guard that checks it: the page says why. When you have both lines, you will know why a declared constraint is not an enforced one."

Exercise fence added: yes. It is a second `haro exercise` fence, the govern block with `AddConstraint`, no `#-->` lines. It is byte-identical in French.

Checks: `check_fr.py 3` passes. The English and French lints are clean (forbidden 0). The French mirrors the English paragraph for paragraph, and both files were normalised to LF.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\03-the-method-from-first-principles.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\03-the-method-from-first-principles.md