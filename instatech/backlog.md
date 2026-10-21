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

## Programme rules (set by the owner, 21 Oct 2026; apply to every page, post, GBP post, schema and proposal)
1. **No prices.** Never write, add, request or placeholder prices: no "from £X", no price tables, no `offers` or
   `priceSpecification` in schema, no price-led titles or meta descriptions. Lead with speed, free diagnostic,
   no fix no fee, warranty, walk-in 7 days and late opening instead. Do not ask the owner for prices. (Existing price
   mentions already on the live site are the owner's business. Leave them alone, and don't copy them into new content.)
2. **Warranty:** say "warranty on every repair, covering parts and labour; the period depends on the repair and is
   confirmed before work starts." Never state a fixed period.
3. **Parts:** both claims are true and may be used together: "genuine replacement parts and high-quality parts that
   meet or exceed the original specification."
4. **Apple:** keep it general ("we repair iPhones / we replace iPhone batteries"). Don't mention a genuine Apple
   battery option, Apple's own pricing or "unknown part" notices on service pages.

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
| 1.8 | Make the 19 duplicate product titles unique (`-2` duplicates) | todo | Check whether the `-2` products are true duplicates, and propose a merge with a 301 or a variant name |
| 1.9 | Image alt text (972 missing at baseline) | live | The mu-plugin covers attachment images. Re-measure on the Monday crawl |
| 1.10 | Link About Us from the header or footer; add named technicians, experience and warranty | live | Footer link is live (v1.1.0). Content still needs owner facts |
| 1.11 | Entity: one spelling ("InstaTech") everywhere, including GBP names; Maps CID links in the schema; full MobilePhoneStore node on each location page; Store schema on Oxford Circus | live | sameAs (v1.0) and Maps cid links plus pinned directions (v1.2) are live. Still to do: rename the GBP listings from "instaTech - (Bloomsbury)" and "instaTech - Moorgate" to "InstaTech Bloomsbury" and "InstaTech Moorgate" (owner, in GBP); a full MobilePhoneStore node on each location page |
| 1.17 | Google review links for the review engine: Bloomsbury https://search.google.com/local/writereview?placeid=ChIJg5Ii0NUbdkgRQL_2omA3r5M · Moorgate https://search.google.com/local/writereview?placeid=ChIJm5ZiHwAddkgRICvcMAd8o3Q | ready | Use in the post-repair SMS and email (Phase 3.3), and on receipts or QR cards in-store |
| 1.12 | Performance: LiteSpeed JS delay for GTM, remove unused CSS, dequeue TI Wishlist and Advanced Popups off-shop | todo | Settings change. Draft for approval, and verify with Lighthouse |
| 1.13 | Search Console: confirm ownership and submit `/sitemap_index.xml` | blocked | Owner to confirm GSC access |
| 1.14 | Lighthouse: links not crawlable (`href="#"`), tap targets, contrast | todo | Identify the elements and draft fixes |
| 1.15 | Elementor Pro security update (4.2.0 → ≥ 4.2.2) | blocked | The Hostinger update job did not apply, most likely a licence issue. Owner to update via WP Admin → Elementor → License / Plugins |
| 1.16 | Review the Soro "SEO Autopilot" plugin output: posts publish daily and earlier ones contained theme-demo links | todo | Check that new posts link to money pages, not demo URLs |

## Phase 2: money pages (draft as WordPress drafts or repo files for approval)
| # | Page | Status | Needs from owner |
|---|---|---|---|
| 2.1 | Battery replacement | drafted | `instatech/pages/battery-replacement.md`, revised to the programme rules. Owner: confirm the Android brand list, then approve the build |
| 2.2 | Charging port repair | todo | — |
| 2.3 | Water damage repair | todo | — |
| 2.4 | Back glass repair | todo | — |
| 2.5 | iPhone repair hub (faults covered, by model family, with no prices) | todo | — |
| 2.6 | Samsung repair hub | todo | — |
| 2.7 | iPad repair (consolidate with `/tablet-repairs/`) | todo | — |
| 2.8 | MacBook repair | todo | — |
| 2.9 | Apple Watch repair (retitle the smartwatch page) | todo | — |
| 2.10–2.13 | iPhone 16, 15, 14 and 13 series model pages | deferred | Without prices, separate model pages would be thin and close to duplicates. Cover the model families as sections inside the iPhone hub (2.5) instead. Revisit with GSC data if model queries show demand |
| 2.14 | Cannibalisation review: `/phone-screen-repair-cost/`, `/tablet-screen-repair-near-me/`, `/desktop-computer-repair-near-me/`, `/laptop-repair-near-me-what-to-check-first/` | todo | GSC data preferred |
| 2.15 | Deepen location pages with nearby areas, station directions and shop reviews | todo | — |

## Phase 3: local prominence
| # | Item | Status |
|---|---|---|
| 3.1 | Full GBP content for Bloomsbury, Moorgate and Oxford Circus (categories, services without prices, attributes, photos) | todo |
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

## Needs from owner
- (No prices needed. See the programme rules.)
- Confirmation of Search Console access (the GBP links are resolved: see 1.11 and 1.17)
- Technician names and experience for About Us
- Approval on items marked "drafted"
