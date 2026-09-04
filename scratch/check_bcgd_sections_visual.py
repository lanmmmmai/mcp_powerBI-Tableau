# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for i in range(1, 6):
    tab_id = f'section-bcgd-{i}-tab-math'
    pos = text.find(tab_id)
    fr_pos = text.find('class="formula-right"', pos)
    print(f"=== Mục 5.{i} Visual Block ===")
    print(text[fr_pos:fr_pos+250])
    print("...")
