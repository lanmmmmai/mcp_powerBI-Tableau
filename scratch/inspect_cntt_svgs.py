import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos1 = text.find('id="section-cntt-1-tab-math"')
svg1_start = text.find('<svg', pos1)
svg1_end = text.find('</svg>', svg1_start) + 6
print("=== SVG #35 in index.html ===")
print(text[svg1_start:svg1_end])

pos2 = text.find('id="section-cntt-2-tab-math"')
svg2_start = text.find('<svg', pos2)
svg2_end = text.find('</svg>', svg2_start) + 6
print("\n=== SVG #36 in index.html ===")
print(text[svg2_start:svg2_end])
