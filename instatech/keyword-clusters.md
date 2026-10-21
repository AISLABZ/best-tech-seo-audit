# InstaTech keyword clusters and ranking-driven content

**Status (21 Oct 2026): framework built, figures pending.** Search Console access for instatech.uk is not yet
confirmed (backlog 1.13), and no query or page data could be pulled in this session. The cluster map below is
built from a full crawl of the sitemap (17 pages, 61 posts, 159 products, 33 product categories), so every target
URL and every structural conflict is real. Primary and supporting keywords are **seed hypotheses** until the first
Search Console pull confirms them; no rule has been applied yet. The first pull is the baseline month, and the
"slipped" rule (R5) starts the month after.

Cluster IDs: **S** commercial service/device · **L** hyperlocal · **B** brand · **I** informational · **O** orphans.

## 1. Cluster map

### Commercial service and device clusters
| ID | Cluster | Target URL | Seed primary | Seed supporting keywords | Our other URLs on the topic | Flag |
|---|---|---|---|---|---|---|
| S1 | Phone repair (any device) | `/mobile-repair-services/` | phone repair london | mobile phone repair london · phone repair near me · same day phone repair · samsung repair london (until 2.6 exists) | `/` | Hub owns any-device searches only |
| S2 | Phone screen repair | `/mobile-repair-services/screen-repair/` | phone screen repair london | iphone screen repair london · cracked phone screen repair · screen replacement near me · phone screen repair cost | `/phone-screen-repair-cost/`, `/how-to-fix-cracked-phone-screen/` | **R7 risk:** the cost post targets a commercial query (backlog 2.14) |
| S3 | Battery replacement | **gap** → `/mobile-repair-services/battery-replacement/` (drafted, 2.1) | phone battery replacement london | iphone battery replacement london · samsung battery replacement · swollen phone battery | `/guide-to-phone-battery-replacement-uk/` | **R8 gap**; the guide post must be re-angled to informational when the page launches |
| S4 | Charging port repair | **gap** (2.2) | charging port repair london | phone not charging repair · iphone charging port repair | `/how-to-fix-phone-charging-issues/`, `/how-to-clean-charging-port-safely/` | R8 gap |
| S5 | Water damage repair | **gap** (2.3) | water damaged phone repair london | phone dropped in water repair | `/can-water-damaged-phones-recover/`, `/phone-corrosion-after-water-damage/` | R8 gap |
| S6 | Laptop and desktop repair | `/laptop-desktop-repair/` | laptop repair london | computer repair london · pc repair london · laptop repair near me | `/laptop-repair-near-me-what-to-check-first/`, `/desktop-computer-repair-near-me/` | **R7 risk:** two "near me" posts (backlog 2.14) |
| S6a | MacBook repair (device) | **gap** (2.8); today `/laptop-desktop-repair/` | macbook repair london | macbook screen repair · macbook battery replacement · macbook logic board repair | `/macbook-logic-board-repair/` | Device page owns MacBook searches once live; S6 then drops them |
| S7 | Tablet and iPad repair | `/tablet-repairs/` | ipad repair london | tablet repair london · ipad screen repair · tablet screen repair near me | `/tablet-screen-repair-near-me/`, `/can-a-cracked-tablet-be-repaired/` | **R7 risk:** near-me post. Title and H1 are scoped to Bloomsbury only, but both shops repair tablets (Q2): retarget London-wide (backlog 5.6) |
| S8 | Smartwatch and Apple Watch repair | `/smartwatch-repair-service/` | apple watch repair london | apple watch screen repair · smartwatch repair | `/smartwatch-repair-costs-uk/`, `/smartwatch-screen-repair-fix-or-replace/` | Retitle planned (2.9) |
| S9 | Sell or trade in a phone | `/buy-sell-phones/` | sell my phone london | sell phone for cash · phone trade in london · buy used phones london | `/where-to-sell-old-phone-best-price/`, `/phone-trade-in-checklist/` | Owner decision Q1: this page owns trade-in. `/phone-accessories-trade-in/` moves to S11 (backlog 5.3) |
| S10 | Data recovery | **gap** → service page (backlog 5.7) | phone data recovery london | recover data from broken phone · data recovery near me · tablet and laptop data recovery | `/phone-data-recovery-service-explained/` | **R8 gap** (owner confirmed the service, Q3); the post is re-angled to the informational question |
| S11 | Accessories shop | `/phone-accessories-trade-in/` (landing page); `/shop/` and product categories own product searches | phone accessories london | usb c cable · iphone charger · power bank · macbook charger | 33 product categories | Category pages own product searches; posts link to them |
| S12 | Currency exchange | `/currency-exchange-service/` | currency exchange central london | currency exchange near me · bureau de change | — | Separate line of business; tracked, not prioritised |

### Hyperlocal clusters (one per shop)
| ID | Cluster | Target URL | Seed primary | Seed supporting keywords |
|---|---|---|---|---|
| L1 | Bloomsbury WC1 | `/locations/bloomsbury/` | phone repair bloomsbury | phone repair holborn · phone repair king's cross · phone repair russell square · phone repair wc1 |
| L2 | Moorgate EC1 | `/locations/moorgate/` | phone repair moorgate | phone repair old street · phone repair barbican · phone repair city of london · phone repair ec1 |
| L3 | Oxford Circus W1 | `/locations/oxford-circus/` | phone repair oxford circus | phone repair oxford street · phone repair soho · phone repair w1 |
| L0 | All shops (hub) | `/locations/` | phone repair shops central london | instatech locations |

### Brand
| ID | Cluster | Target URL | Seed primary | Supporting |
|---|---|---|---|---|
| B1 | InstaTech brand | `/` | instatech | instatech london · instatech bloomsbury · instatech moorgate · instatech reviews (`/about-us/`) |

### Informational clusters (each links into a commercial cluster)
| ID | Cluster | Target URL (keep) | Other posts on the same intent | Links into | Flag |
|---|---|---|---|---|---|
| I1 | Wireless charging | `/wireless-charger-compatibility-guide/` | `/guide-wireless-charging-safety/`, `/how-to-choose-wireless-charger-for-iphone/`, `/do-wireless-chargers-damage-batteries/`, `/wired-vs-wireless-charging/` | S11 | Five posts on one topic: R7 candidate once data shows overlap |
| I2 | Cables and fast chargers | `/usb-c-versus-lightning/` | `/best-usb-c-cable-what-to-buy/`, `/lightning-cable-not-working/`, `/lightning-to-usb-c-adapter-what-to-buy/`, `/best-fast-chargers-for-android/`, `/usb-c-fast-charger-review/`, `/best-phone-charging-accessories/` | S11, S4 | Watch for overlap |
| I3 | Power banks | `/guide-to-choosing-power-banks/` | `/best-power-bank-for-travel/`, `/best-power-banks-for-students/`, `/portable-power-bank-review-everyday-use/` | S11 | Four posts on one topic: R7 candidate |
| I4 | Phone battery problems | `/why-is-my-phone-battery-draining/` | `/why-is-my-phone-overheating/`, `/iphone-battery-health-not-showing/` | S3 | — |
| I5 | Refurbished and second-hand phones | `/guide-to-buying-refurbished-phones/` | `/refurbished-phones-versus-used/`, `/how-to-buy-second-hand-phones/` | S9 | Two refurbished posts overlap |
| I6 | Repair decisions | `/phone-repair-versus-replacement/` | `/are-third-party-repairs-safe/`, `/iphone-unknown-part-message/`, `/how-long-does-phone-repair-take/`, `/back-up-phone-before-repair/` | S1, S2 | — |
| I7 | Laptop problems | `/when-to-replace-laptop-battery/` | `/how-to-troubleshoot-slow-laptop-performance/`, `/how-to-test-laptop-charger/`, `/laptop-charger-replacement/`, `/cracked-laptop-screen-repair-costs-options/` | S6, S6a | — |
| I8 | Tablet problems | `/why-is-my-tablet-not-charging/` | `/ipad-charging-port-repair/`, `/tablet-battery-replacement-service-guide/` | S7 | `/ipad-charging-port-repair/` reads as commercial; confirm intent from data |

### Orphans (report only)
`/phone-cases-everyday-protection-style/`, `/best-phone-mounts-for-cars/`, `/wireless-earphones-for-calls/`,
`/how-to-pair-wireless-earbuds/`, `/how-to-remove-phone-viruses/`, `/how-to-transfer-phone-data/`,
`/same-day-tech-delivery/`, `/how-to-reset-frozen-smartwatch/`. Zero-click generic and off-topic queries found in the
data join this list.

### Page ownership rules for planned pages
- The device page owns device-specific searches; the parent hub owns any-device searches. When the iPhone hub
  (2.5), Samsung hub (2.6), MacBook page (2.8) or Apple Watch retitle (2.9) goes live, its device queries move out
  of S1, S6, S7 or S8, and the hub's copy stops targeting them.
- Sub-service pages (battery, charging port, water damage, back glass) are indexed from launch and own their fault
  cluster; the matching blog guide is re-angled to the informational question.
- Location pages own neighbourhood searches; service pages never target a neighbourhood.

## 2. Ignore list (proposed; owner to confirm)
Never a target, never edited or merged, never counted as a competing page. If one of these ranks for a cluster, treat
the cluster as "none of our pages ranks".
- Theme demo pages: `/layouts/*`, and any `/electronics-repair-*` or `/electronics-store-*` URL
- `/category/uncategorized/` (noindexed) and `/blog-standard/` (301 pending, backlog 1.5)
- WooCommerce system URLs: cart, checkout, my-account, `?add-to-cart=`, `?quick-view=`
- Any URL with a query string

Posts published daily by the Soro "SEO Autopilot" plugin are real pages on our domain and are **not** ignored:
cluster each new one every month and check it against R7.

## 3. Content rules (apply the first that fits)
| Rule | When | Action | Risk |
|---|---|---|---|
| R1 Snippet | pos ≤ 3, ≥ 30 impr, CTR < 3% | Rewrite the title and meta description | L |
| R2 Striking distance | pos 4–10, ≥ 20 impr | Primary keyword in title, H1 and first 100 words; 40–60 word direct answer; supporting keywords as H2s; 2–3 exact-anchor internal links in | meta/links L · copy H |
| R3 Expand | pos 11–20 | Add the sections the supporting keywords ask for (turnaround, brands, FAQ, price-from only if confirmed) plus internal links | H |
| R4 Rewrite/rethink | pos > 20, ≥ 50 impr | Check intent against page one; rewrite or retarget | H |
| R5 Slipped | down ≥ 3 positions MoM, ≥ 20 impr | Find the cause first (ranking URL changed? noindex? recent edit? Soro post?), then revert or refresh | depends |
| R6 Wrong page | ranking URL ≠ target | Exact-anchor internal links to the target; align its title and H1; never weaken a page ranking ≤ 3 | links L · copy H |
| R7 Cannibalised | two or more of our URLs on one cluster | Keep the best, merge, 301 the rest | H + L |
| R8 Gap | ≥ 30 impr/month and no page, or a strategic local cluster | Write a page brief (Phase 2 drafts count) | H |

**Guardrails**
- At most 4 content refreshes a month (R2–R4, R7), highest impressions first. Meta and link changes do not count.
- 28-day cool-down per page after any change.
- Copy uses only facts in `instatech/claims.md`, and only those marked as confirmed by the owner.
- Tag every action with rule and cluster ID, for example `R2 · S2`.
- The autonomy rule applies: scheduled runs draft and propose; nothing goes live without the owner's explicit yes.
  L-class changes can ship through the Tuesday fix run once approved; H-class changes are staged as proposals.

## 4. Decisions
| Date | Decision | By |
|---|---|---|
| 21 Oct 2026 | Clusters live in this file, inside the existing programme; no parallel system | Claude (skill setup) |
| 21 Oct 2026 | October is the baseline month; R5 starts with the December review (November vs October) | Claude (skill setup) |
| 21 Oct 2026 | Q1 `/buy-sell-phones/` owns trade-in (S9); `/phone-accessories-trade-in/` is retargeted to accessories (S11) | Owner |
| 21 Oct 2026 | Q2 Tablet and iPad repairs are done at both shops; `/tablet-repairs/` targets London, not Bloomsbury only | Owner |
| 21 Oct 2026 | Q3 Data recovery is a paid service; it gets a service page (R8 · S10) | Owner |
| 21 Oct 2026 | Warranty period depends on the repair; current parts wording stands (`claims.md` C6, C10) | Owner |
| — | Q4 Confirm the ignore list in section 2 | **Owner** |

## 5. Monthly cluster review (procedure)
Runs in the monthly review, straight after the Search Console pull and before the plan is written.
1. **Pull.** Search Console Performance, last 28 days vs the previous 28, by query and by page, with all four
   metrics. Routes, in order of preference: (a) the Search Console connector, if connected; (b) the browser report
   driven by URL (`resource_id`, `breakdown=query|page`, start/end and compare dates), with the DOM table read by
   JavaScript, since it holds every row whatever the rows-per-page setting; (c) the owner's CSV export, saved to
   `instatech/data/gsc/YYYY-MM-queries.csv` and `YYYY-MM-pages.csv`. Keep queries with ≥ 8 impressions, mapped
   to `query | clicks | impr | pos | imprPrev | posPrev` and sorted by impressions. Drop ignored URLs first.
2. **Re-cluster.** Assign every kept query to a cluster above; add Soro posts and new pages; confirm or replace
   the seed primaries with the highest-impression query in each cluster.
3. **Find ranking URLs.** For each cluster, record the URL ranking today and flag ranking ≠ target (R6), two of our
   URLs competing (R7), and demand with no page (R8).
4. **Apply the rules** in section 3, first match wins, within the guardrails.
5. **Write actions** into `instatech/backlog.md` Phase 5 as numbered items with rule, cluster, risk and status, and
   add them to the refresh queue below.
6. **Fill in last month's results** in the refresh queue (position and impressions, before → after).
7. **Save this file**, with the figures in section 1 updated, and commit.

## 6. Refresh queue
| Cluster | Rule | Action | Backlog item | Last changed | Result next month (pos / impr before → after) |
|---|---|---|---|---|---|
| S9/S11 | R7 | Retarget `/phone-accessories-trade-in/` to accessories; trade-in stays on `/buy-sell-phones/` | 5.3 | — | — |
| S7 | Owner decision Q2 | `/tablet-repairs/` title, meta and H1 cover both shops | 5.6 | — | — |
| S10 | R8 | Data recovery service page | 5.7 | — | — |
