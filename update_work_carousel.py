import os

def rewrite_work_html():
    file_path = 'work.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Split content
    header_end = content.find('<section class="mb-32" aria-label="Project List">')
    footer_start = content.find('</main>')
    
    head = content[:header_end]
    foot = content[footer_start:]
    
    # We need to construct the carousel HTML
    carousel_html = """        <section class="mb-32" aria-label="Project List">
            <!-- Interactive Slideshow Carousel -->
            <div class="relative w-full max-w-4xl mx-auto overflow-hidden group/carousel py-4">
                <!-- Slider Track -->
                <div class="flex transition-transform duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] w-full" id="home-carousel-track">
                    
                    <!-- Project 1: TSITP Map -->
                    <article class="w-full flex-shrink-0 px-2 sm:px-4">
                        <a href="case_study_tsitp_map.html" class="block w-full h-full focus:outline-none p-6 md:p-8 glass-card flex flex-col group">
                            <div class="w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[var(--bg-primary)] shadow-sm mb-6 relative">
                                <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-center justify-center">
                                    <img src="tsitp_map_full.png" alt="TSITP Map Interface" class="w-full h-full object-cover group-hover:opacity-90 transition-opacity" />
                                </div>
                            </div>
                            <div class="mt-auto">
                                <h3 class="text-2xl md:text-3xl font-medium text-[var(--text-primary)] mb-2 group-hover:text-[var(--accent)] transition-colors">Interactive Transmedia Map</h3>
                                <p class="text-[var(--text-secondary)] text-lg font-light">Systems Thinking • Data Viz</p>
                            </div>
                        </a>
                    </article>

                    <!-- Project 2: Puzzle Piece -->
                    <article class="w-full flex-shrink-0 px-2 sm:px-4">
                        <a href="case_study_1.html" class="block w-full h-full focus:outline-none p-6 md:p-8 glass-card flex flex-col group">
                            <div class="w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[var(--bg-primary)] shadow-sm mb-6 relative p-8">
                                <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-center justify-center">
                                    <img src="puzzle_piece.png" alt="Puzzle Piece" class="w-full h-full object-contain drop-shadow-xl scale-110 group-hover:scale-[1.15] transition-transform duration-700" />
                                </div>
                            </div>
                            <div class="mt-auto">
                                <h3 class="text-2xl md:text-3xl font-medium text-[var(--text-primary)] mb-2 group-hover:text-[var(--accent)] transition-colors">Puzzle Piece</h3>
                                <p class="text-[var(--text-secondary)] text-lg font-light">Visual Design • Concept</p>
                            </div>
                        </a>
                    </article>

                    <!-- Project 3: UnionMoods AR -->
                    <article class="w-full flex-shrink-0 px-2 sm:px-4">
                        <a href="case_study_unionmoods.html" class="block w-full h-full focus:outline-none p-6 md:p-8 glass-card flex flex-col group">
                            <div class="w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[var(--bg-primary)] shadow-sm mb-6 relative p-8">
                                <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-center justify-center">
                                    <img src="unionmoods_AR/unionmoods_highfidelity_screenshot.png" alt="UnionMoods AR App" class="w-[90%] h-[90%] object-contain drop-shadow-2xl scale-105 group-hover:scale-[1.1] transition-transform duration-700" />
                                </div>
                            </div>
                            <div class="mt-auto">
                                <h3 class="text-2xl md:text-3xl font-medium text-[var(--text-primary)] mb-2 group-hover:text-[var(--accent)] transition-colors">UnionMoods AR</h3>
                                <p class="text-[var(--text-secondary)] text-lg font-light">AR Design • UX Research</p>
                            </div>
                        </a>
                    </article>

                    <!-- Project 4: StudyBuddy -->
                    <article class="w-full flex-shrink-0 px-2 sm:px-4">
                        <a href="case_study_studybuddy.html" class="block w-full h-full focus:outline-none p-6 md:p-8 glass-card flex flex-col group">
                            <div class="w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[var(--bg-primary)] shadow-sm mb-6 relative p-12">
                                <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-center justify-center">
                                    <img src="studybuddy_app/Homepage.svg" alt="StudyBuddy App Interface" class="w-[90%] h-[90%] object-contain drop-shadow-2xl group-hover:scale-105 transition-transform duration-700" />
                                </div>
                            </div>
                            <div class="mt-auto">
                                <h3 class="text-2xl md:text-3xl font-medium text-[var(--text-primary)] mb-2 group-hover:text-[var(--accent)] transition-colors">StudyBuddy</h3>
                                <p class="text-[var(--text-secondary)] text-lg font-light">Inclusive UI • Productivity</p>
                            </div>
                        </a>
                    </article>
                    
                    <!-- Project 5: Kizuna Dining -->
                    <article class="w-full flex-shrink-0 px-2 sm:px-4">
                        <a href="case_study_kizuna.html" class="block w-full h-full focus:outline-none p-6 md:p-8 glass-card flex flex-col group">
                            <div class="w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[var(--bg-primary)] shadow-sm mb-6 relative p-12">
                                <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-center justify-center">
                                    <img src="restaurant_kizuna_app/images/Welcome%20Back.png" alt="Kizuna Dining" class="w-[80%] h-[80%] object-contain drop-shadow-2xl group-hover:scale-105 transition-transform duration-700" />
                                </div>
                            </div>
                            <div class="mt-auto">
                                <h3 class="text-2xl md:text-3xl font-medium text-[var(--text-primary)] mb-2 group-hover:text-[var(--accent)] transition-colors">Kizuna Dining</h3>
                                <p class="text-[var(--text-secondary)] text-lg font-light">UX/UI • App Design</p>
                            </div>
                        </a>
                    </article>
                    
                    <!-- Project 6: Discover BC -->
                    <article class="w-full flex-shrink-0 px-2 sm:px-4">
                        <a href="case_study_3.html" class="block w-full h-full focus:outline-none p-6 md:p-8 glass-card flex flex-col group">
                            <div class="w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[var(--bg-primary)] shadow-sm mb-6 relative p-12">
                                <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-center justify-center">
                                    <img src="Screenshot 2025-11-08 113155.png" alt="Discover BC" class="w-[90%] h-[90%] object-contain drop-shadow-2xl group-hover:scale-105 transition-transform duration-700" />
                                </div>
                            </div>
                            <div class="mt-auto">
                                <h3 class="text-2xl md:text-3xl font-medium text-[var(--text-primary)] mb-2 group-hover:text-[var(--accent)] transition-colors">Discover BC</h3>
                                <p class="text-[var(--text-secondary)] text-lg font-light">UI Design • Mobile</p>
                            </div>
                        </a>
                    </article>
                    
                    <!-- Project 7: Emotional Journey TTC -->
                    <article class="w-full flex-shrink-0 px-2 sm:px-4">
                        <a href="case_study_2.html" class="block w-full h-full focus:outline-none p-6 md:p-8 glass-card flex flex-col group">
                            <div class="w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[var(--bg-primary)] shadow-sm mb-6 relative p-12">
                                <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-center justify-center">
                                    <img src="Screenshot 2025-10-08 143959.png" alt="Emotional Journey TTC" class="w-[90%] h-[90%] object-contain drop-shadow-2xl group-hover:scale-105 transition-transform duration-700" />
                                </div>
                            </div>
                            <div class="mt-auto">
                                <h3 class="text-2xl md:text-3xl font-medium text-[var(--text-primary)] mb-2 group-hover:text-[var(--accent)] transition-colors">Emotional Journey: TTC</h3>
                                <p class="text-[var(--text-secondary)] text-lg font-light">Wayfinding • Data Viz</p>
                            </div>
                        </a>
                    </article>
                    
                    <!-- Project 8: Puzzle Piece AR -->
                    <article class="w-full flex-shrink-0 px-2 sm:px-4">
                        <a href="case_study_ar_puzzle.html" class="block w-full h-full focus:outline-none p-6 md:p-8 glass-card flex flex-col group">
                            <div class="w-full aspect-[4/3] rounded-2xl overflow-hidden bg-[var(--bg-primary)] shadow-sm mb-6 relative p-12">
                                <div class="w-full h-full project-image transition-transform duration-700 ease-out flex items-center justify-center">
                                    <img src="puzzlepieceAR/Screenshot 2025-12-06 154825.png" alt="Puzzle Piece AR" class="w-[90%] h-[90%] object-contain drop-shadow-2xl group-hover:scale-105 transition-transform duration-700" />
                                </div>
                            </div>
                            <div class="mt-auto">
                                <h3 class="text-2xl md:text-3xl font-medium text-[var(--text-primary)] mb-2 group-hover:text-[var(--accent)] transition-colors">Puzzle Piece AR</h3>
                                <p class="text-[var(--text-secondary)] text-lg font-light">AR Filter • Social</p>
                            </div>
                        </a>
                    </article>
                </div>

                <!-- Arrows -->
                <button id="home-prev" class="absolute top-1/2 -translate-y-1/2 left-2 md:left-6 p-3 dynamic-bg border dynamic-border rounded-full shadow-lg hover:opacity-70 transition-all opacity-0 group-hover/carousel:opacity-100 z-10 cursor-pointer text-[var(--text-primary)]" aria-label="Previous Project">
                    <i data-lucide="chevron-left" class="w-6 h-6"></i>
                </button>
                <button id="home-next" class="absolute top-1/2 -translate-y-1/2 right-2 md:right-6 p-3 dynamic-bg border dynamic-border rounded-full shadow-lg hover:opacity-70 transition-all opacity-0 group-hover/carousel:opacity-100 z-10 cursor-pointer text-[var(--text-primary)]" aria-label="Next Project">
                    <i data-lucide="chevron-right" class="w-6 h-6"></i>
                </button>

                <!-- Dots -->
                <div class="flex justify-center gap-3 mt-8 flex-wrap max-w-sm mx-auto" id="home-carousel-dots">
                    <button class="home-dot w-3 h-3 rounded-full bg-[var(--text-primary)] transition-all cursor-pointer" aria-label="Slide 1"></button>
                    <button class="home-dot w-3 h-3 rounded-full bg-[var(--text-secondary)] opacity-30 hover:opacity-70 transition-all cursor-pointer" aria-label="Slide 2"></button>
                    <button class="home-dot w-3 h-3 rounded-full bg-[var(--text-secondary)] opacity-30 hover:opacity-70 transition-all cursor-pointer" aria-label="Slide 3"></button>
                    <button class="home-dot w-3 h-3 rounded-full bg-[var(--text-secondary)] opacity-30 hover:opacity-70 transition-all cursor-pointer" aria-label="Slide 4"></button>
                    <button class="home-dot w-3 h-3 rounded-full bg-[var(--text-secondary)] opacity-30 hover:opacity-70 transition-all cursor-pointer" aria-label="Slide 5"></button>
                    <button class="home-dot w-3 h-3 rounded-full bg-[var(--text-secondary)] opacity-30 hover:opacity-70 transition-all cursor-pointer" aria-label="Slide 6"></button>
                    <button class="home-dot w-3 h-3 rounded-full bg-[var(--text-secondary)] opacity-30 hover:opacity-70 transition-all cursor-pointer" aria-label="Slide 7"></button>
                    <button class="home-dot w-3 h-3 rounded-full bg-[var(--text-secondary)] opacity-30 hover:opacity-70 transition-all cursor-pointer" aria-label="Slide 8"></button>
                </div>
            </div>
        </section>
"""
    
    # We also need to inject the infinite carousel JS logic into the footer.
    js_logic = """
        // Infinite Carousel Logic
        const track = document.getElementById('home-carousel-track');
        const prevBtn = document.getElementById('home-prev');
        const nextBtn = document.getElementById('home-next');
        const dots = document.querySelectorAll('.home-dot');
        const carouselContainer = document.querySelector('.group\\\\/carousel');
        
        if (track) {
            const originalSlides = Array.from(track.children);
            const totalOriginalSlides = originalSlides.length;
            
            // Clone first and last slide for seamless loop
            const firstClone = originalSlides[0].cloneNode(true);
            const lastClone = originalSlides[totalOriginalSlides - 1].cloneNode(true);
            
            firstClone.setAttribute('aria-hidden', 'true');
            lastClone.setAttribute('aria-hidden', 'true');
            
            track.appendChild(firstClone);
            track.insertBefore(lastClone, originalSlides[0]);
            
            let currentSlide = 1;
            let isTransitioning = false;
            let autoPlayInterval;

            function updateCarousel(instant = false) {
                if (instant) {
                    track.style.transition = 'none';
                } else {
                    track.style.transition = 'transform 700ms cubic-bezier(0.25, 1, 0.5, 1)';
                }
                track.style.transform = `translateX(-${currentSlide * 100}%)`;
                
                let dotIndex = currentSlide - 1;
                if (currentSlide === totalOriginalSlides + 1) dotIndex = 0;
                if (currentSlide === 0) dotIndex = totalOriginalSlides - 1;
                
                dots.forEach((dot, index) => {
                    if(index === dotIndex) {
                        dot.classList.remove('bg-[var(--text-secondary)]', 'opacity-30', 'hover:opacity-70');
                        dot.classList.add('bg-[var(--text-primary)]');
                    } else {
                        dot.classList.add('bg-[var(--text-secondary)]', 'opacity-30', 'hover:opacity-70');
                        dot.classList.remove('bg-[var(--text-primary)]');
                    }
                });
            }
            
            updateCarousel(true);

            function nextSlide() {
                if (isTransitioning) return;
                currentSlide++;
                updateCarousel();
                resetAutoPlay();
            }

            function prevSlide() {
                if (isTransitioning) return;
                currentSlide--;
                updateCarousel();
                resetAutoPlay();
            }

            track.addEventListener('transitionend', () => {
                isTransitioning = false;
                if (currentSlide === totalOriginalSlides + 1) {
                    currentSlide = 1;
                    updateCarousel(true);
                }
                if (currentSlide === 0) {
                    currentSlide = totalOriginalSlides;
                    updateCarousel(true);
                }
            });

            track.addEventListener('transitionstart', () => {
                isTransitioning = true;
            });

            if(prevBtn && nextBtn) {
                prevBtn.addEventListener('click', prevSlide);
                nextBtn.addEventListener('click', nextSlide);
            }

            dots.forEach((dot, index) => {
                dot.addEventListener('click', () => {
                    if (isTransitioning) return;
                    currentSlide = index + 1;
                    updateCarousel();
                    resetAutoPlay();
                });
            });

            function startAutoPlay() {
                if (!animationsDisabled) {
                    autoPlayInterval = setInterval(nextSlide, 4500);
                }
            }

            function resetAutoPlay() {
                clearInterval(autoPlayInterval);
                startAutoPlay();
            }

            startAutoPlay();
            
            if (carouselContainer) {
                carouselContainer.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
                carouselContainer.addEventListener('mouseleave', startAutoPlay);
            }
        }
    </script>
</body>
"""
    # Replace the end script tag to inject our JS
    foot = foot.replace('</script>\n</body>', js_logic)
    
    final_content = head + carousel_html + foot
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

if __name__ == '__main__':
    rewrite_work_html()
