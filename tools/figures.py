"""The book's figures that carry numbers, generated at build from the files that hold the numbers.

A figure drawn by hand would carry typed numbers, which the method forbids (section 9: every number is read,
never composed). So the picture of chapter 4 is written here, at build, from:
  - the library snapshot the book ran at: engine/build.zig (the engine's libraries by layer), engine/vendor/
    (the third-party libraries vendored and pinned), base/test (the narrated guards);
  - the site's Atlas index (data/atlas-index.json): the bands, the areas and the lanes.
Colours are CSS classes, so the figure follows the reader's light and dark themes.
"""
import html, json, re, pathlib

SITE = pathlib.Path("D:/GitHub/stzsite")


def read_facts(lib):
    """The figure's numbers, each with where it was read."""
    facts = {}
    b = (lib / "engine" / "build.zig").read_text(encoding="utf-8")
    def domains(name):
        m = re.search(name + r"\s*=\s*\[_\]Domain\{(.*?)\n\};", b, re.S)
        return len(re.findall(r'\.name\s*=\s*"', m.group(1))) if m else 0
    facts["core_libs"], facts["base_libs"] = domains("core_domains"), domains("base_domains")
    facts["max_libs"] = domains("max_domains")
    vendor = lib / "engine" / "vendor"
    facts["vendored"] = len([p for p in vendor.iterdir() if p.is_dir()]) if vendor.exists() else 0
    facts["guards"] = len(list((lib / "base" / "test").rglob("*_narrated.ring")))
    atlas = json.loads((SITE / "data" / "atlas-index.json").read_text(encoding="utf-8"))
    facts["atlas"] = {"version": atlas.get("version"), "read_at": atlas.get("read_at"), "commit": atlas.get("commit"),
                      "areas": len(atlas["groups"]), "lanes": atlas["tally"]["lanes"]}
    bands = []
    for band in atlas["bands"]:
        groups = [g for g in atlas["groups"] if g["band"] == band["id"]]
        lanes = sum(g.get("s", 0) + g.get("so", 0) + g.get("p", 0) + g.get("e", 0) for g in groups)
        bands.append({"en": band["en"], "fr": band.get("fr", band["en"]), "areas": [g["en"] for g in groups], "lanes": lanes})
    facts["bands"] = bands
    return facts


def T(x, y, s, cls="fg-txt", size=12, weight=400, anchor="start", italic=False):
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x}" y="{y}" class="{cls}" font-family="Inter, system-ui, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}"{st}>{html.escape(str(s))}</text>')


def R(x, y, w, h, cls="fg-box", dash=False, rx=6):
    d = ' stroke-dasharray="5 4"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"{d}/>'


def platform_svg(f, lang="en"):
    W, H = 805, 700
    L, CW = 70, 500          # the floors' left edge and width
    CX, CCW = 588, 205       # the court column
    out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" '
           f'aria-label="The Softanza platform in one picture: five floors, and a court beside each">']
    # the court column
    out.append(R(CX, 18, CCW, H - 36, "fg-court", rx=8))
    out.append(T(CX + CCW / 2, 40, "The court", "fg-txt", 13, 700, "middle"))
    out.append(T(CX + CCW / 2, 57, "nothing is believed,", "fg-soft", 11, 400, "middle", True))
    out.append(T(CX + CCW / 2, 71, "everything is judged", "fg-soft", 11, 400, "middle", True))
    floors = [  # y, height, title, court lines
        (90, 92, "The makers", ["the interface constitution:", "every element traces to a verb"]),
        (196, 112, "The worlds", ["bonds and norms between worlds;", "build before deploy;", "no fake in production"]),
        (322, 150, "The areas", [f"{f['atlas']['lanes']} lanes, each rated", "with its proof line"]),
        (486, 92, "The layers", [f"{f['guards']} narrated guards,", "one dependency rule"]),
        (592, 92, "The engine", ["engine tests; contracts", "between the floors"]),
    ]
    for y, h, title, court in floors:
        out.append(R(L, y, CW, h, "fg-floor", rx=8))
        out.append(T(L + 12, y + 18, title, "fg-accent", 11, 700))
        out.append(f'<line x1="{L + CW}" y1="{y + h / 2}" x2="{CX}" y2="{y + h / 2}" class="fg-arrow" marker-end="url(#fgarr)"/>')
        for k, line in enumerate(court):
            out.append(T(CX + 12, y + h / 2 - (len(court) - 1) * 7 + k * 14 + 4, line, "fg-txt", 11))
    # floor 5, the makers: six doors
    doors = ["programmer", "analyst", "designer", "decision-maker", "educator", "agent"]
    dw = (CW - 24 - 5 * 6) / 6
    for k, d in enumerate(doors):
        x = L + 12 + k * (dw + 6)
        out.append(R(x, 116, dw, 52, "fg-box"))
        out.append(T(x + dw / 2, 147, d, "fg-txt", 10.5, 600, "middle"))
    # floor 4, the worlds
    worlds = [("a world", "stzApp"), ("a constellation", "stzSuperApp"), ("a platform", "stzPlatform")]
    ww = (CW - 24 - 2 * 10) / 3
    for k, (a, b) in enumerate(worlds):
        x = L + 12 + k * (ww + 10)
        out.append(R(x, 222, ww, 46, "fg-box"))
        out.append(T(x + ww / 2, 241, a, "fg-txt", 12, 600, "middle"))
        out.append(T(x + ww / 2, 257, b, "fg-soft", 10.5, 400, "middle"))
    out.append(T(L + CW / 2, 292, "three scopes: development · deployment · runtime", "fg-soft", 11, 400, "middle", True))
    # floor 3, the areas: the Atlas's bands
    bw = (CW - 24 - 2 * 8) / 3
    for k, band in enumerate(f["bands"]):
        col, row = k % 3, k // 3
        x, y = L + 12 + col * (bw + 8), 346 + row * 60
        out.append(R(x, y, bw, 52, "fg-box"))
        out.append(T(x + 8, y + 17, band["en"] if len(band["en"]) < 30 else band["en"][:28] + "…", "fg-txt", 10.5, 700))
        names = ", ".join(a.lower() for a in band["areas"])
        out.append(T(x + 8, y + 32, names if len(names) < 34 else names[:32] + "…", "fg-soft", 9.5))
        out.append(T(x + 8, y + 45, f"{len(band['areas'])} areas · {band['lanes']} lanes", "fg-soft", 9.5))
    # floor 2, the layers: base widest
    out.append(R(L + 12, 512, 90, 52, "fg-box"))
    out.append(T(L + 57, 534, "core", "fg-txt", 12, 700, "middle"))
    out.append(T(L + 57, 550, "stk · lean", "fg-soft", 10, 400, "middle"))
    out.append(R(L + 110, 512, 270, 52, "fg-box-strong"))
    out.append(T(L + 245, 534, "base", "fg-txt", 12, 700, "middle"))
    out.append(T(L + 245, 550, "stz · most of the code, by debt", "fg-soft", 10, 400, "middle"))
    out.append(R(L + 388, 512, 100, 52, "fg-box", dash=True))
    out.append(T(L + 438, 534, "max", "fg-txt", 12, 700, "middle"))
    out.append(T(L + 438, 550, "stx · in part", "fg-soft", 10, 400, "middle"))
    # floor 1, the engine
    out.append(R(L + 12, 618, CW - 24, 52, "fg-box-strong"))
    out.append(T(L + CW / 2, 638, f"Zig · {f['core_libs'] + f['base_libs']} libraries behind a C interface: "
                 f"{f['core_libs']} for core, {f['base_libs']} for base, {f['max_libs'] or 'none yet'} for max", "fg-txt", 11.5, 600, "middle"))
    out.append(T(L + CW / 2, 656, f"{f['vendored']} third-party libraries vendored and pinned: none that anyone can withdraw",
                 "fg-soft", 10.5, 400, "middle"))
    # the architect, spanning every floor
    out.append(f'<line x1="36" y1="680" x2="36" y2="96" class="fg-arrow-strong" marker-end="url(#fgarr2)"/>')
    out.append(f'<text x="28" y="390" class="fg-accent" font-family="Inter, system-ui, sans-serif" font-size="11" font-weight="700" '
               f'text-anchor="middle" transform="rotate(-90 28 390)">the platform architect</text>')
    # arrow heads
    out.insert(1, '<defs><marker id="fgarr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
                  '<path d="M0,0 L10,5 L0,10 z" class="fg-head"/></marker>'
                  '<marker id="fgarr2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
                  '<path d="M0,0 L10,5 L0,10 z" class="fg-head-strong"/></marker></defs>')
    out.append("</svg>")
    return "\n".join(out)


def generate(root, lib):
    """Write the generated figures into assets/figures/, and their facts beside them in data/."""
    facts = read_facts(lib)
    figs = root / "assets" / "figures"
    figs.mkdir(parents=True, exist_ok=True)
    (figs / "platform-one-picture.svg").write_text(platform_svg(facts), encoding="utf-8")
    (root / "data" / "figures.json").write_text(json.dumps(facts, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return facts
