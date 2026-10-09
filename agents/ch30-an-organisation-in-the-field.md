# An organisation in the field

Source: Chapter 30. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: a rule written as data on a model, changed and judged again; the governor that names a rule that governs nothing; a refusal that reaches a person with its context; authority set against risk; a decision kept with its authority at the time; offline as a capability a world must ask for; designed: the hub and its study; a rule language a local developer can learn; the study's promises that a rule is checked before it applies and can be undone; absent: the hub, built; a mechanism for work done offline, kept and sent later; a version history of a rule; a customer platform on the engine

Run: 7 of 7 blocks kept their promise, on 2026-10-09 04:27 UTC+01:00.

## 1. The concept, as the field holds it

The field has two practices that this project needed, and keeps them in separate places.

The first is the business rule that a business person can change. Rule engines and decision tables have existed for decades; the Decision Model and Notation, a standard of 2015, gives business analysts a table in which an approval ceiling is a number in a cell. The second is the application that keeps working with no network. Offline-first design is a practice of its own, with synchronising databases and, since an essay of 2019, a name for its philosophy, local-first software: the data is on your device, and the network is a convenience.

A third practice has come with the agents: a model proposes, and a person approves. In the field it is a button.

## 2. The first principle

The organisation's own study of the project says it in one sentence, and I take it as the principle of this chapter: **the agent proposes, and a person decides.**

## 3. The Softanza form

An organisation works in Niger, with a head office in Niamey and bases in the field. Its own specification preferred a low-code platform built on a large vendor's office suite. My offer of 5 August 2026 was the one retained, for a reason chapter 2 gave: ownership. It owns its vocabulary and its rules; it changes them without programming; it pays no licence per seat; and it can hand everything to a developer of its own country. We built the design study together, with its teams, from 22 September to 8 October 2026. I say "design study" and not "delivery" every time, because the hub is not built. The study's version 1.2 is submitted to the executive director for validation, and the record does not say it was validated.

Four things in that study the library carries. I will show them in the order the organisation would meet them, and then the one it asked for that the library does not carry.

**A rule is data.** An approval ceiling is a sentence with a number in it, attached to the model of the advances it governs. The model judges itself, and says how many subjects the rule looks at. The data below are invented for this chapter, four advances with an amount and a count of approvals; they are not the organisation's figures, and the numbers five hundred and two hundred are mine, not its thresholds.

```haro
oG = new stzGraph("advances")
oG.AddNodeXTT("a0", "A0", [ :amount = 120, :approvals = 1 ])
oG.AddNodeXTT("a1", "A1", [ :amount = 250, :approvals = 1 ])
oG.AddNodeXTT("a2", "A2", [ :amount = 600, :approvals = 1 ])
oG.AddNodeXTT("a3", "A3", [ :amount = 900, :approvals = 2 ])
oRule = new stzGraphRule("second-approval")
oRule.SetDomainQ("advances")
oRule.SetMessageQ("above the ceiling an advance needs two approvals")
oRule.WhenQ("amount", "greaterthan", 500)
oRule.ThenQ("approvals", "greaterthan", 1)
oRule.ThenViolationQ("two approvals needed")
oG.AddRule(oRule)
oG.RulesReport()
#--> Rule report 'advances': 1 finding(s), 1 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [advances] 1 finding(s)
#        ERROR second-approval @ a2 -- two approvals needed
? len(oRule.SubjectsIn(oG))
#--> 2
```

> run: kept

The ceiling is changed, and the same model is judged again. A change of the rule is a change of its values, and the verdict and its scope follow:

```haro
oG.ClearAttachedRules()
oRule = new stzGraphRule("second-approval")
oRule.SetDomainQ("advances")
oRule.SetMessageQ("above the ceiling an advance needs two approvals")
oRule.WhenQ("amount", "greaterthan", 200)
oRule.ThenQ("approvals", "greaterthan", 1)
oRule.ThenViolationQ("two approvals needed")
oG.AddRule(oRule)
oG.RulesReport()
#--> Rule report 'advances': 2 finding(s), 2 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [advances] 2 finding(s)
#        ERROR second-approval @ a1 -- two approvals needed
#        ERROR second-approval @ a2 -- two approvals needed
? len(oRule.SubjectsIn(oG))
#--> 3
```

> run: kept

I have to be honest about what this block shows. The "change" is a rule rebuilt in code with another number. That the organisation's own person changes it like filling in a form is the study's promise, and I did not find a file of the library that makes it so; section 7 says what does and does not exist.

What the library does carry is the answer to the worst thing that can go wrong when a non-programmer edits a rule: a rule that quietly governs nothing. Misspell a property, and the rule finds nothing, and the model reports that it is sound. A governor, which asks rules what they govern and not what they say, names the dead rule:

```haro
oTypo = new stzGraphRule("second-approval-typo")
oTypo.SetMessageQ("above the ceiling an advance needs two approvals")
oTypo.WhenQ("amont", "greaterthan", 200)
oTypo.ThenQ("approvals", "greaterthan", 1)
oTypo.ThenViolationQ("two approvals needed")
? len(oTypo.Check(oG))
#--> 0
oWatch = StzRuleGovernance("hub")
oWatch.AddRule(oTypo)
oWatch.AddCase("advances", oG)
aF = oWatch.CheckRules()
? aF[1][:rule]
#--> scope_empty
? aF[1][:message]
#--> governs nothing in 1 pictures -- a dead rule and a misspelt scope predicate both report as passing
oWatch2 = StzRuleGovernance("hub")
oWatch2.AddRule(oRule)
oWatch2.AddCase("advances", oG)
? len(oWatch2.CheckRules())
#--> 0
```

> run: kept

A dead rule and an all-clear produce identical output: silence. The court has to tell "nothing was wrong" from "nothing was looked at". The word "pictures" in the message is the governor's origin: it was built for the graph plane's drawings first, and I would say "cases".

**A person sees the refusal.** When an answer breaks a law the organisation declared, it is refused with its reason, and the refusal is kept as a checkpoint for a person to see, with its context. Chapter 17 showed the asking half of this machine. Here is the refusing half: a request needs one approval, the law says a request has one approver, and a second approver is refused:

```haro
oKB = new stzKnowledgeGraph("requests")
oKB.AddConversationQ("review").SetGoal(StzGoalQ().RequireOne("request-7", "approved-by"))
? oKB.AskIn("review")
#--> What does 'request-7' have for 'approved-by'?  (why: 'request-7' needs 'approved-by')
oKB.ConstrainRelation("approved-by", :Unique)
oKB.KnowRelation("request-7", "approved-by", "approver-1")
aR = oKB.ReplyIn("review", "approver-2")
? aR[:refused][1][2]
#--> 'request-7' already bears 'approved-by' (to 'approver-1'); the relation is :Unique
aCp = oKB.ConversationQ("review").Checkpoints()
? len(aCp)
#--> 1
? aCp[1][:attempted]
#--> approver-2
? aCp[1][:why]
#--> 'request-7' already bears 'approved-by' (to 'approver-1'); the relation is :Unique
```

> run: kept

**Authority is not permission.** The assistant of this organisation may prepare a file. It may hold the permission to release an advance and still be refused, because its authority does not cover the act's risk. A person with the authority is allowed. The verdict says why, in either case:

```haro
oGov = new stzGovernance("hub")
oGov.DeclareRisk("prepare-file", 1)
oGov.DeclareRisk("release-advance", 3)
oGov.GrantPermission("assistant", "prepare-file")
oGov.GrantPermission("assistant", "release-advance")
oGov.SetAuthority("assistant", :Advisory)
oGov.GrantPermission("approver-1", "release-advance")
oGov.SetAuthority("approver-1", :Autonomous)
? oGov.MayProceed("assistant", "prepare-file")
#--> 1
? oGov.MayProceed("assistant", "release-advance")
#--> 0
? oGov.Why()
#--> refused: 'assistant' holds 'advisory' authority (level 1) but 'release-advance' is risk tier 3 (SHOULD does not cover it)
? oGov.MayProceed("approver-1", "release-advance")
#--> 1
? oGov.Why()
#--> allowed: permission held AND 'autonomous' authority (level 3) covers risk tier 3
```

> run: kept

The library knows an actor only by a name and an authority level. Whether an actor is a person or an assistant is what its level is declared to be, and binding a level to a signed-in person is the work of the authentication plane, which I have not read for this chapter.

**A decision keeps its authority at the time.** Each decision records its reason, its actor, the act, the authority and the risk of that moment. A new decision supersedes the old one without erasing it:

```haro
nAt = 1785700000000
oGov.RecordDecisionAt("c-1", "ceiling raised for the harvest season", "approver-1", "release-advance", nAt)
oGov.RecordDecisionAt("c-1", "ceiling restored, the season is over", "approver-1", "release-advance", nAt + 3600000)
? oGov.LineageOf("c-1")[:rationale]
#--> ceiling restored, the season is over
? len(oGov.LineageHistoryOf("c-1"))
#--> 2
? oGov.LineageHistoryOf("c-1")[1][:rationale]
#--> ceiling raised for the harvest season
? oGov.LineageOf("c-1")[:authorityAtTime]
#--> autonomous
```

> run: kept

The instant is a fixed number, so the clock is not read. This keeps the decision answerable. It is not a version store for the rule itself, and I will not pretend it is.

And the one the organisation asked for first. Its default option is to work offline: bases in the field with no network, entering what they do and sending it later. The library knows offline as a declared, governed capability of a world, asked for and granted or refused like the camera or payments. That is all it knows:

```haro
oApp = StzAppQ("field-visits")
oPlat = StzPlatformQ("field")
oPlat.SetWorld(oApp)
oRegime = new stzGovernance("field-regime")
oRegime.GrantPermission("field-visits", "use-offline")
oRegime.SetAuthority("field-visits", :Advisory)
oPlat.SetGovernedBy(oRegime)
? oPlat.Granted(:offline)
#--> 0
? oPlat.Why()
#--> capability 'offline' was never requested via AddCapabilityQ().
oPlat.AddCapabilityQ(:offline).SetPurposes([ :enter_without_network ])
? oPlat.Granted(:offline)
#--> 1
? oPlat.Why()
#--> allowed: permission held AND 'advisory' authority (level 1) covers risk tier 1
```

> run: kept

Read this block as a limit and not as a win. Nothing in it queues anything. The library does not keep entries on a device, send them when the network comes back, or settle two people's edits.

## 4. The decision, and what I refused

**I refused a per-seat platform as the organisation's ground.** The specification preferred low-code on a vendor's suite. The retained offer proposes Softanza for one reason above the others: the organisation owns its vocabulary and its rules, which it can change without programming, and the whole of the work, programs, configuration and data, is its own, with a handover to a local developer. The vendor's suite stays where it was good, for the user accounts, the documents and the notifications. [AUTHOR: Who chose, and what was weighed against low-code? The record has the outcome and the gains, listed without a ranking, and not the deliberation.]

**I refused to let the assistant decide.** It proposes. Its authority is advisory; a person's covers the risk. The refusal names the level, the risk tier, and the sentence that says the authority does not cover the act.

**I refused a silent rule.** A rule that governs nothing is reported. A rule with no message is reported too. That is the price of letting a non-programmer touch a rule, and I did not wait for the first incident to pay it.

**I refused to call offline a lesson.** The Forged page says it in four words: a gap, not a lesson. A restaurant asked for the same. The study is clear that offline is the organisation's default, and the library has only a permission for it. [AUTHOR: The organisation's study says its offline part "is already in service", and the Forged page says "a gap". The record of a sister package of the estate, a browser-side one, holds a durable outbox on the device and an ordered, idempotent replay, and I did not run it. May the book mention it, as outside the library and not run?]

## 5. The court

`graphruleset_narrated` proves a rule with a comparison and a requirement turned into an implication. `gg_rule_governance` proves that a rule that governs nothing is reported. `wisecoding_narrated`, its third scene, proves a refusal that is governed and checkpointed. `governance_narrated` proves that can is not should: permission held and authority lacking is a refusal. `governance_lineage_narrated` proves the decision kept with its authority at the time. `01_platform_narrated` proves the capability seam: the camera granted, payments refused, a capability never asked for refused with an honest reason. The guard does not itself use the capability for offline; the block above does, with the tier the platform declares for it.

## 6. The field, and where it leads

The field leads in business rules for business people. Decision tables are a standard; a person edits a cell, not a program. Here the change is a rule rebuilt in code, and the file form that would carry a rule as text loads rules and judges nothing: it reads a rule's name, its kind, its severity, its function and its message, and does not read the `when` and `then` lines of its own sample.

The field leads in offline. Local-first software is a practice with synchronising databases and a decade of experience. The library has a permission.

The field leads in people. A decision table is a thing a trained analyst already knows how to read. And the organisation's own specification, which preferred the vendor's suite, had good reasons: its users already have accounts there.

## 7. The limit

What is built: a rule as data, changed and judged again; the governor that names a dead rule; the checkpoint; authority against risk; the lineage; offline as a capability.

What is designed: the hub and its study, whose schedule is in the future; a rule language that a local developer can learn, whose sample in the study is written in a notation that is not the library's; and the study's promises about rules: that they are checked before they apply, that their effect is shown before it is applied, that they can be undone and that their history is kept. The library has the pieces, the governor, the refusal of an unknown rule type or a missing file, and the refusal of a duplicate name.

What is absent: a version history of a rule with an undo: the lineage records the decision, and the rule is rebound; I found no store of rule versions, and my search was not exhaustive. The hub, built. Offline as a mechanism: no class in the library queues, synchronises or settles a conflict. And a customer platform on the Softanza engine.

## 8. Six doors

**The programmer.** A rule is an object with a comparison and a requirement, attached to a model, and a governor tells you when it governs nothing.

**The analyst.** You change a rule's values, not its program, and the model is judged again with the new scope.

**The designer.** A refusal keeps its context for the person who will read it.

**The decision-maker.** Authority is not permission: ask which level covers which risk, and read the lineage of a decision.

**The educator.** An organisation's rule can be taught as a sentence with a number in it.

**The agent.** You prepare. A person decides. And you will be refused, with the level and the risk tier named.

## 9. Exercise

Pick one rule of an organisation you know that has a number in it, a ceiling, a delay, a count of approvals. Write it as a rule with a condition and a requirement, on four invented cases, two that satisfy it and two that do not. Before you run anything, write the report you expect. Then misspell one property of the condition on purpose, and say what the model reports, and what the governor reports.

Run it. The difference between those two answers is the chapter.
