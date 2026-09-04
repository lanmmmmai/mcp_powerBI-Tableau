# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("File size:", len(text))

# Check LaTeX formulas
math_blocks = re.findall(r'(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\$[^\$\n]+\$|\\\([^\)]+\\\))', text)
print(f"Total math blocks: {len(math_blocks)}")

# Check for problematic unescaped % or raw \_
issues = []
for i, mb in enumerate(math_blocks):
    # Check unescaped % (not preceded by \)
    unescaped_pct = re.findall(r'(?<!\\)%', mb)
    if unescaped_pct:
        issues.append(f"Math block {i} has unescaped %: {mb[:60]}")
    # Check \_ inside \text
    if r'\_' in mb:
        issues.append(f"Math block {i} has \\_ : {mb[:60]}")

print(f"LaTeX formula issues found: {len(issues)}")
for iss in issues[:10]:
    print("  -", iss)

# Verify that BCGD sections exist and are populated
for i in range(1, 6):
    tab_id = f'section-bcgd-{i}-tab-math'
    pos = text.find(tab_id)
    print(f"{tab_id} found: {pos != -1}")

print("Dashboard Overview present:", "LIVE DASHBOARD OVERVIEW VISUAL MOCKUP" in text)
print("CSS BCGD present:", "/* BCGD LIVE DASHBOARD VISUALS" in text)
