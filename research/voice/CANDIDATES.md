# Phase C candidates (defects to leave in the reader's hands), proposed by the chapter agents, 2026-10-11 — the author chooses one per chapter, or none

- Give the reader the derivation block (§3, `d.DeclareDerivation`, line 128 onward) with the rule reversed (`<=` instead of `>=`): `d.Refine("vat").To("0.30")` is then refused and `To("0.05")` admitted, and the reader must read `derivation: rule 'vat-above-floor' violated` against the rule's own text to see which is wrong.
- A listing the decision section already rejects: a correct `stzRefinableCode` whose proposals are applied as plain text replacements (a diff) and then reviewed by eye; §4 "I refused the diff as the unit" says why, and §7's unknown-posture limit gives a second one: ask `Refine("vat").As(:martian)` and the gate admits it; the record cannot say whether that is a defect or a design, and the chapter could refuse to answer.

---

- Give the reader the hacked-condition block (§3, `o1.FindW('{ @item > 5 and print("hacked") }')`, `#--> [ ]`) as a bug to explain: the empty list is not "no match" but "a call the language does not know", and §6/§8 already name this as the quiet cost.
- A correct `FindWF( func x { … } )` listing solving exercise sentence Four, rejected because §4 refused arbitrary code from text and the exercise demands the string form; the reason is already on the page (WF "is not safe with input you do not trust").

---

- Block `o2.RemoveManyCS([ "o", "f", "n" ], FALSE)` (§3, first block, line 5 of the fence): hand the reader the article's promise `SOFTANZA` and let them find which flag gives it; the page already shows the wrong expectation beside the run.
- `DoubleEachConcurrently` (§4): a correct-looking listing the decision section rejects, because a method per operation smears the frame across many verbs and puts it back outside the verb.
- A question the record cannot answer: whether the library corrects any typo at all (§3, "I did not trace every file that mentions correction"), or who wrote the scope design document v1.2 (§7).

---

- Give the reader the rule 8 block with `o1.FindNthNext(2, "♥")` and no `:StartingAt`, the two-argument call of the library's own narration, which the page says raises; the fix is the named start.
- The Flexibility block's second call, `ReplaceNextNthOccurrence(2, :With = "##", :StartingAt = 12, :Of = "@@")`, runs and is correct, and §3 says the Haro grammar leaves free-order parameters out: a correct listing to reject with its reason.

---

- Graph-rule block (§3, the organisation), line `g.SetNodeProperty("writer", "capabilities", [ "inference", "effectful" ])`: hand it over with `"effectful"` removed; `RulesAreSound()` answers 1 and the reader must say why the rule stayed silent.
- A correct listing of `stzList`'s methods under the programmer's door, rejected because §4 refuses to present the library by its anatomy.

---

- The Basket block (§3, line `def AddQ(x)` / `return 42`): give the reader the class with `AddQ` returning `This` and `Add` returning nothing, so `StzCodeIsClean` says `TRUE`; then ask which of the fourteen rules a court of style would still want and does not have.
- A correct listing §4 already rejects: the exercise solved as one chain on a single line with positional arguments (`o1.ReplaceEmptyStrings("~")`) prints the right answer and breaks the style the decision refuses to let go; the reader rejects it and says why.

---

- Break the second `rxu()` block (line 59 area, `Trigger(:Number = "\d+")`) by writing the triggers in the other order, `:Big` before `:Number`, and ask the reader whether the order changes `Results()`; the record shows each trigger matched once against the original text, so the answer is no, and the reader learns the second rung by failing to make it the third.
- A chart the chapter refuses: the star-rating comparison in `softanza-reactive-objects-narration.md` (§6). Hand the reader the four overflow strategies and ask them to draw the "kept / dropped" table from `OverflowStats()` instead, which the record can answer and the article's stars cannot.

---

- The govern block (§3, line 69 `bRefused = FALSE` … `oName.UpdateWith("HELLO")`): give the reader the version with `DeclareConstraint` instead of `EnforceConstraint`, so `bRefused` prints `FALSE` and `Content()` prints `HELLO`; the guard's own clause ("a declared one stays passive") is the lesson, and the reader must find which verb to change.
- A correct grid: hand the reader a feature grid in which Softanza's column wins every row (§4 "I refused the grid alone" already rejects it) and refuse to print it without the measured loss of 13 September 2026 beside it.

---

- The layers block (§3, lines 58–65) constructs `stkList` and `stzList` in one program, so both layer files are loaded at once, the state §4 "I refused a flag to choose a layer" calls the failure of all three. A correct listing the decision already rejects; the chapter could say so and ask the reader to split it.
- The constellation block with line `oCon.GovGrant("resto", "order-produce")` removed: the bond exists, the crossing is still refused; the reader writes the `Why()` line before running it (the record must be run to confirm the text).

---

- Give the reader the §7 grammar block (`TheWordQ("haro").IsAQ(:Word).WhichQ().ALengthQ().Of(4)`, second line) as the "correct" one and ask what the court should have said: it prints `TRUE`, and nothing judges "which a length of 4".
- The §3 literal block, third line (`Replace sep with '_'` → `a-_-b`): a listing that runs and that §4 "I refused silent tolerance" arguably rejects, since an unknown verb-position word is refused but an unknown value-position word is silently a literal.

---

- §3, the list block (line ~68): give the reader `Lx("[@N1-3, @S]").Match([1, 2, 3, 4, "end"])` as the first call on a reused object after `[1, 2, 3, "end"]`; §7 says the cache key ignores order and content beyond length and character sum, so the reader must explain a 1 the fresh object would not give.
- §7, the table language: a correct listing `Tbx("{cols(2) & unique(id)}")` for the exercise is one the decision section already rejects as a headline, because it accepts `t3` (the empty email), and the chapter's "unknown word is not refused" means `{cols(2) & nonempty(email)}` would also answer 1 for every table if `nonempty` is not a word: the reader cannot tell a refused clause from an accepted one.

---

- Break on purpose: the grammar-vs-court block (`cBand`, lines 72–83 EN): hand the reader `#--> ?` on `StzGrammarAccepts(cG, cBand)` and `oO.Accepts(cBand)`; most will predict the grammar refuses 40, and the run says `1`.
- Correct listing the decision section rejects: `o.FindWF( func x { return sin(x) < 2 } )` (line 165) runs and answers everything, and §4 "I refused one text for declaring and for computing" refuses it as a word of the closed language: it is the door, not the declaration.

---

- Break the first Python block (§3, line `res = { 'numbers': ...`) by renaming `res` to `result`: no result file is written, and the chapter says failure is detected only by that absence; the reader must explain an empty `Result()` and an exit code of 0.
- A question the record cannot answer: "which seven?" (§3). The record counts four ways; the reader could be asked to pick one count and defend it, and the page already refuses to choose.

---

- Break block 4 on purpose (`oG.Proposes("writer", "send")`, EN line 101): insert a gate between writer and send and ask the reader to predict `IsSound()` and `len(Violations())` before running; §5 says `agentgraph_narrated` proves the governed shape is sound, so the record can judge the answer.
- A correct listing §4 already rejects: a `stzLLMAgent` wired as the first faculty, returning the restaurant answer fluently before `StzDlmQ` is consulted. It runs and is right, and "I refused the model as the mind" rejects it: the model must come after the programmatic path, under the court and a budget.

---

- Give the reader the fifth-register block (§3, line `aV = oKX.ReplyIn("fmt", [ [ "+216-21-298-374", "valid" ], ... ])`) with the two pairs joined as one string `"+216-21-298-374, valid"`: it splits, admits two literal values and reads `fulfilled`; the page says so in prose and never shows it.
- A question the record cannot answer: run `ReplyIn("setup", "tomato sauce")` and ask the reader to predict the verdict; §7 says it raised with an uninitialised variable on 8 October 2026, and no block records it.

---

- §7, the malformed-lines block (`cBad`, line "    g likes h"): hand the reader the file with `merged` and `refused` already printed, and ask which of the four lines reached the graph. The record answers `1` and `[ ]`; the reader must discover that three lines vanished, against the design's "validated on load".
- §4 "I refused to resolve a contradiction in silence" against the clinic block: a correct listing that calls `AddFact("fatou", "treated-by", "dr-sani")` on a non-strict graph would be admitted and overwrite the first fact, with no contradiction recorded; the decision section rejects it because without strict mode the rumour wins in silence.

---

- Block 3 (the grammar), line 75: hand the reader the loop without `aFact[2] != "is-a"`, so `dish` and `wine` enter the object choices and "subject: tiramisu / relation: contains / object: wine" passes `Accepts`; the fix teaches why types must not leak into objects.
- A question the record cannot answer: propose "margherita pairs-with tomato-sauce" (right shape, no `:Unique` law on `pairs-with`). The grammar accepts it, `Admit` admits it, and only "a person" (§4) can refuse it; the exercise's last question has no machine answer there.

---

- The sealed-ledger block (§3, security, `oLed.SealTo` block): give the reader the `StzReplace` line pointed at the **first** entry's text (`"wrong credentials"`) instead of the second; the verifier answers `chain intact` and the reader must explain why the first entry is never caught, which the page already states.
- The exercise file: the possible defect of §7 (a lie as first promise, a promised raise as last) is a question the record cannot answer; the reader could be asked to build that file, predict `diverged`, and read `unreached`, with the open question handed to the Testoor plane.

---

- Break block 4 on purpose: give `oScope3.AllowUnder(cFx)` the path of `oScope` ("/somewhere/else") at line ~148; the reader must predict `StzFileExists($cPrices)` → `0` and an empty audit trail.
- A correct listing §4 already rejects: a plan with `SetExecutor(PIActor(...))` and no `SetScope` commits every path untouched by any check (§7 gap 1). Give it, let it succeed, and ask why "only a governed actor commits" still holds.

---

- Break the gates block on purpose: delete line `oCon.GovSetAuthority("resto", :Delegated)` and leave the recorded `#--> 1`; the reader must read `holds '' authority (level 0)` and name the third gate.
- A correct listing §4 already rejects: a world that holds the envelope, `oResto.AddCapabilityQ(:camera)` on `stzApp` ("I refused to give the world the envelope"). Or: a question the record cannot answer, "what does `Hosts(:VisitApp)` do", since the design's idiom is not in the class.

---

- Break on purpose the "Code first, subscribe later" block at line `oReg.BindLive(:payments, new LiveGateway, "stripe-key")` by naming a key the store does not hold (`"stripe-live"`): `IsSoundVia` then answers `0` with `live-without-secret`, the reader must read the report to see why.
- A correct listing the decision section already rejects: a `MayGoLive` that asks about soundness in the current phase (§4, "I refused to ask a question in the wrong frame"); it would answer `1` in development with a sandbox bound, and the chapter says why that is wrong.

---

- Block 6 (`src/en/29-a-bank-in-niamey.md` ~line 154, `oOrg2.ImportStzOrg( substr(cChart, "department: executive", "department:") )` … `#--> 1`): hand the reader only the first half, a chart that passes BCEAO with audit under the chief executive, and ask why; the `:Banking` line (`#--> pass`, a validator that passes every time) is a second trap in the same block.
- A correct listing §4 already rejects: load the test-data rule file (`when`/`then` text, two rules, §7 bullet 2) and print its rule count; it runs and is true, and the decision "I refused to claim more than the library holds" rejects it as proof that a rule file judges, because the loader reads no `when`/`then` line.

---

- The `ParentOf` block (§3, line 62 onward): hand the reader `ParentOf("stzString")` with the expected line written as `#--> stkstring`, the contract's answer; the run prints `stzobject`, and the reader must say why the court is right and the contract wrong.
- The prefix-count block (§3, `left(aClass[1], 3)`): a correct listing that the agent door already rejects, "do not tell the reader which layer a class lives in by its prefix": max's forty classes carry `stz`, so the count `[10, 693, 0]` is right and says nothing about layers. The exercise could ask for the parent-chain version instead.

---

- Block 2 (§3, the loop `oKB.ReplyIn("c", ReadReply(cIn))`): hand it over without `ReadReply`, so "7" and "2" arrive as strings; the reader predicts `GoalState()` and the `Query` before running. Block 3 holds the answer's key.
- The question the record cannot answer: the exercise's fourth prediction, "yes please". `ReplyIn("c", "grand couscous")` raised in the research run and no block records it (§7, bold item); the chapter could name it as its left defect instead of only its lesson. Also refusable: the recogniser's confidence chart (§3, "I do not print the recogniser's confidence").

---

- The emulator block (§7, line `? StzContains(cH, "Ready to ship.")`): give the reader a plan with a backend only and ask them to predict the four `#-->` lines; the page says "parts healthy" and "Ready to ship." there too, and the chapter already says it was read, not run.
- The `transfer_funds` listing (§3, second block): correct, clean, and the decision section refuses it in substance ("the library does not own the verbs, the constitution does"); the reader could be asked to say which of library, book or nobody refuses it, and why `IsClean()` cannot.

---

- Break block 3 on purpose: give the reader `oWatch.AddRule(oTypo)` without `oWatch.AddCase("advances", oG)` (line 94). The governor then has no case to measure scope against, and the reader must say what `CheckRules()` can report with no picture at all, the chapter's own "nothing was looked at".
- A correct listing §4 already rejects: a rule written as `oRule.WhenQ("amount", "greaterthan", 500)` with no `SetMessageQ` runs and judges correctly, and "I refused a silent rule" says "A rule with no message is reported too". Hand that listing over and ask why the governor flags it although the model's verdict is right.

---

- Block 1 (`oReg.DeclareMany([ :mail, :payments ])`), line `? oReg.IsSound()`: give the reader the block with `oReg.Bind(:payments, new stzPaymentsSandbox())` added before it, so `IsSound()` prints `1` while `payments` is still a sandbox, and ask what the delivery gate would say in production (§5 names the guard: a sandbox in production is a violation).
- The percentage §4 refuses to print ("I refused to print a percentage"): a chart of the bridge runtime's pass rate, correctly computable from the 5 October 2026 session note, that the chapter refuses because no guard produces the figure.

---

- The Lock block (§3, "The Lock"), line 66 `g.SetNodeProperty("loyalty-club", "admitted-by", ...)`: hand it to the reader without that line, so the court's `UNSOUND` report is theirs to resolve by changing the declaration, not the court.
- A speed-budget listing with `ExpectP50` standing in for the owner's seventy-fifth percentile: it runs and is MET, and §6 says the owner's protocol cannot be declared in the library's terms. The chapter could refuse to give that chart.

---

- Block 1 (`StzCheckCode` on `KillOrder`), `src/en/32…md` lines 71–72: hand the reader the block with the last promise blank and ask "clean or not?" before the run; the recorded `1` is the surprise the chapter already builds on.
- A chart the chapter could refuse to draw: composed stamps per desk (34 of 151, 13 of 17 desks) beside the central desk's 5 of 25, refused because §6 says they are "on a different surface" and one axis would make them comparable.

---

- Block 3 (`oDel.Deploy(:Production)`, line with `SetActor(HumanActor("dana"))`): give it to the reader with `BindSandbox` replaced by a live binding and the actor a model, and ask which refusal fires first; the page's own §5 says a model cannot perform the deployment.
- A chart the chapter could refuse: the bridge runtime's percentage. §4 "I refused my own figure" already rejects it; the defect is to leave the reader the measured rows (3,461 of 5,112) and no chart, and say why.

# Places that need the author (phases A and F), as the agents found them

- §3 The Softanza form: whether the second exclamation he is allowed goes on the blast-radius reveal (I added none there).
- §7 The limit: whether the unknown-posture rank (top rank for an unknown origin) is a bug to be filed as a library request or a stance to own.

---

- §4 "I let the edge rule be a design principle": the record does not date it as a ruling; only he can own it as his design or leave it the library's.
- §6 "A table with no loss on it is the shape of a brochure": a stake stated as taste; his to own or soften.

---

- §3 The Softanza form: finish or own the trace of the correction files ("Did you mean").
- §5 The court / §7 The limit: the probe run with the timing failure that `data/` does not record; a recorded run or the stake of printing it from memory.
- §4 The decision: only "I refused to ship the whole engine to the edge" is the author's; the other refusals are the design document's. Say which are his.

---

- §2 The first principle: the goal-oriented-architecture claim is his point only as the study reports it; a sentence of his own would make it his stake.
- §3 The goals (Flexibility): whether the library keeps free-order parameters past the Haro grammar is "a decision the record does not hold".
- §4 first refusal: the disappointment at the AI-era style is reported through the study; his own words are owed.

---

- §2 The first principle: ownership or skill; the record does not settle it (a stake to own).
- §3 A bank in Niamey: who at the bank declared.
- §4 I refused "maker": what the cover image carries.
- §6 "Coding agents lead in hands": an unmapped image, keep or cut.

---

- §4 "What had happened is measurable": the study's recommendation on the one test form has "no ruling of mine"; a ruling to own.
- §4 "three old features were refused as grammar": the refusal is printed as the design's; whether it is his.
- §3 history block: the lost fluent link (`CharsQRT`) and the request to restore it: a stake to own or drop.

---

- §3 The Softanza form: "the Regexuter, a reflex arc" and "a cursor with the intelligence of a place" are the author's images; I kept both, and he should say whether either is one he wants to live with.
- §2 The first principle: the colon-introduced definition is still 46 words in French; only he can shorten his own sentence.

---

- §4 "I refused to add a feature without a need": the quoted article "carries no date"; only he can date or source it.
- §4 "I refused the grid alone": "an internal memo" of September 2026, unnamed; a title or path.
- §6 "Where I think Softanza stands apart": the one stake of the chapter, unmarked as belief or backed.

---

- §3 The engine: the one exclamation is mine; his call.
- §3 The crafters: "three unrelated places" is a particular he could name.
- §6: "A map that prints its weak areas is the only kind worth reading" is a stake to own or mark as his view.

---

- §4 "I built it without a model": five items listed (zero NLP, zero ML, native speed, full determinism, programmer in control), then "a fourth promise"; the count does not match.
- §4 "I refused the markup language": "Two seeds were kept as thin doors" is a sixth sense of *door* (METAPHORS.md flag 3); the author's name for it.
- §7 "What is absent": the private memo of 30 August 2026, whether anything of it may be said.

---

- §2 The first principle: whether "for the first time in computer science history" is his sentence or only the study's attribution.
- §7 The limit: "a finding of the court, and not as a debt of mine" is a stake to own.
- §9 Exercise: the two closing questions are left unanswered on purpose ("I do not answer first"); his call whether that stands under the beats rule.

---

- §3 The factory: "the true sentence has two sides" is followed by three clauses; the count is his.
- §3/§4: one name for factory/forge (METAPHORS flag 1); the French says « usine ».
- §4 last decision: "how many faces before the announcement is mine, and unanswered": a stake to own.
- §1: whether "costume" (the study's words) also drops "wear".

---

- §3 "Which seven?": only the author can rule which count the title means.
- §6: the chapter has no owned stake sentence (C10); "The door is how a Softanza solution takes them without leaving" is the nearest place.

---

- §4 "I refused anything paid or remote": the record supports both readings of "last" and the chapter does not choose; a ruling is his.
- §7 The limit: the rephrased question answered instead of refused is a request to the library; whether it is also the chapter's chosen defect is his call.
- §1: "some of it is very good" (an intensifier the lint tolerates) is an opinion to keep or cut.
- The English file is CRLF (as is ch11's); the French is LF. I preserved each as found, against the brief's "files use LF".

---

Mapping: METAPHORS.md names no ruling metaphor first appearing in chapter 18 (register is mapped in ch1 and restated in §3); nothing inserted. Decorative metaphor deleted: §4 "All five registers land in one funnel" → "go through one door" (the chapter's own image); French « entonnoir » likewise.

Noise: 1 intensifier ("really there") removed; 1 colon lead-in (exercise) made a full sentence; long sentences 2.9% → 0.5% (EN), 5.3% → 0.5% (FR; the one left is the numbered list). French: « réellement » and « simplement » removed; « validation » for the git commit → « commit » (FRENCH.md); no « plan » for plane in this chapter, no « développeur ».

**2. Two candidate defects for phase C**
- Give the reader the fifth-register block (§3, line `aV = oKX.ReplyIn("fmt", [ [ "+216-21-298-374", "valid" ], ... ])`) with the two pairs joined as one string `"+216-21-298-374, valid"`: it splits, admits two literal values and reads `fulfilled`; the page says so in prose and never shows it.
- A question the record cannot answer: run `ReplyIn("setup", "tomato sauce")` and ask the reader to predict the verdict; §7 says it raised with an uninitialised variable on 8 October 2026, and no block records it.

**3. Places that need the author**
- §2 The first principle: why five registers and not four or six, and when wise coding was set against vibe coding (the record holds no sentence of his).
- §6 The field: the dates of slot filling, vibe coding and programming by example are "to be checked before print".

---

- §3 "A law that fires when a fact is added": `EnableAutoDerive` "I did not run it", a stake the author may want to own or run.
- §7 "The 2022 founding dialog": the run that stopped on `@isfruit` was not kept as a block; only the author can decide whether the dialog is shown at all.
- §8 "The designer": "The record is silent … I do not invent one", a door only he can fill.

---

- §4 The decision: "free to the users of its domain" with no licence text; the stake of "free" is his to own.
- §4: "one of the estate's products", "the earlier product": unnamed particulars only he can name.
- §6 The field: "that is what a bank, a ministry or a school can sign": the chapter's lift, unmarked as belief or backed.

---

- §3 The court of perception: whether the verdict "far from being qualified" should be quoted in his own words (the one perception he gave).
- §7 The limit, "A possible defect in the promise judge": whether to file it as a request or own it as a stake.

---

- §3 ledger paragraph: Appendix D now defines *ledger* as the security plane's record only; the paragraph names three ledgers. Reconcile, and say whether the roster's journal is the "ledger of rulings" of ch32.
- §4 "I refused safe agents": the stake (people, craft) is still the doctrine's, not owned in the first person.

---

- §3 "The architect, and the three scopes": whether the architect is told as "what one holds in a scope" is his own application (the page says so) and a stake to own.
- §6 "The field, and where it leads": no lift of the stakes in the chapter; only he can add one.

---

- §4 (closing paragraph): whether the service plan's "user's question" of 23 July 2026 was his.
- §7 "What is designed": a stake to own on the engine-in-a-browser claim (wired, checked by a guard he did not run, seen by no one named).

---

- §3 The Softanza form: the licence, the installation guide and "under licence" are his particulars; whether a single word of the bank's people may be given.
- §4 The decision: chapter 1's "built with Softanza" against the record's Python application; only he reconciles his wording.
- §6 The field: "Where I think this stands apart" is the chapter's one lift of the stakes and is thin; the conviction is his to own or mark as belief.
- §7 The limit: a delivery date, if he has one.

---

- §3 "One engine": the site's 752 cannot be reproduced; only the author can say which count the site should print.
- §6 "The headline": whether the runtime repository's notes are his to correct, or a request to file.
- §7 "Haro": the stage word for the runtime beneath is "mine"; the charter's section 15 is still unread by him.

---

- §3 "The restaurant's medium": the chapter 1 sentence about a messaging-app demonstration, flagged to him; he owns the wording.
- §2 The first principle: whether the constitution's sentence is his wording ("The record is silent").
- §4 "No inferred meaning": "a constitutional amendment wearing a library's clothes" is the record's clothing image (Table 2 row 3's family); keep or cut.
- §4 "Commands, not transcription": « barrière » for "gate" (a threshold here); confirm or prefer « seuil ».

---

- §6 "The field, and where it leads": "That is a bet" — the stake is stated and not owned (no "my view").
- §3 "A status bar that tells the truth": whether `ShellStatus` should gain the specification's *unchecked* state is his design call.

---

- §3 The Softanza form: who in the organisation chose the retained offer and what was weighed against low-code ("the record holds the outcome and the gains, and not the deliberation").
- §3 / §7: whether the study's version 1.2 was validated by the executive director (the record does not say).
- §4 "I refused to call offline a lesson": the sister browser-side package with the outbox was not run; a stake on whether it will be brought into the library is the author's.

---

- §3 "A feature that waits for a named person": the record carries the person's name beside the verdict; whether to print it is his call.
- §4 "I refused two wordings of my own": chapter 1 keeps "runs" / "built with"; only he can change chapter 1.
- §9 Exercise: the tutor's closing question ("which cell did you fill from memory?") is left to the reader by design; whether that is the chapter's chosen defect is his call.

---

- §3 "The Lock" / §7: the production gate is "the last door" in §3 and "the delivery gate" in §7 (METAPHORS flag 5); one name is his call.
- §7 The limit: what happened after 25 August 2026, whether a real order was taken.
- §8 The designer: who held the phone in the eleven iterations.
- §3: "a novel of narrations", if it is not the project's own phrase.

---

- §3 "The code is clean!": the one exclamation is his to keep or cut.
- §7 The limit: the study's "the author should watch the ratio" is a stake only he can own or reject in his words.
- §8 The educator: "at two in the morning" reads as his particular; I could not trace it to the record.
- Housekeeping: `src/en/32` is CRLF (with ten other English pages) against the brief's "files use LF"; I preserved each file's convention rather than convert.

---

- §3 "The record already holds the form of the line": the Principal is unnamed; only the author can say who perceived the drum.
- §7 The limit: "no project that moves to the engine first, and no person who will perceive it" is a stake only he can own.
- Flag 5 of METAPHORS.md: "the last door" (§3, §7) is one of four names for the production gate.