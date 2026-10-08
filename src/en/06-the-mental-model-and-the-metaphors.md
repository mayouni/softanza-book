---
id: the-mental-model-and-the-metaphors
part: 2
number: 6
title: The mental model, and the metaphors
spine: false
narrations: [stz-mental-mode-narration.md, stzwalker-beyond-loops-the -walker-metaphor.md, stzwalker-walking-at-the-edge-narration.md, stz-conditional-code-narration.md, stz-bridging-minds-and-code.md]
site: [learn, craft]
guards: [00_yielder_narrated, 597_walker_basics, 611_checkw, 621_perform, 483_w_and_wf_forms_in_conditional_code, 495_walking_until_and_until_before]
stage:
  built: "the one-dimensional walker, the checker, the yielder and the performer on lists and strings; the condition language compiled by the engine, with its host-code twin"
  designed: "the four metaphors as native engine modules (only the yielder is one); a walker over any indexed structure"
  absent: "runnable code for the three models of the founding article; the edge table of the walker narration as written"
status: draft
rulings: ["12.3", "12.6", "12.14", "12.16", "12.17"]
research: research/ch06.md
---

## 1. The concept, as the field holds it

The field has one tool for repeating a thing, the loop, and a family of cousins that hide it: the iterator, the comprehension, the stream with its map, filter and reduce, the lambda that carries a condition. They are good tools, and they all share one habit. They are written in the language of the machine's motion: an index that starts at zero, a counter that is incremented, a variable that accumulates. A person who reads the loop has to recover the question it asks.

The field also has a vocabulary of metaphors for programming, but it keeps them in the documentation. The code stays a loop.

## 2. The first principle

**Say the problem in plain words, ask the same questions in the same order of any object, and when you would write a loop, name the move you are making: walk, check, yield or perform.** [AUTHOR: The site's Craft page says "a loop hides which move it is making; Softanza names the move", in a session's words of 2 October 2026. May the book give you that sentence as your principle for the metaphors?]

## 3. The Softanza form

The mental model is seven steps, and they are the order in which a person asks. Define the problem in natural terms and take its keywords. Select the object that holds the data. Ask whether it contains what you care about. Ask how many. Ask where. Act on those positions, or call the verb that does it. And celebrate, and repeat. In chapter 5 you ran those steps on a list with empty strings. They do not belong to the list. Here they are on a string, in the same order:

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

Contain, count, find, act, and the same suffix that says whether case matters. The three questions you ask of a string are the three you asked of a list.

When the steps repeat, the loop appears, and this is where the library gives you four metaphors instead. Each one names a move.

**The Walker moves along a route.** A walker is a map of its whole journey, built when it is created: the positions it will visit, the positions it will skip, where it stands, what remains.

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

A loop cannot tell you which positions it will skip until it has skipped them. A walker can, before it moves. And it has a rule for the edge of the road. Beyond the end, it stops in silence. Before the start, it refuses:

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

Ask for ten steps from a walk that has four and you get the four. The article argues that this mirrors how we walk in the physical world: a path may end, and a step behind the first is not a step.

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

**The Yielder produces new data from old, and leaves the old alone.** **The Performer is its opposite number: it changes the items where the condition holds.** Put side by side on the same list, the contrast is the point:

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

Look at the third line from the end and the last one. The yield returned the uppercase words and the list was untouched. The perform changed the list. The verb tells you which, so a design can say "this step only reads" and mean it.

Now the thing that all four share, which is the last piece of the title: a condition travels inside an argument. It is a small string, in the same seat of find, of items, of contains, kept in a variable if you want; and it has a twin that takes a real function:

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

The string form is the W condition, W for where; the function form is WF. They look alike and differ in a way that matters. The engine reads a W condition as data, in a small language of its own: literals, `@item`, arithmetic, comparisons, and a short list of functions. It cannot call your code. So a condition that tries to is not run:

```haro
o1 = new stzList([ 3, 8, 5, 12, 1, 9 ])
? @@( o1.FindW('{ @item > 5 and print("hacked") }') )
#--> [ ]
? @@( W('{ @item > 5 }') )
#--> [ "where", "{ @item > 5 }" ]
```

Nothing was printed. A W condition can be stored, shown to a person, and approved before it runs, because it cannot escape. The WF twin runs host code, and the library's own table says it is not safe with input you do not trust.

The three models of the founding article, the semantic, the mental and the expression, are one idea in three places. The semantic model is the world of the program as knowledge: an apple is a fruit. The mental model is what you just did: create an object, store data in it, find things inside it, act on the positions. The expression model is the code that says it: select the object, type the name of the action, continue the flow of actions, convert the result into another object, and keep doing so until you have the final answer. I tell them in words because the article's code does not run at this commit, as section 7 says.

## 4. The decision, and what I refused

**I made the metaphors a design goal.** The 2022 presentation lists "human-centric metaphors" as one of seven design goals, and its four features are these four. A goal is what makes a feature justifiable or refusable, so I did not leave the metaphors as a nicety of the documentation. They are one of the reasons the library has the shape it has.

**I replaced `eval` with a language the engine owns.** The condition seat used to be compiled by evaluating the string as code, with a faster extended form on the side for speed. I removed both. The engine now reads the condition in its own small language, and the library keeps the host-code form as a separate verb, WF, with its warning. I refused arbitrary code from text, and I refused to split speed from expressiveness: the extended form is retired because the plain one does everything it did.

**I kept the seven steps as written.** When the course was designed, a reading of the technical core found five steps: select, contains, count, find, apply. The course teaches the seven as the source narration has them. Nobody renumbers the source.

**I let the edge rule be a design principle.** Before the start is an error, and beyond the end is ignored. The narration gives its reason in a sentence: it mirrors how we walk. The record does not date it as a ruling, so I tell it as the library's design.

## 5. The court

The four metaphors have no single guard. The yielder has a narrated one, `00_yielder_narrated`: four map operations, three filter operations and a sum. The walker has `597_walker_basics`, named walkers and what they walked, and `495_walking_until_and_until_before`, a walk that stops on a condition, including the item that stops it, or not. The checker has `611_checkw`, which says a check is false when one item fails. The performer has `621_perform`, which says it changes the list in place. `483_w_and_wf_forms_in_conditional_code` proves that W with cursor words and with raw index arithmetic give the same positions.

## 6. The field, and where it leads

The field leads in laziness. A generator produces the next item on demand and can be endless. The walker builds a map of its whole journey the moment it is made. That is a win for foresight, you can ask which positions it will skip before it moves, and a loss for a very large or endless traversal.

The field leads in openness. A lambda carries any logic. The W language is bounded on purpose, and the price of the bound is the second path, WF, which has full host power and no safety against untrusted input. There is also a quieter cost I measured once, on one case: a mistyped condition and a condition that matches nothing look the same. Both give an empty list and no error.

The field leads in reach and in tooling. Iterators and comprehensions are in every mainstream language, with editor support, type checking and a literature. These four metaphors exist in one library.

And I will not print the library's own comparison of walkers with loops and iterators. Its table has thirteen rows, all of them in the walker's favour, none of them run. A table with no loss on it is the shape of a brochure.

## 7. The limit

What is built: the one-dimensional walker, in the max layer, and the walks on lists; the checker as `CheckW`, `ContainsW` and `FindW`; the yielder as a class backed by the engine, and as `YieldW`; the performer as `PerformW`; and the W condition language compiled by the engine.

What is designed: the metaphors as native engine modules. The engine's design marks the walker, the checker and the performer as planned; only the yielder has a file there. And a walker that is not about lists at all but about any indexed structure.

What is absent or broken at this commit, from my runs:

- The walking-at-the-edge article's table does not hold. A single step larger than the range raises where the table promises silence, and a mixed-direction path raises where it promises acceptance. The two principles hold in the cases shown above; the table is a draft. [AUTHOR: Is the principle the law, and the table a draft, so the book may state the principle and print only the cases that run?]
- The "Beyond Loops" article's code differs in places. The history of a walker is a list of walks; a backward walk takes no argument now; the direction prints as "backward" where the article says "reverse". The site's own run of the article kept ten of eighteen blocks.
- The founding article's three models: none of its code runs, twelve blocks raised in the site's run. So I told them in words.
- The mental-model article's dedicated verb for empty strings does not exist; the verb that does is `RemoveEmptyStrings`.
- The dedicated checker class raises when asked `ContainsW`, and the string walker lacks the backward-with-condition walk.
- And "no eval" has not reached everything. The near-natural resolver, the other direction of chapter 13, still evaluates host code.

## 8. Six doors

**The programmer.** Ask the same four questions of any object, and when you reach for a loop, name the move: walk, check, yield or perform.

**The analyst.** Say the problem in plain words, and the verbs you used are the steps: "are all of them", "which ones", "give me the big ones", "make them negative".

**The designer.** The yielder never changes the list and the performer does, and the verb tells you which.

**The decision-maker.** A W condition is a string the engine reads and cannot run as code, so it can be stored, shown and approved. The price is a small language and a mistake that stays quiet.

**The educator.** The self-study book already has the order: find, then apply, then walk, ask, produce and act.

**The agent.** Write the condition as the string, not as code. When the answer is empty, check the condition's words before you trust the emptiness.

## 9. Exercise

Take the list `[ 4, 9, 12, 7, 20, 3 ]`. Four sentences are given. One: are all of them above 2? Two: give me, as a new list, those above 8, doubled. Three: make the ones above 8 negative, in the list itself. Four: which positions are 2, 4 and 6?

For each, say first which move it is, walk, check, yield or perform, and write under the line you will write what you expect it to print. Then write the line, with the condition as a string wherever there is a condition, and run it. After the second and the third, print the list again. Say, before you look, in which of the two the list has changed.
