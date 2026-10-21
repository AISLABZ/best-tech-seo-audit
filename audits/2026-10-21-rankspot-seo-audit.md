# RankSpot SEO Audit — best-tech.co.uk

**Audit date:** 21 October 2026
**Baseline:** 13 August 2026 audit (`index.html` in this repository)
**Scope:** 78 live URLs (73 in the XML sitemap, 5 published but missing from it), plus the two legacy template URLs `/price` and `/career`

## Executive summary

**Overall score: 84 / 100 — Good, with room for improvement** (performance excluded; see Limitations)

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
| Internal linking | Not assessed | 43 of 64 posts orphaned | 5 / 15 |
| Social / Open Graph | Not assessed | `og:url` missing site-wide | 8 / 10 |
| **Total** | | | **84 / 100** |

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
| 8 | Mobile LCP 9.0s (4K hero video) | **Not re-measured** — 3840×2160 video source still referenced in homepage markup |
| 9 | Mobile CLS 0.319 | **Not re-measured** |

## Critical issues (must fix)

- [ ] **43 of 64 blog posts are orphaned.** No crawled page links to them; they are discoverable only through the sitemap. `/blog` lists the 12 most recent posts with no pagination or category archive, and no homepage, service or repair page links to any post. Only 8 posts link to another post. Orphaned pages receive no internal link equity and are crawled and ranked less reliably.
  *Fix:* add pagination or a full archive to `/blog`; add a "Related guides" CMS list to each `/works/*` and `/services/*` page filtered by topic; add 2–3 contextual post-to-post links per article.
- [ ] **Performance has not been verified since August.** The homepage still references the 3840×2160 hero video (`13820343 3840 2160 30Fps_mp4.mp4` / `.webm`). A `besttechvideofixes` script is loaded and may mitigate this, but that cannot be confirmed without a lab run.
  *Fix:* run PageSpeed Insights (mobile) on `/` and one `/post/*` URL; if LCP exceeds 2.5s, serve a ≤ 720p video or a static poster on mobile.

## Warnings (should fix)

- [ ] **5 published posts are missing from `sitemap.xml`** although they are linked from `/blog` and return 200 with valid canonicals:
  `/post/galaxy-s25-charging-port-loose`, `/post/galaxy-s25-will-not-charge`, `/post/iphone-17-cracked-screen`, `/post/macbook-air-m4-battery-draining-fast`, `/post/pixel-10-water-damage`.
  *Fix:* check each CMS item's "Exclude from sitemap" setting and republish the site.
- [ ] **`og:url` missing on all 73 pages; `og:image` missing on 4 posts** (`/post/iphone-17-water-damage`, `/post/pixel-10-will-not-charge`, `/post/pixel-10-black-screen-no-image`, `/post/iphone-17-charging-port-loose`). Shared links will render without a preview image.
- [ ] **All 266 images are lazy-loaded, including the header logo and above-the-fold imagery.** Lazy-loading the LCP element delays it. 262 of 266 images also lack explicit `width`/`height`, a common cause of layout shift.
- [ ] **Header logo links to `#`** (`<a href="#" class="w-nav-brand">`) and has no accessible name (Lighthouse `link-name` failure). It should link to `/` with an `aria-label`.

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
- **Performance was not measured.** PageSpeed Insights returned HTTP 429 (daily quota exhausted) on every attempt. A local Lighthouse run completed, but the audit environment's network proxy blocked Webflow's asset CDN, so its performance figures (mobile 96) reflect an unstyled HTML-only page and are **not reported as valid**. Its DOM-based accessibility and SEO checks are used above.
- The `www.best-tech.co.uk` host could not be tested from the audit environment.
- Orphan detection covers links in server-rendered HTML; links injected later by JavaScript are not counted.
- Not covered: backlinks, keyword rankings, competitor comparison, Google Business Profile, Search Console coverage data.

*The overall score uses the weights in the summary table; performance was excluded from the score because no valid measurement was available.*
