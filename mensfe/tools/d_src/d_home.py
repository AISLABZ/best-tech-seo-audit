from d_common import *

def board_row(icon, cat, state, name, href, desc, last, mods=None, children=None, redirect=False):
    extra = ""
    if children:
        NEWSR = '<span class="sr"> (new posts)</span>'
        links = "".join(f'<a href="#"><span class="cdot{" new" if n else ""}"></span>{c}{NEWSR if n else ""}</a>' for c, n in children)
        extra += f'<p class="b-child"><span>Child boards:</span>{links}</p>'
    if mods:
        extra += f'<p class="b-mod">Moderator: <a href="#">{mods}</a></p>'
    if redirect:
        stats = '<td class="c-num" colspan="2">Redirects: [n]</td>'
        lastc = '<td class="c-last"><span class="muted">Redirects to the Information section</span></td>'
    else:
        stats = ('<td class="c-num">[n]<span class="lbl"> topics</span></td>'
                 '<td class="c-num">[n]<span class="lbl"> posts</span></td>')
        lastc = last_cell(*last)
    return f"""<tr>
<td class="c-icon">{btile(icon, cat, "redir" if redirect else state)}</td>
<td><a class="b-name" href="{href}">{name}</a><p class="b-desc">{desc}</p>{extra}</td>
{stats}
{lastc}
</tr>"""

def category(cid, cat, cicon, title, rows):
    return f"""<section class="panel cat {CAT_OF[cat]}" aria-labelledby="{cid}">
<div class="cat-h">
  <span class="ctile">{I(cicon, 20)}</span>
  <h2 id="{cid}">{title}</h2>
  <div class="end"><button class="collapse" type="button" aria-expanded="true" aria-controls="{cid}-t" aria-label="Collapse {title}">{I("chev", 20)}</button></div>
</div>
<table class="ftable" id="{cid}-t">
<caption class="sr">Boards in {title}</caption>
<thead><tr><th scope="col" class="c-icon"><span class="sr">Status</span></th><th scope="col">Board</th><th scope="col" class="c-num">Topics</th><th scope="col" class="c-num">Posts</th><th scope="col" class="c-last">Last post</th></tr></thead>
<tbody>
{"".join(rows)}
</tbody>
</table>
</section>
"""

T1 = "Just diagnosed with non-obstructive azoospermia. Where do we start?"

cats = [
 category("cat-community", "com", "c_com", "Community", [
   board_row("b_general", "com", "new", "General discussion", "#", "Anything and everything about male fertility.",
             ("How do we tell our parents we are using a donor?", "#", "oakley", "Yesterday"), mods="Mensfe Team"),
   board_row("b_steam", "com", "read", "Let off some steam", "#", "Somewhere to vent when it all gets too much.",
             ("Another pregnancy announcement at work", "#", "[username]", "3 days ago")),
   board_row("b_info", "com", "redir", "Information guides", "article.html",
             "Plain-English guides to tests, causes and treatment, written for Mensfe members.", None, redirect=True),
 ]),
 category("cat-medical", "med", "c_med", "Medical", [
   board_row("b_causes", "med", "new", "Causes of male infertility", "board.html", "Azoospermia, low count, varicocele, hormones and more.",
             (T1, "topic.html", "dan_r", "2h ago"), mods="Mensfe Team",
             children=[("Azoospermia", True), ("Low count", True), ("Varicocele", False), ("Hormones", False)]),
   board_row("b_doctors", "med", "new", "Dealing with doctors", "#", "Appointments, clinics, tests and treatment.",
             ("Micro-TESE next month: what should I ask the urologist?", "#", "mark_t", "5h ago")),
   board_row("b_deardoc", "med", "read", "Dear Doctor (expert panel)", "#", "Questions answered by our medical panel.",
             ("Does a varicocele affect sperm DNA?", "#", "[username]", "4 days ago"), mods="Medical panel"),
 ]),
 category("cat-feelings", "feel", "b_men", "Feelings and relationships", [
   board_row("b_men", "feel", "new", "Men's reactions to infertility", "#", "How it feels, from the men living it.",
             ("Feeling like I have let her down", "#", "quiet_one", "2 days ago")),
   board_row("b_women", "feel", "read", "Women's reactions to male infertility", "#", "Partners share their side.",
             ("How do I support him without pushing?", "#", "jo_partner", "3 days ago")),
 ]),
 category("cat-research", "res", "b_research", "Research", [
   board_row("b_research", "res", "read", "Current research on male infertility", "#", "New studies, trials and news.",
             ("Discussion thread: recent papers on sperm retrieval", "#", "Mensfe Team", "5 days ago")),
 ]),
]

recent = [
 (T1, "topic.html", "Causes of male infertility", "board.html", "dan_r", "2h ago"),
 ("Micro-TESE next month: what should I ask the urologist?", "#", "Dealing with doctors", "#", "mark_t", "5h ago"),
 ("How do we tell our parents we are using a donor?", "#", "General discussion", "#", "oakley", "Yesterday"),
 ("Second semen analysis came back better. Anyone else?", "#", "Causes of male infertility", "board.html", "tomh", "Yesterday"),
 ("Feeling like I have let her down", "#", "Men's reactions to infertility", "#", "quiet_one", "2 days ago"),
]
recent_rows = "".join(f"""<tr>
<td class="c-first"><a class="t-sub" href="{h}">{t}</a></td>
<td class="c-meta"><span class="lbl">Board: </span><a href="{bh}">{b}</a></td>
<td class="c-meta"><span class="lbl">by </span><a href="#">{u}</a></td>
<td class="c-meta c-when">{tm}</td>
</tr>""" for t, h, b, bh, u, tm in recent)

trend = [
 ("med", "b_causes", T1, "topic.html", "Causes of male infertility"),
 ("med", "b_doctors", "Micro-TESE next month: what should I ask the urologist?", "#", "Dealing with doctors"),
 ("com", "b_general", "How do we tell our parents we are using a donor?", "#", "General discussion"),
 ("feel", "b_men", "Feeling like I have let her down", "#", "Men's reactions"),
]
trend_html = "".join(f'<li><a class="chip {CAT_OF[c]}" href="{h}"><span class="ctile">{I(ic, 15)}</span>{t} <small>{b}</small></a></li>' for c, ic, t, h, b in trend)

stack = "".join(f'<span class="av av-{c}" aria-hidden="true">{i}</span>' for i, c in
                [("DR", "1"), ("MT", "2"), ("OA", "4"), ("TH", "6"), ("QO", "5"), ("JP", "7")])

body = header("home") + f"""
<main id="main" class="wrap">
{crumbs([("Mensfe Forum", "home.html")])}
<div class="idx-intro">
  <h1 class="page-title">Mensfe Forum</h1>
  <p>A free, anonymous peer-support forum for men facing infertility, and the partners who stand with them. Read any board without an account.</p>
</div>

<section class="notice" aria-labelledby="newhere">
  <div class="notice-h">{I("info", 22)}<h2 id="newhere">New here?</h2></div>
  <ol class="steps">
    <li><span class="stepn" aria-hidden="true">1</span><span><strong>Pick an anonymous username.</strong> Registering is free and nobody needs your real name.</span></li>
    <li><span class="stepn" aria-hidden="true">2</span><span><strong>Say hello in <a href="#">General discussion</a>.</strong> Share as much or as little as you like.</span></li>
    <li><span class="stepn" aria-hidden="true">3</span><span><strong>Ask anything.</strong> Someone here has usually been through it. Not ready? Just read.</span></li>
  </ol>
  <p class="notice-foot"><a href="#">New-member guide</a> · <a href="#">Forum rules</a></p>
</section>

<section class="trend" aria-labelledby="trend-h">
  <h2 class="trend-l" id="trend-h">{I("flame", 16)}Trending now</h2>
  <ul>{trend_html}</ul>
</section>

{"".join(cats)}

<section class="panel" aria-labelledby="legend-h">
  <h2 class="sr" id="legend-h">Board icon legend</h2>
  <ul class="legend">
    <li>{btile("b_general", "com", "new", 16)}<span>New posts</span></li>
    <li>{btile("b_general", "com", "read", 16)}<span>No new posts</span></li>
    <li>{btile("b_general", "com", "redir", 16)}<span>Redirect board</span></li>
  </ul>
</section>

<section class="panel cat cat-gold" aria-labelledby="recent-h">
  <div class="cat-h">
    <span class="ctile">{I("bubble", 20)}</span>
    <h2 id="recent-h">Recent posts</h2>
    <div class="end"><a class="btn btn-sm" href="#">View all</a></div>
  </div>
  <table class="ftable plain">
  <caption class="sr">The five most recent posts on the forum</caption>
  <thead><tr><th scope="col">Topic</th><th scope="col">Board</th><th scope="col">Started by</th><th scope="col">When</th></tr></thead>
  <tbody>
  {recent_rows}
  </tbody>
  </table>
</section>

<section class="panel cat cat-gold" aria-labelledby="ic-h">
  <div class="cat-h">
    <span class="ctile">{I("stats", 20)}</span>
    <h2 id="ic-h">Info center</h2>
  </div>
  <div class="ic-grid">
    <div class="ic">
      <h3>{I("stats", 18)}Forum stats</h3>
      <p class="big">6.5 million visits in 2025</p>
      <p>[n] posts in [n] topics by [n] members.</p>
      <p>Latest member: <a href="#">[username]</a></p>
      <p><a href="#">View the most recent posts</a> · <a href="#">More stats</a></p>
    </div>
    <div class="ic">
      <h3>{I("people", 18)}Online now</h3>
      <div class="stack" aria-hidden="true">{stack}</div>
      <p>[n] guests, [n] members (most online today: [n])</p>
      <p class="names">Members: <a href="#">dan_r</a>, <a href="#">mark_t</a>, <a href="#">oakley</a>, <a href="#">tomh</a>, <a href="#">quiet_one</a>, <a href="#">jo_partner</a></p>
      <p>Users active in the past 15 minutes.</p>
    </div>
    <div class="ic">
      <h3>{I("shield", 18)}Who runs Mensfe</h3>
      <p>Founded by <strong>Pip Reilly</strong>, a professional fertility counsellor with over 15 years' experience with fertility charities, and <strong>Rob Barlow</strong>, a medical scientist diagnosed with azoospermia more than 25 years ago.</p>
      <p>Pip's book: <a href="https://www.amazon.co.uk/dp/B0G8LX5FBJ">A Journey Through Male Infertility: Stronger Together</a>.</p>
      <p>Member of iCSI, International Consumer Support for Infertility.</p>
    </div>
  </div>
</section>
</main>
""" + FOOTER

html = head("Mensfe Forum | Men's fertility and male infertility support forum since 2007",
            "Mensfe is a free, anonymous peer-support forum for men facing infertility and their partners. Browse boards on causes, doctors, feelings and research. Since 2007.") + body
