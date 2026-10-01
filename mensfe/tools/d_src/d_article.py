from d_common import *
from d_home import T1
from d_board import trow

guides = ["Male fertility", "Infertility", "Semen analysis", "Azoospermia", "Varicocele", "Treatment",
          "Vasectomy reversal", "Erection problems", "Egg donation", "Sperm donation", "Nutrition", "Counselling support"]
glinks = "".join(
    (f'<li><a href="article.html" aria-current="page">{I("doc", 16)}{g}</a></li>' if g == "Azoospermia"
     else f'<li><a href="#">{I("doc", 16)}{g}</a></li>') for g in guides)

toc = [("what", "What is azoospermia?"), ("types", "The two main types"), ("diagnosis", "How it is diagnosed"),
       ("treatment", "Treatment options"), ("discuss", "Discuss this on the forum"), ("sources", "Sources")]
toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)

disc_rows = [
 trow("new", T1, "topic.html", "dan_r", (T1, "topic.html", "jo_partner", "2h ago")),
 trow("read", "High FSH and no sperm: what did your urologist suggest?", "#", "rich_w", ("High FSH and no sperm: what did your urologist suggest?", "#", "dan_r", "2 days ago")),
 trow("new", "Karyotype normal, still waiting on Y-microdeletion results", "#", "sam_k", ("Karyotype normal, still waiting on Y-microdeletion results", "#", "mark_t", "Yesterday")),
]

body = header("info") + f"""
<main id="main" class="wrap">
{crumbs([("Mensfe Forum", "home.html"), ("Information", "#"), ("Azoospermia", "article.html")])}

<div class="with-side">
  <article class="panel cat cat-gold art" aria-labelledby="art-h">
    <header class="art-head">
      <p class="kick">Information guide · Causes of male infertility</p>
      <h1 id="art-h">Azoospermia</h1>
      <p class="lede">What it means when a semen analysis finds no sperm, the two main types, the tests you are likely to have and the routes to parenthood that are open to you.</p>
    </header>
    <p class="byline">
      <span>{I("pen", 16)}Written by [Author name]</span>
      <span>{I("shield", 16)}Medically reviewed by [Reviewer name, credentials]</span>
      <span>{I("calendar", 16)}Last reviewed [date]</span>
    </p>
    <p class="founders">Mensfe is run by <strong>Pip Reilly</strong>, a professional fertility counsellor with over 15 years' experience with fertility charities, and <strong>Rob Barlow</strong>, a medical scientist who was diagnosed with azoospermia more than 25 years ago.</p>

    <div class="prose">
      <section class="inshort" aria-labelledby="short-h">
        <h2 id="short-h">{I("info", 16)}In short</h2>
        <ul>
          <li>Azoospermia means no measurable sperm in the ejaculate. It affects about 1% of all men and around 10–15% of men with infertility.</li>
          <li>It is either <strong>obstructive</strong> (sperm are made but blocked) or <strong>non-obstructive</strong> (the testes make very little or no sperm).</li>
          <li>Many men can still become fathers, through surgery, sperm retrieval with ICSI, or donor sperm.</li>
        </ul>
      </section>

      <h2 id="what">What is azoospermia?</h2>
      <p>Azoospermia means there is no measurable sperm in the ejaculate. It affects about 1% of all men and around 10–15% of men with infertility.</p>
      <p>It is usually confirmed by at least two semen analyses, with the sample spun down (centrifuged) so the laboratory can look for any sperm at all.</p>

      <h2 id="types">The two main types</h2>
      <div class="types">
        <div class="type">
          <span class="tag tag-o">Obstructive</span>
          <h3>Sperm are made, but blocked</h3>
          <p>A blockage stops sperm reaching the ejaculate. This can happen after a vasectomy, an infection or an injury, or because of congenital absence of the vas deferens, which is linked to cystic fibrosis gene changes.</p>
        </div>
        <div class="type">
          <span class="tag tag-n">Non-obstructive</span>
          <h3>Very little or no sperm is made</h3>
          <p>The testes make very little or no sperm. Causes include genetic conditions such as Klinefelter syndrome or Y-chromosome microdeletions, hormone problems, a history of undescended testes, or previous chemotherapy or radiotherapy.</p>
        </div>
      </div>

      <h2 id="diagnosis">How it is diagnosed</h2>
      <ul>
        <li><strong>Repeat semen analysis</strong>, with the sample centrifuged to look for any sperm.</li>
        <li><strong>Physical examination</strong> by a urologist or andrologist.</li>
        <li><strong>Hormone blood tests</strong>: FSH, LH and testosterone.</li>
        <li><strong>Genetic tests</strong>: karyotype, Y-chromosome microdeletion and CFTR (the cystic fibrosis gene).</li>
        <li>Sometimes a <strong>scrotal ultrasound</strong>.</li>
      </ul>

      <h2 id="treatment">Treatment options</h2>
      <h3>Obstructive azoospermia</h3>
      <p>Surgical repair, such as vasectomy reversal, or sperm retrieval (PESA, MESA or TESA) with the sperm then used in ICSI.</p>
      <h3 class="mt">Non-obstructive azoospermia</h3>
      <p>In some men, hormone treatment. Surgical sperm retrieval, such as micro-TESE, with any sperm found used in ICSI.</p>
      <h3 class="mt">Donor sperm</h3>
      <p>Donor sperm is another route to parenthood. Many couples consider it alongside, or after, other options.</p>
      <p>Talk your options through with a urologist or andrologist, who can explain what fits your test results.</p>
    </div>

    <section class="discuss" aria-labelledby="discuss">
      <div class="panel cat cat-med">
        <div class="cat-h">
          <span class="ctile">{I("b_causes", 20)}</span>
          <h2 id="discuss">Discuss this on the forum</h2>
          <p class="sub">From Causes of male infertility · [n] members discussing</p>
        </div>
        <table class="ftable">
          <caption class="sr">Recent azoospermia topics from the Causes of male infertility board</caption>
          <thead><tr><th scope="col" class="c-icon"><span class="sr">Status</span></th><th scope="col">Subject / Started by</th><th scope="col" class="c-rv">Replies / Views</th><th scope="col" class="c-last">Last post</th></tr></thead>
          <tbody>
          {"".join(disc_rows)}
          </tbody>
        </table>
        <div class="discuss-foot">
          <p>You are not alone. Men who have had this diagnosis answer questions here every day.</p>
          <div class="btns">
            <a class="btn" href="board.html">View the board</a>
            <a class="btn btn-gold" href="#">{I("plus", 17, 2.4)}Ask the community: start a topic</a>
          </div>
        </div>
      </div>
    </section>

    <div class="prose">
      <h2 id="sources">Sources</h2>
      <ol class="sources">
        <li>[Source 1, e.g. NHS / NICE / WHO guidance]</li>
        <li>[Source 2, e.g. clinical guideline on male infertility]</li>
        <li>[Source 3, e.g. peer-reviewed review article]</li>
      </ol>
    </div>

    <div class="helpful" role="group" aria-labelledby="helpful-q">
      <p id="helpful-q">Was this page helpful?</p>
      <button class="btn btn-sm" type="button">{I("thumb", 16)}Yes</button>
      <button class="btn btn-sm" type="button">No</button>
    </div>

    <div class="disc" role="note">
      {I("info", 20)}
      <p><strong>Mensfe is peer support.</strong> It does not replace personal professional, legal or medical advice. Please talk to your own doctor about your diagnosis and treatment.</p>
    </div>
  </article>

  <aside class="side" aria-label="Information section">
    <nav class="panel cat cat-gold" aria-labelledby="info-h">
      <div class="cat-h">
        <span class="ctile">{I("book", 20)}</span>
        <h2 id="info-h">Information</h2>
      </div>
      <ul class="side-list">
        {glinks}
        <li class="sep" aria-hidden="true"></li>
        <li><a href="#">{I("book", 16)}Medical guide (jargon explained)</a></li>
        <li><a href="#">{I("heart", 16)}Emotive guide</a></li>
      </ul>
    </nav>
    <nav class="panel cat cat-gold" aria-labelledby="toc-h">
      <div class="cat-h">
        <span class="ctile">{I("doc", 20)}</span>
        <h2 id="toc-h">On this page</h2>
      </div>
      <ol class="toc">{toc_html}</ol>
    </nav>
  </aside>
</div>
</main>
""" + FOOTER

html = head("Azoospermia: causes, tests and treatment | Mensfe Information",
            "Azoospermia means no sperm in the ejaculate. Learn the obstructive and non-obstructive types, how it is diagnosed, treatment options, and talk to men who have been there.") + body
