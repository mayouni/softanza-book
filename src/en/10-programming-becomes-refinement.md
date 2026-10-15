---
id: programming-becomes-refinement
part: 2
number: 10
title: Programming becomes refinement
spine: false
narrations: [stzpolycode-refinement-centered_programming.md]
site: [refinement]
guards: [refinablecode_narrated, refine_deepening_narrated, gate_deepening_narrated]
stage:
  built: "the refinement point declared in the source; the gate with five checks; the cascade of a point and of a class; reversal by step, by checkpoint and to zero; the trust floor and governed refining"
  designed: "the experience the article describes: asking a point to explain itself, applying a plan, a one-line refinement; the cascade of the code graph joined to the gate; the refinement seat of Haro"
  absent: "a saved history: the file keeps the source and nothing of the timeline"
status: draft
rulings: ["12.19", "12.23", "12.29"]
research: research/ch10.md
---

In this chapter I say what I mean by refining rather than programming. It is a change to code declared to be changeable, proposed in a typed form, judged by a gate, recorded as a step, and reversible. I run the library's form of it: the refinement point, the proposal, the gate, the cascade, the trust floor and the reversal. And I print the gate as it is, five checks and not the four of my design. I say where the field leads and where the gate stops. The principle is the sentence I wrote on the back cover of my earlier book, *Refinement-Oriented Programming*: stop trying to govern the intelligence, and govern the change.

## 1. The concept, as the field holds it

The field has a name for changing infrastructure with a rehearsal: plan, then apply. A tool computes what would change, shows it, and applies it only when you say so. Terraform made the pattern familiar, and the field's admission controllers apply the same idea to a request before a cluster accepts it. More recently, the field has a name for a way of working with code-writing AI agents: specifications first, and the agent fills in. All of this is general knowledge, not a study of the record.

What these share is where they stand. The plan and the admission control are about infrastructure and requests. For the code itself, much of the field's answer to a change is still a diff, a patch of text, and a person's review of it. That worked while every change had a person behind it who could be asked. It is a weak instrument when most changes arrive from agents, in volume; I hold this as a view, not a result.

Against that weak instrument I set one sentence.

## 2. The first principle

I wrote the sentence on the back cover of my earlier book, *Refinement-Oriented Programming*, and I have not found a better one: **stop trying to govern the intelligence, and govern the change.** The library's header says the same thing in the form of a type: a change is a typed proposal, not a diff.

The rest of the chapter runs that sentence.

## 3. The Softanza form

The practice has changed names in my life. I used to say I programmed. I now say that, more and more, I refine, and I mean something exact by it. A refinement is a change to code that was declared to be changeable, proposed in a typed form, judged by a gate, recorded as a step, and reversible. My earlier book, *Refinement-Oriented Programming*, tells the discipline through the story of Softibank, a bank facing a regulator's letter. This chapter tells what the library carries of it.

It begins by declaring where the code may change. A refinement point is a named knob written in the source as a tag, with its kind, its value and its bounds, and the code that holds it is questioned in its scene, the form of chapter 5:

```haro
cSrc = 'vat_rate = <R:PARAM name="vat" value="0.20" min="0" max="0.25">' + nl +
       'sort_by  = <R:ALGO name="sort" value="quick" options="quick|merge|heap">'
o = new stzRefinableCode(cSrc)
o {
	? NumberOfPoints()
	#--> 2
	? @@( RefinementPoints() )
	#--> [ [ "vat", "param", "0.20" ], [ "sort", "algo", "quick" ] ]
	? KindOf("vat")
	#--> param
}
```

A change is then a proposal. It names a point and a value; if it clears the gate it takes effect and is recorded as one step:

```haro
o {
	r = Refine("vat").To("0.22")
	? r[:admitted]
	#--> 1
	? ValueOf("vat")
	#--> 0.22
	? NumberOfSteps()
	#--> 1
}
```

The admission prints as `1` and `0`, not `TRUE` and `FALSE`: that is how this verb answers, and I print the run. And what does a proposal that does not clear the gate change, and what does the gate say? Run it:

```haro
o {
	r2 = Refine("vat").To("0.99")
	? r2[:admitted]
	#--> 0
	? r2[:why]
	#--> constraint: 0.99 above max 0.25
	? ValueOf("vat")
	#--> 0.22
	? Refine("sort").To("bubble")[:why]
	#--> constraint: 'bubble' not in options quick|merge|heap
	? Refine("ghost").To("1")[:why]
	#--> structural: no refinement point 'ghost'
	? NumberOfSteps()
	#--> 1
}
```

Three refusals, and the timeline did not grow by a step! The library's comment calls this a law of its own: a rejected proposal never ends changed. Each refusal names its stage first, `constraint` twice and `structural` once, as in `structural: no refinement point 'ghost'`, so that a person, or an agent, can correct the proposal without reading a diff.

**The cascade** is what you read instead of the diff. Before the change, ask what it reaches. There are two cascades, and they are separate. For a point, it is the line it sits on and the other points on that same line:

```haro
cPrice = 'price = <R:PARAM name="vat" value="0.20" min="0" max="0.30"> * <R:PARAM name="margin" value="1.1" min="1" max="2">' + nl +
         'floor = <R:PARAM name="floor" value="0.10" min="0" max="0.30">'
oc = new stzRefinableCode(cPrice)
oc {
	aC = Cascade("vat")
	? aC[:lines][1]
	#--> 1
	? @@( aC[:alsoTouches] )
	#--> [ "margin" ]
	? Cascade("floor")[:lines][1]
	#--> 2
	? len(Cascade("floor")[:alsoTouches])
	#--> 0
}
```

`vat` sits on line 1 and also touches `[ "margin" ]`; `floor` sits on line 2, alone.

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
g0 {
	ScanSource(cCls, "world.ring")
	BuildGraph()
	? @@( Cascade("Tariff")[:descendants] )
	#--> [ "Invoice", "Quote", "Receipt" ]
	? Cascade("Tariff")[:blastRadius]
	#--> 3
	? @@( ImpactOf("Rate")[:inheritedBy] )
	#--> [ "Invoice", "Receipt" ]
}
```

Change the rate of the tariff and three classes are in the blast radius. Two of them inherit the method, and `ImpactOf` names them: `[ "Invoice", "Receipt" ]`. The third, `Quote`, redefines it, so it owns the method and does not merely inherit it. That is the difference `ImpactOf` draws.

How does a change reach its dependents? By a rule that spans several points, judged on the state the change would produce. If the rule fails, the value is put back:

```haro
d = new stzRefinableCode(cPrice)
d {
	DeclareDerivation("vat-above-floor",
		func oCode { return ring_number(oCode.ValueOf("vat")) >= ring_number(oCode.ValueOf("floor")) },
		"vat must not drop below floor")
	? Refine("vat").To("0.30")[:admitted]
	#--> 1
	r3 = Refine("vat").To("0.05")
	? r3[:admitted]
	#--> 0
	? r3[:why]
	#--> derivation: rule 'vat-above-floor' violated -- vat must not drop below floor
	? ValueOf("vat")
	#--> 0.30
}
```

The rule refused the change and named itself: `derivation: rule 'vat-above-floor' violated -- vat must not drop below floor`. The value is still `0.30`.

And who proposed it? Every proposal carries its origin, and a point can set a floor of trust that refuses a lower origin, without refusing a person. What happens to a proposal from a language model when the floor of the point asks for a trusted origin? Run it:

```haro
d {
	TrustFloor("vat", :trusted)
	r4 = Refine("vat").As(:llm).To("0.25")
	? r4[:admitted]
	#--> 0
	? r4[:why]
	#--> trust: posture :llm below the required floor for 'vat'
	? ValueOf("vat")
	#--> 0.30
	? Refine("vat").As(:trusted).To("0.25")[:admitted]
	#--> 1
	? PostureOf(NumberOfSteps())
	#--> trusted
}
```

The model's proposal was refused: `trust: posture :llm below the required floor for 'vat'`. The point kept `0.30`! The same proposal from a trusted origin was admitted, and the step records `trusted`.

And who may turn which knob? That is declared, too: a permission, and an authority level against a risk tier. Take a delegated actor and a knob of the third tier. Run it:

```haro
gv = new stzRefinableCode(cPrice)
gv {
	SetGovernedBy(new stzGovernance("release-ops"))
	SetActor("release-bot")
	SetRiskFor("vat", 3)
	SetAllowRefine("vat")
	SetAuthorityLevel(:Delegated)
	r5 = Refine("vat").To("0.22")
	? r5[:admitted]
	#--> 0
	? r5[:why]
	#--> governance: refused: 'release-bot' holds 'delegated' authority (level 2) but 'refine-vat' is risk tier 3 (SHOULD does not cover it)
	? ValueOf("vat")
	#--> 0.20
	SetAuthorityLevel(:Autonomous)
	? Refine("vat").To("0.22")[:admitted]
	#--> 1
	? GovernanceQ().NumberOfDecisions()
	#--> 1
}
```

The delegated actor was refused, `'release-bot' holds 'delegated' authority (level 2)`, and the value stayed `0.20`. The same proposal was admitted once the actor was escalated! The decision is recorded: `NumberOfDecisions()` printed `1`.

Last, can a step be taken back? Reversibility is part of the data model: every admitted step keeps its prior value. Rewind to a named checkpoint, rewind to zero, go forward again:

```haro
t = new stzRefinableCode(cPrice)
t {
	Refine("vat").To("0.21")
	Refine("vat").To("0.22")
	Checkpoint("reviewed")
	Refine("vat").To("0.28")
	? ValueOf("vat")
	#--> 0.28
	RevertToCheckpoint("reviewed")
	? ValueOf("vat")
	#--> 0.22
	? NumberOfSteps()
	#--> 2
	RevertTo(0)
	? ValueOf("vat")
	#--> 0.20
	? CanRevert()
	#--> 0
	Redo()
	? ValueOf("vat")
	#--> 0.21
}
```

At zero, `CanRevert()` printed `0`. One `Redo()`, and the value is `0.21`, the first step again.

That is the gate in the form the library has it. Five checks, in the order the code runs them. The structure of the proposal, then the constraints of the point, then the governance, then the trust of the origin, and last the derivation across points. I ran them above in the order of the story, not of the code. The header of the file calls this a four-stage gate in one line and five in another. The code numbers its checks 1, 2, 3, 4 and 4b. The trust check was added to the four on 16 July 2026, and the design's count was not changed. I report what runs: five checks.

Behind the gate stand decisions, and what I refused.

## 4. The decision, and what I refused

**I refused to govern the intelligence.** Much of the field's approach to AI agents is to make the model safer: alignment, guardrails, a prompt that asks for confirmation; that too is general knowledge. I refused that frame. A model's output is whatever it is, from whichever model, and the intelligence of the next generation will not hold still for me to govern it. The change is the thing that stays, and it is the thing that reaches the world. So the gate stands where the change arrives, and it asks one thing: what is proposed, from where, and does the code say this point may change that way.

**I refused the diff as the unit.** A diff is a text change. A refinement is a typed proposal about a declared point, with a kind, bounds and an origin. I kept the diff as an artefact, and I refused it as the thing to review.

**I made the library carry the verb, and left the environment elsewhere.** The refinement as a library verb, the point, the gate, the cascade and the reversal, belongs to the open foundation. The environment in which a team lives with it day to day, the screens, the live mode, the book, is a product. It does not leak into the library.

**I printed the gate as it is.** I wrote the design with four stages, and the code has five checks. A page that quotes my design and not my code would be wrong, and it is the code that runs.

## 5. The court

`refinablecode_narrated` proves the point declared, the proposal that passes, the two refusals that leave the source whole (bounds and options), the cascade, the reversal, and the saved file. `refine_deepening_narrated` proves the timeline with its checkpoints and its redo, and the trust floor. `gate_deepening_narrated` proves the refusal of an unknown point, the derivation across points with its rollback, and the governed refusal with its lineage.

Next comes the field, and where it leads.

## 6. The field, and where it leads

The field leads in infrastructure, where plan and apply are the daily practice of many teams and the apply talks to real providers; this is general knowledge, as in section 1. Softanza's gate is about the change to code, which the field handles with a review.

The field's tools lead in breadth: they are not tied to one library, one language, or one declared knob. Softanza's gate judges what the code declared as a point. A change to a place that was never declared is not a refinement here; it is outside the gate.

And on trust, much of the field's approach is built to scale to any AI model. Mine rests on one declaration per point.

Now, where the gate stops.

## 7. The limit

What is built: the refinement point, the gate with its five checks, the cascade of a point and of a class, the reversal, the trust floor, and governed refining. The guards of section 5 cover them, with two exceptions. The cascade of a class has no guard here, because the code-graph guard scans a live path of the library's working tree. And no guard asserts the other points on a line.

What is designed, and absent from the library by name: the experience the original article describes. The class that article names, `stzPolyCode`, is not in the library at this commit. The one-line refinement of the design document, a point that explains itself, a plan that is applied, are not in the library. The cascade of the code graph and the cascade of the gate are not joined. And Haro has a gate in a spike written only in the former host language, with its own seat for refinement not built.

What is built, and where it stops: the limits of the gate as it stands.

- It checks the constraints of three kinds of point, a parameter, an algorithm and a library. A point of another kind, a block of code for instance, parses and passes without a check; checks for those kinds are the next step.
- An unknown trust posture ranks as trusted: the code gives it the top rank. So a proposal from an origin the code does not know clears a floor of trusted.
- A derivation is applied tentatively and restored on failure. So I say "never ends changed", not "never touched".
- The saved file holds the rendered source; the history, the postures, the timeline and the load-back are absent, and are the next step. Reversibility lives in the running object, and carrying it into the file is still to come. The library writes this file with the suffix `.zrfn`, as shipped. The Haro charter, ratified on 1 October 2026, takes the suffix `.rfn` for the refinement sentence of Haro, and leaves `.zrfn` to the library's lift from comment tags, the form this chapter ran.

## 8. Six doors

**The programmer.** Declare the places that may change, and propose changes to them as typed proposals. A refusal names its stage.

**The analyst.** The rule that spans several points is yours to declare, and the gate judges it on the state the change would produce.

**The designer.** The cascade is what you read instead of the diff: for a point, which line and which points on it; for a class, which classes inherit. They are two cascades, not yet one.

**The decision-maker.** Who may turn which knob is a permission and an authority against a risk tier, and the decision is recorded with its authority at the time.

**The educator.** Step back one, rewind to a named checkpoint, rewind to zero, go forward again. A learner can try without fear because every step keeps its prior value.

**The agent.** You may propose. Your origin is on the proposal, and a point can set a floor your origin does not clear.

## 9. Exercise

Take two settings of a program of yours: a rate and a ceiling, say, with a rule that the rate must stay below the ceiling. Declare them as points, with bounds, and declare the rule across them. Before you run anything, write under each proposal whether it is admitted and, if not, at which stage it is refused. Propose a change of the rate above the ceiling, and one from an origin you declare as an AI model, against a floor you set. Then rewind to zero and go forward one step.

Run it. If you were wrong about the stage, you have found a place where your own gate disagrees with your own expectation.

I left this one in your hands. Section 7 says what the gate does with an origin the code does not know, and the trust block of section 3 is the block to run. Its first lines are below, and `d` is the object of that block, so run section 3 first; change one thing, and replace `:llm` with a name of your own, one the code was never told about.

```haro exercise
d.TrustFloor("vat", :trusted)
r4 = d.Refine("vat").As(:yourorigin).To("0.25")
? r4[:admitted]
```

Run it, and read what the gate does against what section 7 says it does. I will not tell you whether the gate is right. When you have decided, you will know what the trust floor does with an origin it has never met.

The next chapter states a law: a language is declared and closed, and whatever speaks it, a person or a model, is judged by it. Here the thing judged was a change; there it is whoever speaks.
