# The method, from first principles

Source: Chapter 3. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the court behind every block of this chapter but the truth one, and the stage words the site prints on every product; designed: the register of rethought concepts as data, with a guard that fails when a concept has no proof; absent: a page that shows each rethought concept with a run proof; a test file for the paradigm engine of section merging

Run: 5 of 5 blocks kept their promise, on 2026-10-09 13:44 UTC+01:00.

## 1. The concept, as the field holds it

In our industry, "from first principles" is a slogan. It means: reason from the bottom, not by analogy. You will hear it in talks and read it in launch posts, and you will rarely be shown what it produced.

The field does have a method for the decisions behind software, and it is a good one. A team writes a short record for each decision it takes: the context, the decision, the consequences. Many teams call these architecture decision records, from a blog post Michael Nygard wrote in 2011. The field also has a method for proving what a function does: an example written under the function, which the tools can run as a test. Python has offered this since 2001 with its doctest module, which runs when someone invokes it, and Rust runs the examples in its documentation as tests by default. And when the field compares one tool with another, it draws a grid: rows of features, one column per tool, ticks and crosses.

## 2. The first principle

Here is the sentence the whole method returns to: **you declare a world in a language made for it, and you govern how that world changes.**

Two acts. Everything else in this book is one of them, or the two together.

## 3. The Softanza form

"From first principles" can be checked. In this book it has a narrow meaning: take a concept everyone uses, write down how the field holds it, redesign it, and leave code that carries the redesign and a court that judges it. The site's history page is titled *From first principles*, and the library has been on GitHub since 12 March 2022. The phrase is not decoration here. It is a work order.

Let me show you the smallest rethink I know. Ask Python how many times the empty string occurs in the word "text", and it answers five: one before each letter and one at the end. Ask it whether "text" contains the empty string, and it says yes; JavaScript says the same. (Python 3.13 and Node 22, run on 8 October 2026.) That is a convention of implementers, not a fact anyone would say aloud. Softanza states a rule instead, and the rule has a name in the narration that argues it: emptiness is uncountable, and emptiness is uncontainable.

```haro
? Q("text").Count("")
#--> 0
? Q("text").Contains("")
#--> FALSE
```

> run: kept

Two lines, and a decision you can disagree with. That is what a rethink looks like when it is honest: small enough to read, explicit enough to refuse.

A reading of the record, made in October 2026, counted forty-six such concepts, in seven families: the paradigms, such as scope-oriented programming, knowledge programming and reactive programming redesigned; the paradigm engines, such as truth, quantifiers and time; patterns and reaction; expression and perception; data, time and reasoning; system, delivery and operations; and the library that knows itself. Forty-six is a reading and not a census; the site's own register page, read on 9 October 2026, says forty-seven. Each concept on it has an article or a design document of its own, and that was the test for entering the list.

Now the two acts, each in a few lines.

**Declare.** A kind of value is declared in a sentence, and every verdict against it is computed and explains itself:

```haro
ConstrainQ("score").ToBeQ(:Number).AndQ().ToBeQ(:Positive).AndQ().ToBeQ(:Even)
? CanQ(42).BeA("score")
#--> TRUE
? CanQ(-4).BeA("score")
#--> FALSE
? Why()
#--> no: -4 is not positive (constraint 2 of 'score')
```

> run: kept

Notice the last line. The verdict names the rule it applied, by its number. A verdict on a declared kind that cannot say why is not admitted in this house.

**Govern.** A declared constraint, once enforced, refuses a change before it lands:

```haro
oName = new stzString("hello")
oName.EnforceConstraint("keep-lowercase", :Lowercase)
bRefused = FALSE
try
	oName.UpdateWith("HELLO")
catch
	bRefused = TRUE
done
? bRefused
#--> TRUE
? oName.Content()
#--> hello
```

> run: kept

The update was refused, and the object stands as it was. The error the library raises says what was tried, why it was refused and what to do: fix the new value, or relax the constraint. Declaring a constraint and enforcing it are two acts, and the guard behind this block checks that a constraint you only declared stays passive.

Governing also has a side that faces the person. The system asks, and it does not let you close a world that is not complete:

```haro
oKB = new stzKnowledgeGraph("restaurant")
oKB.Know("margherita", "dish").Know("tiramisu", "dish")
oKB.AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
aQ = oKB.AskInXT("setup")
? aQ[:why]
#--> every dish needs 'contains'
try
	oKB.ConcludeIn("setup", "world")
catch
	? cCatchError
done
#--> Can't conclude: 2 gap(s) remain -- the wise-coding loop is not done. Ask the next question.
```

> run: kept

The goal was declared: every dish must say what it contains. The gap between the goal and what is known generates the question, and the question carries its reason. Concluding while two gaps remain is refused, and the refusal tells you what to do next. Chapter 18 is about this conversation. Here it is enough to see that governing is not only refusing; it is asking.

One more rethink, because the paradigm engines are part of the method too. Truth, in the language beneath Softanza, is a matter of empty and non-empty, and a list of words counts as true. Softanza keeps that truth by default and lets you extend it by declaration:

```haro
SetItemsMakingAListFalse([ "false", "wrong", "dangerous" ])
? IsTrue([ "hello", "this", "is", "wrong" ])
#--> TRUE
? IsTrueXT([ "hello", "this", "is", "wrong" ])
#--> FALSE
```

> run: kept

The host's answer is unchanged. The extended answer reads your declaration. "Truth becomes a matter of policy", the narration says, and the policy is written where you can read it.

So this is the method, in the form you will meet in every chapter after this one. A concept as the field holds it. The one principle the record returns to. The redesign, in running code, with its promise under each block. The decision, and what was refused. The court that proves it, by name. The field, and where it leads. The limit, in three stage words: **built** means the code exists, a guard exists, and a block ran; **designed** covers what the site calls in construction, specification and ratified proposal; **absent** covers a name with nothing behind it yet, and what nobody has named. Then six doors, one for each kind of reader, and one exercise.

And the book is judged the way the library is. Every block in it ran inside the library on the night the page was built, at the commit printed at the top of the page, and a page whose promises are not kept does not build.

## 4. The decision, and what I refused

There is no single record of a decision called "the method". The method was decided in pieces, and the pieces are in the record.

**I refused to add a feature without a need.** I wrote it in an article of the library, which carries no date: "I introduce new features only when they solve a tangible problem or when I anticipate they'll meet developers' needs." First principles without that rule produce a museum. With it, a rethink has to earn its place: someone had a problem the field's form did not answer.

**I refused general-purpose code as the meeting ground between people and machines.** The vision of the platform says it in one line, which I ratified: humans and AIs meet in declared languages, small, closed and judged, and not in general-purpose code. Declaring is the first act because it makes the second possible. A court can only judge a sentence of a language it knows.

**I refused a title that looked back.** When this book was first proposed, its title was *Programming by Heart*, the slogan of the 2020 presentation. I turned it down as outdated: it named a stance, and the book had to name what was rethought. The next proposal was *Declare, Then Govern*. I kept the site's own sentence for the cover instead (on 8 October 2026 I changed one word of it, for *crafters*), and the two verbs moved to the back cover, where you will find them. They organise every chapter; they did not need to be its name.

**I refused the grid alone.** The library's documents hold dozens of comparison grids, and in them Softanza's column wins almost every row. A reader who sees only those grids is right to discount them. The honesty in the record is elsewhere: in the sections of the field studies titled "what the field has that Softanza lacks, honestly", and in measured numbers. When the runtime beneath Softanza was measured again in September 2026 against the one it was compared with, the earlier headline did not reproduce, and the loss was recorded the same day, in an internal memo. That is the rule this book follows: a loss is printed beside the win, in the same section.

**I refused to call a reading a census.** The forty-six concepts are a reading of the record by one session, not a list I ruled row by row. Appendix A prints the register of forty-six rows as the study gives it, with the book's own column, as a working appendix: the rows are not ruled one by one.

## 5. The court

The three blocks of the two acts stand on two guards. `modality_narrated` proves that a declared kind can be inspected, that a verdict names the constraint that failed, that an unknown kind never silently allows, and that an enforced constraint refuses a bad update before it lands while a declared one stays passive. `wisecoding_narrated` proves the conversation: gaps computed from the declared goal, a question that says why it is asked, answers admitted, a law refusing through the conversation and reaching a person, and concluding with open gaps refused. Its sister, `wisecoding_rich_narrated`, carries the richer cases of the same loop.

The rethink of emptiness stands on `612_dealing_in_emptiness_in_softanza.ring`, a library test written as scenarios, each line stating the result it expects. The rethink of truth stands on its narration and on this book's run, and on no guard: the library's file for it, `04_truth_in_softanza.ring`, sets the list of false words by assignment and never calls the function, so it does not prove the block.

## 6. The field, and where it leads

The field leads in adoption. Decision records are a light standard that many teams use, with templates and tools around them; the decision element of this book exists in this book and in one study of the record, and not yet as data in the library. Examples in documentation can be run by the standard tool of Python, and Rust runs them by default; the promises of Softanza are judged by the house's own runners, which no outside tool reads. And the field's habit of comparing by grid is no worse than the record's, which shows the same weakness on its own pages.

Where I think Softanza stands apart is in one place only: the rethink is carried all the way down. The decision is written, the redesign runs, the promise is judged at build, and the stage word says how far each piece has gone. A decision record does not run. An example does not say what was refused. Here they are one object.

## 7. The limit

What is built: the court behind every block of this chapter but the truth one, and the five stage words the site prints on each product.

What is designed: the register of rethought concepts as data, one row per concept with its article, its code, its guard and its stage, and a guard that fails when a new concept arrives without a row. It is a specification today.

What is absent: a page that shows each concept with a run proof (the site has a register page, read on 9 October 2026, that lists each with its evidence); a test file for the engine module of one paradigm engine, section merging, which has none of its own, though its merge methods run in `base/test/string/289_content.ring` and `max/test/stzListOfPairsTest.ring`; and a few rethinks that do not run as their article wrote them. The article on quantifiers asks whether all your marks `AreGreaterThan` the average, and that method is spelled differently in the library today; its friendlier quantifiers, some, most and few, draw at random, so they cannot carry a promise. The register is a reading, and a reading can miss a concept that lives in only one article.

## 8. Six doors

**The programmer.** Every claim you make can carry its promise, and an enforced constraint refuses a bad update at the object's update point (`Update()` for a string or a number, `_SetContent()` for a list).

**The analyst.** Your rule is a declaration, and its verdict names the rule that failed, by number.

**The designer.** The stage word is part of the interface. A product that does not exist yet says so, in a word you can check.

**The decision-maker.** Ask every vendor for the loss beside the win. Chapter 1 prints one, with its date: the runtime beneath Softanza trails the one it was compared with by 1.04 to 1.88 times, measured on 13 September 2026.

**The educator.** Each rethink has an article that argues it: the concept, the field's form, the redesign. That is a curriculum, ordered by family.

**The agent.** You learn this platform from the platform, and you are corrected by it. A verdict that says why is written for you as much as for a person.

## 9. Exercise

Choose one default of your own language that you never questioned: what the empty string counts to, what counts as true, what "most" means. Before you run anything, write in one sentence the rule you think is right. Then write two promises in the form you have met: the line your language prints today, and the line your rule must print.

```haro exercise
? YourDefault(the_input)
#--> what your language prints today
? YourRule(the_input)
#--> what your declared rule must print
```

> run: exercise

Run both. I will not tell you which rule is right. If your rule and your language disagree, you have found a decision that someone took for you, and you can now take it yourself.
