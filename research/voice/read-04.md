# Voice read, chapter 4, The platform in one picture (src/en/04-the-platform-in-one-picture.md)

Baseline (prose only, fences out): 2,290 words, ? 4 (1.7/k), ! 1 (0.4/k), long sentences 0.0 % by the lint, colons 21/k. Gate needs ! 1 to 2.5/k: the chapter is below it. Questions already pass 1.5/k, but the fixer's target is about 2/k (5 questions).

**1. Shape (C9).** Opening is first person and says what the chapter does and what it refuses: "In this chapter I draw the whole platform in one picture". Good hand-over: "Let me walk it, floor by floor" (3). Section closes: 1 ends on a dead end (no bridge to 2); 2 is one sentence; 4 ends on "worlds, not mini-apps" with no bridge to 5; 5 ends on the list of guards; 6 ends on "the only kind worth reading", then 7 starts cold ("What is built:"). 7 to 8 has no bridge. Chapter close is a bridge: "The next chapter leaves the picture for the code written inside it".

**2. Run, then read (C1).** Run precedes reading in 3 (questions at three blocks). Worst abstract run: 5, "`06_stzsuperapp_narrated` proves the constellation: worlds joining, the commons as world zero, crossings gated by norms..." and "The court" in 3, a paragraph of abstract nouns ("The engine has its tests and the contracts between the floors. The layers have the narrated guards.") with no run within reach.

**3. The defect (C2).** Only the exercise (9) leaves a task, "write the line you expect when you ask it to deploy before you build it": a real prediction, not a defect. The max layer failing (7) is a real defect, shown. No wrong-then-right version, no correct code rejected for taste.

**4. Where it stops (C3).** Stage words are present in 7 ("What is built / designed / absent"). Losses beside wins: yes (stxstring, core broken, "implement those domains twice"). Reach: "Every other crossing is refused with its reason" (only one refusal shown); "no other role crosses every band of the Atlas"; "beside every floor stands its judge" (7 says the layer court is only specified); "a map that prints its weak areas is the only kind worth reading" (marked "I hold this as a view").

**5. Particulars (C4).** Names: FieldVisits, resto, supplier, acme-group, my-shop (code, fine); Zig, C interface, Rust's three crates (field facts); the Arabic word for peace (in the block). Composed or unsourced: "the night this page is made" (poetic, the build has a clock; not a night); "in the vision I ratified" (an act of the author's, only rulings in front matter back it); "the cleanest version I know" (a claim of his knowledge); "The record names that person in three unrelated places" (a count, not checkable here). No `[AUTHOR` marker. No memory or feeling put in his mouth.

**6. Metaphors (C5).** Carry weight: floors and court (the whole structure); "world / constellation / commons as world zero" (no code explains it otherwise). Decorative: "the night this page is made"; "where the next reader would stand" (4); "envelope" (3). The court is never mapped term by term where it first appears (the intro says "beside every floor its court" before any definition). Names drift: floor / layer / altitude / band; "faces" ("computation in the faces", intro and 4) is never explained.

**7. Address (C6).** I: intro, "Let me walk it", six "I refused / I removed / I chose / I let" openers in 4, "I hold this as a view", "so I will not either". You: every run lead-in. We: none. Questions: four, all beats answered by the block ("What does each one count?", "What becomes of a crossing that no bond declares?", "How many engine groups does it ship?", "What does the runtime answer when you ask for one?"). Exclamation: one, "Four letters, not eight!", after a run, not cold. The tool is quoted as speaking: "The runtime answers:" and "the constellation gives its reason", both fine.

**8. Rhythm and noise (C7).** Colon 21/k (profile 15.2): the heavy ones are prose colons, "The numbers in it are not typed by me: the build reads them", "Rust's ... cleanest version I know: three depths", "The core layer itself is broken against the engine today: its string...". No dash, no intensifier, no ellipsis, no superlative. Absolutes: 2 per the lint ("Every other crossing", "no other role").

**9. Counted sets (C8).** Layers: three, names exact (core stk, base stz, max stx). Doors: six, six headings in 8, matches chapter 2's list. Guards: five in front matter, five in section 5. Unfinished domains: six named ("number, list, object, graph, stats and natural"), six. Phone: four capabilities, four in the list, two shipped, matches the printed pair.

**10. The stake (C10).** Rises in the first principle, "nothing is believed, everything is judged", and in "a map that prints its weak areas". The first is stated as an idea, unbacked until the court sections; the second is marked as a view. Neither is a new stake.

**11. Most him.** "Four letters, not eight!" / "The flag was removed rather than kept as a switch that silently does nothing". / "The Atlas itself prints where Softanza is weak". Least him: "Parts II to IV of this book are rethinks, and each of them is a box of this picture. Part V assembles the picture in use." (a table-of-contents sentence at the end of the biggest section, no run or reason).

**12. The one change.** Turn the three flat block lead-ins (layers, areas, worlds) into questions their `#-->` lines answer, and add one verdict sentence after each.

---

## Phase B points

**(a) Runs without a beat** (lead-in flat; the answering line):
1. 3 BigInt, "Numbers too large for the machine's arithmetic are added exactly, by the engine itself:" answered by `#--> 100000000000000000000000000000000`.
2. 3 layers, "A layer is chosen by the file a program loads, and the same verb means the same act at core and base:" answered by `#--> 1` after both `stkList` and `stzList`.
3. 3 areas, "Here it holds for one pair, a string and a list:" answered by `#--> [ 1, 10 ]` and `#--> [ 1, 3 ]`.
4. 3 worlds, "A world is declared, and it can explain itself:" answered by `#--> WORLD FieldVisits   lives in: memory (not persisted)`.
The four existing question beats (engine, constellation, delivery, max layer) are already beats.

**(b) Paraphrased tool.** 3 worlds: nothing follows the Explain block; its `#--> [FieldVisits] is live -- 2 thing(s), 0 flow(s), 0 reaction(s), 0 goal(s); 0 proposal(s)` is never quoted. 3 layers and areas: no sentence retells or quotes the output at all (`1`, `[ 1, 10 ]`; the prose says only "on a string it answers character positions"). The BigInt result is never named. The remaining blocks quote their printed line in backticks.

**(c) Cold exclamations.** None. The single `!` ("Four letters, not eight!", 3, engine) follows the run. Room for more, each after a reveal: the refused crossing (`#--> 0`, 3 constellation: "The other answers `0`"), the count ("Two: `aggregation` and `solver`"), the refusal in 7 ("Error in class name, class not found: stxstring"). 8 and 9 are abstract: none there.

**(d) Missing verdicts** (over 30 words, point buried):
- 4: "The rule is that every feature is implemented once, in the engine; the migration is not finished, and the layer contract lists number, list, object, graph, stats and natural as still in Ring." (33; verdict: the migration is not finished.)
- 4: "The flag was removed rather than kept as a switch that silently does nothing, and the reason was written where the next reader would stand: a layer is chosen by the file you load." (34; verdict: a layer is chosen by the file you load.)
- 4: "Under the pressure of time, the domains landed in base while the engine, the planes such as security and performance, and the customers moved forward." (about 25; verdict: everything went into base.)
- 6: "And the Atlas itself prints where Softanza is weak: the binary area is a plan with no shipped code, the plugin, foreign-function and embed plane ... " (37; verdict: the Atlas prints its weak areas.)
- 7: "The core layer itself is broken against the engine today: its string and character classes call engine names that no engine file registers, as the site study ... reports." (32; verdict: core is broken today.)
- 1: "Rust's three standard crates, one for bare metal, one for memory, one for a full operating system, are the cleanest version I know: three depths of the same language, chosen by what the target offers." (35)
- 3 hand-overs with no bridge: before "Parts II to IV" (end of 3), start of 7 ("What is built:"), start of 8.
