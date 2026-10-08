---
id: the-software-maker
part: 1
number: 2
title: The software maker
spine: true
narrations: [stz-built-on-real-world-need.md, stz-service-virtualization-code-first-subscribe-later.md, stz-agents-that-cannot-hurt-you-narration.md, stz-rules-as-graph-rules-narration.md, stzOrgChartDoc-BankUseCase.md]
site: [offering, customers, forged, coding-agents]
guards: [agentfile_narrated, service_registry_narrated, graphrule_object_narrated, semantic_resolver_narrated, 00_orgchart_narrated]
stage:
  built: "the agent file and its court; the registry that refuses a fake in production; rules as data on a model; a regulator's rules judging an organisation chart; the natural layer in Hausa and Arabic"
  designed: "a journey page for each kind of maker, with each step run; the door through which a coding agent asks the library to judge its work"
  absent: "the three makers' platforms running on the Softanza engine; a maker's own medium, the messaging app on their phone, as a target"
status: draft
rulings: ["12.2", "12.12", "12.13", "12.25", "12.29", "12.30"]
research: research/ch02.md
---

## 1. The concept, as the field holds it

The word "maker" already has an owner. Since the magazine *Make:* in 2005, it has meant the hobbyist with a workshop: a soldering iron, a 3D printer, a fair on a Saturday. That is a fine culture, and it is not what this book is about, which is why the cover says *software* makers.

The field has two other answers to "who makes software, if not programmers". The first is low-code: business people building applications on a vendor's visual platform, the "citizen developer" of the analysts. The second is the coding agent: a model that reads files, edits them and runs commands, steered in plain words, with "vibe coding" as the name for keeping whatever it writes. Both answers share a shape. The maker is defined by a tool, and the work lives where the tool lives. When the vendor changes its prices or its model, the maker's work changes with it.

## 2. The first principle

The site gives the definition in two sentences: **a maker turns what they know about a world into something that runs, without waiting for the software industry; they are not defined by programming skill but by ownership: the artefact is theirs, in plain text, and it does not expire.** [AUTHOR: These sentences were drafted for the site and have not been ruled by you in the record. Are they your definition, or would you put it differently?]

## 3. The Softanza form

I was the first maker of Softanza, and not for a reason I would have chosen. My wife runs a music club where people learn to sing classical Arabic songs. Every Sunday morning she sends me the list of songs to prepare, and I search for their lyrics. The lyrics found online repeat every phrase as the singer performed it, and she reminds me, every time, to remove the duplicates. I wrote `RemoveDuplicates()` to stop doing it by hand, and its family is still in the library:

```haro
o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? o1.ContainsDuplicates()
#--> 1
? o1.NumberOfOccurrence("tea")
#--> 3
```

I write about this in an article on what the library was built on: I introduced its features when a real problem asked for them. The maker comes first, and the feature after.

Since 2022, I have presented Softanza not by its anatomy, its modules and classes, but by who you are and what you are trying to do. The 2022 deck had five audiences, each with a recipe of three to five steps. The site today has six doors, one per kind of maker, and each door says what you declare, what you get, and where to start. Here is what each one declares, in a line or two that run.

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

**The decision-maker** declares what each actor in the world may do, a person or an agent, and the court enforces it. An agent is a small text file; one that does not say what it covers is refused when it is loaded, not when it first acts:

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

**The educator** declares a course, and the learner speaks to the machine in their own language. A sentence in Hausa runs; the engine counts the letters of an Arabic word, not its bytes, and knows its script:

```haro
? NaturallyIn("ha", "Yi rubutu dauke 'hello' Maida shi").Result()
#--> HELLO
? Q("سلام").NumberOfChars()
#--> 4
? Q("مرحبا بالعالم").Script()
#--> arabic
```

**The agent** is the sixth maker, the one 2020 could not draw. It declares itself in the same kind of file, and it is welcome, with one thing withheld. An agent whose mind is a language model may propose; it may not hold an effect, and a file that gives it one is refused at construction:

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

Now the three makers this book is for. They are not personas. They are people with documents, and Part VI tells each of them in full. Here, a page each.

**A restaurateur in Lyon.** He owns a couscous restaurant, and with a few neighbours he wanted a platform for neighbourhood commerce. The project's notes say it plainly: he is not a programmer. The project began with an offer in May 2024 and then two years of rich specification that produced nothing he could use. What came out of that failure is the rule I have worked by since: deliver small, fast and useful, and let the foundations mature in parallel without ever blocking a delivery. In July 2026 he reversed the order of the work, and the library's constellation of worlds was redrawn around his order. The first amendment closed on 4 August 2026, with one ergonomic rule: at most two gestures per action. The rules of the interface were forged by eleven iterations with him, phone in hand. And on 19 August, after a day of tests in the field with two phones and a messaging app, the notes call him the project's co-architect. [AUTHOR: Chapter 1 says the first demonstration was made by the owner himself, on his own phone, over a messaging app. The record has the demonstration day, 15 August 2026, and his own measurements of 19 August. Who demonstrated what on the 15th?]

One of his needs became a law of the library: try payments before paying anyone for an account. A fake payments service is welcome while you rehearse, and refused when you go live:

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

**A bank in Niamey.** A commercial bank under the rules of the central bank of the West African monetary union runs an organisation-assessment product I built, under licence, on its own internal network; the installation guide delivered to the bank is the document that attests it. The lesson it left in the library is that an organisation can be judged by its own chart, under a regulator's rules. Declare a chart with a chief executive and an internal audit that reports to him, and the regulator's rules answer:

```haro
oOrg = new stzOrgChart("bank")
oOrg.AddPositionXTT("ceo", "Chief Executive", [ :department = "executive" ])
oOrg.AddPositionXTT("audit", "Internal Audit", [ :department = "audit", :reportsTo = "ceo" ])
? @@( oOrg.ValidateBCEAOGovernance() )
#--> [ [ "status", "fail" ], [ "domain", "BCEAO_governance" ], [ "issuecount", 3 ], [ "issues", [ "BCEAO-001: No Board of Directors found", "BCEAO-002: Audit reports to non-board position", "BCEAO-003: No dedicated Risk Management function" ] ] ]
```

Three findings, each a rule with a number an auditor can read. [AUTHOR: Who at the bank is the maker in the sense of this chapter, and what did they declare? The record shows the bank as the licensee of a product you built; it is silent on what the bank's own people declared.]

**An organisation in the field.** An organisation working in Niger, with a head office in Niamey and bases in the field, asked for a hub. Its own specification preferred a low-code platform built on a large vendor's office suite. My offer of 5 August 2026 was chosen instead, for one reason above the others: ownership. The organisation owns its vocabulary and its rules, changes them without programming, pays no licence per seat, and can hand everything to a developer of its own country. The design study was built with its teams between 22 September and 8 October 2026. Two of its principles are the book's in small: the default is to work offline, and the agent proposes while a person decides. That rule is data the organisation attaches to its own model, and the model judges itself:

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

Three makers: a restaurateur who is not a programmer, a bank under a regulator, an organisation that chose ownership over a vendor. None of them waited for the software industry. Each of them owns, or will own, what was built.

## 4. The decision, and what I refused

**I kept the programmer first.** The vision of the platform, which I ratified, says it in one line: the first audience stays the programmer in a small team; the agentic era did not replace that person, it multiplied them. I refused the reading that agents make programmers obsolete.

**I added the agent as a maker, and withheld one power.** The agent is the sixth reader of every Softanza language: both a builder and a user. It gets a workbench and a court. It does not get the capability to commit.

**I refused the hobbyist word.** The site's headline said "makers". On the cover of this book I wrote "software makers", so that nobody reads it as the workshop and the printer.

**I refused to count a customer without a document.** The site counts a project as a reference only when a document proves it, quotes no number of countries and no number of developers, and names a customer only on my word. A lesson is listed only when a file of the library carries it.

**I refused to present the library by its anatomy.** Since 2022, the front door is who you are and what you want to do, and the anatomy is placed under each step. The site keeps six doors; the journeys behind them, one page per maker with every step run, are designed and not built.

## 5. The court

`agentfile_narrated` proves that an agent is a file judged when it is loaded: one refusal per gate, the missing coverage among them, and the model agent holding an effect refused by the same rule the graph uses. `service_registry_narrated` proves that a sandbox in production is a violation. `graphrule_object_narrated` proves the rule as an object attached to a model. `semantic_resolver_narrated` proves the Hausa path. `00_orgchart_narrated` proves the organisation chart and its validators.

## 6. The field, and where it leads

Coding agents lead in hands. They already read, search, edit and run, on any project, in any language. What they lack, by the site's own account, is a way to know an unfamiliar interface without guessing, to judge their work against rules and promises, and to present a change as an intention a person can review. Softanza's judges are built; the door between them and a coding agent is decided and not built.

Low-code leads in installed base and in everything around it. The organisation in the field keeps its vendor's suite for its accounts, its documents and its notifications; the maker's platform sits beside the field's tools, not in place of them.

The messaging apps lead where the makers already are. The restaurateur's tools before the project were his head, a paper notebook, a spreadsheet and the messaging apps on his phone. No page of the site names those apps, and no conversational medium is a target of the platform yet. Chapter 25 is about that gap.

And the educator's door is the least proven of the six. The course's editions in French, Arabic and Hausa are drafts that no reviewer has read, and no institution has adopted it.

## 7. The limit

What is built: the agent file and its court; the registry that refuses a fake in production; rules as data on a model; a regulator's rules judging an organisation chart; the natural layer in Hausa and Arabic.

What is designed: a journey page for each kind of maker, with each step run in order and a guard that fails when a step breaks; the door through which a coding agent asks the library to judge its work.

What is absent: the three makers' platforms running on the Softanza engine. Today the restaurant's platform is a set of web worlds, each a single file; the bank's is a Python application; the organisation's hub is a design. Their declarations are being written as Softanza's own. And the maker's own medium, the messaging app on their phone, is not yet something a world can be declared to.

## 8. Six doors

**The programmer.** You declare intent in a library that reads like a sentence, and an engine computes under every call. You stay the first audience.

**The analyst.** You declare your organisation's entities, rules and flows in plain text, and the rules judge the model.

**The designer.** You declare a picture, a map or a screen as a program, and the rule of two gestures came from a real user.

**The decision-maker.** You declare your world, your governance, and what each actor may commit, and you own all of it, in plain text.

**The educator.** You declare a course in your learners' language, and every exercise is checked by running.

**The agent.** You declare yourself in a file: what you cover, how reversible your acts are. You get a workbench and a court. You do not get the capability to commit.

## 9. Exercise

Declare one agent for a world you know: a shop, a class, an office. Write its file: what it covers, how reversible its acts are, when it runs, one skill. Before you run it, write the promise you expect under the question below. Then run it.

```haro exercise
? StzAgentDeclarationQ(cYourAgent).IsValid()
#--> 1
```

If the court refuses, read the rule it cites and change your file, not the court. Then make your agent a language model and give it an effect, and read why it is refused. You will not find the corrected file in this book.
