# Reading report, group B: Part II, chapters 5 to 10

Read as the programmer, each page twice. Nothing edited; `python tools/book_audit.py` run once (clean).

## 05-law-the-code-adheres-to-the-way-a-person-thinks.md

**What I remember.** A line of code should follow the order in which I reasoned, and a machine should judge that whoever wrote the line. The proof: the four steps (contain, count, find, act) on a list, three forms of one verb, a scene, a chain with history, and a court that refuses a class whose `AddQ` returns `42`. The limit: that court judges only the library's own classes; nothing judges the style of my program today.

**Where I lost the thread.** Under "3. The Softanza form": "Five of the fourteen run over the graph of the code." I had not been told what the fourteen were, nor that the court has a graph; the sentence assumes section 5 and chapter 7. Same section: "Chapter 9 tells… deep operations." Chapter 9 runs no deep block (chapter 8 does).

**Where I doubted.** "most code, here as everywhere, is written by AI models" (section "What the AI age changes here"): a figure the page does not show.

**Where it moved me.** "`Removed` printed `RING`, and the object still read `RIxxNxG`!": the verb's form shown, not told. "a law chapter that hides its own founding example would not deserve your trust." Bored: "4. The decision, and what I refused", fifth paragraph: three decisions under one bold lead.

**The code.** Every block was understood from the sentence before it and printed what it promised; the history chain (`[ 12500, 13000, 11500, 23, 46 ]`) I checked by hand. One block I would reconsider: the `RIxxNxG` string spells the former host language's name three times (`RING`, `R I N G`) on a page that never names it; the audit lets it through, but the author's rule is Ring only in Appendix H.

**Errors.** "not the fourteen house rules of the court below": "below" means section 5, but the reader has just seen a court block above.

**The door.** The programmer. "a court reads it whether you wrote it or an AI agent did." Worth the walk; the law in one line.

**Verdict.** `ready after the items above`: the three `RING` strings need the author's ruling, the rest is small.

## 06-the-mental-model-and-the-metaphors.md

**What I remember.** The same three questions on a string as on a list, then four named moves instead of a loop: walk, check, yield, perform. The proof: a walker that knows its route before it moves, a yield that leaves the list alone, a perform that changes it, and a W condition that cannot run code (`print("hacked")` printed nothing). The limit: the walker is not lazy, an unknown call in W gives `[ ]` and no error, three list verbs still call `eval`.

**Where I lost the thread.** Under "3. The Softanza form", first walker block: `Walk()` prints `[ 1, 3 ]` and the next block's `Walk()` prints `[ 10 ]`. Nothing says what one `Walk()` returns (the step as from-and-to?), so the two outputs do not sit together. Same section: "Now the thing that all four share, which is the last piece of the title": the title is "The mental model, and the metaphors"; there is no third piece. Opening: "the seven steps of the mental model, which chapter 5 ran on a list": chapter 5 ran four and never said seven; the list here reads as eight ("celebrate, and repeat").

**Where I doubted.** "in the words of a session of 2 October 2026, as the page reads on 9 October 2026" (section 2): two dates to quote a sentence the chapter then disowns ("That sentence is the site's, not mine"). Section 6: "This is my view, held on this table" repeats the sentence before it.

**Where it moved me.** "Nothing was printed! The positions came back empty, `[ ]`": the refusal shown. "Ask it to walk backward from the start and it refuses!" Bored: "7. The limit", the six-item list, which reads as a changelog.

**The code.** Checker, yielder and condition blocks were clear from the sentence before and printed as promised. The `Wk` walker's `Walk()` is the one output I could not predict.

**Errors.** Section 5 names `597_walker_basics` and `495_walking_until_and_until_before` twice; one sentence would do. "W for where" arrives after the block that uses W.

**The door.** The programmer: "when you reach for a loop, name the move: walk, check, yield or perform." Worth it.

**Verdict.** `ready after the items above`: explain `Walk()` once and fix "the last piece of the title".

## 07-the-writing-style-and-the-seven-goals.md

**What I remember.** The style is fourteen rules read from the code; most run here or in chapter 5, two do not. Under them, seven goals from the 2022 deck, three shown in blocks. The house court is fourteen other rules over the library's own code, run live. I remember the table and `writes_a_mutable_constant`; I could not restate the seven goals without looking.

**Where I lost the thread.** Under "3. The Softanza form", rule 9 block: `ContainsBoth` and `ContainsAll` sit in a block introduced by "Do the two answers differ on an Arabic word?" and no sentence says why. Rule 8: "with the side spelled four ways", then a block that shows two. "The goals": "a matrix of thirty-three features" is never shown, and section 4 counts it in a paragraph I read twice ("twenty-four built, four transformed… one a name only").

**Where I doubted.** "the only way one architect masters a project of this size" (section 2), hedged, then as fact in section 6: "a skeleton for one architect over about three hundred thousand hand-written lines." The number is not on the page. Flexibility block: both orders run; chapter 8 section 7 says "Free order works for the first order only: in my probe of 8 October, the swapped call ended the program". The two pages disagree in front of the reader, and neither names the other.

**Where it moved me.** "The word has four letters!" after `Size()` printed 8. "The court refused the write to a constant!" Bored: "4. The decision", the tags paragraph (6,090 / 6,126 / 89 / 1,360 / 4,766).

**The code.** The viz block (rule 7) is the same block, character for character, as chapter 8's "The prefix viz"; cut one. The `L` range blocks and the court block were the clearest on the page.

**Errors.** Section 7: "the features that run (`CS`, `XT`, `ZZ`, `viz`…)": `ZZ` is chapter 8's. Section 4, first bold: "The study reports the author's disappointment": "the author" in a first-person book. Exercise 5: `L("day8 : day11")` raises "Using uninitialized variable: day8" although `day8` is inside a string; say in one clause that `L` evaluates its text, or the surprise reads as a bug.

**The door.** The programmer: "Fourteen rules you can hold your own line against." Worth it; it is a checklist.

**Verdict.** `ready after the items above`: the free-order contradiction with chapter 8 needs the author; the duplicate viz block and the stray `ContainsBoth` lines are his to cut.

## 08-functions-as-linguistic-expressions-and-scope.md

**What I remember.** A method's name is parsed as a sentence (`_StzParseName` prints `[ "find next", [ "case-sensitive", "from-position", "active" ] ]`); fourteen of twenty-two forms run, five do not. Scope: the frame is in the verb, not in a flag; `Match`, `MatchFirst`, `MatchLine` give three verdicts on one pattern; `Spawn` is `native` on a server and forbidden on a board. The limit: concurrency as a scope has no code.

**Where I lost the thread.** Under "3. The Softanza form": "The answer, in four moves, is the paradigm…", then after the system block: "This is the fifth move: when a scope's capabilities differ from the host's, the library bridges". Four announced, a fifth appears uncounted. Same section: "`_StzParseName`, is an internal helper that no guard covers. The public way in is `ExplainMethod`", and the block then calls the internal helper first.

**Where I doubted.** The exercise asks whether `TRUE` can "keep the article's promise" of `SOFTANZA`; it cannot (the capitals `OO`, `FF`, `NN` stay). Section 7, free order: see chapter 7.

**Where it moved me.** "The chain printed `H A R O`, and the original still holds `haxxrxo`!" "The same verb, `Spawn`, has two verdicts!" The `Forbids`/`Requires` block is the group's clearest proof of "the library can reason with it". Bored: "7. The limit", the "On the scope side" paragraph, which says the 61-of-62 probe twice (section 5 said it already).

**The code.** All blocks understood and printed as promised. The viz block duplicates chapter 7's. `o3 = new stzList([ "R", "I", "N", "G" ])` spells the former host language's name.

**Errors.** Section 3, deep form: `DeepReplace("you", :By = "♥")` where chapters 5 and 7 say `:With`; if both exist, rule 8 of chapter 7 should own it. "`MatchOneSegment`, which the table offers for the lazy case": "the table" was never shown.

**The door.** The programmer: "Read a name as a sentence: its suffixes are its parameters, in order." Worth it.

**Verdict.** `ready after the items above`: the fifth move, the duplicate probe sentence, the `RING` list.

## 09-patterns-of-thought.md

**What I remember.** A Regexuter binds a pattern to code, fires and keeps why; the cascade of triggers is not built, and a block proves it (`BIG` is nowhere). The cascade exists one rung up, in the agent (`Pursue()` printed `2`, then `0`). Reaxis is reactive programming renamed; overflow now counts what it drops. Timeline and grid run. The limit: the dependency chain overflows the stack; the Listexuter fails five of seven classic tests.

**Where I lost the thread.** Under "3. The Softanza form": "So the word has three meanings in the record": the rung, the engine module, the universal engine, but the paragraph also names the macroplan and `stzPIAgent`, and I read it twice. "**Reaxis** is the other half of the chapter's title": the title has three subjects, as the opening says. "In chapter 17 you will see this same agent refused at a gate": chapter 17's agent is `rogue-bot`, not the cook; same class, not the same agent.

**Where I doubted.** "a function in waiting, which is not a callback" is asserted; the block then registers three callbacks. Section 5: the Regexuter's court is a log line, `PASS 8 ERR 0`, and "Nothing there checks what they print".

**Where it moved me.** "I would rather show you the block that fails to cascade than a block that does." "The counter that read zero now counts!" Bored: "7. The limit", eight bullets, the last one three sentences on three things.

**The code.** Every block understood from the sentence before; `REDACTED-16` and positions `19`, `36` hold by hand. The timeline block is long; I would cut the `PHASE2B` lines.

**Errors.** Section 6: "the two media that have an Uter built": "Uter" is not a word the book has defined.

**The door.** The programmer: "Bind a pattern to code, and process". Worth it.

**Verdict.** `ready after the items above`: "other half", "Uter", "this same agent".

## 10-programming-becomes-refinement.md

**What I remember.** A refinement is a typed proposal to a declared point, judged by a five-check gate, recorded as a step, reversible. The proof: one object taken through bounds, options, an unknown point, a derivation across points, a trust floor that refuses `:llm`, a governance tier that refuses a delegated bot, and a rewind to zero. The limit: an unknown trust posture ranks as trusted; the file saves source and no history.

**Where I lost the thread.** Under "2. The first principle": "the back cover of my first book": section 3 says "the first book of this imprint", which is exact; the author has an earlier book (Appendix H), so "my first book" is not. Section 3, the gate paragraph: the five checks are listed in one order (structure, constraints, governance, trust, derivation) and were run in another; say so in half a sentence.

**Where I doubted.** `? r[:admitted]` prints `1` and `0` where every other page of the group prints `TRUE` and `FALSE`; chapter 5 told me that "0 or 1… does not tell a block that failed from a block that never ran." "(General knowledge, not a study of the record.)" and its short form six times on one page: the hedge becomes a tic.

**Where it moved me.** "Three refusals, and the timeline did not grow by a step!" "A page that quotes my design and not my code would be wrong, and it is the code that runs." Bored: "6. The field, and where it leads", three paragraphs each ending in the same parenthesis.

**The code.** Every block followed from its sentence. `stzRingCodeGraph`, `"world.ring"` and `ring_number` name the former host language three times; the audit passes identifiers, but the author's rule should say whether they count. The exercise block depends on `d` from section 3; say so.

**Errors.** Section 7: "`.zrfn`… `.rfn`": a reader of this chapter has met neither suffix.

**The door.** The decision-maker, for this page: "the decision is recorded with its authority at the time." Worth it; it is what the governance block printed.

**Verdict.** `ready after the items above`: "my first book", the `1`/`0`, the six parentheses.

## The group

**The thread.** Every bridge lands: 5 ends on "walk, check, yield or perform" and 6 opens on them; 6 ends on 7's motto; 7 hands over "a function's name is a sentence"; 8 names the Softanzuter; 9 ends on "govern the change"; 10 ends on chapter 11's law in its own words. Part II feels like a part because chapter 5 announces the five chapters and each begins by naming what chapter 5 showed. Two seams: 7 and 8 share a block and disagree on free order; 5 promises deep operations from 9 and 8 delivers them.

**The author at his best.**
1. "I would rather show you the block that fails to cascade than a block that does." (ch. 9, section 4)
2. "I tell you this first because a law chapter that hides its own founding example would not deserve your trust." (ch. 5, section 3)
3. "A page that quotes my design and not my code would be wrong, and it is the code that runs." (ch. 10, section 4)

**Least like him.** Chapter 7, section 4: "The study reports the author's disappointment in these terms, and chapter 5 tells it." The man who wrote "the hand was mine" in chapter 5 is here "the author", reported by "the study".

**What a reader who stops here takes away.** That Softanza's code is meant to read as the steps of a thought, that a machine already judges the library's own classes and the promise under a line, and that the house refuses to claim what it has not run: a cascade, a court over my code. The reader also leaves counting: 14 rules, 14 house rules, 7 goals, 33 features, 22 forms, 4 metaphors, 7 steps, 5 checks. The numbers are honest; there are too many per page to hold.
