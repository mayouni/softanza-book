# Knowledge programming

Source: Chapter 14. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: a system as a plain text file of facts, with laws (unique, transitive, symmetric) and the source of each fact; Prove with its steps, a no as certain as a yes; strict mode; the file written, read back and shipped, from a course catalogue to an agent's memory; designed: rules in the file; derivation on any graph; a query that joins; several relations between two things; class inheritance; validation on load; absent: the 2022 founding dialog, which does not run; Explain on a knowledge graph; the rules section of the file, which the reader skips

Run: 13 of 13 blocks kept their promise, on 2026-10-14 01:35 UTC+01:00.

In this chapter I take the three practices of the field that meet in this idea, the semantic stack, the property-graph database and rules over facts, and set beside them a system that is a plain text file. I run that file: two facts, one law and a proof with its steps, then a clinic in strict mode, where a refused rumour is kept and named. I write the file, read it back and show it at scale, from a course catalogue to an agent's memory. I say what I decided, that a business describes itself in one file and that the file is the program. I say what I refused: a parallel world, a contradiction resolved in silence, retrieval. I print the limit, a file that at this commit has no rules. It stands beside the principle: a system is a file, and adding a line to it makes the system know more, and nothing is coded or trained.

## 1. The concept, as the field holds it

Three practices of the field meet in this idea, and none of them is the same as it.

The first is the semantic stack: RDF, OWL and SPARQL. A fact is a triple of subject, predicate and object, written in a shared vocabulary. An ontology says what classes and properties exist and what follows from them, and a reasoner derives the consequences. These are W3C recommendations, of 2014, 2009 and 2013. What the field asks of the author of a knowledge base is an ontology language of their own, a store and a query language. They usually stand beside the application and not in it.

The second is the property-graph database, with its query language. The record has one comparison that sets such databases against this library. It is a model's text kept in the library, and it credits the field with scale, persistence and transactions.

The third is rules over facts, in Prolog and in Datalog. Facts and rules in one program, a query by resolution. The record names Prolog only, as a language to reach, and not to rebuild.

A fourth practice stands behind the contrast, and the design document names it only to refuse it. It is retrieval, a pile of document fragments searched by similarity. (General knowledge, not a study of the record.)

So in the field the knowledge lives in a store and its logic in a reasoner, both beside the program. Here the knowledge is a plain text file that the program loads.

## 2. The first principle

**A system is a file. Adding a line to it makes the system know more, and nothing is coded or trained.**

Two sentences of the record carry it. The definition, in the design document written from my directive of 13 July 2026: intelligence is the computational ability to derive new knowledge from existing knowledge. And what the 2026 vision keeps from it: adding one fact augments the system's intelligence, with no code change and no training. Chapter 17 opened on the first, and I open here on the second. The design document of 13 July 2026 already says it, in nearly the same words, and the chapter keeps its opening.

Now the form itself, a text and what it does when you run it.

## 3. The Softanza form

Here is a system as a text. Two facts: flour is made from millet, and couscous from flour. Is couscous made from millet? Ask the graph, then add one line to the file, a law saying that *made from* is transitive, and ask again:

```haro
cFacts = 'knowledge "coop"' + nl + nl + "facts" + nl +
         "    flour | made-from | millet" + nl + "    couscous | made-from | flour" + nl
oA = new stzKnowledgeGraph("coop")
oA.ImportKnow(cFacts)
? oA.Prove([ "couscous", "made-from", "millet" ])[:narration]
#--> not derivable: no recorded fact or lawful chain gives 'couscous' made-from 'millet'
oB = new stzKnowledgeGraph("coop")
oB.ImportKnow(cFacts + nl + "ontology" + nl + "    made-from | transitive" + nl)
? oB.Prove([ "couscous", "made-from", "millet" ])[:narration]
#--> proved: couscous made-from flour made-from millet
```

> run: kept

Without the law the graph answers `not derivable`; with it, `proved: couscous made-from flour made-from millet`. The text is the program. The same two facts, one extra line, a different capability. The block does not touch the disk: `ImportKnow` takes a text, and takes a path when the string ends in the file's extension.

Now add a fact to the graph with the law, and nothing else. What do the two graphs answer to the longer question? Run it:

```haro
oB.KnowRelation("porridge", "made-from", "couscous")
? oB.Prove([ "porridge", "made-from", "millet" ])[:narration]
#--> proved: porridge made-from couscous made-from flour made-from millet
? oA.Prove([ "porridge", "made-from", "millet" ])[:narration]
#--> not derivable: no recorded fact or lawful chain gives 'porridge' made-from 'millet'
```

> run: kept

The graph with the law proves the longer chain and writes its steps out: `proved: porridge made-from couscous made-from flour made-from millet`. The graph without the law, which also never received the fact, still answers `not derivable: no recorded fact or lawful chain gives 'porridge' made-from 'millet'`, and I want you to notice that this no has two causes, named in its own line: no recorded fact, and no lawful chain. A refusal is as certain as a proof, about what is recorded and declared: the graph says "not derivable", not "false". The library's comment on `Prove` says it: `a certain no is still certain`.

The same growth reaches the domain model of chapter 19. Nothing is trained. But a model forged from a graph is a snapshot. Does the model learn the new fact when the graph does? Run it:

```haro
oKB = new stzKnowledgeGraph("coop")
oKB.Know("couscous", "dish").KnowRelation("couscous", "contains", "semolina")
oDLM = StzDlmQ(oKB)
? oDLM.Ask("what is millet?")
#--> That is outside the 'coop' domain (I know 1 entities and 1 relations).
oKB.Know("millet", "grain").KnowRelation("couscous", "contains", "millet")
? oDLM.Ask("what is millet?")
#--> That is outside the 'coop' domain (I know 1 entities and 1 relations).
oDLM = StzDlmQ(oKB)
? oDLM.Ask("what is millet?")
#--> Millet is a grain.
? oDLM.Ask("couscous contains what?")
#--> Couscous contains semolina and millet.
```

> run: kept

It does not. The second answer is the old model still refusing, `That is outside the 'coop' domain`, and only the model forged again answers `Millet is a grain.`

**The file the library writes.** A clinic. A relation declared unique, and a graph in strict mode, where every fact needs its provenance. What does it do with a fact that has no source, with one that has, and with a second, contradicting one from a rumour? And what does it then write to the disk? Run it:

```haro
oCl = new stzKnowledgeGraph("clinic")
oCl.ConstrainRelation("treated-by", :Unique)
oCl.EnableStrictMode()
try
	oCl.AddFact("fatou", "treated-by", "dr-diallo")
catch
	? cCatchError
done
#--> Strict mode: every fact needs provenance -- use AddFactXT(s, p, o, [ :source = ..., :confidence = ... ]).
oCl.AddFactXT("fatou", "treated-by", "dr-diallo", [ :source = "registry", :confidence = 0.95 ])
? oCl.AddFactXT("fatou", "treated-by", "dr-sani", [ :source = "rumour", :confidence = 0.2 ])
#--> 0
oCl.WriteToKnowFile("clinic")
? read("clinic.zknw")
#--> knowledge "clinic"
#
#    facts
#        fatou | treated-by | dr-diallo
#
#    provenance
#        fatou | treated-by | dr-diallo | source | text | registry
#        fatou | treated-by | dr-diallo | confidence | number | 0.95
#
#    contradictions
#        fatou | treated-by | dr-diallo | dr-sani | rumour
#
#    ontology
#        treated-by | unique
```

> run: kept (touches files)

The naked fact is refused with the library's own sentence, `Strict mode: every fact needs provenance`. The fact with its source and confidence is admitted. The rumour is refused, `0`, and the refusal is kept! That is what the library writes, a header and up to four sections. They come in this order: the facts, the provenance when a fact carries any, the contradictions when one was refused, and the ontology when a law was declared. One line per record, fields separated by a bar. A bar or a line break inside a value is escaped. The refused rumour sits in the file, named, and never resolved. The code comment on the contradiction list says it: `named, NEVER silently resolved`.

Does the file read back into a strict graph, with the law, the source of every fact and the refusal inside it? Load it:

```haro
oBack = new stzKnowledgeGraph("clinic")
oBack.EnableStrictMode()
aR = oBack.ImportKnow("clinic.zknw")
? aR[:merged]
#--> 1
? @@( oBack.MetaOfFact("fatou", "treated-by", "dr-diallo") )
#--> [ [ "source", "registry" ], [ "confidence", 0.95 ] ]
? len(oBack.Contradictions())
#--> 1
? oBack.RelationHasLaw("treated-by", "unique")
#--> 1
remove("clinic.zknw")
? fexists("clinic.zknw")
#--> 0
```

> run: kept (touches files)

It does: one fact merged, the source and the confidence back, `[ [ "source", "registry" ], [ "confidence", 0.95 ] ]`, one contradiction, and the law. A file of this kind was once written without its provenance. The export wrote only the bare triples, so knowledge read back from the disk no longer said where it came from. A strict graph could not load its own export. The fix is the two sections above. The guard that proves it is named in section 5.

**A law that fires when a fact is added.** On the library's default world, the one behind the natural-language sugar, a symmetric law derives the reverse fact as the first one is added, with no call to a derivation step. Nobody wrote that Ibrahim is married to Amina. Does the default world know it?

```haro
StzConstrainRelation("married-to", :Symmetric)
StzKnowRelation("amina", "married-to", "ibrahim")
? DefaultKnowledgeGraph().Query([ "ibrahim", "married-to", "amina" ])
#--> 1
```

> run: kept

It answers `1`. The reverse fact is there, and nobody wrote it! This is the only place where a declared law fires on add that a run in this book shows, and it is the default world. The graph class also has a switch, `EnableAutoDerive`, that runs the derivation rules after every edge added; it is off by default, and I did not run it. I show the same law on an instance graph in section 7, where it does not.

**A system at scale.** The education program of the library is a knowledge file. Its catalogue, `program.zknw`, says what the program is called and which courses and languages it has. What is its name, and which languages does it carry? Ask it:

```haro
oP = StzProgramQ("../../education/program")
? oP.Id()
#--> softanza-education
? @@( oP.Languages() )
#--> [ "en", "fr", "ar", "ha" ]
```

> run: kept

It is called `softanza-education`, and it has four languages. Adding a course is adding a line there, and the guard checks that every declared course is a folder and every folder is declared. In the education module the snapshot holds ninety-nine knowledge files, counted with `find` on 8 October 2026. They are courses, exercises, worlds and skills, a project world for a learner, and the overlays an institution lays over the core. An agent's memory is also a knowledge graph, saved through the same format, with provenance.

That is the form. Now what I decided, and what I refused.

## 4. The decision, and what I refused

**I decided that a business describes itself in one file, and that the file is the program.** The design document records my directive: entities, relations, an ontology of domain-specific semantics, and rules, in a file that is readable, diffable and hand-editable, validated on load. The last two words I have not yet met, and section 7 says where.

**I decided on four-letter extensions.** `.zknw` for knowledge, and the others of the family; the old spellings still read. The snapshot writes `.zknw` and still reads `.stzknow`. The file of rules was not renamed: the graph still writes and reads `.stzrulz`, though the family names four letters for it. I report it as the record has it.

**I refused a parallel world.** The natural layer once held its entities in globals, and the design document called it the wrong home, the wrong shape and a parallel world. The resolution is one default graph standing behind the natural-language sugar. The old globals still exist, and the graph grows beside them: the library's header calls it a dual write. The law behind it is that naked domain globals are forbidden; a global form may exist only as thin sugar over one default instance. So the dialog of the symmetric law above is sugar over a graph of the same class as the first blocks used.

**I refused to resolve a contradiction in silence.** Strict mode, where every fact needs its provenance, is opt-in knowledge hygiene.

**I refused retrieval.** The design document says: no code change, no training, no RAG machinery. It is the same refusal as chapter 17's.

## 5. The court

`knowledge_integration_narrated` proves that the world answers `WhatIs`, that the graph grew alongside it, and that the law lives in the ontology. It proves that `Prove` narrates the law first and then the links of the chain, with certainty 1, and refuses what it cannot prove. It proves that the file round-trips. It proves that a symmetric law derives the reverse edge when the derivation step is applied after a fact is added through the graph. Last, it proves that strict mode admits a provenanced fact, refuses a naked one, and refuses and records a unique contradiction.

`provenance_survives_save_narrated` proves that a fact's source and confidence survive a save, that a strict graph loads its own export, and that a refused contradiction survives. It proves that a bar or a line break in a value is data, and that an old file with no provenance still loads. It proves that an agent's memory records who learned a fact, and when.

`program_narrated` proves that the program counts its courses, and that every course declared is a folder and every folder is declared. It proves that the texts read the same from a checkout with other line endings.

That is what the guards prove. What the field does better comes next.

## 6. The field, and where it leads

The record's own graph comparison says where the traditional solutions win: large-scale systems that need distributed storage and processing, and performance-critical applications. Its table puts Softanza at business scale, in the hundreds to thousands of nodes, in a single process. That is the fair summary of the loss: the field leads in scale, persistence, transactions and tooling. (The comparison's row for persistence predates the file; the knowledge graph now writes one.)

The field leads in standards and reach, in general knowledge. A knowledge base in RDF can be shared with any tool that reads the W3C formats, linked to public vocabularies and queried across stores. As far as the record shows, a knowledge file is read by this library and by nothing else. A reasoner for a rich ontology language does what three laws and a class declaration do not. The field leads in the expressiveness of rules: Prolog and Datalog derive new facts from arbitrary rules. Here, in the runs I kept, one law derives a fact, and only on the default world. The field leads in multi-step queries, since SPARQL and Cypher join patterns. And in many relations between two things.

Here is where I think this stands apart, with the measured limits beside it. The knowledge is a text file a person can read, edit, diff and ship with the program. Every answer is provable with its steps, and a no is as certain as a yes. What a fact claims travels with its source and its refusals. And the same format carries a course, a learner's project and an agent's memory. None of that needs a store, a server, a model or a training run.

The losses are printed. The limit of the chapter comes next, with its runs.

## 7. The limit

The limit of this chapter is the one the structure line already carries: *entities, relations, an ontology, rules*. The file at this commit has no rules. Here is the file with a rules section. What does the reader make of it?

```haro
cRules = 'knowledge "pairs"' + nl + nl + "facts" + nl + "    margherita | pairs-with | chianti" + nl + nl +
         "rules" + nl + "    pairs-with | symmetric" + nl
oRul = new stzKnowledgeGraph("pairs")
aM = oRul.ImportKnow(cRules)
? aM[:merged]
#--> 1
? len(oRul.Ontology())
#--> 0
```

> run: kept

The file merges, `1`, and the ontology is empty, `0`. The parser recognises the header `rules`, and has a handler for none of the lines under it. They are dropped: the ontology holds `0`, and no refusal comes back. The same law under the header `ontology` gives an ontology of length 1. Rules live elsewhere, as data in a rule attached to a graph, which are chapters 29 and 30, and in a separate file that names rule functions. In this file there are facts and laws. I print "facts and laws", and I send the rules to those two chapters. The single file that holds rules, which the design promises, is not there, and section 7 prints the gap as the chapter's limit.

The law is also not derived on an instance graph. Take the same symmetric law and the same fact as on the default world. Is the reverse there?

```haro
oSy = new stzKnowledgeGraph("pairs")
oSy.ConstrainRelation("pairs-with", :Symmetric)
oSy.KnowRelation("margherita", "pairs-with", "chianti")
? oSy.RelationHasLaw("pairs-with", "symmetric")
#--> 1
? oSy.Query([ "chianti", "pairs-with", "margherita" ])
#--> 0
```

> run: kept

The law is recorded, `1`, and the reverse edge is not there, `0`! The class header says it: `only :unique and :transitive are acted on here`; symmetric is only recorded. Four more limits, each with its run.

**One relation between two things.** The graph stores one edge per node pair. Does it admit a second relation between the same two entities, `amina` and `bread`? Run it:

```haro
oShop = new stzKnowledgeGraph("shop")
oShop.KnowRelation("amina", "sells", "bread")
aV = oShop.Admit("amina", "buys", "bread", [ :source = "till" ])
? aV[:admitted]
#--> 0
? aV[:why]
#--> Can't add fact: 'amina' and 'bread' already carry the edge 'sells' (stzGraph stores one edge per node pair).
```

> run: kept

The second relation is refused, `0`, with the library's own sentence, `Can't add fact: 'amina' and 'bread' already carry the edge 'sells' (stzGraph stores one edge per node pair)`. A knowledge model that cannot hold *sells* and *buys* between the same two entities is a real limit. The code says it: `known limitation, revisit with multi-edge support`.

**A two-step question answers only its first step.** Does `QueryPath` follow its second pattern, and can the predicate of a query be a variable? Run it:

```haro
oQ = new stzKnowledgeGraph("coop2")
oQ.KnowRelation("amina", "sells", "couscous").KnowRelation("couscous", "made-from", "flour")
? @@( oQ.QueryPath([ [ "amina", "sells", "?p" ], [ "?p", "made-from", "?m" ] ]) )
#--> [ "couscous" ]
? @@( oQ.Query([ "amina", "?p", "?o" ]) )
#--> [ ]
```

> run: kept

The path answers `[ "couscous" ]`, the first step and nothing more: `QueryPath` ignores the rest of its patterns, so it is no multi-step query yet. The variable predicate answers `[ ]`.

**A line that is not a fact.** Four lines, three of them not facts: two fields, four fields, and no bars. What does the reader refuse?

```haro
cBad = 'knowledge "t"' + nl + nl + "facts" + nl + "    a | likes | b" + nl + "    c | likes" + nl +
       "    d | likes | e | f" + nl + "    g likes h" + nl
oT = new stzKnowledgeGraph("t")
aBad = oT.ImportKnow(cBad)
? aBad[:merged]
#--> 1
? @@(aBad[:refused])
#--> [ ]
```

> run: kept

Nothing. The file merges, `1`, and the refused list is `[ ]`; the reader is silent and the three lines vanish! The design document promises that the file is "validated on load". At this commit the parser keeps only a line with exactly three fields.

**The 2022 founding dialog.** The narration tells knowledge programming through a dialog: an apple as a fruit and as a company, an owner, relations asked as questions. At this commit its first line does not run. The text, which I show and do not run, is `@Q("Apple").IsA(:Fruit)`. On 8 October 2026 it stopped with `Calling Function without definition: @isfruit`; I did not keep that run as a block. The string class reads the predicate as natural language and looks for a function by that name. Two other forms stop elsewhere. The narration's promise lines are stale. The nearest form that runs keeps the point. Does the world know one name with two meanings?

```haro
StzKnow(:Apple, :Company)
StzKnow(:Apple, :Fruit)
? @@( WhatIs(:Apple) )
#--> [ "company", "fruit" ]
```

> run: kept

It knows both: `[ "company", "fruit" ]`.

The study of the record already says the dialog was kept at the margin, and that the centre moved to the file. The chapter keeps the file as its opening, and the 2022 dialog stays at the margin.

What is designed: rules in the file; derivation on any graph; a multi-step query; several relations between two things; class inheritance. `DefineClass` writes a fact, and no inheritance follows. The nearest that ran, in an earlier probe whose run I did not keep, is to declare `is-a` transitive and state the class as a fact of that relation. And the design's knowledge hygiene beyond provenance, bounded queries, scoped graphs and revision with rollback, has no method of that name.

What is absent or broken: `Explain()` on a knowledge graph, which calls `ApplyInference`, a function defined nowhere. And `ValidateOntology()`, which returns 1 whatever the ontology holds, as its own comment says, `known defect`.

One note on the design document's history. Its amendment of 22 August 2026 says that no knowledge file exists anywhere in the tree, and that this is hygiene and not a gap. At this commit that is no longer true: there are ninety-nine, all of them in the education module.

That is the limit, printed. Now the six doors.

## 8. Six doors

**The programmer.** One class and a text file: `Know`, `KnowRelation`, `ConstrainRelation`, `Prove`, `Query`, `WriteToKnowFile`, `ImportKnow`. The file is diffable and ships with the program.

**The analyst.** The offering page names it: what you declare is your organisation's entities, rules and flows, in a plain-text knowledge file. Read "rules" as the limit above. Where to start, in the course: the chapter called "Teach a world".

**The designer.** The record is silent. Neither the offering page nor the study ties the knowledge file to the designer's door, and I do not invent one.

**The decision-maker.** The file is plain text that a manager can read. Every fact can carry a source and a confidence. A refused claim is kept, named and never resolved. An answer comes with its proof, and a no is certain. The design's second law says no capability may require anything paid or remote. I did not run the file offline.

**The educator.** The whole education program is knowledge files. A learner teaches a world, then questions it, and the project's guard checks the world file, the agent file and one printed answer. An institution adapts by overlay, never by fork.

**The agent.** Your memory is a knowledge graph with provenance, and your world is a file you load and query.

## 9. Exercise

Here is a world with two facts, and a question it cannot answer yet. Your promise is the line proving that class 3b is part of primary, with the chain written out. Change the world, and not the question.

```haro exercise
cWorld = 'knowledge "school"' + nl + nl + "facts" + nl +
         "    class-3b | part-of | grade-3" + nl +
         "    grade-3 | part-of | primary" + nl
oW = new stzKnowledgeGraph("school")
oW.ImportKnow(cWorld)
? oW.Prove([ "class-3b", "part-of", "primary" ])[:narration]
# this prints a refusal. Your promise: the line proving that class-3b is part of primary,
# with the chain written out. Change the world, not the question.
```

> run: exercise

Run it and see what prints. If you change the question to ask about grade 3, it will prove something, and it will not be the line you promised. Then ask the reverse question, whether primary is part of class 3b, once your world has its law, and see whether the law adds a fact in the wrong direction. I do not tell you the line to add.

I left this one in your hands. Section 7 runs a file of four lines, three of them not facts, and prints what the reader says about them. Here is that file again with one change: it also asks the graph about three of the lines, and I print none of the answers.

```haro exercise
cBad = 'knowledge "t"' + nl + nl + "facts" + nl + "    a | likes | b" + nl + "    c | likes" + nl +
       "    d | likes | e | f" + nl + "    g likes h" + nl
oT = new stzKnowledgeGraph("t")
aBad = oT.ImportKnow(cBad)
? aBad[:merged]
? @@(aBad[:refused])
? oT.Query([ "a", "likes", "b" ])
? oT.Query([ "d", "likes", "e" ])
? oT.Query([ "g", "likes", "h" ])
```

> run: exercise

Run it. Read `merged`, read `refused`, read the three queries, and find which lines the graph holds and what the reader told you about the others. Set the design document's promise of a file "validated on load", in section 4, beside what you find; section 7 says what the parser keeps. I do not give you the answer, and I did not fix the reader. When you have it, you will know why a file that merges is not a file that was validated.

The next chapter is about pattern languages: a pattern is a rule about the shape of data, written as data, and the same habit serves data of every kind. Here a law about a relation was a line in a file; there the rule is about the shape of the data itself.
