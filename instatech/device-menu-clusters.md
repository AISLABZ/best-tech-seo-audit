# Device menu: keyword clusters and page plan (25 Oct 2026)

Scope: the "By device" mega menu (Phone, Laptop and Desktop, Tablet, Smartwatch) and the 27 "by problem" links under it.
Method: SearchFit keyword clustering over the menu's own vocabulary plus the seed clusters in `keyword-clusters.md`.
**Search volumes are not available** (Ahrefs plan and Semrush units both refused on 25 Oct), so the priority below is set
from commercial intent, how distinct each query family is from its hub, and whether we have enough true, price-free
content to justify a standalone page. Search Console (backlog 1.13) confirms or reorders it once connected.

## What the live site has today (audited 25 Oct 2026)

| Menu item | Hub page | Design | Problem links in menu | Problem links that land on a matching section |
|---|---|---|---|---|
| Phone Repair | `/mobile-repair-services/` | new (itx) | 8 | 1 (Screen Repair → its own page). The 7 others point to `#battery`, `#charging`, `#camera`, `#speaker`, `#water`, `#buttons` and `#data`, none of which exist |
| Laptop and Desktop | `/laptop-desktop-repair/` | new (itx) | 8 | 0 (`#screen`, `#battery`, `#keyboard`, `#power`, `#water`, `#upgrades`, `#data`, `#case` missing) |
| Tablet Repair | `/tablet-repairs/` | new (itx) | 6 | 0 (`#screen`, `#battery`, `#charging`, `#camera`, `#speaker`, `#water` missing) |
| Smartwatch Repair | `/smartwatch-repair-service/` | new (itx) | 5 | 0 (`#screen`, `#battery`, `#crown`, `#sensors`, `#water` missing) |

Findings:
1. **The hub pages exist and already use the new design.** No device hub is missing.
2. **26 of 27 problem links go nowhere specific.** Each one drops the visitor at the top of the hub, so a "Charging Port"
   click shows a generic page. Phone → Battery Replacement still points at `/mobile-repair-services/#battery` although the
   dedicated page has been live since 21 Oct.
3. **The four device buttons are not links.** They switch the panel but cannot be clicked through to the hub, so they
   pass no link signal and frustrate anyone who expects a click to open the page. The hubs are still crawlable via the Repairs dropdown.
4. **All four hubs show price guides (£29–£79).** These predate the no-prices rule and are left as they are; noted for the owner.

## Keyword clusters

**Keywords processed:** 52 (menu labels, menu descriptions and seed keywords) · **Clusters:** 14

### D1 Phone charging port repair: transactional → dedicated page (backlog 2.2)
| Keyword | Role |
|---|---|
| phone charging port repair london | Primary |
| iphone charging port repair | Secondary |
| phone not charging repair | Secondary |
| samsung charging port replacement | Supporting |
| loose charging port fix | Supporting |

### D2 Phone water damage repair: transactional → dedicated page (2.3)
| Keyword | Role |
|---|---|
| water damaged phone repair london | Primary |
| phone dropped in water repair | Secondary |
| liquid damage phone repair | Secondary |
| iphone water damage repair | Supporting |

### D3 Data recovery (phone, tablet, laptop): transactional → dedicated page (5.7, Wednesday's scheduled run)
| Keyword | Role |
|---|---|
| phone data recovery london | Primary |
| recover data from broken phone | Secondary |
| laptop data recovery london | Secondary |
| dead hard drive recovery | Supporting |
One page serves the three "Data Recovery" menu links (phone, laptop and tablet); the menu links repoint to it.

### D4 MacBook repair: transactional → device page (2.8)
| Keyword | Role |
|---|---|
| macbook repair london | Primary |
| macbook screen repair london | Secondary |
| macbook battery replacement london | Secondary |
| macbook keyboard repair | Supporting |
| macbook liquid damage repair | Supporting |
The laptop hub keeps "laptop repair london", "computer repair london" and the Windows and PC searches.

### D5 iPhone repair: transactional → hub (2.5)
| Keyword | Role |
|---|---|
| iphone repair london | Primary |
| iphone screen repair london | Secondary (the Screen Repair page keeps priority) |
| iphone camera repair | Supporting |
| iphone back glass repair | Supporting (2.4) |
Model families are covered as sections, not separate pages (2.10–2.13 stay deferred).

### D6 Samsung and Pixel repair: transactional → hub (2.6)
| Keyword | Role |
|---|---|
| samsung repair london | Primary |
| samsung screen repair london | Secondary |
| google pixel repair london | Secondary |

### D7 iPad and tablet repair: transactional → existing hub `/tablet-repairs/` (2.7 consolidation)
| Keyword | Role |
|---|---|
| ipad repair london | Primary |
| ipad screen repair london | Secondary → `#screen` section |
| ipad battery replacement | Secondary → `#battery` |
| ipad charging port repair | Supporting → `#charging` |
| galaxy tab repair | Supporting |
No separate pages yet. The query families overlap heavily with the hub, so split one out only if Search Console shows it ranking on its own.

### D8 Apple Watch and smartwatch repair: transactional → existing hub (2.9)
| Keyword | Role |
|---|---|
| apple watch repair london | Primary |
| apple watch screen repair | Secondary → `#screen` |
| apple watch battery replacement | Secondary → `#battery` |
| galaxy watch repair | Supporting |
| digital crown repair | Supporting → `#crown` |

### D9 Laptop screen and battery (non-MacBook): transactional → laptop hub sections
laptop screen repair london (Primary) · laptop battery replacement · laptop keyboard repair · laptop not turning on → `#screen`, `#battery`, `#keyboard`, `#power`

### D10 Laptop upgrades: commercial → laptop hub `#upgrades`
ssd upgrade london (Primary) · laptop ram upgrade · speed up old laptop

### D11 Laptop hinges, case and liquid damage → laptop hub `#case` and `#water`
laptop hinge repair (Primary) · cracked laptop lid · laptop liquid spill repair

### D12 Phone camera repair → mobile hub `#camera`
phone camera repair london (Primary) · blurry phone camera fix · iphone camera repair (shared with D5)

### D13 Phone speaker, mic and buttons → mobile hub `#speaker` and `#buttons`
phone speaker repair (Primary) · phone microphone not working · power button repair · volume button repair

### D14 Tablet and watch minor faults → hub sections
tablet camera, tablet speaker, tablet water damage, watch sensors, watch water damage → hub sections only

## Priority ranking

| # | Cluster | Content type | Primary keyword | Why this rank |
|---|---|---|---|---|
| 1 | Fix the 26 dead problem links (all clusters) | Section ids on the four hubs, Phone → Battery repointed, device buttons made clickable | — | Every menu click works on day one. Small change, no new content |
| 2 | D3 Data recovery | Service page | phone data recovery london | Owner-confirmed (C14), serves 3 menu links, already scheduled |
| 3 | D1 Charging port | Service page | phone charging port repair london | Distinct, high-intent fault; gap |
| 4 | D2 Water damage | Service page | water damaged phone repair london | Urgent intent; gap |
| 5 | D4 MacBook | Device page | macbook repair london | High-value device; currently diluted in the laptop hub |
| 6 | D5 iPhone hub | Device hub | iphone repair london | Largest device family |
| 7 | D6 Samsung and Pixel hub | Device hub | samsung repair london | Second device family |
| 8 | D8 Apple Watch retitle and sections | Hub update | apple watch repair london | Page exists; targeting update only |
| 9 | D7, D9–D14 | Hub sections | — | Covered by #1; promote to pages only on Search Console evidence |

## Build rules for the new pages
- **Same design as the battery page.** Use the `itx-service` template (`pages/assets/itx-service.{css,js}`) through
  `tools/build_service_page.py`: the hero, the fault picker, the device row, the four-step process, reviews, both shops,
  FAQ (with schema generated from the visible FAQ), the related-repairs block and the closing CTA.
- No prices (the build script refuses any £ figure). Warranty "depends on the repair". Parts use the agreed dual wording. Apple stays general.
- Facts come only from `claims.md`. Turnaround times for charging port, water damage and MacBook are **not** in the
  register, so those pages carry no time claims until the owner confirms them.
- Each new page is added to the "by problem" menu link that points at it, to the Repairs dropdown and footer
  (via `instatech_seo_service_links()`), and to contextual links from its blog guides.
