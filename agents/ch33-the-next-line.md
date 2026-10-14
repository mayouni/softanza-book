# The next line: a solution on its own engine

Source: Chapter 33. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: a declared platform built, then deployed, and refused in the other order; the twin that touches nothing real; the production gate that refuses a fake service; designed: the runtime that is the language's own, running the library; the guarantee sheet of a solution in five rows; live hosts and a real board; absent: a customer solution running on the Softanza engine, and a named person's verdict on it; the customers' declarations as files

Run: 3 of 3 blocks kept their promise, on 2026-10-14 22:27 UTC+01:00.

In this chapter I show you the floor the next line will stand on. A platform is declared, built and deployed in that order; a twin touches nothing real; a last door refuses a fake service. Then I say what the three projects establish today, and I read from the record the five steps from that floor to the next line: a solution on Softanza's own engine, and what a named person who used it says. I say five things I refused, among them a reference without a document, my own figure for the bridge runtime, and an instrument as proof of a perception. The record carries a solution only when it ran on its own engine and a named person said what they saw.

## 1. The concept, as the field holds it

In our industry, a platform is proven when someone else runs it for real. The home page shows the logos of companies that use it; a case study tells one of them in two pages. A team that believes in its own product uses it for its own work, and a compiler that is serious compiles itself. Engineers who need a scale have one: NASA's readiness levels, later a standard, where the highest level is a system proven in the place it was built for.

These are reasonable tests, and they all point at the same thing: production. What they do not ask is who saw it work, and what that person said.

## 2. The first principle

**The record carries a solution only when it ran on its own engine and a named person said what they saw.**

## 3. The Softanza form

This is the last chapter, and it looks ahead. Let me first show you the floor the next line will stand on, because the floor exists and runs.

A solution is declared before it is built, and the platform that carries it refuses to be deployed before it is built. What does it answer when you ask it to deploy first? Run it:

```haro
oSol = new stzPlatformProfile("bank")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oPlatform = StzPlatformQ("bank")
oPlatform.SetProfile(oSol)
try
	oPlatform.Deploy()
catch
	? cCatchError
done
#--> stzPlatform.Deploy: the platform must be Build() before it can be deployed.
? oPlatform.IsDeployed()
#--> 0
oPlatform.Build()
oPlatform.Deploy()
? oPlatform.IsDeployed()
#--> 1
```

> run: kept

The platform answers: `stzPlatform.Deploy: the platform must be Build() before it can be deployed.` Built, then deployed, `IsDeployed()` answers `1`.

Before anything is real, the solution can run on a twin, a copy of the system that holds no reference to reality. Where does a file written into the twin live? Run it:

```haro
oTwin = new stzVirtualFileSystem()
oTwin.CreateFile("orders/today.txt", "3 couscous")
? oTwin.ContentOf("orders/today.txt")
#--> 3 couscous
? oTwin.OriginOf("orders/today.txt")
#--> virtual
? StzEngineFileExists("orders/today.txt")
#--> 0
```

> run: kept

It answers `virtual`, and `StzEngineFileExists` answers `0`: the file was written, read back, and is not on the disk at that path!

And at the production gate, a solution cannot reach production with a fake service bound in it, whoever asks. In chapter 1 you saw the registry refuse; here the delivery itself refuses, with an entitled person as the actor. What does the delivery answer when that person deploys to production with a sandbox bound? Run it:

```haro
oReg = new stzServiceRegistry("shop")
oReg.BindSandbox(:payments, new stzPaymentsSandbox())
oDel = new stzDelivery("shop")
oDel.AddBackend("api", "linux")
oDel.UseServicesQ(oReg)
oDel.DeployTo(StzDeploymentSiteQ("host1"), "api")
oDel.SetActor(HumanActor("dana"))
oDep = oDel.Deploy(:Production)
? oDep.WasCommitted()
#--> 0
? oDel.Log().EntriesOfLevel(:error)[2][:message]
#--> sandbox-in-production @ shop/payments
```

> run: kept

The person was allowed to deploy. The delivery refused it! `WasCommitted()` answers `0`. Why did it refuse? The log's first error entry says only that the external surface is not production-ready; the second names the service: `sandbox-in-production @ shop/payments`. A payments service that is a sandbox cannot be what a real customer pays through. This is not a question of authority. It is a question of what is true.

So the floor is there: declare, build, rehearse, refuse the fake, commit through a governed actor.

Now what the projects show, and the step after them.

Has Softanza been used? Yes. I wrote that in chapter 1 and I hold to it. Parts of Softanza are in production, and others are in development. Three projects, and their feedback, shaped its design. A bank in Niamey has an organisation-assessment product I built beside the library, installed on its own network under licence. The installation guide delivered to the bank attests it. A restaurant in Lyon was delivered a first version of a platform for neighbourhood commerce. An amendment closed on 4 August; the notebook shows that the owner took part in the first demonstration, and on 19 August he made a day of field measurements with two phones. The last dated record of that project is 25 August 2026, and the next record is the one the next phase writes. An organisation in Niger has its hub designed. The site lists, project by project, each lesson it names and the file of the library that carries it. Part VI of this book tells their stories.

And the site says, in the same page, what those platforms run on today: ordinary stacks. The bank's is a Python application. The restaurant's is a set of web worlds, each a single file. The organisation's hub is designed, and its build is to come. The site says their declarations are being written as Softanza's own, so that moving them onto the Softanza engine is a change of engine and not of plan. The site's own words are exact: it is a step ahead, not a step taken. That step is the next one.

So the next line is this one: *the solution ran on Softanza's own engine, and this is what the user said.*

What leads from here to that line? Five steps, read from the record and not composed.

1. **A customer's declarations run on the engine instead of the ordinary stack.** The site says the declarations are being written as Softanza's own; I found no file of them yet, and chapter 31 says where I looked. The move to the engine is the next step.
2. **The language's own runtime runs the library on the customer's system.** Today the blocks of this book are run by the runtime of the former host language, version 1.27, and every page says so under its proof line. The bridge runtime that is meant to replace it was reported on 5 October 2026 to pass every assertion the old runtime passes on the library, all but one HTTP/2 request. That request failed once in the pass and passes twice when run alone. On every stable line, 3,461 of 5,112 programs agree with the old runtime. Those are two counts and not one: the first is of the suite's assertions, the second of whole programs, a program counted as agreeing only when every stable line it prints is the same on both runtimes. The morning's run gave 3,425, the figure chapter 27 prints; the 3,461 are the evening's, after a day of fixes. Its pass under Linux is the next step. Haro's charter was ratified on 1 October 2026, and Haro's own stages pass on its own fixtures. Whether Haro's own runtime runs the library is not yet measured.
3. **The solution writes its guarantee sheet.** The vision asks every solution for five rows, one for each system it answers to, technical, social, ecological, economic and cultural, judged as fixtures, with the machine derived from them. The sheet is designed, and the first one is yet to be written.
4. **Live hosts and a real board.** The deployment's verification against a real host or a real account is gated by infrastructure. The declared machine, a device written as a declaration, boots and judges itself in an emulator. Its hosted profile makes four promises: it is always reachable, it has a stable name, it keeps a durable log, and it survives a cut. The emulator can check three. The fourth waits for a watchdog on a real board, a watchdog being, in the field's plain sense, a hardware timer that restarts a machine that stops answering. The site says no production workload is on it yet.
5. **A person perceives it, and the record says who.** Not a counter. A person, named, with a date and what they said.

The last step is a law of the estate, and it was earned. The sound plane of the library once held hundreds of passing assertions while, to my ear, it did not yet sound right. Since then, a piece of work that reaches a person through a sense must ship in a form a person can perceive, and the record must say who perceived it and what they said. And when nobody has, the law says it plainly: unperceived is a state, not a failure. A report may be honest and still be unperceived.

The record already holds the form of the line. In another plane, on 2 October 2026, the record says the Principal, its name for me (chapter 32 says so), listened to a sound the library made and said, in the words written down: "yes it's real drum!!" It is not a solution, and it is not a customer. But it is a person, a date, and a sentence, and it is what the next line will look like.

The record also holds two verdicts still to come. The pictures the library draws were judged by an AI model, forty-one pictures or text sections, twenty right, nine wrong, twelve uncertain. The record says that no human has looked at them yet; that look is the next verdict. The live run of the payments plane with the organisation's test account was postponed, by me, and reported as unperceived. Neither is a failure. Both are next.

## 4. The decision, and what I refused

**I refused to be told the projects did not count.** The first reading of the record wrote that no user outside my own projects had been measured. It was wrong, and I said so: Softanza has been used in real projects which, while not complete, gave the feedback that shaped its design. The reading was corrected in the record, in place, with the date. What replaced it is exact: the users exist, and their feedback shaped the design, and the next step is to move one of them onto the engine.

**I refused a reference without a document.** The site counts a project as a reference only when a document proves it, and it quotes no number of countries and no number of programmers. A lesson is listed only when a file of the library carries it.

**I refused to move a platform by rewriting it.** A customer's platform moves to the engine as a change of engine, not of plan. The declarations are to be written once, as Softanza's own, and the engine beneath them changes. I hold this as a view, not a result.

**I refused my own figure.** I have said aloud how far the bridge runtime has come, as a percentage. I do not print it without the guard that produces it. The stage word is "in construction", and the measured rows are the evidence.

**I refused an instrument as proof of a perception.** A phase whose evidence is entirely a counter is not done when the thing itself is something a person sees or hears. The counter is a result. The person is the verdict. The sound plane above, with its hundreds of passing assertions and the sound that was not yet right, is what stands behind it.

## 5. The court

The floor of this chapter stands on three guards. `full_scope_model_narrated`, the architect's common ground, proves that a solution is modelled first, that a deployment before a build is refused and logged as an error, and that an AI model cannot perform the deployment. `virtual_system_twin_narrated` proves that rehearsal touches nothing real, that the plan narrates itself, and that committing is the one door. `service_delivery_narrated` proves that a production deployment with a fake bound does not run at all, with every reason named, and that the gate opens once the service is real.

The court of this chapter's subject is not a guard. It is a line in the record: who, when, and what they said. That line is the next one to be written.

## 6. The field, and where it leads

The field leads in production. Ordinary stacks run real workloads for real users today, a fact of the field and not a reading of the record; the record's own page names among them the bank's Python application, installed under licence. The restaurant's first version is single-file web worlds, delivered, with a day of field measurements on 19 August, and the hub is designed.

The field leads in live infrastructure. Its tools drive real providers and real hosts every day; Softanza's deployment is proven end to end on local sites and rehearses the rest; live verification against a real host is the next step.

The field leads on hardware in the field. Its devices run in shops and clinics; the declared machine boots in an emulator, and its board is the next step.

The field leads on speed. The runtime Softanza measured itself against was faster on every row, by a factor between one and two, and the estate's note recorded the measure.

Where I think the record stands apart is in what it holds itself to. Every reference has a document. Every stage has a word. By the design document, the emulated deployment runs the same artefact that ships. A fake cannot ship and an AI model cannot commit. And a perception is a named, dated, quoted line, which a logo on a home page does not carry.

## 7. The limit

This chapter looks ahead, so the limit is short.

What is built: the floor. Declare, build, deploy in order; rehearse on a twin; refuse a fake at the production gate; commit only through a governed actor.

What is designed: the runtime that is the language's own, running the library; the guarantee sheet of a solution in five rows; the verification on live hosts and on a real board.

What is absent: a customer solution running on the Softanza engine, a named person's verdict on it, and the customers' declarations as files (chapter 31 says where I looked). Beside it stand the floor above and the feedback of three projects. The record does not yet name the project that moves to the engine first, nor the person who will perceive it; I leave both unwritten until the record can carry them.

## 8. Six doors

**The programmer.** Your code runs today through build, rehearsal and a governed deployment. What comes next is a customer running it on the engine, and the record will carry that claim the day it is true.

**The analyst.** Ask for two things before you count a project as proof: a document, and a named verdict.

**The designer.** What you design is judged last by a person's sense. An AI model's opinion of a picture is a result; a person's is the verdict.

**The decision-maker.** Read the stage word before the promise. Today the floor is built; the customer run on the engine is the next milestone, and its stage word is absent.

**The educator.** Teach that unperceived is a state and not a failure. An honest report can ship on it, if it says so.

**The agent.** You may rehearse a deployment and explain it. You will be refused when you try to perform it (chapter 24 shows the refusal).

## 9. Exercise

Declare a platform for a project you own, with one server. Before you run anything, write the line you expect under each of three questions: what happens when you ask it to deploy before you build it; what happens when an assistant asks to deploy after the build; what happens when a person does.

```haro exercise
oSol = new stzPlatformProfile("my-project")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oP = StzPlatformQ("my-project")
oP.SetProfile(oSol)
# your three questions here, each with the line you expect under it
```

> run: exercise

Run it. Then this one, which I also left in your hands. Here is the production-gate block of section 3 with one line changed: the actor is no longer the person but the assistant, `LLMActor("assistant")`, as in chapter 24. I did not run this version, and I print no answer for it.

```haro exercise
oReg = new stzServiceRegistry("shop")
oReg.BindSandbox(:payments, new stzPaymentsSandbox())
oDel = new stzDelivery("shop")
oDel.AddBackend("api", "linux")
oDel.UseServicesQ(oReg)
oDel.DeployTo(StzDeploymentSiteQ("host1"), "api")
oDel.SetActor(LLMActor("assistant"))
oDep = oDel.Deploy(:Production)
? oDep.WasCommitted()
? oDel.Log().EntriesOfLevel(:error)[2][:message]
```

> run: exercise

Run that one too. Read what `WasCommitted()` answers, and read the log: the block of section 3 printed its second error entry for the person, and I make no claim about the assistant's. Section 5 says what the three guards prove, and section 8 what an AI agent is refused. When the gate answers, you will know what it refuses for what is true and what it refuses for who is asking.

Every block in this book is yours to run again. Now write one more line, the next one for your own project, in the record's form: who perceived it, on what date, and what they said. If nobody has, write "unperceived", and say why. That line is the end of this book, and the beginning of the next one.
