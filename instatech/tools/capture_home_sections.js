// Capture the browser-rendered HTML of the homepage sections that are built by JavaScript, plus the raw server HTML.
// Usage: node capture_home_sections.js <playwright-core path> <chromium path> <out dir>
const [,, pwPath, chrome, out] = process.argv;
const { chromium } = require(pwPath);
const fs = require('fs');
const IDS = ['tiles', 'cats', 'audio', 'chargers', 'rvgrid'];
(async () => {
  const b = await chromium.launch({ executablePath: chrome });
  const ctx = await b.newContext({ viewport: { width: 1366, height: 900 } });
  const p = await ctx.newPage();
  let raw = '';
  p.on('response', async r => { if (r.request().resourceType() === 'document' && r.status() === 200 && r.frame() === p.mainFrame()) raw = await r.text(); });
  await p.goto('https://instatech.uk/', { waitUntil: 'load', timeout: 90000 });
  await p.waitForTimeout(8000);
  const html = await p.evaluate(ids => Object.fromEntries(ids.map(i => [i, document.getElementById(i) ? document.getElementById(i).innerHTML : null])), IDS);
  fs.writeFileSync(out + '/home-sections.json', JSON.stringify(html));
  fs.writeFileSync(out + '/home-raw.html', raw);
  console.log(Object.entries(html).map(([k, v]) => k + ':' + (v ? v.length : 'missing')).join(' '), '| raw', raw.length);
  await b.close();
})();
