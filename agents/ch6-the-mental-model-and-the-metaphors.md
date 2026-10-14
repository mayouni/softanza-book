# The mental model, and the metaphors

Source: Chapter 6. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the one-dimensional walker, the checker, the yielder and the performer on lists; the condition language compiled by the engine, with its host-code twin; designed: the four metaphors as native engine modules (only the yielder is one); a walker over any indexed structure; absent: runnable code for the three models of the article 'Bridging Minds and Code'; the edge table of the walker narration as written

Run: 7 of 7 blocks kept their promise, on 2026-10-14 12:13 UTC+01:00.

In this chapter I take the seven steps of the mental model, which chapter 5 ran on a list, and run them on a string, in the same order. Then I come to the loop, the place where the steps repeat, and to the four metaphors the library gives you instead: the walker, the checker, the yielder and the performer. I show the condition that all four carry inside an argument, the W condition the engine reads as data, and its WF twin, which runs host code. I say why I made the metaphors a design goal, why I replaced `eval` with a language the engine owns, and where the code of the articles this chapter rests on is not yet runnable at this commit. The principle under all of it is the chapter's own: when you would write a loop, name the move you are making, walk, check, yield or perform.

## 1. The concept, as the field holds it

The field has one tool for repeating a thing, the loop, and a family of cousins that hide it: the iterator, the comprehension, the stream with its map, filter and reduce, the lambda that carries a condition. They are good tools, and they all share one habit. They are written in the language of the machine's motion: an index that starts at zero, a counter that is incremented, a variable that accumulates. A person who reads the loop has to recover the question it asks.

The field also has a vocabulary of metaphors for programming, but it keeps them in the documentation. The code stays a loop.

## 2. The first principle

**Say the problem in plain words, ask the same questions in the same order of any object, and when you would write a loop, name the move you are making: walk, check, yield or perform.** The site's Craft page says it, in the words of a session of 2 October 2026, as the page reads on 9 October 2026: "A loop hides which move it is making. Softanza names the four moves, and a task is decomposed into them instead." That sentence is the site's, not mine; the sentence above is this chapter's principle.

## 3. The Softanza form

The mental model is seven steps, and they are the order in which a person asks. Define the problem in natural terms and take its keywords. Select the object that holds the data. Ask whether it contains what you care about. Ask how many. Ask where. Act on those positions, or call the verb that does it. And celebrate, and repeat. In chapter 5 you ran those steps on a list with empty strings. They do not belong to the list. Do they hold on a string? Here they are, in the same order:

```haro
o1 = new stzString("You and you")
? o1.ContainsCS("YOU", FALSE)
#--> TRUE
? o1.NumberOfOccurrenceCS("YOU", FALSE)
#--> 2
? o1.FindNthCS(2, "YOU", FALSE)
#--> 9
o1.ReplaceSection(9, 11, :With = "Me")
? o1.Content()
#--> You and Me
```

> run: kept

Contain prints `TRUE`, count prints `2`, find prints `9`, and act leaves `You and Me`, with the same suffix that says whether case matters. The three questions you ask of a string are the three you asked of a list.

When the steps repeat, the loop appears, and this is where the library gives you four metaphors instead. Each one names a move.

**The Walker moves along a route.** A walker is a map of its whole journey, built when it is created. It holds the positions it will visit, the positions it will skip, where it stands and what remains. What does it know before it takes a step? Ask it:

```haro
oWalker = Wk(1, 10, 2)
? @@( oWalker.Walkables() )
#--> [ 1, 3, 5, 7, 9 ]
? @@( oWalker.Unwalkables() )
#--> [ 2, 4, 6, 8, 10 ]
? @@( oWalker.Walk() )
#--> [ 1, 3 ]
? oWalker.CurrentPosition()
#--> 3
? @@( oWalker.RemainingWalkables() )
#--> [ 5, 7, 9 ]
```

> run: kept

A loop does not hold its route as a value you can ask. A walker does, before it moves. What does it do at the edge of the road? Beyond the end, when the walk is underway, it stops in silence. Before the start, it refuses:

```haro
oWalker = Wk(1, 10, 3)
? @@( oWalker.WalkNSteps(10) )
#--> [ 1, 4, 7, 10 ]
? @@( oWalker.Walk() )
#--> [ 10 ]
oWalker = Wk(1, 10, 3)
try
	oWalker.WalkBackward()
catch
	? cCatchError
done
#--> Can't walk backward! Already at the beginning of walkable positions.
```

> run: kept

Ask for ten steps from a walk that has four and you get the four: `[ 1, 4, 7, 10 ]`. Walk again and it prints `[ 10 ]`, with no error. Ask it to walk backward from the start and it refuses! Its own words: `Can't walk backward! Already at the beginning of walkable positions.` The article argues that this mirrors how we walk in the physical world. You stop when you hit a wall behind you, and that is an error. When the road ahead ends, you stop in silence.

**The Checker asks yes or no.** All of them, any of them, or where:

```haro
o1 = new stzList([ "A", 5, "B", "C" ])
? o1.CheckW('{ isString(@item) and IsUppercase(@item) }')
#--> FALSE
? o1.ContainsW('{ isNumber(@item) }')
#--> TRUE
? @@( o1.FindW('{ isNumber(@item) }') )
#--> [ 2 ]
```

> run: kept

One item fails the test, so `CheckW` prints `FALSE`; a number is in the list, so `ContainsW` prints `TRUE`; and `FindW` says where, `[ 2 ]`.

**The Yielder produces new data from old, and leaves the old alone.** **The Performer is its opposite number: it changes the items where the condition holds.** Which of the two touches the list? Put them side by side on the same list and look:

```haro
o1 = new stzYielder([ 1, -2, 3, -4, 5 ])
? @@( o1.Filter(:IsPositive) )
#--> [ 1, 3, 5 ]
? @@( o1.Map(:Abs) )
#--> [ 1, 2, 3, 4, 5 ]
? o1.Reduce(:Sum)
#--> 3
o2 = new stzList([ 1, "haro", 3, "python", 5, "ruby" ])
? @@( o2.YieldW('isString(@item)', 'upper(@item)') )
#--> [ "HARO", "PYTHON", "RUBY" ]
? @@( o2.Content() )
#--> [ 1, "haro", 3, "python", 5, "ruby" ]
o2.PerformW('isString(@item)', 'upper(@item)')
? @@( o2.Content() )
#--> [ 1, "HARO", 3, "PYTHON", 5, "RUBY" ]
```

> run: kept

Look at the two `Content()` outputs, before and after the `PerformW` call. The yield returned `[ "HARO", "PYTHON", "RUBY" ]`. The list was untouched! The perform changed the list: `[ 1, "HARO", 3, "PYTHON", 5, "RUBY" ]`. The verb tells you which, so a design can say "this step only reads" and mean it.

Now the thing that all four share, which is the last piece of the title: a condition travels inside an argument. It is a small string, kept in a variable if you want. It goes in the same place for find, for items and for contains. And it has a twin that takes a real function:

```haro
o1 = new stzList([ 3, 8, 5, 12, 1, 9 ])
cCond = '{ @item > 5 }'
? @@( o1.FindW(cCond) )
#--> [ 2, 4, 6 ]
? @@( o1.ItemsW(cCond) )
#--> [ 8, 12, 9 ]
? o1.ContainsW(cCond)
#--> TRUE
? @@( o1.FindWF( func x { return x > 5 } ) )
#--> [ 2, 4, 6 ]
```

> run: kept

The two agree: `FindW` with the string and `FindWF` with the function both print `[ 2, 4, 6 ]`. `ItemsW` gives the items themselves, `[ 8, 12, 9 ]`.

The string form is the W condition, W for where; the function form is WF. They look alike, and the difference matters. The engine reads a W condition as data, in a small language of its own: literals, `@item`, arithmetic, comparisons, and a short list of functions. It cannot call your code. So what happens to a condition that tries to? It is not run:

```haro
o1 = new stzList([ 3, 8, 5, 12, 1, 9 ])
? @@( o1.FindW('{ @item > 5 and print("hacked") }') )
#--> [ ]
? @@( W('{ @item > 5 }') )
#--> [ "where", "{ @item > 5 }" ]
```

> run: kept

Nothing was printed! The positions came back empty, `[ ]`, and `W()` shows the condition for what it is, data: `[ "where", "{ @item > 5 }" ]`. A W condition can be stored, shown to a person, and approved before it runs, because it cannot escape. The WF twin runs host code, and the library's own table says it is not safe with input you do not trust.

The code of the article "Bridging Minds and Code" does not run at this commit, as section 7 says.

The three models of that article, the semantic, the mental and the expression, are one idea in three places. The semantic model is the world of the program as knowledge: an apple is a fruit. The mental model is what you just did: create an object, store data in it, find things inside it, act on the positions. The expression model is the code that says it: select the object, type the name of the action, continue the flow of actions, convert the result into another object. Keep doing so until you have the final answer. So I tell them in words.

The next section gives the decision, and what I refused.

## 4. The decision, and what I refused

**I made the metaphors a design goal.** The 2022 presentation lists "human-centric metaphors" as one of seven design goals, and its four features are these four. A goal is what makes a feature justifiable or refusable. I hold this as a view, not a result. So I did not leave the metaphors as a nicety of the documentation. They are one of the reasons the library has the shape it has.

**I replaced `eval` with a language the engine owns.** The condition seat used to be compiled by evaluating the string as code, with a more expressive but slower extended form on the side. I removed both. The engine now reads the condition in its own small language, and the library keeps the host-code form as a separate verb, WF, with its warning. I refused arbitrary code from text, and I refused to split speed from expressiveness: the extended form is retired because the plain one does everything it did.

**I kept the seven steps as written.** When the course was designed, a reading of the technical core found five steps: select, contains, count, find, apply. The course teaches the seven as the source narration has them. Nobody renumbers the source.

**I let the edge rule be a design principle.** Before the start is an error, and beyond the end is ignored. The narration gives its reason in a sentence: it mirrors how we walk. The record does not date it as a ruling, so I tell it as the library's design.

The court comes next, and its guards do not cover every line above.

## 5. The court

The four metaphors have no single guard. The yielder has a narrated one, `00_yielder_narrated`: four map operations, three filter operations and a sum. The walker has `597_walker_basics`, named walkers and what they walked, and `495_walking_until_and_until_before`, a walk that stops on a condition, including the item that stops it, or not. The checker has `611_checkw`, which says a check is false when one item fails. The performer has `621_perform`, which says it changes the list in place. `483_w_and_wf_forms_in_conditional_code` proves that a W condition written with cursor words such as `@NextNumber` and the same one written with raw index arithmetic such as `This[@i+1]` give the same positions. `597_walker_basics` and `495_walking_until_and_until_before` test the list's named walkers and walks, through `StzListQ`, not the `Wk` walker of the blocks above.

None of the guards named here covers `Walkables`, `WalkNSteps` or `WalkBackward`; those lines rest on the runs kept for this chapter.

Next, what the field does better than the walker.

## 6. The field, and where it leads

The field leads in laziness. A generator produces the next item on demand and can be endless. The walker builds a map of its whole journey the moment it is made. That is a win for foresight: you can ask which positions it will skip before it moves. It is a loss for a large or endless traversal.

The field leads in openness. A lambda carries any logic. The W language is bounded on purpose, and the price of the bound is the second path, WF, which has full host power and is meant for input you trust. There is also a quieter cost I measured once, on one case: a condition that calls something the language does not know gives an empty list and no error.

The field leads in reach and in tooling. Iterators and comprehensions are in every mainstream language, with editor support, type checking and a literature. These four metaphors exist in one library.

And I will not print the library's own comparison of walkers with loops and iterators. Its table has thirteen rows, all of them in the walker's favour, none of them run. A table is worth printing when its rows have been run and a loss stands beside the wins; for this one, that is the next step. This is my view, held on this table: thirteen rows, none with a loss.

Next, the limit, in the stage words built, designed and absent.

## 7. The limit

What is built: the one-dimensional walker, in the max layer, and the walks on lists; the checker as `CheckW`, `ContainsW` and `FindW`; the yielder as a class backed by the engine, and as `YieldW`; the performer as `PerformW`; and the W condition language compiled by the engine.

What is designed: the metaphors as native engine modules. The engine's design marks all four as planned; only the yielder has an engine file. And a walker that is not about lists at all but about any indexed structure.

Six things are absent, or still to be aligned with their articles, at this commit, from my runs.

- The walking-at-the-edge article's table and the library differ in two cases; aligning them is the next step. A single step larger than the range raises where the table promises silence, and a mixed-direction path raises where it promises acceptance. The two principles hold in the cases shown above. The book states the principle and prints only the cases that run; the table is not printed.
- The "Beyond Loops" article's code differs in places. The history of a walker is a list of walks; a backward walk takes no argument now; the direction prints as "backward" where the article says "reverse". The site's own run of the article kept ten of eighteen blocks.
- The three models of "Bridging Minds and Code": none of its code runs as written; in the site's run twelve blocks raised and one differed. So I told them in words.
- The mental-model article's getter `EmptyStrings()` is absent.
- On the dedicated checker class, `ContainsW` is in development: it raises today. The string walker's backward-with-condition walk is absent.
- And "no eval" is still on its way to everything. The near-natural resolver, the other direction of chapter 13, still evaluates host code. So do `StringsW` and `ItemsWhere` on the list, and `ContainsW` on the dedicated checker class: each still calls `eval` on a condition string. What I said above, that the engine reads a W condition and cannot run it as code, holds for the engine's path; for these three it is the next step.

Next come the six doors, from the programmer to the agent.

## 8. Six doors

**The programmer.** Ask the same four questions of any object, and when you reach for a loop, name the move: walk, check, yield or perform.

**The analyst.** Say the problem in plain words, and the verbs you used are the steps: "are all of them", "which ones", "give me the big ones", "make them negative".

**The designer.** The yielder never changes the list and the performer does, and the verb tells you which.

**The decision-maker.** A W condition is a string the engine reads and cannot run as code, so it can be stored, shown and approved. The price is a small language, and a call it does not know gives an empty list, not an error.

**The educator.** The self-study book already has the order: find, then apply, then walk, ask, produce and act.

**The agent.** Write the condition as the string, not as code. When the answer is empty, check the condition's words before you trust the emptiness.

## 9. Exercise

Take the list `[ 4, 9, 12, 7, 20, 3 ]`. Four sentences are given. One: are all of them above 2? Two: give me, as a new list, those above 8, doubled. Three: make the ones above 8 negative, in the list itself. Four: which positions are 2, 4 and 6?

For each, say first which move it is, walk, check, yield or perform, and write under the line you will write what you expect it to print. Then write the line, with the condition as a string wherever there is a condition, and run it. After the second and the third, print the list again. Say, before you look, in which of the two the list has changed.

I left this one in your hands, on purpose. Here is the block of section 3 with one change: the list is the exercise's list, and I print nothing under it.

```haro exercise
o1 = new stzList([ 4, 9, 12, 7, 20, 3 ])
? @@( o1.FindW('{ @item > 5 and print("hacked") }') )
```

> run: exercise

Run it. The condition begins by asking whether an item is above 5. Look at what comes back, and at what does not, and say why before you go back to the sections. Section 3 says what the engine does with a condition that calls code; section 6 says what that costs, and section 8 says what an AI agent should do about it. When you have solved it, you will know why an empty answer is not yet a proof that nothing matched.

The next chapter turns to the writing style, and to the seven goals. Its principle is one sentence: what you think is what you write.
