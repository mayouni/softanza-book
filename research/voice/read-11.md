# Voice read, chapter 11 (English), phase B stage 1

Lint now: 2,639 words, long 0.6 %, ! 0.8/k (2), ? 1.1/k, intensifiers 0, absolutes 5. By my count the prose holds two real questions (0.76/k); the lint's third `?` is inside a quoted library message (`did you mean 'boxify'?`), not a beat. The gate needs about 4 questions and 3 exclamations.

## The twelve points

1. **Shape.** Opening ("In this chapter I state the law of Part III and run it") is first person and says what the chapter does, but its second sentence is 40 words and ends by listing the whole chapter. Section closes: "## 5. The court" ends on a list of guards ("`constrained_decoding_narrated` the sampler that holds a model to it.") with no hand-over to section 6; "## 7. The limit" ends on "No native speaker has read them as far as the record shows." and section 8 starts cold. "## 1" ends on "prompting a model." Chapter close is a bridge plus principle ("Chapter 12 is *A language, declared*."): good.
2. **Run, then read.** The abstract stretch with no run in reach is "## What the AI age changes here", three paragraphs. Worst: "A language whose sentences may contain anything cannot refuse anything, and a court cannot judge a sentence it cannot read." Also the paragraphs of "## 4": "The meta-language that declares languages in the estate lives outside this library."
3. **The defect.** Real, and run: `upper('x')` runs inside brackets ("It ran anyway!"). The Hausa hook is told, not shown. The exercise is a defect (the third answer, false but accepted). No wrong-before-right except the misspelled verb. No taste rejection.
4. **Where it stops.** Stage words present in "## 7"; the loss sits beside the win (`semantic_resolver_narrated` "does not pass at this commit"). Reach beyond the page: "a person reading Arabic can check the machine's reading of their sentence without reading a line of code" (no Arabic reader read it); door "The programmer": "the court judges your sentence and an agent's by the same rules" (only the schema court is shown); door "The educator": "a learner reads the machine's reading of their own words" (no learner in the record); "The designer": "so it never needs a warning".
5. **Particulars.** August 2026 study, 2020 slide, July 2026 kit removed "the same day", 8 and 9 October 2026, 135 million parameters, Hadiza: all in `research/ch11.md` (Hadiza is the guard's own name). "Their letter-order cipher had been inverted by its own inventor, from memory" is the one sentence about a person's act. No `[AUTHOR` marker left. No invented memory.
6. **Metaphors.** Court (mapped under "What the AI age changes": "the part that accepts or refuses a sentence by its grammar"), world (glossed), forge (glossed in parentheses), gate ("A grammar is the gate, not the judge"), "an API wearing a language's costume" (the study's, decorative). Name drift: "door" means the natural layer's entry ("the naturalness stays at the door") and the foreign runtime ("a door brings a foreign runtime") and the section "Six doors" (readers).
7. **Address.** I about 24, you about 14 (lead-ins and exercise), we 0. Questions: both are beats answered by the next block. Exclamations: 2. The tool is never quoted as speaking except library messages in blocks; no "it says".
8. **Rhythm and noise.** Colon 18.6/k (the profile 15.2); no dash. Intensifiers: none; soft: "This matters more than it looks", "fairly". Absolutes 5: "never guessed" (twice), "it never declares", "never marks a reference that way", "everything off the list is grammatically impossible". No calques.
9. **Counted sets.** Five languages = English, Hausa, French, Arabic, Turkish: matches. "the six it accepts" = string, number, boolean, oneof, list, structure: matches. Seven guards listed in "## 5" match the front matter. "Six doors": six. "Five sides": chapters 12 to 16. Exact.
10. **The stake.** "humans and machines meet in declared languages, small, closed and judged" is the vision's line, ratified; "This is my view." marks the cost of careless generated language. Backed or marked: yes.
11. **Most him.** (1) "The misspelled verb is not guessed." (2) "A grammar kills malformed sentences, not false ones." (3) "I built the natural layer that way long before the vision named it". Least him: "The record says it in five words, structure kills malformedness, not falsehood, and so does this book: the truth of an answer is not for the grammar." (the record said / this book says, the author hiding behind both).
12. **The one change.** Turn the flat lead-ins into questions the blocks answer, and let the sentence after each block say what it printed.

## (a) Runs without a beat (line = lead-in, answer = the `#-->` line)

- "Begin with a sentence that runs. Not because a model guessed what it means" : box output `H E L L O   N I G E R`. A question like "What does a sentence look like when every word is in the dictionary?" fits; no verdict sentence follows the block.
- "Here is one instruction in English, in Hausa, in French and in Arabic": four lines `HELLO`. Question: can one meaning be said in four languages? No sentence after the block.
- "And a program says back what it understood, in its own language.": `أنشئ قائمة بـ [ 5, 3, 5 ] -> أزل التكرارات`.
- "An agent gets the strict mode, which refuses, and a world ... can limit its sentences": `Strict natural mode: not understood: 'Fooify'` and `Operation not permitted in this world: METHOD_REVERSE`.
- "when it answers no, it gives the reason": `no: 8 is not less than 4`.
- "Now the law at its sharpest: a model.": `stzOutputSchema: unknown field type 'colour'`.
- "and the schema emits its grammar, so that a model can be held to it": answers `1 0 0 1`, then the GBNF.
- "A sentence with an unfilled hole is refused before it runs:": `Unfilled template hole!`.
- "The shape of a list is declared, not written as a loop:": `1 0 1 0`; no sentence follows it (the roadmap paragraph starts at once).
- Already beats (keep): "What does it do with a verb it does not know?" (answered by `Unresolved()` and `0`); "Does a host function inside the brackets run?" (answered `[ "X", 1 ]`).

## (b) Paraphrased tool

- "The function `upper` is not a word of the natural dictionary. It ran anyway!" : retells `[ "X", 1 ]` without quoting it.
- "Hadiza is forty-one in the first answer and sixty-two in the fourth, and the court accepts both!" : the printed `1` and `1` are not quoted; the refusals (`mood: angry`, `age: 900000`, both `0`) are not mentioned.
- "The refusal names the unknown type, `'colour'`, and lists the six it accepts." : the printed `(use string|number|boolean|oneof|list|structure)` is not quoted.
- The Arabic reading under `o1.Understood()` is described, not quoted.
- "## 5": `semantic_resolver_narrated` "stops with an error raised from a string-splitting function": no printed line.

## (c) Cold exclamations

None. "the court accepts both!" follows a reveal (the fourth answer); "It ran anyway!" follows a run. Two exclamations is under the gate (0.8/k): the page can bear one to three more, after a refusal block (the strict mode, the `'colour'` schema, the template hole), at most five in all. None in "## 7" other than the existing one.

## (d) Missing verdicts (over 30 words, point buried)

- Opening: "I begin with a sentence that runs because every word of it is in a dictionary the library owns, in English, Hausa, French and Arabic, and I show what the library says about a word it does not know." (point: the library names the word it does not know).
- "The Hausa sentence is the narration's own, the French one comes from the library's guard with its data changed, and I composed the Arabic one from the library's vocabulary." (point: I composed the Arabic one).
- "The other direction of natural code in Softanza is the near-natural chain, where the person is the parser and the chain reads as a sentence; when it answers no, it gives the reason:".
- "The court judges any answer against it, whoever wrote the answer, and the schema emits its grammar, so that a model can be held to it while it writes:".
- "I built the natural layer that way long before the vision named it: only words defined in the dictionary are interpreted, and every other word is skipped and reported, or refused in strict mode, never guessed." (point: the rule, in a short sentence).
- "## 7": "The forge is built outside the library and designed for the library: a first sketch ... and the library cannot run it yet." (point: the library cannot run it yet).
- "## 7": "The pack stored it in a broken encoding, so, when I probed it on 8 October 2026 ..., a sentence written correctly failed without a word of complaint." (point: a correct sentence failed silently).
- The chapter 12 sentence in the roadmap paragraph (over 40 words, the lint's one long sentence).

## One-sentence paragraph candidates (hand-overs)

End of "## 5" into "## 6"; end of "## 7" into "## 8"; after the `Lx` block before "The chapters of this part prove the law from five sides."
