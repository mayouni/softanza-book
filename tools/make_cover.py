"""Compose the flat front cover (assets/cover/cover.png, cover.fr.png) from the author's figure and the AYOUNI logo.

The first design (1097 x 1434 proportion; wordmark top left, title block left, the figure on the right, author bottom left,
cities and year bottom right), on a pure white page as the author asked (COVER-04), drawn at twice the logical size
(2194 x 2868) so the logo and the type stay sharp. Inputs live in assets/cover/source/: elder.png (the figure) and
ayouni-logo.png (the logo, rasterised from ayouni-logo.svg, which the house traced from the author's file).
Run: python tools/make_cover.py
"""
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "cover" / "source"
OUTS = {"en": ROOT / "assets" / "cover" / "cover.png", "fr": ROOT / "assets" / "cover" / "cover.fr.png"}
K = 2                                   # drawn at twice the logical 1097 x 1434
W, H = 1097 * K, 1434 * K
PAPER = (255, 255, 255)
INK = (20, 20, 20)
GREY = (110, 110, 106)
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


def main():
    for lang in OUTS:
        make(lang)


if __name__ == "__main__":
    sys.exit(main())
