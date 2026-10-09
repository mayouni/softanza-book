# Many minds on one body of work

Source: Chapter 32. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the protocol, its memos and its ledger of rulings; three hooks that refuse wholesale staging and a flooded machine; the instrument that measures composed stamps; the library's fourteen house rules over a code graph; designed: a watcher that wakes a session when a file arrives, in place of the clocks; a court of style for the code a programmer or an agent writes; absent: token figures in the cost record; any team outside this estate that has tried the protocol; a check of a word in the reader's own language

Run: 3 of 3 blocks kept their promise, on 2026-10-09 03:27 UTC+01:00.

## 1. The concept, as the field holds it

When the field speaks of many agents working on one body of code, it usually means a framework. A program holds several agents, a supervisor routes messages between them, and the coordination is a feature of that program. Microsoft's AutoGen, CrewAI and LangChain's LangGraph are the names you will meet, all from the last three years.

When the field speaks of the rules those agents follow, it means a file the agent reads when it starts, a page of instructions in the repository. And when it speaks of many writers on one repository, it means what teams have always used: branches, review, hooks that run before a commit, a list of who owns which folder. These are good tools, and I use them every day.

## 2. The first principle

The one sentence this part of the record returns to was written by one of the sessions, and I keep it because it is right: **every law cites the incident that earned it; a law without a dated failure behind it is a preference.**

## 3. The Softanza form

Softanza was not written by one hand for long. For the last two years, most of its new code has been written by sessions of a model, many at a time, on one machine, in some twenty repositories that depend on each other. I rule; they propose, build, measure and report. The record calls me the Principal. In this chapter I will simply say I.

There is no framework here. No supervisor, no broker, no graph of agents. The arrangement is files and a version history. One repository, the central one, holds the protocol: how a session reports, how it asks, how it closes. Each repository has a mailbox. Each session writes its messages in one fixed form, eight keys in a fixed order, which you have already met if you read the memos at the end of each phase of this book: by whom, about what, why, what was done, the state of named things, what is waiting and on whom, what comes next, and one line of judgement. Every message is also appended to a dated file, so that the day's reasoning is never only in a chat window that closes.

What makes it a discipline and not a filing system is that each rule was paid for.

**Stage by explicit path.** Several sessions write in the same repository at the same time. Twice, a session added every changed file to its commit at once, and swept in another session's work: once it destroyed an edit outright, once it pushed half of a colleague's move between two repositories. Nothing was lost the second time, and the record says that was luck, not method. So now a hook refuses the command before it runs. It was tested on twenty forms of the command, and eighteen behaved as written; the two that did not were repaired the same day. The session that created this book's repository met that hook on its very first commit, and was told why, in those words, before it could do any harm.

**Read the time from the clock, never compose it.** A session writes a time on every message. Sessions, it turns out, invent times: they write a time that feels right after the last one. Nobody notices until a made-up time crosses midnight and a message is filed under the wrong day. When the central session measured itself, five of its twenty-five stamps had been composed, the worst by forty-two minutes, and four of the five were older than the law that forbade them. Across the other desks, thirty-four of a hundred and fifty-one stamps were composed, on thirteen of the seventeen desks measured. The rows behind that figure are published, because the first time it was published the rows had been thrown away and the number could not be defended three hours later. Five weeks after the law, the central session composed a stamp again. Four written warnings had not stopped it; a peer reading a file did. The note it left is the best sentence in the protocol: a reminder is not a mechanism.

**Words name states, never people.** A session once reported my working tree as "dirty". Work that is not yet committed is not dirty, and very often it contains no error at all; and a word that judges the work judges the one who made it. So the record keeps a table of words the estate does not use, with the word it uses instead.

**What no counter can see.** The sound plane of the library held six hundred and twenty-two passing assertions across nineteen guards while it was, to any listener, broken. I heard four defects that no counter reported: a voice too quick to understand, a sentence cut before its end. The law that came out of it says that a thing nobody has perceived is in a state, not in failure: unperceived is a state, and the page must say so. That law is why every chapter of this book carries the line "not yet read by the author" until I have read it.

**The loop is seconds, not minutes.** I stopped two sessions over the same eight-minute test run. It was measured: six seconds of the eight minutes were coverage, the rest were three sweeps that tested nothing new. It was rewritten to twenty seconds. I had written, in my own words, that it "takes a lot of time and should be rethinked". The law was written by a session; the sentence was mine.

**Never ask without saying how.** A session once asked me to check whether a figure was right, and gave me no way to check it. I answered: please never demand a thing without telling me how to get it. Now every request addressed to a person carries the exact command, the exact path, the exact line to read.

You can see the shape. A failure, dated. A rule, written where the next session will read it. Then, when the rule is broken anyway, a mechanism. Some laws reached the last step, some are still a written rule, and the record says which.

Where the laws touch code, the library itself can hold them. Its house rules are validators that run over a graph of the code, the sixth law of the intelligence architecture made runnable: rules an agent can run before it commits, not folklore it must guess. One of them is about words:

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

Read the last line twice. The code is still clean. The tone rule warns; it does not refuse. A word rule advises, and the record says so in its own doctrine: the word law is ruled rather than checked. Here is the remedy the message proposes:

```haro
cCode = "class Shop" + nl + "def RemoveOrder()" + nl + "  return" + nl
? len( StzCheckCode(cCode) )
#--> 0
```

> run: kept

And the rules are a closed set, which an agent can list before it writes:

```haro
? len( StzCodeRuleNames() )
#--> 14
? StzCodeRuleNames()[3]
#--> no-aggressive-verbs
```

> run: kept

That tone rule entered the library in July 2026, five weeks before the estate ruled on its own words. The record does not link the two, so I will not either. But it is the same instinct at two altitudes: the words we use about work are part of the work.

## 4. The decision, and what I refused

**I refused a framework.** The arrangement is files, a history and a few hooks. A supervisor that schedules agents would be one more program to trust, and one more thing that decides without a record. Here, a session that is not running leaves only its files, and the files are the truth.

**I refused to let a coordinator grade its legislator.** Authority runs down from me; correction runs up from any session to the central one, and from the central one to me. A coordinator that judged its own rules would be the one part of the system nothing could fix.

**I refused to automate to the maximum.** From the middle of August 2026, sessions were opened by clocks. On 27 August I stopped them. The record keeps my reason as written then: the routines consumed quota without added value. And it keeps the uncomfortable part: that judgement was the only measurement anybody had, because the cost line every session writes at its close carries no token count. The harness does not tell a session what it spent. Of the three hundred and eighty cost lines written so far, one carries a number. [AUTHOR: What did the clocks cost you, in your own words, when you stopped them on 27 August 2026?] Since then, a timer may run a script, never a model; a session starts when a file arrives in a watched folder, or when I start it.

**I refused to rule in my absence.** A ruling is written in the record only while I am there. When I asked the central session to settle what was pending on my behalf, on 28 September, the five rulings it took that day are marked as taken on my delegation, so that nobody later mistakes them for mine. The decisions at the front of this book are marked the same way.

**I refused to let the protocol become a product.** The doctrine of the harness is open, and it is never to be sold: its value is in what it refuses. It has also been proved in one place only, one person, one machine, one filesystem, about fifteen sessions. It has no adopter outside this estate.

**And I accepted a loss.** The code of the last two years was largely written by sessions, and my hand, which was the style, thinned where they wrote. A study of the record measured it: the promise under each line, the house's way of writing an example, stands at nearly a hundred per thousand lines in the short recipes and at seventy-five in my articles, and at under one in the guards the sessions wrote, which assert in another form. The sessions even took the name of my articles for their test files, a name that a model proposed. I accept the implementation code they wrote. I do not accept that the style a programmer or an agent writes with Softanza should be theirs rather than the house's. That is why the law of Part II exists, and why this book is written in my voice, with sessions as researchers and as the court, and why every chapter waits for my reading before it loses the word draft.

## 5. The court

No guard of the library proves the protocol. Its courts are outside the library, and I name them by what they do: a hook that refuses wholesale staging; a hook that refuses work when the machine has no memory to spare; a check that the hooks installed are the hooks written; an instrument that compares every stamp with its commit and publishes the rows. They are scripts, not Haro, and this book's reader cannot count their assertions, so they are named here and not in the court line below.

The blocks of this chapter stand on the library's guards of its house rules: `coderule_narrated` proves that a code rule is a rule over the graph, that the house findings come out on a planted fixture in a frozen shape, that the rules number fourteen, and that a definition or a comment is not taken for a call. `codegraph_narrated` proves the graph beneath them, and `coderule_project_narrated` runs the rules over the whole library.

## 6. The field, and where it leads

The field leads in scale and in independence. Its frameworks run on many machines for many teams; this protocol has been proved at one person, one machine, one filesystem, and nobody outside the estate has tried it. Its doctrine says so in its own words: these are laws that survived one estate.

The field leads in accounting. A paid interface reports the tokens of every call. This estate's cost record was built to report them and could not, so the most important economic decision it took was taken by feeling.

The field leads in tooling for many writers. Branches, merge queues and owners of folders handle concurrency at a scale the estate has not met; here, the answer is a discipline and one hook, and the hook reads the text of a command, so it also refuses a commit message that merely quotes the forbidden form. That cost is known and accepted.

Where I think the record stands apart is in one habit: each law carries the failure that paid for it, and the record publishes its own rate of breaking its own law. The central desk broke the stamp law more often than the estate it measured, and that number is printed beside the estate's.

## 7. The limit

What is built: the protocol and its files, the dated memos, the ledger of rulings, three hooks that run in every session on this machine, the instrument that measures stamps, and the library's fourteen house rules over its code graph.

What is designed: a watcher that wakes a session when a file arrives, which is the right replacement for the clocks and is not written; a court of style for the code that a programmer or an agent writes with the library, so that the house style is held by a machine and not by a hope.

What is absent: a token figure in the cost record; any team outside this estate that has used the protocol; and a check that a word reads well in the reader's own language, which the word law asks for and nothing performs. The study that read the record named one more limit, and I leave it here in its words: the protocol that makes the record trustworthy also costs energy the product needs, and I should watch the ratio. [AUTHOR: Do you have a reading of the ratio between the work on the protocol and the work on the product? The record holds none.]

## 8. Six doors

**The programmer.** Stage by explicit path, read a file again before you write it, read the time from the clock. Each rule cost someone an edit.

**The analyst.** The record is data you can query, and it publishes its own error rates beside its rules.

**The designer.** A word names a state, never a person. A message is a closed structure a reader scans in one glance, tested on a reader whose first language is not English.

**The decision-maker.** A ruling is written only in your presence. When no figure can answer a question, decide by judgement and write down that it was judgement.

**The educator.** Teach a rule with the failure that earned it. A rule whose cost you cannot name is a rule you will talk yourself out of at two in the morning.

**The agent.** You are a worker with a record. You write a memo, a cost line and a conclusion; the hooks refuse what has hurt others; your stamps are compared with your commits. None of it assumes you are careless. All of it assumes you are many.

## 9. Exercise

Take the last ten messages, notes or log lines in which you wrote a time by hand. For each, find the moment the system recorded on its own: the commit, the time the message was sent, the time the file was saved. Before you look, write down how many of your times you expect to be later than the system's by a minute or more. Then count.

Your count is the finding. I will not give you mine.
