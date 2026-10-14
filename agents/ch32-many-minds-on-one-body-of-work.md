# Many minds on one body of work

Source: Chapter 32. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the protocol, its memos and its ledger of rulings; three hooks: one refuses wholesale staging, one refuses a register edit made on a stale view of its source system, one refuses work on a flooded machine; the instrument that measures composed stamps; the library's fourteen house rules, five of them over a code graph; designed: a watcher that wakes a session when a file arrives, in place of the clocks; a court of style for the code a programmer or an agent writes; absent: token figures in the cost record; any team outside this estate that has tried the protocol; a check of a word in the reader's own language

Run: 3 of 3 blocks kept their promise, on 2026-10-14 01:36 UTC+01:00.

In this chapter I show how Softanza has been written for the last two years: by many sessions of a model on one machine, with no framework, only files, a version history and a few hooks. I walk through the rules the record paid for, one failure at a time, and the library's fourteen house rules that an agent can run before it commits. I say what I refused: a framework, a coordinator that grades its legislator, automation to the maximum, a ruling in my absence, a protocol sold as a product. And I say the loss I accepted: my hand thinned where the sessions wrote. The principle is one of the sessions' own sentences: every law cites the incident that earned it.

## 1. The concept, as the field holds it

When the field speaks of many agents working on one body of code, it usually means a framework. A program holds several agents, a supervisor routes messages between them, and the coordination is a feature of that program. Microsoft's AutoGen, CrewAI and LangChain's LangGraph are the names you will meet, all from the last three years.

When the field speaks of the rules those agents follow, it means a file the agent reads when it starts, a page of instructions in the repository. And when it speaks of many writers on one repository, it means what teams have always used: branches, review, hooks that run before a commit, a list of who owns which folder. These are good tools, and I use them every day.

What I did instead begins with one sentence.

## 2. The first principle

The one sentence this part of the record returns to was written by one of the sessions, and I keep it because it is right: **every law cites the incident that earned it. A new law without a dated failure behind it is a preference, and belongs in a style guide instead.**

## 3. The Softanza form

Softanza was not written by one hand for long. For the last two years, most of its new code has been written by sessions of a model, many at a time, on one machine. That work spans some twenty repositories that depend on each other. I rule; they propose, build, measure and report. The record calls me the Principal. In this chapter I will say I.

There is no framework here. No supervisor, no broker, no graph of agents. The arrangement is files and a version history. One repository, the central one, holds the protocol: how a session reports, how it asks, how it closes. Each repository has a mailbox. Each session writes its messages in one fixed form, eight keys in a fixed order. You have already met it if you read the memos at the end of each phase of this book. The eight keys: by whom, about what, why, what was done, the state of named things, what is waiting and on whom, what comes next, and one line of judgement. Every message is also appended to a dated file, so that the day's reasoning is never only in a chat window that closes.

What makes it a discipline and not a filing system is that each rule was paid for.

**Stage by explicit path.** Several sessions write in the same repository at the same time. Twice, a session added every changed file to its commit at once, and swept in another session's work. Once it destroyed an edit outright, once it pushed half of a colleague's move between two repositories. Nothing was lost the second time, and the record says that was luck, not method. So now a hook refuses the command before it runs. It was tested on twenty forms of the command, and eighteen behaved as written. Of the other two, `git stage -A` was repaired the same day; the other, that the hook also refuses text which only quotes the form, is an accepted cost, met in section 6.

**Read the time from the clock, never compose it.** A session writes a time on every message. Sessions, it turns out, invent times: they write a time that feels right after the last one. Nobody notices until a made-up time crosses midnight and a message is filed under the wrong day. How did the central session fare when it measured itself? Five of its twenty-five stamps had been composed! The worst was out by forty-two minutes, and four of the five were older than the law that forbade them. Across the other desks, thirty-four of a hundred and fifty-one stamps were composed, on thirteen of the seventeen desks measured. The rows behind that figure are published. The first time it was published, the rows had been thrown away, and the number could not be defended three hours later. Five weeks after the law, the central session composed a stamp again. Four written warnings had not stopped it; a peer reading a file did. The note it left is the best sentence in the protocol: a reminder is not a mechanism.

**Words name states, never people.** A session once reported my working tree as "dirty". Work that is not yet committed is not dirty, and often it contains no error at all; and a word that judges the work judges the one who made it. So the record keeps a table of words the estate does not use, with the word it uses instead.

**What no counter can see.** What did the counters say of the sound plane of the library? Six hundred and twenty-two passing assertions across nineteen guards, and yet to any listener it was broken! I heard four defects that no counter reported: a voice too quick to understand, a sentence cut before its end. The law that came out of it says that a thing nobody has perceived is in a state, not in failure: unperceived is a state, and the page must say so. It is the same instinct as the line every chapter of this book carries, "not yet read by the author", until I have read it.

**The loop is seconds, not minutes.** I stopped two sessions over the same eight-minute test run. It was measured: six seconds of the eight minutes were coverage, the rest were three sections re-rendering the world to test one pixel property. It was rewritten to twenty seconds. I had written, in my own words, that it "takes a lot of time and should be rethinked". The law was written by a session; the sentence was mine.

**Never ask without saying how.** A session once asked me to check whether a figure was right, and gave me no way to check it. I answered: please never demand a thing without telling me how to get it. Now every request addressed to a person carries the exact command, the exact path, the exact line to read.

You can see the shape. A failure, dated. A rule, written where the next session will read it. Then, when the rule is broken anyway, a mechanism. Some laws reached the last step, some are still a written rule, and the record says which.

Where the laws touch code, the library itself can hold them. Its fourteen house rules are validators, five of them over a graph of the code and the rest over text, the sixth law of the intelligence architecture made runnable. They are rules an agent can run before it commits, not folklore it must guess. One of them is about words. What does it say of a method called `KillOrder`, and is the code still clean? Run it:

```haro
cCode = "class Shop" + nl + "def KillOrder()" + nl + "  return" + nl
aFindings = StzCheckCode(cCode)
? aFindings[1][:rule]
#--> no-aggressive-verbs
? aFindings[1][:message]
#--> aggressive verb in method 'KillOrder' -- prefer Remove/Delete/Dispose/Clear/Close (Softanza tone)
? StzCodeIsClean(cCode)
#--> 1
```

> run: kept

Read the last line twice. `StzCodeIsClean` still answers `1`: the code is clean! The tone rule warns; it does not refuse. A word rule advises. The estate's doctrine says something close about its own word law: no session can test how a word lands on its reader, so that law is ruled rather than checked. The message says `aggressive verb in method 'KillOrder'` and names the remedy, `prefer Remove/Delete/Dispose/Clear/Close`. What does the rule say once the verb is `Remove`? Run it:

```haro
cCode = "class Shop" + nl + "def RemoveOrder()" + nl + "  return" + nl
? len( StzCheckCode(cCode) )
#--> 0
```

> run: kept

No finding comes back: `0`. Once the verb is `Remove`, the rule has nothing to say.

And the rules are a closed set. How many are there, and can an agent list them before it writes?

```haro
? len( StzCodeRuleNames() )
#--> 14
? StzCodeRuleNames()[3]
#--> no-aggressive-verbs
```

> run: kept

Yes: fourteen names, and the third is the rule that just spoke. The record does not link the library's tone rule to the estate's word law, ruled on 21 August 2026, so I will not either. But it is the same instinct at two altitudes: the words we use about work are part of the work.

Those are the laws. Now for what I refused, and the loss I accepted.

## 4. The decision, and what I refused

**I refused a framework.** The arrangement is files, a history and a few hooks. A supervisor that schedules agents would be one more program to trust, and one more thing that decides without a record. Here, a session that is not running leaves only its files, and the files are the truth.

**I refused to let a coordinator grade its legislator.** Authority runs down from me; correction runs up, and the central session is corrected by the Observer and bound by the doctrine. A coordinator that judged its own rules would be the one part of the system nothing could fix. I hold this as a view, not a result.

**I refused to automate to the maximum.** From the middle of August 2026, sessions were opened by clocks. On 27 August I stopped them. The record keeps my reason as written then: the routines consumed quota without added value. And it keeps the uncomfortable part: that judgement was the only measurement anybody had, because the cost line every session writes at its close carries no token count. The harness does not tell a session what it spent. Of the three hundred and eighty cost lines written so far, one carries a number! What did the clocks cost? It is not in the record: it holds the reason and no figure, and I give none. Since then the ruling is that a timer may run a script, never a model, and every timer is paused for now. The direction is that a session starts when a file arrives in a watched folder, or when I start it; the watcher is not yet written (section 7).

**I refused to rule in my absence.** A ruling is written in the record only while I am there. On 28 September I asked the central session to settle what was pending on my behalf. The five rulings it took that day are marked as taken on my delegation. The mark is there so that nobody later mistakes them for mine. The decisions at the front of this book are marked the same way.

**I refused to let the protocol become a product.** The doctrine of the harness is open, and it is never to be sold: its value is in what it refuses. It has also been proved in one place only, one person, one machine, one filesystem, about fifteen sessions. It has no adopter outside this estate.

**And I accepted a loss.** The code of the last two years was largely written by sessions, and my hand, which was the style, thinned where they wrote. A study of the record measured it. The promise under each line (the `#-->` line) is the house's way of writing an example. It stands at nearly a hundred per thousand lines in the short recipes (the quickers) and at seventy-five in my articles. In the narrated guards the sessions wrote, which assert in another form, it stands at under one. The sessions even took the name of my articles for their test files, a name that a model proposed. I accept the implementation code they wrote. I do not accept that the style a programmer or an agent writes with Softanza should be theirs rather than the house's. That is why the law of Part II exists, and why this book is written in my voice, with sessions as researchers and as the court. And it is why every chapter waits for my reading before it loses the word draft.

Next, the court, and what it cannot prove.

## 5. The court

No guard of the library proves the protocol. Its courts are outside the library, and I name them by what they do. One hook refuses wholesale staging, and one refuses work when the machine has no memory to spare. A check says whether the hooks installed are the hooks written. An instrument compares every stamp with its commit and publishes the rows. They are scripts, not Haro, and this book's reader cannot count their assertions, so they are named here and not in the court line below.

The blocks of this chapter stand on the library's guards of its house rules. `coderule_narrated` proves that a code rule is a rule over the graph, and that the house findings come out on a planted fixture in a frozen shape. It proves that the rules number fourteen, and that a definition or a comment is not taken for a call. `codegraph_narrated` proves the graph beneath them, and `coderule_project_narrated` runs the project rules over a fixture directory.

## 6. The field, and where it leads

The field leads in scale and in independence. Its frameworks run on many machines for many teams; this protocol has been proved at one person, one machine, one filesystem, and nobody outside the estate has tried it. Its doctrine says so in its own words: these are laws that survived one estate.

The field leads in accounting. A paid interface reports the tokens of every call. This estate's cost record was built to report them and could not, so the most important economic decision it took was taken by feeling.

The field leads in tooling for many writers. Branches, merge queues and owners of folders handle concurrency at a scale the estate has not met. Here, the answer is a discipline and one hook. The hook reads the text of a command, so it also refuses a commit message that merely quotes the forbidden form. That cost is known and accepted.

Where I think the record stands apart is in one habit: each law carries the failure that paid for it, and the record publishes its own rate of breaking its own law. The central desk broke the stamp law about as often as the estate it measured, on a different surface: 5 of 25 against 34 of 151. Four of the five came before the law. Both numbers are printed side by side.

Now the limit, in the stage words.

## 7. The limit

What is built: the protocol and its files, the dated memos, the ledger of rulings, three hooks that run in every session on this machine, and the instrument that measures stamps. The library's fourteen house rules are built, five of them over its code graph.

What is designed: a watcher that wakes a session when a file arrives, which, in my view, is the right replacement for the clocks and is not written. And a court of style for the code that a programmer or an agent writes with the library. The house style would then be held by a machine and not by a hope.

What is absent: a token figure in the cost record; any team outside this estate that has used the protocol; and a check that a word reads well in the reader's own language. The word law asks for that check, and nothing performs it. The study that read the record named one more limit. I leave it here in its words, "the author" being me: the protocol that makes the record trustworthy also costs energy the product needs, and the author should watch the ratio. The record holds no reading of that ratio.

## 8. Six doors

**The programmer.** Stage by explicit path, read a file again before you write it, read the time from the clock. Each rule cost someone an edit.

**The analyst.** The record is data you can query, and it publishes its own error rates beside its rules.

**The designer.** A word names a state, never a person. A message is a closed structure a reader scans in one glance, written so that it parses for a reader whose first language is not English.

**The decision-maker.** A ruling is written only in your presence. When no figure can answer a question, decide by judgement and write down that it was judgement.

**The educator.** Teach a rule with the failure that earned it. A rule whose cost you cannot name is a rule you will talk yourself out of at two in the morning.

**The agent.** You are a worker with a record. You write a memo, a cost line and a conclusion; the hooks refuse what has hurt others; your stamps are compared with your commits. None of it assumes you are careless. All of it assumes you are many.

## 9. Exercise

Take the last ten messages, notes or log lines in which you wrote a time by hand. For each, find the moment the system recorded on its own: the commit, the time the message was sent, the time the file was saved. Before you look, write down how many of your times you expect to be later than the system's by a minute or more. Then count.

Your count is the finding. I will not give you mine.

I left this one in your hands. Take the first block of section 3, the one that asks the library to check `KillOrder`, and strip its promises: the block below is that one with no `#-->` line. Before you run it, write under each question the line you expect. Then run it and compare. Section 3 says why the last answer is what it is; whether it is the answer a function with that name should give, I leave to you.

```haro exercise
cCode = "class Shop" + nl + "def KillOrder()" + nl + "  return" + nl
aFindings = StzCheckCode(cCode)
? aFindings[1][:rule]
? aFindings[1][:message]
? StzCodeIsClean(cCode)
```

> run: exercise

When you have settled it, you will know why a word rule advises and does not refuse.

The last chapter is about the one line still owed. Its principle says when that line may be written: the record carries a solution only when it ran on its own engine and a named person said what they saw.
