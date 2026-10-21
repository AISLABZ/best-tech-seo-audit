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

Smoke test after the upload: `/`, `/mobile-repair-services/screen-repair/`, `/desktop-computer-repair-near-me/`, `/product-category/power-bank/`, `/shop/` and `/wp-login.php` all returned 200. LiteSpeed and server caches were purged.

### Elementor Pro security update
Requested an update from 4.2.0, which is affected by an arbitrary-file-upload vulnerability fixed in 4.2.2, through Hostinger `wordpress_plugins_update`. Status: see the next entry.
