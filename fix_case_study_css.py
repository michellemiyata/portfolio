import re
import glob

css_to_inject = """
    <style>
        :root {
            --bg-primary: #FAF9F6;
            --bg-secondary: #F3F1ED;
            --text-primary: #292524;
            --text-secondary: #57534E;
            --accent: #78716C;
            --focus-ring: rgba(120, 113, 108, 0.4);
            --border-subtle: #E7E5E4;
        }
        .logo-blend { mix-blend-mode: multiply; }
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
    </style>
</head>"""

files = glob.glob('/Users/michellemiyata/Downloads/portfolio-main/case_study_*.html')

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Skip if already injected
    if ".logo-blend { mix-blend-mode: multiply; }" in content:
        continue

    content = content.replace("</head>", css_to_inject)

    with open(filepath, 'w') as f:
        f.write(content)
print("Injected CSS to all case studies")
