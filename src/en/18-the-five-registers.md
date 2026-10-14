---
id: the-five-registers
part: 4
number: 18
title: The five registers, and conversations that ask
spine: false
narrations: [stz-knowledge-programming-narration.md, stznatural-narration.md]
site: [wise, byexample]
guards: [wisecoding_narrated, wisecoding_rich_narrated, ownagentstack_narrated, tutor_gaps_narrated]
stage:
  built: "the goal, the gap and the question with its reason; a reply as an option, a data structure or a sentence split on commas and the word 'and'; the governed door with its refusals; the checkpoint with its lifetime; the goal fulfilled or revoked; one wired AI agent that stops where it would have to invent"
  designed: "several readings of one reply, enumerated for the person to choose; the nearest alternatives named after a refusal; the example written back as a promise"
  absent: "the formula register; the example register; a conversation whose question is worded in Arabic, Hausa or French; a value with a space in it"
status: draft
rulings: ["12.25", "12.26", "12.27"]
research: research/ch18.md
---

In this chapter I show you the five forms a reply can take, an option, a data structure, a formula, a sentence and examples. Then I show what the governed door does with each of them. I tell you which three run and which two do not, and what becomes of a refusal once it is written: it waits for a person, with its context and a lifetime. I let the conversation with no one in it run, and I show what a conversation can and cannot do in Arabic and in Hausa. Whatever the form, a reply is only a candidate, and the world's rules decide whether it becomes knowledge.

## 1. The concept, as the field holds it

Two practices meet in the idea of a conversation that asks, and a third stands behind its last register. (General knowledge for this whole section, not a study of the record; the dates are to be checked before print.)

The first is slot filling. A dialogue framework asks the user for the missing pieces of a form until the form is full. The frameworks of the field understand free text with trained models, speak on many channels and ship connectors, and they ask the designer to write intents and flows in their own language. They take the user's reply as the answer and act on it.

The second is vibe coding, a name put into circulation in 2025: the human prompts, the AI model produces, the human keeps what runs.

The third is programming by example. Spreadsheets fill a column from two examples you typed. Research calls it inductive synthesis, and the model era made the example the way one steers a model.

## 2. The first principle

**A reply may come in any of five forms. Whatever the form, it is only a candidate, and the world's rules decide whether it becomes knowledge.**

The design document says it in one sentence I keep: expression is free, admission is governed. The record holds this sentence, captured from my directive of 13 July 2026. It holds no sentence of mine on why these five registers and not four or six, nor on the moment I set wise coding against vibe coding. The chapter opens on this sentence.

## 3. The Softanza form

Chapter 17 showed a conversation asking, and refusing to conclude while a gap is open. This chapter is about the answer. The five registers are five forms a reply can take: an option picked by its number, a data structure, a formula, a sentence, and examples. I will show you each, and I will tell you the ones that do not run.

**The first register: an option.** When the world already knows values, how does the question offer them? Run it:

```haro
oKB = new stzKnowledgeGraph("pizzeria")
oKB.Know("pizza1", "dish").Know("pizza2", "dish").Know("pizza3", "dish").Know("pizza4", "dish")
oKB.AddConversationQ("frame").SetGoal(StzGoalQ().RequireEach("dish", "topping"))
oKB.AskIn("frame")
oKB.ReplyIn("frame", "cheese")
oKB.AskIn("frame")
oKB.ReplyIn("frame", "olives")
? oKB.AskIn("frame")
#--> Which 'topping' does 'pizza3' have? (1) cheese  (2) olives -- or answer freely.  (why: every dish needs 'topping')
? @@(oKB.ReplyIn("frame", 2)[:admitted])
#--> [ "olives" ]
```

The question offers the known values as numbers, and `2` picked `olives`.

What does the door answer to a number nobody offered? Run it:

```haro
? oKB.AskIn("frame")
#--> Which 'topping' does 'pizza4' have? (1) cheese  (2) olives -- or answer freely.  (why: every dish needs 'topping')
aV = oKB.ReplyIn("frame", 99)
? @@(aV[:admitted])
#--> [ ]
? @@(aV[:refused])
#--> [ [ "(99)", "no such option" ] ]
? oKB.ConversationQ("frame").Checkpoints()[1][:why]
#--> no option (99) was offered -- 2 option(s) on the table
? aV[:goalState]
#--> pursuing
```

The door refused it, and said `no such option`! The checkpoint says why: `no option (99) was offered -- 2 option(s) on the table`. A reason, and a count of the options on the table. It does not list them, and the next question offers the same options again: `(1) cheese  (2) olives`. The refusal never guesses a value, it reaches a person as a checkpoint, and the goal stays `pursuing`. That matters for section 7.

The question is data before it is text. It carries a force, which is *what* while the world knows nothing and *which* once it knows a value, and the options. Any medium can render it:

```haro
oKF = new stzKnowledgeGraph("pizzeria2")
oKF.Know("p1", "dish").Know("p2", "dish")
oKF.AddConversationQ("f").SetGoal(StzGoalQ().RequireEach("dish", "topping"))
? oKF.AskInXT("f")[:force]
#--> what
oKF.ReplyIn("f", "cheese")
aQ = oKF.AskInXT("f")
? aQ[:force]
#--> which
? @@(aQ[:options])
#--> [ "cheese" ]
```

**The second register: a data structure.** What becomes of a list of two values sent as one reply? Run it:

```haro
oKD = new stzKnowledgeGraph("desserts")
oKD.Know("tiramisu", "dish")
oKD.AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
oKD.AskIn("setup")
aV = oKD.ReplyIn("setup", [ "mascarpone", "espresso" ])
? @@(aV[:admitted])
#--> [ "mascarpone", "espresso" ]
? aV[:goalState]
#--> fulfilled
```

A list of values is taken as the values, and each one goes through the same door.

**The fourth register: a sentence.** I skip the third for a moment, because it is one of the two that do not run. How is a phrase of the form "X and Y" or "X, Y" read? The conversation keeps a transcript in which every admission is narrated and the fulfilment of the goal is recorded:

```haro
oKM = new stzKnowledgeGraph("menu")
oKM.Know("margherita", "dish")
oKM.AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
oKM.AskIn("setup")
oKM.ReplyIn("setup", "tomato-sauce and mozzarella")
? oKM.ConversationQ("setup").Transcript()
#--> SOFTANZA: Goal adopted -- this conversation is now accountable for it.
#--> SOFTANZA: What does 'margherita' have for 'contains'?  (why: every dish needs 'contains')
#--> YOU:      tomato-sauce and mozzarella
#-->   -> admitted: 'margherita' contains 'tomato-sauce'
#-->   -> admitted: 'margherita' contains 'mozzarella'
#--> SOFTANZA: Goal fulfilled: every required slot is filled in 'menu'
```

It is read as two values, each one judged: the transcript holds `admitted: 'margherita' contains 'tomato-sauce'` and `admitted: 'margherita' contains 'mozzarella'`. "Natural" here means a splitter on commas and on the English word "and". The natural layer of the library, which I will use in a moment, is not called by the conversation.

**When a reply carries several values, and the world allows one.** What does a relation declared unique do with a reply that carries two values? Run it:

```haro
oKS = new stzKnowledgeGraph("staffing")
oKS.AddConversationQ("s").SetGoal(StzGoalQ().RequireOne("kitchen3", "led-by"))
oKS.ConstrainRelation("led-by", :Unique)
oKS.AskIn("s")
aV = oKS.ReplyIn("s", "mario and giovanni")
? @@(aV[:admitted])
#--> [ "mario" ]
? @@(aV[:refused])
#--> [ [ "giovanni", "'kitchen3' already bears 'led-by' (to 'mario'); the relation is :Unique" ] ]
? len(oKS.ConversationQ("s").Checkpoints())
#--> 1
```

The first value was admitted, and the second was refused with the law's reason: `'kitchen3' already bears 'led-by' (to 'mario'); the relation is :Unique`. The refusal reaches a person, as one checkpoint. Be careful what you read in this. The choice between Mario and Giovanni was made by order. It was not made by a person. The design promises something else, and section 7 says what.

**The third register, the formula.** Is a formula typed as a reply evaluated? Run it:

```haro
oKP = new stzKnowledgeGraph("shop")
oKP.Know("tea", "product")
oKP.AddConversationQ("price").SetGoal(StzGoalQ().RequireEach("product", "price"))
oKP.AskIn("price")
? @@(oKP.ReplyIn("price", "=12*3")[:admitted])
#--> [ "=12*3" ]
? oKP.Query([ "tea", "price", "?o" ])[1]
#--> =12*3
```

It is not. The price of the tea is now the text `=12*3`! I found this out by running it, and the code is silent about a formula register. The record lists the wise-coding work on registers 3 and 5 as waiting, not routed.

**The fifth register, examples.** What does the door do with examples offered as pairs? The agent that would read them is on the roster, and reserved:

```haro
oKX = new stzKnowledgeGraph("phones")
oKX.Know("contact1", "contact")
oKX.AddConversationQ("fmt").SetGoal(StzGoalQ().RequireEach("contact", "number-pattern"))
oKX.AskIn("fmt")
aV = oKX.ReplyIn("fmt", [ [ "+216-21-298-374", "valid" ], [ "+33-6-12-34-56-78", "valid" ] ])
? @@(aV[:admitted])
#--> [ ]
? @@(aV[:refused])
#--> [ ]
? aV[:goalState]
#--> pursuing
? len(oKX.ConversationQ("fmt").Checkpoints())
#--> 0
try
	StzOwnAgent("induction")
catch
	? cCatchError
done
#--> Softanza's own agent 'induction' is RESERVED, not wired yet -- refusing rather than returning a stub (LAW 3). See StzOwnAgents().
```

Neither admitted nor refused: `[ ]` and `[ ]`, the goal still `pursuing`, and not one checkpoint! This is not the refusal the protocol describes. It is silence. I hold silence to be the worse answer, as a view and not a result: the reader who offered the examples is not told they were not understood. I found a second form of the same fault. The same examples typed as one string, joined by a comma, are split and admitted as two literal values, and the goal reads fulfilled. The examples became the knowledge. Nothing was inferred.

So three of the five registers are wired, one of them in its simplest form, a splitter. Two are not. I would rather you meet that here than on a page of mine that said five.

That leaves the refusal itself, and what becomes of it.

### What happens to a refusal

A refusal waits for a person, with its context. A lifetime can be set so that a stale one leaves the live list without being deleted:

```haro
oKT = new stzKnowledgeGraph("ttl")
oKT.AddConversationQ("t").SetGoal(StzGoalQ().RequireOne("kitchen", "led-by"))
oKT.AskIn("t")
oKT.ReplyIn("t", 7)
? len(oKT.ConversationQ("t").Checkpoints())
#--> 1
oKT.ConversationQ("t").SetCheckpointTTL(1)
oKT.AskIn("t")
oKT.AskIn("t")
? len(oKT.ConversationQ("t").Checkpoints())
#--> 0
? len(oKT.ConversationQ("t").AllCheckpoints())
#--> 1
```

Nothing is deleted. Expiry is about what still needs a person, and the audit record keeps all of it. Every call here is chained from `ConversationQ`, because a held copy would silently do nothing: the guard's comment explains it.

A conversation is accountable for one goal, and it ends by fulfilling the goal or by revoking it on the record. A revoked conversation asks nothing and cannot conclude:

```haro
oKG = new stzKnowledgeGraph("lifecycle")
oKG.Know("d1", "dish").Know("d2", "dish")
oKG.AddConversationQ("s1").SetGoal(StzGoalQ().RequireEach("dish", "sauce"))
oKG.AddConversationQ("s2").SetGoal(StzGoalQ().RequireEach("dish", "garnish"))
? oKG.ConversationQ("s1").GoalState()
#--> pursuing
oKG.AskIn("s1")
oKG.ReplyIn("s1", "pesto")
oKG.AskIn("s1")
oKG.ReplyIn("s1", "pesto")
? oKG.ConversationQ("s1").GoalState()
#--> fulfilled
? oKG.ConversationQ("s1").GoalWhy()
#--> every required slot is filled in 'lifecycle'
oKG.AskIn("s2")
oKG.ConversationQ("s2").RevokeGoal("out of scope tonight")
? oKG.ConversationQ("s2").GoalState()
#--> revoked
? oKG.ConversationQ("s2").GoalWhy()
#--> out of scope tonight
? len(oKG.OpenConversations())
#--> 0
```

### Programmatic by default: the conversation with no one in it

Chapter 17's law says conversations happen in code first. Here is the conversation with no person and no model. An AI agent of the library asks, an answer source (a plain function) replies, and every reply passes the same door. Where the source has no answer, does the agent invent? Run it:

```haro
oKW = new stzKnowledgeGraph("menu")
oKW.Know("margherita", "dish").Know("tiramisu", "dish")
answers = [ [ "margherita", "tomato-sauce" ], [ "tiramisu", "mascarpone" ] ]
aR = StzOwnAgent("wise-coder").PursueGoal(StzGoalQ().RequireEach("dish", "contains"), oKW, func subj, rel {
	for a in answers
		if a[1] = subj
			return a[2]
		ok
	next
	return ""
})
? aR[:filled]
#--> 1
? aR[:asked]
#--> 2
? aR[:why]
#--> goal filled in 2 question(s), governed admission throughout
oKV = new stzKnowledgeGraph("desserts")
oKV.Know("panna-cotta", "dish")
aR2 = StzOwnAgent("wise-coder").PursueGoal(StzGoalQ().RequireEach("dish", "contains"), oKV, func subj, rel { return "" })
? aR2[:filled]
#--> 0
? aR2[:why]
#--> stopped: no answer for 'panna-cotta' / 'contains' -- gap left for a human
```

It does not. It stops, says `stopped: no answer for 'panna-cotta' / 'contains' -- gap left for a human`, and leaves the gap for a person. Of the library's five own agents, this is the one that is wired. The other four are reserved, and asking for one raises, as the fifth register's block printed: `RESERVED, not wired yet -- refusing rather than returning a stub`. It is never a stub.

### In Arabic, and in Hausa

Chapters 2 and 11 showed the natural layer in Hausa. Here is what the conversation can and cannot do with languages, said in three blocks, because the three are different.

First, the data. Names, values and lists in Arabic script pass the gate exactly as Latin ones do. The words around them, the frame of the question, stay English:

```haro
oKA = new stzKnowledgeGraph("مطعم")
oKA.Know("بيتزا", "dish")
oKA.AddConversationQ("c").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
? oKA.AskIn("c")
#--> What does 'بيتزا' have for 'contains'?  (why: every dish needs 'contains')
aV = oKA.ReplyIn("c", [ "جبن", "طماطم" ])
? @@(aV[:admitted])
#--> [ "جبن", "طماطم" ]
? aV[:goalState]
#--> fulfilled
```

The Arabic values passed the gate, and the goal reads `fulfilled`.

Second, the candidate. A Hausa sentence can produce a value in the natural layer, and the value, sent as a reply, goes through the same door. The two steps are the caller's: the conversation does not call the natural layer itself. This is the principle of the chapter in a small space, since the expression is free and the admission is governed. The graph folds the case of the value, so the printed `JIBINI` is admitted as 'jibini':

```haro
oKH = new stzKnowledgeGraph("menu")
oKH.Know("pizza", "dish")
oKH.AddConversationQ("c").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
oKH.AskIn("c")
cCandidate = NaturallyIn("ha", "Yi rubutu dauke 'jibini' Maida shi").Result()
? cCandidate
#--> JIBINI
aV = oKH.ReplyIn("c", cCandidate)
? aV[:narration]
#--> admitted: 'pizza' contains 'jibini'
```

Third, the question in the learner's language. The tutor is a consumer of the conversation: it uses the gap the conversation names, and it chooses the words to say it in four languages. The sentences are templates. The code's own comment says that the French, Arabic and Hausa wording is a draft awaiting a native reviewer. Read the three below as drafts, and not as reviewed text:

```haro
oEx = StzProgramQ("../../education/program").CourseQ("elementary-introduction").ExerciseQ("ex-01-01")
? oEx.GapText("finds", "en")
#--> Where are the repeated items? Which line of your program asks for their positions? (why: the mental model finds before it applies)
? oEx.GapText("finds", "fr")
#--> Où sont les éléments répétés ? Quelle ligne de votre programme demande leurs positions ? (pourquoi : le modèle mental trouve avant d'agir)
? oEx.GapText("finds", "ar")
#--> أين العناصر المكررة؟ أيّ سطر في برنامجك يسأل عن مواضعها؟ (لماذا: النموذج الذهني يبحث قبل أن يطبّق)
? oEx.GapText("finds", "ha")
#--> Ina abubuwan da aka maimaita? Wane layi a shirinka yake tambayar wurarensu? (dalili: tsarin tunani yana nemo kafin ya aiwatar)
```

So the library cannot ask in Arabic or in Hausa through `AskIn`. What it can do is hold the data in any script, take a candidate computed in any pack, and let the tutor say the gap in four languages. A value with a space in it raises at the moment (section 7 gives the evidence). So the connectors "et" in French, "da" in Hausa and "و" in Arabic are not connectors. The three sentences above are the library's own, printed as they stand, and the code calls them a draft awaiting a native reviewer. I wrote no Arabic or Hausa sentence of my own.

### An AI model is a fluency, never the mind

Without a model, what does a conversation say of its own fluency? Run it:

```haro
oKF2 = new stzKnowledgeGraph("fluency-space")
oKF2.AddConversation("f")
? oKF2.ConversationQ("f").Fluency()
#--> plain
oKF2.ConversationQ("f").SetFluency(:neural)
? oKF2.ConversationQ("f").Fluency()
#--> neural
? oKF2.ConversationQ("f").IsFluencyNeural()
#--> 0
```

`plain`: it stays on its deterministic floor and says so. The word "neural" can be set, and `Fluency()` repeats it, but `IsFluencyNeural()` answers `0`! The word is claimed only when a model is there.

## 4. The decision, and what I refused

**I refused to guess.** The record's phrase is: guessing is replaced by asking; vibes are replaced by governance. A gap is a question. A reply is a candidate.

**I refused a different gate for each way of answering.** A formula is not trusted because it is code, and a structure is not trusted because it is typed. The form does not buy trust, and I hold this as a view, not a result. All five registers go through one door.

**I refused a stub.** A reserved agent raises when it is asked for. The design document calls the raise the law working, and says it should not be read as a defect. I refused to pretend the fifth register works.

**I refused an AI agent that fills a gap to finish the job.** The wise coder stops, and leaves the gap for a person.

**I refused to let a conversation own a world.** It happens inside a knowledge space and never owns one. A copy of the knowledge held in a session goes stale.

**I refused a deleted checkpoint.** Expiry takes a refusal off the live list. The record keeps it.

**I refused to let the example look like the answer.** The record's closing law about the fifth register is that an admitted candidate writes its example back as a promise. That law is designed, and not built.

## 5. The court

`wisecoding_narrated` proves that the gap is computed from the space, and that the question is led by the system, names its subject and says why it asks. It proves that "X and Y" and a data structure admit. It proves that a unique law refuses through the conversation and the refusal reaches a checkpoint. It proves that concluding with a gap open is refused. `wisecoding_rich_narrated` proves the goal monitored to fulfilled or revoked, the frame, and the numbered options. It proves the refusal of a number nobody offered, the lifetime of a checkpoint, and the fluency that is claimed only with a model. `ownagentstack_narrated` proves the roster of five, the wired wise coder, the reserved agent that raises, and the gap left for a person. `tutor_gaps_narrated` proves the exercise's gap question in each language, and that a step with no question in a language is red, never another language. It writes folders, so the book counts it and does not run it; the tutor block above only reads the course.

Three of the guards print their own total and end by calling `pf()`, which prints the time and the runtime's version and then stops the run with a raise. That is their way to end. `tutor_gaps_narrated` ends with `Summary()`, which prints the total and a status, and does not raise.

What the field does better, and where the record stands apart, comes next.

## 6. The field, and where it leads

The field leads in understanding. A dialogue framework, as the field holds it, reads free text with trained models, speaks on many channels and ships connectors. The record says what Softanza lacks, in its own count: the word "WhatsApp" appears in no code file and no design document of the library. The conversation asks one slot at a time, over a graph the user must first have declared, and it does not understand an open reply.

The field leads on examples. Programming by example is, as the field holds it, shipped in spreadsheets today. Softanza has no induction at all, and the record says so: nothing induces yet. A search for "induce", "from examples" and "infer" over the regular-expression folder finds nothing.

The field is honest about costs, and so is the record. Several candidates is the normal case when you ask for a rule from examples. A pattern induced from three examples overfits them. The remedy the record names is the question that tells two candidates apart. And the index that would carry the examples is as clean as the tags of the methods, with about eighty-five misspellings.

Here is where I think the record stands apart. Every reply, in whatever form, is judged by the world's laws before it counts, with the reason. The session keeps a transcript and a checkpoint that a person can read. The field's reply is a prompt, and the human keeps what comes out.

The limit comes next, and it names what is built, what is designed and what is absent.

## 7. The limit

What is built: the goal, the gap, the question with its reason, the frame; the first register, the second, and the fourth in the form of a splitter; the governed door with its refusals. And the checkpoint and its lifetime; the goal fulfilled or revoked; the transcript; one wired agent; the tutor's four-language gap sentence.

What is designed: the *several acceptable* branch as the design writes it. The protocol says that when several readings of a reply are acceptable, the system enumerates them and the person chooses. What is built is two different things. The values already known become numbered options in the question, before the reply. And a reply that carries several values has each one judged on its own, with the first kept under a unique law. No step presents competing readings of one reply. And the *none acceptable* branch as written: the reason is built, and the nearest acceptable alternatives are not. The refusal states a reason, and for a number, how many options were on the table. And the example written back as a promise: the site's page *by example* (read 9 October 2026) calls it a rule of the design that is not built. The site's two pages on this, *wise* and *by example*, say "with the nearest alternatives" and "the person chooses". The two pages promise more than the code does. I say it so that the page or the code is corrected. The code wires three of the five registers. The memo that names the formula and the examples lists them as waiting, not routed, and for this chapter they are absent.

What is absent: the formula register; the example register, and the induction agent behind it; a conversation worded in Arabic, Hausa or French; and a value with a space in it. In the research run of 8 October 2026, on the version of the library this book runs, `ReplyIn` raised on each value containing a space that I tried. The error was an uninitialised variable. The three were "tomato sauce", "fromage et tomate", "jibini da tumatir". Called directly, the door returned the refusal properly. No block of this book records either result, so the run of the book does not show them. The conversation should have refused with the reason and written a checkpoint, and it doesn't. It is in the memo as a request, and the exercise below does not use a value with a space.

## 8. Six doors

**The programmer.** A reply is a verdict you can test with ordinary promises: what was admitted, what was refused, and the state of the goal.

**The analyst.** The goal is the schema of a complete model. The gaps are the list of what is missing. The transcript and the checkpoints are the evidence of how each fact got in.

**The designer.** The question comes back as data: force, subject, relation, options, reason. Any medium can render it. The library renders English, and the tutor shows the pattern for four languages.

**The decision-maker.** A reply is judged before it counts. A refusal reaches a person with its context and a lifetime. The roster is honest: one agent of five is wired, and two of the five registers are not available.

**The educator.** The tutor is wise coding. It names the missing step as a question and never as the answer, in the learner's language, and its wording in three of those languages awaits a native reviewer.

**The agent.** You can drive the loop yourself with an answer source, and you must stop where you would have to invent. You cannot offer examples and be understood, and you are told by name when you ask for a reserved agent.

## 9. Exercise

Choose a small world of your own, a shop, a class, a clinic, with four entities of one type and a goal that each needs one relation. Before you run anything, write under each of the five replies below the verdict you expect: admitted, refused with a reason, or neither.

1. a plain word;
2. a number that picks a value the first reply made known;
3. a number nobody offered;
4. two values at once, for a relation you have declared unique;
5. a list of two pairs of examples.

Then run it. An admitted reply uses up the question, so call `AskIn` again before the next reply. If a promise breaks, do not change the promise: explain the output first.

```haro exercise
oWorld = new stzKnowledgeGraph("my-world")
oWorld.Know("item1", "thing").Know("item2", "thing")
oWorld.AddConversationQ("mine").SetGoal(StzGoalQ().RequireEach("thing", "colour"))
oWorld.AskIn("mine")
# your five replies here, each with the verdict you expect
```

The fifth reply produces silence today, and that is the lesson of the exercise. If the library later turns it into a refusal, the expected answer changes. Run it on the date and commit shown at the foot of the page.

I left this one in your hands. Take the fifth-register block of section 3 and change one thing: send the two phone numbers as one string, joined by a comma, and not as two pairs.

```haro exercise
oKX = new stzKnowledgeGraph("phones")
oKX.Know("contact1", "contact")
oKX.AddConversationQ("fmt").SetGoal(StzGoalQ().RequireEach("contact", "number-pattern"))
oKX.AskIn("fmt")
aV = oKX.ReplyIn("fmt", "+216-21-298-374,+33-6-12-34-56-78")
? @@(aV[:admitted])
? aV[:goalState]
```

Run it, then read what was admitted and what the goal says, and decide whether that is what you wanted to hand to the door as examples. Section 4, in its last refusal, and section 7, in the absent example register, say why I call it a fault. When you can say why, you will know what the door did with your examples, and why that is not induction.

The next chapter is about the domain language model. There the next thing the model says is a checkable unit of your world, a fact your rules admit or refuse, and never a token.
