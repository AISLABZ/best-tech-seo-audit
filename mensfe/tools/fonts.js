// Serves Google Fonts requests through curl (which trusts the environment's CA bundle),
// caching responses locally, so headless Chromium renders the real web fonts.
const { execFileSync } = require('child_process');
const crypto = require('crypto');
const fs = require('fs');
const os = require('os');
const path = require('path');
const cacheDir = path.join(os.tmpdir(), 'mensfe-font-cache');
fs.mkdirSync(cacheDir, { recursive: true });
const UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36';
module.exports = async function useFonts(page) {
  await page.route(/https:\/\/fonts\.(googleapis|gstatic)\.com\//, async (route) => {
    const url = route.request().url();
    const file = path.join(cacheDir, crypto.createHash('sha1').update(url).digest('hex'));
    if (!fs.existsSync(file)) {
      fs.writeFileSync(file, execFileSync('curl', ['-sSfL', '--compressed', '-A', UA, url], { maxBuffer: 50 * 1024 * 1024 }));
    }
    const type = url.includes('googleapis') ? 'text/css' : 'font/woff2';
    await route.fulfill({ status: 200, contentType: type, body: fs.readFileSync(file), headers: { 'access-control-allow-origin': '*' } });
  });
};
