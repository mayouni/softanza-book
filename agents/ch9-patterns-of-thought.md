# Patterns of thought: the Softanzuter, Reaxis and the engines

Source: Chapter 9. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the Regexuter and the Listexuter, reacting with a state that remembers; Reaxis, reactive programming in plain words, on the engine's event loop; the timeline, the grid and deep operations; the agent whose skills cascade to a fixpoint; designed: the Softanzuter proper, many faculties sharing one state and cascading until it settles; the universal engine behind it; its three siblings, genetic, linguistic and quantic; absent: a dependency chain that links one trigger to another; a section-merging verb the article presents as its point

Run: 8 of 8 blocks kept their promise, on 2026-10-09 02:55 UTC+01:00.

## 1. The concept, as the field holds it

The field has three tools for making a program react. Regular expressions recognise a shape in text, and nothing more: they say "this matches", and they stop. Reactive programming, the family of observables, subscribers and schedulers that Rx made popular, lets data flow through a program over time; its vocabulary comes from plumbing, telephony and publishing: pipes, backpressure, hot and cold sources. And rule engines, the production systems of the field with their forward chaining, fire rules when facts appear, and keep firing while new facts appear. (General knowledge; the rule engines of the field are older and more mature than anything in this chapter.)

Each tool is separate. A regular expression does not trigger a computation, a reactive stream does not recognise a pattern, and a rule engine does not have a vocabulary that a person would use to say a thought.

## 2. The first principle

The definition I gave this paradigm is a single sentence, and everything below is an attempt to make it mechanical: **a Softanzuter is a computational representation of a thinking machine, based on one or many Regexuters, enabling it to identify and react to patterns of thought.**

## 3. The Softanza form

I think of it as a ladder with four rungs, each adding one thing.

The first rung is the pattern. You have seen it in chapter 11: a shape in a medium, a string, a list, a number, that can say "this matches, and here is how", and do nothing more. The second rung gives a pattern a reaction: the Regexuter, a reflex arc. You bind a pattern to code, process a text, and the code fires on every match. A Regexuter reacts, and it remembers what it did. Here it redacts the secrets in a sentence, and the state it keeps says what it matched, what it computed, where, and which trigger fired:

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

> run: kept

The state is provenance: every reaction keeps its why. The last line is also an honest limit, and I will come back to it: what the Regexuter records as a dependency is today only its own trigger.

Now the third rung, the one the definition is about: many Regexuters, over different media, sharing one state, so that what one faculty writes is a medium another faculty can match over. A thought is a state entry with its provenance, and a settled thought is a state in which nothing more fires. That rung is not built, and the block shows how I know. The second trigger below is written for numbers of three digits or more. The first trigger turns the 7 into 700, which is one. If the machine thought in cascades, the second would fire on the first's result:

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

> run: kept

It did not. Every trigger is matched once against the original text, and what one trigger writes is not offered to the others. That is the whole difference between the second rung and the third.

The cascade runs one rung above, in the agent: a mind made of skills, each with a condition and an action, which chain. The second skill fires on the fact the first one wrote. `Pursue()` returns how many skills fired and goes on until the world stops changing; asked again, it answers zero. That is a fixpoint:

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

> run: kept

The guard that proves it labels the scene in its own words: the cascade to fixpoint, the Softanzuter at agent level. In chapter 17 you saw this same agent refused at a gate. Here is the other face of it: the agent that chains, because its mind is programmatic.

So the word has three meanings in the record, and the reader deserves to be told which is which. In this chapter, "Softanzuter" is the third rung, the thinking machine of the definition: designed, not built. The engine has a module with the same name, which is the body of the agent: slots with a state and a bounded mailbox, where a message into a full queue is refused, counted and never dropped quietly. And the design of a universal engine behind all of it, a medium where any pattern language becomes a computation, is planned.

**Reaxis** is the other half of the chapter's title, and it is a different idea. It is reactive programming with a vocabulary redesigned from the ground. A reactive thing is a Container, a Stream and an Rfunction: a function in waiting, which is not a callback. Data flows through a stream in plain words, a transformation, a filter, what to do with what passes:

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

> run: kept

The 80 becomes 96 and is dropped by the filter; the 90 becomes 108 and passes. Three functions are in waiting, and nothing subscribes to anything.

Reaxis replaced backpressure with overflow, a word you do not need a diagram to understand. And it was audited. A reading of the four strategies the article documented found that three of them lost data and reported none: the default discarded everything past the capacity while the counter read zero. That is fixed, and proved for all four strategies. Here, four items into a buffer of two, and the stream says what happened:

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

> run: kept

And for what the field calls debounce, Reaxis says what it means: wait for the attribute to settle. Three changes in quick succession, one reaction, after the value has stopped changing for fifty milliseconds:

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

> run: kept

The third part is the engines, the small paradigms the library rethought one by one. Chapter 3 gave you truth and emptiness. Two more, run here. Time is a workspace, not a number: a timeline holds spans, computes the gaps and the overlaps, and a blocked region refuses a point that would fall into it, with the reason, at insertion:

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

> run: kept

And a grid has a cursor with the intelligence of a place: position is column and row, and moving past an edge stays at the edge.

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

> run: kept

## 4. The decision, and what I refused

**I refused to leave regex as a way to read text.** I made it a computational medium: a trigger fires a computation, the computation writes a state, and the state records its why. The Regexuter is a faculty and not a mind, and it holds no goal. I added the goal at the rung above it, in the agent, on purpose.

**I refused the field's vocabulary for reactive programming.** Observables, subscribers, backpressure, hot and cold sources, schedulers: borrowed from plumbing, telephony and publishing, and not from the problem. A function in waiting is an Rfunction. Data flows without a theatre of producers and consumers. Overflow replaces backpressure. Waiting for an attribute to settle replaces debounce. The old spellings still work as aliases: feed, emit, send and receive all call one method, so my change was one of naming and not of removal.

**I refused to build the siblings.** The article that tells the Regexuter describes four more: an analyser, a genetic one where patterns evolve against a fitness, a linguistic one where triggers are grammar rules, and a quantic one where a pattern may be in several states at once. I wrote them in prose and not in code, and the design later found their purpose: answering by example demands pattern induction, and several acceptable answers demand superposed candidates, collapsed by rules or by choice. Chapter 18 tells that. They remain a vision, with their purpose written.

**I refused to claim the cascade.** The library's architecture says it itself: the scaffolding anticipates cascading but does not yet re-fire dependent triggers to a fixpoint. I would rather show you the block that fails to cascade than a block that does.

## 5. The court

The Regexuter and the Listexuter have classic tests, and no narrated guard. The Regexuter's tests that I ran keep their promises; the Listexuter's first five do not. The agent's cascade is proved by `piagent_narrated`, scene five. Reaxis has many guards: `00_overflow_narrated` proves the four overflow strategies and the case that loses nothing; `60_reaxis_on_reactor_narrated` proves the repeating timer, the settling attribute and the stream on the engine's loop. The timeline has `test_timeline_regression`, the grid `00_grid_narrated`, and deep operations `01_deeplist_narrated`.

## 6. The field, and where it leads

The field's rule engines lead. They are older and more mature than the Regexuter, they chain to a fixpoint, and the algorithms behind them are decades old. What I claim is not a rule engine but the condition side: rules that are sentences of the pattern languages over six media, and a state in which every firing keeps its why. The library's own architecture calls the Regexuter a nascent forward-chaining rule engine, and I will not call it more.

The field's reactive libraries lead in reach. Rx exists in every mainstream language, with operators by the hundred. Reaxis is one library on one event loop. The engine's own module for it is a small table of substring rules: the Container, Stream and Rfunction model lives in the library, on the event loop of the engine.

I will not print the article's comparison with the field's star-rating example. It is undated and unsourced.

## 7. The limit

What is built: the Regexuter and the Listexuter; Reaxis on the engine's event loop; the timeline, the grid and deep operations; the agent whose skills chain.

What is designed: the third rung, many faculties on one shared state, cascading until it settles. The universal engine for it is planned. The three siblings are vision. The macroplan marks the engine module as done and the architecture table marks the planned medium as planned: the same name for two things.

What is absent or broken at this commit:

- The dependency chain is not one. Each state entry depends only on its own trigger, so the chain records which trigger was active and never a link between two. Asking for the chain overflows the stack. No test calls it.
- The Listexuter's classic tests keep none of their promises. Its first block no longer raises the error its log remembers, but it still prints the last section's result three times, and its server pattern never fires.
- A nested list that matches as a whole is reported twice.
- The article's repeating timer takes three arguments and the library takes two; the form with units is `RunEveryXT`.
- The deep-lists article's path verbs live on a subclass, `stzDeepList`, and not on a plain list.
- The section-merging article presents a comprehensive verb as its point, and that verb does not exist. The two that do exist, merging what overlaps and merging what is included, run. Section merging has no test file of its own.
- And the dependency of the model on the engine: the Container, Stream and Rfunction model runs in the library, not in a native module.

## 8. Six doors

**The programmer.** Bind a pattern to code, and process; or declare a stream and say in words what happens to the data that flows through it.

**The analyst.** Time is a workspace: gaps, overlaps and blocked regions are computed, and a point that would fall in a blocked region is refused with the reason.

**The designer.** The state of a reaction keeps its why: the match, the computed value, the position, the trigger.

**The decision-maker.** Overflow is a number you can read: kept, dropped. A strategy that lost data and said nothing was found by an audit, and fixed.

**The educator.** The ladder is a curriculum: a pattern, a reaction, a state, a goal.

**The agent.** Your mind can be skills that chain on what they perceive, until the world stops changing.

## 9. Exercise

Write a Regexuter with two triggers, one for numbers and one for numbers of three digits or more, with code that turns a number into its triple. Before you run it, write under each question what you expect: what the matches are, what the results are, and whether the second trigger fires on the first one's result. Run it. If the second trigger fires, you have found something I did not.

Then say in one sentence what would have to change in the machine for it to fire, and which rung of the ladder that change belongs to.
