# Law: a language is declared and closed, and whatever speaks it, person or model, is judged by it

Source: Chapter 11. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the natural layer's vocabulary as data in five languages, with its refusals; the court of structured output, its grammar compiler and its sampler; the pattern languages, which accept a word they do not know; designed: the forge that produces a language's parser, court and grammar from its declaration alone; a grammar emitted for every declared language; the writing style as a declared grammar; absent: a natural layer closed all the way down: one form of list still reaches host code; pattern classes that refuse a word they do not know; the standard Hausa letter ɗ in the Hausa pack

Run: 11 of 11 blocks kept their promise, on 2026-10-14 12:14 UTC+01:00.

In this chapter I state the law of Part III and run it. I begin with a sentence that runs because every word of it is in a dictionary the library owns, in English, Hausa, French and Arabic. I show what the library says about a word it does not know. Then I declare the shape of an answer as a schema, judge answers against it, and show the one thing a grammar cannot kill: a false answer in the right shape. I say which guards prove this, where the field is ahead, and where the natural layer is not yet closed, which the law states. The law itself is one sentence: a language is declared and closed, and whatever speaks it, a person or a model, is judged by it.

## What the AI age changes here

In Part II, the age changed who writes the code. Here it changes who speaks the sentence. A sentence of a language used to have a person behind it, someone who could be asked what they meant. Today the writer of a sentence can be an AI model, which cannot be asked, and which will write a fluent sentence whether or not it is true.

So the grammar must be closed, and the court, the part that accepts or refuses a sentence by its grammar, must read it. A language whose sentences may contain anything cannot refuse anything, and a court cannot judge a sentence it cannot read. The vision of the platform puts the whole movement in one line, which I ratified: humans and machines meet in declared languages, small, closed and judged, not in general-purpose code.

This is also where the order of the book turns around. The cover goes from the familiar to the new: programming, languages, intelligence. The record's logic goes the other way. The first act is to declare a language. Programming, the discipline of Part II, happens inside declared languages: the forms of the vocabulary are already a declaration in Haro, in a spike outside the library. Intelligence, Part IV, is governed by both: a model is held to a declared grammar before it speaks, and its sentence is judged after. The book keeps the cover's order, so this chapter sits in the middle; in the record's order it would come first.

## 1. The concept, as the field holds it

For a working programmer, a language is a general host, Python, JavaScript, Java. A "domain language" is usually a library whose calls read like sentences, while the file around them may contain any code of the host. The estate's own study of the field, written in August 2026, names what happened to those designs. Internal languages died of openness, because a build file is declarative only until someone writes arbitrary code in it. Language workbenches died of the weight of their tools. And it names the languages that won: SQL, regular expressions, Make, HTML and CSS, the configuration languages. They won because they are closed.

The model era added one practice: when an AI model writes, either check what it wrote, or constrain its output while it writes, with a grammar or a schema. The reference implementation of grammar-constrained sampling is an open project, and the record says so where it uses the same algorithm. And in the field's common language today, "programming in natural language" means one thing: prompting a model.

## 2. The first principle

**A language is declared and closed, and whatever speaks it, a person or a model, is judged by it.**

## 3. The Softanza form

Can a sentence run without an AI model guessing what it means? It can, when every word of it is in a dictionary the library owns:

```haro
Naturally("
    Make a string with 'hello niger' inside
    Spacify it and uppercase it
    @Box it while the box@ is rounded
    Display it on the screen
")
#--> ╭───────────────────────╮
#    │ H E L L O   N I G E R │
#    ╰───────────────────────╯
```

> run: kept

Four lines of English became a rounded box around spaced capitals.

The dictionary is data, keyed by meanings, not by English words. So can the same meaning be said in another language by adding a block of data, not code? Here is one instruction in English, in Hausa, in French and in Arabic. The Hausa sentence is the narration's own, and the French one comes from the library's guard with its data changed. I composed the Arabic one from the library's vocabulary. No native speaker has read the Hausa or the Arabic as far as the record shows:

```haro
? Naturally("Create a string with 'hello' and uppercase it").Result()
#--> HELLO
? NaturallyIn("hausa", "Yi rubutu dauke 'hello' Maida shi").Result()
#--> HELLO
? NaturallyIn("fr", "Crée une chaine avec 'hello' et mets la en majuscules").Result()
#--> HELLO
? NaturallyIn("ar", "أنشئ نصا بـ 'hello' ثم كبّره").Result()
#--> HELLO
```

> run: kept

Four languages, one meaning, and `HELLO` four times.

And a program says back what it understood, in its own language. A person reading Arabic can check the machine's reading of their sentence without reading a line of code.

```haro
o1 = NaturallyIn("ar", "أنشئ قائمة بـ [ 5, 3, 5 ] ثم أزل تكراراتها")
? @@( o1.Result() )
#--> [ 5, 3 ]
? o1.Understood()
#--> أنشئ قائمة بـ [ 5, 3, 5 ] -> أزل التكرارات
```

> run: kept

The program said back `أنشئ قائمة بـ [ 5, 3, 5 ] -> أزل التكرارات`: the list it was given, and the removal of duplicates.

Now the part the library does by rule: say what it did not understand. What does it do with a verb it does not know? Misspell one and run it:

```haro
o1 = Naturally("Create a string with 'softanza' Uppercse it")
? o1.Result()
#--> softanza
? @@( o1.Unresolved() )
#--> [ [ "Uppercse", "uppercase" ] ]
? o1.UnderstoodAll()
#--> 0
```

> run: kept

The misspelled verb is not guessed. `Unresolved()` answers `[ [ "Uppercse", "uppercase" ] ]`, the word it met beside the word the library thinks you meant, and `UnderstoodAll()` answers `0`: the program admits that it did not understand everything. That is the permissive mode: an unknown word is skipped and reported. An AI agent gets the strict mode, which refuses, and a world, a declared list of allowed operations, can limit its sentences to that list:

```haro
try
	NaturallyStrict("Create a string with 'x' Fooify it")
catch
	? cCatchError
done
#--> Strict natural mode: not understood: 'Fooify' (did you mean 'boxify'?)
try
	NaturallyStrictIn("en", "Create a list with [ 3, 1 ] Reverse it", [ "METHOD_REMOVEDUPLICATES" ])
catch
	? cCatchError
done
#--> Operation not permitted in this world: METHOD_REVERSE
```

> run: kept

Strict mode refuses `'Fooify'` and still names the nearest word: `did you mean 'boxify'?`. In that world, a sentence that reverses a list is refused! The refusal names the operation: `Operation not permitted in this world: METHOD_REVERSE`.

The other direction of natural code in Softanza is the near-natural chain, where the person is the parser and the chain reads as a sentence. When it answers no, does it say why?

```haro
? IsQ().TheQ().LengthQ().OfQ("softanza").LessThanQ().TheQ().LengthQ().Of("Haro")
#--> 0
? Why()
#--> no: 8 is not less than 4
```

> run: kept

The chain answered `0`, and `Why()` gave the reason: `no: 8 is not less than 4`. A verdict says why.

Now the law at its sharpest: an AI model. The library declares the shape of an answer as a schema. What happens to a schema that names a type the library does not have? It is judged when it is declared, before any model is called:

```haro
try
	StzOutputSchemaQ([ [ :field = "x", :type = :colour ] ])
catch
	? cCatchError
done
#--> stzOutputSchema: unknown field type 'colour' (use string|number|boolean|oneof|list|structure).
```

> run: kept

The refusal names the unknown type, `'colour'`, and lists the six it accepts: `(use string|number|boolean|oneof|list|structure)`. The schema was refused before any model was called! A correct schema is a small closed language. The court judges any answer against it, whoever wrote the answer. And the schema emits its grammar, so that a model can be held to it while it writes:

```haro
oS = StzOutputSchemaQ([
	[ :field = "name", :type = :string ],
	[ :field = "age",  :type = :number, :must = [ [ ">=", 0 ], [ "<=", 130 ] ] ],
	[ :field = "mood", :type = :oneof,  :choices = [ "positive", "negative" ] ]
])
? oS.Accepts("name: Hadiza" + nl + "age: 41" + nl + "mood: positive")
#--> 1
? oS.Accepts("name: Hadiza" + nl + "age: 41" + nl + "mood: angry")
#--> 0
? oS.Accepts("name: Hadiza" + nl + "age: 900000" + nl + "mood: positive")
#--> 0
? oS.Accepts("name: Hadiza" + nl + "age: 62" + nl + "mood: positive")
#--> 1
? oS.ToGBNF()
#--> root ::= name-line age-line mood-line
#    name-line ::= "name: " text "\n"
#    age-line ::= "age: " number "\n"
#    mood-line ::= "mood: " ("positive" | "negative") "\n"
#    text ::= [^\n]+
#    number ::= "-"? [0-9]+ ("." [0-9]+)?
#    boolean ::= ("yes" | "no" | "true" | "false")
```

> run: kept

Look at the four verdicts. The first answer printed `1`. The second, with `mood: angry`, and the third, with `age: 900000`, printed `0`: the court refused both. The fourth printed `1` again. Hadiza is forty-one in the first answer and sixty-two in the fourth, and the court accepts both! A grammar kills malformed sentences, not false ones. The record says it in five words: structure kills malformedness, not falsehood. This book says the same: the truth of an answer is not for the grammar. The record says that truth needs reversibility, an auditor and a Principal, the person who rules. A grammar is the gate, not the judge of everything.

A template is a contract too. A sentence with an unfilled hole is refused before it runs:

```haro
try
	NaturallyWith("Create a string with {#1} and {#2} it", [ "x" ])
catch
	? cCatchError
done
#--> Unfilled template hole! The narration still contains a {#n} slot with no value for it.
```

> run: kept

And patterns are small languages of their own, though not yet closed ones: chapter 15 shows the pattern classes accepting a word they do not know, without complaint. The shape of a list is declared, not written as a loop:

```haro
? Lx("[@N, @S]").Match([42, "hello"])
#--> 1
? Lx("[@N, @S]").Match(["hello", 42])
#--> 0
? Lx("[@N, [@N2], @N]").Match([1, [2, 3], 4])
#--> 1
? Lx("[@N, [@N2], @N]").Match([1, [2], 4])
#--> 0
```

> run: kept

Two shapes matched, two did not, and no loop was written.

The chapters of this part prove the law from five sides. Chapter 12 tells a language declared: the forge (the machinery that produces a language's parser, court, printer and grammar from its declaration alone), the closed grammar with no escape into the host, and the court born with the grammar. It tells too the grammar emitted so that a model can only speak valid sentences, and its surfaces. Chapter 13 tells the two directions of natural code, the machine as the parser and the person as the parser, in one discipline. Chapter 14 tells knowledge programming, one file that is a system. Chapter 15 tells the pattern languages, regex lifted to lists, numbers, tables, matrices, time and graphs. Chapter 16 tells the seven languages Softanza reaches through one governed door, and why a door is not a surface.

## 4. The decision, and what I refused

**I chose the act: declare a language.** Not "use our language". Declare yours: the language of your domain, in your words. That is the kernel of the platform, and it is the reason this part exists.

**I refused the open escape.** The meta-language that declares languages in the estate lives outside this library. Its founding rule refuses to define any form that would let a sentence reach host code, call a function, evaluate a string or touch a file. Not forbidden: unexpressible. An internal language that cannot refuse arbitrary host code is, in the words of the estate's field study, an API wearing a language's costume.

**I refused natural language as a way to declare.** Natural language asks; it never declares. A model may draft a declaration, and by the vision's rule, which is designed and not yet built, the draft enters the world only as a proposal: the model proposes, the court decides, a person ratifies.

**I kept the promise of 2020 and changed its mechanism.** My first slide promised executable natural language. The vision of 2026 judged that slogan: it promised more than a court can defend, because a natural sentence can be ambiguous and a lie can be grammatical. So the naturalness stays at the door, where a sentence asks or drafts, and the execution belongs to closed languages a court can judge. I built the natural layer that way long before the vision named it. Only words defined in the dictionary are interpreted. Every other word is skipped and reported, or refused in strict mode, never guessed.

**I took governance out of the library and kept the refusals in it.** In July 2026, a kit for governing AI agents landed inside the natural layer. I removed it the same day: the strict mode, the refusals, the why and the understood belong to the library; a product for governing agents does not. And I removed a set of markers: their letter-order cipher had been inverted by its own inventor, from memory, and they duplicated meanings. A language a person speaks never marks a reference that way. An ungrammatical chain that runs is a bug.

**I refused a second embedding.** Chapter 1 states that decision; here I add only that a door brings a foreign runtime, a surface brings a familiar syntax over the same grammar, and Chapter 16 tells the difference.

## 5. The court

`multilingual_pack_narrated` proves the languages as data: the packs, the programs in French and Arabic, a pack added at runtime, and the program paraphrasing back in its own language. `semantic_resolver_narrated` proves the unknown word with its suggestion, the strict mode, and the allow-list under which everything off the list is grammatically impossible. Its run does not yet reach its end at this commit. My research for chapter 13 ran it twice on 8 October 2026, and request L45 in the memo of 9 October records the result. It stops with an error raised from a string-splitting function, before its last assertion. So the page counts its assertions and does not claim its verdict. `literate_templates_narrated` proves that a template is a contract. `question_narrated` proves that a yes-or-no verdict records its why. `structuredoutput_narrated` proves the court of structured output, including the lie it lets through. `schema_grammar_narrated` proves the grammar compiler, and `constrained_decoding_narrated` the sampler that holds a model to it.

Seven guards prove the law; the next section says where the field is ahead of it.

## 6. The field, and where it leads

The field leads in tools. The language workbenches remain ahead on the axes the estate's design deliberately gave up: projectional tooling (editors that understand a language as you type), IDE integration, macro-theoretic depth. The estate's study says it in its own words: that is a bet, and it is named as one. I hold that bet as a view, not a result.

The field built constrained decoding first. Softanza's sampler follows the reference implementation's algorithm and vendors nothing. Measured against one small model of a hundred and thirty-five million parameters, on ten prompts, the answers were valid at the first attempt two times in ten when checked afterwards. Held to the grammar, the model was valid ten times in ten. That is one small model and ten prompts, and nothing in the record measures a large one.

And the age cuts both ways. Generated code makes careless language-making cheap too. That is why the court is not an accessory of a declared language. It is the core. This is my view.

## 7. The limit

What is built: the natural layer, its vocabulary as data in five languages, English, Hausa, French, Arabic and Turkish, and its refusals. Built too: the court of structured output with its grammar compiler and its sampler, and the pattern languages. These accept a word they do not know today; closing them is to come.

What is designed: the forge that would produce, from a language's declaration alone, its parser, its court, its printer (the part that writes a sentence back out) and its grammar for a model. The forge is built outside the library and designed for the library: a first sketch of it was built outside the library in October 2026. The library cannot run it yet. The vision's text says the forge has not yet forged (made a language's parts from its declaration). The sketch has since forged courts and grammars for several languages, judged by those languages' own fixtures, and the vision has not caught up. Chapter 12 tells it with its limits. A grammar for every declared language is designed and to come.

What is absent, and the law states it. The natural layer is not closed all the way down. One form, a list written inside brackets, is still handed to the host to evaluate. Does a host function inside the brackets run? Try one:

```haro
? @@( Naturally("Create a list with [ upper('x'), 1 ] and remove its duplicates").Result() )
#--> [ "X", 1 ]
```

> run: kept

The function `upper` is not a word of the natural dictionary, and the list came back as `[ "X", 1 ]`. It ran anyway! The record already knows this escape and has routed its repair. Until the repair lands, "the natural layer is a closed language" is true of its words and not of its lists, and this book will say so.

And the Hausa pack does not yet read the letter ɗ, which standard Hausa spelling uses. The pack stores it in an encoding that does not carry it yet. When I probed it on 8 October 2026 on the snapshot before this commit, a sentence written with the letter was not read, and the pack did not report it. The Hausa in this chapter is written without the hook, the way the pack reads it today. The record holds no reading of the pack's sentences by a Hausa speaker. The foreign-language sentences printed in this chapter come from the library's narration and guards, or are composed from its vocabulary. No native speaker has read them as far as the record shows.

These are the limits; the next section opens six doors on them.

## 8. Six doors

**The programmer.** You keep writing code. What you declare is a closed grammar, and the court judges your sentence and an AI agent's by the same rules.

**The analyst.** Your domain's words become a data pack, and the system understands them or refuses them with the reason.

**The designer.** The refusals are part of the language: what is off the list is refused in strict mode, so it never needs a warning.

**The decision-maker.** An AI model held to a declared grammar answers in the right shape. It can still answer a falsehood in the right shape, and the record prints that limit with the result.

**The educator.** A sentence in Hausa, French or Arabic runs and says back what it understood, so a learner reads the machine's reading of their own words.

**The agent.** You may speak only the declared language. Strict mode is your posture, and your draft is, by the vision's rule (designed), a proposal the court judges.

## 9. Exercise

Declare, with `StzOutputSchemaQ`, a record of three fields from a domain you know: a loan request, for instance, with an amount inside a band, a currency from a closed list, and a purpose in free text. Before you run anything, write three answers an AI model might give: one the court must accept, one it must refuse because of its shape, and one it will accept although it is false. Under each, write your prediction as a promise.

Run it. The third answer is the lesson of this chapter. Write down, in one sentence, who in your domain must judge it, since the grammar cannot.

I left this one in your hands. Section 7 says that a list written inside brackets is still handed to the host, and section 4 says why a language must refuse any form that reaches host code. Run the section 7 block with one change, a different host function inside the brackets:

```haro exercise
? @@( Naturally("Create a list with [ lower('X'), 1 ] and remove its duplicates").Result() )
```

> run: exercise

Look at what the library does with the function, and say in one sentence what a closed natural layer would have done instead. When you have, you will know why "the natural layer is a closed language" is true of its words and not yet of its lists.

Chapter 12 is *A language, declared*. Its principle: declaring a language is as easy as declaring a variable.
