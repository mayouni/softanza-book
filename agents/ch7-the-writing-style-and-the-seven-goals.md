# The writing style, and the seven goals

Source: Chapter 7. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the library's fourteen house rules as a court over its own code; the promise judged as a claim; the small languages of ranges, lists and conditions in strings; the code seat; the viz prefix; alternatives and named parameters in any order, in part; designed: a court that judges the style of a program written with the library; a court that reads the goals; the writing grammar declared in Haro; the classic form of a test block as the one form; absent: any machine that judges the style of the code you write today; the writing in any human language of a function's name; the near-natural sentence as the deck wrote it; the eval-based code on a parameter's name

Run: 10 of 10 blocks kept their promise, on 2026-10-09 05:30 UTC+01:00.

## 1. The concept, as the field holds it

The word *style* means two things in the field, and I have to say which one I mean.

The first is style as layout, enforced by a tool. Python's style guide dates from 2001, Go's formatter from 2009, and every project runs a linter before a commit. They judge the shape of a line: spaces, capitals, length, unused names. They are very good at it, and they run by default. They say nothing about whether a line follows the order in which its writer reasoned.

The second is the small language inside the language. Programmers already write small languages in strings, and nobody calls that a style: a regular expression, a SQL text, a format string such as `"%5.2f"`. Each is a separate notation, with its own tool, learned apart.

For goals, the field says *quality attributes*. The ISO standard for software quality, of 2011, lists eight of them, and architecture methods rank them before a system is drawn. (General knowledge, not a study of the record.) The seven goals of this chapter are a different list, chosen for a different purpose. They do not say what a product promises its users. They say what a feature must serve to be admitted into one library.

## 2. The first principle

**What you think is what you write.** It is chapter 5's sentence, from the diagram of 2020, and I do not argue it again. Chapter 5 took five rules of the style. This chapter takes the rest, as a grammar, and then the goals under which the grammar was designed.

For the goals, the point is the author's, as the study reports it, and not a dated quotation: a software architecture that is truly goal-oriented is the only way one architect masters a project of this size.

## 3. The Softanza form

The study of the record wrote the style down as fourteen rules, in its ruling 12.16, from reading the code. They are readings of the code, stated as rules, and not a standard anyone signed. Here they are with the state each is in at the commit this book runs. I put the table first because it shows which rules carry a block and which carry a limit.

| # | Rule | State at this commit |
|---|---|---|
| 1 | A value is lifted to its object by `Q()` or a typed lifter | runs; chapter 5 |
| 2 | A scene is a brace block on one object | runs; chapter 5 |
| 3 | Every printed line carries its answer under `#-->` | judged by a machine; chapter 5 |
| 4 | A parameter is named, and the name reads as English | runs; chapter 5, and here in any order |
| 5 | A chain mirrors the order of thought, one step per line | runs; chapter 5 |
| 6 | The verb's form says what happens | runs; chapters 5 and 8 |
| 7 | Suffixes and prefixes are small and mean one thing each | in part: `CS`, `XT`, `viz` run; the deck's `FF`, `dft` and `inf` families raise |
| 8 | A function has alternatives for the way a person says it | in part |
| 9 | Precision over generality, when it costs nothing | in part |
| 10 | Code travels inside an argument as a small string | the seat runs; the `@` on a parameter's name is retired |
| 11 | Small literal languages live in strings | runs in one form; the braced form raises |
| 12 | A sentence can be near-natural | not this chapter's; none of the deck's three forms ran as written |
| 13 | A function may be named in any human language | does not run |
| 14 | A comment speaks before the code, in the teacher's voice | runs |

Rule 11 first, because it is the strangest. The host language counts in integers and cuts the decimals. Softanza reads a small range language inside a string, and keeps them. It counts numbered words and letters of any script. The comments below speak before the code, in the teacher's voice, which is rule 14:

```haro
# The host's own range counts in integers: the decimals are cut. Softanza reads
# a small language inside a string, and keeps the decimals, the numbered words,
# and the letters of any script:
? @@( 1.02 : 3.08 )
#--> [ 1, 2, 3 ]
? @@( L("1.02:1.05") )
#--> [ 1.02, 1.03, 1.04, 1.05 ]
? @@( L('"♥1" : "♥3"') )
#--> [ "♥1", "♥2", "♥3" ]
? @@( L(' "ا" : "ج" ') )
#--> [ "ا", "ب", "ة", "ت", "ث", "ج" ]
```

> run: kept

The range language is an argument like any other. It gives the replacements for each occurrence, in order, and the extended form wraps the palette when the occurrences outnumber it:

```haro
o1 = new stzString("haro php ruby haro python haro")
o1.ReplaceByMany("haro", L('"♥1" : "♥3"'))
? o1.Content()
#--> ♥1 php ruby ♥2 python ♥3
o2 = new stzString("haro php ruby haro python haro ruby haro")
o2.ReplaceByManyXT("haro", L('"♥1" : "♥3"'))
? o2.Content()
#--> ♥1 php ruby ♥2 python ♥3 ruby ♥1
```

> run: kept

A list can also be carried as a string in its short form, recognised, converted between forms and evaluated back:

```haro
? StzStringQ('1:3').IsListInString()
#--> TRUE
? @@( StzStringQ('[1,2,3]').ToListInShortForm() )
#--> "1 : 3"
? @@( StzStringQ(' "A":"C" ').ToList() )
#--> [ "A", "B", "C" ]
```

> run: kept

Rule 10: code travels inside an argument as a small string with a placeholder, `@char` for the characters of a string and `@item` for the items of a list. Chapter 6 showed the seat on a list. Here it is on a string, where it finds and removes by a rule and not by a loop:

```haro
o1 = new stzString("SOooooFTAaaannnNZA")
? @@( o1.FindW('{ Q(@char).IsUppercase() }') )
#--> [ 1, 2, 7, 8, 9, 16, 17, 18 ]
o1.RemoveW('{ Q(@char).IsLowercase() }')
? o1.Content()
#--> SOFTANZA
```

> run: kept

The deck of 2022 writes the same call with a named seat, `:Where = '...'`, and that form raises on a string in this commit. I do not show it. The same deck puts an `@` at the end of a parameter's name, `:With@`, to mark that its value is code to be evaluated. That form is retired. A guard's header says so: the eval-based forms are retired. The deck itself marks the form "TODO". Code now travels in the seat as a bounded string that the engine evaluates, or as a function.

Rule 8: the same act may be said in two orders of words, with the container's name, or with the side spelled four ways. Each pair is one method. The library's own narration calls the first with two arguments and it raises; the guards pass the starting position, and so does the block:

```haro
o1 = new stzList([ 1, 2, "♥", 4, 5, "♥", "♥" ])
? o1.FindNthNext(2, "♥", :StartingAt = 1)
#--> 6
? o1.FindNextNth(2, "♥", :StartingAt = 1)
#--> 6
? Q("---haro").NumberOfOccurrenceOfCharLeftSide("-")
#--> 3
? Q("---haro").HowManyOccurrenceOfCharStartSide("-")
#--> 3
o2 = new stzList([ "C", "B", "A" ])
o2.SwapItems(:AtPositions = 1, :And = 3)
? @@( o2.Content() )
#--> [ "A", "B", "C" ]
```

> run: kept

The deck promised more. A family of five names for removing characters at the two ends, `LeadingAndTrailingCharsRemoved` among them, is not defined. Only `LeadingCharsRemoved`, `TrailingCharsRemoved` and `RemoveLeadingAndTrailingChars` are.

Rule 9: precision over generality. The precise name says what is counted. A string's characters are counted by `NumberOfChars`, and `Size()` is the host's byte length, so the two answers differ on an Arabic word:

```haro
? Q("سلام").NumberOfChars()
#--> 4
? Q("سلام").NumberOfBytes()
#--> 8
? Q("سلام").Size()
#--> 8
o1 = new stzList([ "tea", "rice", "fish", "salt" ])
? o1.ContainsBoth("tea", "fish")
#--> TRUE
? o1.ContainsAll([ "tea", "oil" ])
#--> FALSE
```

> run: kept

The library's own documentation line for `NumberOfChars` lists *size* among its alternative words. The run shows that `Size()` does not mean it. I list it among the requests.

Rule 7: a prefix `viz` shows the answer under the word, and the suffix `XT` adds the positions as numbers:

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

The narration and the deck write `vizFindAll`. It does not exist at this commit, and `vizFind` does.

### The goals

Under the grammar there are seven goals, written in the 2022 deck as a matrix of thirty-three features. The study's ruling 12.14 reads them as the library's architectural skeleton: a feature that serves none is refused, and a goal with no feature is a gap. The study's headline is a session's, and no document in the library states the rule in these words. The nearest is the engine's design document: the engine must enable all seven.

I will not list the seven as a table of slogans. Here is what runs of three of them.

**Flexibility: the order of named parameters is free.** Two calls, with the parameters in two orders, are the same call:

```haro
o1 = new stzString("----@@--@@-------@@----@@---")
o1.ReplaceNextNthOccurrence(2, :Of = "@@", :StartingAt = 12, :With = "##")
? o1.Content()
#--> ----@@--@@-------@@----##---
o2 = new stzString("----@@--@@-------@@----@@---")
o2.ReplaceNextNthOccurrence(2, :With = "##", :StartingAt = 12, :Of = "@@")
? o2.Content()
#--> ----@@--@@-------@@----##---
```

> run: kept

A tension must be told with it. The design of Haro refuses free-order parameters as grammar, and the library ships them. What is true today is two facts. The library ships free-order parameters, and the block above runs them; it also ships alternatives under any wording. The grammar a machine is held to leaves them out, by the Haro principle. Whether the library keeps them past that grammar or retires them is a decision the record does not hold, and I do not make it here: they are shipped, and they are not grammar.

**Consistency: one vocabulary across a string and a list.** The same verb answers on both:

```haro
? @@( StzStringQ("hello").FindAllCS("L", :CaseSensitive = 0) )
#--> [ 3, 4 ]
? @@( StzListOfStringsQ([ "h", "e", "l", "l", "o" ]).FindAllCS("L", :CaseSensitive = 0) )
#--> [ 3, 4 ]
? Q("").IsEmpty()
#--> TRUE
? Q([]).IsEmpty()
#--> TRUE
```

> run: kept

The loss beside it, from the same slide group: the deck's "item for any enumerable" does not hold. `NumberOfItems()` on a string raises, and on a list it answers.

**Manageability: a failure that says where, what, why, and what to do.** The library raises an error in four fields. I do not print its message, because its first line carries a line number of the library, and a line number is not a promise.

The other four goals (reliability, expressiveness, universality and the one the deck calls extensibility) I leave to the tables of the study. I have not run them for this chapter, and I will not describe from the deck what I have not run.

## 4. The decision, and what I refused

**I refused a style that was changed when AI became the main writing tool.** The study reports the author's disappointment in these terms, and chapter 5 tells it. The implementation code that the AI wrote is accepted as good. What is demanded is that every line a programmer, human or agent, is asked to write with Softanza embraces the historic style.

**I refused a goal that lives only in a document.** The seven goals are written in one design document and in tags that no court reads. The study's finding is that there is no court over either.

**I refused to hide the cost of the style.** The study measured markers per thousand lines. The narrated guards, the test files written to be read as articles, carry the promise `#-->` in under one line per thousand, and a call to the assertion helper in eighty-five. The older numbered tests carry the promise in fifty-two. The library's code carries the promise in less than two. The style survived where the author wrote for a reader, and thinned where the AI wrote for others. A marker is a reading of the text, not a judgement of the code; the study says so itself.

**I refused to recount the tags as mine.** The goals are marked in the code by info-tags, in comments that begin with `#<` and an `@`, applied by hand. The study counted about six thousand. I counted again on 8 October 2026, with the command in the research file, and found 6,126, with 89 spellings. But 1,360 of them sit outside the archive folders, and 4,766 sit in the archived monolithic files. So the sentence "applied by hand at six thousand points" is, at this commit, mostly a sentence about the archive. No guard reads them: the reflection layer reads a method's name, with a grammar, and not its tag.

**I refused the tally as a count of passes.** The study counts thirty-three features: twenty-four built, four transformed with the project, two that changed form, one partial, one archived, one a name only. The arithmetic holds. But it is a count of names found, and a definition found is not a passing test. Several of the features have names in the code and raise when called: the families `FF` and `FX` for sections, the families `dft` and `inf` for defaults and infinities, `WalkFF` and `AddWalkerFF`, the `Check` on a list, and the deck's `Yield` and `Perform` forms. I print the tally, and I print its losses with it. The deck also says "7 root causes of programming complexity", beside the seven goals. No slide lists those seven causes, and no other file in the record names them, so the chapter names none and does not match them to the goals one by one.

## 5. The court

`coderule_narrated` proves that a house rule is a rule over the code graph; that planted code is found by name; that clean code passes; and that the library lists fourteen. `testoor_promises_narrated` proves that the promise `#-->` is judged as a claim of a stop: kept, diverged, unreached or unjudged. `602_l_function` and `59_use_of_the_l_small_function` prove the range language, in Arabic too. `527_identifying_lists_inside_a_string` proves the lists hosted in strings. `48_replacebymany` proves that the palette cycles. `483_w_and_wf_forms_in_conditional_code` proves the condition in a string and in a function. `28_numberofoccurrenceofcharleftside` proves the alternative names in Arabic as well as Latin, and carries a note that the archive's promise was wrong and the implementation is the authority. `646_content` proves the named parameters. `972_narration_viz-finding_a_recurring_substring` proves the viz tour.

Here is the house court itself, the fourteen rules of the library and not the fourteen of the style. The numerical coincidence is a coincidence. A planted misspelling is found by name and the code stays clean, because it is a warning. A planted write to a constant is found by name, and the code is refused, because it is an error:

```haro
? @@( StzCodeRuleNames() )
#--> [ "no-len-method", "q-returns-object", "no-aggressive-verbs", "engine-first", "q-has-plain-twin", "no-case-collision", "dead-knob", "setter-resets-on-reject", "setter-only-moves-one-way", "misspelled-name", "library-prints", "empty-method-body", "writes-a-mutable-constant", "value-called-as-function" ]
cOne = "class Inbox" + nl + "def Recieve(x)" + nl + "	return x" + nl
? StzCheckCode(cOne)[1][:rule]
#--> misspelled_name
? StzCodeIsClean(cOne)
#--> TRUE
cTwo = "class Inbox" + nl + "def Count()" + nl + "	nl = 3" + nl + "	return nl" + nl
? StzCheckCode(cTwo)[1][:rule]
#--> writes_a_mutable_constant
? StzCodeIsClean(cTwo)
#--> FALSE
```

> run: kept

A detail of the spelling, for Appendix B: the names list uses hyphens, and the finding of eight of the fourteen comes back with underscores. The block shows what the run printed.

What the court does not read is the code of a program written with the library. None of the fourteen rules of the house is a rule of writing.

## 6. The field, and where it leads

The field leads in enforcement by default. A formatter runs on every commit. For the code a programmer writes with Softanza, the enforcement today is none, and chapter 5 says so.

The field leads in having its goals somewhere a reader looks first. The seven goals are in one design document and in tags that no court reads, and the operating notes of the library's own repository name none of them. An AI reader's account of the library says that sixty paradigm documents could easily be sixty disconnected ideas. The study reads it as a sign that the discipline is in the code and written nowhere a reader would look first. It is a session's document, and not an independent witness.

The site once showed a reduced dialect: its blocks had no named parameter and no scene. It has since put the fourteen rules on its Craft page and the rules as data. I did not re-measure the site's blocks after that.

Where I think the style stands apart is that every rule serves a step of thought, and every step has a written form (study 12.17). The verb's form is a contract on the object. And the promise under the line is the example, the test and the documentation at once. The 2022 matrix served as a skeleton for one architect over about three hundred thousand hand-written lines.

## 7. The limit

What is built: the fourteen house rules of the library as a court over its own code, run in the block above; the promise judged by a machine; the small languages, the seat, the prefix. And the features that run (`CS`, `XT`, `ZZ`, `viz`, named parameters, the same verb on a string and a list).

What is designed:

- **A court that judges the style of a program written with the library.** It is a specification in the study: the fourteen rules as house rules over a snippet's graph, such as a positional argument where a named one exists, or a printed line with no promise. I searched the library for it and found nothing.
- **A court that reads the goals.** It would harvest the tags. Not built.
- **The classic form of the test block as the one form for new blocks.** The study's ruling is that the revival "is not a rewrite" but a decision that the classic form is the one form for new blocks, with the converted blocks left as they are. The test tree's own README still calls the classic form the authoritative test surface. I found no ruling that makes it the one form, so it stays a decision, and chapter 5 names it.
- **The writing grammar declared in Haro.** The vocabulary half exists: the forms of the library's names are data in Haro, and the session's record is 584 of 595 shipped spellings agreeing. The usage half, the scene, the chain, the code seat and the promise, is not declared.
- **The discipline declared once.** Partly done on the site, as data, which is the page's source and not a court.

What is absent:

- Any machine that judges, today, the style of a program written with the library.
- Rules 12 and 13 as running forms. The deck's near-natural samples did not run as written, and neither did a function named in Chinese or in French.
- The `@` on a parameter's name as a working form.
- The braced form of the range language, `L('{ "♥1" : "♥6" }')`, which raises, and ranges that change width, such as `day8 : day11`, which also raise, with an uninitialised-variable error from the host. The list constructor from a string raises too.
- The visualised call stack, and the cache and log decorators, which exist as names in comments.

## 8. Six doors

**The programmer.** Fourteen rules you can hold your own line against. Lift the value, ask in a scene, put the answer under `#-->`, name the parameter, chain one step per line, read the verb's form; and put a range, a condition or a palette in a string.

**The analyst.** The words of your problem become the names of the steps. A rule written in a string is a rule you can store and read, and not code you must trust.

**The designer.** The viz prefix draws the answer where the eye expects it. The goals are the headings under which a design is judged, one feature at a time.

**The decision-maker.** Seven goals and thirty-three features are a reading grid. A feature that serves none is refused, and a goal with no feature is a gap. The tally is printed with its losses.

**The educator.** The discipline is taught whole and in order. The converted guard for lists in strings keeps the old promise's wrong spacing in a comment, which is a lesson on the cost of hand-typed answers.

**The agent.** The rules are given to you as data on the site. For the code you write, the court is still a specification. Write the question, then the promise under it, and put your condition in the seat, not in an evaluation of a string.

## 9. Exercise

Write, before you run anything, the line each task needs and the promise under it:

1. From one string, the list `[ "♥7", "♥8", "♥9" ]`.
2. The string `"haro php haro"` with the two `haro` numbered `♥1` and `♥2`, in one call that uses the small language of task 1.
3. The list `[ "C", "B", "A" ]` ordered by swapping the first and the third items, with the positions named.
4. The count of characters of `"سلام"`, with the name that says what is counted.
5. A guess: what does `L("day8 : day11")` print?

```haro exercise
# 1.
# 2.
# 3.
# 4.
# 5.
```

> run: exercise

Run it. For the fifth, you were allowed to be wrong, and you were probably wrong: the range changes width, so the host reads `day8` as a variable, and it raises. That is the limit of the small language, learned by being surprised once. Do not change your promise to match the output. Explain the output first.
