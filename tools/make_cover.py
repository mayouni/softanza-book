"""Compose the flat front cover (assets/cover/cover.png, cover.fr.png) from the author's figure and the AYOUNI logo.

Layout follows the series template (wordmark top left, title block left, the figure on the right, author bottom left,
cities and year bottom right), on a pure white page, with type sized to read at about 440 px wide (the size the house
shows a cover at): title, subtitle and tagline large, nothing italic and tiny. Drawn at twice the logical size
(2194 x 2868, the 1097 x 1434 proportion kept) so the logo and the text are sharp on screen and in print.
Inputs live in assets/cover/source/: elder.png (the figure) and ayouni-logo.png (the logo, rasterised from
ayouni-logo.svg, which the house traced from the author's file). Run: python tools/make_cover.py
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
PAPER = (255, 255, 255)                 # pure white, as the author asked
INK = (23, 20, 15)
GREY = (74, 70, 64)
FONTS = Path("C:/Windows/Fonts")


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), round(size * K))


def logo_png(width):
    im = Image.open(SRC / "ayouni-logo.png").convert("RGBA")
    im = im.crop(im.getbbox())
    return im.resize((round(width * K), round(im.height * width * K / im.width)), Image.LANCZOS)


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

    logo = logo_png(380)
    cover.paste(logo, (80 * K, 84 * K), logo)

    man = Image.open(SRC / "elder.png").convert("RGBA")
    man = man.crop(man.getbbox())
    scale = 0.72 * K
    man = man.resize((round(man.width * scale), round(man.height * scale)), Image.LANCZOS)
    cover.paste(man, (W - man.width + 8 * K, 1318 * K - man.height), man)

    x, colw = 80 * K, 440
    d.text((x, 214 * K), st["title"], font=font("arialbd.ttf", 148), fill=INK)
    y = 420 * K
    f_sub = font("arialbd.ttf", 56)
    for line in wrap(d, st["subtitle"], f_sub, colw):
        d.text((x, y), line, font=f_sub, fill=INK)
        y += 70 * K
    y += 30 * K
    f_tag = font("arial.ttf", 37)
    for line in wrap(d, st["tagline"], f_tag, colw):
        d.text((x, y), line, font=f_tag, fill=INK)
        y += 52 * K

    d.text((x, 1362 * K), "MANSOUR AYOUNI", font=font("arialbd.ttf", 32), fill=INK)
    right = "TUNIS · NIAMEY · PARIS · 2026"
    f = font("arialbd.ttf", 27)
    d.text((W - 80 * K - d.textlength(right, font=f), 1366 * K), right, font=f, fill=GREY)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    cover.save(OUT)
    print("wrote", OUT, cover.size)


def main():
    for lang in OUTS:
        make(lang)


if __name__ == "__main__":
    sys.exit(main())
