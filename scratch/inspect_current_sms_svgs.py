import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

sms_start = text.find('id="page-section-sms"')
curr = sms_start
for i in range(1, 6):
    svg_start = text.find('<svg class="visual-chart-svg"', curr)
    svg_end = text.find('</svg>', svg_start) + 6
    print(f"=== SVG #{i} ===")
    print(text[svg_start:svg_end])
    print()
    curr = svg_end
