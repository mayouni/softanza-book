# Reading report, group F (Part VI: chapters 28 to 31)

Read 2026-10-14, as the decision-maker first, then as the author; each page twice. Nothing changed; `python tools/book_audit.py` run once (clean).

## src/en/28-a-restaurant-in-lyon.md

**What I remember.** Two years of specification produced nothing; a restaurateur reversed the order of work on 4 July 2026 and the project delivered a first iteration he tested himself on 15 August. The library carries four lessons as code (a cycle rule, a sandbox that declines, a gate that refuses a fake, a speed budget judged) and none of the interface rules. The restaurant runs on a Node server and single HTML files, not on Softanza; the record ends 25 August with no production order.

**Where I lost the thread.**
- §3, "Try payments": "a decline is an answer, an outage is not" is followed by "Three answers, and none of them is an empty string". The outage became one of the three answers two sentences after being denied the word.
- §8, the designer: "Fifteen interface rules from one directive, the three-second test". Neither "fifteen" nor "the three-second test" appears in §3, which says "experience in a few lines" and "eleven iterations". I did not know what the test was.
- §8, the decision-maker: "tightened the speed budget himself". §3 tells the five clauses and the criterion he added, but no tightening; first mention is in a door.
- §3, speed budget: `StzPerfMonitor("remote-control")`, a name never explained; every other name in the chapter is the restaurant's.

**Where I doubted.** §3, the production gate: `BindLiveQ(:payments, new stzHttpSandbox(), "payments_key")`, then `ServicesAreProductionReady()` prints `1`. The sentence before warns me ("an HTTP sandbox standing in for an adapter"), but as a buyer I read: the gate that says "a fake must never ship" opened for a class called Sandbox because the verb was `BindLiveQ`. The gate judges the binding's label, not the service. One sentence should say so, or the block proves less than the prose.

**Where it moved me.** §3: "The owner is entitled, and he is refused!" The right exclamation, after a run. And "He turned it around: customer first, restaurateur next, supplier last." Bored: §1, "The concept, as the field holds it", four practices with nothing at stake.

**The code.** Five blocks, each introduced by a question, each output matching the sentence after. The Lock block is declared "a construction, not the restaurant's code" before it runs. The SLA numbers are declared mine. Nothing to cut.

**Errors.** None of fact I am sure of. Form: the opening lists four refusals; §4 announces "Six refusals follow" and gives six.

**The door.** The decision-maker's, worth the walk: "a deployment that an entitled person may commit and that is still refused over a fake" is the sentence I would quote in a meeting, once the doubt above is answered.

**Verdict.** `ready after the items above`: the gate-opens-for-a-Sandbox sentence and the two facts first met in a door.

## src/en/29-a-bank-in-niamey.md

**What I remember.** An organisation chart written as text is judged by rule bases: the regional regulator's three rules, segregation of duties, and a rule of the bank's own written as data; the verdict names the rule and the position. Seven regimes share one mechanism, six carry only the four universal rules. The product installed at the bank is a Python application that calls none of this; the lesson is in the library, not the delivery.

**Where I lost the thread.**
- §3: the first block spoke of a code among three (`BCEAO-002`), the loop prints `BCEAO : 4`, and the reconciliation ("a validator of three rules, and a rule base of four universal ones") only comes in §4. I read the count twice.
- §3: "Its own code does not run at the pinned commit; the calls above do." I went back for what "its" was (the narration of a virtual bank).
- §7, third bullet: "It finds the board by the word "board" in a position title", next to the limit block that blanks the *chief executive's* department. The explanation is about the board, the block is about the CEO; I could not join them.

**Where I doubted.** §4: "Chapter 1 says the product is built with Softanza and keeps its wording". Chapter 1 today says "runs an assessment platform whose building shaped Softanza"; the page cites a sentence that has moved. And §3: "The library names seven regimes: the regional one, Basel III, SOX, PCI DSS, ISO 27001, GDPR and HIPAA", a sentence a buyer reads as coverage; the block two lines later undoes it honestly, but the first reading is the brochure's.

**Where it moved me.** §3: "The regulator's rule reads the chart and refuses it!" And §4: "A rule applied to a database row is a query; a rule applied to a text is something a person can read before it runs." That is the chapter. §6: "is all wins, undated, with cost figures that cite nothing, and I will not print it." Bored: §7's two bulleted lists; the limit block already said the sharpest of it.

**The code.** Six blocks. The seven-regime loop is the best proof in the group: a count printed instead of a sentence. The limit block (`substr(cChart, "department: executive", "department:")`) I understood only from the sentence after; the question before it does not say why a blank department would matter to the audit rule. One line of expectation would fix it.

**Errors.** §4's quotation of chapter 1 (above). The doors are one line each; the brief's "two lines" is kept loosely across the whole group.

**The door.** The decision-maker's: "Ask which of the regulations the library holds, and ask for the count." Worth the walk; it is the only door in the group that tells me what question to put to a vendor.

**Verdict.** `ready after the items above`: the chapter 1 quotation, and one sentence of expectation before the limit block.

## src/en/30-an-organisation-in-the-field.md

**What I remember.** A design study, not a delivery: the hub is not built and version 1.2 awaits validation. The library carries a rule whose number changes the verdict and its scope, a governor that names a rule governing nothing, a refusal kept as a checkpoint, authority judged against risk, and a decision's lineage. Offline, the organisation's default, is a permission and nothing more.

**Where I lost the thread.**
- §3, second block: "A change of the rule is a change of its values" is contradicted by the paragraph after: "The "change" is a rule rebuilt in code with another number." Promise, then retraction. Say the second first.
- §3, authority: the verdict "SHOULD does not cover it". "SHOULD" is a word from chapter 20's vocabulary; here it arrives inside a quoted string with no gloss. A decision-maker reading this chapter alone will not know what SHOULD is.
- §5: "rests on scenes 4 and 5 of `rulz_roundtrip_narrated`", for the refusal of an unknown rule type, a missing file and a duplicate name. No block of the chapter shows any of the three; §7 then counts them among "the pieces". Proof cited for something the page did not show.

**Where I doubted.** §4: "The rule governor exists because the silent rule already happened in the library." A claimed incident with no date or file on the page. §4: "A sister package of the estate, a browser-side one, holds a durable outbox ... I did not run it." Good; then chapter 31's table says "the study's word that the browser-side outbox is already in service". Two pages, two stages for the same outbox.

**Where it moved me.** §3: "The court has to tell "nothing was wrong" from "nothing was looked at"." The best sentence in the group. §9: "The difference between those two answers is the chapter." Bored: §1's three practices, and "I say "design study" and not "delivery" every time", said twice in the same words within forty lines.

**The code.** Seven blocks, all understood from the sentence before, outputs as promised. The governor block is the one I would keep if I could keep one. The offline block is read "as a limit and not as a win", twice, which is right. Nothing to cut.

**Errors.** Form: the one chapter of the four with no bridge sentence before §5 and §8 ("Six doors follow" is in 28 and 29, not here). Front matter says "a local developer", §7 "a local programmer".

**The door.** The decision-maker's: "Authority is not permission: ask which level covers which risk, and read the lineage of a decision." Worth the walk; the lineage block is the proof.

**Verdict.** `ready after the items above`: SHOULD glossed, the "change of values" sentence reordered, the three refusals either shown or not counted.

## src/en/31-what-the-projects-show.md

**What I remember.** A stage report: per project, a table of claim, proof and next step, with cells left empty on purpose; five blocks where the library refuses rather than passes. The sum: no customer platform runs on the engine yet, the declarations are not files, and the next milestone is a dated sentence from a named user.

**Where I lost the thread.**
- Restaurant table, last row: "The comparative study of the record (its section 12.29) conflates two facts." Earlier chapters call it "the study of the record" and only chapter 25 explains it is an outside reader's study with numbered sections. Here it is "the comparative study", with a section number I cannot open, in a table cell; §4 repeats "the study of 12.29". A reader has no 12.29.
- §3, "### What the study of the record marks for measurement": a subsection on what a document I cannot read leaves unmeasured, ending "The study applies its own perception law to itself, which is why I trust the paragraph." I did not know whose paragraph.
- §3, the formant voice block: a chapter on three customers asks "What does the formant voice answer when it is asked to sing". The sentence after ties it to chapter 33's line, but by then I had stopped reading the chapter as being about the projects. The seventy-word error string with its measurements in cents does not belong here; the `UNPERCEIVED` / `SINGING` / date / said lines carry the point.
- §4: "I replaced two wordings of my own with the record's. In chapters 1, 2 and 33 I wrote". A changelog of other pages, on this page; chapter 29 §4 does the same. The reader does not need the history of the edit.

**Where I doubted.** §6: "faster on every row, by a factor between one and two", the one sentence in Part VI a buyer will underline, and it is a number, two paragraphs after "I refused to print a percentage" (§4). Either a guard the page names produces it, or it joins the percentage in the refusal. Across-the-three table: "though not every program agrees on every stable line"; I could not say what that means for a buyer.

**Where it moved me.** §8, the agent: "You may not turn an absent cell into a present one." §3: "Two services declared, none bound, and the registry says so itself". §8, the decision-maker: ""Built" is a statement about a guard. "Runs at a customer" is a statement about a document." Bored: the across-the-three table's last five rows (hardware, speed, pictures) belong to chapters 27 or 33, not to the three projects; and §7 restates the three §7s of 28 to 30 for the third time.

**The code.** Five blocks plus two exercise blocks. The registry, kiosk and pre-flight blocks are understood from the sentence before and print what it promised. The voice block: move, or cut to its last five lines. The first exercise, with `#--> what you expect` three times, is the only one in the group that asks for a prediction before the run; keep it.

**Errors.** `14_bceao_governance` is "two of the three rules" in chapter 29 §5 and "one assertion ... a chart with no board and no risk function" here; compatible, but a checking reader will ask which. Bank table: "The product is "built with Softanza"" quoted with no source (chapter 1 no longer says it). No French in the English; no broken table.

**The door.** The decision-maker's, the best door in the book for me: "Read the stage word before the testimonial ... You can ask for it in writing, with a name beside it."

**Verdict.** `not ready`: the study-of-the-record passages written for the record's keeper rather than the reader, the voice block's detour and error string, and the one-to-two factor against the refused percentage. The tables themselves are ready.

## The group

**The thread.** The bridges land: 28 closes on "the chart says what is, the rule says what must be" and 29 opens with it; 29 closes on "the AI agent proposes, and a person decides" and 30 takes it as its principle; 30 closes on 31's measure word for word. The part feels like a part through chapter 30: three projects, each a story, each with the library's piece and its absence, in the same nine sections. Chapter 31 thins it: a stage report that restates §7 of each chapter as a table, restates the tables as its own §7, then wanders to a singing voice, a board on order and a gallery of pictures. The three projects are judged three times; once, in the tables, was enough.

**The author at his best.**
1. Chapter 30 §3: "The court has to tell "nothing was wrong" from "nothing was looked at"."
2. Chapter 29 §4: "A rule applied to a database row is a query; a rule applied to a text is something a person can read before it runs."
3. Chapter 31 §8: ""Built" is a statement about a guard. "Runs at a customer" is a statement about a document."

**Least like him.** Chapter 31 §3, "### What the study of the record marks for measurement", through "which is why I trust the paragraph": a report to the keeper of a document the reader cannot open, in the voice of a session memo; no run, no reveal, no "you".

**What a reader who stops here takes away.** That the author tells the truth about three customers to the point of telling it three times: a restaurant that tested a first iteration on the owner's own phone and then goes silent on 25 August; a bank with a Python product beside a library that judges charts the bank has never given it; an organisation with a study and no hub. That the library carries one sharp idea per project (a fake never ships; a chart is data a court reads; authority is not permission), each proved in a block that runs. And, from chapter 31, that nothing runs on the engine yet. As the decision-maker I close Part VI trusting the man and able to repeat the three ideas; I also close it having read "absent" more often than "built", with the factor of one to two as the only number I remember. The standing rule says never undersell: the three project chapters do not; the fourth does, by repetition rather than by any one sentence.
