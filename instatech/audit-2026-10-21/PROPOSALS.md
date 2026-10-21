# InstaTech: proposals from the 21 Oct 2026 audit, for owner approval

These are proposals only. Nothing in this file has been applied to instatech.uk.

This audit is now part of the InstaTech programme in `instatech/`. Its rule is that nothing changes
on the live site without the owner's explicit approval. Each item below is mapped to `../backlog.md`.

**Owner approval, 21 Oct 2026:** A (identical pairs only), E (product name) and F are built in
`../wp/mu-plugins/instatech-audit-fixes.php` v1.0.0 and pass `../wp/tests/harness-audit.php`.
They are **not yet deployed**: the session's permission settings blocked the production upload.

## Superseded since this audit's crawl

The crawl ran at about 09:45 UTC. Plugin v1.0–1.2, deployed later the same day, now covers:

- the 64 missing meta descriptions (fallback template; backlog 1.6)
- the homepage H1 keyword line (1.2)
- "instaTech" spelling in titles (1.11)
- fallback alt text (1.9)
- noindex on Uncategorized (1.4)

The Elementor Pro security update (1.15) has been attempted. It is blocked on the owner's licence.

## New or more specific than the backlog

| # | Proposal | Backlog | Risk | Owner input needed |
|---|---|---|---|---|
| A | **Merge the 18 duplicate products.** Keep the original slug, add the `-2` copy's category to it, trash the `-2` copy, then import `duplicate-products-redirects.csv` in Rank Math → Redirections → Import. | 1.8 | Medium: catalogue change | 12 pairs match on price and stock and are redirected by the plugin. **6 pairs differ in price** and are held for the owner (see backlog 1.8). The CSV lists all 18. |
| B | **LiteSpeed Cache → Page Optimization:** turn on Generate Critical CSS and Load CSS Asynchronously; keep CSS Combine on. This targets the 729 KB render-blocking bundle (mobile FCP 10.3 s). | 1.12 | Medium: can cause a flash of unstyled content; test on staging or check visually | Approval |
| C | **LiteSpeed Cache → Crawler:** enable it so the cache is re-warmed after purges. Uncached TTFB is 2.8–3.2 s; cached is 0.2–0.5 s. Also turn on Object Cache: `.litespeed_conf.dat` shows `object-kind: false` even though an `object-cache.php` drop-in exists. | new | Low–medium: the crawler adds server load | Approval; check that the plan allows the crawler |
| D | **Icon fonts:** three icon libraries load on every page (ElementsKit 259 KB, Fontello 125 KB, Font Awesome 79 KB). Turn off the ElementsKit icon pack if no widget uses it (ElementsKit → Modules). | 1.12 | Medium: icons may disappear; needs a visual check | Approval |
| E | **Product schema for merchant listings:** add SKU and GTIN in WooCommerce, a brand attribute, and shipping and returns policy. None of the 159 products has any of these today. Strip the " - InstaTech" suffix from the Product `name`. | new | Low (data entry) / low (filter) | SKU/GTIN data; shipping and returns policy wording |
| F | **Remove `/shop/` from the product sitemap.** It is listed in both `page-sitemap.xml` and `product-sitemap.xml`. | new | Low | Approval |
| G | **Oxford Circus page:** its title says "Opening Soon" and the copy says "October 2026". Update it when the shop opens, and switch its schema to a LocalBusiness node with hours. | 3.2 | Low | Opening date |
| H | **Plugin updates available:** ElementsKit Lite, Essential Addons, Essential Blocks, LiteSpeed Cache, Templately. | new | Medium: run them with a backup | Approval. No server-side UpdraftPlus archive exists: the last on-server activity was the 18 Sep restore. Take a backup first. |

## Not available

Keyword, backlink and competitor data. Semrush returned `no_api_units` and Ahrefs returned
"Insufficient plan" on 21 Oct 2026. Rerun once either account has API access.
