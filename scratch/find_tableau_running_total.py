import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 772559
tableau_pos = text.find('Running total', pos + 1)
print(f"Next 'Running total' at: {tableau_pos}")
if tableau_pos != -1:
    print(text[tableau_pos-300:tableau_pos+600])
