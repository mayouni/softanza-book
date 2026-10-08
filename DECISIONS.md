# DECISIONS — taken on the author's behalf

The author ruled on 2026-10-08 (20:33 UTC+01:00): *"Take decisions on my behalf and continue."* These are the
decisions taken under that ruling, each with its reason. Any of them can be reversed by one word from the author;
each says what reversing it costs. A decision that would publish something, spend money or touch another
repository is not taken here.

| ID | Question | Decision | Why | To reverse |
|---|---|---|---|---|
| PREFACE-01 | The preface draft was not received | Go on without it. `src/en/00-preface.md` keeps its place with `status: missing` | The method writes the preface last, from the book that exists; nothing in Phases 1 to 3 depends on it | Drop `book-00-preface.md` into `drafts/`; it replaces the placeholder |
| REPO-01 | Public or private | **Private, local, no remote**, until the author names a phase for publication | Publishing is outward-facing and not reversible once indexed; a local repository loses nothing | Add a remote and push |
| READER-01 | Copy the Refine reader's code, or rebuild it | **Keep the copy**, with every change a named, asserted edit (`FORMAT.md`) | The lineage is checkable line by line, and a change in the Refine shell stops the build instead of drifting silently | Rewrite `reader/` and `apply_shell` |
| FONTS-01 | Vendor the three fonts | **Not now.** The reader keeps `local()` first and falls back to Georgia and the system sans | Downloading files needs the author's explicit yes, per file; it changes the look, not the book | Say "fetch the fonts"; they go to `assets/fonts/` with their licence |
| SERIES-01 | Where the series line goes | **Keep it visible**: the page description (as the Refine book), under the wordmark, and on the working cover | The prompt asks for the line on the cover and the title page; the Refine reader has no visible slot, so a visible one was made | Delete two lines in `build_book.py` |
| ENGINE-01 | Engine binaries copied, not built at the commit | **Take the build of a worktree at the same commit when one exists** (`D:/GitHub/_wt*`), else the library's checkout; print the gap under every proof line, including engine commits made after the build | A pinned engine build has frozen this machine before; the estate already keeps worktrees with their engines built; the gap is said on every page | Allow one `zig build -j2` with nothing else running |
| LIB-01 | Which commit of the library the book runs at | **`origin/main`**, the public line (93d7a39bd on 2026-10-08), not the working checkout's branch | The working checkout was on another session's side branch (`ringpp/migrate-rule-a`), which split from main on 2026-08-22 and lacks six weeks of main's work; a reader fetches main | Pass `--commit` to the runner, or change `LIB_REF` in `tools/book_common.py` |
| RUNTIME-01 | Say on the page that the blocks ran on the former host language's runtime, not on Haro | **Yes, under every proof line**, with the version read from the runtime itself; the former language is not named there, only "the former host language" | The study rules that until Haro runs the library, the book's code is judged on the old runtime "and the book says so on the page where it matters"; chapter 33 tells it at length | Edit the `engine` line in `build_book.py` |
| STAGE-01 | Three stage words or the site's five | **Three** (built, designed, absent), with the mapping printed once in chapter 3: designed covers in construction, specification and ratified proposal; absent covers named | The contract fixes three; the mapping keeps the site's vocabulary checkable | Change chapter 3 and the badge set |
| CH17-DLM | The domain model answers a rephrased question with the wrong answer | **Shown as a limit, with its own promise**, and a request to the library to refuse instead | A law is only as good as the page that prints where it is broken | Remove the block from section 7 |
| SELF-01 | How the book names the author when telling the protocol (the estate bans "the author" as a name for the Principal) | **First person.** The book is in the author's voice, so it says "I"; the protocol's word, the Principal, is named once in chapter 32 | It removes the question rather than choosing a side | Rewrite chapter 32's paragraph |
| STYLE-01 | Do the Refine book's rules carry over | **Yes, the author-wide ones**: no "substrate" (the build fails on it), no yellow, numbers in Inter. Colour stays allowed for verdicts, stage words and figures, never for prose | They are the author's standing preferences across projects; verdict colour is information, not decoration | Strike a rule here and in `build_book.py` |
| CH01-a | Section 5 says two blocks were run by the site's runner in fresh processes | **Corrected in `src/en/01`**: one block, run by the book's runner inside the library. The draft in `drafts/` is untouched | It is a statement of fact the build contradicts | Restore the sentence from `drafts/` |
| CH01-b | Section 5 places `safeworld_narrated` in the security plane | **Corrected in `src/en/01`** to the agentic plane, where the file lives (`base/test/agentic/`) | Read from the test tree | Same |
| CH01-c | Numbers typed in the prose | **Kept as the author's words**, each traced to its source in the front matter (`figures:`) | All four were found in the record: 76 assertions (read at build), 93 per cent (study 12.15, 93.2 at 93d7a39), 1.04 to 1.88 (study 12.10, the memo of 2026-09-13), 22 verbs and 122 rules (study 12.23) | Replace them with generated figures |
| CH01-d | The front matter I filled | **Kept** (rulings 12.10, 12.11, 12.15, 12.28, 12.29; the two stage lines); narration cited: none, because the chapter argues from the rulings, not from one article | The chapter's own text supports each | Edit the front matter |
| NAMES-01 | Products of other repositories (the bank's platform, the restaurant's platform, the organisation's hub, the conversational agent, the declared machine, the event store, the studios) | **Not named.** Told by what they are, as chapter 1 does ("a bank in Niamey") | §4.8 forbids naming another repository's product without the author's ruling; "Zin" never | Rule a name, and the chapters take it |
| CENTRAL-01 | Register the book with Central | **No.** The book stays outside the estate's protocol; its memos follow the protocol's style | Registration edits Central, another repository; the estate's hooks still apply here | Ask Central to install the block |
| FORMAT-01 | The format verdict the prompt waits for before a third chapter | **Taken as given** by the author's delegation; Phase 1 starts | The author asked to continue | Any change to the format is a builder change; chapters are not affected |

## Ruled by the author, in person

**CRAFTER-01 · 2026-10-08 22:03 UTC+01:00.** The author, in chat: change the hero line and replace "maker" by "crafter",
which says more of the culture the background image carries and of what the author personally thinks of programming:
not maker, not builder. This amends the cover ruled on 2026-10-08 01:12 (study 12.30).

| What | Now |
|---|---|
| English cover, line 2 | **The Software Crafters Platform of the AI Age** |
| Chapter 2, Part I and Part VI titles | "The software crafter"; "The age, the crafter, the method"; "Software crafters, forged" |
| The word in the book | crafter, crafters; "decision-maker" stays: it names a door, not a person's craft |
| French cover, line 2 (taken on the author's behalf, to confirm) | « La plateforme des artisans du logiciel à l'ère de l'IA ». "Crafter" is not a French word, and "artisan du logiciel" is how French says software craftsmanship; the earlier rule kept the English word "makers" only because French already used it |
| The definition (chapter 2) | the site's two sentences with the word changed; a question to the author notes that "craft" suggests skill where the sentence denies it |
| The reason (chapter 2, section 4) | written from the author's message; an open question asks the author to say in his own words what the cover image carries |

**Not changed here, and why.** `drafts/` is the author's: the session prompt and the structure still say "makers". The
site (`stzsite`) is another repository, untouched: its hero lines say "makers" in six places (study 12.30's table:
`tools/build.py` lines 99, 127 and 676; `content/en/tour.md:11` and its French twin; `README.md:3`), plus
`llms.txt:3` and the Offering's "What is a maker?". The book and the site now carry two words until the site is changed;
that is one line for Central, listed in the memo.
