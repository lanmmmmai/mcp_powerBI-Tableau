import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find next occurrence of eservice-ekyc after 83000
pos = text.find('eservice-ekyc', 83000)
print(f"Next 'eservice-ekyc' at: {pos}")
if pos != -1:
    print(text[pos-100:pos+1500])
