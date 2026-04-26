import re
import sys

def convert_file(filepath, project_id, active_bg, hover_bg, text_col):
    with open(filepath, 'r') as f:
        html = f.read()

    # Find the VISUAL STORY (ZIG ZAG) section
    # The section starts with <!-- VISUAL STORY (ZIG ZAG) --> or similar
    # And ends with </section>
    
    pattern = r'<!-- VISUAL.*?\bZIG ZAG\b.*?-->\s*<section class="max-w-6xl mx-auto mb-32.*?>\s*(.*?)\s*</section>'
    match = re.search(pattern, html, flags=re.DOTALL | re.IGNORECASE)
    
    if not match:
        print(f"Could not find zig zag section in {filepath}")
        return False
        
    inner_html = match.group(1)
    
    # Extract features
    # Each feature is a div with class "grid md:grid-cols-2 gap-12 items-center fade-in"
    features = re.findall(r'<div class="grid md:grid-cols-2 gap-12 items-center fade-in">(.*?)</div>\s*(?=<!-- Feature|<div class="grid md:grid-cols-2|\Z)', inner_html, flags=re.DOTALL)
    
    if not features:
        print(f"No features found in {filepath}")
        return False
        
    print(f"Found {len(features)} features in {filepath}")
    
    tab_nav_html = f"""<!-- VISUAL STORY (CAROUSEL) -->
        <section class="max-w-6xl mx-auto mb-32 fade-in">
            <!-- Tab Navigation -->
            <div class="flex flex-wrap justify-center gap-4 mb-12">"""
            
    for i, feature in enumerate(features):
        # find the span with text inside
        span_match = re.search(r'<span class=".*?".*?>(.*?)</span>', feature, flags=re.DOTALL)
        tab_label = span_match.group(1).strip() if span_match else f"Phase {i+1:02d}"
        
        btn_class = f"tab-btn-{project_id} px-6 py-2 rounded-full border dynamic-border {text_col} font-semibold tracking-widest text-xs uppercase transition-all cursor-pointer"
        if i == 0:
            btn_class += f" {active_bg}"
        else:
            btn_class += f" {hover_bg}"
            
        tab_nav_html += f"""
                <button onclick="showSlide('{project_id}', {i}, '{active_bg}', '{hover_bg}')" class="{btn_class}">{tab_label}</button>"""
                
    tab_nav_html += """
            </div>

            <!-- Slides Container -->
            <div class="relative w-full">"""
            
    for i, feature in enumerate(features):
        # Separate the two columns (one has an image, the other has text)
        cols = re.split(r'(<div[^>]*class="order-)', feature)
        # cols will contain fragments
        # A simpler way is to just take the feature HTML, but change the wrapper
        slide_class = f"slide-{project_id} grid md:grid-cols-2 gap-12 items-center opacity-100 transition-opacity duration-500" if i == 0 else f"slide-{project_id} hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center"
        
        tab_nav_html += f"""
                <!-- Slide {i+1} -->
                <div id="slide-{project_id}-{i}" class="{slide_class}">
                    {feature}
                </div>"""
                
    tab_nav_html += """
            </div>
        </section>"""
        
    # Replace the old section
    new_html = html[:match.start()] + tab_nav_html + html[match.end():]
    
    # Inject JS
    if 'window.showSlide = function' not in new_html:
        script_inject = f"""
        // Carousel Logic
        window.showSlide = function(carouselId, index, activeClass = '{active_bg}', hoverClass = '{hover_bg}') {{
            const slides = document.querySelectorAll('.slide-' + carouselId);
            const btns = document.querySelectorAll('.tab-btn-' + carouselId);

            slides.forEach((slide, i) => {{
                if (i === index) {{
                    slide.classList.remove('hidden');
                    // Force reflow
                    void slide.offsetWidth;
                    slide.classList.remove('opacity-0');
                    slide.classList.add('opacity-100');
                }} else {{
                    slide.classList.add('hidden');
                    slide.classList.remove('opacity-100');
                    slide.classList.add('opacity-0');
                }}
            }});

            btns.forEach((btn, i) => {{
                if (i === index) {{
                    btn.classList.add(...activeClass.split(' '));
                    btn.classList.remove(...hoverClass.split(' '));
                }} else {{
                    btn.classList.remove(...activeClass.split(' '));
                    btn.classList.add(...hoverClass.split(' '));
                }}
            }});
        }};
    </script>
"""
        new_html = new_html.replace('</script>\n\n    \n\n    <!-- LIGHTBOX MODAL -->', script_inject + '\n    \n\n    <!-- LIGHTBOX MODAL -->')

    with open(filepath, 'w') as f:
        f.write(new_html)
    print(f"Successfully converted {filepath}")
    return True

convert_file('case_study_kizuna.html', 'kizuna', 'bg-red-50', 'hover:bg-red-50/50', 'text-red-500')
convert_file('case_study_1.html', 'puzzle1', 'bg-stone-50', 'hover:bg-stone-50/50', 'text-stone-500')
convert_file('case_study_2.html', 'ttc', 'bg-amber-50', 'hover:bg-amber-50/50', 'text-amber-500')
convert_file('case_study_ar_puzzle.html', 'arpuzzle', 'bg-blue-50', 'hover:bg-blue-50/50', 'text-blue-500')

