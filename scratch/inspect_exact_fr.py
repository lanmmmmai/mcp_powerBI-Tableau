import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for i in range(1, 6):
    tab_id = f'section-bcgd-{i}-tab-math'
    pos = text.find(tab_id)
    fr_pos = text.find('class="formula-right"', pos)
    fr_end = text.find('</div>\n                  </div>\n                </div>', fr_pos)
    fr_block = text[fr_pos - 25 : fr_end + 33]
    print(f"=== BCGD {i} FR BLOCK (len {len(fr_block)}) ===")
    print(fr_block)
    print()
