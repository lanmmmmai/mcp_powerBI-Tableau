import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="section-bcgd"')
pos_sec1 = text.find('id="section-bcgd-1"')
print(text[pos:pos_sec1])
