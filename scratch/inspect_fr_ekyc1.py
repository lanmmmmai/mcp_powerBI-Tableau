import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('id="eservice-ekyc-1"')
fr_pos = text.find('class="formula-right"', pos)
print(text[fr_pos:fr_pos+300])
