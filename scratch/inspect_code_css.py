import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for term in ['.code-box', 'code-header', 'code-copy-btn', 'language-tableau', 'hljs', 'pre code', 'pre {']:
    pos = 0
    matches = []
    while True:
        pos = text.find(term, pos)
        if pos == -1: break
        matches.append(pos)
        pos += len(term)
    print(f"{term}: {len(matches)} occurrences")
    if matches and matches[0] < text.find('</style>'):
        print(f"  First in CSS at {matches[0]}:")
        print("  " + text[matches[0]:matches[0]+200].replace('\n', ' '))
