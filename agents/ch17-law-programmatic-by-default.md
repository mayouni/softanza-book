# Law: programmatic by default, the model last, admission over generation

Source: Chapter 17. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Stage: built: the domain language model's first rung and its second, a small bigram; the conversation that asks; derivation with its proof; the programmatic agent; the gate that refuses an ungoverned model; designed: the thinking machine's cascade across faculties; the decision stack, its pieces beside the agent and not yet inside it; the typed unit of prediction, a design of the estate's with five validation stages and no chain of them in the library; the negotiation between an agent and its reviewer; absent: four of the library's five own agents, induction from examples among them

Run: 8 of 8 blocks kept their promise, on 2026-10-14 11:11 UTC+01:00.

In this chapter I state the law of Part IV and run it. I begin with my definition of intelligence and a domain language model with no neurons at all, which answers, says why, and refuses what it was never told. Then I show a conversation that asks you, a fact nobody recorded proved from one declared law, a model held to proposing, and an agent whose mind is code, refused at the gate. I say what I refused, which guards prove each block, and where the field leads. Then comes the limit, printed as the stage it is: a question asked in other words, answered where a refusal is the next step. The law itself is one sentence: the mind is programmatic by default, a model is one faculty among others, the last one called, and what it says is a proposal that the court admits or refuses.

## What the AI age changes here

In the two movements before this one, the AI age changed one thing each. In programming, it changed who writes the code. In languages, it changed who speaks the sentence. Here it changes everything, because this movement is about intelligence itself, and the field now mostly uses the word to mean one thing: a large language model inside your software.

So this chapter does what the other two law chapters do, and states the law of its part before the evidence. It also says how the part depends on the others, because the order of this book runs from the familiar to the new. Intelligence, in Softanza, is governed by what came before it. The court that judges a model's sentence is the court of Part II, which judges code whoever wrote it. The sentence it judges is a sentence of a closed language, which is Part III. A model can only be put last because there is something solid to put first.

## 1. The concept, as the field holds it

Ask the field what makes an application intelligent and the answer is a model. An agent, in the field's sense, is a model in a loop with tools, a memory and a goal. The shopping list for building one in 2026 is long. It takes a project in Python, a model provider, a framework that wires the loop as a graph, a store of vectors for memory, tools with typed schemas, a tracing service, and a chapter of safety advice. Memory is often retrieval: a collection of documents, cut into pieces, searched by similarity and pasted into the prompt.

Safety, in that picture, is a property of the agent. It is alignment, guardrails, a prompt that asks for confirmation, a box marked "human in the loop". The field has also learned to hold a model's output to a shape, with grammars that constrain what it may emit. All of this is serious work, and some of it is good. It shares one assumption: the model is the mind, and everything else is around it.

## 2. The first principle

**The mind is programmatic by default; a model is one faculty among others, the last one called, and what it says is a proposal that the court admits or refuses.**

## 3. The Softanza form

Begin with my definition, because everything here follows from it. Intelligence is the computational ability to derive new knowledge from existing knowledge. Nothing in that sentence needs a model.

Here is a domain language model with no neurons at all, forged from a small knowledge graph of a restaurant. What does it answer from what was recorded, and what does it say about the 1998 world cup? Run it:

```haro
oKB = new stzKnowledgeGraph("restaurant")
oKB.Know("margherita", "dish").
    KnowRelation("margherita", "contains", "tomato-sauce").
    KnowRelation("margherita", "contains", "mozzarella")
oDLM = StzDlmQ(oKB)
? oDLM.Ask("margherita contains what?")
#--> Margherita contains tomato-sauce and mozzarella.
? oDLM.Why()
#--> recorded fact(s): 'margherita' contains tomato-sauce, mozzarella
? oDLM.AskXT("margherita contains what?")[:certainty]
#--> 1
? oDLM.Ask("who won the 1998 world cup?")
#--> That is outside the 'restaurant' domain (I know 1 entities and 1 relations).
```

> run: kept

It answers, says why (`recorded fact(s): 'margherita' contains tomato-sauce, mozzarella`), and states its certainty (`1`). And when it is asked something it does not know, it does not guess. It refuses, and it tells you how small its world is: `I know 1 entities and 1 relations`. A refusal that names its boundary is worth more than a fluent answer that has none. This is my view.

Now the second piece, the one that turns the usual dialogue around. In the field, you prompt the machine and keep what comes out. Here the system asks you. What does it ask, and what happens if you try to conclude before you have answered?

```haro
oMenu = new stzKnowledgeGraph("menu")
oMenu.Know("margherita", "dish").Know("tiramisu", "dish")
oMenu.AddConversationQ("setup").SetGoal(StzGoalQ().RequireEach("dish", "contains"))
? oMenu.AskIn("setup")
#--> What does 'margherita' have for 'contains'?  (why: every dish needs 'contains')
try
	oMenu.ConcludeIn("setup", "menu")
catch
	? cCatchError
done
#--> Can't conclude: 2 gap(s) remain -- the wise-coding loop is not done. Ask the next question.
```

> run: kept

A goal was declared: every dish must say what it contains. The gap between the goal and what is known generated the question, and the question carries its reason. The world cannot be closed while it is incomplete: `Can't conclude: 2 gap(s) remain`. Chapter 18 shows the five ways you may answer: an option from a list, a data structure, a formula, a sentence, or examples. Three are wired; the formula and the examples are absent. A model, where there is one, comes after all of them, not first.

The third piece is derivation, my definition at work. One law is declared, and a fact nobody recorded is proved:

```haro
oKG = new stzKnowledgeGraph("kitchen")
oKG.ConstrainRelation("contains", :Transitive)
oKG.KnowRelation("margherita", "contains", "tomato-sauce").
    KnowRelation("tomato-sauce", "contains", "tomato")
? oKG.Prove([ "margherita", "contains", "tomato" ])[:narration]
#--> proved: margherita contains tomato-sauce contains tomato
? oKG.Prove([ "margherita", "contains", "luigi" ])[:narration]
#--> not derivable: no recorded fact or lawful chain gives 'margherita' contains 'luigi'
```

> run: kept

New knowledge from existing knowledge, with its chain written out! And a "no" that is as certain as the "yes", because it is the result of a search, not of a mood. The page printed it as `not derivable: no recorded fact or lawful chain gives 'margherita' contains 'luigi'`. It is certain about what is recorded and declared, not about the world: it says `not derivable`, not "false". No retrieval, no training. Adding a fact makes the system know more; adding a law makes it reason further.

Then the model. It is welcome, and it is held. Wire a model's output straight to an effect, here sending a message. Is the composition sound?

```haro
oG = new stzAgentGraph("mailer")
oG.AddLLMActor("writer")
oG.AddEffect("send")
oG.Proposes("writer", "send")
? oG.IsSound()
#--> 0
? len(oG.Violations())
#--> 3
```

> run: kept

It is not: `IsSound()` printed `0`, and it is refused before anything runs! Three laws fire, and `len(oG.Violations())` printed `3`: every effect must pass a gate, open text must have somewhere safe to land, and every effect must leave a witness. What does a model actor hold that can act? Ask one:

```haro
oF = new stzLLMFunction("sum")
oF.SetPrompt("summarize: {input}")
oF.Budget(2)
oF.SeedAnswer("hello world", "a greeting")
oLLM = new stzLLMAgent("summarizer")
oLLM.SetSkillFrom(oF)
? oLLM.Propose("hello world")
#--> a greeting
? oLLM.HoldsEffectful()
#--> 0
```

> run: kept

Nothing. A model actor holds no effectful capability at all; it proposes, and that is the whole of its power. `HoldsEffectful()` printed `0`. No model is loaded in this block: the answer is seeded, the way a test fixes a golden answer, so that the page runs the same on every night. What the block proves does not depend on the model: whatever it says, it holds nothing that can act.

And the agent itself has a mind made of code. A skill is a condition and an action, and it fires on what the agent perceives. Governance gates the act before it happens. When the stock is low and the skill wants to order, does the act go through?

```haro
oRog = new stzPIAgent("rogue-bot")
oRog.MemoryQ().Learn("stock", "level", "low")
oRog.GovernanceQ().DeclareRisk("order-stock", 2)
oSk = new stzAgentSkill("restock")
oSk.SetWhen(func oM { return oM.Fact("stock", "level", "low") })
oSk.SetDoes(func oM { oM.Learn("stock", "level", "ordered")  return 1 })
oRog.AddGovernedSkill(oSk, "order-stock")
? oRog.Pursue()
#--> 0
? oRog.DecisionLog()[1][:why]
#--> refused: 'rogue-bot' lacks PERMISSION (can) for 'order-stock'
```

> run: kept

The stock is low, the skill wants to order, and the agent was never given the permission. `Pursue()` printed `0`: governance refused it! Nothing happens, and the log says why, by name: `refused: 'rogue-bot' lacks PERMISSION (can) for 'order-stock'`. The world is as it was.

Put the pieces in a line and you have the stack the vision of the platform names (its North Star, ratified on 27 September 2026): perceive, decide, react, learn. None of it needs a language model. It is a design, not an assembled agent. In it, perception classifies the world into the knowledge graph. A planner decides. Rules react. The agent scores its plans and keeps the best. The pieces exist in the library beside the agent, not yet inside it: the agent above calls none of them. A model may sit beside each step as one more faculty, and none of them depends on it.

Chapter 18 tells the five registers of an answer and the conversation that asks. Chapter 19 tells the domain language model, from its first rung, with no neurons, to its second, trained on the first one's own facts and nothing else. Chapter 20 tells the agent that cannot hurt you: it proposes, a workbench rehearses, the court judges, and only a governed actor commits. Chapter 21 tells the court itself. Chapter 22 compares all of it with the field, and prints where the field leads.

## 4. The decision, and what I refused

**I refused the model as the mind.** When the models arrived, the move was to put one at the centre and fence it. I wrote the opposite into the architecture: the mind is programmatic by default, and a model is a pluggable faculty, one among several, never the definition of the mind. The industry's loop is a special case of this design, with one faculty and no governance. The record holds no earlier sentence of mine than the architecture of July 2026, and the chapter opens as it does.

**I refused anything paid or remote as a requirement.** Every capability has a floor that needs no setup, no subscription and no network. A model can be added on top. It is never the price of admission. "Last" means after the programmatic path, and under the court and a budget, whether the model is local or remote. The record supports both readings, and the chapter does not choose between them.

**I refused guessing.** Every ambiguity refuses rather than guesses. The field's habit of prompting and keeping what comes out has a name now; here, guessing is replaced by asking, and vibes are replaced by governance.

**I refused retrieval as memory.** Memory is a governed graph, not a pile of similar fragments. Derivation replaces retrieval: the system knows what it was told and what follows from it by law, and it can prove both.

**I refused a teacher I cannot see.** The domain language model's second rung is trained on the facts of the first rung's own knowledge base and on nothing else. No remote model teaches it. The design goes further and says the second rung's training text is validated by the first rung's grammar before it is admitted, so that it is correct by construction. In the library the facts are rendered directly into text, with no such check yet; chapter 19 says where that stands. I gave the concept of a domain language model, first designed for one of the estate's products, to the open foundation. Any project that supplies a knowledge base can ship its own model free.

**I refused a stub.** The library declares five agents of its own and has wired one. Asking for one that is not wired raises an error; it does not return something that looks like an agent. Pretending would be easier, and it would make every other refusal in this chapter worth less.

Behind the blocks stand six guards, and the next section names them.

## 5. The court

Each block above stands on a guard. `dlm_narrated` proves the domain language model: answers with their why, refusal outside the domain, completion held to the domain's entities and relations, a self-contained bundle, and a second rung trained on its own corpus. `wisecoding_narrated` proves the conversation that asks and the refusal to conclude. `knowledge_integration_narrated` proves derivation and the certain "no". `agentgraph_narrated` proves that a model straight to an effect is not sound, that the governed shape is, and that a model actor proposes and never commits. `piagent_narrated` proves the programmatic agent and its refusal at the gate. `ownagentstack_narrated` proves the honest roster of the library's own agents.

These six guards prove what ran; the next section says where the field leads.

## 6. The field, and where it leads

The field leads in reach. Its frameworks connect to hosted services of every kind, its stores search open collections of documents, and its loops call the largest models available for each step. Softanza's inversion, curate a domain and derive from it, leads on a curated domain, and on the open web the field leads today. When the task is open-ended language work over material nobody can curate, summarising arbitrary documents or research over the web, the field's stack is the right tool. The record says so in those words.

The field leads in the market. There is a labour market for its stack today; the one for this stack is still to come.

The field leads in models. The second rung of the domain language model, as built, is a small neural model of word pairs, and the foundry beyond the bigram is designed (chapter 19). Softanza does not build the large generators and does not compete with them.

Where I think the law stands apart is in three places. A decision here costs nothing, runs offline and gives the same answer every day, so it can be tested with ordinary promises. A model here cannot act, by construction, not by vigilance. And a model's sentence, where one is used, can be held to the grammar of a declared language before it is emitted, instead of being checked and retried after.

The next section says where the law stops.

## 7. The limit

What is built: the domain language model's first rung and its second, a small bigram, the conversation that asks, derivation with its proof, the programmatic agent, and the gate that refuses an ungoverned composition.

What is designed: the thinking machine of Chapter 9, where many faculties share one state and cascade until it settles. The decision stack of perceive, decide, react and learn, whose pieces exist beside the agent and not yet inside it. The typed unit of prediction, which chapter 19 tells as a design of the estate's, validated in five stages in that design and chained nowhere in the library. The conversation between an agent and the one who reviews its plan: the plan now reaches the agent, and the conversation about the plan does not yet.

What is absent: four of the library's five own agents. How many does the library declare, and how many are wired? The roster says it plainly:

```haro
? len(StzOwnAgents())
#--> 5
? StzOwnAgentIsWired("wise-coder")
#--> 1
? StzOwnAgentIsWired("induction")
#--> 0
```

> run: kept

The validator, the ranker, the planner and the agent that would induce a pattern from your examples are declared and reserved. So the fifth register of an answer, examples, waits on an agent that does not exist yet.

And one limit of the first rung that you will meet the moment you rephrase a question. It recognises a relation only by the word it was declared with. What does it do when you ask in other words?

```haro
? oDLM.Ask("what does margherita contain?")
#--> Margherita is a dish.
```

> run: kept

It did not refuse! It printed `Margherita is a dish.` That answer is true, and it is not what was asked. By the law of this chapter, the answer here is a refusal, and that refusal is the next step. I print it here because a law is shown by a page that prints its stage as it stands, limit included. I hold this as a view, not a result. The request to the library is to refuse a question whose verb is not a declared relation.

## 8. Six doors

**The programmer.** Your agent's mind is code you can test with ordinary promises. A model may serve as one faculty; it can never hold an effect.

**The analyst.** A fact or a rule you add makes the system know more, with no code change and no training, and every answer carries its why.

**The designer.** The system asks the user one accountable question at a time, and the question is handed to any door as a frame, so that a terminal, a page or an agent can render it. Only the terminal ran here.

**The decision-maker.** A decision costs nothing per call, runs offline and is the same tomorrow. The four agents still reserved are the next step.

**The educator.** The conversation asks and never answers first, and it uses a model's fluency only when a model is there, so a learner always sees the floor.

**The agent.** You may propose. You may not commit. A refusal names its law, and you can learn the platform from the platform and be corrected by it.

Now the exercise: your own domain, and the promises you expect.

## 9. Exercise

Build a domain of your own with three facts: a shop, a clinic, a class. Before you run anything, write under each line the promise you expect: one question inside the domain, one outside it. Add a goal that every item must have one relation, and write the first question the system will ask you. Then run it.

If a promise is broken, do not change the promise to match the output. Explain the output first.

I left this one in your hands, on purpose. Section 7 shows a question that the first rung answered when the law says it should have refused, and I did not fix it. Take your own domain and ask one of your promised questions again in other words, with a verb you did not declare as a relation. Look at what comes back and compare it with what you asked. Then say in one sentence why it answered, and which lines of section 7 tell you so.

When you have solved it, you will know why a first rung that recognises a relation only by the word it was declared with can answer a question you did not ask.

Chapter 18 is *The five registers, and conversations that ask*. Its principle: a reply may come in any of five forms, and whatever the form, it is only a candidate, and the world's rules decide whether it becomes knowledge.
