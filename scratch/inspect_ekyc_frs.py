import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/ekyc_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for i in range(1, 5):
    aid = f'eservice-ekyc-{i}'
    pos = text.find(aid)
    print(f"=== {aid} ===")
    if pos != -1:
        fr_pos = text.find('class="formula-right"', pos)
        fr_end = text.find('</div>\n                  </div>\n                </div>', fr_pos)
        print(text[fr_pos:fr_end+10])
    print("-" * 50)
