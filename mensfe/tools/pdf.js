// Usage: node pdf.js <in.html> <out.pdf>   (A4, print CSS)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(inp), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font:8px sans-serif;color:#777;text-align:right;padding:0 15mm">Page <span class="pageNumber"></span> of <span class="totalPages"></span></div>' });
  await browser.close();
})();
