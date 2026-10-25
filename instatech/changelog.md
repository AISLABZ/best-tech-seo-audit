# InstaTech live-site changelog

Every change made to instatech.uk is recorded here: what changed, how, and how to roll it back.

## 2026-10-25

### Deployed plugin v1.5.1 (approved by owner): the "By device" menu links now land (backlog 2.16)
Source: `instatech/device-menu-clusters.md`. Before the upload the live file was confirmed as v1.4.0 (626 lines, 21,842 bytes); it is now v1.5.1 (27,751 bytes).

| What | Before | After |
|---|---|---|
| "By problem" links (27 across phone, laptop, tablet and smartwatch) | 26 pointed at `#section` ids that did not exist, so each click landed at the top of the hub | The four hubs' service cards carry the ids (`#battery`, `#charging`, `#screen` and so on) and each link scrolls to its card, which is briefly outlined |
| Phone → Battery Replacement | `/mobile-repair-services/#battery` | `/mobile-repair-services/battery-replacement/` (only while that page is live) |
| Laptop → Charging and Power, Liquid Damage, Hinges and Case | No matching card on the hub | The "Free Diagnostic" step (`#diagnostic`) |
| Device buttons (Phone, Laptop and Desktop, Tablet, Smartwatch) | Switched the panel only | A mouse or keyboard click opens the hub; on a touch screen the first tap still only switches the panel |

- **Mechanism:** an output buffer (`template_redirect`, priority 4) adds the ids to the hub pages, and a small footer script (`#instatech-seo-menu`) corrects the menu links as the menu draws them and handles the device-button clicks.
- **v1.5.0 was live for about 20 minutes:** the ids worked, but its menu-script text patch never matched because LiteSpeed minifies inline scripts after WordPress renders the page. v1.5.1 replaced the patch with the footer script.
- **Tests:** `harness-v15.php` passes, as do all earlier harnesses unchanged.
- **Verified live:** all 24 ids are present on the four hubs; the corrected links appear in both the desktop panel and the mobile drawer; clicking "Laptop and Desktop" opens `/laptop-desktop-repair/`; `/tablet-repairs/#charging` scrolls to and outlines the Charging Port card.
- **Rollback:** re-upload v1.4.0 from git history.
- **Finding (existing, not changed):** on a touch screen showing the desktop layout (for example an iPad in landscape), tapping "Repairs" opens the mega panel and immediately closes it. The menu script opens the panel on `mouseenter` and then toggles it shut on the tap's `click`. This is for the owner or the menu's author to fix; a one-line guard would solve it.

## 2026-10-21

### Deployed `wp-content/mu-plugins/instatech-seo-fixes.php` (v1.0.0)
Source: `instatech/wp/mu-plugins/instatech-seo-fixes.php`. The plugin uses output filters only and makes no database writes.
**Rollback:** overwrite the file with an empty `<?php` file, or add `define( 'INSTATECH_SEO_FIXES_OFF', true );` to `wp-config.php`.

| Fix | Scope | Verified live |
|---|---|---|
| Dead and redirecting internal links repointed to their final URLs | 17 links in 12 blog posts | Yes: 0 remaining |
| `noindex, follow` on theme demo pages | `/layouts/battery/`, `/layouts/display/` | Yes |
| `noindex, follow` on the Uncategorized archive | `/category/uncategorized/` | Yes |
| Fallback meta descriptions | 33 product categories, 6 blog categories, 26 products (only where empty) | Yes |
| Brand spelling "instaTech" → "InstaTech" in titles | 4 titles | Yes (`/locations/moorgate/`) |
| Instagram, TikTok and Facebook added to the Organization `sameAs` | Sitewide schema | Yes |
| Fallback image alt text (parent product or post title) | Images rendered through `wp_get_attachment_image` | Partial: theme icons and logos are not covered |

Scheduled runs created (draft-and-propose only): Mon 08:41 measure and verify · Tue 09:37 fix proposals · Wed 09:43 build money page · Thu 09:47 local and authority · Fri 15:53 weekly report (push and email) · 1st of month 09:33 review (all Europe/London).

Smoke test after the upload: `/`, `/mobile-repair-services/screen-repair/`, `/desktop-computer-repair-near-me/`, `/product-category/power-bank/`, `/shop/` and `/wp-login.php` all returned 200. LiteSpeed and server caches were purged.

### Deployed plugin v1.1.0 (approved by owner)
Same file and the same rollback (re-upload v1.0.0 from git history or an empty file).

| Change | Verified live |
|---|---|
| "Screen Repair" added under Repairs in the desktop, sticky and mobile header menus (`wp_nav_menu_objects` filter) | Yes: 4 links to `/mobile-repair-services/screen-repair/` on every page, up from 2 pages sitewide |
| "Screen Repair" added to the footer services list (Elementor `trx_widget_custom_links`) | Yes, with screenshot |
| Footer "About Us" heading linked to `/about-us/`, which had 0 inlinks | Yes: 1 link on every page |
| Homepage H1 now starts with a visible line, "Phone, laptop & tablet repair in central London"; the campaign headline is unchanged | Yes: one H1 on the homepage, screenshots on desktop and mobile |

Smoke test: `/`, `/mobile-repair-services/`, `/locations/bloomsbury/`, `/shop/`, a blog post and `/wp-login.php` all returned 200. Caches were purged.

### Deployed plugin v1.2.0 (approved by owner): Google Maps links point to the exact listings
Listings were resolved from Google Maps on 21 Oct 2026. Each cid link was confirmed to open the right listing:

| Shop | Listing name on Google | Permanent link | Place ID |
|---|---|---|---|
| Bloomsbury | instaTech - (Bloomsbury) | https://maps.google.com/?cid=10641785332690239296 | ChIJg5Ii0NUbdkgRQL_2omA3r5M |
| Moorgate | instaTech - Moorgate | https://maps.google.com/?cid=8404697699929828128 | ChIJm5ZiHwAddkgRICvcMAd8o3Q |
| Oxford Circus | No listing found | — | — |

- Name-search and address-search Maps links in the schema (`sameAs`, `hasMap`) and in "Find us" links now use the cid links. "Directions" buttons now carry `destination_place_id`. Embedded map iframes are unchanged.
- Verified on `/`, `/locations/`, both location pages, `/about-us/`, `/mobile-repair-services/` and `/locations/oxford-circus/`: 0 old links remain, embeds still render, and all JSON-LD parses. Caches were purged.
- Mechanism: an output buffer on front-end HTML (`template_redirect`). Rollback is the same as for earlier versions.

### Published: Phone Battery Replacement page (approved by owner)
- **URL:** https://instatech.uk/mobile-repair-services/battery-replacement/ (page ID 76574, child of Mobile Repair Services 75806).
- **Created by:** the one-shot mu-plugin `wp-content/mu-plugins/instatech-create-battery-replacement.php`, which does nothing once the page exists. Source block: `instatech/pages/battery-replacement.block.html`, built by `instatech/tools/build_service_page.py`.
- **Design:** the same template stylesheet and script as `/screen-repair/`. Interactive symptom checker, brand tabs, step journey and FAQ were all checked live with 0 JS errors, on desktop and mobile.
- **Search details:** SEO title "Phone Battery Replacement London – Same Day | InstaTech", meta description and focus keyword stored in Rank Math. Indexable, self-canonical and in `page-sitemap.xml`. One H1. Valid JSON-LD (Service, BreadcrumbList, FAQPage); the FAQ is generated from the visible FAQ.
- **Programme rules:** no prices; warranty described as repair-dependent; both parts claims; general Apple wording.
- **Rollback:** set the page to Draft in WP Admin (Pages → Battery Replacement), and re-upload plugin v1.2.0.

### Deployed plugin v1.3.1
- "Battery Replacement" now appears after "Screen Repair" in the desktop, sticky and mobile menus and the footer services list, but only while the page is published.
- `/how-long-does-phone-repair-take/`: the "Battery replacements" link now goes to the new page.
- Verified: 4 navigation links to the battery page on every page tested (`/`, `/locations/moorgate/`, `/shop/`), plus the contextual link.
- v1.3.0 read a WordPress option to decide whether to show the links, and that option read back empty on this server (probably the object cache). v1.3.1 checks the published page directly instead.

### Finding: LiteSpeed Guest Mode reloads every page on a visitor's first visit
A fresh mobile visit loads the page, POSTs to `/wp-content/plugins/litespeed-cache/guest.vary.php`, sets `_lscache_vary`, then reloads the page. This was confirmed on `/`, `/locations/bloomsbury/` and the battery page. It explains the ~8–10 s same-URL "redirect" in the audit's Lighthouse runs. It is not a test artefact; it affects real first visits and Core Web Vitals. Logged as backlog 1.12a for approval.

### Deployed plugin v1.4.0 (approved by owner): merges both sessions' work
`instatech-seo-fixes.php` v1.4.0 = v1.3.2 (v1.3.1 battery menus + the keyword-cluster overrides for `/phone-accessories-trade-in/` and `/tablet-repairs/`) + contextual links to the battery page from the battery guide, the battery-draining and battery-health posts, and both location pages (which also link screen repair). Before upload, live was confirmed as v1.3.1 (483 lines, 15,238 bytes). After upload it is v1.4.0 (21,842 bytes). Verified live: contextual battery links on all 5 pages, plus the screen-repair link on both location pages; tablet and accessories titles and H1s restored; 4 nav links per page to battery and screen; Maps cid links and homepage H1 line intact. Caches purged. Tests: v14 19/19 (against saved live article bodies), v13 11/11, v13-clusters 11/11, v12 11/11, v11 13/13, harness.php ok. **Deploy owner (owner decision, 21 Oct):** the programme session (claude/laughing-clarke-s2j0uk, session_01FswsV4ZkKDJJswjF7gVqD7) is the only session that uploads plugin files. Other sessions commit changes to the repo and ask the owner to have them deployed. Only one session deploys this file at a time, and every deploy first checks that the live version matches the last version recorded here.

### LiteSpeed Guest Mode turned OFF (owner: Option A)
- **How:** the one-shot `wp-content/mu-plugins/instatech-litespeed-guest-off.php` called LiteSpeed's own `Conf::update_confs()` (the same call as the settings Save button). Log `wp-content/instatech-ops/litespeed-guest.json`: before `guest: true, guest_optm: true`, after `false, false`, result `ok` (14:37 UTC). Caches purged. The LiteSpeed settings screen now shows Guest Mode off.
- **Verified:** first visits no longer call `guest.vary.php` and no `_lscache_vary` cookie is set (checked on 5 pages). The guest-mode reload is gone. The battery page went from 3 document loads in testing to 2, and the remaining extra load is the CDN check below.
- **Undo:** LiteSpeed Cache → General → Guest Mode ON.

### Finding: Hostinger CDN bot check ("Checking your browser… Just a moment")
From this cloud test machine, every browser-like first visit gets a `403` interstitial from Hostinger CDN (`server: hcdn`). It waits 3 s, POSTs to `/hcdn-cgi/jschallenge-validate`, then reloads into the real page (`hcdn` cookie). curl, Googlebot and Lighthouse user agents receive the page directly (200). This is most likely datacenter-IP bot protection, so real visitors on home or mobile networks are probably unaffected, but that can't be confirmed from a cloud IP. It also inflates lab speed tests run from cloud machines, which explains part of the ~9 s audit "redirect". **Owner check:** open the site on a phone in a private tab on mobile data; if "Checking your browser…" appears, relax Bot protection in hPanel → CDN → Security. The Hostinger API does not expose this setting.

### Server-side rendering audit, and homepage sections now server-rendered (21 Oct)
**Audit:** 18 key pages (home, mobile/screen/battery repair, locations ×3, tablet, laptop, smartwatch, buy-sell, about, booking, shop, a product category, a product, a blog post, the blog index) were compared as raw server HTML (Googlebot user agent) against a fully rendered browser DOM.
- WordPress, Elementor and the custom service and location pages are server-rendered: 94–98% of visible text is in the raw HTML, and H1s, titles and JSON-LD match.
- JS-only by design, and fine: the Oxford Circus announcement bar, the live "Open/Closed" status, WooCommerce quick-view links (already blocked in robots.txt), cart fragments and comment counts. Product-page "related products" differ between fetches only because WooCommerce shuffles them; they are server-rendered.
- **Gap fixed:** the homepage built 5 sections in the browser from an inline script (`#tiles` repair devices, `#cats` accessory categories, `#audio` and `#chargers` product rails, `#rvgrid` reviews). The server sent them empty, so 34% of the homepage text and its product and category links were invisible to non-rendering crawlers.

**Deployed `wp-content/mu-plugins/instatech-home-ssr.php`:** it injects a captured snapshot of those sections into the containers on the server (output buffer on the front page only). The page script still re-renders identical HTML; there is no duplication (7/6/4/4/3 children with JS on or off), and the no-JS render was checked by screenshot.
- **Fail-safe:** it only injects while the homepage script matches fingerprint `f3d0e9a8…` (whitespace trimmed, `<iframe>`/`<img>` tags normalised, because LiteSpeed rewrites those after WordPress). The first deploy did not inject because LiteSpeed trims the script's surrounding newlines; a mismatch diagnostic (`wp-content/instatech-ops/home-ssr-mismatch-<fp>.txt`) showed the difference, and the trim fix was redeployed.
- **Verified live:** as Googlebot and a plain client, all 5 containers are filled, with 43 crawlable `<a>` product and category links and the review text in the server HTML.
- **Refresh after editing those homepage sections:** run `node instatech/tools/capture_home_sections.js …`, then `python3 instatech/tools/build_home_ssr.py …`, then redeploy. Until refreshed, the plugin steps aside automatically.
- **Rollback:** replace the file with an empty one.

**Crawler access check:** Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended and Applebot user agents all get 200 with the full page. **GPTBot gets `429` from Hostinger CDN, even on robots.txt**, while robots.txt allows all bots. This is most likely Hostinger's AI-crawler blocking setting in hPanel (CDN/Security). It may also be the CDN rejecting a GPTBot user agent from a non-OpenAI IP, which can't be ruled out from here. Owner decision: GPTBot feeds ChatGPT's model knowledge; ChatGPT search uses OAI-SearchBot, which is allowed.

### Elementor Pro security update
Requested an update from 4.2.0, which is affected by an arbitrary-file-upload vulnerability fixed in 4.2.2, through Hostinger `wordpress_plugins_update`. **Result:** the job was accepted, but the plugin still reported 4.2.0 several minutes later. Elementor Pro updates normally need an active licence. **Action for owner:** in WP Admin → Elementor → License, confirm the licence is active, then update from Plugins (or upload the 4.2.2+ zip from your elementor.com account). Re-check on the next Monday run.

### Deployed plugin v1.3.0 (approved by owner): keyword-cluster page changes
Source: `instatech/proposals/2026-10-21-keyword-cluster-decisions.md` §1–2 (backlog 5.3 and 5.6). The live file was confirmed to be v1.2.0 (434 lines, 13,639 bytes) before upload. Same rollback as earlier versions: re-upload v1.2.0 from git history.

| Page | Change | Verified live |
|---|---|---|
| `/phone-accessories-trade-in/` | Title "Phone Accessories London – Bloomsbury & Moorgate \| InstaTech"; new meta description without trade-in; H1 "Phone accessories in central London"; H2 "Selling your phone?"; button anchor "Sell your phone for cash" → `/buy-sell-phones/` | Title, H1, H2 and anchor: yes. Meta and OG tags not yet checked (see note) |
| `/tablet-repairs/` | Title "iPad & Tablet Repair London – Open 7 Days \| InstaTech"; meta description naming both shops, **no prices**; H1 "iPad and tablet repair in London"; H2 "iPad and tablet repair in Bloomsbury and Moorgate"; intro sentence names both shops | Title, H1, H2 and intro: yes. Meta and OG tags not yet checked |

- Mechanism: Rank Math title, description and OpenGraph/Twitter filters, plus exact-string copy swaps in a front-end output buffer (`template_redirect`, priority 2). A swap whose source string no longer exists does nothing.
- Tests: `php -l` clean; `harness-v13.php` 11/11; `harness-v11.php` 13/13 and `harness-v12.php` 11/11 unchanged; `harness.php` output identical to v1.2.0.
- Server and CDN cache cleared. `/`, `/locations/bloomsbury/` and both changed pages render without errors.
- Note: the session's permission check blocked the raw-HTML verification, so meta description and OG tags are to be confirmed on the Monday crawl. Both pages also emit a second, non-Rank Math `og:title` ("Phone Accessories and Trade-In in London", "Tablet Repairs"); its source is still to be traced.

### v1.3.0 overwritten by v1.3.1; combined v1.3.2 prepared (not deployed)
Two sessions deployed the same plugin file in parallel. This session's v1.3.0 (keyword-cluster changes, backlog 5.3 and 5.6) went up at about 13:00. A parallel session's v1.3.1 (battery page links) went up at about 13:05 and replaced it; v1.3.1 does not contain the 5.3 and 5.6 changes. The live file was confirmed as v1.3.1 (483 lines, 15,238 bytes). `instatech/wp/mu-plugins/instatech-seo-fixes.php` is now v1.3.2: v1.3.1 unchanged, plus the keyword-cluster overrides. Tests: `php -l` clean; harness-v11 13/13, v12 11/11, v13 11/11, v13-clusters 11/11; `harness.php` output identical to v1.3.1. **Awaiting owner go-ahead to redeploy.**
