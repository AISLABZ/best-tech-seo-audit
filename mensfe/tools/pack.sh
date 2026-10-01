#!/usr/bin/env bash
# Builds mensfe/Mensfe-Client-Pack.zip from the audit and redesign outputs.
set -euo pipefail
M="$(cd "$(dirname "$0")/.." && pwd)"
W="$(mktemp -d)"; P="$W/Mensfe-Client-Pack"
mkdir -p "$P/1-Audits/web-versions" "$P/2-Redesign-PDF" "$P/3-Redesign-HTML"
cp "$M/audit/seo-audit.pdf" "$P/1-Audits/Mensfe-SEO-Audit.pdf"
cp "$M/audit/ai-visibility-audit.pdf" "$P/1-Audits/Mensfe-AI-Visibility-Audit.pdf"
cp "$M/audit/seo-audit.html" "$P/1-Audits/web-versions/Mensfe-SEO-Audit.html"
cp "$M/audit/ai-visibility-audit.html" "$P/1-Audits/web-versions/Mensfe-AI-Visibility-Audit.html"
cp "$M/redesign/pdf/mensfe-redesign-all-directions.pdf" "$P/2-Redesign-PDF/Mensfe-Redesign-All-Directions.pdf"
for pair in a:A-Harbour b:B-Clear c:C-Stories d:D-Forum-Dark d-light:D-Forum-Light; do
  cp "$M/redesign/pdf/mensfe-redesign-direction-${pair%%:*}.pdf" "$P/2-Redesign-PDF/Mensfe-Redesign-Direction-${pair#*:}.pdf"
done
cp -r "$M/redesign/index.html" "$M/redesign/a" "$M/redesign/b" "$M/redesign/c" "$M/redesign/d" "$M/redesign/d-light" "$M/redesign/previews" "$P/3-Redesign-HTML/"
cat > "$P/START-HERE.txt" <<'TXT'
MENSFE — CLIENT PACK
Prepared 1 October 2026

1-Audits
  Mensfe-SEO-Audit.pdf ............ 28 findings, priorities and a 90-day roadmap
  Mensfe-AI-Visibility-Audit.pdf .. how ChatGPT, Google AI Overviews, Perplexity etc. see Mensfe
  web-versions/ ................... the same reports as web pages

2-Redesign-PDF
  Mensfe-Redesign-All-Directions.pdf .. overview + all four directions (start here)
  Mensfe-Redesign-Direction-A/B/C ..... overview + one direction each
  Mensfe-Redesign-Direction-D-Forum-Dark / -Light .. Direction D in each theme

3-Redesign-HTML
  Open index.html in a web browser, then click through each direction's pages.
  Resize the browser window (or open on a phone) to see the mobile layouts.

The four directions:
  A · Harbour  — bold and branded website front
  B · Clear    — clean and clinical website front
  C · Stories  — warm and human website front
  D · Forum    — a true message board: the board index is the homepage
                 (dark and light versions; each page has a Dark / Light switch)

Notes: member and post counts appear as [n] placeholders; sample forum posts are
illustrative; the medical information page should be checked by a medical reviewer.
An internet connection is needed for the web fonts in the HTML files.
TXT
rm -f "$M/Mensfe-Client-Pack.zip"
(cd "$W" && zip -qr "$M/Mensfe-Client-Pack.zip" Mensfe-Client-Pack)
rm -rf "$W"
ls -la "$M/Mensfe-Client-Pack.zip"
