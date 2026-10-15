#!/usr/bin/env python3
"""Build the Softanza book: run it, read its guards, and write the reader, the status page and the agents' files.

    python tools/build_book.py                # run every block, read every guard, then render
    python tools/build_book.py --render-only  # render from data/ as it stands (no run)

Writes:
  en/index.html, fr/index.html   the reader, one self-contained file per language (the Refine reader's choice)
  index.html                     opens the English reader
  status.html                    every chapter: status, run verdict, guards, words, French, done
  book.json, llms-book.txt       the book as data, for the agent that reads it

The reader's shell is the Refine book's, copied unchanged into reader/shell.refine.html; every change
this book makes to it is one named transformation below (SHELL_EDITS), asserted to apply exactly once,
so the lineage is checkable line by line (FORMAT.md).

The build FAILS (exit status 1) when: a chapter's runnable blocks did not all keep their promise;
a block changed since it was last run; a named guard does not exist; a fence still carries the former
host language's name. It still writes every page first, so the failure is visible where it happened.
"""
import html, json, re, subprocess, sys, urllib.parse
from book_schema import validate
from book_common import (ROOT, SRC, sources, structure, code_blocks, block_hash, former_name_fences,
                         load_json, now, stamp)
from book_judge import WORDS

SITE_BASE = "../../../../stzsite/"   # the site's pages, relative to en/ and fr/; structure.yaml's site_base overrides
ROMAN = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

# ============================================================================ UI words
UI = {
  "en": {
    "lang": "en", "other": "fr", "part": "Part", "chapter": "Chapter", "preface": "Preface",
    "spine": "Spine", "spine_title": "One of the nine spine chapters: they carry the whole argument and can be read alone",
    "spine_only": "Read the spine only", "all_chapters": "Show every chapter",
    "draft": "Draft · not yet read by the author", "read": "Read by the author", "final": "Final",
    "missing": "Missing · the source has not been received",
    "proof": "Run on {d} inside the library at commit {sha}: {k} of {n} blocks kept their promise.",
    "proof_none": "This page has no code to run.",
    "engine": "The blocks were run by the runtime of the former host language, version {v}; Haro does not run the library yet. {eng}",
    "eng_at": "The engine binaries were built in a checkout of this commit, newest built {d}; {n} engine change(s) committed after that build are not in them.",
    "eng_at0": "The engine binaries were built in a checkout of this commit, newest built {d}.",
    "eng_copy": "The engine binaries were copied from the library's working checkout, newest built {d}; they are not pinned to this commit.",
    "stale": "This page's code changed after its last run; its verdicts are not shown until it runs again.",
    "contents": "Contents", "not_drafted": "not yet drafted", "words": "words",
    "decision": "The decision, and what was refused",
    "court_head": "Read from the library's test tree at commit {sha} on {d}. The figure is the number of assertions the guard holds, counted in its file; the site shows each one run.",
    "assertions": "assertions", "guard_missing": "this guard does not exist in the test tree",
    "stage": {"built": "built", "designed": "designed", "absent": "absent"},
    "doors_h": ["Door", "What you take from this chapter"],
    "untranslated": "This chapter is not yet written in English.",
    "read_other": "Read it in French",
    "prev": "← Previous", "next": "Next →",
    "series": "Second of the AYOUNI books", "back_cover": "From the back cover",
    "cover_alt": "Softanza, book cover",
    "description": "Softanza, the Governed Software Platform of the AI Age: declare what you know, a court keeps it, the AI model comes last. Rethinking programming, languages and intelligence, from first principles. By Mansour Ayouni. Second of the AYOUNI books.",
    "theme": "Light or dark", "langs": "Language",
    "status_link": "Status of the book", "agents_link": "For agents",
    # the open book (house OPEN-BOOK.md, HOUSE-11): the ask and the colophon line, word for word; the links are the house's pages
    "invite": "If this book is useful to your organisation, I work with organisations on its subjects: paper copies in quantity, workshops and training, talks, consulting and the building of solutions. Write to ", "invite_mail": "kalidianow@gmail.com", "offer_link": "How these books are offered",
    "colophon": "Free to read and share under CC BY-NC-ND 4.0; code under the library's licence.",
    "offer_url": "https://mayouni.github.io/ayouni/offer/", "licence_url": "https://mayouni.github.io/ayouni/licence/",
    "pdf_public": "../book.en.pdf", "pdf_local": "../print/softanza-en.pdf",
    "src_head": "Where the evidence lives", "src_narration": "Narration", "src_site": "On the site",
    "src_rulings": "Rulings of the study",
    "appendix": "Appendix", "appendices": "Appendices",
  },
  "fr": {
    "lang": "fr", "other": "en", "part": "Partie", "chapter": "Chapitre", "preface": "Préface",
    "spine": "Colonne", "spine_title": "Un des neuf chapitres de la colonne : ils portent tout l'argument et se lisent seuls",
    "spine_only": "Lire la colonne seule", "all_chapters": "Montrer tous les chapitres",
    "draft": "Brouillon · traduit d'un brouillon anglais, pas encore lu par l'auteur", "read": "Lu par l'auteur", "final": "Final",
    "missing": "Manquant · la source n'a pas été reçue",
    "proof": "Exécuté le {d} dans la bibliothèque au commit {sha} : {k} bloc(s) sur {n} ont tenu leur promesse.",
    "proof_none": "Cette page n'a pas de code à exécuter.",
    "engine": "Les blocs ont été exécutés par le runtime de l'ancien langage hôte, version {v} ; Haro n'exécute pas encore la bibliothèque. {eng}",
    "eng_at": "Les binaires du moteur ont été construits dans une copie de ce commit, le plus récent le {d} ; {n} changement(s) du moteur commité(s) après cette construction n'y sont pas.",
    "eng_at0": "Les binaires du moteur ont été construits dans une copie de ce commit, le plus récent le {d}.",
    "eng_copy": "Les binaires du moteur ont été copiés depuis la copie de travail de la bibliothèque, le plus récent construit le {d} ; ils ne sont pas liés à ce commit.",
    "stale": "Le code de cette page a changé depuis sa dernière exécution ; ses verdicts ne sont pas montrés avant qu'elle soit exécutée à nouveau.",
    "contents": "Sommaire", "not_drafted": "pas encore rédigé", "words": "mots",
    "decision": "La décision, et ce qui a été refusé",
    "court_head": "Lu dans l'arbre de tests de la bibliothèque au commit {sha} le {d}. Le chiffre est le nombre d'assertions que la garde contient, compté dans son fichier ; le site montre chacune exécutée.",
    "assertions": "assertions", "guard_missing": "cette garde n'existe pas dans l'arbre de tests",
    "stage": {"built": "construit", "designed": "conçu", "absent": "absent"},
    "doors_h": ["Porte", "Ce que vous retirez de ce chapitre"],
    "untranslated": "Ce chapitre n'est pas encore écrit en français. Le français est rédigé à partir de l'anglais que l'auteur a marqué « lu ».",
    "read_other": "Le lire en anglais",
    "prev": "← Précédent", "next": "Suivant →",
    "series": "Deuxième des livres AYOUNI", "back_cover": "Quatrième de couverture",
    "cover_alt": "Softanza, couverture du livre",
    "description": "Softanza, la plateforme logicielle gouvernée de l'ère de l'IA : déclarez ce que vous savez, un tribunal le garde, le modèle d'IA vient en dernier. Repenser la programmation, ses langages et son intelligence depuis les premiers principes. Par Mansour Ayouni. Deuxième des livres AYOUNI.",
    "theme": "Clair ou sombre", "langs": "Langue",
    "status_link": "État du livre", "agents_link": "Pour les agents",
    "invite": "Si ce livre est utile à votre organisation, je travaille avec les organisations sur ses sujets : exemplaires papier en quantité, ateliers et formations, conférences, conseil et réalisation de solutions. Écrivez à ", "invite_mail": "kalidianow@gmail.com", "offer_link": "Comment ces livres sont offerts",
    "colophon": "Libre à lire et à partager sous CC BY-NC-ND 4.0 ; le code sous la licence de la bibliothèque.",
    "offer_url": "https://mayouni.github.io/ayouni/fr/offre/", "licence_url": "https://mayouni.github.io/ayouni/fr/licence/",
    "pdf_public": "../book.fr.pdf", "pdf_local": "../print/softanza-fr.pdf",
    "src_head": "Où sont les preuves", "src_narration": "Narration", "src_site": "Sur le site",
    "src_rulings": "Décisions de l'étude",
    "appendix": "Annexe", "appendices": "Annexes",
  },
}

# ============================================================================ colours: every one a variable
LIGHT = {
  "--ink": "#1a1612", "--ink-soft": "#3a3326", "--soft": "#6b6358", "--soft-2": "#9a9078",
  "--paper": "#ffffff", "--bg": "#fbfaf6", "--rule": "#e3ddc9", "--rule-strong": "#1a1612",
  "--hover-bg": "#f3eedf", "--hover-bg-soft": "#fcfaf5", "--card-bg": "#ffffff", "--sidebar-bg": "#f5f0e2",
  "--bookmark": "#E96A1A", "--bookmark-text": "#b3480a",
  "--shadow-cover": "rgba(40, 30, 18, 0.16)", "--shadow-soft": "rgba(40, 30, 18, 0.08)",
  "--shadow-side": "rgba(0, 0, 0, 0.12)", "--scrim": "rgba(26, 22, 18, 0.45)", "--scrim-search": "rgba(26, 22, 18, 0.42)",
  "--shadow-panel": "rgba(26, 22, 18, 0.28)", "--shadow-pill": "rgba(26, 22, 18, 0.18)",
  "--mark": "rgba(233, 106, 26, 0.20)", "--mark-strong": "rgba(233, 106, 26, 0.25)",
  "--flash": "rgba(233, 106, 26, 0.22)", "--flash-0": "rgba(233, 106, 26, 0)", "--print-bg": "#ffffff",
  "--code-bg": "#211c15", "--code-rule": "#35302a", "--code-ink": "#e8e1d1", "--code-kw": "#f0914f",
  "--code-str": "#a9c795", "--code-num": "#82c0ae", "--code-com": "#8d8471", "--code-promise": "#d8c3a5",
  "--code-label": "#a39a88",
  "--ok": "#2f6b3f", "--ok-bg": "#e8f0e6", "--bad": "#a3392b", "--bad-bg": "#f6e5e0",
  "--neutral": "#5d564b", "--neutral-bg": "#eee9dc", "--designed": "#2f5d7c", "--designed-bg": "#e3ecf2",
  "--decision-bg": "#f3eee2", "--cover-bg": "#1a1612", "--cover-ink": "#fbfaf6", "--cover-soft": "#bdb4a2",
  "--cover-accent": "#E96A1A",
}
DARK = {
  "--ink": "#ece6da", "--ink-soft": "#cfc6b4", "--soft": "#a39a88", "--soft-2": "#7d7565",
  "--paper": "#1d1a16", "--bg": "#14120f", "--rule": "#3a342b", "--rule-strong": "#ece6da",
  "--hover-bg": "#2a251e", "--hover-bg-soft": "#221e19", "--card-bg": "#1d1a16", "--sidebar-bg": "#191612",
  "--bookmark": "#ef7a2e", "--bookmark-text": "#f4a066",
  "--shadow-cover": "rgba(0, 0, 0, 0.55)", "--shadow-soft": "rgba(0, 0, 0, 0.35)",
  "--shadow-side": "rgba(0, 0, 0, 0.5)", "--scrim": "rgba(0, 0, 0, 0.6)", "--scrim-search": "rgba(0, 0, 0, 0.58)",
  "--shadow-panel": "rgba(0, 0, 0, 0.6)", "--shadow-pill": "rgba(0, 0, 0, 0.5)",
  "--mark": "rgba(239, 122, 46, 0.28)", "--mark-strong": "rgba(239, 122, 46, 0.34)",
  "--flash": "rgba(239, 122, 46, 0.26)", "--flash-0": "rgba(239, 122, 46, 0)", "--print-bg": "#ffffff",
  "--code-bg": "#0f0d0b", "--code-rule": "#2e2923", "--code-ink": "#e8e1d1", "--code-kw": "#f0914f",
  "--code-str": "#a9c795", "--code-num": "#82c0ae", "--code-com": "#8d8471", "--code-promise": "#d8c3a5",
  "--code-label": "#8d8471",
  "--ok": "#8cc79a", "--ok-bg": "#1f2d22", "--bad": "#e99484", "--bad-bg": "#3a211c",
  "--neutral": "#b9b0a0", "--neutral-bg": "#2a261f", "--designed": "#8fb7d3", "--designed-bg": "#1d2a33",
  "--decision-bg": "#1f1b16", "--cover-bg": "#0f0d0b", "--cover-ink": "#f3eee3", "--cover-soft": "#a39a88",
  "--cover-accent": "#ef7a2e",
}


def css_vars(d):
    return " ".join(f"{k}: {v};" for k, v in d.items())


# ============================================================================ the shell, transformed
# Each edit: (name, old, new). Applied in order; each must match exactly once in the Refine shell.
FONT_FACES = """@font-face { font-family: 'EB Garamond'; font-style: normal; font-weight: 400 800; font-display: swap;
  src: local('EB Garamond'), local('EBGaramond-Regular'), url('../assets/fonts/EBGaramond-normal.woff2') format('woff2'); }
@font-face { font-family: 'EB Garamond'; font-style: italic; font-weight: 400 800; font-display: swap;
  src: local('EB Garamond Italic'), local('EBGaramond-Italic'), url('../assets/fonts/EBGaramond-italic.woff2') format('woff2'); }
@font-face { font-family: 'Inter'; font-style: normal; font-weight: 400 800; font-display: swap;
  src: local('Inter'), local('Inter-Regular'), url('../assets/fonts/Inter-normal.woff2') format('woff2'); }
@font-face { font-family: 'Archivo Black'; font-style: normal; font-weight: 400; font-display: swap;
  src: local('Archivo Black'), local('ArchivoBlack-Regular'), url('../assets/fonts/ArchivoBlack-normal.woff2') format('woff2'); }
"""


def shell_edits(ui):
    return [
        ("html lang", '<html lang="en">', f'<html lang="{ui["lang"]}">'),
        ("title", "<title>Refinement-Oriented Programming — AYOUNI</title>", "<title>Softanza — AYOUNI</title>"),
        ("description",
         '<meta name="description" content="A discipline for software in the agentic era. By Mansour Ayouni. First book from the AYOUNI imprint.">',
         f'<meta name="description" content="{html.escape(ui["description"])}">\n'
         '<script>try{var t=localStorage.getItem("softanza-theme");if(t)document.documentElement.setAttribute("data-theme",t);}catch(e){}</script>'),
        ("no CDN: the fonts are local files, with the same families and the same fallbacks",
         '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n',
         ""),
        ("font faces", "<style>\n:root {", "<style>\n" + FONT_FACES + ":root {"),
        ("the print icon opens the book's PDF, never a page the browser generates (OPEN-BOOK, HOUSE-11)",
         "  btnPrint.addEventListener('click', () => window.print());",
         f"  btnPrint.addEventListener('click', () => {{ const served = /\\/books\\/[^/]+\\/(en|fr)\\/(index\\.html)?$/.test(location.pathname); "
         f"window.open(served ? '{ui['pdf_public']}' : '{ui['pdf_local']}', '_blank', 'noopener'); }});"),
        ("the menu keeps the current page at its top", "    // Scroll to top of content\n    window.scrollTo({ top: 0, behavior: 'instant' });", "    // Scroll to top of content\n    window.scrollTo({ top: 0, behavior: 'instant' });\n\n    // the current page is underlined in the menu and brought to its top (the menu is visible now)\n    const sbEl = document.querySelector('.chapter-sidebar');\n    const cur = sbEl && sbEl.querySelector('.sidebar-link.active');\n    if (cur) { sbEl.scrollTo({ top: Math.max(0, cur.getBoundingClientRect().top - sbEl.getBoundingClientRect().top + sbEl.scrollTop - 24), behavior: 'instant' }); }"),
        ("colours: hero shadow", "box-shadow: 0 16px 48px rgba(40, 30, 18, 0.16), 0 4px 12px rgba(40, 30, 18, 0.08);",
         "box-shadow: 0 16px 48px var(--shadow-cover), 0 4px 12px var(--shadow-soft);"),
        ("colours: card shadow", "box-shadow: 0 8px 20px rgba(40, 30, 18, 0.08);", "box-shadow: 0 8px 20px var(--shadow-soft);"),
        ("colours: sidebar shadow", "box-shadow: 4px 0 20px rgba(0,0,0,0.12);", "box-shadow: 4px 0 20px var(--shadow-side);"),
        ("colours: backdrop", "background: rgba(26, 22, 18, 0.45);", "background: var(--scrim);"),
        ("colours: search scrim", "background: rgba(26, 22, 18, 0.42);", "background: var(--scrim-search);"),
        ("colours: search panel", "box-shadow: 0 18px 50px rgba(26, 22, 18, 0.28);", "box-shadow: 0 18px 50px var(--shadow-panel);"),
        ("colours: search hover", ".search-hit:hover { background: #fcfaf5; }", ".search-hit:hover { background: var(--hover-bg-soft); }"),
        ("colours: search mark", "background: rgba(233, 106, 26, 0.20);", "background: var(--mark);"),
        ("colours: term mark", "background: rgba(233, 106, 26, 0.25);", "background: var(--mark-strong);"),
        ("colours: pill shadow", "box-shadow: 0 6px 24px rgba(26, 22, 18, 0.18);", "box-shadow: 0 6px 24px var(--shadow-pill);"),
        ("colours: flash",
         "0%   { background: rgba(233, 106, 26, 0.22); box-shadow: 0 0 0 6px rgba(233, 106, 26, 0.22); }\n  100% { background: transparent; box-shadow: 0 0 0 6px rgba(233, 106, 26, 0); }",
         "0%   { background: var(--flash); box-shadow: 0 0 0 6px var(--flash); }\n  100% { background: transparent; box-shadow: 0 0 0 6px var(--flash-0); }"),
        ("colours: print", "body { background: white; font-size: 11pt; }", "body { background: var(--print-bg); font-size: 11pt; }"),
        ("breadcrumb: the book's name", '<a href="#" class="bc-book" id="bcBook">Refinement-Oriented Programming</a>',
         '<a href="#" class="bc-book" id="bcBook">Softanza</a>'),
        ("header: language and theme",
         '  <div class="hdr-section hdr-right">\n',
         '  <div class="hdr-section hdr-right">\n'
         f'    <div class="lang-toggle" role="group" aria-label="{ui["langs"]}">'
         f'<a href="../en/index.html" class="lang-link{" active" if ui["lang"] == "en" else ""}" data-lang="en" hreflang="en">EN</a>'
         f'<a href="../fr/index.html" class="lang-link{" active" if ui["lang"] == "fr" else ""}" data-lang="fr" hreflang="fr">FR</a></div>\n'
         f'    <button class="circle-btn" id="btnTheme" aria-label="{ui["theme"]}" title="{ui["theme"]}">'
         '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>\n'),
        ("script: theme, spine, language",
         "  // Initial route\n  handleHash();",
         "  // THEME (book): light and dark as first-class themes; the reader's choice is kept\n"
         "  const btnTheme = document.getElementById('btnTheme');\n"
         "  function currentTheme() {\n"
         "    const t = root.getAttribute('data-theme');\n"
         "    if (t) return t;\n"
         "    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';\n"
         "  }\n"
         "  btnTheme.addEventListener('click', () => {\n"
         "    const next = currentTheme() === 'dark' ? 'light' : 'dark';\n"
         "    root.setAttribute('data-theme', next);\n"
         "    try { localStorage.setItem('softanza-theme', next); } catch (e) {}\n"
         "  });\n"
         "  // SPINE (book): the nine chapters that carry the argument alone\n"
         "  const spineButtons = Array.from(document.querySelectorAll('.spine-toggle'));\n"
         "  function applySpine(on) {\n"
         "    document.body.classList.toggle('spine-only', on);\n"
         "    spineButtons.forEach(b => { b.setAttribute('aria-pressed', on ? 'true' : 'false'); b.textContent = on ? b.dataset.off : b.dataset.on; });\n"
         "    try { localStorage.setItem('softanza-spine', on ? '1' : '0'); } catch (e) {}\n"
         "  }\n"
         "  spineButtons.forEach(b => b.addEventListener('click', () => applySpine(!document.body.classList.contains('spine-only'))));\n"
         "  try { if (localStorage.getItem('softanza-spine') === '1') applySpine(true); } catch (e) {}\n"
         "  // LANGUAGE (book): the toggle keeps the page you are on\n"
         "  const langLinks = Array.from(document.querySelectorAll('.lang-link'));\n"
         "  function syncLang() { langLinks.forEach(a => { a.href = '../' + a.dataset.lang + '/index.html' + window.location.hash; }); }\n"
         "  window.addEventListener('hashchange', syncLang);\n"
         "  syncLang();\n\n"
         "  // Initial route\n  handleHash();"),
    ]


def apply_shell(ui):
    shell = (ROOT / "reader" / "shell.refine.html").read_text(encoding="utf-8").replace("\r", "")
    for name, old, new in shell_edits(ui):
        n = shell.count(old)
        if n != 1:
            raise SystemExit(f"shell edit '{name}' matched {n} times; the Refine shell changed, re-read it")
        shell = shell.replace(old, new)
    # the theme variables: the Refine :root block is replaced by the book's light set, then dark is added
    root_block = re.search(r":root \{\n(.*?)\n\}", shell, re.S)
    fonts_and_sizes = "\n".join(l for l in root_block.group(1).split("\n") if not re.search(r"#[0-9a-fA-F]{3,6}", l))
    themed = (":root {\n" + fonts_and_sizes + "\n  " + css_vars(LIGHT) + "\n}\n"
              ":root[data-theme=\"dark\"] { " + css_vars(DARK) + " color-scheme: dark; }\n"
              "@media (prefers-color-scheme: dark) { :root:not([data-theme=\"light\"]) { " + css_vars(DARK) + " color-scheme: dark; } }\n"
              "@media print { :root, :root[data-theme=\"dark\"], :root:not([data-theme=\"light\"]) { " + css_vars(LIGHT) + " } }")
    shell = shell[:root_block.start()] + themed + shell[root_block.end():]
    shell = shell.replace("</style>", BOOK_CSS + type_css() + "\n</style>", 1)
    OV = "<!-- ============ OVERVIEW VIEW ============ -->"
    return shell[:shell.index(OV)], shell[shell.index("<script>"):]


def check_colours(page):
    """Every colour behind a variable: no literal colour outside the variable sets (the mask's #000 is an alpha mask)."""
    css = "\n".join(re.findall(r"<style>(.*?)</style>", page, re.S))
    css = re.sub(r":root[^{]*\{[^}]*\}", "", css)
    css = re.sub(r"@media \((?:prefers-color-scheme|print)[^{]*\{\s*:root[^{]*\{[^}]*\}\s*\}", "", css)
    css = css.replace("#000 70%", "")
    return sorted(set(re.findall(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|\bwhite\b(?!-space)", css)))


# ============================================================================ the book's own CSS
BOOK_CSS = """
/* ---- from the Refine build's additions (web/build.py EXTRA_CSS), colours made variables ---- */
.ch-lede{font-style:italic;color:var(--soft);font-size:1.04em;line-height:1.55;margin:0 0 1.7em;padding-bottom:1.1em;border-bottom:1px solid var(--rule);}
h4.subsubsection-h{font-family:var(--sans);font-weight:700;font-size:0.76em;letter-spacing:0.05em;text-transform:uppercase;color:var(--ink-soft);margin:2em 0 0.5em;line-height:1.4;}
.chapter-page ul,.chapter-page ol{margin:1.1em 0 1.1em 1.3em;padding:0;}
.chapter-page li{margin:0.4em 0;line-height:1.6;}
blockquote{margin:1.5em 0;padding:0.3em 0 0.3em 1.3em;border-left:3px solid var(--rule-strong);color:var(--ink-soft);font-style:italic;}
.book-table{width:100%;border-collapse:collapse;font-family:var(--sans);font-size:0.74em;line-height:1.45;margin:1.7em 0;}
.book-table th,.book-table td{border:1px solid var(--rule);padding:7px 10px;text-align:left;vertical-align:top;}
.book-table th{background:var(--sidebar-bg);font-weight:700;color:var(--ink);}
pre{background:var(--code-bg);border:1px solid var(--code-rule);border-radius:10px;padding:1.1em 1.3em;overflow-x:visible;margin:1.5em 0;font-size:0.7em;line-height:1.65;}
.chapter-page pre code{font-family:ui-monospace,'Cascadia Code','SF Mono',Consolas,Menlo,monospace;font-size:1em;white-space:pre-wrap;overflow-wrap:anywhere;word-break:normal;color:var(--code-ink);background:none;padding:0;border-radius:0;font-variant-ligatures:none;font-feature-settings:"liga" 0,"calt" 0;}
pre .c-kw{color:var(--code-kw);font-weight:600;}
pre .c-string{color:var(--code-str);}
pre .c-number{color:var(--code-num);}
pre .c-comment{color:var(--code-com);font-style:italic;}
pre .c-promise{color:var(--code-promise);}
.chapter-page code{font-family:var(--sans);font-size:0.82em;background:var(--sidebar-bg);padding:0.05em 0.35em;border-radius:4px;}

/* ---- the book's additions ---- */
/* the reader's paragraph rule (indent, justify, reading size) is for prose only */
.chapter-page p.proof,.chapter-page p.proof-engine,.chapter-page .code-cell p,.chapter-page .court p,.chapter-page .untranslated p{text-indent:0;text-align:left;hyphens:none;-webkit-hyphens:none;font-feature-settings:normal;}
.chapter-page p.proof{font-size:13px;}
.chapter-page p.proof-engine{font-size:12px;}
.chapter-page .code-cell p.ran,.chapter-page .code-cell p.effects{font-size:12.5px;line-height:1.5;}
.chapter-page .untranslated p{font-size:15px;}
.lang-toggle{display:inline-flex;align-items:center;border:1px solid var(--rule);border-radius:19px;background:var(--paper);height:38px;overflow:hidden;font-family:var(--sans);font-size:12px;font-weight:700;letter-spacing:1px;}
.lang-toggle a{padding:0 11px;height:100%;display:inline-flex;align-items:center;color:var(--soft);}
.lang-toggle a.active{background:var(--ink);color:var(--paper);}
.lang-toggle a:not(.active):hover{background:var(--hover-bg);color:var(--ink);}

.status-banner{display:inline-block;font-family:var(--sans);font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:5px 10px;border-radius:4px;margin:0 0 14px;border:1px solid var(--rule);color:var(--soft);background:var(--sidebar-bg);}
.status-banner.st-draft{border-color:var(--bookmark);color:var(--bookmark-text);background:transparent;}
.status-banner.st-missing{border-color:var(--bad);color:var(--bad);background:transparent;}
.spine-badge{display:inline-block;font-family:var(--sans);font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--paper);background:var(--ink);border-radius:3px;padding:2px 7px;margin-left:10px;vertical-align:2px;}

.proof{font-family:var(--sans);font-size:13px;line-height:1.55;color:var(--soft);margin:0 0 6px;}
.proof strong{color:var(--ink);font-weight:600;}
.proof.fails strong{color:var(--bad);}
.proof-engine{font-family:var(--sans);font-size:12px;line-height:1.5;color:var(--soft-2);margin:0 0 8px;}

.code-cell{margin:1.6em 0;}
.code-cell pre{margin:0;border-radius:10px 10px 0 0;}
.code-cell .cell-label{font-family:var(--sans);font-size:10.5px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--code-label);background:var(--code-bg);border:1px solid var(--code-rule);border-bottom:none;border-radius:10px 10px 0 0;padding:8px 1.3em 0;}
.code-cell .cell-label + pre{border-top:none;border-radius:0;padding-top:0.5em;}
.code-cell .ran{font-family:var(--sans);font-size:12.5px;line-height:1.5;margin:0;padding:8px 14px;border:1px solid var(--rule);border-top:none;border-radius:0 0 10px 10px;background:var(--neutral-bg);color:var(--neutral);}
.code-cell .ran::before{font-weight:700;margin-right:7px;}
.code-cell .ran.nv-kept{background:var(--ok-bg);color:var(--ok);}
.code-cell .ran.nv-kept::before{content:"\\2713";}
.code-cell .ran.nv-differs,.code-cell .ran.nv-raised,.code-cell .ran.nv-stopped,.code-cell .ran.nv-not-run{background:var(--bad-bg);color:var(--bad);}
.code-cell .ran.nv-differs::before,.code-cell .ran.nv-raised::before,.code-cell .ran.nv-stopped::before,.code-cell .ran.nv-not-run::before{content:"\\2717";}
.code-cell .ran.nv-exercise::before{content:"\\270E";}
.code-cell .ran-out{border-radius:0 0 10px 10px;margin:0;border-top:none;}
.code-cell .ran + .ran-out{border-radius:0 0 10px 10px;}
.code-cell .ran.has-out{border-radius:0;}
.code-cell .effects{font-family:var(--sans);font-size:12px;color:var(--soft);margin:6px 2px 0;}

.stage-list{list-style:none;margin:0 0 1.2em !important;padding:0;}
.stage-list li{display:flex;gap:12px;align-items:baseline;margin:0.45em 0;font-size:0.92em;}
.stage{display:inline-block;flex:0 0 auto;font-family:var(--sans);font-size:10.5px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:3px 8px;border-radius:3px;border:1px solid currentColor;min-width:86px;text-align:center;}
.stage.s-built{color:var(--ok);background:var(--ok-bg);}
.stage.s-designed{color:var(--designed);background:var(--designed-bg);}
.stage.s-absent{color:var(--neutral);background:var(--neutral-bg);}

.decision{background:var(--decision-bg);border-left:4px solid var(--ink);border-radius:0 6px 6px 0;padding:6px 26px 22px;margin:44px -26px 36px -30px;}
.decision > .subsection-h{margin-top:26px;}
.decision-tag{font-family:var(--sans);font-size:10.5px;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--bookmark-text);margin-top:18px;}

.court{border:1px solid var(--rule);border-radius:6px;padding:14px 18px;margin:1.4em 0;background:var(--card-bg);font-family:var(--sans);}
.chapter-page .court p.court-head{font-size:12px;line-height:1.5;color:var(--soft);margin:0 0 10px;font-family:var(--sans);}
.court ul{list-style:none;margin:0 !important;padding:0;}
.court li{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline;padding:7px 0;border-top:1px dotted var(--rule);font-size:14px;margin:0 !important;line-height:1.45;}
.court li:first-child{border-top:none;}
.court .g-name code{font-family:ui-monospace,'Cascadia Code',Consolas,monospace;font-size:13px;background:none;padding:0;color:var(--ink);}
.court .g-name a{border-bottom:1px solid var(--rule);}
.court .g-name a:hover{border-bottom-color:var(--ink);}
.court .g-count{font-weight:700;color:var(--ink);}
.court .g-path{color:var(--soft);font-size:12px;}
.court .g-missing{color:var(--bad);font-weight:600;}

.doors{font-size:0.8em;}
.doors td:first-child{white-space:nowrap;font-weight:700;color:var(--ink);width:1%;}
.doors td{font-family:var(--serif);font-size:1.12em;line-height:1.5;}
.doors td:first-child{font-family:var(--sans);font-size:1em;}

.author-q{font-family:var(--sans);font-size:0.72em;font-weight:600;color:var(--bookmark-text);border:1px dashed var(--bookmark);border-radius:4px;padding:1px 6px;}
.sources{background:var(--sidebar-bg);border-left:3px solid var(--rule-strong);border-radius:0 4px 4px 0;padding:14px 20px;margin:48px 0 0;font-family:var(--sans);font-size:13.5px;line-height:1.55;color:var(--ink-soft);}
.sources ul{list-style:none;margin:6px 0 0 !important;padding:0;}
.chapter-page .sources li{margin:4px 0;line-height:1.5;}
.sources .src-k{display:inline-block;min-width:150px;font-size:10.5px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--soft);}
.sources code{font-family:ui-monospace,Consolas,monospace;font-size:12.5px;background:none;padding:0;}
.book-fig{margin:2em -8px;}
.book-fig .fg-box{fill:var(--card-bg);stroke:var(--rule);stroke-width:1;}
.book-fig .fg-box-strong{fill:var(--card-bg);stroke:var(--ink);stroke-width:1.4;}
.book-fig .fg-floor{fill:var(--sidebar-bg);stroke:var(--rule);stroke-width:1;}
.book-fig .fg-court{fill:var(--decision-bg);stroke:var(--ink);stroke-width:1.2;}
.book-fig .fg-txt{fill:var(--ink);}
.book-fig .fg-soft{fill:var(--soft);}
.book-fig .fg-accent{fill:var(--bookmark);}
.book-fig .fg-arrow{stroke:var(--soft-2);stroke-width:1.2;fill:none;}
.book-fig .fg-arrow-strong{stroke:var(--bookmark);stroke-width:2;fill:none;}
.book-fig .fg-head{fill:var(--soft-2);}
.book-fig .fg-head-strong{fill:var(--bookmark);}
.book-fig svg{max-width:100%;height:auto;display:block;margin:0 auto;}
.untranslated{font-family:var(--sans);font-size:15px;line-height:1.6;color:var(--ink-soft);border:1px dashed var(--rule);border-radius:6px;padding:18px 20px;}
.untranslated a{color:var(--bookmark-text);font-weight:600;}

/* navigation: parts, the spine, the chapters not yet drafted */
.sb-part{font-family:var(--sans);font-weight:700;text-transform:uppercase;color:var(--ink);}
.sidebar-link .sl-spine{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--ink);margin-right:8px;vertical-align:2px;}
.sidebar-link:not(.is-spine) .sl-spine{background:transparent;border:1px solid var(--soft-2);}
.sidebar-link.active .sl-text{text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:5px;}
.sidebar-link.is-absent{color:var(--soft-2);cursor:default;}
.the-invite{margin:3.2em 0 1em;padding:1.6em 0 0;border-top:1px solid var(--rule);}
.the-invite p{text-indent:0;text-align:left;hyphens:none;}
.the-invite .invite-line{font-style:italic;}
.the-invite a{border-bottom:1px solid var(--rule-strong);}
.the-invite .invite-more,.the-invite .colophon-line{font-family:var(--sans);color:var(--soft);line-height:1.5;}
.sidebar-link.is-absent .sl-text{font-style:italic;}
.sidebar-link.is-absent:hover .sl-text{font-weight:400;}
.spine-toggle{font-family:var(--sans);font-size:15px;font-weight:600;border:1px solid var(--rule);border-radius:18px;background:var(--paper);color:var(--ink-soft);padding:9px 18px;margin:0 0 8px;}
.spine-toggle:hover{border-color:var(--ink);color:var(--ink);}
.spine-toggle[aria-pressed="true"]{background:var(--ink);color:var(--paper);border-color:var(--ink);}
body.spine-only .sidebar-link:not(.is-spine),body.spine-only .chapter-card:not(.is-spine),body.spine-only .ce-row:not(.is-spine){display:none;}
.chapter-card.is-spine .card-bookmark{background:var(--ink);}

.hero-series{font-family:var(--sans);font-size:13px;color:var(--soft);letter-spacing:1.5px;text-transform:uppercase;margin:-14px 0 26px;}
.hero-tagline{font-family:var(--serif);font-size:19px;color:var(--ink-soft);margin:-8px 0 22px;line-height:1.45;}
.hero-back{font-family:var(--serif);font-style:italic;font-size:18px;color:var(--ink-soft);margin:0 0 24px;line-height:1.5;}
.hero-back .hb-label{display:block;font-family:var(--sans);font-style:normal;font-size:10.5px;letter-spacing:2px;text-transform:uppercase;color:var(--soft);margin-bottom:4px;}
.hero-status{font-family:var(--sans);font-size:13px;margin:0 0 22px;}
.hero-status a{border-bottom:1px solid var(--rule);color:var(--ink-soft);}
.hero-status a:hover{border-bottom-color:var(--ink);color:var(--ink);}
.cover-svg .cv-bg{fill:var(--cover-bg);}
.cover-svg .cv-ink{fill:var(--cover-ink);}
.cover-svg .cv-soft{fill:var(--cover-soft);}
.cover-svg .cv-accent{fill:var(--cover-accent);}
.cover-svg .cv-rule{stroke:var(--cover-accent);}

.overview-contents{max-width:760px;margin:72px auto 0;}
.overview-contents h2{font-family:var(--sans);font-size:26px;font-weight:800;letter-spacing:-0.3px;margin-bottom:6px;color:var(--ink);}
.contents-listing .ce-row.is-absent .ce-title{color:var(--soft-2);}
.contents-listing .ce-row a.ce-title:hover{text-decoration:underline;}
.contents-listing .ce-spine{font-family:var(--sans);font-size:11.5px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--paper);background:var(--ink);border-radius:3px;padding:1px 6px;margin-left:8px;}

@media (max-width: 600px) {
  .lang-toggle a{padding:0 8px;}
  .decision{margin-left:-16px;margin-right:-16px;padding:4px 16px 18px;}
}
@media print {
  .code-cell, .court, .decision, .doors { break-inside: avoid; }
  .spine-toggle, .lang-toggle, #btnTheme { display: none !important; }
  body.spine-only .sidebar-link, body.spine-only .chapter-card, body.spine-only .ce-row { display: initial; }
}
"""


# ============================================================================ the type scale
# One scale, and a check (the author's rule, repeated: the size of a text follows its level. A part is above a chapter,
# a chapter above a section, a section above the body text it heads; a label is never smaller than 13px).
TYPE = {
    # the reader's navigation, in px
    "sidebar_book": 24, "sidebar_part": 20, "sidebar_link": 18.5,
    "contents_h2": 36, "contents_part": 27, "contents_row": 22, "contents_num": 16, "contents_pg": 15, "contents_badge": 13,
    "card_title": 21, "card_words": 15,
    # inside a chapter page, in em of the reading size (so it follows the font control)
    "section_h3": 1.3, "subsection_h4": 1.12, "body": 1.0, "stage_li": 0.92,
    # labels and notes, in px
    "eyebrow": 13, "decision_tag": 13, "proof": 15, "proof_engine": 14.5, "ran": 15, "effects": 14.5, "banner": 13, "court_li": 15, "court_head": 13, "court_path": 13, "sources": 14.5,
}


def check_type_scale():
    T, bad = TYPE, []
    def above(hi, lo):
        if not T[hi] > T[lo]:
            bad.append(f"the type scale: {hi} ({T[hi]}) must be larger than {lo} ({T[lo]})")
    above("sidebar_book", "sidebar_part"); above("sidebar_part", "sidebar_link")
    above("contents_h2", "contents_part"); above("contents_part", "contents_row"); above("contents_row", "contents_num")
    above("section_h3", "subsection_h4"); above("subsection_h4", "body")
    for k in ("sidebar_link", "contents_num", "contents_pg", "contents_badge", "card_words", "eyebrow", "decision_tag", "proof", "proof_engine", "ran", "effects", "banner",
              "court_li", "court_head", "court_path", "sources"):
        if T[k] < 13:
            bad.append(f"the type scale: {k} ({T[k]}px) is below the 13px floor for any label or note")
    if T["stage_li"] < 0.85:
        bad.append("the type scale: the stage list is below 0.85 of the body text")
    return bad


def type_css():
    T = TYPE
    return (
        "\n/* ---- the type scale (TYPE in build_book.py): generated, checked at build ---- */\n"
        f".sidebar-book-title{{font-size:{T['sidebar_book']}px;margin-bottom:22px;}}\n"
        f".sb-part{{font-size:{T['sidebar_part']}px;letter-spacing:0;font-weight:600;text-transform:none;margin:30px 0 6px;line-height:1.3;}}\n"
        f".sidebar-link,.sidebar-link.is-absent{{font-size:{T['sidebar_link']}px;line-height:1.32;padding:11px 0;}}\n"
        ".sidebar-link .sl-spine{width:9px;height:9px;margin-right:10px;vertical-align:1px;}\n"
        f".contents-listing .ce-part{{font-size:{T['contents_part']}px;font-weight:600;text-transform:none;letter-spacing:0;line-height:1.25;margin:44px 0 12px;}}\n"
        f".contents-listing .ce-row{{font-size:{T['contents_row']}px;padding:11px 0;}}\n"
        f".contents-listing .ce-num{{font-size:{T['contents_num']}px;width:46px;}}\n"
        f".contents-listing .ce-pg{{font-size:{T['contents_pg']}px;}}\n"
        f".contents-listing .ce-spine{{font-size:{T['contents_badge']}px;}}\n"
        f".overview-contents h2{{font-size:{T['contents_h2']}px;}}\n"
        f".chapter-card .card-title{{font-size:{T['card_title']}px;}}\n"
        f".chapter-card .card-words{{font-size:{T['card_words']}px;}}\n"
        f".chapter-page .subsection-h{{font-size:{T['section_h3']}em;font-weight:600;text-transform:none;letter-spacing:0;line-height:1.3;}}\n"
        f".chapter-page h4.subsubsection-h{{font-size:{T['subsection_h4']}em;font-weight:600;text-transform:none;letter-spacing:0;}}\n"
        f".chapter-page .ch-eyebrow{{font-size:{T['eyebrow']}px;}}\n"
        f".decision-tag{{font-size:{T['decision_tag']}px;}}\n"
        f".chapter-page p.proof{{font-size:{T['proof']}px;}}\n"
        f".chapter-page p.proof-engine{{font-size:{T['proof_engine']}px;color:var(--soft);}}\n"
        f".chapter-page .code-cell p.ran{{font-size:{T['ran']}px;line-height:1.5;}}\n"
        f".chapter-page .code-cell p.effects{{font-size:{T['effects']}px;line-height:1.5;}}\n"
        f".status-banner{{font-size:{T['banner']}px;}}\n"
        f".stage-list li{{font-size:{T['stage_li']}em;}}\n"
        f".court li{{font-size:{T['court_li']}px;}}\n"
        f".chapter-page .court p.court-head{{font-size:{T['court_head']}px;}}\n"
        f".court .g-path{{font-size:{T['court_path']}px;}}\n"
        f".sources{{font-size:{T['sources']}px;}}\n"
        f".the-invite .invite-more,.the-invite .colophon-line{{font-size:{T['sources']}px;}}\n"
        f"@media (max-width: 900px){{.sb-part{{font-size:19px;}}.sidebar-link{{font-size:18px;}}.contents-listing .ce-part{{font-size:23px;}}.contents-listing .ce-row{{font-size:20px;}}}}\n"
    )


# ============================================================================ Markdown, as the Refine build reads it
def inline(text):
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    codes = []
    def _stash(m):
        codes.append(m.group(1)); return f"\x00C{len(codes)-1}\x00"
    text = re.sub(r"`([^`]+)`", _stash, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"\x00C(\d+)\x00", lambda m: "<code>" + codes[int(m.group(1))] + "</code>", text)
    # the author's open questions stay visible on the page until answered (method, section 5)
    text = re.sub(r"\[AUTHOR:(.*?)\]", r'<span class="author-q">[AUTHOR:\1]</span>', text)
    return text


def author_questions(body):
    return re.findall(r"\[AUTHOR:(.*?)\]", body, re.S)


def plain(text):
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


HARO_TOKEN = re.compile(r"""
   (?P<promise>^[ \t]*\#[ \t]*-->[^\n]*)
 | (?P<comment>(?:\#|//)[^\n]*)
 | (?P<string>"[^"\n]*"|'[^'\n]*')
 | (?P<kw>(?:^[ \t]*\?(?=\s))|\b(?:new|if|but|else|ok|for|in|to|step|next|while|end|func|def|class|return|load|try|catch|done|switch|on|other|off|and|or|not|see|give|exit|loop|from|package|import|private|this)\b)
 | (?P<number>(?<![\w.])\d+(?:\.\d+)?(?![\w.]))
""", re.M | re.X | re.I)


def highlight(src):
    out, pos = [], 0
    for m in HARO_TOKEN.finditer(src):
        out.append(html.escape(src[pos:m.start()], quote=False))
        out.append(f'<span class="c-{m.lastgroup}">{html.escape(m.group(0), quote=False)}</span>')
        pos = m.end()
    out.append(html.escape(src[pos:], quote=False))
    return "".join(out)


def render_table(rows, cls="book-table", head=None):
    th = "".join(f"<th>{c}</th>" for c in head) if head else ""
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}">' + (f"<thead><tr>{th}</tr></thead>" if th else "") + f"<tbody>{trs}</tbody></table>"


def code_cell(text, flags, rec, ui, run_date):
    w = WORDS[ui["lang"]]
    parts = ['<div class="code-cell">', '<div class="cell-label">Haro</div>',
             f"<pre><code>{highlight(text)}</code></pre>"]
    if rec is None:
        parts.append(f'<p class="ran nv-not-run">{html.escape(w["not-run"].format(why="this block has no run on record"))}</p>')
    else:
        v = rec["verdict"]
        if v == "exercise":
            label = w["exercise"]
        elif v == "not-run":
            label = w["not-run"].format(why=rec.get("why", ""))
        elif v == "ran" and not rec.get("out"):
            label = w["ran0"]
        else:
            label = w[v]
        show_out = v in ("differs", "raised", "ran", "not-run") and rec.get("out")
        parts.append(f'<p class="ran nv-{v}{" has-out" if show_out else ""}">{html.escape(label)}</p>')
        if show_out:
            parts.append(f'<pre class="ran-out"><code>{html.escape(rec["out"])}</code></pre>')
        if rec.get("effects") and v != "exercise":
            parts.append(f'<p class="effects">{html.escape(w["effects"].format(what=", ".join(rec["effects"]), d=run_date))}</p>')
    parts.append("</div>")
    return "\n".join(parts)


def figure_html(slug, caption):
    """A figure is an SVG file in assets/figures/, inlined so the reader stays one file (the Refine build's form)."""
    f = ROOT / "assets" / "figures" / f"{slug}.svg"
    if not f.exists():
        raise SystemExit(f"figure {slug}: assets/figures/{slug}.svg does not exist")
    svg = f.read_text(encoding="utf-8")
    cap = f"<figcaption><strong>Fig.</strong> {inline(caption)}</figcaption>" if caption else ""
    return f'<figure class="book-fig" id="fig-{slug}">{svg}{cap}</figure>'


def sources_box(meta, ui, runs):
    """Where the chapter's evidence lives: the narrations it argues from, the site's pages, the rulings."""
    sha = runs.get("run", {}).get("library", {}).get("commit", "main")
    rows = []
    for n in meta.get("narrations") or []:
        url = f"https://github.com/mayouni/stzlib/blob/{sha}/libraries/stzlib/base/doc/narrations/{urllib.parse.quote(n)}"
        rows.append(f'<li><span class="src-k">{ui["src_narration"]}</span><a href="{url}" target="_blank" rel="noopener"><code>{html.escape(n)}</code></a></li>')
    for page in meta.get("site") or []:
        url = SITE_BASE + f'{ui["lang"]}/{page}.html'
        rows.append(f'<li><span class="src-k">{ui["src_site"]}</span><a href="{url}" target="_blank" rel="noopener">{html.escape(page)}</a></li>')
    if meta.get("rulings"):
        rows.append(f'<li><span class="src-k">{ui["src_rulings"]}</span>{html.escape(", ".join(str(r) for r in meta["rulings"]))}</li>')
    if not rows:
        return ""
    return f'<aside class="sources"><div class="aside-h">{ui["src_head"]}</div><ul>{"".join(rows)}</ul></aside>'


def section_number(head):
    m = re.match(r"(\d+)\.\s", head)
    return int(m.group(1)) if m else None


def convert_body(body, meta, ui, run_rec, run_date, guards):
    """The Refine build's Markdown reading, with the nine-element chapter shape added:
    4 the decision (boxed), 5 the court (guards read at build), 7 the limit (stage words), 8 the doors (a table)."""
    lines = body.split("\n")
    out, para, n = [], [], len(lines)
    blocks = (run_rec or {}).get("blocks", [])
    k_code = 0
    current, decision_open = None, False

    def flush():
        if para:
            out.append("<p>" + inline(" ".join(x.strip() for x in para)) + "</p>")
            para.clear()

    def close_section():
        nonlocal decision_open
        flush()
        if current == 5:
            out.append(court_box(meta, ui, guards))
        if decision_open:
            out.append("</section>"); decision_open = False

    i = 0
    doors = []
    while i < n:
        s = lines[i].strip()
        if s == "":
            flush(); i += 1; continue
        if s.startswith("## "):
            if doors:
                out.append(render_table(doors, "book-table doors", ui["doors_h"])); doors = []
            close_section()
            head = s[3:].strip()
            current = None if meta.get("appendix") else section_number(head)
            if current == 4:
                out.append(f'<section class="decision"><div class="decision-tag">{ui["decision"]}</div>'); decision_open = True
            out.append(f'<h3 class="subsection-h">{inline(head)}</h3>')
            if current == 7 and meta.get("stage"):
                items = "".join(f'<li><span class="stage s-{k}">{ui["stage"].get(k, k)}</span><span>{inline(str(v))}</span></li>'
                                for k, v in meta["stage"].items())
                out.append(f'<ul class="stage-list">{items}</ul>')
            i += 1; continue
        if s.startswith("### "):
            flush(); out.append(f'<h4 class="subsubsection-h">{inline(s[4:].strip())}</h4>'); i += 1; continue
        if s == "---":
            flush(); out.append('<div class="divider">· · ·</div>'); i += 1; continue
        mfig = re.match(r"^\{\{fig:([a-z0-9-]+)(?:\|(.*))?\}\}$", s)
        if mfig:
            flush(); out.append(figure_html(mfig.group(1), mfig.group(2))); i += 1; continue
        if s.startswith("```"):
            flush()
            info = s[3:].strip().split()
            i += 1; code = []
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            text = "\n".join(code)
            if info and info[0].lower() == "haro":
                rec = blocks[k_code] if k_code < len(blocks) else None
                k_code += 1
                out.append(code_cell(text, [w.lower() for w in info[1:]], rec, ui, run_date))
            else:
                out.append(f"<pre><code>{html.escape(text)}</code></pre>")
            continue
        if s.startswith(">"):
            flush(); bq = []
            while i < n and lines[i].strip().startswith(">"):
                bq.append(lines[i].strip().lstrip(">").strip()); i += 1
            out.append("<blockquote>" + "<br>".join(inline(x) for x in bq) + "</blockquote>"); continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip()):
            flush(); tbl = [s]; j = i + 1
            while j < n and lines[j].strip().startswith("|"):
                tbl.append(lines[j].strip()); j += 1
            rows = [[inline(c.strip()) for c in r.strip("|").split("|")] for r in tbl]
            out.append(render_table(rows[2:], head=rows[0])); i = j; continue
        if re.match(r"^[-*]\s+", s) and not s.startswith("**"):
            flush(); items = []
            while i < n and re.match(r"^[-*]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*]\s+", "", lines[i].strip())); i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); continue
        if re.match(r"^\d+\.\s+", s):
            flush(); items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i].strip())); i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); continue
        # the six doors: one paragraph per door, "**The programmer.** what they take"
        if current == 8:
            m = re.match(r"^\*\*(.+?)\.?\*\*\s*(.*)$", s)
            if m:
                flush()
                txt = [m.group(2)]
                i += 1
                while i < n and lines[i].strip() and not lines[i].strip().startswith(("**", "#")):
                    txt.append(lines[i].strip()); i += 1
                doors.append([inline(m.group(1).rstrip(".")), inline(" ".join(txt))])
                continue
        para.append(s); i += 1
    if doors:
        out.append(render_table(doors, "book-table doors", ui["doors_h"]))
    close_section()
    return "\n".join(out)


def court_box(meta, ui, guards):
    names = meta.get("guards") or []
    if not names:
        return ""
    g = guards.get("guards", {})
    items = []
    for name in names:
        rec = g.get(name, {"exists": False})
        if not rec.get("exists"):
            items.append(f'<li><span class="g-name"><code>{html.escape(name)}</code></span><span class="g-missing">{ui["guard_missing"]}</span></li>')
            continue
        items.append(f'<li><span class="g-name"><a href="{rec["url"]}" target="_blank" rel="noopener"><code>{html.escape(name)}</code></a></span>'
                     f'<span class="g-count">{rec["assertions"]} {ui["assertions"]}</span>'
                     f'<span class="g-path">{html.escape(rec["path"])}</span></li>')
    head = ui["court_head"].format(sha=guards.get("commit", "")[:9], d=guards.get("read", ""))
    return f'<div class="court"><p class="court-head">{html.escape(head)}</p><ul>{"".join(items)}</ul></div>'


def words_of(body):
    no_code = re.sub(r"(?ms)^```.*?^```", "", body)
    no_code = re.sub(r"(?m)^#+\s.*$", "", no_code)
    return len(re.findall(r"\b\w+\b", plain(no_code)))


# ============================================================================ the appendices that are read from the build
def _chapters_only(en_src):
    return [(p, m, b) for p, m, b in en_src if not m.get("appendix")]


def generated_body(kind, en_src, guards, runs, st, lang="en", titles=None):
    """Markdown for an appendix that is read from the book itself at build, so that no number in it is typed."""
    chapters = _chapters_only(en_src)
    g = guards.get("guards", {})
    lib = runs.get("run", {}).get("library", {})
    out = []
    T = lambda en, fr: fr if lang == "fr" else en
    title_of = lambda m: (titles or {}).get(m["id"], m["title"])
    if kind == "guards":
        seen, total = {}, 0
        for path, m, body in chapters:
            names = m.get("guards") or []
            if not names:
                continue
            out.append(f"### {m['number']} · {title_of(m)}")
            out.append("")
            out.append(T("| Guard | Assertions | Where in the library's test tree |", "| Garde | Assertions | Où, dans l'arbre de tests de la bibliothèque |"))
            out.append("|---|---|---|")
            for n in names:
                rec = g.get(n, {})
                if rec.get("exists"):
                    out.append(f"| `{n}` | {rec['assertions']} | `{rec['path']}` |")
                    if n not in seen:
                        seen[n] = rec["assertions"]
                else:
                    out.append(f"| `{n}` | {T('missing', 'manquante')} | |")
            out.append("")
        out.insert(0, (f"Les chapitres citent {len(seen)} gardes distinctes, qui contiennent {sum(seen.values())} assertions à elles toutes, "
                      f"lues dans l'arbre de tests au commit {lib.get('short', 'null')} le {guards.get('read', 'null')}. "
                      "Une garde citée par deux chapitres n'est comptée qu'une fois dans ce total. Les noms et les chemins sont imprimés tels que la bibliothèque les écrit ; l'extension est celle de l'ancien moteur tant que Haro ne fait pas tourner la bibliothèque.\n") if lang == "fr" else (f"The chapters cite {len(seen)} distinct guards, holding {sum(seen.values())} assertions between them, "
                      f"read from the test tree at commit {lib.get('short', 'null')} on {guards.get('read', 'null')}. "
                      "A guard cited by two chapters is counted once in this total. Names and paths are printed as the library spells them; the extension is the former runtime's until Haro runs the library.\n"))
    elif kind == "narrations":
        short = lib.get("short")
        nd = ROOT / ".cache" / f"stzlib-{short}" / "libraries" / "stzlib" / "base" / "doc" / "narrations" if short else None
        seen, absent = set(), []
        for path, m, body in chapters:
            names = m.get("narrations") or []
            if not names:
                continue
            out.append(f"### {m['number']} · {title_of(m)}")
            out.append("")
            out.append(T("| Narration | In the library at the pin |", "| Narration | Dans la bibliothèque au commit |"))
            out.append("|---|---|")
            for n in names:
                ok = bool(nd and (nd / n).exists())
                seen.add(n)
                if not ok:
                    absent.append(n)
                out.append(f"| `{n}` | {('oui' if lang == 'fr' else 'yes') if ok else ('non' if lang == 'fr' else 'no')} |")
            out.append("")
        tail = ("Les noms et les chemins sont imprimés tels que la bibliothèque les écrit ; l'extension est celle de l'ancien moteur tant que Haro ne fait pas tourner la bibliothèque.\n"
                if lang == "fr" else "Names and paths are printed as the library spells them; the extension is the former runtime's until Haro runs the library.\n")
        total = len(list(nd.glob('*.md'))) if nd and nd.exists() else None
        if lang == "fr":
            lead = ((f"Le dossier des narrations en compte {total} au commit. " if total else "") + f"Les chapitres citent {len(seen)} narrations distinctes. "
                    + (f"{len(absent)} des noms ne sont pas des fichiers du dossier des narrations de la bibliothèque au commit {lib.get('short', 'null')}" + ": " + ", ".join(f"`{a}`" for a in absent) + ". "
                       if absent else f"Chaque nom est un fichier du dossier des narrations de la bibliothèque au commit {lib.get('short', 'null')}. "))
        else:
            lead = ((f"The library's narration folder holds {total} at the pin. " if total else "") + f"The chapters cite {len(seen)} distinct narrations. "
                    + (f"{len(absent)} of the names are not files of the library's narration folder at commit {lib.get('short', 'null')}" + ": " + ", ".join(f"`{a}`" for a in absent) + ". "
                       if absent else f"Every name is a file of the library's narration folder at commit {lib.get('short', 'null')}. "))
        out.insert(0, lead + tail)
    elif kind == "agents":
        out.append(T("| # | Id | Part | Status | Spine | Blocks kept | Guards | Doors |", "| # | Id | Partie | Statut | Colonne | Blocs tenus | Gardes | Portes |"))
        out.append("|---|---|---|---|---|---|---|---|")
        for path, m, body in en_src:
            r = runs.get("chapters", {}).get(f"en/{path.stem}", {})
            kept = f"{r['kept']} {'sur' if lang == 'fr' else 'of'} {r['runnable']}" if r.get("runnable") else ("pas de code" if lang == "fr" else "no code")
            out.append(f"| {m.get('appendix') or m['number'] or ''} | `{m['id']}` | {m.get('part', '')} | {m.get('status', '')} | {('oui' if lang == 'fr' else 'yes') if m.get('spine') else ''} | {kept} | {len(m.get('guards') or [])} | {len(doors_of(body))} |")
    return "\n".join(out)


# ============================================================================ the cover (typographic, a working cover)
def cover_svg(st, ui, lang):
    """The author's cover image when assets/cover has one (a flat image, embedded so the reader stays one file);
    else the typographic working cover."""
    img = ROOT / "assets" / "cover" / ("cover.fr.png" if lang == "fr" else "cover.png")
    if img.exists():
        import base64, io
        from PIL import Image
        buf = io.BytesIO()
        Image.open(img).convert("RGB").save(buf, "JPEG", quality=86, optimize=True)
        data = base64.b64encode(buf.getvalue()).decode("ascii")
        return (f'<img class="cover-img" src="data:image/jpeg;base64,{data}" width="1097" height="1434" '
                f'alt="{html.escape(ui["cover_alt"])}">')
    sub = st["fr"]["subtitle"] if lang == "fr" else st["subtitle"]
    tag = st["fr"]["tagline"] if lang == "fr" else st["tagline"]
    def wrap(text, width):
        words, lines, cur = text.split(), [], ""
        for w in words:
            if len(cur) + len(w) + 1 > width and cur:
                lines.append(cur); cur = w
            else:
                cur = (cur + " " + w).strip()
        return lines + [cur]
    sub_l = wrap(sub, 26)
    tag_l = wrap(tag, 38)
    y = 300
    t_sub = "".join(f'<text x="40" y="{y + 34*k}" class="cv-ink" font-family="Inter, system-ui, sans-serif" font-size="25" font-weight="700">{html.escape(l)}</text>' for k, l in enumerate(sub_l))
    y2 = y + 34 * len(sub_l) + 24
    t_tag = "".join(f'<text x="40" y="{y2 + 24*k}" class="cv-soft" font-family="EB Garamond, Georgia, serif" font-style="italic" font-size="19">{html.escape(l)}</text>' for k, l in enumerate(tag_l))
    return f'''<svg class="cover-svg" viewBox="0 0 400 600" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{html.escape(ui["cover_alt"])}">
<rect width="400" height="600" class="cv-bg"/>
<rect x="40" y="58" width="44" height="5" class="cv-accent"/>
<text x="38" y="200" class="cv-ink" font-family="Archivo Black, Inter, sans-serif" font-size="66" letter-spacing="-1">Softanza</text>
<line x1="40" y1="246" x2="360" y2="246" class="cv-rule" stroke-width="1.5"/>
{t_sub}
{t_tag}
<text x="40" y="530" class="cv-ink" font-family="Inter, system-ui, sans-serif" font-size="15" font-weight="600">Mansour Ayouni</text>
<text x="360" y="530" text-anchor="end" class="cv-ink" font-family="Archivo Black, Inter, sans-serif" font-size="20">AYOUNI</text>
<circle cx="353.6" cy="507" r="2.6" class="cv-ink"/>
<text x="360" y="556" text-anchor="end" class="cv-soft" font-family="Inter, system-ui, sans-serif" font-size="10.5" letter-spacing="1.2">{html.escape(ui["series"].upper())}</text>
</svg>'''


# ============================================================================ pages
def chapter_title(st, number):
    for p in st["parts"]:
        for num, title in p["chapters"]:
            if num == number:
                return p, title
    return None, None


def build_pages(lang, st, en_src, src_by_id, runs, guards, ui):
    """Every page of one language, in book order. The English sources decide which pages exist;
    a page with no source in this language says so and links to the other."""
    pages = []
    run_date = runs.get("run", {}).get("date", "")
    for path, meta, body in en_src:
        own = src_by_id.get(meta["id"])
        m, b, p_path = (own[1], own[2], own[0]) if own else (meta, body, path)
        number = m["number"]
        appendix = m.get("appendix")
        if appendix:
            slug = f"app-{str(appendix).lower()}-{m['id']}"
            eyebrow = f'{ui["appendix"]} {appendix}'
            spine = False
            if m.get("generated"):
                b = b.rstrip() + "\n\n" + generated_body(m["generated"], en_src, guards, runs, st, lang, {k: v[1]["title"] for k, v in src_by_id.items()})
        else:
            slug = "preface" if number == 0 else f"ch{number}-{m['id']}"
            part, _ = chapter_title(st, number)
            spine = bool(m.get("spine")) or number in st["spine"]
            eyebrow = ui["preface"] if number == 0 else f'{ui["part"]} {ROMAN[part["number"]]} · {ui["chapter"]} {number}'
        key = f"{lang}/{p_path.stem}"
        run_rec = runs.get("chapters", {}).get(key) if own else None
        if own:
            body_html = convert_body(b, m, ui, run_rec, run_date, guards) + sources_box(m, ui, runs)
        else:
            other = "en" if lang == "fr" else "fr"
            body_html = (f'<div class="untranslated"><p>{ui["untranslated"]}</p>'
                         f'<p><a href="../{other}/index.html#{slug}">{ui["read_other"]}</a></p></div>')
        pages.append(dict(key=key, slug=slug, meta=m, number=number, title=m["title"], eyebrow=eyebrow, spine=spine,
                          body_html=body_html, own=bool(own), run=run_rec, words=words_of(b) if own else 0,
                          preview=preview_of(b) if own else "", appendix=appendix))
    for k, p in enumerate(pages):
        p["prev"] = pages[k - 1]["slug"] if k > 0 else ""
        p["next"] = pages[k + 1]["slug"] if k < len(pages) - 1 else ""
    return pages


def preview_of(body):
    txt = ""
    for ln in body.split("\n"):
        s = ln.strip()
        if not s or s.startswith(("#", ">", "-", "|", "`", "[")):
            continue
        txt += (" " if txt else "") + plain(s)
        if len(txt) > 230:
            break
    if len(txt) > 250:
        txt = txt[:250].rsplit(" ", 1)[0] + "…"
    return html.escape(txt, quote=False)


def proof_html(p, runs, ui, stale):
    if not p["own"]:
        return ""
    run = p["run"]
    lib = runs.get("run", {}).get("library", {})
    if stale:
        return f'<p class="proof fails"><strong>{html.escape(ui["stale"])}</strong></p>'
    if not run or not run.get("runnable"):
        return f'<p class="proof">{ui["proof_none"]}</p>' if p["number"] else ""
    line = ui["proof"].format(d=run.get("ran", ""), sha=lib.get("short", ""), k=run["kept"], n=run["runnable"])
    fails = run["kept"] < run["runnable"]
    eng = lib.get("engine_binaries", {})
    out = f'<p class="proof{" fails" if fails else ""}"><strong>{html.escape(line)}</strong></p>'
    if eng:
        later = len(eng.get("engine_commits_after_build") or [])
        key = ("eng_at" if later else "eng_at0") if eng.get("built_in_a_tree_at_this_commit") else "eng_copy"
        note = ui[key].format(d=eng.get("newest_build", ""), n=later)
        v = (runs.get("run", {}).get("runtime") or {}).get("version") or "null"
        out += f'<p class="proof-engine">{html.escape(ui["engine"].format(v=v, eng=note))}</p>'
    return out


def the_invitation(ui):
    """The open book's standing invitation to organisations and the colophon line, once, at the end of the reader (house OPEN-BOOK.md, revised): word for word, no payment."""
    col = html.escape(ui["colophon"]).replace("CC BY-NC-ND 4.0", f'<a href="{ui["licence_url"]}">CC BY-NC-ND 4.0</a>')
    mail = ui["invite_mail"]
    return (f'<section class="the-invite"><p class="invite-line">{html.escape(ui["invite"])}<a href="mailto:{mail}">{mail}</a>.</p>'
            f'<p class="invite-more"><a href="{ui["offer_url"]}">{html.escape(ui["offer_link"])}</a></p>'
            f'<p class="colophon-line">{col}</p></section>\n')


def status_banner(meta, ui):
    st = meta.get("status", "draft")
    label = {"draft": ui["draft"], "read": ui["read"], "final": ui["final"], "missing": ui["missing"]}.get(st, st)
    return f'<div class="status-banner st-{st}">{html.escape(label)}</div>'


def render_reader(lang, st, pages, runs, guards, stale_keys):
    ui = UI[lang]
    head, script = apply_shell(ui)
    title = st["fr"]["title"] if lang == "fr" else st["title"]
    sub = st["fr"]["subtitle"] if lang == "fr" else st["subtitle"]
    tag = st["fr"]["tagline"] if lang == "fr" else st["tagline"]
    by_number = {p["number"]: p for p in pages}

    cards, articles = [], []
    last_chapter = max((p["number"] for p in pages if not p["meta"].get("appendix")), default=0)
    for p in pages:
        sp = " is-spine" if p["spine"] else ""
        meta_line = p["eyebrow"] + (f' · {p["words"]} {ui["words"]}' if p["own"] else "")
        cards.append(f'<a class="chapter-card{sp}" href="#{p["slug"]}">\n<span class="card-bookmark"></span>'
                     f'<div class="card-preview"><p>{p["preview"]}</p></div>\n'
                     f'<div class="card-meta"><h3 class="card-title">{html.escape(p["title"], quote=False)}</h3>'
                     f'<p class="card-words">{html.escape(meta_line)}</p></div>\n</a>')
        stale = p["key"] in stale_keys
        spine_badge = f'<span class="spine-badge" title="{html.escape(ui["spine_title"])}">{ui["spine"]}</span>' if p["spine"] else ""
        articles.append(
            f'<article class="chapter-page" id="page-{p["slug"]}" data-slug="{p["slug"]}" '
            f'data-title="{html.escape(p["title"], quote=True)}" data-prev="{p["prev"]}" data-next="{p["next"]}">\n'
            f'<div class="ch-eyebrow">{html.escape(p["eyebrow"])}{spine_badge}</div>\n'
            f'<h1 class="ch-title">{html.escape(p["title"], quote=False)}</h1>\n'
            f'{status_banner(p["meta"], ui) if p["own"] else ""}\n{proof_html(p, runs, ui, stale)}\n'
            f'<div class="ch-rule"></div>\n{p["body_html"]}\n{the_invitation(ui) if p["number"] == last_chapter else ""}</article>')

    # the navigation: the whole book, parts and chapters; what is not drafted is shown and not linked
    side, rows = [], []
    if 0 in by_number:
        p0 = by_number[0]
        side.append(f'<a class="sidebar-link is-spine" href="#preface"><span class="sl-text" data-t="{ui["preface"]}">'
                    f'<span class="sl-spine"></span>{ui["preface"]}</span><span class="sl-leader"></span></a>')
        rows.append(f'<div class="ce-row is-spine"><span class="ce-num"></span><a class="ce-title" href="#preface">{ui["preface"]}</a></div>')
    for part in st["parts"]:
        ptitle = f'{ui["part"]} {ROMAN[part["number"]]} · {part.get("title_fr") if lang == "fr" and part.get("title_fr") else part["title"]}'
        side.append(f'<div class="sb-part">{html.escape(ptitle)}</div>')
        rows.append(f'<div class="ce-part">{html.escape(ptitle)}</div>')
        for num, ctitle in part["chapters"]:
            sp = num in st["spine"]
            cls = " is-spine" if sp else ""
            p = by_number.get(num)
            label = f"{num} · {html.escape(p['title'] if p else ctitle, quote=False)}"
            spine_mark = f'<span class="ce-spine">{ui["spine"]}</span>' if sp else ""
            if p:
                side.append(f'<a class="sidebar-link{cls}" href="#{p["slug"]}"><span class="sl-text" data-t="{label}">'
                            f'<span class="sl-spine"></span>{label}</span><span class="sl-leader"></span></a>')
                rows.append(f'<div class="ce-row{cls}"><span class="ce-num">{num}</span><a class="ce-title" href="#{p["slug"]}">{html.escape(p["title"])}</a>{spine_mark}</div>')
            else:
                side.append(f'<span class="sidebar-link is-absent{cls}" title="{ui["not_drafted"]}"><span class="sl-text" data-t="{label}">'
                            f'<span class="sl-spine"></span>{label}</span></span>')
                rows.append(f'<div class="ce-row is-absent{cls}"><span class="ce-num">{num}</span><span class="ce-title">{html.escape(ctitle)}</span>{spine_mark}<span class="ce-pg">{ui["not_drafted"]}</span></div>')
    by_letter = {str(p["appendix"]): p for p in pages if p.get("appendix")}
    if st.get("appendices"):
        side.append(f'<div class="sb-part">{html.escape(ui["appendices"])}</div>')
        rows.append(f'<div class="ce-part">{html.escape(ui["appendices"])}</div>')
        for letter, atitle in st["appendices"]:
            p = by_letter.get(letter)
            label = f"{letter} · {html.escape(p['title'] if p else atitle, quote=False)}"
            if p:
                side.append(f'<a class="sidebar-link" href="#{p["slug"]}"><span class="sl-text" data-t="{label}">'
                            f'<span class="sl-spine"></span>{label}</span><span class="sl-leader"></span></a>')
                rows.append(f'<div class="ce-row"><span class="ce-num">{letter}</span><a class="ce-title" href="#{p["slug"]}">{html.escape(p["title"])}</a></div>')
            else:
                side.append(f'<span class="sidebar-link is-absent" title="{ui["not_drafted"]}"><span class="sl-text" data-t="{label}">'
                            f'<span class="sl-spine"></span>{label}</span></span>')
                rows.append(f'<div class="ce-row is-absent"><span class="ce-num">{letter}</span><span class="ce-title">{html.escape(atitle)}</span><span class="ce-pg">{ui["not_drafted"]}</span></div>')
    spine_btn = (f'<button class="spine-toggle" aria-pressed="false" data-on="{ui["spine_only"]}" data-off="{ui["all_chapters"]}">'
                 f'{ui["spine_only"]}</button>')
    back = "".join(f"<span>{html.escape(l)}</span><br>" for l in st["back_cover"])
    series = st["fr"]["series"] if lang == "fr" else st["series"]

    overview = f"""<!-- ============ OVERVIEW VIEW ============ -->
<div class="view view-overview active" id="viewOverview">
<div class="overview-container">

<section class="book-hero">
<div class="hero-cover">
{cover_svg(st, ui, lang)}
</div>
<div class="hero-info">
<div class="hero-imprint ayouni">AYOUN<span class="i-dot">I</span></div>
<p class="hero-series">{html.escape(series)}</p>
<h1 class="hero-title">{html.escape(title)}</h1>
<p class="hero-subtitle">{html.escape(sub)}</p>
<p class="hero-tagline">{html.escape(tag)}</p>
<p class="hero-author">Mansour Ayouni</p>
<p class="hero-back"><span class="hb-label">{ui["back_cover"]}</span>{back}</p>
<p class="hero-status"><a href="../llms-book.txt">{ui["agents_link"]}</a> · <a href="../book.json">book.json</a></p>
{spine_btn}
<div class="view-mode-toggle" role="group" aria-label="View mode">
<button class="vm-list" id="vmList" aria-label="List view">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><circle cx="4" cy="6" r="1.2"/><circle cx="4" cy="12" r="1.2"/><circle cx="4" cy="18" r="1.2"/></svg>
</button>
<button class="vm-grid active" id="vmGrid" aria-label="Grid view">
<svg viewBox="0 0 24 24" fill="currentColor"><rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/></svg>
</button>
</div>
</div>
</section>

<section class="chapter-grid" id="chapterGrid">
{chr(10).join(cards)}
</section>

<section class="overview-contents">
<h2>{ui["contents"]}</h2>
<div class="contents-listing">
{chr(10).join(rows)}
</div>
</section>

</div><!-- /overview-container -->
</div><!-- /view-overview -->

<!-- ============ CHAPTER VIEW ============ -->
<div class="view view-chapter" id="viewChapter">
<div class="chapter-container">

<aside class="chapter-sidebar" id="chapterSidebar">
<h2 class="sidebar-book-title"><a href="#">{html.escape(title)}</a></h2>
{spine_btn}
<nav class="sidebar-nav" id="sidebarNav">
{chr(10).join(side)}
</nav>
</aside>

<main class="chapter-main">

{chr(10).join(articles)}

<nav class="ch-nav" id="chapterNav" aria-label="Chapter navigation">
<a class="ch-nav-btn" id="cnPrev" href="#">
<span class="cnb-dir">{ui["prev"]}</span>
<span class="cnb-title">—</span>
</a>
<a class="ch-nav-btn next" id="cnNext" href="#">
<span class="cnb-dir">{ui["next"]}</span>
<span class="cnb-title">—</span>
</a>
</nav>

</main>

</div><!-- /chapter-container -->
</div><!-- /view-chapter -->

"""
    return head + overview + script


# ============================================================================ status, agents
def render_status(st, en_src, fr_by_id, runs, guards, stale_keys, built):
    rows = []
    by_number = {m["number"]: (path, m, body) for path, m, body in en_src if not m.get("appendix")}
    entries = [(0, "Preface")] + [(n, t) for p in st["parts"] for n, t in p["chapters"]]
    done_count = 0
    for num, title in entries:
        sp = "●" if (num in st["spine"] or num == 0) else ""
        if num not in by_number:
            rows.append(f'<tr class="absent"><td>{num or ""}</td><td>{html.escape(title)}</td><td>{sp}</td>'
                        f'<td>not drafted</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>')
            continue
        path, m, body = by_number[num]
        key = f"en/{path.stem}"
        r = runs.get("chapters", {}).get(key)
        if key in stale_keys:
            run_txt, run_ok = "changed since its last run", False
        elif r and r["runnable"]:
            run_txt, run_ok = f'{r["kept"]} of {r["runnable"]} kept' + (f' · {r["exercises"]} exercise' if r.get("exercises") else ""), r["kept"] == r["runnable"]
        elif r:
            run_txt, run_ok = "no code", True
        else:
            run_txt, run_ok = "not run", False
        gl, g_ok = [], True
        for g in m.get("guards") or []:
            rec = guards.get("guards", {}).get(g, {})
            if rec.get("exists"):
                gl.append(f'<a href="{rec["url"]}"><code>{html.escape(g)}</code></a> {rec["assertions"]}')
            else:
                gl.append(f'<code>{html.escape(g)}</code> <b class="bad">missing</b>'); g_ok = False
        fr = m["id"] in fr_by_id
        read = m.get("status") in ("read", "final")
        checks = [run_ok and m.get("status") != "missing", g_ok, fr, read]
        done = all(checks)
        done_count += done
        marks = " ".join(f'<span class="{"ok" if c else "no"}">{lbl}</span>' for c, lbl in zip(checks, ["runs", "guards", "FR", "read"]))
        rows.append(f'<tr><td>{num or ""}</td><td><a href="en/index.html#{"preface" if num == 0 else f"ch{num}-{m["id"]}"}">{html.escape(m["title"])}</a></td>'
                    f'<td>{sp}</td><td>{html.escape(m.get("status", ""))}</td><td class="{"" if run_ok else "bad"}">{run_txt}</td>'
                    f'<td>{"<br>".join(gl)}</td><td class="num">{words_of(body)}</td><td class="num">{len(author_questions(body)) or ""}</td><td>{"yes" if fr else "no"}</td>'
                    f'<td>{"<b>done</b>" if done else ""} {marks}</td></tr>')
    by_letter = {str(m["appendix"]): (path, m, body) for path, m, body in en_src if m.get("appendix")}
    for letter, atitle in st.get("appendices", []):
        if letter not in by_letter:
            rows.append(f'<tr class="absent"><td>{letter}</td><td>{html.escape(atitle)}</td><td></td>'
                        f'<td>not drafted</td><td></td><td></td><td></td><td></td><td></td><td></td></tr>')
            continue
        path, m, body = by_letter[letter]
        key = f"en/{path.stem}"
        r = runs.get("chapters", {}).get(key)
        if key in stale_keys:
            run_txt, run_ok = "changed since its last run", False
        elif r and r["runnable"]:
            run_txt, run_ok = f'{r["kept"]} of {r["runnable"]} kept', r["kept"] == r["runnable"]
        else:
            run_txt, run_ok = "no code", True
        gl = []
        for g in m.get("guards") or []:
            rec = guards.get("guards", {}).get(g, {})
            gl.append(f'<a href="{rec["url"]}"><code>{html.escape(g)}</code></a> {rec["assertions"]}' if rec.get("exists")
                      else f'<code>{html.escape(g)}</code> <b class="bad">missing</b>')
        rows.append(f'<tr><td>{letter}</td><td><a href="en/index.html#app-{letter.lower()}-{m["id"]}">{html.escape(m["title"])}</a></td>'
                    f'<td></td><td>{html.escape(m.get("status", ""))}</td><td class="{"" if run_ok else "bad"}">{run_txt}</td>'
                    f'<td>{"<br>".join(gl)}</td><td class="num">{words_of(body)}</td><td class="num">{len(author_questions(body)) or ""}</td>'
                    f'<td>{"yes" if m["id"] in fr_by_id else "no"}</td><td>{"generated at build" if m.get("generated") else ""}</td></tr>')
    lib = runs.get("run", {}).get("library", {})
    eng = lib.get("engine_binaries", {})
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Status · Softanza — AYOUNI</title>
<script>try{{var t=localStorage.getItem("softanza-theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<style>
:root {{ {css_vars(LIGHT)} }}
:root[data-theme="dark"] {{ {css_vars(DARK)} color-scheme: dark; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ {css_vars(DARK)} color-scheme: dark; }} }}
body {{ font-family: 'Inter', system-ui, sans-serif; background: var(--bg); color: var(--ink); margin: 0; padding: 32px 16px 64px; }}
main {{ max-width: 1180px; margin: 0 auto; }}
h1 {{ font-size: 30px; font-weight: 800; letter-spacing: -0.5px; margin: 0 0 6px; }}
p.meta {{ color: var(--soft); font-size: 13px; line-height: 1.6; margin: 0 0 4px; }}
a {{ color: var(--ink); }}
.wrap {{ overflow-x: auto; margin-top: 22px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
th, td {{ border-bottom: 1px solid var(--rule); padding: 7px 9px; text-align: left; vertical-align: top; }}
th {{ font-size: 11px; letter-spacing: 1.5px; text-transform: uppercase; color: var(--soft); }}
tr.absent td {{ color: var(--soft-2); }}
td.num {{ font-variant-numeric: tabular-nums; }}
.bad, b.bad {{ color: var(--bad); }}
span.ok, span.no {{ display: inline-block; font-size: 10.5px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; padding: 1px 6px; border-radius: 3px; margin: 1px 2px 1px 0; }}
span.ok {{ color: var(--ok); background: var(--ok-bg); }}
span.no {{ color: var(--neutral); background: var(--neutral-bg); }}
code {{ font-family: ui-monospace, Consolas, monospace; font-size: 12px; }}
</style></head><body><main>
<p class="meta"><a href="en/index.html">← Softanza</a></p>
<h1>Status of the book</h1>
<p class="meta">Built {html.escape(built)}. Blocks run {html.escape(runs.get("run", {}).get("date", "never"))} inside the library at commit {html.escape(lib.get("short", "none"))} ({html.escape(lib.get("ref", ""))}, committed {html.escape(lib.get("commit_date", ""))}).</p>
<p class="meta">Engine binaries: {eng.get("count", "null")} copied from the library's {"worktree at this commit" if eng.get("pinned") else "working checkout"}, newest built {html.escape(str(eng.get("newest_build", "null")))}; {"pinned" if eng.get("pinned") else "not pinned to the commit"}.</p>
<p class="meta">Guards read {html.escape(guards.get("read", "never"))}. A chapter is done when its code runs, its guards resolve, its French exists, and the author has read it: {done_count} done.</p>
<div class="wrap"><table>
<thead><tr><th>#</th><th>Chapter</th><th>Spine</th><th>Status</th><th>Run</th><th>Guards · assertions</th><th>Words</th><th>Open questions</th><th>FR</th><th>Done</th></tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody></table></div>
</main></body></html>
"""


def doors_of(body):
    m = re.search(r"(?ms)^## 8\..*?$(.*?)(?=^## |\Z)", body)
    out = {}
    if m:
        for d in re.finditer(r"(?m)^\*\*The ([^.*]+)\.\*\*\s*(.+)$", m.group(1)):
            out[d.group(1).strip().lower()] = d.group(2).strip()
    return out


AGENT_RULES = [
    "A draft is a draft: a chapter whose status is draft is not the author's final word, and 'the author read it' is a status that only the author sets.",
    "You may quote any cell of a table. You may not turn an absent cell into a present one.",
    "Rely on the stage words: built means the code, a guard and a run; designed means a document and nothing that runs; absent means that the record was searched, and the chapter says how far.",
    "Rely on a promise only with its verdict, and only at the library commit named in this file.",
    "A number printed in the book was read from a file or a run at the date its page gives; a number the book could not read is null.",
    "The blocks ran on the runtime of the former host language, version 1.27; Haro does not run the library yet.",
    "Never name the products of other repositories: the book describes them, and says 'the interface constitution' for the one it quotes.",
]


def page_slug(m):
    if m.get("appendix"):
        return f"app-{str(m['appendix']).lower()}-{m['id']}"
    return "preface" if m["number"] == 0 else f"ch{m['number']}-{m['id']}"


def sections_of(body):
    out = []
    for h in re.findall(r"(?m)^## (.+)$", body):
        mm = re.match(r"(\d+)\.\s+(.*)", h)
        out.append({"n": int(mm.group(1)) if mm else None, "title": (mm.group(2) if mm else h).strip()})
    return out


def principle_of(body):
    m = re.search(r"(?ms)^## 2\..*?$(.*?)(?=^## |\Z)", body)
    if m:
        b = re.search(r"\*\*(.+?)\*\*", m.group(1), re.S)
        if b:
            return " ".join(b.group(1).split())
    return None


def with_verdicts(body, blocks):
    """The chapter's Markdown with, under each Haro block, the verdict of the last run, for a reader that has no page."""
    spans = code_blocks(body)
    out, last = [], 0
    for k, b in enumerate(spans):
        out.append(body[last:b["end"]])
        rec = blocks[k] if k < len(blocks) else {}
        v = rec.get("verdict") or "not run"
        out.append("\n\n> run: " + v + (" (touches " + ", ".join(rec["effects"]) + ")" if rec.get("effects") else ""))
        last = b["end"]
    out.append(body[last:])
    return "".join(out)


def agents_files(st, en_src, runs, guards, built, fr_ids):
    law_by_part = {p["number"]: p.get("law") for p in st["parts"]}
    lib = runs.get("run", {}).get("library", {})
    rt = runs.get("run", {}).get("runtime")
    chapters, texts = [], []
    (ROOT / "agents").mkdir(exist_ok=True)
    for path, m, body in en_src:
        r = runs.get("chapters", {}).get(f"en/{path.stem}", {})
        if m.get("generated"):
            body = body.rstrip() + "\n\n" + generated_body(m["generated"], en_src, guards, runs, st)
        spans = code_blocks(body)
        rb = r.get("blocks") or []
        promises = []
        for k, b in enumerate(spans):
            rec = rb[k] if k < len(rb) else {}
            promises.append({"code": b["text"], "promised": rec.get("promise", ""), "output": rec.get("out", ""),
                             "verdict": rec.get("verdict"), "effects": rec.get("effects") or []})
        part = m.get("part")
        slug = page_slug(m)
        kind = "appendix" if m.get("appendix") else ("preface" if m["number"] == 0 else "chapter")
        doors = doors_of(body)
        text_path = f"agents/{slug}.md"
        entry = {
            "number": m["number"], "id": m["id"], "title": m["title"], "slug": slug, "kind": kind,
            "part": part, "appendix": m.get("appendix"),
            "law": m.get("law") or (law_by_part.get(part) if m["number"] in (5, 11, 17) else None),
            "principle": principle_of(body),
            "spine": bool(m.get("spine")) or m["number"] in st["spine"], "status": m.get("status", "draft"),
            "stage": m.get("stage") or {},
            "guards": [{"name": g, **{k: v for k, v in guards.get("guards", {}).get(g, {}).items() if k in ("exists", "path", "assertions", "url")}}
                       for g in m.get("guards") or []],
            "promises": promises, "narrations": m.get("narrations") or [], "rulings": [str(x) for x in (m.get("rulings") or [])],
            "doors": doors, "sections": sections_of(body),
            "open_questions": [" ".join(q.split()) for q in author_questions(body)],
            "words": words_of(body), "french": m["id"] in fr_ids, "text": text_path,
            "run": {k: r.get(k) for k in ("ran", "kept", "runnable")} if r else None,
        }
        chapters.append(entry)
        lead = "Appendix " + m["appendix"] if m.get("appendix") else ("Preface" if m["number"] == 0 else "Chapter " + str(m["number"]))
        head = [f"# {m['title']}", "",
                f"Source: {lead}. Status: {entry['status']}" + (" (a draft, not read by the author)" if entry["status"] == "draft" else "")
                + f". Library commit {lib.get('short', 'null')}.", ""]
        if entry["stage"]:
            head += ["Stage: " + "; ".join(f"{k}: {v}" for k, v in entry["stage"].items()), ""]
        if entry["run"] and entry["run"].get("runnable"):
            head += [f"Run: {entry['run']['kept']} of {entry['run']['runnable']} blocks kept their promise, on {entry['run'].get('ran')}.", ""]
        txt = "\n".join(head) + "\n" + with_verdicts(body, rb).strip() + "\n"
        (ROOT / text_path).write_text(txt, encoding="utf-8")
        texts.append(txt)
    data = {"schema": "softanza-book/2", "title": st["title"], "subtitle": st["subtitle"], "tagline": st["tagline"], "author": st["author"],
            "series": st["series"], "built": built, "library_commit": lib.get("commit"),
            "edition": "proof copy" if any(c["status"] != "read" for c in chapters) else "read by the author",
            "runtime": {"name": "the former host language", "version": (rt or {}).get("version"), "haro_runs_the_library": False},
            "spine": st["spine"], "rules_for_agents": AGENT_RULES,
            "files": {"schema": "book.schema.json", "summary": "llms-book.txt", "full_text": "llms-full-book.txt",
                      "per_page": "agents/<slug>.md", "reader_en": "en/index.html", "reader_fr": "fr/index.html"},
            "chapters": chapters,
            "note": "Drafts are marked status: draft and are not the author's final word."}
    schema = json.loads((ROOT / "book.schema.json").read_text(encoding="utf-8"))
    problems = validate(data, schema)
    (ROOT / "book.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    lines = [f"# {st['title']} · {st['subtitle']}", "", f"> {st['tagline'].rstrip('.')}. By {st['author']}. {st['series']}.", "",
             "This book runs: every code block was run inside the Softanza library at the commit named below, and judged against the `#-->` promise lines it carries. A draft is marked as a draft.", "",
             f"Edition: {data['edition']} ({sum(1 for c in chapters if c['status'] != 'read')} of {len(chapters)} pages not yet read by the author). Built {built}. Library commit {lib.get('commit', 'null')}. Blocks ran on the runtime of the former host language, version {(rt or {}).get('version', 'null')}; Haro does not run the library yet.", "",
             "## Files", "",
             "- book.json: the whole book as data, one entry per chapter, preface and appendix; book.schema.json describes it",
             "- llms-full-book.txt: every page as text, with the verdict of the last run under each code block",
             "- agents/<slug>.md: one page as text (the slug is in book.json)",
             "- en/index.html, fr/index.html: the reader (status.html, the builder's page, is in the repository and not on the public site)", "",
             "## Rules for an agent", ""] + [f"- {x}" for x in AGENT_RULES] + ["", "## Pages", ""]
    seen_part = None
    for c in chapters:
        head = None
        if c.get("appendix"):
            head = "Appendices"
        elif c.get("part"):
            pt = next((x for x in st["parts"] if x["number"] == c["part"]), None)
            head = f"Part {ROMAN[c['part']]} · {pt['title']}" if pt else f"Part {ROMAN[c['part']]}"
        if head and head != seen_part:
            lines += ["", f"### {head}", ""]
            seen_part = head
        g = ", ".join(f"{x['name']} ({x.get('assertions', 'missing')})" for x in c["guards"]) or "none"
        run = f"{c['run']['kept']} of {c['run']['runnable']} blocks kept" if c["run"] and c["run"].get("runnable") else "no code"
        lead = f"Appendix {c['appendix']}" if c.get("appendix") else f"{c['number']}."
        lines.append(f"- {lead} {c['title']} [{c['status']}{', spine' if c['spine'] else ''}] {c['text']}; guards: {g}; run: {run}")
        if c.get("principle"):
            lines.append(f"  principle: {c['principle'][0].upper() + c['principle'][1:]}")
    (ROOT / "llms-book.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "llms-full-book.txt").write_text(
        f"# {st['title']} · {st['subtitle']}\n\nBuilt {built}. Library commit {lib.get('commit', 'null')}. Every page below is a draft unless it says otherwise.\n\n"
        + "\n\n=====\n\n".join(texts), encoding="utf-8")
    return problems


# ============================================================================ main
def main():
    if "--render-only" not in sys.argv:
        for tool in ("book_run.py", "book_guards.py"):
            r = subprocess.run([sys.executable, str(ROOT / "tools" / tool)])
            if r.returncode not in (0, 1):
                raise SystemExit(f"{tool} could not run (exit {r.returncode})")
    built = stamp(now())
    st = structure()
    global SITE_BASE
    SITE_BASE = st.get("site_base", SITE_BASE)
    runs = load_json("book-run.json", {})
    guards = load_json("guards.json", {})
    # the figures that carry numbers are generated from the snapshot the book ran at
    short = runs.get("run", {}).get("library", {}).get("short")
    snap = ROOT / ".cache" / f"stzlib-{short}" / "libraries" / "stzlib"
    if short and snap.exists():
        import figures
        figures.generate(ROOT, snap)
    en_src = sources("en")
    fr_src = sources("fr")
    errors = []

    # the build's checks
    errors.extend(check_type_scale())
    for lang, srcs in (("en", en_src), ("fr", fr_src)):
        for path, m, body in srcs:
            bad = former_name_fences(body)
            if bad:
                errors.append(f"{lang}/{path.stem}: a fence still names the former host language ({', '.join(bad)}); section 4.8")
    stale_keys = set()
    for lang, srcs in (("en", en_src), ("fr", fr_src)):
        for path, m, body in srcs:
            key = f"{lang}/{path.stem}"
            r = runs.get("chapters", {}).get(key)
            hashes = [block_hash(b["text"]) for b in code_blocks(body)]
            if hashes and (not r or [b.get("hash") for b in r["blocks"]] != hashes):
                stale_keys.add(key); errors.append(f"{key}: its code changed since its last run (or never ran)")
            elif r and r["runnable"] and r["kept"] < r["runnable"]:
                errors.append(f"{key}: {r['kept']} of {r['runnable']} blocks kept their promise")
    for name, g in guards.get("guards", {}).items():
        if not g.get("exists"):
            errors.append(f"guard {name} does not exist in the library's test tree")

    fr_by_id = {m["id"]: (p, m, b) for p, m, b in fr_src}
    en_by_id = {m["id"]: (p, m, b) for p, m, b in en_src}
    for lang, by_id in (("en", en_by_id), ("fr", fr_by_id)):
        pages = build_pages(lang, st, en_src, by_id, runs, guards, UI[lang])
        page = render_reader(lang, st, pages, runs, guards, stale_keys)
        left = check_colours(page)
        if left:
            errors.append(f"{lang}/index.html: colours outside the variables: {left}")
        (ROOT / lang).mkdir(exist_ok=True)
        (ROOT / lang / "index.html").write_text(page, encoding="utf-8")
        if "substrate" in page.lower():
            errors.append(f"{lang}/index.html: the word 'substrate' appears")
    (ROOT / "index.html").write_text('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
                                     '<meta http-equiv="refresh" content="0; url=en/index.html"><title>Softanza — AYOUNI</title></head>'
                                     '<body><a href="en/index.html">Softanza</a></body></html>\n', encoding="utf-8")
    (ROOT / "status.html").write_text(render_status(st, en_src, fr_by_id, runs, guards, stale_keys, built), encoding="utf-8")
    for pr in agents_files(st, en_src, runs, guards, built, set(fr_by_id)):
        errors.append(f"book.json does not match book.schema.json: {pr}")
    print(f"built {built}: en/index.html, fr/index.html, status.html, book.json, llms-book.txt")
    if errors:
        print("BUILD FAILED:\n  " + "\n  ".join(errors))
        sys.exit(1)
    print("build passed")


if __name__ == "__main__":
    main()
