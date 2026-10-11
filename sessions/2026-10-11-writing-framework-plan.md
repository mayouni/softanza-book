# Plan — applying the AYOUNI Writing Framework to the Softanza book (2026-10-11)

The framework is `../../../writing-framework/FRAMEWORK.md` (v0.1); the study it rests on is `../../ring-book/style/STYLE-ANALYSIS.md`. This plan says what the Softanza book, as it stands after Phase 11 (41 pages, all `draft`, 282 of 282 blocks kept, verified by fresh readers), keeps of the framework already, what it lacks, and the phases that bring it in line. Nothing here is started; each phase is a session, and the author's reading remains the one gate no phase replaces.

## 1. Where the book stands against the twelve commitments

Measured with `tools/style_lint.py` over `src/en` (92,583 prose words) and `src/fr`, and read from the Phase 10–11 verification reports.

| Commitment | State | Evidence |
|---|---|---|
| C1 Run it, then read it | **kept, by construction** | every block runs at every build; the verdict is printed under it; the court box per chapter |
| C2 A defect in the reader's hands | **half** | every chapter has element 9 (exercise); none leaves a planted bug, a rejected-correct-code, or a refused chart; the exercises are demonstrations more often than defects |
| C3 Say where you stop | **kept, and over-corrected once** | element 7 (the limit), stage words, "the loss beside the win"; 624 overclaims found and narrowed in Phases 10–11 |
| C4 The true particular | **the hole** | 77 `[AUTHOR]` slots answered by policy with "the record holds none"; the author's true particulars (his own sentences, his memories, his family, his places) are absent except where chapter 1 (his text) and the recorded quotes carry them |
| C5 One metaphor at a time | **partly** | the ruling metaphors (court, doors, twin, world, crafter, gate) are stable in name, but none is mapped term by term where it first appears, and the glossary is an appendix, not a scene |
| C6 I, we, you, the tool that answers | **I and you kept; the beats gone** | questions 0.3 per 1,000 words (Ring: 3.3), exclamations 0.1 (Ring: 2.4); the tool answers only through the verdict box, never in the prose ("Ring complains and says:") |
| C7 Long, then short | **partly** | median sentence 16 words, as the profile; but long sentences 4.1 % (Ring 3.3 %) and the preface, chapters 20, 32, 19, 28, 27, 3 and Appendix G above 6 %; colons 15.1/k (right); dashes 0 (right); one-sentence paragraphs rare |
| C8 Count and name | **kept** | nine elements, six doors, three stage words, nine spine chapters, fourteen rules, twenty-two verbs; counts audited |
| C9 Roadmap and bridge | **shape kept, roadmap missing** | the nine elements give the chapter its shape, but no chapter opens with "in this chapter I…" and most close on the exercise rather than a bridge or a coda |
| C10 Lift the stakes once, own it | **lifted, not owned** | each chapter's principle is a stake; the "owning" sentence ("this is my view, not a scientific truth") appears nowhere; the verification found the reach without the concession |
| C11 The questioner's record | **kept, exemplary** | pinned library, run data, guards, decisions, memos, requests L1–L68, verification reports, book.json |
| C12 Plan large, ship what runs | **kept** | 33 chapters planned and shipped; proof copy until read |

Noise, from the lint (English): 11 forbidden-word hits (all "developer" where the book's word is programmer, in chapters 2, 16, 24, 30, 31, 33), 6 calques ("may be" ×4, "a hole" ×1), 14 hedge stacks ("kind of" ×8), 1 superlative ("for the first time", the restored phrase, attributed), 0 emoji, 0 trailing ellipses, 18 colon lead-ins to a prose paragraph. The French: 6.9 % long sentences (translation lengthens), otherwise clean.

In one sentence: **the book has the discipline of the framework (C1, C3, C8, C11, C12) and not its warmth (C2, C4, C6, C9, C10).** It is the exact inverse of the Ring book, whose warmth was everywhere and whose discipline needed the editor.

## 2. The phases

Each phase is one session or one workflow of agents, ends with a memo, and changes nothing in code fences. Order matters: the author's part (Phase A) is first because every later phase is cheaper once the particulars are his.

### Phase A — the author's own hand (his session, with an agent as scribe)
The 77 delegated answers are the map of where only he can write. For each of the 41 pages the agent prints the slots (the former `[AUTHOR]` sentences, now "the record holds none"), and the author speaks or types what is true: a memory, a date, a name he allows, a sentence of his own, or "leave it". The agent writes it in his words, sourced to the session's date, in both languages; nothing is composed. Expected: 20 to 40 true particulars across the book, a sentence in his voice at the opening of each part, the cover line he wants for the back, the preface's first paragraph. Output: the pages, a memo listing every particular added with its source "author, 2026-xx-xx".
*Gate:* the particulars audit (every name and date traced); no new `[AUTHOR]`.

### Phase B — the beats (agents, chapter by chapter, voice reader then fixer)
Restore C6 and C7 without restoring the noise: in each chapter, a question put to the reader or to the machine where a run follows ("What does the court say? Run it."), an exclamation only after a run or a reveal (target 1–2 per 1,000 words, never on an abstract sentence), the long-then-short verdict after each long sentence, one-sentence paragraphs at hand-overs, the tool quoted as speaking where the prose now paraphrases the verdict box. The voice reader (`briefs/voice-reader.md`) reports per chapter; the fixer applies, English and French; the lint confirms the profile. Budget: 41 readers + 41 fixers (as Phase 11).
*Gate:* lint: questions ≥ 1.5/k, exclamations 1–2.5/k and none cold, long sentences ≤ 4 % per page; `check_fr` clean.

### Phase C — the defect in hand (agents propose, author chooses)
For each chapter, agents propose two candidates for a real defect to leave the reader: a planted bug in a copy of a block (never in the running block), a correct listing the author rejects for taste with his reason (from the decision section), a chart or an answer refused ("it depends on the strategy you adopt"), a question the record cannot answer. The author picks one per chapter in a single pass (a table of 33 rows); the agents write it into element 9 and rename element 9 where the shape allows ("What is left in your hands").
*Gate:* the chapter checklist C2 answered with a line for all 33 chapters.

### Phase D — roadmap and bridge (agents, mechanical, then the author's codas)
Each chapter gains an opening paragraph in the first person, three to five sentences, saying what it does and ending on the chapter's one particular; each chapter's close becomes a bridge to the next (one sentence) or, where the author gave one in Phase A, a coda. The build's `convert_body` keeps the nine elements; the roadmap is prose before element 1 and the bridge after element 9. French follows.
*Gate:* voice reader item 1 clean for all chapters.

### Phase E — the metaphors mapped (one agent, then the author)
A metaphor register of the book (court, judge, verdict, guard, door, gate, twin, world, constellation, bond, crafter, workbench, engine, floor, plane, spine): for each, where it first appears, its term-by-term mapping in one paragraph at that place (as Ringoria's glossary maps water and sand), the names it must keep in both languages, and the field metaphor it refuses, by name. Decorative metaphors (deletable without loss) listed for cutting. The author rules on the register.
*Gate:* names stable (audit extended with the register); no decorative metaphor left.

### Phase F — own the stakes (agents flag, author marks)
From the verification reports, the sentences that lift the stakes (each chapter's principle and its "field" paragraph) are listed; for each, either the page backs it or the author adds the marking in his words ("this is my view", "I have no proof of this beyond three projects"). Agents never add the marking themselves; they add the list to the memo.
*Gate:* voice reader item 10 answered for all chapters.

### Phase G — noise and the lint in the build (agent, one session)
Fix the 11 "developer", 6 calques, 14 hedge stacks; split the long sentences of the preface, chapters 20, 32, 19, 28, 27, 3 and Appendix G (generated: fix its generator); add `style_lint.py --strict` to `tools/release.py` as gate 4 and to `build_book.py` as a warning; a French word list for the lint (`--lang fr`); the Softanza `CLAUDE.md` gains a "voice" section that cites the framework version and replaces "one exclamation per chapter at most" by the framework's placement rule (AWF-03), if the author agrees.
*Gate:* `style_lint --strict` passes on `src/en` and `src/fr`.

### Phase H — the author reads (his; the only gate that makes a release)
Chapter by chapter, `status: read`; the French re-checked against each read page; the proof copy becomes a release when the last page is read. The verification (Phases 10–11) stays a standing gate: any page edited after its report gets a new fresh-reader pass before `read`.

## 3. Order, cost, and what the author decides first

A → B → C → D → E → F → G → H. Phases B, D, G are agents' work in bulk (each about the size of Phase 11: 80 agents, an hour of wall time). Phases A, C, E, F need the author in the room for a focused pass each (A is the longest: 41 pages; C, E, F are a table each). Phase H is his reading.

Before any of it, three rulings from the author (they change what the agents write):
1. **The author's calls** (FRAMEWORK §4): the tool as "she" or "it" in this book; the reader's pronoun; whether the flourish of 2019 ("Ready? Please give me your hand…") has a place in 2026.
2. **The exclamation rule**: the brief's "one per chapter at most" or the framework's "only after a run or a reveal" (AWF-03).
3. **The ruling metaphors**: confirm the register of Phase E, or name the ones to drop.

## 4. What this plan refuses
- Rewriting the chapters in a "warmer" voice by agents alone: the warmth of the Ring book is true particulars and earned beats, and an agent can supply the second only after the first exists (hence A before B).
- Touching chapter 1 (the author's text) in any phase except by him.
- Lowering the discipline to gain the warmth: the court, the limit, the loss beside the win and the verification stay exactly as they are.
