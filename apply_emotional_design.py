import os
import glob
import re

new_style_block = """    <style>
        :root {
            /* Warm, Nostalgic Light Mode */
            --bg-primary: #FDFBF7;
            --bg-secondary: rgba(255, 255, 255, 0.6);
            --text-primary: #2D2422;
            --text-secondary: #6B5B58;
            --accent: #B28F81;
            --focus-ring: rgba(178, 143, 129, 0.4);
            --border-subtle: rgba(231, 225, 221, 0.7);
            
            /* Gradient Backgrounds */
            --gradient-1: #FFE9E3;
            --gradient-2: #F0F0EE;
            --gradient-3: #FDFBF7;
        }

        .dark-theme {
            /* Deep, Immersive Dark Mode */
            --bg-primary: #111016;
            --bg-secondary: rgba(26, 24, 33, 0.6);
            --text-primary: #F3F1F8;
            --text-secondary: #A9A4BA;
            --accent: #9A86A8;
            --focus-ring: rgba(154, 134, 168, 0.6);
            --border-subtle: rgba(54, 50, 68, 0.7);

            /* Gradient Backgrounds */
            --gradient-1: #1C152B;
            --gradient-2: #111016;
            --gradient-3: #221D32;
        }

        .logo-blend {
            mix-blend-mode: multiply;
        }

        .dark-theme .logo-blend {
            filter: invert(1) hue-rotate(180deg) brightness(1.2);
            mix-blend-mode: screen;
        }

        @keyframes gradient-breath {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(-45deg, var(--gradient-1), var(--gradient-2), var(--gradient-3));
            background-size: 400% 400%;
            animation: gradient-breath 20s ease infinite;
            color: var(--text-primary);
            transition: color 0.4s ease;
            -webkit-font-smoothing: antialiased;
        }

        h1, h2, h3, h4 {
            font-family: 'Inter', sans-serif;
            color: var(--text-primary);
        }

        .serif {
            font-family: 'Playfair Display', serif;
        }

        p {
            color: var(--text-secondary);
            line-height: 1.8;
        }

        @media (prefers-reduced-motion: reduce) {
            *, ::before, ::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
                scroll-behavior: auto !important;
            }
        }

        .no-animations * {
            animation: none !important;
            transition: none !important;
        }
        
        .no-animations body {
            background: var(--bg-primary) !important;
        }

        *:focus-visible {
            outline: 2px solid var(--accent);
            outline-offset: 4px;
            box-shadow: 0 0 0 6px var(--focus-ring);
        }

        .fade-up {
            opacity: 0;
            transform: translateY(12px);
            transition: opacity 0.8s ease-out, transform 0.8s ease-out;
        }

        .fade-up.visible {
            opacity: 1;
            transform: none;
        }
        
        .fade-in {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease-out, transform 0.6s ease-out;
        }

        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }

        .link-underline {
            position: relative;
            text-decoration: none;
            color: var(--text-secondary);
            font-weight: 400;
            transition: color 0.3s ease;
        }

        .link-underline:hover,
        .link-underline.active {
            color: var(--text-primary);
            font-weight: 500;
        }

        .link-underline::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 1px;
            bottom: -2px;
            left: 0;
            background-color: var(--accent);
            transform: scaleX(0);
            transform-origin: bottom right;
            transition: transform 0.3s ease-out;
        }

        .link-underline:hover::after,
        .link-underline.active::after {
            transform: scaleX(1);
            transform-origin: bottom left;
        }

        .dynamic-bg {
            background-color: var(--bg-secondary);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }

        .dynamic-border {
            border-color: var(--border-subtle);
        }

        .project-card:hover .project-image {
            transform: scale(1.02);
        }

        @keyframes subtle-breathe {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .animate-breathe {
            animation: subtle-breathe 6s ease-in-out infinite;
        }
    </style>"""

os.chdir("/Users/michellemiyata/Downloads/portfolio-main")

for filepath in glob.glob("*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We only want to replace the first <style>...</style> block which is in the <head>
    # We use re.sub with count=1
    pattern = r"<style>.*?</style>"
    new_content = re.sub(pattern, new_style_block, content, count=1, flags=re.DOTALL)
    
    # Optional: If a file has another <style> block for `.fade-in` later on (e.g. at the bottom),
    # let's remove it entirely because we added `.fade-in` to the universal style block.
    # The bottom <style> block for fade-in looks exactly like:
    # <style>
    #     .fade-in { ... }
    #     .fade-in.visible { ... }
    # </style>
    # We'll just remove any subsequent <style> blocks if they contain '.fade-in'
    
    extra_style_pattern = r"<style>\s*\.fade-in\s*\{.*?</style>"
    new_content = re.sub(extra_style_pattern, "", new_content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No match found in {filepath}")
