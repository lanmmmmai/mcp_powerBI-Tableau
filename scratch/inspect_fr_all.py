import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for i in range(1, 6):
    tab_id = f'section-bcgd-{i}-tab-math'
    pos = text.find(tab_id)
    if pos != -1:
        sub = text[pos:pos+4000]
        fr_start = sub.find('class="formula-right"')
        print(f'=== BCGD {i} ===')
        if fr_start != -1:
            # find end of formula-right div
            fr_end = sub.find('</div>\n                  </div>\n                </div>', fr_start)
            if fr_end != -1:
                print(sub[fr_start:fr_end+10])
            else:
                print(sub[fr_start:fr_start+500])
