import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all SVGs with pie/circle charts
svgs = list(re.finditer(r'<svg[\s\S]*?</svg>', text))
print(f"Total SVGs in index.html: {len(svgs)}")

for i, m in enumerate(svgs):
    svg_code = m.group(0)
    # check if it has a pie chart (has <circle and <path or percent text)
    if '<path' in svg_code and ('circle' in svg_code or '%' in svg_code):
        # find enclosing section
        pos = m.start()
        sec_pos = text.rfind('id="section-', 0, pos)
        sec_id = text[sec_pos:text.find('"', sec_pos+4)] if sec_pos != -1 else "unknown"
        print(f"\n--- SVG #{i+1} in {sec_id} ---")
        # print text elements inside this svg
        texts = re.findall(r'<text\b[^>]*>.*?</text>', svg_code)
        for t in texts:
            if '%' in t or any(c.isdigit() for c in t):
                print("  ", t)
