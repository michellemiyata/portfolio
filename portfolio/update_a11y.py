import os
import glob

def update_html_files():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Update light theme text colors
        content = content.replace('--text-primary: #2D2422;', '--text-primary: #1A1514; /* Darker for a11y */')
        content = content.replace('--text-secondary: #6B5B58;', '--text-secondary: #4A3E3C; /* Darker for a11y */')
        
        # 2. Update dark theme text colors
        content = content.replace('--text-primary: #F3F1F8;', '--text-primary: #FFFFFF; /* Brighter for a11y */')
        content = content.replace('--text-secondary: #A9A4BA;', '--text-secondary: #E0DEE8; /* Brighter for a11y */')
        
        # 3. Increase body font size
        if "font-family: 'Inter', sans-serif;" in content and "font-size: 1.125rem;" not in content:
            content = content.replace("font-family: 'Inter', sans-serif;", "font-family: 'Inter', sans-serif;\n            font-size: 1.125rem; /* Increased for better readability */")
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Successfully updated all HTML files with bigger text and better contrast.")

if __name__ == '__main__':
    update_html_files()
