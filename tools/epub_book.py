#!/usr/bin/env python3
"""The ePub edition: the book as a reflowable EPUB 3 file, one per language.

    python tools/epub_book.py           # en and fr
    python tools/epub_book.py en        # one language

Made from the same pages as the reader and the PDF (`build_book.build_pages`): the same verdict under each block,
the same proof line, the same draft banner. Writes print/softanza-<lang>.epub, then checks its own file: every part is
well-formed XML, every manifest item exists, every id is unique, every internal link points at a page of the book.
No network. The file is deterministic for a given build (its identifier is a hash of the title, the language and the
library commit), so rebuilding an unchanged book gives the same identifier.

epubcheck (the W3C's validator) is not on this machine; this tool checks what it can and says so.
"""
import hashlib, html, re, sys, zipfile
from pathlib import Path
from lxml import etree, html as lhtml

import build_book as B
from book_common import ROOT, sources, structure, load_json, now

OUT = ROOT / "print"
XHTML = "http://www.w3.org/1999/xhtml"
CSS_EXTRA = """
:root { --code-bg: #f4f1e8; --code-rule: #d9d3c2; --code-ink: #1a1612; --code-kw: #a24a0c; --code-str: #3b6b3a;
  --code-num: #1f6a5a; --code-com: #6b6358; --code-promise: #5a4a2a; --code-label: #6b6358; }
html, body { background: #fff; color: #1a1612; margin: 0; padding: 0; }
body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.5; padding: 0 0.6em; }
.ep-eyebrow { font: 700 0.7em Arial, sans-serif; letter-spacing: 0.15em; text-transform: uppercase; color: #6b6358; margin-top: 1.2em; }
.ep-title { font: 800 1.7em/1.15 Arial, sans-serif; margin: 0.3em 0 0.5em; }
.cell, pre { white-space: pre-wrap; overflow-wrap: anywhere; font-family: Consolas, 'Courier New', monospace; font-size: 0.78em; }
.code-cell { border: 1px solid #d9d3c2; background: #f4f1e8; margin: 0.8em 0; }
.code-cell pre { margin: 0; padding: 0.5em 0.7em; }
table { border-collapse: collapse; width: 100%; font-size: 0.85em; }
th, td { border-bottom: 1px solid #d9d3c2; padding: 0.3em 0.4em; text-align: left; vertical-align: top; overflow-wrap: anywhere; }
.proof, .proof-engine, .status-banner { font: 0.72em/1.45 Arial, sans-serif; color: #3a3326; }
.status-banner { display: inline-block; border: 1px solid #1a1612; padding: 0 0.5em; font-weight: 700; }
img.cover { width: 100%; height: auto; display: block; margin: 0 auto; }
nav ol { list-style: none; padding-left: 1em; }
"""


def esc(s):
    return html.escape(s, quote=True)


def to_xhtml_fragment(markup, names):
    """Reserialise HTML as XML so an XHTML reader accepts it: closed tags, escaped entities, the SVG namespace,
    and the reader's own links (#slug) turned into links between the book's files."""
    root = lhtml.fragment_fromstring(markup, create_parent="div")
    for a in list(root.iter("a")):
        h = a.get("href") or ""
        if h.startswith("#") and h[1:] in names:
            a.set("href", names[h[1:]] + h)
        elif h and not h.startswith(("http://", "https://", "mailto:", "#")):
            a.drop_tag()                 # a path into the repository or the site: not a place in this file
    out = (root.text or "") + "".join(etree.tostring(ch, method="xml", encoding="unicode", with_tail=True) for ch in root)
    out = re.sub(r"<svg(?![^>]*xmlns=)", '<svg xmlns="http://www.w3.org/2000/svg"', out)
    out = re.sub(r"\sxmlns=\"http://www\.w3\.org/1999/xhtml\"", "", out)
    return out


def page_xhtml(p, runs, ui, lang, names):
    body = to_xhtml_fragment(
        f'<div class="ep-eyebrow">{esc(p["eyebrow"])}</div><h1 class="ep-title">{esc(p["title"])}</h1>'
        f'{B.status_banner(p["meta"], ui) if p["own"] else ""}{B.proof_html(p, runs, ui, False)}{p["body_html"]}', names)
    return (f'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n<html xmlns="{XHTML}" xmlns:epub="http://www.idpf.org/2007/ops" '
            f'lang="{lang}" xml:lang="{lang}"><head><meta charset="utf-8"/><title>{esc(p["title"])}</title>'
            f'<link rel="stylesheet" type="text/css" href="style.css"/></head><body><section epub:type="chapter" id="{p["slug"]}">{body}</section></body></html>\n')


def build(lang):
    st = structure()
    runs = load_json("book-run.json", {})
    guards = load_json("guards.json", {})
    en_src = sources("en")
    by_id = {m["id"]: (p, m, b) for p, m, b in sources(lang)}
    ui = B.UI[lang]
    pages = [p for p in B.build_pages(lang, st, en_src, by_id, runs, guards, ui) if p["own"]]
    fr = lang == "fr"
    title = st["fr"]["title"] if fr else st["title"]
    sub = st["fr"]["subtitle"] if fr else st["subtitle"]
    tag = st["fr"]["tagline"] if fr else st["tagline"]
    sha = runs.get("run", {}).get("library", {}).get("commit", "main")
    uid = "urn:uuid:" + str(__import__("uuid").UUID(hashlib.sha1(f"{title}|{lang}|{sha}".encode()).hexdigest()[:32]))
    modified = now().strftime("%Y-%m-%dT%H:%M:%SZ")
    cover = ROOT / "assets" / "cover" / ("cover.fr.png" if fr else "cover.png")

    css = B.apply_shell(ui)[0]
    m = re.search(r"<style>(.*?)</style>", css, re.S)
    stylesheet = (m.group(1) if m else "") + CSS_EXTRA

    files = {}   # path in the zip -> bytes
    cover_x = (f'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n<html xmlns="{XHTML}" lang="{lang}" xml:lang="{lang}"><head>'
               f'<meta charset="utf-8"/><title>{esc(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>'
               f'<body><img class="cover" src="cover.png" alt="{esc(ui["cover_alt"])}"/></body></html>\n')
    files["OEBPS/cover.xhtml"] = cover_x.encode()
    files["OEBPS/cover.png"] = cover.read_bytes()
    files["OEBPS/style.css"] = stylesheet.encode()
    names = {p["slug"]: f"p{k:02d}-{p['slug']}.xhtml" for k, p in enumerate(pages)}
    for p in pages:
        files["OEBPS/" + names[p["slug"]]] = page_xhtml(p, runs, ui, lang, names).encode()

    # the navigation document: preface, parts with their chapters, appendices
    by_number = {p["number"]: p for p in pages}
    by_letter = {str(p["appendix"]): p for p in pages if p.get("appendix")}
    items = []
    if 0 in by_number:
        items.append(f'<li><a href="{names["preface"]}">{esc(by_number[0]["title"])}</a></li>')
    for part in st["parts"]:
        pt = part.get("title_fr") if fr and part.get("title_fr") else part["title"]
        chs = [by_number[n] for n, _ in part["chapters"] if n in by_number]
        lis = "".join(f'<li><a href="{names[c["slug"]]}">{c["number"]} · {esc(c["title"])}</a></li>' for c in chs)
        items.append(f'<li><span>{esc(ui["part"])} {B.ROMAN[part["number"]]} · {esc(pt)}</span><ol>{lis}</ol></li>')
    if by_letter:
        lis = "".join(f'<li><a href="{names[by_letter[l]["slug"]]}">{l} · {esc(by_letter[l]["title"])}</a></li>'
                      for l, _ in st["appendices"] if l in by_letter)
        items.append(f'<li><span>{esc(ui["appendices"])}</span><ol>{lis}</ol></li>')
    nav = (f'<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n<html xmlns="{XHTML}" xmlns:epub="http://www.idpf.org/2007/ops" '
           f'lang="{lang}" xml:lang="{lang}"><head><meta charset="utf-8"/><title>{esc(ui["contents"])}</title>'
           f'<link rel="stylesheet" type="text/css" href="style.css"/></head><body><nav epub:type="toc" id="toc"><h1>{esc(ui["contents"])}</h1>'
           f'<ol>{"".join(items)}</ol></nav></body></html>\n')
    files["OEBPS/nav.xhtml"] = nav.encode()

    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="cover-image" href="cover.png" media-type="image/png" properties="cover-image"/>',
                '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>']
    spine = ['<itemref idref="cover" linear="no"/>', '<itemref idref="nav" linear="no"/>']
    for k, p in enumerate(pages):
        manifest.append(f'<item id="i{k:02d}" href="{names[p["slug"]]}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="i{k:02d}"/>')
    n_draft = sum(1 for p in pages if p["meta"].get("status", "draft") == "draft")
    desc = (f"{tag}. " + (f"Épreuve de travail : {n_draft} pages sur {len(pages)} sont des brouillons non lus par l'auteur."
                          if fr else f"Proof copy: {n_draft} of {len(pages)} pages are drafts not yet read by the author."))
    opf = (f'<?xml version="1.0" encoding="utf-8"?>\n<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{lang}">'
           f'<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bookid">{uid}</dc:identifier>'
           f'<dc:title>{esc(title)} — {esc(sub)}</dc:title><dc:creator>Mansour Ayouni</dc:creator><dc:language>{lang}</dc:language>'
           f'<dc:publisher>AYOUNI</dc:publisher><dc:description>{esc(desc)}</dc:description>'
           f'<meta property="dcterms:modified">{modified}</meta><meta name="cover" content="cover-image"/></metadata>'
           f'<manifest>{"".join(manifest)}</manifest><spine>{"".join(spine)}</spine></package>\n')
    files["OEBPS/content.opf"] = opf.encode()
    files["META-INF/container.xml"] = ('<?xml version="1.0" encoding="utf-8"?>\n<container version="1.0" '
        'xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" '
        'media-type="application/oebps-package+xml"/></rootfiles></container>\n').encode()

    OUT.mkdir(exist_ok=True)
    path = OUT / f"softanza-{lang}.epub"
    with zipfile.ZipFile(path, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)   # first, stored
        for name, data in files.items():
            z.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)
    problems = check(path)
    if problems:
        raise SystemExit(f"{lang}: the ePub fails its own check:\n  " + "\n  ".join(problems[:20]))
    print(f"{lang}: {path.relative_to(ROOT)}  {len(pages)} pages, {path.stat().st_size // 1024} KB, checked (not by epubcheck)")


def check(path):
    problems = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if names[0] != "mimetype" or z.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            problems.append("mimetype must be the first entry, stored")
        trees = {}
        for n in names:
            if n.endswith((".xhtml", ".opf", ".xml")):
                try:
                    trees[n] = etree.fromstring(z.read(n))
                except etree.XMLSyntaxError as e:
                    problems.append(f"{n}: not well-formed XML: {e}")
        opf = trees.get("OEBPS/content.opf")
        if opf is None:
            return problems + ["no content.opf"]
        ns = {"o": "http://www.idpf.org/2007/opf"}
        ids, hrefs = [], set()
        for it in opf.findall(".//o:manifest/o:item", ns):
            ids.append(it.get("id")); hrefs.add(it.get("href"))
            if "OEBPS/" + it.get("href") not in names:
                problems.append(f"manifest item {it.get('href')} is not in the file")
        if len(ids) != len(set(ids)):
            problems.append("duplicate manifest ids")
        for ref in opf.findall(".//o:spine/o:itemref", ns):
            if ref.get("idref") not in ids:
                problems.append(f"spine item {ref.get('idref')} is not in the manifest")
        for n in names:
            if n.startswith("OEBPS/") and n.endswith(".xhtml") and n[6:] not in hrefs:
                problems.append(f"{n} is in the file and not in the manifest")
        # every internal link of a page must point at a file of the book
        for n, tree in trees.items():
            if not n.endswith(".xhtml"):
                continue
            for a in tree.iter("{%s}a" % XHTML):
                h = a.get("href") or ""
                if h and not h.startswith(("http://", "https://", "mailto:", "#")):
                    target = h.split("#")[0]
                    if target and target not in hrefs:
                        problems.append(f"{n}: link to {h}, which is not a file of the book")
    return problems


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    for lang in args or ["en", "fr"]:
        build(lang)


if __name__ == "__main__":
    main()
