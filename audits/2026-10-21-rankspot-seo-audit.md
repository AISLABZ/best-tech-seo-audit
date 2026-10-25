# RankSpot SEO Audit — best-tech.co.uk

**Audit date:** 21 October 2026
**Baseline:** 13 August 2026 audit (`index.html` in this repository)
**Scope:** 78 live URLs (73 in the XML sitemap, 5 published but missing from it), plus the two legacy template URLs `/price` and `/career`

## Executive summary

**Overall score: 86 / 100 — Good, with room for improvement** (performance excluded; see Limitations)

The site has been substantially remediated since August. Seven of the nine critical findings from the baseline are now resolved: every page has one H1, a self-referencing canonical, unique and correctly sized titles and descriptions, and valid structured data, including a fully specified `LocalBusiness` entity. GA4 and Search Console verification are live. The site has grown from 16 pages to 78, driven by a 64-article blog.

The issues that remain concern **discovery rather than on-page quality**. The investment in blog content is underperforming because 43 of the 64 articles have no internal link pointing to them, and 5 recent articles are absent from the sitemap. Fixing internal linking is the highest-return action available.

| Area | Aug 2026 | Oct 2026 | Score |
|---|---|---|---|
| Pages live (HTTP 200) | 16 | 78 | — |
| Pages with exactly one H1 | 0 / 16 | 73 / 73 | 15 / 15 |
| Self-referencing canonical | 0 / 16 | 73 / 73 | |
| Unique title, ≤ 60 chars | 7 / 16 duplicated | 71 / 73 | 14 / 15 |
| Structured data (JSON-LD) | 0 / 16 | 73 / 73 | 15 / 15 |
| Analytics / Search Console | None | GA4 + GSC verified | 5 / 5 |
| Content images with alt text | 32% | 100% (empty alt only on decorative icons) | 10 / 10 |
| Crawlability (robots, sitemap, status codes) | Sitemap 404 | Sitemap live; 5 posts missing | 12 / 15 |
| Internal linking | Not assessed | 0 orphaned; related guides on all 9 service/repair pages | 14 / 15 |
| Social / Open Graph | Not assessed | `og:url` missing site-wide | 8 / 10 |
| **Total** | | | **86 / 100** |

## Baseline critical items — status

| # | August finding | Status |
|---|---|---|
| 1 | `/sitemap.xml` returned 404 | **Resolved** — live, 73 URLs |
| 2 | Zero H1 elements | **Resolved** — one H1 on every page |
| 3 | No canonical tags | **Resolved** — self-referencing on every page |
| 4 | No structured data | **Resolved** — `LocalBusiness`, `Service`, `BlogPosting`, `BreadcrumbList`, `CollectionPage`, `AboutPage`, `ContactPage`, `Blog` |
| 5 | `/price`, `/career` carried template metadata | **Resolved** — both pages removed (now 404) |
| 6 | Pricing CTAs linked to template author's demo sites | **Resolved** — page removed; no outbound links to template domains remain |
| 7 | No analytics or Search Console | **Resolved** — GA4 script and `google-site-verification` present |
| 8 | Mobile LCP 9.0s (4K hero video) | **Improved, still failing** — homepage mobile LCP 8.2s (25 Oct); repair pages far worse (see Performance) |
| 9 | Mobile CLS 0.319 | **Resolved on homepage** — 0.031 (25 Oct); `/blog` now 1.00, repair page 0.136 |

## Critical issues (must fix)

- [x] **43 of 64 blog posts were orphaned — fixed and published 21 Oct 2026.** No crawled page links to them; they are discoverable only through the sitemap. `/blog` lists the 12 most recent posts with no pagination or category archive, and no homepage, service or repair page links to any post. Only 8 posts link to another post. Orphaned pages receive no internal link equity and are crawled and ranked less reliably.
  *Done:* `/blog` now carries an "All repair guides" CMS list bound to the Blog Posts collection (limit 100), so every published post — 67 at time of fix — is linked from `/blog` and new posts are added automatically. Links use a new `Post URL` CMS field (`/post/<slug>`), populated for all 84 items. Verified live: 67/67 links return HTTP 200, no sitemap post is left unlinked.
  *Done 25 Oct:* the list is sorted newest-first. Each of the 9 `/works/*` and `/services/*` pages now carries a "Related repair guides" section (1–8 posts each, 40 distinct posts, chosen by service relevance and stored in a `Related guides list` CMS field). Verified live: 9/9 pages render the section, all 40 links return HTTP 200.
  *Maintenance:* new posts must have `Post URL` filled in, and should be added to the relevant service's `Related guides list` field.
  *Fix:* add pagination or a full archive to `/blog`; add a "Related guides" CMS list to each `/works/*` and `/services/*` page filtered by topic; add 2–3 contextual post-to-post links per article.
- [ ] **Mobile performance fails Core Web Vitals on every page tested** (Lighthouse 13.5, mobile, simulated throttling, 25 Oct 2026):

  | Page | Performance | LCP | CLS | TBT | Page weight |
  |---|---|---|---|---|---|
  | `/` | 69 | 8.2s | 0.031 | 233 ms | 1.7 MB |
  | `/works/mobile-phone-repair` | 32 | 20.9s | 0.136 | 3,310 ms | 6.8 MB |
  | `/blog` | 41 | 6.7s | 1.00 | 237 ms | 1.1 MB |

  Targets: LCP ≤ 2.5s, CLS ≤ 0.1. The repair page is the most serious: 5.5 MB of its 6.8 MB is oversized imagery (estimated LCP saving 8.7s). `/blog` CLS of 1.00 indicates content moving after load — the long "All repair guides" list or unsized post thumbnails are the likely cause and should be checked first.
  *Fix:* (1) compress and resize images on the `/works/*` template, serve WebP/AVIF via Webflow's responsive images; (2) give `/blog` card images explicit dimensions and reserve space for the CMS lists; (3) remove lazy-loading from above-the-fold images; (4) homepage: serve a ≤ 720p hero video or a static poster on mobile.

## Warnings (should fix)

- [ ] **5 published posts are missing from `sitemap.xml`** although they are linked from `/blog` and return 200 with valid canonicals:
  `/post/galaxy-s25-charging-port-loose`, `/post/galaxy-s25-will-not-charge`, `/post/iphone-17-cracked-screen`, `/post/macbook-air-m4-battery-draining-fast`, `/post/pixel-10-water-damage`.
  *Fix:* check each CMS item's "Exclude from sitemap" setting and republish the site.
- [ ] **`og:url` missing on all 73 pages; `og:image` missing on 4 posts** (`/post/iphone-17-water-damage`, `/post/pixel-10-will-not-charge`, `/post/pixel-10-black-screen-no-image`, `/post/iphone-17-charging-port-loose`). Shared links will render without a preview image.
- [ ] **All 266 images are lazy-loaded, including the header logo and above-the-fold imagery.** Lazy-loading the LCP element delays it. 262 of 266 images also lack explicit `width`/`height`, a common cause of layout shift.
- [ ] **Header logo** — now links to `/` (fixed 25 Oct). Still lacks an accessible name (Lighthouse `link-name` failure on `/`); add `aria-label="Best Tech Repair home"` in the Designer.

## Opportunities (nice to have)

- [ ] Two titles exceed 60 characters and will truncate: `/post/pixel-10-black-screen-no-image` (62), `/post/iphone-17-charging-port-loose` (63).
- [ ] One meta description is short: `/post/galaxy-s25-cracked-screen` (116 chars).
- [ ] `/price` and `/career` return 404. If either URL has external links or residual impressions in Search Console, 301-redirect it to `/work` or `/contact`.
- [ ] No `aggregateRating` in the `LocalBusiness` schema, although the homepage cites a 5.0 Google rating. Only add it if the reviews are collected first-party on the site; Google does not show star rich results for self-serving reviews of a business on its own site, so the value here is limited.
- [ ] Testimonial avatars on the homepage carry empty alt text; acceptable if purely decorative.

## Passing

- `robots.txt` allows all crawlers and declares the sitemap.
- `http://` permanently redirects (301) to `https://`; HSTS header present.
- Unknown URLs return a true 404 status with a branded page.
- No duplicate titles or meta descriptions across 73 pages.
- Every page has a viewport tag, `lang="en"`, Twitter Card tags, and no empty headings.
- Service and repair pages carry `Service` + `BreadcrumbList` schema; every post carries `BlogPosting`.
- `LocalBusiness` schema is complete: address, geo-coordinates, opening hours (10:00–22:00, 7 days), telephone, `hasMap`, `sameAs`.
- Every blog post links to at least one service page (59 / 59 in sitemap), so posts do pass equity to commercial pages.
- Blog content depth is strong: median 1,571 words per post.
- Lighthouse SEO category: 100 / 100 (mobile and desktop).

## Recommended sequence

1. **This week:** fix the 5 sitemap exclusions and the header logo link (minutes in the Webflow Designer).
2. **This week:** run PageSpeed Insights on mobile to close the performance question.
3. **Next two weeks:** build the internal-linking structure — blog pagination, related-guide lists on the 9 service and repair pages, contextual post-to-post links.
4. **Next two weeks:** add `og:url` site-wide and `og:image` to the 4 newest posts; remove lazy-loading from the logo and hero.
5. **Ongoing:** monitor indexed-page count in Search Console; it should rise toward 78 once orphaned posts are linked.

## Method and limitations

- Every URL in `sitemap.xml`, plus the 5 posts found linked from `/blog`, `/price`, `/career`, a known-bad URL and the `http://` root, was fetched directly and its HTML parsed. Counts are measured, not estimated.
- **Performance (21 Oct):** PageSpeed Insights returned HTTP 429 and a local run could not load Webflow's CDN, so no figures were reported. **Performance (25 Oct):** measured with a hosted Lighthouse 13.5 run (mobile, single lab run per page); figures are lab data, not field data, and single runs can vary by ±10 points.
- The `www.best-tech.co.uk` host could not be tested from the audit environment.
- Orphan detection covers links in server-rendered HTML; links injected later by JavaScript are not counted.
- Not covered: backlinks, keyword rankings, competitor comparison, Google Business Profile, Search Console coverage data.

*The overall score uses the weights in the summary table; performance was excluded from the score because no valid measurement was available.*
