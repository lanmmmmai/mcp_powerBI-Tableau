import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('1.405')
while pos != -1:
    print(f"=== Match at {pos} ===")
    print(text[max(0, pos-200):min(len(text), pos+300)])
    print("-" * 50)
    pos = text.find('1.405', pos + 1)
