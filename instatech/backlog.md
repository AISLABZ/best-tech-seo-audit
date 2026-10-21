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
| 1.1 | Link `/mobile-repair-services/screen-repair/` from the menu, footer, homepage hero and location pages | todo | Elementor and menu change. Draft the exact placement for approval |
| 1.2 | Homepage H1 → "Phone, laptop and tablet repair in central London — same day, walk-in"; keep the Oxford Circus message as a banner or H2. Service-page H1s should lead with the searched phrase | todo | Elementor change. Draft for approval |
| 1.3 | Repoint 17 dead or redirecting links in 12 posts | verified | Done by the mu-plugin. Fix permanently in post content when convenient |
| 1.4 | Noindex `/layouts/*` and `/category/uncategorized/` | verified | Done by the mu-plugin. Deleting the demo pages and re-categorising posts still needs approval |
| 1.5 | 301 `/blog-standard/` to a proper blog hub | todo | Confirm the target with the owner first. It currently serves as the blog listing |
| 1.6 | Meta descriptions for categories and products | verified | Fallback template by mu-plugin. Hand-write the top 10 product categories next |
| 1.7 | Fix category name casing ("USB-C HUBS", "ETHERNET Cables", "For C-C phones", "MacBook/Laptop charger") | todo | Term rename. Draft for approval |
| 1.8 | Make the 19 duplicate product titles unique (`-2` duplicates) | todo | Check whether the `-2` products are true duplicates, and propose a merge with a 301 or a variant name |
| 1.9 | Image alt text (972 missing at baseline) | live | The mu-plugin covers attachment images. Re-measure on the Monday crawl |
| 1.10 | Link About Us from the header or footer; add named technicians, experience and warranty | todo | About Us has 0 inlinks. Needs owner facts |
| 1.11 | Entity: one spelling ("InstaTech") everywhere, including GBP names; Maps CID links in the schema; full MobilePhoneStore node on each location page; Store schema on Oxford Circus | todo | sameAs is done by the mu-plugin. Needs GBP share links from the owner |
| 1.12 | Performance: LiteSpeed JS delay for GTM, remove unused CSS, dequeue TI Wishlist and Advanced Popups off-shop | todo | Settings change. Draft for approval, and verify with Lighthouse |
| 1.13 | Search Console: confirm ownership and submit `/sitemap_index.xml` | blocked | Owner to confirm GSC access |
| 1.14 | Lighthouse: links not crawlable (`href="#"`), tap targets, contrast | todo | Identify the elements and draft fixes |
| 1.15 | Elementor Pro security update (4.2.0 → ≥ 4.2.2) | live | Requested 21 Oct; confirm the version on the next run |
| 1.16 | Review the Soro "SEO Autopilot" plugin output: posts publish daily and earlier ones contained theme-demo links | todo | Check that new posts link to money pages, not demo URLs |

## Phase 2: money pages (draft as WordPress drafts or repo files for approval)
| # | Page | Status | Needs from owner |
|---|---|---|---|
| 2.1 | Battery replacement | todo | Prices by model, turnaround, warranty, parts grade |
| 2.2 | Charging port repair | todo | Same |
| 2.3 | Water damage repair | todo | Same, plus diagnostic fee policy |
| 2.4 | Back glass repair | todo | Same |
| 2.5 | iPhone repair hub | todo | Price matrix |
| 2.6 | Samsung repair hub | todo | Price matrix |
| 2.7 | iPad repair (consolidate with `/tablet-repairs/`) | todo | — |
| 2.8 | MacBook repair | todo | Price matrix |
| 2.9 | Apple Watch repair (retitle the smartwatch page) | todo | — |
| 2.10–2.13 | iPhone 16, 15, 14 and 13 series model pages | todo | Per-fault prices |
| 2.14 | Cannibalisation review: `/phone-screen-repair-cost/`, `/tablet-screen-repair-near-me/`, `/desktop-computer-repair-near-me/`, `/laptop-repair-near-me-what-to-check-first/` | todo | GSC data preferred |
| 2.15 | Deepen location pages with nearby areas, station directions and shop reviews | todo | — |

## Phase 3: local prominence
| # | Item | Status |
|---|---|---|
| 3.1 | Full GBP content for Bloomsbury, Moorgate and Oxford Circus (categories, services, prices, attributes, photos) | todo |
| 3.2 | Oxford Circus GBP verified before opening; lead with Sunday opening | blocked: owner action |
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

## Needs from owner
- Repair price matrix by model and fault, plus warranty, turnaround and parts-grade policy
- Google Maps share or CID links for each shop's Google Business Profile, and confirmation of Search Console access
- Technician names and experience for About Us
- Approval on items marked "drafted"
