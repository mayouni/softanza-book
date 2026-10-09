# The one line still owed

Source: Chapter 33. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: a declared platform built, then deployed, and refused in the other order; the twin that touches nothing real; the last door that refuses a fake service; designed: the runtime that is the language's own, running the library; the guarantee sheet of a solution in five rows; live hosts and a real board; absent: a customer solution running on the Softanza engine, and a named person's verdict on it; the customers' declarations as files

Run: 3 of 3 blocks kept their promise, on 2026-10-09 05:33 UTC+01:00.

## 1. The concept, as the field holds it

In our industry, a platform is proven when someone else runs it for real. The home page shows the logos of companies that use it; a case study tells one of them in two pages. A team that believes in its own product uses it for its own work, and a compiler that is serious compiles itself. Engineers who need a scale have one: NASA's readiness levels, later a standard, where the highest level is a system proven in the place it was built for.

These are reasonable tests, and they all point at the same thing: production. What they do not ask is who saw it work, and what that person said.

## 2. The first principle

**The record carries a solution only when it ran on its own engine and a named person said what they saw.**

## 3. The Softanza form

This is the last chapter, and it is about something that has not happened. Let me first show you the floor it will stand on, because the floor exists.

A solution is declared before it is built, and the platform that carries it refuses to be deployed before it is built:

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

Before anything is real, the solution can run on a twin, a copy of the system that holds no reference to reality. Here a file is written into the twin, read back, and is nowhere on the disk:

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

And at the last door, a solution cannot reach production with a fake service bound in it, whoever asks. In chapter 1 you saw the registry refuse; here the delivery itself refuses, with an entitled person at the controls:

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

The person was allowed to deploy. The deployment still did not run, because a payments service that is a sandbox cannot be what a real customer pays through. This is not a question of authority. It is a question of what is true.

So the floor is there: declare, build, rehearse, refuse the fake, commit through a governed actor. Now the absence.

Softanza has been used. I wrote that in chapter 1 and I hold to it, because the study that first read the record wrote the opposite, that no user outside my own projects had been measured, and I corrected it. A bank in Niamey has an organisation-assessment product I built beside the library, installed on its own network under licence, and the installation guide delivered to the bank attests it. A restaurant in Lyon was delivered a first version of a platform for neighbourhood commerce and field-tested it; the record of that project ends on 25 August 2026, with an amendment closed on 4 August and an owner who took part in the first demonstration and ran a day of field tests with two phones. An organisation in Niger has its hub designed. The site lists, project by project, the lesson each one taught and the file of the library that carries it. Part VI of this book tells their stories.

And the site says, in the same page, what those platforms run on today: ordinary stacks. The bank's is a Python application. The restaurant's is a set of web worlds, each a single file. The organisation's hub is not built. The site says their declarations are being written as Softanza's own, so that moving them onto the Softanza engine is a change of engine and not of plan. The site's own words are exact: it is a step ahead, not a step taken.

So the line the record does not yet carry is this one: *the solution ran on Softanza's own engine, and this is what the user said.*

What is between here and that line, read from the record and not composed:

1. **A customer's declarations run on the engine instead of the ordinary stack.** The site says the declarations are being written; I found no file of them, and chapter 31 says where I looked; the move is not made.
2. **The language's own runtime runs the library on the customer's system.** Today the blocks of this book are run by the runtime of the former host language, version 1.27, and every page says so under its proof line. The bridge runtime that is meant to replace it was reported on 5 October 2026 to pass every assertion the old runtime passes on the library, all but one HTTP/2 request that failed once in the pass; on every stable line, 3,461 of 5,112 programs agree with the old runtime. Its pass under Linux is the next step. Haro's charter was ratified on 1 October 2026, and Haro's own stages pass on its own fixtures. Haro does not run the library yet.
3. **The solution writes its guarantee sheet.** The vision asks every solution for five rows, one for each system it answers to, technical, social, ecological, economic and cultural, judged as fixtures, with the machine derived from them. No solution has written one.
4. **Live hosts and a real board.** The deployment's verification against a real host or a real account is gated by infrastructure. The declared machine boots and judges itself in an emulator; of the four promises its hosted profile makes, the emulator can check three, and the fourth waits for a watchdog on a real board. No customer runs a production workload on it.
5. **A person perceives it, and the record says who.** Not a counter. A person, named, with a date and what they said.

The last step is a law of the estate, and it was paid for. The sound plane of the library once held hundreds of passing assertions while it was, to my ear, broken. Since then, a piece of work that reaches a person through a sense must be perceived by a person, and the record must say who perceived it and what they said. And when nobody has, the law says it plainly: unperceived is a state, not a failure. A report may be honest and still be unperceived.

The record already holds the form of the line. In another plane, on 2 October 2026, the record says the Principal listened to a sound the library made and said, in the words written down: "yes it's real drum!!" It is not a solution, and it is not a customer. But it is a person, a date, and a sentence, and it is what the one line will look like.

The record also holds the opposite, honestly. The pictures the library draws were judged by a model, forty-one pictures or text sections, twenty right, nine wrong, twelve uncertain, and the record says that no human has looked at them yet. The live run of the payments plane with the organisation's test account was postponed, by me, and reported as unperceived. Neither is a failure. Both are owed.

## 4. The decision, and what I refused

**I refused to be told the projects did not count.** The first reading of the record wrote that no user outside my own projects had been measured. It was wrong, and I said so: Softanza has been used in real projects which, while not complete, gave the feedback that shaped its design. The reading was corrected in the record, in place, with the date. What replaced it is smaller and more honest: the users exist and have spoken; they have not yet run on the engine.

**I refused a reference without a document.** The site counts a project as a reference only when a document proves it, and it quotes no number of countries and no number of developers. A lesson is listed only when a file of the library carries it.

**I refused to move a platform by rewriting it.** A customer's platform moves to the engine as a change of engine, not of plan. The declarations are to be written once, as Softanza's own, and the engine beneath them changes. Rewriting would be faster to announce and slower to trust.

**I refused my own figure.** I have said aloud how far the bridge runtime has come, as a percentage. The study that read the record ruled that the figure should not be printed without the guard that produces it. The stage word is "in construction", and the measured rows are the evidence.

**I refused an instrument as proof of a perception.** A phase whose evidence is entirely a counter is not done when the thing itself is something a person sees or hears. The counter is a result. The person is the verdict.

## 5. The court

The floor of this chapter stands on three guards. `full_scope_model_narrated`, the architect's common ground, proves that a solution is modelled first, that a deployment before a build is refused and logged as an error, and that a model cannot perform the deployment. `virtual_system_twin_narrated` proves that rehearsal touches nothing real, that the plan narrates itself, and that committing is the one door. `service_delivery_narrated` proves that a production deployment with a fake bound does not run at all, with every reason named, and that the gate opens once the service is real.

The court of this chapter's subject is not a guard. It is a line in the record: who, when, and what they said. That line does not exist yet.

## 6. The field, and where it leads

The field leads in production. Ordinary stacks run real workloads for real users today, including, by the record's own page, the bank's Python application; the restaurant's first version is single-file web worlds, and the hub is not built.

The field leads in live infrastructure. Its tools drive real providers and real hosts every day; Softanza's deployment verifies against a real host only when the infrastructure is there, and rehearses everything else.

The field leads on hardware in the field. Its devices run in shops and clinics; the declared machine boots in an emulator, and its board is not yet in service.

The field leads on speed. The runtime Softanza measured itself against was faster on every row, by a factor between one and two, and the estate's note recorded the loss.

Where I think the record stands apart is in what it will not let itself say. Every reference has a document. Every stage has a word. By the design document, the emulated deployment runs the same artifact that ships. A fake cannot ship and a model cannot commit. And a perception is a named, dated, quoted line, which a logo on a home page does not carry.

## 7. The limit

This whole chapter is a limit, so I will be brief.

What is built: the floor. Declare, build, deploy in order; rehearse on a twin; refuse a fake at the last door; commit only through a governed actor.

What is designed: the runtime that is the language's own, running the library; the guarantee sheet of a solution in five rows; the verification on live hosts and on a real board.

What is absent: a customer solution running on the Softanza engine, a named person's verdict on it, and the customers' declarations as files (chapter 31 says where I looked). The record names no project that moves to the engine first, and no person who will perceive it; I leave both unwritten.

## 8. Six doors

**The programmer.** Your code runs today through build, rehearsal and a governed deployment. What you cannot claim yet is that a customer runs it on the engine, and the record will not let you claim it.

**The analyst.** Ask for two things before you count a project as proof: a document, and a named verdict.

**The designer.** What you design is judged last by a person's sense. A model's opinion of a picture is a result; a person's is the verdict.

**The decision-maker.** Read the stage word before the promise. Today the floor is built, and the customer run is absent.

**The educator.** Teach that unperceived is a state and not a failure. An honest report can ship on it, if it says so.

**The agent.** You may rehearse a deployment and explain it. You will be refused when you try to perform it, and the refusal will be written down (chapter 24 shows it).

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

Run it. Then write one more line, the one your own project still owes, in the record's form: who perceived it, on what date, and what they said. If nobody has, write "unperceived", and say why. That line is the end of this book, and the beginning of the next one.
