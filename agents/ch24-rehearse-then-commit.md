# Rehearse, then commit

Source: Chapter 24. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: a twin of files and a twin of the process environment, each with its history, snapshots, a narrated plan, its risks and, for the file twin, a validation against reality; the placement plan; the emulator's bundle, wired into the production attach; a deployment as a graph of steps with a rollback; the registry of services with its postures and the gate that refuses a fake at production; designed: the engine seen running in a browser; a drift check for recorded answers; branches of a twin; twins for databases, interfaces and networks; the emulated phase set by the emulated deploy; absent: any live card-gateway adapter for payments (a hub adapter is built and proved only against a twin, chapter 31), a model, mail, SMS or an object store; live verification of a remote host; a person's look at the emulator's surface; a customer solution emulated and deployed through this path

Run: 11 of 11 blocks kept their promise, on 2026-10-14 12:15 UTC+01:00.

In this chapter I take the three practices the field keeps beside the program, plan and then apply, the test double and the emulator, and I show the one path the library puts in their place. I rehearse on a twin of files and a twin of the process environment, and I read the plan of placement. I build the emulator's bundle, run a deployment that fails and rolls back, and code against services by name before I subscribe to any. Then I ask production to refuse, and I print the one fake it does not refuse: a double that says nothing about itself. The principle is joined from three documents of the record. Reality is reached through exactly one door: rehearse on what touches nothing, commit through a governed actor, and let production refuse anything that is fake.

## 1. The concept, as the field holds it

Three practices of the field stand beside the program, each with its own configuration.

The first is plan and then apply: infrastructure as code and deployment pipelines. The record's own references are the dependency graph of a pipeline's jobs, a tool's resource graph with apply-or-revert, and a cluster scheduler that places work by the resources it asks for. The field's habit is that the plan is a file for a tool, and whether the wrong actor may apply it is a policy. The record states the loss it answers: it's a convention, enforced by hope.

The second is service virtualization and the test double: a vendor's test mode with published test cards, a stub server for HTTP, and the libraries that record a call once and replay it. The field's habit is that the double lives in the test suite, and production is a different file. The record's complaint: no gateway will decline a card because you asked nicely.

The third is the emulator and the simulator: a phone emulator, a board emulator, a local stand-in for a cloud. The record's own sentence on the genre is that simulators lie. They mock the database, stub the device, approximate the compute.

What the three share is that each is a separate tool, and the program itself knows nothing of it. (General knowledge for the tools, not a study of the record, except where I quote the documents.)

## 2. The first principle

**Reality is reached through exactly one door: rehearse on what touches nothing, commit through a governed actor, and let production refuse anything that is fake.**

The record's first principle for this ground is the first clause, and the library's own label calls it a first principle: reality is reached through exactly one door. The default path for consequential change is to rehearse in a twin, generate a plan, and commit the plan. The plan is the door. The framework's summary is three words: rehearse, plan, commit. The structure line of this book's outline says the last clause: production refuses a fake. The first clause is a library document without an author line (`SP3`, in `SOFTANZA_SYSTEM_FOUNDATION.md`). The middle clause, commit through a governed actor, is the deployment design's (`SOFTANZA_DEPLOYMENT.md`: "only an effectful actor commits"). The chapter joins the three and attributes each part to its source.

## 3. The Softanza form

### The twin

The one artifact that crosses toward reality is a plan. It names each step. It flags the one that removes something. And asked to validate, it re-reads reality. Chapter 20 said "I saw it warn" and did not show the words. What does the plan say about the source it was going to move? Here are the words, and nothing is executed:

```haro
oBench = new stzVirtualFileSystem()
oBench.CreateFolder("config")
oBench.CreateFile("config/pump.ini", "threshold=40")
oBench.MoveFile("old_settings.txt", "config/legacy.ini")
oPlan = oBench.GenerateUpdatePlan()
? oPlan.Narration()
#--> Update plan (3 of 3 operations to commit):
#-->   * 1. create folder 'config'
#-->   * 2. create file 'config/pump.ini' (12 bytes)
#-->   * 3. move 'old_settings.txt' -> 'config/legacy.ini'
? @@(oPlan.Risks())
#--> [ [ 3, "MOVES (removes source): move 'old_settings.txt' -> 'config/legacy.ini'" ] ]
? @@(oPlan.Validate())
#--> [ [ 3, "source absent in reality: old_settings.txt" ] ]
```

> run: kept

The plan answers `source absent in reality: old_settings.txt`, and it flags the move: `MOVES (removes source)`. The library's narration prints a closing line, that reality is untouched until I choose to commit this plan. The run does not print it, so I do not show it.

The twin is not only a twin of files. A variable set, a directory changed and a child process queued are recorded, narrated and flagged, and no process started. Does the real environment have the variable? Ask it, after the twin has set it:

```haro
oEnv = new stzVirtualEnvironment()
oEnv.SetActor("agent-42")
oEnv.SetVar("SHOP_MODE", "rehearsal")
oEnv.Cd("/srv/shop")
oEnv.Spawn("backup-database --all")
? oEnv.Var("SHOP_MODE")
#--> rehearsal
? oEnv.NumberOfPendingSpawns()
#--> 1
? (new stzEnvironment()).Has("SHOP_MODE")
#--> 0
oEnvPlan = oEnv.GenerateUpdatePlan()
? oEnvPlan.Narration()
#--> Update plan (3 of 3 operations to commit):
#-->   * 1. set env var 'SHOP_MODE' = 'rehearsal'
#-->   * 2. change directory to '/srv/shop'
#-->   * 3. spawn process: backup-database --all
? @@(oEnvPlan.Risks())
#--> [ [ 3, "RUNS an external command (side effects): spawn process: backup-database --all" ] ]
```

> run: kept

The twin holds `rehearsal` and one pending spawn, and the real environment answers `0`! Chapter 20's limit paragraph said that only files are built. That was wrong, and I have corrected it there.

The twin has a second job. A programmer on a laptop with no pins writes pin code for a board. The scope says *rehearsed*, as chapters 8 and 31 showed. At deploy, the lowering bridge turns the rehearsal into the source of firmware. What happens when an assistant asks to deploy? `Build()` records the build command and does not run the toolchain, and `Deploy` lowers in memory, so no file is written:

```haro
oProduct = new stzPlatformProfile("greenhouse")
oProduct.DevelopedOn(:Windows)
oProduct.WithApp(:sensor, :ESP32)
? oProduct.ReadPinIn(:sensor, 34)
#--> rehearsed
? oProduct.WritePinIn(:sensor, 26, 1)
#--> rehearsed
oPlatform = StzPlatformQ("greenhouse")
oPlatform.SetProfile(oProduct)
oPlatform.Build()
try
	oPlatform.DeployAs(LLMActor("copilot"))
catch
	? cCatchError
done
#--> stzPlatform.Deploy: actor 'copilot' lacks the 'effectful' capability -- it may propose a deploy, not perform it.
? oPlatform.IsDeployed()
#--> 0
oPlatform.DeployAs(HumanActor("me"))
? oPlatform.ArtifactFor(:sensor)
#--> // firmware generated by the Softanza lowering bridge
#--> // target: espidf
#--> void setup() {}
#--> void loop() {
#-->   digitalRead(34);
#-->   digitalWrite(26, 1);
#--> }
```

> run: kept

The assistant is refused, and told that it `may propose a deploy, not perform it`! The person's deploy yields the firmware. The limit of this block is in section 7: only two verbs are lowered.

The twin rehearses; next, the plan says where each part would go.

### The plan of placement

Before a byte is built, the delivery planner states, for each capability a part needs, whether the target does it, the engine does it, a construct does it, or the server does it. It gives the reason in a sentence. The figure in parentheses is the catalogue's estimate and not a measure, so do not quote it as a claim. "1 parts" is the library's own grammar:

```haro
oShip = new stzDelivery("shop")
oShip.AddSuperApp(:phone, :Android)
oShip.NeedsIn(:phone, [ :Unicode, :PivotTable, :Collection, :Neural ])
oShip.Plan().Show()
#--> Solution 'shop' -- placement & scope plan (rehearsal; nothing built yet)
#--> ==============================================================================
#-->
#-->   Part 'phone' [superapp] -> android (mobile / edge)
#-->      Unicode            [target]    Unicode: the target-platform is strong at it -> use its own
#-->      PivotTable         [stz.wasm]  PivotTable: Softanza-differential, mobile weak -> the on-device engine
#-->      Collection         [stz.js]    Collection: ergonomic -> a Softanza construct in the target language
#-->      Neural             [server]    Neural: heavy -> runs on the backend, not the edge
#-->      -> stz.wasm carries: [ "PivotTable" ]  (~12 KB, 1 of 4)
#-->
#-->   Summary: 4 capabilities across 1 parts -> target 1, engine 1, construct 1, server 1.
#-->   Build() will compile exactly this scope; Deploy() will commit it.
```

> run: kept

The rule behind the plan, in the emulation design: the edge carries a capability only if it is critical, and either unique to Softanza or weak or absent on the target platform. A regular expression is a construct over the platform's own, and never the engine's matcher compiled for the browser.

The plan says where; the emulator builds what the plan says.

### The emulation

The emulator turns the plan into a bundle, and the bundle is what ships. In the next block the bundle generated for the rehearsal is wired straight into the production attach, and the actor decides. What does the site become when an assistant calls `Deploy(:Production)`, and what when a person does? The manifest that lands names the engine group the part carries. The target here is a local folder, the kind of site that needs no tool but file operations:

```haro
cHere = StzReplace(WorkingDirectory(), "\", "/")
oFront = new stzDelivery("shopfront")
oFront.AddSuperApp(:web, :Browser)
oFront.NeedsIn(:web, [ :Unicode, :PivotTable, :Collection ])
oBundle = new stzEmulator(oFront)
oBundle.CompileEngineQ(FALSE)
oBundle.SetOutDirQ(cHere + "/_bundle")
oBundle.Build()
oSite = new stzDeploymentSite("cdn")
oSite.SetKindQ(:LocalRepo).SetStoreAtQ(cHere + "/_live")
oFront.DeployTo(oSite, :web)
oFront.ShipSlice(:web, oBundle)
oFront.SetActor(LLMActor("assistant"))
oFront.Deploy(:Production)
? oSite.Status()
#--> absent
oFront.SetActor(HumanActor("ops"))
oFront.Deploy(:Production)
? oSite.Status()
#--> launched
? @@(StzEngineDirListFiles(cHere + "/_live"))
#--> [ ".stzsite", "deploy.json", "index.html", "stz.js" ]
? read(cHere + "/_live/deploy.json")
#--> {
#-->   "solution": "shopfront",
#-->   "part": "web",
#-->   "engine": "aggregation",
#-->   "artifacts": "index.html,stz.js"
#--> }
StzDirDeleteAll(cHere + "/_bundle")
StzDirDeleteAll(cHere + "/_live")
```

> run: kept (touches files)

The assistant left the site `absent`, and the person made it `launched`. The honest half: the manifest's artifacts line reads `index.html,stz.js`, and no engine file for the web part is in it, because the engine compile was off. The block says what the run shipped, and not what a full run would. A bare `Deploy(:Production)` with no actor at all returns a rehearsal and writes a warning, "no effectful actor -- returning a rehearsal (nothing committed)". I ran it too, in my research run of 8 October 2026 and not in a block shown here: the site stayed absent and nothing was written.

I did not run `Deploy(:Emulated)`, because it builds each part's subset through the engine toolchain, and the toolchain's build is something this machine must not run. What I ran is the bundle without the compile. In my research run of 8 October 2026, outside this chapter's blocks, its map named an engine file that is not there. Section 7 says what that means for the claim that the engine runs in a browser.

### The deployment

For a local site, a rollout that fails undoes what it had done; the other kinds of site only try, as a best effort. The web part deploys and passes its gate. The api part's store fails. The remaining steps are skipped and the deployment does not commit. What becomes of the web site, already live? The failing site is a server with no storage location, which fails without spawning anything:

```haro
cHere = StzReplace(WorkingDirectory(), "\", "/")
oShop10 = new stzDelivery("shop")
oShop10.AddBackend(:api, :LinuxServer)
oShop10.AddSuperApp(:web, :Browser)
oGood = new stzDeploymentSite("cdn")
oGood.SetKindQ(:LocalRepo).SetStoreAtQ(cHere + "/_site_cdn")
oBad = new stzDeploymentSite("prod-api")
oBad.SetKindQ(:Server)
oRun = new stzDeployment(oShop10)
oRun.SetActor(HumanActor("ops"))
oRun.SetTarget(:web, oGood)
oRun.SetTarget(:api, oBad)
oRun.RunAfter(:api, :web)
aRun = oRun.Run()
? aRun[1]
#--> 0
for aLine in aRun[2]
	? aLine[1] + " -> " + aLine[2]
next
#--> store:web -> done
#--> launch:web -> done
#--> verify:web -> done
#--> store:api -> FAILED
#--> launch:api -> skipped
#--> verify:api -> skipped
? oGood.Status()
#--> rolledback
StzDirDeleteAll(cHere + "/_site_cdn")
```

> run: kept

The api store reads `FAILED`. The web site, whose three steps read `done`, reads `rolledback`! With an assistant as the actor, the same run returns every step as *rehearsed*, the site stays absent, and no folder is created. I ran it in my research run of 8 October 2026, outside this chapter's blocks, and do not print it.

The deployment fails safely; the services come next.

### Code first, subscribe later

The code asks for a service by name and never learns which implementation it got. The sandbox sees the first call and none after I rebind the service as live; the second call goes to the live adapter. The surface is sound once every live binding names a secret that the store holds. The live gateway in this block is a stand-in class written here, since the library ships no live card-gateway adapter. A stand-in named `LiveGateway` that returns "authorized" is a fake in everything but its name. The registry takes it as live because it declares nothing, and section 7 says why that matters:

```haro
oPay = new stzPaymentsSandbox()
oReg = new stzServiceRegistry("shop")
oReg.DeclareMany([ :payments, :mail ])
oReg.Bind(:payments, oPay)
oReg.Bind(:mail, new stzMailSandbox())
? Checkout(oReg, 4200)
#--> authorized
? oPay.NumberOfAuthorizations()
#--> 1
oStoreCf = new stzSecretStore("shop")
oStoreCf.Register( (new stzApiKey("stripe-key")).FromLiteralQ("sk-test-123") )
oStoreCf.Register( (new stzApiKey("mail-key")).FromLiteralQ("mk-test-123") )
oReg.BindLive(:payments, new LiveGateway, "stripe-key")
oReg.BindLive(:mail, new LiveMailer, "mail-key")
? Checkout(oReg, 4200)
#--> authorized
? oPay.NumberOfAuthorizations()
#--> 1
? oReg.PostureOf(:payments)
#--> live
oReg.SetPhase(:production)
? oReg.IsSoundVia(oStoreCf)
#--> 1

func Checkout poReg, nCents
	aRes = poReg.Service(:payments).Authorize(nCents, "tok_visa")
	poReg.Service(:mail).Send("dana@example.com", "Receipt", "Thank you.")
	return aRes[:status]

class LiveGateway
	def init
		return
	def Authorize nAmount, cToken
		return [ :status = "authorized" ]

class LiveMailer
	def init
		return
	def Send cTo, cSubject, cBody
		return 1
```

> run: kept

The day you do subscribe, you change a binding and not a line. The key is an invented test string and not a real one.

### Production refuses

One report names five of the eight ways a surface is not fit for production. Four are errors: a declared service never bound (`unbound-service`), a fake (`sandbox-in-production`), a real database that vanishes on restart (`ephemeral-in-production`), and a live adapter whose key is not in the store (`live-without-secret`). The fifth is a warning: a live adapter that names no secret at all (`inline-credential`). Chapter 31 showed the unbound one and the raise. This is the rest of the list. In the development phase the surface is already not sound, since an unbound service and a missing key are errors in any phase. The other two errors appear only in the production phase. The code lists eight invariants, and the service plan (section 4) and the narration list five:

```haro
oStoreSf = new stzSecretStore("shop")
oSurf = new stzServiceRegistry("shop")
oSurf.Bind(:payments, new stzPaymentsSandbox())
oSurf.Bind(:scratch, StzMemoryDataSourceQ())
oSurf.BindLive(:cache, new stzString("cache-adapter"), "redis-url")
oSurf.BindLive(:sms, new stzString("sms-adapter"), "")
oSurf.Declare(:reporting)
? oSurf.IsSoundVia(oStoreSf)
#--> 0
oSurf.SetPhase(:production)
oSurf.ReportVia(oStoreSf)
#--> Service registry 'shop' [production] -- 4 bound: 1 sandboxed, 1 local, 2 live
#-->   [ERROR] unbound-service @ shop/reporting -- declared but never bound -- asking for it will raise
#-->   [ERROR] sandbox-in-production @ shop/payments -- still bound to a SANDBOX in a production phase -- a fake must never ship
#-->   [ERROR] ephemeral-in-production @ shop/scratch -- a LOCAL source that vanishes on restart (in-memory) is bound in a production phase
#-->   [ERROR] live-without-secret @ shop/cache -- credential 'redis-url' is not in the secret store
#-->   [WARN] inline-credential @ shop/sms -- live adapter bound without naming a store secret
```

> run: kept

Two different questions are asked at the door: who is refused, and what is refused. Why is each refused? Ask the registry twice, once with an assistant and once with a person, in the development phase:

```haro
oStoreWw = new stzSecretStore("shop")
oOne = new stzServiceRegistry("shop")
oOne.Bind(:payments, new stzPaymentsSandbox())
? oOne.Phase()
#--> development
? oOne.MayGoLive(LLMActor("assistant"), oStoreWw)
#--> 0
? oOne.WhyNotLive(LLMActor("assistant"), oStoreWw)
#--> actor 'assistant' is not effectful -- it may propose, not commit
? oOne.MayGoLive(HumanActor("dana"), oStoreWw)
#--> 0
? oOne.WhyNotLive(HumanActor("dana"), oStoreWw)
#--> sandbox-in-production: still bound to a SANDBOX in a production phase -- a fake must never ship
? oOne.Phase()
#--> development
```

> run: kept

The assistant is refused for who it is: `actor 'assistant' is not effectful -- it may propose, not commit`. The person is refused for what the surface is: `sandbox-in-production: still bound to a SANDBOX in a production phase -- a fake must never ship`. And asking leaves the phase where it was: `development` before, `development` after, though the question is asked in the production frame.

And the registry knows services while the delivery knows parts. Joined, they answer a question neither can alone. Which part is about to ship on a double? The registry itself reports nothing, since the phase is development and there are no findings. The part-level check answers anyway, by destination, and names the part:

```haro
oS3 = new stzServiceRegistry("shop")
oS3.DeclareMany([ :payments, :cache ])
oS3.BindSandbox(:payments, new stzPaymentsSandbox())
oS3.BindLocal(:cache, StzMemoryBlobStoreQ())
oD3 = new stzDelivery("shop")
oD3.AddBackend("api", "linux")
oD3.AddApp("web", "browser")
oD3.UseServicesQ(oS3)
oD3.NeedsServiceInQ("api", [ :payments, :cache ])
oD3.NeedsServiceInQ("web", [ :reporting ])
oD3.DeployTo(StzDeploymentSiteQ("host1"), "api")
? oS3.Phase()
#--> development
? len(oS3.Findings())
#--> 0
for aF in StzCheckServiceDelivery(oD3)
	? aF[:rule] + " @ " + aF[:where] + " [" + aF[:severity] + "]"
next
#--> production-part-uses-sandbox @ api [error]
#--> production-part-uses-ephemeral @ api [error]
#--> part-uses-undeclared-service @ web [warning]
```

> run: kept

It names `api` twice, with `[error]`, and `web` once, with `[warning]`, where the registry reported nothing!

That is what the run showed; the decisions behind it come next.

## 4. The decision, and what I refused

Everything below is from the library's design documents and narrations, written in sessions with no author line. The record holds no ruling of my own for this chapter. Its decisions are the documents'.

**I refused the simulator that lies.** The emulator does not mock. Each part runs the same compiled engine artifact that will ship to its target. That claim has a caution, in section 7: the proof that the engine runs in a browser is not in the pinned tree.

**I refused to re-ship what the target does well.** The edge carries a capability only if it is critical and either unique or weak on the target.

**I refused tool sprawl, and the convention enforced by hope.** The target should be one config away, and deploying to it should be one governed act.

**I refused an inline secret.** A site carries an auth reference, not a key.

**I refused to touch reality by default.** Production commits only if the actor may commit. A bare `Deploy(:Production)` with no actor touches nothing.

**I refused the agreeable fake.** An agreeable fake is more dangerous than no fake at all. I hold this as a view, not a result. Silence is the worst answer: the lenient mode answers 501, because a miss must never be mistakable for success.

**I refused "fake versus real" as the whole truth.** It was too coarse. There are four postures now: sandbox, local, live, and conformance. The local posture was added when the database exemplar showed that a SQLite file is a real database in a file you own.

**I refused a gate that fails open.** The registry once kept its state in attributes. Attaching it to a delivery took a snapshot, so the gate would have passed an unsound surface. A gate that fails open is worse than no gate: this is my view. The state now sits in a table keyed by identity, so every copy is the registry. Anything that governs others must survive being copied.

**I refused to virtualize the quality of a model.** Frontier-model quality cannot be virtualized. What the sandbox sells instead is determinism, a cost you can assert, and working offline.

**I refused to ship the live adapters.** The service plan says the live Stripe, PayPal and Adyen adapter is deliberately not shipped, since an account, a key and a network are infrastructure-gated. A hub adapter is built, and chapter 31 shows it. The contract is defined, and the registry refuses to let the fake ship in its place.

**I refused to ask a question in the wrong frame.** `MayGoLive` once asked about soundness in the current phase, so with a fake bound it answered yes. Now it is asked in the production frame whatever the phase.

**I refused to say the restaurant's need was the design's origin.** The site says that the emulation and deployment designs take a solution as an example. It is an example, not the origin of the design. The sample solution in the documents carries a customer's product name, and I have renamed it in every block. Chapter 28 told the story, and I do not repeat it.

The service plan is headed "written 2026-07-23 in answer to the user's question". The question asks whether emulation covers databases, business APIs, frontier models and cloud providers. The aim is that a programmer can code a whole program without subscriptions or fees and still get a working solution ready to deploy. The chapter tells the plan's own heading and date. The record does not say who asked, and the chapter does not claim it was the author's question.

## 5. The court

`service_registry_narrated` proves the declared surface, that an unbound service raises, and that the application asks by name. It proves that a sandbox in production is a violation, with one finding per fake, and that the credential must be in the store. It proves that going live is a governed crossing, with an assistant refused and a person refused over a fake, and that asking leaves the phase. It also proves the CI helpers, the fourth posture, and a live adapter that needs a certificate. `service_delivery_narrated` proves the external surface rehearsed in the plan, and the pre-flight. It proves the gate, which in a production deploy refuses a fake and logs every reason, and opens once the surface is real. It proves that the registry is one registry however many copies are made, and the question of which part depends on a fake. My research run of 8 October 2026 ran both: 93 of 93 and 60 of 60. The second left a file of zero bytes beside itself, and I removed it.

`virtual_system_twin_narrated` proves, in twelve scenes, that the twin touches nothing real, that the plan narrates and flags, that commit is the one door, that a scope refuses, and that a reviewer rejects a step. It proves, too, that a hundred operations stay in memory until one commit. `virtual_environment_twin_narrated` proves the same shape for variables, a directory and queued spawns. `emulator_narrated` proves that the bundle generates, the map renders every part by role, and each part carries only its subset. `deployment_narrated` proves the site as config, the governed commit, the step plan, the rollback, feasibility, and the git backend; it spawns `git`, so the book does not run it. `full_scope_model_narrated`, scenes 13 to 16, proves that building precedes deploying, that an unsound solution cannot be built, the lowering bridge, and the governed deploy.

The refusal that production makes is proved by the first two guards, which ran. That the rehearsed engine runs in a browser is the next proof: no guard that runs checks it today.

## 6. The field, and where it leads

Real services lead. The plan says it: a double is not the real service, and you still need at least one real run before production. A scripted gateway is not a vendor's edge cases. Recorded answers drift, and a replay suite needs re-recording and contract tests against the real API. The library has the recording call; a drift check for recorded answers is designed.

Frontier models lead, and cannot be emulated. The model is judged against the real model, deliberately, as its own activity.

Live infrastructure leads. The deployment is infrastructure-gated: live verification against a real host or account. The commands are generated, and one reachable host away from literal.

The mature deploy tools lead. The narration says it plainly: this does not replace every mature deploy tool, it unifies the seams those tools leave exposed.

Fidelity has a stated boundary. Emulation is faithful but not omniscient, so it says which is which. What a double proves is narrower still: a capture sink proves what you would have sent, and a directory is not a CDN.

Where I think the record stands apart is the coupling. The double, the plan, the credential names, the gate and the actor are declared in the same program that ships, and one gate judges them.

That is the field; the limit is where I stop.

## 7. The limit

**A hand-written fake that says nothing about itself passes the gate.** The registry reads what the object says it is. A double that declares neither that it is a sandbox nor that it is local and real is taken for live: no opinion means live. So "production refuses a fake" is exact for the library's own doubles, and for any double that declares itself. What posture does the registry give a double that declares nothing, and is the surface sound? Ask it in the production phase:

```haro
oUndeclared = new stzServiceRegistry("shop")
oUndeclared.Bind(:payments, new AlwaysYes)
oUndeclared.SetPhase(:production)
? oUndeclared.PostureOf(:payments)
#--> live
? oUndeclared.IsSound()
#--> 1

class AlwaysYes
	def init
		return
	def Authorize nAmount, cToken
		return [ :status = "authorized" ]
```

> run: kept

It answers `live`, and `IsSound()` answers `1`: the always-yes double passed! The stand-in of the earlier block, `LiveGateway`, is such an object.

**The lowering knows two verbs.** Only `read_pin` and `write_pin` become code. Any other rehearsed operation becomes a comment line. In my research run of 8 October 2026, outside this chapter's blocks, I rehearsed `UseIn(:sensor, :gpio, "blink the status led")` and the firmware got a comment. For a server or a phone, the artifact is a header with no lines when nothing was rehearsed. The narration's "the board is the last inch" holds for reads and writes of pins only.

**The fidelity contract is by target class.** The design says each part declares what is faithful and what is approximated. The code returns one fixed text for a microcontroller, listing two approximated things, and one for everything else, "faithful".

**The sizes are estimates.** The plan prints a figure from a catalogue, and the narration prints two different figures for the same part. Do not print a size as a claim.

**`Deploy(:Emulated)` does not yet move the registry.** The plan says it resolves services to sandboxes. The code builds the emulator and returns; only the production deploy touches the registry's phase. The `:emulated` phase value that the registry has is set today only by a guard; setting it from the emulated deploy is designed.

**A refused `Deploy(:Production)` leaves the registry in the production phase.** After my refused deploy (my research run of 8 October 2026, outside this chapter's blocks), `Phase()` printed `production`. The pre-flight restores the phase, and the deploy does not.

**A plan flags today; ranking is the direction.** Chapter 20 said it, and the framework document says "ranked risk assessment".

What is designed: the engine running in a browser. The documents say that the phone's `solve 2 -8` returns `x = 4` in a page. The guard that checks it, `wasm_narrated`, says in its own header that it checks the wiring and the build, since the host language cannot execute wasm. It cites an in-browser page with "8/8 checks". That page is not in the pinned tree: I searched for it and found none. And I have not seen the emulator's surface in a browser, and the record names no one who has. By the law of chapter 33, that surface is unperceived. So the chapter says: wired, its build checked by a guard that I did not run, not seen in a browser by anyone the record names.

Also designed: branches of a twin and the plan's alternatives and feedback, for which no method is built yet; twins for databases, interfaces and networks; and a drift check for recorded answers.

What is absent: a live card-gateway adapter for payments (a hub adapter is built and proved only against a twin, chapter 31), a frontier model, an object store, SMS or mail. The contracts and doubles ship, and the live clients do not, deliberately. Live verification of a remote host or account: commands are generated, and nothing ran against a host. A customer solution emulated and deployed through this path: nothing in the record yet, which chapter 33 carries as the next line.

## 8. Six doors

**The programmer.** You code the whole integration against names, with doubles that raise when you forgot something and a counter that lets you assert a fee. The day you subscribe, you change a binding and not a line. The loss: a double you wrote yourself that declares nothing is taken for live by the gate.

**The analyst.** Before anything moves you can read the placement plan, the external dependencies with the credentials production will ask for by name, the step graph, and which part depends on a fake. The sizes are estimates, and the findings are by part.

**The designer.** The emulator generates a surface from the plan, with a parts grid by role and one window per part. I checked the generated text only, and never the look. Say "generated", and not "seen".

**The decision-maker.** "Who may deploy?" is a property. An assistant may plan the release and the site stays absent. A person may commit. Neither may ship a declared fake. The loss to print: live hosts and real providers are gated by infrastructure, and the record names no live run.

**The educator.** A learner can build a whole shop's integration with no account, no key and no fee, and watch the double refuse what she forgot. Her deployment fails safely and rolls back.

**The agent.** You may rehearse the whole integration and plan the whole release, in a world where nothing real can move: a sandbox payment moves no money and a mail sink sends no mail. You may ask whether you may go live and be told why not. You cannot commit. The loss: that guarantee covers the library's own doubles, and a surface bound to something live is outside it.

## 9. Exercise

Write, under each line, what you expect before you run it:

```haro exercise
oMine = new stzServiceRegistry("my-project")
oMine.Bind(:payments, new stzPaymentsSandbox())
oMine.Bind(:notes, StzMemoryDataSourceQ())
oMine.BindLive(:maps, new stzString("maps-adapter"), "maps_key")
oStoreMine = new stzSecretStore("my-project")
# under each line, write the line you expect before you run it
? oMine.IsSound()
? oMine.IsSoundVia(oStoreMine)
? len(oMine.FindingsForProductionVia(oStoreMine))
? oMine.MayGoLive(HumanActor("me"), oStoreMine)
? oMine.Phase()
```

> run: exercise

Then register a key named `maps_key` in the store, and write the number of production findings again. Then bind a hand-written class with an `Authorize` method that always says yes, and ask what posture the registry gives it. If a promise breaks, do not change it: explain the output first. I do not tell you where you will be surprised.

I left this one in your hands. The block below is the one from section 3, "Code first, subscribe later", with one name changed. I changed it on purpose, and I do not say what it does:

```haro exercise
oPay = new stzPaymentsSandbox()
oReg = new stzServiceRegistry("shop")
oReg.DeclareMany([ :payments, :mail ])
oReg.Bind(:payments, oPay)
oReg.Bind(:mail, new stzMailSandbox())
? Checkout(oReg, 4200)
? oPay.NumberOfAuthorizations()
oStoreCf = new stzSecretStore("shop")
oStoreCf.Register( (new stzApiKey("stripe-key")).FromLiteralQ("sk-test-123") )
oStoreCf.Register( (new stzApiKey("mail-key")).FromLiteralQ("mk-test-123") )
oReg.BindLive(:payments, new LiveGateway, "stripe-live")
oReg.BindLive(:mail, new LiveMailer, "mail-key")
? Checkout(oReg, 4200)
? oPay.NumberOfAuthorizations()
? oReg.PostureOf(:payments)
oReg.SetPhase(:production)
? oReg.IsSoundVia(oStoreCf)

func Checkout poReg, nCents
	aRes = poReg.Service(:payments).Authorize(nCents, "tok_visa")
	poReg.Service(:mail).Send("dana@example.com", "Receipt", "Thank you.")
	return aRes[:status]

class LiveGateway
	def init
		return
	def Authorize nAmount, cToken
		return [ :status = "authorized" ]

class LiveMailer
	def init
		return
	def Send cTo, cSubject, cBody
		return 1
```

> run: exercise

Run it. Compare the answer of its last line with the one section 3 gave, and explain any difference before you touch the name; section 3, "Production refuses", shows how to ask the registry for its report. When you have solved it, you will know what makes a live binding sound: a secret that the store holds, and not only a name.

The next chapter turns from the services behind a program to its users: your users keep their medium, and a new medium adds renderings, never verbs.
