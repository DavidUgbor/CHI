# -*- coding: utf-8 -*-
"""Generate a project-summary PDF for Ugbor Chidinma Benita's portfolio."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, ListFlowable, ListItem)

# ---- palette ----
NAVY  = colors.HexColor("#0D2137")
TEAL  = colors.HexColor("#0B6E6E")
GOLD  = colors.HexColor("#C9A84C")
SKY   = colors.HexColor("#EAF3FB")
MIST  = colors.HexColor("#F6FAFB")
MUTED = colors.HexColor("#5A6B82")
LINE  = colors.HexColor("#D8E2EC")

styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, parent=styles["Normal"], **kw)

st_title   = S("t",  fontName="Helvetica-Bold", fontSize=24, textColor=NAVY, leading=28, spaceAfter=2)
st_sub     = S("su", fontName="Helvetica", fontSize=11.5, textColor=TEAL, leading=15, spaceAfter=2)
st_meta    = S("m",  fontName="Helvetica", fontSize=8.5, textColor=MUTED, leading=12)
st_h2      = S("h2", fontName="Helvetica-Bold", fontSize=13.5, textColor=NAVY, leading=17, spaceBefore=14, spaceAfter=5)
st_body    = S("b",  fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#23323F"), leading=15, spaceAfter=5)
st_bullet  = S("bl", fontName="Helvetica", fontSize=10, textColor=colors.HexColor("#23323F"), leading=14)
st_cell    = S("c",  fontName="Helvetica", fontSize=9, textColor=colors.HexColor("#23323F"), leading=12)
st_cellb   = S("cb", fontName="Helvetica-Bold", fontSize=9, textColor=NAVY, leading=12)
st_cellh   = S("ch", fontName="Helvetica-Bold", fontSize=9, textColor=colors.white, leading=12)
st_link    = S("lk", fontName="Helvetica-Bold", fontSize=10, textColor=TEAL, leading=14)

def hr(c=LINE, w=1.0, sb=4, sa=8):
    return HRFlowable(width="100%", thickness=w, color=c, spaceBefore=sb, spaceAfter=sa)

def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(t, st_bullet), leftIndent=6, value="•") for t in items],
        bulletType="bullet", bulletColor=TEAL, bulletFontSize=9, leftIndent=12, spaceAfter=6)

story = []

# ---------- HEADER BANNER ----------
banner = Table([[
    Paragraph('<font color="#FFFFFF"><b>PORTFOLIO PROJECT SUMMARY</b></font>', S("x", fontSize=12, leading=15)),
]], colWidths=[170*mm])
banner.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), NAVY),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story += [banner, Spacer(1, 10)]

story.append(Paragraph("Ugbor Chidinma Benita", st_title))
story.append(Paragraph("Personal Portfolio Website &nbsp;|&nbsp; 5th-Year Medical Student (MBBS Candidate)", st_sub))
story.append(Paragraph("Abia State University (ABSU) &nbsp;&middot;&nbsp; ABSUTH, Aba, Nigeria &nbsp;&middot;&nbsp; MBBS 2019&ndash;2027", st_meta))
story.append(Paragraph("Document generated: 23 May 2026", st_meta))
story.append(hr(TEAL, 1.6, 8, 10))

# ---------- OVERVIEW ----------
story.append(Paragraph("Project Overview", st_h2))
story.append(Paragraph(
    "A world-class personal portfolio website was designed for Ugbor Chidinma Benita, a fifth-year medical "
    "student at Abia State University training at the Abia State University Teaching Hospital (ABSUTH). "
    "Three distinct design variants were built, version-controlled with Git, and published to GitHub. "
    "Because no photographs were available yet, every image area uses a clearly-marked placeholder.", st_body))

# ---------- INFO PROVIDED ----------
story.append(Paragraph("Information Provided", st_h2))
info = [
    [Paragraph("Full Name", st_cellb), Paragraph("Ugbor Chidinma Benita", st_cell)],
    [Paragraph("University", st_cellb), Paragraph("Abia State University (ABSU)", st_cell)],
    [Paragraph("Teaching Hospital", st_cellb), Paragraph("ABSUTH &mdash; Abia State University Teaching Hospital, Aba", st_cell)],
    [Paragraph("Programme", st_cellb), Paragraph("MBBS (Bachelor of Medicine, Bachelor of Surgery)", st_cell)],
    [Paragraph("Started / Year", st_cellb), Paragraph("2019 &middot; currently 5th year", st_cell)],
    [Paragraph("Expected Graduation", st_cellb), Paragraph("2027 (allowing for academic-calendar disruptions)", st_cell)],
]
t = Table(info, colWidths=[42*mm, 128*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,-1), SKY),
    ("ROWBACKGROUNDS", (1,0), (1,-1), [colors.white, MIST]),
    ("GRID", (0,0), (-1,-1), 0.5, LINE),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(t)

# ---------- DESIGNS ----------
story.append(Paragraph("The Three Designs", st_h2))
designs = [
    [Paragraph("Variant", st_cellh), Paragraph("Theme / Look", st_cellh), Paragraph("Highlights", st_cellh)],
    [Paragraph("Sky-Blue", st_cellb),
     Paragraph("Light sky-blue &amp; white, airy, serif headings (matches the reference template).", st_cell),
     Paragraph("Hero, &lsquo;Special Services&rsquo; cards, profile strip, portfolio gallery, tabbed Resume, appointment + contact.", st_cell)],
    [Paragraph("Classic", st_cellb),
     Paragraph("Navy / teal / gold, sophisticated and elegant.", st_cell),
     Paragraph("Hero with stats &amp; floating cards, About, Education timeline, Clinical Rotations, Skills, Achievements, Contact.", st_cell)],
    [Paragraph("Merged", st_cellb),
     Paragraph("Best of both &mdash; dark navy/teal hero + clean light sections + gold accents.", st_cell),
     Paragraph("Combines the dramatic hero, rotation cards &amp; animations of Classic with the tabbed Resume, services &amp; gallery of Sky-Blue.", st_cell)],
]
t = Table(designs, colWidths=[24*mm, 60*mm, 86*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), TEAL),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, MIST]),
    ("GRID", (0,0), (-1,-1), 0.5, LINE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(t)

# ---------- REPO & BRANCHES ----------
story.append(Paragraph("Git Repository &amp; Branches", st_h2))
story.append(Paragraph('Repository: <font color="#0B6E6E"><b>github.com/DavidUgbor/CHI</b></font> '
                       '(a dedicated repo, isolated from the home-folder Git tree).', st_body))
branches = [
    [Paragraph("Branch", st_cellh), Paragraph("Contents", st_cellh), Paragraph("Design", st_cellh)],
    [Paragraph("main", st_cellb), Paragraph("README.md", st_cell), Paragraph("Project overview", st_cell)],
    [Paragraph("sky-blue", st_cellb), Paragraph("index.html", st_cell), Paragraph("Light sky-blue (reference style)", st_cell)],
    [Paragraph("classic", st_cellb), Paragraph("index.html", st_cell), Paragraph("Navy / teal / gold (original)", st_cell)],
    [Paragraph("merged", st_cellb), Paragraph("index.html", st_cell), Paragraph("Best of both ✔", st_cell)],
]
t = Table(branches, colWidths=[30*mm, 50*mm, 90*mm])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), NAVY),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, MIST]),
    ("GRID", (0,0), (-1,-1), 0.5, LINE),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(t)
story.append(Spacer(1, 6))
story.append(Paragraph("Each design branch ships its variant as <b>index.html</b>. All branches were pushed to GitHub "
                       "and track <i>origin</i>. Commits use a local &lsquo;Chidinma&rsquo; author identity; no global Git config was changed.", st_body))

# ---------- FILE LOCATIONS ----------
story.append(Paragraph("Local File Locations", st_h2))
story.append(bullets([
    "<b>C:\\Users\\USER\\chidinma\\</b> &mdash; main Git repo (branches: main, sky-blue, classic, merged)",
    "<b>C:\\Users\\USER\\portfolio\\index.html</b> &mdash; original sky-blue source file",
    "<b>C:\\Users\\USER\\portfolio\\portfolio-classic.html</b> &mdash; original classic source file",
]))

# ---------- PLACEHOLDERS ----------
story.append(Paragraph("Placeholders To Fill In", st_h2))
story.append(Paragraph("These items are clearly marked in every design and should be replaced with real details:", st_body))
story.append(bullets([
    "Photographs &mdash; hero portrait, About portrait, and portfolio gallery thumbnails",
    "Specialty of interest (e.g. Internal Medicine / Paediatrics / Obs &amp; Gynae)",
    "Secondary school name",
    "Academic award name(s) and year(s)",
    "Leadership role(s) (e.g. Class Rep, Society Officer, Peer Tutor)",
    "Real research / case-study titles",
    "Contact details &mdash; phone number, email address, LinkedIn &amp; social links",
]))

# ---------- NEXT STEPS ----------
story.append(Paragraph("Suggested Next Steps", st_h2))
story.append(bullets([
    "Choose a primary design and set it as the repository&rsquo;s default branch on GitHub.",
    "Publish it free via <b>GitHub Pages</b> for a live URL (e.g. davidugbor.github.io/CHI).",
    "Add real photographs and replace all bracketed placeholders.",
    "Optionally wire the contact form to a real email service (e.g. Formspree).",
]))

story.append(hr(LINE, 0.8, 14, 6))
story.append(Paragraph("Prepared for Ugbor Chidinma Benita &middot; Personal Portfolio Project &middot; 2026", st_meta))

# ---- footer with page numbers ----
def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE); canvas.setLineWidth(0.5)
    canvas.line(20*mm, 14*mm, 190*mm, 14*mm)
    canvas.setFont("Helvetica", 8); canvas.setFillColor(MUTED)
    canvas.drawString(20*mm, 9*mm, "Ugbor Chidinma Benita — Portfolio Project Summary")
    canvas.drawRightString(190*mm, 9*mm, "Page %d" % doc.page)
    canvas.restoreState()

doc = SimpleDocTemplate("Portfolio-Project-Summary.pdf", pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=20*mm,
                        title="Portfolio Project Summary - Ugbor Chidinma Benita",
                        author="Chidinma Portfolio Project")
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("PDF created: Portfolio-Project-Summary.pdf")
