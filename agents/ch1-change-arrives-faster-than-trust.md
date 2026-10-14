# Change arrives faster than trust

Source: Chapter 1. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the court that admits or refuses a change, for a person and for a machine; absent: a customer platform running on the Softanza engine

Run: 2 of 2 blocks kept their promise, on 2026-10-14 22:24 UTC+01:00.

## 1. The concept, as the field holds it

Ask the industry what changed in programming these last years and you will get one answer, said with excitement or with dread: *machines write the code now.*

The picture is familiar. An AI model proposes a function, a file, a whole application. A person reviews it, or does not. Tools are added around the model to make it safer: linters that read what it wrote, tests it generates for itself, guardrails that catch the worst of it, a second model that judges the first. The model is at the centre. Everything else is a fence built around it after the fact.

I do not think that picture is wrong about the facts. It is wrong about where to stand.

## 2. The first principle

Here is the sentence I keep coming back to, and it is the oldest sentence in this book: **change arrives faster than trust.**

Code has become cheap. A thousand lines cost a sentence. What has not become cheap, what has in fact become the scarcest thing in software, is the trust that those lines do what their author, human or machine, says they do. Every team I have met in the last two years has more code than it can review and less confidence than it had before. The bottleneck of our age is not writing. It is admission: deciding what may enter a system and stay there.

So the question Softanza asks is not *how do we generate better?* It is *how do we admit?* Who judges a change, by what law, before it runs, and what is written down about the verdict so that someone can read it later and be answerable for it.

When you put admission at the centre, the picture turns around. The court is in the middle. The model is one proposer among others, and it comes last, after the person, after the data, after the formula, after the plain sentence. Nothing it says enters the world until the court has read it. That is not a fence built around a generator. It is a different building.

## 3. The Softanza form

Let me show you rather than tell you, by example, which is how I have always preferred to teach.

A solution declares that it depends on a mail service. While I program, I bind that dependency to a sandbox: an object that captures every message and sends nothing, so my tests can read what *would* have gone out. Free, offline, deterministic. Then I move the solution to production, with the sandbox still bound, the way people do at two in the morning before a demo.

```haro
oReg = new stzServiceRegistry("my-solution")
oReg.Bind(:mail, new stzMailSandbox())
oReg.SetPhase(:emulated)
? oReg.IsSound()
#--> 1
oReg.SetPhase(:production)
? oReg.IsSound()
#--> 0
? oReg.Findings()[1][:message]
#--> still bound to a SANDBOX in a production phase -- a fake must never ship
```

> run: kept

The registry does not call it sound. In the emulated phase it answers one; in production it answers zero, and the next line says why: a fake must never ship. The fake is refused by name, and a service that was declared and never bound raises the moment it is asked for, instead of silently doing nothing. I did not remember to check this. The phase decided what comes back, and the check is enforced, not remembered.

That is the whole philosophy in one small scene. Expression is free: bind what you like, while you like. Admission is governed: the gate reads the phase and the binding, and refuses.

Now a second scene, because the first one has no AI model in it and you are waiting for the model.

Take a restaurant as the illustration: an AI agent that knows its world proposes to place an order. In Softanza the agent does not place it. It proposes a plan. A workbench rehearses the plan on a twin of the system, a copy that holds no reference to the real one, and records every operation it would perform. A court reads the rehearsal against the rules the restaurant declared: who may order, what may be ordered, what a supplier must confirm. Only then does a governed actor commit, and the commit is recorded with its actor and its outcome. The guard that proves this sequence, `safeworld_narrated`, rehearses in a twin of the files, plans, and lets an actor commit; it holds seventy-six assertions as I write, none of them about a restaurant, and the site shows a recorded run of the same mechanism.

Notice what the model did and did not do. It proposed. It did not decide, did not write, did not send. It was a proposer beside the registers of answer. Three of them, an option chosen, a data structure given, a sentence spoken, are built today and open to the person before the model is called at all; two more, a formula written and an example shown, are not yet built (Chapter 18). I call this *programmatic by default, the model last*. It is the sentence under every chapter of Part IV.

And a third scene, the smallest, because it shows the same law at the level of a single line. The platform is judged on what its code looks like and what it answers:

```haro
o1 = new stzList([ "tea", "rice", "tea", "fish", "rice", "tea" ])
? @@( o1.FindAll("tea") )
#--> [ 1, 3, 6 ]
? @@( o1.DuplicatesRemoved() )
#--> [ "tea", "rice", "fish" ]
```

> run: kept

The question is spoken as it is thought: find all, remove duplicates. And the two lines under the two questions are not my commentary. They are promises the library kept on the night this chapter was built. If it stops keeping them, this page fails. The same law, admission before trust, applied to a paragraph.

## 4. The decision, and what I refused

Every chapter of this book carries this section, and I promised in the preface that it is the reason the book exists. So let me be concrete about the decisions behind this first chapter, because they were not comfortable.

**I refused to put the AI model at the centre.** When the AI models arrived, that was the obvious move, and I had the pieces to make it: a natural layer, a knowledge graph, an agent class. I could have wired a model into each and shipped a Softanza that "talks". I did not, and I wrote the refusal into the architecture as a law: the mind is programmatic by default, and a model may only propose. I gave up some fashion by that choice. I think I kept the platform.

**I retired the language I was born on.** Softanza was written for years on a small, warm scripting language that I love and that I pleaded with, long before the LLM era, to make executable natural language its first concern. It did not, and that is its right. In 2026 I ruled that the language would not be carried forward: the runtime beneath Softanza is being replaced by one we own, written in Zig, a charter and a spike so far, wearing the old surface so that every line I wrote can keep running, under a new name, **Haro**. The old surface stays because the code is the asset; the old runtime goes because sovereignty over the runtime is one of the commitments I made. That decision was not free. It is in Chapter 27 with its numbers, including the one I did not want: our runtime is slower than the one we measured against, by a factor between one and two, on every row. I recorded the loss in the estate memo of 13 September. A book that hides that is not worth your trust, and neither is a platform.

**I refused to let anything into BASE without a court, and I failed.** The three layers of the library, CORE, BASE and MAX, were meant to keep the foundation small and the innovations above it. Under the pressure of time I let everything go into BASE: ninety-three percent of the code sits there today, and the dependency rule is held at the engine and broken at the inheritance. I say this on the first chapter, not the last, because the discipline I am about to preach for thirty-two chapters is one I have broken, and the study of the record caught me. That is what a court is for, and the court for the layers is still only proposed.

**I refused a second embedding.** When someone asks "what about Python, what about JavaScript, what about my language", the answer is one door, to be governed, and never another host runtime sewn into the platform. The record's seven languages, the host and six runtimes behind one door, were chosen for seven layers of a solution, and Chapter 16 counts them. The door is the answer to "what about language X", and it is one answer, not twenty.

What was refused is as much a part of Softanza as what was built. You will not find the refusals on the site, because the site shows what is. You will find them here, in every chapter, under this heading.

## 5. The court

What proves this chapter? Three things, and I give them to you by name so that you can check them rather than believe me.

The service registry's refusal of a fake in production is a guard, `service_registry_narrated`, in the system plane. The AI agent's propose, rehearse, judge and commit is `safeworld_narrated`, seventy-six assertions, in the agentic plane, beside `governance_crossing_narrated`, in the system plane, for the crossing itself. The code blocks on this page were run by the book's own runner inside the library on the night this page was built, and its output is shown as it came.

Three guards for a chapter of philosophy may seem few. They are the right three, because they are the three places where philosophy meets a verdict.

## 6. The field, and where it leads

I will not pretend the field has nothing. It has, in the last three years, built the most capable code generators in history, and every day I use them. The industry's answer to the trust problem is real work: generated tests, review bots, policy engines, sandboxes for AI agents, structured outputs, a second model to grade the first. Where the field leads, and it leads clearly, is in the generators themselves. Softanza does not build the large generators and does not compete with them; where it trains, it trains small models bound to one domain, whose every answer will be checked by a grammar. The field also leads in scale: its review tools read volumes of generated code that nothing in Softanza has been run against.

Where I believe Softanza stands alone is in the order of things. The field adds admission to a generator. Softanza adds a generator to a court. In the field, an AI model writes in your language and tools check it afterwards; here, the model may only write in a language you declared, whose grammar is closed and whose court is meant to be born with it, so that, for the languages whose grammar is compiled today, an invalid sentence cannot be spoken at all. In the field, the dialogue with a system is a prompt; here, the system asks, and the answer can be an example, a formula or a sentence before it is ever a model. In the field, the record of a decision is a log; here, it is a transcript with a speaker and a certainty, answerable forever.

Those are claims, and each has its chapter and its guard. I list them here so that you know where the argument is going, and so that you can hold me to it.

## 7. The limit

The honest limit of this chapter is also the honest limit of the whole platform, and I put it on the first page on purpose.

Softanza has been used. A bank in Niamey runs an assessment platform whose building shaped Softanza, under licence, attested by the installation guide we delivered. A restaurant in Lyon runs a platform for neighbourhood commerce whose first demo its owner made alone, on his own phone, with a messaging app as his support line. An organisation in Niger has its hub designed. Their lessons are in the code, by file name, in Part VI.

But the customer platforms run today on ordinary stacks. The bank's is a Python application; the restaurant's is a set of single-file web worlds; the organisation's hub is not built. Their declarations are being written as Softanza's own, so that moving them onto the Softanza engine is a change of engine and not of plan. That move is the next step. The court is built, and the platforms exist; the next milestone is the first of them running on the engine. That is the next line this book will carry, and Chapter 33 is about nothing else.

## 8. Six doors

**The programmer.** You will keep your editor and your language. What changes is that every claim you make about your code can carry a promise under it, and a court will read it.

**The analyst.** Your rules become data a person can change, and every change is judged before it lands and recorded after.

**The designer.** The interface is judged too: twenty-two verbs, one hundred and twenty-two rules, and a verifier that refuses what a machine can check.

**The decision-maker.** The question you ask every vendor, "who decides, and what is written down", has a mechanical answer here, and it is the same answer for a person and for a machine.

**The educator.** The tutor asks and never answers first. That is a law of the platform, not a feature of a product.

**The agent.** You are welcome here, and you will be judged. Appendix G is yours.

## 9. Exercise

Take one function an AI model wrote for you this week. Under it, write the line it must print for one input you care about, in the form you have just met:

```haro exercise
? YourFunction(the_input)
#--> the line it must print
```

> run: exercise

Run it. If the line matches, you have your first promise. If it does not, you have your first finding, and you have learned more about that function in a minute than the model's explanation told you. Do not fix it yet. Chapter 2 is about who you are when you do.
