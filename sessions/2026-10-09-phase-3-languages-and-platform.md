# 2026-10-09 · Phase 3, the languages and the platform

```yaml
by:        softanza-book · claude-sonnet-5-5 · 2026-10-09 01:10 UTC+01:00

subject:   Parts III and V drafted and running: chapters 12 to 16 and 23 to 27; the cover

why:       the author asked for Phase 3 ("Go ahead with Phase 3") and supplied two images for the cover

did:
  - made the cover from the author's two images (the AYOUNI wordmark, the elder from Niger), in the layout of the
    Refinement-Oriented Programming cover without the hands: assets/cover/cover.png and cover.fr.png, composed by
    tools/make_cover.py, embedded in both readers (FORMAT.md, "The cover")
  - sent ten research sessions (research/ch12 to ch16, ch23 to ch27); drafted every chapter myself from them, built,
    committed with explicit paths
  - every chapter has all its blocks kept at 93d7a39bd; the whole build passes (34 source files, 33 chapters, about 88,000 words)
  - taught the runner to unset the machine variable that the door to foreign runtimes cannot live with
    (NoDefaultCurrentDirectoryInExePath), so chapter 16 can run Python, Node and R on this machine
  - corrected earlier chapters where the new research showed them wrong: chapter 2 (the restaurateur's tools: his own
    report gives a spreadsheet, the messaging apps are the label of a form option), chapter 11 (the factory has forged
    outside the library; the vision has not caught up), chapter 20 (the twin of the process environment is built),
    and chapters 2, 11, 22 (the guard semantic_resolver_narrated does not pass at this commit)
  - showed as limits, with running promises where the library gives one: a language of patterns that does not refuse an
    unknown word (15); time sequences that never match (15); the door to foreign runtimes ungoverned, with a way back
    that reaches the host's eval, and an R door that raises (16); two closed formula languages that differ at the edge (12);
    a hand-written fake that passes the gate (24); a world whose truths are narrated and never judged (23); the lean layer
    that does not run, and that is not lean at the binary (27)

state:
  library:         origin/main 93d7a39bd; engine binaries from the worktree at that commit, built 2026-10-05 20:27
  runtime:         the former host language, version 1.27 (printed under every proof line)
  build:           34 source files; every runnable block kept its promise at the last build; build passes
  cover:           flat image, English and French; the French line is a draft (see waiting)
  preface:         missing · placeholder
  chapter 12:      draft · 8 of 8 kept · 5 guards · 3,380 words · 2 open questions · no French
  chapter 13:      draft · 17 of 17 kept · 7 guards · 3,143 words · 3 open questions · no French
  chapter 14:      draft · 13 of 13 kept · 3 guards · 2,714 words · 3 open questions · no French
  chapter 15:      draft · 13 of 13 kept · 5 guards · 2,611 words · 3 open questions · no French
  chapter 16:      draft · 10 of 10 kept · 5 guards · 2,830 words · 3 open questions · no French
  chapter 23:      draft · 10 of 10 kept · 5 guards · 3,114 words · 3 open questions · no French
  chapter 24:      draft · 11 of 11 kept · 7 guards · 3,463 words · 3 open questions · no French
  chapter 25:      draft · 11 of 11 kept · 6 guards · 3,223 words · 3 open questions · no French
  chapter 26:      draft · 10 of 10 kept · 6 guards · 3,403 words · 3 open questions · no French
  chapter 27:      draft · 9 of 9 kept · 4 guards · 4,168 words · 3 open questions · no French
  done:            0 chapters (none read by the author; no French)

waiting:
  - CH12:  built outside the library, designed for the library, for the factory (and chapter 11 amended: done, say if wrong);
           may the small `order` language I wrote for the research be shown
  - CH13:  which date for the first slide (2020 diagram or 2022 deck); has a speaker read the Arabic, Turkish, French and
           Swahili sentences; may your plea to the former host language's project be told in your words
  - CH14:  "facts and laws" for what the file holds and the rules sent to chapters 29 and 30; open on the file or on the 2022 dialog;
           the first moment you wrote that a business could describe itself in one file
  - CH15:  "for the first time in computer science history": yours?; tell the family as it runs, defects beside the wins;
           the missing refusal of unknown words, as your debt or as a finding of the court
  - CH16:  which seven (the record counts it four ways); Python and JavaScript as Haro's planned facets on your word alone;
           print the door's limit (ungoverned, the way back, R raises)
  - CH23:  the three scopes and the architect: the System Foundation's scopes, or something else; the architect told as what one
           declares, with or without the proposed certification; "declared and narrated, judged only for goals, crossings and capabilities"
  - CH24:  the chapter's sentence (the first principle's clause or yours); was the question of 23 July 2026 yours; a dated run of the
           in-browser engine proof, if you hold one
  - CH25:  the bridge sentence as yours or the constitution's, and the twenty-two verbs; which restaurant story (the QR link, not a
           messaging app); the conversational surfaces as what you mean to build or as a study's proposal
  - CH26:  tell the 26 May 2026 removal of the interaction engine; the pattern as designed with running pieces, or wait for the shell kit;
           print the library's own mission control beside "a status bar that tells the truth"
  - CH27:  base inheriting core, or the contract amended; layer selection in Haro; print the bridge runtime's counts of 5 October 2026 or
           only "in construction"; the correction of the runtime's own notes, and whether the book names the peer
  - CHAPTER 1: flagged in chapter 25 and 31: "first demo over a messaging app" and "built with", "runs"
  - PREFACE: drafts/book-00-preface.md is still missing
  - FR:    "artisans du logiciel" as the French line (on the French cover)
  - SITE:  the hero line still says "makers" in six places and llms.txt (another repository, not edited)
  - LIBRARY-REQUESTS: the list below -> stzlib [not routed] proceeding

next:
  - you:  read the drafts in the reader (python -m http.server 8737 --directory D:\GitHub\ayouni\books\softanza-book,
          then http://localhost:8737/en/index.html), and answer the waiting rows inline
  - me:   Phase 4 (the appendices A to G), the preface when its draft exists, then the French and the agent forms; only when asked

note:      about 88,000 words of the 110,000 the structure plans; the chapters run 2,600 to 4,200 words, longer than the
           first phases because the limit sections carry more. Chapters 24 and 27 are the longest.
```

## Requests for the library (found by running; not edits)

Numbered after Phase 2's L15 to L41.

| # | Finding | Where | Seen in |
|---|---|---|---|
| L42 | A host function in a textual condition is refused silently and whole (`FindW` answers an empty list, even inside an `or`); the refusal should speak, and a guard should assert it | `base/list` | ch12 |
| L43 | `AddCalculatedCol` falls back to the host's evaluator and runs a user-defined function from inside a formula string; close it or name it | `base/table` | ch12 |
| L44 | No narration tells the schema grammar, the sampler or constrained decoding; the forge's grammar says a general identifier for a menu seat where the library's compiler closes the menu into an alternation | narrations; the Haro charter's forge | ch12 |
| L45 | `semantic_resolver_narrated` does not pass at this commit: it stops with an error from a string-splitting function; "caps" resolves to a bounds method because the dictionary is read from the documentation tags; "mirrored" resolves to nothing | `base/test/natural`, `base/natural` | ch13 |
| L46 | The suggestion for an old-era word is poor (`and_` is offered as `addn`); `Understood()` prints verbs and not their arguments; `IfSo("remove duplicates")` is refused | `base/natural` | ch13 |
| L47 | `IsAXT` builds a string and evaluates it, so a function named in a descriptor runs | `base/object/stzObject.ring` | ch13 |
| L48 | Loading the library rewrites cache files inside the tree (`semantic_ops.stzcache`, `reflect_example_index.stzcache`), so the snapshot is not read-only in practice | `base/natural`, `base/reflect` | ch13, ch24, ch27 |
| L49 | On an instance graph the symmetric law is recorded and never derived (only the default world derives it); the `rules` section of the knowledge file is read and skipped; malformed lines are dropped in silence | `base/graph/stzKnowledgeGraph.ring` | ch14 |
| L50 | One relation per pair of entities; `QueryPath` is not a join and the predicate of `Query` cannot be a variable; `DefineClass` gives no inheritance; `Explain()` and `ValidateOntology()` raise or answer 1 whatever the ontology holds | `base/graph` | ch14 |
| L51 | The founding dialog of the knowledge narration does not run (`@Q("Apple").IsA(:Fruit)`); the rules file is still `.stzrulz` where the family names four letters | narrations, `base/graph` | ch14 |
| L52 | The pattern family does not refuse an unknown word: `Nx("{@Banana(3)}").Match(7)` answers 1 (finding HF-5 of the Haro charter session, still open); the matrix language returns an ERROR token that nothing raises | `base/regex` | ch15 |
| L53 | Timex's parser slices with an end position through a count-based function, so every sequence form answers 0 and `{@Event(Lunch)}` tokenises as `Lunch)` | `base/regex/stzTimex.ring` | ch15 |
| L54 | Listex: the cache key is the list's length and the sum of its character codes, which ignores order; the uniqueness flag is ignored; stepped ranges raise; its classic suite runs nothing as shipped (tests after a `func`) | `base/regex/stzListex.ring`, `base/test/listex` | ch15 |
| L55 | Graphex: `->` means "later on one path"; quantifiers are parsed and ignored; the cache is keyed by node ids; no `Explain`, `Tokens`, `Pattern`, small function, or narration; the table language's narration has a double extension in its file name; the declarative builder's headline form is retired or raises | `base/regex` | ch15 |
| L56 | The door to foreign runtimes starts its script by bare name, which fails where `NoDefaultCurrentDirectoryInExePath=1`, and does not quote the runtime path | `base/extercode/stzExterCode.ring` | ch16 |
| L57 | The R wrapper uses identifiers that begin with an underscore, which R rejects, so the R door raises on every call; `Result()` reads the foreign result through the host's `eval` with strings quoted and not escaped; `CallTrace()[n][:exitcode]` is always 0 | `base/extercode` | ch16 |
| L58 | `Execute()` never asks the governance, though the vision says the door is governed; the narrations' `@@R`, `@@C`, `XC()` and `XAI()` are defined nowhere; no guard in the folder runs a foreign runtime and passes | `base/extercode`, narrations | ch16 |
| L59 | A world's truths, a flow's `Require` and `Then`, a reaction's duration and a refinement's bounds are stored and narrated and never judged; the near-natural idiom of the constellation (`Hosts`, `Admits`, `Explain`, ...) is not in the class; a call is not routed into a nested constellation; the scope object has no `Capabilities()`; "refused: refused:" is doubled in the governance reasons | `base/app`, `base/platform`, `base/governance` | ch23 |
| L60 | The registry takes a double that declares nothing for live, so an undeclared fake passes the gate; a refused `Deploy(:Production)` leaves the registry in the production phase; `Deploy(:Emulated)` never sets the emulated phase; the lowering knows two verbs; the fidelity contract is fixed by target class; plan sizes are catalogue estimates | `base/service`, `base/system` | ch24 |
| L61 | The page that proves the engine in a browser (`wasm_proof.html`, "8/8") is not in the pinned tree; `deployment_narrated` is cited as 45/45 and holds more; the narrations carry the restaurant's product name as the sample | `base/test/system`, design documents | ch24 |
| L62 | `ReplyIn` raises on any reply with a space (chapter 18's L18, decisive for a text message); `Generate` could list the reach surfaces before failing; `NaturallyIn("dje")` raises an opaque error instead of naming the missing pack; the schema refusal says "the model answered" whoever speaks | `base/conversation`, `base/platform`, `base/natural`, `base/neural` | ch25 |
| L63 | There is no message unit with a status and a per-medium sandbox; the twenty-two verbs have no data list in the library, and `_ScreenIntent` accepts any word | library | ch25, ch26 |
| L64 | `ToHtml` emits an empty box as `<div id="x"/>`, which a browser reads as an open tag, so the siblings nest and the fixture reads DISAGREE; the web projection carries no roles, labels or intents; `ToPanel` needs a font file and raises without one | `base/gui/stzUiDocument.ring` | ch26 |
| L65 | The emulator's mission control prints "parts healthy", "Ready to ship." and a fidelity text from literals, and "Deploy to production" is an alert; derive them from the plan | `base/system/stzEmulator.ring` | ch26 |
| L66 | The explorer's model (`stzWorldGraph`) is loaded by no entry file; the engine design still lists twenty-four verbs from an interaction engine that was removed on 26 May 2026; the sound studio's test summary ignores "skipped" | `base/world`, design documents, `engine/tools` | ch26 |
| L67 | No guard judges the layers against their contract (532 narrated guards in base, none in core or max); the core string class calls engine names that no library registers (STZLIB-CORE-ENGINE-01); core's `FindMin` calls a base function; `core/stkLib.ring` line 2 and `base/file/stzJson.ring` line 7 load a file in the wrong case | `core`, `base`, `max` | ch27 |
| L68 | The typed constants of the engine's status command (`modules_built`, `dlls_shipping`, `ring_bridge_regs`, `engine_tests`) do not match any count I can make; nine of nineteen vendored libraries have an archive digest, three have no version | `cli/src/engine_status.zig`, `engine/vendor` | ch27 |

## What I could not settle

- Chapter 1 is the author's text. Chapters 25 and 31 flag "first demo over a messaging app", "built with" and "runs"; I have changed none of it.
- The French cover carries "artisans du logiciel" from the structure file's French block; it is a draft until the author confirms.
- Chapters 16 and 24 run foreign runtimes and write folders in the build's working directory; they pass on this machine only (Python at a path in the user's profile, Node and R at the library's default paths). A clean machine will record them as the reader shows, and not rerun them.
- `engine_is_optimised_narrated` is counted at seven by the book's counter and passed six in the researchers' runs; the page says six of six for the run, and the court line reads the build's count.
