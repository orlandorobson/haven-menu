from __future__ import annotations

from pathlib import Path
from math import ceil

from reportlab.graphics.charts.barcharts import HorizontalBarChart, VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    Image,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "pdf"
TMP_DIR = ROOT / "tmp" / "pdfs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
TMP_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "haven-salalah-evergreen-cafe-market-study-2026.pdf"
LOGO = ROOT / "assets" / "img" / "haven-logo-original.jpg"

PAGE_W, PAGE_H = A4
MARGIN_X = 17 * mm
TOP = 18 * mm
BOTTOM = 17 * mm

NAVY = colors.HexColor("#09283A")
NAVY_2 = colors.HexColor("#17485C")
TEAL = colors.HexColor("#1E6F78")
SEA = colors.HexColor("#66A9A8")
FOG = colors.HexColor("#DDEAE7")
SAND = colors.HexColor("#E9DFC9")
SAND_2 = colors.HexColor("#F7F2E8")
CORAL = colors.HexColor("#B34A3C")
GOLD = colors.HexColor("#C9953A")
INK = colors.HexColor("#15242C")
MUTED = colors.HexColor("#66757D")
LIGHT = colors.HexColor("#EEF2F1")
WHITE = colors.white
GRID = colors.HexColor("#C8D4D4")
GREEN = colors.HexColor("#2E7D62")
AMBER = colors.HexColor("#D08B2E")
RED = colors.HexColor("#A63C36")

FONT_PATH = "/Library/Fonts/Arial Unicode.ttf"
pdfmetrics.registerFont(TTFont("HavenSans", FONT_PATH))
FONT = "HavenSans"


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text, style)


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        "TitleCover",
        fontName=FONT,
        fontSize=27,
        leading=31,
        textColor=WHITE,
        alignment=TA_LEFT,
        spaceAfter=5 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "CoverSub",
        fontName=FONT,
        fontSize=11.5,
        leading=16,
        textColor=FOG,
        spaceAfter=4 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "H1x",
        fontName=FONT,
        fontSize=19,
        leading=23,
        textColor=NAVY,
        spaceBefore=1 * mm,
        spaceAfter=5 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "H2x",
        fontName=FONT,
        fontSize=12.3,
        leading=15,
        textColor=NAVY_2,
        spaceBefore=4 * mm,
        spaceAfter=2.2 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "H3x",
        fontName=FONT,
        fontSize=9.8,
        leading=12.3,
        textColor=TEAL,
        spaceBefore=2.4 * mm,
        spaceAfter=1.3 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "Bodyx",
        fontName=FONT,
        fontSize=8.55,
        leading=12.4,
        textColor=INK,
        spaceAfter=2.3 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "Smallx",
        fontName=FONT,
        fontSize=7.3,
        leading=10.2,
        textColor=MUTED,
        spaceAfter=1.6 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "Tinyx",
        fontName=FONT,
        fontSize=6.4,
        leading=8.4,
        textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        "Bulletx",
        fontName=FONT,
        fontSize=8.3,
        leading=11.7,
        leftIndent=4.5 * mm,
        firstLineIndent=-2.7 * mm,
        bulletIndent=1.2 * mm,
        textColor=INK,
        spaceAfter=1.5 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "Calloutx",
        fontName=FONT,
        fontSize=10.2,
        leading=14.2,
        textColor=NAVY,
        leftIndent=4 * mm,
        rightIndent=4 * mm,
        spaceBefore=2 * mm,
        spaceAfter=2 * mm,
    )
)
styles.add(
    ParagraphStyle(
        "TableHead",
        fontName=FONT,
        fontSize=6.9,
        leading=8.6,
        textColor=WHITE,
        alignment=TA_LEFT,
    )
)
styles.add(
    ParagraphStyle(
        "TableBody",
        fontName=FONT,
        fontSize=6.6,
        leading=8.5,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        "TableSmall",
        fontName=FONT,
        fontSize=6.0,
        leading=7.6,
        textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        "KPI",
        fontName=FONT,
        fontSize=20,
        leading=22,
        textColor=NAVY,
        alignment=TA_CENTER,
    )
)
styles.add(
    ParagraphStyle(
        "KPILabel",
        fontName=FONT,
        fontSize=6.8,
        leading=9,
        textColor=MUTED,
        alignment=TA_CENTER,
    )
)


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(FONT, 6.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(MARGIN_X, 8.5 * mm, "HAVEN | SALALAH EVERGREEN CAFE MARKET STUDY")
    canvas.drawRightString(PAGE_W - MARGIN_X, 8.5 * mm, f"{doc.page}")
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.35)
    canvas.line(MARGIN_X, 11.5 * mm, PAGE_W - MARGIN_X, 11.5 * mm)
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(TEAL)
    canvas.circle(PAGE_W * 0.84, PAGE_H * 0.88, 42 * mm, fill=1, stroke=0)
    canvas.setFillColor(NAVY_2)
    canvas.circle(PAGE_W * 0.88, PAGE_H * 0.20, 54 * mm, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 0, 9 * mm, PAGE_H, fill=1, stroke=0)
    canvas.restoreState()


def make_doc():
    doc = BaseDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=MARGIN_X,
        rightMargin=MARGIN_X,
        topMargin=TOP,
        bottomMargin=BOTTOM,
        title="Haven Salalah Evergreen Cafe Market Study 2026",
        author="OpenAI for Haven",
        subject="Market trends, competitor intelligence, customer perception and market-entry strategy",
    )
    cover_frame = Frame(
        21 * mm,
        23 * mm,
        PAGE_W - 42 * mm,
        PAGE_H - 46 * mm,
        id="cover_frame",
        showBoundary=0,
    )
    body_frame = Frame(
        MARGIN_X,
        BOTTOM,
        PAGE_W - 2 * MARGIN_X,
        PAGE_H - TOP - BOTTOM,
        id="body_frame",
        showBoundary=0,
    )
    doc.addPageTemplates(
        [
            PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page),
            PageTemplate(id="body", frames=[body_frame], onPage=header_footer),
        ]
    )
    return doc


def section_title(num: str, title: str, subtitle: str | None = None):
    items = [
        p(f"<font color='#B34A3C'>{num}</font>  {title}", styles["H1x"]),
        HRFlowable(width="100%", thickness=0.8, color=SEA, spaceAfter=3 * mm),
    ]
    if subtitle:
        items.append(p(subtitle, styles["Smallx"]))
    return items


def bullet(text: str):
    return p(f"<bullet>-</bullet>{text}", styles["Bulletx"])


def shaded_callout(text: str, color=SAND_2):
    t = Table([[p(text, styles["Calloutx"])]], colWidths=[PAGE_W - 2 * MARGIN_X])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), color),
                ("BOX", (0, 0), (-1, -1), 0.7, SEA),
                ("LEFTPADDING", (0, 0), (-1, -1), 4 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4 * mm),
                ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
            ]
        )
    )
    return t


def table(data, widths, header=True, small=False, row_bgs=True):
    styled = []
    for r, row in enumerate(data):
        style = styles["TableHead"] if r == 0 and header else (styles["TableSmall"] if small else styles["TableBody"])
        styled.append([p(str(x), style) if not isinstance(x, Paragraph) else x for x in row])
    t = Table(styled, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    cmds = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.1 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.1 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 1.7 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.7 * mm),
    ]
    if header:
        cmds.append(("BACKGROUND", (0, 0), (-1, 0), NAVY_2))
    if row_bgs:
        start = 1 if header else 0
        for r in range(start, len(data)):
            if (r - start) % 2 == 1:
                cmds.append(("BACKGROUND", (0, r), (-1, r), LIGHT))
    t.setStyle(TableStyle(cmds))
    return t


def kpi_row(items):
    cells = []
    for value, label in items:
        cells.append([p(value, styles["KPI"]), p(label, styles["KPILabel"])])
    nested = []
    for value, label in items:
        nt = Table([[p(value, styles["KPI"])], [p(label, styles["KPILabel"])]], colWidths=[(PAGE_W - 2 * MARGIN_X) / len(items)])
        nt.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), SAND_2),
                    ("BOX", (0, 0), (-1, -1), 0.5, GRID),
                    ("TOPPADDING", (0, 0), (-1, 0), 3 * mm),
                    ("BOTTOMPADDING", (0, 1), (-1, 1), 3 * mm),
                ]
            )
        )
        nested.append(nt)
    out = Table([nested], colWidths=[(PAGE_W - 2 * MARGIN_X) / len(items)] * len(items))
    out.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 1.2 * mm)]))
    return out


def season_chart():
    d = Drawing(470, 170)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    resident = [68, 68, 55, 60, 63, 72, 82, 88, 78, 70, 72, 70]
    tourist = [42, 38, 28, 20, 16, 45, 95, 100, 70, 40, 45, 48]
    chart = VerticalBarChart()
    chart.x = 42
    chart.y = 32
    chart.height = 112
    chart.width = 395
    chart.data = [resident, tourist]
    chart.categoryAxis.categoryNames = months
    chart.categoryAxis.labels.fontName = FONT
    chart.categoryAxis.labels.fontSize = 6.5
    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = 110
    chart.valueAxis.valueStep = 25
    chart.valueAxis.labels.fontName = FONT
    chart.valueAxis.labels.fontSize = 6
    chart.bars[0].fillColor = TEAL
    chart.bars[1].fillColor = GOLD
    chart.barWidth = 6
    chart.groupSpacing = 5
    d.add(chart)
    d.add(String(42, 156, "ILLUSTRATIVE DEMAND SHAPE - NOT SALES DATA", fontName=FONT, fontSize=7.2, fillColor=MUTED))
    d.add(Rect(310, 155, 8, 6, fillColor=TEAL, strokeColor=None))
    d.add(String(322, 154, "resident baseline", fontName=FONT, fontSize=6.5, fillColor=MUTED))
    d.add(Rect(390, 155, 8, 6, fillColor=GOLD, strokeColor=None))
    d.add(String(402, 154, "tourism", fontName=FONT, fontSize=6.5, fillColor=MUTED))
    return d


def competitor_map():
    d = Drawing(470, 250)
    x0, y0, w, h = 44, 36, 380, 175
    d.add(Rect(x0, y0, w, h, fillColor=colors.white, strokeColor=GRID, strokeWidth=0.7))
    d.add(Line(x0 + w / 2, y0, x0 + w / 2, y0 + h, strokeColor=GRID))
    d.add(Line(x0, y0 + h / 2, x0 + w, y0 + h / 2, strokeColor=GRID))
    d.add(String(x0, y0 + h + 16, "PLACE / EXPERIENCE LED", fontName=FONT, fontSize=7.5, fillColor=MUTED))
    d.add(String(x0 + w - 75, y0 + h + 16, "ROUTINE LED", fontName=FONT, fontSize=7.5, fillColor=MUTED))
    d.add(String(8, y0 + h - 4, "PREMIUM", fontName=FONT, fontSize=7, fillColor=MUTED))
    d.add(String(14, y0 + 3, "VALUE", fontName=FONT, fontSize=7, fillColor=MUTED))
    points = {
        "Hills": (104, 182, CORAL),
        "Lantana": (132, 153, CORAL),
        "Caika*": (176, 174, GOLD),
        "Caribou": (316, 146, NAVY_2),
        "Bon Lab": (296, 183, TEAL),
        "Hurof": (342, 178, TEAL),
        "2OZ": (274, 159, TEAL),
        "55 Coffee": (365, 92, NAVY),
        "Toqa": (347, 72, NAVY),
        "Pure": (311, 91, NAVY_2),
        "Haven now": (150, 129, GOLD),
        "Haven target": (302, 129, GREEN),
    }
    for label, (x, y, c) in points.items():
        d.add(Rect(x - 3, y - 3, 6, 6, fillColor=c, strokeColor=None))
        d.add(String(x + 6, y - 3, label, fontName=FONT, fontSize=7, fillColor=INK))
    d.add(String(44, 14, "*Caika evidence is sparse; position is provisional.", fontName=FONT, fontSize=6.5, fillColor=MUTED))
    return d


def funnel_chart():
    d = Drawing(470, 200)
    stages = [
        ("REACH", 390, FOG, "views"),
        ("QUALIFIED INTEREST", 325, colors.HexColor("#BFD8D4"), "saves, shares, profile visits"),
        ("INTENT", 255, SEA, "map taps, menu opens, messages"),
        ("ARRIVAL", 190, TEAL, "source-coded transactions"),
        ("REPEAT", 125, NAVY, "30-day return, direct CRM"),
    ]
    y = 165
    for label, width, color, measure in stages:
        x = 235 - width / 2
        d.add(Rect(x, y, width, 24, fillColor=color, strokeColor=WHITE, strokeWidth=1))
        text_color = WHITE if color in (TEAL, NAVY) else NAVY
        d.add(String(235, y + 13, label, fontName=FONT, fontSize=7.2, fillColor=text_color, textAnchor="middle"))
        d.add(String(452, y + 13, measure, fontName=FONT, fontSize=6.5, fillColor=MUTED, textAnchor="end"))
        y -= 31
    d.add(String(40, 7, "Social content is a conversion input. The transaction and repeat visit are the commercial outputs.", fontName=FONT, fontSize=7.2, fillColor=MUTED))
    return d


def score_chart():
    labels = ["Destination dessert", "Low-price drive-through", "Pure coffee lab", "Cake gifting studio", "Dhofari coastal dayhouse"]
    scores = [45, 51, 61, 68, 86]
    d = Drawing(470, 190)
    c = HorizontalBarChart()
    c.x = 145
    c.y = 30
    c.height = 130
    c.width = 270
    c.data = [scores]
    c.categoryAxis.categoryNames = labels
    c.categoryAxis.labels.fontName = FONT
    c.categoryAxis.labels.fontSize = 6.5
    c.valueAxis.valueMin = 0
    c.valueAxis.valueMax = 100
    c.valueAxis.valueStep = 20
    c.valueAxis.labels.fontName = FONT
    c.valueAxis.labels.fontSize = 6
    c.bars[0].fillColor = TEAL
    c.barWidth = 11
    d.add(c)
    d.add(String(42, 173, "WEIGHTED NICHE ATTRACTIVENESS / 100", fontName=FONT, fontSize=7.5, fillColor=MUTED))
    return d


def break_even_chart():
    fixed = [6000, 8000, 10000]
    daily = [ceil(x / 2.072 / 30) for x in fixed]
    d = Drawing(470, 185)
    c = VerticalBarChart()
    c.x = 78
    c.y = 30
    c.height = 120
    c.width = 330
    c.data = [daily]
    c.categoryAxis.categoryNames = ["OMR 6k fixed", "OMR 8k fixed", "OMR 10k fixed"]
    c.categoryAxis.labels.fontName = FONT
    c.categoryAxis.labels.fontSize = 7
    c.valueAxis.valueMin = 0
    c.valueAxis.valueMax = 180
    c.valueAxis.valueStep = 30
    c.valueAxis.labels.fontName = FONT
    c.valueAxis.labels.fontSize = 6
    c.bars[0].fillColor = GOLD
    c.barWidth = 30
    d.add(c)
    for i, val in enumerate(daily):
        d.add(String(133 + i * 110, 34 + val * (120 / 180), str(val), fontName=FONT, fontSize=8, fillColor=NAVY, textAnchor="middle"))
    d.add(String(42, 168, "ILLUSTRATIVE BREAK-EVEN ORDERS PER DAY", fontName=FONT, fontSize=7.5, fillColor=MUTED))
    return d


SOURCES = [
    ("Oman Ministry of Heritage and Tourism - Khareef 2024 visitor results", "https://mht.gov.om/media-center/news/khareef-season-in-dhofar-attracted-1-048-000-visitors-in-2024/"),
    ("Times of Oman / NCSI - 827,115 Khareef visitors through 15 Aug 2025", "https://timesofoman.com/article/162045-khareef-dhofar-visitors-exceed-800000-up-by-over-2-from-last-year"),
    ("Oman Air - record 2025 Khareef passenger volume", "https://services.omanair.com/fr/en/PressRelease/oman-air-wraps-up-khareef-season-with-record-breaking-passenger-numbers"),
    ("AACO citing NCSI - Oman airport traffic 2025", "https://www.aaco.org/media-center/news/industry/passenger-traffic-at-oman-airports-rises-2-8-to-14-9-million-in-2025"),
    ("Oman News Agency - Salalah Airport passenger growth to May 2025", "https://www.omannews.gov.om/topics/en/80/show/123307/"),
    ("Visit Dhofar Seasons - year-round season descriptions", "https://www.visitdhofarseasons.com/page/dhofar-seasons-events"),
    ("US International Trade Administration - Oman business travel and Ramadan operations", "https://www.trade.gov/country-commercial-guides/oman-business-travel"),
    ("DataReportal - Digital 2025: Oman", "https://datareportal.com/reports/digital-2025-oman"),
    ("55 Coffee - brand story and growth timeline", "https://55coffee.co/public/index.php?page=story"),
    ("55 Coffee - current location network", "https://55coffee.co/public/index.php?lang=en&page=locations"),
    ("55 Coffee - product and roastery positioning", "https://55coffee.co/"),
    ("Hills Cafe Ittin - public Google review aggregation via Wanderlog", "https://wanderlog.com/place/details/16794469/hills-cafe-ittin"),
    ("Hills Cafe - public Instagram account snapshot", "https://instastatistics.com/hills.cafe.om"),
    ("Lantana Caffe & Dolci - public review aggregation", "https://wanderlog.com/place/details/10717829/lantana-caffe--dolci"),
    ("Caribou Coffee Salalah - public review aggregation", "https://wanderlog.com/place/details/10864838"),
    ("Caribou Coffee Oman - Talabat rating and best sellers", "https://www.talabat.com/oman/caribou-coffee"),
    ("Toqa Coffee Salalah - public listing and review snapshot", "https://www.top-rated.online/cities/Salalah/place/p/14973434/Toqa%2BCoffee"),
    ("Pure Cafe - public brand site and listed branches", "https://edu-pure.odoo.com/about"),
    ("Bon Lab Cafe - workspace positioning and listing", "https://www.thecoworkingspaces.com/space/bon-lab-cafe"),
    ("Mute Cafe - public review aggregation", "https://wanderlog.com/place/details/13500786/mute-cafe"),
    ("Hurof Cafe - public review aggregation", "https://wanderlog.com/place/details/7799895/hurof-cafe"),
    ("Moin Cafe - public review aggregation", "https://wanderlog.com/place/details/16161103/%D9%85%D9%88%D9%8A%D9%86-%D9%83%D8%A7%D9%81%D9%8A%D9%87-moin-cafe--restaurant"),
    ("Beautiful Salalah - current local cafe discovery list", "https://www.beautifulsalalah.com/best-cafes-in-salalah/"),
    ("UTAS Salalah conference paper - Khareef motivation, satisfaction and value concerns", "https://icapth.utas.edu.om/wp-content/uploads/2025/07/THEME-I-Paper1.pdf"),
    ("Muscat online food delivery study - satisfaction factors", "https://papers.ssrn.com/sol3/Delivery.cfm/5021181.pdf?abstractid=5021181&mirid=1"),
    ("Times of Oman - delivery platform disruption and SME dependence", "https://timesofoman.com/article/164685-online-food-delivery-slowdown-cripples-omans-restaurants-cafs-and-cloud-kitchens"),
    ("Gov.om - permit for tourist restaurants and cafes", "https://gov.om/en/w/get-a-security-permit-to-establish-tourist-restaurants-and-cafes"),
    ("Oman Tax Authority - current tax rates", "https://tms.taxoman.gov.om/portal/web/taxportal/tax-rate"),
    ("Haven internal pricing study - 26 Jul 2026", "internal:docs/pricing-study-2026-07-26.md"),
    ("Haven internal coffee-shop friction study - 28 Jul 2026", "internal:research/coffee-shop-friction-study.md"),
    ("Haven internal Khareef social media playbook - 2026", "internal:output/strategy/Haven_Khareef_Social_Media_Playbook_2026.pdf"),
    ("2OZ Cafe - public profile and Instagram signal", "https://hopsa.io/en/attractions/oman%2Cfood-drink%2C2oz-cafe-c4607e985f"),
    ("Caika Cafe Salalah - public listing; limited public evidence", "https://yandex.com/maps/org/md_cafe_store/121765971573/"),
    ("FARJAR interiors - Caika Salalah project evidence", "https://farjarinteriors.om/pages/projects.html"),
    ("Salalah Gardens Mall - current dining directory", "https://www.salalahgardensmall.com.om/dining-directory"),
    ("Hills Cafe Salalah - current Talabat menu and prices", "https://www.talabat.com/oman/restaurant/699748/hills-cafe-new-salalah?aid=5607"),
    ("Oman Tax Authority - VAT registration guidance", "https://tms.taxoman.gov.om/portal/registration"),
    ("Times of Oman / ONA - Osara coastal destination redevelopment", "https://timesofoman.com/article/160833-osara-project-a-coastal-tourist-entertainment-destination-for-khareef-dhofars-season"),
    ("Beautiful Salalah - Raysut Waterfront destination guide", "https://www.beautifulsalalah.com/raysut-waterfront-salalah/"),
    ("Google Maps - Osara place, reviews and route reference", "https://www.google.com/maps/place/%D8%A7%D9%88%D8%B3%D8%A7%D8%B1%D8%A7+OSARA/@16.9662899,54.0037033,17z"),
    ("Salalah Vocational College - location and published hours", "https://www.bizmideast.com/OM/salalah-vocational-college-23-219614"),
    ("Oasis Club - evidence of established destination dining in Raysut", "https://www.tripadvisor.com/Restaurant_Review-g298419-d2243251-Reviews-or55-Oasis_Club-Salalah_Dhofar_Governorate.html"),
]


def source_ref(n: int) -> str:
    return f"<font color='#1E6F78'>[{n}]</font>"


def build_story():
    s = []

    # Cover
    s.append(Spacer(1, 8 * mm))
    if LOGO.exists():
        s.append(Image(str(LOGO), width=65 * mm, height=37.1 * mm))
        s.append(Spacer(1, 12 * mm))
    s.append(p("Salalah's evergreen cafe opportunity", styles["TitleCover"]))
    s.append(p("An evidence-led market study for Haven", styles["CoverSub"]))
    s.append(Spacer(1, 7 * mm))
    s.append(
        p(
            "Coffee shops, cake and dessert destinations, tourism seasonality, market leaders, emerging concepts, customer perception, social conversion, operating risks and a realistic route to a durable brand.",
            styles["CoverSub"],
        )
    )
    s.append(Spacer(1, 50 * mm))
    s.append(p("RESEARCH DATE  30 JULY 2026", styles["CoverSub"]))
    s.append(p("PRIMARY MARKET  SALALAH AND SURROUNDING DHOFAR", styles["CoverSub"]))
    s.append(p("DECISION HORIZON  2026-2028", styles["CoverSub"]))
    s.append(NextPageTemplate("body"))
    s.append(PageBreak())

    # Executive decision brief
    s += section_title("00", "Decision brief", "The answer first: what Haven should become, what it should avoid, and what must be proved.")
    s.append(
        shaded_callout(
            "<b>Recommendation:</b> build Haven as a <b>resident-first Dhofari coastal dayhouse</b> - a dependable coffee, bakehouse and light-breakfast routine with a distinctive sense of place. The view should amplify the brand, not carry it. The commercial engine is frequent local use; Khareef is the accelerator."
        )
    )
    s.append(Spacer(1, 4 * mm))
    s.append(
        kpi_row(
            [
                ("1.048m", "Khareef visitors in the full 2024 season [1]"),
                ("71.5%", "Omani share of visitors through 15 Aug 2025 [2]"),
                ("29", "55 Coffee branches reported in 2026 [9]"),
                ("61.8%", "Instagram ad reach among Omani adults in early 2025 [8]"),
            ]
        )
    )
    s.append(Spacer(1, 5 * mm))
    s.append(p("The strategic diagnosis", styles["H2x"]))
    for item in [
        "<b>Demand is concentrated but not absent off-season.</b> Khareef creates an extraordinary visitor spike, yet the viable base must come from residents, students, employees, families and repeat expat customers.",
        "<b>The market is crowded with visual sameness.</b> Spanish lattes, San Sebastian cake, polished interiors and evening hours are table stakes. They are not a niche.",
        "<b>The leaders own a job.</b> 55 Coffee owns convenience and scale; Hills owns seasonal spectacle; Bon Lab owns calm productivity; Hurof owns breakfast and care; Caribou owns familiar comfort.",
        "<b>The largest opportunity is consistency with meaning.</b> Reviews repeatedly reward atmosphere, kind service, quiet, breakfast and memorable desserts; they punish weak coffee, slow or dismissive service, crowd management failures and value mismatch.",
        "<b>Social media can fill a new venue once.</b> It converts sustainably only when exact location, hours, product truth, operational readiness, a measurable call to action and repeat capture are joined together.",
    ]:
        s.append(bullet(item))
    s.append(p("No-go concepts", styles["H2x"]))
    s.append(
        table(
            [
                ["Concept to avoid", "Why"],
                ["Another photogenic dessert cafe", "Low defensibility; novelty decays; easy to imitate; atmosphere can outrun product."],
                ["Direct low-price drive-through fight", "55 already combines value, late hours, density, familiarity and national scale."],
                ["Purist specialty lab only", "Credible but narrower demand; hard to support a larger venue without food and occasion breadth."],
                ["Khareef-first pop-up economics", "Peak volume can conceal weak baseline demand and brittle staffing, queue and waste systems."],
            ],
            [54 * mm, 118 * mm],
        )
    )
    s.append(PageBreak())

    # Method
    s += section_title("01", "Scope, method and confidence", "A decision study using public evidence, not a claimed census of every Salalah cafe.")
    s.append(p("Evidence used", styles["H2x"]))
    s.append(
        table(
            [
                ["Evidence layer", "Use", "Confidence / limitation"],
                ["Official and institutional", "Tourism volumes, airport flows, tax and permits", "Highest confidence for reported dates; not a direct cafe-demand measure."],
                ["Brand-owned", "55 history, branch count, product claims; Pure branches", "Reliable for stated positioning; not independent proof of profitability."],
                ["Public listings and menus", "Opening hours, channels, price bands, facilities", "Snapshots change; platform prices can exceed counter prices."],
                ["Review aggregators", "Recurring praise and complaint themes", "Directional. Self-selection, fake reviews and aggregation errors are possible."],
                ["Public social profiles", "Audience size, content architecture, location clarity", "Follower count is not conversion or local audience quality."],
                ["Haven internal studies", "Local price evidence, social and operating implications", "Useful current fieldwork; not an independent external source."],
            ],
            [34 * mm, 65 * mm, 73 * mm],
            small=True,
        )
    )
    s.append(p("Interpretation rules", styles["H2x"]))
    for item in [
        "A brand is called a leader when there is visible scale, strong public awareness, repeat-discovery prominence or a clearly owned use case - not because revenue data are public.",
        "No public local source ties a specific Reel to audited sales. Social conversion conclusions are therefore based on platform mechanics, visible brand behavior and restaurant-choice evidence, with causation stated cautiously.",
        "A separate local business named <b>Toca</b> could not be validated. The report treats the likely reference as <b>Toqa Coffee</b>; the two should be confirmed before site-level decisions.",
        "Caika is included because it is visibly present and design-led, but its indexed public review and operating data are sparse. Conclusions about it are provisional.",
        "Illustrative economics are decision thresholds, not forecasts. Rent, payroll, fit-out, financing, utility capacity and supplier quotations must replace the assumptions before investment.",
    ]:
        s.append(bullet(item))
    s.append(p("Research cut-off", styles["H2x"]))
    s.append(p("Public facts and profile snapshots were checked through 30 July 2026. Sources are listed in the appendix and linked where public.", styles["Bodyx"]))

    # Market demand
    s.append(PageBreak())
    s += section_title("02", "The real Salalah demand curve", "Four commercial seasons and several dayparts - not one annual average.")
    s.append(season_chart())
    s.append(p("The chart is an operating hypothesis, not measured sales. It converts official tourism timing, Ramadan constraints and local cafe-hour patterns into a testable demand calendar.", styles["Smallx"]))
    s.append(
        table(
            [
                ["Demand mode", "Typical customer job", "Commercial implication"],
                ["Jan-Feb: warm winter", "Visitors and residents seek beaches, heritage, breakfast, calm daytime use.", "Protect morning and daytime offer; tourism is lower-volume but less congested."],
                ["Ramadan: lunar / moving", "After-iftar family and friend gathering; gifting and late-night treats.", "Day demand contracts outside hotels; night peak compresses. Build pre-order, gifting and fast recovery."],
                ["Mar-May: resident baseline", "Routine coffee, work/study, school-run, birthdays and delivery.", "This is the truth test. Keep labor, menu and occupancy viable without tourism."],
                ["21 Jun-Sep: Khareef", "Omani and GCC family road trips, mist, scenery, sharing, evening plans.", "Extend capacity, simplify peak menu, control queues, localize discovery and capture visitor spend."],
                ["Late Sep-Nov: Sarb / post-Khareef", "Clearer landscapes, outdoor comfort, local reset, smaller international flows.", "Shift from mist content to coast, harvest, heritage, walking and community occasions."],
                ["Dec: holidays / winter", "Family visits, gifting, social gatherings, cooler outdoor use.", "Seasonal bakes and pre-orders can raise ticket without overloading the drink bar."],
            ],
            [34 * mm, 68 * mm, 70 * mm],
            small=True,
        )
    )
    s.append(p("Scale and concentration", styles["H2x"]))
    for item in [
        f"Dhofar attracted approximately <b>1.048 million</b> visitors between 21 June and 21 September 2024, 9% above 2023. Omanis were roughly 734,588 and GCC visitors 176,643. {source_ref(1)}",
        f"From 21 June to 15 August 2025, preliminary NCSI estimates counted <b>827,115</b> visitors. Omanis were 591,577; GCC visitors 143,431. Nearly <b>46.5%</b> arrived in just 1-15 August. {source_ref(2)}",
        f"Salalah Airport's international passenger total was broadly stable at 678,591 in 2025, while early-2025 passenger growth and Khareef flight growth show that the city also has meaningful non-peak and air-arrival demand. {source_ref(4)} {source_ref(5)}",
        f"Ramadan materially changes cafe operating hours: restaurants and cafes outside some hotels close during daylight and reopen after sunset, concentrating social consumption at night. {source_ref(7)}",
    ]:
        s.append(bullet(item))

    # Customer jobs
    s.append(PageBreak())
    s += section_title("03", "Who buys, and why", "Segment by recurring job and friction, not only nationality.")
    s.append(
        table(
            [
                ["Segment / job", "What wins", "What loses", "Haven response"],
                ["Resident routine seeker", "Predictable taste, parking, speed, fair price, remembered order", "Novelty without reliability", "Fast core menu, direct loyalty, morning reliability."],
                ["Women / family groups", "Comfort, privacy cues, clean facilities, kind service, shareable food", "Crowded ambiguity, rude recovery", "Flexible group seating, queue clarity, hospitality standard."],
                ["Students / remote workers", "Wi-Fi, plugs, quiet, stay permission, affordable repeat item", "Loud peak mix, seat conflict", "Zoned dayparts; not a full coworking business."],
                ["Khareef road-trip family", "Exact route, parking, weather proof, fast group ordering, local memory", "Long unknown waits, sold-out hero items", "Peak menu, car-friendly pickup, live availability."],
                ["GCC social explorer", "Recognizable quality plus a uniquely Dhofari moment", "Generic copy of Riyadh/Dubai aesthetics", "Coastal/Dhofari story, polished signature, bilingual discovery."],
                ["International winter visitor", "Breakfast, local flavor, readable menu, card payment, staff guidance", "Late-only opening, opaque menu", "Strong morning, clear English, tasting flight / origin story."],
                ["Celebration / gifting buyer", "Reliable whole cakes, packaging, personalization, collection slot", "Inconsistent inventory, late handoff", "Pre-order bakehouse line and occasion CRM."],
            ],
            [31 * mm, 46 * mm, 43 * mm, 52 * mm],
            small=True,
        )
    )
    s.append(
        shaded_callout(
            "<b>The evergreen insight:</b> the highest-frequency jobs are not 'see something beautiful.' They are 'make my morning easy,' 'give us a comfortable place to meet,' 'help me work for an hour,' and 'provide a dependable treat or gift.' Haven can still be beautiful - but those jobs pay the rent."
        )
    )
    s.append(p("Daypart architecture", styles["H2x"]))
    s.append(
        table(
            [
                ["Daypart", "Primary use", "Operational promise", "Menu emphasis"],
                ["07:00-11:00", "Routine, school run, breakfast, winter visitors", "< 6 minute core handoff", "Espresso, batch / filter, breakfast bun, croissant, light local special."],
                ["11:00-16:00", "Work, meetings, delivery, quiet social", "Reliable Wi-Fi and low noise zone", "Coffee, tea, lunch-light item, cake, direct delivery."],
                ["16:00-20:00", "Families, after-school, sunset", "Group seating and visible queue", "Signature cold drinks, shareable bakes, kids-safe options."],
                ["20:00-close", "Friends, late social, Ramadan / Khareef peak", "Peak menu and capacity control", "Fast signatures, desserts, decaf / tea, pre-packed gifting."],
            ],
            [28 * mm, 47 * mm, 46 * mm, 51 * mm],
        )
    )

    # Competitive map
    s.append(PageBreak())
    s += section_title("04", "Competitive landscape", "The visible market is broad; the defensible positions are much narrower.")
    s.append(competitor_map())
    s.append(p("Positioning is an analytical estimate from public evidence, not a consumer survey. 'Haven target' moves the brand toward repeat routine while retaining place advantage.", styles["Smallx"]))
    s.append(
        table(
            [
                ["Player", "Position owned", "Evidence / momentum", "Exposed flank"],
                ["55 Coffee", "Accessible Omani chain; value, speed, density, late hours", "From 1 kiosk in 2018 to 29 branches in 2026; 12 in Dhofar claimed. [9][10]", "Scale can feel standardized; room for deeper hospitality and place."],
                ["Hills", "Shareable Khareef / mountain destination plus mall presence", "17.4K public IG snapshot; Ittin setting; accessible 1.2-1.8 OMR drink band. [12][13][36]", "Mixed service and coffee-quality reviews; seasonal dependence."],
                ["Caika", "Cake-led, designed destination", "Local physical/design evidence; weak indexed operating data. [33][34]", "Public discovery and review proof appear underdeveloped."],
                ["Toqa", "Early / 24-hour routine and drive-through convenience", "4.4 / 25 listing snapshot; delivery, drive-through, quick bite. [17]", "Small review footprint; less visible emotional story."],
                ["Pure", "Local tradition-meets-modernity, multi-node access", "Five Salalah-area branches listed, including beach, mall, fuel and resort nodes. [18]", "Public digital presentation appears inconsistent / weakly premium."],
                ["Bon Lab", "Quiet specialty coffee and productive stay", "Work/study positioning, skilled-barista review themes. [19]", "Long dwell can weaken seat economics; narrower family / celebration fit."],
                ["Caribou", "Familiar international comfort and broad menu", "3.9 / 146 local aggregation; 4.4 / 1,000 Oman Talabat ratings. [15][16]", "Coffee may be perceived as conventional; local identity weaker."],
                ["Hurof", "Breakfast, local care, family suitability", "4.5 / 206 aggregation; strong breakfast and staff themes. [21]", "Operational complexity of food; less pure grab-and-go."],
                ["2OZ / Mute", "Coffee credibility, quiet, modern specialty identity", "2OZ 14K Instagram signal; Mute praise for decor, coffee and homemade bakes. [20][32]", "Service incidents can destroy premium trust."],
                ["Lantana", "Beach view, desserts, relaxed occasion", "3.9 / 315 aggregation; strong view/dessert, mixed coffee/service. [14]", "Atmosphere-product mismatch and seat allocation friction."],
            ],
            [25 * mm, 39 * mm, 58 * mm, 50 * mm],
            small=True,
        )
    )

    # Deep dives
    s.append(PageBreak())
    s += section_title("05", "What the leaders teach", "Success patterns, not imitation targets.")
    deep = [
        (
            "55 Coffee - the clearest local scale case",
            [
                "Founded as a Salalah kiosk in 2018; the brand reports 29 branches in 2026, including 12 in Dhofar, 13 in Muscat and 4 in Al Batinah. It says 11 openings occurred in 2025. [9]",
                "Its network includes 24-hour and fuel / route-adjacent sites, plus university, mall and city nodes. This is route capture and availability, not only cafe design. [10]",
                "The national Omani identity, repeatable sweet-leaning cold drinks, own roasting claim and disciplined master brand make expansion legible. [11]",
                "<b>Lesson:</b> a scalable brand makes the same promise in many contexts. Haven should borrow the discipline - signature memory, operating standards and node logic - without fighting on branch density.",
            ],
        ),
        (
            "Hills - attention, setting and the conversion risk",
            [
                "Hills has strong social visibility and an inherently shareable Ittin setting. Its delivery menu is accessible: iced latte OMR 1.4, Spanish latte OMR 1.6 and cakes around OMR 2-3. [13][36]",
                "Public reviews praise the place and pistachio latte, yet visible complaints cite cold drinks, weak V60 / sweets and inattentive service. [12]",
                "<b>Lesson:</b> place can win discovery faster than operations mature. That creates opening volume, but also amplifies failures. Haven needs a capacity-ready peak menu before paid reach.",
            ],
        ),
        (
            "Caribou - the durable reference point",
            [
                "Caribou's strengths are familiar breadth, a comfortable environment, food attachment, seating and dependable category cues. Local reviews repeatedly mention coziness and staff friendliness. [15]",
                "Across Oman, Talabat shows 4.4 from 1,000 ratings and bestseller concentration in Spanish latte, latte and cappuccino. [16]",
                "<b>Lesson:</b> customers value a low-risk place as much as novelty. Haven should be easier to trust while remaining more locally meaningful.",
            ],
        ),
        (
            "Emerging specialists - Hills, Caika, Bon Lab, Hurof, Mute",
            [
                "The most interesting newer players each narrow the reason to visit: a dramatic location, cake / design, quiet work, breakfast / family care, or specialty culture.",
                "The recurring weakness is not lack of creativity. It is the gap between the front-stage promise and service, queue, availability or product consistency.",
                "<b>Lesson:</b> Haven's niche must be operationally simpler than its story sounds.",
            ],
        ),
    ]
    for heading, bullets in deep:
        s.append(p(heading, styles["H2x"]))
        for x in bullets:
            s.append(bullet(x))

    # Perception
    s.append(PageBreak())
    s += section_title("06", "What customers are saying", "A thematic reading of public reviews and local discussion - directional, not statistically representative.")
    s.append(
        table(
            [
                ["Theme", "What earns praise", "What triggers disappointment", "Implication"],
                ["Place", "Beach / mountain views, calm, attractive but comfortable spaces", "A beautiful location that is crowded, unmanaged or not worth the product", "Design the queue and seating system as part of the experience."],
                ["Coffee", "Balanced classics, good espresso, knowledgeable baristas", "Average coffee behind a specialty claim; cold temperature; over-sweetness", "Publish recipes, calibrate daily, offer sweetness control."],
                ["Dessert / bakery", "One memorable hero, homemade character, freshness", "Generic bought-in cake, poor texture, weak value", "Own 3-5 bakes; do not carry a catalogue of lookalikes."],
                ["Service", "Warm recognition, helpful staff, recovery with grace", "Indifference, argument, long unknown waits, understaffing", "Hospitality and recovery are product features."],
                ["Usefulness", "Breakfast, quiet study, Wi-Fi, parking, drive-through, 24-hour access", "Wrong opening hours, unclear route, no non-dairy option", "Conversion surfaces must answer practical questions."],
                ["Value", "Fair price supported by portion and quality", "High seasonal price without service / quality proof", "Keep an accessible entry item and make premiums visible."],
            ],
            [29 * mm, 50 * mm, 52 * mm, 41 * mm],
            small=True,
        )
    )
    s.append(p("Representative public signals", styles["H2x"]))
    for item in [
        f"Lantana reviews praise the white-sand beach, desserts and staff, but also call the coffee average, note limited non-dairy choice and describe seating / wait friction. {source_ref(14)}",
        f"Hills' Ittin reviews show the same attention-quality split: strong place appeal and a recommended pistachio latte alongside service, drink-temperature and V60 complaints. {source_ref(12)}",
        f"Mute demonstrates how a quiet, distinctive interior and homemade cakes can generate affection, while a single confrontational recovery incident can become a highly visible 1-star story. {source_ref(20)}",
        f"Hurof and Moin show a more evergreen pattern: breakfast, calm, staff care and specific food heroes create repeat recommendation beyond scenery. {source_ref(21)} {source_ref(22)}",
        f"A Khareef visitor-perception study reported positive overall feelings but highlighted high prices and weak value-for-money in services - a warning against peak-season opportunism. {source_ref(24)}",
    ]:
        s.append(bullet(item))
    s.append(
        shaded_callout(
            "<b>Customer perception in one sentence:</b> Salalah customers will forgive simplicity; they do not forgive a mismatch. A modest cafe with good coffee, calm and kind service can be loved. A spectacular cafe with weak execution is judged more harshly because the promise was larger."
        )
    )

    # Social
    s.append(PageBreak())
    s += section_title("07", "Social media: where it converts, where it fails", "The useful distinction is not organic versus paid. It is attention versus attributable behavior.")
    s.append(funnel_chart())
    s.append(p("Why social matters locally", styles["H2x"]))
    for item in [
        f"Oman had 3.29 million social-media user identities in early 2025. Instagram's advertising tools indicated 2.50 million reachable users and 61.8% reach among adults; Snapchat reached 2.15 million users and TikTok 1.83 million adults. These are ad-reach estimates, not active-user counts. {source_ref(8)}",
        "Khareef compresses discovery and decision into hours: people ask what to do tonight, what the weather looks like and where the route / parking is. Real-time place evidence is unusually valuable.",
        "Public follower snapshots illustrate awareness, not sales: 55 Coffee was about 62.2K in Haven's July 2026 internal snapshot, Hills about 17.4K, Voliere about 17.1K, 2OZ about 14K and Lantana about 8.2K. [13][31][32]",
    ]:
        s.append(bullet(item))
    s.append(
        table(
            [
                ["Pattern", "Why it works", "What proves conversion"],
                ["Place-first short video", "Answers 'why now?' and is easy to send to a group", "Shares, map taps, arrival code, transactions in the next 24 hours."],
                ["Specific hero product", "Builds memory and makes ordering easy", "Named-item mix and repeat purchase, not likes."],
                ["Creator Collab / guest proof", "Borrows trusted local distribution", "New local reach, profile-to-map rate, creator code contribution."],
                ["Exact route, hours, parking, price", "Removes the last practical reasons not to visit", "Map opens, direction requests, fewer repetitive DMs."],
                ["Live Stories in Khareef", "Shows truthful weather, seat status and energy", "Same-day footfall and saved Location Highlight."],
                ["Review / UGC loop", "Turns operations into distributed trust", "Review velocity, rating quality, tagged content, 30-day return."],
            ],
            [44 * mm, 70 * mm, 58 * mm],
        )
    )
    s.append(p("Where it goes wrong", styles["H2x"]))
    for item in [
        "<b>Views without a local action:</b> cinematic content reaches people who cannot or will not visit.",
        "<b>Influencer opening without capacity:</b> the campaign converts, but the bar, seating and recovery fail. The bad experience then generates stronger word of mouth than the launch.",
        "<b>Generic product beauty:</b> a cup and cake could belong to any cafe. The audience remembers the format, not the brand.",
        "<b>Follower worship:</b> no measurement of map taps, source-coded POS, customer acquisition cost or 30-day repeat.",
        "<b>False scarcity or weather:</b> staged fog, unavailable products and inaccurate hours break trust.",
        "<b>Discount dependency:</b> customers learn to wait for offers; full-price attachment and brand meaning weaken.",
    ]:
        s.append(bullet(item))

    # Experiments
    s.append(PageBreak())
    s += section_title("08", "Experiments, innovations and missed opportunities", "What has worked, what appears underused, and what typically fails.")
    s.append(
        table(
            [
                ["Observed / adjacent pattern", "Verdict", "Why", "Haven use"],
                ["Dense kiosks, route nodes, 24-hour access (55)", "WORKS", "Makes coffee part of an existing journey.", "Design pickup / parking first; consider smaller second node only after baseline proof."],
                ["Own / controlled roasting story (55; specialty set)", "WORKS WITH PROOF", "Signals consistency and craft.", "Start with transparent partner sourcing; do not invest in roasting before volume and expertise."],
                ["Destination placement (Hills, Lantana)", "WORKS FOR DISCOVERY", "A place gives content and occasion.", "Keep the coast, but create a winter / weekday use reason."],
                ["Breakfast + coffee (Hurof, Moin, Caribou)", "EVERGREEN", "Raises frequency, daypart breadth and ticket.", "Build 4-6 fast items, not a restaurant kitchen."],
                ["Quiet work / study (Bon Lab, Mute)", "WORKS SELECTIVELY", "Creates repeat dwell and loyalty.", "Zone seats and dayparts; manage laptop economics."],
                ["Cake hero / gifting", "UNDERDEVELOPED", "Occasion demand survives tourism cycles.", "Pre-order whole cakes, celebration boxes, corporate / hotel gifting."],
                ["Non-dairy, sweetness choice, decaf", "MISSED BASICS", "Public complaints show avoidable exclusion.", "Offer 1-2 plant milks, half-sweet defaults and a credible decaf."],
                ["Owned customer list", "MAJOR GAP", "Platforms and aggregators control reach and margin.", "WhatsApp opt-in, simple stamp / wallet and direct preorder."],
                ["Generic novelty drinks and huge menus", "FAILS QUIETLY", "Inventory, training and decision load rise while memory diffuses.", "Keep signatures scarce and rotate one seasonal test at a time."],
                ["Unmanaged delivery dependence", "HIGH RISK", "Commission and disruption weaken margin and service priority. [25][26]", "Use aggregator for discovery, then migrate permissible repeat business to direct."],
            ],
            [49 * mm, 28 * mm, 51 * mm, 44 * mm],
            small=True,
        )
    )
    s.append(p("The most valuable missed opportunity", styles["H2x"]))
    s.append(
        shaded_callout(
            "The market has many places to buy an iced Spanish latte and a cake. It has fewer brands that connect <b>Dhofari identity, excellent morning use, a tight bakehouse, calm hospitality, reliable direct ordering and a visitor-worthy coastal setting</b> in one repeatable system."
        )
    )

    # Niche scoring
    s.append(PageBreak())
    s += section_title("09", "Which evergreen niche is genuinely attractive?", "Five routes scored against repeat demand, defensibility, fit, margins, season resilience and execution risk.")
    s.append(score_chart())
    s.append(
        table(
            [
                ["Option", "Repeat demand", "Season resilience", "Defensibility", "Execution", "Weighted /100"],
                ["Instagram destination dessert cafe", "2", "1", "2", "3", "45"],
                ["Low-price drive-through", "5", "5", "1", "2", "51"],
                ["Pure specialty coffee lab", "3", "4", "4", "3", "61"],
                ["Cake / gifting studio + cafe", "4", "5", "4", "3", "68"],
                ["Dhofari coastal dayhouse", "5", "5", "4", "4", "86"],
            ],
            [54 * mm, 25 * mm, 28 * mm, 25 * mm, 21 * mm, 19 * mm],
        )
    )
    s.append(p("Why the recommended option wins", styles["H2x"]))
    for item in [
        "It serves at least three resident habits - morning fuel, comfortable meeting and dependable treat - before tourism is counted.",
        "It uses Haven's coastal asset while making the inside, product and service sufficient on a hot, windy or ordinary day.",
        "It is culturally legible to visitors without becoming a souvenir concept.",
        "It supports several revenue forms: drinks, breakfast, slice dessert, whole-cake preorder, gifting, direct pickup and selected delivery.",
        "It can start small. The brand does not need a roastery, complex kitchen, app or large branch network to prove the job.",
    ]:
        s.append(bullet(item))

    # Concept blueprint
    s.append(PageBreak())
    s += section_title("10", "The Haven concept blueprint", "A resident routine with a visitor-worthy sense of Dhofar.")
    s.append(p("Positioning statement", styles["H2x"]))
    s.append(
        shaded_callout(
            "<b>For Salalah residents who want a dependable place to begin, pause or meet - and for visitors who want a real sense of Dhofar - Haven is the coastal coffee and bakehouse dayhouse that combines calibrated coffee, a small fresh bake menu, warm hospitality and a calm place worth returning to.</b>"
        )
    )
    s.append(p("The four pillars", styles["H2x"]))
    s.append(
        table(
            [
                ["Pillar", "Customer promise", "Proof"],
                ["Everyday reliability", "Your usual is available, correctly made and fast.", "Recipe cards, opening discipline, 90th-percentile handoff, stockout control."],
                ["Dhofari sense of place", "This could only feel right in Salalah.", "Coast, materials, stories and restrained local ingredients - no themed clutter."],
                ["Small fresh bakehouse", "There is always one thing worth adding or taking home.", "3 daily heroes, 1 rotating seasonal, whole-cake / box preorder."],
                ["Warm calm", "You are looked after without being rushed or ignored.", "Greeting, seating guidance, recovery standard, zoned dayparts."],
            ],
            [35 * mm, 66 * mm, 71 * mm],
        )
    )
    s.append(p("Menu architecture", styles["H2x"]))
    s.append(
        table(
            [
                ["Layer", "Role", "Recommended shape", "Guardrail"],
                ["Core coffee", "Routine and credibility", "Espresso, Americano, latte, cappuccino, flat white, Spanish, filter / V60", "One calibrated house profile; sweetness choice."],
                ["Dhofar signatures", "Memory and social distinctiveness", "2 permanent drinks + 1 seasonal; test coconut, banana, cardamom, rose or frankincense carefully", "Flavor must improve the drink, not just tell a story."],
                ["Breakfast / savory", "Morning frequency and ticket", "4-6 fast bakes / sandwiches; one light local reference", "No full restaurant line; <6 minute core."],
                ["Bakehouse", "Attachment, celebration, gifting", "3 daily slices, 1 warm hero, 2 preorder whole cakes / boxes", "Freshness and sell-through before variety."],
                ["Inclusive choices", "Avoid preventable exclusion", "Decaf, 1-2 plant milks, low-sugar / unsweetened, child-friendly", "Charge transparently; train recipes."],
            ],
            [34 * mm, 39 * mm, 64 * mm, 35 * mm],
            small=True,
        )
    )
    s.append(p("Price posture", styles["H2x"]))
    s.append(p(f"Haven's current proposed drink band is generally mid-market for Salalah, while its OMR 1.8 San Sebastian slice is value-leading and its OMR 2.5 brownie requires visible premium proof. The recommended posture is <b>accessible specialty</b>: one low-friction daily drink, credible mid-market signatures, and premium only where portion, craft or packaging proves it. {source_ref(29)}", styles["Bodyx"]))

    # Location and channel
    s.append(PageBreak())
    s += section_title("11", "Place, channel and operating model", "The site should create demand, but the operating system must keep it.")
    s.append(
        table(
            [
                ["Design decision", "Recommendation", "Reason"],
                ["Front door", "Readable from a car; exact map pin; parking / pickup instruction", "Salalah is route-based and visitors arrive by car."],
                ["Weather resilience", "A fully credible indoor experience plus shaded / wind-tolerant outside", "The coast is an asset only when customers remain comfortable."],
                ["Seat mix", "2-person, group, short-stay and a limited work zone", "Prevents one use case from consuming all capacity."],
                ["Queue", "One visible order queue, honest ready time, separated pickup", "Unknown waits and crowd conflict damage reviews."],
                ["Peak menu", "Fewer modifiers and items during severe Khareef / Ramadan peaks", "Protects quality and handoff."],
                ["Delivery", "Limited radius and delivery-safe menu; do not prioritize it blindly over dine-in", "Coffee quality and guest service decay with channel conflict."],
                ["Owned channel", "WhatsApp preorder, simple loyalty and opt-in customer list", "Reduces dependency on paid reach and aggregators."],
            ],
            [38 * mm, 72 * mm, 62 * mm],
        )
    )
    s.append(p("Minimum viable technology", styles["H2x"]))
    for item in [
        "POS item and modifier discipline; source code for Google, Instagram, Snapchat, creator, hotel and walk-by.",
        "Google Business Profile as the highest-intent surface: current hours, route, parking, menu, photos and review response.",
        "WhatsApp Business for preorders, collection slots, celebration products and consented broadcast - not spam.",
        "A loyalty mechanism simple enough to explain in one breath. Start with visible visits / stamps before complex points.",
        "A daily dashboard: transactions, average ticket, food attachment, waste, stockouts, median and 90th-percentile handoff, rating / complaint and repeat ID.",
    ]:
        s.append(bullet(item))
    s.append(p("Regulatory reality", styles["H2x"]))
    s.append(p(f"A tourist restaurant / cafe permit route can require Ministry of Heritage and Tourism approval, commercial registration, property plan and security conditions. Oman applies a 5% standard VAT rate to most goods and services; registration obligations depend on turnover. This report is not legal advice - confirm the exact activity, municipality, outdoor seating, food-safety, labor and tax requirements for the chosen entity and site. {source_ref(27)} {source_ref(28)} {source_ref(37)}", styles["Bodyx"]))

    # Osara / Raysut site viability
    s.append(PageBreak())
    s += section_title("11A", "Osara waterfront viability", "The location can work, but the nearby anchors are channels to convert - not demand to assume.")
    s.append(
        shaded_callout(
            "<b>Assessment: conditionally attractive.</b> Keep and improve the waterfront only through a staged expansion with a normal-period demand gate. The strongest base is existing Osara traffic plus Raysut and Awqad residents. College, port and Hilton demand should enter the model only after source-coded tests prove conversion."
        )
    )
    s.append(p("Catchment correction", styles["H2x"]))
    s.append(
        table(
            [
                ["Catchment / anchor", "Indicative drive to Osara", "Commercial role", "Judgment"],
                ["Raysut residents", "About 6 min / 3.4 km", "Routine resident base", "Easy relative win if product, parking and hours are dependable."],
                ["Vocational College", "About 3 min / 1.6 km", "Weekday value and pickup channel", "High potential, but budget, timetable, transport and Fri-Sat closure constrain it."],
                ["Salalah Port", "About 7 min / 5.0 km", "Shift, staff and business-order channel", "Close on a map; gate access and shift timing make passive walk-in demand unlikely."],
                ["Hilton Salalah", "About 7 min / 5.5 km", "Tourist acquisition / concierge channel", "Useful seasonal feeder, but hotel F&B and transport friction must be overcome."],
                ["Awqad", "About 12 min / 9.9 km", "Strong secondary resident base", "Plausible routine / weekly catchment for a differentiated coastal venue."],
                ["Central Salalah / Gardens", "About 13 min / 12.0 km", "Occasion and meeting catchment", "Reachable, but must beat many closer alternatives."],
                ["Dahariz", "About 18 min / 17.1 km", "Destination / event catchment", "Not the hardest; unlikely routine, but viable for sunset, groups and a hero product."],
                ["Saadah", "About 26 min / 25.9 km", "Destination / campaign catchment", "Hard for repeat frequency except loyalists, events and Khareef."],
                ["Sahalnoot", "About 31 min / 34.2 km", "Destination / campaign catchment", "Hardest named resident market; exclude from baseline forecast."],
            ],
            [31 * mm, 28 * mm, 48 * mm, 65 * mm],
            small=True,
        )
    )
    s.append(p(f"Drive times are indicative Google Maps snapshots to the Osara pin, not traffic studies. Osara itself is an established destination: public coverage describes expanded sea-view seating, restaurants, cafes, games and events, while current reviews repeatedly mention the sea, family suitability, seating and parking. This validates the place but also confirms internal competition for the same visit. {source_ref(38)} {source_ref(39)} {source_ref(40)}", styles["Smallx"]))
    s.append(p("What the two-zone plan gets right", styles["H2x"]))
    s.append(
        table(
            [
                ["Zone", "Primary job", "Best dayparts", "Design / operating rule"],
                ["Chill-out garden", "Comfort, repeat use, families, small groups, work and private occasions", "Morning, midday, warm / windy periods", "Shade, air movement, planting, plugs and flexible seating; protect quiet from kitchen and service noise."],
                ["Waterfront", "Acquisition, sunset, sea sound, visitor memory and social proof", "Late afternoon and evening", "Fast table finding, safe edge, low-glare lighting and a simple peak menu."],
                ["Shared kitchen / bar", "Consistency and labor efficiency", "All day", "One order system and one service map; never make guests guess where to order or collect."],
            ],
            [31 * mm, 55 * mm, 34 * mm, 52 * mm],
            small=True,
        )
    )
    s.append(p("Advantages", styles["H2x"]))
    for item in [
        "Rare sea, port and sunset setting with an existing destination audience, broad parking appeal and a credible content engine.",
        "Two distinct comfort modes reduce dependence on a single weather condition or customer occasion.",
        "A closer kitchen can reduce carrying distance, temperature loss and cross-traffic if exhaust, waste and noise are contained.",
        "Road visibility, exact map positioning and reliable hours can convert high-intent route traffic more efficiently than awareness-only social media.",
        f"Raysut already supports destination hospitality, suggesting that distance alone does not prevent a distinctive offer from drawing visitors. {source_ref(42)}",
    ]:
        s.append(bullet(item))
    site_risks = [
        "<b>Osara may own the visit.</b> Customers can switch among on-site cafes, so Haven needs a remembered product, service promise and owned customer relationship.",
        "<b>More seats are not automatically more demand.</b> Expansion is justified only if current peaks show turnaways, queue abandonment or lost group bookings.",
        "<b>Two zones can double complexity.</b> Without one POS, table map, runner plan and collection point, labor and wait times will rise faster than revenue.",
        "<b>Coastal capex ages quickly.</b> Salt corrosion, wind, humidity, spray, sand, rain, drainage, insects, anchoring and anti-slip surfaces need life-cycle costing.",
        "<b>Waterfront safety is a design gate.</b> Edge protection, children, accessibility, emergency access, electrical safety and night lighting require formal review.",
        "<b>Industrial context cuts both ways.</b> Port views can be distinctive, while heavy traffic, light, noise or odor can weaken the atmosphere at certain times.",
        "<b>Permissions and dependencies remain unpriced.</b> Lease control, signage, kitchen exhaust, outdoor structures, music, waste water and venue operating rules must be confirmed before fit-out.",
        f"<b>College availability is narrow.</b> Published hours are Sunday-Thursday, 08:00-17:00; test the actual student / staff population, breaks and transport before forecasting. {source_ref(41)}",
    ]
    s.append(KeepTogether([p("Risks and missing evidence", styles["H2x"]), bullet(site_risks[0])]))
    for item in site_risks[1:]:
        s.append(bullet(item))
    s.append(p("The site-specific niche", styles["H2x"]))
    s.append(
        shaded_callout(
            "The gap is not another beautiful Osara cafe. Osara already supplies scenery and seating. Haven should own the <b>all-day coastal dayhouse</b>: fast morning coffee and breakfast for the west-side routine, a genuinely comfortable garden through the day, and an unmistakable sunset waterfront experience - joined by one excellent product and service system."
        )
    )
    s.append(p("Staged investment gate", styles["H2x"]))
    s.append(
        table(
            [
                ["Stage", "Action", "Proceed only if"],
                ["1. Instrument", "Four normal-period weeks; count entrance traffic, Haven transactions, source, zone occupancy, turnaways, ticket, attachment, wait and repeat.", "Data coverage >=90%; normal weeks are separated from Khareef and launch effects."],
                ["2. Convert anchors", "College preorder / value code; port shift pickup / employer order; Hilton concierge / QR route; Awqad resident campaign.", "Each channel produces attributable contribution and repeat, not views or redemptions alone."],
                ["3. Prototype", "Lease option or short term for one adjacent unit; trial closer kitchen and a reversible garden layout.", "Total Haven sales rise after cannibalization; service time and reviews do not deteriorate."],
                ["4. Commit", "Permanent garden, waterfront and roadside identity.", "Normal-period orders exceed break-even by 20%; incremental contribution covers added fixed cost by at least 1.3x."],
            ],
            [27 * mm, 79 * mm, 66 * mm],
            small=True,
        )
    )

    # Economics
    s.append(PageBreak())
    s += section_title("12", "Illustrative unit economics", "A traffic threshold to challenge the concept before committing capital.")
    s.append(break_even_chart())
    s.append(
        table(
            [
                ["Assumption", "Illustrative value", "Why it matters"],
                ["Average ticket, VAT-inclusive", "OMR 3.20", "Approximately drink + partial food attachment; must be measured at Haven."],
                ["Net ticket before VAT", "OMR 3.05", "3.20 / 1.05."],
                ["Contribution after ingredients / packaging", "68% = OMR 2.07", "Excludes labor, rent, utilities, marketing, finance and owner draw."],
                ["Monthly fixed operating cost", "OMR 6k / 8k / 10k", "Sensitivity range only - replace with quotes."],
                ["Break-even orders / day", "97 / 129 / 161", "Assumes 30 trading days and constant mix."],
            ],
            [55 * mm, 43 * mm, 74 * mm],
        )
    )
    s.append(p("The investment rule", styles["H2x"]))
    s.append(
        shaded_callout(
            "Do not approve a full-scale build because Khareef can produce 160 orders a day. Approve it only when the <b>resident baseline</b>, measured in a normal non-holiday period, can plausibly support the fixed-cost case - ideally with a 20% buffer above break-even."
        )
    )
    s.append(p("Economics to model before a lease / expansion", styles["H2x"]))
    for item in [
        "Hourly order arrival and product mix by season; not daily averages alone.",
        "Drink-to-food attachment, whole-cake preorders and waste by SKU.",
        "Counter versus delivery contribution after platform fee, discount, VAT and remakes.",
        "Seat occupancy by daypart and revenue per occupied seat-hour.",
        "Peak labor, housing / transport, training, overtime and turnover.",
        "Utility capacity, cooling / weather protection, water, drainage, parking and fit-out life.",
    ]:
        s.append(bullet(item))

    # 90 day plan
    s.append(PageBreak())
    s += section_title("13", "A 90-day evidence plan", "Test the niche with behavior before expressing it in expensive architecture.")
    s.append(
        table(
            [
                ["Phase", "Test", "Success gate"],
                ["Days 1-14: baseline", "Instrument current operation. Record source, handoff, ticket, attachment, waste, stockouts, repeat identity and daypart.", "At least 90% of transactions captured with clean item / time data."],
                ["Days 15-30: morning job", "Launch one breakfast bundle and a 6-minute core promise on selected mornings.", "Incremental morning transactions; >=25% food attachment; P90 core handoff <=8 min."],
                ["Days 31-45: bakehouse", "Three daily bakes + two preorder celebration products.", "Sell-through >=85%; waste <=8%; whole-order contribution positive."],
                ["Days 46-60: Dhofar signatures", "Blind / named test of two signatures against current bestseller.", "One item reaches >=8% drink mix with repeat intent and acceptable complexity."],
                ["Days 61-75: owned repeat", "Simple stamp / WhatsApp opt-in with a return reason, no blanket discount.", ">=20% identifiable customers; >=25% 30-day repeat among enrolled baseline cohort."],
                ["Days 76-90: acquisition", "Run Google + Instagram / Snapchat local creative with source-coded POS.", "Positive contribution after media; map-to-transaction evidence; no service deterioration."],
            ],
            [36 * mm, 86 * mm, 50 * mm],
            small=True,
        )
    )
    s.append(p("Decision gates after 90 days", styles["H2x"]))
    s.append(
        table(
            [
                ["Decision", "Proceed if", "Stop / revise if"],
                ["Full dayhouse fit-out", "Normal-period baseline covers modeled fixed cost with 20% margin of safety.", "Demand only works on weekends, weather or paid launch bursts."],
                ["Bakehouse expansion", "Attachment and gifting contribution exceed waste and labor complexity.", "Variety grows faster than sell-through."],
                ["Second node / kiosk", "Core recipes, service times and repeat demand are stable; route opportunity is proven.", "Founder / best barista is still the operating system."],
                ["Roastery investment", "Bean volume, wholesale demand and specialist capability justify equipment and QA.", "It is mainly a branding wish."],
                ["Paid social scale", "Source-coded contribution and repeat exceed acquisition cost.", "Views rise but map taps, orders and repeat do not."],
            ],
            [38 * mm, 68 * mm, 66 * mm],
            small=True,
        )
    )

    # Risk register
    s.append(PageBreak())
    s += section_title("14", "Risk register and countermeasures", "The concept is attractive only if its failure modes are designed out.")
    s.append(
        table(
            [
                ["Risk", "Probability", "Impact", "Leading signal", "Countermeasure"],
                ["Khareef masks weak baseline", "High", "High", "Traffic drops >50% outside peak", "Resident baseline gate before fixed-cost expansion."],
                ["Atmosphere outruns coffee / service", "Medium", "High", "Review mentions 'nice place, average coffee'", "Calibration, mystery checks, recovery training, product truth."],
                ["Menu complexity", "High", "Medium", "Stockouts, remakes, long P90 wait", "SKU hurdle; one-in / one-out seasonal tests."],
                ["Delivery destroys margin / queue", "Medium", "High", "Platform mix rises while dine-in wait worsens", "Channel caps, separate queue rules, direct pickup migration."],
                ["Work guests occupy peak seats", "Medium", "Medium", "Low revenue per seat-hour", "Zoning and time / daypart policy, not confrontation."],
                ["Dhofari identity becomes gimmick", "Medium", "High", "Content shares but low repeat / taste score", "Subtle design, credible suppliers, flavor-first testing."],
                ["Founder dependence", "High", "High", "Quality falls on off-shifts", "Recipes, training, shift leads, audits and visual standards."],
                ["Price-value mismatch", "Medium", "High", "Low attachment, review complaints, discount sensitivity", "Accessible anchor, portion proof, bundle tests, no peak gouging."],
            ],
            [38 * mm, 20 * mm, 17 * mm, 44 * mm, 53 * mm],
            small=True,
        )
    )
    s.append(p("Final recommendation", styles["H2x"]))
    s.append(
        shaded_callout(
            "<b>Haven should not try to be Salalah's most fashionable cafe.</b> It should aim to be the cafe residents can use most naturally and visitors can remember most specifically. The winning sequence is: reliable routine first, bakehouse attachment second, Dhofari distinctiveness third, social amplification fourth, and expansion only after normal-period unit economics are proven.",
            color=FOG,
        )
    )

    # Appendix profiles
    s.append(PageBreak())
    s += section_title("A1", "Competitor profile notes", "Current public evidence, with confidence explicitly stated.")
    s.append(
        table(
            [
                ["Brand", "Public signal", "Confidence", "Research note"],
                ["55 Coffee", "Brand-owned history, 29 locations, current network and product architecture", "High for claimed facts", "Strongest scale benchmark; financial performance not public."],
                ["Hills", "Instagram scale, Talabat menu, Ittin reviews", "Medium-high", "Clear social / place momentum; execution appears uneven by branch / shift."],
                ["Caika", "Salalah listing and interior-project evidence", "Low", "Validate owner, current status, menu, social handle, sales and customer base in field."],
                ["Toqa", "24-hour / drive-through listing and reviews", "Medium", "Likely user's 'Toca'; confirm naming."],
                ["Pure", "Brand site lists five local nodes", "Medium", "Physical reach clear; brand site quality and listed hours should be field-checked."],
                ["Bon Lab", "Workspace listings and review themes", "Medium", "Strong use-case ownership; quantify seat / ticket economics in observation."],
                ["Caribou", "Local and Oman-wide review / delivery data", "Medium-high", "Useful reference for comfort, menu breadth and familiar risk reduction."],
                ["Hurof / Moin", "Large review samples and specific breakfast praise", "Medium-high", "Best evidence for evergreen food + hospitality strategy."],
                ["Lantana", "315-review aggregation with mixed themes", "Medium-high", "Strong case study in place-led demand and experience-product mismatch."],
                ["2OZ / Mute", "Specialty / quiet positioning and public profiles", "Medium", "Shows coffee credibility and work appeal; service consistency remains decisive."],
            ],
            [28 * mm, 66 * mm, 27 * mm, 51 * mm],
            small=True,
        )
    )
    s.append(p("Fieldwork still required before capital approval", styles["H2x"]))
    for item in [
        "Three normal weekdays and two weekends of traffic counts at shortlisted sites, by 30-minute interval.",
        "Mystery-shop the named competitors across morning, afternoon and evening; record order, price, wait, seat use, service and recovery.",
        "Twenty resident interviews each with women / family customers, young professionals / students and frequent specialty-coffee buyers.",
        "Ten hotel / tour / transport partner interviews covering winter and Khareef recommendations.",
        "Supplier quotations, lease heads of terms, utility survey, municipal pre-check and staffing plan.",
        "A review export or compliant manual sample large enough to code themes by brand, language, date and season.",
    ]:
        s.append(bullet(item))

    # Sources
    s.append(PageBreak())
    s += section_title("A2", "Sources and links", "Numbers in square brackets refer to this list. Internal Haven work is identified separately.")
    for i, (label, url) in enumerate(SOURCES, 1):
        if url.startswith("internal:"):
            rel = url.split("internal:", 1)[1]
            line = f"<b>[{i}] {label}</b><br/><font color='#66757D'>{rel}</font>"
        else:
            line = f"<b>[{i}] {label}</b><br/><link href='{url}' color='#1E6F78'>{url}</link>"
        s.append(p(line, styles["Smallx"]))
        if i in (12, 24):
            s.append(PageBreak())
            s += section_title("A2", "Sources and links - continued")

    # Closing
    s.append(PageBreak())
    s += section_title("A3", "One-page owner checklist", "The questions that should be answered before Haven spends the next rial.")
    checklist = [
        ["Question", "Yes / No", "Evidence"],
        ["Can normal-period resident demand support the fixed-cost model with a 20% buffer?", "", ""],
        ["Is there one customer job Haven can state without mentioning decor or views?", "", ""],
        ["Can 80% of peak orders be produced from a deliberately short menu?", "", ""],
        ["Do the top three bakes sell through with <=8% waste?", "", ""],
        ["Can a new barista reproduce the house drinks without the founder?", "", ""],
        ["Are map pin, parking, hours, menu and WhatsApp accurate everywhere?", "", ""],
        ["Can every paid / creator campaign be tied to a POS source and repeat cohort?", "", ""],
        ["Is delivery contribution positive after commission, packaging, VAT and remakes?", "", ""],
        ["Are permit, food safety, labor, tax and outdoor seating requirements confirmed?", "", ""],
        ["Would the concept still be attractive on a hot, ordinary Tuesday in May?", "", ""],
    ]
    s.append(table(checklist, [105 * mm, 22 * mm, 45 * mm], small=True))
    s.append(Spacer(1, 8 * mm))
    s.append(
        shaded_callout(
            "The evergreen niche is not a product category. It is a repeatable relationship: <b>the easiest good place in Salalah to return to, with a distinctly Dhofari reason to remember it.</b>",
            color=SAND,
        )
    )
    return s


if __name__ == "__main__":
    doc = make_doc()
    doc.build(build_story())
    print(OUT)
