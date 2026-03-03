import re
import glob
import os

files = glob.glob('/Users/michellemiyata/Downloads/portfolio-main/case_study_*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Make sure Work is underlined active, not Home
    content = content.replace('<a href="index.html" class="link-underline active" aria-current="page">Home</a>', '<a href="index.html" class="link-underline">Home</a>')
    
    # If work is just link-underline, make it link-underline active
    content = content.replace('<a href="work.html" class="text-stone-900 font-medium">Work</a>', '<a href="work.html" class="link-underline active" aria-current="page">Work</a>')
    content = content.replace('<a href="work.html" class="link-underline">Work</a>', '<a href="work.html" class="link-underline active" aria-current="page">Work</a>')

    with open(filepath, 'w') as f:
        f.write(content)
print("done")
