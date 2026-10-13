# Voice read: chapter 15, Pattern languages

Lint: 2,836 words, ? 2.5/k (6 real questions), ! 1.1/k (it counts `@!`; one real exclamation), 17 sentences over 30 words.

## The twelve points

1. **Shape.** Opening is a first-person roadmap, sound. Sections 1, 2, 5, 6 end on a fact, no hand-over: 5 ends "filed this on 1 October 2026 as still open."; 6 ends "it is also a likely reason time fails." Close bridges to chapter 16.
2. **Run, then read.** Sections 1 and 2 have no run. Worst: section 5, "proves the anchors and the search, the classes, the exact quantifiers, the groups" (a catalogue of nouns).
3. **Defect.** Exercise is real ("If a promise breaks, do not change it"). Section 7 shows the wrong behaviour (Banana matches). No taste rejection.
4. **Stops.** Stage words and losses present ("The loss is that it runs only on `stzTable`."). Reach: "across seven kinds of data" (section 2) against six media in the opening; "no class takes a pattern" (section 7); "none of the six media can yet refuse" (section 8).
5. **Particulars.** All dates and tools sourced on the page (14 June 2026, 28 September 2026, PCRE2, Python 3.10); Niamey, Dakar, Ali, Sara are example data. "English, French, Arabic and Hausa" (section 8) is unsourced on the page. No `[AUTHOR` left. No invented memory.
6. **Metaphors.** Court and doors carry weight, mapped elsewhere. "The family" (about 8 times) and "siblings" are unmapped here; mildly decorative.
7. **Address.** I about 25, you about 8, we none. Questions are beats answered on the page; the two in section 9 are left to the reader on purpose. One exclamation, "matches every number!", after a run. The tool is quoted once, correctly.
8. **Rhythm.** Colons 20.1/k (profile 15.2); dashes, intensifiers, calques 0; superlative 1 ("the first honest correction"). Paragraphs mostly end on a fact, rarely a short verdict.
9. **Counted sets.** Six doors: six, matches. Counts in play: "seven kinds of data" (section 2), six pattern classes (section 7), "seven languages" (next chapter line), six small functions.
10. **Stake.** Faint: "A closed language that cannot refuse is not yet the law of chapter 11", backed by the run and marked as view.
11. **Most him.** "It refuses, and says why: `The pattern name you provided does not exist in stzRegexData file.`"; "The tokens are `[ ]`, and nothing is raised."; "I do not answer first." **Least him:** section 5 catalogue above (report voice).
12. **One change.** Turn the lead-ins of the section 3 blocks into questions their `#-->` lines answer.

## Phase B points

**(a) Runs without a beat** (lead-in; answering line):
- "Take a list. Its pattern is written in square brackets..." : `[@N1-3, @S]` on `[1, 2, 3, 4, "end"]` gives `#--> 0`.
- "The numbers have properties, and a property is meaning, not procedure." : `#--> [ 6, 28, 496 ]`.
- "Tables: a data-quality rule is a sentence of the language." : `{cols(4) & unique(city)}` gives `#--> 0`.
- "A pattern is data, so patterns compose" : `#--> {cols(4) & rows(4)}`.
- "A matrix: a concept, square and symmetric, is one line." : second matrix `#--> 0`.
- "Time, in the part of it that runs." : 90 minutes `#--> 1`, 80 minutes `#--> 0`.
- "A graph: a pattern reads like the path it looks for." : `{@Node(served) -> @Node(placed)}` gives `#--> 0`.
- "Last, the habit." : `len(...Tokens())` gives `#--> 2`.
- "A pattern can also answer the half-written value" : `"abc"` gives `#--> 0`.
Already beats: isoDate refusal, timeline, graph quantifier, Banana, exercise.

**(b) Paraphrased tool.** The graph sentence "no `Tokens`, no `Pattern` and no working `Explain`" has no printed line; "a range without a step raised" (time) has no error text; "`rx("[a-z]+").Explain()` raises" has no message. Both are from research notes, not blocks, so nothing recorded to quote. The refusal after the isoDate block is quoted verbatim, fine.

**(c) Cold exclamations.** None. The one prose `!` (section 7, "matches every number!") follows a run.

**(d) Missing verdicts** (over 30 words):
- Section 2: "I found it in no text of the library, and the study does not let the site claim it; I keep the phrase here as what I said..." Point: the phrase is mine, not the library's.
- Section 5: "I ran a copy with the function moved to the end... sixty checks ran, and two of them disagree" Point: two of sixty disagree.
- Section 7: "The cache of this class is keyed by the node and edge counts and the node ids, so a second graph..." Point: a stale answer.
- Section 7: "The chapter prints it as a finding of the court, and not as a debt of mine; I hold that as my view..." Point: the run stands behind it.
- Section 5: the `00_numbrex_narrated` and `tablex_narrated` sentences (36, 34 words): the regression each killed.
- Section 4: "The older work on naming is kept as history... which I hold, as a view and not a result..."

**One-sentence-paragraph spots:** the ends of sections 1, 5, 6.
