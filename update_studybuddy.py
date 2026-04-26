import os

filepath = 'case_study_studybuddy.html'
with open(filepath, 'r') as f:
    html = f.read()

target = """        <!-- VISUALS / FEATURES (ZIG ZAG) -->
        <section class="max-w-6xl mx-auto mb-32 space-y-32">

            <!-- Feature 1 -->
            <div class="grid md:grid-cols-2 gap-12 items-center fade-in">
                <div
                    class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border  aspect-[4/3] group">
                    <img src="studybuddy_app/Homepage.svg"
                        class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-700" />
                </div>
                <div class="order-1 md:order-2">
                    <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">01
                        Overview</span>
                    <h3 class="text-3xl font-medium  mb-4">Unified Dashboard</h3>
                    <p class=" text-lg leading-relaxed mb-6">
                        The central hub tracks study sessions and vocabulary stats at a glance. The interface uses soft
                        shadows and translucency (Glassmorphism) to keep the most important task—studying—in clear focus
                        while maintaining a premium feel.
                    </p>
                </div>
            </div>

            <!-- Feature 2 -->
            <div class="grid md:grid-cols-2 gap-12 items-center fade-in">
                <div class="order-1">
                    <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">02
                        Focus</span>
                    <h3 class="text-3xl font-medium  mb-4">Sensory-Friendly Focus Mode</h3>
                    <p class=" text-lg leading-relaxed mb-6">
                        A distraction-free environment designed for ADHD brains. Users can toggle "Brown Noise" or
                        ambient soundscapes (Rain, Cafe) to mask background noise. The timer is large and distinct,
                        reducing time blindness.
                    </p>
                </div>
                <div
                    class="order-2 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border  aspect-[4/3] group">
                    <img src="studybuddy_app/Focus%20Mode.svg"
                        class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-700" />
                </div>
            </div>

            <!-- Feature 3 -->
            <div class="grid md:grid-cols-2 gap-12 items-center fade-in">
                <div
                    class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border  aspect-[4/3] group">
                    <img src="studybuddy_app/Smart%20Dictionary.svg"
                        class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-700" />
                </div>
                <div class="order-1 md:order-2">
                    <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">03
                        Learning</span>
                    <h3 class="text-3xl font-medium  mb-4">Smart Dictionary</h3>
                    <p class=" text-lg leading-relaxed mb-6">
                        Supporting auditory learners and those with dyslexia, definitions are presented with generous
                        line-height and integrated Text-to-Speech (TTS). This multi-modal approach reinforces vocabulary
                        acquisition without visual stress.
                    </p>
                </div>
            </div>

        </section>"""

replacement = """        <!-- VISUAL STORY (CAROUSEL) -->
        <section class="max-w-6xl mx-auto mb-32 fade-in">
            <!-- Tab Navigation -->
            <div class="flex flex-wrap justify-center gap-4 mb-12">
                <button onclick="showSlide('studybuddy', 0, 'bg-indigo-50', 'hover:bg-indigo-50/50')" class="tab-btn-studybuddy px-6 py-2 rounded-full border dynamic-border text-indigo-500 font-semibold tracking-widest text-xs uppercase transition-all bg-indigo-50 cursor-pointer">01 Overview</button>
                <button onclick="showSlide('studybuddy', 1, 'bg-indigo-50', 'hover:bg-indigo-50/50')" class="tab-btn-studybuddy px-6 py-2 rounded-full border dynamic-border text-indigo-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-indigo-50/50 cursor-pointer">02 Focus</button>
                <button onclick="showSlide('studybuddy', 2, 'bg-indigo-50', 'hover:bg-indigo-50/50')" class="tab-btn-studybuddy px-6 py-2 rounded-full border dynamic-border text-indigo-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-indigo-50/50 cursor-pointer">03 Learning</button>
            </div>

            <!-- Slides Container -->
            <div class="relative w-full">
                <!-- Phase 1 -->
                <div id="slide-studybuddy-0" class="slide-studybuddy grid md:grid-cols-2 gap-12 items-center opacity-100 transition-opacity duration-500">
                    <div class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="studybuddy_app/Homepage.svg" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-700" />
                    </div>
                    <div class="order-1 md:order-2">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">01 Overview</span>
                        <h3 class="text-3xl font-medium mb-4">Unified Dashboard</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            The central hub tracks study sessions and vocabulary stats at a glance. The interface uses soft shadows and translucency (Glassmorphism) to keep the most important task—studying—in clear focus while maintaining a premium feel.
                        </p>
                    </div>
                </div>

                <!-- Phase 2 -->
                <div id="slide-studybuddy-1" class="slide-studybuddy hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-1">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">02 Focus</span>
                        <h3 class="text-3xl font-medium mb-4">Sensory-Friendly Focus Mode</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            A distraction-free environment designed for ADHD brains. Users can toggle "Brown Noise" or ambient soundscapes (Rain, Cafe) to mask background noise. The timer is large and distinct, reducing time blindness.
                        </p>
                    </div>
                    <div class="order-2 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="studybuddy_app/Focus%20Mode.svg" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-700" />
                    </div>
                </div>

                <!-- Phase 3 -->
                <div id="slide-studybuddy-2" class="slide-studybuddy hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="studybuddy_app/Smart%20Dictionary.svg" class="w-full h-full object-cover object-top group-hover:scale-105 transition duration-700" />
                    </div>
                    <div class="order-1 md:order-2">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">03 Learning</span>
                        <h3 class="text-3xl font-medium mb-4">Smart Dictionary</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Supporting auditory learners and those with dyslexia, definitions are presented with generous line-height and integrated Text-to-Speech (TTS). This multi-modal approach reinforces vocabulary acquisition without visual stress.
                        </p>
                    </div>
                </div>
            </div>
        </section>"""

if target in html:
    html = html.replace(target, replacement)
else:
    print("Could not find target block in studybuddy")

if 'window.showSlide = function' not in html:
    script_inject = """
        // Carousel Logic
        window.showSlide = function(carouselId, index, activeClass = 'bg-indigo-50', hoverClass = 'hover:bg-indigo-50/50') {
            const slides = document.querySelectorAll('.slide-' + carouselId);
            const btns = document.querySelectorAll('.tab-btn-' + carouselId);

            slides.forEach((slide, i) => {
                if (i === index) {
                    slide.classList.remove('hidden');
                    // Force reflow
                    void slide.offsetWidth;
                    slide.classList.remove('opacity-0');
                    slide.classList.add('opacity-100');
                } else {
                    slide.classList.add('hidden');
                    slide.classList.remove('opacity-100');
                    slide.classList.add('opacity-0');
                }
            });

            btns.forEach((btn, i) => {
                if (i === index) {
                    btn.classList.add(...activeClass.split(' '));
                    btn.classList.remove(...hoverClass.split(' '));
                } else {
                    btn.classList.remove(...activeClass.split(' '));
                    btn.classList.add(...hoverClass.split(' '));
                }
            });
        };
    </script>
"""
    html = html.replace('</script>\n\n    \n\n    <!-- LIGHTBOX MODAL -->', script_inject + '\n    \n\n    <!-- LIGHTBOX MODAL -->')

with open(filepath, 'w') as f:
    f.write(html)
print("Updated studybuddy")

