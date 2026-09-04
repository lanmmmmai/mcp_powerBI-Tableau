import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="section-cntt-1-tab-math"')
svg_start = text.find('<svg', pos)
svg_end = text.find('</svg>', svg_start) + 6
print("SVG #35:")
print(text[svg_start:svg_end])
