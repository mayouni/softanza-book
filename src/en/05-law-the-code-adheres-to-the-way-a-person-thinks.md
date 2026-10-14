---
id: law-the-code-adheres-to-the-way-a-person-thinks
part: 2
number: 5
title: "Law: the code adheres to the way a person thinks, and the court judges it whoever wrote it"
law: "the code adheres to the way a person thinks, and the court judges it whoever wrote it"
spine: true
narrations: [stz-mental-mode-narration.md, stz-bridging-minds-and-code.md, stz-functions-as-linguistic-expressions.md, stzobject-history-narration.md, stz-near-natural-language-programming.md]
site: [learn, craft, principles]
guards: [coderule_narrated, testoor_promises_narrated, 05_containsemptystrings, 466_keeping_the_history_of_updates_of_a_softanza_objec]
stage:
  built: "the forms of the vocabulary in thousands of method names; the house rules as a court over the library's own code; the promise read by a machine in the house's own form"
  designed: "a court of style for the code a programmer or an AI agent writes; the writing grammar declared in Haro, so an AI model can only write in it"
  absent: "any machine that judges today the style of a program written with the library"
status: draft
rulings: ["12.2", "12.3", "12.14", "12.16", "12.17", "12.21"]
research: research/ch05.md
figures:
  - "promises per thousand lines, 98.9 / 75.1 / 52.5 / 0.7: study 12.16, measured at stzlib 93d7a39"
  - "fourteen house rules: StzCodeRuleNames(), run in chapter 32"
---

In this chapter I take the two things the field calls coding style and ask the question it does not ask: whether a line follows the order in which its writer reasoned. I run the founding example in the nearest form that still runs, then the mental model on a list, the verb's forms, the named parameter, the scene and the history of a chain. A promise stands under every question. I say what I let go, the library's own implementation, and what I refused to let go, the style of the code written with it. I show the court that exists today, over the library's own classes, and the one that is only designed. The motto has not changed since 2020: what you think is what you write.

## What the AI age changes here

For years, most of the code written with Softanza was written by one hand, and the hand was mine. The style of the library was the way I wrote. Then the machines arrived, and today most code here is written by AI models, as the design of the intelligence plane says it is everywhere, in one sentence: most programming today is done by agents and language models, not humans.

That changes what a style is. A style that lives in one person's habits dies when that person stops writing every line. It has to become something a machine can be held to, and something a machine can check, or it thins away. In this house it did thin, and I will show you where. So this movement of the book, Programming rethought, opens on a law that has two halves. The second half exists because of the age: the code adheres to the way a person thinks, and the court judges it whoever wrote it. By the court I mean the machine that judges code against the house's rules; today it judges only the library's own classes, and section 5 says how.

There is a dependency to say aloud. This book follows the order of its cover, from the familiar to the new: programming, then languages, then intelligence. The record's own logic runs the other way. The first act is to declare a language; programming happens inside a declared language; intelligence is governed by both. The vocabulary's forms are already declared in a spike of Haro, as its charter's entry of 3 October 2026 records. The usage that this chapter describes, the scene, the chain, the named parameter, the promise under each line, is meant to be declared too. So read this law knowing that Part III holds it up.

## 1. The concept, as the field holds it

In our industry, "coding style" means two things, and neither is about how a person thinks. The first is layout and naming, enforced by machines: Python's style guide since 2001, Go's formatter since 2009, and the formatters that every modern project runs before a commit. They settle arguments about spaces and capital letters, and they are good at it. The second is the fluent interface: methods chained so that a line reads almost like a sentence.

The age of generated code added a third practice: check after. A model writes, the tests and the linters read what it wrote, and the model tries again if they complain. The line itself is judged for its shape and its result. Whether it follows the order in which the writer reasoned is a question I know no tool to ask.

## 2. The first principle

My motto for this has not changed since 2020: **what you think is what you write.**

Section 3 shows the motto at work.

## 3. The Softanza form

The founding slide put the whole idea on one page. On the left, a person's four steps of thought: I take the word "softanza"; I turn it to uppercase; I get its characters; I join them with a space. On the right, the same four steps as one line of code, as if the text on the left had been pasted and run.

That exact line no longer runs. Its third link, a method that turned the characters into a list of strings in one step, is not in the library today. It survives only in archived files and in one scratch sample, as `CharsQRT`. I tell you this first because a law chapter that hides its own founding example would not deserve your trust. What is the nearest form that runs, with the four steps still visible, and what does the library offer as one dedicated verb? Run both:

```haro
? StzListOfStringsQ( StzStringQ("softanza").UppercaseQ().Chars() ).ConcatenatedUsing(" ")
#--> S O F T A N Z A
? StzStringQ("softanza").UppercaseQ().Spacified()
#--> S O F T A N Z A
```

Both forms print `S O F T A N Z A`. The idea is intact; the fluent link was lost. A request goes to the library to restore it.

The mental model is the same idea at the level of a problem. You say the problem in plain words. You select the object that holds the data. Then you ask, in order: does it contain what I care about, how many, where? Then you act on those positions, or you call the verb that does it for you. Take a list with empty strings in it. Does it contain them, how many, and where? Run it:

```haro
o1 = new stzList([ "A", "", "B", "", "", "C" ])
? o1.ContainsEmptyStrings()
#--> TRUE
? o1.CountEmptyStrings()
#--> 3
? @@( o1.FindEmptyStrings() )
#--> [ 2, 4, 5 ]
o1.ReplaceEmptyStrings(:With = "~")
? @@( o1.Content() )
#--> [ "A", "~", "B", "~", "~", "C" ]
```

The list answers `TRUE`, then `3`, then `[ 2, 4, 5 ]`, and after the act it reads `[ "A", "~", "B", "~", "~", "C" ]`. Contain, count, find, act. Each line is one step of thought, and the names are the words you would use to say it.

The verb's form says what happens to the object. What does each form do to it? Run them on one string:

```haro
o1 = new stzString("HAxxRxO")
? o1.Removed("x")
#--> HARO
? o1.Content()
#--> HAxxRxO
o1.Remove("x")
? o1.Content()
#--> HARO
? Q("haxxrxo").RemoveQ("x").UppercaseQ().Spacified()
#--> H A R O
```

`Removed` printed `HARO`, and the object still read `HAxxRxO`! `Remove` then acted on it, and `Content()` read `HARO`. The chain with Q ended on `H A R O`. By the library's convention, the past participle gives you a changed copy and leaves the object alone. The plain verb acts on the object. The verb with Q acts and hands the object back, so the next step can follow.

Do you need to remember which argument comes second? A parameter can be named, and the name reads as English:

```haro
? Q("I love Haro").Replaced("love", :With = "♥")
#--> I ♥ Haro
o2 = new stzList([ "tea", "rice", "fish" ])
o2.SwapItems(:AtPositions = 1, :And = 3)
? @@( o2.Content() )
#--> [ "fish", "rice", "tea" ]
```

The text prints `I ♥ Haro` and the list `[ "fish", "rice", "tea" ]`. The names `:With`, `:AtPositions` and `:And` say which argument is which.

How do several questions about one thing read as a list? They are asked inside its scene, a block of braces around the object. The object is named once:

```haro
Q("haro php HARO ruby Haro") {
	? NumberOfOccurrence(:Of = "haro")
	#--> 1
	? NumberOfOccurrenceCS(:Of = "haro", :CS = FALSE)
	#--> 3
	? @@( FindAllCS("haro", FALSE) )
	#--> [ 1, 10, 20 ]
}
```

The scene answers `1`, then `3`, then `[ 1, 10, 20 ]`. The same word counted `1`, then `3` once `:CS = FALSE` was said! The object was named once, and the three questions read as a list.

Can the steps of thought be read back? An object lifted with history keeps the result of each step of its chain:

```haro
? @@( Qh(12500).AddQ(500).RetrieveQ(1500).DivideByQ(500).MultiplyByQ(2).History() )
#--> [ 12500, 13000, 11500, 23, 46 ]
```

The run printed `[ 12500, 13000, 11500, 23, 46 ]`. Five values, the starting one included, and the chain ends at `46`! The article that first told this promised four values, without the first, and a final value one unit short, 45. The guard behind the block states today's rule, on a string chain: the initial value, then each step's result. The book takes the run's answer, not the article's.

Notice the line under every question. It is not a comment. It is a promise, what the line must print. In this house it has been the form of an example from the first day: a short story, a few questions, and the answers written under them. That is the first half of the law, made visible: the code follows the order of thought, and each step says what it expects.

Now the second half. A rule a person must remember is folklore. The library turns its house rules into validators, so that a person or an AI agent can check a class before it lands. The rules are fourteen, and section 5 counts them; five of them read the graph of the code, the structure the library builds from a class's text. Here a class breaks the house's convention that a verb ending in Q returns the object. This rule needs the return statements, which the graph does not model, so it runs as a text pass. What does the court say of the class? Run it:

```haro
cCode = "class Basket" + nl + "def Add(x)" + nl + "	return x" + nl + "def AddQ(x)" + nl + "	return 42" + nl
? StzCodeIsClean(cCode)
#--> FALSE
? StzCheckCode(cCode)[1][:rule]
#--> q-returns-object
```

The court answers `FALSE`, and names the rule: `q-returns-object`. It did not ask who wrote the class! That is the whole of the second half. And the promise under each question is read by a machine too: the library's runner judges a promise as a claim about what the line printed. The house's oldest form of example is also its newest form of test.

The chapters of this part prove the law, each from one side. Chapter 6 tells the mental model and the four metaphors that replace loops: walk, check, yield, perform. Chapter 7 tells the writing style as fourteen rules of its own, not the fourteen house rules of the court you have just seen, and the seven design goals as its architectural half. Chapter 8 tells the forms a function's name can take, the deep form among them, and scope named in the verb. Chapter 9 tells patterns of thought: the machine that reacts to what it recognises, reactive programming in plain words, and the timeline and the grid. Chapter 10 tells how programming becomes refinement.

## 4. The decision, and what I refused

**I let the library's implementation go.** The code the models wrote inside the library is accepted as good. It does not look like mine. Its local variables carry underscores on both sides, hundreds of times per thousand lines. They are a safeguard. The language beneath Softanza lets a library's local variable overwrite a caller's global, and the convention prevents it. I did not ask for the old style there, and I would refuse a campaign to impose it.

**I refused to let the style of the code written with Softanza go.** Every line a programmer, a person or an AI agent, writes with the library must take the historic style. That style is the scene, the chain one step per line, the named parameter, the verb's form, and the promise under each question. That is the line I drew when I saw what had happened.

What had happened is measurable. My study of the record counted the promise under each line, per thousand lines. In the short recipes the house keeps, there are nearly a hundred. In my articles, seventy-five. In the classic tests, fifty-two. In the guards the sessions wrote, under one. They assert in another form, a call that names the expectation. They adopted it because the bare comparisons of the older suites printed 0 or 1, and that does not tell a block that failed from a block that never ran. That gap is closed now; the runner reads the promise as a claim. The study that counted them recommends one form for new test blocks: the classic form, a title, the questions and the promises under them. The converted blocks are left as they are. The record holds that recommendation, and no ruling of mine on it.

**I refused to rewrite code when the language changed its name.** When the language beneath became Haro, the code in my articles was renamed and nothing else. The forms are the asset; the name is a label.

**The forms of the vocabulary were made data, and three old features were refused as grammar.** In Haro, the forms a verb can take are declared once and generated. In the language's spike, the library's shipped names are judged against that declaration. Its charter's entry of 3 October 2026 reports 584 of the 595 shipped spellings of the string class in agreement. The design of that work refuses three things the record counted as features: names that tolerate a misspelling, parameters in any order, and method names in other human languages. The founding deck counted the last two; the narration of the forms counted the first. Misspelling tolerance and free order stay in the library, in part; the multilingual names survive only in an archived file. None of the three is part of the grammar a machine is held to. The refusal is written in the language's principles file, as its seventh principle, marked designed. The book prints it as the design's, and the record does not say it is mine.

**I chose goals before laws.** The 2022 design held seven goals, expressiveness, flexibility, reliability, consistency, human metaphors, practical abstractions and manageability, and every feature served one. The operating rules of today are laws paid for by incidents, which say how and not why. Chapter 7 puts the goals back beside the laws.

## 5. The court

`coderule_narrated` proves that a house rule is a rule over the code graph and that the findings come out on planted code. It proves that clean code passes, and that the library's house rules are fourteen. `testoor_promises_narrated` proves that the promise is judged by a machine in the house's own form. Each rule is planted both ways: the lie it must catch, and the truth it must not accuse. `05_containsemptystrings` is the mental model's steps on the same list, a classic block kept as a guard. `466_keeping_the_history_of_updates_of_a_softanza_objec` proves the history of a chain.

Section 6 sets the court beside the field.

## 6. The field, and where it leads

The field leads in enforcement. Most mainstream languages have a formatter and a linter, and most projects run them before a commit or in continuous integration; that is general knowledge, not a study of the record. The court that would judge the style of a program written with Softanza is a specification; the one that exists judges the library's own classes.

The field leads in reach and in people. There is a labour market for its tools and none yet for this one, and the field's generators are the largest that exist.

The field also leads, today, over Softanza's own pages. The study that measured the record found that the site's code blocks carry no named parameter and no scene: a reduced dialect of the library, shown to every visitor. An AI agent that learned from the site would learn that dialect. I did not measure the site's blocks again. A style that is not shown is not learned.

Where I think Softanza stands apart is in what the style is tied to. A formatter judges the shape of a line; a fluent interface makes a line pleasant. Here the line is tied to a step of thought, and the verb's form is a contract about the object. The promise under the line is the example, the test and the documentation at once.

## 7. The limit

What is built: the forms of the vocabulary, in thousands of method names; the house rules as a court over the library's own code; the promise judged by a machine.

What is designed: a court of style for the code a programmer or an AI agent writes with the library. It would read a positional argument where a named one exists, a question with no promise, a chain on one line past two steps. And the writing grammar declared in Haro, so that an AI model's output is held to it before it is written.

What is absent: any machine that judges, today, the style of a program written with the library. The founding slide's chain does not run as written. In this book the discipline carries the name of its motto: what you think is what you write.

## 8. Six doors

**The programmer.** Your lines follow your reasoning: select, contain, count, find, act. Each question carries its promise, and a court reads it whether you wrote it or an AI agent did.

**The analyst.** The method starts from your problem in plain words. The keywords you use become the names of the steps.

**The designer.** The verb's form is an interface contract: by the library's convention, the past participle does not touch the object. A court for that rule is designed, not built.

**The decision-maker.** I hold this as a view, not a result: a style a machine can be held to can be reviewed goal by goal, not line by line. It is the only reading one person can give to hundreds of thousands of lines.

**The educator.** Teach the discipline whole, and in order: formulate, then express, then be judged.

**The agent.** You will be corrected by the library, not by folklore. Write the question, then the promise under it.

## 9. Exercise

Take the list `[ "tea", "", "rice", "", "fish", "" ]`. Write the questions of the mental model in order, one line each: does it contain empty strings, how many, where. Then one act, with a named parameter. Under every question, write the line it must print, before you run anything.

Run it. Then ask an AI agent to solve the same problem, and judge its answer with two questions only: does each line follow a step of thought, and does each question carry its promise.

I left this one in your hands, on purpose. The Basket class of section 3 fails the court because `AddQ` returns `42`. Change that one value to `This` and run the question again:

```haro exercise
cCode = "class Basket" + nl + "def Add(x)" + nl + "	return x" + nl + "def AddQ(x)" + nl + "	return This" + nl
? StzCodeIsClean(cCode)
```

Do not stop at the court's answer. Ask whether the class, as it stands, follows the way a person thinks, and what the court read to answer you. I do not give you the verdict: section 6 says which court exists, and section 7 says what it does not read. When you have settled it, you will know why a court that passes a class has not yet judged the style of a program written with the library.

The next chapter is the mental model, and the metaphors. Where you would write a loop, it asks you to name the move you are making instead: walk, check, yield or perform.
