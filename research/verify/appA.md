Appendix A (the register of innovations) · claims checked: 120 · verified 111 · wrong 1 · unsupported 1 · overclaim 7

Source for the rows: drafts/stzsite-roots-and-achievements.md, section 12.19 (lines 722-810). All 46 rows, their one-line texts, evidence cells and the prose on engines, "not measured" and "what the register says" match 12.19 (numbers copied exactly; "about six thousand" for 6,090 is fair). The family and "not told" counts are right (seven not told: rows 16, 21, 25, 27, 28, 30, 31). The problems are in the column the book added, "In this book", checked against src/en/*.md.

Findings
- line 75 (row 36) · "15 (matrices only)" · wrong · chapter 15 tells the Matrex pattern language (front matter narration stzMatrex, guard 00_matrex_narrated), which is row 23. Row 36's matrices are matrix computing (narrations stzmatrix-matrix-computing, stzLinearSolver); grep "LinearSolver|stzmatrix-matrix|statistic" in src/en finds neither (16:272 is R's statistics, other tool) · say "not told", make the line-14 count eight and delete "One more ... told only in part".
- line 14 / line 10 · "forty-six" as the study's final ruling · overclaim · same day, 12.26 (stzsite-roots-and-achievements.md:1107) adds row 47, and chapter 3:46 says the site register "says forty-seven" · add one sentence: row 47 (answer-by-example) was added later and is not in this table.
- line 28 (row 9) · "Future actions ... 8" · overclaim · chapter 8:217 says the future form was removed on purpose on 10 July 2026 and 8:13 lists it absent · "8 (removed on purpose, 10 July 2026)".
- line 29 (row 10) · "a four-stage gate" · overclaim · chapter 10:204 and 214: the header says four stages, the code has five checks · "(four stages in the design, five checks in the code, chapter 10)".
- line 61 (row 26) · "viz, boxes, string art, the plotting system ... 7" · overclaim · chapter 7 tells only the `viz` prefix (7:147-160, vizFind; vizFindAll absent); grep box|string art|plot finds none · "7 (the viz prefix only)".
- line 72 (row 32) · "Time programming ... 9, 15" · overclaim · 9 tells the timeline (row 17) and 15 the Timex pattern language (row 23); none of the six time narrations (time, datetime, duration, calendar capacity) is in their front matter; grep calendar|capacity finds no calendar planning · "9, 15 (the timeline and Timex only)".
- line 88 (row 43) · "The front door and secrets ... 21" · overclaim · 21:129-131 tells redaction and secrets; the front door appears only as one ledger event (21:116 "auth.login.failed") · "21 (secrets; the front door as an event only)".
- line 94 (row 45) · "tagging and self-documentation ... 7" · overclaim · chapter 7:206-210 tells the tags (6,126 recounted, "no guard reads them"); Ask/ExplainMethod and "conversational" are not told there; grep finds none · "7 (the tags, and that no court reads them)".
- line 84 (row 40) · "the frame profiler" among things told in 21 · unsupported · 21 has the stopwatch, governed loop, judgment and tail (guard tracing_tail_narrated); "frame profiler" appears nowhere in 21 as a thing shown · drop it from the "told" reading, or add "(not shown)".
- line 39 (row 15) · "few, some, most, all ... they draw at random, and I say so" · verified for some/few/most (stzRandom.ring defines them; 3:150), but the sentence is silent on "all", which the narration does not show drawing · "(some, most and few draw at random)".

Reading problems
1. Line 34: the heading "The twelve paradigm engines" sits over nine rows; the reason (three engines have no row of their own) is only given at line 101.
2. Line 99: "except those with a page" cannot be followed once the site column is removed (line 10); the reader does not know which paradigms have a page.
3. Line 14: "in the shade" is used before the register has explained it (line 99).

Other rules
No other repository's product named; no "Zin", no "substrate". "RegexMaker" (row 24) is a library class name, not the word "maker" in the book's voice. The appendix prints no guard counts, so nothing to compare with data/guards.json.
