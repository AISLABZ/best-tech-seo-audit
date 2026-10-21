# InstaTech — SEO & GEO audit

Audit of **instatech.uk** (WordPress + WooCommerce + Rank Math, Hostinger), carried out 21 October 2026.
Open **`index.html`** for the full dashboard.

## Summary

15 findings: 3 critical, 4 high, 8 medium. On-site SEO is strong. The main gap is off-site entity
presence, which limits how often AI assistants (ChatGPT, Perplexity, Gemini, Copilot, AI Overviews)
name the business.

| Metric | Value |
|---|---|
| URLs crawled (sitemap) | 276 (all HTTP 200, all self-canonical) |
| Pages / posts / products / categories | 17 / 61 / 159 / 39 |
| Structured data coverage | 276 / 276 |
| AI crawlers allowed | 11 / 11 tested |
| llms.txt | Present (Rank Math) |
| Images missing alt text | 972 / 3,449 (28%) |
| Lighthouse mobile performance (lab) | 27 home, 44 screen repair |
| Mobile LCP / TBT / CLS (lab, home) | 10.1s / 2,990ms / 0.002 |
| Third-party reviews/directories found | None |

## Critical items

1. Near-zero off-site footprint: no review, directory or press results for the brand or domain.
   Competitors are surfaced for local repair queries instead.
2. Mobile LCP of about 10s and TBT of about 3s (lab).
3. The homepage H1 is an Oxford Circus announcement, not a service or location statement.

## Method

All sitemap URLs were fetched and parsed from the live site. AI-crawler access was tested by user agent.
Performance comes from a local Lighthouse 12 mobile run (PageSpeed Insights quota was exhausted, so there is
no field data). The off-site footprint was assessed by web search. Ahrefs, Semrush and Search Console data
were unavailable for this run.

## Fix pack

Ready-to-apply fixes are in [`fixes/`](fixes/README.md): a must-use plugin (noindex rules, 64 meta
descriptions, Organization and author schema), corrected LocalBusiness JSON-LD, a revised llms.txt,
copy changes, performance settings and the off-site GEO playbook.

## Status

- [ ] 1. Homepage H1
- [x] 2. SEO fixes mu-plugin installed (21 Oct 2026; /category/uncategorized/ still in category sitemap, set noindex on the term in wp-admin)
- [ ] 3. LocalBusiness schema replaced (values filled in `fixes/localbusiness-schema-ready.html`; paste in wp-admin pending)
- [ ] 4. Brand spelling unified
- [x] 5. llms.txt updated (21 Oct 2026, static file at site root)
- [ ] 6. Mobile performance pass
- [ ] 7. Bing Webmaster Tools, IndexNow, Search Console
- [ ] 8. Off-site presence (GBP, Bing Places, Apple Business Connect, citations, reviews)
- [ ] 9. Hygiene (duplicate products, alt text, accessibility, blog consolidation)
