#!/usr/bin/env bash
# Builds preview thumbnails, the overview PDF, one PDF per direction and the combined PDF.
set -euo pipefail
cd "$(dirname "$0")/../redesign"
export NODE_PATH=$(npm root -g)
node ../tools/render-redesign.js .
mkdir -p previews pdf
dirs="a b c d d-light"
pages() { if [ "${1:0:1}" = d ]; then echo "home-desktop home-mobile board-desktop topic-desktop article-desktop"; else echo "home-desktop home-mobile boards-desktop topic-desktop article-desktop"; fi; }
for d in $dirs; do
  convert build/$d-home-desktop.png -crop 1440x900+0+0 +repage -resize 1200x -quality 82 previews/$d-home-hero.jpg
  convert build/$d-home-mobile.png -crop 780x1688+0+0 +repage -resize 390x -quality 82 previews/$d-home-mobile.jpg
done
node ../tools/pdf.js index.html build/overview.pdf
all=""
for d in $dirs; do
  files=""; for p in $(pages $d); do files="$files build/$d-$p.pdf"; done
  pdfunite build/overview.pdf $files pdf/mensfe-redesign-direction-$d.pdf
  all="$all $files"
done
pdfunite build/overview.pdf $all pdf/mensfe-redesign-all-directions.pdf
ls -la pdf
