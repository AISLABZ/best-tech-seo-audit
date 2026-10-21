# Best Tech Repair: keyword clusters, October 2026 update (laptop-led)

**Site:** https://best-tech.co.uk (Webflow) · **Shop:** Unit 4, Piccadilly Circus Underground Station, London W1J 9HS
**Prepared:** 21 October 2026, AiS LABZ · **Status:** merge pack for the "Best tech website" project docs

> **How to use this file.** Best Tech already has a programme of record in the claude.ai project
> "Best tech website": `clients/best-tech-keyword-clusters.md`, `clients/best-tech-tracked-keywords.md`,
> `clients/best-tech-confirmed-claims.md`, the newest `clients/best-tech-game-plan-YYYY-MM.md` and
> `clients/seo-monthly-report-runbook.md`. The growth-engine task (`trig_01UcG691KzdRVuDx1ZNbYcEE`, Mon/Thu
> 10:00 am London) reads those documents. This session could not reach the Projects tool, so this file is **not a
> parallel system**: sections 2–7 below are written to be merged into those five documents, section by section.
> Cluster IDs use the prefix **L** (laptop) and **D** (other devices and services) so they don't collide with IDs
> already in the project doc. If an existing cluster already covers one of these, keep its ID and add the
> supporting keywords to it.

---

## 0. The finding that shapes everything

**The laptop hub `/works/laptop-repair` gets almost no internal link equity from the 19 laptop and MacBook posts
written to support it.** Only 2 of the 19 link to it with the anchor "laptop repair". Ten have no link to it in
the body at all (only the site-wide footer), and the other seven use generic anchors: "repair service",
"professional inspection", "the laptop itself", "will not power on". Meanwhile two posts target the hub's own
commercial intent: `/post/macbook-repair-near-me-london` and `/post/how-to-find-a-laptop-repair-shop-near-me`.
That sets up a wrong-page (R6) and cannibalisation (R7) pattern before any ranking data arrives.

The fix is mostly class L (anchors and links), so it costs no content-refresh slot. It is the first action below.

## 1. Data status and method

| Item | Status |
|---|---|
| Search Console property | `sc-domain:best-tech.co.uk`, owned by susman2005@gmail.com |
| Pull this session | **Not possible.** The GSC connector failed to connect, the Ahrefs plan does not cover GSC data, Semrush has no API units, and this cloud session has no Chrome bridge to SaM's Mac. |
| Consequence | This is the **structural baseline**: the cluster map, target URLs and pre-ranking flags come from a live crawl of all 73 sitemap URLs (21 Oct 2026). Impressions and positions are marked `pending` and are filled in on the first GSC pull. |
| "Slipped" rule (R5) | Starts the month **after** the first GSC pull. The first pull is the baseline. |
| Ignore list | `/blog?post=` (Soro auto-blog embed copies). Never a target, never edited or merged, never counted as a competing page. If one ranks for a cluster, record it as "none of our pages ranks". |

**Query-pull method (for the runbook):** Search Console → Performance, driven by URL: `resource_id=sc-domain:best-tech.co.uk`,
`breakdown=query` and then `breakdown=page`, last 28 days with compare = previous 28, all four metrics on. Read the
DOM table with `javascript_tool`. It holds every row, whatever the rows-per-page setting. Columns: `name, clicks,
clicksPrev, clicksDiff, impr, imprPrev, imprDiff, ctr, ctrPrev, ctrDiff, pos, posPrev, posDiff`. Keep queries with
≥ 8 impressions, map each to `query | clicks | impr | pos | imprPrev | posPrev`, sort by impressions, and return the
rows in ~1,000-character slices. Strip `?`, `=` and `/` from anything returned, because the bridge blocks query
strings. Drop ignored URLs before analysis.

## 2. Cluster map → merge into `clients/best-tech-keyword-clusters.md`

Rules: one cluster = one page. A device page owns device-specific searches; the parent hub owns any-device
searches. The two never target the same cluster.

### 2a. Laptop clusters (priority)

| ID | Kind | Primary keyword | Target URL | Supporting keywords | Ranking URL today | Rule / flag |
|---|---|---|---|---|---|---|
| **L1** | Commercial hub | laptop repair london | `/works/laptop-repair` | laptop repair near me · laptop repair shop london · same day laptop repair london · laptop repair piccadilly · windows laptop repair london · laptop keyboard repair london · laptop charging port repair london · laptop repair central london | pending | **R6 risk:** `/post/how-to-find-a-laptop-repair-shop-near-me` targets "laptop repair shop near me". Re-angle it to "how to choose" and point it at L1. **R2 prep:** H1 is just "Laptop Repair" (no "London"); no visible FAQ; MacBook named once in the body. |
| **L2** | Commercial device | macbook repair london | MacBook device page if it exists unindexed in Webflow (backlog item 30); otherwise **R8 gap** brief for `/works/laptop-repair/macbook-repair` | macbook repair near me · macbook pro repair london · macbook air repair london · apple laptop repair london | pending | **R7 risk:** `/post/macbook-repair-near-me-london` is a blog post targeting a commercial device query. Keep it as the interim owner until a device page is live, then re-angle it and 301 nothing (it stays as a supporting post). |
| **L3** | Commercial sub-service | laptop screen replacement london | `/post/laptop-screen-repair-fix-or-replace` (interim) → R8 candidate if GSC shows ≥ 30 impr/month | laptop screen repair · cracked laptop screen · laptop screen repair cost · macbook screen repair cost | pending | `/services/screen-replacement` stays the any-device screen hub. Don't retarget it at laptops. `/post/macbook-screen-repair-cost` is a supporting post; **prices are not confirmed**, so no "from £" copy. |
| **L4** | Commercial sub-service | laptop battery replacement london | `/post/laptop-battery-replacement-guide-london` | laptop battery replacement · laptop not holding charge · macbook battery replacement (supporting post `/post/macbook-battery-replacement-when-to-act`) | pending | `/services/battery-replacement` stays the any-device battery hub. |
| **L5** | Commercial specialist | macbook logic board repair | `/post/macbook-logic-board-repair-explained` | macbook motherboard repair london · macbook not turning on · board level repair london | pending | Claim confirmed 21 Oct (in-house board-level work), so the copy can say so. |
| **L6** | Commercial specialist | macbook liquid damage repair | `/post/macbook-liquid-damage-repair` | spilled water on macbook · laptop water damage repair london | pending | Separate from the phone water-damage posts. |
| **L7** | Commercial sub-service | laptop diagnostics london | `/post/same-day-laptop-diagnostics` | free laptop diagnostic · laptop not turning on · same day laptop diagnostics | pending | "Free diagnostic" is already live on the hub. Confirm it in the register (Q-L4). |
| **L8** | Commercial sub-service | laptop software repair | `/post/laptop-software-troubleshooting-service` | laptop virus removal · laptop software troubleshooting · windows reinstall london | pending | `/services/software-fixing` stays the any-device software hub. |
| **L9** | Informational | why is my laptop overheating | `/post/why-is-my-laptop-overheating` | laptop fan loud (`/post/why-is-my-laptop-fan-loud`) · laptop getting hot · laptop fan noise | pending | **R7 watch:** two posts on one intent. If both rank on the same queries, merge the fan post into the overheating post and 301 it. |
| **L10** | Informational | how to fix a slow laptop | `/post/how-to-fix-slow-laptop` | laptop running slow · old macbook slow (`/post/how-to-fix-older-macbook-problems`) | pending | |
| **L11** | Informational / data | laptop data recovery | `/post/laptop-data-recovery-guide` | recover files from dead laptop · laptop hard drive recovery london | pending | `/services/data-recovery` stays the any-device hub. |
| **L12** | Informational | laptop repair or replace | `/post/laptop-repair-or-replacement` | is it worth repairing a laptop · laptop repair vs new | pending | |
| **L13** | Commercial | sell my laptop london | `/post/sell-my-laptop-london-guide` (interim) → **R8 gap**: no buy/trade-in page exists | sell macbook london · sell laptop for cash london | pending | Unlocked 21 Oct: SaM confirmed Best Tech buys used devices. |

`/post/how-to-repair-laptop-in-home-safely` and `/post/top-notch-mobile-and-laptop-repair-services-in-london` are
supporting posts only. Each links to L1 with an exact anchor, and neither owns a cluster.

### 2b. Other device, service, local and brand clusters

| ID | Kind | Primary keyword | Target URL | Notes |
|---|---|---|---|---|
| D1 | Commercial hub | mobile phone repair london | `/works/mobile-phone-repair` | iPhone/Samsung/Pixel device searches belong to device pages, not this hub. `/post/iphone-repair-london-fast-fixes` and `/post/samsung-galaxy-repair-near-me-london` are R7 watch items. |
| D2 | Commercial hub | ipad repair london | `/works/tablet-repair` | Supporting: tablet repair london, ipad screen repair. `/post/ipad-and-tablet-repair-done-fast` is supporting. |
| D3 | Commercial hub | apple watch repair london | `/works/smartwatch-repair` | Supporting: smartwatch repair london, apple watch screen repair. |
| D4 | Any-device service | screen replacement london | `/services/screen-replacement` | Any-device only. Device screens go to L3 / D1 / D2. |
| D5 | Any-device service | battery replacement london | `/services/battery-replacement` | Any-device only. |
| D6 | Any-device service | phone camera repair london | `/services/camera-speaker-repair` | Supporting: phone speaker repair. |
| D7 | Any-device service | data recovery london | `/services/data-recovery` | |
| D8 | Any-device service | phone software repair | `/services/software-fixing` | |
| D9 | Hyperlocal | phone repair piccadilly circus | `/` (homepage) | Supporting: phone repair near me, laptop repair piccadilly (→ L1 if laptop-specific). |
| D10 | Hyperlocal | phone repair leicester square | `/post/phone-repair-near-leicester-square-soho-covent-garden` | **Decision needed:** Covent Garden Tech (another AiS LABZ client) owns Covent Garden / WC2 terms. Keep D10 to Leicester Square and Soho. |
| D11 | Commercial | sell my phone london | `/post/how-to-sell-my-phone-safely` (interim) | Same R8 gap as L13. One "sell your device" page should own both. |
| B1 | Brand | best tech piccadilly | `/` | Report only. |
| — | Orphans | zero-click generics, off-topic, currency-exchange queries | — | Report only. The GBP "Currency exchange service" category may pull these in. |

## 3. Content rules (unchanged from the project doc; apply the first that fits)

| Rule | When | Action | Risk |
|---|---|---|---|
| R1 Snippet | pos ≤ 3, ≥ 30 impr, CTR < 3% | rewrite title + meta description | L |
| R2 Striking distance | pos 4–10, ≥ 20 impr | primary keyword in title/H1/first 100 words, 40–60-word direct answer, supporting keywords as H2s, 2–3 exact-anchor internal links in | meta/links L · copy H |
| R3 Expand | pos 11–20 | add the sections the supporting keywords ask for (turnaround, brands, FAQ, price-from only if confirmed) + internal links | H |
| R4 Rewrite/rethink | pos > 20, ≥ 50 impr | check intent against page one; rewrite or retarget | H |
| R5 Slipped | down ≥ 3 positions MoM, ≥ 20 impr | find the cause first (ranking URL changed? noindex? recent edit?), then revert or refresh | depends |
| R6 Wrong page | ranking URL ≠ target | exact-anchor internal links to the target, align its title/H1; never weaken a page ranking ≤ 3 | links L · copy H |
| R7 Cannibalised | two or more of our URLs on one cluster | keep the best, merge, 301 the rest | H + L |
| R8 Gap | ≥ 30 impr/month and no page, or a strategic local cluster | write a page brief | H |

**Guardrails:** at most 4 content refreshes a month (R2–R4, R7), highest impressions first; meta and link changes
don't count. 28-day cool-down per page. Only facts from the confirmed-claims register. Every action is tagged with
rule + cluster ID (e.g. `R6 · L1`).

## 4. Refresh queue and actions → merge into the game plan backlog

The October content-refresh budget is held for the first GSC pull; the items below are link and structure work
(class L) plus staged H items. Numbering continues from the project backlog's last item. Each item is shown here as
**KC-n**; renumber on merge.

| # | Cluster · rule | Action | Risk | Status | Last changed | Result next month |
|---|---|---|---|---|---|---|
| KC-1 | `R6 · L1` | Add one in-body exact-anchor link to `/works/laptop-repair` ("laptop repair in London" / "laptop repair at Piccadilly Circus") in the 10 laptop posts with no body link: how-to-find-a-laptop-repair-shop-near-me, macbook-repair-near-me-london, laptop-repair-or-replacement, why-is-my-laptop-overheating, macbook-logic-board-repair-explained, macbook-battery-replacement-when-to-act, how-to-repair-laptop-in-home-safely, laptop-software-troubleshooting-service, how-to-fix-older-macbook-problems, top-notch-mobile-and-laptop-repair-services-in-london. Resubmit the whole rich-text field, one item per call, and byte-compare before publishing. | L | todo (needs SaM's yes before any site write in this session) | — | — |
| KC-2 | `R6 · L1` | Re-anchor the 7 generic in-body links ("repair service", "professional inspection", "battery, storage and screen", "repair assessment", "the laptop itself", "will not power on", "diagnose laptop faults") to descriptive laptop-repair anchors. Change the 5 `https://www.best-tech.co.uk/…` links (and the 2 absolute apex links) to the apex root-relative `/works/laptop-repair`; www is a redirect hop. | L | todo | — | — |
| KC-3 | `R6 · L1` | `/post/how-to-find-a-laptop-repair-shop-near-me`: retitle to a "how to choose" angle (e.g. "How to Choose a Laptop Repair Shop: 7 Checks") so it stops competing with L1 for "laptop repair near me". Meta is L; title/H1 is H. | L + H | staged | — | — |
| KC-4 | `R2 prep · L1` | Laptop hub on-page: H1 "Laptop Repair" → "Laptop Repair in London — Piccadilly Circus" (H); add a visible FAQ from real questions (turnaround, MacBook vs Windows, data safety, board-level work, warranty without a length) with FAQPage schema (H copy + L schema); add MacBook/board-level wording now that the claim is confirmed (H). Counts as 1 of 4 refreshes once GSC confirms pos 4–20. | H | staged; waiting for GSC position | — | — |
| KC-5 | `R8 · L2` | Check Webflow for an unindexed MacBook device page (backlog item 30). If it exists, it becomes the L2 target and needs SaM's indexing go. If not, write the brief for `/works/laptop-repair/macbook-repair`. | H | todo | — | — |
| KC-6 | `R8 · L13 + D11` | Brief one "Sell your phone or laptop" page (buying confirmed 21 Oct). The two sell guides become supporting posts linking to it. **Needs:** what devices are bought, how valuation works, payment method. | H | todo, needs SaM inputs | — | — |
| KC-7 | `R7 watch · L9` | After the first GSC pull: if `/post/why-is-my-laptop-fan-loud` and `/post/why-is-my-laptop-overheating` rank on the same queries, merge the fan post into the overheating post and 301 it. | H + L | watch | — | — |
| KC-8 | `R7 watch · L2` | After the first GSC pull: check whether `/post/macbook-repair-near-me-london` outranks the L1 hub for "macbook repair london". If it does, apply R6 to the MacBook target once it exists. | — | watch | — | — |

**Change-log line (game plan):** `21 Oct 2026 — Keyword-cluster engine set up (L1–L13 laptop, D1–D11, B1). Structural
baseline from live crawl; GSC pull pending (connector down, no Chrome bridge). Added KC-1…KC-8. Laptop hub internal
links identified as the lead issue: 2 of 19 laptop posts link to it with an exact anchor.`

## 5. Tracked keywords → merge into `clients/best-tech-tracked-keywords.md`

Add each primary, tagged with its cluster ID (position and impressions filled in on the first pull):

| Keyword | Cluster | Target URL |
|---|---|---|
| laptop repair london | L1 | /works/laptop-repair |
| laptop repair near me | L1 | /works/laptop-repair |
| same day laptop repair london | L1 | /works/laptop-repair |
| macbook repair london | L2 | device page / gap |
| laptop screen replacement london | L3 | /post/laptop-screen-repair-fix-or-replace |
| laptop battery replacement london | L4 | /post/laptop-battery-replacement-guide-london |
| macbook logic board repair | L5 | /post/macbook-logic-board-repair-explained |
| macbook liquid damage repair | L6 | /post/macbook-liquid-damage-repair |
| laptop diagnostics london | L7 | /post/same-day-laptop-diagnostics |
| laptop software repair | L8 | /post/laptop-software-troubleshooting-service |
| why is my laptop overheating | L9 | /post/why-is-my-laptop-overheating |
| how to fix a slow laptop | L10 | /post/how-to-fix-slow-laptop |
| laptop data recovery | L11 | /post/laptop-data-recovery-guide |
| laptop repair or replace | L12 | /post/laptop-repair-or-replacement |
| sell my laptop london | L13 | /post/sell-my-laptop-london-guide |
| mobile phone repair london | D1 | /works/mobile-phone-repair |
| ipad repair london | D2 | /works/tablet-repair |
| apple watch repair london | D3 | /works/smartwatch-repair |
| screen replacement london | D4 | /services/screen-replacement |
| battery replacement london | D5 | /services/battery-replacement |
| phone repair piccadilly circus | D9 | / |
| phone repair leicester square | D10 | /post/phone-repair-near-leicester-square-soho-covent-garden |

Re-tag any keyword already in the doc with its cluster ID from section 2.

## 6. Confirmed claims → merge into `clients/best-tech-confirmed-claims.md`

Confirmed by SaM in this session, 21 Oct 2026:

| Q | Claim | Status | Copy rule |
|---|---|---|---|
| Q-L1 | Services: laptop repair, screen repair, battery repair, smartwatch repair and all other listed services | Confirmed | Already live on the hubs |
| Q-L2 | Best Tech **buys used devices** | Confirmed | May be used; valuation method and payment terms still open |
| Q-L3 | **Same-day laptop repair** on common jobs (screen, battery, diagnostics) | Confirmed | Say "same day on most jobs", which matches the live hub. Never promise a time for every repair. |
| Q-L4 | **MacBook logic-board / board-level and liquid-damage repair** in-house | Confirmed | May be used on L1, L2, L5, L6 |
| Q-L5 | A **repair warranty** is offered | Confirmed (offered) | **Length still PARKED.** Say "warranty on repairs" with no duration until SaM confirms one. |

Still open: prices / price-from (blocks "from £" copy on L3 and `/post/macbook-screen-repair-cost`), warranty length,
the trade-in valuation method.

## 7. Monthly run → merge into the runbook and engine doc

**Runbook (`clients/seo-monthly-report-runbook.md`):** add step **"Keyword-cluster review"** directly after the
Search Console pull:

1. Pull queries and pages (method in section 1; ignore `/blog?post=`).
2. Re-cluster queries with ≥ 8 impressions into existing L/D/B clusters; new ID only if none fits.
3. Record each cluster primary's ranking URL; flag ranking ≠ target, two of our URLs on one cluster, and demand
   with no page.
4. Apply R1–R8 (first that fits); max 4 refreshes; 28-day cool-down; facts only from the register.
5. Write the actions into the game plan's content workstream, tagged `R# · ID`.
6. Fill in last month's refresh queue "Result next month" (before → after: position, impressions, clicks).
7. Save the clusters doc and the tracked-keyword doc.

**Monthly report:** a "Refreshes before → after" table, plus one snapshot line, e.g. "Laptop hub L1: pos x → y,
impressions a → b after KC-1/KC-2 links."

**Scheduled tasks:** the growth engine (`trig_01UcG691KzdRVuDx1ZNbYcEE`) already runs the monthly re-cluster with
R1–R8 and the `/blog?post=` exclusion, reading `clients/best-tech-keyword-clusters.md`. Once sections 2–6 are merged
into that doc, it picks this up with no prompt change. The Best Tech month-end report task was not located in this
session, so it was **not edited**. Its prompt should say: "read `clients/best-tech-keyword-clusters.md` and run the
keyword-cluster review before writing the game plan." Note: the growth engine's last run (19 Oct) failed on a usage
limit, and its prompt still names the older "work" browser lock rather than the account-based rule the other
clients moved to on 17–20 Oct.

## 8. Publishing

- Class L (KC-1, KC-2, meta in KC-3, schema in KC-4) can ship through the Monday/Thursday engine run.
- Class H (copy, H1s, new pages, merges, indexing of device pages) is staged.
- **Nothing in this file has been applied to best-tech.co.uk.** Every change needs SaM's explicit yes on the exact
  before → after first.
