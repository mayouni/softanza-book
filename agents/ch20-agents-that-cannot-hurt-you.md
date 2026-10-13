# Agents that cannot hurt you

Source: Chapter 20. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: reversibility as a declared contract and a registration gate; posture set against reversibility, at the door and at load; the workbench, the plan, the reviewer's rejection, the committing actor under a scope; the containment drill; the engine's bounded slots and queue (the bounded inbox is tested in Zig only, not run for the book); designed: the agent's side of the negotiation over a plan; the examination hall; branches as parallel minds; twins for databases, interfaces and networks; absent: a plan with no executor that is refused; a ranking of a plan's risks; code already running in the process, which is out of scope; the Right to a Human as a machine check

Run: 9 of 9 blocks kept their promise, on 2026-10-13 10:17 UTC+01:00.

In this chapter I take the action half of what chapter 17 said of the whole mind: what happens when the proposal meets the world. I show four steps in code, the agent proposes, the workbench rehearses, the court judges, and only a governed actor commits, and then the cases where a step does not hold. I say what I refused: safe agents, a permission check as the boundary, a second workbench for machines, an optional gate. And I say where it stops: a plan with no executor at all is allowed, and the loop checks that a coverage statement exists, not that it is true. The principle is the doctrine's: do not build safe agents; build a safe world, and let ordinary agents loose inside it.

## 1. The concept, as the field holds it

In the field, safety is a property of the agent. The doctrine document of the library lists what the field offers: alignment, guardrails, confirmation prompts, a checkbox that says a human is in the loop. Tool-using agents, and the autonomous agents that descend from them, let the model's tool calls touch reality immediately, with a prompt for confirmation. Computer-use agents run in a sandboxed virtual machine, which contains a process, and does not tell a file moved from random bytes churning.

The best advice of the field, which the narration says every serious guide of 2026 gives (it paraphrases one roadmap), is to separate planning from execution and put a human approval between them. It is good advice, and it is advice: a pattern you implement, and can forget. The threat lists of the field, the OWASP list of risks for agentic applications among them, are lenses, and the record uses them so.

So the field's posture, in a line, is that the agent is a model in a loop, and safety is vigilance around it. (General knowledge, not a study of the record, except where I name the document.) Chapter 17 said this of the whole mind. This chapter takes the action half: what happens when the proposal meets the world.

## 2. The first principle

**Do not build safe agents. Build a safe world, and let ordinary agents loose inside it.**

The sentence is in the library's doctrine document: "We will not build safe agents. We will build a safe world, and let ordinary agents loose inside it." The document gives its structural half in one more sentence. The only artifact that ever leaves its world is an update plan, and plans are executed by someone else. The document carries no date and no author line in its header, and git first records it in a commit of 9 July 2026. The chapter holds the sentence as the document's, dated by that first commit, and gives no date of writing.

## 3. The Softanza form

Four steps, in the form the study of the record gives them: the agent proposes, the workbench rehearses, the court judges, and only a governed actor commits. I will show each in code, and then the cases where a step does not hold.

**May this agent exist?** Before an agent runs a single tick, the governance asks the question, and it asks it when the answer is free. An agent that declares no coverage, one sentence saying what it covers, is refused. An agent that declares no reversibility class is refused too: reversible, compensable or irreversible. Both refusals are in the engine's own sentences, and the door of the former host language repeats them. What does it say to an agent that declares no coverage, and to one that declares no reversibility class? Run it:

```haro
oGov = new stzGovernance("shop")
oGov.DeclareReversibility("restocker", :Compensable)
? oGov.ReversibilityOf("restocker")
#--> compensable
? oGov.MayRegister("mystery", "", "reversible")
#--> 0
? oGov.Why()
#--> AGENTLOOP-R4: agent 'mystery' declares no coverage statement. Registration refuses it. Say what this agent covers, in one sentence, before the loop will run it. Law 18: nothing schedules what nobody has stated the reach of.
? oGov.MayRegister("mystery", "reorders stock", "")
#--> 0
? oGov.Why()
#--> AGENTLOOP-R5: agent 'mystery' declares no reversibility class. Registration refuses it. Declare one of: reversible | compensable | irreversible. Law 18: an agent whose reversal nobody stated cannot be scheduled by something that cannot undo it.
? oGov.MayRegister("mystery", "reorders stock", :Compensable)
#--> 1
```

> run: kept

The first refusal ends on its law, `Law 18: nothing schedules what nobody has stated the reach of.` With both stated, the third call answers `1`.

Reversibility is the sixth contract of the governance, beside risk, authority, commitment, decommission and lineage. It is orthogonal to risk: an act of small risk that cannot be undone deserves more ceremony than a large one that can.

**The harder an act is to undo, the more trusted the code that does it must be.** Which postures may perform which classes of act? Here is the whole table, printed by a loop of the book's own:

```haro
aPostures = [ "trusted", "external", "sandboxed" ]
aClasses = [ "reversible", "compensable", "irreversible" ]
for cP in aPostures
	cRow = cP + ":"
	for cC in aClasses
		if StzPostureReversibilityRefusal(cP, cC) = ""
			cRow += " yes"
		else
			cRow += " no"
		ok
	next
	? cRow
next
#--> trusted: yes yes yes
#--> external: yes yes no
#--> sandboxed: yes no no
? StzPostureReversibilityRefusal("sandboxed", "irreversible")
#--> a 'sandboxed' posture does not cover 'irreversible' work -- the harder an act is to undo, the more trusted the code performing it must be (reversibility x posture, ruling 3.2)
```

> run: kept

Read down the rows: trusted code may do all three classes of act, external code the first two, sandboxed code only the reversible. The last line asks for the refusal and prints its sentence.

**The agent runs, believes it acted, and the disk does not move.** An agent is a file and a few functions. Its function writes a price list. It is given a workbench, and the function reaches the bench as an ambient object during one cycle, with no change in its signature. The skill verifies its own work and the fact is learned. After one cycle, does the real file exist? Ask the disk, then the bench:

```haro
StzAllowAgentFunction("ScribblePrices", "trusted")
cFx = StzReplace(WorkingDirectory(), "\", "/") + "/_fixture"
StzDirCreatePath(cFx)
$cPrices = cFx + "/prices.csv"
cPia = "pia: 2
name: scribbler
kind: pi
coverage: writes a price list and records that it did
reversibility: compensable
schedule:
  timer: 20
skills:
  - name: scribble
    when: always
    does: ring:ScribblePrices
    verify: fact prices were written
    posture: trusted
"
oAg = StzAgentDeclarationQ(cPia).ToAgent()
oAg.GiveWorkbench()
? oAg.Cycle()
#--> 1
? oAg.MemoryQ().Fact("prices", "were", "written")
#--> 1
? StzFileExists($cPrices)
#--> 0
? oAg.WorkbenchQ().Exists($cPrices)
#--> 1
? oAg.WorkbenchQ().ContentOf($cPrices)
#--> espresso,2.40
#--> flat-white,3.10

func ScribblePrices(poMemory)
	StzActiveWorkbenchQ().WriteFile($cPrices, "espresso,2.40" + char(10) + "flat-white,3.10")
	poMemory.Learn("prices", "were", "written")
```

> run: kept

The file lives in the twin. The agent believes it acted, and the disk did not move!

Two lines decide who may act. `posture: trusted` is in the file, because a `ring:` clause must carry a posture. `StzAllowAgentFunction` is a line of the platform's code, and not of the agent's file, and it decides which functions a file may call.

**The only export is a plan, and it narrates itself.** The tick exports toward reality a plan and nothing else. The plan says what it would do before anything is attempted. A language model set as its executor is refused before any attempt: `actor 'eager-llm' cannot commit -- it lacks the 'effectful' capability (required by operation 1)`. A named actor under a scope that does not cover the path commits nothing: the disk still did not move. The same actor under a scope that covers the path commits once, and the audit trail reads `[ [ 1, "committed", "write_file", "shop-committer" ] ]`. Who may commit, and when does the disk finally move? In this block, reality changes here and only here:

```haro
oPlan = oAg.GenerateUpdatePlan()
? StzReplace(oPlan.Narration(), cFx, "<fixture>")
#--> Update plan (1 of 1 operations to commit):
#-->   * 1. write 29 bytes to '<fixture>/prices.csv'
oPlan.SetExecutor(LLMActor("eager-llm"))
? oPlan.MayCommit()[2]
#--> actor 'eager-llm' cannot commit -- it lacks the 'effectful' capability (required by operation 1)
oScope = new stzCommitScope()
oScope.AllowUnder("/somewhere/else")
oPlan2 = oAg.GenerateUpdatePlan()
oPlan2.SetExecutor(PIActor("shop-committer"))
oPlan2.SetScope(oScope)
oPlan2.Execute()
? StzFileExists($cPrices)
#--> 0
oScope3 = new stzCommitScope()
oScope3.AllowUnder(cFx)
oPlan3 = oAg.GenerateUpdatePlan()
oPlan3.SetExecutor(PIActor("shop-committer"))
oPlan3.SetScope(oScope3)
oPlan3.Execute()
? StzFileExists($cPrices)
#--> 1
? @@(oPlan3.AuditTrail())
#--> [ [ 1, "committed", "write_file", "shop-committer" ] ]
StzDirDeleteAll(cFx)
```

> run: kept (touches the system)

I replaced the absolute path in the narration so the output is stable. A plan embeds the path of the file it would write.

**The court at load.** Is the table above enforced when the file is loaded, before the first tick? Take the same file, make the agent irreversible, and make its code sandboxed:

```haro
cIrrev = StzReplace(StzReplace(cPia, "reversibility: compensable", "reversibility: irreversible"), "posture: trusted", "posture: sandboxed")
oD = StzAgentDeclarationQ(cIrrev)
? oD.IsValid()
#--> 0
? oD.CiteFindings()
#--> [pia-posture-reversibility @ skills.scribble.posture] a 'sandboxed' posture does not cover 'irreversible' work -- the harder an act is to undo, the more trusted the code performing it must be (reversibility x posture, ruling 3.2)
```

> run: kept

The court answers with the table's own sentence: `a 'sandboxed' posture does not cover 'irreversible' work`. The same rule, at load: the file is refused before its first tick!

**A proposal gone wrong.** A tidy-up that deletes every file of a folder, driven here by hand through the twin as an agent would drive it, proposes thirty deletions. The plan lists thirty operations and flags thirty as risks. A language model that asks to commit is refused. And when it calls `Execute()` anyway, how many files are left? Count them:

```haro
cDir = StzReplace(WorkingDirectory(), "\", "/") + "/_course"
StzDirCreatePath(cDir)
for i = 1 to 30
	StzFileWrite(cDir + "/lesson" + i + ".txt", "lesson " + i)
next
oBench = new stzVirtualFileSystem()
oBench.SetActor("tidy-bot")
for i = 1 to 30
	oBench.MirrorFile(cDir + "/lesson" + i + ".txt")
	oBench.DeleteFile(cDir + "/lesson" + i + ".txt")
next
oBig = oBench.GenerateUpdatePlan()
? oBig.NumberOfOperations()
#--> 30
? len(oBig.Risks())
#--> 30
oBig.SetExecutor(LLMActor("helper-llm"))
? oBig.MayCommit()[2]
#--> actor 'helper-llm' cannot commit -- it lacks the 'effectful' capability (required by operation 1)
oBig.Execute()
nLeft = 0
for i = 1 to 30
	nLeft += StzFileExists(cDir + "/lesson" + i + ".txt")
next
? nLeft
#--> 30
```

> run: kept (touches files, the system)

Thirty! The model asked, was refused, called `Execute()` anyway, and nothing on the disk changed.

The site shows this with a larger course, in its education demo of 30 September 2026, which I did not run for this book, and prints a count of six hundred and ten. That figure is the site's, quoted with its source and date. I print thirty, because thirty is what this block runs.

**A person can argue with a plan.** The plan is a medium. A reviewer rejects one step, with a reason. What do the other twenty-nine steps do, and what is left on the disk? The block prints the counts, not the name of the file:

```haro
oRev = oBench.GenerateUpdatePlan()
oRev.RejectOperation(2, "reviewer: keep lesson 2")
oRev.SetExecutor(PIActor("oncall"))
oScopeC = new stzCommitScope()
oScopeC.AllowUnder(cDir)
oRev.SetScope(oScopeC)
aRes = oRev.Execute()
? aRes[1][2]
#--> 29
? aRes[2][2]
#--> 1
nLeft = 0
for i = 1 to 30
	nLeft += StzFileExists(cDir + "/lesson" + i + ".txt")
next
? nLeft
#--> 1
StzDirDeleteAll(cDir)
```

> run: kept (touches the system)

A named actor under a scope commits the other twenty-nine (`29`); one is skipped (`1`); and one file is still on disk (`1`), the file of the step the reviewer protected.

**One rule, two layers, the same words.** The refusal that chapter 17 showed at the graph, and that the file showed above, is also enforced in the engine's own tick loop, at registration. It is enforced in the sentence of the graph rule, no-llm-effectful. A model with the capability to produce effects is refused. A model without it registers like any other slot, a slot being the place in the loop that one agent takes:

```haro
StzResetEngineAgentLoop()
nL = stzenginezutercreate("summarizer")
? stzengineagentloopregister(nL, 1, 1, 0, 1, 0, 10, "summarises tickets")
#--> -6
? stzengineagentlooplastrefusal()
#--> AGENTLOOP-R6: agent 'summarizer' (slot 0) breaks the rule no-llm-effectful -- llm actor holds 'effectful' -- an LLM proposes, only a pi-gate commits. Registration refuses it. Drop the effectful capability, or register it as a pi-gated composition rather than an llm actor.
nL2 = stzenginezutercreate("proposer")
? stzengineagentloopregister(nL2, 1, 1, 0, 0, 0, 10, "proposes summaries")
#--> 0
StzResetEngineAgentLoop()
```

> run: kept

The engine refused the summarizer, in the words of the graph rule! The arguments after the slot are, in the order the guard gives them: the kind (1 is a model), the reversibility class, the trigger and the capability. What remains is the priority, the interval in milliseconds and the coverage sentence. They are the engine's low-level names, and I show them so you can see the refusal come from the engine, in the same words.

**An agent of the estate's own roster, rehearsed.** Until 22 August 2026, an agent of the estate's own roster, the one that rolls the ledger, moved a real journal file directly, on a tick. It had no plan, no scope and no committing actor.

A ledger is a record of what happened, kept in the order it happened. This agent rolls the estate's own ledger. Chapter 21 has the security ledger, which the court writes and never the thing it judged, a hash chain in which an edited line is named. Chapter 23 has the constellation's ledger of crossings, with their timings. A register is something else: a form a reply can take, or Appendix A.

The doctrine had been written before it was true, and the record caught it the same day. Since then the function that writes for that agent has a rehearsing path. Inside the tick of an agent that holds a workbench it writes into the twin. Outside one, in the migration state the live estate still runs, it is still the direct write. The declaration below is my own, written for this book; it is not the live roster file, which I did not run. Given a workbench, the agent relocates the file in the twin. Two skills fire and verify; the real journal file is where it was; no archive exists; the tick has exported a plan. And only the committing actor, under a scope, moves the file:

```haro
cEstate = StzReplace(WorkingDirectory(), "\", "/") + "/_estate"
StzDirCreatePath(cEstate + "/dashboard")
StzDirCreatePath(cEstate + "/journal")
SetEnvVar("STZ_SOFTANZA_ROOT", cEstate)
StzFileWrite(cEstate + "/journal/2000-01-scar.md", "an old journal entry" + char(10))
StzFileWrite(cEstate + "/dashboard/SESSION-LOG.md", "# SESSION-LOG" + char(10) + char(10) + "2000-01-15 09:00 | someone | long ago" + char(10))
StzAllowAgentFunction("RollRelocateMonths", "trusted")
StzAllowAgentFunction("RollWritePointer", "trusted")
cRoll = "pia: 2
name: ledger-roll
kind: pi
coverage: moves journal months before the current one into archive and leaves a pointer
reversibility: reversible
schedule:
  event: roll
governance:
  authority: delegated
  risks:
    relocate-evidence: 2
  grants:
    - relocate-evidence
skills:
  - name: relocate
    when: always
    does: ring:RollRelocateMonths
    verify: fact archive holds month
    effect: relocate-evidence
    posture: trusted
  - name: pointer
    when: fact archive holds month
    does: ring:RollWritePointer
    verify: fact ledger holds pointer
    effect: relocate-evidence
    posture: trusted
"
oRoll = StzAgentDeclarationQ(cRoll).ToAgent()
oRoll.GiveWorkbench()
? oRoll.Cycle()
#--> 2
? StzFileExists(cEstate + "/journal/2000-01-scar.md")
#--> 1
? StzFileExists(cEstate + "/journal/archive/2000-01-scar.md")
#--> 0
oRP = oRoll.GenerateUpdatePlan()
? oRP.NumberOfOperations()
#--> 7
? len(oRP.Risks()) >= 1
#--> 1
oRP.SetExecutor(PIActor("roll-committer"))
oScopeR = new stzCommitScope()
oScopeR.AllowUnder(cEstate)
oRP.SetScope(oScopeR)
oRP.Execute()
? StzFileExists(cEstate + "/journal/2000-01-scar.md")
#--> 0
? StzFileExists(cEstate + "/journal/archive/2000-01-scar.md")
#--> 1
StzDirDeleteAll(cEstate)
```

> run: kept (touches the system)

The count of seven operations is what this run measures. The library's own guard only promises at least five.

The blocks have shown what the world does; section 4 says what I refused to build instead.

## 4. The decision, and what I refused

**I refused safe agents.** The doctrine's reason is that the field's safety tries to make a fundamentally unpredictable actor trustworthy. I hold this reason as a view, not a result. Asking whether the agent might escape is like asking whether a chess engine might move a piece on a physical board. The doctrine says the agent's tool surface contains no operation that touches the disk, a database or the network. That is the doctrine's claim, and section 6 gives its limits.

**I refused a permission check as the boundary.** It is not a check that the agent might route around. The powers are separated: creativity without authority, authority without creativity.

**I refused a second workbench for machines.** The sandbox is the same workbench that the human programmer already uses. The framework was conceived for human programmers, and everything designed to liberate one is exactly what is needed to contain an artificial one. I hold this as a view, not a result.

**I refused to leave the gate optional.** The ruling of 22 August 2026 says the registration gate is doctrine, and that opting in is a migration state, not the design. The record is honest about the finding behind the ruling: where the doctrine of agents that cannot hurt you bound that day was nowhere. The safe world existed, and the agentic folder did not mention any of it. The ruling closed it the same day.

**I refused a stub.** Asking for a reserved agent raises. The architecture says that this is the law working, and not a defect.

**I refused to drop quietly.** In the engine, a send to a full inbox is refused with a code and counted. That is tested in the engine's Zig code, in a test I did not run, and no block here and no narrated guard shows it. When the run queue is full, further visits are dropped and counted. The loop also states what it cannot see: the inside of a callback, the clock, and whether a coverage statement is true.

**I refused to let a machine be the last resort.** The interface constitution of the estate has a right, the sixth of six: the Right to a Human. Wherever a machine serves, a person is reachable, clearly, and without penalty. It is enforced by judgment, a person's, and not by a guard that runs; the library does not mention it. The constitution holds it as the human end of the loop; its row is in Appendix C, read from the rules file.

Section 5 names the guards that prove what the blocks showed.

## 5. The court

`safeworld_narrated` has seven scenes: reversibility as the sixth contract; the registration gate in the engine's sentences; the table of posture against reversibility; the file's court at load. Three more follow: what the file declares landing in the agent's governance; the workbench, from the disk that did not move to the audit trail; and the roster's agent rehearsed and then committed. `agentfile_narrated` proves that an agent is a file judged at load, with one refusal per gate, and that a folder is a deployment. `agentloop_engine_narrated` proves that the engine loop states its coverage at run time, that registration is a gate, that one rule gives the same words in two layers, and that an over-full queue drops visits and counts them. `containment_drill_narrated` proves a drill against a real target on loopback: a model investigator proposes the containment and commits nothing; a human commits, and containment holds when verified from outside. In the run I made for my research note on 8 October 2026, the drill read 443 ms to detect and 61 ms to contain, on this machine. The book's data does not hold that run. The site prints other numbers from its own run, and the threat model others from its own. The three differ because the drill measures a clock. The limit of the drill is one attack shape, on loopback, on one machine, run on demand. `virtual_system_twin_narrated` proves the twin: a rehearsal touches nothing real; the plan narrates and flags its risks; a scope refuses; a reviewer rejects a step; snapshots roll back.

The guard `roster_narrated` is not in the front matter, because it cannot run from a snapshot of the library: it loads the estate's roster files from a sibling repository. The rehearsal of the roster's agent is proved by `safeworld_narrated`, whose seventh scene is the last block above.

Section 6 turns to the field, and to where it leads.

## 6. The field, and where it leads

The record's own table is honest, and I carry its rows in prose.

The field leads in connectors: chat, drives and trackers, hosted vector stores, streaming interfaces. They are reachable from Softanza and not paved.

The field leads in retrieval over open corpora. Softanza wins on a curated domain and loses on the open web.

The field leads in frontier reasoning. That stack orchestrates the largest models on every call.

The field leads in ecosystem and hiring. There is a labour market for that stack, and none for this one.

When to reach for which, after the narration: the mainstream stack, when the task is open-ended language work over material you cannot curate. Its examples are summarising arbitrary documents, conversational products, research over the open web. The Softanza layer, when actions have consequences and someone will eventually ask why it did that. Among those cases, in the narration's words: "regulated or audited work, anything that runs unattended, and anything that must keep working offline at zero marginal cost." The two are not exclusive, and a model can sit inside a Softanza system as a proposer.

The twin is a model of reality, not reality. The framework asks for fidelity and honesty, and the plan re-validates against reality before it is committed. After the real file is deleted behind the twin's back, the validation says the target is absent in reality. I saw it warn, and did not test whether it blocks the commit.

And the largest honest loss. The threat model puts *code already running in the process* out of scope: it can do anything the process can, wipe the ledger or read a secret. The workbench contains what is written through the bench. A function that does not ask for the bench is not confined. Reads are free: the workbench's own header says reads are sensing and stay free, and that only writes are confined to the twin. The architecture says that the escape is not a defect to be closed by removing it. It narrows it with a declared posture, and with code, not the file, deciding which functions an agent may call. I did not run a trusted function that bypasses the bench: I read this limit in the architecture, the threat model and the workbench's header.

## 7. The limit

What is built: reversibility as a declared contract, and the registration gate, in the door of the former host language and in the engine; posture set against reversibility at the door and at load. The workbench is built, with a plan that narrates, flags, validates, takes a rejection and keeps an audit trail; so is the roster's agent rehearsed and then committed, and so is the drill. The engine's bounded structures are built: 64 agent slots, an inbox of 8 messages (tested in Zig only, not run for this book) and a run queue of 256.

What is designed: the agent's side of the negotiation, in which the plan reaches the agent but the conversation about the plan does not yet. The architecture says so, and the threat model repeats it. I searched the library's code and found no revising of a plan. The examination hall, which would certify an agent for a commit scope the way you certify a driver for a licence class: it occurs in documents and in no code. Branches as parallel minds: snapshots and rollback are built, and I found no branch call. Twins for databases, interfaces and networks: the framework names them. The twin of files is built, and so is the twin of the process environment, with its variables, its working directory and its queued spawn (chapter 24). The other three are not.

Each item below is a gap, found while running and reading.

- **An unset executor and an unset scope are unguarded.** A plan with no executor answers that no executor is set, and that a human at the keyboard is unguarded, and `Execute()` is allowed. The refusal of the block above applies to a model set as the executor. Likewise the scope check runs only when a scope is set: a plan with an executor and no scope is committed with no check on the paths it touches. So "only a governed actor commits" is exact when an executor and a scope are set, and a person at a keyboard may commit a plan that names none.
- **A plan flags; it does not rank.** The narration says that a plan ranks its own risks. The code returns one flag per destructive step, in the order of the operations, with a label such as DESTRUCTIVE. There is no score and no order of severity. The chapter says "flags".
- **The gate is opt-in at the host.** The default flips when the last host in the tree declares. A fresh host runs the older pump.
- **The loop checks that a coverage statement exists, not that it is true.**
- **The drill's limits:** one shape of attack, on loopback, on one machine.

Six doors follow, the same chapter seen from six places.

## 8. Six doors

**The programmer.** Your agent is a file and a few functions. It runs and believes it acted, and the disk does not move. You read the plan, choose the committing actor and the scope, and the court tells you in one sentence which rule refused you.

**The analyst.** Every proposal is a narrated plan of operations with the destructive steps flagged, and an audit line for each commit. You can read what the agent meant to do, step by step, without running it. The flags are by kind, not scored.

**The designer.** The plan is the one artefact that crosses from the agent to the person, and a person can reject one step. The Right to a Human says a person is reachable wherever a machine serves, and the right is held by judgment.

**The decision-maker.** You declare what each agent covers and how reversible it is before it may exist, and you decide the scope and the actor that commits. A model is structurally unable to commit, even when fooled; the threat model assumes it will be. The hardest part is the one the design leaves to you: which functions code allows an agent to call.

**The educator.** A learner's agent that tidies a course folder by deleting everything is a lesson in what a plan is. She sees what it would have done, and the files are still there.

**The agent.** You may rehearse without limit, inside the twin. Your only export is a plan, and you can be argued with over it. You may not commit. Today the argument is one-way: you do not yet receive the reviewer's objection and revise.

## 9. Exercise

Choose a folder of ten files you could lose. Write an agent file for a tidy-up job on it: what it covers, how reversible it is, one skill. Before you run anything, write under each line the promise you expect: how many files exist on disk after one cycle, how many operations the plan holds, and how many of them the plan flags as risks. Then write what happens when you set a language model as the executor.

```haro exercise
cDirMine = StzReplace(WorkingDirectory(), "\", "/") + "/_mine"
StzDirCreatePath(cDirMine)
for i = 1 to 10
	StzFileWrite(cDirMine + "/file" + i + ".txt", "file " + i)
next
oMine = new stzVirtualFileSystem()
oMine.SetActor("my-tidy-bot")
# your tidy-up proposal here, with the promise you expect under each line
StzDirDeleteAll(cDirMine)
```

> run: exercise

Run it. Then give the plan to a committing actor under a scope that does not cover the folder, and write the promise again. If a promise breaks, do not change the promise: explain the output first. A good learner is surprised once. The plan flags its destructive steps and does not rank them, and a plan with no executor at all is allowed.

I left this one in your hands, on purpose. Take the block that committed the price list. The six lines that built `oScope3` and committed under it become these three, and the lines after them stay:

```haro exercise
oPlan3 = oAg.GenerateUpdatePlan()
oPlan3.SetExecutor(PIActor("shop-committer"))
oPlan3.Execute()
```

> run: exercise (touches the system)

Run it, and ask the disk what the plan did, then ask the audit trail. I do not tell you what you will find. The page says why in section 7, in the first item of its list of gaps; read it after you have looked, not before. When you can say why "only a governed actor commits" holds for this plan or does not, you will know what that sentence depends on.

Chapter 21 is about the court itself, in four of its forms: promises, perception, security and performance. Its principle is that a claim is only as good as the court that can refuse it, and that where no court can see, the record says so.
