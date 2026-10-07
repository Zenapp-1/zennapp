
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
            name = line.replace(url, '').strip()
            name = re.sub(r'[:]+$', '', name).strip()
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
                    "youtube_url": "", 
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
    new_modules_data = parse_raw_text(TEXT_PATH)
    print(f"Parsed {len(new_modules_data)} titles:")
    for m in new_modules_data:
        print(f"- {m['title']} ({len(m['materials'])} materials)")

if __name__ == "__main__":
    main()
