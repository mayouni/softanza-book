# FORMAT — what this book's reader took from the Refine book, file by file

The session prompt (§6) asks for the Refine book's reading experience, not its content, with the lineage
checkable. This file is that record. Written 2026-10-08, Phase 0.

## The source

The Refine book's reader is `ayouni/books/refinement-book/web/` (moved there from the `ayouni` root on
2026-10-08). The prompt pointed at `D:\GitHub\refine`; that repository holds the product's site, and the book's
reader is in the AYOUNI folder. That folder is not under git, so the copy is pinned by hash instead of commit:

| Book file | Taken from | How |
|---|---|---|
| `reader/shell.refine.html` | `refinement-book/web/shell.template.html` (last written 2026-07-12 23:56 UTC+01:00, sha256 `58d6be2e…4ca29df4`) | copied unchanged |
| `tools/build_book.py`, `inline` / `plain` / `convert_body` / `render_table` | `refinement-book/web/build.py` (the same functions) | ported, then extended with the nine-part chapter shape |
| `tools/build_book.py`, `BOOK_CSS` (first block) | `refinement-book/web/build.py`, `EXTRA_CSS` | copied, colours turned into variables |
| `tools/build_book.py`, the overview and chapter views | `refinement-book/web/build.py`, section 7 | same markup, with the book's additions |

**Not taken**: the Refine figure pipeline (`figures.py`, `figpanels.py`, the diagrams folder). This book has no
figures yet. The PDF pipeline (`print.py`) is not taken either; the prompt does not ask for one yet.

## What is the same

- **The page**: an overview (cover on the left, title block on the right, then chapter cards in a grid or a
  list), and a chapter view (a fixed contents sidebar, the page in a 36em column). One file per language.
- **Moving around**: hash routing (`#ch1-…`); previous and next buttons at the foot of each page; ← and → keys;
  Esc goes back to the overview; the mobile sidebar slides in under 900px.
- **Type**: EB Garamond for reading at 22px, with seven steps from 18 to 30px (the A A control, + and − keys);
  Inter for headings, labels and numbers; Archivo Black for the AYOUNI wordmark, with the dot drawn above the I.
- **Paragraphs**: a blank line and a first-line indent, justified, old-style figures. Section heads are small
  uppercase Inter.
- **Search**: Ctrl+K or `/`, accent-insensitive, results by passage, highlights on the page.
- **Print**: the print button and the print stylesheet (header, sidebar and navigation hidden, a page break
  before each chapter, 0.7in margins, 11pt).
- **Code**: dark blocks with the same tones; `#-->` promise lines get their own tone.

## What changed in the shell, and why

`build_book.py` applies a list of named edits, `SHELL_EDITS`. Each must match the Refine shell exactly once,
or the build stops. So if the Refine shell changes, the book notices.

| Edit | Why |
|---|---|
| `html lang`, `title`, `description` | this book, in two languages |
| the Google Fonts `<link>` removed; `@font-face` with `local()` first, then `../assets/fonts/*.woff2` | §6: no CDN, and the page opens from the file system. **The font files are not in `assets/fonts/` yet** (see the open questions); until then each family falls back to its Refine fallback (Georgia, the system sans) |
| every colour literal (shadows, scrims, highlight marks, the print background) → a variable | §6: every colour behind a CSS variable. The build checks this on every page and fails if a literal colour is left. The one exception is `#000` in the card preview's fade, which is an alpha mask, not a colour |
| the `:root` colour set replaced; a dark set added (`data-theme="dark"`, and `prefers-color-scheme` when you have not chosen) | §6: light and dark as first-class themes. The Refine reader has no dark theme. Print always uses the light set |
| breadcrumb: "Softanza" | the book's name |
| header: an EN · FR toggle and a light/dark button, before the font control | §6 |
| script: theme, spine and language handlers, added before the first route | §6 |

## What this book adds (prompt §6)

| Addition | Where | State |
|---|---|---|
| a code cell: the block as written, its promise lines, and under it the verdict from the run, in the site's exact wording | `code_cell`; the words are in `tools/book_judge.py` `WORDS`, copied from stzsite `build_narration_pages.py` | built |
| verdicts the site has no words for: an exercise, a block that was not run, a block that touches files, the clock or chance | `WORDS[...]` marked "book:" | built; the effects wording has not been exercised yet (chapter 1 has no such block) |
| the proof line per chapter: `Run on <date> inside the library at commit <sha>: <k> of <n> blocks kept their promise.` | `proof_html` | built, plus a second line saying the engine binaries are not pinned to that commit |
| a stage word as a badge: built · designed · absent | from `stage:` in the front matter, shown at the head of "The limit" | built |
| the decision block, visually distinct | section 4 is boxed | built |
| the court line: the guard's name linked to its file at the commit, and its assertion count | `court_box`, read from `data/guards.json` | built |
| the six doors as a compact table | section 8 | built |
| EN · FR per chapter | one reader per language; the toggle keeps the page you are on; a chapter with no French yet says so and links to the English | built; no French chapter exists yet |
| the spine marked in the navigation, readable alone | a dot in the sidebar, a badge on the page, a "Read the spine only" button that hides the other chapters | built |
| the whole contents visible | the sidebar and the overview list every chapter of `src/structure.yaml` by part; chapters not yet drafted are shown and not linked | built |
| reading progress | the Refine reader has none, so by §6 none is added | not added, on purpose |
| print stylesheet | the Refine one, plus rules that keep code cells, the court and the doors whole | built |
| `book.json`, `llms-book.txt` | written at every build | a first form; Phase 5 completes them |
| `status.html` | written at every build | built |

## Two readings of the prompt that the author should confirm

1. **One file per language, not one file per chapter.** §7 lists `book/en/*.html`; §6 says to follow the Refine
   reader's single-file choice. The build writes `en/index.html` and `fr/index.html`, one self-contained file each,
   with a page per chapter inside. Splitting into a file per chapter later is a change to the writer only.
2. **The series line.** §0 asks for it "exactly where the Refine book places its own". The Refine reader shows
   none: "First book from the AYOUNI imprint" appears only in its page `description`, and its title page and cover
   carry the wordmark alone. So the line is in the `description`, as in the Refine book, and also shown under the
   wordmark on the overview and on the working cover, so it can be seen. Remove those two if the author wants the
   Refine placement strictly.

## The cover

The overview shows the author's cover: a flat image, `assets/cover/cover.png` (English) and `cover.fr.png` (French),
composed by `tools/make_cover.py` from the two images the author supplied (`assets/cover/source/`: the AYOUNI wordmark and
the elder from Niger), in the layout of the *Refinement-Oriented Programming* cover (wordmark top left, title block on the
left, the figure on the right, author bottom left, cities and year bottom right), without the hands: the strict rectangular
image only. The build embeds it as a JPEG so each reader stays one file. If the image is missing the build falls back to
the typographic working cover it drew before. The back-cover lines are shown on the overview under "From the back cover".

## The type scale (TYPE-01)

The Refine shell sets some sizes that invert the hierarchy at the reader's size (part labels at 11px under chapter rows at 17px; section headings at 0.8em of the body). The book's reader replaces them with one scale, `TYPE` in `tools/build_book.py`: size follows level (book, part, chapter, section, body), a heading is above the text it heads, every label is at least 12px. The CSS is generated from the scale and `check_type_scale()` fails the build on a broken order.
