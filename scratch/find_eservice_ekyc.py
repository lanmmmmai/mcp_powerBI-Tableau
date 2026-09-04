import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="eservice-ekyc"')
if pos == -1:
    pos = text.find('eservice-ekyc')
print("Position of eservice-ekyc:", pos)
if pos != -1:
    print(text[pos-100:pos+1500])
