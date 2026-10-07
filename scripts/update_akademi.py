
import json
import re
import os

JSON_PATH = r'd:\Alfath\Alfath\ccp\web adli\data\akademi-crypto.json'
TEXT_PATH = r'd:\Alfath\Alfath\ccp\web adli\scripts\new_modules_raw.txt'

def parse_raw_text(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modules = []
    current_module = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check if it has a URL
        url_match = re.search(r'(https?://\S+)', line)
        if url_match:
            url = url_match.group(1)
            # Remove URL from name
            name = line.replace(url, '').strip()
            # Clean up name (remove trailing colons, leading numbers/words like "Video X X")
            name = re.sub(r'[:]+$', '', name).strip()
            # Try to remove leading numbers/patterns like "Video 3 1" or "1 "
            name = re.sub(r'^(\d+|\w+\s+\d+\s+\d+)\s+', '', name).strip()
            
            if current_module:
                current_module['materials'].append({
                    "name": name,
                    "url": url,
                    "image": ""
                })
        else:
            # It's a title
            title = line
            # Clean title (remove leading numbers like "1 " or "01 ")
            title = re.sub(r'^\d+\.?\s+', '', title).strip()
            
            # Check if we already have it in the list we are building
            existing_in_list = False
            for m in modules:
                if m['title'].lower() == title.lower():
                    current_module = m
                    existing_in_list = True
                    break
            
            if not existing_in_list:
                current_module = {
                    "title": title,
                    "materials": [],
                    "youtube_url": "", # Will fill with first material URL
                    "description": f"Pelajari seluk beluk {title} untuk meningkatkan pemahaman Anda dalam dunia cryptocurrency.",
                    "thumbnail": "image/crypto.jpeg",
                    "banner_image": "image/crypto.jpeg",
                    "level": 1,
                    "category": "Crypto",
                    "pdf_url": ""
                }
                modules.append(current_module)
                
    return modules

def main():
    if not os.path.exists(JSON_PATH):
        print(f"Error: {JSON_PATH} not found.")
        return

    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_modules = data.get('modules', [])
    existing_titles_map = {m['title'].lower().strip(): m for m in existing_modules}
    
    # Get max ID
    max_id = 0
    for m in existing_modules:
        if isinstance(m.get('id'), int):
            if m['id'] > max_id:
                max_id = m['id']
    
    new_modules_data = parse_raw_text(TEXT_PATH)
    
    added_count = 0
    updated_count = 0
    
    for new_mod in new_modules_data:
        title_clean = new_mod['title'].lower().strip()
        
        # Find first material URL for the top-level youtube_url if missing
        if new_mod['materials']:
            new_mod['youtube_url'] = new_mod['materials'][0]['url']
            
        if title_clean in existing_titles_map:
            # Update existing module
            existing = existing_titles_map[title_clean]
            
            # Add materials that don't already exist (by URL)
            existing_material_urls = {mat['url'].lower().strip() for mat in existing.get('materials', [])}
            newly_added_mats = 0
            for mat in new_mod['materials']:
                if mat['url'].lower().strip() not in existing_material_urls:
                    if 'materials' not in existing:
                        existing['materials'] = []
                    existing['materials'].append(mat)
                    newly_added_mats += 1
            
            if newly_added_mats > 0:
                updated_count += 1
        else:
            # Add as new module
            max_id += 1
            new_mod['id'] = max_id
            existing_modules.append(new_mod)
            added_count += 1
            # Update map to avoid adding same title twice from the new list if it repeats
            existing_titles_map[title_clean] = new_mod

    data['modules'] = existing_modules
    
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully processed {len(new_modules_data)} titles from text.")
    print(f"Added {added_count} new modules.")
    print(f"Updated {updated_count} existing modules.")

if __name__ == "__main__":
    main()
