# A world, a constellation, a platform, and the architect

Source: Chapter 23. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: a world as a declaration with a being, a becoming and a way of being met; a goal whose gap is measured; a constellation of worlds with bonds and three gates on every crossing; the commons as a platform; the capability seam; the profile of a solution as a text file, and the three system scopes; designed: the near-natural idiom of the constellation; a call routed into a nested constellation; shells that embed the engine; the architect's certification, which is a proposal; the five-row guarantee sheet, as a requirement; absent: a world that judges its own truths; a narration for the constellation or the platform envelope; a written five-row guarantee sheet for any solution

Run: 10 of 10 blocks kept their promise, on 2026-10-12 16:28 UTC+01:00.

In this chapter I declare a solution at three levels, a world, a constellation and a platform, and I name the one person who declares all three, the architect. I take the field's three habits first: the super-app, the context map and the platform team. Then I run a world that explains itself, a constellation whose crossings are refused one gate at a time, and a profile that a platform refuses to build when it is not sound. I say where the code stops: a world's truths are narrated and not judged, the shells are tiny, and the architect's certification is a proposal. The principle is this: the solution is declared as worlds, bonds and an envelope before any of it is built, and every crossing between them is governed.

## 1. The concept, as the field holds it

Three habits of the field have each a home, and I take them from general knowledge, not from a study of the record. The record holds no field study of super-apps, of platform engineering or of context maps. Its only named field is one line of a design document: a famous messaging super-app, and its kin.

The first is the super-app and the mini-program. One large application embeds a runtime and runs small applications inside it, sharing its services and its store. The host is privileged, the mini-app second-class, and the isolation a sandbox.

The second is the bounded context and the context map of domain-driven design, of 2003. A large system is cut into models, each with its words, and a map shows how they relate. It is the field's nearest idea to a world and a bond. It lives in diagrams and in review, and not in a running registry that refuses a call.

The third is the platform team and the deployment declared as code. A team builds the internal base that others deploy onto, and tools declare machines before they exist. The person who works across the floors is, in the field, a software architect, a solutions architect or a platform engineer: a title held by a person, whose artefacts are diagrams and manifests.

For the scopes, the field's home is the compiler: the target of a build, and the check that flags a call the minimum platform level lacks. Each decides which system the code is for. None lets the program name that system at the call site and refuse the act.

The shared shape: the field draws the picture, a host, a map, a diagram, and keeps the judge outside it. In all three the program knows nothing of its own composition. This is my reading of the three, not a survey of the field.

## 2. The first principle

**The solution is declared as worlds, bonds and an envelope before any of it is built, and every crossing between them is governed.**

The sentences of the record are three. An application is a living world of meaning. Worlds, not mini-apps: a governed graph and not a host container. A Softanza architect models the deployment architecture first, as a declarative artifact, before a line of system feature code. The sentence above is built from the three and from the book's method, which is to declare and then govern. The three are the record's, put in my words; the sentence above is the chapter's own principle, in the book's voice.

## 3. The Softanza form

Three levels, then. A world is one application. A constellation is a graph of worlds. A platform is the envelope around a solution and the ground a constellation stands on. And one person declares all three.

### A world

A world has a being, a becoming, and a way of being met. Chapter 4 showed its being. What does a world answer when it is asked to explain all three? Ask one, for an agency that visits clients:

```haro
oApp = new stzApp("FieldVisits")
oApp {
    AddThingQ(:Account) { Has([ :number, :chapter, :balance ])  IsTrue(:balance, "@ >= 0") }
    AddThingQ(:Client)  { Has([ :code, :name, :city ])  Owns(:Account) }
    AddThingQ(:Visit)   { Of(:Client)  Has([ :agent, :date, :subject ]) }
    AddRelation(:Account, :belongsTo, :Client)
    AddFlowQ(:agent, :records, :Visit) { Require(:subject) }
    AddReactionQ(:Client).Unseen(90, :Days) { Propose(:Visit) }
    AddGoalQ(:EveryClientSeenThisQuarter) {
        Means      = "every :Client Has(:visit) Since(:quarterStart)"
        ReachedBy  = :planning
    }
    SetBody([ :GraphDB, :Files ]) { Graph = ".stzapp/world.stzgraf"  Files = "./" }
}
oApp.AddScreenQ(:ClientFile) { ToUnderstand(:Client)  Shows([ :identity, :accounts, :visits ]) }
oApp.AddRefinementQ(:balance).Bounds(0, 1000000)
oApp.AddReaches([ :mobile, :desktop, :web ])
oApp.Explain()
#--> WORLD FieldVisits   lives in: graphdb + files
#      BEING
#        account (number, chapter, balance)
#            true when balance @ >= 0
#        client (code, name, city)
#        visit (agent, date, subject)
#      RELATIONS
#        client owns account
#        visit of client
#        account belongsto client
#      BECOMING
#        when agent records visit require subject
#        whenever client unseen 90 days -> propose visit
#        wants everyclientseenthisquarter -> reached by planning
#      MET FROM WITHOUT
#        screen clientfile: understand client shows identity, accounts, visits
#        refine balance bounds [0..1000000]
#        reaches mobile, desktop, web
```

> run: kept

`SetBody` only declares. No file was written by this block.

A world strives. A goal is a wanted state of the graph, and the gap is measured. A goal with no pattern to evaluate is refused, and never faked:

```haro
oApp = StzAppQ("visits")
oApp.AddThingQ(:Client) { Has([ :code, :name ]) }
oApp.AddThingQ(:Visit)  { Of(:Client) }
oApp.AddGoalQ(:EveryClientVisited) { Means = "every :Client Has(:visited)"  ReachedBy = :planning }
oApp.AddInstance("anna", :Client)
oApp.AddInstance("bilal", :Client)
oApp.Relate("anna", :visited, "visit1")
? @@( oApp.Pursue(:EveryClientVisited) )
#--> pursuing everyclientvisited via planning -- 1 proposal(s)
#    [ [ "attend", "client", "for", "bilal" ] ]
? oApp.GoalSatisfied(:EveryClientVisited)
#--> 0
oApp.Relate("bilal", :visited, "visit2")
? @@( oApp.Pursue(:EveryClientVisited) )
#--> pursuing everyclientvisited via planning -- 0 proposal(s)
#    [ ]
? oApp.GoalSatisfied(:EveryClientVisited)
#--> 1
oApp.AddGoalQ(:Vague) { Means = "make things nice" }
try
    oApp.Pursue(:Vague)
catch
    ? cCatchError
done
#--> stzGraphGoal.FromMeans: no 'every :Type' clause in 'make things nice'.
```

> run: kept

`Pursue` prints its own first line, and then the `?` prints the list it returns. One relation later the gap is closed: `0 proposal(s)`, and `GoalSatisfied` answers `1`. The vague goal is refused with its reason: `no 'every :Type' clause in 'make things nice'`. With a reaction declared, the same gap proposes a *visit* for Bilal, and without one the default act is *attend*.

### A constellation

Nothing crosses between worlds unless it is declared and governed. A bond must exist, and then three gates stand on the crossing: the act must have a declared risk tier, the caller must hold the permission, and the caller's authority must cover the risk. Each refusal names its gate. Which gate refuses first? The bond exists in all four calls below, so the three refusals are the governance's:

```haro
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oSupplier = StzAppQ("supplier")
oSupplier.AddThingQ(:crate) { Has([ :produce, :qty ]) }
oCon = new stzSuperApp("acme-group")
oCon.AddWorld("resto", oResto)
oCon.AddWorld("supplier", oSupplier)
oCon.Bond("resto", "supplier", "order-produce")
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 0
? oCon.Why()
#--> governance refused: refused: 'order-produce' has NO declared risk tier (undeclared actions never proceed)
oCon.GovDeclareRisk("order-produce", 2)
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 0
? oCon.Why()
#--> governance refused: refused: 'resto' lacks PERMISSION (can) for 'order-produce'
oCon.GovGrant("resto", "order-produce")
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 0
? oCon.Why()
#--> governance refused: refused: 'resto' holds '' authority (level 0) but 'order-produce' is risk tier 2 (SHOULD does not cover it)
oCon.GovSetAuthority("resto", :Delegated)
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 1
? oCon.Why()
#--> allowed: active + bonded + governed
? oCon.GovernanceQ().NumberOfDecisions()
#--> 1
? @@( oCon.GovernanceQ().DecisionsOf("resto")[1][2] )
#--> [ "rationale", "cross-world call cleared" ]
```

> run: kept

The risk tier refuses first: `'order-produce' has NO declared risk tier`. The doubled word "refused: refused:" is the library's own text. The cleared crossing wrote a decision by itself! Its record holds the authority and the risk of that moment, and a clock read, so the block prints only the rationale. That is the lineage chapter 30 uses.

The shared ground is a world too. Inside a constellation the commons is itself a platform, and it holds an identity, a session and a store. The commons is not a special kind of node; the design's own words are that it is uniform and recursive. What class is the commons? Ask it:

```haro
oCon = new stzSuperApp("acme-group")
oDb = new stzDatabase(":memory:")
oCon.OpenCommonsOn(oDb)
? classname( oCon.CommonsQ() )
#--> stzplatform
? oCon.RegisterIdentity("owner", "s3cret")
#--> 1
? oCon.RegisterIdentity("owner", "other")
#--> 0
? len( oCon.OpenSession("owner", "s3cret") ) > 0
#--> 1
? oCon.OpenSession("owner", "wrong") = ""
#--> 1
oCon.StorePut("currency", "EUR")
? oCon.StoreGet("currency")
#--> EUR
oDb.Close()
```

> run: kept

This block uses an in-memory database, so no file and no network. The session token is random, and only its presence is printed. Secrets are stored salted and hashed, with the engine's key-derivation function. The first line answers `stzplatform`, and that is the point: a platform is not only the envelope around a solution. It is what a constellation stands on. In code the commons is not a node of the constellation graph: when I probed it the graph held two nodes for two registered worlds. World zero is a role the platform plays.

A world is swapped live and keeps its bonds. A constellation nests in another. A name is taken once:

```haro
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oCon = new stzSuperApp("acme-group")
oCon.AddWorld("resto", oResto)
oCon.AddWorld("supplier", StzAppQ("supplier"))
oCon.Bond("resto", "supplier", "order-produce")
oCon.GovDeclareRisk("order-produce", 2)
oCon.GovGrant("resto", "order-produce")
oCon.GovSetAuthority("resto", :Delegated)
oNew = StzAppQ("supplier-v2")
oCon.Swap("supplier", oNew)
? oCon.NumberOfWorlds()
#--> 2
? oCon.WorldQ("supplier").Name()
#--> supplier-v2
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 1
oHolding = new stzSuperApp("holding")
oHolding.AddConstellation("acme", oCon)
? oHolding.KindOf("acme")
#--> super
? oHolding.WorldQ("acme").NumberOfWorlds()
#--> 2
? oCon.KindOf("resto")
#--> app
try
    oCon.AddWorld("resto", oResto)
catch
    ? cCatchError
done
#--> stzSuperApp: world 'resto' already in the constellation.
```

> run: kept

The bond survived the swap: `CallAcross` still answers `1`! Chapter 28 used `Retire` and `Revive`, and this block is `Swap` and `AddConstellation`. Nesting is a fact of the registry. Nothing in the code routes a call into a nested constellation, so the recursion of the design is a registry's recursion and not yet a call's. A crossing is a verdict: `CallAcross` clears or refuses with 1 or 0, and nothing is handed to the target yet.

One trap. A registered world is a copy. The host language copies an object by value when it is stored, so the world you register is not the world you hold. The header of the class says it: world objects are reached through the registry index, the live path. Configure the world fully, register it, and reach it through the constellation from then on. The envelope has the same doctrine: setting a world on the platform harvests its declarations at call time, and setting the governance snapshots the regime.

### The envelope, and the seam

A platform grants a capability of a device only if governance clears its risk. A permission is held and the world is refused anyway. The risk tiers, two for the camera and four for payments, are the library's declared ones:

```haro
oGov = new stzGovernance("resto-regime")
oGov.GrantPermission("resto", "use-camera")
oGov.GrantPermission("resto", "use-payments")
oGov.SetAuthority("resto", :Delegated)
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oPlat = StzPlatformQ("resto-envelope")
oPlat.SetWorld(oResto)
oPlat.SetGovernedBy(oGov)
oPlat.AddCapabilityQ(:camera).SetPurposes([ :scan_dish_photo ])
? oPlat.Granted(:camera)
#--> 1
oPlat.AddCapabilityQ(:payments).SetPurposes([ :charge_guests ])
? oPlat.Granted(:payments)
#--> 0
? oPlat.Why()
#--> refused: 'resto' holds 'delegated' authority (level 2) but 'use-payments' is risk tier 4 (SHOULD does not cover it)
```

> run: kept

The class header says what the world lacks: the world models the world, and deliberately lacks the operational envelope. The envelope's duties are generation, the capability seam, the commons runtime, a networked body and a registry with enforcement. Generation is real, and refuses to generate for a world that declares no reach. The success path writes real files, so I do not run it here. I ran it once, for a world of one screen and one thing, and removed what it wrote. The web shell is a page of 318 bytes with the world's screens and things as list items, and the desktop shell a launcher of 251 bytes; other worlds give other sizes. That is the limit of "per-platform shells": generation is real, and tiny.

### The architect, and the three scopes

By *scope* I mean the System Foundation's: development, deployment, and runtime-current. Every system act is written in a named scope. A Softanza architect models the deployment architecture first. The same verb, in two scopes, gets two verdicts, and the target's own words say why:

```haro
oSol = new stzPlatformProfile("greenhouse")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oSol.WithSuperApp(:phone, :Android)
oSol.WithApp(:sensor, :ESP32)
? oSol.DevelopmentSystem().OSName()
#--> windows
? oSol.App(:phone).System().OSName()
#--> android
? oSol.App(:sensor).System().OSName()
#--> espidf
? @@( oSol.App(:sensor).System().System().Capabilities() )
#--> [ "gpio", "network", "clock", "threads" ]
? oSol.CurrentSystem().IsRuntime()
#--> 1
? oSol.App(:backend).System().Spawn("cron")
#--> native
try
    oSol.App(:phone).System().Spawn("cron")
catch
    ? cCatchError
done
#--> scope 'android' (android) forbids 'process' -- spawn 'cron'. This target has no such capability.
```

> run: kept (touches the system)

The development system's name is the declared one, so it does not depend on the machine. The line `native` is host-dependent: it holds only on a host that can spawn a process, as chapter 31 says of its own word. The Android refusal, `scope 'android' (android) forbids 'process'`, and the capability list of the board are the target's, whatever the host. The three scopes are `new stzDevSystem()` or `DevelopmentSystem()` for development, which is tooling only; `App(:x).System()` for deployment, where feature code is written and checked; and `new stzCurrentSystem()` or `CurrentSystem()` for runtime-current, which is what runs now. The scope object has no `Capabilities()` of its own: the call goes through `.System().System()`. A request.

The architect's artefact is a text file. Can it be read back, and what does the platform say of a solution that is not sound? Run it:

```haro
oSol = new stzPlatformProfile("greenhouse")
oSol.DevelopedOn(:Windows)
oSol.WithServer(:backend, :LinuxServer)
oSol.WithSuperApp(:phone, :Android)
oSol.WithApp(:sensor, :ESP32)
? oSol.ToStzPlatform()
#--> # .stzplatform -- a Softanza solution profile
#    platform: greenhouse
#    developed_on: windows
#    server: backend -> linux
#    superapp: phone -> android
#    app: sensor -> espidf
oBack = StzPlatformProfileQ()
oBack.FromString( oSol.ToStzPlatform() )
? oBack.App(:sensor).DeploymentOSName()
#--> espidf
oBad = new stzPlatformProfile("empty")
? @@( oBad.Validate() )
#--> [ "no development system declared (use DevelopedOn)", "the solution deploys no apps" ]
oPlat = StzPlatformQ("empty")
oPlat.SetProfile(oBad)
try
    oPlat.Build()
catch
    ? cCatchError
done
#--> stzPlatform.Build: the solution is not sound -- no development system declared (use DevelopedOn); the solution deploys no apps
```

> run: kept

The file form is plain text that the architect owns, and it round-trips from a string. The unsound one is refused before building, with both faults named: `the solution is not sound -- no development system declared (use DevelopedOn); the solution deploys no apps`. The order of building and deploying is chapter 33's, and the gate on who deploys is chapter 24's.

Who is the architect? The record names the person twice by name: in the System Foundation, and in Central's memo for a school that would certify architects of Softanza, with three levels. That memo is marked withdrawn, as a launch prompt, on the day it was written. A third place, a private book of the estate on platform modelling, models platforms and does not name the architect. That certification is a proposal of 30 September 2026, not a delivery, and the site must not announce it. The estate's protocol defines a role as a profile held in a scope. Applied here, which is my application and not the record's, the architect is not a rank. It is what one holds in the scope of a solution: the profile, the worlds, the governance. I hold this as a view, not a result. The site has a journey page for the platform architect and a certification page that says the proposal is not announced (read from the site, 9 October 2026). I tell the architect as what one declares, and the certification is only that proposal; no school is named here.

## 4. The decision, and what I refused

**I refused the host and the mini-app.** Worlds, not mini-apps; a governed graph, not a host container. Chapter 4 told it, and I point back.

**I refused to make the commons a special kind of node.** It is a world, and a world is uniform and recursive.

**I refused the sandbox as the definition of isolation.** Isolation is a declared, inspectable meaning and not a black-box virtual machine. A world's sovereign body plus norm-gated bonds. A runtime sandbox is only an implementation for untrusted worlds.

**I refused to make governance one more facet, beside the design's constellation, bonds, commons, reach and presence.** It is the ambient. In code, one governance per constellation, configured through it, so that there is one live governance and never a stale copy held by a caller.

**I refused to give the world the envelope.** `stzApp` models the world, and deliberately lacks the operational envelope.

**I refused to freeze *current* under a better name.** The cure is not a better name: every system act is written in a named scope. The attempts it refuses are a pair of words, this system and the target system, and a triple, host, runtime and target.

**I refused to deploy a profile.** We do not deploy a profile; we deploy a platform and its parts. The profile only describes. The platform owns it and drives the building and then the deployment.

## 5. The court

`06_stzsuperapp_narrated` proves that worlds register as nodes; that the commons holds an identity and a store; that a crossing is refused for an undeclared risk, accepted when governed, and refused when unbonded with the bond named; that a retired world breaks its bonds and revives; that a swap keeps the node and the bond; and that a constellation nests in another. `01_platform_narrated` proves that shells are generated per declared reach and a world without a reach is refused; that a capability is granted only when governance covers its risk tier, and a capability never requested is refused with a reason. It proves that the commons registers identities, opens sessions, posts and reads messages, and stores; that the world is served over a real port; and that the registry refuses a call to an unbonded or retired world. It writes shells beside itself and opens a loopback port. `full_scope_model_narrated`, which the guard calls the architect's common ground, proves that the solution is modelled first, that an unsound one is flagged, that the three scopes are distinct, that the scope refuses what the target forbids and rehearses what the host lacks, that the text file round-trips, that building precedes deploying, and that a deploy by a language-model actor is refused. `04_stzapp_pursue_narrated` and `05_stzapp_live_narrated` carry the goal and the reactions.

The guard the chapter does not have: none judges a world's truths, a flow, or the time of a reaction.

## 6. The field, and where it leads

The super-app leads in users. The design names its model and replaces it; chapter 4 says the record measures nothing against them. The Platforms page prints the other half: the customer platforms run today on ordinary web stacks. No platform runs on the constellation in production.

The field leads in shells. The design promises a progressive web app, a desktop shell, a mobile shell. The code generates a page and a launcher of a few hundred bytes. The shells are designed. Generation is built, and tiny.

The field leads in what a bounded context carries: a team and a language. A world carries a graph and a narration. The persona a world is for is not a field of the class: a world has the list of surfaces it reaches and nothing else about whom it serves. The site's five things, a shared ground, a world for each person and device, bonds, rules, roles, are true of the commons, the bonds and the governance. The roles are the actors, permissions and authority of the governance. There is no role class, and a world per person and device is a naming convention.

The Atlas does not rate this plane. `stzApp` is named once, in the lane of the area for interfaces called App shell and windowing; that lane, not the world, is rated solid, with the note that there is no multi-window orchestration, dialogs, menus or tray. The platform in a lane of the area for the system. The constellation in none.

The compiler leads on scopes. It checks against a target in daily use at scale; Softanza's scope is a runtime object that a program asks. What it adds is a verdict at the call site in the target's own words, and a twin that rehearses what the host lacks, which is chapter 24.

Where the field and the record meet: a super-app is a graph of graphs. The field's context map is a diagram. Softanza's is a registry that refuses.

## 7. The limit

A world's truths are narrated and not judged. The number in a reaction is the first case. Do ninety days and one day give different proposals? A reaction fires for each instance that lacks a relation named after the thing it proposes, and the comment above `Pulse()` says so. Run two clinics:

```haro
oA = StzAppQ("clinic-a")
oA.AddThingQ(:Patient) { Has([ :name ]) }
oA.AddThing(:Checkup)
oA.AddReactionQ(:Patient).Unseen(90, :Days) { Propose(:Checkup) }
oA.AddInstance("alice", :Patient)
oA.AddInstance("bob", :Patient)
oA.Relate("alice", :checkup, "checkup-1")
oB = StzAppQ("clinic-b")
oB.AddThingQ(:Patient) { Has([ :name ]) }
oB.AddThing(:Checkup)
oB.AddReactionQ(:Patient).Unseen(1, :Days) { Propose(:Checkup) }
oB.AddInstance("alice", :Patient)
oB.AddInstance("bob", :Patient)
oB.Relate("alice", :checkup, "checkup-1")
oA.Live()
#--> [clinic-a] is live -- 2 thing(s), 0 flow(s), 1 reaction(s), 0 goal(s); 1 proposal(s)
oB.Live()
#--> [clinic-b] is live -- 2 thing(s), 0 flow(s), 1 reaction(s), 0 goal(s); 1 proposal(s)
? @@( oA.Proposals() )
#--> [ [ "propose", "checkup", "for", "bob" ] ]
? @@( oB.Proposals() )
#--> [ [ "propose", "checkup", "for", "bob" ] ]
```

> run: kept

Both clinics answer `[ "propose", "checkup", "for", "bob" ]`. Ninety days and one day give the same proposals.

The same reading holds for `IsTrue`, which is stored and narrated while instances carry no fields to judge it against. It holds for a flow's `Require` and `Then`, stored and narrated, where I found no executor; and for the bounds of a refinement. A world today declares that a balance must not be negative. It does not judge a balance. What it does judge is a goal's gap, a crossing and a capability. So I say "a world that wants" for the goal, and "narrated" for the truth. Chapter 4's `true when balance @ >= 0` is a declaration only. So the chapter says it in one line: declared and narrated; judged only for goals, crossings and capabilities.

The design writes more than the class speaks. Does the class speak the design's near-natural idiom for the constellation? Ask it for `Hosts`, `Admits` and `Explain`:

```haro
oSuper = new stzSuperApp("acme-group")
try
    oSuper.Hosts(:VisitApp)
catch
    ? cCatchError
done
#--> Error (R14) : Calling Method without definition: hosts
try
    oSuper.Admits(:VisitApp)
catch
    ? cCatchError
done
#--> Error (R14) : Calling Method without definition: admits
try
    oSuper.Explain()
catch
    ? cCatchError
done
#--> Error (R14) : Calling Method without definition: explain
```

> run: kept

Three times the answer is `Calling Method without definition`. `Shares`, `Provides`, `Norm`, `Reaches` and `Generate` are not defined on a constellation either. The class has `AddWorld`, `AddConstellation`, `Bond`, `Retire`, `Revive`, `Swap`, the `Gov*` family, `CallAcross`, `Crossings`, the commons calls, and calls that look: `Why`, `GraphQ`, `WorldQ`, `KindOf`, `IsActive`, `HasWorld`, `NumberOfWorlds`, `AreBonded`, `CrossingCount` and `LastCallMs`. The verbs of composition are these. The design's three aspects are reached today by `AddWorld`, `Bond` and `OpenCommonsOn`, and governance by `Gov*`; reach and presence are the part that is not there. The design's own header calls the document a forward design.

What is built: the world; the constellation with its gates, its ledger of crossings with timings, a decision written on a cleared crossing, and a refused crossing noted as evidence; the platform's capability seam, its commons, its registry, its shells, its profile with building then deploying; the three scopes.

What is designed: the near-natural idiom; a call routed into a nested constellation (today a crossing is a verdict, and nothing is handed to the target); loading one world without rebuilding a host; shells that embed the engine; the five-row guarantee sheet, which the vision asks for and the site's journey page marks designed: one row for each of five systems the solution answers to, technical, social, ecological, economic and cultural.

What is absent: a narration for the constellation or the envelope, since none exists. The narration for building a first app uses verbs the class does not have: seven of its calls fail at this commit, and I cite it for the idea and not the syntax. A customer platform on the engine as a constellation. The written five-row guarantee sheet: no solution has one. A lane of the Atlas for the world, the constellation or the envelope.

## 8. Six doors

**The programmer.** You declare a world with braces, ask it to explain itself, and cross between worlds with a call that returns 0 and a `Why()` that names the gate. Watch the copy: configure, then register.

**The analyst.** You declare things, relations and a goal as a wanted state of the graph, and the gap is measured. Your truths and durations are narrated and not yet judged.

**The designer.** A world declares screens as intents, a refinement as a bounded knob, and where it appears. The shells generated today are stubs, and the persona a world serves is not a field.

**The decision-maker.** You declare who may cross where and at what risk, in three gates, and every cleared crossing leaves a decision with the actor, the authority and the risk of its moment. Your architect's file is text you own.

**The educator.** The record is thin. The education plan lists a ladder from practitioner to architect to contributor among five competing level schemes, and I say so. The exercise below is judged by running.

**The agent.** A world can be wrapped as an agent that the host ticks. A deploy by a language-model actor is refused, and nothing is deployed. The crossing between worlds is governed by the calling world's name and authority.

## 9. Exercise

Declare two worlds for a place you know: a shop and its supplier, a class and its library, a clinic and its pharmacy. Give each a thing. Join them with one bond for one act. Before you run anything, write what you expect `CallAcross` to return, and which reason you expect to read first.

```haro exercise
? YourConstellation.CallAcross("a", "b", "act")
#--> 1
```

> run: exercise

Then ask for the call, read the reason, and repair the declaration, not the court, one gate at a time, until it returns 1. Count the refusals. Which gate would you have forgotten without the court? The court tells you which gate refuses: a missing risk tier, a missing permission, an authority that does not cover the risk. It does not write the declaration. A harder one: retire the second world and predict the new reason before asking; then register a copy of the first, change your original, and predict what the constellation sees.

The next chapter is about how a declared solution reaches reality, through exactly one door: rehearse on what touches nothing, commit through a governed actor, and let production refuse anything that is fake. Rehearse, then commit.
