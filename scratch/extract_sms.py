import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

sms_start = text.find('id="page-section-sms"')
sms_end = text.find('id="page-section-cntt"')
if sms_end == -1:
    sms_end = text.find('</main>')

print(f"SMS section length: {sms_end - sms_start}")
with open('scratch/sms_section_content.txt', 'w', encoding='utf-8') as out:
    out.write(text[sms_start:sms_end])

print("Saved scratch/sms_section_content.txt")
