import os
import glob
from bs4 import BeautifulSoup
import re

def create_slideshow(soup, section, project_id, active_color_class, hover_color_class, text_color_class):
    # active_color_class: e.g. 'bg-indigo-50'
    # hover_color_class: e.g. 'hover:bg-indigo-50/50'
    # text_color_class: e.g. 'text-indigo-500'

    features = section.find_all('div', class_=re.compile(r'grid md:grid-cols-2 gap-12 items-center'))
    if not features:
        return False
        
    new_section = soup.new_tag('section', attrs={'class': 'max-w-6xl mx-auto mb-32 fade-in'})
    
    # Comment
    new_section.insert_before("<!-- VISUAL STORY (CAROUSEL) -->\n")
    
    # Tab Nav
    tab_nav = soup.new_tag('div', attrs={'class': 'flex flex-wrap justify-center gap-4 mb-12'})
    
    # Slides Container
    slides_container = soup.new_tag('div', attrs={'class': 'relative w-full'})
    
    for i, feature in enumerate(features):
        # Extract data
        img_tag = feature.find('img')
        if not img_tag: continue
        
        text_container = None
        img_container = None
        for child in feature.children:
            if child.name == 'div':
                if child.find('img'):
                    img_container = child
                else:
                    text_container = child
        
        if not text_container or not img_container:
            continue
            
        span_tag = text_container.find('span')
        tab_label = span_tag.text.strip() if span_tag else f"Phase {i+1:02d}"
        
        # Create button
        btn = soup.new_tag('button')
        btn['onclick'] = f"showSlide('{project_id}', {i}, '{active_color_class}', '{hover_color_class}')"
        base_classes = f"tab-btn-{project_id} px-6 py-2 rounded-full border dynamic-border {text_color_class} font-semibold tracking-widest text-xs uppercase transition-all cursor-pointer"
        if i == 0:
            btn['class'] = f"{base_classes} {active_color_class}"
        else:
            btn['class'] = f"{base_classes} {hover_color_class}"
        btn.string = tab_label
        tab_nav.append(btn)
        
        # Create slide
        slide = soup.new_tag('div', attrs={'id': f'slide-{project_id}-{i}'})
        if i == 0:
            slide['class'] = f"slide-{project_id} grid md:grid-cols-2 gap-12 items-center opacity-100 transition-opacity duration-500"
        else:
            slide['class'] = f"slide-{project_id} hidden opacity-0 transition-opacity duration-500 grid md:grid-cols-2 gap-12 items-center"
            
        # Keep original classes for containers
        new_img_container = soup.new_tag('div', attrs={'class': img_container.get('class')})
        if 'group' not in new_img_container.get('class', []):
            new_img_container['class'] = new_img_container.get('class', []) + ['group']
        
        new_img = soup.new_tag('img', attrs={
            'src': img_tag.get('src'), 
            'class': 'w-full h-full object-contain group-hover:scale-105 transition duration-700'
        })
        new_img_container.append(new_img)
        
        new_text_container = soup.new_tag('div', attrs={'class': text_container.get('class')})
        for content in text_container.contents:
            if content.name:
                new_tag = soup.new_tag(content.name, attrs={'class': content.get('class')})
                new_tag.string = content.text
                new_text_container.append(new_tag)
            
        slide.append(new_img_container)
        slide.append(new_text_container)
        
        slides_container.append(slide)

    new_section.append(tab_nav)
    new_section.append(slides_container)
    
    section.replace_with(new_section)
    return True

def process_file(filepath, project_id, active_bg, hover_bg, text_col):
    with open(filepath, 'r') as f:
        html = f.read()
        
    if 'showSlide' not in html:
        script_to_add = """
        // Carousel Logic
        window.showSlide = function(carouselId, index, activeClass = 'bg-indigo-50', hoverClass = 'hover:bg-indigo-50/50') {
            const slides = document.querySelectorAll('.slide-' + carouselId);
            const btns = document.querySelectorAll('.tab-btn-' + carouselId);

            slides.forEach((slide, i) => {
                if (i === index) {
                    slide.classList.remove('hidden');
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
"""
        html = html.replace('</script>\n\n    \n\n    <!-- LIGHTBOX MODAL -->', script_to_add + '\n    </script>\n\n    \n\n    <!-- LIGHTBOX MODAL -->')
    
    soup = BeautifulSoup(html, 'html.parser')
    sections = soup.find_all('section')
    changed = False
    
    for s in sections:
        # Check if this is the zig zag section
        if 'space-y-32' in s.get('class', []) or 'space-y-20' in s.get('class', []):
            if s.find('div', class_=re.compile(r'grid md:grid-cols-2 gap-12 items-center')):
                changed = create_slideshow(soup, s, project_id, active_bg, hover_bg, text_col)
                break
                
    if changed:
        with open(filepath, 'w') as f:
            f.write(str(soup))
        print(f"Updated {filepath}")

# We will just run it on the ones we know have ZIG ZAG
process_file('case_study_studybuddy.html', 'studybuddy', 'bg-indigo-50', 'hover:bg-indigo-50/50', 'text-indigo-500')
process_file('case_study_kizuna.html', 'kizuna', 'bg-red-50', 'hover:bg-red-50/50', 'text-red-500')
process_file('case_study_1.html', 'puzzle1', 'bg-stone-50', 'hover:bg-stone-50/50', 'text-stone-500')
process_file('case_study_2.html', 'ttc', 'bg-amber-50', 'hover:bg-amber-50/50', 'text-amber-500')
process_file('case_study_ar_puzzle.html', 'arpuzzle', 'bg-blue-50', 'hover:bg-blue-50/50', 'text-blue-500')

