# The platform in one picture

Source: Chapter 4. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the engine and its libraries; the base layer; worlds, constellations and platforms with their guards; the engine subset a part ships, for the web; designed: the max layer loaded by its entry file; the base layer building on the core one; a loader for one domain of base alone; a court that checks the layers against their contract; absent: a whole program and its engine packed into one file; a customer platform on the engine

Run: 8 of 8 blocks kept their promise, on 2026-10-14 01:34 UTC+01:00.

In this chapter I draw the whole platform in one picture, read from the bottom up: the engine, the layers, the areas, the worlds, the crafters, and beside every floor its court. I walk it floor by floor, with one block at each floor that you can run. Then I say what I refused along the way: computation in the faces, a flag to choose a layer, mini-applications. The picture is summed up in one idea at every altitude: nothing is believed, everything is judged.

## 1. The concept, as the field holds it

The field draws a platform as a stack of boxes. The kernel at the bottom, a runtime and its libraries in the middle, applications on top, and sometimes a column at the side for security or tools. Inside one codebase the same picture becomes a rule about dependencies: an inner layer knows nothing of the outer ones, and the arrows only point inward. Rust's three standard crates, one for bare metal, one for memory, one for a full operating system, are the cleanest version I know. Three depths of the same language, chosen by what the target offers.

For applications, the field's picture is a host. A large application embeds a runtime and runs small applications inside it, which share its services and its store. In both pictures the judge is outside: a test suite beside the code, a review beside the store. In the pictures I know, neither draws the court as a column standing at every floor.

Softanza draws that column, and one idea holds the whole picture.

## 2. The first principle

The stack of the platform is summed up, in the vision I ratified, in one idea at every altitude: **nothing is believed, everything is judged.**

## 3. The Softanza form

Here is the whole platform in one picture, read from the bottom up. Each floor stands on the one beneath it, and each floor is judged by a court beside it. The numbers in it are not typed by me. The build reads them, when this page is made, from the library and from the site's map of its areas.

{{fig:platform-one-picture|The platform in one picture. Each floor stands on the one beneath it; each is judged by the court beside it; the architect works across all of them. The numbers are read at build from the library's engine, its test tree and the site's Atlas.}}

Let me walk it, floor by floor, with one block at each floor that you can run.

**The engine.** At the bottom is an engine written in Zig: a set of libraries behind a C interface, one per domain, grouped by the layer that loads them. By the engine's design rule, the engine does the computation; the library above it gives it a vocabulary. A small example makes the division visible. Ask the language beneath Softanza for the length of the Arabic word for peace, then ask the engine. What does each one count? Run it:

```haro
? len("سلام")
#--> 8
? Q("سلام").NumberOfChars()
#--> 4
? Q("مرحبا بالعالم").Script()
#--> arabic
```

> run: kept

The language counts bytes and answers `8`. The engine counts letters and answers `4`, and it knows the script: `arabic`. Four letters, not eight!

The engine also has its own door, beneath every class. Numbers too large for the machine's arithmetic are added exactly, by the engine itself:

```haro
a = StzEngineBigIntFromString("99999999999999999999999999999999")
? StzEngineBigIntToString( StzEngineBigIntAdd(a, StzEngineBigIntFromString("1")) )
#--> 100000000000000000000000000000000
```

> run: kept

The engine answers `100000000000000000000000000000000`, the exact sum.

**The layers.** Above the engine, the library is cut in three layers, by depth of capability. Core, with the prefix `stk`, is lean and talks to the engine directly, for small devices and small binaries. Base, `stz`, is the rich layer, where the vocabulary and its forms live, enough for most solutions. Max, `stx`, is meant for the strongest innovations. A layer is chosen by the file a program loads. Does the same verb mean the same act at core and base? Run it:

```haro
o1 = new stkList([ "one", "and", "one", "makes", "two", "ones" ])
? o1.FindFirst("one")
#--> 1
o2 = new stzList([ "one", "and", "one", "makes", "two", "ones" ])
? o2.FindFirst("one")
#--> 1
```

> run: kept

Both answer `1`: the same verb, the same act, at two depths.

**The areas.** Across the layers, the library is mapped by the site's Atlas into areas grouped in bands, and each area into lanes. Each lane is rated from emerging to strong, most of them with the line that proves it. The Atlas says what exists, and how well. The engine's design rule is that a verb means the same act on every structure that admits it. Does it hold for one pair, a string and a list? Run it:

```haro
? @@( Q("tea rice tea").FindAll("tea") )
#--> [ 1, 10 ]
? @@( Q([ "tea", "rice", "tea" ]).FindAll("tea") )
#--> [ 1, 3 ]
```

> run: kept

On the string, `FindAll` answers character positions: `[ 1, 10 ]`. On the list, it answers item positions: `[ 1, 3 ]`. The same act, on two structures.

**The worlds.** Above the library, the unit is not a module but a world: an application is a living world of meaning, with its things, its relations and its rules. A world is declared. What does it say of itself when you ask it to explain? Run it:

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

It answers `WORLD FieldVisits   lives in: memory (not persisted)`, then lists its being and its relations. `Live()` answers `[FieldVisits] is live -- 2 thing(s), 0 flow(s), 0 reaction(s), 0 goal(s); 0 proposal(s)`. Two things, and no flow, no reaction, no goal. The world says what was declared, and no more.

Worlds compose into a constellation. Here a restaurant and its produce supplier are two worlds, and a bond between them declares the one crossing that is allowed. What becomes of a crossing that no bond declares? Run it:

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

The declared crossing answers `1`. The other answers `0`, refused! The constellation gives its reason in one line: `no bond declares 'raid-kitchen' from 'resto' to 'supplier'.` Every other crossing is refused with its reason.

The commons is the shared ground of a constellation, what every world of it stands on. It holds an identity, a session and a store. It is a world like the others, world zero, and not a node of a special kind. Chapter 23 shows it and says where the code falls short of that.

And a platform is the envelope around a solution: its parts, the systems they run on, and the order in which it is built, rehearsed and deployed. You will see it refuse to deploy before it is built in chapter 33. Here is what it does with the layers, for the web: a part of a solution ships only the engine groups it needs, and only those that are Softanza's own. The phone below asks for four capabilities. How many engine groups does it ship? Run it:

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

Two, not four: `aggregation` and `solver`! The phone's own system handles one of the other two, Unicode, and Softanza ships the other, Regex, as a construct in the target's own language.

**The crafters.** At the top are the six doors of chapter 2: the programmer, the analyst, the designer, the decision-maker, the educator and the agent. And one person works across every floor, from the engine to the organisation: the platform architect. The record names that person in three unrelated places, and no other role crosses every band of the Atlas.

**The court.** Beside every floor stands its judge. The engine has its tests and the contracts between the floors. The layers have the narrated guards. Most lanes in the areas carry a proof line. The worlds have their bonds and norms, the order of build and deploy, and the refusal of a fake in production. The crafters' interfaces have a constitution of verbs and rules that every element must trace to. And above all of it, the platform's threat model lists its guarantees, each tied to the guard that proves it. Its own guard fails when a row names a guard that no longer exists.

Parts II to IV of this book are rethinks, and each of them is a box of this picture. Part V assembles the picture in use.

## 4. The decision, and what I refused

**I refused computation in the faces.** The engine is the product. The language above it adds beauty, not computation: thousands of methods that read like sentences, and the algorithms beneath them in one place. The rule is that every feature is implemented once, in the engine. The migration is not finished. The layer contract lists number, list, object, graph, stats and natural as still in Ring.

**I removed the old framework, with no fallback.** The library sat on a large C++ framework for its text, its dates and its files. When the engine replaced it, every path through the framework was removed: no fallback, no feature flag kept in case.

**I chose sovereignty as a verdict on each dependency, not as "every line ours".** The engine vendors and pins a set of third-party libraries, the figure counts them. The record defines the word in one line: nothing anyone else can withdraw. That is the test. A library whose source is pinned in the tree passes it.

**I refused a flag to choose a layer.** The first way of choosing a layer was a flag. It could never work, because the language beneath loads every file it sees at compile time, so all three layers loaded on every call. The failure of one was the failure of all. The flag was removed rather than kept as a switch that silently does nothing. The reason was written where the next reader would stand: a layer is chosen by the file you load.

**I let everything go into base, and I say so.** Under the pressure of time, the domains landed in base. The engine, the planes such as security and performance, and the customers moved forward meanwhile. That was the agile choice, and it is defensible only while the debt is visible. So the figure draws base widest, and chapter 27 tells the debt with its numbers.

**I refused mini-applications.** The field's super-app is a host that runs small applications. Softanza's is a governed graph of worlds: worlds, not mini-apps; bonds and norms, not a container.

Five guards stand beside the floors; the next section names what each proves.

## 5. The court

`00_stzapp_narrated` proves a world declared and made visible. `06_stzsuperapp_narrated` proves the constellation: worlds joining, the commons as world zero, crossings gated by norms with the bond named as the reason, a retired world breaking its bonds. `full_scope_model_narrated`, the architect's common ground, proves the solution modelled first, the scopes that refuse what a target forbids, and the order of build and deploy. `01_platform_narrated` proves the platform's duties. `threat_model_narrated` reads the platform's threat model and fails when a guarantee names a guard that no longer exists.

## 6. The field, and where it leads

Rust's three depths are enforced by its compiler and used every day on bare metal. Softanza's rule is held at the engine and at the entry files, and broken where base should build on core, as section 7 shows.

The field's text libraries lead on locale: Softanza's own map says that the clear gap of its strings is the international components' locale layer. Its locale area is a deliberate bet against those components: no collation, no plural rules and no time zones.

The field's super-app hosts run real users at a scale this platform has never met. The record names them as the model it refused and measures nothing against them, so I will not either.

And the Atlas itself prints where Softanza is weak. The binary area is a plan with no shipped code, the plugin, foreign-function and embed plane of extensibility is mostly planned, the system area has few strong lanes. I hold this as a view, not a result. A map that prints its weak areas is the only kind worth reading.

## 7. The limit

Now I put the three stage words on the picture, built, designed and absent.

What is built: the engine and its libraries, the base layer, worlds, constellations and platforms with their guards, and, for the web, the engine subset a part ships.

What is designed, or built and not reachable. The max layer's own classes are written and loaded by no entry file. What does the runtime answer when you ask for one? Run it:

```haro
try
	o3 = new stxString("one and one")
catch
	? cCatchError
done
#--> Error (R11) : Error in class name, class not found: stxstring
```

> run: kept

The runtime answers: `Error in class name, class not found: stxstring`. The class is written, and no entry file loads it!

The layer contract says the base layer builds on core, by inheritance or delegation. It does neither for the common domains: the two share the engine and implement those domains twice. The core layer itself is broken against the engine today. Its string and character classes call engine names that no engine file registers, as the site study of the book's roots reports. The block in section 3 shows lists only. A loader that brings one domain of base without the others is not built. A court that reads the layer contract against the tree and fails on drift is a specification, proposed in that site study. What is built is two implementations sharing one engine; the contract's line that base builds on core is designed.

What is absent: a whole program and its engine packed into one file with no dependency, and a customer platform running on the engine.

## 8. Six doors

Each of the six doors reads this picture from where it stands.

**The programmer.** You choose your depth by the file you load, and one verb means the same act on a string and on a list.

**The analyst.** The Atlas tells you, lane by lane, where the platform is strong and where it is emerging. Build on the strong lanes.

**The designer.** Your interface has a court of its own, the constitution's verbs and rules, in the same column as the code's guards.

**The decision-maker.** Ask two questions of every floor: what stands beneath it, and who judges it. The engine's answer to the first is a written list of pinned libraries.

**The educator.** The picture is the book's map. Each rethink in Parts II to IV is one box of it.

**The agent.** The picture exists as data you can read, the Atlas as a file, and every floor you write to has a court that will read you.

## 9. Exercise

Draw your own solution the way this chapter draws Softanza: floors, and a court beside each. For each box, write the file that declares it and the guard that judges it, and put a stage word on it: built, designed or absent.

Then declare two parts of it with `stzPlatformProfile`, and before you run anything, write the line you expect when you ask it to deploy before you build it. Run it. A box with no court beside it is your first finding.

I left this one in your hands. Section 7 says the core layer's string classes are broken against the engine, and the block of section 3 shows you lists only. Take the block of section 7 and change one word: `stxString` becomes `stkString`.

```haro exercise
try
	o3 = new stkString("one and one")
catch
	? cCatchError
done
```

> run: exercise

Run it, and read what the runtime answers. Then go back to section 7 and find which name is called, and who should have registered it. When you have solved it, you will know why the layer contract's line that base builds on core is called designed, and not built.

The next chapter leaves the picture for the code written inside it, and states the first law: the code adheres to the way a person thinks, and the court judges it whoever wrote it. Its principle is one sentence: what you think is what you write.
