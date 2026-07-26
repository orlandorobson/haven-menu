from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "output" / "print" / "HAVEN_COLD_BREW_PRINTER_PACK"
OUTPUT = PACK / "00_HAVEN_COLD_BREW_PRINT_INSTRUCTIONS.pdf"
PREVIEW = PACK / "HAVEN_COLD_BREW_REFERENCE_ONLY_DO_NOT_PRINT.jpg"


def wrapped_lines(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


page_width, page_height = A4
pdf = canvas.Canvas(str(OUTPUT), pagesize=A4)
pdf.setTitle("Haven Cold Brew - Printer Instructions")
pdf.setAuthor("Haven Cafe")

navy = HexColor("#061F33")
gold = HexColor("#D6BC86")
red = HexColor("#7F2028")
grey = HexColor("#4B5560")

pdf.setFillColor(navy)
pdf.rect(0, page_height - 76, page_width, 76, stroke=0, fill=1)
pdf.setFillColor(gold)
pdf.setFont("Helvetica-Bold", 20)
pdf.drawString(34, page_height - 43, "HAVEN COLD BREW - PRINTER HANDOFF")
pdf.setFont("Helvetica", 9)
pdf.drawString(34, page_height - 59, "Finished size 420 x 720 mm | Prepared 24 July 2026")

preview_width = 184
preview_height = preview_width * 720 / 420
preview_y = page_height - 106 - preview_height
pdf.drawImage(
    str(PREVIEW),
    34,
    preview_y,
    width=preview_width,
    height=preview_height,
    preserveAspectRatio=True,
    mask="auto",
)
pdf.setFillColor(red)
pdf.setFont("Helvetica-Bold", 8)
pdf.drawCentredString(
    34 + preview_width / 2,
    preview_y - 13,
    "REFERENCE IMAGE ONLY - DO NOT PRINT FROM THIS JPEG",
)

x = 244
y = page_height - 104
column_width = page_width - x - 34


def heading(text: str) -> None:
    global y
    pdf.setFillColor(navy)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(x, y, text)
    y -= 14


def paragraph(text: str, *, bullet: bool = False) -> None:
    global y
    pdf.setFillColor(grey)
    pdf.setFont("Helvetica", 8.5)
    indent = 10 if bullet else 0
    if bullet:
        pdf.setFillColor(red)
        pdf.circle(x + 2.5, y + 2.5, 1.5, stroke=0, fill=1)
        pdf.setFillColor(grey)
    for line in wrapped_lines(text, "Helvetica", 8.5, column_width - indent):
        pdf.drawString(x + indent, y, line)
        y -= 11
    y -= 3


heading("PRIMARY PRODUCTION FILE")
paragraph("HAVEN_COLD_BREW_PRINT_426x726MM_3MM_BLEED_OUTLINED_RGB.pdf")
paragraph("Trim to the embedded 420 x 720 mm TrimBox.", bullet=True)
paragraph("Print at 100%. Do not Fit, Shrink, Enlarge, Crop to Artwork, or Auto Rotate.", bullet=True)
paragraph("Full bleed with no white border.", bullet=True)

heading("ALTERNATIVES")
paragraph(
    "Use the exact-size 420 x 720 mm PDF only when the workflow does not require bleed.",
    bullet=True,
)
paragraph(
    "Use the 240 ppi sRGB TIFF only if the RIP cannot process the outlined PDF.",
    bullet=True,
)

heading("COLOUR")
paragraph(
    "Use the RIP's machine, ink, and substrate profile. Do not assign generic CMYK.",
    bullet=True,
)
paragraph(
    "Disable automatic brightness, contrast, sharpening, saturation, and image correction.",
    bullet=True,
)
paragraph(
    "Metallic appearance is simulated. No foil, metallic ink, or spot UV unless separately ordered.",
    bullet=True,
)

heading("KHAREEF / OUTDOOR FINISH")
paragraph(
    "Use a waterproof outdoor print system and matte or low-glare UV-resistant laminate.",
    bullet=True,
)
paragraph(
    "Seal exposed edges against moisture and mount without stretching the artwork.",
    bullet=True,
)

heading("PREPRESS FACTS")
paragraph("All English and Arabic typography is outlined; there are no live fonts.", bullet=True)
paragraph("The photograph is 3969 x 6803 px at 240 ppi.", bullet=True)
paragraph("Price: 2.4 OMR. Confirm print quantity with Haven.", bullet=True)

pdf.setFillColor(navy)
pdf.rect(0, 0, page_width, 30, stroke=0, fill=1)
pdf.setFillColor(gold)
pdf.setFont("Helvetica-Bold", 8)
pdf.drawCentredString(
    page_width / 2,
    11,
    "PRINT PRODUCTION ARTWORK FROM THE SUPPLIED PDF - NOT FROM THIS INSTRUCTION SHEET",
)

pdf.showPage()
pdf.save()
print(OUTPUT)
