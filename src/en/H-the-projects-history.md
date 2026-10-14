---
id: the-projects-history
appendix: H
number: 108
title: "The project's history: from Ring to Haro"
status: draft
---

This is the one page of the book that names the language Softanza grew up on. The chapters do not, because the platform is going where that language cannot follow. The history belongs here, told once, with thanks.

## Where it began

Softanza was born on Ring, a small scripting language. I wrote its library in Ring for years. I taught Ring, I promoted it in the field, and I spent nine months writing its book, *Beginning Ring Programming*, published by Apress in 2020. In 2021 I described the library to the Ring community for the first time. In 2022 the first presentation of Softanza called it "a best friend of existing Ring programmers". Ring's simplicity and its multiparadigm expressiveness are two things Softanza keeps, because they were never the problem.

## What real projects taught

Three things, and they are the reasons.

**The limits showed.** Real projects showed that Ring was not suited to the challenges of modern applications. The limits are in three places: performance, strong typing and ease of build. The project's own sessions measured them.

**The direction could not be influenced.** The direction of a language belongs to its owner, and ours could not be influenced. The project built Ring++ to solve those three pains without leaving Ring, and it did not meet the reception we hoped for.

**Governance is a design property.** A dependency whose direction you cannot influence, and whose behaviour you cannot fence, fails the due diligence that regulated domains require. Softanza's answer is not independence for its own sake, but independence for its users: an engine written in Zig with no third-party dependency, a virtual machine and a compiler of our own, and commitments the project already runs as tests. An open core. Charters ratified in public. Every decision in a dated record. Every claim linked to its proof.

## The path

Ring is where it began. Ring++ is the bridge, in construction. Haro is the destination. Under all three sits the engine in Zig, which does the computation once.

Today the library still runs on its first runtime, version 1.27, and the blocks of this book run on it. Haro uses the syntax of that first runtime as its first facet, so all the code already written keeps working. The library's narrated tests are the test of that promise: Haro has to run them. Chapter 27 tells where the engine stands, with numbers.

## Thanks

Softanza says thank you to the language it grew up on, and goes where its users' sovereignty requires.
