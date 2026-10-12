---
id: a-language-declared
part: 3
number: 12
title: A language, declared
spine: false
narrations: [stz-conditional-code-narration.md, stznatural-vs-ring-naturallib.md, stznatural-narration.md, stz-bridging-minds-and-code.md]
site: [languages]
guards: [structuredoutput_narrated, schema_grammar_narrated, constrained_decoding_narrated, 483_w_and_wf_forms_in_conditional_code, calc_column_engine_narrated]
stage:
  built: "in the library: a declaration judged when it is declared; a court and a grammar from the one declaration, with the list of what the grammar dropped; a grammar machine that walks bytes and refuses by name; a description for a person and a prompt for a model from the same text. Outside the library: a forge that turns a declaration into a court and a grammar, run on the estate's own languages"
  designed: "the forge inside the library; its full list of products from one declaration (printer, knowledge graph, natural door, narration, runtime, one static binary); the projections of a language to an application"
  absent: "the forge's grammar for a menu word; a guard that asserts the refusal of a host function in a condition; the figure two of ten against ten of ten, which needs a model file the snapshot does not hold"
status: draft
rulings: ["12.10", "12.21", "12.27", "12.29", "12.30"]
research: research/ch12.md
---

In this chapter I take one declaration of a restaurant's order and give it to three readers: a person, a model and the court. I let the same declaration produce a grammar, and I show where the grammar and the court agree and where they part. Then I leave the library for the forge, the machinery that turns a language's declaration alone into its court and its grammar, and I say what it has forged and what it has not. I decided that Haro is the language of languages, and I refused an open escape form. The principle is one rule of Haro: declaring a language is as easy as declaring a variable.

## 1. The concept, as the field holds it

Two families of tools let you declare a language in the field. The first is the language workbench and the parser generator: JetBrains MPS, Xtext, Spoofax, and Racket's `#lang` give you the means to define a language with its grammar, its editor and its checks. The estate's own field study of August 2026 says why they did not win. They depended on an ecosystem, and Racket's languages live and die inside Racket.

The second is the internal DSL: a library whose calls read like sentences, while the file can still hold any host code. The same study has the sentence I keep: closedness is the product, and an internal DSL that cannot refuse arbitrary host code is an API wearing a language's costume. Its control group is the closed languages that won: SQL, regex, Make, HTML and CSS, HCL, GraphQL, Markdown, CUE.

For the grammar a model must obey, the record names one tool: the grammar sampler of a well-known local inference library, which the library's machine follows for its element encoding and its algorithm. Nothing of it is vendored. (General knowledge, not a study of the record: model vendors offer structured-output modes that take a JSON schema, and open libraries turn a schema or a regular expression into a mask on the model's tokens.)

Chapter 11 told what a closed language is, and what was lost when the field left it open. I take that as read. This chapter says what is new: what *produces* a closed language.

## 2. The first principle

**Declaring a language is as easy as declaring a variable.**

It is the heading of one rule of Haro, ruled on 1 October 2026, and the kernel of the vision says the same: the era makes declaring a language as easy as declaring a variable. The sentence of the other half of the chapter, from the alphabet's totality doctrine, ratified on 27 September: malformedness dies at the sampler, falsehood dies at the court, and non-termination is unexpressible.

And the one I must carry beside every win, from the library's contract for structured output: structure kills malformedness, and not falsehood.

## 3. The Softanza form

Take a declaration of what a restaurant's order must look like. It has three fields: a dish from a closed menu, a quantity between 1 and 12, and an optional note. One text is read by three readers. A person reads a description. A model reads a clause for its prompt. And the court reads the same text and judges an answer. What does it answer to a dish called pizza and forty portions? Run it:

```haro
oO = StzOutputSchemaQ([
	[ :field = "dish",     :type = :oneof,  :choices = [ "margherita", "tiramisu" ] ],
	[ :field = "quantity", :type = :number, :must = [ [ ">=", 1 ], [ "<=", 12 ] ] ],
	[ :field = "note",     :type = :string, :optional = 1 ]
])
? oO.Describe()
#--> schema 'output' -- 3 field(s)
#      dish : oneof (margherita | tiramisu) [required]
#      quantity : number [required], must be at least '1', must be at most '12'
#      note : string [optional]
? oO.PromptClause()
#--> Answer with ONLY this structure, one field per line, nothing before it and nothing after it:
#
#    dish: <one of: margherita | tiramisu>
#    quantity: <number>
#    note: <text>
aV = oO.Verify([ :dish = "pizza", :quantity = 40 ])
? aV[:ok]
#--> 0
? aV[:findings][1][:message]
#--> field 'dish' is a closed enumeration (margherita | tiramisu) and the model answered 'pizza'.
? aV[:findings][2][:message]
#--> field 'quantity' must be at most '12', and the model answered '40'.
```

The court answers in the declaration's words: `field 'dish' is a closed enumeration (margherita | tiramisu) and the model answered 'pizza'.` Now the same declaration produces a grammar. The court and the grammar are born of one text, and they agree on the shape. They part ways on a value. Forty portions has the right shape: which of the two lets it through, and does the library say what the grammar dropped? Run it:

```haro
cG = oO.ToGBNF()
cGood  = "dish: margherita" + nl + "quantity: 2" + nl + "note: no basil" + nl
cBand  = "dish: margherita" + nl + "quantity: 40" + nl + "note: no basil" + nl
cShape = "dish: margherita" + nl + "quantity: many" + nl + "note: no basil" + nl
? StzGrammarAccepts(cG, cGood)
#--> 1
? oO.Accepts(cGood)
#--> 1
? StzGrammarAccepts(cG, cBand)
#--> 1
? oO.Accepts(cBand)
#--> 0
? StzGrammarAccepts(cG, cShape)
#--> 0
? oO.Accepts(cShape)
#--> 0
? len(StzFind("lessequal", oO.UnenforcedByGrammar())) > 0
#--> 1
```

The second pair is the point of the chapter: the grammar answers `1` and the court answers `0`. I do not print the list of what the grammar dropped, because its text carries the former name of the court in one place. I test that it names the limit of the range.

A model is not asked to be careful. The sampler asks the grammar at every candidate token whether it could continue. So a word that is not on the menu is not refused after it is said. Can it begin at all?

```haro
? StzGrammarCouldContinue(cG, "dish: t")
#--> 1
? StzGrammarCouldContinue(cG, "dish: p")
#--> 0
? StzGrammarCouldContinue(cG, "dish: margherita" + nl + "quantity: 2")
#--> 1
? StzGrammarCouldContinue(cG, "dish: margherita" + nl + "quantity: <")
#--> 0
```

It cannot: `dish: p` answers `0`. The last line is a failure the measurement found in a small model: the placeholder `<number>` echoed where a number belongs. And a token is not a byte. A piece may be valid as a prefix and invalid as a completion, and the machine is fed the whole piece:

```haro
cY = 'root ::= "yes" "\n"'
? StzGrammarCouldContinue(cY, "y")
#--> 1
? StzGrammarCouldContinue(cY, "ye")
#--> 1
? StzGrammarCouldContinue(cY, "yesterday")
#--> 0
```

What the machine will not hold, it refuses by name. A closed language refuses what it cannot carry, and never approximates. A left-recursive rule is refused by a code, and so is a rule referred to and never defined. A nested structure is refused by the grammar. Does the court still read it?

```haro
? left(StzGrammarRefusal('root ::= tail' + nl + 'tail ::= tail "x" | "x"'), 7)
#--> GBNF-M7
? left(StzGrammarRefusal('root ::= greeting'), 7)
#--> GBNF-M4
? StzGrammarRefusal(cG) = ""
#--> 1
oNest = StzOutputSchemaQ([
	[ :field = "title",  :type = :string ],
	[ :field = "author", :type = :structure, :fields = [ [ :field = "name", :type = :string ] ] ]
])
? oNest.IsExpressibleAsGrammar()
#--> 0
try
	oNest.ToGBNF()
catch
	? len(StzFind("GBNF-F5", cCatchError)) > 0
done
#--> 1
? oNest.ParseOutput('{ "title":"T", "author":{"name":"Ada"} }')[:ok]
#--> 1
```

The text of the nested-structure refusal carries the former name of the court, so I print only the codes. The last line is the point: the court reads what the grammar refuses to write.

The declaration language is itself closed. A typo in the law is refused when the law is declared. The library's contract says why: a key such as `:requird = 0`, quietly leaving a field required, is exactly the class of typo a court must not tolerate in its own law:

```haro
try
	StzOutputSchemaQ([ [ :field = "x", :type = :string, :requird = 0 ] ])
catch
	? cCatchError
done
#--> stzOutputSchema: unknown key ':requird' in field #1 (use :field, :name, :type, :required, :optional, :choices, :oneof, :of, :fields, :must, :note, :description).
```

And a host function is not a word of the closed language of conditions. There are two ways to say a condition, the closed language and the door of a function. A square root is a word of the engine's expression language, and a sine is not. The textual form answers nothing, and the function form runs host code and answers everything:

```haro
o = new stzList([ 4, 7, 10, 3, 8 ])
? @@( o.FindW('{ sqrt(@item) < 3 }') )
#--> [ 1, 2, 4, 5 ]
? @@( o.FindW('{ sin(@item) < 2 }') )
#--> [ ]
? @@( o.FindWF( func x { return sin(x) < 2 } ) )
#--> [ 1, 2, 3, 4, 5 ]
```

What I saw, and the narration does not say: the refusal is silent and whole. A condition with the true left branch and a sine on the right printed `[ ]`. A condition that calls a function of mine never called it. A syntax error also printed `[ ]`. The language is closed, and it refuses without a word. Chapter 11's natural layer says why it refuses, and this one does not.

### The forge, outside the library

A language declared once should give its court, its mouth, its voice and its readers. That is the forge, and it is where the study of this book meets its own limit: the forge is not in the library.

I will say what the record holds, and what I observed on 8 October 2026 on the older runtime, the oracle. The record is a charter and a spike in another repository, in pure core code that runs on the oracle. The forge reads a declaration and writes two files, a court program and a grammar. The spike's rungs, between 1 and 4 October 2026, forged courts and grammars for the machine language of the estate and for a fleet language declared over it. They did the same for the expression language and for four more letters of the alphabet. Each was judged against the pre-existing language's own cases: unadapted for the expression language (W) and for Z, re-expressed for F and A, and, for Q, against the older language's own answers, captured. In order: 117 of 120 for the machine language, the three left being the fleet file's kinds. Then 32 of 32 for the fleet language, 29 of 29 for W, 16 of 16 for Z, 25 of 25 for Q, 26 of 26 for F and 35 of 35 for A. This is chapter 3's method, declare then govern, applied to the forge itself.

I ran the forge on a small language I wrote for this book, a table's order in the words of the dining room. It is an example, written for the book and run once, outside the library:

```text
DEFINE LANGUAGE order AS ( VERSION "0.2", GRAMMAR "0.2", COURT "none", EXTENSION ".order" )
  RATIONALE "A table's order, in the words of the dining room"
DEFINE MENU dishes AS ( WORDS [margherita, tiramisu, chianti],
  MESSAGE "the kitchen cooks margherita, tiramisu or chianti" ) RATIONALE "The kitchen's closed menu"
DEFINE RANGE portions AS ( MIN 1, MAX 12,
  MESSAGE "{value} portions is not an order: one to twelve" ) RATIONALE "A table orders between one and twelve"
DEFINE DECLARATION line AS ( VERB "ORDER", SEATS [dish: dishes, quantity: portions, note: text?] )
  RATIONALE "One line of an order: what, how many, and a word for the kitchen"
DEFINE REFUSAL unknown_verb AS ( MESSAGE "The dining room speaks only of orders." )
  RATIONALE "The closure speaks when an alien verb arrives"
```

The forge printed that it had forged one kind and one refusal, in a fraction of a second of wall time, and wrote a court of about 2.6 kilobytes. The court refused three sentences in the declaration's own words:

```text
DISH pizza          ->  order (line 2): the kitchen cooks margherita, tiramisu or chianti, not 'pizza'
QUANTITY 40         ->  order (line 3): 40 portions is not an order: one to twelve
DROP TABLE orders   ->  order (line 1): Unknown verb 'DROP': The dining room speaks only of orders.
```

The refusals are the declaration's own words, written beside the grammar. This is the whole of the evidence for the `order` language: it ran once, outside the library, and it is not a declaration of the record.

Three more observations, each a limit.

**The meta-court refuses the escape.** The declaration of the language of declarations lists the operators and operands it may use. A declaration that listed `eval` among its operators, in a fixture pinned on 29 August 2026, was refused: `eval` is not in the closed operator menu, an escape hatch is unexpressible, not forbidden. A host call among the operands was refused in the same way.

**The forge's grammar holds shape only.** A menu seat comes out as a general identifier, so the forged grammar lets `pizza` through. The library's own schema compiler, in the blocks above, closes the same menu into an alternation. On the estate's machine language, the forged grammar accepts a dangling reference that the court refuses. The record names a difference between mouth and court, the part that a context-free grammar cannot say: duplicate names, dangling references. I found no record that states the menu gap as a gap.

**The vision has not caught up.** The vision's text, dated between 27 September and 5 October 2026, says the forge has not forged. The principles file, dated 1 October 2026, says that the forge does not exist. The same repository built the spike the same day and forged for several languages. So the true sentence has two sides. The forge has forged courts and grammars for several languages, outside the library, and it has not forged the full list the principle promises. And the vision's text has not been updated. In the book's stage words, the forge is built outside the library and designed for the library, and chapter 11's limit says the same.

### The facets of a declared language

By facet I mean here a surface of a declared language. The charter lists what the forge produces from a declaration, and I give each a stage word:

| facet | what it is | stage |
|---|---|---|
| the text | the declaration, plain and closed, with a rationale required on every declaration | built outside; the library's analogue is the schema declaration |
| the court | the judge generated for the language, speaking in the declaration's own words | built outside; the library's analogue is `Verify` and `Accepts` |
| the mouth | the grammar for a constrained model | built in the library for schemas; built outside for declared languages, shape only |
| the prompt | the instruction a model reads, tuned by measurement | built in the library; not known for declared languages |
| the person's reading | a description for a human | built in the library (`Describe`) |
| the voice | the language narrating a run, a sentence, a refusal; never stored and never parsed back | built outside; the library's analogue is `Understood()` |
| the tongues | a human language as a data file | built outside for two tongues; built in the library for five packs (chapter 11) |
| the projections | the world rendered to an application, a server, a page, a device | designed |
| the faces | a second syntax of Haro | designed; chapter 16 tells it |

The word *facet* has other meanings in this book, and I define mine here: a surface of a declared language. The second sense is a syntax of Haro for a programmer of another language: the table calls it a *face*, and chapter 16 tells it. The third is a tab of the environment's ribbon, one phase of a life, which is chapter 26's.

## 4. The decision, and what I refused

**I decided that Haro is the language of languages.** The charter's header quotes me, from 1 October 2026: Haro is a language of languages, in which the crafters define a language for their domain and program in it, or let their agents. The charter records a reversal: its first decision, as the general-purpose floor under the family of declared languages, was reversed. The rest of that ratification was my "go with your recommendations" on seven decisions, and those are rulings by delegation.

**I decided to declare, and not to write.** The act of the kernel: declare a language. It was extraction and not invention: the first languages were declared after they already ran and had consumers.

**I refused an open escape form.** No clause, operator or operand denotes host code, calls, evaluation or input and output. Unexpressible, not forbidden. Two fixtures pin the refusal, and I re-ran them.

**I refused logic in the declaring surface.** The declaration declares and does not compute. The alphabet is deliberately not Turing-complete, and that is its power and not its poverty. This is my view.

**I refused natural language as the declaring surface.** Natural language asks, and it never declares. A draft may be proposed, and the court decides, and the human ratifies.

**I refused one text for declaring and for computing.** Programmability and closure never occupy the same surface. Computing code reaches a declared world only through the doors the forge generates, and chapter 16 is about the door.

**I refused to let the grammar half retire the court.** The contract says the court does not retire when constrained decoding lands. And what the grammar cannot express it refuses, and never flattens or approximates.

**I refused a second face as a second meaning.** A face spells the graph; it never gives it Python's or JavaScript's meaning. That is a session's memo, which proposes and rules nothing, and its question of how many faces before the announcement is mine, and unanswered in the record.

## 5. The court

`structuredoutput_narrated` proves that a declaration is judged when declared, with an unknown type, an unknown key and an empty menu refused. It proves that two wire shapes are read and nothing is guessed, that there is no partial credit, that nesting works, and that a retry fits in one budget. In its tenth scene, it proves that a lie is let through on purpose. `schema_grammar_narrated` proves that the declaration compiles to a grammar, and that a closed enumeration becomes a closed alternation. It proves that optional and list arity are handled, that the unenforced constraints are listed by field and operator, and that a nested structure is refused with a named code. `constrained_decoding_narrated` proves that the machine walks a grammar byte by byte, that a prefix is not a whole, and that `yesterday` is refused. It proves that the placeholder the model wrote cannot be reached, that refusals are named, that structure is not falsehood, and that a grammar on a streaming session is refused. Its two scenes that need a generative model say so. `483_w_and_wf_forms_in_conditional_code` proves that the two forms of a condition give the same positions. It does not assert the closed language's refusal, and no guard does.

No guard in the library tests a forge, since there is none. The forge's guard is outside: the spike passes twenty-three stages in 367.5 seconds on 4 October 2026, by its own file. I did not run it. And the meta-court's own first run was twenty-eight of twenty-eight on 29 August 2026. The book's guard reader resolves only guards in the library's test tree, so these cannot be named in the front matter.

The figure that the first attempt is valid in two cases of ten when checked afterwards, and in ten of ten when constrained, is a number in a comment of these guards. It cannot be re-taken here: the live scenes need a generative model file, and the snapshot holds only a checksum file in its folder for models. Chapter 11 carries the figure, and I point to it.

## 6. The field, and where it leads

The workbenches lead on tooling. The field study says it itself: they remain superior on the axes the design deliberately abandons, projectional tooling, editor integration and depth of macros. And the bet that those axes are the wrong ones is named as a bet.

Generated code makes undisciplined language-making cheap too, and that is why the court is the core and not an accessory. I hold this as a view, not a result.

Constrained decoding: the field built it first, and the reference implementation is another library's. What the record adds is the pairing: a grammar and a court from one declaration, and the list of what the grammar dropped.

A grammar over-approximates a court. Duplicate names, dangling references and the coherence of a menu are not context-free. I observed it both ways above: a band the grammar cannot carry, and a reference it cannot carry.

The code a forge emits must be read by someone. The family style that every declared language inherits has a success test, that learning the second language should take an evening, because it is the first language with different verbs. It is a design requirement and not a measurement. No learner has been timed in the record I read.

## 7. The limit

The library has two closed formula languages, and they behave differently at the edge. A reader who takes the closed condition language of chapter 11 and of the condition above to cover every formula will be wrong at the table. The calculated column of a table falls back, by its own header, to the classic evaluation path when the engine cannot compile a formula. Does the word `sin` that the condition refused run here?

```haro
o1 = new stzTableAggregator([
	[ :A, [ 0, 1, 4 ] ],
	[ :B, [ 2, 4, 20 ] ]
])
o1.AddCalculatedCol(:SINE, 'sin(@(:A))')
? @@( o1.Col(:SINE) )
#--> [ 0, 0.84, -0.76 ]
```

The sine the condition refused, the table computed! I also saw, and do not show, a second thing. On another probe table, with A as 1, 3 and 10 and B as 2, 4 and 20, I wrote a formula `@(:A) + HostBonus(@(:B))` around a function of mine that multiplies by a thousand. It printed `[ 2001, 4003, 20010 ]`: a user-defined host function ran from inside a formula string. And a formula that names a function that does not exist raised the host's own error. So the second closed language is open at its edge. No guard asserts either behaviour.

What is built: in the library, a declaration judged when declared; a court and a grammar from it; the list of what the grammar dropped. A grammar machine that says it is constrained; a prompt and a description from the same text. The build counts 151 assertions in three narrated guards. Two closed little languages of conditions, with limits. The natural layer's tongues as data.

What is built, but outside the library: a forge from a declaration to a court and a grammar, in the Haro charter's repository.

What is designed: the forge producing from a declaration alone the parser, court, printer, grammar, knowledge graph, query grammar, natural door, narration, runtime and one static binary. By my reading of the charter, the spike has shown the court, the grammar, a runtime that walks the declaration, a query grammar, a narration and the court of the natural letter. I did not find shown a printer for declared sentences, a knowledge graph forged from a declaration, or the one static binary per language. The library having a forge: nothing in it declares or forges a language. A grammar for every declared language shipping in the library: promised in the kernel, not shipped. And the projections: the world rendered to an application, a server, a page, a device.

What is absent: the forge's grammar for a menu word, which I saw above holds shape only, and the figure of two of ten against ten of ten, re-taken. And any record that the forge runs on the Haro runtime. At the time of the vision's writing the language did not exist; the charter's runs are on the older runtime and on the oracle.

## 8. Six doors

**The programmer.** You declare the shape in a few lines and get its court, its grammar and its prompt from them. What you do not get is a way to run a host function from the declaration: the language has no word for it.

**The analyst.** The declaration is plain text in the domain's words, and the court answers in those words.

**The designer.** The refusal is declared beside the grammar, in the domain's voice, and is not authored per runtime. A designer chooses what a closed menu says when it is broken.

**The decision-maker.** One declaration produces the mouth and the court, and the forge itself publishes where they disagree. The forge is outside the library today. Do not buy it as shipped.

**The educator.** The reader can predict, byte by byte, what the sampler will allow, and learns that a grammar kills malformedness and not falsehood.

**The agent.** You speak only the grammar you were handed. A sentence you draft is a proposal that the court judges. Your mouth is shape, and your falsehoods are the court's and a person's.

## 9. Exercise

Write, by hand, a grammar for one line of a lunch order: `dish: ` then one of two dishes of your choice, then a newline. Before you run anything, write your predictions as promises:

```haro exercise
cG = 'root ::= ...'     # your grammar here
? StzGrammarAccepts(cG, "dish: <your first dish>" + nl)
#--> ?
? StzGrammarAccepts(cG, "dish: <a dish not on your menu>" + nl)
#--> ?
? StzGrammarCouldContinue(cG, "dish: <the first letters of your first dish>")
#--> ?
? StzGrammarAccepts(cG, "dish: <the first letters of your first dish>")
#--> ?
? StzGrammarRefusal(cG) = ""
#--> ?
```

Then add a number to the line, `quantity: ` and digits, and write a sixth prediction: does your grammar accept `quantity: 4000`? Run it. The lesson is the third, the fourth and the sixth. The machine already knows that a prefix could continue and is not yet a sentence, and it cannot know that the number is too large. Write down, in one sentence, who in your restaurant must refuse forty portions, since the grammar cannot.

The next chapter turns to the natural sentence, in two directions and under one discipline. A sentence runs because every word of it is in a dictionary the library owns, and what the library does not know, it refuses, with the reason.
