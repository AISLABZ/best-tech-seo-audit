// Renders each direction's pages to full-length PDF pages and PNG previews.
// Usage: node render-redesign.js <redesignDir>
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const root = path.resolve(process.argv[2]);
const out = path.join(root, 'build');
fs.mkdirSync(out, { recursive: true });
const shots = [
  ['home', 1440, 'Homepage — desktop'],
  ['home', 390, 'Homepage — mobile'],
  ['boards', 1440, 'Forum board index'],
  ['topic', 1440, 'Topic view'],
  ['article', 1440, 'Information page'],
];
(async () => {
  const browser = await chromium.launch();
  for (const dir of ['a', 'b', 'c']) {
    if (!fs.existsSync(path.join(root, dir, 'home.html'))) { console.log('skip', dir); continue; }
    for (const [name, w] of shots) {
      const tag = `${dir}-${name}-${w === 390 ? 'mobile' : 'desktop'}`;
      const page = await browser.newPage({ viewport: { width: w, height: 900 }, deviceScaleFactor: w === 390 ? 2 : 1 });
      await page.goto('file://' + path.join(root, dir, name + '.html'), { waitUntil: 'networkidle' });
      await page.evaluate(() => document.fonts.ready);
      await page.screenshot({ path: path.join(out, tag + '.png'), fullPage: true });
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      await page.emulateMedia({ media: 'screen' });
      const h = await page.evaluate(() => Math.ceil(document.documentElement.scrollHeight));
      await page.pdf({ path: path.join(out, tag + '.pdf'), width: w + 'px', height: (h + 2) + 'px', printBackground: true, pageRanges: '1' });
      console.log(tag, 'height', h, overflow > 0 ? `HORIZONTAL OVERFLOW ${overflow}px` : '');
      await page.close();
    }
  }
  await browser.close();
})();
