import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Check all pie charts with <circle and <text with %
svgs = list(re.finditer(r'<svg[\s\S]*?</svg>', text))
for i, m in enumerate(svgs):
    svg = m.group(0)
    # find texts with %
    pct_texts = re.findall(r'<text\b[^>]*>[^<]*%[^<]*</text>', svg)
    if pct_texts and '<circle' in svg:
        sec_pos = text.rfind('id="section-', 0, m.start())
        sec_id = text[sec_pos:text.find('"', sec_pos+4)] if sec_pos != -1 else "unknown"
        print(f"SVG #{i+1} in {sec_id}:")
        for pt in pct_texts:
            print("  ", pt)
