# InstaTech — SEO & performance audit

Audit of **instatech.uk** (WordPress + WooCommerce, Rank Math SEO, LiteSpeed Cache on Hostinger),
carried out 21 October 2026.

Open **`index.html`** in a browser for the full dashboard, or view the rendered
version via GitHub Pages if enabled for this repo.

## Summary

21 findings across 276 sitemap URLs — 3 critical, 8 high, 10 medium.

| Metric | Value |
|---|---|
| URLs crawled | 276 (all HTTP 200) — 17 pages, 61 posts, 159 products, 33 product categories, 6 blog categories |
| Self-referencing canonical | 276 / 276 |
| Structured data present | 274 / 276 |
| GA4 tag present | 276 / 276 (`G-QY19S5963V`) |
| Duplicate product URLs | 36 (18 pairs at `-2` slugs) |
| Missing meta description | 64 / 276 |
| Images with alt text | 2,477 / 3,449 (72%) |
| Lighthouse mobile performance | 27 / 100 (desktop 67) |
| Mobile FCP / LCP | 10.3s / 11.1s (target LCP ≤ 2.5s) |
| Mobile TBT / CLS | 2,790ms / 0.011 |
| Uncached server response | 2.8–3.2s (cached 0.2–0.5s) |

## The three critical items

1. 18 products are published twice (original + `-2` slug), both self-canonical and both in the sitemap.
2. Mobile homepage: FCP 10.3s, LCP 11.1s, Lighthouse performance 27.
3. A single 729 KB combined stylesheet blocks rendering, plus three icon-font libraries (~463 KB).

## High priority

4. Total Blocking Time 2,790ms; main-thread work 18.9s on mobile.
5. Uncached TTFB ~3s — cache misses are slow for first visitors and Googlebot.
6. Product schema lacks brand, SKU, GTIN/MPN, shipping and returns on all 159 products.
7. Local-business schema split across inconsistent entities ("InstaTech" vs "instaTech", mismatched `@id`/`url`).
8. 64 URLs with no meta description (all product categories).
9. 972 images without alt text.
10. Homepage H1 is a promotional line, not a keyword.
11. Oxford Circus page still reads "opening soon" for an October 2026 opening.

## Status

The crawl ran at about 09:45 UTC on 21 October 2026. The fix programme's plugin, `instatech-seo-fixes.php` v1.0–1.2,
was deployed later the same day and now covers the meta descriptions, the homepage H1 line, the brand spelling in titles
and fallback alt text. The Elementor Pro security update has been attempted but is blocked on the licence.
The open items, with owner-approval proposals, are in [`PROPOSALS.md`](PROPOSALS.md). The 301 map for the duplicate
products is in [`duplicate-products-redirects.csv`](duplicate-products-redirects.csv).

## Method

Every URL in the Rank Math sitemap index was fetched and parsed directly; counts are measured,
not estimated. Performance figures are single Lighthouse 12.2 lab runs (mobile and desktop) on the
homepage. PageSpeed Insights' shared API quota was exhausted on the audit date, so field (CrUX)
data was not retrieved.

Not covered: WordPress admin settings, backlinks, keyword rankings, competitor comparison,
Google Business Profile, field Core Web Vitals.
