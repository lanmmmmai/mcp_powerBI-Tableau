import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/sms_section_content.txt', 'r', encoding='utf-8') as f:
    sms = f.read()

# find all visual-chart-svg or svg
svgs = list(re.finditer(r'<svg[\s\S]*?</svg>', sms))
print(f"Total SVGs in SMS section: {len(svgs)}")
for i, m in enumerate(svgs):
    print(f"\n--- SVG #{i+1} --- (pos {m.start()}..{m.end()})")
    print(m.group(0)[:400])
