# Mensfe forum redesign — build brief (shared by all three directions)

Client: **Mensfe** (mensfe.net), a men's fertility / male infertility support **forum** running since 2007.
The whole site is a forum. Information pages support the forum; they are not a separate site.
Treat every screen as part of a forum product (forum-first navigation, latest discussions, boards, topics).

## Output

Each direction lives in its own folder: `mensfe/redesign/a/`, `b/`, `c/`. Write exactly four files:

| File | Screen |
|---|---|
| `home.html` | Homepage (forum-first) |
| `boards.html` | Forum board index (all boards grouped by category) |
| `topic.html` | A single topic/thread view with posts, replies and a reply box |
| `article.html` | Medical information page template, using **Azoospermia** as the example |

Rules:
- Plain, static, self-contained HTML5. One `<style>` block per file (repeat shared CSS in each file; no external CSS/JS files). No JavaScript needed.
- Fonts: Google Fonts `<link>` only. No other external resources, no images from the web. No emoji. Icons are inline stroke SVG.
- `<meta name="viewport" content="width=device-width, initial-scale=1">`, `lang="en"`, `charset utf-8`, a proper `<title>` and meta description per page (the redesign must model good SEO: one `<h1>`, logical H2/H3, semantic `header/nav/main/aside/footer/article`).
- **Fully responsive**: must look designed at 1440px wide AND at 390px wide (the mobile homepage is rendered from the same `home.html` at 390px). Use CSS grid/flex with media queries; no horizontal scrolling at 390px. Touch targets ≥ 44px.
- Accessible: text contrast ≥ 4.5:1, real `<a href>`, `<button>`, `<label>` + `<input>`; `aria-label` on icon-only buttons; visible focus styles.
- Links between the four pages use relative hrefs (`home.html`, `boards.html`, `topic.html`, `article.html`). Other links use `#`.
- Print-friendly: add `@media print { * { -webkit-print-color-adjust: exact; print-color-adjust: exact; } }` so backgrounds survive PDF export. Avoid `position: fixed/sticky` elements (they repeat in PDFs).
- No invented statistics. Member/topic/post counts are written as `[n]` placeholders. Dates for reviewer etc. are placeholders like `[Last reviewed date]`. The only real number you may use: **6.5 million visits in 2025** (from the client's current site).
- No AI design tropes: no gradient washes, no left-border accent cards, no Inter/Roboto/Arial.
- Do NOT render, screenshot or open the files; just write them carefully and check your HTML is well-formed. Do not git commit.

## Real content from the current site (use it)

- Tagline ideas from the current site: "You don't have to work this out on your own." / "You'll never walk alone at Mensfe" / "Information, help and support for male infertility and fertility issues by you for you." / "Our information resources are FREE for everyone".
- Current homepage questions: Seeking help for male infertility? Help increase sperm count, low testosterone, sperm motility? Trying to understand treatment options? Help with gender communication difficulties?
- Left nav today: About Us, Mission, Contact, Login, Patrons. Info pages: Male Fertility, Infertility, Semen Analysis, Azoospermia, Varicocele, Treatment, Vasectomy Reversal, Erection Problems, Egg Donation, Sperm Donation, Nutrition, Counselling Support. Also "Medical" (jargon explained) and "Emotive" (emotional issues) guides.
- Research board: "Current Research On Male Infertility".
- Mensfe is a member of **iCSI** (International Consumer Support for Infertility); presented a poster at the ICSI 2007 conference.
- Email: info@mensfe.net. Footer: © 2007–2026 Mensfe. Disclaimer: "Mensfe is peer support. It does not replace personal professional, legal or medical advice."
- Book: **"A Journey Through Male Infertility — Stronger Together" by Pip Reilly** — "A book for men that women should read". An honest, accessible account of the relational, emotional and physical challenges men face, often unspoken, with practical support strategies — "You are stronger together." Amazon link: https://www.amazon.co.uk/dp/B0G8LX5FBJ . Draw the cover as a typographic block (no image file).
- Logo: wordmark "mensfe" (lowercase) with a simple inline-SVG mark (e.g. a circle with an arrow — the male symbol — kept abstract).

## Forum structure to show (example boards — the client will map these to their real boards)

Categories and boards (name — one-line description):
- **Getting started**: Introductions — Say hello, share as much or as little as you like. · Forum help — Questions about using the site.
- **Diagnosis and tests**: Semen analysis — Make sense of count, motility and morphology. · Azoospermia — Obstructive and non-obstructive, sperm retrieval, next steps. · Varicocele — Diagnosis, surgery and recovery. · Hormones and testosterone — Low T, FSH, LH and hormone treatment.
- **Treatment**: ICSI and IVF — Cycles, clinics, the waiting and the outcomes. · Surgical sperm retrieval — PESA, TESE, micro-TESE. · Vasectomy reversal — Reversal surgery and what came after.
- **Family building**: Donor conception — Choosing donor sperm or eggs and talking to children about it.
- **Emotional support**: Talking it through — Anger, grief and hope all belong here. · Partners' corner — For partners supporting a man through infertility. · Relationships and communication — Talking to each other, family and friends.
- **Research**: Current research on male infertility — Members share and discuss new studies, trials and news.

Board rows show: name, description, `[n] topics · [n] posts`, and a "last post" (sample topic title, username, relative time). The board index also needs a forum search, a "Start a new topic" button, and a small sidebar (who's online `[n]`, forum rules, new-member guide).

Sample latest discussions (title — board — username — time):
- Just diagnosed with non-obstructive azoospermia. Where do we start? — Azoospermia — dan_r — 2h ago
- Micro-TESE next month: what should I ask the urologist? — Surgical sperm retrieval — mark_t — 5h ago
- How do we tell our parents we are using a donor? — Donor conception — oakley — Yesterday
- Second semen analysis came back better. Anyone else? — Semen analysis — tomh — Yesterday
- Feeling like I have let her down — Talking it through — quiet_one — 2 days ago

Homepage must include: header with forum-first nav (Forum, Information, Research, About), search, Sign in, "Join free"; hero with a forum CTA ("Join the forum, free" + "Read without an account"); trust points (6.5 million visits in 2025 · Post under any username · Free since 2007 · Member of iCSI); latest discussions; boards preview; a 3-step "New here?" guide (anonymous username → say hello in Introductions → ask anything); the 12 info topics as links; research board promo; the book; footer with disclaimer.

## Topic view content (sample posts — keep this wording)

Breadcrumb: Forum › Azoospermia › topic. Title: "Just diagnosed with non-obstructive azoospermia. Where do we start?" Actions: Reply, Follow, Share. Each post: avatar initials, username, role badge, "Joined [date] · [n] posts", relative time, body, reactions ("Helpful [n]", "Support [n]"), Quote / Reply buttons.

1. **dan_r** (Member, original poster): "My wife and I got the results last week. Two semen analyses, both showed no sperm at all, and the consultant thinks it is probably non-obstructive. My FSH came back high." / "I honestly don't know what to feel. I keep reading about micro-TESE and success rates and it is all a blur. If anyone has been through this, what should we be asking at the next appointment?"
2. **mark_t** (Member): "I was exactly where you are three years ago. Write your questions down before the appointment, because you will forget them in the room. Ask whether they have checked your karyotype and for Y-chromosome microdeletions, because that changed what our options were." / "And look after yourself. The first month was the hardest part for me."
3. **Mensfe Team** (Moderator badge): "Welcome, and thank you for posting. A lot of men read this board without ever writing, so this will help others too. Our Azoospermia guide explains the tests and treatment terms you will hear, and the Counselling Support page lists services if you would like to talk to someone." (link both to article.html / #)
4. **jo_partner** (Partner badge): "Wife of a member here. It is not your fault, and she is probably as worried about you as about the result. Talking to each other helped us more than anything the clinic said."

Sidebar: topic info (board, started, `[n]` replies, `[n]` following), related information links (Azoospermia explained, Surgical sperm retrieval, Counselling support), "This is peer support, not medical advice" note, similar topics. Bottom: reply composer (label "Your reply", textarea, formatting buttons Bold/Italic/Link/Quote with aria-labels, "Notify me of replies" checkbox, "Post reply" button).

## Article page content (Azoospermia — medically accurate; keep claims to these)

Breadcrumb: Information › Azoospermia. H1 "Azoospermia". Byline row: "Written by [Author name]" · "Medically reviewed by [Reviewer name, credentials]" · "Last reviewed [date]". An "In short" summary box. A table of contents sidebar. Sections:
- **What is azoospermia?** No measurable sperm in the ejaculate. It affects about 1% of all men and around 10–15% of men with infertility. It is usually confirmed by at least two semen analyses, with the sample spun down (centrifuged) to look for any sperm.
- **The two main types**: *Obstructive* — sperm are made but a blockage stops them reaching the ejaculate (e.g. after vasectomy, infection or injury, or congenital absence of the vas deferens, which is linked to cystic fibrosis gene changes). *Non-obstructive* — the testes make very little or no sperm (causes include genetic conditions such as Klinefelter syndrome or Y-chromosome microdeletions, hormone problems, a history of undescended testes, or previous chemotherapy/radiotherapy).
- **How it is diagnosed**: repeat semen analysis, physical examination, hormone blood tests (FSH, LH, testosterone), genetic tests (karyotype, Y-chromosome microdeletion, CFTR), sometimes scrotal ultrasound.
- **Treatment options**: Obstructive — surgical repair (such as vasectomy reversal) or sperm retrieval (PESA, MESA, TESA) used with ICSI. Non-obstructive — in some men hormone treatment; surgical sperm retrieval such as micro-TESE, used with ICSI. Donor sperm is another route to parenthood. Talk options through with a urologist or andrologist.
- **You are not alone**: a forum CTA box linking to the Azoospermia board (`[n]` members discussing) and showing 2–3 recent topic titles from that board.
- **Sources**: placeholder list `[Source 1 — e.g. NHS / NICE / WHO guidance]` etc.
- Disclaimer.
Also a "Was this page helpful?" Yes/No button pair and an "Ask the community" CTA.

## UPDATE — real client facts (apply these; they override the example boards above)

**Real forum boards** (the forum runs on SMF). Use this structure in boards.html and the homepage boards preview:
- **Community**: General discussion — Anything and everything about male fertility. · Let off some steam — Somewhere to vent when it all gets too much.
- **Medical**: Causes of male infertility — Azoospermia, low count, varicocele, hormones and more. · Dealing with doctors — Appointments, clinics, tests and treatment. · Dear Doctor (expert panel) — Questions answered by our medical panel.
- **Feelings and relationships**: Men's reactions to infertility — How it feels, from the men living it. · Women's reactions to male infertility — Partners share their side.
- **Research**: Current research on male infertility — New studies, trials and news.

Remap the sample discussion board labels: Azoospermia → Causes of male infertility; Surgical sperm retrieval → Dealing with doctors; Donor conception → General discussion; Semen analysis → Causes of male infertility; Talking it through → Men's reactions to infertility. Topic breadcrumb: Forum › Causes of male infertility › topic. jo_partner's badge stays "Partner".

**Founders** (add an "About / who runs Mensfe" strip on the homepage, and use in the article byline area as "Mensfe is run by…"): Mensfe was founded by **Pip Reilly**, a professional fertility counsellor with over 15 years' experience with fertility charities (also the book's author), and **Rob Barlow**, a medical scientist who was diagnosed with azoospermia more than 25 years ago. Keep "Medically reviewed by [Reviewer name, credentials]" as a placeholder.
