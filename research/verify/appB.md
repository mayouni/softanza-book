Appendix B (the fourteen house rules) · claims checked: 96 · verified 85 · wrong 1 · unsupported 2 · overclaim 8

Source for the table: `base/meta/stzCodeRules.ring` (names 23-29; text passes) and `stzCodeRule.ring` (graph rules). The 14 names, order, [2], [14], the three fired rows and the 8 underscore / 6 hyphen split match the source and `data/book-run.json` (both blocks kept). Guard `coderule_narrated` (77) is front matter only; no count in prose.

Findings
- line 11 · "It reads a class as a graph and judges it against rules" · overclaim · `stzCodeRule.ring` builds 5 graph rules (no-len-method, no-aggressive-verbs, engine-first, q-has-plain-twin, no-case-collision); the other nine are text passes (`stzCodeRules.ring:136-146, 225-256`; chapter 32 line 60 says "five of them over a graph") · "reads a class as a graph (five rules) or as text (nine)".
- line 11 · "each of which was written after the library did something it should not have" · overclaim · incidents are recorded in comments for rows 5 (62 Q-only mutators, `stzCodeRule.ring:243`), 7-14; none found for no-len-method, q-returns-object, no-aggressive-verbs, engine-first (a "scope ruling", `stzCodeRules.ring:19-21`) or no-case-collision (a C22 explained, no incident) · "most were written after..." or drop.
- line 15 · "The list is closed and the library can print it" · overclaim · `StzCheckCode` also emits `for_in_loop` (`stzCodeRules.ring:145, 1140-1163`), not in `StzCodeRuleNames()`; `StzCheckProject` adds no-dead-code and no-cyclic-calls (`stzCodeRule.ring:337-386`); research/ch07.md:603(c) already asked the writer to say so · "The list of names is fourteen; one more text pass (for_in_loop) and two project rules also report."
- line 56 (row 3) · "begin with a violent verb" · overclaim · the rule tests two prefixes only, `kill` and `destroy`, on methods and functions (`stzCodeRule.ring:131-146`) · "begin with Kill or Destroy".
- line 60 (row 7) · severity "error" · overclaim · `stzCodeRules.ring:663-681`: error when nothing reads the attribute; warning when only its own getter reads it, or the class has a parent in another file · "error; warning when only its getter reads it".
- line 61 (row 8) · severity "per the source" · overclaim · the source declares `:warning` (`stzCodeRules.ring:820`, `_StzCheckSetterResets`) and line 69 says the severities are "the source's declarations" · write "warning".
- line 65 (row 12) · severity "warning" · overclaim · `stzCodeRules.ring:1408-1411` gives `:error` for a predicate (Is/Has/Contains/Can/Are/Was/Should), warning otherwise; the "what it refuses" cell says "harsher" but the severity cell does not · "warning; error for a predicate".
- line 83 (writing rule 3) · "judged by a machine" · overclaim · Testoor judges a promise that is present (kept, diverged, unreached); no rule refuses a `?` line with no `#-->` (chapter 7 line 255 and research/ch07.md:531 find no such court); line 13 says no machine judges the rules of writing, which this row contradicts · "the promise is judged when written; a line without one is not refused".
- line 69 · "I did not fire them" (rows 3, 4, 5, 8, 14) · wrong for row 3 · chapter 32 lines 64-72 fire `no-aggressive-verbs` and print `1` for `StzCodeIsClean` (book-run, kept) · remove 3 from that list.
- line 69 · "rows 2, 7, 9, 10, 12 and 13 in the research for chapter 7" · unsupported · only research/ch07.md:385 says probes fired them; the kept blocks cover rows 10 and 13 (chapter 7) and row 2 (chapter 5); no data row for 7, 9, 12 · "rows 10 and 13 in chapter 7, row 2 in chapter 5; rows 7, 9 and 12 read from the source".
- line 93 (writing rule 13) · "does not run" · unsupported · research/ch07.md:125 ran Chinese and French names only; the Arabic `الحرف_الأخير` was not run (defined only in `string/archive/stzString_monolithic.ring:96429`) · "Chinese and French names raise; the Arabic one was not run".

Reading problems
1. Line 48 speaks of "the rules over the code graph" but nothing in the appendix marks which five they are; the table could carry a column "graph / text".
2. Line 67 (row 14): "the shape a sweep leaves" uses "sweep" (a token-replacement rewrite) with no explanation; the rule's other trigger, a name glued to a call on a def line, is not mentioned.
3. Line 69: "in the research for chapter 7" points at a file the reader does not have.

Other rules
No other repository's product named; no "Zin", "substrate" or "maker". "Host" is used for the former language, consistent with CLAUDE.md. Stage words: the court is built (kept blocks, guard 77); the style court is correctly marked as not existing (lines 73, 83-94).
