---
id: what-the-projects-did-not-prove
part: 6
number: 31
title: What the projects did not prove
spine: false
narrations: [stz-built-on-real-world-need.md, stz-service-virtualization-code-first-subscribe-later.md, stz-getting-paid-and-paying-narration.md, stz-system-dev-to-deploy-narration.md]
site: [customers, forged, platforms, estate]
guards: [service_registry_narrated, full_scope_model_narrated, payments_live_adapter_narrated, sound_mu5_narrated, deployment_narrated, orgrule_narrated, governance_narrated]
stage:
  built: "the three lessons the library carries, each with a guard (a fake never ships; a chart judged under a regulator's rules; authority against risk, with its lineage); refusals that show an absence instead of hiding it"
  designed: "the customers' declarations written as Softanza's own; the five-row guarantee sheet; a runtime that is the language's own running the library; the declared machine on a board"
  absent: "any customer platform on the engine; a word from the bank; the restaurant's use after 25 August 2026; the hub; an offline mechanism in the library; a live payments run against the hub's sandbox; a named person's verdict on any of it"
status: draft
rulings: ["12.5", "12.10", "12.13", "12.21", "12.22", "12.29", "12.30"]
research: research/ch31.md
---

## 1. The concept, as the field holds it

The field has three habits for saying what a piece of work has proved.

The first is the reference: a logo on a home page, a customer story of two pages, the sentence "trusted by". It proves that someone paid or signed. It does not say what they ran, for how long, or what they said.

The second is the readiness scale. NASA's technology readiness levels, later an international standard, name how far a technology has travelled from a laboratory to the place it was built for. The highest level is a system proven in operation. It is a vocabulary of stage, and this book uses one of its own (built, designed, absent).

The third is the limits section. An empirical study must state its threats to validity; a machine-learning model ships with a card whose last part is its caveats; an artifact submitted to a research conference is badged by what someone else did with it. This is the form closest to this chapter, and the one most often skipped when the reader is a buyer.

What the three have in common is that the claim and its proof travel apart. A page says "used by", and the proof is a trust in the page. (General knowledge, not a study of the record.)

## 2. The first principle

The record gives two sentences, and they are one. The site says: "Nothing is a reference until a document proves it." And, of what the author remembers: what "no file proves is not listed."

**A project proves exactly what a document, a file, a run and a named person reach, and the page says where they stop.** [AUTHOR: Is this the principle in your words, or the site's two sentences as they stand?]

## 3. The Softanza form

This chapter is the other half of chapters 28 to 30. Those told what three projects taught the library. This one says, project by project, what they did not prove. I did not write it after the fact, to be modest. The site carries the same page, with the same heading, and it was written before any reader asked.

The shape of the answer is a table of three columns for each project: the claim, the document or file that proves it, and what is absent. I leave a cell empty when I cannot name what fills it. And I will not fill the third column from memory.

Before the tables, five small blocks. Each is a place where the library shows an absence by refusing, instead of passing silently. They are the chapter's sentence, written as code.

**A dependency declared and never bound is an error.** The surface of a solution is declared before anything is bound. A declared service that nothing backs is counted as a finding, not a pass, and asking for it raises where the mistake is. This is the first unproved thing the restaurant's lesson cannot hide: no live payments service is bound anywhere in the record.

```haro
oReg = new stzServiceRegistry("shop")
oReg.DeclareMany([ :mail, :payments ])
? @@( oReg.UnboundServices() )
#--> [ "mail", "payments" ]
? oReg.Findings()[1][:invariant]
#--> unbound-service
? oReg.IsSound()
#--> 0
try
	oReg.Service(:payments)
catch
	? cCatchError
done
#--> stzServiceRegistry(shop): nothing is bound for service 'payments'. Bind it (or BindLive it) before use.
```

**What a rehearsal can claim, and what only the target can.** The platform model gives three verdicts for the same operation. *Refused*: the target forbids it. *Native*: the host can really do it. *Rehearsed*: the target allows it and the host lacks it, so the run proves only the plan. Reading a pin on a development machine is rehearsed and never native. The word depends on the machine this book was run on: a Windows PC has no such pin, and a board that has one would print `native` for the same line.

```haro
oSol = new stzPlatformProfile("kiosk")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oSol.WithApp(:firmware, :ESP32)
oFw = oSol.App(:firmware).System()
? oFw.ReadPin(4)
#--> rehearsed
try
	oFw.Spawn("worker")
catch
	? cCatchError
done
#--> scope 'esp32' (espidf) forbids 'process' -- spawn 'worker'. This target has no such capability.
oFw.Show()
#--> Scope: esp32 (espidf)
#      [rehearsed] read pin 4
```

The library's own comment above this code says the last step, flashing a board, "remains a planned external action".

**The live payments adapter exists, and refuses to guess.** The code for the live hub exists. It has never been run against the hub's sandbox. Given no credentials, it refuses before any network call and says what is missing. The host in this block does not exist, and nothing reaches it:

```haro
oAd = new stzPispiHttpAdapter()
oAd.WithParticipant("shop")
oAd.WithBaseUrl("https://pispi.example")
oAd.AsLive()
? oAd.IsSandbox()
#--> 0
try
	oAd.Request("GET", "/comptes", [], [])
catch
	? cCatchError
done
#--> stzPispiHttpAdapter: no credentials. Give it the store and an actor: WithSecretsFrom(oStore, oActor).
? oAd.TokensFetched()
#--> 0
```

The library has a script that tries the live run. I ran it once, with none of its variables set, for this chapter. It printed the word UNPERCEIVED, named the four variables that are missing, and said that nothing about the live adapter is perceived until a named person has watched a payment land. It ended without failure. The run was postponed, by me, for a reason that is not the library's: it needs the organisation's involvement. A run that could not happen is reported as unperceived. It is not reported as a pass or a failure.

**A feature that waits for a named person.** In the sound plane, the library holds as data the verdict of a person on a thing only a person can judge. While the verdict is UNPERCEIVED, the verb that would claim the result refuses and says why. Where a person has said yes, the verdict carries the date and their words:

```haro
oVoice = StzSoundFormantVoiceQ()
oVoice.Sing("la la la", "c4 e4 g4")
? oVoice.Refusals()
#--> 1
? oVoice.LastError()
#--> Sing is not available YET: the formant voice has not been heard by the author (sound_mu5_demo.ring plays it). SAPI was measured and does not hold a pitch (measured 2026-09-26: +-6 st asked, +-2.5 st given, up to 407 cents off, 286-575 cents of wander within a syllable -- it speaks, it cannot hold a note). Until the author calls the formant voice singing, Vowel and VowelsQ are what this voice honestly does
aVerdicts = StzSoundSingingVerdict()
? aVerdicts[:formant][:verdict]
#--> UNPERCEIVED
? aVerdicts[:retuned][:verdict]
#--> SINGING
? aVerdicts[:retuned][:date]
#--> 2026-09-27
? aVerdicts[:retuned][:said]
#--> the retuned voice is somehow singing, open Sing()
```

This is the form of the line chapter 33 says the customers' runs do not yet have: a date, a person, and a sentence. The record also carries the person's name beside it, and I do not print it here. (SAPI is the operating system's speech interface.)

**A pre-flight that says "feasible" without touching a host.** The deployment's pre-flight refuses a host that is too small. For a host whose provider is a cloud, it says feasible and "provision on aws", without any account. A feasibility is a plan, not a verification. The design file says it plainly: what remains is the verification against a real host or account, gated by infrastructure. The figures below are illustrative.

```haro
oBrain = new stzDelivery("shop")
oBrain.AddBackend(:api, :LinuxServer)
oBrain.RequiresIn(:api, StzResourcesQ().SetMemoryQ(2048).SetComputeQ(2).SetStorageQ(20))
oSmall = new stzDeploymentSite("tiny")
oSmall.SetKindQ(:Server).SetCapacityQ(StzResourcesQ().SetMemoryQ(512).SetComputeQ(1).SetStorageQ(5))
oTiny = new stzDeployment(oBrain)
oTiny.SetTarget(:api, oSmall)
? oTiny.Feasible()
#--> 0
? oTiny.Feasibility()[1][5]
#--> SHORTFALL -- host too small
oCloud = new stzDeploymentSite("pool")
oCloud.SetKindQ(:Server).SetProviderQ(:aws)
oPool = new stzDeployment(oBrain)
oPool.SetTarget(:api, oCloud)
? oPool.Feasible()
#--> 1
? oPool.Feasibility()[1][5]
#--> provision on aws
```

Now the tables. Every cell is from the record, read on 8 October 2026. A line count or a file date I read myself is labelled as mine.

### The restaurant in Lyon

| Claim | Proof | What is absent |
|---|---|---|
| The platform exists, and its first delivery was made | the site: an amendment closed on 4 August 2026; the project's commit "iteration 1" of 15 August; a server of 565 lines that I read; the last commit, 25 August 2026, 13:07 | anything after 25 August: production, a real order, the planned go-live gate. The record is silent |
| The restaurant runs it | a day of field measurements with two phones, 19 August | a sentence that says it runs. Chapters 1 and 33 write "runs" |
| No growth of scope during a cycle (the Lock) | the pact and the notebook: private documents | the Lock as code. Chapter 28 shows the nearest the library gives |
| Payments can be tried without a subscription, and a fake never ships | the registry and the delivery gate, with their guards | the live payment adapter for the restaurant: "a later desk" in the library's own design file. Nothing is bound live |
| The constellation of worlds | the restaurant's map of its worlds; the library's super-app class, with a guard | the restaurant on the constellation: its worlds are single-file web pages, and the map says it is a map, not an implementation |
| A speed budget is a promise | the library's service-level object, with a guard | a measure on a real 4G network: the project's own notebook defers it to the next cycle |
| The interface rules were forged with the owner, phone in hand | the project's file says eleven iterations with the real user | who held the phone. The site and chapter 2 conflate two facts |

### The bank in Niamey

| Claim | Proof | What is absent |
|---|---|---|
| The bank runs the author's assessment product | the installation guide delivered to the bank; a licence file | a word from the bank: who declares the chart, for how long, how many people use it. And no date of delivery: the files carry file-system times, which are not dates |
| The product is "built with Softanza" | the author built both | the product does not call the library. It is a Python application with a small web server; I searched its code, and found no regional or Basel check and no call to the library |
| The regulator's rules judge the chart | the library's validator of three rules and of segregation of duties, with guards | the validators inside the product; an article of the central bank's text for the three rule codes; a finding read by an auditor |
| A rule file for the bank | a file of two regional rules that loads | it judges nothing: on a chart with no board it reports sound |
| The product's interface rules came from the bank | the interface constitution's rules 117 to 124 | the evidence line in the constitution says a banking-supervision product of a sibling platform, not this bank's installation. The site attaches them to the bank |

### The organisation in the field

| Claim | Proof | What is absent |
|---|---|---|
| The organisation chose my offer | the offer of 5 August 2026 was retained; the design study of 8 October 2026 | the hub: nothing of it is in production, and the study's version 1.2 is submitted for validation. And who chose, against what: the record is silent |
| Rules are data that a person changes without a programmer | the library's rule clauses and the governor that names a dead rule | a text form for clause rules; a version record with undo, which the study promises; the study's own rule notation is not the library's |
| An agent prepares, a person decides, with the authority at the time | the governance object and its lineage, with guards | a person bound to a signed-in account; a hub to do it in |
| Offline by default | the study's word that the browser-side outbox is already in service | in the library: no queue, no outbox, no synchronisation. The site calls it "a gap, not a lesson learned". Chapter 30's last block is the whole of it |

### Across the three

| Claim | Proof | What is absent |
|---|---|---|
| The platforms run today on ordinary stacks | the site's own page: single-file web worlds and a small Node server; a Python application; the hub not built | no platform runs on the engine. The site says so, and every repository I opened agrees |
| Their declarations "are being written as Softanza's own" | the platforms page and the forged page, as intent | I searched, on 8 October 2026, and did not find them as a file: in the restaurant's repository no code file declares an app, a constellation or a platform; in the bank's delivery, none; in the organisation's study folder, none (its annex uses a notation that is not the library's). The record shows the intent and the maps, not yet the declarations |
| A change of engine, not of plan | the principle: rewriting was refused | the move itself; who moves first; who perceives it |
| A solution writes its guarantee sheet in five rows | the vision asks for it | no solution has one; no class, fixture or guard in the library has the sheet |
| The runtime beneath is the language's own | the charter ratified on 1 October 2026; its stages pass on its own fixtures | Haro does not run the library. The bridge runtime has passed the library's suite on Windows in a session's notes; the Linux pass is the next step. I print no percentage. This book's blocks run on the former runtime, 1.27 |
| A live host verifies a deployment | the deployment design | the verification is infrastructure-gated. Local sites run for real; remote transfer is "a later slice" |
| The payments plane works against the hub's sandbox | the twin, served over HTTP, with a guard | the sandbox run: unperceived, postponed. Production is never from this plane |
| A named person has said what they saw | a drum, and the retuned voice, in another plane | any of the three platforms |

### What the study of the record did not measure

The comparative study that read the record says, in its own paragraphs headed "Not measured", what it could not support. It did not run what it read: its ruling on the three projects says "Nothing in it was run". It did not measure whether Haro's runtime runs the library. It did not test whether two published speed benchmarks hold today, and both were run on the former runtime. Some guards in the system folder took their totals from design documents, and one of them still says forty-five where the guard now holds more. The gallery's forty-one pictures were judged by a model, and no person has looked at them. The restaurant's speed budget has no real 4G measure. The study applies its own perception law to itself, which is why I trust the paragraph.

## 4. The decision, and what I refused

**I refused the author's memory as evidence.** The site lists nothing that I remember and no file proves. The same rule bound the bank: I know the product, because I built it, and what the bank's own people did with it is not in a file.

**I refused to call the library the origin of what it only uses as an example.** The forged page says "example" where the library holds a project as its example and not as its origin. And I will not repeat a sentence in the study of 12.29 that says a lesson was "born of the client's need". The registry and the SLA were first committed after the reversal of 4 July, and the order of the commits makes "born of" unproved. What I can say is "needed" and "carries".

**I refused two wordings of my own.** In chapters 1, 2 and 33 I wrote that the bank "runs" a product "built with" Softanza, and that the restaurant "runs" a platform. The record shows a Python application that does not call the library, built beside it by the same person, and for the restaurant a first delivery and a field day, then silence after 25 August. The honest wording is *built by me, under the discipline the library now carries*, and *delivered and field-tested*. [AUTHOR: May I correct chapters 1, 2 and 33 to those wordings? Chapter 1 is your text, and I have changed none of it. And shall the block under "a date, a person, and a sentence" print the person's name too, as the record's form of "named"? That is yours to say.]

**I refused a stage word the repository does not carry.** The site's estate page says it: never called available before it is. A piece of work that reaches a person through a sense is perceived by a person, and until then it is unperceived, which is a state and not a failure.

**I refused to print a percentage.** I have said aloud how far the bridge runtime has come. The study ruled that the figure should not be printed without the guard that produces it. I agree.

## 5. The court

`service_registry_narrated` proves that a declared service nobody backs is an error finding, that an unbound service raises, and that a sandbox in production is a violation. `full_scope_model_narrated`, scenes 5 to 8, proves the three verdicts: refused, rehearsed, native. `payments_live_adapter_narrated` proves the adapter against a twin served over HTTP, an adapter without credentials that refuses to guess, and the scenario that says stage (b) is unperceived. It starts real server processes, and the book does not run it; it only counts its assertions. `sound_mu5_narrated` proves, in its fifth scene, that while the verdict is unperceived `Sing` returns nothing and says why. `deployment_narrated` proves that an undersized host is not feasible, and that an assistant rehearses and commits nothing; it writes a scratch folder beside itself, so the book does not run it either. `orgrule_narrated` and `governance_narrated` carry the other two lessons.

The court of this chapter's subject is not a guard. It is a line of the record, of the form the estate's law prescribes: a date, a person, and what they said. The library holds one such line in its data, in the sound plane. The estate holds one in its record, and chapter 33 tells it.

## 6. The field, and where it leads

The field leads in production. Ordinary stacks run real workloads for real users, including, on the site's own page, the three platforms of this part.

The field leads in references at scale. The site prints two references and a design study, and quotes no number of countries and no number of developers. A buyer reading a logo wall sees more.

The field leads in live infrastructure. Provisioning tools drive real providers every day. The library's deployment stops short of a real host, and the fifth block shows where.

The field leads in hardware in the field. The declared machine boots and judges itself in an emulator, and the vision says no customer runs on it. Its guarantee text says four of four promised, three kept in the emulator; the fourth, surviving a cut, waits for a watchdog on a real board, and the board is on order.

The field leads in speed. The runtime Softanza measured itself against was faster on every row, by a factor between one and two, and both benchmarks were run on the former runtime.

The field leads in pictures judged by people. Forty-one pictures and text sections of the gallery were judged by a model: twenty right, nine wrong, twelve uncertain. The record says that no human has looked at them.

Where I think the record stands apart is that its limit is a page, with a heading, written before any reader asked. Every stage has a word. A feature can be built and still refuse until a named person has spoken. And a live run that could not happen is reported unperceived, never a failure and never a pass.

## 7. The limit

This whole chapter is a limit. Here is its sum in the stage words.

What is built: the three lessons that are proved. *A fake never ships*: the registry and the delivery gate. *An organisation is judged by its own chart under a regulator's rules*: the organisation chart and its validators. *Authority is not permission, and a decision keeps its authority at the time*: the governance object. Each has a file of the library that carries it, a guard that resolves, and a block already kept in a neighbouring chapter. The limit of each is in the tables: a sandbox is bound and no live payment adapter is; the bank's product does not call the chart validator; no hub exists and offline is a gap.

What is designed: the customers' declarations written as Softanza's own; the five-row guarantee sheet; the runtime that is the language's own, running the library; the declared machine on a board.

What is absent: any customer platform on the engine; a word from the bank; the restaurant's use after 25 August; the hub; an offline mechanism in the library; a live payments run against the hub's sandbox; a named person's verdict on any of it.

The sum of every absent cell is the one line chapter 33 says is still owed: *the solution ran on Softanza's own engine, and this is what the user said.* [AUTHOR: The site says the customers' declarations are being written. I found no declaration file in the three projects' repositories. Do they live in a repository I did not search, or are they still to be written? The chapter's word for them, designed or absent, depends on it.]

## 8. Six doors

**The programmer.** Your demo is a rehearsal until a target has run it. Ask the scope whether the line was native, rehearsed or refused, and write the same word beside your own claims.

**The analyst.** When you cite a project, write three columns: the claim, the document, and what is absent. Do not fill the third from memory.

**The designer.** A feature that no person has seen or heard ships shut, and says so. The stage is a state of the design and not an apology.

**The decision-maker.** Read the stage word before the testimonial. "Built" is a statement about a guard. "Runs at a customer" is a statement about a document, and you can ask for it in writing, with a name beside it.

**The educator.** Teach the difference between a project that taught the library and a project that runs on it. The first is proved here, and the second is the line still owed. Unperceived is a state, not a failure.

**The agent.** You may read the tables and quote any cell. You may not turn an absent cell into a present one. If you do, the next reader of the record will find your sentence and the missing file side by side.

## 9. Exercise

Declare the surface of one project of yours: a mail service, a payments service, and one more of your own. Before you run anything, write the line you expect under each of three questions: which services are unbound; whether the registry is sound; which are unbound once the mail service has a sandbox bound.

```haro exercise
oReg = new stzServiceRegistry("my-project")
oReg.DeclareMany([ :mail, :payments, :your_service ])
? @@( oReg.UnboundServices() )
#--> what you expect
? oReg.IsSound()
#--> what you expect
oReg.Bind(:mail, new stzMailSandbox())
? @@( oReg.UnboundServices() )
#--> what you expect
```

Then, on paper, make the table of three columns for the project you know best. Leave empty what you cannot name. On the last line write who perceived it, on what date, and what they said, or the word "unperceived" and why.

The exercise has no answer to be checked first. The question the tutor asks is: which cell did you fill from memory?
