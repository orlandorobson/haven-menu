from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "output" / "pdf"
SOURCE_PDF = PDF_DIR / "haven-cold-brew-42x72cm-print-outlined.pdf"
NORMALIZED_PDF = PDF_DIR / "HAVEN_COLD_BREW_PRINT_420x720MM_OUTLINED_RGB.pdf"
BLEED_PDF = PDF_DIR / "HAVEN_COLD_BREW_PRINT_426x726MM_3MM_BLEED_OUTLINED_RGB.pdf"

POINTS_PER_MM = 72 / 25.4
TRIM_WIDTH = 420 * POINTS_PER_MM
TRIM_HEIGHT = 720 * POINTS_PER_MM
BLEED = 3 * POINTS_PER_MM
MEDIA_WIDTH = TRIM_WIDTH + 2 * BLEED
MEDIA_HEIGHT = TRIM_HEIGHT + 2 * BLEED


def set_boxes(page, *, trim_box: RectangleObject, media_box: RectangleObject) -> None:
    page.mediabox = media_box
    page.cropbox = media_box
    page.bleedbox = media_box
    page.trimbox = trim_box
    page.artbox = trim_box


def write_pdf(writer: PdfWriter, destination: Path) -> None:
    writer.add_metadata(
        {
            "/Title": "Haven Cold Brew - Passion Fruit - 420 x 720 mm",
            "/Author": "Haven Cafe",
            "/Subject": "Outlined large-format signboard artwork",
            "/Keywords": "Haven, cold brew, Salalah, signboard, outlined",
        }
    )
    with destination.open("wb") as handle:
        writer.write(handle)


source_reader = PdfReader(SOURCE_PDF)
source_page = source_reader.pages[0]
source_width = float(source_page.mediabox.width)
source_height = float(source_page.mediabox.height)

# Exact trim-size master. Chrome rounds CSS millimetres through CSS pixels, so
# normalize the page to mathematically exact physical dimensions.
trim_writer = PdfWriter()
trim_page = trim_writer.add_blank_page(width=TRIM_WIDTH, height=TRIM_HEIGHT)
trim_page.merge_transformed_page(
    source_page,
    Transformation().scale(TRIM_WIDTH / source_width, TRIM_HEIGHT / source_height),
)
trim_rect = RectangleObject((0, 0, TRIM_WIDTH, TRIM_HEIGHT))
set_boxes(trim_page, trim_box=trim_rect, media_box=trim_rect)
write_pdf(trim_writer, NORMALIZED_PDF)

# Bleed master. A scaled duplicate sits underneath only to populate the 3 mm
# bleed perimeter; the exact-size artwork is then placed unchanged at +3 mm.
normalized_reader = PdfReader(NORMALIZED_PDF)
normalized_page = normalized_reader.pages[0]
bleed_writer = PdfWriter()
bleed_page = bleed_writer.add_blank_page(width=MEDIA_WIDTH, height=MEDIA_HEIGHT)

underlay_scale = max(MEDIA_WIDTH / TRIM_WIDTH, MEDIA_HEIGHT / TRIM_HEIGHT)
underlay_width = TRIM_WIDTH * underlay_scale
underlay_height = TRIM_HEIGHT * underlay_scale
underlay_x = (MEDIA_WIDTH - underlay_width) / 2
underlay_y = (MEDIA_HEIGHT - underlay_height) / 2
bleed_page.merge_transformed_page(
    normalized_page,
    Transformation().scale(underlay_scale).translate(underlay_x, underlay_y),
)
bleed_page.merge_translated_page(normalized_page, BLEED, BLEED)

media_rect = RectangleObject((0, 0, MEDIA_WIDTH, MEDIA_HEIGHT))
bleed_trim_rect = RectangleObject(
    (BLEED, BLEED, BLEED + TRIM_WIDTH, BLEED + TRIM_HEIGHT)
)
set_boxes(bleed_page, trim_box=bleed_trim_rect, media_box=media_rect)
write_pdf(bleed_writer, BLEED_PDF)

print(f"Normalized PDF: {NORMALIZED_PDF}")
print(f"Bleed PDF: {BLEED_PDF}")
print(f"Trim points: {TRIM_WIDTH:.6f} x {TRIM_HEIGHT:.6f}")
print(f"Media points: {MEDIA_WIDTH:.6f} x {MEDIA_HEIGHT:.6f}")
