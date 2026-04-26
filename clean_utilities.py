import os
import glob
import re

os.chdir("/Users/michellemiyata/Downloads/portfolio-main")

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Clean hardcoded tailwind colors so the emotional CSS variables take over
    content = re.sub(r'\bbg-stone-50\b', '', content)
    content = re.sub(r'\btext-stone-900\b', '', content)
    content = re.sub(r'\btext-stone-800\b', '', content)
    content = re.sub(r'\btext-stone-700\b', '', content)
    content = re.sub(r'\btext-stone-600\b', '', content)
    content = re.sub(r'\btext-stone-500\b', '', content)
    
    # Add !important to body in the CSS to override Tailwind
    content = content.replace("background: linear-gradient(-45deg, var(--gradient-1), var(--gradient-2), var(--gradient-3));", 
                              "background: linear-gradient(-45deg, var(--gradient-1), var(--gradient-2), var(--gradient-3)) !important;")
    
    # Replace solid card backgrounds with glassmorphism 'dynamic-bg'
    content = re.sub(r'\bbg-white\b', 'dynamic-bg', content)
    content = re.sub(r'\bbg-stone-100\b', 'dynamic-bg', content)
    content = re.sub(r'\bborder-stone-100\b', 'dynamic-border', content)
    content = re.sub(r'\bborder-stone-200\b', 'dynamic-border', content)

    # Some headers might need 'text-[var(--text-primary)]' instead of nothing if they had custom colors
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Cleaned utility classes in {filepath}")
