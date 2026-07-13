import os

filepath = 'case_study_ar_puzzle.html'
with open(filepath, 'r') as f:
    html = f.read()

import re
pattern = r'<!-- VISUAL STORY \(CAROUSEL\) -->.*?</section>'
match = re.search(pattern, html, flags=re.DOTALL)

replacement = """<!-- VISUAL STORY (CAROUSEL) -->
        <section class="max-w-6xl mx-auto mb-32 fade-in">
            <!-- Tab Navigation -->
            <div class="flex flex-wrap justify-center gap-4 mb-12">
                <button onclick="showSlide('arpuzzle', 0, 'bg-blue-50', 'hover:bg-blue-50/50')" class="tab-btn-arpuzzle px-6 py-2 rounded-full border dynamic-border text-blue-500 font-semibold tracking-widest text-xs uppercase transition-all bg-blue-50 cursor-pointer">01 Assets</button>
                <button onclick="showSlide('arpuzzle', 1, 'bg-blue-50', 'hover:bg-blue-50/50')" class="tab-btn-arpuzzle px-6 py-2 rounded-full border dynamic-border text-blue-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-blue-50/50 cursor-pointer">02 Tracking</button>
                <button onclick="showSlide('arpuzzle', 2, 'bg-blue-50', 'hover:bg-blue-50/50')" class="tab-btn-arpuzzle px-6 py-2 rounded-full border dynamic-border text-blue-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-blue-50/50 cursor-pointer">03 Logic</button>
            </div>

            <!-- Slides Container -->
            <div class="relative w-full">
                <!-- Slide 1 -->
                <div id="slide-arpuzzle-0" class="slide-arpuzzle grid md:grid-cols-2 gap-12 items-center opacity-100 transition-opacity duration-500">
                    <div class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="puzzlepieceAR/Screenshot 2025-12-06 155428.png" class="w-full h-full object-contain group-hover:scale-105 transition duration-700" />
                    </div>
                    <div class="order-1 md:order-2">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">01 Assets</span>
                        <h3 class="text-3xl font-medium mb-4">Asset Preparation</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Preparing the puzzle piece assets in Adobe Illustrator. The graphics needed to be transparent and perfectly aligned to overlay naturally on a user's face without feeling intrusive.
                        </p>
                    </div>
                </div>

                <!-- Slide 2 -->
                <div id="slide-arpuzzle-1" class="slide-arpuzzle hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-1">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">02 Tracking</span>
                        <h3 class="text-3xl font-medium mb-4">Face Tracker Setup</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Setting up the face tracker in Effect House. This involved mapping the 2D assets to 3D anchor points on the face mesh to ensure they moved realistically with the user's head turn.
                        </p>
                    </div>
                    <div class="order-2 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="puzzlepieceAR/Screenshot 2025-12-06 155434.png" class="w-full h-full object-contain group-hover:scale-105 transition duration-700" />
                    </div>
                </div>

                <!-- Slide 3 -->
                <div id="slide-arpuzzle-2" class="slide-arpuzzle hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="puzzlepieceAR/Screenshot 2025-12-06 155456.png" class="w-full h-full object-contain group-hover:scale-105 transition duration-700" />
                    </div>
                    <div class="order-1 md:order-2">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">03 Logic</span>
                        <h3 class="text-3xl font-medium mb-4">Visual Scripting</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Using the Patch Editor to create the logic. I connected the "Mouth Smile" detection node to the "Opacity" property of the image, adding a smoothing node to make the transition feel organic rather than jarring.
                        </p>
                    </div>
                </div>
            </div>
        </section>"""

if match:
    new_html = html[:match.start()] + replacement + html[match.end():]
    with open(filepath, 'w') as f:
        f.write(new_html)
    print("Fixed arpuzzle")
else:
    print("Could not find section in arpuzzle")
