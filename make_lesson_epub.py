# -*- coding: utf-8 -*-
"""Build an EPUB lesson: how we built the portfolio + the prompts that drove it."""
import zipfile, uuid, html

BOOK_ID = "urn:uuid:" + str(uuid.uuid4())
TODAY = "2026-05-23"
OUT = "How-We-Did-It.epub"

def code(snippet):
    """Escape a code block safely for XHTML."""
    return '<pre class="code">' + html.escape(snippet.strip("\n")) + '</pre>'

def esc(t):
    return html.escape(t)

CSS = """
@charset "utf-8";
body { font-family: Georgia,'Times New Roman',serif; color:#1A2332; line-height:1.6; margin:1em 1.2em; }
h1 { font-family:'Helvetica Neue',Arial,sans-serif; color:#0D2137; font-size:1.6em; line-height:1.2; margin:0.2em 0 0.2em; }
h2 { font-family:'Helvetica Neue',Arial,sans-serif; color:#0B6E6E; font-size:1.25em; margin:1.1em 0 0.4em; border-bottom:2px solid #C9A84C; padding-bottom:0.15em; }
h3 { font-family:'Helvetica Neue',Arial,sans-serif; color:#0D2137; font-size:1.05em; margin:0.9em 0 0.3em; }
.subtitle { color:#0B6E6E; font-style:italic; margin:0 0 0.3em; }
.meta { color:#5A6B82; font-size:0.85em; margin:0 0 0.4em; }
p { margin:0.5em 0; }
a { color:#0B6E6E; }
.banner { background:#0D2137; color:#fff; font-family:'Helvetica Neue',Arial,sans-serif; font-weight:bold; letter-spacing:1px; padding:0.6em 0.8em; }
pre.code { background:#0D2137; color:#E5F3F3; font-family:'Courier New',monospace; font-size:0.8em; line-height:1.45; padding:0.7em 0.9em; border-radius:6px; white-space:pre-wrap; word-wrap:break-word; overflow-wrap:break-word; margin:0.6em 0; }
code { font-family:'Courier New',monospace; background:#EAF3FB; color:#0B6E6E; padding:0 3px; border-radius:3px; font-size:0.9em; }
table { border-collapse:collapse; width:100%; margin:0.7em 0; font-family:'Helvetica Neue',Arial,sans-serif; font-size:0.82em; }
th { background:#0B6E6E; color:#fff; text-align:left; padding:6px 8px; }
td { border:1px solid #D8E2EC; padding:6px 8px; vertical-align:top; }
tr:nth-child(even) td { background:#F6FAFB; }
ul,ol { margin:0.4em 0 0.8em 1.2em; padding:0; }
li { margin:0.3em 0; }
.prompt { background:#FCF6E4; border-left:4px solid #C9A84C; font-family:'Courier New',monospace; font-size:0.85em; color:#5a4a16; padding:0.5em 0.7em; margin:0.6em 0 0.3em; white-space:pre-wrap; }
.meaning { color:#0B6E6E; font-size:0.92em; margin:0.1em 0; }
.did { color:#23323F; font-size:0.92em; margin:0.1em 0 0.9em; }
.lbl { font-family:'Helvetica Neue',Arial,sans-serif; font-weight:bold; font-size:0.72em; letter-spacing:0.5px; text-transform:uppercase; }
.lbl-m { color:#0B6E6E; } .lbl-d { color:#8a6d1a; }
hr { border:0; border-top:1px solid #D8E2EC; margin:1.3em 0; }
.note { background:#EAF3FB; border-radius:6px; padding:0.6em 0.8em; font-size:0.9em; margin:0.7em 0; }
"""

def pg(title, body):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><meta charset="utf-8"/><title>{esc(title)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
{body}
</body></html>"""

# ===================================================================
# CH 1 - INTRO
# ===================================================================
c1 = pg("Introduction", """
<div class="banner">HOW WE DID IT &#8212; A LINE-BY-LINE LESSON</div>
<h1>Building Chidinma's Portfolio</h1>
<p class="subtitle">From an idea to three live designs, a Git repo, a PDF and an EPUB &#8212; explained step by step.</p>
<p class="meta">A teaching companion &#183; 23 May 2026</p>
<hr/>
<h2>What this book covers</h2>
<p>In one session we turned a simple idea &#8212; &#8220;build a portfolio for a 5th-year medical
student&#8221; &#8212; into a finished, version-controlled, published project. This book explains
<b>everything we did</b>, in order, in plain language:</p>
<ol>
<li><b>The prompts</b> &#8212; every instruction you gave Claude, what each one meant, and what Claude did.</li>
<li><b>Part 1 &#8211; The webpage</b> (HTML, CSS, JavaScript).</li>
<li><b>Part 2 &#8211; Git</b> (saving versions as branches).</li>
<li><b>Part 3 &#8211; GitHub</b> (publishing online).</li>
<li><b>Part 4 &#8211; The PDF</b> (Python + reportlab).</li>
<li><b>Part 5 &#8211; The EPUB</b> (a ZIP built by hand &#8212; this very file!).</li>
<li><b>Recap</b> &#8212; the whole journey on one page.</li>
</ol>
<div class="note">Tip: a website, a PDF and an EPUB are all just <b>text files in disguise</b>.
Once you see that, none of this is mysterious.</div>
""")

# ===================================================================
# CH 2 - THE PROMPTS
# ===================================================================
prompts = [
    ("lets build a world class personal portfolio for a medical student in 5th year. tell me what info you'll need and you'll use placeholders of the medical profession to fill the place for photos as she has no photos yet. read it back so i know you understand",
     "Start the project; ask what information is needed; use medical-themed placeholders for missing photos; confirm understanding first.",
     "Claude read the request back and listed exactly what info it needed (name, school, specialty, rotations, etc.), promising placeholders for everything missing."),
    ("ugbor chidinma benita / abia state university / abia state university teaching hospital absuth",
     "Here are the core facts: full name, university, and teaching hospital.",
     "Claude recorded the name (Ugbor Chidinma Benita), university (ABSU) and hospital (ABSUTH), then asked for the remaining details."),
    ("fill in the rest she started in 2019 now in 5th year",
     "Use smart placeholders for everything else; she began in 2019 and is now in 5th year.",
     "Claude calculated an expected graduation of 2027 and BUILT the first portfolio (navy/teal/gold) as index.html."),
    ("[shared a reference design image] use my info but follow this implicitly. read back so i understand.",
     "Match THIS reference template closely, but keep her real info. Confirm understanding first.",
     "Claude described the reference layout section-by-section, then rebuilt the site as a light sky-blue design to match it."),
    ("i said follow it implicitly. why do i still see elements of the one you did, like '5+ years in medicine'? does that appear anywhere in the one i sent?",
     "You added invented details that are NOT in my reference image. Remove them.",
     "Claude apologised and stripped out the fabricated stats (5+/6+/2027 counters, the 'My Journey' button) to match the reference faithfully."),
    ("lets see it on chrome",
     "Open the page in the Chrome browser.",
     "Claude launched Chrome pointed at the local index.html file."),
    ("retain yours in a seperate html",
     "Keep your original navy/teal/gold design too, in its own file.",
     "Claude saved the original design as portfolio-classic.html so both versions survived."),
    ("in a seperate branch called claown",
     "Put the work in a separate Git branch named 'claown'.",
     "Claude discovered the home folder was already a Git repo, warned about it, and began a SAFE dedicated repo instead. (You then redirected.)"),
    ("create a full repo called chidinma and put each variant in two branches",
     "Make a proper repo named 'chidinma'; put each design on its own branch.",
     "Claude created the 'chidinma' repo with a 'main' branch (README) plus 'sky-blue' and 'classic' branches, each holding its design as index.html."),
    ("push",
     "Upload it to GitHub.",
     "gh wasn't installed, so Claude asked how you wanted to authenticate; you chose to create the repo yourself."),
    ("https://github.com/DavidUgbor/CHI.git",
     "Here is the empty GitHub repo URL.",
     "Claude added it as the 'origin' remote and pushed all three branches; Git Credential Manager handled the login."),
    ("ok now on a new branch merge the best of both",
     "Create a new branch combining the strongest parts of both designs.",
     "Claude built a 'merged' branch: dark hero + rotations + animations (classic) plus tabbed resume + services + gallery (sky-blue), then pushed it."),
    ("take everything we did and put in pdf",
     "Produce a PDF documenting the whole project.",
     "Claude wrote a Python (reportlab) script that generated a branded one-page Portfolio-Project-Summary.pdf."),
    ("make it readable in epub",
     "Also produce an EPUB version.",
     "Claude hand-built a valid EPUB 3 (a specially-structured ZIP) with a clickable table of contents."),
    ("i meant teach how we did everything we did today line by line",
     "Explain, step by step, HOW it was all done.",
     "Claude taught the full walkthrough (HTML/CSS/JS, Git, GitHub, PDF, EPUB) in the chat."),
    ("epub now, also add how we did it / how we instructed claude, your prompts and all",
     "Put that lesson into an EPUB, and include the prompts themselves.",
     "Claude built THIS EPUB &#8212; the lesson plus this chapter of every prompt."),
]
rows = ""
for i,(p,m,d) in enumerate(prompts,1):
    rows += f'<h3>Prompt {i}</h3>\n'
    rows += f'<div class="prompt">{esc(p)}</div>\n'
    rows += f'<p class="meaning"><span class="lbl lbl-m">What it meant:</span> {m}</p>\n'
    rows += f'<p class="did"><span class="lbl lbl-d">What Claude did:</span> {d}</p>\n'
c2 = pg("The Prompts", f"""
<h2>Every Instruction You Gave</h2>
<p>Below is the whole conversation distilled to its instructions (lightly de-typo&#8217;d for clarity).
For each one: the prompt, what it meant, and what Claude did about it. This is the &#8220;how we drove the work&#8221; record.</p>
<hr/>
{rows}
""")

# ===================================================================
# CH 3 - PART 1 WEBPAGE
# ===================================================================
c3 = pg("Part 1: The Webpage", f"""
<h2>Part 1 &#8212; Building the Webpage</h2>
<p>A webpage is one text file (<code>index.html</code>) made of three languages:</p>
<table>
<tr><th>Language</th><th>Job</th><th>Analogy</th></tr>
<tr><td><b>HTML</b></td><td>Content &amp; structure</td><td>The skeleton</td></tr>
<tr><td><b>CSS</b></td><td>Styling (colour, layout, fonts)</td><td>The skin &amp; clothes</td></tr>
<tr><td><b>JavaScript</b></td><td>Behaviour (animation, clicks)</td><td>The muscles</td></tr>
</table>

<h3>The skeleton of every page</h3>
{code('''<!DOCTYPE html>          <!-- "this is modern HTML" -->
<html lang="en">         <!-- the whole document -->
<head> ... </head>       <!-- INVISIBLE setup: title, fonts, styles -->
<body> ... </body>       <!-- VISIBLE content the user sees -->
</html>''')}

<h3>Loading fonts &amp; icons (in the head)</h3>
{code('''<link href="https://fonts.googleapis.com/...Playfair+Display..." rel="stylesheet">
<link rel="stylesheet" href="https://...font-awesome...">''')}
<p>Line 1 borrows nice Google fonts. Line 2 loads Font Awesome, so writing
<code>&lt;i class="fa-solid fa-stethoscope"&gt;&lt;/i&gt;</code> shows a stethoscope icon.</p>

<h3>CSS variables &#8212; the master control panel</h3>
{code(''':root {
    --navy: #0D2137;
    --teal: #0B6E6E;
    --gold: #C9A84C;
}''')}
<p><code>--navy</code> is a nickname for a colour. Anywhere we write <code>color: var(--navy)</code>
it uses it. Change the nickname once and the whole site recolours &#8212; that&#8217;s why switching
navy &#8594; sky-blue was quick. (Hex codes like <code>#0D2137</code> are Red/Green/Blue in base-16.)</p>

<h3>Layout: Grid &amp; Flexbox</h3>
{code('''display: grid;
grid-template-columns: 1fr 1fr;   /* two equal columns */
display: flex;                    /* a row of items, easy to centre */''')}
<p><code>1fr</code> means &#8220;one fraction&#8221; of the space. The hero (text left, photo right) is a two-column grid.</p>

<h3>Responsive design (works on phones)</h3>
{code('''@media (max-width: 900px) {
    .hero-grid { grid-template-columns: 1fr; }  /* stack to 1 column */
    .hero-visual { display: none; }             /* hide photo on small screens */
}''')}
<p><code>@media</code> = &#8220;only apply when the screen is narrower than 900px.&#8221; Same file, looks good on desktop and phone.</p>

<h3>JavaScript &#8212; the behaviour</h3>
{code('''const nav = document.getElementById('navbar');
addEventListener('scroll', () => nav.classList.toggle('scrolled', scrollY > 50));''')}
<ol>
<li><code>getElementById('navbar')</code> &#8594; grab the nav bar.</li>
<li><code>addEventListener('scroll', ...)</code> &#8594; &#8220;each time the user scrolls, run this.&#8221;</li>
<li><code>classList.toggle('scrolled', scrollY &gt; 50)</code> &#8594; past 50px down, add the <code>scrolled</code> style (turns the bar white).</li>
</ol>
<p>The Resume <b>tabs</b> work the same way: a click hides all panels, then shows the chosen one.</p>
""")

# ===================================================================
# CH 4 - GIT
# ===================================================================
c4 = pg("Part 2: Git", f"""
<h2>Part 2 &#8212; Git (saving versions safely)</h2>
<p>Git is a &#8220;save-game system&#8221; for files: it records snapshots (<b>commits</b>) and lets you keep
parallel versions (<b>branches</b>) &#8212; no more <code>final_v2_REAL.html</code> copies.</p>
{code('''git init -b main           # start tracking this folder; first branch = main
git add README.md          # stage a file for the next snapshot
git commit -m "message"    # take the snapshot, with a description
git checkout -b sky-blue   # create + switch to a new branch
cp source.html ./index.html# (plain copy) put a design into this branch
git checkout main          # jump back to main
git checkout -b classic    # branch off again for the other design''')}
<p>Result: <code>main</code> holds the README; <code>sky-blue</code>, <code>classic</code> and later
<code>merged</code> each hold one design as <code>index.html</code>. One folder, many versions.</p>
<div class="note">We deliberately made a <b>dedicated</b> repo inside the <code>chidinma</code> folder,
because your whole home folder turned out to be a Git repo &#8212; committing there would have swept in
thousands of unrelated files.</div>
""")

# ===================================================================
# CH 5 - GITHUB
# ===================================================================
c5 = pg("Part 3: GitHub", f"""
<h2>Part 3 &#8212; GitHub (publishing online)</h2>
<p>GitHub is a website that hosts Git repositories.</p>
{code('''git remote add origin https://github.com/DavidUgbor/CHI.git
git push -u origin main sky-blue classic''')}
<ul>
<li><code>remote add origin ...</code> &#8594; &#8220;the online copy lives here; nickname it <i>origin</i>.&#8221;</li>
<li><code>push</code> &#8594; upload your commits.</li>
<li><code>-u</code> &#8594; remember the link so future pushes are just <code>git push</code>.</li>
<li>Listing branch names uploads them all at once.</li>
</ul>
<p>A secure <b>Git Credential Manager</b> popup handled the GitHub login &#8212; no password typed into commands.</p>
""")

# ===================================================================
# CH 6 - PDF
# ===================================================================
c6 = pg("Part 4: The PDF", f"""
<h2>Part 4 &#8212; The PDF (Python + reportlab)</h2>
<p>We wrote a small Python program that <i>draws</i> a PDF.</p>
{code('''from reportlab.platypus import SimpleDocTemplate, Paragraph, Table

story = []                                   # an empty list
story.append(Paragraph("Ugbor Chidinma Benita", st_title))
# ... keep appending tables, spacers, paragraphs in order ...

doc = SimpleDocTemplate("Summary.pdf", pagesize=A4)
doc.build(story)                             # writes the actual file''')}
<ul>
<li><code>story</code> is a <b>list</b>; we stack pieces (title, table, spacer) in reading order.</li>
<li><code>Paragraph</code> = text, <code>Table</code> = a table, <code>SimpleDocTemplate</code> = the document.</li>
<li><code>.build(story)</code> pours the list into an A4 page and saves it.</li>
</ul>
<p>The colours reused the same hex codes as the website, so the PDF matched the portfolio&#8217;s look.</p>
""")

# ===================================================================
# CH 7 - EPUB
# ===================================================================
c7 = pg("Part 5: The EPUB", f"""
<h2>Part 5 &#8212; The EPUB (a ZIP built by hand)</h2>
<p>The secret: <b>an EPUB is just a ZIP folder with a strict structure.</b> Rename <code>.epub</code> to
<code>.zip</code> and you can open it. Inside it needs:</p>
{code('''mimetype                  <- says "I am an epub" (MUST be 1st & uncompressed)
META-INF/container.xml    <- points to the package file
OEBPS/content.opf         <- manifest: lists files + reading order (the "spine")
OEBPS/nav.xhtml           <- the clickable Table of Contents
OEBPS/style.css           <- styling
OEBPS/c1.xhtml ...        <- each chapter is an XHTML page''')}
<p>The one rule people trip on:</p>
{code('''z.writestr("mimetype", "application/epub+zip",
           compress_type=zipfile.ZIP_STORED)   # first + UNCOMPRESSED''')}
<p>If <code>mimetype</code> isn&#8217;t the first entry and stored uncompressed, e-readers reject the file.
Everything else is compressed (<code>ZIP_DEFLATED</code>) to save space. This very book was built that way.</p>
""")

# ===================================================================
# CH 8 - RECAP
# ===================================================================
c8 = pg("Recap", """
<h2>The Whole Journey on One Page</h2>
<ol>
<li><b>HTML / CSS / JS</b> &#8212; built the portfolio in three designs.</li>
<li><b>Git</b> &#8212; saved each design as its own branch (main, sky-blue, classic, merged).</li>
<li><b>GitHub</b> &#8212; pushed all branches to <b>github.com/DavidUgbor/CHI</b>.</li>
<li><b>Python + reportlab</b> &#8212; generated a PDF project summary.</li>
<li><b>Python + zipfile</b> &#8212; hand-built EPUB summaries (including this lesson).</li>
</ol>
<h2>How you could repeat it</h2>
<ol>
<li>Write/clone the <code>index.html</code>.</li>
<li><code>git init</code>, then commit &amp; branch each version.</li>
<li>Create an empty GitHub repo, <code>git remote add origin</code>, <code>git push</code>.</li>
<li>(Optional) Run a Python script to produce PDF/EPUB docs.</li>
</ol>
<hr/>
<p class="meta">Prepared for Ugbor Chidinma Benita &#183; Personal Portfolio Project &#183; 2026</p>
""")

chapters = [
    ("c1.xhtml", "Introduction", c1),
    ("c2.xhtml", "The Prompts (How We Instructed Claude)", c2),
    ("c3.xhtml", "Part 1: The Webpage (HTML/CSS/JS)", c3),
    ("c4.xhtml", "Part 2: Git", c4),
    ("c5.xhtml", "Part 3: GitHub", c5),
    ("c6.xhtml", "Part 4: The PDF", c6),
    ("c7.xhtml", "Part 5: The EPUB", c7),
    ("c8.xhtml", "Recap", c8),
]

nav_items = "\n".join(f'      <li><a href="{fn}">{esc(t)}</a></li>' for fn,t,_ in chapters)
nav = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><meta charset="utf-8"/><title>Contents</title>
<link rel="stylesheet" type="text/css" href="style.css"/></head>
<body><nav epub:type="toc" id="toc"><h2>Contents</h2><ol>
{nav_items}
</ol></nav></body></html>"""

navpoints = "\n".join(
    f'    <navPoint id="np{i}" playOrder="{i}"><navLabel><text>{esc(t)}</text></navLabel><content src="{fn}"/></navPoint>'
    for i,(fn,t,_) in enumerate(chapters,1))
ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{BOOK_ID}"/></head>
<docTitle><text>How We Did It - Building Chidinma's Portfolio</text></docTitle>
<navMap>
{navpoints}
</navMap></ncx>"""

manifest = '\n'.join(f'    <item id="{fn.replace(".","_")}" href="{fn}" media-type="application/xhtml+xml"/>' for fn,_,_ in chapters)
spine = '\n'.join(f'    <itemref idref="{fn.replace(".","_")}"/>' for fn,_,_ in chapters)
opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{BOOK_ID}</dc:identifier>
    <dc:title>How We Did It - Building Chidinma's Portfolio</dc:title>
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

with zipfile.ZipFile(OUT, "w") as z:
    z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
    z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/nav.xhtml", nav, compress_type=zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/toc.ncx", ncx, compress_type=zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/style.css", CSS, compress_type=zipfile.ZIP_DEFLATED)
    for fn,_,content in chapters:
        z.writestr(f"OEBPS/{fn}", content, compress_type=zipfile.ZIP_DEFLATED)

print("EPUB created:", OUT, "with", len(chapters), "chapters")
