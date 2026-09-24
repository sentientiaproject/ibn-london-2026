const puppeteer = require('puppeteer');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const FFMPEG_PATH = path.resolve(__dirname, '.venv/Lib/site-packages/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe');
const AUDIO_PATH = path.resolve(__dirname, 'soundtrack.wav');
const OUTPUT_MP4 = path.resolve(__dirname, 'IBN_London_2026_Cinematic_Advert_9x16.mp4');

const FPS = 30;
const DURATION_SEC = 15;
const TOTAL_FRAMES = FPS * DURATION_SEC; // 450 frames

(async () => {
  console.log(`Starting Vertical Reel Render (${TOTAL_FRAMES} frames @ ${FPS}fps)...`);

  // Scale to standard 9:16 mobile resolution: 720x1280 (or 1080x1920)
  const ffmpegArgs = [
    '-y',
    '-f', 'image2pipe',
    '-vcodec', 'png',
    '-r', String(FPS),
    '-i', '-',
    '-i', AUDIO_PATH,
    '-vf', 'scale=720:1280',
    '-c:v', 'libx264',
    '-preset', 'veryfast',
    '-crf', '19',
    '-pix_fmt', 'yuv420p',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-shortest',
    OUTPUT_MP4
  ];

  const ffmpeg = spawn(FFMPEG_PATH, ffmpegArgs);

  ffmpeg.stderr.on('data', (d) => {
    const msg = d.toString();
    if (msg.includes('error') || msg.includes('Error')) {
      console.error('FFmpeg stderr:', msg);
    }
  });

  ffmpeg.stdin.on('error', (err) => {
    console.error('FFmpeg stdin error:', err.message);
  });

  const browser = await puppeteer.launch({
    executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--allow-file-access-from-files']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 720, height: 1280, deviceScaleFactor: 1 });

  const htmlPath = 'file:///' + path.resolve(__dirname, 'cinematic_advert_vertical_9_16.html').replace(/\\/g, '/');
  await page.goto(htmlPath, { waitUntil: 'networkidle0' });

  const viewport = await page.$('#videoViewport');

  console.log('Rendering vertical frames into FFmpeg pipeline...');
  const startTime = Date.now();

  for (let f = 0; f < TOTAL_FRAMES; f++) {
    await page.evaluate((frameNum) => {
      renderFrame(frameNum);
    }, f);

    const buf = await viewport.screenshot({ type: 'png' });
    
    if (ffmpeg.stdin.writable) {
      const canWrite = ffmpeg.stdin.write(buf);
      if (!canWrite) {
        await new Promise(r => ffmpeg.stdin.once('drain', r));
      }
    } else {
      console.error('FFmpeg stdin closed at frame', f);
      break;
    }

    if (f % 45 === 0 || f === TOTAL_FRAMES - 1) {
      const progress = Math.round((f / TOTAL_FRAMES) * 100);
      const elapsed = ((Date.now() - startTime) / 1000).toFixed(1);
      console.log(`Vertical progress: ${progress}% (Frame ${f}/${TOTAL_FRAMES}) [${elapsed}s]`);
    }
  }

  ffmpeg.stdin.end();

  await new Promise((resolve, reject) => {
    ffmpeg.on('close', (code) => {
      if (code === 0) {
        console.log(`✅ Vertical MP4 Render Complete: ${OUTPUT_MP4}`);
        resolve();
      } else {
        reject(new Error(`FFmpeg exited with code ${code}`));
      }
    });
  });

  await browser.close();
  const stats = fs.statSync(OUTPUT_MP4);
  console.log(`Vertical Reel File Size: ${(stats.size / (1024 * 1024)).toFixed(2)} MB`);
})();
