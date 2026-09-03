const fs = require('fs');
const zlib = require('zlib');

const bmpBuffer = fs.readFileSync('temp_cloud.bmp');

const pixelOffset = bmpBuffer.readUInt32LE(10);
const width = bmpBuffer.readInt32LE(18);
const height = Math.abs(bmpBuffer.readInt32LE(22));
const bpp = bmpBuffer.readUInt16LE(28);

console.log(`BMP: ${width}x${height}, ${bpp} bpp, offset: ${pixelOffset}`);

// In visible image:
// Top ~78% is the Cloud Emblem
// Bottom ~22% is the text "2) SINGLE-LINE CLOUD MIST."

// In bottom-up BMP:
// BMP Y = 0 to (0.22 * height) is the text
// BMP Y = (0.22 * height) to height is the cloud emblem!

const textHeight = Math.floor(height * 0.22);
const cloudHeight = height - textHeight;

const rowSize = Math.floor((bpp * width + 31) / 32) * 4;
const rgbaBuffer = Buffer.alloc(width * cloudHeight * 4);

let minX = width, maxX = 0, minY = cloudHeight, maxY = 0;

for (let y = 0; y < cloudHeight; y++) {
  // Top-down visible Y=0 corresponds to BMP Y = height - 1 - y
  const bmpY = height - 1 - y;
  const rowOffset = pixelOffset + bmpY * rowSize;
  
  for (let x = 0; x < width; x++) {
    const srcPixelOffset = rowOffset + x * (bpp / 8);
    const b = bmpBuffer[srcPixelOffset];
    const g = bmpBuffer[srcPixelOffset + 1];
    const r = bmpBuffer[srcPixelOffset + 2];
    
    // Luminance
    const lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0;
    const dstOffset = (y * width + x) * 4;
    
    // Background is off-white (#FDFBF7 ~ 0.93+)
    if (lum > 0.92) {
      rgbaBuffer[dstOffset] = 0;
      rgbaBuffer[dstOffset + 1] = 0;
      rgbaBuffer[dstOffset + 2] = 0;
      rgbaBuffer[dstOffset + 3] = 0;
    } else {
      let alpha = 255;
      if (lum > 0.65) {
        alpha = Math.round((1.0 - (lum - 0.65) / (0.92 - 0.65)) * 255);
      }
      
      // Target stroke color: Terracotta Rose #B28F81 (178, 143, 129)
      rgbaBuffer[dstOffset] = 178;
      rgbaBuffer[dstOffset + 1] = 143;
      rgbaBuffer[dstOffset + 2] = 129;
      rgbaBuffer[dstOffset + 3] = alpha;
      
      if (alpha > 20) {
        if (x < minX) minX = x;
        if (x > maxX) maxX = x;
        if (y < minY) minY = y;
        if (y > maxY) maxY = y;
      }
    }
  }
}

// Bounding box with small padding
const pad = 12;
const bMinX = Math.max(0, minX - pad);
const bMaxX = Math.min(width - 1, maxX + pad);
const bMinY = Math.max(0, minY - pad);
const bMaxY = Math.min(cloudHeight - 1, maxY + pad);

const finalW = bMaxX - bMinX + 1;
const finalH = bMaxY - bMinY + 1;

console.log(`Bounding box: ${finalW}x${finalH} (from [${bMinX},${bMinY}] to [${bMaxX},${bMaxY}])`);

const finalRGBA = Buffer.alloc(finalW * finalH * 4);
for (let y = 0; y < finalH; y++) {
  for (let x = 0; x < finalW; x++) {
    const srcIdx = ((bMinY + y) * width + (bMinX + x)) * 4;
    const dstIdx = (y * finalW + x) * 4;
    finalRGBA[dstIdx] = rgbaBuffer[srcIdx];
    finalRGBA[dstIdx + 1] = rgbaBuffer[srcIdx + 1];
    finalRGBA[dstIdx + 2] = rgbaBuffer[srcIdx + 2];
    finalRGBA[dstIdx + 3] = rgbaBuffer[srcIdx + 3];
  }
}

// CRC32
const crcTable = [];
for (let n = 0; n < 256; n++) {
  let c = n;
  for (let k = 0; k < 8; k++) {
    if (c & 1) c = 0xedb88320 ^ (c >>> 1);
    else c = c >>> 1;
  }
  crcTable[n] = c;
}
function calculateCRC(buf) {
  let c = 0xffffffff;
  for (let i = 0; i < buf.length; i++) {
    c = crcTable[(c ^ buf[i]) & 0xff] ^ (c >>> 8);
  }
  return (c ^ 0xffffffff) >>> 0;
}

function makeChunk(type, data) {
  const len = Buffer.alloc(4);
  len.writeUInt32BE(data.length, 0);
  const typeBuf = Buffer.from(type);
  const combined = Buffer.concat([typeBuf, data]);
  const crc = calculateCRC(combined);
  const crcBuf = Buffer.alloc(4);
  crcBuf.writeUInt32BE(crc, 0);
  return Buffer.concat([len, typeBuf, data, crcBuf]);
}

function createPNG(w, h, rgba) {
  const scanlines = Buffer.alloc(h * (w * 4 + 1));
  for (let y = 0; y < h; y++) {
    const lineOffset = y * (w * 4 + 1);
    scanlines[lineOffset] = 0;
    rgba.copy(scanlines, lineOffset + 1, y * w * 4, (y + 1) * w * 4);
  }
  
  const compressed = zlib.deflateSync(scanlines);
  const sig = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(w, 0);
  ihdr.writeUInt32BE(h, 4);
  ihdr[8] = 8;
  ihdr[9] = 6;
  ihdr[10] = 0;
  ihdr[11] = 0;
  ihdr[12] = 0;

  const chunkIHDR = makeChunk('IHDR', ihdr);
  const chunkIDAT = makeChunk('IDAT', compressed);
  const chunkIEND = makeChunk('IEND', Buffer.alloc(0));

  return Buffer.concat([sig, chunkIHDR, chunkIDAT, chunkIEND]);
}

const pngBuffer = createPNG(finalW, finalH, finalRGBA);
fs.writeFileSync('cloud_emblem.png', pngBuffer);
fs.writeFileSync('portfolio/cloud_emblem.png', pngBuffer);

// Dark mode version (Lavender #9A86A8 - 154, 134, 168)
const darkRGBA = Buffer.from(finalRGBA);
for (let i = 0; i < darkRGBA.length; i += 4) {
  if (darkRGBA[i + 3] > 0) {
    darkRGBA[i] = 154;
    darkRGBA[i + 1] = 134;
    darkRGBA[i + 2] = 168;
  }
}
const darkPngBuffer = createPNG(finalW, finalH, darkRGBA);
fs.writeFileSync('cloud_emblem_dark.png', darkPngBuffer);
fs.writeFileSync('portfolio/cloud_emblem_dark.png', darkPngBuffer);

const base64Light = pngBuffer.toString('base64');
const base64Dark = darkPngBuffer.toString('base64');

// Aspect ratio of the emblem
const emblemAspect = finalW / finalH;
const emblemH = 54;
const emblemW = Math.round(emblemH * emblemAspect);
const totalW = emblemW + 185;

const svgContent = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${totalW} 60" fill="none">
  <style>
    .cloud-light { display: block; }
    .cloud-dark { display: none; }
    .text-title {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 24px;
      font-weight: 500;
      letter-spacing: -0.01em;
      fill: #1A1514;
    }
    .text-sub {
      font-weight: 300;
      fill: #B28F81;
    }
    @media (prefers-color-scheme: dark) {
      .cloud-light { display: none; }
      .cloud-dark { display: block; }
      .text-title { fill: #FFFFFF; }
      .text-sub { fill: #9A86A8; }
    }
    .dark-theme .cloud-light { display: none !important; }
    .dark-theme .cloud-dark { display: block !important; }
    .dark-theme .text-title { fill: #FFFFFF !important; }
    .dark-theme .text-sub { fill: #9A86A8 !important; }
  </style>

  <!-- Pixel-Perfect Exact Single-Line Cloud Mist Artwork -->
  <g transform="translate(0, 3)">
    <image class="cloud-light" href="data:image/png;base64,${base64Light}" width="${emblemW}" height="${emblemH}" />
    <image class="cloud-dark" href="data:image/png;base64,${base64Dark}" width="${emblemW}" height="${emblemH}" />
  </g>

  <!-- Typography -->
  <text x="${emblemW + 14}" y="38" class="text-title">Miyata<tspan class="text-sub">Creative</tspan></text>
</svg>
`;

fs.writeFileSync('miyata_logo.svg', svgContent);
fs.writeFileSync('portfolio/miyata_logo.svg', svgContent);
console.log('SUCCESS! Pixel-perfect exact upright artwork generated!');
