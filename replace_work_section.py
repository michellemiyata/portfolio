import sys

with open("/Users/michellemiyata/Downloads/portfolio-main/index.html", "r") as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "<!-- Selected Work List -->" in line:
        start_idx = i
    if "<!-- Soft Call to Action -->" in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    new_html = """        <!-- Selected Work List -->
        <section class="mb-32 fade-up" aria-labelledby="work-heading">
            <div class="flex justify-between items-end mb-16 border-b dynamic-border pb-6">
                <h2 id="work-heading" class="text-3xl font-medium text-[var(--text-primary)]">Selected Work</h2>
                <a href="work.html" class="hidden md:flex items-center text-lg text-[var(--text-secondary)] hover:text-[var(--text-primary)] transition group">
                    View All Projects <i data-lucide="arrow-right" class="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform"></i>
                </a>
            </div>

            <!-- Single Main Slider -->
            <div class="relative group/slider w-full">
                <div class="flex overflow-x-auto snap-x snap-mandatory flex-nowrap slider-container gap-6 pb-8 -mx-4 px-4 md:mx-0 md:px-0" style="scrollbar-width: none; -ms-overflow-style: none;">
                    
                    <!-- StudyBuddy -->
                    <article class="min-w-[85%] md:min-w-[70%] snap-center shrink-0 block project-card">
                        <a href="case_study_studybuddy.html" class="block focus:outline-none h-full bg-[var(--bg-secondary)] rounded-2xl p-6 md:p-8 hover:-translate-y-2 transition-transform duration-300">
                            <div class="aspect-[16/9] md:aspect-[21/9] rounded-xl overflow-hidden relative mb-8 border dynamic-border bg-[var(--bg-primary)]">
                                <img src="studybuddy_app/Homepage.svg" alt="StudyBuddy App Interface" class="w-full h-full object-contain project-image p-8" />
                            </div>
                            <div>
                                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                                    <h3 class="text-3xl font-medium text-[var(--text-primary)]">StudyBuddy</h3>
                                    <div class="flex gap-4">
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">UX/UI</span>
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">Accessibility</span>
                                    </div>
                                </div>
                                <p class="text-[var(--text-secondary)] text-lg md:text-xl font-light leading-relaxed">
                                    Inclusive productivity tool designed for neurodiversity and sensory-friendly focus.
                                </p>
                            </div>
                        </a>
                    </article>

                    <!-- Kizuna Dining -->
                    <article class="min-w-[85%] md:min-w-[70%] snap-center shrink-0 block project-card">
                        <a href="case_study_kizuna.html" class="block focus:outline-none h-full bg-[var(--bg-secondary)] rounded-2xl p-6 md:p-8 hover:-translate-y-2 transition-transform duration-300">
                            <div class="aspect-[16/9] md:aspect-[21/9] rounded-xl overflow-hidden relative mb-8 border dynamic-border bg-[var(--bg-primary)]">
                                <img src="restaurant_kizuna_app/images/Welcome%20Back.png" alt="Kizuna Dining Interface" class="w-full h-full object-cover project-image" />
                            </div>
                            <div>
                                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                                    <h3 class="text-3xl font-medium text-[var(--text-primary)]">Kizuna Dining</h3>
                                    <div class="flex gap-4">
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">UX/UI</span>
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">App Design</span>
                                    </div>
                                </div>
                                <p class="text-[var(--text-secondary)] text-lg md:text-xl font-light leading-relaxed">
                                    A seamless dining companion app enhancing the customer experience through digital ordering.
                                </p>
                            </div>
                        </a>
                    </article>

                    <!-- UnionMoods -->
                    <article class="min-w-[85%] md:min-w-[70%] snap-center shrink-0 block project-card">
                        <a href="case_study_unionmoods.html" class="block focus:outline-none h-full bg-[var(--bg-secondary)] rounded-2xl p-6 md:p-8 hover:-translate-y-2 transition-transform duration-300">
                            <div class="aspect-[16/9] md:aspect-[21/9] rounded-xl overflow-hidden relative mb-8 border dynamic-border bg-[var(--bg-primary)]">
                                <img src="unionmoods_AR/unionmoods_highfidelity_screenshot.png" alt="UnionMoods AR App" class="w-full h-full object-cover project-image" />
                            </div>
                            <div>
                                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                                    <h3 class="text-3xl font-medium text-[var(--text-primary)]">UnionMoods AR</h3>
                                    <div class="flex gap-4">
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">AR Design</span>
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">UX Research</span>
                                    </div>
                                </div>
                                <p class="text-[var(--text-secondary)] text-lg md:text-xl font-light leading-relaxed">
                                    Augmented reality experience mapping emotional connection in public transit.
                                </p>
                            </div>
                        </a>
                    </article>

                </div>

                <!-- Navigation Controls -->
                <button class="hidden md:flex absolute left-[-2rem] top-1/2 -translate-y-1/2 p-3 rounded-full bg-[var(--bg-primary)] border dynamic-border text-[var(--text-primary)] opacity-0 group-hover/slider:opacity-100 focus:opacity-100 transition-all slider-prev z-10 hover:scale-105 shadow-sm items-center justify-center cursor-pointer" aria-label="Previous project">
                    <i data-lucide="chevron-left" class="w-6 h-6"></i>
                </button>
                <button class="hidden md:flex absolute right-[-2rem] top-1/2 -translate-y-1/2 p-3 rounded-full bg-[var(--bg-primary)] border dynamic-border text-[var(--text-primary)] opacity-0 group-hover/slider:opacity-100 focus:opacity-100 transition-all slider-next z-10 hover:scale-105 shadow-sm items-center justify-center cursor-pointer" aria-label="Next project">
                    <i data-lucide="chevron-right" class="w-6 h-6"></i>
                </button>
            </div>

            <!-- More button for mobile -->
            <div class="mt-8 pt-8 text-center md:hidden fade-up">
                <a href="work.html" class="inline-flex items-center px-8 py-4 border dynamic-border rounded-full text-[var(--text-primary)] hover:bg-[var(--bg-secondary)] transition">
                    View All Projects <i data-lucide="arrow-right" class="ml-2 w-4 h-4"></i>
                </a>
            </div>
        </section>
"""
    lines[start_idx:end_idx] = [new_html]
    with open("/Users/michellemiyata/Downloads/portfolio-main/index.html", "w") as f:
        f.writelines(lines)
    print("SUCCESS")
else:
    print(f"COULD NOT FIND START OR END MARKERS st:{start_idx} end:{end_idx}")

