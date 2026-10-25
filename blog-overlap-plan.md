# Blog overlap plan — for approval

Prepared 25 October 2026. Covers all 80 live posts plus the 4 flagged drafts.

**Goal:** stop posts competing with each other for the same searches. Each overlap gets one
strongest page (the "keeper"). The weaker post's useful, non-duplicate material moves into the
keeper, and the weaker URL then 301-redirects to it.

**Choosing the keeper:** when two posts cover the same question, the keeper is the older,
established URL, since it's the one most likely already indexed. Model-specific posts (iPhone 17,
Galaxy S25, Pixel 10, MacBook Air M4) are kept. Each targets a distinct search.

---

## 1. Redirect only: the 4 flagged drafts (already offline)

These were flagged "[CHECK DUPLICATE]" in Webflow and are unpublished again. They need 301s so
their old Soro links (`/blog?post=…`) and any shared URLs land somewhere useful.

| Old URL | Redirect to |
|---|---|
| `/post/commuter-phone-charging-port-repair-london` | `/post/charging-port-repair-when-to-fix-it-fast` |
| `/post/how-to-sell-an-iphone-safely` | `/post/how-to-sell-my-phone-safely` |
| `/post/iphone-17-lcd-repair` | `/post/iphone-17-cracked-screen` |
| `/post/laptop-fan-noise-causes-practical-fixes` | `/post/why-is-my-laptop-fan-loud` |

## 2. Merge and redirect (11 posts)

| Merge this post | Into the keeper | Why |
|---|---|---|
| `screen-repair-fast-attention` | `how-to-fix-cracked-phone-screen` | Both answer "my screen is cracked, what now" |
| `screen-repair-vs-replacement` | `screen-replacement-vs-new-phone` | Same repair-or-replace decision |
| `repair-versus-replace-broken-phone` | `screen-replacement-vs-new-phone` | Same decision, wider framing; fold in the non-screen faults |
| `central-london-device-repairs-without-the-wait` | `same-day-phone-repair-london` | Same "fast repair in central London" search |
| `piccadilly-device-repairs` | `same-day-phone-repair-london` | Same search; Piccadilly is the homepage's job |
| `top-notch-mobile-and-laptop-repair-services-in-london` | `/` (homepage) | 300-word generic overview of what the homepage already says |
| `phone-repair-checklist` | `how-to-choose-a-cell-phone-repair-shop` | Both are "what to check before you hand over your phone" |
| `buy-and-sell-phones-fair-deal` | `how-to-sell-my-phone-safely` | Same selling intent |
| `battery-replacement-vs-new-tablet` | `tablet-battery-replacement-service-london` | Same tablet-battery decision |
| `restoring-business-files-after-crash` | `how-to-recover-lost-files` | Same recovery steps; keep the business angle as one section |
| `iphone-17-pro-max-lcd-repair` | `iphone-17-cracked-screen` | Same model family and fault; keep Pro Max specifics as a section |

Ten of these have their useful material merged into the keeper first. The `top-notch…` post just
redirects to the homepage.

## 3. Keep, but link to each other (no URL changes)

These are related but answer different questions. Each gets a short "Related" link to the others.

- **Battery:** `phone-battery-replacement-when-is-it-worth-it` ↔ `what-causes-phone-battery-drain` ↔ `iphone-15-battery-draining-fast`
- **Laptop heat:** `why-is-my-laptop-fan-loud` ↔ `why-is-my-laptop-overheating`
- **Samsung:** `samsung-galaxy-repair-near-me-london` ↔ `samsung-screen-repair-what-to-do-fast` ↔ the Galaxy S25 posts
- **Data:** `data-recovery-for-broken-phones` ↔ `laptop-data-recovery-guide` ↔ `how-to-recover-deleted-tablet-files`
- **Tablet:** `ipad-and-tablet-repair-done-fast` ↔ `is-tablet-repair-worth-it` ↔ `why-tablet-touchscreens-stop-responding`
- **Selling:** `how-to-sell-my-phone-safely` ↔ `cash-converter-or-repair-which-pays-off` ↔ `used-phones-what-to-check-before-you-buy`

## 4. Small fixes alongside

- Retitle `how-to-choose-a-cell-phone-repair-shop` to "How to Choose a Mobile Phone Repair Shop".
  The URL stays the same, but UK searchers say "mobile", not "cell".

---

## How it runs, once approved

1. **Me:** for each merge, move the useful, non-duplicate sections into the keeper. That means
   new headings and steps, not repeated paragraphs. Then publish the keeper. Before/after notes
   go in this repo.
2. **You:** in Webflow → Site settings → Publishing → **301 redirects**, add the 15 rows above
   (4 in section 1, 11 in section 2). Webflow's tools here can't create redirects. It takes
   about ten minutes.
3. **Me:** unpublish the 11 merged posts as soon as you confirm the redirects exist, so no URL
   is left showing a 404. Then add the related links from section 3, do one full site publish
   so the sitemap updates, and check every redirect and keeper live.

**Result:** 80 live posts become 69, with no lost URLs and fewer pages competing for the same searches.
