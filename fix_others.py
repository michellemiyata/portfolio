import re

def fix_file(filepath, project_id, active_bg, hover_bg, text_col):
    with open(filepath, 'r') as f:
        html = f.read()

    # I'll just write a script to restore them from their current broken state if they are broken.
    # Actually, let's check if they are broken.
    pattern = r'<!-- VISUAL STORY \(CAROUSEL\) -->.*?</section>'
    match = re.search(pattern, html, flags=re.DOTALL)
    if match:
        print(f"{filepath} has the carousel section.")
    else:
        print(f"{filepath} does NOT have the carousel section.")
        
fix_file('case_study_2.html', 'ttc', 'bg-amber-50', 'hover:bg-amber-50/50', 'text-amber-500')
fix_file('case_study_ar_puzzle.html', 'arpuzzle', 'bg-blue-50', 'hover:bg-blue-50/50', 'text-blue-500')
