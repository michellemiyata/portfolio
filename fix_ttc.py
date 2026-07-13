import os

filepath = 'case_study_2.html'
with open(filepath, 'r') as f:
    html = f.read()

import re
pattern = r'<!-- VISUAL STORY \(CAROUSEL\) -->.*?</section>'
match = re.search(pattern, html, flags=re.DOTALL)

replacement = """<!-- VISUAL STORY (CAROUSEL) -->
        <section class="max-w-6xl mx-auto mb-32 fade-in">
            <!-- Tab Navigation -->
            <div class="flex flex-wrap justify-center gap-4 mb-12">
                <button onclick="showSlide('ttc', 0, 'bg-amber-50', 'hover:bg-amber-50/50')" class="tab-btn-ttc px-6 py-2 rounded-full border dynamic-border text-amber-500 font-semibold tracking-widest text-xs uppercase transition-all bg-amber-50 cursor-pointer">01 System</button>
                <button onclick="showSlide('ttc', 1, 'bg-amber-50', 'hover:bg-amber-50/50')" class="tab-btn-ttc px-6 py-2 rounded-full border dynamic-border text-amber-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-amber-50/50 cursor-pointer">02 Process</button>
                <button onclick="showSlide('ttc', 2, 'bg-amber-50', 'hover:bg-amber-50/50')" class="tab-btn-ttc px-6 py-2 rounded-full border dynamic-border text-amber-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-amber-50/50 cursor-pointer">03 Iteration</button>
                <button onclick="showSlide('ttc', 3, 'bg-amber-50', 'hover:bg-amber-50/50')" class="tab-btn-ttc px-6 py-2 rounded-full border dynamic-border text-amber-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-amber-50/50 cursor-pointer">Output</button>
            </div>

            <!-- Slides Container -->
            <div class="relative w-full">
                <!-- Slide 1 -->
                <div id="slide-ttc-0" class="slide-ttc grid md:grid-cols-2 gap-12 items-center opacity-100 transition-opacity duration-500">
                    <div class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="Screenshot 2025-11-21 113358.png" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" />
                    </div>
                    <div class="order-1 md:order-2">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">01 System</span>
                        <h3 class="text-3xl font-medium mb-4">Emotional Colour Framework</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            I established a colour code to represent feeling states:
                        </p>
                        <ul class="space-y-2">
                            <li><strong>Yellow</strong> — Relief / Lightness</li>
                            <li><strong>Blue</strong> — Heaviness / Sadness</li>
                            <li><strong>Red</strong> — Anger / Overwhelm</li>
                            <li><strong>Purple</strong> — Surprise / Awakening</li>
                        </ul>
                    </div>
                </div>

                <!-- Slide 2 -->
                <div id="slide-ttc-1" class="slide-ttc hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-1">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">02 Process</span>
                        <h3 class="text-3xl font-medium mb-4">Mapping the Pacing</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Exploration included emotional research and mapping emotional pacing across stations using Miro. I tracked the fluctuating intensity of the commute, from the quiet anticipation at Finch to the overwhelm at Eglinton.
                        </p>
                    </div>
                    <div class="order-2 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="Screenshot 2025-11-20 104324.png" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" />
                    </div>
                </div>

                <!-- Slide 3 -->
                <div id="slide-ttc-2" class="slide-ttc hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="Screenshot 2025-11-21 113322.png" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" />
                    </div>
                    <div class="order-1 md:order-2">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">03 Iteration</span>
                        <h3 class="text-3xl font-medium mb-4">Developing the Stations</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Refining the geometry of the route. <strong>Finch → Sheppard</strong> felt like quiet nerves. <strong>Eglinton → Bloor</strong> was pure noise. <strong>Bloor → Union</strong> offered a soft return to self.
                        </p>
                    </div>
                </div>

                <!-- Slide 4 -->
                <div id="slide-ttc-3" class="slide-ttc hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-1">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">Output</span>
                        <h3 class="text-3xl font-medium mb-4">The Result</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            A soft, colour-based emotional map visualizing a daily TTC journey. It transforms a mundane routine into a visual artifact of human experience.
                        </p>
                    </div>
                    <div class="order-2 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="Screenshot 2025-10-08 143959.png" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" />
                    </div>
                </div>
            </div>
        </section>"""

if match:
    new_html = html[:match.start()] + replacement + html[match.end():]
    with open(filepath, 'w') as f:
        f.write(new_html)
    print("Fixed ttc")
else:
    print("Could not find section in ttc")
