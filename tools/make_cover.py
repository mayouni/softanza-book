"""Compose the flat covers: the front (assets/cover/cover.png, cover.fr.png) from the author's figure and the AYOUNI logo,
and the back (assets/cover/back.png, back.fr.png, COVER-05) on the same grid, from src/structure.yaml.

The first design (1097 x 1434 proportion; wordmark top left, title block left, the figure on the right, author bottom left,
cities and year bottom right), on a pure white page as the author asked (COVER-04), drawn at twice the logical size
(2194 x 2868) so the logo and the type stay sharp. Inputs live in assets/cover/source/: elder.png (the figure) and
ayouni-logo.png (the logo, rasterised from ayouni-logo.svg, which the house traced from the author's file).
The back carries the author's two lines, the description (the preface's own sentences, never new prose), the imprint,
a QR code to the free reader in its language, the edition and the licence. Run: python tools/make_cover.py
"""
import sys
from pathlib import Path

import json

import segno
import yaml
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "cover" / "source"
OUTS = {"en": ROOT / "assets" / "cover" / "cover.png", "fr": ROOT / "assets" / "cover" / "cover.fr.png"}
BACKS = {"en": ROOT / "assets" / "cover" / "back.png", "fr": ROOT / "assets" / "cover" / "back.fr.png"}
K = 2                                   # drawn at twice the logical 1097 x 1434
W, H = 1097 * K, 1434 * K
PAPER = (255, 255, 255)
INK = (20, 20, 20)
GREY = (110, 110, 106)
GREY_DARK = (58, 56, 52)
RULE = (200, 198, 192)
RED = (212, 21, 25)          # the dot of the AYOUNI logo
FONTS = Path("C:/Windows/Fonts")


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size * K)


def logo_png(width):
    im = Image.open(SRC / "ayouni-logo.png").convert("RGBA")
    im = im.crop(im.getbbox())
    return im.resize((width * K, round(im.height * width * K / im.width)), Image.LANCZOS)


def wrap(draw, text, fnt, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if draw.textlength(t, font=fnt) <= maxw * K or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = word
    return lines + [cur]


def make(lang):
    st = yaml.safe_load((ROOT / "src" / "structure.yaml").read_text(encoding="utf-8"))
    if lang == "fr":
        st = {**st, **st["fr"]}
    OUT = OUTS[lang]
    cover = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(cover)

    logo = logo_png(232)
    cover.paste(logo, (80 * K, 92 * K), logo)

    man = Image.open(SRC / "elder.png").convert("RGBA")
    man = man.crop(man.getbbox())
    scale = 0.74 * K
    man = man.resize((round(man.width * scale), round(man.height * scale)), Image.LANCZOS)
    cover.paste(man, (W - man.width + 8 * K, 1318 * K - man.height), man)

    x = 80 * K
    d.text((x, 232 * K), st["title"], font=font("arial.ttf", 112), fill=INK)
    y = 400 * K
    for line in wrap(d, st["subtitle"], font("arial.ttf", 46), 400):
        d.text((x, y), line, font=font("arial.ttf", 46), fill=INK)
        y += 58 * K
    y += 26 * K
    ital = font("georgiai.ttf", 31)
    for line in wrap(d, st["tagline"], ital, 390):
        d.text((x, y), line, font=ital, fill=INK)
        y += 46 * K

    d.text((x, 1366 * K), "MANSOUR AYOUNI", font=font("arialbd.ttf", 28), fill=INK)
    right = "TUNIS \u00b7 NIAMEY \u00b7 PARIS \u00b7 2026"
    f = font("arial.ttf", 26)
    d.text((W - 80 * K - d.textlength(right, font=f), 1368 * K), right, font=f, fill=GREY)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    cover.save(OUT)
    print("wrote", OUT, cover.size)


def typeset(text, fr):
    """Typographic apostrophes; in French, no line may start with a colon, a question or exclamation mark, or a semicolon."""
    text = text.replace("'", "\u2019")
    if fr:
        for mark in (":", "?", "!", ";"):
            text = text.replace(" " + mark, "\u00a0" + mark)
    return text


def rich_lines(draw, text, regular, bold, maxw):
    """Wrap a paragraph whose **...** runs are bold; returns lines of (word, font) pairs."""
    words, on = [], False
    for i, part in enumerate(text.split("**")):
        on = i % 2 == 1
        words += [(w, bold if on else regular) for w in part.split(" ") if w]
    lines, cur, width = [], [], 0
    for w, f in words:
        ww = draw.textlength(w, font=f)
        sp = draw.textlength(" ", font=f) if cur else 0
        if cur and width + sp + ww > maxw * K:
            lines.append(cur)
            cur, width = [(w, f)], ww
        else:
            cur.append((w, f))
            width += sp + ww
    return lines + ([cur] if cur else [])


def spaced(draw, xy, text, fnt, fill, track):
    """Letter-spaced capitals (track in logical px)."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + track * K
    return x


def spaced_width(draw, text, fnt, track):
    return sum(draw.textlength(ch, font=fnt) for ch in text) + track * K * (len(text) - 1)


def qr_image(url, size):
    """The QR code of the free reader, drawn module by module (no plugin), error level M, on white."""
    q = segno.make(url, error="m", micro=False)
    m = list(q.matrix)
    n = len(m)
    cell = (size * K) // n
    im = Image.new("RGB", (cell * n, cell * n), PAPER)
    d = ImageDraw.Draw(im)
    for r, row in enumerate(m):
        for c, v in enumerate(row):
            if v:
                d.rectangle((c * cell, r * cell, (c + 1) * cell - 1, (r + 1) * cell - 1), fill=INK)
    return im


def portrait(size):
    """The author's portrait as a disc, antialiased (drawn at four times, then reduced); never enlarged."""
    src = Image.open(SRC / "author.png").convert("RGB")
    side = min(src.size)
    src = src.crop(((src.width - side) // 2, (src.height - side) // 2, (src.width + side) // 2, (src.height + side) // 2))
    px = size * K
    if px > side:
        raise SystemExit(f"the portrait is {side} px; the cover asks {px}: it would be enlarged")
    src = src.resize((px, px), Image.LANCZOS)
    mask = Image.new("L", (px * 4, px * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, px * 4 - 1, px * 4 - 1), fill=255)
    return src, mask.resize((px, px), Image.LANCZOS)


BAND = 1192          # the imprint band's hairline
BODY_SIZES = (25, 24, 23, 22)


def make_back(lang, body, write=True):
    """Draw the back cover with the description at `body` px; returns the free space above the author (negative: it overflows)."""
    st = yaml.safe_load((ROOT / "src" / "structure.yaml").read_text(encoding="utf-8"))
    fr = lang == "fr"
    loc = {**st, **st["fr"]} if fr else st
    edition = json.loads((ROOT / "book.json").read_text(encoding="utf-8")).get("edition", "proof copy")
    fix = lambda s: typeset(s, fr)
    back = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(back)
    x, right, maxw = 80 * K, W - 80 * K, 937

    # the book named first (COVER-06), then the author's two lines together (PRINT-03), then the accent
    head, place = st["back_cover"][1], st["back_cover"][0]
    spaced(d, (x, 86 * K), fix(f'{loc["title"]} · {loc["subtitle"]}').upper(), font("arialbd.ttf", 17), GREY, 2.0)
    d.text((x, 116 * K), head, font=font("arial.ttf", 68), fill=INK)
    d.text((x, 204 * K), place, font=font("georgiai.ttf", 31), fill=INK)
    d.rectangle((x, 262 * K, x + 64 * K, 262 * K + 5 * K), fill=RED)

    # the description: the hook, the thesis, what Softanza is, who it is for
    y = 296 * K
    lead = round(body * 1.42)
    reg, bld = font("georgia.ttf", body), font("georgiab.ttf", body)
    for para in loc["back_blurb"]:
        if para.startswith("## "):
            y += 6 * K
            spaced(d, (x, y), fix(para[3:]).upper(), font("arialbd.ttf", 16), RED, 2.0)
            y += 28 * K
            continue
        for line in rich_lines(d, fix(para), reg, bld, maxw):
            cx = x
            for w, f in line:
                d.text((cx, y), w, font=f, fill=INK)
                cx += d.textlength(w + " ", font=f)
            y += lead * K
        y += 12 * K
    d.text((x, y), fix(loc["back_runs"]), font=font("arial.ttf", 22), fill=INK)
    y += 28 * K

    # the author (COVER-07): his portrait as a disc, his name, his note; set just above the imprint band
    disc = 120
    tx, tw = x + (disc + 26) * K, 937 - disc - 26
    nf, bf = font("arialbd.ttf", 18), font("georgia.ttf", 20)
    note = rich_lines(d, fix(loc.get("back_author_note") or st["back_author_note"]), bf, bf, tw)
    block = max(disc, 30 + 28 * len(note))
    top = BAND - 24 - block
    free = top - 20 - y // K
    if not write:
        return free
    if free < 0:
        raise SystemExit(f"back cover ({lang}): the description runs into the author ({-free} px too long at {body} px)")
    photo, mask = portrait(disc)
    back.paste(photo, (x, top * K), mask)
    spaced(d, (tx, top * K), st["back_author"].upper(), nf, INK, 1.6)
    yy = (top + 30) * K
    for line in note:
        d.text((tx, yy), " ".join(w for w, _ in line), font=bf, fill=GREY_DARK)
        yy += 28 * K

    # the imprint band: a hairline, the logo and the series on the left; the free reader and its QR code on the right
    d.rectangle((x, BAND * K, right, BAND * K + 1 * K), fill=RULE)
    logo = logo_png(180)
    back.paste(logo, (x, (BAND + 28) * K), logo)
    spaced(d, (x, (BAND + 28) * K + logo.height + 16 * K), loc["series"].upper(), font("arialbd.ttf", 16), GREY, 2.2)
    qr = qr_image(loc["back_url"], 132)
    back.paste(qr, (right - qr.width, (BAND + 22) * K))
    qx = right - qr.width - 28 * K
    f1, f2 = font("arial.ttf", 23), font("arial.ttf", 20)
    url = loc["back_url"].split("://", 1)[1]
    host, path = url.split("/", 1)[0] + "/ayouni/", url.split("/ayouni/", 1)[1]
    for i, (s, f, c) in enumerate(((loc["back_free"], f1, INK), (host, f2, GREY), (path, f2, GREY))):
        d.text((qx - d.textlength(s, font=f), (BAND + 30 + (0 if i == 0 else 6 + 28 * i)) * K), s, font=f, fill=c)

    # the foot: the shelf on the left, the edition and the licence on the right, on the front's baseline
    foot, track = font("arial.ttf", 19), 0.8
    cat = fix(loc["back_category"]).upper()
    ed = ("ÉPREUVE DE TRAVAIL · " if fr else "PROOF COPY · ") if edition == "proof copy" else ""
    lic = ed + "CC BY-NC-ND 4.0"
    end_cat = spaced(d, (x, 1373 * K), cat, foot, GREY, track)
    start_lic = right - spaced_width(d, lic, foot, track)
    if start_lic - end_cat < 40 * K:
        raise SystemExit(f"back cover ({lang}): the foot's two lines touch ({(start_lic - end_cat) // K} px apart)")
    spaced(d, (start_lic, 1373 * K), lic, foot, GREY, track)

    out = BACKS[lang]
    back.save(out)
    print("wrote", out, back.size, f"body {body} px, {free} px free above the author, foot gap {(start_lic - end_cat) // K}")
    return free


def fitted_body():
    """The largest description size at which both editions fit: one size for both, so the two backs match."""
    for body in BODY_SIZES:
        if all(make_back(lang, body, write=False) >= 0 for lang in BACKS):
            return body
    raise SystemExit(f"the back cover's description does not fit at {BODY_SIZES[-1]} px: shorten it in src/structure.yaml")


def main():
    body = fitted_body()
    for lang in OUTS:
        make(lang)
        make_back(lang, body)


if __name__ == "__main__":
    sys.exit(main())
