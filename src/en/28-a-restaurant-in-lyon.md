---
id: a-restaurant-in-lyon
part: 6
number: 28
title: A restaurant in Lyon
spine: false
narrations: [stz-service-virtualization-code-first-subscribe-later.md, stz-perf-judgment-narration.md, stzApp-building-your-first-app-narration.md]
site: [forged, customers]
guards: [06_stzsuperapp_narrated, service_delivery_narrated, payments_port_narrated, judgment_narrated, graphrule_object_narrated]
stage:
  built: "the constellation of worlds with its bonds and norms; the payments sandbox and the production gate that refuses a fake; the speed budget declared and judged"
  designed: "the Lock as a rule of the library; the constellation written in the near-natural idiom the design describes"
  absent: "the restaurant's live payment adapter; a measurement of the budget on a real mobile network; a speed expectation in the owner's own percentile; browser-side timing; the platform on the Softanza engine"
status: draft
rulings: ["12.15", "12.19", "12.25", "12.29", "12.30"]
research: research/ch28.md
---

In this chapter I tell a paid lesson in order, with its dates: a restaurateur in Lyon, two years of specification that produced nothing he could use, and the reversal of 4 July 2026 that put the customer first. I show what the library carries of each lesson: the Lock as a rule over a cycle's worlds, a payments sandbox that is not agreeable, a constellation that puts a world to sleep, a speed budget declared and judged. I say where it carries nothing, and what I refused: the grand system in one piece, silent drift, the agreeable fake, and crediting the owner with what a simulation said. The principle is one sentence on the site: deliver small, fast and useful, and let the foundations mature in parallel without ever blocking a delivery.

## 1. The concept, as the field holds it

Each lesson of this project has an ordinary home in the field, and the field keeps it outside the program.

A fixed scope for a cycle lives in a process. In Scrum the goal of a sprint does not change while it runs; in Shape Up, the time is fixed and the scope varies, and new ideas wait outside the cycle. Trying a service before paying for it lives in a vendor's test mode and in tools that stand in for an HTTP service. A performance budget lives in a continuous-integration check of a page's weight and speed, and the web's own measure of speed is a figure taken over real page loads, at the seventy-fifth percentile. The picture of a whole constellation of small applications lives in the super-app: one host that embeds a runtime and runs mini-applications inside it. (All of this is general knowledge, not a study of the record.)

All four are good practices, and in all four the program itself knows nothing of them.

## 2. The first principle

The project was a paid lesson, and the lesson is one sentence on the site: **deliver small, fast and useful, and let the foundations mature in parallel without ever blocking a delivery.**

Its companion is this chapter's rule of evidence, taken from the same page: a lesson is listed only when a file of the library carries it.

## 3. The Softanza form

A restaurateur in Lyon owns a couscous restaurant, and he wanted a platform for neighbourhood commerce. He is not a programmer, and the project's own notes say so. I am going to tell the project in order, with its dates, and then show what the library carries of each lesson.

It began with an offer, on 2 May 2024, for a mission of business analysis. What followed was two years, in the owner's own count, of research and reflection, and of what I called specification: founding analyses, a novel of narrations, a first product specified in full. It produced nothing he could use. In the middle of 2025 the project came close to ending, and a silence of six months followed. That is where I learned the doctrine of section 2: deliver small, fast and useful.

On 3 July 2026, two of us rehearsed the project: a scoping of his answers that I wrote with a session, and a campaign of twenty-two simulated tests, run by the sessions playing the owner. I say "simulated" every time, because the answers in that file are not his. The next day, 4 July, he answered a real scoping report in his own words. He reversed the order of the work. We had imagined a line that ran from the supplier to the restaurateur and ended with the customer. He turned it around: customer first, restaurateur next, supplier last. And he wrote that the speed of ordering was his first priority, non-negotiable. His great fear was friction at the first load, and the second fear, in the same report, was the calendar: none of the deadlines until then had been kept.

The project's answer to his fear is a document and a notebook. We called it the Lock. In July, a second scoping proposed it to him, clause by clause. The first three: a single amendment; every new idea goes into a notebook, read at the end of the cycle; one entry needs one written exit. The last two: a demonstration every two weeks and no date beyond the next cycle; and a definition of done. He accepted four clauses as written and adjusted the fifth by adding a criterion of his own: that other merchants and partners must be able to install the product alone. In the record I am the one who asked for the Lock first, as a rule on myself: that the change of course had to be the only change of course allowed. On 4 August 2026, the first amendment closed. Twelve decisions were sealed; three were asked again in plain words, because he himself had flagged that he had not understood them. The lesson written down is about how to ask: the moment a question speaks of milestones and phasing and cycles, the owner stops following. So the questions moved into his trade's language.

On 15 August the first demonstration was designed for him alone. The checklist is titled with his name and "alone". He opens the delivery on his own computer, scans one code with his phone and another with his tablet, places his own order from the phone, and watches it land on the tablet. If he gets stuck, a button prepares a message to paste into a messaging app. The criterion of success reads: he orders from his phone, and it lands on his tablet, without us. The notebook shows it happened: his remarks of that day were entered in it on the 17th. And on 19 August he spent a field day with two phones and photographs sent over a messaging app, measuring on a real phone. A hotspot works with no card in it; the address of the gateway was stable across restarts. A phone is a Wi-Fi client or a hotspot, never both; an iPhone's system does not return by itself to a network with no internet. The project's notes then call him its co-architect. The record ends on 25 August 2026.

That is the story. Here is what the library carries of it.

**The Lock.** I have to be exact here, because the Forged page of the site holds a rule I made: a lesson is listed only when a file of the library carries it. No file carries the Lock. It was a pact and a notebook, kept in documents. What the library can do is give you the nearest declaration of it: a rule over the worlds of a cycle, that a world without a written admission is a finding. What does the court say when an idea enters the cycle with no written admission? This block is a construction, not the restaurant's code:

```haro
oRule = new stzGraphRule("the-lock")
oRule.SetDomainQ("scope")
oRule.WhenQ("kind", "equals", "world")
oRule.WhenQ("admitted-by", "missing", "")
oRule.ThenViolationQ("a world entered the cycle with no written admission")
g = new stzGraph("cycle-1")
g.AddNode("customer-phone")
g.SetNodeProperty("customer-phone", "kind", "world")
g.SetNodeProperty("customer-phone", "admitted-by", "the opening scope")
g.AddRule(oRule)
? g.RulesAreSound()
#--> 1
g.AddNode("loyalty-club")
g.SetNodeProperty("loyalty-club", "kind", "world")
g.RulesReport()
#--> Rule report 'cycle-1': 1 finding(s), 1 error(s), 0 warning(s) -> UNSOUND (errors present)
#      [scope] 1 finding(s)
#        ERROR the-lock @ loyalty-club -- a world entered the cycle with no written admission
g.SetNodeProperty("loyalty-club", "admitted-by", "a notebook entry, and one exit written")
? g.RulesAreSound()
#--> 1
```

The idea of a loyalty club arrives, and the cycle is no longer sound! The court answers `UNSOUND (errors present)`, and names the rule and the node: `ERROR the-lock @ loyalty-club`. The cycle is sound again when the idea carries its written admission.

**Try payments without a subscription.** The project's rule was to test without committing: a payment institution's free sandbox, and the library's simulated services, and no subscription before a gate that the notes call the go-live gate. The library's side of it is a payments sandbox that is not agreeable. It behaves like a gateway: a decline is an answer, an outage is not, and a capture cannot be made twice. The amounts are integers in minor units, so 4200 is forty-two euros. What does it answer to a token it was told to decline, to an outage, and to a second capture? Run it:

```haro
oPay = new stzPaymentsSandbox()
oPay.DeclineTokenQ("tok_chargeback")
? oPay.Authorize(4200, "tok_chargeback")[:status]
#--> declined
oPay.FailNextQ()
? oPay.Authorize(4200, "tok_visa")[:status]
#--> refused
aAuth = oPay.Authorize(4200, "tok_visa")
? aAuth[:status]
#--> authorized
oPay.Capture(aAuth[:id])
? oPay.Capture(aAuth[:id])[:why]
#--> this authorization was already captured
```

Three answers, and none of them is an empty string: `declined`, `refused`, and `this authorization was already captured`.

And the production gate refuses to open while a fake is still bound, even for an entitled person. Here the live binding is an HTTP sandbox standing in for an adapter, as the guard does it: the registry holds only the name of the secret. What does the production gate answer when the owner, entitled, asks for production while the fake is still bound? Run it:

```haro
oReg = new stzServiceRegistry("shop")
oReg.BindSandbox(:payments, new stzPaymentsSandbox())
oDel = new stzDelivery("shop")
oDel.AddBackend("api", "linux")
oDel.UseServicesQ(oReg)
oDel.NeedsServiceInQ("api", [ :payments ])
oDel.DeployTo(StzDeploymentSiteQ("host1"), "api")
oDel.SetActor( HumanActor("owner") )
? oDel.Deploy(:Production).WasCommitted()
#--> 0
? oDel.Log().EntriesOfLevel(:error)[1][:message]
#--> REFUSED -- the external surface is not production-ready
? oDel.WhyServicesNotReady()
#--> sandbox-in-production: still bound to a SANDBOX in a production phase -- a fake must never ship
oDel.ServicesQ().BindLiveQ(:payments, new stzHttpSandbox(), "payments_key")
? oDel.ServicesAreProductionReady()
#--> 1
```

The owner is entitled, and he is refused! Nothing is committed, and the log says why: `REFUSED -- the external surface is not production-ready`; the reason under it is the rule: `a fake must never ship`. It opens when the binding is real.

**The constellation.** When he reversed the order of the work, the project's architecture was redrawn as a constellation of five worlds on a shared ground. The worlds are the customer's phone, the kitchen screen, the merchant's workshop, management, which is the first application kept and put to sleep, and the publisher's console. The shared ground is identity, the catalogue, orders, payments and the fleet. In the library, the last world in the order of work can be put to sleep; a call to it is refused with its reason, and it is revived when its turn comes:

```haro
oCon = new stzSuperApp("neighbourhood")
oCon.AddWorld("customer", StzAppQ("customer"))
oCon.AddWorld("kitchen", StzAppQ("kitchen"))
oCon.AddWorld("supplier", StzAppQ("supplier"))
oCon.Bond("customer", "kitchen", "send-order")
oCon.Bond("kitchen", "supplier", "order-produce")
oCon.GovDeclareRisk("send-order", 1)
oCon.GovDeclareRisk("order-produce", 2)
oCon.GovGrant("customer", "send-order")
oCon.GovGrant("kitchen", "order-produce")
oCon.GovSetAuthority("customer", :Delegated)
oCon.GovSetAuthority("kitchen", :Delegated)
oCon.Retire("supplier")
? oCon.CallAcross("customer", "kitchen", "send-order")
#--> 1
? oCon.CallAcross("kitchen", "supplier", "order-produce")
#--> 0
? oCon.Why()
#--> target world 'supplier' is not active.
oCon.Revive("supplier")
? oCon.CallAcross("kitchen", "supplier", "order-produce")
#--> 1
```

The call across the bond passes; the call to the sleeping world does not, and the reason is one line: `target world 'supplier' is not active.` Revived, it passes.

**The speed budget.** The owner's first priority was speed, so speed had to be a promise judged by something, not an aspiration. I hold this as a view, not a result. The budget has three numbers: the time to first display, the time to react to a tap, and the time for an order to reach the kitchen. The library declares them next to the code as expectations, judges them against what was measured, and a breach fails the same gate as a security finding. The bounds and the samples in this block are mine, to show the form; they are not the project's budget. What does a breach look like? Run it:

```haro
oMon = StzPerfMonitor("remote-control")
oMon.NewTimer("first.display.ms").Record(900)
oMon.NewTimer("tap.ms").Record(40)
oMon.NewTimer("order.to.kitchen.ms").Record(1800)
oSla = StzSla("speed-budget")
oSla.ExpectP95("first.display.ms").Under(1200)
oSla.ExpectP95("tap.ms").Under(80)
oSla.ExpectP95("order.to.kitchen.ms").Under(2500)
oSla.CheckAgainst(oMon)
oSla.Show()
#--> SLA speed-budget -- 3 expectation(s), last check: MET.
#      [MET] p95-first.display.ms-under-1200: measured 900 (must be <= 1200)
#      [MET] p95-tap.ms-under-80: measured 40 (must be <= 80)
#      [MET] p95-order.to.kitchen.ms-under-2500: measured 1800 (must be <= 2500)
oMon.MetricQ("order.to.kitchen.ms").Record(3100)
oSla.CheckAgainst(oMon)
oRep = new stzRuleReport("cycle-gate")
oRep.Ingest(oSla.Findings())
? oRep.IsSound()
#--> 0
? oSla.Findings()[1][:message]
#--> p95-order.to.kitchen.ms-under-2500: measured 3100 (must be <= 2500)
```

Three expectations met, then one order takes 3100 milliseconds and the gate is no longer sound. The finding says it in the budget's own words: `p95-order.to.kitchen.ms-under-2500: measured 3100 (must be <= 2500)`.

One more thing the project learned, and the library does not carry. The project's file of interface rules is experience in a few lines: one clear action per screen; undo instead of confirm; a button that is refused is disabled in view, never hidden. And one test: a simulated first day on an empty database found the gravest hole, that no supplier could be created in production. Those rules were forged, in the project's own count, by eleven iterations and a campaign of twenty-two simulated tests with seventeen fixes. The library carries none of them as a check. So by the rule of this chapter they are the project's lesson and not the library's, and I tell them here without a block.

## 4. The decision, and what I refused

**I refused the grand system in one piece.** After two years of rich specification, the project nearly ended. The estimate of 2025 stays the reference for the project's scope; it is never to be presented as today's calendar. What replaced it is the doctrine of this chapter: deliver small, fast and useful.

**I refused to throw the first application away.** When the owner reversed the order, the application already built was kept, dormant, until the first version of the new order was in production. The project's own words for it: nothing is thrown away.

**I refused silent drift.** The Lock exists because a project that has failed once drifts without anyone deciding to. That is my view. A second change of course before the first version runs in production is refused, and so is an idea that enters the cycle without a written exit.

**I refused the agreeable fake.** A double that silently answers with an empty string produces a test that passes for the wrong reason. The sandbox declines when a gateway declines, refuses when a gateway is down, and refuses a second capture. And I refused a fixed fee before the go-live gate: no subscription to a payment institution before the owner's written go.

**I refused to credit the owner with what a simulation said.** The project has carried a rule since July 2026, that no action on its screens takes more than two gestures. The site prints it as part of the first amendment, and the project's documents carry it as the owner's constraint. Its earliest source is a line in the file of simulated answers of 3 July, written by me and a session. The project set it for itself, from its own simulation of his answers, and kept it. I tell it that way. What he did say, and what I take as his, is the priority on speed.

**I refused to say the library was born of his need.** The constellation design, the virtualization plan, the registry, the payments port and the performance judgment were all first committed after the reversal of 4 July. The plan is dated 23 July, and the performance study 29 July. The site says carefully that the project needed these things and that the library carries them. I will say no more than that. The record does not say which came first, his need or the parts: it shows the project finding them in the library, and I leave the order open.

## 5. The court

`06_stzsuperapp_narrated` proves the constellation: worlds joining, a call across worlds needing both worlds active, a declared bond and governance, and a retired world breaking its bonds and reviving. `service_delivery_narrated` proves that a production deployment by an entitled actor is refused while a fake is bound, with every reason logged, and that it opens once the binding is real. `payments_port_narrated` proves the sandbox's state machine: capture once, capture only an authorised charge, refund no more than captured, a decline is an answer and an outage is not. `judgment_narrated` proves an expectation declared in the operational vocabulary and judged against measured numbers, a breach as a finding that fails the gate, and an expectation on a number nobody measures as an error and never a silent pass. `graphrule_object_narrated` proves the rule as an object attached to a model, with the operators the Lock's construction uses.

## 6. The field, and where it leads

The field leads in storage, in queries and in ecosystem. The library's own study of the performance field, written against the tools of early 2026, says it without softening: no time-series database, no query language for it, no dashboards, by design; export instead. Among the five properties it claims against them, the one this chapter uses is the first: nothing in the field couples a budget to the codebase's own rule system.

The field leads in the browser. The restaurant's worlds run in the browsers of customers and the kitchen, and I found nothing in the library that measures a first display or a tap there. The library's monitor observes a server, and the SLA judges whatever numbers are recorded into a timer. The owner's measurement protocol, at the seventy-fifth percentile on a mid-range phone, cannot be declared exactly in the library's terms, which offer the fiftieth, the ninety-fifth and the ninety-ninth.

The field leads on real services. A double is not the service, and the plan says so: you still need at least one real run before production, and recorded responses drift. The real providers lead in the edge cases the sandbox does not model.

And the super-app hosts lead in installed base. The design names what the industry's super-app has, a store, a review, a native bridge, and replaces it; it does not claim users.

## 7. The limit

What is built: the constellation of worlds with its bonds and norm-gated crossings, retirement, revival, hot swap and nesting; the payments sandbox and the production gate; the speed budget declared and judged; the graph rules the Lock's construction uses.

What is designed: the Lock as a rule of the library, of which the record has no code; the near-natural idiom of the constellation, with the verbs the design names and the class does not have.

What is absent: the restaurant's live payment adapter, which the library's charter calls a later task and the owner's decision. A measurement of the budget on a real mobile network, which the project's dashboard of 23 August postponed to the next cycle. The interface rules, the two-gesture rule among them, as checks, a seventy-fifth percentile expectation and browser-side timing, of which no document of the library holds a design. And the state of the platform after 25 August 2026, where the record ends. Nothing in it says the first version reached production at the restaurant, passed the go-live gate, or took a real order from a real customer. The record is silent on what happened after 25 August 2026, and I say so. Of the owner's tightened speed thresholds I print none, and say only that such a budget exists.

And what runs today is ordinary. The worlds are single HTML files, one per world, with a vendored framework, no build step and no content network. The server is a Node program of a few hundred lines that uses five of Node's own modules, serves the worlds on the local network, and keeps one thing: a journal, chained by hashes, replayed at restart. The first management application has a phone wrapper around a web view. None of it runs on the Softanza engine. The library is the project's design reference. The constellation is, in the site's words, a design the library can run. The restaurant does not.

## 8. Six doors

**The programmer.** You declare worlds and bonds and run a constellation in which a call to a world that is not yet active is refused with its reason. The restaurant's own code, however, is a web application.

**The analyst.** Rigour in numbers was the contract of the first application: a due date computed from the invoice date, a date required, a debt with no due date made visible.

**The designer.** Fifteen interface rules from one directive, the three-second test; and a refused button is disabled and visible, never hidden. On who held the phone in the eleven iterations, the project's files say both, the real user and me, and the chapter does not choose.

**The decision-maker.** The owner accepted the Lock in writing, tightened the speed budget himself, and kept the gate on fixed fees. The library's mirror is a deployment that an entitled person may commit and that is still refused over a fake.

**The educator.** The record supports only a small thing: the first application taught its user by doing, with guides whose words leave no doubt. There is no educator in this story, and I say so.

**The agent.** An agent can drive a production deployment and change nothing: the gate passes the services, nothing is committed, and the reason given is the actor and not the services. In the project, the agent is the session working beside me under the Lock, with a person deciding.

## 9. Exercise

Declare your own Lock for one cycle. Write the worlds of the cycle you are in, three of them, as a restaurant would: the customer's phone, the kitchen screen, and one more, each with the written reason it is in. Add a fourth, the idea you had this morning. Run the court. Change the declaration, not the court, until it says the cycle is sound.

```haro exercise
? YourGraph.RulesAreSound()
#--> 1
```

The court will tell you the circumstance and the rule. It will not write the declaration. If you want a harder one, add a rule about the actions of your cycle, and find the action that costs a third gesture.

Chapter 29 is a bank in Niamey, where an organisation is judged by its own chart, under a regulator's rules, by a program that reads the chart as data. The chart says what is, the rule says what must be, and the verdict names the rule and the place.
