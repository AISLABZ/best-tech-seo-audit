"""AIS LABZ SEO / AEO / GEO proposal for Lumos Dental & Aesthetic Clinic."""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether, NextPageTemplate, Preformatted)

OUT = sys.argv[1]
F = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("Sans", F + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Bold", F + "LiberationSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Sans-Italic", F + "LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Mono", F + "LiberationMono-Regular.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans-Italic", boldItalic="Sans-Bold")

NAVY = colors.HexColor("#0E2440")
TEAL = colors.HexColor("#167E7E")
TEAL_LT = colors.HexColor("#E3F1F1")
GOLD = colors.HexColor("#B8923A")
INK = colors.HexColor("#1D1D1F")
GREY = colors.HexColor("#5B5E66")
RULE = colors.HexColor("#D9DCE1")
ROW = colors.HexColor("#F5F6F8")
CRIT = colors.HexColor("#B42318")
HIGH = colors.HexColor("#C4570C")
MED = colors.HexColor("#A67C00")
GOOD = colors.HexColor("#1E7B34")

W, H = A4
M = 18 * mm

S = {}
def st(name, **kw):
    base = dict(fontName="Sans", fontSize=9.6, leading=14, textColor=INK, spaceAfter=5)
    base.update(kw)
    S[name] = ParagraphStyle(name, **base)
st("body")
st("lead", fontSize=11, leading=16.5, textColor=INK, spaceAfter=8)
st("small", fontSize=8.2, leading=11.5, textColor=GREY)
st("h1", fontName="Sans-Bold", fontSize=21, leading=26, textColor=NAVY, spaceBefore=0, spaceAfter=4)
st("kicker", fontName="Sans-Bold", fontSize=8.2, leading=11, textColor=TEAL, spaceAfter=2)
st("h2", fontName="Sans-Bold", fontSize=13, leading=17, textColor=NAVY, spaceBefore=10, spaceAfter=5)
st("h3", fontName="Sans-Bold", fontSize=10.4, leading=14, textColor=TEAL, spaceBefore=7, spaceAfter=3)
st("bullet", leftIndent=12, bulletIndent=2, spaceAfter=2.5)
st("cell", fontSize=8.3, leading=11.2, spaceAfter=0)
st("cellb", fontName="Sans-Bold", fontSize=8.3, leading=11.2, spaceAfter=0)
st("head", fontName="Sans-Bold", fontSize=8.1, leading=10.5, textColor=colors.white, spaceAfter=0)
st("kpi_v", fontName="Sans-Bold", fontSize=19, leading=22, textColor=NAVY, spaceAfter=0)
st("kpi_l", fontSize=7.8, leading=10.2, textColor=GREY, spaceAfter=0)
st("callout", fontSize=9.4, leading=13.6, textColor=NAVY, spaceAfter=0)
st("code", fontName="Mono", fontSize=7.1, leading=9.0, textColor=INK)

def P(t, s="body"): return Paragraph(t, S[s])
def B(items, s="bullet"): return [Paragraph(i, S[s], bulletText="–" if s == "sub" else "•") for i in items]
def h1(kicker, title): return [P(kicker.upper(), "kicker"), P(title, "h1"), Rule()]

class Rule(Table):
    def __init__(self, width=W - 2 * M, color=GOLD, thickness=1.4):
        super().__init__([[""]], colWidths=[width], rowHeights=[thickness + 6])
        self.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, -1), thickness, color),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))

def table(rows, widths, head=True, zebra=True, pad=4.2):
    data = []
    for i, r in enumerate(rows):
        data.append([c if not isinstance(c, str) else P(c, "head" if (head and i == 0) else "cell") for c in r])
    t = Table(data, colWidths=widths, repeatRows=1 if head else 0)
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
             ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
             ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE)]
    if head:
        style += [("BACKGROUND", (0, 0), (-1, 0), NAVY)]
    if zebra:
        for i in range(1 if head else 0, len(data)):
            if i % 2 == 0:
                style.append(("BACKGROUND", (0, i), (-1, i), ROW))
    t.setStyle(TableStyle(style))
    return t

def callout(text, color=TEAL, bg=TEAL_LT):
    t = Table([[P(text, "callout")]], colWidths=[W - 2 * M])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, -1), 3, color),
                           ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                           ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return t

def sev(level):
    c = {"Critical": CRIT, "High": HIGH, "Medium": MED, "Good": GOOD}[level]
    return Paragraph(f'<font color="{c.hexval().replace("0x", "#")}"><b>{level}</b></font>', S["cell"])

def kpis(items, cols=4):
    cw = (W - 2 * M) / cols
    cells = []
    for v, l, c in items:
        inner = Table([[Paragraph(f'<font color="{c.hexval().replace("0x", "#")}">{v}</font>', S["kpi_v"])],
                       [P(l, "kpi_l")]], colWidths=[cw - 8])
        inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 1),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
        cells.append(inner)
    rows = [cells[i:i + cols] for i in range(0, len(cells), cols)]
    t = Table(rows, colWidths=[cw] * cols)
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, RULE), ("INNERGRID", (0, 0), (-1, -1), 0.5, RULE),
                           ("BACKGROUND", (0, 0), (-1, -1), colors.white), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("LEFTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 8),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    return t

# ---------------------------------------------------------------- page furniture
def cover(c, doc):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(TEAL); c.rect(0, 0, 9 * mm, H, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(M + 4 * mm, H - 62 * mm, 34 * mm, 1.6 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("Sans-Bold", 15); c.drawString(M + 4 * mm, H - 40 * mm, "AiS LABZ")
    c.setFont("Sans", 9.5); c.setFillColor(colors.HexColor("#B9C6D6"))
    c.drawString(M + 4 * mm, H - 46 * mm, "Business Consultants")
    c.setFillColor(colors.white); c.setFont("Sans-Bold", 30)
    c.drawString(M + 4 * mm, H - 90 * mm, "Search Growth Proposal")
    c.setFont("Sans", 15); c.setFillColor(colors.HexColor("#D6DEE8"))
    c.drawString(M + 4 * mm, H - 101 * mm, "SEO  ·  AEO  ·  GEO  ·  Local Search  ·  UI/UX  ·  Google Ads")
    c.setFillColor(colors.white); c.setFont("Sans-Bold", 19)
    c.drawString(M + 4 * mm, H - 132 * mm, "Lumos Dental & Aesthetic Clinic")
    c.setFont("Sans", 11); c.setFillColor(colors.HexColor("#B9C6D6"))
    c.drawString(M + 4 * mm, H - 140 * mm, "lumosclinics.com  ·  Aspin Commercial Tower, Sheikh Zayed Road, Dubai")
    y = 52 * mm
    c.setStrokeColor(colors.HexColor("#30476A")); c.setLineWidth(0.6)
    c.line(M + 4 * mm, y + 16 * mm, W - M, y + 16 * mm)
    for i, (k, v) in enumerate([("Prepared by", "Salman Usman"), ("Date", "21 October 2026"),
                                ("Audit basis", "127 URLs crawled · Lighthouse lab test")]):
        x = M + 4 * mm + i * 58 * mm
        c.setFont("Sans", 8); c.setFillColor(colors.HexColor("#8FA3BC")); c.drawString(x, y + 8 * mm, k.upper())
        c.setFont("Sans-Bold", 10.5); c.setFillColor(colors.white); c.drawString(x, y + 2 * mm, v)
    c.setFont("Sans", 7.5); c.setFillColor(colors.HexColor("#8FA3BC"))
    c.drawString(M + 4 * mm, 20 * mm, "Confidential — prepared exclusively for Lumos Polyclinic L.L.C.")
    c.restoreState()

def inner(c, doc):
    c.saveState()
    c.setFillColor(NAVY); c.rect(0, H - 11 * mm, W, 11 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Sans-Bold", 8.2); c.drawString(M, H - 7 * mm, "AiS LABZ")
    c.setFont("Sans", 8.2); c.setFillColor(colors.HexColor("#B9C6D6"))
    c.drawRightString(W - M, H - 7 * mm, "Lumos Dental & Aesthetic Clinic  ·  Search Growth Proposal")
    c.setStrokeColor(RULE); c.setLineWidth(0.5); c.line(M, 13 * mm, W - M, 13 * mm)
    c.setFont("Sans", 7.6); c.setFillColor(GREY)
    c.drawString(M, 8.5 * mm, "Confidential · AiS LABZ Business Consultants · October 2026")
    c.drawRightString(W - M, 8.5 * mm, f"{doc.page}")
    c.restoreState()

doc = BaseDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=20 * mm, bottomMargin=19 * mm,
                      title="Lumos Clinics — SEO, AEO & GEO Growth Proposal", author="AiS LABZ Business Consultants",
                      subject="Search growth proposal for lumosclinics.com")
frame = Frame(M, 19 * mm, W - 2 * M, H - 39 * mm, id="f", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
doc.addPageTemplates([PageTemplate(id="cover", frames=[frame], onPage=cover),
                      PageTemplate(id="inner", frames=[frame], onPage=inner)])
TW = W - 2 * M
s = [NextPageTemplate("inner"), PageBreak()]

# ---------------------------------------------------------------- contents
s += h1("Contents", "What this proposal covers")
toc = [("1", "Overview & Objective"), ("2", "Executive Summary — Audit Scorecard"), ("3", "Our Services"),
       ("4", "Audit Findings (Technical, On-Page, Content, Local, AI)"), ("5", "Plan of Action — SEO Optimisation & Ranking Techniques"),
       ("6", "Keyword Clustering & Page Mapping"), ("7", "Answer Engine Optimisation (AEO)"),
       ("8", "Generative Engine Optimisation (GEO / AI Search)"), ("9", "Schema & Structured Data Plan"),
       ("10", "Sitemap & Site Architecture"), ("11", "Website Design & UI/UX Changes"),
       ("12", "Plan of Action — Google Business Profile"), ("13", "Plan of Action — Google Ads & GMB Ads (optional)"),
       ("14", "Healthcare Compliance & E-E-A-T"), ("15", "Measurement, KPIs & Reporting"),
       ("16", "Six-Month Roadmap"), ("17", "Why This Approach Works · Pricing · Terms")]
s.append(table([[f"<b>{n}</b>", t] for n, t in toc], [14 * mm, TW - 14 * mm], head=False))
s.append(Spacer(1, 14))
s.append(callout("<b>How to read this document.</b> Sections 2 and 4 describe what we measured on lumosclinics.com on "
                 "21 October 2026. Sections 5 to 16 set out what we will do about it, in priority order. Every audit "
                 "figure is measured directly from the live website, not estimated."))
s.append(PageBreak())

# ---------------------------------------------------------------- 1 overview
s += h1("Section 1", "Overview")
s.append(P("In the competitive Dubai dental and aesthetic market, your online presence is your digital storefront. "
           "Patients now discover clinics in three places: the traditional Google results page, the Google Map Pack, "
           "and — increasingly — AI answers in Google AI Overviews, ChatGPT, Gemini and Perplexity. AiS LABZ provides a "
           "comprehensive strategy designed to win visibility across all three, and to convert that visibility into "
           "high-value patient traffic.", "lead"))
s.append(P("Our goal is to move beyond simple clicks and focus on generating <b>confirmed consultations</b> for "
           "high-value treatments such as veneers and Hollywood smiles, dental implants, orthodontics, injectables, "
           "skin boosters and laser treatments."))
s.append(P("Objective", "h2"))
s.append(P("To transform the Lumos Clinics digital footprint into a conversion engine. We will lead the UI/UX "
           "improvements, execute an aggressive SEO, AEO and GEO strategy, and dominate local search through Google "
           "Business Profile and Ad management — so that Lumos is the first choice for patients searching on and "
           "around Sheikh Zayed Road, DIFC, Downtown, Business Bay and Trade Centre."))
s.append(P("What success looks like at six months", "h3"))
s += B(["Every treatment page indexed, eligible for featured snippets and AI Overviews, and mapped to one clear keyword cluster.",
        "Mobile page speed brought from failing to passing Core Web Vitals thresholds.",
        "Lumos cited by name when patients ask AI assistants for dental or aesthetic clinics on Sheikh Zayed Road.",
        "A growing, steady flow of Google reviews and a fully built-out Google Business Profile.",
        "Every call, WhatsApp click and online booking tracked to the channel and campaign that produced it."])
s.append(PageBreak())

# ---------------------------------------------------------------- 2 executive summary
s += h1("Section 2", "Executive summary — audit scorecard")
s.append(P("Lumos has an unusually strong base for a clinic website: 127 live pages, around 90 dedicated treatment "
           "pages, an SEO plugin already generating sitemaps and breadcrumbs, and Google Tag Manager installed. "
           "The problem is not volume of content — it is that a set of technical settings and structural issues are "
           "<b>preventing that content from ranking, appearing in AI answers and converting on mobile</b>.", "lead"))
s.append(Spacer(1, 4))
s.append(kpis([("28/100", "Lighthouse mobile performance (desktop 51)", CRIT),
               ("10.9s", "Mobile Largest Contentful Paint (target under 2.5s)", CRIT),
               ("12.7 MB", "Homepage weight on mobile; 5.9 MB is two videos", CRIT),
               ("2.0s", "Server response time (target under 0.8s)", HIGH),
               ("36", "Pages blocked from snippets & AI answers (nosnippet)", CRIT),
               ("18", "Treatments published twice at two URLs", CRIT),
               ("57", "Pages with zero or multiple H1 headings (of 127)", HIGH),
               ("29", "Pages missing a meta description", HIGH),
               ("80", "Page titles longer than 60 characters", MED),
               ("1,891", "Images without alt text", MED),
               ("0", "Blog articles published (blog page exists)", HIGH),
               ("0", "MedicalClinic / Dentist / Physician schema", HIGH)]))
s.append(Spacer(1, 10))
s.append(P("The five issues that matter most", "h2"))
s.append(table([
    ["#", "Issue", "Why it matters to Lumos"],
    ["1", "<b>36 pages carry a 'nosnippet' directive</b>, including the core 'Dentist in Dubai', 'Cosmetic Dentistry', "
          "'Aesthetic Treatments' and 'Anti-Aging' hub pages.",
     "Google cannot show a description, a featured snippet or use these pages in AI Overviews. These are the clinic's "
     "most commercially important pages."],
    ["2", "<b>Mobile performance is 28/100</b>; the homepage downloads 12.7 MB and takes 10.9s to show its main content.",
     "Most Dubai treatment searches happen on mobile. Slow pages lose rankings and lose patients before the booking button appears."],
    ["3", "<b>18 treatments exist at two URLs</b> (e.g. /orthodontics/ and /treatments/orthodontics/) with identical titles.",
     "The two versions compete against each other, splitting authority so neither ranks as well as one consolidated page."],
    ["4", "<b>OpenAI's GPTBot crawler is rate-limited (HTTP 429)</b> at the hosting CDN, while other AI crawlers are served normally.",
     "ChatGPT's training and knowledge crawler cannot reliably read the site, weakening Lumos's presence in ChatGPT answers."],
    ["5", "<b>No medical-entity schema, no doctor credentials, no blog</b>.",
     "Google and AI engines treat healthcare as 'Your Money or Your Life' content and reward demonstrable expertise. "
     "Today the site does not prove who the clinicians are."],
], [8 * mm, 78 * mm, TW - 86 * mm]))
s.append(PageBreak())

# ---------------------------------------------------------------- 3 services
s += h1("Section 3", "Our services")
s.append(P("Long-Term SEO, AEO & GEO Marketing Plan — results in 4 to 6 months", "h2"))
svc = [["Service line", "What it includes"],
       ["Organic SEO", "Technical fixes, on-page optimisation, content consolidation and ongoing ranking improvement."],
       ["Keyword optimisation", "Cluster-based keyword mapping so every treatment has one page, one intent and one primary keyword."],
       ["On-page optimisation", "Titles, meta descriptions, heading hierarchy, internal links, image alt text and calls to action."],
       ["Answer Engine Optimisation (AEO)", "Question-led content and FAQ structures that win featured snippets, People Also Ask and voice results."],
       ["Generative Engine Optimisation (GEO)", "Making Lumos citable by Google AI Overviews, ChatGPT, Gemini and Perplexity."],
       ["Schema & structured data", "MedicalClinic, Dentist, Physician, MedicalProcedure and FAQ markup across the site."],
       ["Backlink development", "Healthcare directories, Dubai lifestyle press, partnerships and digital PR."],
       ["Improved local rankings", "Map Pack visibility for Sheikh Zayed Road and the surrounding districts."],
       ["Google listing enhancement", "Full Google Business Profile build-out, review programme and weekly posting."]]
s.append(table(svc, [55 * mm, TW - 55 * mm]))
s.append(P("Website Development & UI/UX Solution", "h2"))
s.append(P("<b>Focus: Strategic Audit and Implementation Oversight.</b> Because your platform is already established "
           "(WordPress, Elementor, Rank Math, LatePoint booking), our role is to act as the <b>Strategic Bridge</b> "
           "between your brand goals and your development team. We provide the 'Blueprint for Conversion' that your "
           "developer will execute, so that no lead is lost."))
s += B(["<b>Conversion Rate Optimisation (CRO) Audit</b> — every step from landing page to confirmed booking.",
        "<b>User Journey Mapping</b> — separate journeys for dental, aesthetic, dermatology and wellness patients.",
        "<b>Aesthetic Content Strategy</b> — compliant before-and-after galleries, doctor profiles and treatment explainers.",
        "<b>Technical Implementation Guidance</b>:"])
st("sub", leftIndent=26, bulletIndent=16, spaceAfter=2.5)
s += B(["<b>Mobile Call-to-Action bar</b>: 'Call', 'WhatsApp' and 'Book' stay visible while patients scroll.",
        "<b>Page speed benchmarks</b>: specific load-time targets for your developer to meet (Section 11)."], "sub")
s += B(["<b>Form & booking optimisation</b> — fewer fields and fewer steps to increase digital enquiries."])
s.append(PageBreak())

# ---------------------------------------------------------------- 4 audit
s += h1("Section 4", "Audit findings")
s.append(P("Status: <b>completed for SEO</b>, <b>completed for AI search readiness</b>, <b>completed for website "
           "performance</b>, and <b>completed for Google Profile and Google Ads readiness</b>. All 127 URLs listed in "
           "the site's XML sitemaps were fetched and parsed on 21 October 2026. Performance figures are from a "
           "Lighthouse lab test of the homepage (mobile and desktop)."))
s.append(P("4.1 Technical SEO & performance", "h2"))
aw = [17 * mm, 62 * mm, TW - 79 * mm]
s.append(table([
    ["Severity", "Finding", "Evidence & recommended fix"],
    [sev("Critical"), "Mobile performance 28/100; LCP 10.9s; Total Blocking Time 8.8s; Speed Index 12.9s.",
     "Desktop scores 51 (LCP 1.9s). Fix: replace autoplay hero videos with a compressed poster image, defer scripts, "
     "reduce Elementor add-ons, enable page caching."],
    [sev("Critical"), "Homepage weighs 12.7 MB: two MP4 videos (5.9 MB), 114 images (4.2 MB), 11 font files (1.4 MB).",
     "Offscreen images could save 3.8 MB and responsive sizing a further 2.9 MB. Two icon-font plugins load 0.8 MB on their own."],
    [sev("High"), "Server response time 2.0s; CDN reports pages as uncached ('DYNAMIC').",
     "Enable full-page caching on Hostinger (LiteSpeed Cache or equivalent) and object caching. Target under 0.8s."],
    [sev("High"), "Page structure is very heavy: 4,806 DOM elements, 42 scripts and 47 stylesheets on the homepage.",
     "Simplify Elementor sections, remove unused widgets and plugins; target under 1,500 elements."],
    [sev("Medium"), "Accessibility 83/100 mobile; Best Practices 79/100.",
     "Contrast, link names and image alt text fixes (below) also lift these scores."],
    [sev("Good"), "HTTPS enforced; HTTP and www redirect correctly; every page returns 200 with a self-referencing canonical.",
     "No action — a sound foundation."],
], aw))
s.append(P("4.2 Indexing, duplication & crawl directives", "h2"))
s.append(table([
    ["Severity", "Finding", "Evidence & recommended fix"],
    [sev("Critical"), "36 pages use the robots directive 'nosnippet, noarchive'.",
     "Includes /dentist-in-dubai/, /cosmetic-dentistry-in-dubai/, /aesthetic-treatments-in-dubai/, "
     "/anti-aging-treatments-in-dubai/, /dermatology-skin-care-in-dubai/. Fix: remove 'nosnippet' in Rank Math so "
     "these pages can earn snippets and AI Overview citations."],
    [sev("Critical"), "18 treatments are published at both a root URL and a /treatments/ URL with identical titles.",
     "e.g. /orthodontics/ and /treatments/orthodontics/; /fotona-laser/ and /treatments/fotona-laser/. Fix: keep the "
     "stronger URL, 301-redirect the other, update internal links."],
    [sev("High"), "Further overlapping pages split the same topic.",
     "/root-canals/ vs /treatments/root-canal-in-dubai/; two 'dental-treatments-dubai' pages (one ends '-2'); two "
     "skin-booster pages; two Exosomes pages; 'hyperpigmentation' and 'pigmentation-hyperpigmentation'."],
    [sev("High"), "Malformed URLs contain the domain name inside the slug.",
     "/treatments/https-lumosclinics-com-tooth-extraction-in-dubai/, ...-tmj-surgery-in-dubai/, "
     "...-skin-boosters-hydration-quality-in-dubai/. Fix: clean slugs with 301 redirects."],
    [sev("High"), "Utility and account pages are in the XML sitemap.",
     "/my-account/, /customer-dashboard/, /latepoint/, /latepoint-booking/, /survey-page/, /sitemap/. Fix: noindex and remove."],
    [sev("High"), "The About page (/about/) — which holds the doctor team — is missing from the sitemap. "
                  "/contact/ and /contact-us/ return 404.",
     "Add /about/ to the sitemap and create a dedicated Contact page with map, hours and NAP."],
    [sev("Medium"), "Spelling error in a treatment URL and title: 'viginismus'.",
     "Correct to 'vaginismus' (the term patients search for) with a 301 redirect."],
], aw))
s.append(P("4.3 On-page SEO", "h2"))
s.append(table([
    ["Severity", "Finding", "Evidence & recommended fix"],
    [sev("High"), "34 pages have no H1; 23 pages have between 3 and 19 H1 headings each.",
     "Treatment templates tag 'Benefits', 'Step 1', 'Consultation' and related-treatment cards as H1. Fix: one H1 per page, "
     "H2/H3 for sections — a template-level fix that corrects ~90 pages at once."],
    [sev("High"), "29 pages have no meta description; 16 title tags are duplicated.",
     "Write unique, benefit-led descriptions (150–160 characters) with a clear call to action."],
    [sev("Medium"), "80 of 127 titles (63%) exceed 60 characters and are truncated in Google.",
     "The suffix 'Lumos Dental & Aesthetic Clinic In Dubai' uses 40 characters. Use '| Lumos Clinic Dubai' instead."],
    [sev("Medium"), "The phone number is marked up as an H2 heading many times per page.",
     "Convert to styled text or a button; headings should describe content."],
    [sev("Medium"), "1,891 images (13%) lack alt text.",
     "Descriptive alt text on treatment, doctor and clinic images; decorative images marked as such."],
], aw))
s.append(P("4.4 Content, local & AI readiness", "h2"))
s.append(table([
    ["Severity", "Finding", "Evidence & recommended fix"],
    [sev("High"), "The blog exists but has no published articles.",
     "No informational content to capture 'how much', 'does it hurt', 'how long' searches — the questions AI engines answer."],
    [sev("High"), "Doctors are named without qualifications, DHA licence numbers or individual profile pages.",
     "Build doctor profile pages with credentials and link each treatment to its treating clinician."],
    [sev("High"), "Structured data is generic (Organization, WebPage, Service). No MedicalClinic, Dentist, Physician, "
                  "address, geo-coordinates or opening hours.",
     "Deploy the schema plan in Section 9."],
    [sev("High"), "GPTBot (OpenAI) receives HTTP 429 'Too Many Requests'; ClaudeBot, PerplexityBot and OAI-SearchBot are served normally.",
     "Allow-list verified AI crawlers in the Hostinger CDN / security settings."],
    [sev("Medium"), "Brand name is inconsistent: 'Lumos Polyclinic llc.', 'Lumos Clinic', 'Lumos Dental & Aesthetic Clinic'.",
     "Standardise one public name across website, schema, Google, Apple, Bing and directories. A Turkish clinic named "
     "'Lumos Dental' also exists — consistent naming prevents AI engines confusing the two."],
    [sev("Medium"), "llms.txt exists but lists legal pages first, contains HTML entities and a spelling error ('Dermathology').",
     "Rewrite as a clean guide to services, doctors, location, hours and booking."],
    [sev("Medium"), "Schema 'sameAs' lists only Facebook; Instagram (@lumosclinic.ae) and directories are missing. No Arabic version or hreflang.",
     "Expand sameAs; plan an Arabic language layer for the top 20 treatments (Phase 2)."],
], aw))
s.append(PageBreak())

# ---------------------------------------------------------------- 5 SEO plan
s += h1("Section 5", "Plan of action — SEO optimisation & ranking techniques")
s.append(P("Keyword Research and Optimisation", "h2"))
s.append(P("A thorough analysis will identify high-impact, achievable keywords for Lumos Dental & Aesthetic Clinic in "
           "Dubai across English and Arabic. Keywords are organised into the twelve clusters in Section 6, and every "
           "cluster is assigned one primary page so that pages never compete with each other. Search volumes, "
           "difficulty and baseline rankings are captured in Month 1 from Google Search Console and Google Keyword "
           "Planner, and form the benchmark for monthly reporting."))
s.append(P("On-Page Optimisation", "h2"))
s += B(["Rewrite title tags to a consistent pattern: <i>[Treatment] in Dubai | [Benefit or 'From AED'] | Lumos Clinic</i>, under 60 characters.",
        "Unique meta descriptions for all 127 pages, written to raise click-through rate.",
        "Fix the treatment template so each page has exactly one H1 and a logical H2/H3 outline.",
        "Clean, keyword-led URLs; consolidate the 18 duplicate pairs and overlapping pages with 301 redirects.",
        "Descriptive alt text for all treatment, clinician and clinic images.",
        "A visible 'Medically reviewed by Dr. ___, DHA licence ___ · Last updated ___' line on every treatment page."])
s.append(P("Content Strategy", "h2"))
s += B(["Four expert articles per month answering real patient questions (cost, recovery, comparisons, suitability) — "
        "each linked to the relevant treatment page.",
        "An FAQ block of 5–8 questions on every treatment page, written for voice search and AI answers.",
        "Transparent 'from' pricing or price-range guides for veneers, implants, Botox, fillers, Profhilo and laser hair removal — "
        "the single most-searched question category in this market.",
        "Comparison pages: veneers vs. composite bonding, Profhilo vs. polynucleotides, Botox vs. fillers, Invisalign vs. braces."])
s.append(P("Technical SEO", "h2"))
s += B(["Remove 'nosnippet' and 'noarchive' from all indexable pages; noindex account, booking and survey pages.",
        "Implement the full schema plan (Section 9) and validate with Google's Rich Results Test.",
        "Fix broken links and redirect chains created during consolidation; regenerate and resubmit the XML sitemap.",
        "Bring mobile Core Web Vitals into the 'good' range (Section 11 benchmarks).",
        "Allow-list verified AI crawlers; register the site in Bing Webmaster Tools (Bing data feeds ChatGPT search and Copilot)."])
s.append(P("Ranking Improvement Techniques", "h2"))
s.append(table([
    ["Technique", "How we apply it at Lumos"],
    ["Hub-and-spoke internal linking", "Category hubs (Dentistry, Injectables, Skin, Laser, Hair, Wellness) link to every treatment; "
     "treatments link back to the hub, to related treatments and to the treating doctor."],
    ["Content consolidation", "Merge duplicate and overlapping pages so ranking signals concentrate on one strong URL per topic."],
    ["Click-through optimisation", "Titles and descriptions tested against Search Console data; pages ranking 5–15 are prioritised."],
    ["Topical authority", "Cluster articles that answer every question around a high-value treatment before moving to the next."],
    ["E-E-A-T signals", "Doctor profiles, credentials, medical review dates, DHA licence, real clinic photography."],
    ["Local relevance", "Area pages only where Lumos genuinely serves patients (DIFC, Downtown, Business Bay, Trade Centre) — "
     "each with unique travel, parking and landmark content, never thin duplicates."],
    ["Freshness", "Quarterly review of every treatment page; 'last updated' dates kept honest."],
], [50 * mm, TW - 50 * mm]))
s.append(P("Link Building", "h2"))
s += B(["Healthcare directories and booking platforms: Doctify, Okadoc, Vezeeta, Yellow Pages UAE, HiDubai, Connect.ae.",
        "Dubai lifestyle and wellness media (e.g. features, expert quotes and 'best of' round-ups).",
        "Partnerships with Sheikh Zayed Road and DIFC corporate wellness programmes, gyms and hotels.",
        "Expert commentary from Lumos doctors for health and beauty journalists (digital PR).",
        "Reclaiming unlinked brand mentions and fixing broken inbound links."])
s.append(P("Performance Tracking and Reporting", "h2"))
s.append(P("Performance is monitored through Google Analytics 4, Google Search Console, Bing Webmaster Tools and "
           "third-party SEO software. Monthly reports highlight organic traffic, keyword rankings, Map Pack "
           "position, AI-answer visibility, backlinks and — most importantly — calls, WhatsApp clicks and bookings. "
           "Adjustments are made each month based on the data."))
s.append(PageBreak())

# ---------------------------------------------------------------- 6 keyword clusters
s += h1("Section 6", "Keyword clustering & page mapping")
s.append(P("Keywords are grouped by the patient's intent, then mapped to one owning page. 'Priority' reflects "
           "commercial value and achievability for Lumos. Clusters marked <b>NEW PAGE</b> are gaps — demand the site does not "
           "currently serve."))
kw = [["Cluster", "Representative keywords", "Owning page", "Intent", "Priority"],
      ["1. Clinic & location", "dental clinic Sheikh Zayed Road; dentist near me Dubai; dental and aesthetic clinic Dubai; "
       "polyclinic Trade Centre; dentist DIFC", "Home + /dentist-in-dubai/", "Local / transactional", "Very high"],
      ["2. Cosmetic dentistry", "veneers Dubai; veneers price Dubai; Hollywood smile Dubai; Hollywood smile cost; "
       "E-max veneers; composite veneers; smile makeover", "/treatments/veneers-in-dubai/; /hollywood-smile-makeovers/",
       "Commercial", "Very high"],
      ["3. Implants & restorative", "dental implants Dubai; implant cost Dubai; All-on-4 Dubai; zygomatic implants; full mouth "
       "rehabilitation; crowns; dentures", "/dental-implants-in-dubai/ + sub-pages", "Commercial", "Very high"],
      ["4. Orthodontics", "Invisalign Dubai; clear aligners Dubai; braces cost Dubai; adult orthodontics",
       "/orthodontics/ + <b>NEW PAGE</b> Invisalign / clear aligners", "Commercial", "High"],
      ["5. General & emergency dentistry", "teeth cleaning Dubai; free dental check-up; root canal cost Dubai; tooth extraction; "
       "fillings; emergency dentist Dubai", "Existing pages + <b>NEW PAGE</b> emergency dentist", "Transactional", "High"],
      ["6. Teeth whitening", "teeth whitening Dubai; Zoom whitening price; laser teeth whitening", "/teeth-whitening-in-dubai/",
       "Commercial", "High"],
      ["7. Injectables", "Botox Dubai; anti-wrinkle injections price; lip fillers Dubai; jawline filler; liquid rhinoplasty; "
       "MD Codes; fat-dissolving injections", "/anti-wrinkle-injectables-in-dubai/; /lip-fillers-in-dubai/ etc.",
       "Commercial", "Very high"],
      ["8. Skin boosters & regenerative", "Profhilo Dubai; polynucleotides Dubai; Rejuran; Jalupro; PDRN salmon DNA; exosomes; skin boosters",
       "Existing treatment pages + hub", "Commercial / research", "High"],
      ["9. Laser & advanced skin", "laser hair removal Dubai; pico laser; Fotona; HydraFacial price Dubai; chemical peel; Cosmelan; "
       "acne scar treatment; melasma / pigmentation treatment", "Laser & skin pages (consolidated)", "Commercial", "High"],
      ["10. Hair restoration", "PRP hair treatment Dubai; exosomes for hair loss; hair loss treatment for women; hair mesotherapy",
       "/hair-loss-treatment-in-dubai/ hub", "Commercial", "Medium"],
      ["11. Wellness & IV therapy", "IV drip Dubai; glutathione drip; vitamin infusion; NAD+ drip; nutrition consultation",
       "/iv-drips-vitamin-infusions-in-dubai/", "Commercial", "Medium"],
      ["12. Intimate wellness", "vaginal rejuvenation Dubai; vaginismus treatment; labial fillers; intimate lightening; P-shot; "
       "snoring laser (NightLase)", "Consolidated /treatments/ pages", "Commercial (discreet)", "Medium"]]
s.append(table(kw, [31 * mm, 62 * mm, 44 * mm, 20 * mm, TW - 157 * mm], pad=2.6))
s.append(P("Supporting informational clusters (AEO & blog)", "h3"))
s.append(table([
    ["Question cluster", "Example queries", "Format"],
    ["Cost & pricing", "how much are veneers in Dubai; Hollywood smile price per tooth; Botox price Dubai", "Price guide + FAQ"],
    ["Suitability & safety", "are veneers permanent; is Profhilo safe; who should not get fillers", "Expert article + FAQ"],
    ["Comparisons", "veneers vs bonding; Invisalign vs braces; Profhilo vs polynucleotides; Botox vs fillers", "Comparison table"],
    ["Recovery & results", "how long do lip fillers last; laser hair removal sessions needed; implant healing time", "Step guide + FAQ"],
    ["Arabic-language demand", "Arabic searches for dental clinic, Hollywood smile, fillers and Botox in Dubai", "Arabic pages (Phase 2)"],
], [38 * mm, 98 * mm, TW - 136 * mm], pad=2.6))
s.append(PageBreak())

# ---------------------------------------------------------------- 7 AEO
s += h1("Section 7", "Answer Engine Optimisation (AEO)")
s.append(P("AEO earns Lumos the 'answer' position — featured snippets, People Also Ask boxes, voice assistant "
           "responses and Google AI Overviews. The single largest barrier today is technical: 36 pages, including the "
           "main dental and aesthetic hubs, instruct Google not to show any snippet from them.", "lead"))
s.append(callout("<b>Quick win:</b> removing the 'nosnippet' directive is a settings change in Rank Math that takes "
                 "minutes and immediately makes these pages eligible for snippets and AI Overview citations again.",
                 CRIT, colors.HexColor("#FBEDEC")))
s.append(Spacer(1, 6))
s.append(P("AEO techniques we will apply", "h2"))
s.append(table([
    ["Technique", "Implementation on lumosclinics.com"],
    ["Question-led headings", "H2s phrased the way patients ask: 'How much do veneers cost in Dubai?', 'Does Botox hurt?'"],
    ["Answer-first paragraphs", "A direct 40–60 word answer immediately below each question, followed by detail."],
    ["Structured FAQs", "5–8 FAQs per treatment page with FAQPage schema; questions sourced from Search Console, "
     "People Also Ask and front-desk enquiries."],
    ["Lists, steps & tables", "The existing 'Step 1–5' treatment journey re-tagged as an ordered list with H3s; "
     "price and comparison tables in HTML (not images)."],
    ["Price transparency", "'From AED ___' ranges where DHA rules permit — the most frequently asked question type."],
    ["Voice & conversational search", "Natural-language phrasing, local references (Sheikh Zayed Road, Trade Centre Metro) and opening-hours answers."],
    ["Snippet monitoring", "Monthly tracking of owned featured snippets and People Also Ask placements."],
], [48 * mm, TW - 48 * mm]))
s.append(P("Example — veneers page answer block", "h3"))
s.append(callout("<b>How much do veneers cost in Dubai?</b><br/>At Lumos Dental & Aesthetic Clinic, porcelain veneers "
                 "start from AED ___ per tooth and composite veneers from AED ___ per tooth. The final price depends "
                 "on the number of teeth, the material and whether gum contouring is needed. Your dentist confirms a "
                 "written quote after a consultation. <i>(Prices to be supplied by Lumos.)</i>", NAVY, ROW))
s.append(PageBreak())

# ---------------------------------------------------------------- 8 GEO
s += h1("Section 8", "Generative Engine Optimisation (GEO / AI search)")
s.append(P("Patients increasingly ask ChatGPT, Gemini, Perplexity and Google AI Mode questions such as "
           "<i>'Which clinic on Sheikh Zayed Road is good for veneers?'</i>. These engines recommend businesses they "
           "can crawl, clearly identify, and see corroborated by other trusted sources. GEO makes Lumos that business.", "lead"))
s.append(P("GEO workstreams", "h2"))
s.append(table([
    ["Workstream", "Actions", "Status today"],
    ["1. Crawl access", "Allow-list GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended and Bingbot at the CDN; "
     "keep robots.txt open to them.", "GPTBot blocked (429)"],
    ["2. Entity clarity", "One consistent brand name, address and phone everywhere; MedicalClinic schema with geo-coordinates "
     "(25.20896, 55.27250); full sameAs list.", "Inconsistent"],
    ["3. Machine-readable summary", "Rewrite llms.txt: who Lumos is, services by category, doctors, location, hours, booking links.",
     "Present but weak"],
    ["4. Citable content", "Clear facts AI engines can quote: prices, session counts, recovery times, doctor credentials, "
     "devices used (Fotona, PicoSure, Zoom).", "Partial"],
    ["5. Third-party corroboration", "Reviews on Google, Doctify and Okadoc; mentions in Dubai media and 'best clinic' lists; "
     "accurate Bing Places and Apple Business Connect listings.", "Minimal"],
    ["6. Freshness & authorship", "Dated, medically reviewed content with named clinician authors.", "Missing"],
    ["7. AI visibility tracking", "A fixed monthly panel of 30 patient prompts run across ChatGPT, Gemini, Perplexity and "
     "Google AI Overviews; we report mention rate, citation rate and competitors cited.", "Not measured"],
], [40 * mm, 100 * mm, TW - 140 * mm]))
s.append(P("Sample monitoring prompts", "h3"))
s += B(["Best dental clinic on Sheikh Zayed Road Dubai",
        "Where can I get a Hollywood smile in Dubai and how much does it cost?",
        "Recommended clinic for Profhilo or polynucleotides near DIFC",
        "Clinic in Dubai that does dentistry and aesthetics in one place",
        "Laser hair removal clinic near Trade Centre Metro"])
s.append(PageBreak())

# ---------------------------------------------------------------- 9 schema
s += h1("Section 9", "Schema & structured data plan")
s.append(P("Rank Math currently outputs generic Organization, WebSite, WebPage, Service and BreadcrumbList markup. "
           "We will replace this with a medical-entity graph that tells Google and AI engines exactly what Lumos is, "
           "where it is, who works there and what each treatment involves."))
s.append(table([
    ["Schema type", "Where", "Key properties"],
    ["MedicalClinic + Dentist", "Site-wide (homepage, contact)", "name, address, geo, telephone, openingHoursSpecification, "
     "medicalSpecialty, priceRange, hasMap, sameAs, logo, image"],
    ["Physician", "Each doctor profile", "name, medicalSpecialty, qualifications, memberOf, worksFor, image, DHA licence identifier"],
    ["MedicalProcedure / Service", "Each treatment page", "name, procedureType, bodyLocation, howPerformed, preparation, "
     "followup, offers (price range), provider"],
    ["MedicalWebPage", "Treatment & blog pages", "about, lastReviewed, reviewedBy (Physician), audience"],
    ["FAQPage", "Treatment pages with FAQs", "Question / acceptedAnswer pairs matching visible on-page FAQs"],
    ["BreadcrumbList", "All pages (exists)", "Keep; align with new category hierarchy"],
    ["VideoObject / ImageObject", "Treatment videos, galleries", "name, description, thumbnailUrl, uploadDate"],
    ["Article / BlogPosting", "Blog", "author (Physician), datePublished, dateModified, publisher"],
], [40 * mm, 40 * mm, TW - 80 * mm]))
s.append(P("Note: Google does not display star-rating rich results for reviews a business publishes about itself, so "
           "we will not mark up on-site testimonials as AggregateRating. Review strength is built on Google instead.", "small"))
s.append(P("Sample — site-wide MedicalClinic markup (abridged)", "h3"))
code = '''{
  "@context": "https://schema.org",
  "@type": ["MedicalClinic", "Dentist"],
  "@id": "https://lumosclinics.com/#clinic",
  "name": "Lumos Dental & Aesthetic Clinic",
  "legalName": "Lumos Polyclinic L.L.C.",
  "url": "https://lumosclinics.com/",
  "telephone": "+971 4 352 4140",
  "email": "info@lumosclinics.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Aspin Commercial Tower, Sheikh Zayed Road",
    "addressLocality": "Dubai",
    "addressCountry": "AE"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 25.20896, "longitude": 55.27250 },
  "medicalSpecialty": ["Dentistry", "Dermatology"],
  "openingHoursSpecification": [ "... to be confirmed by Lumos ..." ],
  "sameAs": [
    "https://www.instagram.com/lumosclinic.ae/",
    "https://www.facebook.com/p/Lumos-Dental-Aesthetic-Clinic-61573771378003/",
    "<Google Business Profile URL>", "<Doctify profile URL>"
  ]
}'''
ct = Table([[Preformatted(code, S["code"])]], colWidths=[TW])
ct.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), ROW), ("BOX", (0, 0), (-1, -1), 0.5, RULE),
                        ("LEFTPADDING", (0, 0), (-1, -1), 9), ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7)]))
s.append(ct)
s.append(PageBreak())

# ---------------------------------------------------------------- 10 sitemap
s += h1("Section 10", "Sitemap & site architecture")
s.append(P("The site's XML sitemap (generated by Rank Math) lists 127 URLs across a page sitemap and a treatments "
           "sitemap. It includes pages that should not be indexed, omits the About page, and exposes duplicate "
           "treatment URLs. We will restructure both the XML sitemap and the visible navigation around a clear "
           "category hierarchy."))
s.append(P("XML sitemap changes", "h2"))
s.append(table([
    ["Action", "URLs affected"],
    ["Remove & noindex", "/my-account/, /customer-dashboard/, /latepoint/, /latepoint-booking/, /survey-page/, /sitemap/ (HTML sitemap)"],
    ["Redirect & remove (duplicates)", "18 root-level treatment pages duplicated under /treatments/, plus overlapping pages listed in Section 4.2"],
    ["Fix slug & redirect", "Three /treatments/https-lumosclinics-com-.../ URLs; /viginismus/; /dental-treatments-dubai-2/"],
    ["Add", "/about/, new doctor profiles, new Contact page, category hubs, blog post sitemap, video sitemap"],
    ["Consolidate legal pages", "/terms/ and /terms-and-conditions/ into one URL"],
    ["Resubmit", "Google Search Console and Bing Webmaster Tools after each structural release"],
], [48 * mm, TW - 48 * mm]))
s.append(P("Proposed site architecture", "h2"))
arch = [["Level 1", "Level 2 (category hubs)", "Level 3 (examples)"],
        ["Home", "—", "—"],
        ["Dentistry", "Cosmetic · Implants & Restorative · Orthodontics · General & Emergency",
         "Veneers · Hollywood Smile · Whitening · Dental Implants · All-on-4 · Invisalign · Root Canal · Cleaning"],
        ["Aesthetics", "Injectables · Skin Boosters & Regenerative · Body",
         "Botox · Lip Fillers · Jawline · Profhilo · Polynucleotides · Rejuran · Fat Dissolving"],
        ["Dermatology & Laser", "Medical Dermatology · Laser · Facials & Peels",
         "Acne & Scars · Pigmentation · Pico Laser · Fotona · Laser Hair Removal · HydraFacial · Chemical Peels"],
        ["Hair", "Hair Restoration", "PRP · Exosomes for Hair · Mesotherapy"],
        ["Wellness", "IV Therapy · Intimate Wellness · Men's Health", "IV Drips · Vaginal Rejuvenation · P-Shot · NightLase"],
        ["Our Doctors", "One profile per clinician", "Dr. Ammar Zaki · Dr. Saleh Ibrahim · Dr. Rahul Patel · Dr. Shima · Dr. Lama Husein"],
        ["Prices & Offers", "Price guides by category", "Shine Rewards · seasonal offers"],
        ["Patient Guides (Blog)", "Dental · Aesthetic · Skin · Wellness", "Cost guides · comparisons · aftercare"],
        ["About · Contact · Book", "—", "Location, parking, Metro directions, hours, map, WhatsApp"]]
s.append(table(arch, [32 * mm, 62 * mm, TW - 94 * mm]))
s.append(P("URL convention: /dentistry/veneers-dubai/, /aesthetics/lip-fillers-dubai/ — short, readable and grouped "
           "by category. Where changing URLs would put existing rankings at risk, we keep the current URL and "
           "achieve the hierarchy through breadcrumbs and internal links.", "small"))
s.append(PageBreak())

# ---------------------------------------------------------------- 11 design
s += h1("Section 11", "Website design & UI/UX changes")
s.append(P("Today's main navigation offers only 'Home' and 'All Services'. A patient looking for a specific "
           "treatment, a doctor or a price has to scroll or search. The changes below are prioritised by their "
           "effect on bookings."))
s.append(table([
    ["Priority", "Change", "Rationale"],
    [sev("Critical"), "Sticky mobile action bar: Call · WhatsApp · Book", "Keeps conversion one tap away on every screen."],
    [sev("Critical"), "Replace the two autoplay hero videos (5.9 MB) with an optimised still image and a tap-to-play video",
     "Single largest cause of the 10.9s mobile load."],
    [sev("High"), "Mega-menu navigation by category (Section 10) plus 'Our Doctors', 'Prices' and 'Book'", "Faster path to the right treatment; stronger internal linking."],
    [sev("High"), "Trust strip above the fold: DHA licence, Google rating and review count, years in practice, technologies",
     "Healthcare patients decide on trust before price."],
    [sev("High"), "Doctor profile pages with photo, qualifications, languages and treatments performed", "E-E-A-T and patient confidence."],
    [sev("High"), "Treatment page template: one H1, answer-first intro, price range, steps, FAQs, doctor, before & after, CTA",
     "One template fix improves ~90 pages."],
    [sev("High"), "Booking flow: shorten the LatePoint journey; pre-select treatment from the page the patient came from",
     "Fewer steps mean more completed bookings."],
    [sev("Medium"), "Compliant before-and-after galleries with consent and disclaimers", "Strongest persuasion asset in aesthetics."],
    [sev("Medium"), "Dedicated Contact page: map, parking, Metro directions, hours, WhatsApp", "/contact/ currently returns 404."],
    [sev("Medium"), "Replace phone-number headings with buttons; fix contrast and link labels", "Accessibility (83/100) and clean structure."],
    [sev("Medium"), "Arabic language version for top treatments (Phase 2)", "Serves Arabic-speaking patients and Arabic search demand."],
], [17 * mm, 85 * mm, TW - 102 * mm]))
s.append(P("Page-speed benchmarks for your developer", "h2"))
s.append(table([
    ["Metric (mobile)", "Today", "Target"],
    ["Lighthouse performance score", "28", "70 or higher"],
    ["Largest Contentful Paint", "10.9 s", "2.5 s or less"],
    ["Total Blocking Time", "8,820 ms", "300 ms or less"],
    ["Server response (TTFB)", "2.0 s", "0.8 s or less"],
    ["Page weight (homepage)", "12.7 MB", "2.5 MB or less"],
    ["DOM elements", "4,806", "1,500 or fewer"],
    ["Cumulative Layout Shift", "0.00", "Keep below 0.1"],
], [70 * mm, 45 * mm, TW - 115 * mm]))
s.append(PageBreak())

# ---------------------------------------------------------------- 12 GBP
s += h1("Section 12", "Plan of action — Google Business Profile")
s.append(P("The Google Business Profile is the most influential factor for appearing in the Map Pack and on Google "
           "Maps. Our plan covers a full audit, a build-out of every available field, and a weekly operating rhythm."))
s.append(P("Profile audit & build-out", "h2"))
s += B(["<b>NAP consistency</b>: one public name, address (including unit number in Aspin Commercial Tower) and phone across "
        "Google, Apple Business Connect, Bing Places, Doctify, Okadoc, Salonist and directories.",
        "<b>Categories</b>: primary 'Dental clinic'; secondary categories such as 'Cosmetic dentist', 'Dental implants provider', "
        "'Orthodontist', 'Skin care clinic', 'Dermatologist' and 'Laser hair removal service' — only where the service is genuinely provided.",
        "<b>Services</b>: every treatment listed individually with a description and, where permitted, a 'from' price — "
        "from general dentistry to specific fillers and skin boosters.",
        "<b>Hours</b>: regular hours plus special hours for Ramadan, Eid and public holidays.",
        "<b>Links</b>: booking link and WhatsApp chat enabled; website link tagged with UTM codes so GBP traffic is measured separately.",
        "<b>Attributes</b>: accessibility, payment methods, languages spoken, appointment requirements.",
        "<b>Description</b>: 750-character description leading with location and specialties."])
s.append(P("Ongoing optimisation", "h2"))
s += B(["<b>Weekly posts</b>: clinic updates, treatment spotlights, compliant before-and-after highlights and monthly offers.",
        "<b>Photo programme</b>: fresh, authentic photos and short videos every week — clinic interior, team, equipment, building "
        "entrance and parking — tagged and named with location-relevant descriptions.",
        "<b>Review programme</b>: post-appointment WhatsApp and QR-code review requests; target a steady weekly flow rather than bursts; "
        "every review answered within 48 hours, with care taken never to confirm patient details in replies.",
        "<b>Location-based keywords</b>: services, posts and replies referencing Sheikh Zayed Road, Trade Centre, DIFC and Downtown naturally.",
        "<b>Spam & competitor monitoring</b>: watch for incorrect edits to the listing and report policy-violating competitor listings.",
        "<b>Map Pack rank tracking</b>: grid-based tracking of key searches across the surrounding districts, reported monthly."])
s.append(callout("<b>Gap we will close:</b> outside Google, Lumos has almost no review footprint — the Salonist listing shows "
                 "no reviews and Lumos does not appear on Doctify. Building verified reviews on these platforms feeds "
                 "both local rankings and AI recommendations."))
s.append(PageBreak())

# ---------------------------------------------------------------- 13 ads
s += h1("Section 13", "Plan of action — Google Ads & GMB Ads")
s.append(callout("<b>Optional service.</b> Google Ads management is not part of the monthly retainer and involves no "
                 "ad spend unless Lumos chooses to proceed. It is set out here so the clinic can add it later."))
s.append(Spacer(1, 6))
s.append(P("A Google Ads tag is already installed. Paid search delivers patient enquiries immediately while organic "
           "rankings build over 4 to 6 months, and its search-term data feeds directly into our SEO keyword strategy."))
s.append(table([
    ["Campaign", "Focus", "Notes"],
    ["Local Search & Maps Ads", "Ads inside Google Maps and the Local Map Pack", "Driven by the optimised GBP; location extensions."],
    ["High-intent dental", "Veneers price Dubai, Hollywood smile Dubai, dental implants cost Dubai, emergency dentist",
     "Separate ad groups per treatment, each landing on its own page."],
    ["High-intent aesthetics", "Botox Dubai, lip fillers Dubai, Profhilo Dubai, laser hair removal Dubai", "Offer-led ads within DHA rules."],
    ["Brand protection", "'Lumos clinic' and misspellings", "Low cost; prevents competitors capturing brand searches."],
    ["Remarketing", "Visitors who viewed treatment or price pages but did not book", "Display and YouTube; consultation-led messaging."],
], [40 * mm, 72 * mm, TW - 112 * mm]))
s.append(P("Conversion tracking", "h2"))
s += B(["Working with your developer, every call, WhatsApp click, form submission and LatePoint booking is tracked in GA4 and Google Ads.",
        "Call tracking for website and ad calls, so each enquiry is credited to the right campaign.",
        "Offline conversion import (attended consultations) so bidding optimises for real patients, not just clicks.",
        "Budget recommendations are finalised after Month 1 keyword and CPC research, and presented for your approval."])
s.append(callout("<b>Policy note:</b> Google restricts advertising for some sexual-health and intimate-wellness treatments. "
                 "These services are best grown through organic search and GBP rather than paid ads.", HIGH,
                 colors.HexColor("#FDF1E7")))
s.append(Spacer(1, 4))

# ---------------------------------------------------------------- 14 compliance
s += h1("Section 14", "Healthcare compliance & E-E-A-T")
s.append(P("Healthcare is a 'Your Money or Your Life' category: Google and AI engines hold medical content to a higher "
           "standard, and UAE regulators govern healthcare advertising. These items are often missed in SEO plans; we "
           "build them in from day one."))
s += B(["<b>DHA advertising rules</b>: all promotional content, offers and before-and-after imagery prepared to align with Dubai "
        "Health Authority requirements; claims such as 'Best in-class' reviewed and replaced with verifiable statements.",
        "<b>Clinician credentials</b>: every doctor's qualifications, specialty and DHA licence displayed and linked from treatments.",
        "<b>Medical review</b>: each treatment page and article carries a named medical reviewer and a review date.",
        "<b>Patient privacy</b>: review responses, testimonials and case studies handled in line with UAE data protection law and the clinic's "
        "Patient Data & Consent Policy; consent captured for all patient imagery.",
        "<b>Balanced information</b>: risks, contraindications and recovery described alongside benefits — a ranking signal and a regulatory expectation."])
s.append(PageBreak())

# ---------------------------------------------------------------- 15 KPIs
s += h1("Section 15", "Measurement, KPIs & reporting")
s.append(P("Month 1 establishes the baseline from Google Search Console, GA4, Google Business Profile Insights and the "
           "AI-visibility prompt panel. Targets below are what we will work towards and report against monthly."))
s.append(table([
    ["KPI", "Baseline (Oct 2026)", "Target by Month 6"],
    ["Pages blocked by 'nosnippet'", "36", "0 indexable pages"],
    ["Duplicate / overlapping treatment URLs", "18 pairs + 6 overlaps", "0"],
    ["Pages with exactly one H1", "70 of 127", "100%"],
    ["Pages with meta description", "98 of 127", "100%"],
    ["Mobile Lighthouse performance / LCP", "28 / 10.9 s", "70+ / 2.5 s or less"],
    ["Medical schema coverage (clinic, doctors, treatments)", "0%", "100%"],
    ["Published patient-guide articles", "0", "20+"],
    ["AI-assistant mention rate (30-prompt panel)", "Measured Month 1", "Month-on-month growth"],
    ["Organic clicks & non-brand keywords in top 10", "Measured Month 1", "Month-on-month growth"],
    ["Google reviews (count & velocity)", "Measured Month 1", "Steady weekly growth; 48-hour response"],
    ["Calls, WhatsApp clicks & bookings from organic + GBP", "Tracking set up Month 1", "Reported monthly by channel"],
], [74 * mm, 45 * mm, TW - 119 * mm]))
s.append(P("Monthly report contents", "h3"))
s += B(["Executive one-page summary: enquiries, bookings and cost per enquiry by channel.",
        "Rankings by keyword cluster, Map Pack grid, featured snippets and AI-answer visibility.",
        "Work completed, work planned, and decisions we need from Lumos."])
s.append(Spacer(1, 4))

# ---------------------------------------------------------------- 16 roadmap
s += h1("Section 16", "Six-month roadmap")
s.append(table([
    ["Phase", "Timing", "Key deliverables"],
    ["1. Foundation & quick wins", "Weeks 1–4",
     "Remove 'nosnippet'; noindex utility pages; allow-list AI crawlers; GA4 / Ads conversion tracking; Search Console & Bing "
     "setup; GBP audit and build-out; keyword baseline; caching and hero-video fix."],
    ["2. Consolidation & on-page", "Month 2",
     "Redirect duplicate and malformed URLs; treatment template fix (H1s, structure); titles and meta descriptions for all pages; "
     "MedicalClinic and Physician schema; new sitemap."],
    ["3. Content & AEO", "Months 3–4",
     "FAQs on top 30 treatments; price guides; doctor profiles; first 8–10 patient-guide articles; mega-menu and mobile CTA bar; "
     "directory citations (Doctify, Okadoc, Apple, Bing)."],
    ["4. Authority & GEO", "Months 5–6",
     "Digital PR and backlinks; review programme at full pace; llms.txt and entity work; comparison pages; Arabic content plan; "
     "AI-visibility optimisation from prompt-panel results."],
    ["Ongoing", "Monthly", "Four articles, weekly GBP posts and photos, review responses, rank and AI tracking, monthly report and strategy call."],
], [42 * mm, 24 * mm, TW - 66 * mm]))
s.append(PageBreak())

# ---------------------------------------------------------------- 17 why / pricing
s += h1("Section 17", "Why this approach works")
s += B(["<b>Collaboration, not competition:</b> we work <i>with</i> your existing developer, providing the strategy and specifications that turn the site into a revenue generator.",
        "<b>Data-driven decisions:</b> every recommendation in this proposal is backed by measured evidence from your live website.",
        "<b>Built for how patients search now:</b> one programme covering Google, the Map Pack and AI assistants.",
        "<b>Measurable growth:</b> a direct line from our work to calls, WhatsApp enquiries and booked consultations.",
        "Proven track record of delivering high ROI for service businesses.",
        "Expertise in tailored organic and paid media strategies.",
        "Commitment to transparency and measurable results."])
s.append(P("Moving forward", "h2"))
s.append(P("We are happy to discuss your needs and refine this proposal so that it aligns with your budget and "
           "objectives. Phase 1 quick wins can begin within one week of signing."))
s.append(P("Pricing Structure — Lumos Dental & Aesthetic Clinic", "h2"))
s.append(P("<b>Starting retainer: 500 AED</b>"))
s.append(table([
    ["Service", "Scope", "Price", "Total"],
    ["UI/UX Consultation", "1 website", "Free", "Free"],
    ["Monthly SEO, AEO, GEO & GMB Profile Optimisation", "1 website", "1,000 AED / month", "1,000 AED / month"],
], [70 * mm, 25 * mm, 45 * mm, TW - 140 * mm]))
s.append(P("Payment terms", "h3"))
s += B(["Billed monthly.", "Minimum 6-month commitment recommended.", "Upfront retainer paid on signing of the contract.",
        "No advertising spend is included or required under this retainer."])
s.append(P("Optional add-ons (if needed later)", "h3"))
s += B(["Additional landing pages and Arabic-language pages.", "Email and WhatsApp marketing campaigns.",
        "Content writing packages beyond four articles per month.",
        "Google Ads and Meta (Instagram / Facebook) ads management (Section 13), quoted separately if required."])
s.append(Spacer(1, 12))
s.append(P("We are confident that we can build a successful business together."))
s.append(Spacer(1, 14))
sig = Table([[P("Sincerely,<br/><br/><b>Salman Usman</b><br/>AiS LABZ Business Consultants"),
              P("Accepted for Lumos Polyclinic L.L.C.<br/><br/>_______________________________<br/>Name, signature & date")]],
            colWidths=[TW / 2, TW / 2])
sig.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
s.append(sig)

doc.build(s)
print("built", OUT)
