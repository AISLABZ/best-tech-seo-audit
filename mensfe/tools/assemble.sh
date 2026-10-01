#!/usr/bin/env bash
# Builds preview thumbnails, the overview PDF and one PDF per direction.
set -euo pipefail
cd "$(dirname "$0")/../redesign"
export NODE_PATH=$(npm root -g)
node ../tools/render-redesign.js .
mkdir -p previews pdf
for d in a b c; do
  convert build/$d-home-desktop.png -crop 1440x900+0+0 +repage -resize 1200x -quality 82 previews/$d-home-hero.jpg
  convert build/$d-home-mobile.png -crop 780x1688+0+0 +repage -resize 390x -quality 82 previews/$d-home-mobile.jpg
  for p in home boards topic article; do convert build/$d-$p-desktop.png -resize 900x -quality 80 previews/$d-$p-full.jpg; done
  convert build/$d-home-mobile.png -resize 390x -quality 80 previews/$d-home-mobile-full.jpg
done
node ../tools/pdf.js index.html build/overview.pdf
for d in a b c; do
  pdfunite build/overview.pdf build/$d-home-desktop.pdf build/$d-home-mobile.pdf build/$d-boards-desktop.pdf build/$d-topic-desktop.pdf build/$d-article-desktop.pdf pdf/mensfe-redesign-direction-$d.pdf
done
pdfunite build/overview.pdf \
  build/a-home-desktop.pdf build/a-home-mobile.pdf build/a-boards-desktop.pdf build/a-topic-desktop.pdf build/a-article-desktop.pdf \
  build/b-home-desktop.pdf build/b-home-mobile.pdf build/b-boards-desktop.pdf build/b-topic-desktop.pdf build/b-article-desktop.pdf \
  build/c-home-desktop.pdf build/c-home-mobile.pdf build/c-boards-desktop.pdf build/c-topic-desktop.pdf build/c-article-desktop.pdf \
  pdf/mensfe-redesign-all-directions.pdf
ls -la pdf
