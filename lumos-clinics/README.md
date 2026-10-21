# Lumos Dental & Aesthetic Clinic — SEO, AEO & GEO proposal

Client-ready proposal for **lumosclinics.com** in the AiS LABZ format, dated 21 October 2026:
[`AIS-LABZ-Lumos-Clinics-SEO-AEO-GEO-Proposal.pdf`](AIS-LABZ-Lumos-Clinics-SEO-AEO-GEO-Proposal.pdf) (19 pages).

## Headline findings

| Metric | Value |
|---|---|
| URLs in XML sitemaps (all HTTP 200) | 127 |
| Pages with `nosnippet` robots directive | 36 |
| Treatments duplicated at a root URL and a `/treatments/` URL | 18 |
| Pages with no H1 / with 3–19 H1s | 34 / 23 |
| Pages missing a meta description | 29 |
| Titles over 60 characters | 80 |
| Images without alt text | 1,891 |
| Lighthouse mobile performance / LCP | 28 / 10.9 s |
| Homepage weight (mobile) | 12.7 MB |
| GPTBot response at CDN | HTTP 429 |
| Published blog posts | 0 |

## Rebuilding

```
python3 crawl.py                       # writes crawl.json from the live sitemaps
python3 build_proposal.py out.pdf      # requires reportlab and Liberation fonts
```

Raw crawl and Lighthouse summaries are in `data/`. Keyword search volumes are not included;
they are to be baselined in Month 1 from Search Console and Keyword Planner.
