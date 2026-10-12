# The fourteen house rules

Source: Appendix B. Status: draft (a draft, not read by the author). Library commit 93d7a39bd.

Run: 2 of 2 blocks kept their promise, on 2026-10-12 16:28 UTC+01:00.

The library has a court over its own code. It reads a class as a graph (five rules) or as text (nine) and judges it against rules, most of which were written after the library did something it should not have. This appendix lists the fourteen, and shows three of them firing.

There are two fourteens in this book, and they are different sets. The fourteen **house rules** of this appendix are rules of the library's code: they are a court, and they run. The fourteen **rules of writing**, in chapter 7, are a reading of how the style is written. They are readings of the code, stated as rules, and no machine judges them. The coincidence in the number is a coincidence.

The list of names is fourteen and the library can print it. One more text pass, `for_in_loop`, also reports, and so do two rules over a whole project, `no-dead-code` and, in the deep audit, `no-cyclic-calls`:

```haro
? len( StzCodeRuleNames() )
#--> 14
? StzCodeRuleNames()[2]
#--> q-returns-object
? StzCodeRuleNames()[14]
#--> value-called-as-function
```

> run: kept

Here are three of them, fired on code I planted. A method that writes to the console is a warning, so the code stays clean. A method that differs from another only by case is an error, since the host language does not tell the two apart and the file would not load. And a class that defines `Len()` shadows the host's own function, and is refused:

```haro
cSay = "class Door" + nl + "def Say()" + nl + "	? 'hello'" + nl + "	return 1" + nl
? StzCheckCode(cSay)[1][:rule]
#--> library_prints
? StzCheckCode(cSay)[1][:severity]
#--> warning
? StzCodeIsClean(cSay)
#--> 1
cBox = "class Box" + nl + "def Size()" + nl + "	return 1" + nl + "def size()" + nl + "	return 2" + nl
? StzCheckCode(cBox)[1][:rule]
#--> no-case-collision
? StzCodeIsClean(cBox)
#--> 0
cLen = "class Box" + nl + "def Len()" + nl + "	return 1" + nl
? StzCheckCode(cLen)[1][:rule]
#--> no-len-method
? StzCodeIsClean(cLen)
#--> 0
```

> run: kept

A note on spelling, which a program that reads findings must know. The list uses hyphens: `library-prints`. A finding of eight of the fourteen comes back with underscores: `library_prints`. The findings of the five rules over the code graph (rows 1, 3, 4, 5 and 6) keep their hyphens, and so does the finding of row 2. I print what the run printed.

### The fourteen

| # | Rule | What it refuses | Severity |
|---|---|---|---|
| 1 | `no-len-method` | defining `Len()` on a class: it shadows the host's builtin and breaks every caller | error |
| 2 | `q-returns-object` | a method named with a closing `Q` that does not return an object to chain | error |
| 3 | `no-aggressive-verbs` | method names that begin with Kill or Destroy: the Softanza tone | warning |
| 4 | `engine-first` | new code that reaches for the host's byte-oriented string functions where the engine's forms exist | warning |
| 5 | `q-has-plain-twin` | a chaining mutator with no plain twin: `Q` chains, and plain acts | warning |
| 6 | `no-case-collision` | two methods of one class that differ only in case: the host is case-insensitive, so the file fails to load | error |
| 7 | `dead-knob` | an attribute that a setter writes and nothing reads: a setting that can change nothing | error; warning when only its own getter reads it |
| 8 | `setter-resets-on-reject` | a setter that answers a value it dislikes by overwriting what was already there | warning |
| 9 | `setter-only-moves-one-way` | `max()` or `min()` against the very attribute being set: a ratchet that swallows the other direction | error |
| 10 | `misspelled-name` | a method with a known misspelling while the correct name does not exist | warning |
| 11 | `library-prints` | a class method that writes to the console while it works; methods whose purpose is to display are exempt | warning |
| 12 | `empty-method-body` | a method declared and doing nothing; harsher for a predicate, which then answers nothing, read as false | warning; error for a predicate |
| 13 | `writes-a-mutable-constant` | assigning to `true`, `false`, `null`, `nl`, `tab` or `cr`: in the host they are ordinary globals | error |
| 14 | `value-called-as-function` | calling the result of a call, the shape a global replacement of tokens leaves | error |

I fired rows 6, 11 and 1 above. Chapter 32 fires row 3, chapter 7 fires rows 10 and 13, and chapter 5 fires row 2. For rows 7, 9 and 12 I read the severities from the source, as I did for rows 4, 5, 8 and 14; I did not fire these seven.

### What the court does not judge

None of the fourteen is a rule of writing. No machine judges, today, the style of a program written with the library. That is chapter 7's limit, and it is the reason the other fourteen are in this book as a table with their state, and not as a court.

### The other fourteen: the rules of writing, and where each stands

Read from the study's ruling on the style, with the state of each at the commit this book runs.

| # | Rule of writing | State |
|---|---|---|
| 1 | A value is lifted to its object by `Q()` or a typed lifter | runs |
| 2 | A scene is a brace block on one object | runs |
| 3 | Every printed line carries its answer under `#-->` | the promise is judged when written; a line without one is not refused |
| 4 | A parameter is named, and the name reads as English | runs, and in any order |
| 5 | A chain mirrors the order of thought, one step per line | runs |
| 6 | The verb's form says what happens | runs |
| 7 | Suffixes and prefixes are small and mean one thing each | in part |
| 8 | A function has alternatives for the way a person says it | in part |
| 9 | Precision over generality, when it costs nothing | in part |
| 10 | Code travels inside an argument as a small string | the seat runs; the mark on a parameter's name is retired |
| 11 | Small literal languages live in strings | runs in one form |
| 12 | A sentence can be near-natural | not as the deck wrote it |
| 13 | A function may be named in any human language | Chinese and French names raise; the Arabic one was not run |
| 14 | A comment speaks before the code, in the teacher's voice | runs |
