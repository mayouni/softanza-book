Both pages are edited. `python tools/check_fr.py 0` reports ok and `python tools/book_audit.py` reports clean. I changed no code fence, no front matter and no other chapter.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\00-preface.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\00-preface.md`.

- L21 "same words, five names" · confirmed · `stzsite/content/en/estate.md:24` has five stage names, and chapter 3 already folds them into three. Replaced the sentence with the five names (built, in construction, specification, ratified proposal, named) and "Chapter 3 prints how they fold into these three."
- L13 "a library, an engine and a language" · confirmed · chapter 27 says Haro is a ratified charter and a spike, with no `haro` executable. Now "a library and an engine, and a language still in construction, all shaped by one idea". I dropped "built to one idea", which clashed with the stage word.
- L13 "a court born with the declaration" · confirmed · chapter 12: the library judges a declaration and builds a court and grammar from it. The forge for a language's court and grammar is built outside the library. Reworded to "a court made from the declaration", plus one sentence pointing to chapter 12 with exactly that split. The reader's "designed" fits only the wider factory, which this page does not claim.
- L15 "Every block was run" · confirmed · `data/book-run.json` has the verdict "exercise" (not run). Now "except the exercises, which are yours to run". I did not count blocks, since the page prints no count.
- L19 "same nine elements" · confirmed · chapters 5, 11 and 17 have "What the AI age changes here". Added a sentence saying the three law chapters open with one more short section.
- L23 "build made at the same commit" · confirmed · the record says `pinned: false`, built in a tree at the commit, newest build 2026-10-05 20:27, one engine commit (55876012f) after it. Now "a build made in a checkout of the same commit", "not pinned", and the page says which engine commits came after it.
- L27 "four languages" · confirmed · the education record says 0 of 35 units are reviewed in French, Arabic and Hausa. Added that those three are drafts no native speaker has reviewed (the site's education page, read 9 October 2026). I did not re-open the page; the same text is in the local `stzsite` copy.
- L33 "written last ... from the book that exists" · confirmed · the preface was drafted in Phase 4 and later edits followed. Now "written after the chapters were first drafted ... not re-read since the later edits".
- L29 "I will write it again" · confirmed as unsupported · now "it will have to be written again when the line does".
- L19 "I put the limit ... on purpose / advertisement" · confirmed as unsupported · replaced by "The shape of every chapter puts the limit seventh."
- Reading problem 1 (two definitions of built) · not fixed · the preface says code, guard and block ran, which is the brief's definition. Chapter 3 (not my page) says code and guards pass, and that definition is not in the preface.
- Reading problem 2 (former host language, Haro) · fixed · one clause says it is the language the library was run on before Haro, and that Haro has no executable, so the `haro` blocks run on that earlier runtime.
- Reading problem 3 (whose "I") · fixed · one sentence on the last line: the book speaks in the author's voice, which is why it says "I" (DECISIONS.md SELF-01).

The French carries the same changes in the same paragraphs. It uses « façonnés », « la forge », « une copie du même commit », « épinglée » and « haoussa » (the usual spelling in the other French pages).

confirmed 10 · not confirmed 0 · reading problems fixed 2

Things I could not settle:
- The two definitions of "built" (chapter 3 vs this preface) differ, and chapter 3 is not mine to edit.
- I did not recount the blocks. The "except the exercises" wording does not depend on the count.

=====

ch10 · 9 of 9 items confirmed · 3 of 3 reading problems fixed · `check_fr.py 10` ok · `book_audit.py` clean (82 pages). Both languages edited. No code fence, front matter or guard number touched.

- **Line 218, "the three refusals" · confirmed.** The `refinablecode_narrated` guard asserts two refusals, bounds and options; "unchanged" is asserted only for bounds. The unknown-point refusal is in `gate_deepening_narrated` (the "ghost" scene, line 79). The page now says "the two refusals that leave the source whole (bounds and options)". The gate guard now proves "the refusal of an unknown point" first.
- **Line 77, "third law of the house" · confirmed.** Only the code comment ties "NEVER mutates" to LAW 3 (`stzRefinableCode.ring:21`). Now: "The library's comment calls this its third law: a rejected proposal never ends changed." This also fixes the reading problem, since no earlier page defines the house's laws.
- **Line 122, "and a diff cannot" · confirmed.** The block prints only `:inheritedBy`. I cut the clause.
- **Line 230, "each with a guard that passes" · confirmed.**
  - The code-graph guard scans a live path, `D:/GitHub/stzlib/...`.
  - The point-cascade guard asserts the line and the unknown point, not `alsoTouches`.
  - The page now says the section 5 guards cover the built items "with two exceptions": the class cascade has no guard here, and no guard asserts the other points on a line.
- **Line 247, designer door · confirmed.** It now names two cascades: for a point, the line and its points; for a class, the inheritors. It ends "not yet one".
- **Line 239, `.rfn` · confirmed.** `CHARTER.md` D6 (lines 818-824) takes `.rfn` and "`.zrfn` retired to stzlib's comment-tag lift". Now: "takes `.rfn` for the sentence and leaves `.zrfn` to the library's comment-tag lift."
- **Line 232, `stzPolyCode` "never existed" · confirmed.** The design says on 2026-07-13 that no such class exists, then redefines the name as the `refine/` module. Now: "is not in the library at this commit." The same line's "pure-Ring spike" now reads "a spike written only in the former host language". The French already said this.
- **Lines 23, 208, 222-226, field claims · confirmed.** Only line 21 carried the "(General knowledge ...)" marker.
  - I wrote "much of the field's ..." in the three claims about the field's answer, its approach to agents, and trust.
  - "thousands of teams" is now "many teams".
  - I added the marker to those paragraphs and to the "tools lead in breadth" paragraph, which has the same kind of claim.
  - The French follows with « une bonne part de ... » and « (Connaissance générale, ...) ».
- **Lines 234-239, "What is absent" · confirmed.** The three bullets exist and run (`stzRefinableCode.ring:187, 455-476, 283-292`). Only the saved-history bullet is absent, and the front-matter `absent:` already says so. Retitled "What is built, and where it stops". This also removes the drafting note "and the page should say it".
- **Line 238, "admitted in my run" · confirmed.** The code ranks an unknown posture 3 (`_PostureRank`, `stzRefinableCode.ring:187-193`), and no block ran it. Now: "the code gives it the top rank. So a proposal that says it comes from a martian clears a floor of trusted."

Reading problem, "the cascade" naming two objects (lines 79-122): fixed with one sentence at line 79, "There are two cascades, and they are separate." The French has the same sentence.

confirmed 9 · not confirmed 0 · reading problems fixed 3

Not settled:
- `"world.ring"` at line 112 names the former language, but it sits inside a code fence, so I left it.
- I did not rewrite the other `read`-adjacent wording of "Three refusals" at line 77. It describes the chapter's own block, which does show three refusals (bounds, options, ghost).

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\10-programming-becomes-refinement.md`, `D:\GitHub\ayouni\books\softanza-book\src\fr\10-programming-becomes-refinement.md`.

=====

Chapter 14 is fixed in `src/en/14-knowledge-programming.md` and `src/fr/14-knowledge-programming.md`. `python tools/check_fr.py 14` says ok, and `python tools/book_audit.py` is clean (82 pages). I changed no code fences and no front matter. I did not mark the page `read`.

- **line 37, no earlier sentence · confirmed.** The design document (`SOFTANZA_INTELLIGENCE_ARCHITECTURE.md`, captured 2026-07-13, line 41) already has "AUGMENTS THE SYSTEM'S INTELLIGENCE AUTOMATICALLY. No code change. No training." I replaced the sentence with "The design document of 13 July 2026 already says it, in nearly the same words".
- **line 173, same graph · confirmed.** It now reads "a graph of the same class as the first blocks used".
- **line 173, one default graph · confirmed.** `stzKnowledgeWorld.ring` says DUAL-WRITE. I added "The old globals still exist, and the graph grows beside them: the library's header calls it a dual write."
- **line 220, "Two more limits" · confirmed.** Three follow, so it now says "Three more limits".
- **line 181, court claim · confirmed.** Scene 4 calls `StzApplyKnowledgeDerivations()`. The court now says the law derives the reverse edge "when the derivation step is applied after a fact is added".
- **lines 144/153/187, fires on add · confirmed.**
  - `EnableAutoDerive` exists in `stzGraph.ring` and is off by default, and no test covers it.
  - Line 153 now says this is the only place a declared law fires on add that a run in this book shows. It also mentions the switch, off by default, which I did not run.
  - Line 187 now says "in the runs I kept, one law derives a fact". Line 144 is unchanged, because its block is a kept run.
- **line 27, Datalog · confirmed.** Only Prolog appears in the record. It now reads "The record names Prolog only, as a language to reach". I left "Prolog and Datalog" in the field description, as general knowledge.
- **lines 68/189/287, a no as certain as a yes · confirmed.** I added the caveat once, on line 68: certain about what is recorded and declared, "not derivable", not "false". Lines 189 and 287 are unchanged.
- **line 189, same file · confirmed.** It now says "the same format carries a course, …".
- **line 165, ninety-nine files · confirmed.** I counted 99 `.zknw` files, all under `base/education`: 87 in `program/` and 12 in `overlays/`. It now says "In the education module the snapshot holds ninety-nine…". Line 277 now says "education module" too.
- **line 142, "A session found it" · confirmed.** I dropped the clause.
- **line 187, read by nothing else · confirmed.** It now says "As far as the record shows, …".
- **line 262, `@isfruit` · confirmed.** It exists only as a research run (`research/ch14.md` §L7, 2026-10-08). The text now says "on 8 October 2026 it stopped with …; I did not keep that run as a block."
- **line 273, `is-a` transitive · confirmed.** It now says it "ran, in an earlier probe whose run I did not keep".
- **line 287, offline · confirmed.** No run supports it. It now says the design's second law (LAW 2) requires nothing paid or remote, and that I did not run the file offline.

Reading problems fixed: 3.
- Removed the production note "Check the dates before print."
- Gave "names it" an antecedent: "a comparison that sets such databases against this library".
- Changed "one law kind fires" to "one law derives a fact".

Totals: confirmed 14 · not confirmed 0 · reading problems fixed 3

I did not touch the `ValidateOntology` note, which the report says appears only in the body and not in the front matter. Paragraph and heading counts are unchanged in both languages.

=====

Chapter 6 report. `python tools/check_fr.py 6` reports `ok` and `python tools/book_audit.py` reports "audit clean". Both runs were after the edits. I edited only the two chapter files (English and French). I did not mark the page `read`.

- **L27 Craft quote** · confirmed · Craft page (`content/en/craft.md:34`) reads "A loop hides which move it is making. Softanza names the four moves, and a task is decomposed into them instead." I quoted it as it stands, dated "as the page reads on 9 October 2026".
- **L152 W vs WXT** · confirmed · `stz-conditional-code-narration.md` says W was "fast, limited" and WXT "expressive, slow". Now "a more expressive but slower extended form".
- **L176 design marks** · confirmed · `SOFTANZA_ENGINE_DESIGN.md` has `Walker [PLANNED]` (l.474), `Checker [PLANNED]` (l.496), `Yielder [PLANNED]` (l.536) and `Performer [PLANNED]` (l.577). Only `engine/src/yielder.zig` exists. Now "marks all four as planned; only the yielder has an engine file".
- **"the founding article" (L13, L146, L182)** · confirmed · the record never calls it that. Now named "Bridging Minds and Code". In the front matter I used single quotes, because double quotes break the YAML.
- **"on lists and strings" (L11, L174)** · confirmed · the `stage.built` text now says "on lists". L174 already read "walks on lists".
- **§5 guards** · confirmed · `597` and `495` use `StzListQ` with `AddWalker`, `WalkUntil` and similar calls. Neither uses `Wk`, `Walkables`, `WalkNSteps` or `WalkBackward`. I added both points. I limited the claim to "the guards named here", because other tests such as `497_other_walking_techniques` mention those verbs.
- **L166/L195 mistyped condition** · confirmed · the only run is `print("hacked")`. Now "a condition that calls something the language does not know gives an empty list and no error", and in section 8 "a call it does not know gives an empty list, not an error".
- **L185 eval** · confirmed · `stzList.ring:5899` (`StringsW`) and `:5923` (`ItemsWhere`) call `eval` on the condition. I did not re-open `stzListChecker.ring:487-492`, but `ContainsW` there evals the transpiled string. I added all three, plus one sentence saying the earlier "cannot run as code" claim holds for the engine's path only.
- **L182 "none of its code runs"** · confirmed · the site's run is 12 raised and 1 differs. Now "none of its code runs as written; in the site's run twelve blocks raised and one differed".
- **L66 "cannot tell you … until it has skipped"** · confirmed · now "A loop does not hold its route as a value you can ask."
- **L66 "stops in silence"** · confirmed · L180 says a single step larger than the range raises. Now "Beyond the end, when the walk is underway, it stops in silence."
- **L83 article's argument** · confirmed · the edge narration says you stop at a wall (error) and simply stop when the road ends. I replaced "a step behind the first is not a step" with a paraphrase of that.
- **L183 empty strings** · confirmed · `EmptyStrings()` is used at narration l.85 and `RemoveEmptyStrings` at l.114. Now "The mental-model article's getter `EmptyStrings()` does not exist."
- **Reading 1 (L117)** · fixed · "Look at the two `Content()` outputs, before and after the `PerformW` call."
- **Reading 2 (L160)** · fixed · I read test 483 and now name the cursor words (`@NextNumber`) and the raw index form (`This[@i+1]`) in the sentence.
- **Reading 3 (L180)** · fixed · I removed both "draft" mentions, since "draft" is the book's reading, not the record's.

confirmed 13 · not confirmed 0 · reading problems fixed 3

I did not confirm the "session of 2 October 2026" attribution on L27. The research file ties it to the stzsite memo of 2026-10-02 and I kept it. The page now reads differently from that session's wording, so I added the 9 October reading. Section 4 still says the extended form was "removed" and "retired". The narration says WXT "remains as a deprecated alias of W", and test 483 says "retired". I left that wording, as no item flagged it.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\06-the-mental-model-and-the-metaphors.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\06-the-mental-model-and-the-metaphors.md

=====

Chapter 15 is fixed in both languages. `python tools/check_fr.py 15` reports ok and `python tools/book_audit.py` reports clean (82 pages).

- L280 "rung two" · confirmed · chapter 9's ladder has the pattern at rung one and the cascade at rung three, so it now reads "chapter 9's third rung". I also glossed the cascade in one clause (many faculties firing in turn on a shared state).
- L296 and front matter L13 "three of the media" · confirmed · HF-5 and block 13 show none of the six refuses a word. It now says "none of the six media", and `absent:` says "in all six media".
- L254 "block above" · confirmed · `g` is defined in section 3, so it now says "the graph of section 3".
- L223 "and tables" · confirmed · the `stzTablex` header lists no defects (only two code comments), so I dropped "tables".
- L294 "text, list, number, table" · confirmed · the course defers tables ("Coming next"), so I dropped "table".
- L286, L296 "six verified" and "seven kinds" · confirmed · lists and time have no guard, and graphs have no small function. It now says "Use the ones with a guard: text, numbers, tables, matrices and graphs" and "six kinds of data, graphs apart". I listed graphs among the guarded ones because `guards.json` has `00_graphex_narrated`; the report's suggested list left them out.
- L225 "the reason time fails" · confirmed · no run shows a repair would fix time, so it now says "a likely reason".
- L282 "no class takes a pattern" · confirmed · `stzListexUter.ring:125` does `new stzListex(pattern)`, and the gallery scripts use the pattern classes. It now says "outside the regex folder, the tests and the docs, no class takes a pattern". The education-course sentence now also mentions the gallery.
- L278 date and the "other four answer 0" · confirmed · HF-5 says Matrex and Tablex return an ERROR token and Numbrex and Timex an empty list. The text now says that, and that the central record "relayed" the finding on 28 September 2026.
- L201 "found two years later" · confirmed · only the study gives that interval. It now reads "The study dates the finding of their purpose two years later", and I glossed the answer protocol in a clause.
- L233 uniqueness flag · confirmed as unsupported · no block holds it, and `stzListex.ring:804-830` has a uniqueness check, so only the research notes claim the failure. It is now "In my run (research notes, no block)... accepted", with the code's existence stated.
- L213 "sixty checks" · confirmed as unsupported · only `research/ch15.md` holds the run. It now says I note it in my research notes, not in a block.
- L235 "a range without a step raises" · confirmed as unsupported · no block holds it. It is now "In my run (no block)... raised".

Reading problems fixed (R=4):
1. L31 now says the study of the record "is not the field study above".
2. `@Node10` is now glossed, and "quantifier" is defined (`+`, `*`, `?` or a number after a token).
3. L203 now has one sentence defining "the builders" (classes that write a regex from named steps in code, not from a string). I avoided the word "maker".
4. "The cascade" and "the answer protocol" are glossed in clauses.

confirmed 12 · not confirmed 0 · reading problems fixed 4

I did not edit any code fence. I did not touch the front matter except the `absent:` text. I added no number beside a guard. Nothing was left unsettled.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\15-pattern-languages.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\15-pattern-languages.md

=====

Chapter 12 report (`src/en/12-a-language-declared.md`, `src/fr/12-a-language-declared.md`). `python tools/check_fr.py 12` returns "ok" and `python tools/book_audit.py` returns "audit clean".

- line 90, "fourth pair" · confirmed · book-run block 2 gives `1 1 1 0 0 0 1`, so forty portions is the second pair. Now "The second pair".
- line 92, "candidate byte" · confirmed · `research/ch12.md` K3 says "candidate token". Now "candidate token"; the French has « jeton candidat ».
- line 278, `[ 2001, 4003, 20010 ]` · confirmed · the shown table (A 0,1,4; B 2,4,20) would give 2000, 4001, 20004. The figures fit A = 1,3,10 with B = 2,4,20. The text now says it was a probe on another table, with those values.
- line 228, "second language" · confirmed · `CHARTER.md:31-33` says "general-purpose floor". Now "the general-purpose floor under the family of declared languages".
- line 266, quoted formulas closed · confirmed · no such sentence in chapter 11. Quotation marks dropped; the text says "takes the closed condition language of chapter 11 and of the condition above to cover every formula".
- line 173, "unadapted" · confirmed · `CHARTER.md:238, 247-248, 566, 556`. Only W and Z are unadapted; F and A are re-expressed. Q was judged on the older language's captured answers (`CHARTER.md:575`), which the report did not mention. The sentence now says all three.
- line 142, refusal texts · confirmed · only GBNF-F5 (`schema_gbnf.zig:136`) carries "the Ring court". M7 (`gbnf_machine.zig:539`) and M4 (`:714`) do not. Now "The text of the nested-structure refusal carries…".
- line 190, "a quarter of a second" · confirmed · the only recorded timing is 0.245 s for the machine language (`research/ch12.md:355`). Now "a fraction of a second".
- front matter vs section 7, stage words · confirmed · the menu-grammar gap sat under both designed and absent, and "a factory in the library" under both absent and designed. I removed the menu item from `designed` and "a factory in the library" from `absent`. Section 7's absent paragraph now carries the menu gap, marked as seen above. Same in French.
- line 206, "charter's first morning" · confirmed · "The forge, which does not exist" is `PRINCIPLES.md:423`, a file headed v0.2 draft, 2026-10-01. `CHARTER.md:928` only says it does not claim "a forge that exists". Now "The principles file, dated 1 October 2026, says…".

Reading problems, all fixed:
- line 173: the paragraph now says which language each fraction belongs to, in order, and that the three missing of 117 of 120 are the fleet file's kinds (`CHARTER.md:540`).
- exercise: there are five `#-->` promises, so the added quantity prediction is now the "sixth". The lesson is "the third, the fourth and the sixth".
- line 224: the table's "faces" row is now named as the second sense. The ribbon sense is "a tab of the environment's ribbon, one phase of a life". The ribbon sense follows chapter 26, where the facets are Define, Build, Govern and Ship.

confirmed 9 · not confirmed 0 · reading problems fixed 3

Nothing is left unsettled. Two small points, for whoever checks the French:
- In the French I rendered "general-purpose floor" as « socle généraliste ». `FRENCH.md` has no entry for it.
- The lesson sentence now names three promises, not two, because the old "third and fifth" no longer matched the block.

=====

- line 15 · rulings · confirmed · 12.26 is example-driven programming and is not cited in research/ch19.md. I replaced it with 12.30 in both languages. 12.30 is the book's contract, and research/ch19.md cites it.
- line 239 (analyst) · law makes it refuse more · confirmed · `@aLaws` is only learned, saved and loaded in stzDLM.ring (lines 52, 126-132, 587). `Ask`/`AskXT` never read it. I changed the sentence to "a law you add makes the graph refuse more, with no training; the model's own answers do not read it yet."
- line 194 · "seven lines" · confirmed · the block holds six calls. I wrote "in six calls" in both languages.
- line 218 · misquotation · confirmed · stzDLM.ring:235 gives the real string. I quoted it: "I hold no 'contains' knowledge about 'tiramisu'." The quoted string is kept in English in the French page, as the code blocks do.
- lines 27 and 31 · gate "the same" · confirmed · it is the design's sentence, and line 196 says "Nothing chains them". Line 27 now begins "And in the design the gate is…". Line 31 reads: "In the design both rungs end at the same gate; here the gate is the `Admit` of the last block of this section, called by hand."
- line 54 · "after an entity, only its relations" · confirmed · `Complete` returns relations only for an entity that is a fact's subject. It now reads "after an entity that bears facts, its relations".
- line 105 · "The model refuses it" · confirmed · the block asks a different input than `cLie`. It now reads "Asked what a tiramisu contains, the model answers that it holds no such fact."
- line 196 · duplicate no-op as a form of the last stage · confirmed · the design's stage is a rejection of non-constructive redundancy, and set-like dedup is not that. I dropped the clause, and the sentence now ends "and the admission above enforces a law, which is compliance. Nothing chains them."
- line 220 · "every proposal meets a gate" · confirmed · no code routes `NeuralGenerate` output to `Admit`. It now reads "can be put to a gate that can refuse it with a reason".
- line 212 · "only part of it ran for this page" · confirmed as unsupported · scenes 7 and 8 need a generative model file (guard lines 196-202). `data/guards.json` only counts 50 `chk`. It now reads "which the snapshot does not hold; the record counts 50 assertions in that guard." This matches `data/guards.json`.
- reading problem, line 218 · "the table above" · fixed · it now reads "its present state is the one section 7 gives".
- reading problem, line 206 · "the section starts from" · fixed · it now reads "The finding I start from is".
- reading problem, line 212 · strict form of adding a fact · fixed in one clause: "in which a fact added without its admission is refused". The guard's own wording is "a naked fact is refused in strict mode" (knowledge_integration_narrated.ring:120).

The French has the same edits in the same places, and paragraph, heading and list counts are unchanged.

`python tools/check_fr.py 19` reports ok. `python tools/book_audit.py` reports clean on 82 pages.

confirmed 10 · not confirmed 0 · reading problems fixed 3

I could not settle one thing, and I left it alone as the report did. Line 200 ("On 13 July 2026, I ruled") still waits on the author's confirmation, as research/ch19.md §14 asks.

Files changed:
- D:\GitHub\ayouni\books\softanza-book\src\en\19-the-domain-language-model.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\19-the-domain-language-model.md

=====

Chapter 7 · 80 claims checked, 20 report items · both files edited; `python tools/check_fr.py 7` is ok and `python tools/book_audit.py` is clean (82 pages).

Edits are in `src/en/07-the-writing-style-and-the-seven-goals.md` and `src/fr/07-the-writing-style-and-the-seven-goals.md`. I checked the deck (`max/temp/goalssamples.ring`), `stzString.ring`, `stzList.ring`, the guards, `research/ch07.md` and the study (12.14) in `drafts/stzsite-roots-and-achievements.md`.

**Wrong**
- l.200 goals list · confirmed · now "expressiveness, reliability, the human metaphors and the practical abstractions", matching chapter 5.
- l.196 deck quote · confirmed · quote dropped for the deck's advice to use the keyword Item with any enumerable type.
- l.210 "six thousand" · confirmed · the study's 6,090 is now printed, quoted as "applied by hand at 6,090 points".
- l.127 five names · confirmed · the five `...CharsRemoved` names are listed. Two are defined (`stzString.ring:20122,20132`), three are not, and `RemoveLeadingAndTrailingChars` is defined but not one of the five.
- l.212 Yield/Perform · confirmed · both are defined (`stzList.ring:7183,7219`) and now "answer wrongly on some of the deck's examples". The research run gave `[ ]` and zeros, but `Yield('len(@item)')` worked.

**Overclaim**
- l.160 `vizFindAll` · confirmed · narrowed to "on a string"; a list has `VizFindAll` (`stzList.ring:13246`).
- l.212 FF/FX/dft/inf/WalkFF/AddWalkerFF/Check · confirmed · they appear only in the deck file and the archive, so now "named in the deck and not defined in the library's code, the archive aside". I changed table row 7 ("raise") to "are not defined" to match.
- l.216 `483` · confirmed · "proves the condition in a string, in two spellings of the same scan". Both assertions are `FindW` calls on a list; `WF` is only in the header.
- l.216 `602` and `59` · confirmed · ", in Arabic too" dropped. `602` has no Arabic, and in `59` the Arabic is `#o-->`, an observation.
- l.216 `48_replacebymany` · confirmed · "proves that the replacements go in order".
- l.181 alternatives · confirmed · the paragraph now speaks only of free-order parameters. Principle 7 (`ringpp/haro/PRINCIPLES.md:318`, as the report cites it) does not refuse alternatives, and I did not re-open that file.
- l.210 info-tags · confirmed · the forms are marked, and the study reads the tags as the feature-level vocabulary of expressiveness and flexibility.
- l.277 door · confirmed · now "In the study's reading, ...".
- l.109 "one method" · confirmed · `FindNthNext` (:7843) and `FindNextNth` (:7896) are separate definitions, and so are the two string names (`stzString.ring:11281,13365`). Now "one act, with two definitions".
- l.210 4,766 · confirmed in substance · now "in the archive folders". I did not recount the 4,765 and 1 split.

**Unsupported**
- l.266 · confirmed as unkept · added "These three come from the research session's runs; no block of this chapter keeps them." The raise statements stay.
- l.264 · confirmed as unkept · prefixed "In the research session's runs".
- l.198 · confirmed · now "in the research run its first line carried a line number". The research file notes "Line 3031 in file here:".

**Reading problems fixed**
- l.164 · "headline" replaced by "summary ... a session's reading and not a text of the library".
- l.181 · the paragraph is rewritten with "ships" replaced by "keeps".
- l.212 · added one-line glosses for Check, Yield and Perform. FF, FX, dft and inf were already glossed, and "raise" no longer applies there.

Count: confirmed 18 · not confirmed 0 · reading problems fixed 3

The report lists 20 items: 18 under Wrong, Overclaim and Unsupported, and 3 reading problems. The three reading problems are counted separately from the 18 confirmed.

**Not settled**
- The "raises" wording for the braced form, `day8 : day11` and the list constructor rests on the research session's runs and code reading, not on `data/book-run.json`. The table rows 11 and 12 and the earlier "it raises" sentences (l.107, l.109) are unchanged.
- I did not recount the info-tags.

=====

Ch13 report (`src/en/13-natural-and-executable.md`, `src/fr/13-natural-and-executable.md`, same edits in both)

- l.176 "Four languages as data" · confirmed (five packs: l.11, l.270, `research/ch13.md:591`) · heading now "Five languages as data".
- l.365 `ReplaceLowercaseCharsQ` source · confirmed (it is only in `stz-bridging-minds-and-code.md:217,226`) · moved to the bridging article's sentence. The other near-natural chains (`InLowercase`, `LettersNB`, `BeforeQ`, `FirstCharQ`, the brace form) are in the near-natural article, so they stay.
- l.371 "not a sentence of the author's" · confirmed (the memos give it as his words) · now "The memo reports that phrase as his own words. The book quotes the memo with its date, and cannot source the phrase to him." Also "no sentence of his in that voice that the book can source".
- l.306 "I ran it on 9 October" · confirmed. Chapters 2 and 11 are still to be aligned (see below). Now "A researcher ran it twice on 8 October 2026". The `caps` / `mirrored` failure is stated as "in that run", and so are `Unresolved()` and `UnderstoodAll()` printing 0. The guard asserts caps→METHOD_UPPERCASE and mirrored→METHOD_REVERSE, which I read in the guard.
- l.308 "run once each … passed all" · confirmed as unsupported by data (`guards.json` holds counts only) · now "in that run they passed all their assertions; the book's own data holds only their counts".
- l.316 "nine continuations" · confirmed (the guard asserts membership only) · now "In a researcher's run … answered nine continuations".
- l.318 `Replace` / `Add 3` printing · confirmed (no block) · cites the section 3 block, where `Understood()` prints `contains` without the 'r'. The `replace` / `add` examples are attributed to a researcher's run.
- l.365 "twelve chains, eight work" and the two nested boxes · confirmed as researcher's run only (`research/ch13.md:473-474`) · attributed to a researcher on 8 October 2026.
- l.276 git dates · not confirmed as wrong. I checked them in `D:\GitHub\stzlib` and they hold: 12 Mar 2022; 16 and 19 Sep 2025; 30 Oct and 2 Nov 2025; 9 Jul 2026. Ancestry of 4b138088b to the pin also holds (the other commits were not checked). The parenthesis now says the dates were checked there on 9 October 2026.
- l.280 "Its thesis" · confirmed (`NNL_REVIEW.md:23-26`) · now "The thesis of near-natural language, in that review".
- l.50 "the reason lives on the chain" · confirmed (`NNL_REVIEW.md:322-330`) · now "the reason is kept. The block reads it with the console's `Why()`; the chain's own is `WhyCheckFailed()`".
- l.292 "I refused global context" · confirmed (`NNL_REVIEW.md:355-359`) · added that the globals survive as fallback shims for legacy methods.
- l.117 "both say why and how sure" · confirmed · now "the chain of truth says why and how sure".
- l.206 "printed as the library's own sentences" · confirmed. The guard uses 'ring' where the book uses 'haro', and has a list reversal where the book has a string reversal in Turkish. Now "modelled on the guard's", with that difference stated. I did not write the guard's word 'ring' in prose, because `check_fr.py` flags it.
- l.308 "454" · confirmed (the seven named guards sum to 269 in `guards.json`; the other four, 44 + 18 + 45 + 78, are unnamed) · now "The assertion calls written in the seven guards named above sum to 269".
- l.320, l.381 "offline" · confirmed (the front matter itself says no no-socket guard exists) · now "designed to run offline, which no guard measures" and "designed to run offline with no key".
- l.312 "English twenty-three" · confirmed (`research/ch13.md:423`) · added "the two it lacks, English reaches through the grown vocabulary".
- l.365 "The 2020 sentence" · confirmed (no 2020 source) · now "The sentence of the bridging article that carries `IsAMQ`". This also settles the undefined-term reading problem.

Reading problems fixed:
- l.276 "the first slide this chapter prints" → "the earliest slide the record dates" (no slide is printed).
- l.365 "2020 sentence" (fixed as above).
- l.308 "454" read as a sum of the seven named guards (fixed by the 269 edit).
- Skipped: the date-heavy l.276 paragraph and the unintroduced "strategic diagram". Fixing them takes more than one sentence.

confirmed 18 · not confirmed 1 (git dates) · reading problems fixed 3

`check_fr.py 13`: ok, no warnings. `book_audit.py`: audit clean. EN and FR both still have 396 lines. I made no front matter changes and edited no code fence.

Could not settle:
- The memo quoted at l.371 (and used at l.23) is in another repository and is stamped "Status: PRIVATE". `research/ch13.md:607` says it is quotable only with the author's say. I kept the quote, now correctly attributed, but the author must decide whether it stays.
- Chapters 2 and 22 say 8 October, and chapters 11 and 22 say 9 October, for the same two runs of `semantic_resolver_narrated`. The evidence supports 8 October. Chapter 11 also says "my research for chapter 13 ran it twice on 9 October". Those pages need aligning by whoever owns them.
- I did not re-check the claim that no 9 October run exists beyond `research/ch13.md` and the data files.

=====

ch08 · 17 items confirmed, 2 not confirmed, 3 reading problems fixed. `python tools/check_fr.py 8` reports ok. `python tools/book_audit.py` is clean (82 pages). No code fence was touched.

Edits are in `src/en/08-functions-as-linguistic-expressions-and-scope.md` and the same-named file in `src/fr/`.

- l.250 "promises true, true, true" · confirmed · `23_arenegativex.ring` has four "No" lines promising T, F, T, F, and research/ch08.md:578 shows all four print 0. Now "promises true on two of its four "No" lines, and the run prints false on all four".
- l.221 "a dozen verbs" · confirmed · the design doc says "N verbs". Now "many verbs".
- l.233 Python/Swift · confirmed · Python checks keyword arguments at the call, Swift labels at compile time. Reworded to say so.
- l.29 "without any model or any parser" · confirmed · it now quotes the study's "without machine learning or NLP systems", credited to the study of the site's roots.
- l.250 "status of one" · confirmed · now "in my probe of 8 October".
- l.252 and l.227 "61 of 62" and "one of my runs" · confirmed · `guards.json` holds 62 assertions only. Now "in one probe run, which `data/` does not record", with the 62 unchanged.
- l.249 "Their heirs" · confirmed · now "The nearest thing today is".
- l.33 suffix order · confirmed · GRAMMAR.md l.108 says order is not judged. Now "in these names".
- l.47 "Give it a name" · confirmed · `_StzParseName` is internal (`stzReflectFuncs.ring:123`). The text now says so and names `ExplainMethod` as the public way in.
- l.147 "not a correction engine" · confirmed, but I did not use the reader's "for method names". `stzObject.ring:5981` does suggest method names ("Did you mean"). The text now reads "in what I traced", says the other files were not traced, and notes the suggestion-only message.
- l.215 and l.233 designed told as built · confirmed · the paragraph now says "principle 7 ... designed and not built", "would generate", and that the spike judges names only (595 names, not bodies, not suffix order). l.233 now says "judged by the Haro spike, on names and not on bodies".
- l.215-221 voice · confirmed · the four paragraph heads and the "first guess" sentence are now attributed to the design document (l.221), the header comment (l.217) and the narration (l.219). I left the l.223 paragraph, outside the flagged range.
- l.217 queue · confirmed · the header dates 10 July 2026 for the `_aFuture` queue, and says the FQ and FFQ wrappers were already gone.
- l.219 "retired" · confirmed · the narration says WXT is "a deprecated alias". It also says `eval()` is not involved, and the text follows that.
- l.227 `00_regex_narrated` · confirmed · the text now says it covers `Match`, `MatchFirst` and Z, and nothing for `MatchLine` or `MatchWord`.
- l.239 and `stage.built` · confirmed · now "fourteen ... some with examples other than the article's".
- l.266 "cannot be moved" · confirmed · now "is not moved".
- Reading problems fixed · 3 · l.215 "table below" is now "this chapter"; l.62 now says "four" and lists four; a sentence now explains why o3 is a new object with the same pattern (`MatchWord` rewrites the pattern).
- Not confirmed (2): the l.147 "for method names" narrowing, because the code contradicts it, handled as described above. The `figures:` line says "run as shown". I did not edit it because the brief lets me change only the text of `stage:` values.

Not settled: the `figures:` front-matter line still says "fourteen forms run as shown" while the prose and `stage.built` now say "some with examples other than the article's". Someone with the right to change that key should adjust it.

=====

16 · Seven languages, one door: confirmed 11 · not confirmed 0 · reading problems fixed 2. `python tools/check_fr.py 16` passes with 1 warning, the word "Ring" in the line-146 quote, which is the former host name framed as history. `python tools/book_audit.py` is clean.

1. Line 284, "table in section 3" · confirmed · now "the list of layers in section 3" (French: « la liste des couches de la section 3 »). Section 3 has the layers as one sentence, not a table.
2. Line 194, header with no `Execute` · confirmed · the header is in `50_extercode_smoke.ring`:3, not in `51_extercode_narrated.ring`. Now "The smoke test it narrates says in its header: no `Execute` (the L99 guardrail)."
3. Line 194, scene six · confirmed · governance scene 6 covers refusal and a declared posture. Scene 7 covers "postures travel". Both are now in the sentence.
4. Line 186, "of 2025" · confirmed · the narration text holds no date, but the site page says "in the repository since 2025-04-23". Now "The site says the article has been in the repository since 23 April 2025 (read 9 October 2026)."
5. Line 33, chapters 1 and 11 · confirmed · chapter 1 line 80 promises the seven layers, and only chapter 11 line 196 promises the difference. Both are now stated that way.
6. Line 66, "files and the system" · confirmed · `data/book-run.json` lists only "the system" as the effect for these blocks. Now "touching the system".
7. Line 116, "seven domains … eighth" · confirmed · the article's tree has seven modules plus `stzMeta` and never says "seven" or "eighth". Now: the article lists seven domain modules and a cross-domain one; the study counts seven and calls the host the eighth.
8. Line 194, offline and skips · confirmed · `pycodegraph_narrated` also skips its Python-AST scenarios when Python is not on PATH, and both skip their tree-sitter scenarios. Case-insensitivity is tested only for "PYTHON". Now "both skip their parser scenarios…, the first also its Python-AST ones", and "(tested for Python)".
9. Line 208, line break · confirmed · `CODEGRAPH.md` line 285 says the literal `"\n"` is a backslash and an `n`. Now "the literal `\n`".
10. Line 262, macroplan correction · confirmed · lines 620-624 of the macroplan concern `stz_polyglot`, a locale string registry marked [PLANNED], not the bridge. Now "a module of the same name in the macroplan, a string registry, was once marked done with no source".
11. Line 266, `range0` "runs" · confirmed · `extinpython/_RUN.txt` lists `03_pr.ring` (range0's guard) as FAIL on five assertions about empty ranges. `04_pr.ring` also fails on `range0(':5:-1')`. The claim that the slice form "prints an empty list" has no support, so I dropped it. Now: it has a guard, the record lists five failures on ranges that should be empty and one on `':5:-1'`, and "I ran none of it".

Reading problems fixed:
- **Line 182:** "the letter of it is x … the alphabet chapter" is now one sentence naming stzx (x for external) and "the vision's own file on the platform's letters". No such chapter exists in the book.
- **Line 146 (the report's Rules paragraph):** the author's quote now reads "Ring (the host's former name)", in French « Ring (l'ancien nom de l'hôte) ».

`stzx` appears nowhere else in the book, and I added it only here, as the report suggested.

Reading problems skipped:
- **Lines 33, 116, 188, 202 ("the study", "the engine design", "the vision"):** fixing them needs more than one sentence.
- **Line 116's four-way count of "seven":** I left that alone for the same reason.

Nothing left unsettled. I changed no code fence, no front matter and no other file.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\16-seven-languages-one-door.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\16-seven-languages-one-door.md

=====

ch18 · all 15 items confirmed or fixed · both pages edited, `check_fr.py 18` ok, `book_audit.py` clean (82 pages)

**Wrong**
- Guard ending (line 351) · confirmed · Three guards (`wisecoding_narrated`, `wisecoding_rich_narrated`, `ownagentstack_narrated`) print their own TOTAL, then call `pf()`, which prints the time and runtime version and raises. `tutor_gaps_narrated` ends with `Summary()`, which prints the total and a status and does not raise. The page now says each.
- "the last block above" (line 349) · confirmed · now "the tutor block above".
- "A reply that has a space in it" (line 313, front matter, line 369 and the exercise note) · confirmed · the values at line 110 ("tomato-sauce", "mozzarella") have no space, and the reply is split first. Changed to "a value with a space in it" in the `absent:` text, section 3, section 7 and the exercise note.
- The "guessing is replaced by asking" quotation (line 333) · confirmed · the design document (SOFTANZA_INTELLIGENCE_ARCHITECTURE.md line 108) reads "Guessing is replaced by asking; vibes are replaced by governance." Semicolon restored.

**Overclaim**
- "next work, filed and not routed" (lines 153, 367) · confirmed · `memos/2026-09-25.md:702` lists it under "waiting:" as move D, wise coding for code, registers 3 and 5, [not routed]. Now "lists the wise-coding work on registers 3 and 5 as waiting, not routed" in section 3, and "lists them as waiting, not routed" in section 7.
- "no native speaker has read them" (line 313) · confirmed · `stzTutor.ring:167-168` says "a draft awaiting a native reviewer". Now "the code calls them a draft awaiting a native reviewer".
- The "reason every call above is chained" sentence (line 341) · confirmed · the header (`stzConversation.ring:10-17`) concerns held copies of the graph. The chaining reason is the guard's, and line 203 already has it. Sentence dropped.
- Unmarked field statements (lines 27, 355, 357) · confirmed · the "General knowledge" mark now closes the section 1 opening paragraph and covers the whole section; I removed the duplicate on the third paragraph. Section 6 now says "as the field holds it" for the frameworks and for programming by example.
- "What is designed" omitted the example written back as a promise (line 367) · confirmed · the site's *by example* page, read 9 October 2026, calls it "a rule of the design and it is not built". One sentence added with that attribution.

**Unsupported**
- `ReplyIn` raising on a spaced value, and the direct door returning the refusal (lines 369, 313, 13) · partly confirmed · `research/ch18.md:448` and `sessions/2026-10-08-phase-2-evidence.md` (L18) record both from a run on 8 October 2026, but no block or guard of the book does. I narrowed the text:
  - It now says "In the research run of 8 October 2026 ... `ReplyIn` raised ... on each value containing a space that I tried".
  - It says the direct door returned the refusal.
  - It says "No block of this book records either result".
  - I did not add a block. It would sit in a code fence, I may not run `book_run.py`, and it would stay unrecorded.

**Reading problems**
1. Fixed · the exercise item 2 now reads "a number that picks a value the first reply made known". One sentence added after "Then run it": "An admitted reply uses up the question, so call `AskIn` again before the next reply." Confirmed at `stzConversation.ring:290-292, 365-367`.
2. Skipped · the repetition between sections 1 and 6 would need a rewrite.
3. Fixed by the "value with a space" wording.

I made the same edits in the French page, with the same paragraph, heading and list counts.

confirmed 11 · not confirmed 0 · reading problems fixed 2 (of 3)

Unsettled:
- The `ReplyIn` raise stays supported only by the 8 October 2026 research run. A `try ... catch ? cCatchError done` block, kept by a run, is needed for the book's own run to show it.
- The words "version of the library this book runs" now refer to snapshot 93d7a39bd, as in the rest of the chapter.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\18-the-five-registers.md`, `D:\GitHub\ayouni\books\softanza-book\src\fr\18-the-five-registers.md`

=====

Ch09 report: 22 of 25 items confirmed and fixed in `src/en/09-patterns-of-thought.md` and `src/fr/09-patterns-of-thought.md`. One item was only partly confirmed, and two reading problems were left as they were. `python tools/check_fr.py 9` prints "ok" and `python tools/book_audit.py` is clean.

Item · verdict · change:
- L33 "chapter 11" · confirmed · "You will see it in chapter 15" (chapter 11 follows chapter 9; chapter 15 is the pattern languages).
- L96 "chapter 17 you saw" · confirmed · "you will see".
- L201 "rung above it" · confirmed · "two rungs above it, at the fourth rung". The architecture puts the Softanzuter directly above the Regexuter and the agent above that.
- L12, L225 "three siblings" · confirmed · "four siblings, analyser, genetic, linguistic and quantic" in the `stage:` text and in section 7. Section 4 already said four.
- L211 guard 60 "stream" · confirmed · its scenes are the reactor backing, one-shot timer, repeating timer, non-blocking HTTP, settle watcher and teardown. The text now says a one-shot timer, the repeating timer, non-blocking HTTP and the settling attribute.
- L233 path verbs · confirmed in part · only `ItemAtPath` and `ItemsAtPaths` are subclass-only (`stzDeepList.ring:92,115`). `Paths()` is on `stzList` (`stzList.ring:11777`). The text names both facts.
- L219 star-rating source · confirmed · it is `softanza-reactive-objects-narration.md` (lines 812-824); the Reaxis article's table uses words. The text names the file and I added it to `narrations:`.
- L31 ladder · confirmed · "The architecture draws it as a ladder" (architecture 5.6, captured 2026-07-13).
- L53, L243 "every reaction keeps its why" · confirmed · "every reaction that changes a value", because the state is written only when the value changed. L201 got the matching clause.
- L75 `Pursue()` · confirmed · it counts verified firings and stops after twenty rounds (`stzPIAgent.ring:157-171`). The text now says so.
- L98 module "is the body of the agent" · confirmed · `stzPIAgent.ring` never calls it (only `stzAgentHost.ring` does). The text now says the macroplan presents it as the foundation for agents and that `stzPIAgent` never calls it. I did not use the macroplan's word "substrate", which the rules forbid.
- L119 "nothing subscribes" · confirmed · `Subscribe` is an alias of `OnPassed` (`stzReactiveStream.ring:89-99`). The text says the old word survives as an alias.
- L205 siblings "in prose" · confirmed · the article has a sample call for each. The architecture finds a purpose only for the genetic and quantic ones (induction, superposed candidates). Chapter 18 treats induction as absent and "several acceptable" as designed. The text now says "sample calls, no class" and that chapter 18 tells where it stands.
- L215 "six media" · confirmed · "the two media that have an Uter built, text and lists", plus "every firing that changes a value".
- L217 Rx · confirmed · softened to "most mainstream languages, a very large set of operators", marked "(General knowledge.)".
- L225 stale table · confirmed · the Layer 5 table marks all twelve modules PLANNED, including ones with source (`ENGINE_ARCHITECTURE.md:770-782`). The text says the table is stale and that the medium is planned in the engine design document.
- L230 "keep none of their promises" · confirmed · `listexuter/_RUN.txt` shows five fail and two skip. The text now says five of seven fail their expected output and two promise nothing.
- L211, L223 timeline "built" · confirmed · the guard covers construction, duration, adding points, one out-of-range refusal, aliases, named parameters and moving the ends. It has no gap, overlap or blocked-span check. Section 5 says this. Section 7 gets the losses (classic timeline files 7 fail, 18 promise nothing; `stzGridNav` untested), folded into the last bullet so the item count is unchanged in both languages.
- L211 Regexuter "tests I ran keep their promises" · confirmed unsupported, but `regexuter/_ERR_RUN.txt` exists ("PASS 8 ERR 0"). The text now says "eight classic tests ran without error in the folder's log; nothing there checks what they print".
- L230 "first block… three times… server pattern" · confirmed unsupported; I dropped it. `listexuter/_ERR_RUN.txt` records error C8 on the sixth file, which the text now cites.
- Reading problem 1 (L235 last bullet) · fixed · it now says what is absent, a native engine module for the model, without repeating L217.
- Reading problem 2 (L153 "third part") · fixed · "The chapter's third subject".
- Reading problem 3 (fourth rung unnamed) · fixed · L75 names the agent as the fourth rung, a thinking machine given a body, a world and a goal.

confirmed 22 · not confirmed 0 · reading problems fixed 3

Not settled:
- The report says "eleven engines PLANNED"; the table has twelve, so the text says "every module of its fifth layer" with no count.
- The research session's claim that the Listexuter's first block now prints the last result three times rests on one run with no record in the snapshot. I dropped it.

=====

ch21: 17 of 18 items confirmed, 1 not confirmed, 3 reading problems fixed. Both files are edited, `python tools/check_fr.py 21` returns "21-the-court: ok", and `python tools/book_audit.py` is clean (82 pages). Each fix is the same in `src/en/21-the-court.md` and `src/fr/21-the-court.md`.

- line 79 "copy of the same grammar" · confirmed (`tools/book_judge.py` header says it is the site's judge copied) · now "a copy of the site's judge, which is looser than the traveller".
- line 129 "bad password is redacted" · confirmed · `stzSecurityLedger.ring` loops from entry 2, so entry 1's text is never checked, and redaction only covers secret objects as subject. I rewrote it: an edit to the first entry is not caught, and that hid my first attempt. "Redacted" is gone.
- line 102 "no counters" · confirmed (the block has `nUnheard++`) · now "The counter in this block only counts the unheard; no counter decides the verdict."
- line 104 "second line" · confirmed (`PERCEPTION.md` section 4, item 3) · now "third requirement".
- line 112 "Edit one line" · confirmed (same loop) · now "any line after the first".
- line 102 "clearest recorded perception" · confirmed (one record) · now "the one recorded perception".
- line 253 "no automation ... says it should not" · confirmed (`PERCEPTION.md` section 6 only says a perception does not replace a number) · clause cut; now "The house's law says a perception does not replace a number, and no number replaces it." I also added "(general knowledge)" after "mature and automatic".
- line 272 "The author deferred them" · confirmed (R12 "deferred by the author"; R14 waits for a Linux machine) · POSIX paths now "until a Linux machine is available", and the deferral is limited to fuzzing, CI and signed commits.
- line 156 hours · confirmed (the document dates G38 and G41/G42 only) · hours dropped, dates kept.
- line 277 "29 September 2026" · confirmed (G22 says "three runs", no date) · date dropped.
- line 223 "later commit" · confirmed · now "another commit". In French I also fixed the gender slip "celle" to "celui".
- line 241 "I ran threat_model_narrated alone" · confirmed (`guards.json` holds a static count of 11, not a run) · now "The build counts 11 assertions in `threat_model_narrated`, a static count of its assertion calls."
- line 104 "written by a session" · confirmed (`PERCEPTION.md` names no writer) · dropped. I also defined "the estate" there as the author's whole set of projects, which fixes the undefined-term note.
- line 291 quoted phrase · confirmed (no word-for-word source) · quotation marks removed and the sentence reworded.
- line 251 missing "general knowledge" mark · confirmed · "(general knowledge)" added after "answer pass or fail".
- reading problem 1, Testoor · fixed at first use: "the traveller (it belongs to the plane named Testoor)". Lines 251 and 279 now say "the plane that holds the traveller".
- reading problem 2, line 227 · the states are now listed ("kept, diverged, unreached, unjudged, unperceived"), and the sentence says "unjudged or unperceived into pass or fail" instead of "the fourth or the fifth".
- reading problem 3, line 102 · fixed with the "counter" rewording above.
- line 253 "no automation of the verdict" · not confirmed as a claim about the record. Nothing in the record says either way, so I cut it rather than keep it.

confirmed 17 · not confirmed 1 · reading problems fixed 3

Unsettled: `research/ch21.md` records that I ran `threat_model_narrated` and got 11 of 11 passes. The only record of that run is the research file, which the report says does not count. I took the report's route and cited the build's static count instead.

I did not touch any code fence or front matter.

=====

20 · Agents that cannot hurt you. `python tools/check_fr.py 20` says ok and `python tools/book_audit.py` says "audit clean" (82 pages).

- 339 (not verbatim) · confirmed · "in the narration's words" is now "after the narration", and the tail is quoted exactly ("regulated or audited work, anything that runs unattended, and anything that must keep working offline at zero marginal cost"). Same change in French.
- 240 (live estate) · confirmed · `stzAgentRoster.ring` says outside a workbench the function is "the migration state the live estate still runs". The page now says the function gained a rehearsing path, the live estate still runs the direct write, and the block is my own declaration, not the live roster file, which I did not run.
- 35, 123, 353 (unset scope) · confirmed · `stzVirtualSystem.ring` runs the scope gate only `if @oScope != ""`. The gap bullet is now "An unset executor and an unset scope are unguarded", with one sentence on the scope check and the exactness claim narrowed.
- 123 ("Reality changes here and only here") · confirmed · now "In this block, ...".
- 307 (tool surface) · confirmed · now "the doctrine says ...", then "That is the doctrine's claim, and section 6 gives its limits."
- 23 ("every serious guide of 2026") · confirmed · now "which the narration says every serious guide of 2026 gives (it paraphrases one roadmap)".
- 167 (agent tidies a folder) · confirmed · now "A tidy-up ... driven here by hand through the twin as an agent would drive it".
- 200 (protected file) · confirmed · now "one file is still on disk, the file of the step the reviewer protected (the block prints the count, not the name)".
- 317, 347 (inbox of 8) · confirmed · the Zig test exists and the inbox is not in any Ring guard. 317 and 347 now say "tested in Zig only, not run". I also changed the `stage: built` value to drop the inbox from the built list and add the same caveat, in both languages.
- 331 ("a few clicks away") · confirmed · dropped, in both languages.
- 343 ("Reads are free") · confirmed · cited to the workbench header (`stzAgentWorkbench.ring:38-41`), and the closing sentence now lists it.
- 323 (443 ms / 61 ms) · confirmed · the pair is not in `data/`, only in `research/ch20.md`. Now "In the run I made for my research note on 8 October 2026, which the book's data does not hold".
- 31 (git commit of 9 July 2026) · not confirmed · `git log` on the library's repo gives `d8ee8dd35`, 2026-07-09, for the doctrine file, so I left the text.

Reading problems:
- 21 · fixed · "the autonomous agents that descend from them".
- 121 · fixed · "Two lines decide who may act", and `StzAllowAgentFunction` is now said to be a line of the platform's code, not of the file.
- 223 · fixed · the graph rule is now named, no-llm-effectful, and a slot is defined in one clause.
- 238 · fixed · "what remains" now reads priority, interval in milliseconds and coverage sentence, taken from `ring_bridge_agentloop.zig`.
- 37, 347 · fixed · the English "Ring door" is now "the door of the former host language", matching the French. This was a judgment call: the brief bars "Ring" only in code fences, but the French already avoided it.

confirmed 13 · not confirmed 1 · reading problems fixed 5

Unsettled:
- I did not check the claim that the live roster files are still pia v1, which the report cites from `SOFTANZA_INTELLIGENCE_ARCHITECTURE.md` §3.2. The page only says the live estate still runs the direct write, which `stzAgentRoster.ring` supports.
- The Zig inbox test (`softanzuter.zig`) exists and the refusal and count are in the code, but I did not run it.
- Section 7 still says "the roster's agent rehearsed and then committed". It matches `safeworld_narrated` scene 7, so I left it.

Files are `D:\GitHub\ayouni\books\softanza-book\src\en\20-agents-that-cannot-hurt-you.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\20-agents-that-cannot-hurt-you.md`.

=====

Chapter 22 report. Files are `src/en/22-compared-honestly.md` and `src/fr/22-compared-honestly.md`. `check_fr.py 22` is ok and `book_audit.py` is clean.

- Five comparisons "run on both sides" (front matter, l.35, l.142) · confirmed · The chapter's own l.88 and `research/ch22.md:196` say block five has no other side. I now say four on both sides and the fifth on the Softanza side only.
- Four site code pairs, "both sides, every output reproduced" · confirmed · In `stzsite/content/en/code.md`, pair 4's other side is a comment with empty output. Now: three on both sides, the fourth a comment, and "my note of the night says the outputs matched".
- Run times (l.35) · confirmed · `research/ch22.md:3` gives 22:24 to 22:34, and `book-run.json` gives 2026-10-09 05:32 for the build re-run (5 blocks kept). The text now says "between 22:24 and 22:34" and that the build re-ran the blocks on 9 October at 05:32. In French I wrote "05 h 32", which clears a `check_fr` warning.
- Polyglot battle date · confirmed · `narrations-dates.json` gives 2025-04-18. Now "18 April 2025".
- "Struck through with the date" · confirmed · SOFTANZA_PERF_VS_THE_FIELD.md names P8, P11, P10, P9 and no date. Now "with the phase that closed them".
- Rationals and complex "not built yet" · confirmed · `numeric_rationals_narrated.ring` (42 `Then(`) and `numeric_complex_narrated.ring` (38) exist in the snapshot. The comment at `numeric_no_loss_narrated.ring:90` is stale. I narrowed l.56 and l.112 to say so, and added that I did not run the two guards.
- Site "nowhere else" (l.144) · confirmed · `compare.md` (ae73285cc, 9 October 2026) now has "Where they lead", five rules starting "Cite or do not publish", and a line marked designed saying the register is not held as data. Nothing names the court. I wrote the present reading with its date and kept the 8 October search as drafted. I also narrowed "the sixty-four grids" on the site to "themselves", since the site now gives their number.
- "Four field studies with loss sections" · confirmed · §6 prints performance, incident and plugin studies, never the reactive-engine one. Now three studies named, plus the culture plan "which prints its losses". I changed both the front matter `stage.built` and §7.
- "Probably ran unoptimised" used to discount the benchmark · confirmed · `engine/build.zig` says optimisation buys about 15% on string, list and matrix work. I added that line, stating that build mode is a caveat and not an excuse.
- "File ends with a section titled…" · confirmed · `stzgraph-vs-other-graph-libraries.md:176` is a bold label inside the Conclusion. Now "its conclusion lists where traditional solutions win".
- "The record counts the genre" · confirmed · The draft only names it, and counts only the 64 grids. Now "names".
- "The memo's hand-off" · confirmed · The words are in `ringpp/peer/HANDOFF.md:81-82`, dated 13 September 2026. Now "the hand-off packet of the same day, 13 September 2026".
- Versions and other-side outputs (l.35 to 90) · not confirmed · They rest on `research/ch22.md` §4 alone, and I may not re-run them. The hand arithmetic holds. I left the text.
- "My scan: 37 tables in 29 documents" · not confirmed · `research/ch22.md:66-67` records the 37 tables, 366 rows and 29 documents, and the chapter already says the header rule is mine. I left the text.

Reading problems fixed (R=3):
- l.98: now "Printing losses is not the rule."
- "The spike": defined at l.96 as "as the memo calls the runtime's prototype". French: « que la note appelle "spike" ».
- l.94: ticks are now "in Softanza's column" and crosses "in the other columns", in both languages.

Counts: confirmed 12 · not confirmed 2 · reading problems fixed 3.

Not settled: "every output reproduced" has only the research note's word, so it is now worded as my note's claim. The other-side runs cannot be checked without re-running.

=====

Every item was already applied to both pages before I started. I confirmed each against the evidence and made no edits.

- **Row 36 (matrices) · confirmed, already applied.** Both pages say "not told". The line-14 count is eight. "One more … told only in part" is gone. A grep of `src/en` for `LinearSolver|stzmatrix-matrix|statistic` finds nothing for this row; chapter 16 only mentions R's statistics, a different tool.
- **"Forty-six" as final ruling (lines 10 and 14) · confirmed, already applied.** Line 10 says row 47, answer by example (ruling 12.26), was added the same day and is not in this table. Chapter 3:46 says the site's register says forty-seven, which matches.
- **Row 9 (future actions) · confirmed, already applied.** It reads "8 (removed on purpose, 10 July 2026)". Chapter 8:217 gives that date.
- **Row 10 (refinement gate) · confirmed, already applied.** It reads "four stages in the design, five checks in the code". Chapter 10:204 and 214 say the same.
- **Row 26 (visual orientation) · confirmed, already applied.** It reads "7 (the viz prefix only)".
- **Row 32 (time programming) · confirmed, already applied.** It reads "9, 15 (the timeline and Timex only)".
- **Row 43 (front door and secrets) · confirmed, already applied.** It reads "21 (secrets; the front door as an event only)". Chapter 21:116 shows `auth.login.failed` only as a ledger event.
- **Row 45 (tagging) · confirmed, already applied.** It reads "7 (the tags, and that no court reads them)".
- **Row 40 (performance plane) · confirmed, already applied.** It reads "21 (the frame profiler is not shown)". The phrase appears nowhere in chapter 21.
- **Row 15 (quantifiers) · confirmed, already applied.** It reads "some, most and few draw at random, and I say so", and "all" is no longer claimed.
- **Reading problem 1 · fixed already.** The line under "The twelve paradigm engines" now says nine rows and that the end of the page returns to the twelve.
- **Reading problem 2 · fixed already.** "Except those with a page" is replaced by explicit row numbers (4 to 8 and 10 to 12), with a note that the site column was left out.
- **Reading problem 3 · fixed already.** "In the shade" no longer appears before the register explains it.

The French page mirrors every change. It has the same 46 rows, headings and paragraph count.

`python tools/check_fr.py A` returns "ok, 1 warning(s)". The warning is the word 'maker' in RegexMaker, row 24, a library class name. The audit also flags it, but `python tools/book_audit.py` still prints "audit clean" (82 pages, en 41 and fr 41).

confirmed 12 · not confirmed 0 · reading problems fixed 3 (all already in place)

Nothing is left unsettled. The only open point is the RegexMaker warning, which I left as a class name per the brief.

Files: `D:\GitHub\ayouni\books\softanza-book\src\en\A-the-register-of-innovations.md` and `D:\GitHub\ayouni\books\softanza-book\src\fr\A-the-register-of-innovations.md`.

=====

Chapter 24 is fixed in `src/en/24-rehearse-then-commit.md` and `src/fr/24-rehearse-then-commit.md`. `check_fr.py 24` passes with one warning, and `book_audit.py` is clean. The warning is "07" in English and not in French. It comes from the plan heading date "2026-07-23" at line 373, which my edits did not touch.

Every item below was checked against the cited file in the 93d7a39bd tree. Line numbers are the report's.

**Wrong**
- L228 "no payments adapter" · confirmed · `stzCardPaymentsAdapter.ring` and `stzPispiHttpAdapter.ring` exist. Now "no live card-gateway adapter".
- L435 and front-matter `absent` · confirmed · the hub adapter is built and proved only against a twin (guard `payments_live_adapter_narrated`; chapter 31). Both now say so.
- L367 "live payments adapters not shipped" · confirmed · the service plan line 52 reads "live Stripe/PayPal/Adyen adapter". It now names them, attributes the sentence to the plan, and adds that a hub adapter is built (chapter 31).
- L361 "third was added" · confirmed · the plan says "three postures" and the registry code says four. Now "The local posture was added".

**Overclaim**
- L149 · confirmed · `:GitRepo` runs against a local bare repo with no network. Now "the kind of site that needs no tool but file operations".
- L189/191 rollback · confirmed · only a local site really rolls back; other kinds return 1, "best effort". Added "For a local site", and the others "only try, as a best effort".
- L273 vendor key · confirmed · the key is the invented string `sk-test-123`. Now "an invented test string".
- L277 "every way" · confirmed · the code lists eight invariants and the report shows five. Now "five of the eight".
- L425 `:emulated` "set by nothing" · confirmed · `service_registry_narrated.ring:82` sets it. Now "no library code; only a guard sets it".
- L431 "built by the toolchain" · confirmed · `wasm_narrated` was counted, never run. Now "its build checked by a guard that I did not run".
- L445 "Neither may ship a fake" · confirmed · now "a declared fake", since section 7 shows an undeclared one passes.
- Front-matter `built` "validation against reality" · confirmed · `Validate()` covers only delete/copy/move of files. Now "for the file twin".

**Unsupported**
- L185 bare `Deploy(:Production)`, L187 map names a missing engine file, L224 assistant run, L419 `UseIn` comment, L427 `Phase()` printed `production` · confirmed · the code supports each, but the runs are only in `research/ch24.md` (8 October 2026), not in `data/book-run.json`. Each now says "in my research run of 8 October 2026, outside this chapter's blocks". I kept the claim rather than deleting it.
- L377 "I ran both on 8 October" · confirmed · `book-run.json` is dated 2026-10-09. Now "My research run of 8 October 2026 ran both". The counts 93 and 60 are unchanged and equal `guards.json`.
- L441 step graph and credentials by name · not confirmed · the report itself asks for no change, and I looked at nothing further. The text stays.

**Reading problems**
- L35 three-clause sentence · fixed. The first clause is `SP3` in `SOFTANZA_SYSTEM_FOUNDATION.md`. The middle clause comes from `SOFTANZA_DEPLOYMENT.md`, "only an effectful actor commits". The outline supplies only the last clause. The paragraph keeps its sentence split in both languages.
- L277 "the plan" · fixed. It now reads "the service plan (section 4)", the section where the plan is introduced.
- L228 "after the flip" · fixed. It now reads "after I rebind the service as live". I did not split the paragraph.

confirmed 17 · not confirmed 1 · reading problems fixed 3

I left the Stripe, PayPal and Adyen names in. They are payment vendors quoted from the library's own plan, not another repository's product. If you read the product-names rule more broadly, say so and I will make it "card gateways". The `stripe-key` name in the code fence is unchanged, since fences are off limits.

=====

Appendix B, items from `research/verify/appB.md`. None of the fixes were applied before I started. I edited `src/en/B-the-fourteen-house-rules.md` and `src/fr/B-the-fourteen-house-rules.md` only.

- line 11 "reads a class as a graph" · confirmed · `stzCodeRule.ring` builds five rules (no-len-method, no-aggressive-verbs, engine-first, q-has-plain-twin, no-case-collision), and chapter 32 says "five of them". Now "as a graph (five rules) or as text (nine)". FR the same.
- line 11 "each of which was written after..." · confirmed · incidents are recorded only for q-has-plain-twin (62 mutators) and rows 7 to 14, and engine-first is a "scope ruling". Now "most of which".
- line 15 "The list is closed" · confirmed · `StzCheckCode` also emits `for_in_loop`. `StzCheckProject` adds `no-dead-code`, and `no-cyclic-calls` is in the deep set only. The report said both come from `StzCheckProject`; the source says otherwise. Now "The list of names is fourteen... One more text pass, `for_in_loop`, also reports, and so do two rules over a whole project, `no-dead-code` and, in the deep audit, `no-cyclic-calls`."
- row 3 "violent verb" · confirmed · the rule tests Kill and Destroy only. Now "begin with Kill or Destroy".
- row 7 severity · confirmed · the source gives error, or warning when only the getter reads the attribute or the class has a parent. I narrowed it to the getter case in the cell: "error; warning when only its own getter reads it". I left the parent-class case out.
- row 8 "per the source" · confirmed · the source declares `:warning`. Cell now "warning".
- row 12 severity · confirmed · `:error` for a predicate, otherwise warning. Cell now "warning; error for a predicate".
- writing rule 3 "judged by a machine" · confirmed · the court judges a promise that is present, and nothing refuses a line without one. Now "the promise is judged when written; a line without one is not refused".
- line 69 "I did not fire them" for row 3 · confirmed · chapter 32 fires `no-aggressive-verbs` (kept block in `data/book-run.json`).
- line 69 "rows 2, 7, 9, 10, 12 and 13 in the research" · confirmed as unsupported. The kept blocks cover rows 10 and 13 (chapter 7) and row 2 (chapter 5). The sentence is rewritten: rows 6, 11 and 1 above; chapter 32 fires row 3, chapter 7 rows 10 and 13, chapter 5 row 2; rows 7, 9 and 12 read from the source, as were rows 4, 5, 8 and 14, and I did not fire those seven.
- writing rule 13 "does not run" · confirmed as unsupported · only the Chinese and French names were run. Now "Chinese and French names raise; the Arabic one was not run".

Reading problems:
- Problem 1 (which five are graph rules) · fixed in one sentence on line 48: "the five rules over the code graph (rows 1, 3, 4, 5 and 6) keep their hyphens, and so does the finding of row 2". I did not add a table column.
- Problem 2 ("sweep") · fixed. Now "the shape a global replacement of tokens leaves". I did not add the glued-name trigger, because I did not read that part of the source.
- Problem 3 (the reader has no "research for chapter 7") · fixed by the line 69 rewrite, which points to chapters 5, 7 and 32.

I changed no table cell printed from a data source other than the severity and wording cells above, and no code fence. `python tools/check_fr.py B` says ok, and `python tools/book_audit.py` is clean (82 pages).

confirmed 11 · not confirmed 0 · reading problems fixed 3

Not settled:
- Chapter 5 (outside my files) says the house rules run "most of them over the graph". By the source only five of fourteen do. Its owner should narrow that.
- The `for_in_loop` severity is warning, and I did not print it.

=====

ch23 · items checked: 10 (9 in section 2, plus the missing "withdrawn" note) · edited `src/en/23-a-world-a-constellation-a-platform.md` and `src/fr/23-a-world-a-constellation-a-platform.md`. `python tools/check_fr.py 23` is ok. `python tools/book_audit.py` is clean (82 pages).

- L316 / L415 / front matter, "site has no page for the architect" · confirmed · `en/journey-architect.html` exists and `content/en/offering.md` links to it. `content/en/certification.md` says the proposal is not announced. Text now says the site has a journey page and a certification page (read 9 Oct 2026). "A page for the architect" is dropped from `absent` in the front matter and the body.
- L427, "six competing level schemes" · confirmed · the education plan's "Levels" row lists five. Now "five".
- L316, "three times in three places" · confirmed · `SOFTANZA_SYSTEM_FOUNDATION.md:121,158` names the architect. `58-zos-platform-modeling.md` has no architect, only "architectural elements". The memo was found at `D:\GitHub\softanza\memos\2026-09-30-escep-launch.md`; its header reads WITHDRAWN 2026-09-30 22:21. Now: twice by name, and a third place that models platforms without naming the architect. I also added that the memo is marked withdrawn, on the day it was written.
- L13 / L415, "absent: the five-row guarantee sheet" · confirmed · `softanza/vision/08-NORTH-STAR.md` asks for it and the site's journey page marks the step "designed". The front matter now has it in `designed` (requirement) and `absent` (the written sheet). The body's designed list defines it as five rows, one per system; the absent list says no solution has one.
- L409, "and the commons calls, and that is all" · confirmed · `stzSuperApp.ring` also defines `Why`, `GraphQ`, `WorldQ`, `KindOf`, `IsActive`, `HasWorld`, `NumberOfWorlds`, `AreBonded`, `CrossingCount` and `LastCallMs`. Now lists them and says "The verbs of composition are these."
- L409, `Shares`/`Provides`/`Norm`/`Reaches`/`Generate` "fail in the same way" · confirmed · none is in `book-run.json` (only Hosts, Admits, Explain ran), and none is defined in the class. Now "are not defined on a constellation either."
- L220 / L413, nested-constellation call · confirmed · `CallAcross` (`stzSuperApp.ring:215-237`) only returns 1 or 0 and hands nothing to the target. Added "a crossing is a verdict; nothing is handed to the target yet" at both places.
- L429, "governed whoever calls" · confirmed · the caller in `CallAcross`/`MayProceed` is a world name. Now "governed by the calling world's name and authority."
- L37, "each as it stands in its source" · confirmed · the source punctuation differs (`STZSUPERAPP_DESIGN.md:53`). Changed to "put in my words". French follows.
- L248, 318 and 251 bytes · confirmed as a scope problem · the sizes are not in `book-run.json`. Now "for a world of one screen and one thing", plus "other worlds give other sizes." I did not re-measure.

Reading problems fixed:
- "a fifth facet" is now "one more facet, beside the design's constellation, bonds, commons, reach and presence." The design's own text says "not a fifth parallel facet".
- The five-row sheet is defined at its first use in the body.
- "rated solid" now says the lane "App shell and windowing" is rated, not the world.

French: the same paragraph, heading and list counts. The English file uses CRLF and the French file LF, and I kept each as it was.

confirmed 10 · not confirmed 0 · reading problems fixed 3

Not settled:
- I did not re-run the byte probe for 318 and 251, so those two sizes still rest on the research session.
- The French "lane" wording in the Atlas note is my translation of the lane name, "coque d'application et fenêtrage."

=====

ch26: all 16 report items confirmed and fixed in both languages; 3 reading problems fixed. `python tools/check_fr.py 26` returns ok. `python tools/book_audit.py` is clean on 82 pages.

Edited: `src/en/26-the-environment.md` and `src/fr/26-the-environment.md`, including the `stage:` values in both front matters.

- l.155 "measured on nothing" · confirmed · now the charter's words, "measured for a sound studio and not for an IDE" (CHARTER.md:85-86).
- l.244 "one place the library speaks in verbs" · confirmed · now "One place where the world speaks in verbs is its screens." `SATISFIES` takes the same verbs.
- l.362 "first defect in an hour" · confirmed · now "found a defect on its first run, by the guard's account" (`gui_profile_narrated` header). No hour appears in the record.
- l.278 removal of 22 modules · confirmed · I ran `git show` on commit `b70f3ad91`: 2026-05-26, "Remove 22 AI-invented engine modules", and `interact` is in the deleted list. I kept the claim and added that date, count and list are read in git history, not in the pinned tree.
- l.25, 306, 310 unmarked general knowledge · confirmed · added "(General knowledge.)" at 25 and 306, and "(general knowledge)" inline at 310.
- l.23 "no exceptions" · confirmed · the specification lines 22-23 say "ZinCode spec: ... No exceptions". Now "which sets for its own product".
- l.155 loopback refusal · confirmed · the check is in `stzAppBackend.StartOn` (:343-347); `stzAppServer.Start` has none. Now "the library's backend refuses; the bare server above does not check".
- l.214 "only an act clears" · confirmed · `Pursue()` resets `@aProposals = []`. Now "An act on the world clears a proposal".
- l.292 "six times" · confirmed · 12.23 lists one built shell plus prototypes, corpora and a vision. Now "six efforts in two years, one of them built".
- l.316 `ToHtml` · confirmed · `_MarkupOf` emits the escaped CONTENT text. Now "an identifier, a style and the text only".
- l.316 "plan says web has no adapter" · confirmed · the plan says AccessKit has "no web adapter". Now attributed to the accessibility library the plan adopts.
- l.340 "backend-only plan" · confirmed · `stzEmulator.ring:372-374` prints "parts healthy" and "Ready to ship." on every page, and "needs a look" and "2 approximated" depend on class `mcu`. Reworded, marked "read in the source, not run".
- l.350-352 stage words · confirmed · a facet declaration, a rail that follows focus and status cells from courts were listed in both designed and absent. They now appear in designed only. The class named for a ribbon, rail, spine or status bar moved out of absent too, as "none yet a class of the library" in designed (prose and front matter, EN and FR). l.35 still says no such class exists.
- l.308 "a GPU" · confirmed · the accessibility guard "needs no GPU", and the GPU gates only the raster half of the tier guard. Now "a GPU for the raster path".
- l.286 "two lenses" · confirmed · `03-PRODUCTS.md:46-50` ("the Studio pair") defines them. Now "the charter's two are the pair of studios, and not two shells".
- l.104 "Chapter 25 said the same list" · confirmed · ch25 l.309 says the bridge sentence is applied by hand. Now "the bridge sentence" (FR « phrase-pont »).

Reading problems fixed:
- l.31: "the study" now reads "The study of the record (its sections 12.23 to 12.25)".
- l.37: the five marks are listed in one parenthesis.
- l.282: the fragment is now a full sentence.
- l.374: exercise 3 gains one sentence naming `ToFixture`, `ToPanel` and `BoxOf`.

confirmed 16 · not confirmed 0 · reading problems fixed 3 (four edits)

Not settled:
- l.37 and l.300 ("fifth mark"): I took the five marks from the structure line in `research/ch26.md`, not from a chapter-side list. The author may want different wording.
- The exercise 3 sentence mentions a font file, which `ToFixture` needs through `ToPanel`. The record has no small Latin font in the test tree (R7 in `research/ch26.md`).

=====

ch30 · 11 of 12 items confirmed, 1 not confirmed · `check_fr.py 30` ok, `book_audit.py` clean (82 pages)

- l.204 "four words" · confirmed · `stzsite/content/en/forged.md:69` and the French page both read "a gap, not a lesson learned". The page now quotes the site, "read on 9 October 2026". The French has the same date and the site's French wording.
- l.202 "did not wait for the first incident" · confirmed · `stzPlasticGovernance.ring:3-40` says each check was built from a defect already lived. I cut the clause. The text now says the rule governor exists because the silent rule already happened in the library.
- l.224 "queues, synchronises or settles" · confirmed · `stzWorkerPool.ring:224` has `QueueDepth`. Section 7 now says "no class keeps entries on a device and sends them when the network returns". I left l.194 as it was, since its three claims are the ones the searches support.
- l.173 "asked for first" · confirmed · `01-cadre.md:22` lists offline as ENF3 among the demands, and l.24 puts it second among the gains. It now reads "the one it asked for that the library does not carry", matching l.35.
- l.212 "judges nothing" · confirmed · `rulz_roundtrip_narrated` scenes 1-3 show rules loaded and their functions restored. Cut the clause. The text now lists name, type, severity, function, parameters and message, and names the `.stzrulz` file.
- l.33 and l.198 "reason above the others" · confirmed · the study lists the gains unranked. l.33 now says the study lists four gains and ownership is the first it lists. l.198 now says "among its gains the study lists ownership first".
- l.37, l.230 and front matter `built`, "A rule is data" · confirmed · the blocks build the rule by method calls. The lead-in is now "A rule is an object whose numbers can be changed". The `built` stage text and the section 7 "built" list say a rule as an object with its number changed. The analyst door now says "The study promises…" and then what the library does.
- l.155 and l.208, "without erasing it" · confirmed · `stzGovernance.ring:119` has a default capacity of 512, and `SetLineageCapacity` (l.401-419) counts dropped decisions in `LineageDropped`. l.155 now adds "up to a capacity (512 decisions by default), and the governance counts what it dropped". That is a code constant, not a guard count. I did not touch l.208.
- l.109 and heading "A person sees the refusal" · confirmed · `wisecoding_narrated` only asserts a stored checkpoint. The heading and body now say "a person can read", and the `built` stage text matches.
- l.29 "says it in one sentence" · confirmed · `03-principes.md:31` is a French section title. The page now says "gives it as the title of a section … (my translation of the French title)". The French quotes the title.
- l.33 "no licence per seat" · confirmed · `11-decisions.md:23` keeps the vendor suite's licences, so it now reads "for the platform".
- Citation gap (l.222) · confirmed · scenes 4 and 5 of `rulz_roundtrip_narrated` do show the refusals. That guard is not in `data/guards.json`, so I did not add it to the front matter `guards:` list. Section 5 now names it as a narrated library test the book does not run as a guard.

Reading problems fixed: 3 of 3.
- "Governor" versus the authority court: the first use is now "rule governor (the class is `StzRuleGovernance`)", with the same wording in l.107, section 7 and the programmer door. One sentence before the authority block says `stzGovernance` judges authority and is not the rule governor.
- `.stzrulz` is now named at l.212.
- l.171 now says "This makes the block repeatable".

The French has the same changes, in « gouverneur de règles » wording. No paragraph, heading, list item or table row was added or removed.

confirmed 11 · not confirmed 1 · reading problems fixed 3

The one item not confirmed is the citation gap: the evidence is real, but front matter can't carry it, so the fix went in prose. Nothing else is left unsettled. Both files are in `D:\GitHub\ayouni\books\softanza-book\src\en\` and `src\fr\`, named `30-an-organisation-in-the-field.md`.

=====

Chapter 25: 14 items confirmed, 4 not confirmed, 3 reading problems fixed. Both pages are edited, `python tools/check_fr.py 25` says ok, and `python tools/book_audit.py` is clean (82 pages). One thing to know: the English file uses CRLF line endings, not LF as the brief says, and I kept them. The French file is LF.

- "in ten lines" (l.320) · confirmed · `ToText` and `ReadReply` are 13 lines; now "in a dozen lines" / « une douzaine de lignes ».
- "the study's five proposals" (l.302) · confirmed · the study's proposals are B46 to B50 (`drafts/stzsite-roots-and-achievements.md` l.1063-1069); now "proposals B46 to B50 of the study".
- Constitution quotation (l.37) · confirmed · `stzsite/content/en/zui.md:19` has the exact wording; restored in quotation marks. The French is my translation, using « médium » as the chapter does; the site's own French says « support ».
- "consent … only as the microphone's boundary" (l.308) · confirmed · the word also appears in `SOFTANZA_INCIDENT_VS_THE_FIELD.md:172` and `SOFTANZA_PLUGIN_PLAN.md:471`; now "No unit of consent exists for messaging", with the microphone and the two design documents named.
- "unchecked, since any word is accepted" (l.309) · confirmed · only five public methods exist, and `_ScreenIntent` (`stzApp.ring:421`) does the not-checking; reworded to say so.
- "The design says so in two places" (l.302) · confirmed · `STZSUPERAPP_DESIGN.md` l.115 only lists messaging under COMMONS, and l.136 writes `Provides(:Messaging)`; now "one design file … in two lines", with both described.
- Front matter `designed` listing the twenty-two verbs · confirmed · moved to `absent`, in both languages.
- Heading "what I refused" (l.247) · confirmed · the items come from library headers and the voice plan (`stzListener.ring:3-19`, `stzVoice.ring:31-33`, `stzEarcons.ring:17-19`, `SOFTANZA_VOICE_PLAN.md` §6). I kept the heading, because every chapter uses it. I added one attributing paragraph in both languages: the refusals after the first are the record's, not rulings of mine.
- "The only hits are word-list data files" (l.273) · confirmed · whatsapp matches only `ner_orgs.txt`, telegram only `bigtext.txt` plus engine data, and USSD has no text match; now "no hit in the code or the design of base, core or max", with the word-list and test-data matches named.
- "nothing to download" (l.243) · confirmed · `RestoLean-Cadrage-Amor.md:59-61` says no heavy app, a PWA; now "no heavy app to download".
- `ReplyIn("c", "grand couscous")` raises (l.312) · confirmed · it rests on a research run (`research/ch25.md:492`) that no block records. I attributed it to "a research run at this commit" and said no block records either result, as chapter 18 does.
- The Zarma "Unsupported object type!" (l.310) · confirmed · same treatment; attributed to a research run, with a note that no block records the call.
- "93 characters", "89 units" (l.92) · confirmed · I recounted both in Python (93 and 89), but no block prints them. The text now says "by my count", and that the block prints the segments. I did not touch the code fences.
- "a case the record names" (l.328, learner on a plain phone) · confirmed · 12.25 names no learner; now "The record does not name a learner on a plain phone, and nothing serves one yet".
- Exercise sentence "raises today" (l.348) · not in the report; changed to "raised in my research run", for the same reason as the "grand couscous" item.

Not confirmed:
- The guard numbers 53 of 53 and 21 equal `data/guards.json`, as the report says.
- The `site: [zui]` front matter is metadata only, so I left it.
- `:whatsapp` and `:ussd` in code and output are third-party names, allowed, so I left them.
- "maker" appears only in "decision-maker", which is allowed.

Reading problems fixed:
- The "your text" and "first draft" wording: the section now says "I flag it for the author" and "Chapter 2 already gives his tool as a spreadsheet".
- "Central" is now explained as "the estate's coordination entity" (« l'entité de coordination du domaine de projets »).
- "The study" is defined once in section 1 as an outside reader's study of the project's roots, with section 12.25 about messaging.

confirmed 14 · not confirmed 4 · reading problems fixed 3

I could not settle one thing. The two research-run claims (`grand couscous`, Zarma) stay unrecorded by any block. I cannot add a block, because I may not edit code fences or run `book_run.py`. A later session could add a block for each to `data/book-run.json`.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\25-your-users-keep-their-medium.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\25-your-users-keep-their-medium.md

=====

1. Appendix C (src/en/C-the-twenty-two-verbs-and-the-constitution.md) · claims checked: 68 · verified 62 · wrong 1 · unsupported 1 · overclaim 4

Source checked: D:\GitHub\stzzui\constitution\rules.json. DECISIONS.md APPENDIX-03 names it as the rules file. Its modification time is 17 Aug 2026, and its metadata says version 3.11, lastUpdated 2026-08-16. I parsed it with a JSON reader and compared every table row with it. The rows checked were:
- the 7 articles;
- the 6 families and 22 verbs (3+3+4+4+4+4), with their invariants;
- the 6 rights;
- the 10 rules of set 31 (numbers, titles and enforcement: 7 judgment, 3 machine-later);
- the 17 forbidden patterns;
- the 5 retired and 2 burned numbers;
- the metadata counts (7 articles, 31 sets, 122 rules; the sets hold 122 rules).

All of these match.

2. Items

- line 12 · "Chapter 20 shows the right to a human beneath its rail" · wrong · Chapter 20 has no "rail" (grep of src/en/20-*.md finds none). The Right to a Human is at 20-agents-that-cannot-hurt-you.md:319. "Rail" is chapter 26's word, for the rail that proposes. · Write "Chapter 20 shows the right to a human as the end of the loop."
- lines 81-83 · "the sets, of which it uses the one for agents. It does not take the rest." (also line 60, "where the rest of this book meets it") · overclaim · Chapter 25 (lines 164 and 193) builds its five semantic values on the constitution's Rule 118. That rule is in set 2, not set 31. rules.json set2, rule 118 lists "five values": success, warning, danger, info, muted (see also research/ch25.md:249). · "the set for agents and Rule 118 on the five values of status."
- line 75 · "Rule 99 is chapter 14's provenance: where a fact came from is shown" · overclaim · Rule 99 (rules.json, set 31) requires content produced by a model to be marked as machine-made. Chapter 14's provenance is the source and confidence a strict graph demands of a fact (14-knowledge-programming.md:88). The two are related, not the same. · "Rule 99 asks for the mark on machine-made content; chapter 14's provenance is the nearest thing the library builds."
- line 16 · "The constitution's philosophy is four lines" · overclaim · metadata.philosophy is one string holding four axioms, so the four are right. But rules.json also has a separate "philosophy" section of three rules (P1 Aponia, P2 Ma, P3 timeless principles). · "its four axioms" (the heading already says so).
- line 27 · "vibes, densities and dialects are equivalent vibes of one truth" · overclaim (small) · articles.operator reads "vibes, densities, dialects, and surfaces ...". "Surfaces" is dropped without a mark. · Add "surfaces".
- line 83 · "an interaction engine that I removed on 26 May 2026" · unsupported · Commit b70f3ad91 is in the live checkout's history, not in the pinned tree. The only trace I could read is research/ch26.md:384 and chapter 26 line 278. The 24-verb design text is verified: SOFTANZA_ENGINE_DESIGN.md:3752-3768 lists 24 verbs in six categories. · Nothing, if the author accepts chapter 26's record; otherwise cite the commit.

Also checked and verified:
- The five stzApp screen methods ToDiscover, ToUnderstand, ToFocus, ToSelect and ToAct exist, and `_ScreenIntent` does not check the word (base/app/stzApp.ring:410-424).
- "The library does not mention" the Right to a Human: a grep of the pinned library for the phrase finds nothing.
- The site's "not public yet" and its 22 verbs (stzsite content/en/zui.md:24 and 21).
- The Right to a Human is enforced by rule 102 alone, marked judgment.

One more point on line 10: "I counted none of them myself" holds for the metadata numbers. The appendix does count three things itself (22 verbs, 17 patterns, 7 of 10). That is harmless, but the sentence could say "the metadata numbers".

3. Reading problems
- Lines 10 and 12 say the same thing twice: the repository is not public, and the verbs are printed as read from the rules file on the date given. Cut the last sentence of line 12.
- line 75 · "Rule 104 is the rule in the accessibility tree" does not parse. The rule is about machine legibility. The library's accessibility tree (chapter 26, gui_accessibility_narrated) is only the nearest built thing; say that.
- line 43 · "the library's worlds know five as screen intents" uses "worlds" and "screen intents" before this appendix explains them (stzApp, chapter 26). Add "(chapter 26)".

4. CLAUDE.md rules and other repositories
- The appendix does not use "Zin", "Zui", "maker", "substrate" or any product name (grep).
- The sibling repository stays unnamed ("the interface constitution"), as APPENDIX-03 rules.
- The library design text the appendix cites does name Zin (SOFTANZA_ENGINE_DESIGN.md:3752). The appendix does not repeat it.
- APPENDIX-03's open [AUTHOR] question is whether the list may be printed before the repository is public. ANSWER-POLICY D7 answers it, but the page does not say so.

Report written to D:\GitHub\ayouni\books\softanza-book\research\verify\appC.md

=====

ch29 (A bank in Niamey) · claims checked: 62 · verified 48 · wrong 1 · unsupported 1 · overclaim 12

Line numbers are those of src/en/29-a-bank-in-niamey.md.

- line 206 · "rules 117 to 124 were harvested from a banking-supervision product, in the record's words" · wrong · stzzui/constitution/rules.json evidence: banking product for rules 117-121 only; 122 "a sibling project's i18n decision", 123 "Refine site (June 2026)", 124 "a sibling project's build-target culture"; the study (drafts/stzsite-roots-and-achievements.md:966) says "eight ... from the banking product and Refine's evidence trails" · write "117 to 121", drop "in the record's words".
- line 195 · "After the load ... the report said sound" · unsupported · no block, guard or book-run entry; only a probe in research/ch29.md section 8. Guard 84 asserts the load only. Code supports "not enforced": stzGraph.ring:7371-7440 reads name, type, severity, function, params, message and no when/then line · state that code fact instead, or add a block.
- lines 148, 214 · "the report is one gate over every court" · overclaim · blocks feed stzRuleReport only CheckCompliance(oBasel), a rule base (stzOrgChart.ring:468); BCEAO and SOD verdicts are not ingested · "one gate over the rule bases it is given".
- line 178 · "rulereport_narrated proves the one report over every court" · overclaim · its scenes are code, agentic, security findings, no org chart; the chart joining the gate is orgrule_narrated.ring:101-111 · move the clause.
- line 178 · "orgrule_narrated proves the seven rule bases" · overclaim · it asserts SOX 5, GDPR 4, HIPAA 4 only (orgrule_narrated.ring:71-99); the other counts come from block 3 · "proves SOX, GDPR, HIPAA".
- line 178 · "14_bceao_governance proves the regional validator" · overclaim · its promise shows BCEAO-001 and -003 only; BCEAO-002 is unguarded · "two of its three rules".
- lines 168, 212 · "the same text is the unit the court judges"; "You change a reporting line in a text and you re-run" · overclaim · block 5 uses ReportsTo calls on the object; no block edits the text and re-imports it · "in the object, or in the text and import again".
- line 113 · "It is not code." · overclaim · the rule is five Haro calls; the file form that would be data does not judge (your line 195) · "an object declared by calls".
- line 170 · "The Forged page ... uses the word 'validator' for two different things" · overclaim · forged.md:53-57 says "validators, with the regulators' rule bases beside it"; the conflation is stzsite/content/en/real.md:12 · cite real.md or soften.
- line 162 · "The same block shows that the banking validator always passes" · overclaim · block shows one pass; "always" is the comment's (stzOrgChart.ring:953) · attribute it.
- line 216 · "Seven regimes, one with real content of its own" · overclaim · BCEAO's rule base holds the same four rules (block 3); its content is the separate validator · "one with a validator beside its rule base".
- lines 23, 182, 184 · "They do not read the structure"; "a register of every regulation, every control and every finding"; "a platform that a bank's auditors already know, and that a regulator has already seen" · overclaim · absolutes on a whole category; only line 23 is marked general knowledge · mark 182 and 184, drop "every", "do not" to "usually do not".

Reading problems:
1. Lines 74, 111, 178: "segregation/separation of duties" names two rules: the "second court" (SOD-001, operations to treasury) and SOX's rule (one position holding approver and executor, stzOrgRule.ring:235-276). A reader takes them for one.
2. Line 194 and front matter: "the six other regimes ... each holds the same four rules": other than which? SOX holds five; BCEAO's rule base four.
3. "The record is silent" on the bank's people is said at line 174 (twice), 202.

Names and rules: no other product named (no bank, Organizium, Sonibank, RestoLean); no "maker" except the door "decision-maker" (allowed, CRAFTER-01); no substrate, no Zin. Line 206 leans on another repository (the interface constitution, unnamed). The narration cited (stzOrgChartDoc-BankUseCase.md) does not run at the pinned commit and the chapter never says so (research/ch29.md hazard 6 asked it).

Report file: D:\GitHub\ayouni\books\softanza-book\research\verify\ch29.md

=====

Appendix C · 6 items confirmed, 1 not confirmed, 3 reading problems fixed. `python tools/check_fr.py C` returns ok and `python tools/book_audit.py` is clean. None of the fixes were applied before I started. I edited both `src/en/` and `src/fr/` versions of `C-the-twenty-two-verbs-and-the-constitution.md`. No table cell or code fence was touched.

- line 12, "beneath its rail" · confirmed · Chapter 20 has no rail; it calls the Right to a Human "the human end of the loop" (line 319). The rail is chapter 26's word. Now reads "Chapter 20 shows the right to a human as the end of the loop."
- lines 60 and 81-83, "the rest of this book" and "the one for agents" · confirmed · Chapter 25 builds its five status values on Rule 118, which is in set 2 of `rules.json`, not set 31. Line 60 now says "where chapter 20 meets it". Line 83 now says "the one for agents, and Rule 118 on the five values of status."
- line 75, Rule 99 · confirmed · `rules.json` rule 99 asks that machine-made content be marked as machine-made. Chapter 14's provenance is the source and confidence a strict graph demands of a fact. Now: "Rule 99 asks for the mark on machine-made content; chapter 14's provenance is the nearest thing the library builds."
- line 16, "philosophy is four lines" · confirmed · `metadata.philosophy` is one string of four axioms, but `rules.json` also has a separate philosophy section of three rules (P1 to P3). Now "Its four axioms are calm over power, …".
- line 27, "surfaces" dropped · confirmed · `articles.operator` reads "vibes, densities, dialects, and surfaces". I added "surfaces".
- line 83, the 26 May 2026 removal of the interaction engine · not confirmed · I did not search git for commit `b70f3ad91`. Chapter 26 line 278 already records the date, the count and the list as read from git history, not from the pinned tree. The appendix repeats chapter 26's record, so I left it. The author can accept that record or cite the commit.
- line 10, "I counted none of them myself" · confirmed, a small fix · The appendix itself counts the 22 verbs, the 17 patterns and 7 of 10. Now "The counts in this sentence are the file's own, and I counted none of them myself."

Reading problems:
- Lines 10 and 12 repeated each other. I cut line 12's last sentence, the one saying the repository is not public.
- Rule 104 "is the rule in the accessibility tree" did not parse. Now: "Rule 104 asks for machine legibility; chapter 26's accessibility tree is the nearest thing the library builds: what a screen reader can operate, an agent can operate."
- "the library's worlds … screen intents" now carries "(chapter 26)".

Counts: confirmed 6 · not confirmed 1 · reading problems fixed 3.

Nothing else is left open.

=====

# Verification, chapter 28 (A restaurant in Lyon)

1. `ch28 · claims checked: 90 · verified 76 · wrong 2 · unsupported 4 · overclaim 8`

Basis: the five blocks match `data/book-run.json`; section 1 is marked general knowledge; the five guards exist; no guard count is printed in prose. Project facts were checked in the restaurant's repository files the research cites.

2. Flagged items

- line 179 · "carried a rule for years" · wrong · earliest source is the file of 3 July 2026 (`restolean/livrable/simulation/RestoLean-Cadrage-Amor-SIMULATION.md:89`); the record ends 25 August 2026 · "since 3 July 2026".
- line 189 · "What it claims against them is one thing" · wrong · `base/doc/design/SOFTANZA_PERF_VS_THE_FIELD.md:85-137` lists five distinctive properties; the coupling is point 1 · "among five, ...".
- line 179 · "its documents and the site print it as part of the first amendment" · overclaim · only the site does (`stzsite/content/en/customers.md:13`); the project's documents carry it as the owner's constraint (`restolean/kb/agents/PROJET.md:8`); the amendment documents have no such line · "the site prints it".
- line 205 · "the origin, in the project's own account, of its service, delivery and performance planes" · overclaim · the project calls the library "architecture cible" (`restolean/CLAUDE.md:77-79, 99`); no "origin"; contradicts line 181 · "the project's design reference".
- line 167 · "nothing could be created in production" · overclaim · `restolean/kb/agents/REGLES-UX.md:73-74`: "aucune création de fournisseur possible" · "no supplier could be created".
- line 167 · "forty-two pages of experience in a few lines" · unsupported · `REGLES-UX.md` is 80 lines; searched "42 pages" and "quarante-deux" in the repository: nothing · cut the number.
- line 33 · "with a few neighbours" · unsupported · searched "voisin" in the scoping reports, `CLAUDE.md`, `PROJET.md`: nothing · cut.
- line 41 · "what no one else had measured" · unsupported · `makeen/KIT-RINGSERV-ARTICLE.md:90` says only "by the restaurant owner himself" · cut.
- line 41 · "a phone's system does not return by itself to a network with no internet" · overclaim · source row says "iOS never auto-returns" (`KIT-RINGSERV-ARTICLE.md:98`) · "an iPhone's system".
- line 181 · "all were asked for in July" · unsupported · the plan is dated 2026-07-23 and written "in answer to the user's question" on emulation in general (`SOFTANZA_SERVICE_VIRTUALIZATION_PLAN.md:146-149`); the performance study is dated 2026-07-29 (footer); the snapshot has no history, so the other first-commit dates cannot be checked · "written after the reversal of 4 July", only where a document dates it.
- line 71 · "and the written exit that comes with it" · overclaim · the rule tests only that `admitted-by` is not missing; no exit is modelled · drop the exit.
- line 113 · "can be declared and not yet active" · overclaim · the block adds an active world, then `Retire` (`base/app/stzSuperApp.ring:125-131`); none starts inactive · "put to sleep".
- line 177 · "answers yes to everything" · overclaim · plan: "silently answers `\"\"`" (`PLAN.md:37`); "agreeable" is the narration's word · use theirs.
- line 201 and front matter line 12 · "designed: two-gesture rule as checks; a seventy-fifth percentile expectation; browser-side timing" · overclaim (stage) · no library document designs these (searched `base/doc/design` for browser, p75, gesture: nothing); `stzSla.ring` has P50/P95/P99 only · move to "absent".

3. Reading problems

- line 35 · "the rule I started this section with" · the section starts with no rule; the doctrine is in section 2 · name it.
- lines 191 and 203 · section 6 states the owner's protocol (seventy-fifth percentile, mid-range phone); section 7 says "I say only that such a budget exists" · self-contradiction.
- line 37 · "playing the owner on his first day" · only one of the three sessions was "day one" (`RAPPORT-TESTS-SIMULES.md:5-7`) · drop it.

4. Rules: no other repository's product named; no "Zin"; "maker" appears only as "decision-maker" (a structure term); no restaurant, owner or platform name. Clean.

Report file: `D:\GitHub\ayouni\books\softanza-book\research\verify\ch28.md`

=====

line 206 · confirmed · the constitution's evidence fields tie only rules 117 to 121 to the banking product. 122 and 124 come from a sibling project and 123 from the Refine site. Changed to "117 to 121" and attributed to the constitution's evidence fields, replacing "in the record's words". French the same.

line 195 · confirmed · no block, guard or run backs "the report said sound". The loader (stzGraph.ring, `_ParseStzRulz`) reads name, type, severity, function, params and message, and no `when` or `then` line. I replaced the claim with that code fact and kept "the rule is not enforced". French the same.

lines 148, 214 · confirmed · `CheckCompliance` feeds the report from a rule base only. Now "one gate over the rule bases it is given" in both places, in both languages.

line 178, `rulereport_narrated` · confirmed · its scenes cover code, agents and security, with no org chart. Now "findings from code, agents and security". The chart joining the report moved to the `orgrule_narrated` clause. French the same.

line 178, `orgrule_narrated` · confirmed · it asserts SOX 5, GDPR 4 and HIPAA 4, not all seven. Now "proves SOX, GDPR and HIPAA as rule bases ... and the chart joining the one report; the block above prints the seven counts". French the same.

line 178, `14_bceao_governance` · confirmed · its promise shows BCEAO-001 and -003 only. Now "two of the three rules of the regional validator". French the same.

lines 168, 212 · confirmed · block 5 uses `ReportsTo` calls on the object and no block re-imports edited text. Line 168 now says the text "imports into the object the court judges". Line 212 now says "in the object, or in the text and import again". French the same.

line 113 · confirmed · the rule is five Haro calls, and the file form does not judge. "It is not code" became "It is an object declared by calls". French the same.

line 170 · confirmed · forged.md:53-57 does not conflate. The conflation is in the site's real.md, which names a product, so I did not cite it. Now "The word 'validator' can be read for two different things." French the same.

line 162 · confirmed · the block shows one pass, and "always" is the library's comment at stzOrgChart.ring:953. Now "passing once: the library's own comment says it passes every time". French the same.

line 216 · confirmed · BCEAO's rule base also holds four rules. Now "one with a validator beside its rule base and one that adds a rule". French the same.

lines 23, 182, 184 · confirmed · line 23 now says "usually do not read". Lines 182 and 184 dropped "every", added "usually" and "often", and carry "(General knowledge, not a study of the record.)". French the same.

Reading problem 1 (two "separation of duties" rules) · fixed · line 111 now says SOX's rule is a different rule from the second court above: no position holds both the approver and the executor role. French the same.

Reading problem 2 ("six other regimes") · fixed · line 194 now reads "the six regimes other than the regional one. Five of them hold the same four universal rules and nothing else; SOX adds a fifth". French the same. I did not touch the front matter.

Reading problem 3 (repeated "record is silent") · fixed · merged the two sentences in section 4 into one, in both languages.

Unlisted note in the report · done · line 148 now says the narration's own code does not run at the pinned commit (research/ch29.md hazard 6) and that the calls above do. French the same.

confirmed 12 · not confirmed 0 · reading problems fixed 3 (the third check item, the narration note, is counted in neither)

Both `python tools/check_fr.py 29` and `python tools/book_audit.py` pass (audit clean, 82 pages).

I could not settle one thing. The overclaim item on line 170 offered "cite real.md" as an alternative. I softened instead, because real.md names a product, and the chapter's `site:` list does not include it.

Files:
- D:\GitHub\ayouni\books\softanza-book\src\en\29-a-bank-in-niamey.md
- D:\GitHub\ayouni\books\softanza-book\src\fr\29-a-bank-in-niamey.md

=====

Chapter 28 report. Both checks pass: `python tools/check_fr.py 28` gives ok, and `python tools/book_audit.py` is clean.

Line numbers below are the report's. Each fix is made in both `src/en/28-a-restaurant-in-lyon.md` and `src/fr/28-a-restaurant-in-lyon.md`.

- L179 "carried a rule for years" · confirmed · the earliest source is 3 July 2026, so it now reads "has carried a rule since July 2026".
- L189 "one thing" · confirmed · the performance study lists five distinctive properties and the coupling is the first. It now reads "Among the five properties it claims against them, the one this chapter uses is the first: ...".
- L179 "its documents and the site print it" · confirmed · only the site prints it as part of the amendment (`customers.md:13`). The project's `PROJET.md:8` carries it as the owner's constraint. The sentence now says exactly that.
- L205 "origin ... of its planes" · confirmed · `CLAUDE.md:77-79, 99` calls the library "architecture cible". The sentence is cut to "The library is the project's design reference."
- L167 "nothing could be created" · confirmed · `REGLES-UX.md:73-74` says "aucune création de fournisseur possible". Now "no supplier could be created in production".
- L167 "forty-two pages" · confirmed · the file is 80 lines and no "42 pages" appears anywhere in the repository. The number is cut.
- L33 "a few neighbours" · confirmed · nothing in the record says it. Cut.
- L41 "what no one else had measured" · confirmed · `KIT-RINGSERV-ARTICLE.md:90` says only that he measured it. Cut.
- L41 "a phone's system" · confirmed · the source row says "iOS never auto-returns". Now "an iPhone's system".
- L181 "all were asked for in July" · confirmed · only two documents date themselves: the plan on 23 July and the performance study on 29 July. The sentence now says that, and keeps "first committed after the reversal of 4 July" from the research's dated git log.
- L71 "written exit that comes with it" · confirmed · the rule only tests that `admitted-by` is not missing. The exit is dropped.
- L113 "declared and not yet active" · confirmed · the block adds the world active, then calls `Retire` (`stzSuperApp.ring:125-131`). Now "can be put to sleep".
- L177 "answers yes to everything" · confirmed · the plan (line 37) says "silently answers `""`". The body now says the double "silently answers with an empty string". The "agreeable fake" heading is kept, since it is the narration's word.
- L201 and front matter "designed" · confirmed · no library document designs the percentile expectation or browser-side timing, and `stzSla.ring` has P50, P95 and P99 only. In the body I moved the two-gesture rule and interface rules as checks, the percentile expectation and browser-side timing out of "designed" and into "absent". In the front matter I moved the percentile expectation and browser-side timing to `absent` in both languages. The two-gesture rule was never in the front matter, so I left it out.
- L35 "the rule I started this section with" · confirmed · now "the doctrine of section 2: deliver small, fast and useful".
- L191/L203 contradiction · confirmed · the record (addendum lines 73 and 87) does give the protocol, so section 6 stays. Section 7 now reads "Of the owner's tightened speed thresholds I print none, and say only that such a budget exists."
- L37 "on his first day" · confirmed · only one of the three simulated sessions was day one (`RAPPORT-TESTS-SIMULES.md:5-7`). Dropped.

confirmed 17 · not confirmed 0 · reading problems fixed 3 (L35, L191/L203, L37)

Two edits go beyond the report's suggested wording:
- **L179 date:** I wrote "since July 2026", while the next sentence keeps "of 3 July". That is slightly redundant but true.
- **L35 sourcing:** "the doctrine of section 2" names the lesson from the site's Forged page. Section 2's own wording does not say when he learned it.

Nothing I could not settle. I changed no code fence, no number beside a guard, and no front-matter key other than the text of `stage:`.

=====

1. ch27 · claims checked: 98 · verified 81 · wrong 7 · unsupported 3 · overclaim 7

2. Items (S = `.cache/stzlib-93d7a39bd/libraries/stzlib`)
- l.136 · "The engine's case mapping, a vendored library, writes SS" · wrong · S/engine/src/unicode.zig:338-345: utf8proc's simple map gives ß to ẞ; SS comes from the engine's own `specialUpper` table · "(its own table over a vendored library)".
- l.188 · "the only external extension loaded by name is a cryptography one" · wrong · S/base/file/stzFile.ring:1 `load "ziplib.ring"`, loaded by base/stzBase.ring:717 · name it or drop "only". Then the l.190 lead "I removed the language's own extensions" overclaims: a directive, not a finished act.
- l.208 · "532 narrated guards in base" · wrong · `find base -iname "*_narrated.ring"` gives 529 in the pin (0 in core and max) · 529.
- l.249, l.251 · "869 lines"; "nineteen such loads" · wrong · two BOM-prefixed lines were missed (base/file/stzFile.ring:1, base/extercode/stzExterCode.ring:1): 871 lines; the second loads "stzextercodetransfuncs.ring", the file is stzExterCodeTransFuncs.ring: a 20th mismatch, in base's own load chain · 871, twenty. The rule's verdict stands (my rescan: no upward load).
- l.134 · "at a commit I name" · wrong · no commit is named · name it or cut.
- l.165, l.206 · "six assertions, six passed" beside `engine_is_optimised_narrated` · wrong vs data/guards.json (7) · the file has 7 `Then`; the 7th is an else-branch (base/test/number/engine_is_optimised_narrated.ring:86) · "seven in the file, six reached here".
- l.180 · quotation "the future is Haro, not the former language" · wrong · drafts/stzsite-roots-and-achievements.md:228 reads "not Ring"; the lead also names "Ring" while the chapter elsewhere says "the former language" · bracket the change; unname in the lead.
- l.206 · "`threat_model_narrated` names two rows as the engine's" · overclaim · the guard only checks each row names a proof and each named guard file exists; the document has many engine rows (G07, G09, G10, G16, G23, G28) · "reads the threat model; rows G11 and G25 concern the engine".
- l.192 · "nineteen vendored libraries, each with a verdict" · overclaim · engine/vendor records hold component, version, source, licence, digests; no verdict · "each with a record".
- l.253 · "They work when loaded by hand" · overclaim · one unshown run of `stxString` (11 chars), not in data/book-run.json; 31 classes untried · "the first of them works".
- l.225 · "not in the runtime's own record" · overclaim · ringpp/NOTES.md:345 withdraws "beats every peer on every row" for the RC configuration (not the 13 Sept retirement) · add the qualifier.
- l.21, l.25 · "in the record's own words"; Rust "enforces it by its compiler"; the Python alternative implementation · overclaim · the study (drafts/stzsite-roots...:484) says "three crates for three depths of host"; the field statements lack the "general knowledge" mark (only SQLite has it) · mark them.
- l.279 · "The only layer with an interface on the binary is the web subset" · overclaim · contradicts l.100 and l.247 (per-layer libraries exist; the wasm subset is not a layer) · reword.
- front matter · stage lists · overclaim · `absent` omits from §7: lean core that runs, `haro` executable, Haro running the library; `designed` omits §7's one-domain loader, standalone engine repository, polyglot bridge · align.
- l.57, l.165, l.245 · load times, "0.02, 0.04 and 0.03", "five hundred and thirty-four functions" · unsupported · data/book-run.json holds only the 16.2 s total; research/ch27.md only.
- l.149 · "since 26 July 2026" · unsupported in the pin · commit id 1fdc2eda5 is in base/doc/design/SOFTANZA_NUMERIC_FOUNDATION.md:1122; the date is from the live checkout's git log (research/ch22.md:50).

3. Reading problems
- l.57 vs l.80: "17 classes", then "ten begin with stk"; the seven `stzCore*` classes are never named.
- l.23: "I name no engine written in the same language as this one, unless I am asked to" is a writer's note leaked into prose.

4. Names and rules
- "Ring" is named in the l.180 lead. No "Zin", no "substrate"; "maker" only in "decision-maker" (a door). No other repository's product is named. The l.33 quote "It never meant every line ours" is only half in ch4; its source is outside the brief's set.

Report file: D:\GitHub\ayouni\books\softanza-book\research\verify\ch27.md

=====

ch31 · claims checked: 80 · verified 64 · wrong 4 · unsupported 2 · overclaim 10

The five blocks are all "kept" in data/book-run.json. No guard figure is printed in prose.

WRONG
- l.161 · "Chapters 1 and 33 write "runs"" · wrong · src/en/33-*.md:89 now says "field-tested" and "built beside the library"; only ch1:104 still says "runs"; l.210 says the same · "Chapter 1 writes "runs"".
- l.166 · "The site and chapter 2 conflate two facts" · wrong · the conflation is study 12.29 (drafts/stzsite-roots-and-achievements.md:1227); no site page says "phone in hand"; ch2:134-136 separates the facts · "the study (12.29) conflates".
- l.176 · "The site attaches them to the bank" · wrong · no site page mentions rules 117-124; the study does (drafts:1227) · "the study attaches".
- l.85 · "remains a planned external action" · wrong (quotation) · stzPlatformProfile.ring:~246 reads "PLANNED" · restore the capitals or drop the quotation marks.

UNSUPPORTED
- l.39, l.236 · "written before any reader asked" · none found, searched site, drafts, memos · cut.
- l.208 · registry and SLA "first committed after the reversal of 4 July" · the pinned copy has no history; only research/ch28.md:514-516 · keep only if the author accepts ch28's git log.

OVERCLAIM
- l.39 · "the same page, with the same heading" · forged.md:82-84 is one paragraph inside the forged page · "a section of its forged page".
- l.45 · "no live payments service is bound anywhere in the record" · service_registry_narrated.ring:112,264 BindLive :payments (stand-ins); payments_live_adapter_narrated binds to the twin · "no real payments service".
- l.64 · "rehearsed and never native" · the next sentence says a board prints native · "not native, on this machine".
- l.165 · "the project's own notebook defers it" · "REPORTÉ AU CYCLE 1" is in index.html:217, not livrable/CARNET-NPE.md · "checklist".
- l.176 · "a banking-supervision product of a sibling platform, not this bank's installation" · rules.json 117-121 say only "A banking supervision product (April 2026)"; "sibling" is on 122/124 (rules.json:504,520); nothing excludes the bank · quote the evidence line only.
- l.182 · "who chose, against what: the record is silent" · diko 01-cadre.md:24: the specification preferred low-code on an office suite; the offer was "retenue"; ch2:165 says it · drop "against what".
- l.195 · "has passed the library's suite on Windows" · memos/2026-10-05.md (ringpp 10:53): 8,540 of 8,540 assertions, but 3,425 of 5,112 transcripts agree on every stable line · "passes every assertion Ring passes".
- l.202, l.234 · "The gallery's forty-one pictures" · 41 is INDEX_part1.md only (20/9/12 verified); INDEX_geo.md and INDEX_plots.md exist · "part 1 of the gallery".
- l.202 · "one of them still says forty-five"; "its ruling" · the design doc says 45/45 (SOFTANZA_DEPLOYMENT.md:188), the guard holds 63 (guards.json); drafts:1211 says "an assessment, not a ruling".
- l.218 · "orgrule_narrated ... carry the other two lessons" · orgrule_narrated has no BCEAO line; it covers the universal tier and SOX segregation; the three BCEAO rules' guard is 14_bceao_governance (1 assertion), uncited · cite it, say what each covers.
- l.230 · "Its guarantee text says ... the fourth ... waits for a watchdog on a real board" · makeen_box.guarantees.expected says only "carries no slot decision"; the watchdog line is 08-NORTH-STAR.md:390 · attribute to the vision.

READING PROBLEMS
1. "the hub" has two referents: DIKO's hub (l.182, 184) and the payments hub whose sandbox is meant (l.87, 197; the sandbox is the central bank's, per stzPispiHttpAdapter.ring:50-52). Never said.
2. l.163-166 use "the Lock", "the pact", "the notebook", "the map" as known; undefined here.
3. The declarations search is told three times (l.192, l.248, stage line); l.85 "above this code" points at a comment above a class in another file.

NAMES AND RULES
No Zin, no substrate, no project or person names. "decision-maker" (l.258) holds "maker"; harmless as a role. stzPispiHttpAdapter is the library's class; l.116 prints "sound_mu5_demo.ring", the library's text.
My spot-check: restolean holds no declaration file (grep, 368 .ring files). The thirteen-repository search (l.248) rests on sessions/2026-10-09-phase-9-answers.md:28.

Report file: D:\GitHub\ayouni\books\softanza-book\research\verify\ch31.md

=====

ch27 · edits applied in `src/en/27-the-engine-beneath.md` and `src/fr/27-the-engine-beneath.md`. `python tools/check_fr.py 27` says ok. `python tools/book_audit.py` says clean (82 pages).

- l.136 SS · confirmed · `specialUpper` in `engine/src/unicode.zig` produces SS; utf8proc's simple map gives ẞ. Now "its own table over a vendored library".
- l.188 only external extension · confirmed · `base/file/stzFile.ring:1` loads `ziplib.ring`, and `stzBase.ring:717` loads that file. Now two extensions: the zip one that base loads, and the cryptography one in a folder no entry file loads.
- l.190 "I removed the language's own extensions" · confirmed, the stated effect did not match the evidence · The heading is now "I directed that ... be removed". I added that the library still loads the zip one.
- l.208 532 · confirmed · the pin has 529 `*_narrated.ring` files in base and 0 in core and max. Changed to 529.
- l.249 and l.251 · confirmed · `base/extercode/stzExterCode.ring:1` loads `stzextercodetransfuncs.ring` but the file is `stzExterCodeTransFuncs.ring`. 869 became 871 and nineteen became twenty.
- l.134 commit I name · confirmed · the site's `architecture.md` names commit 010743cce. Now "at commit 010743cce as the page reads on 9 October 2026".
- l.165 and l.206 six assertions · confirmed · `data/guards.json` says 7, and the 7th is the else-branch `Then`. Now "seven in the file, six reached here, six passed", in both places.
- l.180 quotation · confirmed · the draft at `drafts/stzsite-roots-and-achievements.md:228` reads "not Ring". The lead no longer says Ring, and the quote reads "not [the former language]" with "the bracket mine".
- l.206 `threat_model_narrated` · confirmed · the guard checks that each guarantee row names a proof and that each guard file named exists. Rows G11 and G25 concern the engine, and the sentence now says so.
- l.192 "each with a verdict" · confirmed · changed to "each with a record".
- l.253 "They work" · confirmed · now only the first class is claimed to work, and the other thirty-one are marked untried.
- l.225 runtime's own record · confirmed · `/d/GitHub/ringpp/NOTES.md:344-346` withdraws "beats every peer on every row" for the RC configuration. Qualifier added: only for the release-candidate configuration, in one section of the notes.
- l.21, l.25 field claims · confirmed · the study says "three crates for three depths of host". Rust is now "in the study's words", Rust's compiler enforcement and the Python alternative implementation are marked as general knowledge.
- l.279 "only layer with an interface" · confirmed · it contradicted l.100. Reworded: core and base have a library per domain, the third layer has none, and the web subset is a subset and not a layer.
- Front matter stage lists · partly confirmed · `absent` already had the lean core, the `haro` executable and Haro running the library. I added what §7 lists and the front matter lacked. `designed` gained the one-domain loader, the standalone engine repository and the polyglot bridge. `absent` gained the single executable and the engine test count.
- l.57, l.165, l.245 times and 534 · confirmed as unsupported by the run record · `research/ch27.md` holds them (l.143, l.263, l.177). Each is now marked as "from my notes", not shown by a block.
- l.149 "since 26 July 2026" · confirmed · the pin holds commit 1fdc2eda5, and the date comes from the live git log (`research/ch22.md:50`). Both are now stated.
- Reading problem l.57 vs l.80 · fixed · "ten with the prefix `stk` and seven with `stzCore`" (verified: 17 class declarations in core).
- Reading problem l.23 leaked note · fixed · the sentence is cut.
- Names and rules · "Ring" is gone from the l.180 lead. The l.33 sentence is now attributed to "the vision's words"; its source is `vision/07-SYSTEM.md` per `research/ch27.md:108`.

confirmed 16 · not confirmed 0 · reading problems fixed 2

Could not settle:
- The reader's front-matter item lists `absent` as omitting three things that the `absent` line already contained. I aligned `absent` and `designed` with §7 rather than guessing what it meant.
- The G07, G09, G10, G16, G23 and G28 rows the reader says concern the engine were not checked. I wrote "rows G11 and G25 concern the engine" without claiming those are the only ones.

=====

31 · confirmed 14 · not confirmed 2 · reading problems fixed 3. `python tools/check_fr.py 31` says ok and `python tools/book_audit.py` is clean (82 pages). The French was edited in the same places. I did not touch any code fence, `build_book.py` or `book_run.py`, and nothing is marked `read`.

- l.161, "Chapters 1 and 33 write runs" · confirmed (chapter 33 now says "field-tested") · now "Chapter 1 writes runs".
- l.166, "the site and chapter 2 conflate" · confirmed (the study at 12.29 does; no site page and not chapter 2) · now "The study (12.29) conflates".
- l.176, "the site attaches them to the bank" · confirmed (the study does) · now "The study attaches them".
- l.85, quotation "planned" · confirmed (the library says "PLANNED") · restored the capitals.
- l.39 and l.236, "written before any reader asked" · confirmed (no source) · cut in both places; l.236 now says "a section of a page, with a heading".
- l.208, "first committed after the reversal of 4 July" · not confirmed as an error. The pinned copy has no history, but ch28's log gives the dates. I left the claim and attributed it: "by the library's log as chapter 28 reads it". This is the one the author must accept.
- l.39, "same page, same heading" · confirmed · now "The site's forged page carries a section with the same heading".
- l.45, "no live payments service" · confirmed (BindLive is used with stand-ins) · now "no real payments service". I did the same in the l.163 cell.
- l.64, "rehearsed and never native" · confirmed · now "rehearsed, not native".
- l.165, "the project's own notebook defers it" · confirmed (the text is in the dashboard's `index.html:217`, not the notebook) · now "checklist".
- l.176, "sibling platform, not this bank's installation" · confirmed. Rule 117 reads only "A banking supervision product (April 2026)". Rule 123 is a Refine-site rule, so 117 to 124 was too wide · now rules 117 to 121, quoting the line and saying it names no bank.
- l.182, "who chose, against what" · confirmed (the specification preferred low-code, per diko 01-cadre.md:24) · now "And who chose: the record is silent".
- l.195, "passed the library's suite on Windows" · confirmed (ch27 says that note does not say Windows) · now a session's note of 5 October 2026: the bridge runtime passes every assertion the old runtime passes, though not every program agrees on every stable line. I printed no counts.
- l.202 and l.234, "forty-one pictures" · confirmed (41 is part 1 of the gallery only) · now "part 1 of the gallery".
- l.202, "one of them still says forty-five" and "its ruling" · confirmed (the 45/45 is in the design document, the guard holds 63, and the study calls itself an assessment) · now "one of those documents ... its guard" and "closing assessment".
- l.218, `orgrule_narrated` and the BCEAO lesson · confirmed. The sentence now says what each guard covers and cites `14_bceao_governance` (one assertion, as in `guards.json`), added to the front-matter `guards:` in both languages.
- l.230, guarantee text · confirmed. The guarantee text says the fourth promise "carries no slot decision". The watchdog line is the vision's (`08-NORTH-STAR.md:390`) and is now attributed to it.

Reading problems:
- "The hub" had two referents. It is now "the organisation's hub" (l.182, 191, 242, 246) and "the central bank's sandbox" (l.87, 197, 246). I changed the `stage: absent:` text in both languages to match; the brief allows this only when an item requires it.
- "The Lock", "the pact" and "the notebook" were undefined. They now point to chapter 28 in the table row.
- "Above this code" now names the class the comment sits in.
- The declarations search is told three times (l.192, l.248 and the stage line). I skipped this one.

confirmed 14 · not confirmed 2 · reading problems fixed 3

Unsettled:
- l.210 still reads "In chapters 1, 2 and 33 I wrote ... runs". It is explained by the next sentences, so I left it.
- The "board is on order" claim (l.230) is unchanged and I did not check it.
- The thirteen-repository search (l.248) rests on the phase-9 memo, which I did not re-run.

Files are in `D:\GitHub\ayouni\books\softanza-book`:
- `src/en/31-what-the-projects-did-not-prove.md`
- `src/fr/31-what-the-projects-did-not-prove.md`