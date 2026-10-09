# Programming becomes refinement

Source: Chapter 10. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the refinement point declared in the source; the gate with five checks; the cascade of a point and of a class; reversal by step, by checkpoint and to zero; the trust floor and governed refining; designed: the experience the article describes: asking a point to explain itself, applying a plan, a one-line refinement; the cascade of the code graph joined to the gate; the refinement seat of Haro; absent: a saved history: the file keeps the source and nothing of the timeline

Run: 9 of 9 blocks kept their promise, on 2026-10-09 13:45 UTC+01:00.

## 1. The concept, as the field holds it

The field has a name for changing infrastructure with a rehearsal: plan, then apply. A tool computes what would change, shows it, and applies it only when you say so; Terraform made the pattern familiar, and the field's admission controllers apply the same idea to a request before a cluster accepts it. More recently, the field has a name for a way of working with code-writing agents: specifications first, and the agent fills in. (General knowledge, not a study of the record.)

What these share is where they stand. The plan and the admission control are about infrastructure and requests. For the code itself, much of the field's answer to a change is still a diff, a patch of text, and a person's review of it. (General knowledge, not a study of the record.) That worked while every change had a person behind it who could be asked. It is a weak instrument when most changes arrive from agents, in volume.

## 2. The first principle

I wrote the sentence on the back cover of my first book, and I have not found a better one: **stop trying to govern the intelligence, and govern the change.** The library's header says the same thing in the form of a type: a change is a typed proposal, not a diff.

## 3. The Softanza form

The practice has changed names in my life. I used to say I programmed. I now say that, more and more, I refine, and I mean something exact by it. A refinement is a change to code that was declared to be changeable, proposed in a typed form, judged by a gate, recorded as a step, and reversible. The first book of this imprint, *Refinement-Oriented Programming*, tells the discipline through the story of a bank facing a regulator's letter. This chapter tells what the library carries of it.

It begins by declaring where the code may change. A refinement point is a named knob written in the source as a tag, with its kind, its value and its bounds:

```haro
cSrc = 'vat_rate = <R:PARAM name="vat" value="0.20" min="0" max="0.25">' + nl +
       'sort_by  = <R:ALGO name="sort" value="quick" options="quick|merge|heap">'
o = new stzRefinableCode(cSrc)
? o.NumberOfPoints()
#--> 2
? @@( o.RefinementPoints() )
#--> [ [ "vat", "param", "0.20" ], [ "sort", "algo", "quick" ] ]
? o.KindOf("vat")
#--> param
```

> run: kept

A change is then a proposal. It names a point and a value; if it clears the gate it takes effect and is recorded as one step:

```haro
r = o.Refine("vat").To("0.22")
? r[:admitted]
#--> 1
? o.ValueOf("vat")
#--> 0.22
? o.NumberOfSteps()
#--> 1
```

> run: kept

And a proposal that does not clear the gate changes nothing, and says at which stage it was refused and why:

```haro
r2 = o.Refine("vat").To("0.99")
? r2[:admitted]
#--> 0
? r2[:why]
#--> constraint: 0.99 above max 0.25
? o.ValueOf("vat")
#--> 0.22
? o.Refine("sort").To("bubble")[:why]
#--> constraint: 'bubble' not in options quick|merge|heap
? o.Refine("ghost").To("1")[:why]
#--> structural: no refinement point 'ghost'
? o.NumberOfSteps()
#--> 1
```

> run: kept

Three refusals, and the timeline did not grow by a step. The library's comment calls this its third law: a rejected proposal never ends changed. Each refusal names its stage, so that a person, or an agent, can correct the proposal without reading a diff.

**The cascade** is what you read instead of the diff. Before the change, ask what it reaches. There are two cascades, and they are separate. For a point, it is the line it sits on and the other points on that same line:

```haro
cPrice = 'price = <R:PARAM name="vat" value="0.20" min="0" max="0.30"> * <R:PARAM name="margin" value="1.1" min="1" max="2">' + nl +
         'floor = <R:PARAM name="floor" value="0.10" min="0" max="0.30">'
oc = new stzRefinableCode(cPrice)
aC = oc.Cascade("vat")
? aC[:lines][1]
#--> 1
? @@( aC[:alsoTouches] )
#--> [ "margin" ]
? oc.Cascade("floor")[:lines][1]
#--> 2
? len(oc.Cascade("floor")[:alsoTouches])
#--> 0
```

> run: kept

For a class, the cascade is a property of the structure of the code: who descends from it and who inherits a method. The library computes it from the code graph, and it can scan a text without touching a file:

```haro
cCls = 'class Tariff' + nl +
       '	def Rate()' + nl +
       '		return 0.20' + nl +
       'class Invoice from Tariff' + nl +
       '	def Total()' + nl +
       '		return 1' + nl +
       'class Receipt from Invoice' + nl +
       '	def Print()' + nl +
       '		return 1' + nl +
       'class Quote from Tariff' + nl +
       '	def Rate()' + nl +
       '		return 0.18' + nl
g0 = new stzRingCodeGraph("")
g0.ScanSource(cCls, "world.ring")
g0.BuildGraph()
? @@( g0.Cascade("Tariff")[:descendants] )
#--> [ "Invoice", "Quote", "Receipt" ]
? g0.Cascade("Tariff")[:blastRadius]
#--> 3
? @@( g0.ImpactOf("Rate")[:inheritedBy] )
#--> [ "Invoice", "Receipt" ]
```

> run: kept

Change the rate of the tariff and three classes are in the blast radius; but two of them inherit the method and the third redefines it, so it owns the method and does not merely inherit it. That is the difference `ImpactOf` draws.

Inside the gate, a change reaches its dependents by a rule that spans several points, judged on the state the change would produce. If the rule fails, the value is put back:

```haro
d = new stzRefinableCode(cPrice)
d.DeclareDerivation("vat-above-floor",
	func oCode { return ring_number(oCode.ValueOf("vat")) >= ring_number(oCode.ValueOf("floor")) },
	"vat must not drop below floor")
? d.Refine("vat").To("0.30")[:admitted]
#--> 1
r3 = d.Refine("vat").To("0.05")
? r3[:admitted]
#--> 0
? r3[:why]
#--> derivation: rule 'vat-above-floor' violated -- vat must not drop below floor
? d.ValueOf("vat")
#--> 0.30
```

> run: kept

Now the question of this age: who proposed it? Every proposal carries its origin, and a point can set a floor of trust that refuses a lower origin, without refusing a person. A proposal that comes from a language model is below a floor that a trusted one clears:

```haro
d.TrustFloor("vat", :trusted)
r4 = d.Refine("vat").As(:llm).To("0.25")
? r4[:admitted]
#--> 0
? r4[:why]
#--> trust: posture :llm below the required floor for 'vat'
? d.ValueOf("vat")
#--> 0.30
? d.Refine("vat").As(:trusted).To("0.25")[:admitted]
#--> 1
? d.PostureOf(d.NumberOfSteps())
#--> trusted
```

> run: kept

And who may turn which knob is declared, too: a permission, and an authority level against a risk tier. A delegated actor cannot turn a knob of the third tier. Escalated, it can, and the decision is recorded:

```haro
gv = new stzRefinableCode(cPrice)
gv.SetGovernedBy(new stzGovernance("release-ops")).SetActor("release-bot")
gv.SetRiskFor("vat", 3).SetAllowRefine("vat").SetAuthorityLevel(:Delegated)
r5 = gv.Refine("vat").To("0.22")
? r5[:admitted]
#--> 0
? r5[:why]
#--> governance: refused: 'release-bot' holds 'delegated' authority (level 2) but 'refine-vat' is risk tier 3 (SHOULD does not cover it)
? gv.ValueOf("vat")
#--> 0.20
gv.SetAuthorityLevel(:Autonomous)
? gv.Refine("vat").To("0.22")[:admitted]
#--> 1
? gv.GovernanceQ().NumberOfDecisions()
#--> 1
```

> run: kept

Last, reversibility is part of the data model. Every admitted step keeps its prior value, so a person can step back one, rewind to a named checkpoint, rewind to zero, and go forward again:

```haro
t = new stzRefinableCode(cPrice)
t.Refine("vat").To("0.21")
t.Refine("vat").To("0.22")
t.Checkpoint("reviewed")
t.Refine("vat").To("0.28")
? t.ValueOf("vat")
#--> 0.28
t.RevertToCheckpoint("reviewed")
? t.ValueOf("vat")
#--> 0.22
? t.NumberOfSteps()
#--> 2
t.RevertTo(0)
? t.ValueOf("vat")
#--> 0.20
? t.CanRevert()
#--> 0
t.Redo()
? t.ValueOf("vat")
#--> 0.21
```

> run: kept

That is the gate in the form the library has it. Five checks, in the order the code runs them: the structure of the proposal, then the constraints of the point, then the governance, then the trust of the origin, and last the derivation across points. The header of the file calls this a four-stage gate in one line and five in another; the code numbers its checks 1, 2, 3, 4 and 4b, because the trust check was added to the four on 16 July 2026 and the design's count was not changed. I report what runs: five checks.

## 4. The decision, and what I refused

**I refused to govern the intelligence.** Much of the field's approach to agents is to make the model safer: alignment, guardrails, a prompt that asks for confirmation. (General knowledge, as above.) I refused that frame. A model's output is whatever it is, from whichever model, and the intelligence of the next generation will not hold still for me to govern it. The change is the thing that stays, and it is the thing that reaches the world. So the gate stands where the change arrives, and it asks one thing: what is proposed, from where, and does the code say this point may change that way.

**I refused the diff as the unit.** A diff is a text change. A refinement is a typed proposal about a declared point, with a kind, bounds and an origin. I kept the diff as an artefact, and I refused it as the thing to review.

**I made the library carry the verb, and left the environment elsewhere.** The refinement as a library verb, the point, the gate, the cascade and the reversal, belongs to the open foundation. The environment in which a team lives with it day to day, the screens, the live mode, the book, is a product, and does not leak into the library.

**I printed the gate as it is.** I wrote the design with four stages, and the code has five checks. A page that quotes my design and not my code would be wrong, and it is the code that runs.

## 5. The court

`refinablecode_narrated` proves the point declared, the proposal that passes, the two refusals that leave the source whole (bounds and options), the cascade, the reversal, and the saved file. `refine_deepening_narrated` proves the timeline with its checkpoints and its redo, and the trust floor. `gate_deepening_narrated` proves the refusal of an unknown point, the derivation across points with its rollback, and the governed refusal with its lineage.

## 6. The field, and where it leads

The field leads in infrastructure, where plan and apply are the daily practice of many teams and the apply talks to real providers. (General knowledge, as in section 1.) Softanza's gate is about the change to code, which the field handles with a review.

The field's tools lead in breadth: they are not tied to one library, one language, or one declared knob. (General knowledge, as in section 1.) Softanza's gate judges only what the code declared as a point. A change to a place that was never declared is not a refinement here; it is outside the gate.

And on trust, much of the field's approach is built to scale to any model. (General knowledge, as in section 1.) Mine rests on one declaration per point.

## 7. The limit

What is built: the refinement point, the gate with its five checks, the cascade of a point and of a class, the reversal, the trust floor, and governed refining; the guards of section 5 cover them, with two exceptions. The cascade of a class has no guard here, because the code-graph guard scans a live path of the library's working tree. And no guard asserts the other points on a line.

What is designed, and absent from the library by name: the experience the original article describes. The class that article names, `stzPolyCode`, is not in the library at this commit. The one-line refinement of the design document, a point that explains itself, a plan that is applied, are not in the library. The cascade of the code graph and the cascade of the gate are not joined. And Haro has a gate in a spike written only in the former host language, with its own seat for refinement not built.

What is built, and where it stops: the limits of the gate as it stands.

- It checks the constraints of three kinds of point, a parameter, an algorithm and a library; a point of another kind, a block of code for instance, parses and passes unchecked.
- An unknown trust posture ranks as trusted: the code gives it the top rank. So a proposal that says it comes from a martian clears a floor of trusted.
- A derivation is applied tentatively and restored on failure. So I say "never ends changed", not "never touched".
- The saved file holds the rendered source and nothing else: no history, no postures, no timeline, and no way to load it back. Reversibility does not survive the file. The library writes this file in the format `.zrfn`, as shipped. The Haro charter, ratified on 1 October 2026, takes `.rfn` for the sentence and leaves `.zrfn` to the library's comment-tag lift.

## 8. Six doors

**The programmer.** Declare the places that may change, and propose changes to them as typed proposals. A refusal names its stage.

**The analyst.** The rule that spans several points is yours to declare, and the gate judges it on the state the change would produce.

**The designer.** The cascade is what you read instead of the diff: for a point, which line and which points on it; for a class, which classes inherit. They are two cascades, not yet one.

**The decision-maker.** Who may turn which knob is a permission and an authority against a risk tier, and the decision is recorded with its authority at the time.

**The educator.** Step back one, rewind to a named checkpoint, rewind to zero, go forward again. A learner can try without fear because every step keeps its prior value.

**The agent.** You may propose. Your origin is on the proposal, and a point can set a floor your origin does not clear.

## 9. Exercise

Take two settings of a program of yours: a rate and a ceiling, say, with a rule that the rate must stay below the ceiling. Declare them as points, with bounds, and declare the rule across them. Before you run anything, write under each proposal whether it is admitted and, if not, at which stage it is refused. Propose a change of the rate above the ceiling, and one from an origin you declare as a model, against a floor you set. Then rewind to zero and go forward one step.

Run it. If you were wrong about the stage, you have found a place where your own gate disagrees with your own expectation.
