# Brief: the scene as the basis of the code (CODESTYLE-01, 2026-10-15)

The author, on a screenshot of chapter 5's chained history example:

> "The @@() has been made to fix a Ring inability to correctly print list contents, I think this could disappear in Haro and let the expressive printout be the norm. [...] Also you should embrace the beauty of the declarative style with braces (which Ring++ should maintain from Ring) [...] do you see the beauty of the style? this should be the basis. Of course, sometimes one sentence with chaining is a better choice and the book must make good use of both. The more classic style should also be shown [...] as well as the more sophisticated natural form using Naturally("....")"

Chapter 5 now shows the four forms on one example (the scene, the chain, the classic, and a word on the natural form and on `@@()`). Your job is the rest of the book: **make the scene, the brace block on one object, the basis of the code**, and keep the chain where one sentence reads better.

## The four forms (verified at the pin, 93d7a39bd)

```haro
QH(12500) {
	Add(500)
	Retrieve(1500)
	DivideBy(500)
	MultiplyBy(2)
	? @@( History() )
	#--> [ 12500, 13000, 11500, 23, 46 ]
}
```

- **The scene** (the basis): `Q(...) { ... }`, `QH(...) { ... }`, or `oObject { ... }`: the object named once, each line inside the braces speaks to it. Variables assigned inside the braces are visible after them. Method names inside braces resolve to the object first.
- **The chain** (one sentence): `Q(...).AQ().BQ().C()`, where the thought is one sentence. Keep it there.
- **The classic** (`o1 = new stzX(...)` then `o1.A()` line by line): shown in chapter 5; keep it where the page is about the object as a variable passed around, or where a reader is told to type it.
- **The natural** (`Naturally("...")`): chapter 13's ground; it runs on text at the pin, not on numbers. Do not add new natural blocks.

**`@@()` stays for now.** On the former host language `?` prints a list one item per line; `@@()` asks for the expressive form `[ 1, 2, 3 ]`. The author wants Haro to print that form by default, and then `@@()` leaves the examples; until then every list printed with `?` keeps its `@@( )`, inside a scene too, so that the promised `#-->` lines do not change.

## What to convert

A block (in a ` ```haro ` fence, not ` ```haro exercise `) is converted to a scene when **it makes three or more successive calls on one object**, written either classic (`o.A()`, `o.B()`, `o.C()` on separate lines) or as a long chain (four or more `Q` links) that reads as a procedure rather than one sentence. Not converted: a chain of one to three links that reads as one sentence; a block that calls many different objects; a declaration (a text in quotes) and the court calls on it; code whose point is the classic form; exercises; chapter 1 (the author's own); any block where you are not sure the scene is clearer: leave it.

How, mechanically:
- `o = new stzList(...)` followed by `o.A()` lines becomes `o = new stzList(...)` then `o { A() ... }` (keep the variable when a later block uses it), or `Q(...) { ... }` / `StzListQ(...) { ... }` when the variable is used nowhere else in the chapter.
- Inside the braces drop the `o.` prefix and the `Q` of a fluent call that no longer chains (`AddQ(500)` becomes `Add(500)`) **only where the non-Q method exists** with the same effect; when unsure, keep the call as it was, braces still work with `o.` calls.
- Keep every `#-->` line, in the same order, and every comment's meaning; indent the scene's lines with one tab, as the author's example does.
- A `?` that prints a list keeps `@@( )`.
- `QH(...)` (history) turns the global history switch on; `History()` consumes and clears the stream. Do not add history where the block had none.

## Prose
Where a block's form changes and the sentence before it describes the code line by line ("each call on `o`"), make the sentence say the same of the scene, in one clause. Do not add a paragraph explaining braces: chapter 5 does it once; a page may point to it ("the scene of chapter 5"). French: the same, with byte-identical fences (`tools/check_fr.py` checks), « la scène », « les accolades ».

## Rules
- You cannot run the blocks (the build runs once, after all of you): be conservative, convert only what the rules above make safe, and say in your report every block you converted, with its chapter section, so the build's failures can be traced.
- Edit only your chapters' EN and FR files. Scripts in your scratchpad, exact strings asserted once; `python -I tools/check_fr.py <n>`; `python tools/book_audit.py` once at the end. Do not commit, build or push.
- Report (final message, under 300 words): per chapter, the number of blocks converted to scenes, kept as chains, left classic, and any block you were unsure about.
