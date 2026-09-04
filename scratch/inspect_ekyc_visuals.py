import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/ekyc_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# check for formula-right or visual-chart-svg or svg
svgs = re.findall(r'<svg[\s\S]*?</svg>', text)
print(f"Total SVGs in page-eservice-ekyc: {len(svgs)}")

frs = re.findall(r'<div class="formula-right">[\s\S]*?</div>\s*</div>\s*</div>', text)
print(f"Total formula-right in page-eservice-ekyc: {len(frs)}")
for i, fr in enumerate(frs):
    print(f"\n--- FR #{i+1} ---")
    print(fr[:300])
