#!/usr/bin/env python3
"""The press edition: the book as a paginated PDF, one file per language.

    python tools/print_book.py            # en and fr
    python tools/print_book.py en         # one language
    python tools/print_book.py --html     # compose print/<lang>.html only, no PDF

Reads what the build already wrote (data/book-run.json, data/guards.json) and the pages the reader is made of
(`build_book.build_pages`), so a printed page says exactly what the reader says: the same verdict under each block,
the same proof line, the same draft banner. Nothing is run here and nothing is composed from memory.

Writes print/<lang>.html and print/softanza-<lang>.pdf. Chrome (headless) lays out the pages with its own
@page rules; there is no network, no CDN, no paged.js. The contents carry real page numbers: the book is laid
out once with placeholders, the first page of every chapter is found in that PDF's text, and it is laid out again.

Trim 6.5 x 8.5 in, the cover's own proportion (1097 x 1434 px), so the cover prints full bleed with no crop.
Page 1 is the cover; folios are the physical page numbers, so the contents and the folios agree.
"""
import base64, html, os, re, subprocess, sys, tempfile
from pathlib import Path
from pypdf import PdfReader

import build_book as B
from book_common import ROOT, sources, structure, load_json, now, stamp

CHROME = Path(os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
OUT = ROOT / "print"
PAGE_W, PAGE_H = "6.5in", "8.5in"

PRINT_CSS = """
/* ---- the press edition: light, serif, narrow ---- */
:root { --font-body: Georgia, 'Times New Roman', serif;
  --code-bg: #f4f1e8; --code-rule: #d9d3c2; --code-ink: #1a1612; --code-kw: #a24a0c; --code-str: #3b6b3a;
  --code-num: #1f6a5a; --code-com: #6b6358; --code-promise: #5a4a2a; --code-label: #6b6358; }
@page { size: %(w)s %(h)s; margin: 0.72in 0.6in 0.8in 0.6in;
  @bottom-center { content: counter(page); font: 8pt Arial, Helvetica, sans-serif; color: #1a1612; } }
@page :left  { margin-left: 0.5in;  margin-right: 0.7in; }
@page :right { margin-left: 0.7in;  margin-right: 0.5in; }
@page cover { size: %(w)s %(h)s; margin: 0; @bottom-center { content: none; } }
@page cover:left { margin: 0; @bottom-center { content: none; } }
@page cover:right { margin: 0; @bottom-center { content: none; } }
@page cover:blank { margin: 0; @bottom-center { content: none; } }
@page front { @bottom-center { content: none; } @top-center { content: none; } }
html { font-size: 9.6pt; background: #fff; }
body { background: #fff; color: #1a1612; font-family: Georgia, 'Times New Roman', serif; line-height: 1.46; margin: 0; padding: 0; }
a { color: inherit; text-decoration: none; }
p { margin: 0 0 0.62em; orphans: 3; widows: 3; hyphens: auto; }

.pcover, .pback { page: cover; break-after: page; margin: 0; padding: 0; width: %(w)s; height: %(h)s; overflow: hidden; }
.pcover img { display: block; width: %(w)s; height: %(h)s; }
.pback { position: relative; background: #1a1612; color: #fbfaf6; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; }
.pback .bl { font-style: italic; font-size: 15pt; line-height: 1.7; }
.pback .bl-first { font-style: normal; font-family: Arial, sans-serif; font-size: 8pt; letter-spacing: 3px; color: #E96A1A; margin-bottom: 0.4in; }
.pback .im { position: absolute; bottom: 0.7in; font-family: Arial Black, Arial, sans-serif; font-size: 13pt; letter-spacing: 1px; }

.pfront { page: front; break-before: page; }
.halftitle { padding-top: 2.7in; text-align: center; font: 800 16pt Arial, sans-serif; }
.titlepage { padding-top: 1.8in; text-align: center; }
.titlepage .t { font: 800 30pt/1.1 Arial, sans-serif; letter-spacing: -0.6px; }
.titlepage .s { font-style: italic; font-size: 13pt; margin-top: 0.25in; color: #3a3326; }
.titlepage .g { font-style: italic; font-size: 10.5pt; margin-top: 0.14in; color: #6b6358; }
.titlepage .a { font: 600 12pt Arial, sans-serif; margin-top: 0.75in; }
.titlepage .i { font: 800 13pt Arial, sans-serif; margin-top: 0.9in; letter-spacing: 1px; }
.titlepage .c { font: 8pt Arial, sans-serif; letter-spacing: 2px; color: #6b6358; margin-top: 0.1in; }
.colophon { padding-top: 4.4in; font: 7.8pt/1.6 Arial, sans-serif; color: #3a3326; }
.colophon p { margin-bottom: 0.08in; }
.colophon.ask { break-before: page; padding-top: 2.2in; font-size: 10pt; }
.colophon .warn { border: 1px solid #1a1612; padding: 0.08in 0.12in; font-weight: 600; color: #1a1612; }

.toc h2 { font: 800 20pt Arial, sans-serif; margin: 0 0 0.25in; letter-spacing: -0.3px; }
.toc .tp { font: 700 7pt Arial, sans-serif; letter-spacing: 2px; text-transform: uppercase; color: #6b6358; margin: 0.16in 0 0.04in; }
.toc .tr { display: flex; align-items: baseline; gap: 0.07in; font-size: 9.2pt; line-height: 1.5; }
.toc .tr .n { font: 600 8pt Arial, sans-serif; color: #6b6358; width: 0.26in; flex: none; }
.toc .tr .tt { flex: none; max-width: 4.2in; }
.toc .tr .dots { flex: 1; border-bottom: 1px dotted #9a9078; transform: translateY(-0.03in); min-width: 0.2in; }
.toc .tr .pg { font: 8.5pt Arial, sans-serif; flex: none; }
.toc .tr .sp { font: 700 6pt Arial, sans-serif; letter-spacing: 1px; text-transform: uppercase; border: 1px solid #1a1612; padding: 0 3px; border-radius: 2px; }

.ppart { page: front; break-before: page; padding-top: 2.4in; }
.ppart .pn { font: 700 9pt Arial, sans-serif; letter-spacing: 3px; text-transform: uppercase; color: #E96A1A; }
.ppart h2 { font: 800 25pt/1.15 Arial, sans-serif; letter-spacing: -0.5px; margin: 0.15in 0 0.3in; }
.ppart .law { font-style: italic; font-size: 11.5pt; line-height: 1.5; color: #3a3326; border-left: 3px solid #1a1612; padding-left: 0.16in; }
.ppart .ol { margin-top: 0.4in; font: 8.5pt/1.7 Arial, sans-serif; color: #3a3326; }

.pch { break-before: page; }
.pch .ch-eyebrow { font: 700 7.5pt Arial, sans-serif; letter-spacing: 2.4px; text-transform: uppercase; color: #6b6358; margin-top: 0.3in; }
.pch .ch-title { font: 800 21pt/1.14 Arial, sans-serif; letter-spacing: -0.4px; margin: 0.08in 0 0.16in; }
.pch .ch-rule { border-top: 2px solid #1a1612; width: 0.7in; margin: 0.14in 0 0.22in; }
.pch h2 { font: 800 12.5pt/1.25 Arial, sans-serif; margin: 0.28in 0 0.1in; break-after: avoid; }
.pch h3 { font: 700 10.5pt/1.3 Arial, sans-serif; margin: 0.2in 0 0.07in; break-after: avoid; }
.pch ul, .pch ol { margin: 0 0 0.62em 1.2em; padding: 0; }
.pch li { margin-bottom: 0.3em; }
.pch blockquote { margin: 0.1in 0.2in; font-style: italic; color: #3a3326; }
.pch .proof, .pch .proof-engine, .pch .status-banner { font: 7.2pt/1.45 Arial, sans-serif; color: #3a3326; margin: 0 0 0.05in; }
.pch .status-banner { display: inline-block; border: 1px solid #1a1612; padding: 1px 7px; font-weight: 700; letter-spacing: 0.4px; margin: 0.06in 0 0.08in; }
.pch .proof.fails { color: #a3392b; }

.pch pre, .pch code { font-family: Consolas, 'Courier New', monospace; }
.pch .code-cell { margin: 0.12in 0 0.18in; break-inside: auto; border: 1px solid var(--code-rule); border-radius: 3px; background: var(--code-bg); }
.pch .code-cell pre { white-space: pre-wrap; overflow-wrap: anywhere; word-break: normal; font-size: 7.3pt; line-height: 1.38; margin: 0; padding: 0.08in 0.12in; overflow: visible; }
.pch .code-cell .verdict, .pch .code-cell .cell-head, .pch .code-cell .cell-foot { font-family: Arial, sans-serif; font-size: 6.8pt; }
.pch .court, .pch .decision, .pch .doors, .pch .sources { break-inside: avoid; }
.pch .sources { margin-top: 0.3in; font-size: 7.6pt; padding: 0.1in 0.14in; background: #f5f0e2; }
.pch table { border-collapse: collapse; width: 100%%; font-size: 8.3pt; line-height: 1.4; margin: 0.1in 0 0.16in; }
.pch table { table-layout: auto; }
.pch td, .pch th, .pch code, .pch p, .pch li { overflow-wrap: anywhere; }
.pch code { white-space: pre-wrap; }
.pch th, .pch td { border-bottom: 1px solid #d9d3c2; padding: 0.04in 0.06in; text-align: left; vertical-align: top; }
.pch th { font: 700 7.4pt Arial, sans-serif; letter-spacing: 0.8px; text-transform: uppercase; color: #6b6358; border-bottom: 1.5px solid #1a1612; }
.pch .doors { font-size: 8.6pt; }
.pch .book-fig { margin: 0.14in 0; break-inside: avoid; }
.pch .book-fig svg { max-width: 100%%; height: auto; }
.pch .author-q { font: 600 7pt Arial, sans-serif; border: 1px dashed #E96A1A; color: #E96A1A; padding: 0 4px; border-radius: 3px; }
"""


def shell_style(ui):
    head, _ = B.apply_shell(ui)
    m = re.search(r"<style>(.*?)</style>", head, re.S)
    return m.group(1) if m else ""


def esc(s):
    return html.escape(s, quote=False)


def css_str(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def data_uri(path):
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")


def compose(lang, st, pages, runs, guards, ui, pgmap):
    """The whole print document. pgmap: slug -> page number ('000' on the first pass)."""
    title = st["fr"]["title"] if lang == "fr" else st["title"]
    sub = st["fr"]["subtitle"] if lang == "fr" else st["subtitle"]
    tag = st["fr"]["tagline"] if lang == "fr" else st["tagline"]
    series = st["fr"]["series"] if lang == "fr" else st["series"]
    built = runs.get("run", {})
    lib = built.get("library", {})
    fr = lang == "fr"
    by_number = {p["number"]: p for p in pages}
    by_letter = {str(p["appendix"]): p for p in pages if p.get("appendix")}

    cover = ROOT / "assets" / "cover" / ("cover.fr.png" if fr else "cover.png")
    n_draft = sum(1 for p in pages if p["own"] and p["meta"].get("status", "draft") == "draft")
    n_read = sum(1 for p in pages if p["own"] and p["meta"].get("status") in ("read", "final"))
    kept = sum(p["run"]["kept"] for p in pages if p["own"] and p["run"])
    runnable = sum(p["run"]["runnable"] for p in pages if p["own"] and p["run"])
    stamped = now().strftime("%Y-%m-%d")

    # running heads: one named page per chapter, so each page carries its chapter's title
    named = []
    for p in pages:
        label = (f'{p["number"]} · {p["title"]}' if p["number"] and not p.get("appendix")
                 else (f'{ui["appendix"]} {p["appendix"]} · {p["title"]}' if p.get("appendix") else p["title"]))
        named.append(f'@page p-{p["slug"]} {{ @top-center {{ content: "{css_str(label)}"; '
                     f'font: 7pt Arial, sans-serif; letter-spacing: 1.2px; text-transform: uppercase; color: #6b6358; }} }}')
        named.append(f'.pch[data-slug="{p["slug"]}"] {{ page: p-{p["slug"]}; }}')

    out = [f'<!DOCTYPE html><html lang="{lang}" data-theme="light"><head><meta charset="utf-8">'
           f'<title>{esc(title)} — {esc(sub)}</title><style>\n{shell_style(ui)}\n{PRINT_CSS % dict(w=PAGE_W, h=PAGE_H)}\n'
           + "\n".join(named) + '\n</style></head><body>']

    out.append(f'<section class="pcover"><img alt="{esc(ui["cover_alt"])}" src="{data_uri(cover)}"></section>')

    out.append(f'<section class="pfront halftitle">{esc(title)}</section>')
    out.append(f'<section class="pfront titlepage"><div class="t">{esc(title)}</div><div class="s">{esc(sub)}</div>'
               f'<div class="g">{esc(tag)}</div><div class="a">Mansour Ayouni</div>'
               f'<div class="i">AYOUNI</div><div class="c">TUNIS · NIAMEY · PARIS · 2026</div></section>')

    if fr:
        warn = (f"Épreuve de travail. {n_draft} pages sur {len(pages)} sont des brouillons que l'auteur n'a pas encore lus ; "
                f"{n_read} sont lues. Cette édition française est une traduction des brouillons anglais.")
        proof = (f"Le code de chaque bloc a été exécuté dans la bibliothèque au commit {lib.get('short', 'null')} : "
                 f"{kept} blocs sur {runnable} ont tenu leur promesse. Les verdicts imprimés sont ceux de l'exécution, jamais réécrits.")
        line = f"Imprimé le {stamped}. {series}."
    else:
        warn = (f"Proof copy. {n_draft} of {len(pages)} pages are drafts the author has not yet read; {n_read} are read.")
        proof = (f"Every block of code was run inside the library at commit {lib.get('short', 'null')}: "
                 f"{kept} of {runnable} blocks kept their promise. The verdicts printed are the run's, never rewritten.")
        line = f"Printed {stamped}. {series}."
    out.append(f'<section class="pfront colophon"><p class="warn">{esc(warn)}</p><p>{esc(proof)}</p><p>{esc(line)}</p>'
               f'<p>© Mansour Ayouni · AYOUNI</p></section>')

    # contents
    rows = []

    def row(num, p, spine=False):
        pg = pgmap.get(p["slug"], "000")
        sp = f'<span class="sp">{ui["spine"]}</span>' if spine else ""
        return (f'<div class="tr"><span class="n">{esc(str(num))}</span><span class="tt">{esc(p["title"])}</span>{sp}'
                f'<span class="dots"></span><span class="pg">{pg}</span></div>')

    if 0 in by_number:
        rows.append(row("", by_number[0], True))
    for part in st["parts"]:
        pt = part.get("title_fr") if fr and part.get("title_fr") else part["title"]
        rows.append(f'<div class="tp">{esc(ui["part"])} {B.ROMAN[part["number"]]} · {esc(pt)}</div>')
        for num, ctitle in part["chapters"]:
            if num in by_number:
                rows.append(row(num, by_number[num], num in st["spine"]))
    if st.get("appendices"):
        rows.append(f'<div class="tp">{esc(ui["appendices"])}</div>')
        for letter, _ in st["appendices"]:
            if letter in by_letter:
                rows.append(row(letter, by_letter[letter]))
    out.append(f'<section class="pfront toc"><h2>{esc(ui["contents"])}</h2>{"".join(rows)}</section>')

    # body: the preface, then each part (a divider, then its chapters), then the appendices
    def chapter(p):
        stale = False
        sb = B.status_banner(p["meta"], ui) if p["own"] else ""
        spine = f' · {esc(ui["spine"])}' if p["spine"] else ""
        return (f'<article class="pch" data-slug="{p["slug"]}"><div class="ch-eyebrow">{esc(p["eyebrow"])}{spine}</div>'
                f'<h1 class="ch-title">{esc(p["title"])}</h1>{sb}{B.proof_html(p, runs, ui, stale)}'
                f'<div class="ch-rule"></div>{p["body_html"]}</article>')

    if 0 in by_number:
        out.append(chapter(by_number[0]))
    for part in st["parts"]:
        pt = part.get("title_fr") if fr and part.get("title_fr") else part["title"]
        law = part.get("law_fr") if fr and part.get("law_fr") else part.get("law")
        chs = [(n, t) for n, t in part["chapters"] if n in by_number]
        ol = "<br>".join(f'{n} · {esc(by_number[n]["title"])}' for n, _ in chs)
        out.append(f'<section class="ppart"><div class="pn">{esc(ui["part"])} {B.ROMAN[part["number"]]}</div><h2>{esc(pt)}</h2>'
                   + (f'<div class="law">{esc(law[0].upper() + law[1:])}.</div>' if law else "")
                   + f'<div class="ol">{ol}</div></section>')
        for n, _ in chs:
            out.append(chapter(by_number[n]))
    if by_letter:
        out.append(f'<section class="ppart"><div class="pn">{esc(ui["appendices"])}</div><h2>{esc(ui["appendices"])}</h2></section>')
        for letter, _ in st["appendices"]:
            if letter in by_letter:
                out.append(chapter(by_letter[letter]))

    # the open book: the ask and the colophon line on the last page (house OPEN-BOOK.md, HOUSE-11)
    out.append(f'<section class="pfront colophon ask"><p class="warn">{esc(ui["ask"])}</p>'
               f'<p>{esc(ui["ask_btn"])} : {esc(ui["offer_url"])}</p>'
               f'<p>{esc(ui["colophon"])}</p><p>{esc(ui["licence_url"])}</p></section>')
    back = st["back_cover"]
    out.append(f'<section class="pback"><div class="bl bl-first">{esc(series.upper())}</div>'
               + "".join(f'<div class="bl">{esc(l)}</div>' for l in back)
               + '<div class="im">AYOUNI</div></section>')
    out.append("</body></html>")
    return "\n".join(out)


def render_pdf(html_path, pdf_path):
    prof = tempfile.mkdtemp(prefix="stzbook-chrome-")
    cmd = [str(CHROME), "--headless=new", "--disable-gpu", f"--user-data-dir={prof}", "--no-pdf-header-footer",
           "--no-first-run", "--disable-extensions", f"--print-to-pdf={pdf_path}", html_path.as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if not pdf_path.exists() or pdf_path.stat().st_size < 10_000:
        raise SystemExit(f"Chrome did not write {pdf_path}: {r.stderr[-600:]}")


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def find_pages(pdf_path, pages, toc_end):
    """The page (1-based) on which each chapter begins: the first page after the contents whose text holds
    the chapter's eyebrow and its title."""
    rd = PdfReader(str(pdf_path))
    texts = [norm(pg.extract_text() or "") for pg in rd.pages]
    found, start = {}, toc_end
    for p in pages:
        eb, ti = norm(p["eyebrow"]), norm(p["title"])
        for i in range(start, len(texts)):
            t = texts[i]
            if ti in t and (eb in t or p["number"] == 0 or p.get("appendix")):
                if p.get("appendix") and eb not in t:
                    continue
                found[p["slug"]] = i + 1
                start = i
                break
    return found, len(rd.pages), texts


def build(lang, html_only=False):
    st = structure()
    runs = load_json("book-run.json", {})
    guards = load_json("guards.json", {})
    en_src = sources("en")
    src = sources(lang)
    by_id = {m["id"]: (p, m, b) for p, m, b in src}
    ui = B.UI[lang]
    pages = B.build_pages(lang, st, en_src, by_id, runs, guards, ui)
    pages = [p for p in pages if p["own"]]
    OUT.mkdir(exist_ok=True)
    html_path = OUT / f"{lang}.html"
    pdf_path = OUT / f"softanza-{lang}.pdf"
    pgmap = {}
    doc = compose(lang, st, pages, runs, guards, ui, pgmap)
    html_path.write_text(doc, encoding="utf-8")
    if html_only:
        print(f"wrote {html_path.relative_to(ROOT)}")
        return
    render_pdf(html_path, pdf_path)
    # the contents are 1 cover + half title + title + colophon + n pages; find where the first chapter begins
    first, total, _ = find_pages(pdf_path, pages, 4)
    pgmap = dict(first)
    html_path.write_text(compose(lang, st, pages, runs, guards, ui, pgmap), encoding="utf-8")
    render_pdf(html_path, pdf_path)
    final, total, texts = find_pages(pdf_path, pages, 4)
    if final != pgmap:
        # the contents changed length between passes; one more round settles it
        pgmap = dict(final)
        html_path.write_text(compose(lang, st, pages, runs, guards, ui, pgmap), encoding="utf-8")
        render_pdf(html_path, pdf_path)
        final, total, texts = find_pages(pdf_path, pages, 4)
    missing = [p["slug"] for p in pages if p["slug"] not in final]
    if missing:
        raise SystemExit(f"{lang}: the first page of {missing} was not found in the PDF")
    if final != pgmap:
        raise SystemExit(f"{lang}: the contents' page numbers did not settle")
    size = pdf_path.stat().st_size // 1024
    print(f"{lang}: {pdf_path.relative_to(ROOT)}  {total} pages, {size} KB, {len(pages)} chapters, contents numbered")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    langs = args or ["en", "fr"]
    for lang in langs:
        build(lang, html_only="--html" in sys.argv)


if __name__ == "__main__":
    main()
