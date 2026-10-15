---
id: an-organisation-in-the-field
part: 6
number: 30
title: An organisation in the field
spine: false
narrations: [stz-rules-as-graph-rules-narration.md, stz-governance-lineage-narration.md]
site: [forged, customers]
guards: [graphruleset_narrated, gg_rule_governance, wisecoding_narrated, governance_narrated, governance_lineage_narrated, 01_platform_narrated]
stage:
  built: "a rule built as an object on a model, its number changed and the model judged again; the rule governor that names a rule that governs nothing; a refusal kept as a checkpoint a person can read, with its context; authority set against risk; a decision kept with its authority at the time; offline as a capability a world must ask for"
  designed: "the hub and its study; a rule language a local programmer can learn; the study's promises that a rule is checked before it applies and can be undone"
  absent: "the hub, built; a mechanism for work done offline, kept and sent later; a version history of a rule; a customer platform on the engine"
status: draft
rulings: ["12.13", "12.29"]
research: research/ch30.md
---

In this chapter I take one organisation's design study and show the four things in it that the library carries. They are a rule as an object whose numbers can be changed, a refusal a person can read, authority set against risk, and a decision kept with its authority at the time. Then I show the one thing the organisation asked for that the library does not carry, offline, and I read that block as a limit and not as a win. I say "design study" and not "delivery" every time, because the hub is not built. The principle is the organisation's own: the AI agent proposes, and a person decides.

## 1. The concept, as the field holds it

The field has two practices that this project needed, and keeps them in separate places.

The first is the business rule that a business person can change. Rule engines and decision tables have existed for decades; the Decision Model and Notation, a standard of 2015, gives business analysts a table in which an approval ceiling is a number in a cell. The second is the application that keeps working with no network. Offline-first design is a practice of its own, with synchronising databases. Since an essay of 2019 it has a name for its philosophy, local-first software: the data is on your device, and the network is a convenience.

A third practice has come with AI agents: an AI model proposes, and a person approves. In the field it is a button.

The organisation's study turns that third practice into a principle.

## 2. The first principle

The organisation's own study of the project gives it as the title of a section, and I take it as the principle of this chapter, in my translation of its French title: **the AI agent proposes, and a person decides.**

## 3. The Softanza form

An organisation works in Niger, with a head office in Niamey and bases in the field. Its own specification preferred a low-code platform built on a large vendor's office suite. My offer of 5 August 2026 was the one retained. The study lists four gains, and ownership is the first it lists. The organisation owns its vocabulary and its rules; it changes them without programming; it pays no licence per seat for the platform; and it can hand everything to a programmer of its own country. We built the design study together, with its teams, from 22 September to 8 October 2026. The hub is not built. The study's version 1.2 is submitted to the executive director for validation, and the record does not say it was validated.

Four things in that study the library carries. I will show them in the order the organisation would meet them, and then the one it asked for that the library does not carry.

**A rule is an object whose numbers can be changed.** An approval ceiling is a sentence with a number in it, attached to the model of the advances it governs. The model judges itself, and says how many subjects the rule looks at. The data below are invented for this chapter, four advances with an amount and a count of approvals. They are not the organisation's figures, and the numbers five hundred and two hundred are mine, not its thresholds. Does a ceiling of five hundred catch an advance, and how many advances does the rule look at?

```haro
oG = new stzGraph("advances")
oG {
	AddNodeXTT("a0", "A0", [ :amount = 120, :approvals = 1 ])
	AddNodeXTT("a1", "A1", [ :amount = 250, :approvals = 1 ])
	AddNodeXTT("a2", "A2", [ :amount = 600, :approvals = 1 ])
	AddNodeXTT("a3", "A3", [ :amount = 900, :approvals = 2 ])
}
oRule = new stzGraphRule("second-approval")
oRule {
	SetDomain("advances")
	SetMessage("above the ceiling an advance needs two approvals")
	When("amount", "greaterthan", 500)
	ThenQ("approvals", "greaterthan", 1)
	ThenViolation("two approvals needed")
}
oG.AddRule(oRule)
oG.RulesReport()
#--> Rule report 'advances': 1 finding(s), 1 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [advances] 1 finding(s)
#        ERROR second-approval @ a2 -- two approvals needed
? len(oRule.SubjectsIn(oG))
#--> 2
```

The report names one advance, `a2`, at 600 with a single approval, and the rule looks at `2` of the four, `a2` and `a3`.

What happens when the ceiling is changed and the same model is judged again? Here the change is the rule rebuilt in code with another number, and the verdict and its scope follow:

```haro
oG.ClearAttachedRules()
oRule = new stzGraphRule("second-approval")
oRule {
	SetDomain("advances")
	SetMessage("above the ceiling an advance needs two approvals")
	When("amount", "greaterthan", 200)
	ThenQ("approvals", "greaterthan", 1)
	ThenViolation("two approvals needed")
}
oG.AddRule(oRule)
oG.RulesReport()
#--> Rule report 'advances': 2 finding(s), 2 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [advances] 2 finding(s)
#        ERROR second-approval @ a1 -- two approvals needed
#        ERROR second-approval @ a2 -- two approvals needed
? len(oRule.SubjectsIn(oG))
#--> 3
```

The report now says `2 finding(s), 2 error(s)` where it said one, and the scope is `3` where it was `2`! I have to be honest about what this block shows. That a change of the rule is a change of its values, which the organisation's own person makes like filling in a form, is the study's promise. I did not find a file of the library that makes it so. Section 7 says what does and does not exist.

What the library does carry is the answer to the worst thing that can go wrong when a non-programmer edits a rule: a rule that quietly governs nothing. I hold that as a view, not a result. Misspell a property, and the rule finds nothing, and the model reports that it is sound. What does a rule governor say of the same rule? The class is `StzRuleGovernance`; it asks rules what they govern and not what they say, and it names the dead rule:

```haro
oTypo = new stzGraphRule("second-approval-typo")
oTypo {
	SetMessage("above the ceiling an advance needs two approvals")
	When("amont", "greaterthan", 200)
	ThenQ("approvals", "greaterthan", 1)
	ThenViolation("two approvals needed")
	? len(Check(oG))
	#--> 0
}
oWatch = StzRuleGovernance("hub")
oWatch {
	AddRule(oTypo)
	AddCase("advances", oG)
	aF = CheckRules()
	? aF[1][:rule]
	#--> scope_empty
	? aF[1][:message]
	#--> governs nothing in 1 pictures -- a dead rule and a misspelt scope predicate both report as passing
}
oWatch2 = StzRuleGovernance("hub")
oWatch2 {
	AddRule(oRule)
	AddCase("advances", oG)
	? len(CheckRules())
	#--> 0
}
```

The misspelt rule finds nothing, `0`, and to the model nothing found means sound! The governor answers `scope_empty`, and says why: `governs nothing in 1 pictures -- a dead rule and a misspelt scope predicate both report as passing`. A dead rule and an all-clear produce identical output: silence. The court has to tell "nothing was wrong" from "nothing was looked at". The word "pictures" in the message is the rule governor's origin: it was built for the graph plane's drawings first, and I would say "cases".

**A person can read the refusal.** When an answer breaks a law the organisation declared, it is refused with its reason. The refusal is kept as a checkpoint a person can read, with its context. Chapter 17 showed the asking half of this machine. Here is the refusing half. A request needs one approval, and the law says a request has one approver. What does the machine do with a second approver?

```haro
oKB = new stzKnowledgeGraph("requests")
oKB {
	AddConversationQ("review").SetGoal(StzGoalQ().RequireOne("request-7", "approved-by"))
	? AskIn("review")
	#--> What does 'request-7' have for 'approved-by'?  (why: 'request-7' needs 'approved-by')
	ConstrainRelation("approved-by", :Unique)
	KnowRelation("request-7", "approved-by", "approver-1")
	aR = ReplyIn("review", "approver-2")
	? aR[:refused][1][2]
	#--> 'request-7' already bears 'approved-by' (to 'approver-1'); the relation is :Unique
	aCp = ConversationQ("review").Checkpoints()
	? len(aCp)
	#--> 1
	? aCp[1][:attempted]
	#--> approver-2
	? aCp[1][:why]
	#--> 'request-7' already bears 'approved-by' (to 'approver-1'); the relation is :Unique
}
```

The machine asks first: `What does 'request-7' have for 'approved-by'?  (why: 'request-7' needs 'approved-by')`. Then the second approver is refused! The checkpoint keeps what was attempted, `approver-2`, and the reason, in the refusal's own words: `'request-7' already bears 'approved-by' (to 'approver-1'); the relation is :Unique`.

**Authority is not permission.** The assistant of this organisation may prepare a file. It may hold the permission to release an advance and still be refused, because its authority does not cover the act's risk. A person with the authority is allowed. May the assistant release the advance, and may the approver? The verdict says why, in either case:

```haro
oGov = new stzGovernance("hub")
oGov {
	DeclareRisk("prepare-file", 1)
	DeclareRisk("release-advance", 3)
	GrantPermission("assistant", "prepare-file")
	GrantPermission("assistant", "release-advance")
	SetAuthority("assistant", :Advisory)
	GrantPermission("approver-1", "release-advance")
	SetAuthority("approver-1", :Autonomous)
	? MayProceed("assistant", "prepare-file")
	#--> 1
	? MayProceed("assistant", "release-advance")
	#--> 0
	? Why()
	#--> refused: 'assistant' holds 'advisory' authority (level 1) but 'release-advance' is risk tier 3 (SHOULD does not cover it)
	? MayProceed("approver-1", "release-advance")
	#--> 1
	? Why()
	#--> allowed: permission held AND 'autonomous' authority (level 3) covers risk tier 3
}
```

The assistant holds the permission for `release-advance`, and the answer is `0`! The verdict reads `refused: 'assistant' holds 'advisory' authority (level 1) but 'release-advance' is risk tier 3 (SHOULD does not cover it)`. For the approver it reads `allowed: permission held AND 'autonomous' authority (level 3) covers risk tier 3`. In the message, SHOULD is the library's word for what an authority level covers, as against CAN, the permission held; the guard behind this block says it as "can is not should".

The class here, `stzGovernance`, judges authority; it is not the rule governor of the dead rule above. The library knows an actor only by a name and an authority level. Whether an actor is a person or an assistant is what its level is declared to be. Binding a level to a signed-in person is the work of the authentication plane, which I have not read for this chapter.

**A decision keeps its authority at the time.** Each decision records its reason, its actor, the act, the authority and the risk of that moment. A new decision supersedes the old one without erasing it, up to a capacity (512 decisions by default), and the governance counts what it dropped. Record two decisions on the same case an hour apart: which one does the lineage answer with, and does the first survive?

```haro
nAt = 1785700000000
oGov {
	RecordDecisionAt("c-1", "ceiling raised for the harvest season", "approver-1", "release-advance", nAt)
	RecordDecisionAt("c-1", "ceiling restored, the season is over", "approver-1", "release-advance", nAt + 3600000)
	? LineageOf("c-1")[:rationale]
	#--> ceiling restored, the season is over
	? len(LineageHistoryOf("c-1"))
	#--> 2
	? LineageHistoryOf("c-1")[1][:rationale]
	#--> ceiling raised for the harvest season
	? LineageOf("c-1")[:authorityAtTime]
	#--> autonomous
}
```

The lineage answers `ceiling restored, the season is over`. It keeps `2` decisions, and the first still reads `ceiling raised for the harvest season`. The authority at the time is `autonomous`. The instant is a fixed number, so the clock is not read. This makes the block repeatable. It is not a version store for the rule itself, and I will not pretend it is.

And the one it asked for that the library does not carry. Its default option is to work offline: bases in the field with no network, entering what they do and sending it later. The library knows offline as a declared, governed capability of a world, asked for and granted or refused like the camera or payments. Is offline granted before the world asks for it, and after? That is all the library knows of it:

```haro
oApp = StzAppQ("field-visits")
oPlat = StzPlatformQ("field")
oPlat.SetWorld(oApp)
oRegime = new stzGovernance("field-regime")
oRegime.GrantPermission("field-visits", "use-offline")
oRegime.SetAuthority("field-visits", :Advisory)
oPlat {
	SetGovernedBy(oRegime)
	? Granted(:offline)
	#--> 0
	? Why()
	#--> capability 'offline' was never requested via AddCapabilityQ().
	AddCapabilityQ(:offline).SetPurposes([ :enter_without_network ])
	? Granted(:offline)
	#--> 1
	? Why()
	#--> allowed: permission held AND 'advisory' authority (level 1) covers risk tier 1
}
```

Before the request, `Granted(:offline)` is `0`, and the printed reason is `capability 'offline' was never requested via AddCapabilityQ().`. After the request it is `1`, and the printed reason is `allowed: permission held AND 'advisory' authority (level 1) covers risk tier 1`.

Read this block as a limit and not as a win. Nothing in it queues anything. The library does not keep entries on a device, send them when the network comes back, or settle two people's edits.

The next section sets down the decision, and what I refused.

## 4. The decision, and what I refused

**I refused a per-seat platform as the organisation's ground.** The specification preferred low-code on a vendor's suite. The retained offer proposes Softanza, and among its gains the study lists ownership first. The organisation owns its vocabulary and its rules, which it can change without programming, and the whole of the work, programs, configuration and data, is its own, with a handover to a local programmer. The vendor's suite stays where it was good, for the user accounts, the documents and the notifications. The record holds the outcome and the gains, and not the deliberation. Who chose, and what was weighed against low-code, it does not say. The chapter does not fill the gap.

**I refused to let the assistant decide.** It proposes. Its authority is advisory; a person's covers the risk. The refusal names the level, the risk tier, and the sentence that says the authority does not cover the act: `SHOULD does not cover it`.

**I refused a silent rule.** A rule that governs nothing is reported. A rule with no message is reported too. That is the price of letting a non-programmer touch a rule. The rule governor exists for that case, and the library's own comment says why: a dead rule and a misspelt predicate produce identical output, silence.

**I refused to call offline a lesson.** The Forged page, read on 9 October 2026, says: "This is a gap, not a lesson learned." A restaurant asked for the same. The study is clear that offline is the organisation's default, and the library has only a permission for it. A sister package of the estate, a browser-side one, holds a durable outbox on the device and an ordered, idempotent replay; it is outside the library. I did not run it.

Six guards stand behind the blocks.

## 5. The court

`graphruleset_narrated` proves a rule with a comparison and a requirement turned into an implication. `gg_rule_governance` proves that a rule that governs nothing is reported. `wisecoding_narrated`, its third scene, proves a refusal that is governed and checkpointed. `governance_narrated` proves that can is not should: permission held and authority lacking is a refusal. `governance_lineage_narrated` proves the decision kept with its authority at the time. `01_platform_narrated` proves the capability seam: the camera granted, payments refused, a capability never asked for refused with an honest reason. The guard does not itself use the capability for offline; the block above does, with the tier the platform declares for it. The refusal of an unknown rule type, of a missing file and of a duplicate name rests on scenes 4 and 5 of `rulz_roundtrip_narrated`. That is a narrated test of the library, and this book does not run it as one of its guards.

The next section sets what the field does against what the library has.

## 6. The field, and where it leads

The field leads in business rules for business people. Decision tables are a standard; a person edits a cell, not a program. Here the change is a rule rebuilt in code. The file form that would carry a rule as text, the `.stzrulz` file, reads a rule's name, its type, its severity, its function, its parameters and its message. It does not read the `when` and `then` lines of its own sample.

The field leads in offline. Local-first software is a practice with synchronising databases and a decade of experience. The library has a permission.

The field leads in people. A decision table is a thing a trained analyst already knows how to read. And the organisation's own specification, which preferred the vendor's suite, had good reasons: its users already have accounts there.

The next section lists what is built, what is designed and what is absent.

## 7. The limit

What is built: a rule as an object, its number changed and the model judged again; the rule governor that names a dead rule; the checkpoint; authority against risk; the lineage; offline as a capability.

What is designed: the hub and its study, whose schedule is in the future; a rule language that a local programmer can learn; and the study's promises about rules. The language's sample in the study is written in a notation that is not the library's. The study promises that a rule is checked before it applies, that its effect is shown before it is applied, that it can be undone and that its history is kept. The library has only the pieces. They are the rule governor, shown above, and the refusals of an unknown rule type, a missing file and a duplicate name, which a narrated test of the library proves and this chapter does not show.

What is absent: a version history of a rule with an undo. The lineage records the decision, and the rule is rebound. I found no store of rule versions, and my search was not exhaustive. The hub, built. Offline as a mechanism: no class in the library keeps entries on a device and sends them when the network returns. And a customer platform on the Softanza engine.

Six doors follow, one for each reader.

## 8. Six doors

**The programmer.** A rule is an object with a comparison and a requirement, attached to a model, and a rule governor tells you when it governs nothing.

**The analyst.** The study promises that you change a rule's values, not its program. In the library, when the values change, the model is judged again with the new scope.

**The designer.** A refusal keeps its context for the person who will read it.

**The decision-maker.** Authority is not permission: ask which level covers which risk, and read the lineage of a decision.

**The educator.** An organisation's rule can be taught as a sentence with a number in it.

**The agent.** You prepare. A person decides. And you will be refused, with the level and the risk tier named.

## 9. Exercise

Pick one rule of an organisation you know that has a number in it, a ceiling, a delay, a count of approvals. Write it as a rule with a condition and a requirement, on four invented cases, two that satisfy it and two that do not. Before you run anything, write the report you expect. Then misspell one property of the condition on purpose, and say what the model reports, and what the governor reports.

Run it. The difference between those two answers is the chapter.

I left this one in your hands. The block below is the second block of section 3 followed by the last lines of the governor block, with one change: the rule has no `SetMessageQ` line, so it carries no message.

```haro exercise
oG.ClearAttachedRules()
oRule = new stzGraphRule("second-approval")
oRule.SetDomainQ("advances")
oRule.WhenQ("amount", "greaterthan", 200)
oRule.ThenQ("approvals", "greaterthan", 1)
oRule.ThenViolationQ("two approvals needed")
oG.AddRule(oRule)
oG.RulesReport()
oWatch2 = StzRuleGovernance("hub")
oWatch2.AddRule(oRule)
oWatch2.AddCase("advances", oG)
? len(oWatch2.CheckRules())
```

Run it on the model of section 3. Compare what the model reports with what it reported when the rule had its message, and read what the governor returns. Under "I refused a silent rule", section 4 says what the governor does with such a rule, and why. I do not give the answer here. When you have solved it, you will know why the governor reports a rule that has no message.

The next chapter says what the projects show, and what comes next. Its measure is this: a project shows exactly what a document, a file, a run and a named person reach, and the page says where they stop.
