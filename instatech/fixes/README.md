# InstaTech fix pack

Implementation package for the [21 October 2026 audit](../index.html). Work through it in order: each step lists
who does it, where, and how to check it worked. Purge LiteSpeed Cache after every site change
(LiteSpeed Cache → Toolbox → Purge All).

| # | Fixes audit item | Effort | Who |
|---|---|---|---|
| 1 | Homepage H1 (Critical) | 5 min | Site editor |
| 2 | Template residue, archives, product meta, author, Organization schema (High/Medium) | 10 min | Site admin |
| 3 | LocalBusiness schema (High) | 20 min | Site admin |
| 4 | Brand spelling (High) | 20 min | Site editor + owner |
| 5 | llms.txt (Medium) | 5 min | Site admin |
| 6 | Mobile performance (Critical) | 1–2 hrs, test as you go | Site admin |
| 7 | Bing, IndexNow, Search Console (Medium) | 15 min | Site admin |
| 8 | Off-site presence / GEO (Critical) | Ongoing, 60 days | Owner |
| 9 | Remaining hygiene (Medium) | 1–2 hrs | Site editor |

Take a full backup before steps 2, 3 and 6 (hPanel → Websites → Backups, or your backup plugin).

---

## 1. Homepage H1

**Where:** Elementor → edit the homepage → first slide of the hero slider (the heading with the classes `hh-c oc-h1`).

| | Text | HTML tag |
|---|---|---|
| Now | 2 shops weren’t enough. *Oxford Circus is next.* | H1 |
| Change to | Phone, laptop & tablet repair in central London. *Fixed same day.* | H1 |
| Move the Oxford Circus line to | 2 shops weren’t enough. Oxford Circus is next. | H2, or keep it in the top banner |

If the slider rotates, only one slide may carry the H1. Set the headings on all other slides to H2.

**Check:** view the page source and confirm that it contains exactly one `<h1` and that it holds the new text.

## 2. Install the SEO fixes must-use plugin

**File:** [`instatech-seo-fixes.php`](instatech-seo-fixes.php)
**Where:** upload to `wp-content/mu-plugins/` (hPanel → File Manager; create the `mu-plugins` folder if it is missing).

What it does (all through Rank Math filters, so it switches itself off if Rank Math is removed):

- Sets `noindex, follow` on `/blog-standard/` (theme demo page) and `/category/uncategorized/`, and drops both from the sitemap.
- Fills the empty meta descriptions on all 33 product categories, the 5 blog categories without one and the
  26 products without one. A description typed into Rank Math later always overrides it.
- Adds `alternateName`, `email`, `contactPoint` and `sameAs` to the Organization schema.
- Gives the blog author schema a name. It is currently blank on 60 posts.

Then, in wp-admin:

- **Users → your author → Display name publicly as:** set a real technician's name and add a two-line
  biography (years repairing, specialisms, shop). When this is filled in, it replaces the plugin's fallback name.
- Edit `INSTATECH_SAME_AS` in the plugin file each time a new profile goes live (step 8).

**Check:**
- `https://instatech.uk/blog-standard/` shows `noindex` in its robots meta tag.
- `https://instatech.uk/product-category/power-bank/` has a meta description.
- The Organization block on any page includes `contactPoint`.

## 3. Replace the LocalBusiness schema

**File:** [`localbusiness-schema.html`](localbusiness-schema.html). Instructions are at the top of the file.

Changes compared with the live block:

- Each shop's `url` and `@id` point to its own location page instead of `/locations/`.
- `image` is a shopfront photo instead of the logo (you supply the photo).
- `hasMap` uses the Google Maps share link containing the place ID (you supply the link).
- Adds `areaServed` neighbourhoods, `logo`, and an `OfferCatalog` of "from" prices that matches the prices
  already shown on the service pages.
- The Oxford Circus node is ready to paste in on the day that shop opens.

**Check:** run [Rich Results Test](https://search.google.com/test/rich-results) on the homepage. Expect two
LocalBusiness items with no errors.

## 4. One brand spelling: “InstaTech”

The Organization schema and most pages already use **InstaTech**. Change these to match:

| Where | Now | Change to |
|---|---|---|
| Rank Math title, /locations/moorgate/ | … \| instaTech | … \| InstaTech |
| Rank Math title, /locations/bloomsbury/ | … \| instaTech | … \| InstaTech |
| Rank Math title, /locations/oxford-circus/ | … \| instaTech | … \| InstaTech |
| Rank Math title, /mobile-repair-services/screen-repair/ | … \| instaTech | … \| InstaTech |
| Body copy and Service schema on /mobile-repair-services/screen-repair/ (“instaTech London”, provider “instaTech Bloomsbury”) | instaTech | InstaTech |
| Google Business Profile names | instaTech - (Bloomsbury) / instaTech - Moorgate | InstaTech Bloomsbury / InstaTech Moorgate |

Google rejects name changes that look like keyword stuffing, so keep the GBP names exactly as above. Expect the
change to go through Google's review.

Also, on the tablet page, change the title from “Tablet & iPad Repair in Bloomsbury, London WC1 | InstaTech”
to **“Tablet & iPad Repair London – Same Day Screens & Batteries | InstaTech”**, so that it covers both shops.

## 5. llms.txt

**File:** [`llms.txt`](llms.txt)
**Where:** Rank Math → General Settings → llms.txt. Paste it into the additional-content field the current
version uses, or upload it to the site root if the Rank Math module is switched off.

It adds a price and turnaround table, nearest stations, the Oxford Circus opening and the free-diagnostic and
warranty terms. These are the facts an AI assistant needs to answer “how much”, “how long” and “where”.
Update it whenever prices change.

## 6. Mobile performance

The stack is Elementor 4.3.5, the Reboot theme, WooCommerce and LiteSpeed Cache, with 44 script tags on the homepage.
Change one group of settings at a time, purge, and check the homepage, a service page, the shop and checkout
before moving on.

**LiteSpeed Cache → Page Optimization**

- CSS: *CSS Minify* on, *CSS Combine* off, *Generate UCSS* on, *Load CSS Asynchronously* on (requires
  QUIC.cloud; it generates critical CSS).
- JS: *JS Minify* on, *JS Combine* off, *Load JS Deferred* set to **Delayed**. Add the cookie banner and the
  booking form script to the *JS Delayed Includes exclusions* if they stop working.
- Media: *Lazy Load Images* on, then add the homepage hero image to *LCP / Above-the-fold exclusions*. Turn on
  *Add Missing Sizes*.
- HTML: *DNS Prefetch Control* on; *Remove Google Fonts* on if the brand font is self-hosted, otherwise set
  Elementor → Settings → Performance → Google Fonts to **Load locally**.

**Elementor → Settings → Features / Performance**

- Turn on *Optimized DOM Output*, *Improved Asset Loading*, *Improved CSS Loading*, *Lazy Load Background Images*,
  and *Element Caching*.
- Set *CSS print method* to **External file**. It is currently `internal`, which inlines CSS into every page and stops it being cached.

**WooCommerce**

- Use LiteSpeed's *JS Excludes*, or Asset CleanUp / Perfmatters, to stop `wc-cart-fragments`, `woo-smart-quick-view`,
  and `ti-woocommerce-wishlist` scripts loading on non-shop pages.

**Homepage**

- The hero is a slider. Make the first slide's image a real `<img>` (not a CSS background), at most 1600px wide, in WebP.
- Cut DOM size, currently 2,035 nodes. Remove hidden mobile/desktop duplicate sections and flatten nested containers.

**Check:** run [PageSpeed Insights](https://pagespeed.web.dev/) (mobile) on the homepage and on /mobile-repair-services/screen-repair/.
Aim for LCP under 2.5s and TBT under 200ms. Once Google has enough traffic data, use the field-data section
("Discover what your real users are experiencing") as the real target.

## 7. Bing, IndexNow, Search Console

ChatGPT search relies heavily on Bing's index, so Bing Webmaster Tools matters as much as Google Search Console here.

1. [Bing Webmaster Tools](https://www.bing.com/webmasters): add the site and choose *Import from Google Search Console* to verify. Submit `https://instatech.uk/sitemap_index.xml`.
2. Rank Math → General Settings → Instant Indexing: enable IndexNow. New and updated URLs are then pushed to Bing and Yandex automatically.
3. Google Search Console: confirm the domain property exists, submit the sitemap, and use URL Inspection → *Request indexing* on the homepage after step 1.

## 8. Off-site presence (the main GEO lever)

AI assistants recommend businesses that other sources corroborate. Use exactly this name, address and phone
(NAP) block everywhere, character for character:

```
InstaTech Bloomsbury
67 Marchmont Street, London WC1N 1AP
+44 7377 244454
https://instatech.uk/locations/bloomsbury/

InstaTech Moorgate
16 City Road, London EC1Y 2AA
+44 7508 088898
https://instatech.uk/locations/moorgate/
```

**Weeks 1–2: platforms that feed AI assistants and maps**

- [ ] Google Business Profile, both shops: primary category *Mobile phone repair shop*, secondary categories *Computer repair service*, *Electronics repair shop* and *Mobile phone store*. Add the services with “from” prices, at least 10 photos each (shopfront, inside, bench work), the opening hours, and the location page as the website link. Post weekly.
- [ ] [Bing Places](https://www.bingplaces.com/): import from Google Business Profile. This listing feeds Copilot and ChatGPT.
- [ ] [Apple Business Connect](https://businessconnect.apple.com/): both shops. This feeds Apple Maps and Siri.
- [ ] Reviews: after every completed repair, send a short-link SMS or show a QR code asking for a Google review. Aim for a steady flow (a few a week per shop) rather than a burst.

**Weeks 2–6: citations (same NAP every time)**

- [ ] Trustpilot (claim the profile; invite customers after each repair)
- [ ] Yelp UK
- [ ] Yell
- [ ] Thomson Local
- [ ] FreeIndex
- [ ] Cylex UK
- [ ] Hotfrog UK
- [ ] Scoot
- [ ] Facebook page and Instagram (link both shops; add the URLs to schema `sameAs`)
- [ ] Checkatrade or TrustATrader (optional, for the Pick & Drop service)

**Weeks 4–8: corroboration that AI assistants weight heavily**

- [ ] 3–5 local editorial mentions. Candidates: Bloomsbury and Camden local news, Islington/Clerkenwell local press,
  UCL/SOAS/Birkbeck student union discount schemes (Marchmont Street sits in the middle of them), City of London
  office-worker newsletters (Moorgate), and an Oxford Circus opening story.
- [ ] Answer genuine repair questions on Reddit (r/london, r/LondonSocialClub) and Quora, disclosing that you
  work at InstaTech. Perplexity and ChatGPT cite these threads frequently.

**Monthly: measure AI visibility**

Ask each of ChatGPT (search on), Perplexity, Gemini, Copilot and Google AI Mode the prompts below, and record
whether InstaTech is named and which source it cites:

1. Best phone repair shop near Russell Square
2. iPhone screen repair near King's Cross, how much
3. Phone repair open on Sunday in Bloomsbury
4. Same-day iPhone battery replacement near Old Street
5. MacBook screen repair in the City of London
6. Where can I sell my old iPhone for cash in central London
7. Apple Watch screen repair London price
8. Phone repair shop near Moorgate station
9. Cheap iPad screen repair central London
10. Phone repair near Oxford Circus

## 9. Remaining hygiene

- **Duplicate products.** These pairs exist as two products each: `world-travel-adapter-series-x` / `-x-2`,
  `ethernet-cable-1-gbps-speed-2m` / `-2m-2`, `ethernet-cable-1-gbps-speed-5m` / `-5m-2`,
  `ethernet-cable-10-gbps-speed-2m` / `-2m-2`, `ethernet-cable-10-gbps-speed-5m` / `-5m-2`,
  `z-series-usb-c-to-3-5mm-audio-cable-1-2m` / `-1-2m-2`. Keep one of each. Move the other to the bin and
  add a 301 redirect to the kept product (Rank Math → Redirections). Also check the two Lightning splitter pairs
  (A10, J21), the J2 HDMI cable and the QUATRE multi-port, which share titles.
- **Image alt text.** 791 product gallery images have none. In WooCommerce, the product name plus the view
  (e.g. “EnergyBar T20 power bank – side view”) is enough. Rank Math → General Settings → Images → *Add missing ALT
  attributes* `%title% %count(alt)%` covers this automatically as a fallback.
- **Accessibility** (Lighthouse 82/89):
  - Raise text contrast on the light-grey captions.
  - Make tap targets at least 24×24px with spacing.
  - Fix heading order (no H4 directly under an H2).
  - Give the search close button (`<a class="search_close">`) an `href="#"` and `aria-label="Close search"`, or turn it into a `<button>`.
- **Currency exchange page.** Keep it if the service is real, but take it out of the main repair navigation.
  Do not add it to the LocalBusiness schema.
- **Blog.** Do not publish more accessory buying guides. Merge overlapping ones (the 4 power bank posts, the
  5 wireless-charging posts and the 4 USB-C/Lightning cable posts) into one strong guide per topic, with 301 redirects.
  New posts should be repair-led and carry first-hand evidence (photos from the bench, actual prices, turnaround).
