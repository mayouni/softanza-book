# Compared, honestly

Source: Chapter 22. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: five comparisons, four run on both sides with the other side's version and the date, and the fifth run on the Softanza side only; the four code pairs of the site, re-run, three of them on both sides; three field studies that end on what the field has and the library lacks, and a culture plan that prints its losses; designed: a comparison register as data; a comparison court whose rule is that a row with no source or date does not publish; both benchmarks re-run on the present engine; absent: locale collation; locale casing; a grapheme count on the public string; a time-zone database; the benchmark of 7 July 2026 re-run; the source of the coverage matrix, which I could not locate

Run: 5 of 5 blocks kept their promise, on 2026-10-09 13:46 UTC+01:00.

## 1. The concept, as the field holds it

Comparison, in the field, is a genre of marketing with a few honest exceptions. The record names the genre: a "Compare" page for each rival, and a comparison block on each feature page. Its commonest form is the grid, with rows of features, columns of tools, ticks and crosses.

The honest exceptions are practices and not products. Benchmarks published with the method, the machine and the build mode. And sections that say what the other tool has that we lack. (General knowledge, not a study of the record. I name no tool, since the author names none.)

## 2. The first principle

**A comparison is worth nothing until the other side's version and the date are on the page, the other side has been run, and the loss is printed beside the win.**

It is built from three sentences of the record. The study of 7 October 2026: every claim about another tool is cited, dated and run, and every loss is published with the wins. The estate's study of a browser runtime, run on 8 August 2026: losses are published with the wins. And the site's page of coverage: a platform that shows its gaps is believed on its strengths. The author's request, as the study reports it, is a comparative tone that is "a motor force, to learn from the best and beat them when possible". The study adds: with "when possible" measured.

## 3. The Softanza form

Chapter 3 said "I refused the grid alone". This chapter is the method that replaces it, with its evidence. Here is what the record measured about the grid. The study scanned the library's text for tables whose header names Softanza and at least one other tool. It found sixty-four tables, in thirty-one documents. In them, the column of Softanza carries 286 ticks, 2 warnings and 2 crosses. The other columns carry 204 ticks, 207 warnings and 269 crosses. The study's judgement is that this is the shape of a brochure, and that the record itself does not trust it. I could not reproduce those figures: a narrower scan of my own, with a header rule I wrote, found thirty-seven tables in twenty-nine documents. The study does not print its header rule. I cite its numbers as its own, and dated.

The form that replaces the grid is a pair: the same task, both sides run, the other side's version on the page, and a line where the other side leads. I show five. Four were run on both sides, and the fifth, block five, on the Softanza side only. The runs were made on 8 October 2026, between 22:24 and 22:34, on a Windows machine, and the book's build ran the Softanza blocks again on 9 October 2026 at 05:32, all kept. The other side is Python 3.13.15, and Node v22.20.0 with its V8 12.4 engine and ICU 77.1. R and Julia are not installed on this machine, and no pair uses them.

**One: an integer is exact at any size.** Forty digits, from two numbers of twenty:

```haro
oN = new stzNumber("12345678901234567890")
? oN.MultiplyByQ("98765432109876543210").Content()
#--> 1219326311370217952237463801111263526900
```

> run: kept

The other side, Python 3.13.15, prints the same digits for `12345678901234567890 * 98765432109876543210`. Python's integer is exact by default, and Softanza is level with it. The Softanza line is the longer one: a literal this long cannot be a native number, so it is given as a string. The other side, Node v22.20.0, prints `1.219326311370218e+39`, because its default number is a 64-bit float. It is exact only when you ask for it with the suffix `n`, a second kind of number. So the win here is over JavaScript's default, and not over Python.

**Two: exact decimals.** `0.1` plus `0.2` is `0.3`, and a price times a rate keeps its cents:

```haro
? (new stzNumber("0.1")).AddQ("0.2").Content()
#--> 0.3
? (new stzNumber("19.99")).MultiplyByQ("0.15").Content()
#--> 2.9985
```

> run: kept

The other side, Python with floats, prints `0.30000000000000004` and `2.9984999999999995`. Node prints the same two, because JavaScript has no decimal type. Python's standard `decimal` module, imported and fed strings, prints `0.3` and `2.9985`: level with Softanza, and with the same cost per line. So Softanza wins on the default, since a number made from a string is exact decimal, and is level with the one library that does it deliberately. The guard's comment says why: the value is stored as a string, and the computation is done on scaled integers by the engine. Its limit is in the record's words, and one of them is stale: the rungs for rationals and for complex numbers are named in the plan and, in a comment of the guard of numbers that are not lost, "not built yet". The snapshot holds a narrated guard for each, `numeric_rationals_narrated` and `numeric_complex_narrated`, so that comment is out of date and I do not rely on it. I did not run those two guards.

**Three: sorting accented words. Here the field leads.** Softanza sorts by code point. The field's locale-aware sort puts `étoile` between `eau` and `zèbre`:

```haro
? @@( Q([ "zèbre", "étoile", "eau", "zoo" ]).SortedInAscending() )
#--> [ "eau", "zoo", "zèbre", "étoile" ]
```

> run: kept

The other side, Python's `sorted`, prints the same list: level, and both wrong for French. With the standard `locale` module set to `fr_FR.UTF-8`, sorted with `locale.strxfrm`, Python prints `eau, étoile, zèbre, zoo`. That worked on the machine of the run. The locale must exist on the host, and the call is process-wide. Node, with `Intl.Collator('fr')`, prints the same French order with a built-in library. So the field leads: JavaScript with one argument, Python with the host's locale. Softanza has no collation. The culture plan of 18 August 2026 says the sorting is the engine's ordinal sort. And the coverage page rates internationalisation partial, against deep for two other platforms, with a note: a deliberate bet against the big international library.

This block is a pinned gap. Its promise records the library's present, weaker answer, so the page fails the day the library gains collation. That is by design. The culture plan's own rule says that pinning a known gap is legitimate only when the assertion fails the day the gap is fixed, and when the label says so.

**Four: Turkish uppercase. The field leads.** A locale argument that is accepted and ignored:

```haro
? Q("istanbul").UppercasedInLocale("tr_TR")
#--> ISTANBUL
```

> run: kept

Python prints `ISTANBUL`: level, since the standard library has no locale casing. Node, with `toLocaleUpperCase('tr')`, prints `İSTANBUL`. Turkish needs the dotted capital. This is the loss most worth printing, and it is not that the engine lacks Turkish. It is that the method takes a locale and returns the wrong answer silently. The source comment says: plain uppercase when it has no rule. The culture plan measured the same on 18 August 2026 and called it the code equivalent of the fake progress bar. Its law is the reason for this chapter: no facades. An operation either honours the culture it was given, or refuses.

**Five: an instruction in your language.** A natural-language instruction is dictionary-driven and local: no network, no model, no key.

```haro
o1 = Naturally("Make a list holding [ 3, 1, 3 ] then drop its duplicates")
? @@( o1.Result() )
#--> [ 3, 1 ]
? o1.Understood()
#--> create a list with [ 3, 1, 3 ] -> remove duplicates
```

> run: kept

I did not run the other side. The field's equivalent of "take this sentence and do it" is a model call. What it needs is a model: a hosted one needs a network, an account, a key and a per-token cost; a local one needs a downloaded model and a GPU or a patient CPU. It needs a prompt, and a check that the answer is what was asked, and the answer is not guaranteed to be the same twice. The site's own pair of this kind writes the other side as a comment, which says that there is no counterpart without an external language model.

One more loss, which is not a block. A string of a family emoji, five code points, joined by joiners, shows a weakness in what the public string exposes. The counter class answers `1` for the grapheme count; `NumberOfChars` answers `5` and `NumberOfBytes` answers `18`; and `GraphemeCount()` on the string itself raises, because the method is not defined. The engine knows, and the string does not say. Python's `len` gives `5`, and Node's `.length` gives `8`.

## 4. The decision, and what I refused

**I refused the grid alone.** Two hundred and eighty-six ticks in Softanza's column against two hundred and sixty-nine crosses in the other columns is the shape of a brochure.

**I refused to keep a headline that does not reproduce.** The estate's memo of 13 September 2026 re-measured the runtime beneath the library against a fast runtime of the field on six matched kernels: identical algorithm and sizes on both sides, each side its fast idiom, cross-language checksums asserted before any number, minima over repeated runs. The field leads every row, by a factor between 1.04 and 1.88. The memo says the claim to retire is that the runtime beats it, in the present tense, on x64. The headline was never re-measured after the spike, as the memo calls the runtime's prototype, became a product. The memo asked the author to correct the runtime's own notes. The headline was withdrawn in the estate memo of 13 September 2026, and I say no more.

**I refused a retraction that deletes its evidence.** The runtime's own notes of 29 August 2026 retracted a published table in the other direction, a loss on a phone, because the run had executed on the phone's slow cores while the peer ran on fast ones. The notes keep the table, struck through, and say that a retraction that deletes its own evidence is not a retraction. So the record has withdrawn a win and withdrawn a loss. The rule is to reproduce before you print. Printing losses is not the rule.

**I refused a comparison that cannot be redone.** The hand-off packet of the same day, 13 September 2026, says the spike's kernels died with the working tree, which is why an outside session had to reconstruct the measurement from prose.

**I refused a facade.** Blocks three and four.

**I refused the large international library.** The culture plan's table says it is killed, a decision made and standing in the first layer. The cost is blocks three and four. The coverage page prints it as a deliberate bet.

**I refused to compare on the tool's strongest ground.** The estate's study of a browser runtime has three honesty rules: each language gets idiomatic code; losses are published with the wins; every engine is a release build. It says, of its own page, that without them it is marketing. Its scoreboard has nine scenarios, four won and five lost. It is not a regression gate: its numbers are for learning, and not for gating.

## 5. The court

The comparison court is proposed and not built. The study's plan names it: a comparison row with no source or no date does not publish, and a code pair whose other side did not run, or ran in a debug build, does not publish. I found no file in the library or the site that implements it. So what exists is what proves the blocks and bears on the method:

`numeric_exactness_narrated` proves exact decimal arithmetic, integers past 2 to the power of 53, the forty-digit product, and exact division when it terminates. `numeric_no_loss_narrated` proves that a number is not destroyed on its way in, and that the representation ladder is observable; its closing comment still names the rungs for rationals and complex numbers as not built, and is stale (see block two). `semantic_resolver_narrated` proves that paraphrases resolve to canonical operations through the local lexicon, and block five's sentence is one of its cases. It does not pass at this commit: I ran it on 8 October 2026 and it stops with an error raised from a string-splitting function, before it ends, so the page counts its assertions and does not claim its verdict. `engine_is_optimised_narrated` proves that the engine is compiled with optimisation, by a time gate: it is the library's own guard for the release-build rule.

No guard asserts blocks three and four as pinned gaps. No guard exists for a code pair whose other side did not run. I list both among the requests.

## 6. The field, and where it leads

The record already keeps the list of what the field has and Softanza lacks. I print it, by file and date, beside the wins.

**Performance, against the field, 29 July 2026.** No time-series store, no query language, no dashboards: by design, the plane exports. No distributed context beyond HTTP. Sampling that is honest and cruder. Decades of integrations, which the incumbents own. The study's own words are that on breadth the incumbents win decisively, and that the plane does not compete with them and should not pretend to. Four losses are struck through with the phase that closed them.

**Incident analysis, against the field, 1 August 2026.** Scale, retention and search, where bounded means forgetting. No telemetry from the host, the kernel or the network. A small set of shipped detections against a community's corpus. The workflow of an operations centre. And the unwired seams, which the study calls the system's largest honest gap, listed and not hidden.

**The plugin study, 16 August 2026.** The field is ahead on permission granularity, on dependency resolution, on distribution and signing. The study's header says it is analysis and not rules.

**The culture plan, 18 August 2026.** Every row was verified in that session by running it. Casing is a facade four levels deep. Collation, digit shaping, non-Gregorian calendars and time zones do not exist. The plan's status then was not started.

**The estate's browser-runtime study, 8 August 2026.** Four of nine rows won, five to the peers, and the fused loop opcode of one peer stays a design generation ahead.

**The runtime against a fast peer, 13 September 2026.** Six kernels, checksums first, the peer ahead on every row.

**The string benchmark of 7 July 2026**, and the polyglot battle, in a narration dated 18 April 2025: the former host language came last of seven in two of three rounds and in the total. Both carry caveats the later record has put on them. I did not re-run the benchmark. The engine's default build was a debug build until 26 July 2026, and the library's own build file says every shared library it had ever loaded was compiled unoptimised. So the benchmark probably ran unoptimised. That is an inference, and I state it as one. The same comment says that on string, list and matrix work the change buys only about fifteen percent, so the build mode is a caveat on the numbers and not an excuse for them. I could not read the engine's build mode here, and the clock of the host language resolves ten to fifteen milliseconds. So the benchmark is cited here as a dated record, with that caveat, and not as a present measure.

**The coverage matrix.** Thirty domains in seven groups, against four other platforms, read on 17 September 2026. Softanza's tally is seven deep, fourteen solid, seven partial, two absent, present in twenty-eight of thirty. I recounted it from the rows and it matches. The two absent rows are symbolic mathematics ("no computer algebra") and package, build and deploy ("a library, not a registry"). Among the seven partial rows is internationalisation, "a deliberate bet against ICU", and the neural row is "inference only; no training foundry". The stored tallies of two of the other platforms do not match their own rows, by one in two places. I print Softanza's tally only. The matrix cites a compass file as the source of the ratings, and I could not locate the file in the snapshot, in the live checkout or in the estate's repository.

**The graph comparison, a narration dated 26 December 2025.** A model wrote it, and says so in its byline. Its column for Softanza rates itself with a cross on scalability and on transactions and with a warning on performance, and its conclusion lists where traditional solutions win.

Where Softanza stands apart, by the record, without a number: the SLA; the governed act; the typed event; the matrix's one row of governance and safe execution; exact numbers by default, against two floats; an instruction that resolves locally. And a method that prints each of them beside a loss.

## 7. The limit

What is built: four of the five pairs, run on both sides, and the fifth on the Softanza side; the four code pairs of the site, which I re-ran on 8 October 2026, three of them on both sides (the fourth has a comment for its other side), with my note of the night saying the outputs matched; the library's field studies of performance, incident analysis and plugins, with their loss sections, and the culture plan, which prints its losses; the harness of the string benchmark; the guard that the engine is optimised.

What is designed or proposed: a comparison register as data; a comparison court; the re-run of both benchmarks. The study holds all three. When I drafted this chapter, on 8 October 2026, I searched for them in the library and in the site and found nothing. The site, read on 9 October 2026, now prints five rules for comparing, the first being "Cite or do not publish", and a list of the nine rows where Softanza is partial or absent, with the platforms that are deep there. It says, in a line marked designed, that a register of comparisons is not held as data yet. It does not name the court.

What is absent: a *compared* column on the Atlas, on the register of innovations and on the narrations; the field studies, the sixty-four grids themselves (the site now gives their number and no more), both benchmarks and the runtime table on the site; locale collation; locale casing; a grapheme count on the public string; a time-zone database; the re-run of the benchmark of 7 July 2026; the source of the coverage matrix.

And something that is unreproduced: the study's sixty-four, six hundred and fifteen and thirty-one, which my scan did not reproduce, and the symbol counts.

The method is stricter than the record it is applied to. Older comparisons in the library fail one or more of its rules. The string benchmark probably ran on a debug engine. The polyglot battle has no versions and no dates inside its text, and says its times are relative to a specific computer environment. The graph grid has no versions, dates or sources for its cells. The cognitive-load grid of another design article makes claims of sixty to seventy percent with no method printed beside them. That article then ends on an honest positioning that names four things the library does not compete on.

## 8. Six doors

**The programmer.** Copy a pair. Run both sides in your own versions, keep the output as it came, and add the line where the other tool is ahead.

**The analyst.** The coverage matrix is a buying aid only because it shows two absent rows and seven partial ones in its own colours. Read those first.

**The designer.** The loss goes in the same block and in the same type as the win. The stage word is part of the interface.

**The decision-maker.** Ask any vendor, this one included, for the other side's version, the date, whether it was run, and the line they lose. The memo of 13 September 2026 is a model of a headline withdrawn.

**The educator.** A code pair is a lesson in what a line costs. The learner writes the other side's output before running it.

**The agent.** When you repeat a claim about another tool, carry its version and date, and say if you did not run it. The register that would make this checkable by an agent is proposed and not built.

## 9. Exercise

Pick one task where you believe your own tool is ahead, and one where you believe the other is. Make a comparison that obeys the three rules: the other side's version and the date, both sides run, the loss printed.

```haro exercise
? YourSide(the_input)
#--> the line your tool prints
```

> run: exercise

Under it, write as text: the other tool's name and version, the date, the exact line it prints, and one line of the form "here the other leads because...". A reader checks the three text lines, since a runner cannot.

A variant that a machine can judge: take the five lines of block three's other side and predict, before running, the order each one prints. I will not tell you which order is right.
