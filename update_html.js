const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');

const startTag = '        <!-- Selected Work List -->';
const endTag = '        <!-- Soft Call to Action -->';

const startIdx = content.indexOf(startTag);
const endIdx = content.indexOf(endTag);

if (startIdx !== -1 && endIdx !== -1) {
    const newHtml = `        <!-- Selected Work List -->
        <section class="mb-32 fade-up" aria-labelledby="work-heading">
            <div class="flex flex-col md:flex-row md:justify-between items-start md:items-end mb-12 border-b dynamic-border pb-6">
                <h2 id="work-heading" class="text-3xl font-medium text-[var(--text-primary)]">Selected Work</h2>
                <a href="work.html" class="hidden md:flex items-center text-lg text-[var(--text-secondary)] hover:text-[var(--text-primary)] transition group">
                    View All Projects <i data-lucide="arrow-right" class="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform"></i>
                </a>
            </div>

            <!-- Single Main Slider -->
            <div class="relative group/slider w-full">
                <div class="flex overflow-x-auto snap-x snap-mandatory flex-nowrap slider-container gap-6 pb-8 mx-[-1rem] px-[1rem] md:mx-0 md:px-0" style="scrollbar-width: none; -ms-overflow-style: none;">
                    
                    <!-- StudyBuddy -->
                    <article class="min-w-[90%] md:min-w-[70%] lg:min-w-[60%] snap-center shrink-0 block project-card">
                        <a href="case_study_studybuddy.html" class="block focus:outline-none h-full bg-[var(--bg-secondary)] rounded-2xl overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-300">
                            <div class="aspect-[16/9] md:aspect-[21/9] relative bg-[var(--bg-primary)] border-b dynamic-border">
                                <img src="studybuddy_app/Homepage.svg" alt="StudyBuddy App Interface" class="w-full h-full object-contain p-8" />
                            </div>
                            <div class="p-8">
                                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                                    <h3 class="text-3xl font-medium text-[var(--text-primary)]">StudyBuddy</h3>
                                    <div class="flex gap-4">
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">UX/UI</span>
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">Accessibility</span>
                                    </div>
                                </div>
                                <p class="text-[var(--text-secondary)] text-lg font-light leading-relaxed">
                                    Inclusive productivity tool designed for neurodiversity and sensory-friendly focus.
                                </p>
                            </div>
                        </a>
                    </article>

                    <!-- Kizuna Dining -->
                    <article class="min-w-[90%] md:min-w-[70%] lg:min-w-[60%] snap-center shrink-0 block project-card">
                        <a href="case_study_kizuna.html" class="block focus:outline-none h-full bg-[var(--bg-secondary)] rounded-2xl overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-300">
                            <div class="aspect-[16/9] md:aspect-[21/9] relative bg-[var(--bg-primary)] border-b dynamic-border">
                                <img src="restaurant_kizuna_app/images/Welcome%20Back.png" alt="Kizuna Dining Interface" class="w-full h-full object-cover" />
                            </div>
                            <div class="p-8">
                                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                                    <h3 class="text-3xl font-medium text-[var(--text-primary)]">Kizuna Dining</h3>
                                    <div class="flex gap-4">
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">UX/UI</span>
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">App Design</span>
                                    </div>
                                </div>
                                <p class="text-[var(--text-secondary)] text-lg font-light leading-relaxed">
                                    A seamless dining companion app enhancing the customer experience through digital ordering.
                                </p>
                            </div>
                        </a>
                    </article>

                    <!-- UnionMoods -->
                    <article class="min-w-[90%] md:min-w-[70%] lg:min-w-[60%] snap-center shrink-0 block project-card">
                        <a href="case_study_unionmoods.html" class="block focus:outline-none h-full bg-[var(--bg-secondary)] rounded-2xl overflow-hidden dynamic-border border hover:-translate-y-2 transition-transform duration-300">
                            <div class="aspect-[16/9] md:aspect-[21/9] relative bg-[var(--bg-primary)] border-b dynamic-border">
                                <img src="unionmoods_AR/unionmoods_highfidelity_screenshot.png" alt="UnionMoods AR App" class="w-full h-full object-cover" />
                            </div>
                            <div class="p-8">
                                <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4">
                                    <h3 class="text-3xl font-medium text-[var(--text-primary)]">UnionMoods AR</h3>
                                    <div class="flex gap-4">
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">AR Design</span>
                                        <span class="text-xs font-medium tracking-wide text-[var(--text-secondary)] border dynamic-border px-3 py-1 rounded-full uppercase">UX Research</span>
                                    </div>
                                </div>
                                <p class="text-[var(--text-secondary)] text-lg font-light leading-relaxed">
                                    Augmented reality experience mapping emotional connection in public transit.
                                </p>
                            </div>
                        </a>
                    </article>

                </div>

                <!-- Navigation Controls -->
                <button class="hidden md:flex absolute left-[-2rem] top-[40%] -translate-y-1/2 p-3 rounded-full bg-[var(--bg-primary)] border dynamic-border text-[var(--text-primary)] opacity-0 group-hover/slider:opacity-100 focus:opacity-100 transition-all slider-prev z-10 hover:scale-105 shadow-sm items-center justify-center cursor-pointer" aria-label="Previous project">
                    <i data-lucide="chevron-left" class="w-6 h-6"></i>
                </button>
                <button class="hidden md:flex absolute right-[-2rem] top-[40%] -translate-y-1/2 p-3 rounded-full bg-[var(--bg-primary)] border dynamic-border text-[var(--text-primary)] opacity-0 group-hover/slider:opacity-100 focus:opacity-100 transition-all slider-next z-10 hover:scale-105 shadow-sm items-center justify-center cursor-pointer" aria-label="Next project">
                    <i data-lucide="chevron-right" class="w-6 h-6"></i>
                </button>
            </div>

            <!-- More button for mobile -->
            <div class="mt-8 pt-4 text-center md:hidden fade-up">
                <a href="work.html" class="inline-flex items-center px-8 py-4 border dynamic-border rounded-full text-[var(--text-primary)] hover:bg-[var(--bg-secondary)] transition focus:outline-none">
                    View All Projects <i data-lucide="arrow-right" class="ml-2 w-4 h-4"></i>
                </a>
            </div>
        </section>

`;
    const updatedContent = content.substring(0, startIdx) + newHtml + content.substring(endIdx);
    fs.writeFileSync('index.html', updatedContent);
    console.log('SUCCESS');
} else {
    console.error('Tags not found.');
}
