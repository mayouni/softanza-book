# The engine beneath: three layers, one engine, Haro

Source: Chapter 27. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: three layers chosen by the entry file you load, each including the one beneath and none above; the dependency rule held at the loads; an engine of eighty-nine libraries, in Zig, built in optimised safe mode, with the engine's own count of what it exposes; Haro as a ratified charter and a spike whose courts run on the new runtime and on the old one; designed: the base layer inheriting the core layer; the max layer as a built layer; a court that checks the layers against their contract; a layer chosen by a declaration the compiler honours; the other faces of Haro over one program graph; a loader for one domain of base; the standalone engine repository and its command line; the engine's polyglot bridge, which is chapter 16's; absent: a lean core layer that runs its strings; a Linux or macOS engine in service; a measured pass of the library on the new runtime under Linux; a `haro` executable; Haro running the library; a single executable with no dependency; an engine test count that I may print

Run: 9 of 9 blocks kept their promise, on 2026-10-14 12:15 UTC+01:00.

In this chapter I load the three layers of the library, one entry file at a time, and count what each holds. I read the engine beneath them, its eighty-nine libraries and the functions it registers, and I let the court say whether it is optimised. I set down the decisions, that the future is Haro and that every feature is implemented once, in the engine, and I print the rows where a fast peer still leads. The principle stands over all of it: the surface is the promise, and the runtime is the part you measure, and never assert.

## 1. The concept, as the field holds it

A platform inside one codebase is drawn as a stack with one rule: an inner layer knows nothing of an outer one. The cleanest peer, in the study's words, is Rust's three crates for three depths of host, chosen by the target. (General knowledge for the field: Rust enforces the rule by its compiler.) Softanza holds it by entry files, and section 7 says what that costs.

The field's habit for an engine is a native library with a plain C interface, wrapped thinly by each language. SQLite is the common example: one C library, bindings in nearly every language. The record states the same design for its engine: language clients are thin bridges that add syntax and paradigms, and never computation. (General knowledge for the field, well established.)

And the field has done, repeatedly, a third thing: a language keeps its surface and its libraries and changes the machine beneath. The record's own example is a typed descendant of Lua. Another is the alternative implementation of Python. (General knowledge for the field, well established.) Both teach the same thing the record teaches: the surface is the promise, and the runtime is the part you must measure.

The principle that follows is one sentence, and section 2 sets it down.

## 2. The first principle

**Every feature is implemented once, in the engine. The surface is the promise, and the runtime is the part you measure, and never assert.**

The first sentence is the engine architecture's design rule, in a session's document: every feature is implemented once, in the engine. Language clients are thin bridges that add syntax and paradigms, never computation. Chapter 4 told the author's ruling that follows from it, that I refused computation in the faces. The second sentence is the brief of the runtime beneath: performance and portability, measured, never asserted.

And the definition that governs the engine's dependencies, which chapter 4 already states: sovereignty is nothing anyone else can withdraw. In the vision's words, it never meant every line ours.

## 3. The Softanza form

Three claims, and a block for each of what a block can prove. I tell you first what a block cannot prove, because it matters. The dependency rule of the layers, that no core file loads base and no base file loads max, needs a scan of about eight hundred and seventy load lines. Only a guard could carry that, and none exists. I did the scan with a script of my own, and section 7 gives its result.

### A layer is the file you load

How many classes does each entry file load? Three entry files, three fresh processes. Each prints how many classes it holds, and whether `stkList`, `stzList` and `stzListXT` exist. The block spawns child processes, because this chapter's own process has already loaded the largest layer, and only a child can show the core alone:

```haro
cAsk = 'aC = ringvm_classesList()' + nl +
       '? "" + len(aC) + " " + (find(aC, "stklist", 1) > 0) + " " + (find(aC, "stzlist", 1) > 0) + " " + (find(aC, "stzlistxt", 1) > 0)' + nl
aEntries = [ "core/stkLib.ring", "stzLib.ring", "max/stxLib.ring" ]
for i = 1 to 3
    write("layer" + i + ".ring", 'load "../../../' + aEntries[i] + '"' + nl + cAsk)
    ? trim(systemcmd("ring layer" + i + ".ring"))
    remove("layer" + i + ".ring")
next
#--> 17 1 0 0
#--> 674 1 1 0
#--> 714 1 1 1
```

> run: kept (touches files)

The first process prints `17 1 0 0`. Core holds 17 classes, ten with the prefix `stk` and seven with `stzCore`, and no base class. The second prints `674 1 1 0`: base holds 674 and no max class. The third prints `714 1 1 1`: max holds 714. Each layer includes the one beneath and none above: core inside base inside max, loaded from below. A load of the core entry alone takes about a tenth of a second on this machine. A load of base takes between three and eight seconds, in single runs on 9 October 2026. My notes hold those times, and no block shows them.

The contract says base builds on core, by inheritance or delegation. What do the classes say? `ringvm_classesList()` returns, for each class, its name, its identifier, and its parent:

```haro
aClasses = ringvm_classesList()
? ParentOf("stkString")
#--> stzcorestring
? ParentOf("stzString")
#--> stzobject
? ParentOf("stzList")
#--> stzobject
? ParentOf("stzListXT")
#--> stzlist

func ParentOf(cClass)
    n = find(aClasses, lower(cClass), 1)
    if n = 0  return "(not loaded)" ok
    return aClasses[n][3]
```

> run: kept

The second line prints `stzobject`: `stzString` inherits `stzObject`, and not `stkString`! Core carries a parallel hierarchy, in which `stkString` inherits `stzCoreString`, the first line's `stzcorestring`. Max does build on base: `stzListXT` inherits `stzList`, the last line's `stzlist`. Exactly two base classes inherit a core class, `stzSciNumber` and `stzPointer`, and one delegates, in a line of `stzPointer`. They are two of about six hundred and seventy-seven. The contract is not met, and it is not met in the way chapter 4 asked about. I print it as a debt.

And the third layer by its prefix. In the process of the largest layer, how many classes begin with `stk`, how many with `stz`, and how many with `stx`?

```haro
nStk = 0  nStz = 0  nStx = 0
aClasses = ringvm_classesList()
for aClass in aClasses
    cPrefix = left(aClass[1], 3)
    if cPrefix = "stk"  nStk++
    but cPrefix = "stz"  nStz++
    but cPrefix = "stx"  nStx++
    ok
next
? @@([ nStk, nStz, nStx ])
#--> [ 10, 693, 0 ]
```

> run: kept

The block prints `[ 10, 693, 0 ]`. Ten, six hundred and ninety-three, and none! The forty classes max adds to base all carry the base prefix. The thirty-two classes with the third prefix exist, all in one folder, and no entry file loads them. Section 7 says it again.

### One engine

The layers are real at the binary. The build file declares the core domains and the base domains and builds one library per domain, in a loop. How many libraries does it declare for each layer? This block reads that file, and the claim is about that file:

```haro
$cEngineDir = "../../../engine"
cBuild = read($cEngineDir + "/build.zig")
n1 = substr(cBuild, "const core_domains")
n2 = substr(cBuild, "const base_domains")
n3 = substr(cBuild, "fn addSpeech")
? Q(substr(cBuild, n1, n2 - n1)).NumberOfOccurrence('.name = "stk_')
#--> 4
? Q(substr(cBuild, n2, n3 - n2)).NumberOfOccurrence('.name = "stz_')
#--> 85
? Q(cBuild).NumberOfOccurrence('stx_')
#--> 0
```

> run: kept (touches files)

The block prints `4`, `85` and `0`. Four core libraries, eighty-five base libraries, and no library for the third layer: eighty-nine in all. The marker `fn addSpeech` is the first function after the two tables, a boundary in plain text, arbitrary but visible. A court of layers would parse properly, and I list it among the requests. The study says eighty-six base domains at this commit and I read eighty-five.

The engine tells the library what it is. Its version is a constant. How many distinct functions does it register in the virtual machine once it is loaded?

```haro
? StzEngineEmbedVersionString()
#--> 0.8.0
aAll = ringvm_cfunctionslist()
aNames = []
for cName in aAll
    if left(lower(cName), 9) = "stzengine"  aNames + lower(cName)  ok
next
? len( Q(aNames).DuplicatesRemoved() )
#--> 2786
```

> run: kept

The block prints `0.8.0` and `2786`. Two thousand seven hundred and eighty-six distinct engine functions, the library's own view, taken at run time. The same call returns more entries, since the virtual machine's own are included, and several names appear more than once; I did not trace why. I assigned the list to a variable first. The call is re-evaluated at every turn of a loop, and I stopped two runs that grew to gigabytes before I learned it. The count moves with the built engine.

There are three counts of three different things, and the chapter says which it prints. The first is the count to the library at run time: the 2,786 above. The second is the count to any host through the C interface. A script of mine read the export tables of the eighty-nine libraries on 9 October 2026 and found 1,710 named symbols, of which eighty-nine are the loader's hook, so 1,621 functions. The third is the count in the Zig sources, as registration names: 2,703 distinct literals. The site says 752 and 2,652, at commit 010743cce as the page reads on 9 October 2026, and the library's typed constants say 1,513, dated 16 June 2026. I cannot reproduce 752 by any method I tried. Print only a count the build reads, with its method and date.

**The engine does the work.** What does the host's `upper` make of the German sharp s, and what does the engine's case mapping make of it, its own table over a vendored library? A second vendored library stems words. These are two of the nineteen:

```haro
? upper("Straße")
#--> STRAßE
? Q("Straße").Uppercased()
#--> STRASSE
? @@( Q("running runs ran").StemmedWords() )
#--> [ "run", "run", "ran" ]
```

> run: kept

The first line prints `STRAßE`: the host leaves the sharp s alone. The second prints `STRASSE`: the engine writes SS! The third prints `[ "run", "run", "ran" ]`: the stemmer folds `running` and `runs` to `run` and leaves `ran`. If Haro's `upper` becomes full Unicode, the promise changes.

And the engine is optimised. The default mode of the build is optimised and safe, since commit 1fdc2eda5, which the library's git log dates 26 July 2026. The pinned files hold the commit and not the date. Until then every library the library had ever loaded was compiled with no optimisation, and that closes the question chapter 22 left open about the build mode. A guard reads time, since it cannot read a flag. Do twenty sums over two million doubles that live in the engine finish in under a tenth of a second, and are they right?

```haro
oBuf = StzNumBufferOfSizeQ(2000000)
oBuf.RangeFrom(1, 1)
nT0 = clock()
for k = 1 to 20
    nSum = oBuf.Sum()
next
? (clock() - nT0) / clockspersecond() < 0.10
#--> 1
? nSum
#--> 2000001000000
oBuf.Free()
```

> run: kept (touches the clock)

The block prints `1` and `2000001000000`, the boolean and the sum, and no time, because a time is not a promise. In three runs on 8 and 9 October 2026 the elapsed times were 0.02, 0.04 and 0.03 seconds, from my notes and not in the run record. The guard's own table says 0.14 for the unoptimised mode and 0.04 for the optimised one. The guard itself ran on 8 October: seven assertions in the file, six reached here, six passed. The seventh sits on an else-branch that is not reached when the parser is built.

### What runs it

What runs every block of this book? I ask the runtime for its version:

```haro
? version()
#--> 1.27
```

> run: kept

It prints `1.27`: the version of the former host language, the oracle against which the new runtime is judged. Haro does not run the library. Under a future runtime the promise changes, as the proof line says.

The decisions come next, and the first of them is about that future.

## 4. The decision, and what I refused

**I decided that the future is Haro, and not the former language.** My words of 7 October 2026, in the study's quotation, the bracket mine: the future is Haro, not [the former language], and the site must be clear about it. Haro's face of the former language will be maintained only so that the code already written continues to work. What is not carried is that language's runtime and its governance. The first ruling, on 28 August, was that it is not carried forward at all; it was superseded two days after, as the vision's amendment says.

**I decided that the rewrite is a rename.** The code of the articles, in the name of Haro, is the same as the former language's face. The charter measures the same: Haro's own stages run the same text, byte-identical on the new compiler and on the oracle.

**I decided that Haro is the language of languages.** The charter's header quotes my note of 1 October 2026. The charter was ratified that day, with my "go with your recommendations" on seven decisions. Its amendments of 4 October answer nineteen of the compass's questions, and the version stays ratified until I have read its section 15.

**I decided that the surface is kept.** Its surface today is the one the compiler compiles. The library is its compatibility specification. Other surfaces are faces over one program graph: every syntax a face, so that an AI agent fluent in the former language, in Python or in JavaScript writes Haro. Of these only the first face exists. A Python-shaped face is a spelling, not Python.

**I removed the old framework, with no fallback.** Engine-only: no fallback, no feature flags, no Qt dependency. The status of 12 June 2026 says zero of them remain. I checked. No loaded file loads a Qt library. Two external extensions are loaded by name: a zip one, which base loads, and a cryptography one, in a folder that no entry file loads.

**I directed that the language's own extensions be removed.** My directive of 13 June 2026: ensure that no external extensions are required, and that engine alternatives replace them. The library still loads one of them, a zip extension, as the entry above says.

**I put the engine in Zig, with no dependency on a library,** as the study reports my ask. It is qualified by the record's own definition of sovereignty: nineteen vendored libraries, each with a record.

**I let everything go into base.** My sentence, as the study reports it: under the pressure of time, everything went into base, waiting for the right moment to refactor again. By my count below, base is ninety-three per cent of the lines.

**I chose safe optimisation.** Not the fastest mode, and not the unoptimised one. I hold it as a view, not a result, that a clean panic beats silent memory corruption, and that here it costs nothing.

**I refused a headline that does not reproduce.** The memo of 13 September 2026 says the claim to retire is that the runtime beats the fast peer, present tense, on x64. Chapter 22 told the refusal, and section 6 prints the rows.

**I refused a percentage.** The figure is mine, and it should not be printed without the guard that produces it. Chapters 31 and 33 say so.

**I have no sentence on how a layer is chosen in Haro.** The study only proposes that, in Haro, layer selection should be a declaration the compiler honours. The charter has no text on core, base and max. Base inheriting core is the contract as designed, with the stage word designed. The code does not meet it today, as section 3 prints, and the book's account is what the code does: two implementations over one engine. And in Haro, a layer is chosen by the file you load, today. A declaration the compiler honours is the study's proposal, and is designed.

Section 5 reads what the court proves of all this, and what no guard proves.

## 5. The court

`engine_is_optimised_narrated` proves that the engine is compiled with optimisation: twenty sums over two million doubles under a tenth of a second, and the right answer. It proves that an index of 99 and an index of 0 are refused and the buffer unharmed, and that the vendored parser which the optimised mode once broke now answers. I ran it: six of the seven assertions in the file were reached, and six passed. `engine_senses_narrated` proves that the engine gives the process five senses: memory, its peak, system memory, processor time, and a bounded series. I ran it: thirty-six of thirty-six, and the run then stops with "STOPPED!" by design. `wasm_narrated` proves that the engine's entry for the browser exports its curated interface and that the build has a target for it. It builds a subset and asserts that it is smaller. I did not run it, because it calls a build of the toolchain. `threat_model_narrated` reads the threat model and checks that each guarantee row names a proof and that each guard file it names exists. Rows G11, the fuzz harnesses, and G25, the bill of materials with its digests, concern the engine.

What does not exist: **no guard judges the layers.** No file under the test folders loads a layer's entry file or reads the contract. There are 529 narrated guards in base, and none in core or in max. The study says 517 in one place and 387 in another, and the site 501; I print only what the build reads. And no guard judges the engine's counts: the numbers the engine's command-line status prints are typed constants dated 16 June 2026.

Section 6 sets the runtime beside the field, and the peer leads every row.

## 6. The field, and where it leads

**Speed.** The runtime beneath against a fast scripting runtime of the field, on 13 September 2026. The method is the memo's own: six pairs of kernels written fresh, identical algorithm and sizes on both sides, each side in its fast idiom, checksums across languages asserted before any number. The minima are over three inner repeats and two process runs, the new compiler built for speed, the peer interpreter-only with no JIT, on Windows, x64. The peer leads every row:

| row | the runtime beneath (min ms) | the peer (min ms) | the peer leads by |
|---|---:|---:|---:|
| sieve | 128 | 74.5 | 1.72 |
| matmul | 349 | 185.6 | 1.88 |
| fib | 57 | 50.2 | 1.14 |
| mergesort | 376 | 206.7 | 1.82 |
| binsearch | 536 | 513.1 | 1.04 |
| bytescan | 53 | 37.5 | 1.41 |

The memo's words: the peer leads every row, fib and binsearch are near-ties, and nothing is worse than 2x. ARM is unmeasured. The win that the memo keeps: within 2x on every row, which no version of the former runtime ever was.

**The headline is still alive in the repository's own notes.** As I read on 9 October 2026, the brief of the runtime's own repository and its notes still say that the spike beats the peers on every row. The correction is carried in another repository of the estate and in the memo. In the runtime's own record it is carried only for its release-candidate configuration, in one section of the notes. The memo asked for it. The memo of 13 September 2026 withdraws the claim, and the six rows above are its rows, although the repository's notes still carry the old claim. I name no peer, and describe it as chapter 22 does: a fast scripting runtime of the field.

**Memory.** On the same day the note says: resident, running the library, this morning 733 megabytes, now 149, and the former runtime 139. A loss of ten to the former runtime, after a fall of 584. A win and a loss in one note.

**Compatibility, on 5 October 2026.** The wide suite of the library was run on a snapshot. The note records parity of assertions on every one the former runtime passes, that most programs agree on every stable line, and that nineteen rows differ in kind. The note does not say Windows in that entry, and the Linux pass is listed as the next step. These are a session's notes from a private branch, and no number of mine. I print them, dated 5 October 2026, with the stage word in construction: 8,540 of 8,540 assertions at parity, 1,253 of 1,253 tests that bear assertions, and 3,425 of 5,112 programs identical on every stable line. Another 1,267 are identical but for the line that prints the elapsed time, and 19 rows differ in kind: 13 print more, 5 are refused or raise, one writes a stderr line. They are the note's counts, and I ran none of them.

**The platform.** Built and run on Windows today. A Linux build of eighty-five of the eighty-nine modules exists on a working branch; the site says it is in construction. A whole program with its engine in one file, with no dependency, is absent.

**The engine against the field.** The threat model's row for fuzzing says it itself: no scheduled or coverage-guided fuzzing, no continuous integration and unsigned commits, deferred by the author for the development phase. The field's maintained native libraries have continuous fuzzing and signed releases. And chapter 22's loss, unchanged: no collation by locale, and no time zones.

Section 7 says where the layers and the engine stop.

## 7. The limit

**The lean layer does not run.** What does a string of the core give back when I ask it for its content?

```haro
o = new stkString("abc")
? o.Content()
#--> Error (R3) : Calling Function without definition: stkenginestringfrom
```

> run: kept

The runtime answers: `Error (R3) : Calling Function without definition: stkenginestringfrom`. The core string cannot give back `abc`! The core string class calls engine names that no engine library registers. In a process of the core alone, the engine's core library registers five hundred and thirty-four functions under the base names and none under the core names. That count is from my notes, and no block shows it. So `stkString` and `stkChar` find nothing. The study files it as an open item of the core and the engine. `stkList` runs, which chapter 4 showed, and the load of seventeen classes in a tenth of a second is real.

**The lean layer is not lean at the binary, for strings.** By file size, on the build of 5 October 2026, the core string library is 22,355,968 bytes and the base one 22,362,624. The read-only data is 20.8 megabytes in both; I did not diagnose what it holds. The four core libraries total 24.1 megabytes of the eighty-nine libraries' 122.4. The core libraries for dates, files and locale differ from their base twins by under one per cent.

**The dependency rule holds at the loads, with one exception at a call.** I parsed every load of every non-test, non-archive file of core, base and max, 871 lines, and resolved each. Core loads, outside its own folder, only the engine face; base loads core and the engine; no file under base loads anything under max or future; max loads base. But `FindMin`, in the core's list of numbers, calls a function that is defined only in base. In a core-only process, `FindMin([4,2,9])` answers 2, and `FindMin("not a list")` raises "Calling Function without definition". In a base process it raises the intended error. I found one instance by a search for base names in core, and I did not look for others.

**On a case-sensitive disk the core entry file does not load.** Its second line loads a file by a name in the wrong case. My scan finds twenty such loads in non-test files at this commit; the runtime's session counted fifty-five with tests, on 8 October 2026. The book is built on Windows, which hides it.

**The third layer is written and not wired.** Its thirty-two classes are all in one folder, and no entry file loads them. The first of them works when loaded by hand. I ran it and do not show it, a string of eleven characters counted by it. I tried none of the other thirty-one. A library layer for them in the engine does not exist.

What is built: a layer is a folder, a prefix and an entry file. I counted on 9 October 2026 at this commit, by files with the extension, excluding test and archive folders. Core, 27 files and 6,366 lines; base, 984 files and 519,579; max, 115 and 31,292; and a folder of the future, 51 files and 6,356. Base is 93.2 per cent of the three layers' lines. The engine: eighty-nine libraries from the Zig sources, 401 source files, 179,985 lines, and 2,464 declared tests, which I did not run. The toolchain is Zig 0.15.2 by the build file's own comment. Nineteen vendored libraries, each with a record of component, version, source, licence and digest. The record's own gaps: an archive digest is recorded for nine of the nineteen, and three have no version.

What is designed: the base layer inheriting the core layer. The seven shared domains are implemented twice over the same engine. Max as a built layer. A loader for one domain of base. A court that checks the layers against their contract. The standalone engine repository and its command line, which the architecture lists as a phase. The engine's polyglot bridge, which is chapter 16's.

What is absent: a Linux and a macOS engine in service; a measured pass of the library on the new runtime under Linux; a single executable with no dependency; an engine test count that I may print.

### Haro

I tell what is built, what is designed, and what is absent, as the record has it on 9 October 2026.

**Built, as a charter, a family of grammars and a guard.** The charter, version 0.2, ratified on 1 October 2026. A spike of nineteen rungs, between 1 and 4 October, each a grammar document with fixtures. Its guard reported a pass of the whole run on 5 October. Its courts are programs that run byte-identical on the new compiler and on the official former runtime. The new compiler also formats and dumps the library's files: of about six thousand, nearly all print the reference's bytes, and a few dozen are refused by both. A first slice of a graph of the code was built on 5 October.

**What Haro is today, in one sentence the record supports:** a ratified charter and a spike whose courts run on the new runtime and on the old one, over the surface the library is written in. There is no `haro` executable. The folder of binaries holds the compiler and two others. The forged courts load no library. **Haro does not run the library.** The vision of 27 September said that Haro does not exist and that the new runtime's Linux row is unmeasured. The first half is out of date, since a charter and a spike exist. The second half is still true of the wide suite on Linux.

**Designed:** the three altitudes, declaring, declared, and computing; the alphabet of six letters, five forged whole in the spike; refinement as the write surface; other faces over one program graph. Those faces arrive as printers before they arrive as parsers, and never as semantics. The verbs `haro forge`, `check`, `refine`, `run`, `project` and `narrate` are a recommendation, and not a program.

**The runtime beneath, as the record dates it.** Its brief: a register machine and a compiler from the former language's source to its bytecode, running existing programs. About three hundred thousand lines of Softanza are its compatibility specification. Its public face: the main branch is public and untouched; the work lives on a branch pushed to a private remote only. Its last commit at my reading is of 8 October 2026, at 22:26. The stage word is mine, and it is "in construction".

The six doors follow, one for each reader.

## 8. Six doors

**The programmer.** You choose your depth by the file you load, and you can prove it in three fresh processes. The lean layer does not run its strings today: reach for base. Read the engine's count the way the library sees it, and not the way a page types it.

**The analyst.** Three numbers for "how big is the engine", and three methods. Ask which one a vendor means. The core library is the size of the base one for strings.

**The designer.** A layer is a decision about what you ship, and not about taste. At the binary, core and base have a library per domain and the third layer has none; the web subset, which chapters 4 and 24 show, is a subset and not a layer.

**The decision-maker.** The two questions of chapter 4, plus two. What runs it: version 1.27 today, with the replacement in construction. What the replacement lost: every row against a fast peer, by 1.04 to 1.88 times, and ten megabytes of memory to the old one. This is my view: a record that prints its loss is the only kind to trust.

**The educator.** Teach the dependency rule by making a learner load the core alone and predict, then count. Teach "measured, never asserted" with the memo of 13 September 2026.

**The agent.** You may count the engine's functions yourself. Do not repeat a count from a page, and do not write a loop over the list of classes directly. Tell the reader which layer a class lives in by its parent chain, and not by its prefix.

## 9. Exercise

Before you run anything, write three numbers: how many classes each entry file will load, and which of `stkList`, `stzList` and `stzListXT` each holds.

```haro exercise
# core/stkLib.ring, stzLib.ring, max/stxLib.ring: write your three predictions here,
# then load each entry in its own process and count with ringvm_classesList().
```

> run: exercise

Then choose any class of the library, predict its parent, and read it with the parent chain. Write the line your prediction got wrong. A learner who guesses that `stzString` inherits `stkString` is in good company: the contract says so, and the library does not. I do not say which of the 17, 674 or 714 is which.

I left this one in your hands. The count by prefix in section 3, `[ 10, 693, 0 ]`, is correct, and it says nothing about layers. Write that count again so that it asks each class's parent chain, read with `ParentOf`, and not its first three letters, and look at what you get. Section 3 says what the prefix hides, and section 8, the agent's door, says why I refuse it. When your count answers, you will know why a class's layer is read from what it inherits, and not from what it is called.

The next chapter leaves the engine for a restaurant in Lyon, and for the one sentence the project there taught: deliver small, fast and useful, and let the foundations mature in parallel without ever blocking a delivery.
