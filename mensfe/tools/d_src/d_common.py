
def svg(inner, size=20, sw=2, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{inner}</svg>')

P = {
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
 "chev": '<path d="m6 15 6-6 6 6"/>',
 "home": '<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/>',
 "book": '<path d="M4 5a2 2 0 0 1 2-2h14v15H6a2 2 0 0 0-2 2z"/><path d="M4 20a2 2 0 0 0 2 2h14v-4"/>',
 "flask": '<path d="M9 3h6M10 3v6l-5.4 9.2A2 2 0 0 0 6.3 21h11.4a2 2 0 0 0 1.7-2.8L14 9V3"/><path d="M7.5 15h9"/>',
 "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6"/><path d="M12 17.5h.01"/>',
 "login": '<path d="M14 4h4a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-4"/><path d="M10 16l4-4-4-4M14 12H4"/>',
 "useradd": '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M19 8v6M16 11h6"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "mega": '<path d="M3 10v4h3l7 5V5L6 10z"/><path d="M17 9a4 4 0 0 1 0 6"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5h.01"/>',
 "flame": '<path d="M12 3c.6 3.4 5.5 5.6 5.5 10.5a5.5 5.5 0 0 1-11 0c0-2.6 1.4-4 2-6 1.6 1 2.4 2.6 2.4 4.2C12 10 12.4 6.5 12 3z"/>',
 "pin": '<path d="M9 3h6l-1 6 3.5 3.5V15h-11v-2.5L10 9z"/><path d="M12 15v6"/>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 "bubble": '<path d="M5 4h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-8l-5 4v-4H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/><path d="M8 9h8M8 12.5h5"/>',
 "redirect": '<path d="M7 17 17 7M9 7h8v8"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
 "check": '<path d="m5 12 5 5 9-10"/>',
 "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
 "reply": '<path d="M9 7 4 12l5 5"/><path d="M4 12h10a6 6 0 0 1 6 6v1"/>',
 "quote": '<path d="M5 11h4v6H5zM5 11c0-3 1-5 4-6M14 11h4v6h-4zM14 11c0-3 1-5 4-6"/>',
 "print": '<path d="M7 9V3h10v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
 "unread": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3" fill="currentColor"/>',
 "flag": '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
 "logged": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "heart": '<path d="M12 20s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7a4.3 4.3 0 0 1 7.5 2.8C19.5 15.4 12 20 12 20z"/>',
 "hand": '<path d="M7 11V6a1.5 1.5 0 0 1 3 0v4M10 10V4.5a1.5 1.5 0 0 1 3 0V10M13 10V5.5a1.5 1.5 0 0 1 3 0V12M16 9.5a1.5 1.5 0 0 1 3 0V14a7 7 0 0 1-7 7h-1a6 6 0 0 1-5-2.8L3.6 15a1.5 1.5 0 0 1 2.4-1.8L7 14.5V11"/>',
 "same": '<circle cx="8" cy="9" r="3"/><circle cx="16" cy="9" r="3"/><path d="M2.5 20a5.5 5.5 0 0 1 11 0M10.5 20a5.5 5.5 0 0 1 11 0"/>',
 "thumb": '<path d="M7 11v9H4v-9zM7 11l4-8a2.5 2.5 0 0 1 2.5 3L13 10h6a2 2 0 0 1 2 2.3l-1.2 6A2 2 0 0 1 17.8 20H7"/>',
 "stats": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 "people": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2A5 5 0 0 1 21.5 19"/>',
 "shield": '<path d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "pen": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
 "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "doc": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
 "moon": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "arrowr": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "arrowl": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
 # board icons
 "b_general": '<path d="M3 5.5A2.5 2.5 0 0 1 5.5 3h8A2.5 2.5 0 0 1 16 5.5v5a2.5 2.5 0 0 1-2.5 2.5H9l-4 3v-3h0a2 2 0 0 1-2-2z"/><path d="M19 8.5h.5A1.5 1.5 0 0 1 21 10v5a2 2 0 0 1-2 2v3l-4-3h-3.5a2 2 0 0 1-2-2"/>',
 "b_steam": '<path d="M7.5 20h9.5a4 4 0 0 0 .6-7.96A5.5 5.5 0 0 0 7 11.2 4.4 4.4 0 0 0 7.5 20z"/><path d="M9 7c-1-1 0-2 0-3M12.5 6.5c-1-1 0-2 0-3M16 7c-1-1 0-2 0-3"/>',
 "b_causes": '<circle cx="10" cy="10" r="6.5"/><path d="m15 15 6 6"/><circle cx="9" cy="9" r="1.8"/><path d="M10.4 10.3c1.4.8 1.2 2.2 2.4 2.7"/>',
 "b_doctors": '<path d="M5 3H4v6a5 5 0 0 0 10 0V3h-1"/><path d="M9 14v1.5a5 5 0 0 0 10 0V13"/><circle cx="19" cy="11" r="2"/>',
 "b_deardoc": '<rect x="4" y="3" width="16" height="18" rx="3"/><path d="M12 8v7M8.5 11.5h7"/>',
 "b_men": '<path d="M12 20s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7a4.3 4.3 0 0 1 7.5 2.8C19.5 15.4 12 20 12 20z"/>',
 "b_women": '<circle cx="8.5" cy="8" r="3.2"/><circle cx="16.5" cy="9" r="2.6"/><path d="M2.5 20a6 6 0 0 1 12 0M14.5 14.3A4.8 4.8 0 0 1 21.5 19"/>',
 "b_research": '<path d="M9 3h6M10 3v6l-5.4 9.2A2 2 0 0 0 6.3 21h11.4a2 2 0 0 0 1.7-2.8L14 9V3"/><path d="M7.5 15h9"/>',
 "b_info": '<path d="M4 5a2 2 0 0 1 2-2h14v15H6a2 2 0 0 0-2 2z"/><path d="M4 20a2 2 0 0 0 2 2h14v-4M9 8h7M9 11.5h5"/>',
 "c_com": '<path d="M3 5.5A2.5 2.5 0 0 1 5.5 3h8A2.5 2.5 0 0 1 16 5.5v5a2.5 2.5 0 0 1-2.5 2.5H9l-4 3v-3a2 2 0 0 1-2-2z"/><path d="M19 8.5h.5A1.5 1.5 0 0 1 21 10v5a2 2 0 0 1-2 2v3l-4-3h-3.5a2 2 0 0 1-2-2"/>',
 "c_med": '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
}

def I(name, size=20, sw=2, cls=""):
    return svg(P[name], size, sw, cls)

LOGO_MARK = ('<svg width="34" height="34" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.8" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">'
             '<circle cx="13" cy="19" r="8"/><path d="M19 13 27 5M20 5h7v7"/></svg>')

def figure(x, y, s=1.0, sw=2.6):
    return (f'<g class="k-fig" transform="translate({x} {y}) scale({s})" stroke-width="{sw}" stroke-linecap="round" fill="none">'
            '<circle class="k-head" cx="0" cy="-29" r="3.3" stroke="none"/>'
            '<path d="M0-24.5 1.2-12.5"/><path d="M1.2-12.5-4.2 0M1.2-12.5 5.6-.5"/>'
            '<path d="M.2-21.5-4.2-14.5M.2-21.5 4.6-15.5"/></g>')

SCENE_D = (
 '<svg class="scene scene-d" viewBox="0 0 1440 140" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">'
 '<rect class="k-sky" width="1440" height="140"/>'
 '<rect class="k-s1" y="58" width="1440" height="16"/>'
 '<rect class="k-s2" y="74" width="1440" height="12"/>'
 '<rect class="k-s3" y="86" width="1440" height="14"/>'
 '<g class="k-star"><circle cx="560" cy="22" r="1.2"/><circle cx="640" cy="40" r="1"/><circle cx="905" cy="18" r="1.3"/><circle cx="980" cy="44" r="1"/><circle cx="1210" cy="26" r="1.2"/><circle cx="1330" cy="14" r="1"/><circle cx="1395" cy="48" r="1.1"/><circle cx="470" cy="12" r="1"/></g>'
 '<path class="k-land" d="M1040 100 1100 90 1150 94 1215 84 1280 92 1340 86 1440 92V100Z"/>'
 '<path class="k-land" d="M0 100V95L70 91 130 94 200 89 260 100Z"/>'
 '<circle class="k-sun" cx="760" cy="99" r="32"/>'
 '<rect class="k-sea1" y="100" width="1440" height="40"/>'
 '<rect class="k-sea2" y="110" width="1440" height="10"/>'
 '<rect class="k-sea3" y="120" width="1440" height="20"/>'
 '<rect class="k-hz" y="100" width="1440" height="1.5" opacity=".6"/>'
 '<g class="k-glint"><rect x="722" y="104" width="76" height="2.5" rx="1.2"/><rect x="734" y="110" width="52" height="2.5" rx="1.2" opacity=".8"/><rect x="744" y="116" width="32" height="2.5" rx="1.2" opacity=".6"/><rect x="752" y="122" width="16" height="2" rx="1" opacity=".45"/></g>'
 '<path class="k-shore" d="M0 140V129C220 122 470 121 700 124S1120 132 1440 124V140Z"/>'
 + figure(800, 126, 1.0) +
 '</svg>')

SCENE_M = (
 '<svg class="scene scene-m" viewBox="0 0 390 96" preserveAspectRatio="xMaxYMax slice" aria-hidden="true" focusable="false">'
 '<rect class="k-sky" width="390" height="96"/>'
 '<rect class="k-s1" y="48" width="390" height="10"/>'
 '<rect class="k-s2" y="58" width="390" height="9"/>'
 '<rect class="k-s3" y="67" width="390" height="9"/>'
 '<g class="k-star"><circle cx="250" cy="12" r="1"/><circle cx="300" cy="28" r="1"/><circle cx="372" cy="10" r="1"/></g>'
 '<path class="k-land" d="M230 76 260 71 290 73 320 69 350 72 390 70V76Z"/>'
 '<circle class="k-sun" cx="326" cy="75" r="19"/>'
 '<rect class="k-sea1" y="76" width="390" height="20"/>'
 '<rect class="k-sea2" y="81" width="390" height="6"/>'
 '<rect class="k-sea3" y="87" width="390" height="9"/>'
 '<rect class="k-hz" y="76" width="390" height="1" opacity=".6"/>'
 '<g class="k-glint"><rect x="304" y="78.5" width="44" height="1.6" rx=".8"/><rect x="312" y="82.5" width="28" height="1.6" rx=".8" opacity=".7"/><rect x="319" y="86.5" width="14" height="1.6" rx=".8" opacity=".5"/></g>'
 '<path class="k-shore" d="M0 96V92C90 89 200 89 280 90.5S360 92 390 89.5V96Z"/>'
 + figure(344, 91.5, 0.5, sw=3.4) +
 '</svg>')

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&amp;family=Source+Sans+3:wght@400;600;700&amp;display=swap" rel="stylesheet">')

def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
<style>
@@CSS@@
</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

TABS = [("home", "Home", "home.html", "home"), ("info", "Information", "article.html", "book"),
        ("research", "Research", "#", "flask"), ("help", "Help", "#", "help"),
        ("search", "Search", "#", "search"), ("login", "Login", "#", "login"), ("register", "Register", "#", "useradd")]

def header(current, scope_board=False):
    tabs = []
    for key, label, href, ic in TABS:
        cur = ' aria-current="page"' if key == current else ""
        cls = ' class="push"' if key == "login" else ""
        tabs.append(f'<li{cls}><a href="{href}"{cur}>{I(ic, 17)}{label}</a></li>')
    sel_all = "" if scope_board else " selected"
    sel_b = " selected" if scope_board else ""
    return f"""<header>
<div class="banner">
{SCENE_D}
{SCENE_M}
<div class="wrap banner-in">
  <div class="brand">
    <a class="logo" href="home.html" aria-label="Mensfe forum home">{LOGO_MARK}<span class="logo-word">mensfe</span></a>
    <p class="brand-line"><span class="walk">You'll never walk alone.</span> <span class="tagline">The men's fertility forum · since 2007</span></p>
  </div>
  <form class="search" role="search" action="#">
    <label class="sr" for="q">Search the forum</label>
    <input id="q" type="search" name="q" placeholder="Search topics and posts">
    <label class="sr" for="scope">Search in</label>
    <select id="scope" name="scope"><option{sel_all}>Entire forum</option><option{sel_b}>This board</option></select>
    <button class="btn btn-gold" type="submit">{I("search", 18, 2.4)}Search</button>
  </form>
</div>
</div>
<nav class="tabs" aria-label="Main">
<div class="wrap"><ul>
{chr(10).join(tabs)}
</ul></div>
</nav>
</header>
<div class="wrap">
<div class="userbar">
  <div class="ub-left">
    <span class="ub-av">{I("user", 20)}</span>
    <div class="ub-text">
      <p>Welcome, <strong>Guest</strong>. Please <a href="#">login</a> or <a href="#">register</a>.</p>
      <a class="small" href="#">Did you miss your activation email?</a>
    </div>
  </div>
  <div class="ub-btns"><a class="btn btn-sm" href="#">{I("login", 17)}Login</a><a class="btn btn-sm btn-gold" href="#">{I("useradd", 17)}Register</a></div>
  <div class="ub-right">
    @@THEME@@
    <p class="ub-when">[date, time]</p>
  </div>
</div>
<div class="news" role="note">
  <span class="news-tag">{I("mega", 16)}Announcement</span>
  <p>New to Mensfe? Read the <a href="#">new-member guide</a> and <a href="#">forum rules</a> before posting.</p>
</div>
</div>
"""

def crumbs(items):
    lis = []
    for i, (label, href) in enumerate(items):
        last = i == len(items) - 1
        if last and href:
            lis.append(f'<li><a href="{href}" aria-current="page">{label}</a></li>')
        elif last:
            lis.append(f'<li><span aria-current="page">{label}</span></li>')
        else:
            lis.append(f'<li><a href="{href}">{label}</a></li>')
    return f'<nav class="linktree" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'

FOOTER = f"""<footer class="foot">
<div class="wrap foot-in">
  <div>
    <a class="logo" href="home.html" aria-label="Mensfe forum home">{LOGO_MARK}<span class="logo-word">mensfe</span></a>
    <p class="foot-stats">[n] posts in [n] topics by [n] members · 6.5 million visits in 2025 · Latest member: <a href="#">[username]</a></p>
    <p class="foot-stats">Member of iCSI, International Consumer Support for Infertility · <a href="mailto:info@mensfe.net">info@mensfe.net</a></p>
  </div>
  <nav aria-label="Footer">
    <ul class="foot-links">
      <li><a href="#">Forum rules</a></li><li><a href="#">Privacy</a></li><li><a href="#">Terms</a></li>
      <li><a href="#">Contact</a></li><li><a href="#">About</a></li><li><a href="#">Patrons</a></li>
    </ul>
  </nav>
  <div class="foot-disc">
    <p><strong>Mensfe is peer support, not medical advice.</strong> It does not replace personal professional, legal or medical advice.</p>
    <p>&copy; 2007–2026 Mensfe</p>
  </div>
</div>
</footer>
</body>
</html>
"""

# ---------- helpers for tables ----------
CAT_OF = {"com": "cat-com", "med": "cat-med", "feel": "cat-feel", "res": "cat-res"}

def btile(icon, cat, state="read", size=22):
    """state: new | read | redir"""
    if state == "redir":
        return f'<span class="btile redir {CAT_OF[cat]}">{I("redirect", size)}<span class="sr">Redirect board</span></span>'
    dot = '<span class="dot"></span><span class="sr">New posts</span>' if state == "new" else '<span class="sr">No new posts</span>'
    cls = "btile" + ("" if state == "new" else " read")
    return f'<span class="{cls} {CAT_OF[cat]}">{I(icon, size)}{dot}</span>'

def last_cell(title, href, user, time):
    return (f'<td class="c-last"><span class="mlbl">Last post: </span><a class="lp-t" href="{href}">{title}</a> '
            f'<span class="lp-by">by <a href="#">{user}</a> · {time}</span></td>')
