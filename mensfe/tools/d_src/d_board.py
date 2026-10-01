from d_common import *
from d_home import board_row, T1

children = [
  board_row("b_causes", "med", "new", "Azoospermia", "#", "Obstructive and non-obstructive, sperm retrieval, next steps.",
            (T1, "topic.html", "dan_r", "2h ago")),
  board_row("b_causes", "med", "new", "Low sperm count", "#", "Count, motility and morphology, and what the numbers mean.",
            ("Second semen analysis came back better. Anyone else?", "#", "tomh", "Yesterday")),
  board_row("b_causes", "med", "read", "Varicocele", "#", "Diagnosis, surgery and recovery.",
            ("Varicocele repair: did your numbers improve?", "#", "[username]", "2 days ago")),
  board_row("b_causes", "med", "read", "Hormones and testosterone", "#", "Low T, FSH, LH and hormone treatment.",
            ("Anyone tried clomiphene for low testosterone?", "#", "[username]", "3 days ago")),
]

def trow(state, subj, href, starter, last, flags=(), pages=None, pinned=False, icon="bubble"):
    fl = ""
    for f in flags:
        if f == "pin": fl += f'<span class="flag f-pin">{I("pin", 13, 2.4)}Pinned</span>'
        if f == "lock": fl += f'<span class="flag f-lock">{I("lock", 13, 2.4)}Locked</span>'
        if f == "hot": fl += f'<span class="flag f-hot">{I("flame", 13, 2.4)}Hot</span>'
        if f == "new": fl += '<span class="flag f-new">New</span>'
    fl = f'<span class="flags">{fl}</span>' if fl else ""
    pg = f'<span class="pagelinks"><span class="sr">Topic pages: </span>« <a href="#">1</a> <a href="#">2</a> »</span>' if pages else ""
    tile_icon = "pin" if pinned else icon
    return f"""<tr{' class="pinned"' if pinned else ''}>
<td class="c-icon">{btile(tile_icon, "med", state)}</td>
<td><a class="t-sub" href="{href}">{subj}</a>{fl}<p class="t-by">Started by <a href="#">{starter}</a> {pg}</p></td>
<td class="c-rv"><span>[n] Replies</span><span>[n] Views</span></td>
{last_cell(*last)}
</tr>"""

topics = [
 trow("read", "READ FIRST: Board guidelines and useful links", "#", "Mensfe Team", ("READ FIRST: Board guidelines and useful links", "#", "Mensfe Team", "[date]"), flags=("pin", "lock"), pinned=True),
 trow("new", "Azoospermia: frequently asked questions", "#", "Mensfe Team", ("Azoospermia: frequently asked questions", "#", "mark_t", "Yesterday"), flags=("pin",), pinned=True, pages=True),
 trow("new", T1, "topic.html", "dan_r", (T1, "topic.html", "jo_partner", "2h ago"), flags=("new",)),
 trow("new", "Second semen analysis came back better. Anyone else?", "#", "tomh", ("Second semen analysis came back better. Anyone else?", "#", "tomh", "Yesterday")),
 trow("new", "Karyotype normal, still waiting on Y-microdeletion results", "#", "sam_k", ("Karyotype normal, still waiting on Y-microdeletion results", "#", "mark_t", "Yesterday")),
 trow("read", "High FSH and no sperm: what did your urologist suggest?", "#", "rich_w", ("High FSH and no sperm: what did your urologist suggest?", "#", "dan_r", "2 days ago")),
 trow("read", "Varicocele repair: did your numbers improve?", "#", "lee_b", ("Varicocele repair: did your numbers improve?", "#", "[username]", "2 days ago"), flags=("hot",), pages=True),
 trow("read", "Obstructive after vasectomy: PESA or reversal?", "#", "pete_m", ("Obstructive after vasectomy: PESA or reversal?", "#", "[username]", "3 days ago")),
 trow("read", "Anyone tried clomiphene for low testosterone?", "#", "gaz77", ("Anyone tried clomiphene for low testosterone?", "#", "[username]", "3 days ago")),
 trow("read", "Low motility on two tests: what changes helped you?", "#", "andy_c", ("Low motility on two tests: what changes helped you?", "#", "tomh", "4 days ago")),
 trow("read", "Klinefelter diagnosis in my thirties: where next?", "#", "[username]", ("Klinefelter diagnosis in my thirties: where next?", "#", "Mensfe Team", "5 days ago")),
 trow("read", "Morphology at 1%: should we be worried?", "#", "nick_s", ("Morphology at 1%: should we be worried?", "#", "[username]", "[date]")),
]

def toolbar(pos):
    return f"""<div class="toolbar">
  <nav class="pages" aria-label="Pages ({pos})">Pages: <span class="cur" aria-current="page">1</span><a href="#">2</a><a href="#">3</a><span class="gap">…</span><a href="#">[n]</a><a href="#" aria-label="Next page">{I("arrowr", 16)}</a></nav>
  <div class="btns">
    <a class="btn btn-gold" href="#">{I("plus", 17, 2.4)}New topic</a>
    <a class="btn" href="#">{I("bell", 17)}Notify</a>
    <a class="btn" href="#">{I("check", 17, 2.4)}Mark read</a>
  </div>
</div>"""

body = header("home", scope_board=True) + f"""
<main id="main" class="wrap">
{crumbs([("Mensfe Forum", "home.html"), ("Medical", "home.html#cat-medical"), ("Causes of male infertility", "board.html")])}

<section class="panel cat cat-med" aria-labelledby="board-h">
  <div class="bhead">
    {btile("b_causes", "med", "new", 28)}
    <div>
      <h1 class="page-title" id="board-h">Causes of male infertility</h1>
      <p>Azoospermia, low count, varicocele, hormones and more. Share test results, ask what they mean and compare notes with men who have had the same diagnosis.</p>
      <p class="b-mod">Moderators: <a href="#">Mensfe Team</a> · <a href="#">Medical panel</a></p>
    </div>
  </div>
</section>

<section class="panel cat cat-med" aria-labelledby="child-h">
  <div class="cat-h">
    <span class="ctile">{I("b_causes", 20)}</span>
    <h2 id="child-h">Child boards</h2>
    <div class="end"><button class="collapse" type="button" aria-expanded="true" aria-controls="child-t" aria-label="Collapse child boards">{I("chev", 20)}</button></div>
  </div>
  <table class="ftable" id="child-t">
  <caption class="sr">Child boards of Causes of male infertility</caption>
  <thead><tr><th scope="col" class="c-icon"><span class="sr">Status</span></th><th scope="col">Board</th><th scope="col" class="c-num">Topics</th><th scope="col" class="c-num">Posts</th><th scope="col" class="c-last">Last post</th></tr></thead>
  <tbody>
  {"".join(children)}
  </tbody>
  </table>
</section>

{toolbar("top")}

<section class="panel cat cat-med" aria-labelledby="topics-h">
  <div class="cat-h">
    <span class="ctile">{I("bubble", 20)}</span>
    <h2 id="topics-h">Topics</h2>
    <p class="sub">Sorted by last post</p>
  </div>
  <table class="ftable">
  <caption class="sr">Topics in Causes of male infertility, page 1</caption>
  <thead><tr><th scope="col" class="c-icon"><span class="sr">Status</span></th><th scope="col">Subject / Started by</th><th scope="col" class="c-rv">Replies / Views</th><th scope="col" class="c-last">Last post</th></tr></thead>
  <tbody>
  {"".join(topics)}
  </tbody>
  </table>
</section>

{toolbar("bottom")}

<section class="panel" aria-labelledby="tools-h">
  <h2 class="sr" id="tools-h">Topic icons and navigation</h2>
  <div class="split">
    <ul class="legend">
      <li>{btile("bubble", "med", "new", 16)}<span>New posts</span></li>
      <li>{btile("bubble", "med", "read", 16)}<span>No new posts</span></li>
      <li><span class="flag f-pin">{I("pin", 13, 2.4)}Pinned</span><span>Pinned topic</span></li>
      <li><span class="flag f-lock">{I("lock", 13, 2.4)}Locked</span><span>Locked topic</span></li>
      <li><span class="flag f-hot">{I("flame", 13, 2.4)}Hot</span><span>Hot topic (many replies)</span></li>
    </ul>
    <form class="jump" action="#">
      <label for="jumpto">Jump to:</label>
      <select id="jumpto" name="board">
        <optgroup label="Community"><option>General discussion</option><option>Let off some steam</option></optgroup>
        <optgroup label="Medical"><option selected>Causes of male infertility</option><option>&#8195;Azoospermia</option><option>&#8195;Low sperm count</option><option>&#8195;Varicocele</option><option>&#8195;Hormones and testosterone</option><option>Dealing with doctors</option><option>Dear Doctor (expert panel)</option></optgroup>
        <optgroup label="Feelings and relationships"><option>Men's reactions to infertility</option><option>Women's reactions to male infertility</option></optgroup>
        <optgroup label="Research"><option>Current research on male infertility</option></optgroup>
      </select>
      <button class="btn" type="submit">Go</button>
    </form>
  </div>
  <p class="browsing">Users browsing this board: [n] guests</p>
</section>
</main>
""" + FOOTER

html = head("Causes of male infertility | Mensfe Forum",
            "Forum board for azoospermia, low sperm count, varicocele, hormones and other causes of male infertility. Read topics free and ask men who have been there.") + body
