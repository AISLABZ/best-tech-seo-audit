# Drafts: Charging Port Repair and Water Damage Repair (backlog 2.2 and 2.3)

**Status:** approved and published 25 Oct 2026.
**Design:** built with the same template as the live battery page (`pages/assets/itx-service.{css,js}`,
`tools/build_service_page.py`), with the same sections and order. Previews, rendered inside the live site's header and footer:
`pages/previews/charging-port-repair.jpg` and `pages/previews/water-damage-repair.jpg` (mobile versions alongside).
**Publishing:** one-shot creator plugins (`wp/mu-plugins/instatech-create-<slug>.php`). Each creates its page once, under
Mobile Repair Services, with Rank Math title, description and focus keyword, then does nothing. **Both pages should be
published together, because they link to each other.**

| | Charging Port Repair | Water Damage Repair |
|---|---|---|
| URL | `/mobile-repair-services/charging-port-repair/` | `/mobile-repair-services/water-damage-repair/` |
| SEO title | Phone Charging Port Repair London \| InstaTech (45 chars) | Water Damaged Phone Repair London \| InstaTech (45 chars) |
| Meta description | Phone charging only at an angle or not at all? Port cleaned or replaced at our Bloomsbury and Moorgate shops. Free diagnostic, no fix no fee. Walk in 7 days. | Dropped your phone in water or spilled a drink on it? Switch it off and bring it to Bloomsbury or Moorgate. Free diagnostic, no fix no fee. Open 7 days. |
| H1 | Phone charging port repair in London, cleaned or replaced | Water damaged phone repair in London, switch it off and bring it in |
| Primary query | phone charging port repair london | water damaged phone repair london |
| Interactive section | "Tap what your phone is doing": 5 symptoms, each with its likely cause | "Tap what happened": 5 situations, each with first-aid advice |
| FAQ (7 items, with FAQ schema) | angle charging, cleaning, appointment, data, moisture warning, parts, warranty | rice, can it be fixed, photo recovery, water resistance, appointment, tablets, warranty |
| Blog links | `/how-to-fix-phone-charging-issues/`, `/how-to-clean-charging-port-safely/` | `/can-water-damaged-phones-recover/`, `/phone-corrosion-after-water-damage/` |

## Programme rules applied
- **No prices.** The build script refuses any £ figure, and the meta, schema and copy carry none.
- **No repair times.** The charging port time (30–60 min, C7) is published on the site but not confirmed for reuse, and
  water damage has no time on record. Both pages say "Repair time confirmed at the free diagnostic". If you confirm C7,
  the charging page can say "30–60 minutes" like the battery page does.
- **Warranty:** "on the part and the labour; the period depends on the repair" (C10).
- **Parts:** "genuine replacement parts and high-quality parts that meet or exceed the original specification".
- **Apple:** general wording only ("Lightning and USB-C iPhones", "current and recent iPhone models").
- **Reviews:** verbatim from the live site, never written for these pages.
  - **Charging page:** Paola Ayala (Moorgate), whose review is about a Samsung charging port, plus Lisa Loar (Bloomsbury).
  - **Water damage page:** no published review mentions water damage, so its section is headed "What customers say about both shops" and uses Lisa Loar and Chan Chanou.

## Facts used that are published but not yet confirmed (same as the battery page)
C1/C2 shop addresses and phones · C4 opening hours · C9 free diagnostic, no fix no fee. Data recovery (water page FAQ)
uses C14, which is confirmed: a paid service with a free assessment.

## Technical claims to sanity-check (general repair knowledge, stated cautiously)
- On many iPhone models the charging port shares a flex cable with the microphone.
- On many Galaxy models the USB-C port sits on a separate charging board.
- Rice doesn't draw water out of a phone. Apple's own guidance also advises against rice.
- Corrosion keeps working after a phone gets wet; sugary or salty liquids corrode faster than water.

## When the pages go live (plugin v1.5.2, already prepared)
- **Repairs menu and footer:** list both pages after Battery Replacement.
- **"By device" menu:** Phone → Charging Port and Water Damage point at the new pages instead of hub sections.
- **Battery page:** its "While it is on the bench" cards link to the new pages.

All three switch over automatically once each page exists.
