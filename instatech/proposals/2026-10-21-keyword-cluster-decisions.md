# Proposal: changes from the owner's keyword-cluster decisions (21 Oct 2026)

**Status:** drafted, awaiting owner approval. Nothing here is live.
**Source decisions:** `keyword-clusters.md` section 4 (Q1–Q3) and `claims.md` C6, C10–C14.
Every fact below appears in `claims.md`. The Rank Math fields are set per page in WP Admin → Pages → Edit →
Rank Math → Edit Snippet.

## 1. Trade-in belongs to `/buy-sell-phones/` (backlog 5.3 · R7 · S9/S11)
`/buy-sell-phones/` keeps trade-in unchanged. `/phone-accessories-trade-in/` becomes the accessories landing page
(S11), which stops the two pages competing for trade-in searches. Its existing short "Sell or trade in your phone"
section stays as a pointer.

| Field | Current | Proposed | Risk |
|---|---|---|---|
| SEO title | Phone Accessories and Trade-In in London - InstaTech | Phone Accessories London – Bloomsbury & Moorgate \| InstaTech | L |
| Meta description | Chargers, cables, power banks, earphones and car mounts, plus cash or trade-in for your old phone, at our Bloomsbury and Moorgate shops. Open 7 days. | Chargers, cables, power banks, earphones and car mounts in stock at our Bloomsbury and Moorgate shops, open 7 days. Selling your phone? Get a cash offer. | L |
| H1 | Phone accessories and phone trade-ins in central London | Phone accessories in central London | H |
| "Sell or trade in your phone" section | Present, with 4 links to `/buy-sell-phones/` | Keep it to 2–3 sentences; make one link's anchor exactly "sell your phone for cash" | H (copy) · L (anchor) |

The URL slug keeps `trade-in`. Changing it would need a 301 redirect, which costs more than it gains.

**Verify:** re-crawl both pages; next month, check that trade-in queries rank `/buy-sell-phones/` only.
**Roll back:** restore the current values above.

## 2. `/tablet-repairs/` covers both shops (backlog 5.6 · S7)
The owner confirmed that both shops repair tablets, but the page is currently written for Bloomsbury WC1 only.

| Field | Current | Proposed | Risk |
|---|---|---|---|
| SEO title | Tablet & iPad Repair in Bloomsbury, London WC1 \| InstaTech | iPad & Tablet Repair London – Open 7 Days \| InstaTech | L |
| Meta description | iPad and tablet screens from £59 and batteries from £39 at 67 Marchmont Street, near Russell Square and King's Cross. Free diagnostic, open 7 days. | iPad and tablet screens from £59 and batteries from £39 at our Bloomsbury WC1 and Moorgate EC1 shops. Free diagnostic, open 7 days a week. | L |
| H1 | iPad and tablet repair in Bloomsbury, near Russell Square and King's Cross | iPad and tablet repair in London, at our Bloomsbury and Moorgate shops | H |
| Body | Shop details for Bloomsbury only | Add the Moorgate address, phone and a link to `/locations/moorgate/` beside Bloomsbury | H |

The Rank Math title and meta are L-class and can ship through the Tuesday fix run once you approve. The H1 and body
change visible copy, so they are staged.

**Verify:** re-crawl; check that the og and Twitter titles follow the SEO title.
**Roll back:** restore the current values above.

## 3. Data recovery service page brief (backlog 5.7 · R8 · S10)
| Field | Value |
|---|---|
| URL | `/mobile-repair-services/data-recovery/` (beside `/screen-repair/`) |
| SEO title (60) | Data Recovery London – Phones, Tablets & Laptops \| InstaTech |
| Meta description | Lost photos or contacts on a dead phone? We recover data from phones, tablets and laptops in 1–24 hours, with a free assessment at both London shops. |
| H1 | Data recovery in London from broken, dead and water-damaged devices |
| Primary keyword | phone data recovery london |
| Supporting keywords (H2s) | recover data from broken phone · water damaged phone data recovery · tablet and laptop data recovery · data recovery near me |
| Facts allowed | All devices; free assessment; 1–24 hours; no fix, no fee; warranty depends on the repair (C9, C10, C14) |
| **Needed from owner** | A price or "from" price, and whether recovered data is returned on a USB drive, by transfer to a new phone, or both |
| Sections | Direct answer (40–60 words) · what we recover · the process (assessment → quote → recovery → handover) · turnaround · privacy and data handling · FAQ (5–6) · both shops · booking CTA |
| Schema | Service + Offer (price placeholder), FAQPage, BreadcrumbList |
| Links in (exact anchor "data recovery") | `/mobile-repair-services/` (Data Recovery card), `/tablet-repairs/` (Data Recovery card), `/laptop-desktop-repair/`, `/can-water-damaged-phones-recover/`, `/back-up-phone-before-repair/` |
| Overlapping post | `/phone-data-recovery-service-explained/`: re-angle to "how phone data recovery works", linking to the new page; do not merge |

The Wednesday build run can draft the full page from this brief once the price is supplied.
