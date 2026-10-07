
import json
import os
import re
import difflib

# Paths
TEXT_FILE = r'd:\Alfath\Alfath\ccp\web adli\ALL MODUL SULI.txt'
JSON_FILE = r'd:\Alfath\Alfath\ccp\web adli\data\trade-with-suli.json'
IMAGE_DIR = r'd:\Alfath\Alfath\ccp\web adli\image\Tws'
OUTPUT_FILE = r'd:\Alfath\Alfath\ccp\web adli\data\trade-with-suli_updated.json'

def parse_text_file(filepath):
    modules = []
    current_module = None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Determine if line is a material or a title
        is_material = False
        material_name = ""
        material_url = ""
        
        # Case 1: Starts with a number (e.g., "1 Material Name")
        number_match = re.match(r'^(\d+)\s+(.+)$', line)
        if number_match:
            is_material = True
            content = number_match.group(2)
            # Check for URL in content
            url_match = re.search(r'(https?://\S+)', content)
            if url_match:
                material_url = url_match.group(1)
                material_name = content.replace(material_url, '').strip()
                # Clean up trailing colons or "tradewithsuli com"
                material_name = re.sub(r'[:]+$', '', material_name).strip()
            else:
                material_name = content
        
        # Case 2: Contains a URL but no leading number (e.g., "Name: https://...")
        elif 'http' in line:
            is_material = True
            url_match = re.search(r'(https?://\S+)', line)
            if url_match:
                material_url = url_match.group(1)
                material_name = line.replace(material_url, '').strip()
                material_name = re.sub(r'[:]+$', '', material_name).strip()
            else:
                # Should not happen given 'http' in line check, but safe fallback
                material_name = line
                
        if is_material and current_module:
             # Clean name further
            material_name = re.sub(r'\s*tradewithsuli\s*\.?com.*$', '', material_name, flags=re.IGNORECASE).strip()
            if not material_url:
                material_url = "#"
                
            current_module['materials'].append({
                "name": material_name,
                "url": material_url,
                "image": ""
            })
        else:
            # It's a title (new module)
            if current_module:
                modules.append(current_module)
            
            # Clean title
            title = line
            title = re.sub(r'^\d+\.?\s+', '', title) 
            
            current_module = {
                "title": title,
                "materials": []
            }
            
    # Append last module
    if current_module:
        modules.append(current_module)
        
    return modules

def find_best_image(title, image_dir):
    # Get all files in image dir
    try:
        files = os.listdir(image_dir)
    except FileNotFoundError:
        return ""
        
    # Prepare title for matching
    clean_title = title.lower().replace(':', '').replace('?', '').replace('/', '')
    
    # 1. Exact match (case insensitive) with extension
    for f in files:
        fname = os.path.splitext(f)[0].lower()
        if fname == clean_title:
             return f"image/Tws/{f}"
    
    # 2. Fuzzy match
    # Get list of filenames without extension
    fnames = {os.path.splitext(f)[0].lower(): f for f in files}
    matches = difflib.get_close_matches(clean_title, fnames.keys(), n=1, cutoff=0.7)
    
    if matches:
        return f"image/Tws/{fnames[matches[0]]}"
        
    return ""

def main():
    # 1. Load existing JSON to preserve metadata
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    existing_modules = data.get('modules', [])
    existing_map = {m['title'].lower().strip(): m for m in existing_modules}
    
    # 2. Parse text file
    new_modules_data = parse_text_file(TEXT_FILE)
    
    final_modules = []
    
    # 3. Merge
    for i, new_mod in enumerate(new_modules_data):
        title = new_mod['title']
        clean_title = title.lower().strip()
        
        # Try to find existing
        # Direct match or close match?
        existing = existing_map.get(clean_title)
        
        # If not exact match, try fuzzy on existing keys
        if not existing:
             matches = difflib.get_close_matches(clean_title, existing_map.keys(), n=1, cutoff=0.8)
             if matches:
                 existing = existing_map[matches[0]]
        
        module_entry = {}
        
        if existing:
            # Preserve ID, Category, Level, Description, Must Watch
            module_entry['id'] = existing['id']
            module_entry['title'] = existing['title'] # Keep existing title format or use new? text file seems authoritative on content, keep text title? User said "sesuai dengan materi teks". Let's use text title.
            module_entry['title'] = title # Update title to match text file exactly
            module_entry['category'] = existing.get('category', 'Uncategorized')
            module_entry['level'] = existing.get('level', 0)
            if 'must_watch' in existing:
                module_entry['must_watch'] = existing['must_watch']
            if 'start_here' in existing:
                module_entry['start_here'] = existing['start_here']
            module_entry['description'] = existing.get('description', '')
        else:
            # New module
            module_entry['id'] = 1000 + i # Temporary ID assignment logic
            module_entry['title'] = title
            module_entry['category'] = "Uncategorized"
            module_entry['level'] = 0
            module_entry['description'] = f"Modul tentang {title}"
            
        # Materials - overwrite with new data
        module_entry['materials'] = new_mod['materials']
        
        # Thumbnail / Image
        # Try to find image based on title
        img_path = find_best_image(title, IMAGE_DIR)
        if img_path:
            module_entry['thumbnail'] = img_path
            module_entry['banner_image'] = img_path
        else:
            # Keep existing if available
            if existing and existing.get('thumbnail'):
                module_entry['thumbnail'] = existing['thumbnail']
                module_entry['banner_image'] = existing.get('banner_image', existing['thumbnail'])
            else:
                module_entry['thumbnail'] = "" 
                module_entry['banner_image'] = ""

        # Remove "youtube_url", "pdf_url" from top level if we are using materials structure, 
        # or keep them blank. The existing JSON had them.
        module_entry['youtube_url'] = "https://www.youtube.com" # Default
        module_entry['pdf_url'] = ""
        
        final_modules.append(module_entry)
        
    # Re-assign IDs to be sequential or keep unique? 
    # Better to keep existing IDs for those that matched, and assign new ones for others.
    # The loop above preserved IDs for matched ones.
    # Check for duplicates or collisions?
    
    # Let's just ensure 'modules' is updated
    data['modules'] = final_modules
    
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
        
    print(f"Updated JSON saved to {JSON_FILE}")
    print(f"Processed {len(final_modules)} modules.")

if __name__ == "__main__":
    main()
