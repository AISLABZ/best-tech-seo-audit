# InstaTech live-site changelog

Every change made to instatech.uk is recorded here: what changed, how, and how to roll it back.

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

### Elementor Pro security update
Requested an update from 4.2.0, which is affected by an arbitrary-file-upload vulnerability fixed in 4.2.2, through Hostinger `wordpress_plugins_update`. **Result:** the job was accepted, but the plugin still reported 4.2.0 several minutes later. Elementor Pro updates normally need an active licence. **Action for owner:** in WP Admin → Elementor → License, confirm the licence is active, then update from Plugins (or upload the 4.2.2+ zip from your elementor.com account). Re-check on the next Monday run.
