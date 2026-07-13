import os

filepath = 'case_study_kizuna.html'
with open(filepath, 'r') as f:
    html = f.read()

import re
pattern = r'<!-- VISUAL STORY \(CAROUSEL\) -->.*?</section>'
match = re.search(pattern, html, flags=re.DOTALL)

replacement = """<!-- VISUAL STORY (CAROUSEL) -->
        <section class="max-w-6xl mx-auto mb-32 fade-in">
            <!-- Tab Navigation -->
            <div class="flex flex-wrap justify-center gap-4 mb-12">
                <button onclick="showSlide('kizuna', 0, 'bg-red-50', 'hover:bg-red-50/50')" class="tab-btn-kizuna px-6 py-2 rounded-full border dynamic-border text-red-500 font-semibold tracking-widest text-xs uppercase transition-all bg-red-50 cursor-pointer">Phase 01</button>
                <button onclick="showSlide('kizuna', 1, 'bg-red-50', 'hover:bg-red-50/50')" class="tab-btn-kizuna px-6 py-2 rounded-full border dynamic-border text-red-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-red-50/50 cursor-pointer">Phase 02</button>
                <button onclick="showSlide('kizuna', 2, 'bg-red-50', 'hover:bg-red-50/50')" class="tab-btn-kizuna px-6 py-2 rounded-full border dynamic-border text-red-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-red-50/50 cursor-pointer">Phase 03</button>
                <button onclick="showSlide('kizuna', 3, 'bg-red-50', 'hover:bg-red-50/50')" class="tab-btn-kizuna px-6 py-2 rounded-full border dynamic-border text-red-500 font-semibold tracking-widest text-xs uppercase transition-all hover:bg-red-50/50 cursor-pointer">Phase 04</button>
            </div>

            <!-- Slides Container -->
            <div class="relative w-full">
                <!-- Slide 1 -->
                <div id="slide-kizuna-0" class="slide-kizuna grid md:grid-cols-2 gap-12 items-center opacity-100 transition-opacity duration-500">
                    <div class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group flex items-center justify-center p-6">
                        <div class="flex gap-4 h-full w-full justify-center items-center group-hover:scale-105 transition duration-700">
                            <img src="restaurant_kizuna_app/images/Menu.png" class="h-full w-auto object-contain shadow-sm rounded-lg" />
                            <img src="restaurant_kizuna_app/images/Japanese Menu.png" class="h-full w-auto object-contain shadow-sm rounded-lg" />
                        </div>
                    </div>
                    <div class="order-1 md:order-2">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">Phase 01</span>
                        <h3 class="text-3xl font-medium mb-4">Menu Design</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            The menu features dedicated English and Japanese versions to accommodate a diverse range of guests. This bilingual approach ensures clarity and inclusivity, while the interface remains intuitive and visually engaging with clean typography and appetite-stimulating imagery.
                        </p>
                    </div>
                </div>

                <!-- Slide 2 -->
                <div id="slide-kizuna-1" class="slide-kizuna hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-1">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">Phase 02</span>
                        <h3 class="text-3xl font-medium mb-4">Menu Browsing</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Focusing on appetising visuals and clear categorization to help users easily browse and select their favorite dishes. The interface is designed to be clean and distraction-free.
                        </p>
                    </div>
                    <div class="order-2 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group flex items-center justify-center p-6">
                        <img src="restaurant_kizuna_app/images/Menu 3.png" class="h-full w-auto object-contain shadow-sm rounded-lg group-hover:scale-105 transition duration-700" />
                    </div>
                </div>

                <!-- Slide 3 -->
                <div id="slide-kizuna-2" class="slide-kizuna hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-2 md:order-1 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group flex items-center justify-center p-6">
                        <img src="restaurant_kizuna_app/images/Checkout.png" class="h-full w-auto object-contain shadow-sm rounded-lg group-hover:scale-105 transition duration-700" />
                    </div>
                    <div class="order-1 md:order-2">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">Phase 03</span>
                        <h3 class="text-3xl font-medium mb-4">Checkout Flow</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Streamlining the checkout process to minimize friction. Clear summary views and easy payment options ensure a smooth transition from selection to purchase.
                        </p>
                    </div>
                </div>

                <!-- Slide 4 -->
                <div id="slide-kizuna-3" class="slide-kizuna hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center">
                    <div class="order-1">
                        <span class="text-indigo-500 font-semibold tracking-widest text-xs uppercase mb-2 block">Phase 04</span>
                        <h3 class="text-3xl font-medium mb-4">Visual Identity</h3>
                        <p class="text-lg leading-relaxed mb-6">
                            Incorporating authentic Japanese aesthetic elements with a modern UI approach. The color palette and imagery are carefully chosen to evoke a sense of warmth and reliability.
                        </p>
                    </div>
                    <div class="order-2 relative rounded-2xl overflow-hidden shadow-2xl border dynamic-border aspect-[4/3] group">
                        <img src="restaurant_kizuna_app/images/Brand%20Colours.png" class="w-full h-full object-cover group-hover:scale-105 transition duration-700" />
                    </div>
                </div>
            </div>
        </section>"""

if match:
    new_html = html[:match.start()] + replacement + html[match.end():]
    with open(filepath, 'w') as f:
        f.write(new_html)
    print("Fixed kizuna")
else:
    print("Could not find section in kizuna")
