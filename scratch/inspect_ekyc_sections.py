import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="page-eservice-ekyc"')
next_page = text.find('class="portal-page', pos + 30)
ekyc_content = text[pos:next_page]

print(f"page-eservice-ekyc length: {len(ekyc_content)} chars")

with open('scratch/ekyc_full.txt', 'w', encoding='utf-8') as out:
    out.write(ekyc_content)

# find all section- inside
import re
sections = re.findall(r'<article\b[^>]*id="([^"]+)"[^>]*>[\s\S]*?<h3[^>]*>(.*?)</h3>', ekyc_content)
print(f"Total articles/sections in ekyc: {len(sections)}")
for sid, title in sections:
    print(f"  - {sid}: {title.strip()}")
