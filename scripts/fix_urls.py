
import json
import re

JSON_FILE = r'd:\Alfath\Alfath\ccp\web adli\data\trade-with-suli.json'

def fix_urls(data):
    if isinstance(data, dict):
        return {k: fix_urls(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [fix_urls(v) for v in data]
    elif isinstance(data, str):
        # Remove .com from ends of youtu.be links
        # Match youtu.be links that end with .com and are followed by nothing or end of string
        return re.sub(r'(https?://youtu\.be/[A-Za-z0-9_-]+)\.com$', r'\1', data)
    return data

def main():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        fixed_data = fix_urls(data)
        
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(fixed_data, f, indent=2)
            
        print(f"Successfully fixed URLs in {JSON_FILE}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
