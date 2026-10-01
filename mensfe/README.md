# Mensfe — audits and forum redesign concepts

Client: Mensfe (www.mensfe.net), the men's fertility forum. Prepared 1 October 2026.

## Audits (`audit/`)
- `seo-audit.pdf` / `.html` — 28 findings (6 critical, 11 high, 11 medium), roadmap, starter `<head>` code.
- `ai-visibility-audit.pdf` / `.html` — prompt tests, AI readiness scorecard, 11 fixes, monthly tracking set, starter robots.txt and llms.txt.

The site needs a VPN from our location, so both audits are based on the homepage source and
screenshots supplied by the client plus public search results on the audit date.

## Redesign (`redesign/`)
Three directions, each with a homepage (desktop + mobile), board index, topic view and information page:
- **A · Harbour** — bold and branded (`redesign/a/`)
- **B · Clear** — clean and clinical (`redesign/b/`)
- **C · Stories** — warm and human (`redesign/c/`)

Open `redesign/index.html` for the "choose a direction" overview. PDFs are in `redesign/pdf/`
(one per direction plus `mensfe-redesign-all-directions.pdf`). `redesign/BRIEF.md` is the shared build brief.

## Rebuilding
`tools/assemble.sh` renders every page with Playwright/Chromium, regenerates previews and PDFs.
`tools/pdf.js` renders a single HTML file to A4 PDF. `tools/fonts.js` fetches Google Fonts through
curl so headless Chromium uses the real typefaces.
