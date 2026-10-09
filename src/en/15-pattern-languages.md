---
id: pattern-languages
part: 3
number: 15
title: Pattern languages
spine: false
narrations: [stznumbrex-pattern-language-for-number.md, stztablex-pattern-langauge-for-tables.md.md, stzlistex-pattern-matching-for-lists.md, stzTimex-A-Pattern-Language-for-Time-in-Softanza.md, stzMatrex-Declarative-Pattern-Matching-for-Matrices.md]
site: [languages]
guards: [00_regex_narrated, 00_numbrex_narrated, tablex_narrated, 00_matrex_narrated, 00_graphex_narrated]
stage:
  built: "patterns for text, numbers and tables, each with a guard; the same small habit across the media (a constructor, a pattern in a string, Match, Tokens)"
  designed: "one pattern engine shared by every medium; the pattern as the condition side of the cascade; the pattern written from examples"
  absent: "the refusal of a word the pattern language does not know, in all six media; sequences over a timeline in time; a narration and a small function for graphs; the genetic, linguistic and quantic siblings"
status: draft
rulings: ["12.4", "12.18", "12.26"]
research: research/ch15.md
---

## 1. The concept, as the field holds it

For a working programmer, a pattern is a regular expression: a compact notation for the shape of a string, handed to an engine that says whether the text fits, and where. The engines are old and well known. The one beneath this library is PCRE2, and the site measures it against two others.

For data that is not text, the field uses other tools, one per medium and none shared. Structural pattern matching in the languages of the ML family, in Rust, and since Python 3.10 in Python. Schema checks for lists and records. Data-quality libraries for tables. Row pattern recognition in SQL, and stream engines, for sequences over time. And graph query languages, whose core is a path pattern. (General knowledge, well established; the record holds no dated study of any of them, and I invent none.)

The estate's own field study of August 2026 gives the small languages that survived a profile: a closed grammar, one domain question, plain text, a tiny surface, a specification with a conformance suite, decades of stability. A pattern language is exactly that. One question, does this data fit, in a few characters. What the field does not offer is the same notation across the media.

## 2. The first principle

**A pattern is a rule about the shape of data, written as data. The same habit serves every kind of data.**

The sentence the library's articles return to, in each medium, is the one in the article on numbers: instead of instructing the machine how to test a condition, you state what you mean. The study of the record, which is not the field study above, also carries a phrase it calls the author's, "for the first time in computer science history". I found it in no text of the library, and the study does not let the site claim it; the chapter prints it as the study's attribution and claims no more than the study allows. The claim the study allows is the measured one: one regex-shaped grammar across seven kinds of data in one library, with the same small-function habit. And I will show you at once that the grammar is not quite one.

## 3. The Softanza form

A pattern called by name is a closed catalogue. The library has a data file of named patterns, and asking for a name it does not hold is refused:

```haro
? rx(pat(:isoDate)).Match("2023-12-25")
#--> 1
? rx(pat(:isoDate)).Match("25/12/2023")
#--> 0
? rx(pat(:isoDate)).Explain()
#--> Matches ISO 8601 date format (YYYY-MM-DD)
try
	pat(:banana)
catch
	? cCatchError
done
#--> The pattern name you provided does not exist in stzRegexData file.
```

A pattern can also answer the half-written value, which is what a form wants as the person types:

```haro
o1 = new stzRegex("^\d{3}-\d{2}-\d{4}$")
? o1.MatchAsYouType("123-45")
#--> 1
? o1.MatchAsYouType("abc")
#--> 0
? o1.IsPartialMatch("123-45")
#--> 1
? o1.IsPartialMatch("123-45-6789")
#--> 0
```

Now the move that gives the chapter its title. Take a list. Its pattern is written in square brackets, and counts, nesting and negation are written, not looped. `@N` stands for a number, `@S` for a string, `+` for one or more, `@N1-3` for one to three, and `@!` for not:

```haro
? Lx("[@N+, @S]").Match([1, 2, 3, "end"])
#--> 1
? Lx("[@N1-3, @S]").Match([1, 2, 3, 4, "end"])
#--> 0
? Lx("[@S, [@N+]]").Match(["tea", [1, 2, 3]])
#--> 1
? Lx("[@S, [@N+]]").Match(["tea", ["x"]])
#--> 0
? Lx("[@!N, @N]").Match(["a", 1])
#--> 1
? Lx("[@!N, @N]").Match([1, 1])
#--> 0
```

Every call here uses a fresh object, for a reason that section 7 gives. Chapter 11 showed four calls of the same language, and I do not repeat them.

The numbers have properties, and a property is meaning, not procedure. The last line turns a pattern from a test into a search:

```haro
? Nx("{@Property(Even) & @Property(Prime)}").Match(2)
#--> 1
? Nx("{@Property(Even) & @Property(Prime)}").Match(4)
#--> 0
? Nx("{@Digit(:unique)+}").Match(1234)
#--> 1
? Nx("{@Digit(:unique)+}").Match(1223)
#--> 0
? Nx("{@Relation(Mod:5=0)}").Match(10)
#--> 1
? @@( Nx("{@Property(Perfect)}").MatchingNumbersBetween(1, 500) )
#--> [ 6, 28, 496 ]
```

Tables: a data-quality rule is a sentence of the language. The person who owns the data can read it. Niamey appears twice, so the cities are not unique, and the negation of that is true:

```haro
oT = new stzTable([
	[ :ID, :NAME, :AGE, :CITY ],
	[ 1, "Ali", 28, "Niamey" ],
	[ 2, "Sara", 32, "Paris" ],
	[ 3, "Omar", 41, "Niamey" ],
	[ 4, "Awa", 25, "Dakar" ]
])
? Tbx("{cols(4) & unique(id) & avgcol(age:>30)}").Match(oT)
#--> 1
? Tbx("{cols(4) & unique(city)}").Match(oT)
#--> 0
? Tbx("{@!unique(city)}").Match(oT)
#--> 1
? Tbx("{sorted(id) & numeric(age) & alphabetic(name)}").Match(oT)
#--> 1
```

A pattern is data, so patterns compose: one is built from patterns.

```haro
oA = new stzTablex("{cols(4)}")
oB = new stzTablex("{rows(4)}")
oAnd = oA.And_(oB)
? oAnd.Pattern()
#--> {cols(4) & rows(4)}
? oAnd.Match(oT)
#--> 1
? oA.Not_().Pattern()
#--> {@!cols(4)}
? oA.Not_().Match(oT)
#--> 0
```

A matrix: a concept, square and symmetric, is one line.

```haro
? Mx("{shape(square) & property(symmetric)}").Match([ [1,2,3], [2,4,5], [3,5,6] ])
#--> 1
? Mx("{shape(square) & property(symmetric)}").Match([ [1,2,3], [4,5,6], [7,8,9] ])
#--> 0
? Mx("{size(2x3)}").Match([ [1,2,3], [4,5,6] ])
#--> 1
? Mx("{property(identity)}").Match([ [1,0], [0,1] ])
#--> 1
```

Time, in the part of it that runs. A duration must fit a rule: ninety minutes is inside one to two hours and on a step of a quarter of an hour; eighty is inside and off the step; three hours is outside.

```haro
oTm = new stzTimex("{@Duration(1h..2h:15min)}")
? oTm.Match(new stzDuration("1 hour 30 minutes"))
#--> 1
? oTm.Match(new stzDuration("1 hour 20 minutes"))
#--> 0
? oTm.Match(new stzDuration("3 hours"))
#--> 0
```

A graph: a pattern reads like the path it looks for. The labels match without regard to case, and direction matters, as the second line shows:

```haro
g = new stzGraph("Order")
g.AddNodeXT(:a, "Placed")
g.AddNodeXT(:b, "Cooking")
g.AddNodeXT(:c, "Served")
g.AddEdgeXT(:a, :b, "starts")
g.AddEdgeXT(:b, :c, "finishes")
? (new stzGraphex("{@Node(placed) -> @Edge(starts) -> @Node(cooking)}", g)).Match(g)
#--> 1
? (new stzGraphex("{@Node(served) -> @Node(placed)}", g)).Match(g)
#--> 0
? (new stzGraphex("{@Node(placed) -> @!Node(refunded)}", g)).Match(g)
#--> 1
```

Last, the habit. The pattern is data in every language, and a language that exposes its tokens can be read back by a person and by an agent. Five of the six languages do:

```haro
? len( Lx("[@N, @S]").Tokens() )
#--> 2
? Lx("[@N, @S]").Tokens()[2][:type]
#--> string
? Nx("{@Property(Even) & @Property(Prime)}").Tokens()[1][:type]
#--> conjunction
? len( Mx("{shape(square) & property(symmetric)}").Tokens()[1][:conditions] )
#--> 2
```

Graphs have no `Tokens`, no `Pattern` and no working `Explain` at this commit, and no small function either. There is no `Gx`, and there is no `Tx` for time, although the study's table names both. The small functions are `rx`, `Lx`, `Nx`, `Tbx`, `Mx` and `Tmx`.

## 4. The decision, and what I refused

**I decided that a pattern states a meaning and not a procedure.** That decision is in the articles, and the articles are mine. The same ones decided to carry the regex idea to non-text data with one habit: braces, an `@` for a token, `&`, `|`, `@!` for not, `@cs:` for case. Lists keep square brackets. The other five use braces. That is the first honest correction of the phrase "one grammar".

**I refused to reinvent the notation for text.** Simple matches are kept: a classic pattern string, named groups and captures work as written. Clearer names are put around it. The older work on naming is kept as history, for educational value, which is the right way to retire a mechanism.

**I refused, for now, to build the siblings.** The articles planned classes in which patterns are genetic, linguistic or quantic. The article says that they are in an early prototype and not in the library, and a search of the regex folder for "induce", "from example" and "infer" finds nothing. The study dates the finding of their purpose two years later, in the answer protocol (the way a person may answer by examples): induction from examples, and superposed candidates. That is chapter 18's ground, and chapter 9's refusal.

**I refused the declarative builder as a headline.** The builders are the classes that write a regex from named steps in code, not from a string. Eighteen of the fifty-one files in the builder's test folder are marked retired: the parser of a declarative pattern is pending. The article's lead example, `CanContainAChar(:Between = ...)`, raises. What runs is the conditional builder, and the look-around object. I do not build the chapter on the builder's headline form.

**I have not yet refused a word the language does not know.** That is the tension of this chapter, and I keep it for section 7.

## 5. The court

`00_regex_narrated` proves the anchors and the search, the classes, the exact quantifiers, the groups, the four match types, partial matching as you type, and positions as data. `00_numbrex_narrated` proves prime, perfect, Fibonacci, even and odd, square and composite, each with a number that matches and one that does not; its header records a regression in which `Match()` once returned TRUE for every input. `tablex_narrated` proves the parser, counting, uniqueness, sorting, types, sums and averages, the three connectives, sequences, and building patterns from patterns. Its header names the fault it killed: the parser sliced with an end position through a function that counts, and about ninety patterns parsed into a token of the right type with no value. `00_matrex_narrated` proves exact size, any size and the square shape; its header records that `Match()` once returned FALSE for every input. `00_graphex_narrated` proves that a pattern compiles to a graph, present and absent labels, a sequence as a subsequence, the case rules, negation, alternation, numeric properties, and the cache by graph signature.

Note the placement: the guard for tables lives in the folder for regex, and its stem has no `00_` prefix.

There is no narrated guard for lists, time, or the regex builders. The courts of those are classic files without usable promises. The tests of lists sit after a function definition, so the host language reads them as the body of the function and runs none of them. I ran a copy with the function moved to the end, and I note it in my research notes, not in a block: sixty checks ran, and two of them disagree with the file's own expectation. The classic file of time says that a promise is TRUE and the run prints 0, and the central record filed this on 1 October 2026 as still open.

## 6. The field, and where it leads

**Strings.** The field leads on safety and speed, and Softanza leads on naming. The site's page for the area says it itself: it trails the modern engines on safety and throughput, with no JIT and no linear-time matcher, and the control against catastrophic backtracking is not reachable from Haro, although the code for both is already compiled into the binary. The engine's header confirms that the hardening exists underneath: a match limit, a recursion limit, length caps.

**Lists, numbers, time, graphs.** The field has older, stronger single tools. The study says it without ranking them: one tool has list patterns, uniqueness and stepped ranges; three languages have structural matching; graph query languages exist; event processing exists for time. What the field lacks, and what the record claims, is the one habit across the media.

**Tables.** Data-quality libraries lead in reach and ecosystem. Here a rule is a sentence the person who owns the data can read. The loss is that it runs only on `stzTable`.

**Where the family is weak in itself.** The class headers print their defects as warnings: for matrices and graphs. That is rare, and I say it. Graphs: the quantifiers are parsed but not yet used by the match. Matrices: known gaps today, each carried as a warning on its method.

**A date for the family's one recurring bug.** The same root cause hit the family language by language: the parsers sliced with an end position through a function that counts. The numbers and matrices were repaired on 14 June 2026, the tables on 5 October, and the graphs in a fix whose date the file does not give. Time still carries it. This is evidence that the family shares one design and one parser's habits; it is also a likely reason time fails.

## 7. The limit

What is built: strings, numbers and tables, each with a guard and a small function. The shared habit.

What is built in part:

- **Lists**: types, counts, nesting, negation, alternation and sets run. Stepped ranges raise. In my run (research notes, no block) the uniqueness flag was ignored, so `[@N2-3{1; 2; 3}U]` accepted `[1, 1]`, though the class has code for a uniqueness check. The wildcard of the article, `@A`, is not a token; the real wildcard is `@$`. And a reused object answers from a cache whose key is the list's length and the sum of its characters' codes, which does not depend on order. A fresh object answers 0 for `["hello", 1]`, and the same object after `[1, "hello"]` answers 1.
- **Matrices**: size, shape, element and three properties run. The class header lists the terms that accept every matrix: `row`, `col`, `pattern`, `determinant` and `sum`. A matrix of two by two is accepted by `{row(99)}`.
- **Time**: instants and durations with a step run. In my run (no block) a range without a step raised. And sequences over a timeline do not run at all: here is a timeline with a meeting, a break and a lunch, and the pattern the article promises, which should match:

```haro
oTl = new stzTimeLine("2025-10-22", "2025-10-22")
oTl.AddInstant("Meeting", "2025-10-22 09:00:00")
oTl.AddSpan("Break", "2025-10-22 10:00:00", "2025-10-22 10:15:00")
oTl.AddInstant("Lunch", "2025-10-22 12:00:00")
o1 = new stzTimex("{@Event(Meeting) -> @Duration* -> @Event(Break)}")
? o1.MatchPartial(oTl)
#--> 0
o2 = new stzTimex("{@Event(Lunch)}")
? o2.MatchPartial(oTl)
#--> 0
? @@( o2.Tokens()[1][:label] )
#--> "Lunch)"
```

The article promises that the first is TRUE. The second shows that even a single event the timeline holds does not match, and the third shows why: the label was read with its closing parenthesis. That is the shared bug, still present in time.

- **Graphs**: labels in order along a path, negation, alternation and numeric properties run. The arrow means *later on one path*, and not *next*. The quantifiers (`+`, `*`, `?` or a number after a token) are read and ignored. The graph of section 3 has three nodes; here `@Node10`, a node with the quantifier ten, is asked for between them, and the pattern matches:

```haro
? (new stzGraphex("{@Node(placed) -> @Node(served)}", g)).Match(g)
#--> 1
? (new stzGraphex("{@Node(placed) -> @Node10 -> @Node(served)}", g)).Match(g)
#--> 1
```

Cooking lies between the first and the last, so the first answer is the arrow's meaning. The second is the quantifier being ignored. The cache of this class is keyed by the node and edge counts and the node ids, so a second graph with the same ids and other labels is answered from the cache, until `ClearCache()`.

**The refusal the family has not yet made.** Chapter 11's law is that a language is declared and closed, with refusals. Here is the family, asked a word it does not know:

```haro
? Nx("{@Banana(3)}").Match(7)
#--> 1
? Nx("{@Banana(3)}").Match(1000003)
#--> 1
? @@( Nx("{@Banana(3)}").Tokens() )
#--> [ ]
? Nx("{@Property(Banana)}").Match(7)
#--> 0
```

A pattern with a word the language does not know matches every number. The tokens are empty, and nothing is raised. The matrix and table languages return an ERROR token that nothing raises, and the number and time languages return an empty list. The Haro charter session filed this as a finding, which the central record relayed on 28 September 2026: the six pattern classes accept unknown tokens silently. I reproduced it on this commit, and the request is not closed. A closed language that cannot refuse is not yet the law of chapter 11. The chapter prints it as a finding of the court, and not as a debt of mine.

What is designed: one pattern engine shared by all the media. The engine design says the backtracking engine, the constraint solver and the pattern compiler are the same across all domains, and that only the vocabulary changes. Its status is planned. At this commit the vocabulary changes and so does the code. The engine's own file named *pattern* is another thing: palindromes, repeats and arithmetic and geometric sequences. The pattern as the condition side of the cascade, many faculties firing one after another on a shared state, is chapter 9's third rung, and designed.

What is absent: induction from examples, which is reserved. The genetic, linguistic and quantic siblings, which are vision only. The explanation of an unnamed pattern, since `rx("[a-z]+").Explain()` raises because the analyser class was never built. And any use of the pattern classes by the rest of the library: outside the regex folder, the tests and the docs, no class takes a pattern. `stzList`, `stzNumber`, `stzTable`, `stzMatrix` and `stzGraph` have no `Matches(pattern)`. In the docs, the education course uses them, in a chapter and an exercise whose answer is checked by running the learner's program, and the gallery has a few scripts that use them.

## 8. Six doors

**The programmer.** One habit across six kinds of data, graphs apart: a small constructor, a pattern in a string, `Match`. The pattern is data you can read and compose. Use the ones with a guard: text, numbers, tables, matrices and graphs, and build nothing on the cache of a reused list pattern.

**The analyst.** A data-quality rule is a sentence of the table language. The person who owns the data can read it.

**The designer.** A pattern states a shape the interface can show before the data arrives, and a half-typed value is answered on the way.

**The decision-maker.** A rule is a line and not a procedure. It can be reviewed, and its verdict is 1 or 0. Say beside it that a pattern with an unknown word is not refused, and that a graph arrow means *later*.

**The educator.** The course teaches patterns in two chapters, in English, French, Arabic and Hausa. The ladder is a curriculum: text, list, number.

**The agent.** A pattern is a small closed notation that an agent can be held to and can read back. Be told that none of the six media can yet refuse a word it does not know, and that writing a pattern from examples is reserved.

## 9. Exercise

Three small tables are given. Write one pattern that accepts only the first. Before you run anything, write under each of the three printed lines what you expect and why.

```haro exercise
t1 = new stzTable([ [ :ID, :EMAIL ], [ 1, "ali@x.org" ], [ 2, "sara@x.org" ] ])
t2 = new stzTable([ [ :ID, :EMAIL ], [ 1, "ali@x.org" ], [ 1, "sara@x.org" ] ])
t3 = new stzTable([ [ :ID, :EMAIL ], [ 1, "ali@x.org" ], [ 2, "" ] ])
# write ONE pattern, then print whether it matches t1, t2, t3, on three lines
cPattern = "{ ... }"
? Tbx(cPattern).Match(t1)
? Tbx(cPattern).Match(t2)
? Tbx(cPattern).Match(t3)
#--> 1
#--> 0
#--> 0
```

Run it. One clause rejects the second table and another rejects the third; which is which? And what would the pattern say if the email were a single space? I do not answer first. If a promise breaks, do not change it: explain the output.
