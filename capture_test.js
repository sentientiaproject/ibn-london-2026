const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  try {
    const browser = await puppeteer.launch({
      executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--allow-file-access-from-files']
    });
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
    
    const filePath = 'file:///' + path.resolve(__dirname, 'cinematic_advert_15s.html').replace(/\\/g, '/');
    console.log('Loading:', filePath);
    await page.goto(filePath, { waitUntil: 'networkidle0' });
    
    // Test keyframes
    const framesToCapture = [
      { frame: 50, name: 'advert_frame_01_lotus.png' },
      { frame: 160, name: 'advert_frame_02_commons.png' },
      { frame: 280, name: 'advert_frame_03_packages.png' },
      { frame: 390, name: 'advert_frame_04_cta.png' }
    ];

    for (const item of framesToCapture) {
      await page.evaluate((f) => {
        renderFrame(f);
      }, item.frame);
      await new Promise(r => setTimeout(r, 100));
      const el = await page.$('#videoViewport');
      await el.screenshot({ path: path.join(__dirname, item.name) });
      console.log(`Saved ${item.name}`);
    }

    await browser.close();
    console.log('All keyframes successfully captured!');
  } catch (err) {
    console.error('Error during capture:', err);
  }
})();
