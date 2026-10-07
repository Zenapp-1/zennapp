
import json

with open(r'd:\Alfath\Alfath\ccp\web adli\data\akademi-crypto.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for module in data.get('modules', []):
    print(f"{module.get('id')}: {module.get('title')}")
