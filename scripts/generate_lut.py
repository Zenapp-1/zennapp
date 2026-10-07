#!/usr/bin/env python3
"""Generate a 120-step easing lookup table (easeOutCubic) for use in JS animations.
Run: python scripts/generate_lut.py
Generates: easing120.json in project root.
"""
import json
from math import pow

def ease_out_cubic(t):
    return 1 - pow(1 - t, 3)

def main():
    steps = 120
    values = [ease_out_cubic(i / steps) for i in range(steps + 1)]
    with open('easing120.json','w',encoding='utf-8') as f:
        json.dump(values,f,indent=2)
    print('Wrote easing120.json with', len(values), 'values')

if __name__ == '__main__':
    main()
