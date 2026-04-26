import os
import glob

def update_nav_size():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Target the nav link container
        content = content.replace('text-sm md:text-base mt-2 md:mt-0', 'text-base md:text-lg font-medium mt-2 md:mt-0')
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Successfully updated the nav bar size in all HTML files.")

if __name__ == '__main__':
    update_nav_size()
