# InstaTech SEO backlog

This file is the single source of truth for the growth engine. Scheduled runs read it, work the next item for their day,
and update it. Statuses:
- `todo`
- `drafted` (proposal ready in the repo, awaiting the owner)
- `approved`
- `live` (deployed)
- `verified` (confirmed by re-crawl)
- `blocked` (waiting on the owner; the reason is given)

**Autonomy rule (set by the owner, 21 Oct 2026):** scheduled runs draft and propose only. Nothing is changed on the live
site without the owner's explicit approval in a conversation. Approved changes are deployed and logged in `changelog.md`.

## Phase 1: fix the leaks
| # | Item | Status | Notes |
|---|---|---|---|
| 1.1 | Link `/mobile-repair-services/screen-repair/` from the menu, footer, homepage hero and location pages | verified | Header, mobile and footer links are live via plugin v1.1.0 (4 per page). Contextual links from location pages and posts are still todo |
| 1.2 | Homepage H1 → "Phone, laptop and tablet repair in central London — same day, walk-in"; keep the Oxford Circus message as a banner or H2. Service-page H1s should lead with the searched phrase | live | The homepage H1 now carries the service line (v1.1.0). Service-page H1s ("ProfessionalMobile RepairServices" etc.) are still todo. Draft for approval |
| 1.3 | Repoint 17 dead or redirecting links in 12 posts | verified | Done by the mu-plugin. Fix permanently in post content when convenient |
| 1.4 | Noindex `/layouts/*` and `/category/uncategorized/` | verified | Done by the mu-plugin. Deleting the demo pages and re-categorising posts still needs approval |
| 1.5 | 301 `/blog-standard/` to a proper blog hub | todo | Confirm the target with the owner first. It currently serves as the blog listing |
| 1.6 | Meta descriptions for categories and products | verified | Fallback template by mu-plugin. Hand-write the top 10 product categories next |
| 1.7 | Fix category name casing ("USB-C HUBS", "ETHERNET Cables", "For C-C phones", "MacBook/Laptop charger") | todo | Term rename. Draft for approval |
| 1.8 | Make the duplicate product titles unique (`-2` duplicates) | approved, not deployed | 18 pairs found (`audit-2026-10-21/`). 12 have identical price and stock: 301s are built in `wp/mu-plugins/instatech-audit-fixes.php` v1.0.0 (approved by owner 21 Oct, awaiting deploy). 6 pairs have **different prices** and are held for the owner: A12 splitter £14.99/£19.99, A32 adapter £9.99/£12.99, J2 USB-C–HDMI £24.99/£29.99, QUATRE hub £29.99/£44.99, Smart Watch USB-C cable £19.99/£24.99, World Travel Adapter £44.99/£34.99 (`-2` price first). Permanent fix: trash the `-2` products in WP Admin once the 301s are live |
| 1.9 | Image alt text (972 missing at baseline) | live | The mu-plugin covers attachment images. Re-measure on the Monday crawl |
| 1.10 | Link About Us from the header or footer; add named technicians, experience and warranty | live | Footer link is live (v1.1.0). Content still needs owner facts |
| 1.11 | Entity: one spelling ("InstaTech") everywhere, including GBP names; Maps CID links in the schema; full MobilePhoneStore node on each location page; Store schema on Oxford Circus | live | sameAs (v1.0) and Maps cid links plus pinned directions (v1.2) are live. Still to do: rename the GBP listings from "instaTech - (Bloomsbury)" and "instaTech - Moorgate" to "InstaTech Bloomsbury" and "InstaTech Moorgate" (owner, in GBP); a full MobilePhoneStore node on each location page |
| 1.18 | Remove `/shop/` from `product-sitemap.xml` (it is also in `page-sitemap.xml`) | approved, not deployed | In `instatech-audit-fixes.php` v1.0.0; it also turns off Rank Math sitemap caching so the change takes effect |
| 1.19 | Product schema: strip the " - InstaTech" suffix from Product `name` | approved, not deployed | In `instatech-audit-fixes.php` v1.0.0. Brand, SKU, GTIN, shipping and returns still need owner data |
| 1.20 | Uncached TTFB of 2.8–3.2 s: enable LiteSpeed Crawler; review Object Cache (`object-kind: false` in `.litespeed_conf.dat` despite an `object-cache.php` drop-in) | todo | WP Admin → LiteSpeed Cache → Crawler / Cache → Object. No API route to these settings |
| 1.21 | Plugin updates available: ElementsKit Lite, Essential Addons, Essential Blocks, LiteSpeed Cache, Templately | todo | Take a backup first: there is no on-server UpdraftPlus archive (last activity was the 18 Sep restore) |
| 1.17 | Google review links for the review engine: Bloomsbury https://search.google.com/local/writereview?placeid=ChIJg5Ii0NUbdkgRQL_2omA3r5M · Moorgate https://search.google.com/local/writereview?placeid=ChIJm5ZiHwAddkgRICvcMAd8o3Q | ready | Use in the post-repair SMS and email (Phase 3.3), and on receipts or QR cards in-store |
| 1.12 | Performance: LiteSpeed JS delay for GTM, remove unused CSS, dequeue TI Wishlist and Advanced Popups off-shop | todo | Settings change. Draft for approval, and verify with Lighthouse |
| 1.13 | Search Console: confirm ownership and submit `/sitemap_index.xml` | blocked | Owner to confirm GSC access |
| 1.14 | Lighthouse: links not crawlable (`href="#"`), tap targets, contrast | todo | Identify the elements and draft fixes |
| 1.15 | Elementor Pro security update (4.2.0 → ≥ 4.2.2) | blocked | The Hostinger update job did not apply, most likely a licence issue. Owner to update via WP Admin → Elementor → License / Plugins |
| 1.16 | Review the Soro "SEO Autopilot" plugin output: posts publish daily and earlier ones contained theme-demo links | todo | Check that new posts link to money pages, not demo URLs |

## Phase 2: money pages (draft as WordPress drafts or repo files for approval)
| # | Page | Status | Needs from owner |
|---|---|---|---|
| 2.1 | Battery replacement | drafted | `instatech/pages/battery-replacement.md`. Needs per-model prices, warranty period, parts wording ("genuine" vs "meets OEM spec" is inconsistent on the live site) and the genuine Apple battery option |
| 2.2 | Charging port repair | todo | Same |
| 2.3 | Water damage repair | todo | Same, plus diagnostic fee policy |
| 2.4 | Back glass repair | todo | Same |
| 2.5 | iPhone repair hub | todo | Price matrix |
| 2.6 | Samsung repair hub | todo | Price matrix |
| 2.7 | iPad repair (consolidate with `/tablet-repairs/`) | todo | — |
| 2.8 | MacBook repair | todo | Price matrix |
| 2.9 | Apple Watch repair (retitle the smartwatch page) | todo | — |
| 2.10–2.13 | iPhone 16, 15, 14 and 13 series model pages | todo | Per-fault prices |
| 2.14 | Cannibalisation review: `/phone-screen-repair-cost/`, `/tablet-screen-repair-near-me/`, `/desktop-computer-repair-near-me/`, `/laptop-repair-near-me-what-to-check-first/` | moved to 5.4 | — |
| 2.15 | Deepen location pages with nearby areas, station directions and shop reviews | todo | — |

## Phase 3: local prominence
| # | Item | Status |
|---|---|---|
| 3.1 | Full GBP content for Bloomsbury, Moorgate and Oxford Circus (categories, services, prices, attributes, photos) | todo |
| 3.2 | Oxford Circus GBP verified before opening; lead with Sunday opening | blocked: owner action. No listing exists on Google Maps as of 21 Oct 2026. Create it as "InstaTech Oxford Circus" at 22 Great Castle St W1G 0HY |
| 3.3 | Review-request SMS and email templates (all customers, no incentives) | todo |
| 3.4 | Citations with identical business details: Apple Business Connect, Bing Places, Yell, Yelp, Thomson Local, Foursquare, Trustpilot. Tracked in `citations.md` | todo |
| 3.5 | Weekly GBP post per shop | recurring (Thursday run) |

## Phase 4: authority
| # | Item | Status |
|---|---|---|
| 4.1 | Student-discount partnership outreach (UCL, SOAS, Birkbeck) | todo |
| 4.2 | Local business association and BID outreach (Marchmont St, City Road, Oxford Circus area) | todo |
| 4.3 | Data-led PR piece from repair data | todo |
| 4.4 | Two blog posts a month, each linking to a money page | recurring |

## Phase 5: keyword clusters and ranking-driven content
The cluster map, rules and refresh queue are in `keyword-clusters.md`, tracked keywords are in `tracked-keywords.md`, and
copy facts are in `claims.md`. Every action carries its rule and cluster ID. At most 4 content refreshes a month, with a
28-day cool-down per page.

| # | Item | Rule · cluster | Risk | Status | Notes |
|---|---|---|---|---|---|
| 5.1 | Search Console data route for the monthly pull: connector, browser report, or owner CSV export to `instatech/data/gsc/` | — | — | blocked | Same blocker as 1.13. The Search Console connector failed to connect on 21 Oct 2026 |
| 5.2 | Baseline pull and first cluster review: confirm primaries, ranking URLs, R6/R7/R8 flags; fill the refresh queue | all | — | todo | Monthly review, 1 Nov 2026. October is the baseline month; R5 starts in December |
| 5.3 | Retarget `/phone-accessories-trade-in/` to accessories; `/buy-sell-phones/` owns trade-in (owner decision Q1) | R7 · S9/S11 | H + L | drafted | `proposals/2026-10-21-keyword-cluster-decisions.md` §1 |
| 5.4 | Commercial-intent posts competing with service pages: `/phone-screen-repair-cost/` (S2), `/laptop-repair-near-me-what-to-check-first/` and `/desktop-computer-repair-near-me/` (S6), `/tablet-screen-repair-near-me/` (S7), `/guide-to-phone-battery-replacement-uk/` (S3) | R7 · S2/S3/S6/S7 | H + L | todo | Supersedes 2.14. Confirm with the 5.2 data before merging or re-angling |
| 5.5 | Informational overlap: five wireless-charging posts (I1), four power-bank posts (I3), two refurbished posts (I5) | R7 · I1/I3/I5 | H + L | todo | Merge only where the data shows the posts share queries |
| 5.6 | `/tablet-repairs/` title, meta and H1 cover both shops, not Bloomsbury only (owner confirmed, Q2) | S7 | L (title/meta) · H (H1) | drafted | `proposals/2026-10-21-keyword-cluster-decisions.md` §2 |
| 5.7 | Data recovery service page (owner confirmed the service, Q3) | R8 · S10 | H | drafted (brief) | `proposals/2026-10-21-keyword-cluster-decisions.md` §3. Needs a price from the owner |

## Needs from owner
- Repair price matrix by model and fault, plus warranty, turnaround and parts-grade policy
- Google Maps share or CID links for each shop's Google Business Profile, and confirmation of Search Console access
- Technician names and experience for About Us
- Approval on items marked "drafted"
- Keyword clusters: confirm the ignore list (Q4 in `keyword-clusters.md`); data recovery pricing; Moorgate opening hours
- Search Console: a working data route for the monthly pull (connector access, or a monthly CSV export of the query and page reports)

## Backlog change log
- 2026-10-21: Merged the 21 Oct performance and catalogue audit (`audit-2026-10-21/`). Updated 1.8 and added 1.18–1.21.
- 2026-10-21: Added Phase 5 (keyword clusters, items 5.1–5.7), moved 2.14 into 5.4, and created `keyword-clusters.md`, `tracked-keywords.md` and `claims.md`.
- 2026-10-21: Owner decided Q1–Q3 and the warranty and parts wording. 5.3, 5.6 and 5.7 moved to drafted.
