import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

sms_start = text.find('id="page-section-sms"')
sms_end = text.find('</section>', text.find('id="section-sms-4"', sms_start))
sms_block = text[sms_start:sms_end+2000]

# find all <svg in sms_block
svg_pos = 0
while True:
    svg_pos = sms_block.find('<svg', svg_pos)
    if svg_pos == -1: break
    svg_end = sms_block.find('</svg>', svg_pos)
    print(f"=== SVG in SMS (len {svg_end - svg_pos}) ===")
    print(sms_block[svg_pos:svg_end+6])
    print("=" * 60)
    svg_pos = svg_end + 6
