import struct
import zlib
import base64

with open('cloud_emblem.png', 'rb') as f:
    png_light = f.read()
with open('cloud_emblem_dark.png', 'rb') as f:
    png_dark = f.read()

b64_light = base64.b64encode(png_light).decode('ascii')
b64_dark = base64.b64encode(png_dark).decode('ascii')

# Emblem dimensions
# Tight width: 469, height: 200 -> Aspect ratio: 2.345
# At height = 44, width = 103
emblem_h = 44
emblem_w = 103

# Spacing: tighten gap to 6px so it sits right next to the mark without dead space
text_x = emblem_w + 6
total_w = text_x + 155

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} 48" fill="none">
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

  <!-- Tight, cohesive lockup: Cloud Mist + Typography -->
  <g transform="translate(0, 2)">
    <image class="cloud-light" href="data:image/png;base64,{b64_light}" width="{emblem_w}" height="{emblem_h}" />
    <image class="cloud-dark" href="data:image/png;base64,{b64_dark}" width="{emblem_w}" height="{emblem_h}" />
  </g>

  <!-- Typography positioned right next to emblem -->
  <text x="{text_x}" y="31" class="text-title">Miyata<tspan class="text-sub">Creative</tspan></text>
</svg>
'''

with open('miyata_logo.svg', 'w') as f:
    f.write(svg_content)
with open('portfolio/miyata_logo.svg', 'w') as f:
    f.write(svg_content)

print(f"Generated tight logo with text_x={text_x}, total_w={total_w}")
