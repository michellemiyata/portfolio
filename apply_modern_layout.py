import os
import glob
import re

os.chdir("/Users/michellemiyata/Downloads/portfolio-main")

# 1. Update work.html to use the Bento Grid
with open("work.html", "r") as f:
    work_content = f.read()

# Replace the header in work.html
new_work_header = """        <header class="mb-24 md:mb-32 fade-up pt-12 md:pt-24" style="transition-delay: 0.1s">
            <h1 class="text-[3.5rem] leading-[1.1] md:text-8xl lg:text-9xl font-light tracking-tighter mb-8 text-[var(--text-primary)]">
                Selected <span class="serif italic text-[var(--accent)]">Work</span>
            </h1>
            <p class="text-2xl md:text-3xl max-w-2xl font-light text-[var(--text-secondary)] leading-relaxed">
                A collection of projects exploring emotion, accessibility, and calm technology.
            </p>
        </header>"""

work_content = re.sub(r'<header class="mb-32 fade-up".*?</header>', new_work_header, work_content, flags=re.DOTALL)

# Copy the Bento Grid from index.html (I'll just paste the HTML I wrote for index.html here)
bento_grid = """        <section class="mb-32" aria-label="Project List">
            <!-- Asymmetrical Bento Grid -->
            <div class="grid grid-cols-1 md:grid-cols-12 gap-6 md:gap-8 w-full">
                
                <!-- Project 1: Large Feature (Spans 8 cols) -->
                <article class="md:col-span-8 flex fade-up project-card">
                    <a href="case_study_tsitp_map.html"
                        class="group block w-full focus:outline-none bg-[var(--bg-secondary)] dynamic-bg rounded-[2rem] overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-500 shadow-sm flex flex-col h-[500px] md:h-[650px] relative">
                        <div class="absolute inset-0 z-0">
                            <div class="w-full h-full project-image transition-transform duration-700 ease-out">
                                <img src="tsitp_map_full.png" alt="TSITP Map Interface" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity" />
                            </div>
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[var(--bg-primary)] via-[var(--bg-primary)]/50 to-transparent opacity-95 z-10"></div>
                        <div class="relative z-20 p-8 md:p-12 flex flex-col justify-end h-full mt-auto">
                            <div class="flex gap-3 mb-4">
                                <span class="text-[10px] md:text-xs font-semibold tracking-[0.15em] text-[var(--bg-primary)] bg-[var(--text-primary)] px-4 py-2 rounded-full uppercase">Systems Thinking</span>
                                <span class="text-[10px] md:text-xs font-semibold tracking-[0.15em] text-[var(--text-primary)] border dynamic-border dynamic-bg px-4 py-2 rounded-full uppercase">Data Viz</span>
                            </div>
                            <h3 class="text-4xl md:text-6xl font-medium tracking-tight text-[var(--text-primary)] mb-4">Interactive Transmedia Map</h3>
                            <p class="text-[var(--text-secondary)] text-xl font-light leading-relaxed max-w-xl">
                                A digital interactive map applying systems thinking to visualize the multi-platform narrative journey of "The Summer I Turned Pretty".
                            </p>
                        </div>
                    </a>
                </article>

                <!-- Project 2: Tall Sidebar (Spans 4 cols) -->
                <article class="md:col-span-4 flex fade-up project-card" style="transition-delay: 0.1s">
                    <a href="case_study_1.html"
                        class="group block w-full focus:outline-none bg-[var(--bg-secondary)] dynamic-bg rounded-[2rem] overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-500 shadow-sm flex flex-col h-[500px] md:h-[650px] relative">
                        <div class="absolute inset-0 z-0 p-8 pt-16">
                            <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-start justify-center">
                                <img src="puzzle_piece.png" alt="Puzzle Piece" class="w-[120%] max-w-none h-auto object-contain drop-shadow-xl" />
                            </div>
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[var(--bg-primary)] via-[var(--bg-primary)]/80 to-transparent opacity-95 z-10"></div>
                        <div class="relative z-20 p-8 md:p-10 flex flex-col justify-end h-full mt-auto">
                            <h3 class="text-3xl md:text-4xl font-medium tracking-tight text-[var(--text-primary)] mb-3">Puzzle Piece</h3>
                            <p class="text-[var(--text-secondary)] text-lg font-light leading-relaxed">Emotional interaction design exploring alignment and clarity.</p>
                        </div>
                    </a>
                </article>

                <!-- Project 3: Medium (Spans 6 cols) -->
                <article class="md:col-span-6 flex fade-up project-card">
                    <a href="case_study_studybuddy.html"
                        class="group block w-full focus:outline-none bg-[var(--bg-secondary)] dynamic-bg rounded-[2rem] overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-500 shadow-sm flex flex-col h-[400px] md:h-[500px] relative">
                        <div class="absolute inset-0 z-0 bg-[var(--bg-primary)]/40">
                            <div class="w-full h-full project-image transition-transform duration-700 ease-out p-12">
                                <img src="studybuddy_app/Homepage.svg" alt="StudyBuddy App Interface" class="w-full h-full object-contain drop-shadow-2xl" />
                            </div>
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[var(--bg-primary)] via-transparent to-transparent opacity-95 z-10"></div>
                        <div class="relative z-20 p-8 md:p-10 flex flex-col justify-end h-full mt-auto">
                            <h3 class="text-3xl md:text-4xl font-medium tracking-tight text-[var(--text-primary)] mb-3">StudyBuddy</h3>
                            <p class="text-[var(--text-secondary)] text-lg font-light leading-relaxed">Inclusive productivity tool designed for neurodiversity.</p>
                        </div>
                    </a>
                </article>

                <!-- Project 4: Medium (Spans 6 cols) -->
                <article class="md:col-span-6 flex fade-up project-card" style="transition-delay: 0.1s">
                    <a href="case_study_kizuna.html"
                        class="group block w-full focus:outline-none bg-[var(--bg-secondary)] dynamic-bg rounded-[2rem] overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-500 shadow-sm flex flex-col h-[400px] md:h-[500px] relative">
                        <div class="absolute inset-0 z-0 bg-[var(--bg-primary)]/40">
                            <div class="w-full h-full project-image transition-transform duration-700 ease-out p-12">
                                <img src="restaurant_kizuna_app/images/Welcome%20Back.png" alt="Kizuna Dining Interface" class="w-full h-full object-contain drop-shadow-2xl" />
                            </div>
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[var(--bg-primary)] via-transparent to-transparent opacity-95 z-10"></div>
                        <div class="relative z-20 p-8 md:p-10 flex flex-col justify-end h-full mt-auto">
                            <h3 class="text-3xl md:text-4xl font-medium tracking-tight text-[var(--text-primary)] mb-3">Kizuna Dining</h3>
                            <p class="text-[var(--text-secondary)] text-lg font-light leading-relaxed">Seamless dining companion app enhancing customer experience.</p>
                        </div>
                    </a>
                </article>

                <!-- Project 5: Wide Focus (Spans 12 cols) -->
                <article class="md:col-span-12 flex fade-up project-card">
                    <a href="case_study_unionmoods.html"
                        class="group block w-full focus:outline-none bg-[var(--bg-secondary)] dynamic-bg rounded-[2rem] overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-500 shadow-sm flex flex-col md:flex-row h-auto md:h-[500px] relative">
                        <div class="md:w-[45%] p-8 md:p-16 flex flex-col justify-center z-20 relative order-2 md:order-1">
                            <div class="flex gap-3 mb-6">
                                <span class="text-[10px] md:text-xs font-semibold tracking-[0.15em] text-[var(--bg-primary)] bg-[var(--text-primary)] px-4 py-2 rounded-full uppercase">AR Design</span>
                            </div>
                            <h3 class="text-4xl md:text-5xl font-medium tracking-tight text-[var(--text-primary)] mb-6">UnionMoods AR</h3>
                            <p class="text-[var(--text-secondary)] text-xl font-light leading-relaxed mb-8">
                                Augmented reality experience mapping emotional connection in public transit.
                            </p>
                            <span class="text-[var(--text-primary)] font-medium inline-flex items-center group-hover:gap-3 transition-all duration-300 gap-2">View Case Study <i data-lucide="arrow-right" class="w-4 h-4"></i></span>
                        </div>
                        <div class="md:w-[55%] h-[350px] md:h-full relative z-0 order-1 md:order-2 bg-[var(--bg-primary)]/30 md:border-l dynamic-border">
                            <div class="w-full h-full project-image transition-transform duration-700 ease-out p-8 md:p-16 flex items-center justify-center">
                                <img src="unionmoods_AR/unionmoods_highfidelity_screenshot.png" alt="UnionMoods AR App" class="w-full h-full object-contain drop-shadow-2xl scale-[1.15]" />
                            </div>
                        </div>
                    </a>
                </article>
                
                <!-- Remaining Projects -->
                <article class="md:col-span-6 flex fade-up project-card">
                    <a href="case_study_3.html"
                        class="group block w-full focus:outline-none bg-[var(--bg-secondary)] dynamic-bg rounded-[2rem] overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-500 shadow-sm flex flex-col h-[400px] md:h-[500px] relative">
                        <div class="absolute inset-0 z-0 bg-[var(--bg-primary)]/40">
                            <div class="w-full h-full project-image transition-transform duration-700 ease-out p-12">
                                <img src="Screenshot 2025-11-08 113155.png" alt="Discover BC" class="w-full h-full object-contain drop-shadow-2xl" />
                            </div>
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[var(--bg-primary)] via-transparent to-transparent opacity-95 z-10"></div>
                        <div class="relative z-20 p-8 md:p-10 flex flex-col justify-end h-full mt-auto">
                            <h3 class="text-3xl md:text-4xl font-medium tracking-tight text-[var(--text-primary)] mb-3">Discover BC</h3>
                            <p class="text-[var(--text-secondary)] text-lg font-light leading-relaxed">Calm, photography-led travel booking experience.</p>
                        </div>
                    </a>
                </article>

                <article class="md:col-span-6 flex fade-up project-card" style="transition-delay: 0.1s">
                    <a href="case_study_2.html"
                        class="group block w-full focus:outline-none bg-[var(--bg-secondary)] dynamic-bg rounded-[2rem] overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-500 shadow-sm flex flex-col h-[400px] md:h-[500px] relative">
                        <div class="absolute inset-0 z-0 bg-[var(--bg-primary)]/40">
                            <div class="w-full h-full project-image transition-transform duration-700 ease-out p-12">
                                <img src="Screenshot 2025-10-08 143959.png" alt="Emotional Journey TTC" class="w-full h-full object-contain drop-shadow-2xl" />
                            </div>
                        </div>
                        <div class="absolute inset-0 bg-gradient-to-t from-[var(--bg-primary)] via-transparent to-transparent opacity-95 z-10"></div>
                        <div class="relative z-20 p-8 md:p-10 flex flex-col justify-end h-full mt-auto">
                            <h3 class="text-3xl md:text-4xl font-medium tracking-tight text-[var(--text-primary)] mb-3">Emotional Journey: TTC</h3>
                            <p class="text-[var(--text-secondary)] text-lg font-light leading-relaxed">Visualizing shifting moods on the Line 1 commute.</p>
                        </div>
                    </a>
                </article>
            </div>
        </section>"""

work_content = re.sub(r'<section class="space-y-32 mb-32" aria-label="Project List">.*?</section>', bento_grid, work_content, flags=re.DOTALL)

with open("work.html", "w") as f:
    f.write(work_content)
print("Updated work.html to use Bento Grid")


# 2. Add overflow-x-hidden to body to prevent horizontal scrollbars
for filepath in glob.glob("*.html"):
    with open(filepath, "r") as f:
        html = f.read()
    if "<body" in html and "overflow-x-hidden" not in html:
        html = re.sub(r'<body([^>]*)>', r'<body\1 class="overflow-x-hidden">', html)
        with open(filepath, "w") as f:
            f.write(html)
        print(f"Added overflow-x-hidden to body in {filepath}")


# 3. Update Case Study Headers to be full bleed
for filepath in glob.glob("case_study_*.html"):
    with open(filepath, "r") as f:
        html = f.read()
    
    # We want to find the <section> containing the header text and image
    # and transform the image into a full-bleed block.
    # The existing image has class="relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border dynamic-bg aspect-video group" or similar.
    # We will replace `rounded-2xl` with `w-screen relative left-1/2 right-1/2 -ml-[50vw] -mr-[50vw] rounded-none`
    
    # This regex is a bit complex, so let's just do standard string replacements.
    if 'class="relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border' in html:
        html = html.replace('class="relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border', 
                            'class="w-screen relative left-[50%] right-[50%] -ml-[50vw] -mr-[50vw] rounded-none overflow-hidden shadow-2xl border-y dynamic-border')
        
    if 'class="max-w-5xl mx-auto mb-24 fade-in"' in html:
        html = html.replace('class="max-w-5xl mx-auto mb-24 fade-in"', 'class="mb-32 fade-in relative"')
        
    if '<div class="text-center mb-16">' in html:
        html = html.replace('<div class="text-center mb-16">', '<div class="text-center mb-16 max-w-5xl mx-auto px-6">')
    
    with open(filepath, "w") as f:
        f.write(html)
    print(f"Made case study header full bleed in {filepath}")
