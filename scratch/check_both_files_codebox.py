import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for fname in ['index.html', 'BAO_CAO_CONG_THUC_TINH_TOAN_POWERBI.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"=== {fname} ===")
    print("code-box:", len(re.findall(r'class="[^"]*code-box[^"]*"', text)))
    print("code-copy-btn:", len(re.findall(r'class="[^"]*code-copy-btn[^"]*"', text)))
    print("pre without code-block:", len(re.findall(r'<pre>(?!\s*<code class="code-block")', text)))
