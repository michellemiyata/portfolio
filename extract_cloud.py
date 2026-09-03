import struct
import zlib
import base64

with open('sheet.bmp', 'rb') as f:
    bmp_data = f.read()

offset = struct.unpack('<I', bmp_data[10:14])[0]
width = struct.unpack('<i', bmp_data[18:22])[0]
height = struct.unpack('<i', bmp_data[22:26])[0]
bpp = struct.unpack('<H', bmp_data[28:30])[0]

is_top_down = (height < 0)
abs_height = abs(height)

# Pure Cloud Emblem Crop (excluding text completely):
# X: 740 to 1320
# Y: 210 to 410

min_x, max_x = 740, 1320
min_y, max_y = 210, 410

crop_w = max_x - min_x
crop_h = max_y - min_y

row_size = ((bpp * width + 31) // 32) * 4
rgba_data = bytearray(crop_w * crop_h * 4)

non_empty_min_x = crop_w
non_empty_max_x = 0
non_empty_min_y = crop_h
non_empty_max_y = 0

for y in range(crop_h):
    sheet_y = min_y + y
    if is_top_down:
        bmp_y = sheet_y
    else:
        bmp_y = abs_height - 1 - sheet_y
        
    row_offset = offset + bmp_y * row_size
    
    for x in range(crop_w):
        sheet_x = min_x + x
        pixel_offset = row_offset + sheet_x * (bpp // 8)
        
        b = bmp_data[pixel_offset]
        g = bmp_data[pixel_offset + 1]
        r = bmp_data[pixel_offset + 2]
        
        lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
        dst_offset = (y * crop_w + x) * 4
        
        # Background is warm off-white (> 0.91)
        if lum > 0.91:
            rgba_data[dst_offset:dst_offset+4] = b'\x00\x00\x00\x00'
        else:
            if lum < 0.65:
                alpha = 255
            else:
                alpha = int((1.0 - (lum - 0.65) / (0.91 - 0.65)) * 255)
            
            # Stroke color: Warm Terracotta Rose #B28F81 (178, 143, 129)
            rgba_data[dst_offset] = 178
            rgba_data[dst_offset + 1] = 143
            rgba_data[dst_offset + 2] = 129
            rgba_data[dst_offset + 3] = alpha
            
            if alpha > 25:
                if x < non_empty_min_x: non_empty_min_x = x
                if x > non_empty_max_x: non_empty_max_x = x
                if y < non_empty_min_y: non_empty_min_y = y
                if y > non_empty_max_y: non_empty_max_y = y

pad = 12
b_min_x = max(0, non_empty_min_x - pad)
b_max_x = min(crop_w - 1, non_empty_max_x + pad)
b_min_y = max(0, non_empty_min_y - pad)
b_max_y = min(crop_h - 1, non_empty_max_y + pad)

final_w = b_max_x - b_min_x + 1
final_h = b_max_y - b_min_y + 1

print(f"Pristine Option 2 extracted bounding box: {final_w}x{final_h}")

final_rgba = bytearray(final_w * final_h * 4)
for y in range(final_h):
    for x in range(final_w):
        src_idx = ((b_min_y + y) * crop_w + (b_min_x + x)) * 4
        dst_idx = (y * final_w + x) * 4
        final_rgba[dst_idx:dst_idx+4] = rgba_data[src_idx:src_idx+4]

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

# Dark mode: Soft Lavender #9A86A8 (154, 134, 168)
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

emblem_aspect = final_w / final_h
emblem_h = 56
emblem_w = int(round(emblem_h * emblem_aspect))
total_w = emblem_w + 180

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} 62" fill="none">
  <style>
    .cloud-light {{ display: block; }}
    .cloud-dark {{ display: none; }}
    .text-title {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 24px;
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

  <!-- Pixel-Perfect Exact Single-Line Cloud Mist Artwork -->
  <g transform="translate(0, 3)">
    <image class="cloud-light" href="data:image/png;base64,{b64_light}" width="{emblem_w}" height="{emblem_h}" />
    <image class="cloud-dark" href="data:image/png;base64,{b64_dark}" width="{emblem_w}" height="{emblem_h}" />
  </g>

  <!-- Typography -->
  <text x="{emblem_w + 14}" y="39" class="text-title">Miyata<tspan class="text-sub">Creative</tspan></text>
</svg>
'''

with open('miyata_logo.svg', 'w') as f:
    f.write(svg_content)
with open('portfolio/miyata_logo.svg', 'w') as f:
    f.write(svg_content)

print("SUCCESS! Created pristine pixel-perfect miyata_logo.svg!")
