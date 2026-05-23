# -*- coding: utf-8 -*-
"""Build a readable EPUB 3 of the portfolio project summary (no external deps)."""
import zipfile, uuid, datetime

BOOK_ID = "urn:uuid:" + str(uuid.uuid4())
TODAY = "2026-05-23"
OUT = "Portfolio-Project-Summary.epub"

CSS = """
@charset "utf-8";
body { font-family: Georgia, 'Times New Roman', serif; color:#1A2332; line-height:1.6; margin:1em 1.2em; }
h1 { font-family:'Helvetica Neue',Arial,sans-serif; color:#0D2137; font-size:1.7em; line-height:1.2; margin:0.2em 0 0.1em; }
h2 { font-family:'Helvetica Neue',Arial,sans-serif; color:#0B6E6E; font-size:1.25em; margin:1.2em 0 0.4em; border-bottom:2px solid #C9A84C; padding-bottom:0.15em; }
.subtitle { color:#0B6E6E; font-size:1.05em; font-style:italic; margin:0 0 0.2em; }
.meta { color:#5A6B82; font-size:0.85em; margin:0 0 0.4em; }
p { margin:0.5em 0; }
a { color:#0B6E6E; }
.banner { background:#0D2137; color:#fff; font-family:'Helvetica Neue',Arial,sans-serif; font-weight:bold; letter-spacing:1px; padding:0.6em 0.8em; font-size:0.95em; }
table { border-collapse:collapse; width:100%; margin:0.8em 0; font-family:'Helvetica Neue',Arial,sans-serif; font-size:0.85em; }
th { background:#0B6E6E; color:#fff; text-align:left; padding:6px 8px; }
td { border:1px solid #D8E2EC; padding:6px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#F6FAFB; }
dt { font-family:'Helvetica Neue',Arial,sans-serif; font-weight:bold; color:#0D2137; margin-top:0.6em; }
dd { margin:0.1em 0 0.4em 0; color:#23323F; }
ul { margin:0.4em 0 0.8em 1.1em; padding:0; }
li { margin:0.3em 0; }
.tag { display:inline-block; background:#EAF3FB; color:#0B6E6E; border-radius:10px; padding:1px 8px; font-size:0.8em; font-family:'Helvetica Neue',Arial,sans-serif; }
hr { border:0; border-top:1px solid #D8E2EC; margin:1.4em 0; }
.footernote { color:#5A6B82; font-size:0.8em; font-style:italic; }
"""

def page(title, body):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><meta charset="utf-8"/><title>{title}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
{body}
</body></html>"""

# ---------- chapters ----------
c1 = page("Overview", """
<div class="banner">PORTFOLIO PROJECT SUMMARY</div>
<h1>Ugbor Chidinma Benita</h1>
<p class="subtitle">Personal Portfolio Website &#8212; 5th-Year Medical Student (MBBS Candidate)</p>
<p class="meta">Abia State University (ABSU) &#183; ABSUTH, Aba, Nigeria &#183; MBBS 2019&#8211;2027</p>
<p class="meta">Document generated: 23 May 2026</p>
<hr/>
<h2>Project Overview</h2>
<p>A world-class personal portfolio website was designed for Ugbor Chidinma Benita, a fifth-year medical
student at Abia State University training at the Abia State University Teaching Hospital (ABSUTH).
Three distinct design variants were built, version-controlled with Git, and published to GitHub.</p>
<p>Because no photographs were available yet, every image area uses a clearly-marked placeholder that can
be swapped for real photos later.</p>
""")

c2 = page("Information Provided", """
<h2>Information Provided</h2>
<dl>
<dt>Full Name</dt><dd>Ugbor Chidinma Benita</dd>
<dt>University</dt><dd>Abia State University (ABSU)</dd>
<dt>Teaching Hospital</dt><dd>ABSUTH &#8212; Abia State University Teaching Hospital, Aba</dd>
<dt>Programme</dt><dd>MBBS (Bachelor of Medicine, Bachelor of Surgery)</dd>
<dt>Started / Year</dt><dd>2019 &#183; currently 5th year</dd>
<dt>Expected Graduation</dt><dd>2027 (allowing for academic-calendar disruptions)</dd>
</dl>
""")

c3 = page("The Three Designs", """
<h2>The Three Designs</h2>
<table>
<tr><th>Variant</th><th>Theme / Look</th><th>Highlights</th></tr>
<tr><td><b>Sky-Blue</b></td><td>Light sky-blue &amp; white, airy, serif headings (matches the reference template).</td>
<td>Hero, &#8216;Special Services&#8217; cards, profile strip, portfolio gallery, tabbed Resume, appointment + contact.</td></tr>
<tr><td><b>Classic</b></td><td>Navy / teal / gold, sophisticated and elegant.</td>
<td>Hero with stats &amp; floating cards, About, Education timeline, Clinical Rotations, Skills, Achievements, Contact.</td></tr>
<tr><td><b>Merged</b></td><td>Best of both &#8212; dark navy/teal hero + clean light sections + gold accents.</td>
<td>Combines the dramatic hero, rotation cards &amp; animations of Classic with the tabbed Resume, services &amp; gallery of Sky-Blue.</td></tr>
</table>
""")

c4 = page("Git Repository & Branches", """
<h2>Git Repository &amp; Branches</h2>
<p>Repository: <b>github.com/DavidUgbor/CHI</b> (a dedicated repo, isolated from the home-folder Git tree).</p>
<table>
<tr><th>Branch</th><th>Contents</th><th>Design</th></tr>
<tr><td><b>main</b></td><td>README.md</td><td>Project overview</td></tr>
<tr><td><b>sky-blue</b></td><td>index.html</td><td>Light sky-blue (reference style)</td></tr>
<tr><td><b>classic</b></td><td>index.html</td><td>Navy / teal / gold (original)</td></tr>
<tr><td><b>merged</b></td><td>index.html</td><td>Best of both &#10004;</td></tr>
</table>
<p>Each design branch ships its variant as <b>index.html</b>. All branches were pushed to GitHub and track
<i>origin</i>. Commits use a local &#8216;Chidinma&#8217; author identity; no global Git config was changed.</p>
""")

c5 = page("Files & Placeholders", """
<h2>Local File Locations</h2>
<ul>
<li><b>C:\\Users\\USER\\chidinma\\</b> &#8212; main Git repo (branches: main, sky-blue, classic, merged)</li>
<li><b>C:\\Users\\USER\\portfolio\\index.html</b> &#8212; original sky-blue source file</li>
<li><b>C:\\Users\\USER\\portfolio\\portfolio-classic.html</b> &#8212; original classic source file</li>
</ul>
<h2>Placeholders To Fill In</h2>
<p>These items are clearly marked in every design and should be replaced with real details:</p>
<ul>
<li>Photographs &#8212; hero portrait, About portrait, and portfolio gallery thumbnails</li>
<li>Specialty of interest (e.g. Internal Medicine / Paediatrics / Obs &amp; Gynae)</li>
<li>Secondary school name</li>
<li>Academic award name(s) and year(s)</li>
<li>Leadership role(s) (e.g. Class Rep, Society Officer, Peer Tutor)</li>
<li>Real research / case-study titles</li>
<li>Contact details &#8212; phone number, email address, LinkedIn &amp; social links</li>
</ul>
""")

c6 = page("Next Steps", """
<h2>Suggested Next Steps</h2>
<ul>
<li>Choose a primary design and set it as the repository&#8217;s default branch on GitHub.</li>
<li>Publish it free via <b>GitHub Pages</b> for a live URL (e.g. davidugbor.github.io/CHI).</li>
<li>Add real photographs and replace all bracketed placeholders.</li>
<li>Optionally wire the contact form to a real email service (e.g. Formspree).</li>
</ul>
<hr/>
<p class="footernote">Prepared for Ugbor Chidinma Benita &#183; Personal Portfolio Project &#183; 2026</p>
""")

chapters = [
    ("c1.xhtml", "Overview", c1),
    ("c2.xhtml", "Information Provided", c2),
    ("c3.xhtml", "The Three Designs", c3),
    ("c4.xhtml", "Git Repository & Branches", c4),
    ("c5.xhtml", "Files & Placeholders", c5),
    ("c6.xhtml", "Next Steps", c6),
]

# ---------- nav.xhtml (EPUB3 TOC) ----------
nav_items = "\n".join(f'      <li><a href="{fn}">{title}</a></li>' for fn, title, _ in chapters)
nav = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><meta charset="utf-8"/><title>Contents</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
<nav epub:type="toc" id="toc"><h2>Contents</h2><ol>
{nav_items}
</ol></nav>
</body></html>"""

# ---------- toc.ncx (EPUB2 fallback) ----------
navpoints = "\n".join(
    f'    <navPoint id="np{i}" playOrder="{i}"><navLabel><text>{title}</text></navLabel><content src="{fn}"/></navPoint>'
    for i, (fn, title, _) in enumerate(chapters, 1))
ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{BOOK_ID}"/></head>
<docTitle><text>Portfolio Project Summary - Ugbor Chidinma Benita</text></docTitle>
<navMap>
{navpoints}
</navMap></ncx>"""

# ---------- content.opf ----------
manifest = '\n'.join(f'    <item id="{fn.replace(".","_")}" href="{fn}" media-type="application/xhtml+xml"/>' for fn,_,_ in chapters)
spine = '\n'.join(f'    <itemref idref="{fn.replace(".","_")}"/>' for fn,_,_ in chapters)
opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{BOOK_ID}</dc:identifier>
    <dc:title>Portfolio Project Summary - Ugbor Chidinma Benita</dc:title>
    <dc:creator>Chidinma Portfolio Project</dc:creator>
    <dc:language>en</dc:language>
    <dc:date>{TODAY}</dc:date>
    <meta property="dcterms:modified">{TODAY}T00:00:00Z</meta>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="css" href="style.css" media-type="text/css"/>
{manifest}
  </manifest>
  <spine toc="ncx">
{spine}
  </spine>
</package>"""

container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>"""

# ---------- write the zip ----------
with zipfile.ZipFile(OUT, "w") as z:
    # mimetype first, stored (uncompressed)
    z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
    z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/nav.xhtml", nav, compress_type=zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/toc.ncx", ncx, compress_type=zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/style.css", CSS, compress_type=zipfile.ZIP_DEFLATED)
    for fn, _, content in chapters:
        z.writestr(f"OEBPS/{fn}", content, compress_type=zipfile.ZIP_DEFLATED)

print("EPUB created:", OUT)
