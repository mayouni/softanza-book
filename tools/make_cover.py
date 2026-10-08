"""Compose the flat front cover (assets/cover/cover.png) from the two images the author supplied.

Layout follows the Refinement-Oriented Programming cover (1097 x 1434, off-white paper, wordmark top left,
title block left, the figure on the right, author bottom left, cities and year bottom right), without the
hands: the strict rectangular image only. Inputs live in assets/cover/source/. Run: python tools/make_cover.py
"""
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "cover" / "source"
OUTS = {"en": ROOT / "assets" / "cover" / "cover.png", "fr": ROOT / "assets" / "cover" / "cover.fr.png"}
W, H = 1097, 1434
PAPER = (247, 246, 242)
INK = (20, 20, 20)
GREY = (110, 110, 106)
FONTS = Path("C:/Windows/Fonts")


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def logo_with_alpha(path, width):
    """The supplied logo carries a drawn checkerboard instead of transparency: take the coloured pixels only."""
    im = Image.open(path).convert("RGB")
    px = im.load()
    w, h = im.size
    out = Image.new("RGBA", (w, h))
    po = out.load()
    bg = 238.0
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            chroma = max(r, g, b) - min(r, g, b)
            a = min(1.0, max(0.0, (chroma - 10) / 70.0))
            if a <= 0:
                po[x, y] = (0, 0, 0, 0)
                continue
            c = [min(255, max(0, int((v - (1 - a) * bg) / a))) for v in (r, g, b)]
            po[x, y] = (c[0], c[1], c[2], int(a * 255))
    box = out.getbbox()
    out = out.crop(box)
    return out.resize((width, round(out.height * width / out.width)), Image.LANCZOS)


def wrap(draw, text, fnt, maxw):
    lines, cur = [], ""
    for word in text.split():
        t = (cur + " " + word).strip()
        if draw.textlength(t, font=fnt) <= maxw or not cur:
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

    logo = logo_with_alpha(SRC / "ayouni-logo.jpg", 232)
    cover.paste(logo, (80, 92), logo)

    man = Image.open(SRC / "elder.png").convert("RGBA")
    man = man.crop(man.getbbox())
    scale = 0.74
    man = man.resize((round(man.width * scale), round(man.height * scale)), Image.LANCZOS)
    cover.paste(man, (W - man.width + 8, 1318 - man.height), man)

    x = 80
    d.text((x, 232), st["title"], font=font("arial.ttf", 112), fill=INK)
    y = 400
    for line in wrap(d, st["subtitle"], font("arial.ttf", 46), 400):
        d.text((x, y), line, font=font("arial.ttf", 46), fill=INK)
        y += 58
    y += 26
    ital = font("georgiai.ttf", 31)
    for line in wrap(d, st["tagline"], ital, 390):
        d.text((x, y), line, font=ital, fill=INK)
        y += 46

    d.text((x, 1366), "MANSOUR AYOUNI", font=font("arialbd.ttf", 28), fill=INK)
    right = "TUNIS · NIAMEY · PARIS · 2026"
    f = font("arial.ttf", 26)
    d.text((W - 80 - d.textlength(right, font=f), 1368), right, font=f, fill=GREY)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    cover.save(OUT)
    print("wrote", OUT, cover.size)


def main():
    for lang in OUTS:
        make(lang)


if __name__ == "__main__":
    sys.exit(main())
