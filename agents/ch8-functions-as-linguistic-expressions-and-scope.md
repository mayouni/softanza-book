# Functions as linguistic expressions, and scope

Source: Chapter 8. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: fourteen of the twenty-two forms, some with examples other than the article's, and three more in another shape; the library reading a name as a sentence; scope in the regex verbs, in the system and in the placement of a deployment; designed: the forms declared once as data and generated, in Haro; the scope paradigm for time, units, memory and style; absent: five forms: partial, future, free, default and multilingual; concurrency as a scope: a plan with no code

Run: 13 of 13 blocks kept their promise, on 2026-10-14 11:10 UTC+01:00.

In this chapter I read a function's name the way the library reads it: a sentence whose prefixes, suffixes and parameters are a grammar. I walk the forms of a name that run, and I count the five that do not. Then I turn to scope: the same verb, three verdicts, with the frame in the verb and not in a flag set earlier. I say what Haro's design keeps of the forms, what it refuses, and what the court proves. The principle is this: a function's name is a sentence, and its prefixes, suffixes and parameters are a grammar that the library can read.

## 1. The concept, as the field holds it

In the field, a function's name is a label. It follows a convention, camel case or snake case, and it tells you roughly what the function does; the details are in the signature and the documentation. A name does not carry grammar. The related tools are all about structure. Python and Swift offer the keyword argument, so that a call can say which parameter is which. The fluent interface chains calls so that a line reads like a sentence, and the overload gives one name several signatures.

And when the field wants a function to behave differently in a different context, it changes its meaning by a flag set somewhere else. The flag is a mode, a locale, an environment variable. The function's name does not tell you which frame it will run in.

## 2. The first principle

**A function's name is a sentence, and its prefixes, suffixes and parameters are a grammar that the library can read.** The paper that first made the claim says, in the words the study of its roots quotes, that it was achieved "without machine learning or NLP systems". It was done by naming conventions that encode meaning, a parameter order that mirrors speech, flexible forms and intelligent defaults.

## 3. The Softanza form

Look at a name the way the library looks at it. `FindNextSTCS`: find next, from a start position, with a case flag. `RemoveManyCS`: remove, many things, a case flag. Each suffix is small and means one thing, and, in these names, the order of the suffixes is the order of the parameters. Here the first name finds. What does the second leave when it removes every occurrence of three letters, whatever their case? Run it:

```haro
o1 = new stzString("123456789HARO")
? o1.FindNextSTCS("haro", 5, FALSE)
#--> 10
o2 = new stzString("SOOooooFFfffTANNnnnZA")
o2.RemoveManyCS([ "o", "f", "n" ], FALSE)
? o2.Content()
#--> STAZA
```

> run: kept

The article promised `SOFTANZA` on the second line. The run prints `STAZA`! The code is right and the article is wrong: a removal that does not care about case removes the capitals too. I print the run.

Does the library only follow this grammar, or does it read it? Its name parser, `_StzParseName`, is an internal helper that no guard covers. The public way in is `ExplainMethod`, which explains a method in those terms:

```haro
? @@( _StzParseName("FindNextSTCS") )
#--> [ "find next", [ "case-sensitive", "from-position", "active" ] ]
? @@( _StzParseName("RemoveManyCS") )
#--> [ "remove", [ "case-sensitive", "plural", "active" ] ]
? StzSelfDocQ("stzString").ExplainMethod("RemoveMany")
#--> RemoveMany -- Remove every occurrence of each given substring (mutating).
#-->   (plural form -- applies the operation to many items at once)
#-->   reads as: remove -- over many values at once
```

> run: kept

It reads it. That is the claim, made mechanical: the grammar is in the code and not only in the article. The printed line `reads as: remove -- over many values at once` is the parser's reading of `RemoveMany`. The parser decodes the prefixes and the suffixes, the words "except" and "is not", and the voice: a name that ends in `ed` is passive.

I will walk the forms now. Chapter 5 showed four of them: the active, the passive, the fluent and the named parameter. Here are the others that run.

**Z and ZZ** say whether a position comes as a number or as a section. A suffix, and the answer changes shape:

```haro
o1 = new stzString("haro php haro ruby haro")
? @@( o1.FindZ("haro") )
#--> [ 1, 10, 20 ]
? @@( o1.FindZZ("haro") )
#--> [ [ 1, 4 ], [ 10, 13 ], [ 20, 23 ] ]
o2 = new stzString("SOFTANZA")
? @@( o2.FirstHalfZ() )
#--> [ "SOFT", 1 ]
? @@( o2.FirstHalfZZ() )
#--> [ "SOFT", [ 1, 4 ] ]
```

> run: kept

**The prefix viz** changes the kind of answer: a drawing. The position is shown under the text, and an option can number it:

```haro
o1 = new stzString("fjharoljharodjharog")
? o1.vizFind("haro")
#--> fjharoljharodjharog
#--> --^-----^-----^----
? o1.vizFindXT("haro", [ :Numbered = TRUE ])
#--> fjharoljharodjharog
#--> --^-----^-----^----
#-->   3     9     15
```

> run: kept

**The plural** extends a verb to many things without a loop, and **the exceptional form** keeps only what you name. The article's example for the second, `RemoveNonLettersExcept`, does not exist. The form does, in other names:

```haro
o1 = new stzString("__H~~~AR***O__")
? @@( o1.FindMany([ "~", "*" ]) )
#--> [ 4, 5, 6, 9, 10, 11 ]
o1.RemoveMany([ "_", "~", "*" ])
? o1.Content()
#--> HARO
o2 = new stzString("--Haro--&__Softanza__")
o2.RemoveAllExcept([ "Haro", "&", "Softanza" ])
? o2.Content()
#--> Haro&Softanza
```

> run: kept

**The negative** is a word in the name, not a NOT around the call:

```haro
? Q("*").IsNotLetter()
#--> TRUE
o3 = new stzList([ "R", "I", "N", "G" ])
? o3.IsNotAString()
#--> TRUE
? o3.DoesNotContain("♥")
#--> TRUE
```

> run: kept

**The deep form** answers a path, a list of indices that goes as deep as the data does, and the same family replaces and removes at that depth:

```haro
o1 = new stzList([ "you", "other", [ "other", "you", [ "you" ], "other" ], "other", "you" ])
? @@( o1.DeepFind("you") )
#--> [ [ 1 ], [ 3, 2 ], [ 3, 3, 1 ], [ 5 ] ]
o1.DeepReplace("you", :By = "♥")
? @@( o1.Content() )
#--> [ "♥", "other", [ "other", "♥", [ "♥" ], "other" ], "other", "♥" ]
```

> run: kept

**The immutable form**, QC, runs the whole chain on a copy. After that chain, what does the original hold?

```haro
o1 = new stzString("haxxrxo")
? o1.RemoveQC("x").UppercaseQ().Spacified()
#--> H A R O
? o1.Content()
#--> haxxrxo
```

> run: kept

The chain printed `H A R O`, and the original still holds `haxxrxo`!

**The misspelled form** is accepted, with a note on what stands behind it. A misspelling of a name works:

```haro
? Q("   Haro ").WithoutSapces()
#--> Haro
```

> run: kept

The article says the library recognises and corrects minor typos, and that the intelligence resides in the library itself. The code shows how the form works: `WithoutSapces` works because that spelling was written by hand as an alias. Another misspelling, `WithoutSpces`, fails. So the form is real, and in what I traced it is a list of declared aliases; the correction engine the article describes is not among what I traced. I did not trace every file that mentions correction; one message in the object class only suggests a name, with "Did you mean".

Now the scope half of the chapter. The same fault shows up everywhere in programming: behaviour with an invisible governing frame. I hold this as a view, not a result; what stands behind it here is three instances: the regex verbs, the system and the placement of a deployment. A function does one thing here and another there, and nothing in its name says which frame it is in. The answer, in four moves, is the paradigm I call scope-oriented programming. Name the hidden frame. Turn it into a small, closed set of named scopes. Choose the scope at the call site, in the verb, and not in a flag set earlier. And give the library the scope to reason with, a semantic handle and not a comment.

It was born in regular expressions, where the frame is how much of the text a pattern must cover. The same pattern, the same text, three verbs: what does each answer?

```haro
cText = "First: Line1" + nl + "Second: Line2" + nl + "Third: Line3"
o1 = new stzRegex("^Second:.*$")
? o1.Match(cText)
#--> FALSE
? o1.MatchFirst(cText)
#--> FALSE
? o1.MatchLine(cText)
#--> TRUE
```

> run: kept

`Match` answers `FALSE`: it asks whether the pattern covers the whole value. `MatchFirst` answers `FALSE` too: it asks whether the pattern occurs anywhere, with the line anchors off. `MatchLine` answers `TRUE`: it makes `^` and `$` bind at each line. The frame is in the verb. There is a word scope too, which supplies the word boundaries so that you do not write them. It rewrites the pattern of its object for good, which is why the second instance is a new object with the same pattern. Does the same pattern answer alike under `MatchFirst` and under `MatchWord`?

```haro
o2 = new stzRegex("pre\w+")
? o2.MatchFirst("compress")
#--> TRUE
o3 = new stzRegex("pre\w+")
? o3.MatchWord("compress")
#--> FALSE
```

> run: kept

The same pattern answers `TRUE` under `MatchFirst` and `FALSE` under `MatchWord`!

The second instance is the system. Feature code is written in a named scope, and the same verb gets a different verdict in each. The scope can make a laptop behave like a device it does not have, or refuse what the target forbids. Here, one solution with a backend on a Linux server and a firmware on a small board. What does each system answer when the same verb, `Spawn`, is asked of it? Run it:

```haro
oSol = new stzPlatformProfile("my-iot-product")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oSol.WithApp(:firmware, :ESP32)
oBack = oSol.App(:backend).System()
oFirm = oSol.App(:firmware).System()
? oBack.Spawn("worker")
#--> native
? oFirm.ReadPin(4)
#--> rehearsed
try
	oFirm.Spawn("worker")
catch
	? cCatchError
done
#--> scope 'esp32' (espidf) forbids 'process' -- spawn 'worker'. This target has no such capability.
```

> run: kept (touches the system)

The same verb, `Spawn`, has two verdicts! The server answers `native`; the board answers `scope 'esp32' (espidf) forbids 'process'`. The scope decides, not the operation. And the laptop has no pin to read, so the scope answers `rehearsed`. This is the fifth move: when a scope's capabilities differ from the host's, the library bridges the difference, in both directions. Two declared systems can be compared as data, with a closed set of capabilities:

```haro
oEsp = DeclareSystem("esp32-firmware")
oEsp.SetOSName(:rtos)
oEsp.SetCapabilityList([ :gpio, :network, :clock, :threads ])
oBox = DeclareSystem("laptop")
oBox.SetOSName(:windows)
oBox.SetCapabilityList([ :filesystem, :process, :network, :clock, :threads ])
? @@( oBox.Forbids(oEsp) )
#--> [ "filesystem", "process" ]
? @@( oBox.Requires(oEsp) )
#--> [ "gpio" ]
```

> run: kept

The run printed `[ "filesystem", "process" ]` for what the laptop can do that the board cannot, and `[ "gpio" ]` for what the board needs that the laptop lacks. That is the second instance. The third is deployment: the target is the frame, and the scope decides not to ship what the target already does well; chapter 4 showed the plan. The fourth is concurrency, and it is a plan.

The design is next, with what Haro keeps of these forms and what it refuses.

## 4. The decision, and what I refused

**In the Haro design, principle 7 makes forms a grammar that the language owns.** It is designed and not built: the forms are declared once, and the compiler would generate and check each family. The passive form may not mutate; a verb with Q returns the object; suffix order is parameter order; a W takes a literal parsed at compile time. The spike judges names only: it does not read bodies and it does not judge suffix order. Its first measure is the library's string class: of its 595 shipped spellings of the verbs find, replace and remove, 584 agree with the declaration and 11 do not. I told in chapter 5 what Haro refused as grammar: the misspelled form, the free order of parameters and per-language method names. Here is what it means for this chapter: five forms do not run.

**The future form was trimmed on purpose.** The header of the natural-code file dates it 10 July 2026: the global queue of deferred actions left, and its FQ and FFQ wrappers were already gone. The reason is written in the design: natural language demands building the whole computational model before executing, and the engine's token plan now does that. It is a plan of the natural engine and no longer a suffix.

**The conditional form changed its mechanism.** The narration says it no longer goes through `eval()` but through a small text language that the engine compiles, and that the old extended form, WXT, is now a deprecated alias of W.

**For scope, the design document refuses the floating current.** Feature code is never written against an ambient "current system". It names its scope. And for concurrency the document records two refusals before there was any code. One is a method per operation that smears the frame across many verbs, such as `DoubleEachConcurrently`. The other is a mode set earlier. That mode is the antipattern this paradigm was founded against. It also refuses a scope that no host can perform. Its first guess for concurrency was thread vocabulary, and the language beneath has no threads.

**I refused to ship the whole engine to the edge.** The placement rule is: ship only what is critical and either unique to Softanza or weak on the target. A target that already excels at something gets nothing shipped.

Now the court, and which guards prove which of these claims.

## 5. The court

`00_regex_narrated` proves the verbs `Match` and `MatchFirst`: `Match` anchors, `MatchFirst` searches, Z hands back positions and does not print them. It asserts nothing for `MatchLine` and `MatchWord`: the blocks above show them, and only classic blocks, which are not guards, cover them. `972_narration_viz-finding_a_recurring_substring` proves the drawn answer. `full_scope_model_narrated` proves the system scope, with its three verdicts. `system_scope_model_narrated` proves the closed set of capabilities; one of its assertions is a timing limit, and in one probe run under load it did not hold, a run `data/` does not record. I print it beside the proof. `delivery_narrated` proves the placement plan.

Where the field does better comes next.

## 6. The field, and where it leads

The field leads in convention. A name that is a label is easier to teach and easier to type. The grammar of this chapter has to be learned, and some of its forms are rarely used.

The field leads in the guarantee. Python's keyword arguments are checked at the call, and Swift's labels by the compiler, for every function, from the first day. The forms here are judged by the Haro spike, on names and not on bodies, and by the library's own parser, and only in the names that follow them.

On scope, the field leads in maturity. The closest field practice is the explicit context: the Go habit of passing a context to every call, a locale object that carries a frame. They are older and more widely used. What this paradigm adds is that the frame is one of a small, closed set, chosen in the verb, and the library can reason with it.

Last, the limit, with what is built, what is designed and what is absent.

## 7. The limit

What is built: fourteen of the twenty-two forms of a name run, some with examples other than the article's, and three more run in another shape. The library reads a name as a sentence. And scope runs in the regex verbs, in the system, and in the placement of a deployment. The article counts twenty-three sections: the twenty-two forms of a name, and "small functions", which are functions and not a form of a name. The book's number is twenty-two, the forms of a name.

What is designed: Haro's forms as data, with generated families; and the scope paradigm for time, units, memory and style, as rows of a table.

What is absent, and the page should say each with what exists beside it:

- **Partial**, `@Removed`, is in the archive only: the call is not defined.
- **Future**, `BeforeQ`, was trimmed on purpose, as I said.
- **Free**, the suffix that lets a call give its parameters in any order and any subset: there is no definition of it outside the archive. The library's own parser knows the name `FX` and not `FF`. The two narrations that tell it use two names, and the code has neither.
- **Default**, `dftRange` and `infRange`: not defined; the library's comment calls the informing form not yet built.
- **Multilingual**, a method named in French or Arabic: not in the live library. The names exist in the archive. The nearest thing today is the language packs of chapter 11.
- The three that run in another shape. The exceptional form exists, but the article's example does not. Free order works for the first order only: in my probe of 8 October, the swapped call ended the program with a status of one and printed nothing. And the statement form is half in place: the "All" half works, and the "No" half is the next step. The library's own classic test promises true on two of its four "No" lines, and the run prints false on all four.

On the scope side: the regex verbs differ from the design table in two places. `MatchLine` lets a dot cross a line, where the table says it stays within one, and `MatchOneSegment`, which the table offers for the lazy case, is not defined. The system scope is built, and the design document still calls it designed: the record contradicts itself. The scope design document, version 1.2 of 16 August 2026, is quoted here as the document's text. The record does not say who wrote it, and I do not print it as mine. The system foundation document of 20 July 2026 says the foundation is implemented. In one probe run, which `data/` does not record, 61 of the 62 assertions of its narrated guard passed, and the one assertion that did not hold was a timing limit. I state what the code does: the system scope is built, with that result printed beside it, and the design document's word "designed" is the document's, out of date. And concurrency is a plan of record with no code: the word `Concurrently` has no definition.

## 8. Six doors

**The programmer.** Read a name as a sentence: its suffixes are its parameters, in order.

**The analyst.** A position can come as a number or as a section; a name says which.

**The designer.** The prefix changes the kind of answer: viz draws it.

**The decision-maker.** A scope is chosen in the verb, so the frame is visible where the call is made, and a review can see it.

**The educator.** The library parses a name into its sentence, so a learner can ask it what a method says.

**The agent.** Write the scope in the verb. A call that names a scope is not moved to another frame by a flag set elsewhere.

## 9. Exercise

Take one verb from a library you use that behaves differently in two frames: a mode, a locale, a target. Say in one sentence what the hidden frame is. Then write, as you would like it to be, two names for the same act in the two frames, with the frame in the verb. Before you run anything in Softanza, take `Match` and `MatchLine` on a text of three lines and write what each prints for a pattern that anchors at the start.

Run it. If your two names differ only by a flag, you have not yet moved the frame into the verb.

I left this one in your hands, on purpose. In section 3 the article promised `SOFTANZA` from a removal, and the run printed `STAZA`. Here is that block with one change, the last argument of the call:

```haro exercise
o2 = new stzString("SOOooooFFfffTANNnnnZA")
o2.RemoveManyCS([ "o", "f", "n" ], TRUE)
? o2.Content()
```

> run: exercise

Run it. Set what it prints beside what the article promised and beside what the first run printed. Section 3 says why the first run did not give the article's line; I do not print what this one gives. When you have solved it, you will know what the case flag decides in a removal, and whether it alone can keep the article's promise.

Chapter 9 turns to patterns of thought. It presents the Softanzuter, a computational representation of a thinking machine. It is based on one or many Regexuters, which identify and react to patterns of thought. With it come Reaxis and the engines.
