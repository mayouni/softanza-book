# The platform in one picture

Source: Chapter 4. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the engine and its libraries; the base layer; worlds, constellations and platforms with their guards; the engine subset a part ships; designed: the max layer loaded by its entry file; the base layer inheriting the core one; a loader for one domain of base alone; a court that checks the layers against their contract; absent: a whole program and its engine packed into one file; a customer platform on the engine

Run: 8 of 8 blocks kept their promise, on 2026-10-09 02:55 UTC+01:00.

## 1. The concept, as the field holds it

The field draws a platform as a stack of boxes. The kernel at the bottom, a runtime and its libraries in the middle, applications on top, and sometimes a column at the side for security or tools. Inside one codebase the same picture becomes a rule about dependencies: an inner layer knows nothing of the outer ones, and the arrows only point inward. Rust's three standard crates, one for bare metal, one for memory, one for a full operating system, are the cleanest version I know: three depths of the same language, chosen by the target and not by a flag.

For applications, the field's picture is a host. A large application embeds a runtime and runs small applications inside it, which share its services and its store. In both pictures the judge is outside: a test suite beside the code, a review beside the store. Neither draws the court as a column standing at every floor.

## 2. The first principle

The stack of the platform is summed up, in the vision I ratified, in one idea at every altitude: **nothing is believed, everything is judged.**

## 3. The Softanza form

Here is the whole platform in one picture, read from the bottom up. Each floor stands on the one beneath it, and each floor is judged by a court beside it. The numbers in it are not typed by me: the build reads them, the night this page is made, from the library and from the site's map of its areas.

{{fig:platform-one-picture|The platform in one picture. Each floor stands on the one beneath it; each is judged by the court beside it; the architect works across all of them. The numbers are read at build from the library's engine, its test tree and the site's Atlas.}}

Let me walk it, floor by floor, with one block at each floor that you can run.

**The engine.** At the bottom is an engine written in Zig: a set of libraries behind a C interface, one per domain, grouped by the layer that loads them. The engine does the computation; the library above it gives it a vocabulary. A small example makes the division visible. The language beneath Softanza, asked for the length of the Arabic word for peace, counts bytes; the engine counts letters, and knows the script:

```haro
? len("سلام")
#--> 8
? Q("سلام").NumberOfChars()
#--> 4
? Q("مرحبا بالعالم").Script()
#--> arabic
```

> run: kept

The engine also has its own door, beneath every class. Numbers too large for the machine's arithmetic are added exactly, by the engine itself:

```haro
a = StzEngineBigIntFromString("99999999999999999999999999999999")
? StzEngineBigIntToString( StzEngineBigIntAdd(a, StzEngineBigIntFromString("1")) )
#--> 100000000000000000000000000000000
```

> run: kept

**The layers.** Above the engine, the library is cut in three layers, by depth of capability. Core, with the prefix `stk`, is lean and talks to the engine directly, for small devices and small binaries. Base, `stz`, is the rich layer, where the vocabulary and its forms live, enough for most solutions. Max, `stx`, is meant for the strongest innovations. A layer is chosen by the file a program loads, and the same verb means the same act at each depth:

```haro
o1 = new stkList([ "one", "and", "one", "makes", "two", "ones" ])
? o1.FindFirst("one")
#--> 1
o2 = new stzList([ "one", "and", "one", "makes", "two", "ones" ])
? o2.FindFirst("one")
#--> 1
```

> run: kept

**The areas.** Across the layers, the library is mapped by the site's Atlas into areas grouped in bands, and each area into lanes, each lane rated from emerging to strong with the line that proves it. The Atlas is the platform's anatomy: what exists, and how well. One rule holds across all of it: a verb means the same act on every structure that admits it. On a string it answers character positions; on a list, item positions:

```haro
? @@( Q("tea rice tea").FindAll("tea") )
#--> [ 1, 10 ]
? @@( Q([ "tea", "rice", "tea" ]).FindAll("tea") )
#--> [ 1, 3 ]
```

> run: kept

**The worlds.** Above the library, the unit is not a module but a world: an application is a living world of meaning, with its things, its relations and its rules. A world is declared, and it can explain itself:

```haro
oApp = new stzApp("FieldVisits")
oApp {
    AddThingQ(:Account) { Has([ :number, :chapter, :balance ])  IsTrue(:balance, "@ >= 0") }
    AddThingQ(:Client)  { Has([ :code, :name, :city ])  Owns(:Account) }
    AddRelation(:Account, :belongsTo, :Client)
}
oApp.Explain()
#--> WORLD FieldVisits   lives in: memory (not persisted)
#      BEING
#        account (number, chapter, balance)
#            true when balance @ >= 0
#        client (code, name, city)
#      RELATIONS
#        client owns account
#        account belongsto client
oApp.Live()
#--> [FieldVisits] is live -- 2 thing(s), 0 flow(s), 0 reaction(s), 0 goal(s); 0 proposal(s)
```

> run: kept

Worlds compose into a constellation. Here a restaurant and its produce supplier are two worlds; a bond between them declares the one crossing that is allowed, and every other crossing is refused with its reason:

```haro
oResto = StzAppQ("resto")
oResto.AddThingQ(:dish) { Has([ :name, :price ]) }
oSupplier = StzAppQ("supplier")
oSupplier.AddThingQ(:crate) { Has([ :produce, :qty ]) }
oCon = new stzSuperApp("acme-group")
oCon.AddWorld("resto", oResto)
oCon.AddWorld("supplier", oSupplier)
oCon.Bond("resto", "supplier", "order-produce")
oCon.GovDeclareRisk("order-produce", 2)
oCon.GovGrant("resto", "order-produce")
oCon.GovSetAuthority("resto", :Delegated)
? oCon.CallAcross("resto", "supplier", "order-produce")
#--> 1
? oCon.CallAcross("resto", "supplier", "raid-kitchen")
#--> 0
? oCon.Why()
#--> no bond declares 'raid-kitchen' from 'resto' to 'supplier'.
```

> run: kept

And a platform is the envelope around a solution: its parts, the systems they run on, and the order in which it is built, rehearsed and deployed. You will see it refuse to deploy before it is built in chapter 33. Here is what it does with the layers: a part of a solution ships only the engine groups it needs, and only those that are Softanza's own:

```haro
oDelivery = new stzDelivery("my-shop")
oDelivery.AddSuperApp(:phone, :Android)
oDelivery.AddBackend(:api, :LinuxServer)
oDelivery.NeedsIn(:phone, [ :Unicode, :PivotTable, :ConstraintSolver, :Regex ])
oPlan = oDelivery.Plan()
? @@( oPlan.EngineCapsFor(:phone) )
#--> [ "pivottable", "constraintsolver" ]
? @@( StzWasmGroupsFor( oPlan.EngineCapsFor(:phone) ) )
#--> [ "aggregation", "solver" ]
```

> run: kept

The phone asked for four capabilities and ships two engine groups, because the phone's own system already handles the other two.

**The crafters.** At the top are the six doors of chapter 2: the programmer, the analyst, the designer, the decision-maker, the educator and the agent. And one person works across every floor, from the machine to the organisation: the platform architect. The record names that person in three unrelated places, and no other role crosses every band of the Atlas.

**The court.** Beside every floor stands its judge. The engine has its tests and the contracts between the floors. The layers have the narrated guards. The areas have a proof line for every lane. The worlds have their bonds and norms, the order of build and deploy, and the refusal of a fake in production. The crafters' interfaces have a constitution of verbs and rules that every element must trace to. And above all of it, the platform's threat model lists its guarantees, each tied to the guard that proves it, and its own guard fails when a row names a guard that no longer exists.

Parts II to IV of this book are rethinks, and each of them is a box of this picture. Part V assembles the picture in use.

## 4. The decision, and what I refused

**I refused computation in the faces.** The engine is the product. The language above it adds beauty, not computation: thousands of methods that read like sentences, and the algorithms beneath them in one place. Every feature is implemented once, in the engine.

**I removed the old framework, with no fallback.** For years the library sat on a large C++ framework for its text, its dates and its files. When the engine replaced it, every path through the framework was removed: no fallback, no feature flag kept in case.

**I chose sovereignty as a verdict on each dependency, not as "every line ours".** The engine vendors and pins a set of third-party libraries, the figure counts them, and each one is a decision. The record defines the word in one line: nothing anyone else can withdraw. That is the test. A library whose source is pinned in the tree passes it; a binary blob that cannot be pinned does not, and was not taken.

**I refused a flag to choose a layer.** The first way of choosing a layer was a flag. It could never work, because the language beneath loads every file it sees at compile time, so all three layers loaded on every call and the failure of one was the failure of all. The flag was removed rather than kept as a switch that silently does nothing, and the reason was written where the next reader would stand: a layer is chosen by the file you load.

**I let everything go into base, and I say so.** Under the pressure of time, the domains landed in base while the engine, the planes and the customers moved forward. That was the agile choice, and it is defensible only while the debt is visible. So the figure draws base widest, and chapter 27 tells the debt with its numbers.

**I refused mini-applications.** The field's super-app is a host that runs small applications. Softanza's is a governed graph of worlds: worlds, not mini-apps; bonds and norms, not a container.

## 5. The court

`00_stzapp_narrated` proves a world declared and made visible. `06_stzsuperapp_narrated` proves the constellation: worlds joining, the commons as world zero, crossings gated by norms with the bond named as the reason, a retired world breaking its bonds. `full_scope_model_narrated`, the architect's common ground, proves the solution modelled first, the scopes that refuse what a target forbids, and the order of build and deploy. `01_platform_narrated` proves the platform's duties. `threat_model_narrated` reads the platform's threat model and fails when a guarantee names a guard that no longer exists.

## 6. The field, and where it leads

Rust's three depths are enforced by its compiler and used every day on bare metal. Softanza's rule is held at the engine and at the entry files, and broken at the inheritance, as section 7 shows.

The field's text libraries lead on locale: Softanza's own map says that the clear gap of its strings is the international components' locale layer, and that its locale area is a deliberate bet against those components, with no collation, no plural rules and no time zones.

The field's super-app hosts run real users at a scale this platform has never met. The record names them as the model it refused and measures nothing against them, so I will not either.

And the Atlas itself prints where Softanza is weak: the binary area is a plan with no shipped code, extensibility is mostly planned, the system area has few strong lanes. A map that prints its weak areas is the only kind worth reading.

## 7. The limit

What is built: the engine and its libraries, the base layer, worlds, constellations and platforms with their guards, and the engine subset a part ships.

What is designed, or built and not reachable. The max layer's own classes are written and loaded by no entry file:

```haro
try
	o3 = new stxString("one and one")
catch
	? cCatchError
done
#--> Error (R11) : Error in class name, class not found: stxstring
```

> run: kept

The base layer does not inherit the core one, as the layer contract says it should; the two share the engine and implement their common domains twice. A loader that brings one domain of base without the others is not built. A court that reads the layer contract against the tree and fails on drift is a specification. [AUTHOR: Is the base-inherits-core rule to be realised, or the contract amended to "two implementations sharing one engine"?]

What is absent: a whole program and its engine packed into one file with no dependency, and a customer platform running on the engine.

## 8. Six doors

**The programmer.** You choose your depth by the file you load, and one verb means the same act on a string and on a list.

**The analyst.** The Atlas tells you, lane by lane, where the platform is strong and where it is emerging. Build on the strong lanes.

**The designer.** Your interface has a court of its own, the constitution's verbs and rules, in the same column as the code's guards.

**The decision-maker.** Ask two questions of every floor: what stands beneath it, and who judges it. The engine's answer to the first is a written list of pinned libraries, each a verdict.

**The educator.** The picture is the book's map. Each rethink in Parts II to IV is one box of it.

**The agent.** The picture exists as data you can read, the Atlas as a file, and every floor you write to has a court that will read you.

## 9. Exercise

Draw your own solution the way this chapter draws Softanza: floors, and a court beside each. For each box, write the file that declares it and the guard that judges it, and put a stage word on it: built, designed or absent.

Then declare two parts of it with `stzPlatformProfile`, and before you run anything, write the line you expect when you ask it to deploy before you build it. Run it. A box with no court beside it is your first finding.
