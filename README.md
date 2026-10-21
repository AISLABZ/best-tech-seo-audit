# Best Tech Repair — SEO & performance audit

Audit of **best-tech.co.uk** (Webflow, CMS plan), carried out 13 August 2026.

Open **`index.html`** in a browser for the full dashboard, or view the rendered
version via GitHub Pages if enabled for this repo.

## Summary

30 findings across all 16 published pages — 9 critical, 11 high, 10 medium.

| Metric | Value |
|---|---|
| Pages crawled | 16 (all HTTP 200) |
| Pages with an H1 | 0 / 16 |
| Pages with structured data | 0 / 16 |
| Analytics / tracking tags | 0 |
| Images with alt text | 51 / 157 (32%) |
| Lighthouse mobile performance | 47 / 100 |
| Mobile LCP | 9.0s (target ≤ 2.5s) |
| Mobile CLS | 0.319 (target ≤ 0.1) |
| Desktop LCP / CLS | 1.4s / 0.002 — passing |

## The nine critical items

1. `/sitemap.xml` returns 404 — auto-generate sitemap was off in Webflow.
2. Zero `<h1>` elements across all 16 pages.
3. No canonical tags anywhere.
4. No structured data — no LocalBusiness schema for a walk-in London repair shop.
5. `/price` and `/career` still carry the Oxygen Studio template's title and meta description.
6. The pricing page CTAs link out to the template author's demo sites.
7. No GA4, Tag Manager, pixel, or Search Console verification.
8. Mobile LCP 9.0s, driven by a 4K hero video (5.78 MB).
9. Mobile CLS 0.319.

## Status

Fixed in Webflow (13 Aug 2026):

- [x] Auto-generate sitemap turned on
- [x] Global canonical URL set to `https://best-tech.co.uk`
- [x] robots.txt populated

Everything else in the dashboard is outstanding.

## Method

All 16 pages were fetched and parsed directly from the live site; counts are measured,
not estimated. Performance figures come from a single Lighthouse mobile lab run via
PageSpeed Insights. No real-user field data exists for this domain yet.

Not covered: backlinks, keyword rankings, competitor comparison, Google Business Profile.

---

# InstaTech — SEO growth engine

Audit and 90-day growth plan for **instatech.uk** (WordPress + WooCommerce + Rank Math), carried out
21 October 2026. Open **`instatech/index.html`** for the full dashboard.

All 276 sitemap URLs were crawled. The site has 16 findings: 5 critical, 6 high and 5 medium. Its technical
hygiene is sound: every URL returns 200 and every URL has a self-referencing canonical. The gap to the top
position is commercial page depth, internal link flow to the money pages, and off-site local prominence.

| Metric | Value |
|---|---|
| URLs crawled | 276 (all HTTP 200) |
| Internal links to `/mobile-repair-services/screen-repair/` | 2 (location pages: ~280) |
| Device- or model-level repair pages | 0 |
| Category archives with a meta description | 1 / 39 |
| Images without alt text | 972 / 3,449 |
| Dead internal links (theme demo slugs) | 6 targets, from 7 posts |

Not included: keyword volumes, rankings, backlinks and CrUX field data. Semrush returned
"insufficient API units", Ahrefs returned "insufficient plan" and the PageSpeed Insights quota was exhausted.
