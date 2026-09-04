import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for fname in ['index.html', 'BAO_CAO_CONG_THUC_TINH_TOAN_POWERBI.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    
    pre_tags = re.findall(r'<pre\b[^>]*>', text)
    non_code_block = [t for t in pre_tags if 'code-block' not in t]
    code_box_tags = re.findall(r'class="[^"]*code-box[^"]*"', text)
    code_copy_tags = re.findall(r'class="[^"]*code-copy-btn[^"]*"', text)
    
    print(f"=== {fname} ===")
    print(f"Total <pre> tags: {len(pre_tags)}")
    print(f"<pre> without 'code-block': {len(non_code_block)}")
    print(f"Remaining 'code-box': {len(code_box_tags)}")
    print(f"Remaining 'code-copy-btn': {len(code_copy_tags)}")
