# Natural, and executable: two directions, one discipline

Source: Chapter 13. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: both directions: chains where the human is the parser, and sentences where the machine is; five language packs as data and a sixth added at runtime; refusals with reasons on both sides; question frames; a thin truth chain; natural code as data in documents and templates; designed: a grammar that holds a model to the lexicon; a guard that no socket opens during a natural run; the plan emitted as a chain; the article examples pinned as fixtures; absent: any machine that judges a chain's grammar; Ajami, Zarma and Fulfulde; a natural layer closed all the way down; a dictionary protected from the drift of the documentation it is read from; the old articles' promises, several of which do not run

Run: 17 of 17 blocks kept their promise, on 2026-10-09 03:26 UTC+01:00.

## 1. The concept, as the field holds it

In the field's common language, "programming in natural language" means one thing: asking a model for code, or asking it to do the task, in a prompt. The tools are chat assistants and code completers, in wide use since about 2021. What the sentence runs on is the model's guess. The same sentence may give different code on different days, the model needs a network or a local runtime, and a person reads the result to know what was understood. Chapter 11 said it, and I point back.

Older practices exist, and the record names them. Inform 7, a language whose programs are English sentences, compiled whole, with a world model and a way to say *it* across sentences. AppleScript, English-like and hard to write, because its naturalness was on the surface and not in a semantic model. Controlled natural languages, whose strongest device, the library's own comment says, is showing what can be said next. A session's reading of 30 August 2026 is that Inform 7 is a whole-text compiler with referential context, and not a command dispatcher. (General knowledge for the dates, not a study of the record.)

None of them is what the record claims. The claim is the opposite of prompting: a sentence executes because every word of it is in a closed lexicon, defined as data, mapped to a verb the library documents, and anything else is refused with the reason. And it has two directions, which the library's design review tabulates. In the first, the machine is the parser. In the second, the human is.

## 2. The first principle

**A sentence runs because every word of it is in a dictionary the library owns. What the library does not know, it refuses, with the reason.**

The study's thesis line for the page it asked for, and the lede of the site's page of 8 October 2026, say it. For the second direction, the design review's thesis: in near-natural language, the human is the parser. And the older motto, which chapter 5 carries: what you think is what you write.

## 3. The Softanza form

I start with the second direction, because it is the older.

### The human is the parser

A near-natural chain is a sentence in which every link is a real call. The sentence is "the word haro is a lowercase Latin word with a length of 4 letters and only 2 vowels". When it is false, the chain says why:

```haro
? TheWordQ("haro").IsAQ([ :Lowercase, :Latin, :Word ]).WithQ().ALengthQ().OfQ(4).UnitQ(:Letters).AndQ().OnlyQ(2).VowelNB()
#--> TRUE
? TheWordQ("haro").IsAQ([ :Lowercase, :Latin, :Word ]).WithQ().ALengthQ().OfQ(4).UnitQ(:Letters).AndQ().OnlyQ(1).VowelNB()
#--> FALSE
? Why()
#--> no: expected exactly 1, found 2
```

> run: kept

Degree words are devices, and the reason lives on the chain:

```haro
? Q("AnnIE").AtLeast(2).VowelNB()
#--> TRUE
? Q("AnnIE").AtMost(2).VowelNB()
#--> FALSE
? Why()
#--> no: expected atmost 2, found 3
```

> run: kept

The chain refuses what its subject cannot do. It speaks the same lexicon as the machine's direction: a French word works inside a chain. And a misspelled word is refused with the nearest word. This is "one lexicon, two directions" in three lines:

```haro
try
	Q(5).VowelNB()
catch
	? cCatchError
done
#--> NNL: a stznumber cannot count 'numberofvowels' -- and neither can the chain subject.
? Q("haro").IsAQ(:String).IfSo("majuscule").Content()
#--> HARO
try
	Q("haro").IsAQ(:String).IfSo("uppercse")
catch
	? cCatchError
done
#--> NNL: this stzstring does not understand 'uppercse'. Did you mean 'uppercase'?
```

> run: kept

A chain branches on its own truth, and an ordinal is a word:

```haro
? Q("haro").IsAQ(:String).IfSo(:Uppercase).Otherwise(:Reverse).Content()
#--> HARO
? Q("hello").IsAQ(:Number).IfSo(:Reverse).Otherwise(:Uppercase).Content()
#--> HELLO
? Q("hello brave world").TheNth(2, :Words)
#--> brave
```

> run: kept

Questions work the same way. A force word opens a frame, one word and one method. A tag question ends in "or not". The session keeps every answer and folds them, like a narration:

```haro
? @@( WhatQ().TheQ().VowelsQ().OfQ("AnnIE").Is() )
#--> [ "A", "I", "E" ]
? HowManyQ().WordsQ().Of("hello brave world")
#--> 3
ClearAnswers()
? IsQ().TheQ().LengthQ().OfQ("Haro").TheSameAsQ().TheQ().LengthQ().OfQ("Ruby").OrNot()
#--> 1
? Why()
#--> yes: 4 is the same as 4
? IsQ().TheQ().LengthQ().OfQ("Haro").TheSameAsQ().TheQ().LengthQ().OfQ("softanza").OrNot()
#--> 0
? Why()
#--> no: 4 is not the same as 8
? @@( AnswersSoFar() )
#--> [ 1, 0 ]
? AllYesSoFar()
#--> FALSE
? AnyYesSoFar()
#--> TRUE
```

> run: kept

### The machine is the parser

Now the other direction. The sentence is a string, and the library reads it. The same verdict can come from a narration of questions and from a chain of truth, and both say why and how sure:

```haro
oT = Naturally("Create a string with 'haro' Is it lowercase ? Does it contain 'r' ?")
? @@( oT.Answers() )
#--> [ 1, 1 ]
? oT.AllYes()
#--> TRUE
? oT.Understood()
#--> create a string with haro -> ask: is lowercase -> ask: contains
? TruthOf("haro").IsA(:Lowercase).AndIsA(:Latin).AndContaining("r").Holds()
#--> TRUE
? Why()
#--> yes: "haro" is lowercase and is latin and containing "r"
? Certainty()
#--> 1
? Evidentially()
#--> certainly
```

> run: kept

The whole paragraph is compiled into code before anything runs, and the code is readable. It is the library's own account of why the layer exists:

```haro
o1 = Naturally("Create a string with 'test.data' Replace '.' with '_' Uppercase it")
? o1.Result()
#--> TEST_DATA
? o1.Code()
#--> oStr = StzStringQ("test.data")
#    oStr.Replace(".", "_")
#    oStr.Uppercase()
#    @result = oStr.Content()
```

> run: kept

The same meaning in Hausa lands on the same code, and the program says back what it understood, in its own words. Hausa is written here without the hooked letter, as the pack reads it today, for a reason that chapter 11 gives:

```haro
oE = Naturally("Make a string with 'hello niger' inside Spacify it and uppercase it")
oH = NaturallyIn("hausa", "Yi rubutu da dauke 'hello niger' a ciki Raba shi kuma maida shi")
? oE.Code() = oH.Code()
#--> TRUE
? oH.Understood()
#--> yi rubutu dauke hello niger -> raba -> maida
? oE.Understood()
#--> create a string with hello niger -> spacify -> uppercase
```

> run: kept

The sentence-dictionary is not the only vocabulary. A word it does not hold is looked up in the library's own vocabulary, here the documentation tags of the uppercase verb. A value in quotes is data, and never a verb. An unknown word in a value position stays a literal:

```haro
? Naturally("Create a string with 'softanza' Capitals it").Result()
#--> SOFTANZA
? Naturally("Create a string with 'capitals' Uppercase it").Result()
#--> CAPITALS
? Naturally("Create a string with 'a-sep-b' Replace sep with '_'").Result()
#--> a-_-b
```

> run: kept

The third line is also a limit. The word `sep` was in no dictionary, and was used as the text to replace. A word it does not know is a literal.

**Four languages as data.** The dictionary is keyed by meaning, and each language's word lands on one id. French, Arabic and Turkish words land on the same one:

```haro
? StzResolveSemanticInLang("fr", "doublons")
#--> METHOD_REMOVEDUPLICATES
? StzResolveSemanticInLang("ar", "تكرارات")
#--> METHOD_REMOVEDUPLICATES
? StzResolveSemanticInLang("tr", "tekrarları")
#--> METHOD_REMOVEDUPLICATES
? StzResolveSemantic("removeduplicates")
#--> METHOD_REMOVEDUPLICATES
```

> run: kept

The languages follow their own grammar, and they are not word-for-word translations. Turkish puts the verb last, with the parameters before it. Arabic, with its vowel marks and a doubled letter, is stripped by the pack; the suffix on the verb is the masculine "it" for a text. French elides:

```haro
? NaturallyIn("tr", "'a.b' ile bir metin oluştur '.' yerine '_' koy").Result()
#--> a_b
? NaturallyIn("tr", "'haro' ile bir metin oluştur ve tersine çevir").Result()
#--> orah
? NaturallyIn("ar", "أنشئ نصا بـ 'haro' ثم اقلبه").Result()
#--> orah
? NaturallyIn("ar", "أنشئ نصًا بـ 'haro' ثمّ اقلِبْه").Result()
#--> orah
? NaturallyIn("ar", "أنشئ نصا بـ 'haro' ثم اقلبه").Understood()
#--> أنشئ سلسلة بـ haro -> اعكس
? NaturallyIn("fr", "Crée une chaine avec 'haro' et mets la à l'envers").Result()
#--> orah
```

> run: kept

No native reader has read these sentences. They are the guard's, and I do not know that a speaker has read them. [AUTHOR: Chapter 11 asked it of Hausa. Has a speaker read the Arabic, Turkish, French and Swahili sentences of the pack's guard?]

A language is a block of data. Here is Swahili, added at runtime, by the guard's own words:

```haro
StzAddNaturalLanguage([
	:code = "sw",
	:name = "swahili",
	:script = "latin",
	:ignored_words = [ "na", "ya", "kwa", "hii" ],
	:semantic_mappings = [
		[:natural = "unda",   :semantic = "CREATE_OBJECT"],
		[:natural = "orodha", :semantic = "OBJECT_LIST"],
		[:natural = "na",     :semantic = "VALUE_INDICATOR"],
		[:natural = "panga",  :semantic = "METHOD_SORT"]
	],
	:phrases = [
		[:semantic = "METHOD_REMOVEDUPLICATES", :words = "ondoa nakala, futa nakala"]
	]
])
? StzHasLanguagePack("sw")
#--> TRUE
osw = NaturallyIn("sw", "Unda orodha na [ 9, 4, 9 ] ondoa nakala")
? @@( osw.Result() )
#--> [ 9, 4 ]
? osw.Understood()
#--> unda orodha na [ 9, 4, 9 ] -> ondoa nakala
```

> run: kept

Natural code is data too. A document's fenced blocks run, and a template is filled:

```haro
cDoc = "This tutorial explains deduplication." + nl +
	"#<" + nl +
	"Create a list with [ 3, 1, 3 ] and remove its duplicates" + nl +
	"#>" + nl +
	"The end."
? len( StzNaturalBlocks(cDoc) )
#--> 1
? @@( NaturallyFromDoc(cDoc)[1].Result() )
#--> [ 3, 1 ]
cT = "Create a list with {#1} and remove its duplicates"
? @@( NaturallyWith(cT, [ [ 5, 3, 5 ] ]).Result() )
#--> [ 5, 3 ]
? @@( NaturallyWith(cT, [ [ 9, 9, 4 ] ]).Result() )
#--> [ 9, 4 ]
```

> run: kept

**What the packs can say.** The packs are honest about how much they say. The library has a function for it, and no guard prints its figures. I count against twenty-five reference meanings, which are the structural ones and every method and modifier any shipped pack names. They are not the thousands of verbs the library grew:

```haro
for cLang in [ "en", "ha", "fr", "ar", "tr" ]
	aC = StzPackCoverage(cLang)
	? cLang + " " + aC[:covered] + " of " + aC[:total]
next
#--> en 23 of 25
#    ha 9 of 25
#    fr 25 of 25
#    ar 16 of 25
#    tr 10 of 25
? StzHasNeuralModel()
#--> FALSE
```

> run: kept

The Hausa pack speaks nine of twenty-five meanings. And no model is loaded. The layer has an optional rescue by embedding, when nothing lexical was found and a model is loaded. At this commit none is, and none is needed. So I say "no model is loaded", and not "never touches a model".

### From the 2020 diagram to the three eras

The library names three eras, in a design document of 10 July 2026. The first is near-natural language, the first paradigm. The second is natural programming: lower the language toward code, with free text, and one object per block. The third, of 2026, is one lexicon shared by execution and documentation, multilingual packs with morphology, and `Understood()`. I call the third *the shared lexicon*. The vision's own heading for it uses a word this book does not use.

Here are the dates, as the record gives them. My strategic diagram carries the years 2020 to 2025, shared on 13 September 2026; its Narrations band reads "executable natural language". The deck of 2022 was exported on 20 September 2022, and its slide 2 says to express thinking in an executable natural language. The library's repository begins on 12 March 2022, and its history cannot date 2020 or 2021. The near-natural files and the engine at its present path were first committed between 16 and 19 September 2025. On 30 October 2025 languages became configuration. On 2 November 2025 string input replaced brace capture. On 9 July 2026 the lexicon was unified from the documentation tags. On 10 July 2026 the two design documents were written, and the audit of fifteen canonical examples found that four ran, and two of those answered correctly. The site's flagship page is of 8 October 2026. (The git dates come from the library's own repository, which the snapshot lacks, and all the commits cited are ancestors of the pin.) [AUTHOR: Which date does the chapter print for the first slide? The structure says "the 2020 slide". The record has the diagram of 2020 to 2025 and the deck of 2022; chapter 5 says "the founding slide of 2022".]

## 4. The decision, and what I refused

**I built it without a model, as a dictionary.** The design says everything in the natural folder attacks one wall: the semantic gap between a human intention and its execution. Its thesis: zero NLP, zero ML, native speed, full determinism, and the programmer in control. The layer quietly delivered a fourth promise that the old documents never dared to make: accountability.

**I decided on two directions, one discipline.** The review's table: who parses, a machine with a lexicon or the human; ambiguity, refused loudly or impossible by construction; vocabulary, bounded by packs or unbounded; understanding, verified by the machine or by a human reading; audience, domain experts and agents or programmers. Both end at the same place: a deterministic sequence of semantic operations.

**I refused markers on reference.** On 10 July 2026 I rejected the family of suffixes that marked a reference. The cipher was inverted by its own inventor from memory, it duplicated meanings, and language itself never marks reference this way. More than two hundred and sixty methods were removed. Chapter 11 tells it in two sentences.

**I refused the ungrammatical chain.** The chain is the sentence, and an ungrammatical chain that runs is a bug. The doctrine is held by reading aloud, not by a machine, and I show the proof below.

**I refused negation as a prefix.** Negation lives in negative forms, in antonym comparators and in the tag closer `OrNot()`. The tag question above is that ruling running.

**I refused silent tolerance.** The old typo tolerance was replaced by explaining everything: the refusal with the nearest word, above.

**I refused global context.** Two chains interleaved contaminated each other, and the fix put the context on the chain. The process-wide `Why()` remains as a convenience for the console and the tests.

**I refused the markup language.** Annotations that handed the machine what it could not infer governed by making the human annotate. The system governs by dialogue. Two seeds were kept as thin doors, and they are the document and the template above.

**I refused a command interpreter for narratives, and brace capture.** In my own words in the article: it is designed for commands, not narratives. And one object per block. The string form replaced the brace form, because natural code became a first-class data type, storable, versionable and searchable. The rule since relaxed: a program may name objects and switch between them.

**I refused governance inside the natural layer.** I ruled that scope out of the library on 12 July 2026, and the code was removed.

**I refused natural language as a way to declare.** It asks, and never declares.

## 5. The court

`nnl_narrated` proves the flagship sentence, the generated surface of nouns, the degree words, the conditional mood, the ordinal reference, the refusal that accounts for itself, the grammaticality doctrine, context on the chain, and the discourse tense. `multilingual_pack_narrated` proves packs as data, programs in French, Arabic and Turkish that run, verified affix stripping, a language added at runtime, and `Understood()` back in the program's language. `question_narrated` proves the question frames and that a frame with no aspect is refused. `literate_templates_narrated`, the documents and templates. `truthchain_narrated` and `interrogative_narrated`, the folded verdicts.

`semantic_resolver_narrated` is the guard that ought to protect the dictionary, and at this commit it fails. I ran it on 9 October 2026 and it stops with an error; a researcher's run on 8 October counted three assertions failed, and the run ended after the twenty-ninth. The word "caps", which the guard asserts, now resolves to a method for bounds, and "mirrored" resolves to nothing. The reason is the design's own: the vocabulary is read from the library's documentation tags, plus seventeen hand-written operations grown by reflection to about three thousand, so a documentation edit changes what a word means. The library refuses honestly in the second case: `Unresolved()` names the word and `UnderstoodAll()` prints 0. The court of the dictionary has failed on the dictionary, and chapter 11, chapter 22 and chapter 2 name this guard.

The other guards named above were run once each by a researcher on 8 October 2026, and passed all their assertions. The sum of the assertion calls in the eleven narrated guards of this form is 454.

## 6. The field, and where it leads

The field leads in breadth of phrasing. A model accepts any phrasing in any language, and the dictionary accepts what the packs name. Measured above: the Hausa pack covers nine of twenty-five meanings, Turkish ten, Arabic sixteen, English twenty-three, French twenty-five. And the sentence layer acts on three classes only: strings, lists and numbers. A customer's domain objects are not among them; the domain goes through the knowledge graph.

The field leads in whole-program semantics. Inform 7 compiles a whole world. Here a program is a sequence of operations on a live object.

The field leads in an editor. The suggestion function answers nine continuations for a half-written sentence, and the code credits the controlled-language field for the idea. There is no editor here that shows them as you type.

And there is a loss on the library's own side. `Understood()` prints verbs and not their arguments: `Replace` prints as `replace`, and `Add 3 to it` prints as `add` while the result was 8. A reader who checks the machine's reading sees no 3. This qualifies chapter 11's claim that a person can check what the machine understood.

Where the win is, with the loss beside it: the same sentence gives the same answer, with a reason, offline, in the user's language. The loss is that the user's language must be in a pack, and a word outside is a literal or a refusal. The record says the winning case is regulated or sovereign work: an instruction that executes locally and can be audited to the word.

## 7. The limit

An ungrammatical chain runs. The second chain below reads "which a length of 4", which is not English, and nothing judges it:

```haro
? TheWordQ("haro").IsAQ(:Word).WhichQ().HasQ().ALengthQ().Of(4)
#--> TRUE
? TheWordQ("haro").IsAQ(:Word).WhichQ().ALengthQ().Of(4)
#--> TRUE
```

> run: kept

The doctrine is that reviewing a chain is reading it aloud as English. It is the human's job.

A chain's descriptor reaches host code. `IsAXT` builds a string and evaluates it, so a function defined by the program and named in the string ran. This is the residue that the study of the record and chapter 6 name:

```haro
? Q("haro").IsAXT([ "String('x') and HostRan() and @isString" ])
#--> host code ran
#    TRUE

func HostRan()
	? "host code ran"
	return 1
```

> run: kept

And a word of the old era is reported, and never guessed. Permissive mode still runs the rest, and strict mode refuses. The suggestion offered, `addn`, is a poor one:

```haro
o = Naturally("Create a string with 'softanza' Spacify it and_ Uppercase it")
? o.Result()
#--> S O F T A N Z A
? o.UnderstoodAll()
#--> FALSE
? @@( o.Unresolved() )
#--> [ [ "and_", "addn" ] ]
try
	NaturallyStrict("Create a string with 'softanza' Spacify it and_ Uppercase it")
catch
	? cCatchError
done
#--> Strict natural mode: not understood: 'and_' (did you mean 'addn'?)
```

> run: kept

**The old articles have decayed.** The 2020 sentence needs a marker that I removed by my ruling of 10 July 2026. Several chains of the near-natural article do not run at this commit: `InLowercase()` raises for lack of an object; `LettersNB`, `BeforeQ`, `TheirQ().FirstCharQ()` and `ReplaceLowercaseCharsQ` are not defined; and the brace form `Naturally() { ... }` raises for too few parameters. Of the twelve chains of that article that I ran, eight work. The bridging article's paragraph still runs in permissive mode, and prints two nested boxes around "NOTHING SOFTANZA" instead of the one it promises. The machine said so, since `UnderstoodAll()` is 0 and the unresolved word is named, but a reader has to ask.

What is built: both directions; five packs as data and a sixth at runtime; refusals with reasons on both sides; the question frames, the thin truth chain, the evidential register; natural code as data. The folder holds thirteen files and about twelve thousand lines in twelve classes, by `wc` and `grep` on 8 October 2026.

What is designed: the plan of a narration emitted as an executable chain, so that chains gain `Understood()` for free. A grammar emitted for the natural lexicon, so that a model may only produce sentences the layer executes: I searched the folder, and no grammar emitter touches it. A guard that fails if a socket opens during a natural run, which does not exist. A coverage figure per pack printed by a guard. And the articles' examples pinned as fixtures.

What is absent: Hausa in the Ajami script, Zarma and Fulfulde. A natural layer closed all the way down: a plain list in a natural sentence reaches host code, which chapter 11 prints, and a descriptor reaches host code, above. Any machine that judges a chain's grammar. The standard Hausa letter, which the pack stores broken. A dictionary protected from drift. [AUTHOR: May the chapter tell your plea to the project of the former host language in your own words? The record has no sentence of yours in that voice, only a private memo of 30 August 2026 that quotes "seductive at first, unusable after".]

## 8. Six doors

**The programmer.** Write the chain as the sentence and read it aloud. The library refuses what its subject cannot do, and says why. You are the parser, so the sentence is only as grammatical as you are.

**The analyst.** A requirement can be a paragraph that runs, with a paraphrase that comes back. Today it acts on strings, lists and numbers, so the analyst's domain words go in a knowledge file (chapter 14), not here.

**The designer.** A designer's tone is in the refusals: a message names the word and the nearest word. The record has no designer-specific evidence for this chapter, and I keep the line short.

**The decision-maker.** Ask any "natural language" claim what it does with a word it does not know. Here it reports it, refuses it in strict mode, or takes it as a literal, and says which. It runs offline with no key. The no-network claim is not yet measured.

**The educator.** A learner writes in Hausa, French, Arabic or Turkish, and the program says back what it understood in the same language. The Hausa pack speaks nine of twenty-five meanings, and no reviewer has read the course's other-language editions.

**The agent.** Speak the lexicon. Use strict mode and an allow-list (chapter 11). Expect refusal with a reason. Your sentence is a proposal. A grammar that would hold you to the lexicon is designed and not built.

## 9. Exercise

Take one sentence you say about a word in your own language: that it is lowercase, has a given length, and a given number of vowels. Write it twice before you run anything. First as a near-natural chain, where you are the parser. Second as a `Naturally` sentence, where the library is. Under each, write the line you expect it to print.

```haro exercise
# 1. as a chain, where you are the parser:
# 2. as a Naturally sentence, where the library is:
```

> run: exercise

Then run both. Then change one word of the chain, and one word of the sentence, to a word the dictionary does not hold. Which direction told you? Which did you have to tell yourself? In one direction the machine tells you, and in the other you must tell yourself. If a promise breaks, do not change it: explain the output first.
