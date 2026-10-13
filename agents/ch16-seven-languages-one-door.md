# Seven languages, one door

Source: Chapter 16. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: a closed registry of six foreign runtimes and a process-based call that brings Python's and NodeJS's results home as lists; the trust postures; the twin's rehearsal of a spawn; a reader of Python and of JavaScript into one code graph; designed: the door governed, with a posture asked at the call; the engine's bridge and its three tiers; the domain library on top of the door; Haro wearing a Python syntax and a JavaScript one; absent: a door whose way back is closed; a door for R that runs; a passing run of a foreign runtime in the library's own court; the model as a door

Run: 10 of 10 blocks kept their promise, on 2026-10-13 09:43 UTC+01:00.

In this chapter I take the field's two lessons about reaching another language, an escape that is open and a border with no way out, and I put the door where they meet. I ask the door which languages it knows, run Python and NodeJS through it, read Python and JavaScript into one code graph, and show the governance refusing an executor with no posture. Then I say what I decided: one door, and no further host embeddings. And I say where the door stops at this commit: it is not governed, its way back is not closed, and the R door raises. The principle is the one chapter 11 promised: a facet is a syntax of one grammar and never a runtime, a door is a runtime and never a syntax, and the door is one.

## 1. The concept, as the field holds it

For a working programmer, reaching another language from the one you write means one of two things. The first is a foreign function interface, a call into a shared library. The second is a child process, a run of an interpreter whose output you parse. Notebooks and polyglot virtual machines make the same move with more comfort. (General knowledge. The record holds no dated study of these tools, and says so itself.)

The estate's own field study of August 2026 has two sentences on this, and they pull in opposite directions. On the way out, the host language is the escape hatch, and the escape hatch is always taken. It gives two internal languages that died of openness. On the way in, the differentiator is escape; a language you make must be consumable from any stack. It gives one language that stalled at the border of its own world.

So the lesson of the field is double. An escape that is open destroys a closed language. And a language with no way out dies at its own border. A door is where those two lessons meet.

There is a second habit, which looks like the first and is not. Tools that let you write in the syntax you know over another engine, a transpiler, a second front end for one compiler, I will call by the word of this book, *facets*. The estate's design memo for them is blunt about their cost. The promise of a second face is readability for a human who knows the other language, and not behavioural transfer.

## 2. The first principle

**A facet is a syntax of one grammar, and never a runtime. A door is a runtime, and never a syntax. The door is one, and it is the answer to "what about language X".**

The vision's own sentence, ratified in session on 28 August 2026, says it of the door: foreign code in the selected languages, governed, one door, with no further host embeddings. The study of the record reads the pair in a line I keep: the facet brings the programmer, and the door brings the ecosystem. Chapter 11 promised that this chapter would tell the difference; chapter 1 promised it the seven layers. Here is the difference.

## 3. The Softanza form

The door's list is closed. The foreign languages are a registry, and the host is not on it. Which languages does the door know? Ask it about six, then about the host, then about one that was never on the list:

```haro
oDoor = new stzExterCode(:python)
aNames = [ "c", "nodejs", "julia", "r", "prolog", "python", "ring", "cobol" ]
for cLang in aNames
	? cLang + ": " + oDoor.IsLanguageSupported(cLang)
next
#--> c: 1
#--> nodejs: 1
#--> julia: 1
#--> r: 1
#--> prolog: 1
#--> python: 1
#--> ring: 0
#--> cobol: 0
```

> run: kept

"What about language X" has one answer, and for a language not on the list it is a refusal by name:

```haro
try
	oNo = new stzExterCode(:cobol)
catch
	? cCatchError
done
#--> Language 'cobol' is not supported
```

> run: kept

The door refused it by name: `Language 'cobol' is not supported`!

Now the door runs a real runtime. A short note on the machine first. The door writes a script, starts the runtime by it, and reads a result file back. This book was built on a machine where Python lives at its own path, so the path is given as a short path without spaces. Node and R are at the library's default places. The blocks that start a runtime are marked, in the reader, as touching the system, and they show the output that was recorded on the date of the build.

What comes home from a Python call? The result arrives as the host's own structure, a list, and the call leaves a trace:

```haro
cPython = "C:/Users/ASUSV3~1/AppData/Local/Programs/Python/Python313/python.exe"
oPy = new stzExterCode(:python)
oPy.SetRuntimePath(cPython)
oPy.SetCode("
res = { 'numbers': [1, 2, 3, 4, 5], 'mean': sum([1, 2, 3, 4, 5]) / 5 }
")
oPy.Execute()
? @@( oPy.Result() )
#--> [ [ "numbers", [ 1, 2, 3, 4, 5 ] ], [ "mean", 3 ] ]
? oPy.CallTrace()[1][:language]
#--> python
? oPy.CallTrace()[1][:mode]
#--> interpreted
? isNumber(oPy.LastCallDuration())
#--> 1
```

> run: kept (touches the system)

The Python float `3.0` came back as `3`, in `[ "mean", 3 ]`. The trace also holds a duration. The block prints only `1`, the answer to `isNumber`, because a duration is a clock, and a clock cannot be promised.

That is the rationale of the whole plane, in one picture. Each layer of a solution is in the language best at it, and the host passes data in as text and reads data back. The library's own article lists the layers: system performance in C, event-driven systems in NodeJS, scientific computing in Julia, statistics in R, logical reasoning in Prolog, and machine learning in Python. It adds AI reasoning in a language model, and solution integration in the host. Here are two of them in a pipeline, Python computing the averages of two students and NodeJS deciding. The thresholds are mine; the data is the article's:

```haro
aStudents = [ [ "Alice", [ 85, 90, 78 ] ], [ "Bob", [ 72, 65, 70 ] ] ]
oPy2 = new stzExterCode(:python)
oPy2.SetRuntimePath(cPython)
oPy2.SetCode("
students = " + @@(aStudents) + "
res = [ [ s[0], round(sum(s[1]) / len(s[1]), 2) ] for s in students ]
")
oPy2.Execute()
aAverages = oPy2.Result()
? @@(aAverages)
#--> [ [ "Alice", 84.33 ], [ "Bob", 69 ] ]
oNode = new stzExterCode(:nodejs)
oNode.SetCode("
const avgs = " + @@(aAverages) + ";
const res = avgs.map(a => [ a[0], a[1] >= 80 ? 'Excellent' : 'Needs work' ]);
")
oNode.Execute()
? @@( oNode.Result() )
#--> [ [ "Alice", "Excellent" ], [ "Bob", "Needs work" ] ]
```

> run: kept (touches the system)

The data goes in by composing the code string with the host's own list printer, since the article's marshalling functions do not exist (section 7).

**Which seven?** The title commits to a number, and I ruled on 12 October 2026 which one: the six foreign runtimes of the registry above and the host, as the article on the plane and the article on performance count them. The language model is not one of them, because it is not a door of this plane at all. Chapters 17 and 20 make the model a proposer that cannot commit, while the narrations run it as a first-class runtime through a function that does not exist. Section 7 prints that as a limit. The record counts it differently elsewhere: seven domain modules with one for a language model, seven domains with the host as an eighth, the registry's six without the host, the vision's "7 selected languages" that it never lists, and the engine design's five with COBOL. The registry above is the one that runs.

**A facet is not a door.** Reading a foreign language is also not running it. The two languages that the author names as Haro's planned facets are also the two that the library can already read into one code graph. It does not run them and does not write them. One set of questions answers over both:

```haro
cPy = "class Animal:" + nl +
      "    def speak(self):" + nl +
      "        return '...'" + nl +
      "" + nl +
      "class Dog(Animal):" + nl +
      "    def speak(self):" + nl +
      "        return 'woof'"
cJs = "class Animal { speak() { return '...' } }" + nl +
      "class Dog extends Animal { speak() { return 'woof' } }"
oPG = StzPyCodeGraphFromSourceTS(cPy)
oJG = StzJsCodeGraphFromSourceTS(cJs)
? oPG.Language()
#--> python
? @@( oPG.ParentsOf("Dog") )
#--> [ "Animal" ]
? @@( oPG.OwnersOf("speak") )
#--> [ "Animal", "Dog" ]
? oJG.Language()
#--> javascript
? @@( oJG.ParentsOf("Dog") )
#--> [ "Animal" ]
? @@( oJG.OwnersOf("speak") )
#--> [ "Animal", "Dog" ]
```

> run: kept

This is a parser into an index of classes, methods and inheritance, and not a program graph that can print a program. It is a coincidence of the order of work, and not yet a facet. The record has one statement of mine on facets. I made it in session on 8 October 2026, and it says that a link should be made with the future vision of Haro and its facet languages. In that vision Ring (the host's former name) is already there, and Python and JavaScript are planned. The charter of Haro on this machine speaks of one grammar and one text. Its design memo for a second face, which proposes and rules nothing, calls them faces and recommends printers read by humans before any parser. Its own table lists the collisions: a Python reader expects zero-based indexing and Haro's is one-based. The chapter says "planned" only with that statement named as its source, and the memo's word for the same thing is face.

**A door is governed.** The governance has the word for foreign code. `external` is the posture the library defines as out-of-process. What does the governance answer before that posture is declared, and after? Ask it:

```haro
oGov = new stzGovernance("shop")
? oGov.MayExecute("python")
#--> 0
? oGov.Why()
#--> refused: 'python' has NO declared trust posture
oGov.DeclarePosture("python", :External)
? oGov.MayExecute("python")
#--> 1
? oGov.Why()
#--> allowed: posture 'external' declared
```

> run: kept

The refusal says why: `refused: 'python' has NO declared trust posture`. An executor with no declared trust posture never proceeds.

And the twin can rehearse a spawn before it runs, flagged as a risk. Chapter 24 owns the twin, and one block here is enough to say what the door does not use:

```haro
oTwin = new stzVirtualEnvironment()
oTwin.Spawn("python analyse.py")
? oTwin.NumberOfPendingSpawns()
#--> 1
oPlan = oTwin.GenerateUpdatePlan()
? oPlan.Narration()
#--> Update plan (1 of 1 operations to commit):
#-->   * 1. spawn process: python analyse.py
? @@( oPlan.Risks() )
#--> [ [ 1, "RUNS an external command (side effects): spawn process: python analyse.py" ] ]
```

> run: kept

Nothing is run there, and the plan flags the spawn: `RUNS an external command (side effects): spawn process: python analyse.py`. The script named does not exist.

Next, what I decided about the door, and what I refused.

## 4. The decision, and what I refused

**I decided on one door.** Its vision name is stzx, the door of the foreign languages, the x standing for external. The retired names are two older ones. The letter X was refused for algorithmics, because it would have sat beside the door, the clash that the vision's own file on the platform's letters named as its sharpest. The door took a letter and kept it.

**I refused further host embeddings.** The door is the answer to "what about language X". Chapter 1 promised this chapter on those words: seven languages were chosen for seven layers of a solution.

**I refused to surrender the domains to generated code.** The article on the domain library puts it as a stance. Rather than forcing programmers to master each domain, or to surrender to AI-generated code, provide carefully crafted abstractions. The site says the article has been in the repository since 23 April 2025 (read 9 October 2026). Its code is absent.

**I refused a facet as a runtime.** The study's plan says it in a line: a facet is a syntax of one grammar and never a runtime. So the door stays the only way to foreign code. It is a plan, proposed. It is not ruled.

**I refused an approximating printer.** The design memo's rule for faces: a printer refuses before it approximates. A face spells the graph and never gives it the meaning of Python or JavaScript.

Now the court, and what it proves of the door.

## 5. The court

`51_extercode_narrated` proves that the registry knows Python, R, Julia, Prolog, C and NodeJS, and rejects an unknown name. It proves that the lookup ignores case (tested for Python); that the code set is the code read back; and that the factory constructs and forwards. The smoke test it narrates says in its header: no `Execute` (the L99 guardrail). `governance_narrated`, scene six, proves that an execution without a posture refuses and that a declared posture proceeds and names itself; scene seven, that postures travel through save and load. `virtual_environment_twin_narrated` proves that a queued spawn does not run until commit, by a marker file; that a scope refuses; and that the plan narrates and flags the spawn. `pycodegraph_narrated` and `jscodegraph_narrated` prove classes, methods, inheritance chains, owners, impact and cascade over Python and over JavaScript sources, offline and without the runtime. Both skip their parser scenarios when the engine's tree-sitter is absent, and the first also skips its Python-AST ones when Python is not on the path.

I want to be exact about the court of the door. No guard in the snapshot runs a foreign runtime and passes. The door's court is a registry and a construction test. The folder's own run record, under an older runtime version, lists thirty-seven failures. Several promises cannot match by construction, because the file names carry a random suffix and the calls a duration.

The field comes next, and where it leads.

## 6. The field, and where it leads

The field leads in speed, and speed is what the door exists for. The article on performance measures seven runtimes on three tasks, and the host comes last in two of them. I carry its caveats from chapter 22: it has no versions and no dates inside its text, and it says that its times are relative to a specific computer environment. Sorting a million elements takes the host about thirty seconds and Python about four, in the article's table. I print no more of it.

The field leads in runtimes it can actually run. Of six doors, three ran on this machine: Node, Python, and R, which raised. The other three had no runtime to start. The study says its description of the field's polyglot tools was written from the genre and not re-read, and I claim no measured comparison.

The field leads in the ecosystem and in being used. The compare page speaks of Python only as a rival; to cover its thirty rows in Python you assemble numpy, pandas and others. The door is how a Softanza solution takes them without leaving. I hold this as a view, not a result: section 3 shows the door carrying two runtimes in one pipeline, and nothing on this page runs numpy or pandas.

The field's other loss is that the foreign process is outside the court. Chapter 21's threat model puts code already running in the process out of scope.

And the cost of a facet, in the memo's own table: a Python reader expects zero-based indexing, and Haro's is one-based. The literal `\n` is a backslash and an `n`; two letters of different case are one variable. "Any model writes Haro in the shape it knows" is true only of the spellings that are the minority.

## 7. The limit

The word *governed* is a design. Does the door ask the governance before it runs? This is the block that shows it:

```haro
oGov2 = new stzGovernance("shop")
? oGov2.MayExecute("python")
#--> 0
oPy3 = new stzExterCode(:python)
oPy3.SetRuntimePath(cPython)
oPy3.SetCode("res = 6 * 7")
oPy3.Execute()
? oPy3.Result()
#--> 42
```

> run: kept (touches the system)

The governance said no, and the door ran anyway, and returned `42`! Nothing in the door's folder mentions governance or posture. The door calls the system directly, and not the twin.

The way back is not closed. The result file is read by the host's own `eval`, and a string that comes out of the foreign runtime is wrapped in single quotes without escaping. Can a foreign string that carries a quote and a call reach host code? The function used here is `upper`, harmless on purpose:

```haro
oPy4 = new stzExterCode(:python)
oPy4.SetRuntimePath(cPython)
oPy4.SetCode(`
res = "x' + upper('y') + 'z"
`)
oPy4.Execute()
? oPy4.Result()
#--> xYz
```

> run: kept (touches the system)

The result file held `'x' + upper('y') + 'z'`, and `Result()` evaluated it. The data became a call, and the block printed `xYz`! A plain apostrophe in data, `it's fine`, writes a string the host cannot read, and the method prints the error and returns the raw text. It is the same defect class as chapter 11's list in a natural sentence. I did not test the other five languages' marshalling.

The R door raises on every call, because its generated script is not valid R. It holds an identifier that begins with an underscore, which R rejects. I confirmed it with R on a one-line file. And the trace records an exit code of 0 for a call that failed. The code passes a literal 0 to the recorder, and failure is detected only by the absence of the result file:

```haro
oStat = new stzExterCode(:R)
oStat.SetCode("res <- c(1, 2, 3)")
bRaised = 0
try
	oStat.Execute()
catch
	bRaised = 1
done
? bRaised
#--> 1
? oStat.CallTrace()[1][:exitcode]
#--> 0
```

> run: kept (touches the system)

The call raised, and the trace still holds `0`! R's message was in French on this machine, so I do not promise it. This is the limit of the door at this commit, in the voice of chapter 11's open list. The runs above are its evidence. The door is not governed, so the vision's word "governed" stays a design. It is not closed on the way back, since data returns through a file that the host evaluates. And the R door raises on every call.

What else is designed: the engine's own polyglot bridge, which the engine design marks as planned. A module of the same name in the macroplan, a string registry, was once marked done with no source. Then the three tiers for Python, of which only the external subprocess exists. Then the domain library on top of the door, none of whose classes I found in code. And the facets, a memo that proposes and rules nothing.

What is absent: the article's functions that bring data in, `@@R`, `@@C`, `XC()` and `XAI()`, which are defined in no file. Factories exist for Python, R, Julia and Prolog. The C and NodeJS doors are reached only by the class. The model is not a door of this plane at all; the article's function that runs it inside the host is the opposite of chapter 17's law, and the book does not teach it.

And a door shape I did not run: Julia, C and Prolog, for which no runtime is installed here. And a third relation, named in the study beside the door: the shim that pastes a solution found on the internet in another language and changes it a little. `range0`, Python's range as a host function, has a guard. The folder's own record lists for it five failures on ranges that should be empty and one on the slice form `':5:-1'`. I ran none of it.

Six readings of the door follow, one for each person who meets it.

## 8. Six doors

**The programmer.** You write Haro and, for the layer another language does best, you hand it a string of code and a list of data and take a list back. In the plan, a Python or JavaScript programmer will also write Haro in a syntax they know. Two different things: a syntax brings you, and a runtime brings your libraries.

**The analyst.** The statistical layer is R's, the machine-learning layer Python's, the logic layer Prolog's. You stay in one file and one list of results. Today the R door raises, and the record says so.

**The designer.** There is nothing to design at the door itself. The record's lesson is its refusal: a language not on the list is refused by name, and "what about my language" has one answer.

**The decision-maker.** The door is the one place where the closure ends, by decision. At this commit it is not yet governed and its way back reaches host code. The vision's word "governed" is a design. Every call's duration is recorded in the trace today.

**The educator.** A learner sees which layer belongs to which language and runs a two-door pipeline. The lesson is the difference between reading a language, running it, and writing in its syntax.

**The agent.** You never reach the door by yourself. A function in an agent's file must carry a posture, and `external` fits a foreign runtime; and a model has no capability to produce effects (chapter 20).

## 9. Exercise

You are building a small solution with three jobs: sorting a million numbers, deciding which of two students passes, and checking a family tree for who is an ancestor of whom. For each job, choose the language from the list of layers in section 3 that owns its layer, and write your reason in one line. Then, without running anything, write the promise for each line of this block, and run it:

```haro exercise
oDoor = new stzExterCode(:python)
# promise: the door answers "julia" with ...
# promise: the door answers "ring" with ...
# promise: asking for "cobol" raises with the sentence ...
oGov = new stzGovernance("mine")
# promise: oGov.MayExecute("prolog") before any posture is declared gives ...
# promise: after oGov.DeclarePosture("prolog", :External), it gives ...
```

> run: exercise

The last promise is the one that matters. If you now call the door for Prolog, will the governance have been asked? Write yes or no, and why. Then read section 7. If a promise breaks, do not change it: explain the output first.

Chapter 17 opens the part on intelligence with its law: programmatic by default, the model last, admission over generation. A model there is one faculty among others, the last one called, and what it says is a proposal that the court admits or refuses.
