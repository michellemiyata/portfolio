import os
import glob

noise_css = """
        body::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            pointer-events: none;
            z-index: 9999;
            opacity: 0.04;
            background-image: url('data:image/svg+xml,%3Csvg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"%3E%3Cfilter id="noiseFilter"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noiseFilter)"/%3E%3C/svg%3E');
        }
"""

os.chdir("/Users/michellemiyata/Downloads/portfolio-main")
for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "body::before" not in content and "</style>" in content:
        content = content.replace("</style>", noise_css + "    </style>", 1)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"Added noise to {filepath}")
