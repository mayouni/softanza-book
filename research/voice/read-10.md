# Voice read, chapter 10 (Programming becomes refinement), English

Lint, before: 2,010 prose words; questions 1.5/k (3); exclamations 0.5/k (1); long sentences 0.9 %; colon lead-ins 0; intensifiers 0. The gate asks 1.5/k or more questions (about 4 for this length is safe), 1 to 2.5/k exclamations (2 to 5), none cold.

## 1. Shape (C9)
Opening is in the first person and does the job, but its first sentence repeats, nearly word for word, the definition that section 3 gives again: "a change to code declared to be changeable, proposed in a typed form, judged by a gate, recorded as a step, and reversible". Section closes: sections 1, 2, 4, 5, 6 end flat. Section 3 closes on the five-checks reveal, good, but section 5 ends on a list of what the guards prove, with no hand-over to section 6. Chapter close: a bridge to chapter 11 ("Here the thing judged was a change; there it is whoever speaks"). No release for the exercise beyond "you have found a place where your own gate disagrees".

## 2. Run, then read (C1)
Worst: before the governance block, "A delegated actor cannot turn a knob of the third tier. Escalated, it can, and the decision is recorded" states the result, then the block shows it. Same for reversal: "so a person can step back one, rewind to a named checkpoint, rewind to zero, and go forward again", then the run. Section 6 ("The field leads in infrastructure ... breadth ... trust") is three paragraphs of abstract nouns with no run near. Section 8 "Six doors" is abstract by design.

## 3. The defect (C2)
The chapter has a real defect: the header says four stages, the code runs five ("4b"). A wrong version (four) is shown before the right, in prose only. Exercise is a demonstration with a prediction step, acceptable. No correct code rejected for taste.

## 4. Where it stops (C3)
Limit section is present, with built / designed / absent and four bullets. Losses beside wins: the file does not keep history; unknown posture ranks trusted. Reach: "reversibility is part of the data model" (section 3), "so a person can correct the proposal without reading a diff", "A learner can try without fear" (section 8; a claim about learners, not shown).

## 5. Particulars (C4)
"16 July 2026" and "1 October 2026" (charter) are sourced as facts of the record. "The practice has changed names in my life. I used to say I programmed. I now say that, more and more, I refine" is a personal history not on the page or the record; it reads composed. "the sentence I wrote on the back cover of my first book" appears twice (opening and section 2) and is the author's own. No `[AUTHOR` markers. Six "(General knowledge ...)" tags.

## 6. Metaphors (C5)
"a named knob" (carries weight, mapped by the tag); "blast radius" (a library term, carries); "the court" (section 5 heading, unmapped on this page); "doors" (section 8, decorative); "floor of trust" (library term). "the intelligence of the next generation will not hold still" is decorative.

## 7. Address (C6)
I: opening, 2, 3, 4 (heavy: "I refused" x4, "I printed"), 7. You: "Run it", exercise, doors. Questions: 3, all answered by the next block, but the lead-ins of blocks 2 and 3 pair two questions in one ("and what does a proposal ... change, and what does the gate say?"). "Now the question of this age: who proposed it?" is answered, but "of this age" is a flourish. Exclamations: one, "Three refusals, and the timeline did not grow by a step!", earned (after a run). Tool quoted as speaking: no.

## 8. Rhythm and noise (C7)
Median 18; long sentences rare. Colon is used. Intensifiers 0, dashes 0. Absolutes: "never ends changed" (qualified in the limit section). "Much of the field's" x3, hedged by tag. Calques: none heard.

## 9. Counted sets (C8)
"five checks" matches the list in order (structure, constraints, governance, trust, derivation); "4b" explained. "Three refusals" matches three. "three kinds of point" matches parameter, algorithm, library. "Six doors": six present. "two cascades" matches.

## 10. The stake (C10)
"stop trying to govern the intelligence, and govern the change", marked as the author's view ("this is my view"). Backed by the gate runs; fine.

## 11. Passages
Most him: "I printed the gate as it is. I wrote the design with four stages, and the code has five checks." / "I report what runs: five checks." / "I refused the diff as the unit. A diff is a text change."
Least him: "Now the question of this age: who proposed it?", a rhetorical flourish.

## Phase B points

**(a) Runs without a beat** (lead-in flat; the answering line):
1. "It begins by declaring where the code may change." -> `#--> [ [ "vat", "param", "0.20" ], [ "sort", "algo", "quick" ] ]`
2. "A change is then a proposal. It names a point and a value; if it clears the gate it takes effect and is recorded as one step:" -> `#--> 1` (NumberOfSteps) and `#--> 0.22`
3. "For a point, it is the line it sits on and the other points on that same line:" -> `#--> [ "margin" ]`, `#--> 0` for floor
4. "For a class, the cascade is a property of the structure of the code:" -> `#--> [ "Invoice", "Quote", "Receipt" ]`, `#--> 3`
5. "Inside the gate, a change reaches its dependents by a rule that spans several points ... the value is put back:" -> `#--> derivation: rule 'vat-above-floor' violated -- vat must not drop below floor`
6. "And who may turn which knob is declared, too:" -> `#--> governance: refused: 'release-bot' holds 'delegated' authority (level 2) ...`
7. "Last, reversibility is part of the data model." -> `#--> 0.20` after `RevertTo(0)`, then `#--> 0.21` after `Redo()`
Already with a beat: the refusal block and the trust block.

**(b) Paraphrased tool:** "Each refusal names its stage first, `constraint` twice and `structural` once" retells the three printed refusals (`#--> structural: no refinement point 'ghost'`). "two of them inherit the method and the third redefines it" retells `#--> [ "Invoice", "Receipt" ]`. "A delegated actor cannot turn a knob of the third tier" retells the governance line. The trust block, `#--> trust: posture :llm below the required floor for 'vat'`, has no sentence after it at all; neither do the derivation and governance blocks.

**(c) Cold exclamations:** none. The one `!` is earned. Room for 1 to 4 more after real reveals: the trust block (value stays `0.30`), the governance block (refused at level 2, admitted once escalated), the reversal block (`#--> 0` for CanRevert, then `0.21`).

**(d) Missing verdicts:** (1) "Change the rate of the tariff and three classes are in the blast radius; but two of them inherit the method and the third redefines it, so it owns the method and does not merely inherit it." (about 38 words): the point (ImpactOf separates inheriting from owning) is buried. (2) Opening sentence of the chapter (about 35 words), repeats section 3. (3) "The code numbers its checks 1, 2, 3, 4 and 4b, because ..." (31 words), and "Five checks, in the order the code runs them: ..." (about 40 words as a list). (4) Section 4, "I made the library carry the verb ..." (about 32 words after the heading).

Other: "just"/"simply" none; "only" x3 benign; "(General knowledge ...)" tag x6 is heavy; "Doors" section 8 has no run.

## The one change
Give every block after the first a question it answers and a short verdict sentence after it (governance, trust, derivation, reversal have none now), so the chapter reads run, then verdict, not run, then silence.
