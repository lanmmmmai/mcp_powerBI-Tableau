import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('DAX MEASURE / CALCULATION')
print(f"Found 'DAX MEASURE / CALCULATION' at {pos}")
if pos != -1:
    print(text[pos-200:pos+600])
