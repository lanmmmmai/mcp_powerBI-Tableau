# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_tag = '<!-- LIVE DASHBOARD OVERVIEW VISUAL MOCKUP (THEO THIET KE POWER BI DSC) -->'
end_tag = '<!-- 5.1 Bộ 5 Chỉ Số KPI Tổng Quan & Sparklines Xu Hướng -->'

pos1 = text.find(start_tag)
pos2 = text.find(end_tag)

if pos1 != -1 and pos2 != -1:
    # remove the block from pos1 up to pos2
    text = text[:pos1] + text[pos2:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Removed Dashboard Overview block ({pos2 - pos1} chars) successfully.")
else:
    print(f"Could not find tags: pos1={pos1}, pos2={pos2}")
