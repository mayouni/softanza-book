---
id: the-software-crafter
part: 1
number: 2
title: The software crafter
spine: true
narrations: [stz-built-on-real-world-need.md, stz-service-virtualization-code-first-subscribe-later.md, stz-agents-that-cannot-hurt-you-narration.md, stz-rules-as-graph-rules-narration.md, stzOrgChartDoc-BankUseCase.md]
site: [offering, customers, forged, coding-agents]
guards: [agentfile_narrated, service_registry_narrated, graphrule_object_narrated, semantic_resolver_narrated, 00_orgchart_narrated]
stage:
  built: "the agent file and its court; the registry that refuses a fake in production; rules as data on a model; a regulator's rules judging an organisation chart; the natural layer in Hausa and Arabic"
  designed: "a guard that fails when a step of a journey page breaks, each step run in order; the door through which a coding agent asks the library to judge its work"
  absent: "the platforms of the three customers running on the Softanza engine; a crafter's own medium, the messaging app on their phone, as a target"
status: draft
rulings: ["12.2", "12.12", "12.13", "12.25", "12.29", "12.30"]
research: research/ch02.md
---

In this chapter I take the word "crafter" from the field's craftsmanship and from its two answers that define the person by a tool, low-code and the coding agent. I say what the site means by it. I show the six doors, each with a line or two that run, and the three cases this book is for: a restaurateur in Lyon, a bank in Niamey, an organisation in the field. I say what I kept, the programmer first; what I added, the agent, with one power withheld; and what I refused, "maker" and "builder". The principle is one sentence that joins the site's and the glossary's: a crafter is whoever declares what they know about a world, and owns what they declare.

## 1. The concept, as the field holds it

The field already has a word for programmers who care about their work: craftsmanship. A book of 2001 gave the idea its name, and a manifesto of 2009 gave it its slogan. Since then "software craftsman" has meant a professional who holds their code to a standard higher than the one the job requires. (General knowledge, not a study of the record.) It is a good movement. It is also a movement of programmers, about programmers' standards.

The field's two other answers to "who makes software, if not programmers" define the person by a tool. The first is low-code: business people building applications on a vendor's visual platform, the "citizen developer" of the analysts. The second is the coding agent: a model that reads files, edits them and runs commands, steered in plain words, with "vibe coding" as the name for keeping whatever it writes. Both answers share a shape. The person is defined by a tool, and the work lives where the tool lives. When the vendor changes its prices or its model, the person's work changes with it. (General knowledge, not a study of the record.)

## 2. The first principle

The site gives the definition in two sentences. They say "crafter" today (read on 9 October 2026); until 8 October they said "maker". The glossary says that a crafter is whoever is declaring, at the moment they declare. The site says that a crafter owns what they make. I ruled on 12 October 2026 that the book keeps both, in one sentence: **a crafter is whoever declares what they know about a world, and owns what they declare: the artefact is theirs, in plain text, and it does not expire.** Skill does not enter the definition. The word "craft" suggests it, and I keep the word: the person is defined by the act and by ownership, not by programming skill. I hold this as a view, not a result.

## 3. The Softanza form

I was the first crafter of Softanza, and not for a reason I would have chosen. My wife runs a music club where people learn to sing classical Arabic songs. Every Sunday morning she sends me the list of songs to prepare, and I search for their lyrics. The lyrics found online repeat every phrase as the singer performed it, and she reminds me, every time, to remove the duplicates. I wrote `RemoveDuplicates()` to stop doing it by hand, and its family is still in the library:

```haro
o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.ContainsDuplicates()
#--> 1
? o1.NumberOfOccurrence("tea")
#--> 3
```

I write about this in an article on what the library was built on: I introduced its features when a real problem asked for them, or when I anticipated they would meet programmers' needs. This one came from a problem: the crafter comes first, and the feature after.

Since 2022, I have presented Softanza not by its anatomy, its modules and classes, but by who you are and what you are trying to do. The 2022 deck had five audiences, each with a recipe of three to five steps. The site today has seven doors (read on 9 October 2026), one per kind of crafter. The seventh, for a team that ships an application, was added that day, and this chapter keeps the six it was drafted with. Each door says what you declare, what you get, and where to start. Here is what each of the six declares, in a line or two that run.

**The programmer** declares intent in a library that reads like a sentence. You have just seen it.

**The analyst** declares the data of a world, and the engine computes the view. Here, three regions of Niger with the population the 2012 census counted:

```haro
o = new stzTable([ [ :region, :population ],
    [ "Agadez", 487620 ], [ "Maradi", 3402094 ], [ "Zinder", 3539764 ] ])
o.Show()
#--> ╭────────┬────────────╮
#    │ Region │ Population │
#    ├────────┼────────────┤
#    │ Agadez │     487620 │
#    │ Maradi │    3402094 │
#    │ Zinder │    3539764 │
#    ╰────────┴────────────╯
```

**The designer** declares a picture as a program, and gets the same picture every time:

```haro
? Q("Softanza").BoxedXT([ :AllCorners = :Round ])
#--> ╭──────────╮
#    │ Softanza │
#    ╰──────────╯
```

**The decision-maker** declares what each actor in the world may do, a person or an agent, and the court enforces it. An agent is a small text file. What does the court say to one that does not say what it covers? In the answer, "law 18" is the engine's rule that an agent with no coverage statement is never scheduled, and `pia` names the format of the file, as its first line shows. Load it:

```haro
cPia = "pia: 1
name: stock-watcher
kind: pi
reversibility: compensable
schedule:
  timer: 20
skills:
  - name: restock
    does: learn stock level ordered
"
oD = StzAgentDeclarationQ(cPia)
? oD.IsValid()
#--> 0
? oD.CiteFindings()
#--> [pia-coverage @ coverage] an agent must say WHAT IT COVERS. The engine loop refuses to schedule an agent with no coverage statement (law 18), so a file without one could never run and is refused here instead of at the first tick.
```

**The educator** declares in the learner's own language. A sentence in Hausa runs; the engine counts the letters of an Arabic word, not its bytes, and knows its script:

```haro
? NaturallyIn("ha", "Yi rubutu dauke 'hello' Maida shi").Result()
#--> HELLO
? Q("سلام").NumberOfChars()
#--> 4
? Q("مرحبا بالعالم").Script()
#--> arabic
```

**The agent** is the sixth crafter, the one 2020 could not draw. It declares itself in the same kind of file, and it is welcome, with one thing withheld. An agent whose mind is a language model may propose; it may not hold an effect. What happens to a file that gives it one? In the answer, a "pi-gate" is the gate where a governed actor commits:

```haro
cLlm = "pia: 1
name: rogue
kind: llm
coverage: proposes a summary
reversibility: reversible
schedule:
  timer: 20
proposes:
  prompt: Summarize {input}
  structure:
    - field: topic
      type: string
skills:
  - name: send
    when: always
    does: propose
    effect: send-email
"
oBad = StzAgentDeclarationQ(cLlm)
? oBad.IsValid()
#--> 0
? oBad.CiteFindings()
#--> [no-llm-effectful @ skills.send.effect] REFUSED: granting 'effectful' to llm actor 'rogue' -- an LLM proposes, only a pi-gate commits (no-llm-effectful, enforced at CONSTRUCTION, not merely audited).
```

The llm actor `rogue` does not get its effect! The court answers `REFUSED`, and says when: `enforced at CONSTRUCTION, not merely audited`.

Now the three cases this book is for. They are not personas. They are people and organisations with documents, and Part VI tells each of them in full. Here, a page each.

**A restaurateur in Lyon.** He owns a couscous restaurant, and the project is a platform for neighbourhood commerce. The project's notes say it plainly: he is not a programmer. The project began with an offer in May 2024 and then two years of rich specification that produced nothing he could use. What came out of that failure is the rule I have worked by since: deliver small, fast and useful, and let the foundations mature in parallel without ever blocking a delivery.

On 4 July 2026 he answered a scoping report in his own words and reversed the order of the work: customer first, restaurateur next, supplier last. The project's architecture was redrawn as a constellation of worlds, using the library's design, and the first amendment closed on 4 August 2026.

A constellation is a graph of worlds. A world is one application; a bond is a declared relation between two worlds, for one named act, and nothing crosses without one. Chapter 23 shows all three run; here it is only the shape the project took.

The project counts eleven iterations and a campaign of twenty-two simulated tests behind its interface rules, and in his own report the speed of ordering is his first, non-negotiable priority. And on 19 August, after a day of tests in the field with two phones and a messaging app, the notes call him the project's co-architect.

Chapter 1 tells the first demonstration as the owner's own, on his own phone, over a messaging app. The record is more exact. Its checklist for the 15 August demonstration plans it for the owner alone, with his own phone and a messaging app as the support line. The measurements he took over a messaging app are those of 19 August.

One of his needs is carried by a law of the library: try payments before paying anyone for an account. What does the registry say to a fake payments service while you rehearse, and what does it say when you go live? Run it:

```haro
oReg = new stzServiceRegistry("restaurant")
oReg.Bind(:payments, new stzPaymentsSandbox())
oReg.SetPhase(:emulated)
? oReg.IsSound()
#--> 1
oReg.SetPhase(:production)
? oReg.IsSound()
#--> 0
? oReg.Findings()[1][:message]
#--> still bound to a SANDBOX in a production phase -- a fake must never ship
```

It answers `1` in the emulated phase and `0` in production, and says why: `still bound to a SANDBOX in a production phase -- a fake must never ship`.

**A bank in Niamey.** A commercial bank under the rules of the central bank of the West African monetary union has an organisation-assessment product I built beside the library, installed under licence on its own internal network. The installation guide delivered to the bank is the document that attests it. The lesson it left in the library is that an organisation can be judged by its own chart, under a regulator's rules. Declare a chart with a chief executive and an internal audit that reports to him, and the regulator's rules answer:

```haro
oOrg = new stzOrgChart("bank")
oOrg.AddPositionXTT("ceo", "Chief Executive", [ :department = "executive" ])
oOrg.AddPositionXTT("audit", "Internal Audit", [ :department = "audit", :reportsTo = "ceo" ])
? @@( oOrg.ValidateBCEAOGovernance() )
#--> [ [ "status", "fail" ], [ "domain", "BCEAO_governance" ], [ "issuecount", 3 ], [ "issues", [ "BCEAO-001: No Board of Directors found", "BCEAO-002: Audit reports to non-board position", "BCEAO-003: No dedicated Risk Management function" ] ] ]
```

Three findings, each a rule with a number an auditor can read: `BCEAO-001: No Board of Directors found` is the first. The record shows the bank as the licensee of a product I built; it does not say who at the bank declared anything, and this page does not say it.

**An organisation in the field.** An organisation working in Niger, with a head office in Niamey and bases in the field, asked for a hub. Its own specification preferred a low-code platform built on a large vendor's office suite. My offer of 5 August 2026 was chosen instead; the study lists four gains, with ownership first among them. The organisation owns its vocabulary and its rules, changes them without programming, pays no licence per seat, and can hand everything to a programmer of its own country. The design study was built with its teams between 22 September and 8 October 2026. Two of its principles are the book's in small: the default is to work offline, and the agent proposes while a person decides. That rule is data the organisation attaches to its own model, and the model judges itself:

```haro
oRule = new stzGraphRule("no-llm-effectful")
oRule.SetDomainQ("agentic")
oRule.WhenQ("kind", "equals", "llm_actor")
oRule.WhenQ("capabilities", "contains", "effectful")
oRule.ThenViolationQ("an LLM proposes, only a pi-gate commits")
g = new stzGraph("agents")
g.AddNode("writer")
g.SetNodeProperty("writer", "kind", "llm_actor")
g.SetNodeProperty("writer", "capabilities", [ "inference", "effectful" ])
g.AddRule(oRule)
? g.RulesAreSound()
#--> 0
```

Three cases: a restaurateur who is not a programmer, a bank under a regulator, an organisation that chose ownership over a vendor. The restaurateur and the organisation are crafters by the record; the bank is the licensee of a product, and the record does not say who there declared anything. The restaurateur and the organisation did not wait for the software industry, and each is offered ownership of what is built for them.

## 4. The decision, and what I refused

**I kept the programmer first.** The vision of the platform, which I ratified, says it in one line: the first audience stays the programmer in a small team; the agentic era did not replace that person, it multiplied them. I held that agents do not make programmers obsolete.

**I added the agent as a crafter, and withheld one power.** The agent is the sixth reader of every Softanza language: both a builder and a user. It gets a workbench and a court. It does not get the capability to commit.

**I refused "maker", and I refused "builder".** "Maker" names the workshop movement, the soldering iron and the 3D printer (general knowledge, not a study of the record). The site's headline used it until 8 October 2026. "Builder" names someone who assembles what a plan says. Neither says what I think programming is. It is handwork, done with care, on something that is yours: it is craft. I call the person who does it a crafter. What this book's cover image carries, the record does not say, and this page does not say it for me.

**I refused to count a customer without a document.** The site counts a project as a reference only when a document proves it, and quotes no number of countries and no number of programmers. It names a customer only on my word. A lesson is listed only when a file of the library carries it.

**I refused to present the library by its anatomy.** Since 2022, the front door is who you are and what you want to do, and the anatomy is placed under each step. The site keeps seven doors (read on 9 October 2026), and the journeys behind them exist as pages, nine on that day, each step carrying its stage word. That every step runs in order under a guard is designed and not built.

## 5. The court

`agentfile_narrated` proves that an agent is a file judged when it is loaded: one refusal per gate, the missing coverage among them, and the model agent holding an effect refused by the same rule the graph uses. `service_registry_narrated` proves that a sandbox in production is a violation. `graphrule_object_narrated` proves the rule as an object attached to a model. `semantic_resolver_narrated` holds the Hausa path as its last scenario. It does not pass at this commit: I ran it on 8 October 2026 and it stops with an error raised from a string-splitting function, after 29 assertions and before it reaches the Hausa ones. So the page counts its assertions and does not claim its verdict; the Hausa block ran on its own. `00_orgchart_narrated` proves the chart's positions, reporting lines and vacancy tracking; the BCEAO finding printed above comes from a sibling file, `14_bceao_governance.ring`.

## 6. The field, and where it leads

Coding agents lead in hands. They already read, search, edit and run. What they lack, by the site's own account, is a way to know an unfamiliar interface without guessing, to judge their work against rules and promises, and to present a change as an intention a person can review. Softanza's judges are built; the door between them and a coding agent is decided and not built.

Low-code leads in installed base and in everything around it. (General knowledge, not a study of the record.) The organisation in the field keeps its vendor's suite for its accounts, its documents and its notifications. The crafter's platform sits beside the field's tools, not in place of them.

The messaging apps lead where the crafters already are. This is my view, not a result. The restaurateur's tool before the project was a spreadsheet; his own report of 4 July 2026 says so. The line that names messaging apps is the label of an option in the scoping form, and not his answer. No page of the site names those apps, and no conversational medium is a target of the platform yet. Chapter 25 is about that gap.

And the educator's door is not proven. The course's editions in French, Arabic and Hausa are drafts that no reviewer has read, and no institution has adopted it.

## 7. The limit

What is built: the agent file and its court; the registry that refuses a fake in production; rules as data on a model; a regulator's rules judging an organisation chart; the natural layer in Hausa and Arabic.

What is designed: a guard that fails when a step of a journey page breaks, each step run in order; the door through which a coding agent asks the library to judge its work.

What is absent: the platforms of the three customers running on the Softanza engine. Today the restaurant's platform is a set of web worlds, each a single file; the bank's is a Python application; the organisation's hub is a design. Their declarations are being written as Softanza's own. And the crafter's own medium, the messaging app on their phone, is not yet something a world can be declared to.

## 8. Six doors

**The programmer.** You declare intent in a library that reads like a sentence, and an engine computes under every call. You stay the first audience.

**The analyst.** You declare your organisation's entities, rules and flows in plain text, and the rules judge the model.

**The designer.** You declare a picture, a map or a screen as a program, and the first rule of an interface can come from a real trade: for a restaurateur, the speed of ordering.

**The decision-maker.** You declare your world, your governance, and what each actor may commit, and you own all of it, in plain text.

**The educator.** You declare a course in your learners' language, and every exercise is checked by running, in the site's words. The editions in French, Arabic and Hausa are still drafts no reviewer has read.

**The agent.** You declare yourself in a file: what you cover, how reversible your acts are. You get a workbench and a court. You do not get the capability to commit.

## 9. Exercise

Declare one agent for a world you know: a shop, a class, an office. Write its file: what it covers, how reversible its acts are, when it runs, one skill. Before you run it, write the promise you expect under the question below. Then run it.

```haro exercise
? StzAgentDeclarationQ(cYourAgent).IsValid()
#--> 1
```

If the court refuses, read the rule it cites and change your file, not the court. Then make your agent a language model and give it an effect, and read why it is refused. You will not find the corrected file in this book.

Chapter 3 is the method, from first principles, and the sentence its method returns to is this: you declare a world in a language made for it, and you govern how that world changes.
