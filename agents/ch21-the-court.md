# The court: promises, perception, security and performance

Source: Chapter 21. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the promise judged as a claim about a stop; the security plane with its ledger, sentinel, drill, response and secrets, and its table of guarantees tied to guards; the performance plane with its instrument and its governed loop; the perception law, adopted; designed: routes, the clock and weather, and perception for the promise runner; the plugin plane; the negotiation over a rejected plan; absent: a human verdict on any picture of the gallery; seven of the eight musical traditions heard by a person from them; a real vault and a real sandbox as proofs; a time-series store

Run: 7 of 7 blocks kept their promise, on 2026-10-14 12:00 UTC+01:00.

In this chapter I take the court of chapter 5, which judges whoever wrote the code. I show four courts, each by something it refuses: promises, perception, security and performance. I walk the traveller over a file of three promises, and ask the record how many of eight musical traditions a person has heard. I edit a sealed ledger and read which entry the chain names, and I let a model propose a performance plan it may not commit. I say what I refused, seven things in all, among them the word "narration" for what cannot lie, a second assertion library, a sixth state for a stop, a guarantee without a guard. The principle holds the four courts together: a claim is only as good as the court that can refuse it, and where no court can see, the record says so.

## 1. The concept, as the field holds it

Four practices of the field are four courts, and they are rarely seen as one.

The first is the example that runs. Python's doctest runs the interactive session found in a docstring and compares the printed text. Rust runs the examples in its documentation, and Go has testable examples with an expected output in a comment. The example is the specification. Its weakness is that the comparison is text against text, and the harness decides what a failure is.

The second is the snapshot test. A screenshot or a rendered tree is stored and compared on the next run. It proves that today's picture equals yesterday's.

The third is the audit against a list. The field's lists are OWASP's, NIST's and the compliance frameworks'. For detection and evidence, the toolchain is the log aggregator, the rule format, the orchestration of responses.

The fourth is the instrument. Micrometer, OpenTelemetry, Prometheus and the profilers of every runtime measure a program from the outside. (General knowledge, not a study of the record, except where I name the file.)

## 2. The first principle

**A claim is only as good as the court that can refuse it. And where no court can see, the record says so.**

The record has it in two sentences that meet. The threat model: every guarantee names the guard that proves it, and a guarantee without a guard is listed as an open risk. And the perception law: a comparison proves sameness and never rightness, and if a person is the last consumer, a person is the last gate. Under both lies the doctrine that the library repeats in every plane: expression is free, and admission is governed.

## 3. The Softanza form

Chapter 5 told the court that judges whoever wrote the code. This chapter has four courts, one per kind of claim. I show each by something it refuses.

### The court of promises

A promise in this book is the line `#-->` under an expression, and it is a claim about a stop of the program. The tool that reads it, called the traveller (it belongs to the plane named Testoor), says a promise is kept, diverged, unreached or unjudged. A promise that argues with itself, prose after a value, is never accused. What does the traveller say of a promise that is true, one that is false and one that argues with itself? Run it:

```haro
write("tour.haro", '? 1 + 1' + nl + '#--> 2' + nl +
	'? 1 + 1' + nl + '#--> 3' + nl +
	'? "C"  #--> "C" but should be "sm_AS"' + nl)
oTour = TravellerQ().Silent().Walk("tour.haro")
aClaims = oTour.Records()[1][:run][:stops][1][:claims]
? aClaims[1][:state]
#--> kept
? aClaims[2][:state]
#--> diverged
? aClaims[3][:state]
#--> unjudged
? oTour.ExitCode()
#--> 1
remove("tour.haro")
```

> run: kept (touches files)

It says `kept`, `diverged` and `unjudged`, and the exit code is `1`. That code is the runner's, and not the language's.

A promise can be that the line raises. That is read as a raise that was promised. When it happens, how does the tour end? Run it:

```haro
write("raise.haro", '? "before"  #--> before' + nl +
	'? Boom()  #--> ERROR: boom happened' + nl +
	'func Boom()' + nl + char(9) + 'raise("boom happened")' + nl)
oRaise = TravellerQ().Silent().Walk("raise.haro")
aRun = oRaise.Records()[1][:run]
? aRun[:stops][1][:claims][2][:state]
#--> kept
? aRun[:end]
#--> finished
? oRaise.ExitCode()
#--> 0
remove("raise.haro")
```

> run: kept (touches files)

The promise is `kept`, the end is `finished` and the exit code is `0`! The language process ended with an error, and the tour has finished as it said it would.

Every rule of this judge was learned by watching the harness accuse the library falsely. The guard's header says it. A short promise `6` once hid inside a later `[ 6, 28 ]`, and that is why the rule on spellings exists. This book's own judge is a copy of the site's judge, which is looser than the traveller.

### The court of perception

The record's sentence is that a comparison proves sameness, and that it never proves rightness. The library holds the case. A bar plot drew vertical bars for horizontal data while all of its seventy-three examples went on passing. This is why the plots now compare the picture exactly. That makes sameness strict; it does not make it rightness. Rightness is a person.

So a declared world carries its perception state. Eight musical traditions are declared as data in the library. How many of them has a person heard? Ask the record:

```haro
nUnheard = 0
for cName in StzSoundUniverses()
	if StzSoundUniverseQ(cName).Listener() = "UNPERCEIVED"
		nUnheard++
	ok
next
? len(StzSoundUniverses())
#--> 8
? nUnheard
#--> 7
? left(StzSoundUniverseQ("tunisian").Listener(), 5)
#--> HEARD
```

> run: kept

It answers `8`, `7` and `HEARD`: eight declared, and seven of them unperceived! Only one is heard, and that one's record carries a name, a date and a verdict. The counter in this block only counts the unheard; no counter decides the verdict. The one tradition that was heard was heard by me on 26 September 2026, through five original examples, and my verdict was "far from being qualified". Which part fails, whether the tuning, the phrasing, the rhythm or the timbre, I have not yet said. Those are my words, and they are the one recorded perception that is a refusal.

The law is the estate's, meaning the author's whole set of projects, adopted on 25 September 2026 at the author's instruction. It requires that the record names the perceiver and quotes the verdict. Its third requirement is the one I take with me: unperceived is a state, not a failure. It refuses two things as well. It does not say that a human must gate every commit, because it binds at the granularity of a phase. And it does not say that it generalises from one plane without further evidence, and it was held for a month on that account.

The gallery of pictures is where it is unmet. The library holds ninety-five judgements of pictures and text sections, in three index files, committed on 5 October 2026. Every one is by a model, reading the picture or reading the text the program printed. None has a human name. The first index says it in a sentence: no human has looked at these pictures. The register of findings ends with a line I repeat: a human verdict on a sample is still owed. The record holds no human verdict on any gallery picture. It stays unperceived.

### The court of security

The security plane starts from a claim. The threat model assumes that a hijacked language model will get through, and makes it harmless. The model never holds the capability, and so an LLM that is fooled still cannot act. The document does not try to detect every malicious prompt.

The evidence of what happened is a hash chain. Edit any line after the first, and the chain says which entry broke. If I edit one, which entry does it name, and does a wrong key draw the same accusation? Run it:

```haro
oLed = StzSecurityLedger(256)
oLed.Record(StzSecurityRefusal("auth.login.failed", HumanActor("admin"), "user:admin", "wrong credentials"))
oLed.Record(StzSecurityRefusal("secret.reveal.refused", LLMActor("advisor"), "secret:payments-key", "actor is not effectful"))
oLed.SealTo("evidence.txt", "the-evidence-key")
? StzVerifySealedLedger("evidence.txt", "the-evidence-key")[:why]
#--> chain intact over 2 entries
? StzVerifySealedLedger("evidence.txt", "another-key")[:why]
#--> the chain is intact but the SEAL does not match this key
write("evidence.txt", StzReplace(read("evidence.txt"), "actor is not effectful", "routine maintenance"))
? StzVerifySealedLedger("evidence.txt", "the-evidence-key")[:why]
#--> the chain breaks at entry 2 -- that record (or one before it) was edited
remove("evidence.txt")
```

> run: kept (touches files)

The verifier answers `chain intact over 2 entries`, then `the SEAL does not match this key`, then `the chain breaks at entry 2`. The chain named the break! A wrong key and an edited line are two different accusations. Notice which entry I chose to edit: the second. An edit to the first entry is not caught. The verifier checks each entry's text against the digest of the entry before it, and the first has none before it. That hid my first attempt. The narration states the limit in its own words: this is not protection against an attacker already running code in the process.

A secret is the same law applied to a key. Its only public face is its descriptor. A hand that may commit can read it. What does the court answer when a language model asks? Run it:

```haro
StzOpenSecurityLedger(64)
oKey = new stzSecret("deploy-key")
oKey.FromLiteralQ("ssh-ed25519-AAAA")
? oKey.Descriptor()
#--> <secret 'deploy-key' (secret) from literal>
? oKey.Reveal(HumanActor("ops"))
#--> ssh-ed25519-AAAA
try
	oKey.Reveal(LLMActor("planner"))
catch
	? cCatchError
done
#--> Refused: actor 'planner' (posture sandboxed) may not reveal secret 'deploy-key'. Only an effectful, non-sandboxed actor can read a secret.
? len(StzSecurityLedgerQ().Refusals())
#--> 1
StzCloseSecurityLedger()
```

> run: kept

It answers `Refused: actor 'planner' (posture sandboxed) may not reveal secret 'deploy-key'`. The court refused the model, and the ledger counts `1` refusal without anyone having called the ledger! This is chapter 17's law, that a model does not hold the capability to produce effects, applied to a key, with the record added.

What does the table of guarantees tie to a guard? The meta-guard of the threat model checks that the document exists with its sections, and that every guarantee row contains a proof. A proof is a guard's path, a fuzz run, a bill-of-materials check or a runbook. It checks that every guard path in the rows exists on disk, and that a planted fake row with an unproven guarantee is caught. It does not run the guards, and it does not check that a guard asserts what its row says. That is the security gate's job. So "each tied to a guard" is, exactly, "each names at least one proof, and every guard file it names exists".

At this commit the table holds 43 guarantees. The site says 38, on three pages. Both are true of their dates: the document had 38 rows on 30 September 2026, and the rows from 39 to 43 were added on 5 October. The site's number is the site's to update.

### The court of performance

An instrument owes a number. The honest stopwatch gives a number from a clock that only moves forward. It excludes a pause, and it ships two spans of one trace in one batch for an observability collector. If I pause it for 200 milliseconds, does the pause count in the elapsed time? Run it:

```haro
w = StzStopwatchXT("import-orders")
w.Lap("parsed")
w.Pause()
StzEngineTimeSleepMs(200)
w.Resume()
w.Stop()
? isnumber(w.ElapsedMs())
#--> 1
? w.ElapsedMs() < 200
#--> 1
? w.Record()[:running]
#--> 0
w2 = StzStopwatchXT("notify-customer")
w2.JoinTrace(w.TraceParent())
w2.Stop()
? w2.TraceId() = w.TraceId()
#--> 1
oBatch = StzOtelBatch("shop")
oBatch.AddSpan(w).AddSpan(w2)
? Q(oBatch.ToJson()).NumberOfOccurrence(w.TraceId())
#--> 2
```

> run: kept

The pause did not count: `w.ElapsedMs() < 200` printed `1`, and `w.Record()[:running]` printed `0`, because the stopwatch had stopped. The second stopwatch joined the first one's trace: `w2.TraceId() = w.TraceId()` printed `1`, and the batch's JSON holds the trace identifier `2` times, for two spans.

Careful with what this does not claim. The narration says the joined stopwatch gets a new span. I checked: it gets the same trace, as the `1` above shows, and the same span identifier, which this block does not print. The sentence holds for the server's echo, which I did not run, and not for the stopwatch. I list it among the requests.

The instrument is not the end of the court. Judgment and action live inside the program. A performance plan is proposed by a machine, and only an effectful actor commits it. What happens when a model asks to commit it, and then a person does? Run it:

```haro
oPlan = StzPerfPlan("relieve-queue")
oPlan.Propose(:ScaleUp, "nlp", "queue.depth: measured 900 (must be <= 100)")
oFleet = new FakeFleet
? oPlan.MayCommit(LLMActor("advisor"))
#--> 0
? oPlan.ExecuteOn(oFleet, LLMActor("advisor"))
#--> 0
? oFleet.CallCount()
#--> 0
? oPlan.ExecuteOn(oFleet, HumanActor("mansour"))
#--> 1
? oFleet.CallCount()
#--> 1
oPlan.Show()
#--> Perf plan relieve-queue -- 1 proposed action(s).
#      1. scaleup 'nlp' -- queue.depth: measured 900 (must be <= 100)
#    Audit (2):
#      #1 REFUSED scaleup 'nlp' by advisor -- actor is not effectful -- expression is free; admission is governed
#      #1 COMMITTED scaleup 'nlp' by mansour -- queue.depth: measured 900 (must be <= 100)

class FakeFleet
	aFleetCalls = []
	def ScaleUp(pcTag)
		aFleetCalls + [ "scaleup", pcTag ]
	def CallCount()
		return len(aFleetCalls)
```

> run: kept (touches the system)

The fleet here is a rehearsal double, any object that answers the same effectful verbs. The loop is proved against the double and not against a real fleet. A model asking to commit is refused before any attempt: `ExecuteOn` printed `0` and `CallCount` printed `0`, so the double counted zero calls! For the person, `ExecuteOn` printed `1` and `CallCount` followed with `1`. The same action is judged twice, and the audit keeps both judgments: `REFUSED scaleup 'nlp' by advisor -- actor is not effectful -- expression is free; admission is governed`, and `COMMITTED scaleup 'nlp' by mansour`.

The four courts have spoken, and now I say what I refused.

## 4. The decision, and what I refused

**I refused the word for the thing it was not.** The structure of this book and the closing assessment of the study call the articles "narrations that cannot lie". My own ruling of 7 October 2026, the study's 12.20, says that "narration" names the articles under the library's documentation folder, and not the executable suites. The site's runner annotates an article and no longer decides whether it is shown. The site's own record of 8 October 2026, run on another commit than this book's, says that of 135 articles 55 ran. Of the 423 blocks in those, 123 kept their promise. So the articles can drift. What cannot lie are the executable guards, and this book's own build, which fails when a block does not keep its promise.

**I refused a second assertion library.** The promise runner's rulings refuse a second library, a rewrite of the test files, a coverage percentage before there are routes, and a mock written for a platform's production. They refuse the word "verified" on a perceptual claim without a name and a sentence.

**I refused to fold unjudged or unperceived into pass or fail.** A stop has five states and no sixth: kept, diverged, unreached, unjudged, unperceived. A runner that folds unjudged or unperceived into pass or fail is wrong. I hold this as a view, not a result.

**I refused to analyse tampered evidence.** A tool that verifies, warns, and then analyses anyway teaches its users to ignore the warning. This is my view.

**I refused to detect everything.** Detections are declared. The sentinel speaks on transitions only: quiet, one alarm after five wrong passwords, and nothing new after a sixth, since the story did not restart. It does not write its own firings into the ledger, because detections over detection events invite feedback loops.

**I refused to compete with the field's ecosystem.** The performance study of 29 July 2026 says the plane does not compete with Grafana, Datadog or the ecosystem of OpenTelemetry, and should not pretend to. It exports.

**I refused a guarantee without a guard.** The threat model's last rule is that a guarantee is added only together with its guard.

Now the guards that prove what ran.

## 5. The court

`testoor_promises_narrated` proves each promise rule planted both ways. A lie is diverged; two lies are both caught; a short lie does not hide in a later list; the spellings of a true value are all kept. An expected raise is honoured; prose is unjudged; a program that does not compile is not diverged; a raise part-way leaves the later promises unreached. `threat_model_narrated` proves the meta-guard described above, including its negative sibling. `security_ledger_narrated`, `secretstore_narrated` and `secret_narrated` prove the chain and the seal, the store and the secret. `security_sentinel_narrated` proves the edge-triggered sentinel. `stopwatch_narrated` and `tracing_tail_narrated` prove the instrument and the batch. `governed_loop_narrated` proves the plan, the preflight, the commit and the audit.

The build counts 11 assertions in `threat_model_narrated`, a static count of its assertion calls. The others are counted by the build too, and not run here. The performance plane has twelve guards. I do not print their sum, because the build counts them.

## 6. The field, and where it leads

The record's own honest sections, each loss beside its win.

**In performance.** A time-series database, a query language and dashboards are the field's today, and absent here. By design, the plane exports. Its sampling answer is bounded rings that drop the oldest; head and tail sampling are what the field does better today. Distributed context reaches HTTP today; going past it is the next step. The ecosystem of integrations and auto-instrumentation for every framework is the field's. The profiler is cooperative: it sees what you bracket, where a native profiler sees everything. The win it claims is that judgment and action live inside the program: budgets that fail the build, tuning that passes governance, monitoring that prices itself.

**In security.** The ledger is a bounded ring, and bounded means forgetting. Telemetry from the host, the kernel and the network is absent; the plane reads what the program's own seams emit. Detections are declared and not learned; learning them is the next step, and one detection of rates on 30 September 2026 already covers part of it. The record's own comparison is that a rule corpus of the field's format is larger today than the eight detections shipped, and the field leads here. The workflow of a security operations centre is the field's today. The largest gap, in the record's words, is that a detection can only see what a seam emits. The win is that the event is typed at birth, where the door refuses, so no parser stands between what the program knew and what the detector judges.

**In promises.** The field's doctests sit in the host's toolchain and answer pass or fail (general knowledge). The house's judge has five states. Where the field leads is instruments: the launch memo of Testoor, the plane that holds the traveller, counts coverage instruments of any kind at zero today, and route coverage is the next step.

**In perception.** The field's visual snapshot services are mature and automatic (general knowledge). The house's law says a perception does not replace a number, and no number replaces it.

The study of the record puts the tone I try to echo. A grid of two hundred and eighty-six ticks against two hundred and sixty-nine crosses is, in its words, the shape of a brochure.

Now to where the chapter stops.

## 7. The limit

What is built: the promises as stops; the security plane, with its ledger, sentinel, drill, response, attestation and secrets; the performance plane from its first phase to its last; the perception law, adopted. And the declared verdict tables for the singing voice and the eight universes. The table of guarantees holds 43 rows that name 57 distinct guard files, none missing.

What is designed:

- The promise runner's routes and map, its clock and weather, its excursions, perception and mutation, and its inherited tours. All are planned. The state *unperceived* is named in the runner's header, and the reader assigns none of them.
- The negotiation over a rejected plan, which the threat model calls design only.
- The plugin plane: plugins are not shipped, and foreign code is not yet governed.

What is absent:

- **A human verdict on any gallery picture.** Zero of ninety-five. The law's second requirement, a name, a date and what they said, is unmet there. The chapter says unperceived, and does not say verified.
- Of the eight musical traditions, seven unheard.
- A real vault and a real sandbox as proofs. The vault resolver is tested against a stand-in, over real HTTP. The cloud key-management adapter is absent.
- Paths on POSIX systems, unverified, until a Linux machine is available; scheduled fuzzing; continuous integration; signed commits, which the author deferred for the development phase.
- A time-series store. A coverage percentage, which is refused until there are routes.

Three more things belong here, found while running the court.

**The drill's numbers differ by source.** The threat model's measure of responsiveness comes from three runs. It is a detection in a little over three hundred and fifty milliseconds, and a containment in a little over fifty. The site prints 395 and 50, from a replay of 1 October. They differ because the drill measures a clock. One attack shape, on loopback, on one machine, run on demand. Whichever number you print, you name its source.

**A possible defect in the promise judge, which I report and have built nothing on.** A file whose first promise is a lie and whose last is a promised raise reads the lie as unreached and the raise as kept. The tour is broken, with zero diverged, and the exit code is 1. I reproduced it twice. Each rule alone behaves as the guard plants it. Whether a divergence above a promised raise should read *diverged* is a question for the Testoor plane, which holds the traveller.

**Counts that disagree between sources.** The study's closing says 387 narrated guards. My `find` on the pinned snapshot says 529 files named so. The build's own count of guards is the one to use, and neither of the two.

Six doors follow, one for each reader.

## 8. Six doors

**The programmer.** Your examples already carry their expected output. The traveller reads them as promises and says kept, diverged or unjudged, and prose that argues with itself is never accused.

**The analyst.** The threat model is a table you can read: each row with the guard that proves it and its honest limit. The performance judgment is declared before the code runs.

**The designer.** A picture or a sound is a claim only a person can close. The gallery says a model looked and no human has. Your verdict is a named line in the record.

**The decision-maker.** The question who decided, and what is written down, has a mechanical answer in both planes. The same action is refused for the model and committed for the human, both in one audit, and the evidence is sealed so that an edit is named.

**The educator.** The tutor's rule meets the court. Predict the verdict of a promise before the traveller walks it.

**The agent.** You may propose a containment plan or a tuning plan and you may commit neither. Your refusal is itself a recorded event. Do not tell a person that a picture is right. Say "unperceived".

## 9. Exercise

Predict, in writing, before you run anything. The file below holds three promises. Which state will each one have?

```haro exercise
write("mine.haro", '? 2 * 3' + nl + '#--> 6' + nl +
	'? 2 * 3' + nl + '#--> 7' + nl +
	'? "ok"  #--> "ok" but see why' + nl)
# before you run: which state will each of the three promises have?
oMine = TravellerQ().Silent().Walk("mine.haro")
aMine = oMine.Records()[1][:run][:stops][1][:claims]
# your three predictions, then:  ? aMine[1][:state]   ? aMine[2][:state]   ? aMine[3][:state]
remove("mine.haro")
```

> run: exercise (touches files)

Run it. The states are kept, diverged and unjudged. Then add a fourth line that raises, promise it with `#--> ERROR:`, and predict first how the tour will end. Do not change your prediction to match what you see. Explain the output first.

I left this one in your hands. Here is the raise block of section 3 with one change: its first promise is now a lie.

```haro exercise
write("raise.haro", '? "before"  #--> after' + nl +
	'? Boom()  #--> ERROR: boom happened' + nl +
	'func Boom()' + nl + char(9) + 'raise("boom happened")' + nl)
oRaise = TravellerQ().Silent().Walk("raise.haro")
aRun = oRaise.Records()[1][:run]
# what does the tour say of each promise, how does it end, what is the exit code?
? aRun[:stops][1][:claims][1][:state]
? aRun[:stops][1][:claims][2][:state]
? aRun[:end]
? oRaise.ExitCode()
remove("raise.haro")
```

> run: exercise (touches files)

Run it. Read what the traveller says of the lie, what it says of the raise, how the tour ends and what the exit code is, then compare with what each of the two promises gave alone in section 3. Section 7 says why I cannot tell you: it is a possible defect in the promise judge, which I reported and built nothing on, and I left it unfixed on purpose. When you can say what the court answers here, you will know the question that section 7 hands to the Testoor plane.

Chapter 22 is *Compared, honestly*. Its principle is this: a comparison is worth nothing until the other side's version and the date are on the page, the other side has been run, and the loss is printed beside the win.
