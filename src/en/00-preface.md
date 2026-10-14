---
id: preface
part: 0
number: 0
title: Preface
spine: true
narrations: []
guards: []
status: draft
rulings: []
---

## A question you already have

You use a tool that writes code. You ask it for a function, or for a whole feature, and it answers in seconds. Then comes the question that no tool answers for you: should this code enter my system?

You have always had ways to answer. You run the tests. The type checker agrees, or it does not. A colleague reads the change. Those ways were made when people wrote code slowly. Now one sentence can produce a thousand lines, and nobody has time to read a thousand lines for every sentence.

Code has become cheap. Trust has not become cheap. This book keeps coming back to one sentence, the one every chapter rests on: **change arrives faster than trust.**

## The idea, in two moves

First you **declare**. In plain text, you say what a thing is: an application (I call it a *world*), a language, an AI agent, a whole product. Then you **govern**. From your declaration you get a judge, which I call a *court*. A court is a validator built from your declaration. It gives a verdict, *kept* or *refused*, and the reason, in the words of your declaration.

Every change goes to the court before it enters, whoever wrote it: you, a colleague, a script or an AI model. The model can still propose anything. It cannot decide anything. It is also asked last: whatever rules can decide, the rules decide first.

## A declaration, in real code

Here is the smallest case. You add an AI agent to your system, a program that watches stock levels and reorders. You do not start with its code. You start with a short text file that says what it is: its name, how often it runs, what it may do, and whether its actions can be undone. That file is a declaration. You load it, and the court reads it before the agent can ever run. This agent's file leaves something out. What does the court say?

```haro
cPia = "pia: 1
name: stock-watcher
kind: pi
reversibility: compensable
schedule:
  timer: 20
skills:
  - name: restock
    does: learn stock level ordered
"
oD = StzAgentDeclarationQ(cPia)
? oD.IsValid()
#--> 0
? oD.CiteFindings()
#--> [pia-coverage @ coverage] an agent must say WHAT IT COVERS. The engine loop refuses to schedule an agent with no coverage statement (law 18), so a file without one could never run and is refused here instead of at the first tick.
```

Read it in three parts. The text between the quotes is the declaration. The next line loads it. Then `?` prints an answer, and the line after `#-->` is what the block printed when I ran it. The court answers `0`: refused. It names the rule and gives the reason: an agent must say what it covers, because the engine will not schedule an agent that does not, so the file is refused now and not at its first run. A few words of the file: `pia` names the file format, `compensable` means its effects can be undone by a compensating action, and law 18 is the engine's rule that an agent with no coverage is never scheduled.

You could write this check in your own CI. Here nobody had to. The court for agents ships with the library, so the rule is the library's, and the facts are yours, in the declaration. A one-off assert in a start-up script judges one fact. A declaration holds all the facts about the agent in one text, and the same court judges it whether a person, a script or a model wrote it. The rule can be yours too: chapter 2 has a rule you write in a few lines over two facts, that an actor is a language model and that it holds an effect, and the court finds the violation in your own graph of agents. This example is small on purpose, and a schema can check it too. The book does not argue that a court checks more than a schema. It argues that one court, built from your declaration, stands in front of every actor and gives its reason. It does not read a thousand generated lines and call them good: it checks that a change fits what you declared, and chapter 24 shows a change tried out on a copy of your system before anything is committed. For a thing of your own, such as a language you invent, chapter 12 shows how you make the court, and says how far that is built. Chapter 1 tells a second scene, with a mail service, and chapter 2 runs this block again.

You will say that you already have tests, schemas and policy checks in your CI. You do. Today those rules live in many places: tests here, a schema there, a policy file elsewhere, each written by hand after the code. Here you state them once, in the declaration, and the court comes from it. Chapter 22 compares the two honestly, and where the field does better, it says so. A court judges what you declared. It cannot judge what you left out, and each chapter's limit says where that stops.

## What Softanza is

Three things, and for each I say how far it exists.

- A **library** that you call from code. Today that code is Ring, a small scripting language: you write a few lines like the ones above, and you run them with the library loaded. The library holds the declarations and the courts made from them. Its source is at github.com/mayouni/stzlib, and every block of code in this book ran against a named commit of it. If your work is in Python or TypeScript, today you would use the library beside your code, not inside it: through one governed door it can run code in Python, NodeJS (JavaScript), R, Julia, Prolog and C, and chapter 16 shows how.
- An **engine** beneath the library, written in Zig, a systems language. It does the actual computation, on text, lists and tables, once and in one place, so that every language that talks to it gets the same behaviour. It runs today.
- A **language**, Haro, meant to hold the declarations. It is meant to read the code already written for Ring, so nothing written so far is lost. It is still being built: it has a charter and a first experiment, and no executable yet.

Chapter 4 draws the three in one picture.

## Where it stands

Three projects, a restaurant, a bank and an organisation, shaped the library. None of them runs on the engine yet. So this book owes you one thing it does not have: a whole solution that ran on Softanza's own engine, and a named person who said what they saw. Chapter 33 is about that gap. I would rather you heard it from me now.

## What this book is

This is a book of arguments, with running code. For each question about programming, about languages and about intelligence, I do four things. I give the answer the field usually gives. I give the answer Softanza takes. I give the decision I made, and what I refused. And I give the proof: the code ran, and the tests that prove it are named. I also say where Softanza is weaker than what the field already does well.

It has seven parts and thirty-three chapters. You do not need to know Softanza, Ring or Zig. You need to have written code, and to have felt the doubt above. The project's website holds its evidence, with the proofs, and its course teaches the same ground by exercises. This book holds the argument.

Each chapter ends with six short doors. A door is a way in for one kind of reader: the programmer, the analyst, the designer, the decision-maker, the educator and the agent. The agent is an AI program, because the book is also published as data that a program can read. Enter by the door that is yours today.

## How to read it

Read nine chapters first. They carry the whole argument and can be read alone: the four of Part I, the last two, and three that each state a rule the book holds everywhere. Chapter 5: the code should read the way a person thinks. Chapter 11: a language is declared and closed. Chapter 17: a program is programmatic by default, which means rules and code decide first, and the model comes last. The reader has a button that shows only these nine. Come back to the others when one of them interests you.

Every chapter has the same nine parts, in the same order. The idea as the field holds it today. The first principle. The form it takes in Softanza, in code. The decision, and what I refused. The court: the named tests that prove the chapter's claim. The field, and what it does better. The limit. The six doors. An exercise, which you answer before you run it. Chapters 5, 11 and 17 open with one more short section, on what the AI age changes.

## What to trust

Every block of code in this book was run inside the library. Under each title the page says when, at which commit, and how many blocks kept their promise: how many printed what the line after `#-->` says they print. If a block prints something else, the build fails, and so does the page. The exercises are yours to run.

When a chapter says what is not finished, it uses three words and no others. *Built*: the code exists, a test exists, and a block ran. *Designed*: a document says so, and nothing runs. *Absent*: I looked and found nothing, and I say how far I looked. The project's website uses five names for the same things, and chapter 3 shows how they map to these three.

One more honest note. Haro does not run the library yet, so the blocks marked `haro` run on Ring, the older language, version 1.27. Each page says so.

## About this draft

The chapters were drafted with AI agents working from the project's own files, and every code block was run. I have not read every page yet, and each chapter has a banner at its top that says so until I do. Where the files held no answer to a question, the page says so in one plain sentence and does not invent one. The French edition is a translation of the English drafts, and each French page says so. This preface was written after the chapters, and it stays unfinished until I write my own. This is the second book of my imprint, AYOUNI. The first, *Refinement-Oriented Programming*, is about one discipline for software in the age of AI agents, told through one bank.
