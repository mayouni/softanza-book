# 2026-10-08 · Phase 0, the skeleton

```yaml
by:        softanza-book · claude-opus-5-5 · 2026-10-08 20:24 UTC+01:00

subject:   the book's skeleton: the Refine reader carried over, chapter 1 running, the build failing when it should

why:       Phase 0 of the session prompt; the author's verdict on the format comes before a third chapter

did:
  - moved the Refine book to ayouni/books/refinement-book and created this repository at ayouni/books/softanza-book
  - read the Refine reader (shell.template.html, build.py, print.py), the site's runner and judge (narrations_run.py,
    showcase_run.py, harvest_examples.py, build_narration_pages.py), Central's memo style, chapter 1, the structure,
    the prompt, and the headings of the rulings study
  - copied the Refine shell unchanged to reader/shell.refine.html, and recorded every change made to it in FORMAT.md
  - wrote tools/book_run.py, book_guards.py, book_judge.py, book_common.py and build_book.py
  - put chapter 1 in src/en/ with front matter; the text is the author's draft, the fence tags renamed ring -> haro
  - built: chapter 1, 1 of 1 blocks kept its promise, its exercise recorded as not run; 3 of 3 guards resolved
    (service_registry_narrated 51, safeworld_narrated 76, governance_crossing_narrated 31 assertions, counted in the files)
  - checked the failure path: a wrong promise, a missing guard, and code changed after its run each exit 1
  - looked at the reader in the browser pane: light, dark, French fallback page, status page, 375px width with no sideways scroll

state:
  refs read:
    stzsite:          fa8e1e605 (main)
    stzlib:           b9d5cd1e4 (ringpp/migrate-rule-a); it was 03c632cbc when this session started, and its
                      working tree holds 956 uncommitted entries, so the book runs a snapshot, not the tree
    softanza:         28eb676 (main), protocol read: CLAUDE.md, STYLE.md
    refinement-book:  not under git; shell.template.html sha256 58d6be2e...4ca29df4
  not yet read:       the vision corpus, the 135 narrations, the full rulings study (only its headings), stzsite content/;
                      each is read per chapter, before drafting it
  preface:            missing (src/en/00-preface.md holds its place)
  chapter 1:          draft · run 1 of 1 kept · guards 3 of 3 · no French · not read by the author
  chapters 2 to 33:   not drafted
  format:             waiting for the author's verdict (FORMAT.md)

waiting:
  - PREFACE-01:   book-00-preface.md was not among the files received -> author [asked here] proceeding
  - REPO-01:      public from the first commit, or private until a named phase? No remote exists yet -> author [asked here] proceeding
  - READER-01:    the Refine reader's code was copied (lineage in FORMAT.md) rather than rebuilt; keep that? -> author [asked here] proceeding
  - FONTS-01:     may I vendor EB Garamond, Inter and Archivo Black (open-licence, from Google Fonts) into assets/fonts/?
                  Without them the reader falls back to Georgia and the system sans -> author [asked here] proceeding
  - SERIES-01:    the Refine reader shows no series line (only in its page description); I also placed this book's
                  under the wordmark and on the working cover. Keep, or Refine's placement strictly? -> author [asked here] proceeding
  - ENGINE-01:    the engine binaries are copied, not built at the commit; a pinned build means a zig build this machine
                  has frozen on. Accept the stated gap? -> author [asked here] proceeding
  - STYLE-01:     do the Refine book's rules carry over (no "substrate", no yellow, monochrome body text, numbers in Inter)?
                  The build already checks "substrate" and uses no yellow; verdicts and stage badges use colour -> author [asked here] proceeding
  - CH01-AUTHOR:  three proposals on chapter 1, which I did not change:
      a. section 5 says "the two code blocks above were run by the site's own runner ... each side in a fresh process";
         the chapter has one runnable block and an exercise, and the book's runner runs them in one process
      b. section 5 places safeworld_narrated "in the security plane"; the file is base/test/agentic/, and
         governance_crossing_narrated is base/test/system/
      c. numbers typed in the prose ("seventy-six assertions", "ninety-three percent", "a factor between one and two",
         "twenty-two verbs, one hundred and twenty-two rules"): the rule says every number is read at build. 76 matches
         the file today; the others I have not read. Generate them, or keep them as the author's words with a date?
    and to confirm the front matter I filled in: narrations (none cited), rulings 12.10, 12.11, 12.15, 12.28, 12.29,
    the two stage lines, and the site link the chapter should carry -> author [asked here] proceeding
  - CENTRAL-01:   this repository is not in the estate (no mailbox, no installed block), so nothing was filed to Central;
                  register it? -> author [asked here] proceeding

next:
  - you:  open the reader (en/index.html, or run: python -m http.server 8737 --directory D:\GitHub\ayouni\books\softanza-book)
          and FORMAT.md, and give the format verdict
  - you:  answer the waiting rows above; drop book-00-preface.md into drafts/
  - me:   on the verdict, Phase 1: chapters 2, 3, 4, 5, 11, 17, 32, 33 in English, each read from its rulings first
          (run with: claude-opus-5-5 · effort high)

note:      the skeleton proves the one thing it must: a page whose promise breaks does not build
```
