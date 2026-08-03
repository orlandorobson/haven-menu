from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "haven-dhofar-ocean-culture-study-2026-08-03.md"
OUTPUT = ROOT / "output" / "pdf" / "haven-dhofar-ocean-culture-study-2026.pdf"

PAGE_W, PAGE_H = A4
NAVY = colors.HexColor("#12243A")
SEA = colors.HexColor("#2F7180")
GOLD = colors.HexColor("#B49052")
INK = colors.HexColor("#20262D")
MUTED = colors.HexColor("#65717C")
PALE = colors.HexColor("#EFF4F3")
LINE = colors.HexColor("#D8E0E2")
WHITE = colors.white


def register_fonts() -> None:
    candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial.ttf"),
        Path("/Library/Fonts/Arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ]
    bold_candidates = [
        Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
        Path("/Library/Fonts/Arial Bold.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ]
    regular = next((p for p in candidates if p.exists()), None)
    bold = next((p for p in bold_candidates if p.exists()), None)
    if regular and bold:
        pdfmetrics.registerFont(TTFont("HavenSans", str(regular)))
        pdfmetrics.registerFont(TTFont("HavenSansBold", str(bold)))
        pdfmetrics.registerFontFamily(
            "HavenSans",
            normal="HavenSans",
            bold="HavenSansBold",
            italic="HavenSans",
            boldItalic="HavenSansBold",
        )


register_fonts()
FONT = "HavenSans" if "HavenSans" in pdfmetrics.getRegisteredFontNames() else "Helvetica"
FONT_BOLD = "HavenSansBold" if "HavenSansBold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"


class ReportDocTemplate(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        if style_name not in {"H1", "H2"}:
            return
        level = 0 if style_name == "H1" else 1
        text = flowable.getPlainText()
        key = f"heading-{self.seq.nextf('heading')}"
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(text, key, level=level, closed=False)
        if level == 0:
            self.notify("TOCEntry", (level, text, self.page, key))


def draw_page(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.45)
        canvas.line(18 * mm, PAGE_H - 15 * mm, PAGE_W - 18 * mm, PAGE_H - 15 * mm)
        canvas.setFont(FONT, 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, PAGE_H - 11.6 * mm, "HAVEN · DHOFAR'S OCEAN CULTURE")
        canvas.drawRightString(PAGE_W - 18 * mm, 11.5 * mm, str(doc.page - 1))
        canvas.setStrokeColor(GOLD)
        canvas.setLineWidth(1.2)
        canvas.line(18 * mm, 16 * mm, 45 * mm, 16 * mm)
    canvas.restoreState()


def markdown_inline(text: str) -> str:
    link_pattern = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
    output = []
    position = 0
    for match in link_pattern.finditer(text):
        output.append(html.escape(text[position : match.start()]))
        label = html.escape(match.group(1))
        url = html.escape(match.group(2), quote=True)
        output.append(f'<link href="{url}" color="#2F7180"><u>{label}</u></link>')
        position = match.end()
    output.append(html.escape(text[position:]))
    rendered = "".join(output)
    rendered = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", rendered)
    rendered = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", rendered)
    rendered = rendered.replace("  ", " ")
    return rendered


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        "CoverKicker",
        fontName=FONT_BOLD,
        fontSize=9,
        leading=12,
        textColor=GOLD,
        tracking=1.6,
        spaceAfter=10,
    )
)
styles.add(
    ParagraphStyle(
        "CoverTitle",
        fontName=FONT_BOLD,
        fontSize=31,
        leading=34,
        textColor=WHITE,
        spaceAfter=16,
    )
)
styles.add(
    ParagraphStyle(
        "CoverSub",
        fontName=FONT,
        fontSize=13,
        leading=19,
        textColor=colors.HexColor("#D9E4E7"),
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        "CoverMeta",
        fontName=FONT,
        fontSize=8.5,
        leading=13,
        textColor=colors.HexColor("#BFCBD0"),
    )
)
styles.add(
    ParagraphStyle(
        "H1",
        fontName=FONT_BOLD,
        fontSize=18,
        leading=22,
        textColor=NAVY,
        spaceBefore=13,
        spaceAfter=8,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        "H2",
        fontName=FONT_BOLD,
        fontSize=12.2,
        leading=15.5,
        textColor=SEA,
        spaceBefore=10,
        spaceAfter=5,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        "BodyHaven",
        fontName=FONT,
        fontSize=9.15,
        leading=13.5,
        textColor=INK,
        spaceAfter=6.5,
        allowWidows=0,
        allowOrphans=0,
    )
)
styles.add(
    ParagraphStyle(
        "BulletHaven",
        parent=styles["BodyHaven"],
        leftIndent=11,
        firstLineIndent=-7,
        bulletIndent=1,
        spaceAfter=4,
    )
)
styles.add(
    ParagraphStyle(
        "QuoteHaven",
        parent=styles["BodyHaven"],
        fontName=FONT_BOLD,
        fontSize=11.2,
        leading=16,
        textColor=NAVY,
        leftIndent=8,
        rightIndent=8,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        "SmallHaven",
        parent=styles["BodyHaven"],
        fontSize=7.2,
        leading=9.7,
        spaceAfter=0,
    )
)
styles.add(
    ParagraphStyle(
        "TOCHead",
        fontName=FONT_BOLD,
        fontSize=22,
        leading=26,
        textColor=NAVY,
        spaceAfter=12,
    )
)


def cover_page():
    top = Table(
        [[Paragraph("HAVEN · RESEARCH & DEVELOPMENT", styles["CoverKicker"])],
         [Paragraph("Haven and Dhofar's<br/>Ocean Culture", styles["CoverTitle"])],
         [Paragraph("A strategic study for a living maritime-cultural destination at Osara, Raysut", styles["CoverSub"])]],
        colWidths=[PAGE_W - 36 * mm],
        rowHeights=[18 * mm, 60 * mm, 40 * mm],
    )
    top.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 17 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 17 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 12 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    statement = Table(
        [[Paragraph(
            "A contemporary Dhofari coastal majlis where the Indian Ocean's routes, people and stories are encountered through hospitality.",
            styles["QuoteHaven"],
        )]],
        colWidths=[PAGE_W - 54 * mm],
    )
    statement.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), PALE),
                ("BOX", (0, 0), (-1, -1), 0.6, LINE),
                ("LINEBEFORE", (0, 0), (0, -1), 4, GOLD),
                ("LEFTPADDING", (0, 0), (-1, -1), 9 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 9 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 8 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8 * mm),
            ]
        )
    )
    meta = Paragraph(
        "Prepared 3 August 2026<br/>Strategic research paper · Not a heritage designation or approved development plan",
        styles["CoverMeta"],
    )
    return [top, Spacer(1, 20 * mm), statement, Spacer(1, 35 * mm), meta, PageBreak()]


def toc_page():
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOC1",
            fontName=FONT_BOLD,
            fontSize=9.5,
            leading=14,
            leftIndent=0,
            firstLineIndent=0,
            textColor=NAVY,
            spaceBefore=3,
        ),
        ParagraphStyle(
            "TOC2",
            fontName=FONT,
            fontSize=8,
            leading=11.5,
            leftIndent=12,
            firstLineIndent=0,
            textColor=MUTED,
        ),
    ]
    return [Paragraph("Contents", styles["TOCHead"]), toc, PageBreak()]


def make_table(rows: list[list[str]]):
    count = len(rows[0])
    available = PAGE_W - 36 * mm
    if count == 3:
        widths = [0.20 * available, 0.35 * available, 0.45 * available]
    elif count == 4:
        widths = [0.19 * available, 0.28 * available, 0.27 * available, 0.26 * available]
    else:
        widths = [available / count] * count
    data = []
    for row_index, row in enumerate(rows):
        style = ParagraphStyle(
            f"Table{row_index}",
            parent=styles["SmallHaven"],
            fontName=FONT_BOLD if row_index == 0 else FONT,
            textColor=WHITE if row_index == 0 else INK,
        )
        data.append([Paragraph(markdown_inline(cell.strip()), style) for cell in row])
    table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT", splitByRow=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return [table, Spacer(1, 6)]


def parse_markdown(lines: list[str]):
    story = []
    paragraph = []
    quote = []
    table_rows = []

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            text = " ".join(item.strip() for item in paragraph)
            story.append(Paragraph(markdown_inline(text), styles["BodyHaven"]))
            paragraph = []

    def flush_quote():
        nonlocal quote
        if quote:
            text = " ".join(item.lstrip("> ").strip() for item in quote)
            box = Table([[Paragraph(markdown_inline(text), styles["QuoteHaven"])]], colWidths=[PAGE_W - 54 * mm])
            box.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), PALE),
                        ("LINEBEFORE", (0, 0), (0, -1), 3, GOLD),
                        ("LEFTPADDING", (0, 0), (-1, -1), 9),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                        ("TOPPADDING", (0, 0), (-1, -1), 8),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                    ]
                )
            )
            story.extend([box, Spacer(1, 7)])
            quote = []

    def flush_table():
        nonlocal table_rows
        if table_rows:
            cleaned = [row for i, row in enumerate(table_rows) if i != 1]
            story.extend(make_table(cleaned))
            table_rows = []

    for line in lines:
        stripped = line.rstrip()
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph()
            flush_quote()
            table_rows.append([cell for cell in stripped.strip("|").split("|")])
            continue
        flush_table()
        if not stripped:
            flush_paragraph()
            flush_quote()
            continue
        if stripped.startswith("### "):
            flush_paragraph()
            flush_quote()
            story.append(Paragraph(markdown_inline(stripped[4:]), styles["H2"]))
        elif stripped.startswith("## "):
            flush_paragraph()
            flush_quote()
            story.extend([Spacer(1, 3), Paragraph(markdown_inline(stripped[3:]), styles["H1"])])
        elif stripped.startswith(">"):
            flush_paragraph()
            quote.append(stripped)
        elif re.match(r"^\d+\. ", stripped):
            flush_paragraph()
            number, text = stripped.split(". ", 1)
            story.append(Paragraph(markdown_inline(text), styles["BulletHaven"], bulletText=f"{number}."))
        elif stripped.startswith("- "):
            flush_paragraph()
            story.append(Paragraph(markdown_inline(stripped[2:]), styles["BulletHaven"], bulletText="•"))
        elif stripped.startswith("**Prepared") or stripped.startswith("**Status"):
            continue
        else:
            paragraph.append(stripped)
    flush_paragraph()
    flush_quote()
    flush_table()
    return story


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    text = SOURCE.read_text(encoding="utf-8")
    lines = text.splitlines()
    body_start = next(i for i, line in enumerate(lines) if line.startswith("## Executive judgement"))

    frame = Frame(
        18 * mm,
        18 * mm,
        PAGE_W - 36 * mm,
        PAGE_H - 36 * mm,
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    template = PageTemplate(id="main", frames=[frame], onPage=draw_page)
    doc = ReportDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        pageTemplates=[template],
        title="Haven and Dhofar's Ocean Culture",
        author="Haven",
        subject="A strategic study for a living maritime-cultural destination at Osara, Raysut",
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )
    story = cover_page() + toc_page() + parse_markdown(lines[body_start:])
    doc.multiBuild(story)
    print(OUTPUT)


if __name__ == "__main__":
    build()
