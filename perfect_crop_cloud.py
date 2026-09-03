import zlib
import struct
import base64

with open('cloud_emblem.png', 'rb') as f:
    d = f.read()

w, h = struct.unpack('>II', d[16:24])

idat = b''
pos = 8
while pos < len(d):
    length = struct.unpack('>I', d[pos:pos+4])[0]
    ctype = d[pos+4:pos+8]
    if ctype == b'IDAT':
        idat += d[pos+8:pos+8+length]
    pos += 12 + length

raw = zlib.decompress(idat)

# Find true tight bounding box of the cloud emblem alone
min_x, max_x = w, 0
min_y, max_y = h, 0

for y in range(h):
    for x in range(w):
        a = raw[y*(w*4+1) + 1 + x*4 + 3]
        # Ignore anything past x > 356 (which was card border)
        if a > 25 and x <= 356:
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

pad = 4
crop_min_x = max(0, min_x - pad)
crop_max_x = min(w - 1, max_x + pad)
crop_min_y = max(0, min_y - pad)
crop_max_y = min(h - 1, max_y + pad)

final_w = crop_max_x - crop_min_x + 1
final_h = crop_max_y - crop_min_y + 1

print(f"True tight cloud emblem size: {final_w}x{final_h} (X: {crop_min_x} to {crop_max_x}, Y: {crop_min_y} to {crop_max_y})")

final_rgba = bytearray(final_w * final_h * 4)
for y in range(final_h):
    src_y = crop_min_y + y
    for x in range(final_w):
        src_x = crop_min_x + x
        src_idx = src_y * (w * 4 + 1) + 1 + src_x * 4
        dst_idx = (y * final_w + x) * 4
        final_rgba[dst_idx:dst_idx+4] = raw[src_idx:src_idx+4]

def make_png(w, h, rgba):
    raw_scanlines = bytearray()
    for y in range(h):
        raw_scanlines.append(0)
        raw_scanlines.extend(rgba[y*w*4 : (y+1)*w*4])
    
    compressed = zlib.compress(bytes(raw_scanlines), 9)
    
    def make_chunk(ctype, cdata):
        buf = bytearray(ctype)
        buf.extend(cdata)
        crc = zlib.crc32(buf)
        length = struct.pack('>I', len(cdata))
        crc_bytes = struct.pack('>I', crc)
        return length + buf + crc_bytes
    
    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)
    return sig + make_chunk(b'IHDR', ihdr) + make_chunk(b'IDAT', compressed) + make_chunk(b'IEND', b'')

png_light = make_png(final_w, final_h, final_rgba)
with open('cloud_emblem.png', 'wb') as f:
    f.write(png_light)
with open('portfolio/cloud_emblem.png', 'wb') as f:
    f.write(png_light)

# Dark mode (Lavender #9A86A8 - 154, 134, 168)
dark_rgba = bytearray(final_rgba)
for i in range(0, len(dark_rgba), 4):
    if dark_rgba[i + 3] > 0:
        dark_rgba[i] = 154
        dark_rgba[i + 1] = 134
        dark_rgba[i + 2] = 168

png_dark = make_png(final_w, final_h, dark_rgba)
with open('cloud_emblem_dark.png', 'wb') as f:
    f.write(png_dark)
with open('portfolio/cloud_emblem_dark.png', 'wb') as f:
    f.write(png_dark)

b64_light = base64.b64encode(png_light).decode('ascii')
b64_dark = base64.b64encode(png_dark).decode('ascii')

# Render proportions:
# At emblem height = 40, width = 40 * (final_w / final_h)
emblem_aspect = final_w / final_h
emblem_h = 42
emblem_w = int(round(emblem_h * emblem_aspect))

# Gap between emblem and text: 8px
gap = 8
text_x = emblem_w + gap
total_w = text_x + 162

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} 46" fill="none">
  <style>
    .cloud-light {{ display: block; }}
    .cloud-dark {{ display: none; }}
    .text-title {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 21px;
      font-weight: 500;
      letter-spacing: -0.01em;
      fill: #1A1514;
    }}
    .text-sub {{
      font-weight: 300;
      fill: #B28F81;
    }}
    @media (prefers-color-scheme: dark) {{
      .cloud-light {{ display: none; }}
      .cloud-dark {{ display: block; }}
      .text-title {{ fill: #FFFFFF; }}
      .text-sub {{ fill: #9A86A8; }}
    }}
    .dark-theme .cloud-light {{ display: none !important; }}
    .dark-theme .cloud-dark {{ display: block !important; }}
    .dark-theme .text-title {{ fill: #FFFFFF !important; }}
    .dark-theme .text-sub {{ fill: #9A86A8 !important; }}
  </style>

  <!-- Tight Lockup: Pure Cloud Emblem + MiyataCreative -->
  <g transform="translate(0, 2)">
    <image class="cloud-light" href="data:image/png;base64,{b64_light}" width="{emblem_w}" height="{emblem_h}" />
    <image class="cloud-dark" href="data:image/png;base64,{b64_dark}" width="{emblem_w}" height="{emblem_h}" />
  </g>

  <!-- Typography with exact 8px gap -->
  <text x="{text_x}" y="29" class="text-title">Miyata<tspan class="text-sub">Creative</tspan></text>
</svg>
'''

with open('miyata_logo.svg', 'w') as f:
    f.write(svg_content)
with open('portfolio/miyata_logo.svg', 'w') as f:
    f.write(svg_content)

print(f"Generated tight lockup: emblem_w={emblem_w}, text_x={text_x}, total_w={total_w}")
