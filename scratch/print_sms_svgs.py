import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/sms_section_content.txt', 'r', encoding='utf-8') as f:
    sms = f.read()

svgs = list(re.finditer(r'<svg[\s\S]*?</svg>', sms))
for i, m in enumerate(svgs):
    print(f"==================== SVG #{i+1} ====================")
    print(m.group(0))
    print()
