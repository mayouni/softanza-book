# Brief: "AI model" and "AI agent" where the bare words are ambiguous (VOICE-05)

The author, on 2026-10-14: **"When you say 'model' or 'agent' it can be sometimes imprecise; use AI model and AI agent when clarification is required."**

"Model" in this book can mean an AI model (what proposes), a data model, a domain model (the knowledge base a world declares), the *domain language model* (Softanza's own concept, chapter 19: a model with no neurons), a model file (exported bigram). "Agent" can mean an AI agent, a declared programmatic agent (an entry that a `pia:` declaration describes), a person acting for someone, the sixth reader door ("the agent" who reads the book), or the `Agent` class. A decision-maker or a reader who meets the bare word has to guess. Your job: in your pages, make the sense exact where a reader could take the other one.

## The rule
1. **Where the bare word could be taken for another sense, write "AI model" / "AI agent"** (plural "AI models", "AI agents"; the possessive "the AI model's"). In French: « modèle d'IA », « agent d'IA » (« modèles d'IA », « agents d'IA »); keep « modèle de langage » where the English says "language model".
2. **First use in each page, in prose where the AI sense is meant**: say "AI model" or "AI agent" (the front-matter description and the roadmap paragraph count as prose). After that, the bare word is fine **while the paragraph or the section keeps one sense**; say it in full again wherever another sense of the word sits within about a paragraph (a data model, a domain model, a person's agent), at the head of a section, in a list item or a table cell that stands alone, in a heading, and in a sentence the reader could lift out alone (the first line of a section, a bridge).
3. **Do not use the long form everywhere.** "The AI model proposed. The AI model did not decide. The AI model came last." is worse than the bare word. The test is: could a reader take another sense here? If not, leave it.
4. **Never touch** (the long form must not be forced into these): code fences and every `#-->` line; names the library owns (`StzAgentDeclarationQ`, `pia:`, class and guard names, file names); front-matter keys other than the free text of `description`, `built`, `designed`, `absent` and similar descriptive values; the chapter titles, `law:` strings and glossary headwords **unless they are plainly ambiguous**: if one is, report it, do not change it (titles and law names are the author's and feed `structure.yaml`, the audit and the cross references); Softanza's own terms keep their names: *domain language model*, *domain model*, *model file*, *programmatic agent*, *agent class*, *the sixth door: the agent*, *language model*. Those are exact already; do not prefix them with "AI" unless the sentence is plainly about a neural one ("the AI model that completes it").
5. Where a sentence says "the model" meaning the AI model the field hypes (chapter 1's "the model proposes"), "AI model" at the first use and where a domain/data sense is near; the exact word *proposer* already used there stays.
6. A **person-agent** ("a purchasing agent") stays "agent"; do not turn it into an AI agent. A **declared agent** in a `pia:` declaration is an AI agent in the book's sense (a program that watches, decides within limits and acts): "AI agent" at first use, then "agent".
7. The count must not grow into noise: the lint (`style_lint`) flags none of this, but a page that now says "AI model" in every sentence has failed. Typically a chapter takes 2 to 8 changes, a dense one (chapter 20, 17, 19) up to 15.

## The French
Same changes in `src/fr/`, same sentences (the French is a translation, same paragraph, heading, list-item, table-row and fence counts). « modèle d'IA » / « agent d'IA »; « le modèle » alone stays where the English stays bare. `FRENCH.md` rows 108 and 109 govern; do not edit `FRENCH.md` (the lead adds the row).

## What you keep
Every fact, every number, every code fence, every `#-->` line, the nine elements and their headings, the stage words, the voice (first person, plain words, long then short). Edit **only** your pages' two files each (EN and FR). Do not set `status`. Do not run the build or the printers.

## How
For each of your pages: `grep -n -i -E "\\b(model|models|agent|agents)\\b"` on the English; read each hit in its paragraph; decide with the test of rule 3; edit with a small script in your scratchpad (read bytes, normalise CRLF to LF, replace an exact string asserted to occur once, write bytes back; `python -I`), the same sentence in the French. Then `python -I tools/check_fr.py <number>` and `python -I ../../writing-framework/tools/style_lint.py src/en/<file>.md` (and `src/fr/<file>.md --lang fr`); fix what they report in your files. Run `python tools/book_audit.py` once at the end (no `-I`) and fix errors in your files.

## Report (final message, under 250 words)
Per page: `page · changes EN/FR · titles or law strings you judged ambiguous and did not change`. Then anything ambiguous you could not settle (a sentence where the sense is the author's to rule).
