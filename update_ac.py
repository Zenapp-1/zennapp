import json
import os
import glob
import re

txt_path = 'c:/Zepetto/web adli/ac.txt'
json_path = 'c:/Zepetto/web adli/data/akademi-crypto.json'
img_dir = 'c:/Zepetto/web adli/image/AC BACKGROUND'

# Read images
images = {}
for file in os.listdir(img_dir):
    name, ext = os.path.splitext(file)
    images[name.strip().lower()] = f'image/AC BACKGROUND/{file}'

# Read existing JSON to preserve categories if possible
try:
    with open(json_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)
        existing_modules = {m['title'].strip().lower(): m for m in existing_data.get('modules', [])}
except Exception as e:
    existing_modules = {}

# Parse ac.txt
modules = []
with open(txt_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Split by double newline to get blocks
blocks = re.split(r'\n\s*\n', content.strip())

module_id = 1
for block in blocks:
    lines = [L.strip() for L in block.split('\n') if L.strip()]
    if not lines: continue
    
    title = lines[0]
    materials = []
    
    for line in lines[1:]:
        # Find 'http'
        http_idx = line.find('http')
        if http_idx != -1:
            name = line[:http_idx].strip()
            if name.endswith(':'):
                name = name[:-1].strip()
            url = line[http_idx:].strip()
            materials.append({"name": name, "url": url, "image": ""})
        else:
            materials.append({"name": line, "url": "", "image": ""})
            
    # Find matching image
    title_key = title.strip().lower()
    
    # Try exact match
    img_path = images.get(title_key)
    
    # Try approximate match
    if not img_path:
        for k, v in images.items():
            if k in title_key or title_key in k:
                img_path = v
                break
                
    if not img_path:
        img_path = "image/crypto.jpeg"
        
    # Preserve category or use default
    category = "Crypto"
    existing = existing_modules.get(title_key)
    if existing:
        category = existing.get('category', 'Crypto')
        
    mod = {
        "id": module_id,
        "title": title,
        "category": category,
        "level": 1,
        "description": f"Materi pembelajaran tentang {title}.",
        "materials": materials,
        "thumbnail": img_path,
        "banner_image": img_path,
        "youtube_url": "https://www.youtube.com",
        "pdf_url": ""
    }
    modules.append(mod)
    module_id += 1

final_data = {
    "pageTitle": "Akademi Crypto",
    "pageDescription": "Materi belajar Akademi Crypto",
    "modules": modules
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(final_data, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(modules)} modules to {json_path}")
