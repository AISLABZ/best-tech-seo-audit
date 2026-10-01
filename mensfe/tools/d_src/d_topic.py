from d_common import *
from d_home import T1

def pips(n):
    return '<span class="pips" aria-hidden="true">' + "".join('<i class="f"></i>' if i < n else '<i></i>' for i in range(5)) + '</span>'

def post(idx, user, ini, avc, online, rank, rank_cls, npips, location, body, reacts, sig=None, op=False, group=None, alt=False):
    subj = T1 if idx == 0 else "Re: " + T1
    when = "« on: [date, time] »" if idx == 0 else f"« Reply #{idx} on: [date, time] »"
    status = '<span class="on"></span>' if online else '<span class="off"></span>'
    status_sr = "Online" if online else "Offline"
    opb = '<span class="op" title="Original poster">OP</span>' if op else ""
    grp = f'<span class="rank rank-partner">{group}</span>' if group else ""
    sig_html = f'<p class="sig">{sig}</p>' if sig else ""
    rk = "".join(f'<button class="rchip" type="button" aria-pressed="false">{I(ic, 16)}{label} <span>{n}</span></button>' for ic, label, n in reacts)
    return f"""<article class="post{' alt' if alt else ''}" id="msg{idx}" aria-labelledby="subj{idx}">
<div class="poster">
  <span class="av av-{avc}"><span aria-hidden="true">{ini}</span>{status}</span>
  <div class="pwho">
    <p class="pname"><a href="#">{user}</a>{opb}<span class="sr"> ({status_sr})</span></p>
    {grp}
    <span class="{('rank ' + rank_cls).strip() if not group else 'rank'}">{rank}</span>
    {pips(npips)}
  </div>
  <div class="pstat">
    <span>Posts: [n]</span>
    <span>{location}</span>
    <span class="pextra">Joined: [date]</span>
  </div>
  <div class="picons">
    <a href="#" aria-label="View {user}'s profile">{I("user", 18)}</a>
    <a href="#" aria-label="Send {user} a personal message">{I("mail", 18)}</a>
  </div>
</div>
<div class="pmain">
  <div class="phead">
    <div>
      <h2 id="subj{idx}"><a href="#msg{idx}">{subj}</a></h2>
      <p class="pdate">{when}</p>
    </div>
    <div class="pact">
      <a class="btn btn-sm" href="#quickreply">{I("quote", 16)}Quote</a>
      <a class="btn btn-sm" href="#quickreply">{I("reply", 16)}Reply</a>
    </div>
  </div>
  <div class="pbody">
    {body}
  </div>
  <div class="react" role="group" aria-label="Reactions to this post">{rk}</div>
  {sig_html}
  <div class="pfoot">
    <a href="#">{I("flag", 15)}Report to moderator</a>
    <a href="#">{I("logged", 15)}Logged</a>
  </div>
</div>
</article>"""

R = lambda a, b, c: [("thumb", "Helpful", a), ("heart", "Support", b), ("same", "Same here", c)]

posts = [
 post(0, "dan_r", "DR", "1", True, "Newbie", "", 1, "[location]",
      """<p>My wife and I got the results last week. Two semen analyses, both showed no sperm at all, and the consultant thinks it is probably non-obstructive. My FSH came back high.</p>
    <p>I honestly don't know what to feel. I keep reading about micro-TESE and success rates and it is all a blur. If anyone has been through this, what should we be asking at the next appointment?</p>""",
      R("[n]", "[n]", "[n]"), op=True),
 post(1, "mark_t", "MT", "2", True, "Full Member", "", 3, "[location]",
      f"""<div class="bbq">
      <p class="bbq-h">{I("quote", 16)}<span>Quote from: <a href="#msg0">dan_r</a> on [date, time]</span></p>
      <blockquote><p>what should we be asking at the next appointment?</p></blockquote>
    </div>
    <p>I was exactly where you are three years ago. Write your questions down before the appointment, because you will forget them in the room. Ask whether they have checked your karyotype and for Y-chromosome microdeletions, because that changed what our options were.</p>
    <p>And look after yourself. The first month was the hardest part for me.</p>""",
      R("[n]", "[n]", "[n]"), sig="Diagnosed 2023 · micro-TESE 2024 · one day at a time", alt=True),
 post(2, "Mensfe Team", "M", "3", False, "Moderator", "rank-mod", 5, "Mensfe",
      """<p>Welcome, and thank you for posting. A lot of men read this board without ever writing, so this will help others too. Our <a href="article.html">Azoospermia guide</a> explains the tests and treatment terms you will hear, and the <a href="#">Counselling Support page</a> lists services if you would like to talk to someone.</p>""",
      R("[n]", "[n]", "[n]"), sig="Mensfe is peer support. It does not replace personal professional, legal or medical advice."),
 post(3, "jo_partner", "JP", "4", True, "Junior Member", "", 2, "[location]",
      """<p>Wife of a member here. It is not your fault, and she is probably as worried about you as about the result. Talking to each other helped us more than anything the clinic said.</p>""",
      R("[n]", "[n]", "[n]"), group="Partner", sig="Partner of a Mensfe member · stronger together", alt=True),
]
# Partner group pill styling

def toolbar(pos):
    return f"""<div class="toolbar">
  <nav class="pages" aria-label="Pages ({pos})">Pages: <span class="cur" aria-current="page">1</span></nav>
  <div class="btns">
    <a class="btn btn-gold" href="#quickreply">{I("reply", 17, 2.4)}Reply</a>
    <a class="btn" href="#">{I("bell", 17)}Notify</a>
    <a class="btn" href="#">{I("unread", 17)}Mark unread</a>
    <a class="btn" href="#">{I("print", 17)}Print</a>
  </div>
</div>"""

body = header("home", scope_board=True) + f"""
<main id="main" class="wrap">
{crumbs([("Mensfe Forum", "home.html"), ("Causes of male infertility", "board.html"), (T1, "topic.html")])}

{toolbar("top")}

<div class="panel cat cat-med">
  <div class="thead-bar">
    <div class="th-a" aria-hidden="true">Author</div>
    <div class="th-t">
      <p class="kick">Topic · Causes of male infertility</p>
      <h1>{T1}</h1>
      <p class="reads">Read [n] times · [n] replies · started by dan_r</p>
    </div>
  </div>
  {"".join(posts)}
</div>

{toolbar("bottom")}

<nav class="prevnext" aria-label="Other topics">
  <a href="#">{I("arrowl", 16)}previous topic</a>
  <a href="#">next topic{I("arrowr", 16)}</a>
</nav>

<section class="panel cat cat-gold" id="quickreply" aria-labelledby="qr-h">
  <div class="cat-h">
    <span class="ctile">{I("pen", 20)}</span>
    <h2 id="qr-h">Quick reply</h2>
  </div>
  <form class="qr-body" action="#">
    <p class="qr-note">With Quick-Reply you can write a post when viewing a topic without loading a new page. You can still use the normal reply and preview features.</p>
    <label class="l" for="reply">Your reply</label>
    <div class="qr-tools" role="toolbar" aria-label="Formatting">
      <button type="button" aria-label="Bold"><strong aria-hidden="true">B</strong></button>
      <button type="button" aria-label="Italic"><em class="fi" aria-hidden="true">I</em></button>
      <button type="button" aria-label="Underline"><span class="fu" aria-hidden="true">U</span></button>
      <button type="button" aria-label="Insert link">{I("link", 18)}</button>
      <button type="button" aria-label="Insert quote">{I("quote", 18)}</button>
    </div>
    <textarea id="reply" name="reply" placeholder="Share your experience or a kind word"></textarea>
    <div class="qr-row">
      <label class="check"><input type="checkbox" name="notify" checked> Notify me of replies</label>
      <div class="btns">
        <button class="btn" type="button">Preview</button>
        <button class="btn btn-gold" type="submit">{I("reply", 17, 2.4)}Post</button>
      </div>
    </div>
  </form>
  <p class="browsing">Users browsing this topic: [n] guests</p>
</section>

<div class="disc" role="note">
  {I("info", 20)}
  <p><strong>This is peer support, not medical advice.</strong> Members share their own experience. Please talk to your doctor, urologist or clinic about your own diagnosis and treatment. Read the <a href="#">forum rules</a>.</p>
</div>
</main>
""" + FOOTER

html = head("Just diagnosed with non-obstructive azoospermia. Where do we start? | Mensfe Forum",
            "A Mensfe member asks where to start after a non-obstructive azoospermia diagnosis. Men and partners who have been there reply with practical questions to ask.") + body
