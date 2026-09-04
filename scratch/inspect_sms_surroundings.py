import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/sms_section_content.txt', 'r', encoding='utf-8') as f:
    sms = f.read()

for i in range(1, 6):
    m_id = f'section-sms-{i}'
    pos = sms.find(m_id)
    print(f"=== {m_id} at pos {pos} ===")
    if pos != -1:
        svg_start = sms.find('<svg', pos)
        svg_end = sms.find('</svg>', svg_start)
        print("SVG length:", svg_end - svg_start)
        print("Context before SVG:")
        print(sms[max(0, svg_start-150):svg_start])
        print("---")
