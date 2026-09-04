import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for fname in ['BAO_CAO_CONG_THUC_TINH_TOAN_POWERBI.html', 'README.md']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    print(fname, "has section-bcgd-1?", "section-bcgd-1" in text, "has page-section-bcgd?", "page-section-bcgd" in text)
