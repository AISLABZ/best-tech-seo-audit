# Draft: Phone Battery Replacement London (Phase 2.1)

**Status:** drafted 21 Oct 2026, awaiting owner review. Not published.
**Build route:** in Elementor, duplicate `/mobile-repair-services/screen-repair/` (Templates → Saved, or Duplicate Post) and swap in the copy below. The new page then inherits the proven layout, booking widget, hours block and styling.

| Field | Value |
|---|---|
| URL | `/mobile-repair-services/battery-replacement/` (sits beside `/screen-repair/` under Mobile Repair) |
| SEO title (59 chars) | Phone Battery Replacement London – While You Wait \| InstaTech |
| Meta description (141 chars) | New phone battery in 20–40 minutes at our Bloomsbury and Moorgate shops. Free diagnostic, no fix no fee. Walk in 7 days a week, open until 9pm. |
| H1 | Phone battery replacement in London, done while you wait |
| Primary query | phone battery replacement london |
| Secondary queries | iphone battery replacement london · samsung battery replacement london · battery replacement near me (Bloomsbury, King's Cross, Russell Square, Moorgate, Old Street) · swollen phone battery |

**Fact sources:** every claim below is already published on instatech.uk unless it is marked **[OWNER]**:
- "20–40 min" and "Free diagnostic", from `/mobile-repair-services/`
- **No pricing anywhere** (owner rule, 21 Oct 2026): this page states no prices; the quote is given after the free diagnostic
- "No fix, no fee", "warranty on parts and labour" and "walk in, 7 days", from `/mobile-repair-services/screen-repair/`
- Opening hours, from `/locations/bloomsbury/` and `/locations/moorgate/`
- Reviews, quoted verbatim from the location pages

---

## Page copy

### Hero
**Phone battery replacement in London, done while you wait**

Phone dying by lunchtime, shutting down at 30%, or bulging at the back? We fit a new battery at our Bloomsbury or Moorgate shop, usually in 20 to 40 minutes. Every job starts with a free diagnostic, and if we can't fix it, you pay nothing.

- **A clear quote after the free diagnostic,** before any work starts.
- **20–40 minutes** for most phones, while you wait.
- **Warranty on parts and labour.** The period depends on the repair; we confirm it before we start. (Owner, 21 Oct 2026.)
- **Walk in 7 days a week, open until 9pm** Monday to Saturday.

[Book a battery replacement] → `/book-an-appointment/`  ·  [Call Bloomsbury] `tel:+447377244454`  ·  [Call Moorgate] `tel:+447508088898`

### Signs your battery needs replacing
- The phone drains from full to empty in a few hours, or dies before the end of the working day.
- It switches off suddenly at 20–40%, or in the cold.
- iPhone Battery Health shows "Service", or maximum capacity has dropped well below 80%.
- The phone gets hot while charging or during light use.
- **The back or screen is lifting.** A swollen battery is a safety issue. Stop charging the phone, switch it off, keep it away from heat, and bring it in as soon as you can. See our [guide to swollen and failing batteries](/guide-to-phone-battery-replacement-uk/).

Not sure it's the battery? Draining can also come from software, a faulty charging port or a damaged cable. The free diagnostic tells you which before you spend anything. Related reading: [Why is my phone battery draining?](/why-is-my-phone-battery-draining/) and [iPhone battery health not showing](/iphone-battery-health-not-showing/).

### How the quote works
Every job starts with a free diagnostic. We tell you what the repair involves and what it will cost for your model before any work starts. If we can't fix it, you pay nothing.

### How it works
1. **Walk in or book.** Either shop, any day. Booking holds the battery for less common models.
2. **Free diagnostic.** We check battery health and rule out charging-port or software causes.
3. **Fitted while you wait.** Most batteries take 20–40 minutes.
4. **Collect with warranty.** The warranty covers the part and the work.

### Parts and data
- **Parts:** we fit high-quality replacement batteries that meet or exceed the original specification, tested before and after fitting. (Owner, 21 Oct 2026: current parts wording is fine.)
- **iPhone note:** on recent iPhones, a non-Apple battery can show a "Non-genuine part" or "Unknown part" message in Settings. The phone still works normally. See [iPhone unknown part message explained](/iphone-unknown-part-message/). [OWNER: confirm whether you offer a genuine Apple battery option. No price is shown.]
- **Your data:** a battery replacement doesn't touch your photos, messages or apps. We still recommend a backup before any repair.

### Why InstaTech
- Two central London shops, **open later than the station-kiosk chains**: Bloomsbury and Moorgate are open until 9pm Monday to Saturday and 10am–8pm on Sunday.
- A free diagnostic, and no fix, no fee.
- Same-day service for most phones.
- What customers say:
  > "Deb was great, sorted my battery in 24 hrs. Heartily recommend five stars." (Bloomsbury customer)

  > "Jerin was very fast and efficient with replacing the battery of my phone." (Moorgate customer)

### Our shops
**InstaTech Bloomsbury**, 67 Marchmont Street, London WC1N 1AP. A short walk from Russell Square (Piccadilly line), and about ten minutes on foot from King's Cross St Pancras. Mon–Sat 9:30am–9pm, Sun 10am–8pm. [Directions](https://maps.google.com/?cid=10641785332690239296)

**InstaTech Moorgate**, 16 City Road, London EC1Y 2AA. Between Moorgate and Old Street stations, by Finsbury Square. Mon–Sat 9am–9pm, Sun 10am–8pm. [Directions](https://maps.google.com/?cid=8404697699929828128)

**Opening soon: InstaTech Oxford Circus**, 22 Great Castle Street, W1. → `/locations/oxford-circus/`

### FAQ
**How is a battery replacement priced?**
The price depends on your model. We confirm it after a free diagnostic, before any work starts, and if we can't fix it, you pay nothing.

**How long does a battery replacement take?**
Most phone batteries are replaced in 20 to 40 minutes while you wait. Book ahead for less common models so the battery is in stock.

**Do I need an appointment?**
No. Walk in to Bloomsbury or Moorgate any day of the week. Booking is optional.

**Will I lose my data?**
No. A battery replacement doesn't affect your photos, messages or apps. A backup beforehand is always sensible.

**My battery is swollen. Is it safe to bring in?**
Yes, and the sooner the better. Stop charging the phone, switch it off, keep it away from heat, and bring it to either shop. Don't try to press the case back together.

**Will my iPhone show a warning after a battery replacement?**
Recent iPhones may show a "Non-genuine part" or "Unknown part" notice in Settings after a third-party battery is fitted. The phone works normally. [OWNER: add the genuine-battery option here if you offer one.]

**Is there a warranty?**
Yes. Every battery replacement carries a warranty on the part and the labour. The period depends on the repair, and we confirm it before we start.

---

## Structured data (JSON-LD)
Paste into an Elementor HTML widget, or add it via Rank Math → Schema → Custom. Before publishing, replace `[OWNER]` values and make sure the visible FAQ above matches the FAQ schema word for word.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "@id": "https://instatech.uk/mobile-repair-services/battery-replacement/#service",
      "name": "Phone battery replacement",
      "serviceType": "Mobile phone battery replacement",
      "description": "Phone battery replacement in central London, usually in 20 to 40 minutes, with a free diagnostic and no fix, no fee.",
      "areaServed": { "@type": "City", "name": "London" },
      "provider": [
        {
          "@type": ["MobilePhoneStore", "LocalBusiness"],
          "name": "InstaTech Bloomsbury",
          "telephone": "+447377244454",
          "address": { "@type": "PostalAddress", "streetAddress": "67 Marchmont Street", "addressLocality": "London", "postalCode": "WC1N 1AP", "addressCountry": "GB" },
          "hasMap": "https://maps.google.com/?cid=10641785332690239296"
        },
        {
          "@type": ["MobilePhoneStore", "LocalBusiness"],
          "name": "InstaTech Moorgate",
          "telephone": "+447508088898",
          "address": { "@type": "PostalAddress", "streetAddress": "16 City Road", "addressLocality": "London", "postalCode": "EC1Y 2AA", "addressCountry": "GB" },
          "hasMap": "https://maps.google.com/?cid=8404697699929828128"
        }
      ],
      "url": "https://instatech.uk/mobile-repair-services/battery-replacement/"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://instatech.uk/" },
        { "@type": "ListItem", "position": 2, "name": "Mobile Repair Services", "item": "https://instatech.uk/mobile-repair-services/" },
        { "@type": "ListItem", "position": 3, "name": "Battery Replacement", "item": "https://instatech.uk/mobile-repair-services/battery-replacement/" }
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        { "@type": "Question", "name": "How is a battery replacement priced?", "acceptedAnswer": { "@type": "Answer", "text": "The price depends on your model. We confirm it after a free diagnostic, before any work starts, and if we can't fix it, you pay nothing." } },
        { "@type": "Question", "name": "How long does a battery replacement take?", "acceptedAnswer": { "@type": "Answer", "text": "Most phone batteries are replaced in 20 to 40 minutes while you wait. Book ahead for less common models so the battery is in stock." } },
        { "@type": "Question", "name": "Do I need an appointment?", "acceptedAnswer": { "@type": "Answer", "text": "No. Walk in to Bloomsbury or Moorgate any day of the week. Booking is optional." } },
        { "@type": "Question", "name": "Will I lose my data?", "acceptedAnswer": { "@type": "Answer", "text": "No. A battery replacement doesn't affect your photos, messages or apps. A backup beforehand is always sensible." } },
        { "@type": "Question", "name": "My battery is swollen. Is it safe to bring in?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, and the sooner the better. Stop charging the phone, switch it off, keep it away from heat, and bring it to either shop. Don't try to press the case back together." } }
      ]
    }
  ]
}
```
No `aggregateRating` is included on purpose. Google does not show self-published review stars for LocalBusiness or Service pages, and adding them risks a manual action.

---

## Internal-link plan

**Links into the new page** (deploy with plugin v1.3 once the page is live):

| From | Anchor | Mechanism |
|---|---|---|
| Header and mobile menu, under Repairs (after Screen Repair) | Battery Replacement | `wp_nav_menu_objects` filter, same as Screen Repair |
| Footer services list | Battery Replacement | `elementor/widget/render_content`, same as Screen Repair |
| `/mobile-repair-services/` battery card | phone battery replacement | Elementor edit, or a content filter |
| `/guide-to-phone-battery-replacement-uk/` | battery replacement in London | Contextual, first mention |
| `/why-is-my-phone-battery-draining/` | replace the battery | Contextual |
| `/iphone-battery-health-not-showing/` | iPhone battery replacement | Contextual |
| `/how-long-does-phone-repair-take/` | Battery replacements | Repoint the existing link (currently plugin-mapped to `/mobile-repair-services/`) |
| `/locations/bloomsbury/` and `/locations/moorgate/` | battery replacement | Contextual, in the services sentence |

**Links out from the new page:** `/book-an-appointment/`, both location pages, the battery guide, the draining-battery and battery-health posts, `/iphone-unknown-part-message/`, `/tablet-repairs/` and `/laptop-desktop-repair/`.

**Cannibalisation check:**
- `/guide-to-phone-battery-replacement-uk/` (1,936 words, informational) stays as it is. It answers "when and why", and the new page answers "where, how much, how fast". The fix is the contextual link above.
- No existing URL targets "battery replacement london" commercially, so nothing needs merging.

---

## Needs from owner before publishing
1. Whether a genuine Apple battery option exists (described without a price).
2. Approval to publish, plus the menu and footer links.

Resolved 21 Oct 2026: no pricing on the page (owner rule); warranty period depends on the repair; current parts wording stands.
