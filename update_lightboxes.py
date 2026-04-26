import os
import glob
import re

new_lightbox = """<!-- LIGHTBOX MODAL -->
    <div id="lightbox" class="fixed inset-0 z-50 bg-stone-900/90 backdrop-blur-sm opacity-0 pointer-events-none transition-opacity duration-300 flex items-center justify-center p-4 md:p-10 cursor-zoom-out">
        <div class="relative max-w-5xl w-full max-h-full flex items-center justify-center">
            <button id="lightbox-prev" class="absolute left-2 md:-left-12 z-50 text-white/70 hover:text-white bg-stone-900/50 hover:bg-stone-900 p-2 rounded-full backdrop-blur-md transition-all cursor-pointer">
                <i data-lucide="chevron-left" class="w-6 h-6 md:w-8 md:h-8"></i>
            </button>

            <img id="lightbox-img" src="" class="max-w-full max-h-[90vh] object-contain rounded-lg shadow-2xl scale-95 transition-transform duration-300" />
            
            <button id="lightbox-next" class="absolute right-2 md:-right-12 z-50 text-white/70 hover:text-white bg-stone-900/50 hover:bg-stone-900 p-2 rounded-full backdrop-blur-md transition-all cursor-pointer">
                <i data-lucide="chevron-right" class="w-6 h-6 md:w-8 md:h-8"></i>
            </button>

            <button id="lightbox-close" class="absolute -top-4 -right-4 md:-top-6 md:-right-6 z-50 text-white/70 hover:text-white bg-stone-900/50 hover:bg-stone-900 p-2 rounded-full backdrop-blur-md transition-all cursor-pointer">
                <i data-lucide="x" class="w-5 h-5 md:w-6 md:h-6"></i>
            </button>
        </div>
    </div>

    <script>
        // Lightbox Logic
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxClose = document.getElementById('lightbox-close');
        const lightboxNext = document.getElementById('lightbox-next');
        const lightboxPrev = document.getElementById('lightbox-prev');
        const images = document.querySelectorAll('main img');
        const imagesArray = Array.from(images);
        let currentImageIndex = 0;

        images.forEach((img, index) => {
            // Add pointer cursor to images
            img.style.cursor = 'zoom-in';
            
            img.addEventListener('click', (e) => {
                e.stopPropagation();
                currentImageIndex = index;
                lightboxImg.src = img.src;
                lightbox.classList.remove('opacity-0', 'pointer-events-none');
                lightbox.classList.add('opacity-100');
                // Small scale animation
                setTimeout(() => {
                    lightboxImg.classList.remove('scale-95');
                    lightboxImg.classList.add('scale-100');
                }, 50);
            });
        });

        const closeLightbox = () => {
            lightbox.classList.remove('opacity-100');
            lightbox.classList.add('opacity-0', 'pointer-events-none');
            lightboxImg.classList.remove('scale-100');
            lightboxImg.classList.add('scale-95');
            setTimeout(() => {
                lightboxImg.src = '';
            }, 300);
        };

        const showNextImage = (e) => {
            if (e) e.stopPropagation();
            if (imagesArray.length > 0) {
                currentImageIndex = (currentImageIndex + 1) % imagesArray.length;
                lightboxImg.src = imagesArray[currentImageIndex].src;
            }
        };

        const showPrevImage = (e) => {
            if (e) e.stopPropagation();
            if (imagesArray.length > 0) {
                currentImageIndex = (currentImageIndex - 1 + imagesArray.length) % imagesArray.length;
                lightboxImg.src = imagesArray[currentImageIndex].src;
            }
        };

        lightbox.addEventListener('click', closeLightbox);
        lightboxClose.addEventListener('click', closeLightbox);
        lightboxNext.addEventListener('click', showNextImage);
        lightboxPrev.addEventListener('click', showPrevImage);

        // Prevent clicks on the image from closing the lightbox
        lightboxImg.addEventListener('click', (e) => {
            e.stopPropagation();
        });

        document.addEventListener('keydown', (e) => {
            if (lightbox.classList.contains('opacity-100')) {
                if (e.key === 'Escape') closeLightbox();
                if (e.key === 'ArrowRight') showNextImage();
                if (e.key === 'ArrowLeft') showPrevImage();
            }
        });
    </script>"""

import os
import glob
import re

# Navigate to the correct directory
os.chdir("/Users/michellemiyata/Downloads/portfolio-main")

for filepath in glob.glob("case_study_*.html"):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Use regex to find the old lightbox block and replace it
    pattern = r"<!-- LIGHTBOX MODAL -->.*?</script>"
    new_content = re.sub(pattern, new_lightbox, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Lightbox not found or already updated in {filepath}")
