# The domain language model

Source: Chapter 19. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the domain model's first rung with no neurons; its facts rendered as a corpus; a closed vocabulary; completion by lookup; a plain-text bundle that travels with its tests; a small second rung, a bigram, exported to a model file; the admission of a fact by a law; designed: a grammar derived from a knowledge base by one call; the typed unit of prediction validated in five stages; a second rung whose corpus is checked before it trains; the foundry that would make it larger; absent: a pipeline that chains the five stages on any unit; an end-of-sentence word for the second rung; a completion that sees the sentence so far

Run: 7 of 7 blocks kept their promise, on 2026-10-13 09:43 UTC+01:00.

In this chapter I forge a domain language model from a knowledge base, and no one writes its training text: every sentence is a recorded fact. It has two rungs. The first answers from those facts and has no neurons. The second, a small neural model, is fluent in the grammar of the domain and wrong about facts. I show the grammar that refuses a malformed sentence and the graph that refuses a false one. I say which pieces the library holds and which the reader still has to compose. The principle is this: the next thing the model says is a checkable unit of your world, a fact your rules admit or refuse, never a token.

## 1. The concept, as the field holds it

A language model predicts the next token. A token is a fragment of text with no type, no role and no constraint: it can be the end of a word, a space, a bracket. Everything a model says is built by choosing tokens one after another. Everything that makes the result useful, that it is a valid sentence, that it is true, that it fits a schema, is checked afterwards or enforced from outside.

The field has made this work with three tools. You adapt a general model to a domain by training it further on the domain's documents. You give it the relevant documents at the moment of the question, retrieved by similarity. And you constrain its decoding with a grammar, so that it cannot produce a malformed sentence, as chapter 11 showed. All three keep the unit the same: the token.

The next section names the one thing I change: the unit.

## 2. The first principle

**The next thing the model says is a checkable unit of your world, a fact your rules admit or refuse, never a token.**

In the design the gate is the same for every model of this kind: generations are proposals, and the graph and its rules decide admission.

Section 3 shows the form it takes, and runs it.

## 3. The Softanza form

I call it a domain language model, and it has two rungs. The first has no neurons at all and was shown in chapter 17: it answers from recorded facts, says why, and refuses outside its domain. The second is a small neural model, optional, which gives it fluency. In the design both rungs end at the same gate; here the gate is the `Admit` of the last block of this section, called by hand.

Where does the training text come from? Build a small knowledge base, render it, and read the corpus and the vocabulary it gives.

```haro
oKB = new stzKnowledgeGraph("restaurant")
oKB.Know("margherita", "dish").
    Know("tiramisu", "dish").
    Know("chianti", "wine").
    KnowRelation("margherita", "contains", "tomato-sauce").
    KnowRelation("margherita", "contains", "mozzarella").
    KnowRelation("margherita", "pairs-with", "chianti")
oDLM = StzDlmQ(oKB)
? @@( oDLM.GenerateCorpus() )
#--> [ "margherita is a dish.", "tiramisu is a dish.", "chianti is a wine.", "margherita contains tomato-sauce.", "margherita contains mozzarella.", "margherita pairs-with chianti." ]
? @@( oDLM.Tokenizer() )
#--> [ "<unk>", "margherita", "tiramisu", "chianti", "dish", "wine", "contains", "pairs-with", "is", "a", "tomato-sauce", "mozzarella" ]
? @@( oDLM.Tokenize("margherita contains something-new") )
#--> [ 2, 7, 1 ]
```

> run: kept

No one wrote that corpus: each of its six sentences is a fact of the knowledge base, rendered. The vocabulary is closed, every word the domain holds with a first entry for the unknown. Twelve entries, and `something-new`, a word outside the domain, maps to the first one: `[ 2, 7, 1 ]`. "Correct by construction" holds here in the one sense the code gives it: each sentence is a recorded fact. It does not yet hold in the sense the design intended; section 7 says where.

Completion is constrained to the domain. What does the model offer after an entity that bears facts, after a relation, after a fragment, and after a word the domain does not hold? Run it:

```haro
? @@( oDLM.Complete("margherita") )
#--> [ "contains", "pairs-with" ]
? @@( oDLM.Complete("contains") )
#--> [ "tomato-sauce", "mozzarella" ]
? @@( oDLM.Complete("tira") )
#--> [ "tiramisu" ]
? @@( oDLM.Complete("pizza") )
#--> [ ]
```

> run: kept

After an entity that bears facts, its relations: `[ "contains", "pairs-with" ]`. After a relation, only its objects: `[ "tomato-sauce", "mozzarella" ]`. A fragment completes to entities, and a word that the domain does not hold completes to nothing: `[ ]`. The guard that proves this calls it "the grammar spirit". It is a lookup in the facts, not decoding under a compiled grammar. And it sees one word, not the sentence so far: `Complete("contains")` returns the objects of every `contains` fact, whatever its subject.

The grammar itself can be derived from the knowledge base, and here the reader of this book has to write the derivation. There is no call in the library that turns a knowledge base into a grammar, and the design lists it as the first rung's task. But the pieces compose. The domain's vocabulary becomes the choices of a schema from chapter 11, the schema compiles to a grammar, and the grammar has no path for a word outside the domain:

```haro
aLex = oDLM.Lexicon()
acObjects = []
for aFact in oKB.Facts()
	if aFact[2] != "is-a" and find(acObjects, aFact[3]) = 0
		acObjects + aFact[3]
	ok
next
oS = StzOutputSchemaQ([
	[ :field = "subject",  :type = :oneof, :choices = aLex[:entities] ],
	[ :field = "relation", :type = :oneof, :choices = aLex[:relations] ],
	[ :field = "object",   :type = :oneof, :choices = acObjects ]
])
? oS.ToGBNF()
#--> root ::= subject-line relation-line object-line
#    subject-line ::= "subject: " ("margherita" | "tiramisu" | "chianti") "\n"
#    relation-line ::= "relation: " ("contains" | "pairs-with") "\n"
#    object-line ::= "object: " ("tomato-sauce" | "mozzarella" | "chianti") "\n"
#    text ::= [^\n]+
#    number ::= "-"? [0-9]+ ("." [0-9]+)?
#    boolean ::= ("yes" | "no" | "true" | "false")
cGood = "subject: margherita" + nl + "relation: contains" + nl + "object: mozzarella" + nl
cOut  = "subject: pizza" + nl + "relation: contains" + nl + "object: mozzarella" + nl
cLie  = "subject: tiramisu" + nl + "relation: contains" + nl + "object: mozzarella" + nl
? oS.Accepts(cGood)
#--> 1
? oS.Accepts(cOut)
#--> 0
? oS.Accepts(cLie)
#--> 1
? oDLM.Ask("tiramisu contains what?")
#--> I hold no 'contains' knowledge about 'tiramisu'.
```

> run: kept

Look at the last four lines together. The grammar accepts the lie! It has the right shape, and every word is in the domain. Asked what a tiramisu contains, the model answers: `I hold no 'contains' knowledge about 'tiramisu'.` A grammar is a gate for shape; the truth belongs to the graph.

A domain language model is a file that travels. It is saved as plain text, readable and diff-able, with no binary and no weights. Can a second model that has never seen the knowledge base answer from it, and run its own tests? Save it, read it back, and load it:

```haro
oDLM.AddGolden("what is margherita", "Margherita is a dish.")
oDLM.AddGolden("what is the weather today?",
	"That is outside the 'restaurant' domain (I know 3 entities and 2 relations).")
cFile = oDLM.Save("probe_dlm")
? cFile
#--> probe_dlm.zdlm
? read(cFile)
#--> dlm "restaurant"
#    entities
#        margherita | dish
#        tiramisu | dish
#        chianti | wine
#    relations
#        contains
#        pairs-with
#    facts
#        margherita | contains | tomato-sauce
#        margherita | contains | mozzarella
#        margherita | pairs-with | chianti
#    laws
#    goldens
#        what is margherita | Margherita is a dish.
#        what is the weather today? | That is outside the 'restaurant' domain (I know 3 entities and 2 relations).
oShipped = StzDlmQ("")
oShipped.LoadFrom(cFile)
? oShipped.Ask("what is tiramisu")
#--> Tiramisu is a dish.
? @@( oShipped.RunGoldens() )
#--> [ [ "total", 2 ], [ "passed", 2 ], [ "failed", [ ] ] ]
remove(cFile)
? fexists(cFile)
#--> 0
```

> run: kept (touches files)

The second model answers: `Tiramisu is a dish.` The refusal travels with the bundle as a golden test, and the model that has never seen the graph passes it too! The laws section is empty because no law was declared before the model was forged; declare that a relation is unique, forge again, and the line appears.

Now the second rung. It is a small neural model trained on the corpus you saw, with no teacher, and it can be exported as a model file. How small is it, and does it learn?

```haro
oDLM.TrainNeuralRung(500)
? oDLM.NeuralWhy()
#--> neural bigram rung: 15 pairs over a 12-word vocab; trained 500 epoch(s), lr 0.50: loss 2.57 -> 0.70
? oDLM.NextToken("is")
#--> a
? oDLM.NextTokenConfidence("is")
#--> 1.00
cGguf = oDLM.ExportNeuralGguf("probe_bigram")
? cGguf
#--> probe_bigram.gguf
? StzEngineNeuralGgufInspect(cGguf)
#--> 2
remove(cGguf)
```

> run: kept (touches files)

It is small: a single layer that predicts the next word from the previous one, `15 pairs over a 12-word vocab`. And it learns: `loss 2.57 -> 0.70`. The library inspects the exported file and prints `2`, the two tensors it holds, a weight and a bias. I do not claim another runtime loads it as a text generator. It trains in a fraction of a second, offline, and gives the same numbers on every run.

What does a model like this say? It is fluent in the grammar of the domain, and it is wrong about facts. That is the reason for the gate:

```haro
aCorpus = oDLM.GenerateCorpus()
for cSeed in [ "tiramisu", "chianti", "margherita" ]
	cSaid = oDLM.NeuralGenerate(cSeed, 3)
	? cSaid + "  ->  " + ( find(aCorpus, cSaid + ".") > 0 )
next
#--> tiramisu is a wine  ->  0
#    chianti is a wine  ->  1
#    margherita contains mozzarella is  ->  0
```

> run: kept

"Tiramisu is a wine" is false, because tiramisu is a dish. "Chianti is a wine" is true. And "margherita contains mozzarella is" is a run-on, because the bigram has no word that ends a sentence. The test against the corpus is a crude gate, and it would refuse a true fact nobody recorded. The real gate is the graph and its laws. What does the graph answer when the false sentence is proposed to it as a fact? Declare the law, then propose:

```haro
oKB.ConstrainRelation("is-a", :Unique)
aVerdict = oKB.Admit("tiramisu", "is-a", "wine", [ :source = "rung 2" ])
? aVerdict[:admitted]
#--> 0
? aVerdict[:why]
#--> 'tiramisu' already bears 'is-a' (to 'dish'); the relation is :Unique
? @@( oKB.Contradictions() )
#--> [ [ [ "subject", "tiramisu" ], [ "relation", "is-a" ], [ "existing", "dish" ], [ "attempted", "wine" ], [ "source", "rung 2" ] ] ]
? oKB.Admit("pizza", "is-a", "dish", [ :source = "rung 2" ])[:why]
#--> admitted: 'pizza' is-a 'dish'
```

> run: kept

The graph refused the false proposal! It says why: `'tiramisu' already bears 'is-a' (to 'dish'); the relation is :Unique`. The refusal is kept, with its source: the model's second rung. A new fact is admitted. That is the whole of the principle in six calls: a proposal, a law, a refusal with its why, and the refusal on the record.

The design describes the unit of prediction in three levels. A token is a fragment with no type. An embedding is a vector without a role. And a chunk is a typed node of a graph, with a tag, a payload and edges: a declaration, a relationship, a constraint. A chunk is validated in five stages before it enters the graph: type, pattern, graph integrity, compliance, and constructive contribution. I tell it as design, because there is no chunk in the library. What exists are pieces: the court of chapter 11 checks a text's type and shape; and the admission above enforces a law, which is compliance. Nothing chains them.

## 4. The decision, and what I refused

On 13 July 2026, I ruled on this. The concept of a domain language model had been designed for one of the estate's products. I donated it to the open foundation, so that any Softanza project that supplies a knowledge base can ship its own model free to the users of its domain. The format is `.zdlm`. The first rung is in every model; the second is optional fluency. The record holds the ruling that a model is free to ship, and no licence text. I tell "free" as the ruling's word: a plain file, in the open foundation, with no licence fee or meter.

**I refused the token as the unit.** The unit is a chunk of the world, which a graph can admit or refuse.

**I refused a teacher I cannot see.** The earlier design of the idea used a large commercial model to write its training corpus. I put a law against it, and this model's corpus is rendered from the domain's own facts: the library's second law says a capability never requires anything paid or remote.

**I refused neural first.** The finding I start from is that the canonical model is not neural. A review of the earlier product archived a transformer of one to three billion parameters, in favour of rule-based prediction. Its ground was that hallucination is impossible when the model cannot generate almost-valid text. So the first rung has zero training and zero cost, and the neural rung comes second.

**I refused to let the shape stand for the truth.** The grammar says structure kills malformedness, not falsehood. The truth belongs to the graph, to its laws, and to a person.

Section 5 says what the court proves of this.

## 5. The court

`dlm_narrated` proves the model forged from a graph, its answers with their why, its refusal outside the domain and the completion. It proves also the plain-text bundle with its goldens, the closed tokenizer and the second rung with its model file. One of its assertions on the second rung checks only that the generated sentence begins with a fixed prefix, so it would also pass the false sentence above. `structuredoutput_narrated`, `schema_grammar_narrated` and `constrained_decoding_narrated` prove the court of chapter 11, the grammar compiler and the sampler. The last of them has two scenes that need a generative model file, which the snapshot does not hold; the record counts 50 assertions in that guard. `knowledge_integration_narrated` proves derivation and the refusal by a law. The admission I show in the last block is not called by its name in any guard. It is reached through the conversation, and by the strict form of adding a fact, in which a fact added without its admission is refused. That much the guard does assert.

Section 6 asks where the field leads, and where this model stands.

## 6. The field, and where it leads

The field leads in scale. Training and serving models of every size is a mature practice. This second rung is a single layer over twelve words, and the steps that would make it more, a validated corpus, deduplication, a trained tokenizer, a larger network, quantisation, are not done. I do not compete with large models.

The field leads in fluency, which is the point of a model. A first rung that answers from facts will say "I hold no 'contains' knowledge about 'tiramisu'." where a general model would write something plausible, and for a customer the plausible thing is often more useful. The record's own answer is the second rung, and its present state is the one section 7 gives.

Where I think this stands apart is in what the output is. A general model's answer is text, and every check on it is after the fact. Here every answer of the first rung carries its why and a certainty of one. Every proposal of the second can be put to a gate, and the gate can refuse it with a reason. A model that can only say what the domain holds, and a gate that remembers what it refused: that is what a bank, a ministry or a school can sign. I hold that as a view, not a result.

Section 7 says what is built, what is designed and what is absent.

## 7. The limit

What is built: the first rung and its answers; the facts rendered as a corpus, with a closed vocabulary; completion by lookup; and the bundle that travels with its tests. Also built: a second rung that trains in a fraction of a second and exports a small model file, and the admission of a fact by a law.

What is designed comes in four points, and the page must say each.

- The grammar derived from a knowledge base by one call. Chapter 19's composition is the reader's, not the library's.
- The second rung's corpus validated by the first rung's grammar before it is admitted. The design says so; the code renders the facts directly, with no such check. So "correct by construction" holds for the training text, and not for what the model says.
- The five-stage validation of a chunk. None exists as a pipeline.
- The foundry's steps beyond the bigram.

What is absent: an end-of-sentence word for the second rung, which is why one of its sentences runs on. Absent too is a completion that sees the sentence so far; that is why a completion after a relation lists the objects of every fact of that relation. The first rung also answers a rephrased question with the type, as chapter 17 showed, where the law of this part says it should refuse.

## 8. Six doors

**The programmer.** A model is a file you can read, diff and test: its facts, its laws and its goldens.

**The analyst.** A fact you add makes the model know more, and a law you add makes the graph refuse more, with no training; the model's own answers do not read it yet.

**The designer.** The model's refusal is part of its contract: the golden test says what it must decline to answer.

**The decision-maker.** The model can only say what the domain holds, and the gate keeps the record of what it refused and why.

**The educator.** Rung one is a model a learner can read in full. Rung two is small enough to train in front of a class.

**The agent.** What you propose is a fact the graph can admit or refuse, with a reason you can read.

## 9. Exercise

Forge a domain of your own with three entities and two relations. Before you run anything, write what you expect from three calls. They are the completion of an entity, the completion of a relation, and the answer to a question about a thing the domain does not hold. Then declare that one relation is unique and propose, in the form of a fact, something that contradicts it.

Run it. Then write a sentence of the right shape and the wrong truth, and say which of the grammar and the graph refuses it, and which does not.

Chapter 20 turns from what a model says to what an agent does. Its title is *Agents that cannot hurt you*, and its principle is this: do not build safe agents; build a safe world, and let ordinary agents loose inside it.
