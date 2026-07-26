from __future__ import annotations

import base64
import html
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, "/private/tmp/haven-vector-deps")

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTCollection, TTFont


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets" / "signboards"
FONT_DIR = ASSET_DIR / "fonts"
EDITABLE_SVG = ASSET_DIR / "haven-cold-brew-vector-editable.svg"
OUTLINED_SVG = ASSET_DIR / "haven-cold-brew-vector-outlined.svg"
PRINT_HTML = ROOT / "tmp" / "pdfs" / "haven-cold-brew-print-source.html"
PHOTO_NAME = "haven-cold-brew-photo-master-v3-upscaled-240ppi.png"
CANVAS_WIDTH = 420.0


def clean_number(value: float) -> str:
    return f"{value:.4f}".rstrip("0").rstrip(".")


def font_name(font: TTFont, name_id: int) -> str:
    record = font["name"].getName(name_id, 3, 1)
    if record is None:
        record = font["name"].getName(name_id, 1, 0)
    return record.toUnicode() if record else ""


@dataclass
class FontSource:
    path: Path
    font_number: int = 0
    weight: float | None = None

    def __post_init__(self) -> None:
        self.data = self.path.read_bytes()
        if self.path.suffix.lower() in {".ttc", ".otc"}:
            collection = TTCollection(self.path)
            self.ttfont = collection.fonts[self.font_number]
        else:
            self.ttfont = TTFont(self.path)
        self.upem = self.ttfont["head"].unitsPerEm
        self.glyph_order = self.ttfont.getGlyphOrder()
        location = {"wght": self.weight} if self.weight is not None and "fvar" in self.ttfont else None
        self.glyph_set = self.ttfont.getGlyphSet(location=location)
        self.hb_face = hb.Face(self.data, self.font_number)
        self.hb_font = hb.Font(self.hb_face)
        self.hb_font.scale = (self.upem, self.upem)
        if self.weight is not None:
            self.hb_font.set_variations({"wght": self.weight})

    @property
    def postscript_name(self) -> str:
        return font_name(self.ttfont, 6)


def ttc_face(path: Path, postscript_name: str) -> int:
    collection = TTCollection(path)
    for index, font in enumerate(collection.fonts):
        if font_name(font, 6) == postscript_name:
            return index
    choices = ", ".join(font_name(font, 6) for font in collection.fonts)
    raise RuntimeError(f"{postscript_name} not found in {path}; choices: {choices}")


@dataclass
class ShapedLine:
    path_data: str
    width: float


def shape_to_path(
    text: str,
    source: FontSource,
    size_mm: float,
    baseline_mm: float,
    *,
    tracking_mm: float = 0,
    center_x_mm: float = CANVAS_WIDTH / 2,
    offset_x_mm: float = 0,
    start_x_mm: float | None = None,
    right_to_left: bool = False,
) -> ShapedLine:
    buffer = hb.Buffer()
    buffer.add_str(text)
    if right_to_left:
        buffer.direction = "rtl"
        buffer.script = "arab"
        buffer.language = "ar"
    else:
        buffer.guess_segment_properties()
    hb.shape(source.hb_font, buffer, {"kern": True, "liga": True})
    infos = buffer.glyph_infos
    positions = buffer.glyph_positions
    scale = size_mm / source.upem

    total_advance_units = sum(position.x_advance for position in positions)
    total_width_mm = total_advance_units * scale
    if positions:
        total_width_mm += tracking_mm * (len(positions) - 1)
    start_x = (
        start_x_mm
        if start_x_mm is not None
        else center_x_mm - total_width_mm / 2 + offset_x_mm
    )

    pen = SVGPathPen(source.glyph_set)
    cursor_units = 0
    tracking_units = tracking_mm / scale if scale else 0
    for index, (info, position) in enumerate(zip(infos, positions)):
        glyph_name = source.glyph_order[info.codepoint]
        x_mm = start_x + (cursor_units + position.x_offset) * scale
        y_mm = baseline_mm - position.y_offset * scale
        transform_pen = TransformPen(
            pen,
            (scale, 0, 0, -scale, x_mm, y_mm),
        )
        source.glyph_set[glyph_name].draw(transform_pen)
        cursor_units += position.x_advance
        if index < len(positions) - 1:
            cursor_units += tracking_units

    return ShapedLine(pen.getCommands(), total_width_mm)


cormorant_path = FONT_DIR / "CormorantGaramond-wght.ttf"
noto_path = FONT_DIR / "NotoNaskhArabic-wght.ttf"
avenir_path = Path("/System/Library/Fonts/Avenir Next.ttc")

cormorant_600 = FontSource(cormorant_path, weight=600)
noto_600 = FontSource(noto_path, weight=600)
noto_700 = FontSource(noto_path, weight=700)
avenir_demi = FontSource(
    avenir_path,
    font_number=ttc_face(avenir_path, "AvenirNext-DemiBold"),
)
avenir_bold = FontSource(
    avenir_path,
    font_number=ttc_face(avenir_path, "AvenirNext-Bold"),
)

haven = shape_to_path(
    "HAVEN",
    cormorant_600,
    42,
    50.1,
    tracking_mm=8,
    offset_x_mm=4,
)
product = shape_to_path(
    "COLD BREW",
    cormorant_600,
    44,
    92.8,
    tracking_mm=5.5,
    offset_x_mm=2.75,
)
flavour_en = shape_to_path(
    "PASSION FRUIT",
    avenir_demi,
    11.2,
    122.55,
    tracking_mm=4,
    offset_x_mm=1.6,
)
arabic_name = shape_to_path(
    "هيڤن كولد برو",
    noto_600,
    28,
    170.7,
    right_to_left=True,
)
flavour_ar = shape_to_path(
    "بـــاشـــن فـــروت",
    noto_700,
    12.5,
    200.25,
    right_to_left=True,
)
price = shape_to_path(
    "2.4",
    avenir_demi,
    13,
    696.15,
    tracking_mm=0.3,
    start_x_mm=357.12,
)
price_unit = shape_to_path(
    "OMR",
    avenir_bold,
    5,
    696.15,
    tracking_mm=0.8,
    start_x_mm=380.26,
)

DEFINITIONS = """
<defs>
  <linearGradient id="topShade" x1="0" y1="0" x2="0" y2="281" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#020e18" stop-opacity=".25"/>
    <stop offset=".59" stop-color="#020e18" stop-opacity=".10"/>
    <stop offset="1" stop-color="#020e18" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="champagne" x1="55" y1="0" x2="365" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#d6bc86"/>
    <stop offset=".27" stop-color="#f3e6c8"/>
    <stop offset=".53" stop-color="#e6d2a5"/>
    <stop offset=".76" stop-color="#f1e2bf"/>
    <stop offset="1" stop-color="#d6bc86"/>
  </linearGradient>
  <linearGradient id="champagneArabic" x1="138" y1="0" x2="282" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#d6bc86"/>
    <stop offset=".33" stop-color="#f3e6c8"/>
    <stop offset=".62" stop-color="#e5cf9e"/>
    <stop offset="1" stop-color="#f0dfb8"/>
  </linearGradient>
  <linearGradient id="panelFill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f6f0e5" stop-opacity=".27"/>
    <stop offset="1" stop-color="#ecdcbc" stop-opacity=".24"/>
  </linearGradient>
  <linearGradient id="metalEdge" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#a9824b"/>
    <stop offset=".32" stop-color="#f2dfb6"/>
    <stop offset=".62" stop-color="#c09b61"/>
    <stop offset=".82" stop-color="#ead2a0"/>
    <stop offset="1" stop-color="#9e7743"/>
  </linearGradient>
  <linearGradient id="oxblood" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#702029"/>
    <stop offset=".37" stop-color="#a94b49"/>
    <stop offset=".68" stop-color="#7f2028"/>
    <stop offset=".84" stop-color="#b06055"/>
    <stop offset="1" stop-color="#702029"/>
  </linearGradient>
  <linearGradient id="oxbloodArabic" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#702029"/>
    <stop offset=".39" stop-color="#ad514d"/>
    <stop offset=".70" stop-color="#7f2028"/>
    <stop offset="1" stop-color="#a74645"/>
  </linearGradient>
</defs>
"""

PANELS = """
<g id="flavour-panels">
  <rect x="131.68" y="108.39" width="156.64" height="18.82" rx="9.41" fill="url(#metalEdge)"/>
  <rect x="132.08" y="108.79" width="155.84" height="18.02" rx="9.01" fill="url(#panelFill)"/>
  <rect x="130.7" y="116.47" width="2.2" height="2.2" transform="rotate(45 131.8 117.57)" fill="#061f33" fill-opacity=".7" stroke="#e1c996" stroke-opacity=".74" stroke-width=".3"/>
  <rect x="287.1" y="116.47" width="2.2" height="2.2" transform="rotate(45 288.2 117.57)" fill="#061f33" fill-opacity=".7" stroke="#e1c996" stroke-opacity=".74" stroke-width=".3"/>
  <rect x="163.94" y="186.21" width="92.12" height="20.13" rx="10.06" fill="url(#metalEdge)"/>
  <rect x="164.34" y="186.61" width="91.32" height="19.33" rx="9.66" fill="url(#panelFill)"/>
  <rect x="162.96" y="195.18" width="2.2" height="2.2" transform="rotate(45 164.06 196.28)" fill="#061f33" fill-opacity=".7" stroke="#e1c996" stroke-opacity=".74" stroke-width=".3"/>
  <rect x="254.94" y="195.18" width="2.2" height="2.2" transform="rotate(45 256.04 196.28)" fill="#061f33" fill-opacity=".7" stroke="#e1c996" stroke-opacity=".74" stroke-width=".3"/>
</g>
"""

OUTLINED_TYPOGRAPHY = f"""
<g id="outlined-typography">
  <path id="haven-title" d="{haven.path_data}" fill="url(#champagne)"/>
  <path id="product-title" d="{product.path_data}" fill="url(#champagne)"/>
  <path id="passion-fruit-en" d="{flavour_en.path_data}" fill="url(#oxblood)"/>
  <path id="arabic-name-shadow" d="{arabic_name.path_data}" transform="translate(0 .7)" fill="#010a12" fill-opacity=".18"/>
  <path id="arabic-name" d="{arabic_name.path_data}" fill="url(#champagneArabic)"/>
  <path id="passion-fruit-ar" d="{flavour_ar.path_data}" fill="url(#oxbloodArabic)"/>
  <path id="price-shadow" d="{price.path_data}" transform="translate(0 1)" fill="#010a12" fill-opacity=".40"/>
  <path id="price" d="{price.path_data}" fill="#e9d7ae"/>
  <path id="price-unit" d="{price_unit.path_data}" fill="#c9ad78"/>
</g>
"""

EDITABLE_TYPOGRAPHY = """
<style>
  @font-face {
    font-family: "Cormorant Garamond Local";
    src: url("fonts/CormorantGaramond-wght.ttf") format("truetype");
    font-weight: 300 700;
  }
  @font-face {
    font-family: "Noto Naskh Arabic Local";
    src: url("fonts/NotoNaskhArabic-wght.ttf") format("truetype");
    font-weight: 400 700;
  }
</style>
<g id="editable-typography" text-anchor="middle">
  <text x="214" y="50.1" font-family="Cormorant Garamond Local" font-size="42" font-weight="600" letter-spacing="8" fill="url(#champagne)">HAVEN</text>
  <text x="212.75" y="92.8" font-family="Cormorant Garamond Local" font-size="44" font-weight="600" letter-spacing="5.5" fill="url(#champagne)">COLD BREW</text>
  <text x="211.6" y="122.55" font-family="Avenir Next" font-size="11.2" font-weight="600" letter-spacing="4" fill="url(#oxblood)">PASSION FRUIT</text>
  <text x="210" y="170.7" direction="rtl" font-family="Noto Naskh Arabic Local" font-size="28" font-weight="600" fill="url(#champagneArabic)">هيڤن كولد برو</text>
  <text x="210" y="200.25" direction="rtl" font-family="Noto Naskh Arabic Local" font-size="12.5" font-weight="700" fill="url(#oxbloodArabic)">بـــاشـــن فـــروت</text>
  <text x="357.12" y="696.15" text-anchor="start" font-family="Avenir Next" font-size="13" font-weight="600" letter-spacing=".3" fill="#e9d7ae">2.4</text>
  <text x="380.26" y="696.15" text-anchor="start" font-family="Avenir Next" font-size="5" font-weight="700" letter-spacing=".8" fill="#c9ad78">OMR</text>
</g>
"""


def svg_document(typography: str, *, embed_photo: bool = False) -> str:
    photo_href = PHOTO_NAME
    if embed_photo:
        photo_bytes = (ASSET_DIR / PHOTO_NAME).read_bytes()
        photo_href = "data:image/png;base64," + base64.b64encode(photo_bytes).decode("ascii")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="420mm"
     height="720mm"
     viewBox="0 0 420 720">
  <title>Haven Cold Brew - Passion Fruit pavement sign</title>
  <desc>Full-size 42 by 72 centimetre Haven signboard artwork.</desc>
  {DEFINITIONS}
  <image id="photograph" href="{photo_href}" x="0" y="0" width="420" height="720" preserveAspectRatio="none"/>
  <rect id="top-tone-control" x="0" y="0" width="420" height="281" fill="url(#topShade)"/>
  {PANELS}
  {typography}
</svg>
"""


EDITABLE_SVG.write_text(svg_document(EDITABLE_TYPOGRAPHY), encoding="utf-8")
OUTLINED_SVG.write_text(
    svg_document(OUTLINED_TYPOGRAPHY, embed_photo=True),
    encoding="utf-8",
)

PRINT_HTML.parent.mkdir(parents=True, exist_ok=True)
outlined_uri = OUTLINED_SVG.as_uri()
PRINT_HTML.write_text(
    f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    @page {{ size: 420mm 720mm; margin: 0; }}
    html, body {{ width: 420mm; height: 720mm; margin: 0; padding: 0; overflow: hidden; }}
    img {{ display: block; width: 420mm; height: 720mm; }}
  </style>
</head>
<body><img src="{html.escape(outlined_uri)}" alt=""></body>
</html>
""",
    encoding="utf-8",
)

print(f"Cormorant: {cormorant_600.postscript_name}")
print(f"Noto Naskh: {noto_600.postscript_name}")
print(f"Avenir: {avenir_demi.postscript_name}")
print(f"HAVEN width: {clean_number(haven.width)} mm")
print(f"COLD BREW width: {clean_number(product.width)} mm")
print(f"Editable SVG: {EDITABLE_SVG}")
print(f"Outlined SVG: {OUTLINED_SVG}")
print(f"Print source: {PRINT_HTML}")
