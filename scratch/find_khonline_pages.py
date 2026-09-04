import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['eservice-khonline', 'page-eservice-khonline', 'eservice-tvs', 'page-eservice-tvs', 'Báo cáo quản lý khách hàng online', 'Báo cáo khách hàng TVS']:
    pos = 0
    matches = []
    while True:
        pos = text.find(term, pos)
        if pos == -1: break
        matches.append(pos)
        pos += len(term)
    print(f'{term}: {len(matches)} matches at {matches}')
