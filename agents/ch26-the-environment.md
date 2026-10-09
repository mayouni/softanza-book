# The environment

Source: Chapter 26. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the interface as a text with a court that finds the element serving no verb; two projections of it, native and web, with a recorded table of divergences and a page that can say DISAGREE; the accessibility tree emitted from the declaration; a page the language serves on the loopback; a world that proposes and whose proposals clear when it is acted on; screens declared as intents; one generated browser surface; designed: the shell kit with two shells; the chrome as closed kinds (spine, ribbon, rail, status bar); the facet as data; a rail bound to focus; status cells read from the courts, with a guard that a cell never shows a state the court did not emit; absent: an IDE of this family; a class named for a ribbon, a rail, a spine or a status bar; a list of the twenty-two verbs in the library and a refusal of an unknown verb; a guard that judges a shell against the verbs; an editor; a measured latency

Run: 10 of 10 blocks kept their promise, on 2026-10-09 04:26 UTC+01:00.

## 1. The concept, as the field holds it

The field's environments have settled on a shape. A toolbar and a menu at the top, a sidebar of files, an editor, a terminal below, and a status bar at the foot. Lately an assistant sits in a pane or a terminal beside the code, and the human approves its edits. (General knowledge, marked.)

The record's own field studies, dated, are three. The notepad that ships with the former host language, measured on 12 August 2026 at thirty-three source files and about four thousand lines, seven dock widgets, a fifteen-key configuration and no language service: it exists, it ships in the box, and it works on the day you install it. The fast editors, in the ergonomics specification of March 2026: input to screen under sixteen milliseconds on any modern hardware, no exceptions; minimal chrome; no status bar clutter, no toolbar forests; a dry run before a structural change; and inspections that say why and offer a fix. And the status bar, as that specification wrote it: twenty-four pixels high, carrying only essential state, with five build states, one of which is *unchecked*, for a project where no build has run yet. The state of "not yet judged" has its own word. A bar that was green by default would be the field's usual lie.

Where the field is silent, the chapter answers. The field orders its toolbars by the tool's features, and not by the life of the thing being made. And it lets an assistant's proposal land as an edit, with the human's approval as a habit.

## 2. The first principle

**Declare the interface once. Every shell is a projection of it, and a projection may add renderings, never verbs.**

The library's header for its authored interface says it: the file is the contract, and the native markup and the web page are its projections. The study reads it as one declaration, two projections, proved to agree, resting on my ruling of 7 October 2026: carry both. The companion sentence is the interface constitution's, on the site: a new medium adds renderings, never verbs.

## 3. The Softanza form

Here I have to tell you something before the blocks. At this commit, **no IDE of this family exists**. No class in the library is named for a ribbon, a rail, a spine or a status bar. The study's own honesty line, proposed for the site, says it: no IDE of this family ships today; one shell does, for the sound plane; the foundation that would make the next one a projection is specified and not yet built. My reading agrees, with one addition: the library generates one browser surface, the emulator's, and I show it below with a loss.

What the library has are the pieces under each mark of the pattern, and they run. I take them in order.

### One shell, declared as text, judged by a court

The chrome is declared as text and judged before it is shown. The ribbon is generated from data, here a plain list; the facet as a library object is designed and not built. The court finds the one element that serves no verb. The four facet names are four of the five phases of the design corpus in the record: define, architect, build, govern, ship. I took four to keep the block short. Every declaration must carry its rationale, and a declaration without one is refused:

```haro
aFacets = [ "Define", "Build", "Govern", "Ship" ]
cTabs = ""
cIds = ""
for cF in aFacets
	cId = "tab_" + lower(cF)
	cIds += cId + ", "
	cTabs += 'DEFINE TEXT ' + cId + ' ( CONTENT "' + cF + '", ROLE tab, SATISFIES select ) RATIONALE "A facet."' + nl
next
cShell = 'DEFINE PANEL shell ( SIZE [640, 360], DIRECTION column, FONT "app", SATISFIES locate, CHILDREN [ribbon, work, status] ) RATIONALE "One shell, three bands."' + nl +
	'DEFINE BOX ribbon ( HEIGHT 32, DIRECTION row, ROLE tablist, SATISFIES discover, CHILDREN [' + cIds + '] ) RATIONALE "Facets, in the order of a life."' + nl + cTabs +
	'DEFINE BOX work ( HEIGHT fill, DIRECTION row, CHILDREN [page, rail] ) RATIONALE "The workspace and its rail."' + nl +
	'DEFINE TEXT page ( CONTENT "the work", SATISFIES read ) RATIONALE "What is being made."' + nl +
	'DEFINE BOX rail ( WIDTH 160, ROLE group, SATISFIES preview, CHILDREN [advice] ) RATIONALE "What the court proposes."' + nl +
	'DEFINE TEXT advice ( CONTENT "no proposal", SATISFIES understand ) RATIONALE "The rail, empty."' + nl +
	'DEFINE BOX status ( HEIGHT 24, ROLE status, SATISFIES understand, CHILDREN [state] ) RATIONALE "The truth of the build."' + nl +
	'DEFINE TEXT state ( CONTENT "clean", SATISFIES understand ) RATIONALE "The court verdict."'
oShell = new stzUiDocument(cShell)
? oShell.IsClean()
#--> 1
? len(oShell.Declarations())
#--> 12
? @@( oShell.Orphans() )
#--> [ "work" ]
```

> run: kept (touches the system)

The generating loop is the book's own, and the roles are from the closed list in the library: `tablist`, `tab`, `group` and `status` are on it.

### The twenty-two verbs

Every element must trace to at least one verb, and a word that is not one of the twenty-two is found. There is an honest division of labour. The library records the claim, with `SATISFIES`, and finds the untraced elements, with `Orphans()`. It does not hold the list and does not refuse an unknown intent: the guard asserts that an intent nobody has defined is not an error. So the list below is typed from the constitution, which is in its own repository, and the book holds it:

```haro
cShell = StzReplace(cShell, "DEFINE BOX work ( HEIGHT fill,", "DEFINE BOX work ( SATISFIES focus, HEIGHT fill,")
oShell = new stzUiDocument(cShell)
? @@( oShell.Orphans() )
#--> [ ]
aVerbs = [ "discover", "understand", "locate", "focus", "filter", "compare", "read", "scan", "scroll", "zoom", "select", "highlight", "preview", "mark", "act", "confirm", "cancel", "undo", "pause", "resume", "retry", "exit" ]
? len(aVerbs)
#--> 22
aStrangers = []
for cIntent in oShell.SatisfiedIntents()
	if not StzContains(aVerbs, cIntent)
		aStrangers + cIntent
	ok
next
? @@( aStrangers )
#--> [ ]
oOdd = new stzUiDocument(StzReplace(cShell, "SATISFIES preview", "SATISFIES transfer_funds"))
? oOdd.IsClean()
#--> 1
aStrangers = []
for cIntent in oOdd.SatisfiedIntents()
	if not StzContains(aVerbs, cIntent)
		aStrangers + cIntent
	ok
next
? @@( aStrangers )
#--> [ "transfer_funds" ]
```

> run: kept

`work` was a pure layout box, and the court counts containers too. Whether a container should be exempt from the verbs is the constitution's to say, and not the library's. The families, from the constitution: orienting, attention, information, selection, action, and continuity. And the interpretation I give: the library finds the stranger, and a list the library does not hold cannot refuse it. Chapter 25 said that the same list is applied by hand today. [AUTHOR: The twenty-two verbs are the interface constitution's, in its own repository, which the site says is not public yet. The library's own design text still lists twenty-four verbs from an interaction engine that your commit of 26 May 2026 removed as invented by an AI. May the chapter tell that removal as the refusal at its centre, that the library does not own the verbs, and print the twenty-two typed from the constitution?]

### Two projections

The same text yields the native markup and the web page. Every declared element is in both, and the two spell a property differently exactly where the profile records a divergence:

```haro
cRml = oShell.ToRml()
cHtml = oShell.ToHtml()
nBoth = 0
for cName in oShell.Names()
	if StzContains(cRml, 'id="' + cName + '"') and StzContains(cHtml, 'id="' + cName + '"')
		nBoth++
	ok
next
? nBoth
#--> 11
? len(oShell.Names()) - 1
#--> 11
? StzContains(cRml, "--rmlui-direction")
#--> 1
? StzContains(cHtml, "--rmlui-direction")
#--> 0
```

> run: kept

Eleven elements and not twelve: the panel is the page itself, and not a `div`. The native tier lays out through the engine's layout library, vendored, and draws through the graphics plane. I did not open a window.

### The browser shell

The browser shell is a page that the language serves, on the loopback. One request, one process, no network beyond 127.0.0.1. A second reactor plays the client, so it is offline by construction. The handler reads a global, because lambdas of the host language do not capture locals:

```haro
$cShellPage = cHtml
oSrv = new stzAppServer()
oSrv.Get_("/", func oReq, oResp { oResp.Html($cShellPage) })
oSrv.Start(0, "127.0.0.1")
oClient = new stzReactor()
cCRLF = char(13) + char(10)
nJob = oClient.SubmitTcp("127.0.0.1", oSrv.Port(), "GET / HTTP/1.1" + cCRLF + "Host: local" + cCRLF + "Connection: close" + cCRLF + cCRLF)
? oSrv.ServeOne(3000)
#--> 1
cAnswer = oClient.AwaitTcp(nJob, 5000)
? StzContains(cAnswer, "200 OK")
#--> 1
? StzContains(cAnswer, 'id="status"')
#--> 1
? oSrv.Host()
#--> 127.0.0.1
oSrv.Stop()
```

> run: kept

The cost of this shape is named in the record. A locally bound port is a surface and must be treated as one, and the design intent has been measured on nothing. The library already refuses to leave the loopback unauthenticated, at bind time:

```haro
oT = new stzAppTopology("shell")
oT.AddDataset("notes", [ [ "first" ] ])
oT.SetDatasetColumns("notes", [ "text" ])
oBackend = new stzAppBackend("shell", oT)
bRaised = FALSE
try
	oBackend.StartOn("0.0.0.0", 0)
catch
	bRaised = TRUE
done
? bRaised
#--> 1
? oBackend.IsLive()
#--> 0
```

> run: kept

### A status bar that tells the truth

A status cell is a function of the court's verdict, so it cannot say *clean* about a document the court refused. The function below is the book's own, over the library's `IsClean()` and its diagnostics. The library has no status-cell class, and no guard that a cell shows only what the court emitted; that guard is designed. The specification also names the state before any build, *unchecked*, and my function has no such state:

```haro
? ShellStatus(cShell)
#--> clean
? ShellStatus(StzReplace(cShell, "[page, rail]", "[page, ghost]"))
#--> refused: DANGLING_REFERENCE
? ShellStatus(StzReplace(cShell, "ROLE status", "ROLE sttus"))
#--> refused: UNKNOWN_ROLE

func ShellStatus(cText)
	oD = new stzUiDocument(cText)
	if oD.IsClean()
		return "clean"
	ok
	return "refused: " + oD.Diagnostics()[1][:code]
```

> run: kept

And what a screen reader reads is emitted from the declaration. A region declared `ROLE status` is emitted into the accessibility tree with its rationale as its description, in reading order, and no flag turns the tree off. The layout needs a font file, and this block uses the system's:

```haro
oShell.UseFont("C:/Windows/Fonts/segoeui.ttf")
oP = oShell.ToPanel()
oT = new stzAccessibilityTree(oShell, oP)
? oT.NodeCount()
#--> 12
? oT.NodeOf("status")[:role]
#--> status
? oT.NodeOf("status")[:description]
#--> The truth of the build.
? @@( oT.ReadingOrder() )
#--> [ "window", "tablist", 'tab "Define"', 'tab "Build"', 'tab "Govern"', 'tab "Ship"', "group", 'label "the work"', "group", 'label "no proposal"', "status", 'label "clean"' ]
```

> run: kept

The library's header says why: every toolkit gates accessibility behind a performance flag, which is where users silently get nothing, so here there is nothing to gate and nothing to forget to switch on. The same file says what a screen reader can operate, an agent can operate.

### A rail that proposes

A rail is a view over what the world proposes. A pulse proposes and never relates. Only an act on the world clears a proposal, and the world's own status line counts from the same list the rail shows:

```haro
oApp = StzAppQ("fieldvisits")
oApp.AddThingQ(:Client) { Has([ :name ]) }
oApp.AddThing(:Visit)
oApp.AddReactionQ(:Client).Unseen(90, :Days) { Propose(:Visit) }
oApp.AddInstance("amadou", :Client)
oApp.AddInstance("binta", :Client)
oApp.Live()
#--> [fieldvisits] is live -- 2 thing(s), 0 flow(s), 1 reaction(s), 0 goal(s); 2 proposal(s)
for aP in oApp.Proposals()
	? aP[1] + " " + aP[2] + " " + aP[3] + " " + aP[4]
next
#--> propose visit for amadou
#--> propose visit for binta
? oApp.Pulse()
#--> 0
? len(oApp.Proposals())
#--> 2
oApp.Relate("amadou", :visit, "visit-1")
oApp.Pulse()
for aP in oApp.Proposals()
	? aP[1] + " " + aP[2] + " " + aP[3] + " " + aP[4]
next
#--> propose visit for binta
```

> run: kept

`Live()` prints its line, and the judge compares what is printed. "2 thing(s)" counts the two things, Client and Visit, and not the instances. Chapter 20 owns the law beneath the rail, the proposal, the plan and the court.

And a screen is an intent. The one place the library already speaks in verbs is the world's screens. Five methods exist: `ToDiscover`, `ToUnderstand`, `ToFocus`, `ToSelect` and `ToAct`. A sixth verb, `ToCompare`, does not exist:

```haro
oW = StzAppQ("fieldvisits")
oW.AddThingQ(:Client) { Has([ :name ]) }
oW.AddScreenQ(:Home)  { ToDiscover(:Client) }
oW.AddScreenQ(:File)  { ToUnderstand(:Client) }
oW.AddScreenQ(:Pick)  { ToSelect(:Client) }
oW.AddScreenQ(:Edit)  { ToAct(:Client) }
oW.Explain()
#--> WORLD fieldvisits   lives in: memory (not persisted)
#      BEING
#        client (name)
#      MET FROM WITHOUT
#        screen home: discover client
#        screen file: understand client
#        screen pick: select client
#        screen edit: act client
try
	oW.AddScreenQ(:Side) { ToCompare(:Client) }
catch
	? cCatchError
done
#--> Error (R3) : Calling Function without definition: tocompare
```

> run: kept

The intent word is stored as a string, and is not checked against any list.

## 4. The decision, and what I refused

**I decided to carry both shells.** On 7 October 2026 I was asked whether the foundation takes the native shell or the browser shell, and I answered: carry both. The consequence the study states is that one chrome is declared once, and two shells project it.

**I decided that the mechanics are the library's and the IDE is the product's.** The library's design document: the paradigm mechanics are platform; the book, the brand, the IDE are product, and never leak. The foundation ships refinement as a library verb available to every program.

**I removed the interaction engine.** On 26 May 2026 my commit removed twenty-two modules invented by an AI that were not in the original Softanza, among them the interaction module. Its design text, which says twenty-four verbs and laws enforced by the engine, is still in the tree. The constitution's list is twenty-two.

**I refused to resolve intents inside the language of the panel.** The panel declares no meanings: there is no `:Danger` and there never may be. The intent slot was left deliberately unresolved.

**I refused to author the markup, and I refused a script engine.** The native markup is emitted, never authored; there is no script engine; flexbox only. The reason that the chrome is a text file and not a class.

**I refused a flag that turns the accessibility tree off.**

**I admitted a lens that cannot capture.** The estate's charter for its products: one truth, in files, and two lenses. What the charter refused was frameworks that capture the work. A lens that cannot capture is admissible. The environment is a projection of plain text, and not a store.

**A session removed a facet, and I restored it.** The reference design records that the Connections facet was first-class in the prototype of June 2026, and was removed by an agent on circular reasoning, which cascaded into five documents. I reinstated it. Who decides the ribbon is the author.

**I accepted the browser shell with its cost, unmeasured.** The charter of the front-door IDE chose a browser tab, built with the engine, with no install step, and named the loss.

**The pattern was learned by building it six times in two years**, the study counts. That count is the study's.

## 5. The court

`gui_stzui_narrated` proves the closure of the panel court, a dangling reference, a duplicate, an orphan box, a missing panel, the mandatory rationale and a round trip; and in scene 13, the intent slot: `SATISFIES`, `Orphans()`, and that an intent nobody has defined is not an error. `gui_profile_narrated` proves that the profile is data, with three recorded divergences; that one document has two projections and every declared element is in both; and that the fixture emits a self-checking page. The browser half of that guard is a procedure to reproduce. `gui_tier_agreement_narrated` proves that one display list rendered as vector and as pixels agrees to the pixel. It is not HTML against native. `gui_accessibility_narrated` proves the tree emitted from the declaration. `05_stzapp_live_narrated` proves that a live world proposes and acting clears. `emulator_narrated` proves the generated surface of the emulator.

There is no guard that judges a shell against the twenty-two verbs, none that a status cell shows only what a court emitted, and none that the two projections of a chrome agree in the browser. The study says so, and I found nothing to the contrary.

**The two-projections check can fail, and it did.** The library's fixture is a page and not an assertion: it carries the web projection and the boxes the native layout produced, and a script that compares them and prints a verdict strip. A runner cannot judge it, so I read it by hand on 8 October 2026. On the chrome of the first block, eleven boxes with text in each region, the strip read "AGREE on every declared box of 11", with a note that four boxes of automatic width differ, which is two shapers and not the profile. On the same three-band chrome with empty regions, the strip read "DISAGREE on 1 declared boxes of 3". The cause is in the web projection: an empty box is emitted as `<div id="body"/>`, which an HTML parser reads as an open tag, so the siblings that follow nest inside it. The native tier is unaffected. The fixture catches it, and the library's guards do not, since their own showcase has no empty box. An empty workspace is the pattern's first state. So the strip tells the truth both ways, which is the chapter's fifth mark in one picture, and the library has a defect on the exact case.

## 6. The field, and where it leads

The fast editors set a bar that the record writes down as law for its own product: input to screen under sixteen milliseconds, a cold start under four hundred, no exceptions. And it has measured it on none: neither shell has a latency number.

A text change dirties the whole document. One bound value changed re-shapes every string, where a colour re-shapes one. The field's editors patch.

The browser costs what it costs: file access through the browser's model, a port to guard, and an unmeasured latency. The native shell costs a window system and a GPU.

The field has a language service, and the record has a contract and no service. The explorer's model reads the world file the service would emit, and it is loaded by no entry file: a block that calls it without a hand-written load fails.

The field's fast editor treats the status bar as clutter. The pattern keeps one and asks it to be true. That is a bet, and the record's own corpus argues the field's side in the same breath.

## 7. The limit

**The web projection carries no roles, no labels and no intents.** `ToHtml` emits an identifier and a style only. The tree that carries roles is a separate artefact, as the block above shows, so a browser shell would infer from bare `div`s what the native shell emits. The plan itself says the web has no adapter.

**The library's own mission control does not tell the truth.** The emulator generates a browser surface, a parts grid with status chips and fidelity badges, a device window and a console for each part. Its status words are constants of the device class and of the template, and they are not measured. Here a plan with one firmware part and one GPIO capability, and no pump anywhere:

```haro
oPlan = new stzDelivery("greenhouse")
oPlan.AddFirmware(:node, :ESP32)
oPlan.NeedsIn(:node, [ :GPIO ])
oEmu = new stzEmulator(oPlan)
oEmu.CompileEngineQ(FALSE)
oEmu.SetOutDirQ("_emu")
oEmu.Build()
cH = read("_emu/index.html")
? StzContains(cH, "needs a look")
#--> 1
? StzContains(cH, "2 approximated")
#--> 1
? StzContains(cH, "parts healthy")
#--> 1
? StzContains(cH, "Ready to ship.")
#--> 1
StzDirDeleteAll("_emu")
```

> run: kept (touches files)

The part gets "2 approximated" and, in the grid's detail, a text about pump timing and sensor noise: the greenhouse demo's text, returned for any microcontroller. The header says "parts healthy" and the banner says "Ready to ship." for the same plan, from literals. A backend-only plan prints "parts healthy" and none of the other words. "Deploy to production" is an alert. The truthful half is real: fidelity is printed, and the console refuses a verb that the part's engine subset lacks. That is narration in the library, which I did not run.

This is the loss against the library's own page. [AUTHOR: May the chapter print it beside "a status bar that tells the truth", as the loss against the library's own page, before the request to derive those words from the plan is answered?]

**`ToPanel` needs a font file and raises without one.** The accessibility tree and the fixture need a laid-out panel, so the blocks that use them depend on a system font.

**`Orphans()` counts containers.** Whether a layout-only box owes a verb is the constitution's rule to state.

What is built: the interface as text with a court; four closed kinds, a closed list of nineteen roles, a closed field set, a mandatory rationale, a round trip to a fixpoint; two projections, with a recorded table of three divergences and a page that can say DISAGREE; the accessibility tree, and a bridge that reaches a real screen reader's interface on Windows, read and not run by me; a declared value changes and the screen follows, with focus kept; a page hosted on the loopback; a backend that refuses to leave the loopback unsigned; a world that proposes; screens declared as intents; one generated browser surface; and one binary shell, the sound plane's listening bench, in about seven hundred lines of Zig, which I read and did not build.

What is designed: the shell kit with two shells; the chrome as closed kinds named for the spine, ribbon, rail and status bar; the facet as data, with its group, its place in the life, its artefact kinds, its court and its profile; the rail bound to focus; the governance cells read from the courts, with a guard that a cell never shows a state the court did not emit.

What is absent: an IDE of this family. Any class named for a ribbon, a rail, a spine or a status bar. A facet declaration. A list of the twenty-two verbs inside the library, and any refusal of an unknown verb: `transfer_funds` passes the court. A guard judging a shell against the verbs. A rail that follows focus. Status cells derived from courts. An editor. A measured latency. [AUTHOR: At this commit no IDE of this family exists. Should the chapter tell the pattern as designed, with the running pieces as evidence, ending on "no IDE of this family ships today", or wait for the shell kit?]

## 8. Six doors

**The programmer.** You write the shell as text, and a court tells you the one box that serves no verb before anything is drawn. The same file is a native window and a page, and the library has a page that says when they disagree.

**The analyst.** The ribbon is the order of your solution's life, and not of a tool's features. The status cell reads the court, and you can ask the world what it proposes before it is asked to act.

**The designer.** Your interface has a constitution of twenty-two verbs and a closed grammar that adds renderings and never verbs. Every element must say which verb it serves, and the library already finds the ones that say none.

**The decision-maker.** Ask of any environment three things. Does its status bar read a court? Does its assistant live in one panel and propose? And who judges that the two shells agree? Here the answers are: designed; designed, with the rail's law built beneath it in chapter 20; and a self-checking page, with its first defect found in an hour.

**The educator.** The exercise is a prediction: say what the court will answer before you run it. The status word that is a constant is a lesson in the difference between a label and a truth.

**The agent.** The shell is a text file that you can read and write, and the tree a screen reader reads is the tree you may read. Your proposals appear in a rail and commit nowhere.

## 9. Exercise

One exercise, in three moves.

1. Write a shell of your own in five elements: a title bar, a ribbon of three facets taken from your own solution's life, a work area, a rail, a status bar. Before you run anything, write on paper which of the twenty-two verbs each element serves, and which one of your boxes you expect the court to call an orphan.
2. Run `IsClean()` and `Orphans()`, and compare with your paper. Then break the file three ways: a child that is declared nowhere, a role that is not on the list, and an intent that is not one of the twenty-two. For each, write what your status function will answer, and whether the library, the book's function, or nobody will catch it.
3. Emit the page, open it, and write the line the fixture strip will print for a version with an empty work area. Then look.

```haro exercise
oMine = new stzUiDocument('DEFINE PANEL shell ( SIZE [640, 360], DIRECTION column, CHILDREN [bar] ) RATIONALE "Mine."' + nl + 'DEFINE TEXT bar ( CONTENT "mine", SATISFIES understand ) RATIONALE "Mine too."')
# under each line, write what you expect before you run it
? oMine.IsClean()
? @@( oMine.Orphans() )
```

> run: exercise (touches the system)

If a promise breaks, do not change it: explain the output first.
