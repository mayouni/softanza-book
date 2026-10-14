# What the projects show, and what comes next

Source: Chapter 31. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: what the three projects delivered, each with a document (a first delivery, field-tested; a product installed under licence; a design study built with the organisation's teams); the three lessons the library carries, each with a guard (a fake never ships; a chart judged under a regulator's rules; authority against risk, with its lineage); refusals that show an absence instead of hiding it; designed: the five-row guarantee sheet; a runtime that is the language's own running the library; the declared machine on a board; absent: any customer platform on the engine; the customers' declarations written as Softanza's own, as files; a word from the bank; the record of the restaurant after 25 August 2026; the organisation's hub; an offline mechanism in the library; a live payments run against the central bank's sandbox; a named person's verdict on any of it

Run: 5 of 5 blocks kept their promise, on 2026-10-14 12:01 UTC+01:00.

In this chapter I say, project by project, what the three projects of chapters 28 to 30 show today, and what each one makes the next step. I start with the field's three habits for saying what a piece of work has shown. Then I run five small blocks in which the library shows, by refusing, where a stage ends, and I lay out the tables: for each project, the claim, the document or file that backs it, and what comes next. I say what I refused, the author's memory as evidence first of all, and I give the court, the field and the limit in the stage words. The principle is the chapter's own sentence: a project shows exactly what a document, a file, a run and a named person reach, and the page says where they stop.

## 1. The concept, as the field holds it

The field has three habits for saying what a piece of work has shown.

The first is the reference: a logo on a home page, a customer story of two pages, the sentence "trusted by". It shows that someone paid or signed. It does not say what they ran, for how long, or what they said.

The second is the readiness scale. NASA's technology readiness levels, later an international standard, name how far a technology has travelled from a laboratory to the place it was built for. The highest level is a system proven in operation. It is a vocabulary of stage, and this book uses one of its own (built, designed, absent).

The third is the limits section. An empirical study must state its threats to validity. A machine-learning model ships with a card whose last part is its caveats. An artifact submitted to a research conference is badged by what someone else did with it. This is the form closest to this chapter, and the one most often skipped when the reader is a buyer.

What the three have in common is that the claim and its proof travel apart. A page says "used by", and the proof is a trust in the page. (General knowledge, not a study of the record.)

## 2. The first principle

The record gives two sentences, and they are one. The site says: "Nothing is a reference until a document proves it." And, of what the author remembers: what "no file proves is not listed."

**A project shows exactly what a document, a file, a run and a named person reach, and the page says where they stop.** This is the chapter's own sentence, drawn from the site's two. The site's words are the two quoted above, from its customers page and its forged page.

## 3. The Softanza form

This chapter is the other half of chapters 28 to 30. Those told what three projects taught the library. This one says, project by project, what each project shows today and what it makes the next step. Parts of Softanza are in production, and others are in development. I did not write this chapter after the fact, to be modest: the site's forged page already carries a section on the same subject.

The shape of the answer is a table of three columns for each project: the claim, the document or file that backs it, and what comes next. I leave a cell empty when I cannot name what fills it. And I will not fill the third column from memory.

Before the tables, five small blocks. Each is a place where the library shows, by refusing, where a stage ends, instead of passing silently. They are the chapter's sentence, written as code.

**A dependency declared and never bound is an error.** The surface of a solution is declared before anything is bound. A declared service that nothing backs is counted as a finding, not a pass, and asking for it raises where the mistake is. This is the first step the restaurant's lesson points to: binding a real payments service, which the record does not yet hold. What does the registry answer when the payments service is asked for and nothing backs it? Run it:

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

> run: kept

Two services declared, none bound, and the registry says so itself: `nothing is bound for service 'payments'`!

**What a rehearsal can claim, and what only the target can.** The platform model gives three verdicts for the same operation. *Refused*: the target forbids it. *Native*: the host itself can do it. *Rehearsed*: the target allows it and the host lacks it, so the run shows only the plan. Reading a pin on a development machine is rehearsed, not native. The word depends on the machine this book was run on. A Windows PC has no such pin, and a board that has one would print `native` for the same line. What does the board's scope answer to a pin read, and to a request to spawn a process? Run it:

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

> run: kept (touches the system)

The pin read answers `rehearsed`, and the scope refuses the process with `forbids 'process'`!

The library's own comment, in the class that lowers a rehearsal to a real artifact, names the next step: the last one, flashing a board, "remains a PLANNED external action".

**The live payments adapter exists, and refuses to guess.** The code for the live payments system exists. Its run against the central bank's sandbox has not happened yet, and it is the next step. Given no credentials, it refuses before any network call and says what is missing. What does it say when it is asked for accounts and holds no credentials? The host in this block does not exist, and nothing reaches it:

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

> run: kept

The adapter answers `no credentials`, names what would fill the gap, `WithSecretsFrom(oStore, oActor)`, and `TokensFetched()` stays at `0`.

The library has a script that tries the live run. I ran it once, with none of its variables set, for this chapter. It printed the word UNPERCEIVED, named the four variables that are missing, and said that nothing about the live adapter is perceived until a named person has watched a payment land. It ended without failure. The run was postponed, by me, for a reason that is not the library's: it needs the organisation's involvement. A run that could not happen is reported as unperceived. It is not reported as a pass or a failure.

**A feature that waits for a named person.** In the sound plane, the library holds as data the verdict of a person on a thing only a person can judge. While the verdict is UNPERCEIVED, the verb that would claim the result refuses and says why. Where a person has said yes, the verdict carries the date and their words. What does the formant voice answer when it is asked to sing, and what does the retuned voice's verdict hold? Run it:

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

> run: kept

The formant voice refused to sing: `Refusals()` reads `1`, and the message begins `Sing is not available YET`! The verdict of the formant voice stays `UNPERCEIVED`. The verdict of the retuned voice reads `SINGING`, with the date `2026-09-27` and the words `the retuned voice is somehow singing, open Sing()`. This is the form of the line that chapter 33 sets as the next milestone for a customer's run: a date, a person, and a sentence. The record also carries the person's name beside it, and I do not print it here. (SAPI is the operating system's speech interface.)

**A pre-flight that says "feasible" without touching a host.** The deployment's pre-flight refuses a host that is too small. For a host whose provider is a cloud, it says feasible and "provision on aws", without any account. A feasibility is a plan, not a verification. The design file names the next step plainly: the verification against a real host or account, which waits on infrastructure. The figures below are illustrative. What does the pre-flight answer to a host that is too small, and to a cloud provider with no account? Run the block:

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

> run: kept

The tiny host gets `SHORTFALL -- host too small`, and the cloud with no account is feasible, with `provision on aws`!

Now the tables. Each one opens with what the project delivered or ran, and ends with what comes next. Every cell is from the record, read on 8 October 2026. A line count or a file date I read myself is labelled as mine.

### The restaurant in Lyon

| Claim | Proof | What comes next |
|---|---|---|
| The platform exists, and its first delivery was made | the site: an amendment closed on 4 August 2026; the project's commit "iteration 1" of 15 August; a server of 565 lines that I read; the last commit, 25 August 2026, 13:07 | 25 August 2026 is the last dated record; the next record is the one the next phase writes: production, a real order, the planned go-live gate |
| The first version was field-tested with the restaurant's owner | a day of field measurements with two phones, 19 August | the owner's own sentence on how he uses it is the next record to gather; chapter 1 writes "runs", and the record's wording is "delivered and field-tested" |
| No growth of scope during a cycle (the Lock, chapter 28) | the pact and the notebook of the Lock: private documents | the Lock as code; chapter 28 shows the nearest the library gives |
| Payments can be tried without a subscription, and a fake never ships | the registry and the production gate, with their guards | the live payment adapter for the restaurant, "a later desk" in the library's own design file; the sandbox is bound today, and the live binding is the step after it |
| The constellation of worlds | the restaurant's map of its worlds; the library's super-app class, with a guard | the restaurant on the constellation: its worlds are single-file web pages today, and the map says it is a map, not an implementation |
| A speed budget is a promise | the library's service-level object, with a guard | a measure on a real 4G network: the project's own checklist moves it to the next cycle |
| The interface rules were forged with the owner, phone in hand | the project's file says eleven iterations with the real user | who held the phone: the record does not hold it. The study (12.29) conflates two facts |

### The bank in Niamey

| Claim | Proof | What comes next |
|---|---|---|
| The bank has the author's assessment product, installed on its own internal network under licence | the installation guide delivered to the bank; a licence file | the bank's own account: who declares the chart, for how long, how many people use it. And a date of delivery: the files carry file-system times, which are not dates |
| The product is "built with Softanza" | the author built both | the product calling the library. Today it is a Python application with a small web server; I searched its code, and found no regional or Basel check and no call to the library |
| The regulator's rules judge the chart | the library's validator of three rules and of segregation of duties, with guards | the validators inside the product; an article of the central bank's text for the three rule codes; a finding read by an auditor |
| A rule file for the bank | a file of two regional rules that loads | its first judgment: on a chart with no board it reports sound today |
| The product's interface rules came from the bank | the interface constitution's rules 117 to 121 | the evidence line of rule 117 in the constitution reads "A banking supervision product (April 2026)" and names no bank. The study attaches them to this bank, and the record does not |

### The organisation in the field

| Claim | Proof | What comes next |
|---|---|---|
| The organisation chose my offer | the offer of 5 August 2026 was retained; the design study, built with its teams from 22 September to 8 October 2026 | the organisation's hub, designed and not yet built; the study's version 1.2 is submitted for validation. And who chose: the record is silent |
| Rules are data that a person changes without a programmer | the library's rule clauses and the governor that names a dead rule | a text form for clause rules; a version record with undo, which the study promises; the study's own rule notation is not the library's |
| An agent prepares, a person decides, with the authority at the time | the governance object and its lineage, with guards | a person bound to a signed-in account; a hub to do it in |
| Offline by default | the study's word that the browser-side outbox is already in service | the mechanism in the library is to come: no queue, outbox or synchronisation yet. The site calls it "a gap, not a lesson learned". Chapter 30's last block is the whole of it |

### Across the three

| Claim | Proof | What comes next |
|---|---|---|
| The platforms run today on ordinary stacks | the site's own page: single-file web worlds and a small Node server; a Python application; the organisation's hub not built | the first platform on the engine. The site says so, and every repository I opened agrees |
| Their declarations "are being written as Softanza's own" | the platforms page and the forged page, as intent | the declarations as files are the next piece to write. I searched, on 8 October 2026, and did not find them as a file: in the restaurant's repository no code file declares an app, a constellation or a platform; in the bank's delivery, none; in the organisation's study folder, none (its annex uses a notation that is not the library's). The record shows the intent and the maps; the declarations are the step that follows |
| A change of engine, not of plan | the principle: rewriting was refused | the move itself; the record does not yet say who moves first or who perceives it |
| A solution writes its guarantee sheet in five rows | the vision asks for it | the first sheet is to come: no solution has one yet, and no class, fixture or guard in the library holds the sheet |
| The runtime beneath is the language's own | the charter ratified on 1 October 2026; its stages pass on its own fixtures | Haro running the library is the next step. A session's note of 5 October 2026 reports that the bridge runtime passes every assertion the old runtime passes on the library, though not every program agrees on every stable line; the Linux pass is the step after that. I print no percentage. This book's blocks run on the former runtime, 1.27 |
| A live host verifies a deployment | the deployment design | the verification waits on infrastructure and is the next step. Local sites run for real; remote transfer is "a later slice" |
| The payments plane works against the central bank's sandbox | the twin, served over HTTP, with a guard | the sandbox run: postponed, unperceived so far. Production is never from this plane |
| A named person has said what they saw | a drum, and the retuned voice, in another plane | the same line for any of the three platforms, which is the next milestone |

### What the study of the record marks for measurement

The comparative study that read the record says, in its own paragraphs headed "Not measured", what it leaves to measure next. It read the record and did not run it: its closing assessment of the record says "Nothing in it was run". Whether Haro's runtime runs the library is the first measure still to come. Whether two published speed benchmarks hold today is the second, and both were run on the former runtime. Some guards in the system folder took their totals from design documents, and one of those documents still says forty-five where its guard now holds more; the document is the next to update. The forty-one pictures of part 1 of the gallery were judged by a model, and a person looking at them is the next step. The restaurant's speed budget awaits its measure on a real 4G network. The study applies its own perception law to itself, which is why I trust the paragraph.

## 4. The decision, and what I refused

**I refused the author's memory as evidence.** The site lists nothing that I remember and no file proves. The same rule bound the bank: I know the product, because I built it, and what the bank's own people do with it is not yet in a file.

**I refused to call the library the origin of what it only uses as an example.** The forged page says "example" where the library holds a project as its example and not as its origin. And I will not repeat a sentence in the study of 12.29 that says a lesson was "born of the client's need". The registry and the SLA were first committed after the reversal of 4 July, by the library's log as chapter 28 reads it. The order of the commits does not support "born of". What I can say is "needed" and "carries".

**I replaced two wordings of my own with the record's.** In chapters 1, 2 and 33 I wrote that the bank "runs" a product "built with" Softanza, and that the restaurant "runs" a platform. The record shows a Python application, installed at the bank under licence and built beside the library by the same person, and for the restaurant a first delivery and a field day, with the record ending on 25 August. The wording that the record bears out is *built by me, under the discipline the library now carries*, and *delivered and field-tested*. Chapters 2 and 33 now carry those wordings. Chapter 1 keeps its own, and this paragraph is where the record's more exact one stands.

**I refused a stage word the repository does not carry.** The site's estate page says it: never called available before it is. A piece of work that reaches a person through a sense is perceived by a person. Until then it is unperceived, which is a state and not a failure.

**I refused to print a percentage.** I have said aloud how far the bridge runtime has come. The study ruled that the figure should not be printed without the guard that produces it. I agree.

## 5. The court

`service_registry_narrated` proves that a declared service nobody backs is an error finding, that an unbound service raises, and that a sandbox in production is a violation. `full_scope_model_narrated`, scenes 5 to 8, proves the three verdicts: refused, rehearsed, native. `payments_live_adapter_narrated` proves the adapter against a twin served over HTTP, an adapter without credentials that refuses to guess, and the scenario that says stage (b) is unperceived. It starts real server processes, and the book does not run it; it only counts its assertions. `sound_mu5_narrated` proves, in its fifth scene, that while the verdict is unperceived `Sing` returns nothing and says why. `deployment_narrated` proves that an undersized host is not feasible, and that an assistant rehearses and commits nothing; it writes a scratch folder beside itself, so the book does not run it either. `orgrule_narrated` proves the universal rules of the chart and the separation of duties. `14_bceao_governance`, one assertion, runs the regional rules on a chart with no board and no risk function. `governance_narrated` proves authority against risk, with its lineage.

The court of this chapter's subject is not a guard. It is a line of the record, of the form the estate's law prescribes: a date, a person, and what they said. The library holds one such line in its data, in the sound plane. The estate holds one in its record, and chapter 33 tells it.

## 6. The field, and where it leads

The field leads in production. Ordinary stacks run real workloads for real users, including, on the site's own page, the platforms of this part; moving their declarations onto Softanza's own engine is the next step.

The field leads in references at scale. The site prints two references and a design study, and quotes no number of countries and no number of programmers. A buyer reading a logo wall sees more.

The field leads in live infrastructure. Provisioning tools drive real providers every day. The library's deployment reaches local sites for real today, and the real host is the next step; the fifth block shows where the line runs.

The field leads in hardware in the field. The declared machine boots and judges itself in an emulator, and the vision records that no customer is on it yet. Its guarantee text says four of four promised, three kept in the emulator; the fourth, surviving a cut, waits for the watchdog on the board, and that text carries no slot decision yet. The board is on order.

The field leads in speed. The runtime Softanza measured itself against was faster on every row, by a factor between one and two, and both benchmarks were run on the former runtime; Haro's own speed is the measure still to come.

The field leads in pictures judged by people. Forty-one pictures and text sections of part 1 of the gallery were judged by a model: twenty right, nine wrong, twelve uncertain. The record says that no person has looked at them yet, and that look is the next step.

Where I think the record stands apart is that its limit is a section of a page, with a heading. Every stage has a word. A feature can be built and still refuse until a named person has spoken. And a live run that could not happen is reported unperceived, never a failure and never a pass.

## 7. The limit

This whole chapter is a stage report. Here is its sum in the stage words.

What is built: what the three projects delivered, each with a document (a first delivery, field-tested at the restaurant; a product installed at the bank under licence; a design study built with the organisation's teams), and the three lessons they gave the library. *A fake never ships*: the registry and the production gate. *An organisation is judged by its own chart under a regulator's rules*: the organisation chart and its validators. *Authority is not permission, and a decision keeps its authority at the time*: the governance object. Each has a file of the library that carries it, a guard that resolves, and a block already kept in a neighbouring chapter. The next step of each is in the tables. A sandbox is bound, and the live payment adapter is the step after it; the bank's product does not call the chart validator yet. The organisation's hub is designed, and its offline mechanism is to come.

What is designed: the five-row guarantee sheet; the runtime that is the language's own, running the library; the declared machine on a board.

What is absent: any customer platform on the engine; the customers' declarations written as Softanza's own, as files; a word from the bank; the record of the restaurant after 25 August; the organisation's hub; an offline mechanism in the library; a live payments run against the central bank's sandbox; a named person's verdict on any of it.

The sum of every next step is the line that chapter 33 sets as the next milestone: *the solution ran on Softanza's own engine, and this is what the user said.* The customers' declarations are its first piece, and they are absent today. The site says they are being written as Softanza's own. On 8 October 2026 I looked for a file of them in the restaurant's repository, in the bank's delivery and in the organisation's study folder, and found none. On 9 October 2026 I looked again, read-only, in thirteen repositories beside the library. They are the restaurant's, the bank product's web repository with its older copies, the organisation's, the central one, the engine's, the site's, and four of the estate's other projects. I searched their text for the library's own classes for a platform, an organisation chart and a constellation, and the file names of five of them for declaration files. The hits are the library's notes and memos, the site's data, and, in the older copies of the bank product's web repository, a JavaScript class for an organisation chart that is that application's own code. No file declares a customer's platform as Softanza's own. The chapter's word for them is *absent*, and the stage line at the top says so.

## 8. Six doors

**The programmer.** Your demo is a rehearsal until a target has run it. Ask the scope whether the line was native, rehearsed or refused, and write the same word beside your own claims.

**The analyst.** When you cite a project, write three columns: the claim, the document, and what comes next. Do not fill the third from memory.

**The designer.** A feature that no person has seen or heard ships shut, and says so. The stage is a state of the design and not an apology. I hold this as a view, not a result. What stands behind it on this page is the sound plane, where `Sing` refuses until a person has heard the voice.

**The decision-maker.** Read the stage word before the testimonial. "Built" is a statement about a guard. "Runs at a customer" is a statement about a document. You can ask for it in writing, with a name beside it.

**The educator.** Teach the difference between a project that taught the library and a project that runs on it. The first is shown here, and the second is the next milestone, in chapter 33. Unperceived is a state, not a failure.

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

> run: exercise

Then, on paper, make the table of three columns for the project you know best: the claim, the document or file that backs it, and what comes next. Leave empty what you cannot name. On the last line write who perceived it, on what date, and what they said, or the word "unperceived" and why.

The exercise has no answer to be checked first. The question the tutor asks is: which cell did you fill from memory?

I left this one in your hands, on purpose. Below is the first block of this chapter with one line added: it binds the payments service to the library's sandbox before the registry is asked whether it is sound.

```haro exercise
oReg = new stzServiceRegistry("shop")
oReg.DeclareMany([ :mail, :payments ])
oReg.Bind(:payments, new stzPaymentsSandbox())
? oReg.IsSound()
```

> run: exercise

Run it and read what `IsSound()` answers. Then ask whether a sound registry is a registry ready to ship, and what the guard of section 5 says about a fake still bound in production. I do not give the answer: section 5 names the guard that holds it, and section 7 says what the project has bound and what it has not. When you have solved it, you will know what a sound registry does not say about the service behind it.

Chapter 32 turns first to how many minds worked on this one body of work, and to the rule they keep: every law cites the incident that earned it, and a new law without a dated failure behind it is a preference. Chapter 33 then closes the book on the next milestone, a solution running on Softanza's own engine.
