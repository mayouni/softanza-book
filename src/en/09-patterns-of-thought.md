---
id: patterns-of-thought
part: 2
number: 9
title: "Patterns of thought: the Softanzuter, Reaxis and the engines"
spine: false
narrations: [stzregexuter-regex-as-computational-reactive-medium.md, stz-reaxis-reactive-programming-narration.md, stz-managing-deep-lists-narration.md, softanza-reactive-objects-narration.md]
site: [softanzuter, craft]
guards: [00_overflow_narrated, 60_reaxis_on_reactor_narrated, piagent_narrated, 00_grid_narrated, test_timeline_regression, 01_deeplist_narrated]
stage:
  built: "the Regexuter and the Listexuter, reacting with a state that remembers; Reaxis, reactive programming in plain words, on the engine's event loop; the timeline, the grid and deep operations; the AI agent whose skills cascade to a fixpoint"
  designed: "the Softanzuter proper, many faculties sharing one state and cascading until it settles; the universal engine behind it; its four siblings, analyser, genetic, linguistic and quantic"
  absent: "a dependency chain that links one trigger to another; a section-merging verb the article presents as its point"
status: draft
rulings: ["12.4", "12.18", "12.19"]
research: research/ch09.md
---

In this chapter I take the three subjects of the title in turn: the Softanzuter, Reaxis, and the engines, of which the timeline and the grid run here. The Regexuter binds a pattern to code that fires and remembers why; Reaxis is reactive programming with its vocabulary redesigned. I climb the ladder the architecture draws, four rungs, and at the third I run the block that fails to cascade rather than claim a rung that is not built. I say what I refused: regex as a way to read text, the field's words for reactive programming, the four siblings, and the cascade. Everything serves one sentence: a Softanzuter is a computational representation of a thinking machine, based on one or many Regexuters, enabling it to identify and react to patterns of thought.

## 1. The concept, as the field holds it

The field has three tools for making a program react. Regular expressions recognise a shape in text, and nothing more: they say "this matches", and they stop. Reactive programming, the family of observables, subscribers and schedulers that Rx made popular, lets data flow through a program over time. Its vocabulary comes from plumbing, telephony and publishing: pipes, backpressure, hot and cold sources. And rule engines, the production systems of the field with their forward chaining, fire rules when facts appear, and keep firing while new facts appear; that is general knowledge, and the rule engines of the field are older and more mature than anything in this chapter.

Each tool is separate. A regular expression does not trigger a computation, a reactive stream does not recognise a pattern, and a rule engine does not have a vocabulary that a person would use to say a thought. I hold this as a view, not a result.

The next section gives the one sentence I answer with.

## 2. The first principle

I gave this paradigm one sentence, and everything below tries to make it mechanical: **a Softanzuter is a computational representation of a thinking machine, based on one or many Regexuters, enabling it to identify and react to patterns of thought.**

The next section shows how far the library has made it mechanical.

## 3. The Softanza form

The architecture draws it as a ladder with four rungs, each adding one thing.

The first rung is the pattern. You will see it in chapter 15: a shape in a medium, a string, a list, a number, that can say "this matches, and here is how", and do nothing more. The second rung gives a pattern a reaction: the Regexuter, a reflex arc. You bind a pattern to code, process a text, and the code fires on every match. A Regexuter reacts, and it remembers what it did. Here it redacts the secrets in a sentence. What does the state it keeps say about each one: what it matched, what it computed, where, and which trigger fired?

```haro
rxu() {
	Trigger(:SensitiveData = "(password|secret|key):\s*(\w+)")
	@C(:When = :SensitiveData, :Do = '{ @value = "REDACTED-" + len(@value) }')
	Process("User credentials: password: abc123 secret: def456")
	? @@( Results() )
	#--> [ "REDACTED-16", "REDACTED-14" ]
	? @@( Positions() )
	#--> [ 19, 36 ]
	? State()[1][:matchedvalue]
	#--> password: abc123
	? State()[1][:computedvalue]
	#--> REDACTED-16
	? @@( State()[2][:dependson] )
	#--> [ "sensitivedata" ]
}
```

The state is provenance: every reaction that changes a value keeps its why. The last line, `[ "sensitivedata" ]`, is also an honest limit, and I will come back to it: what the Regexuter records as a dependency is today only its own trigger.

Now the third rung, the one the definition is about. It is many Regexuters, over different media, sharing one state, so that what one faculty writes is a medium another faculty can match over. A thought is a state entry with its provenance, and a settled thought is a state in which nothing more fires. That rung is not built, and the block shows how I know. The second trigger below is written for numbers of three digits or more. The first trigger turns the 7 into 700, which is one. If the machine thought in cascades, would the second fire on the first's result? Run it:

```haro
rxu() {
	Trigger(:Number = "\d+")
	Trigger(:Big = "\d{3,}")
	@C(:When = :Number, :Do = '{ @value = @number(@value) * 100 }')
	@C(:When = :Big, :Do = '{ @value = "BIG" }')
	Process("Found 7 items")
	? @@( Matches() )
	#--> [ "7" ]
	? @@( Results() )
	#--> [ 700 ]
	? @@( Triggers() )
	#--> [ "number" ]
}
```

It did not: the results read `[ 700 ]`, the triggers that fired read `[ "number" ]`. `BIG` is nowhere! Every trigger is matched once against the original text, and what one trigger writes is not offered to the others. That is the whole difference between the second rung and the third.

The cascade runs one rung above, at the fourth rung, the AI agent: the thinking machine given a body in a world, and a goal. Its mind is made of skills, each with a condition and an action, which chain. The second skill fires on the fact the first one wrote. `Pursue()` returns how many skill firings were verified, and goes on until the world stops changing, or for twenty rounds at most. What does it answer when asked again?

```haro
oAgent = new stzPIAgent("cook")
oAgent.MemoryQ().Learn("order", "state", "placed")
s1 = new stzAgentSkill("cook")
s1.SetWhen(func oM { return oM.Fact("order", "state", "placed") })
s1.SetDoes(func oM { oM.Forget("order","state","placed") oM.Learn("order","state","cooking") return 1 })
s2 = new stzAgentSkill("serve")
s2.SetWhen(func oM { return oM.Fact("order", "state", "cooking") })
s2.SetDoes(func oM { oM.Forget("order","state","cooking") oM.Learn("order","state","served") return 1 })
oAgent.AddSkill(s1)
oAgent.AddSkill(s2)
? oAgent.Pursue()
#--> 2
? oAgent.MemoryQ().Fact("order", "state", "served")
#--> TRUE
? oAgent.Pursue()
#--> 0
```

It answers `2`, then `0`, and between the two the fact `served` reads `TRUE`. That is a fixpoint. The guard that proves it labels the scene in its own words: `the cascade to fixpoint (Softanzuter at agent level)`. In chapter 17 you will see an agent of this same class refused at a gate. Here is the other face of it: the agent that chains, because its mind is programmatic.

So the word has three meanings in the record, and the reader deserves to be told which is which. First, in this chapter, "Softanzuter" is the third rung, the thinking machine of the definition: designed, not built. Second, the engine has a module with the same name, which the macroplan presents as the foundation for AI agents. Its slots hold a state and a bounded mailbox, and a message into a full queue is refused, counted and never dropped quietly; the agent of the block above, `stzPIAgent`, never calls it. Third, the design of a universal engine behind all of it, a medium where any pattern language becomes a computation, is planned.

**Reaxis** is the second subject of the chapter's title, and it is a different idea. It is reactive programming with a vocabulary redesigned from the ground. A reactive thing is a Container, a Stream and an Rfunction: a function in waiting, which is not a callback. Data flows through a stream in plain words, a transformation, a filter, what to do with what passes. Four prices go in, 80, 90, 100 and 120: which ones come out, and at what value?

```haro
aSeen = []
Rs = new stzReactiveSystem()
Rs {
	oStream = CreateStream("prices")
	oStream {
		Transform(func price { return price * 1.20 })
		Filter(func price { return price >= 100 })
		OnPassed(func item { aSeen + item })
		FeedMany([ 80, 90, 100, 120 ])
	}
	RunLoop()
}
? @@( aSeen )
#--> [ 108, 120, 144 ]
```

`aSeen` reads `[ 108, 120, 144 ]`: the 80 became 96 and was dropped by the filter; the 90 became 108 and passed. Three functions are in waiting, and nothing here is called a subscriber; the old word `Subscribe` survives as an alias of `OnPassed`.

Reaxis replaced backpressure with overflow, a word you do not need a diagram to understand. And it was audited. A reading of the four strategies the article documented found that three of them lost data and reported none. The default discarded everything past the capacity while the counter read zero. That is fixed, and proved for all four strategies. Here, four items go into a buffer of two. What does the stream say happened?

```haro
oRs = new stzReactiveSystem()
oS = oRs.CreateStream("probe")
oS.SetOverflowStrategy(BUFFER_REJECT_NEWEST, 2)
for i = 1 to 4
	oS.Receive(i)
next
? oS.OverflowStats()[:currentBuffer]
#--> 2
? oS.OverflowStats()[:droppedCount]
#--> 2
```

It says `currentBuffer` is `2` and `droppedCount` is `2`. The counter that read zero now counts!

And for what the field calls debounce, Reaxis says what it means: wait for the attribute to settle. Three changes in quick succession: how many reactions, once the value has stopped changing for fifty milliseconds?

```haro
nSettled = 0
oRs4 = new stzReactive()
oX = oRs4.ReactiveObject()
oX.WaitForAttributeToSettle("query", 50, func(attr, oldV, newV) { nSettled++ })
oX.SetAttribute("query", "s")
oX.SetAttribute("query", "so")
oX.SetAttribute("query", "sof")
oX { ProcessPendingReactions() }
oRs4.RunLoop()
? nSettled
#--> 1
oRs4.Stop()
```

One reaction. `nSettled` reads `1`.

The chapter's third subject is the engines, the small paradigms the library rethought one by one. Chapter 3 gave you truth and emptiness. Two more, run here. Time is a workspace, not a number. A timeline holds spans and computes the gaps and the overlaps. What does it say of the gap between two phases, and what does it do with a point that would fall into a blocked region?

```haro
oTl = new stzTimeLine("2024-01-01 00:00:00", "2024-12-31 23:59:59")
oTl.AddSpan("PHASE1", "2024-01-01 00:00:00", "2024-02-15 23:59:59")
oTl.AddSpan("PHASE2", "2024-03-01 00:00:00", "2024-04-15 23:59:59")
? len(oTl.Gaps())
#--> 1
? oTl.Gaps()[1][:after]
#--> PHASE1
? oTl.Gaps()[1][:before]
#--> PHASE2
? oTl.HasOverlaps()
#--> FALSE
oTl.AddSpan("PHASE2B", "2024-04-01 00:00:00", "2024-05-15 23:59:59")
? oTl.HasOverlaps()
#--> TRUE
oB = new stzTimeLine("2024-01-01", "2024-12-31")
oB.AddBlockedSpan("MAINTENANCE", "2024-06-15 09:00:00", "2024-06-15 17:00:00")
oB.AddPoint("EVENT1", "2024-06-15 08:00:00")
try
	oB.AddPoint("EVENT2", "2024-06-15 12:00:00")
catch
	? cCatchError
done
#--> Point 'EVENT2' falls within a blocked span or blocked point
```

The gap is named by what it lies between, `PHASE1` and `PHASE2`. The blocked span refused `EVENT2`! The refusal carries its reason: `Point 'EVENT2' falls within a blocked span or blocked point`.

And a grid has a cursor that knows where it is: position is column and row, and moving past an edge stays at the edge. Two moves down and three to the right, then three more to the right: where is the cursor?

```haro
o = new stzGrid([ 5, 5 ])
o.MoveDown()
o.MoveDown()
o.MoveRight()
o.MoveRight()
o.MoveRight()
? @@( o.CurrentPosition() )
#--> [ 4, 3 ]
o.MoveRight()
o.MoveRight()
o.MoveRight()
? @@( o.CurrentPosition() )
#--> [ 5, 3 ]
```

At `[ 4, 3 ]`, then at `[ 5, 3 ]`. Three more moves to the right gained one column, and the cursor stayed at the edge!

## 4. The decision, and what I refused

**I refused to leave regex as a way to read text.** I made it a computational medium. A trigger fires a computation, the computation writes a state when it changes the value, and the state records its why. The Regexuter is a faculty and not a mind, and it holds no goal. I added the goal two rungs above it, at the fourth rung, in the agent, on purpose.

**I refused the field's vocabulary for reactive programming.** Observables, subscribers, backpressure, hot and cold sources, schedulers: borrowed from plumbing, telephony and publishing, and not from the problem. A function in waiting is an Rfunction. Data flows, and nothing is called a producer or a consumer. Overflow replaces backpressure. Waiting for an attribute to settle replaces debounce. The old spellings still work as aliases: feed, emit, send and receive all call one method, so my change was one of naming and not of removal.

**I refused to build the siblings.** The article that tells the Regexuter describes four more: an analyser, a genetic one, a linguistic one and a quantic one. In the genetic one patterns evolve against a fitness, in the linguistic one triggers are grammar rules, and in the quantic one a pattern can be in several states at once. The article gives each a sample call, and no class stands behind it. The design later found a purpose for two of them. Answering by example demands pattern induction, the genetic one's ground; several acceptable answers demand superposed candidates, collapsed by rules or by choice, the quantic one's. Chapter 18 tells where that stands. They remain a vision; two have their purpose written.

**I refused to claim the cascade.** The library's architecture says it itself: the scaffolding anticipates cascading but does not yet re-fire dependent triggers to a fixpoint. I would rather show you the block that fails to cascade than a block that does.

## 5. The court

The Regexuter and the Listexuter have classic tests, and no narrated guard. The Regexuter's eight classic tests ran without error: the folder's log reads `PASS 8 ERR 0`. Nothing there checks what they print. Five of the Listexuter's seven fail their own expected output, and two promise nothing. The agent's cascade is proved by `piagent_narrated`, scene five. Reaxis has many guards. `00_overflow_narrated` proves the four overflow strategies and the case that loses nothing; `60_reaxis_on_reactor_narrated` proves a one-shot timer, the repeating timer, non-blocking HTTP and the settling attribute on the engine's loop. The timeline has `test_timeline_regression`, which covers construction, duration, adding points and moving the ends, and not gaps, overlaps or blocked spans. The grid has `00_grid_narrated`, and deep operations `01_deeplist_narrated`.

The next section sets this record beside the field's.

## 6. The field, and where it leads

The field's rule engines lead. They are older and more mature than the Regexuter, they chain to a fixpoint, and the algorithms behind them are decades old. What I claim is not a rule engine. It is the condition side: rules that are sentences of the pattern languages, over the two media that have a reacting machine built, text for the Regexuter and lists for the Listexuter. The state keeps, for every firing that changes a value, its why. The library's own architecture calls the Regexuter a nascent forward-chaining rule engine, and I will not call it more.

The field's reactive libraries lead in reach. Rx exists in most mainstream languages, with a large set of operators; that is general knowledge. Reaxis is one library on one event loop. The engine's own module for it is a small table of substring rules: the Container, Stream and Rfunction model lives in the library, on the event loop of the engine.

I will not print the star-rating comparison with the field's tools that the library's article on reactive objects carries. It is undated and unsourced.

The next section says where all of this stops.

## 7. The limit

What is built: the Regexuter and the Listexuter; Reaxis on the engine's event loop; the timeline, the grid and deep operations; the AI agent whose skills chain.

What is designed: the third rung, many faculties on one shared state, cascading until it settles. The universal engine for it is planned. The four siblings are vision. The macroplan marks the engine module as done, and the architecture table marks it planned: the same name for two things. That table marks every module of its fifth layer planned, including ones that have source, so it is stale on this point. The universal medium is planned in the engine design document.

What is absent or broken at this commit:

- The dependency chain is not one. Each state entry depends only on its own trigger, so the chain records which trigger was active and never a link between two. Asking for the chain overflows the stack: the run ends with `Error (R4) : Stack Overflow`. No test calls it.
- Five of the Listexuter's seven classic tests fail their own expected output, and two promise nothing. The error log of that folder records, in the sixth file, `Error (C8) : Parentheses ')' is missing`.
- A nested list that matches as a whole is reported twice.
- The article's repeating timer takes three arguments and the library takes two; the form with units is `RunEveryXT`.
- Two of the deep-lists article's path verbs, `ItemAtPath` and `ItemsAtPaths`, live on a subclass, `stzDeepList`, and not on a plain list; `Paths()` is on a plain list.
- The section-merging article presents a comprehensive verb as its point, and that verb does not exist. The two that do exist, merging what overlaps and merging what is included, run. Section merging has no test file of its own.
- There is no native engine module for the Container, Stream and Rfunction model: it runs in the library, and the engine's own reactive module is a small table of substring rules. The timeline's guard checks no gap, no overlap and no blocked span; in the classic timeline files, seven fail their expected output and eighteen promise nothing. The grid's engine-backed navigator, `stzGridNav`, has no test.

## 8. Six doors

**The programmer.** Bind a pattern to code, and process; or declare a stream and say in words what happens to the data that flows through it.

**The analyst.** Time is a workspace: gaps, overlaps and blocked regions are computed, and a point that would fall in a blocked region is refused with the reason.

**The designer.** The state of a reaction that changes a value keeps its why: the match, the computed value, the position, the trigger.

**The decision-maker.** Overflow is a number you can read: kept, dropped. A strategy that lost data and said nothing was found by an audit, and fixed.

**The educator.** The ladder is a curriculum: a pattern, a reaction, a state, a goal.

**The agent.** Your mind can be skills that chain on what they perceive, until the world stops changing.

## 9. Exercise

Write a Regexuter with two triggers, one for numbers and one for numbers of three digits or more, with code that turns a number into its triple. Before you run it, write under each question what you expect: what the matches are, what the results are, and whether the second trigger fires on the first one's result. Run it. If the second trigger fires, you have found something I did not.

Then say in one sentence what would have to change in the machine for it to fire, and which rung of the ladder that change belongs to.

I left this one in your hands. Take the second block of section 3 and write its two `Trigger` lines in the other order, the three-digit one first:

```haro exercise
rxu() {
	Trigger(:Big = "\d{3,}")
	Trigger(:Number = "\d+")
	@C(:When = :Number, :Do = '{ @value = @number(@value) * 100 }')
	@C(:When = :Big, :Do = '{ @value = "BIG" }')
	Process("Found 7 items")
	? @@( Matches() )
	? @@( Results() )
	? @@( Triggers() )
}
```

Before you run it, write down whether the order changes what `Results()` and `Triggers()` hold. I do not print the output of this version, and I do not tell you the answer: section 3 says what each trigger is matched against, and section 4 says what I refused to claim. When you can say why, you will know what separates the second rung from the third.

Chapter 10 turns from the machine that thinks to the code that changes. Its title is *Programming becomes refinement*, and it holds to one principle: stop trying to govern the intelligence, and govern the change.
