# The preface, tested on cold readers (2026-10-14)

The author said the preface "may seem readable for you, but this is just because you know the internals of Softanza": for a foreign reader it does not frame the book's mission and subject in simple words based on the mental model most programmers have.
I rewrote it for a programmer who knows Python or TypeScript, tests, CI, schemas and an AI assistant, and tested it on fresh agents with that profile (a native reader and a French-speaking reader at English level B2), who saw only the preface.

| Round | What the readers could not do | Change made |
|---|---|---|
| 0, the old preface | (not run; the author's verdict) opens on the imprint, then "declare, govern, court, world, forge, the former host language" | rewritten |
| 1 | could not say what Softanza is concretely, in which language, or why it beats CI; "world, court, kept, the record, door, a line owed" were private words; the mail scene looked like a config lint | opened on the question every programmer has (AI writes code, should it enter my system?); "change arrives faster than trust"; declare then govern in two moves with the court as "a validator built from your declaration"; "the record", "line owed" removed; Ring and Zig glossed; the CI difference stated |
| 2 | still no way to try it; "a lint rule can catch this too" undercut the pitch; the second reader understood the idea | "Where it stands" added (none of the three projects runs on the engine; the book owes a whole solution); the language to call the library from named (Ring) with the Python/NodeJS door and the repository |
| 3 | the block (a built-in sandbox rule) showed an effect, not a declaration; "chapter 1 runs this scene" was false (chapter 1 only tells the mail scene; the code that runs it is chapter 2's payments block) | the false promise removed; the example replaced by chapter 2's agent declaration, a real text file refused by the court with its reason (the block is run by the build and was kept) |
| 4 | the example is a required-field check a JSON Schema could do; the rule is the library's; "state them once and the court comes from it" asserted not shown; nothing about the thousand generated lines | the preface says it plainly (the example is small on purpose and a schema can check it too); the rule can be yours (chapter 2's rule over two facts); the court does not read a thousand lines and call them good, it checks a change fits what was declared (chapter 24, rehearse on a copy); `pia`, `compensable`, law 18 glossed |

What the readers still doubt, honestly, and the preface does not hide: nothing runs on the engine yet; Haro has no executable; the library is called from Ring today (a barrier for a Python or TypeScript programmer, answered only by the one governed door, chapter 16); the book is a draft the author has not fully read.
Those are facts of the project, not of the preface. The preface stays a working page until the author writes his own.
