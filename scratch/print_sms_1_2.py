import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/sms_section_content.txt', 'r', encoding='utf-8') as f:
    sms = f.read()

svgs = list(re.finditer(r'<svg[\s\S]*?</svg>', sms))
print("SVG #2:")
print(svgs[1].group(0))
print("\nSVG #1:")
print(svgs[0].group(0))
