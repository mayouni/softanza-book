# Voice read, chapter 21, The court (English)

Lint: 3,248 words; questions 1.8 per 1,000 (6); exclamations 0.6 per 1,000 (2); long 0.0 %; intensifiers 0; dashes 0. Lines are those of `src/en/21-the-court.md`.

## The four phase B points

**(a) Runs without a beat.** Seven runs; four have a question lead-in (l.45, 66, 91, 137). Three have a flat statement:
- Ledger (l.118): "A wrong key and an edited line are two different accusations:". Question: if I edit one line, which entry does the chain name? Answer: `#--> the chain breaks at entry 2 -- that record (or one before it) was edited`.
- Stopwatch (l.166): "An instrument owes a number." Question: does a 200 ms pause count in the elapsed time? Answer: `? w.ElapsedMs() < 200` then `#--> 1`.
- Plan (l.194): "The same action is judged twice, and both judgments stay in the audit:". Question: what happens when a model asks to commit? Answer: `ExecuteOn(oFleet, LLMActor("advisor"))` then `#--> 0`, `CallCount` `#--> 0`.

**(b) Paraphrased tool.**
- l.225: "A model asking to commit is refused before any attempt, and the double counts zero calls!" The printed `0` lines are not quoted.
- Stopwatch block: the prose never reads its outputs (`1`, `0`, `2`); l.192 goes straight to "Careful with what this does not claim."
- l.192: "it gets the same trace and the same span identifier." The block prints only trace equality.
- l.85: "A short promise `6` once hid inside a later `[ 6, 28 ]`": the guard header retold.
- l.285 (promise-judge defect): the run is retold, no block, no printed state.

**(c) Cold exclamations.** None. Both follow a run: l.83 "though the language process ended with an error!" (on a clause, not on the exit code) and l.225 "the double counts zero calls!". At 0.6 per 1,000 the chapter is under the gate; reveals with no beat: the chain break, `Refused: actor 'planner'`, seven of eight unperceived.

**(d) Missing verdicts** (over 30 words, point buried):
- l.135: "An edit to the first entry is not caught, because the verifier checks each entry's text against the digest of the entry before it, and the first has none before it."
- l.160: "The meta-guard of the threat model checks that the document exists with its sections, and that every guarantee row contains a proof:" (~37).
- l.166: "The honest stopwatch gives a number from a clock that only moves forward, excludes a pause, and ships two spans..." (31).
- l.229: "The site's own record of 8 October 2026, run on another commit than this book's, says that of 135 articles 55 ran" (34).
- l.283: "The threat model's measure of responsiveness is a detection in a little over three hundred and fifty milliseconds" (31).
- l.19, the opening sentence (31).

## The twelve points

1. **Shape.** The opening is first person but a six-sentence list of contents; it names four refusals, section 4 holds seven. Section closes are dead ends: "The site's number is the site's to update." "It stays unperceived." The close is a bridge to chapter 22.
2. **Run, then read.** Mostly run first. Worst: "The ecosystem of integrations and auto-instrumentation for every framework is the field's." (section 6); also l.245, a paragraph of guard names with no run.
3. **Defect.** The exercise is a demonstration. The one real defect is l.285, reported, nothing built, no block. A wrong version before the right: the wrong key and the edited line. No taste rejection.
4. **Where it stops.** Stage words and section 7 are present; losses sit in section 6. Reach: "A claim is only as good as the court that can refuse it" (l.35); "What cannot lie are the executable guards" (l.229); "the evidence is sealed so that an edit is named" (l.297), without the first-entry limit of l.135.
5. **Particulars.** Dates: 26, 25, 30 Sep, 1, 5, 7, 8 Oct, 29 July 2026. Names: `HumanActor("mansour")`. No `[AUTHOR`. Memory in the author's mouth, not sourced on the page: "heard by me on 26 September 2026 ... my verdict was "far from being qualified"" (l.108); "That hid my first attempt" (l.135).
6. **Metaphors.** The court carries weight. "The door refuses", "a hand that may commit" are decorative. The four courts are announced in one sentence (l.41), not mapped; "the court of chapter 5" and the heading "The court" blur.
7. **Address.** "I" about 25, "you" a handful, "we" none. Six questions, all answered, but l.160 "What does the table of guarantees tie to a guard?" has no run. The tool speaks only with its printed text quoted.
8. **Rhythm.** Median 12; no dash; intensifiers 0. Absolutes 5: "is never accused" (l.45, 291), "None has a human name". Colon lead-ins that are flat statements: l.118, 166, 194.
9. **Counted sets.** Four courts, nine guards, five states, six doors, eight traditions match. Mismatches: four refusals listed in the opening against seven in section 4; "The performance plane has twelve guards" (l.247) with three named.
10. **Stake.** "Rightness is a person." and "Zero of ninety-five" are backed. "the doctrine that the library repeats in every plane" (l.37) is neither backed nor marked.
11. **Most him.** "Every rule of this judge was learned by watching the harness accuse the library falsely." (l.85). "Notice which entry I chose to edit: the second." (l.135). "Those are my words, and they are the one recorded perception that is a refusal." (l.108). **Least him:** "The ecosystem of integrations and auto-instrumentation for every framework is the field's." A noun stack with no run.
12. **The one change.** Turn the ledger, stopwatch and plan lead-ins into questions their last `#-->` answers, and give the stopwatch block the verdict it lacks.
