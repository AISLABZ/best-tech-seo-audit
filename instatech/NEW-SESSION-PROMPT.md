You are taking over the SEO growth programme for **instatech.uk**. It is a phone, laptop, tablet and smartwatch repair business with walk-in shops at 67 Marchmont Street, Bloomsbury WC1N 1AP (+44 7377 244454) and 16 City Road, Moorgate EC1Y 2AA (+44 7508 088898). A third shop at 22 Great Castle Street, Oxford Circus W1G 0HY opens in October 2026. The site runs on WordPress, WooCommerce, Rank Math and LiteSpeed Cache, and is served through the Hostinger CDN.

The goal is to make instatech.uk number 1 in three arenas:
1. The local pack within about 1 km of each shop.
2. Neighbourhood searches (Bloomsbury, Holborn, King's Cross, Moorgate, Old Street, Barbican, Oxford Circus).
3. London head terms such as "iphone screen repair london" and "macbook repair london".

## Context
- The full audit (21 Oct 2026) is in the GitHub repo `aislabz/best-tech-seo-audit`, branch `claude/laughing-clarke-s2j0uk`. The dashboard is `instatech/index.html` and this brief is `instatech/NEW-SESSION-PROMPT.md`. Read the dashboard first.
- **Step 0:** confirm which connected tool gives write access to instatech.uk's WordPress, for example a Hostinger account that hosts it, a WordPress MCP connector, or a WordPress application password stored as an environment secret. Show me what access you have before changing anything. Note: the site's `/wp-json/` index does not advertise application-password authentication, so it may be disabled by a security plugin. If so, tell me.

## Rules for working on the live site
- Take a full backup, or confirm a restorable one exists, before the first change. Log every change, with URL, field, old value and new value, in `instatech/changelog.md` in the repo, and push it.
- Ask me before deleting any page or post, or changing the theme, plugins, menus or LiteSpeed settings. Content and metadata edits listed below are pre-approved.
- **Programme rules (owner, 21 Oct 2026). These override anything below that mentions prices:** no prices anywhere (no price tables, "from £X", `offers` in schema, or price requests to the owner); warranty "covers parts and labour, period depends on the repair"; parts "genuine replacement parts and high-quality parts that meet or exceed the original specification"; Apple kept general (no genuine-Apple-battery or "unknown part" mentions on service pages). See `instatech/backlog.md` → Programme rules.
- Never invent warranties, turnaround times, staff names or reviews. If a page needs a fact I haven't given you, leave a clearly marked placeholder and add it to a "needs from owner" list.
- Follow Google's review policy: review requests go to every customer, with no incentives and no filtering to only happy customers.
- Do not create doorway pages. Every new page must carry unique, real content: prices, faults, turnaround, parts grade, warranty and FAQ.
- After each batch, re-crawl the affected URLs and confirm the change is live. Purge the LiteSpeed cache if needed.

## Phase 1: fix the leaks (do now, weeks 1–2)
1. **Internal links to the money page.** `/mobile-repair-services/screen-repair/` has only 2 internal links, while each location page has about 280. Add it, and every future repair-type page, to the main menu and footer (ask me before the menu change). Link it from the homepage hero, from both location pages, and contextually from blog posts that mention screens.
2. **Homepage H1.** The current H1 is "2 shops weren't enough. Oxford Circus is next." Change it to a descriptive H1, for example "Phone, laptop and tablet repair in central London — same day, walk-in", and keep the Oxford Circus message as a banner or H2. Also make the service-page H1s lead with the searched phrase, for example "Phone repair in London" rather than "Professional Mobile Repair Services".
3. **Broken and redirecting links in posts.** Repoint each link to its final URL:

| Post | Current link | Anchor | Repoint to |
|---|---|---|---|
| /tablet-screen-repair-near-me/ | /electronics-store-1/ (404) | chargers and cables | /product-category/chargers/ |
| /tablet-screen-repair-near-me/ | /layouts/display/ | no image at all | /tablet-repairs/ |
| /tablet-screen-repair-near-me/ | /services/tablet-repairs/ (301) | worth repairing | /tablet-repairs/ |
| /laptop-charger-replacement/ | /electronics-repair-1/ (404) | support repairs | /laptop-desktop-repair/ |
| /laptop-charger-replacement/ | /services/laptop-desktop-repair/ (301) | the laptop may need attention | /laptop-desktop-repair/ |
| /wireless-earphones-for-calls/ | /services/laptop-desktop-repair/ (301) | calls keep cutting out | /mobile-repair-services/ |
| /why-is-my-phone-battery-draining/ | /electronics-repair-2/ (404) | professional cleaning | /mobile-repair-services/ |
| /desktop-computer-repair-near-me/ | /electronics-repair-2/ (404) | practical replacements | /laptop-desktop-repair/ |
| /phone-screen-repair-cost/ | /3-in-1-trio-1-charging-cable/ (301) | charger cable | /product/3-in-1-trio-1-charging-cable/ |
| /phone-screen-repair-cost/ | /budget-friendly-gadgets-with-premium-features/ (404) | everyday accessories | /shop/ |
| /phone-screen-repair-cost/ | /signs-your-gadget-needs-repair-service-soon/ (404) | other faults | /mobile-repair-services/ |
| /how-long-does-phone-repair-take/ | /layouts/battery/ | Battery replacements | /mobile-repair-services/ (later: the new battery page) |
| /laptop-repair-near-me-what-to-check-first/ | /layouts/battery/ | swollen battery | /laptop-desktop-repair/ |
| /tablet-battery-replacement-service-guide/ | /electronics-store-2/ (404) | local shop | /locations/ |
| /smartwatch-screen-repair-fix-or-replace/ | /request-quote/ (301) | DIY might appeal | /book-an-appointment/ |
| /wireless-charger-compatibility-guide/ | /choose-car-phone-holder-mount/ (301) | wireless car charger | /best-phone-mounts-for-cars/ |
| /phone-data-recovery-service-explained/ | /testimonials/ (301) | local credibility | /about-us/ |

4. **Theme demo leftovers.** Set `/layouts/battery/` and `/layouts/display/` to noindex now, and ask me before deleting them. 301 `/blog-standard/` to a real blog hub (`/repair-guides/` or `/blog/`). Move all posts out of "Uncategorized", then noindex or remove `/category/uncategorized/`.
5. **Category metadata.** None of the 33 product categories has a meta description. Set a Rank Math template, for example "%term% — buy online or collect today from our Bloomsbury and Moorgate shops in central London.", then hand-write descriptions for the top 10. Fix casing in category names: "USB-C HUBS", "ETHERNET Cables", "For C-C phones", "MacBook/Laptop charger". Add descriptions to the 6 blog categories, and add an H1 to the blog archive template (ask me first, since it is a theme change).
6. **Products.** Write meta descriptions for the 26 products that lack one, mentioning in-store collection. These are mainly the Ethernet cables, EnergyBar power banks, World Travel Adapter, Z-series cables, stylus pens, ME-02/ME-08C earphones, the DJ-BoomBox speaker, the CC25 car charger and the 45W PD charger. Make the 19 duplicate titles unique by length or variant, for example the `-2` duplicates of the Ethernet cables and World Travel Adapter. Fill in missing alt text: 972 of 3,449 images have none, 791 of them on products. Use Rank Math's add-missing-alt option as a stopgap, and hand-write alt text on core pages.
7. **About Us.** It has 0 internal links. Link it from the header or footer, and link the blog author profiles to it.
8. **Entity consistency.** Use "InstaTech" everywhere; "instaTech" appears in 4 titles and in the Google Maps listing names. Replace the Google Maps *search* URLs in the schema's `sameAs` and `hasMap` with each listing's share or CID link (ask me for them). Add Instagram (instagram.com/instatechlondon), TikTok (@instatechlondon), Facebook and the GBP links to the Organization `sameAs`. Give each location page the full MobilePhoneStore node with `@id`, `geo`, `hasMap`, `sameAs`, hours and phone. Give `/locations/oxford-circus/` Store schema.
9. **Performance (ask before changing).** The homepage is 2.2 MB with 2,412 DOM nodes, about 168 KB of unused JS and 191 KB of GTM. In LiteSpeed: delay JS for GTM and non-critical scripts, remove unused CSS, lazy-load iframes and maps, and enable the cache crawler. Dequeue TI Wishlist and Advanced Popups assets on non-shop pages. Verify with PageSpeed Insights.
10. Confirm Search Console ownership and submit `/sitemap_index.xml`. Fix the Lighthouse "links are not crawlable" failure by replacing `href="#"` and JS-only links, and fix the tap-target size failures.

## Phase 2: money pages (weeks 3–8)
Before building, check whether existing blog posts overlap with these pages (for example `/phone-screen-repair-cost/`, `/tablet-screen-repair-near-me/`, `/desktop-computer-repair-near-me/` and `/laptop-repair-near-me-what-to-check-first/`). Merge them with a 301 or re-angle them to informational queries.

Build these pages, in this order:
- Battery replacement
- Charging port repair
- Water damage repair
- Back glass repair
- iPhone repair hub
- Samsung repair hub
- iPad repair (consolidate with /tablet-repairs/)
- MacBook repair
- Apple Watch repair (retitle the smartwatch page)
- iPhone 16, 15, 14 and 13 series model pages

Each page needs:
- A price table per fault (from me)
- Turnaround, parts grade, warranty and FAQ
- Service and Offer schema, plus FAQPage and Breadcrumb schema
- A booking CTA and links to both shops
- Links into the page from the menu or hub, location pages and related posts

Deepen the location pages with nearby areas and stations, directions, and shop-specific reviews.

## Phase 3: local prominence (from week 2, ongoing)
- **Google Business Profiles.** Prepare complete content for all three: primary category "Mobile phone repair shop", services with prices, attributes, a weekly post and photos. The Oxford Circus GBP should be verified before opening, and Sunday opening is a differentiator against iSmash, which is closed on Sundays.
- **Review requests.** Draft a review-request SMS and email that I send after every repair.
- **Citations.** Prepare listings with identical business details for Apple Business Connect, Bing Places, Yell, Yelp, Thomson Local, Foursquare and Trustpilot. Track them in `instatech/citations.md`.

## Phase 4: authority (from month 2)
Draft outreach for:
- Student-discount partnerships with nearby universities (UCL, SOAS, Birkbeck)
- Local business associations and BIDs for Marchmont Street, City Road and the Oxford Circus area
- A data-led PR piece using our repair data

Publish two blog posts a month, each linking to a money page.

## Scheduled runs
Create these as scheduled tasks. Each fires a **fresh session** (standalone prompt), in the Europe/London timezone, with this repo and the WordPress write connector attached. Every run must:
- Start by pulling branch `instatech-seo-engine`. Create it from `claude/laughing-clarke-s2j0uk` if it is missing.
- Read `instatech/backlog.md`, the single source of truth, which you create now from the phases above.
- Do its job, update the backlog, changelog and scorecard, and push.
- Message me only if something needs my input or broke.

1. **Mon 08:41 — Measure and verify.** Re-crawl all sitemap URLs. Compare against the baseline: H1s, meta descriptions, canonicals, schema, alt text, dead links and inlinks to money pages. Flag regressions, mark completed backlog items as verified, and update the scorecard (and GSC and GBP data once connected).
2. **Tue 09:37 — Fix.** Apply the next pre-approved Phase 1 items, or queue the items that need approval with an exact proposal.
3. **Wed 09:43 — Build.** Draft the next Phase 2 money page in full: copy, schema, internal-link plan and placeholders. Publish it as a draft in WordPress (not live) and list what it needs from me.
4. **Thu 09:47 — Earn.** Draft this week's GBP post for each shop and the next 2 citation or outreach items. Report review counts if available.
5. **Fri 15:53 — Report.** Write a one-page weekly scorecard with what shipped, what's verified, what's blocked on me, and next week's plan. Add it to `instatech/reports/YYYY-MM-DD.md`, refresh the dashboard, and notify me.
6. **Monthly, 1st at 09:33 — Review.** Re-run Lighthouse on the homepage, screen repair and location pages. Re-check live SERPs for the target terms against iSmash and others. Re-prioritise the backlog.

Start now: do Step 0, then create `instatech/backlog.md` and `instatech/changelog.md`, then work through Phase 1 items 1, 3, 5, 6 and 7 (pre-approved content and metadata). Then create the scheduled tasks and show me the list.
