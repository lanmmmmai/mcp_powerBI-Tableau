import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['Báo cáo mở TKGDCK qua eKYC', 'ekyc', 'page-section-', 'Báo cáo Core Flex']:
    pos = 0
    matches = []
    while True:
        pos = text.lower().find(term.lower(), pos)
        if pos == -1: break
        matches.append(pos)
        pos += len(term)
    print(f'{term}: {len(matches)} matches')
    if matches:
        print(f"  First match: {text[matches[0]-50:matches[0]+150]}")
