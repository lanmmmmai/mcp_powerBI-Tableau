import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Check all occurrences of 'code-box'
code_box_matches = list(re.finditer(r'class="[^"]*code-box[^"]*"', text))
print(f"Total 'code-box' occurrences: {len(code_box_matches)}")
for m in code_box_matches:
    pos = m.start()
    line_no = text[:pos].count('\n') + 1
    # find enclosing section or tab
    sec_pos = text.rfind('id="section-', 0, pos)
    sec_id = text[sec_pos:text.find('"', sec_pos+4)] if sec_pos != -1 else "unknown"
    print(f"  Line {line_no} ({sec_id}): {text[pos-20:pos+50]}")

# 2. Check all occurrences of 'code-copy-btn'
copy_btn_matches = list(re.finditer(r'class="[^"]*code-copy-btn[^"]*"', text))
print(f"\nTotal 'code-copy-btn' occurrences: {len(copy_btn_matches)}")
for m in copy_btn_matches[:10]:
    pos = m.start()
    line_no = text[:pos].count('\n') + 1
    sec_pos = text.rfind('id="section-', 0, pos)
    sec_id = text[sec_pos:text.find('"', sec_pos+4)] if sec_pos != -1 else "unknown"
    print(f"  Line {line_no} ({sec_id}): {text[pos-20:pos+50]}")

# 3. Check <pre> tags without class="code-block"
pre_no_block = []
for m in re.finditer(r'<pre\b([^>]*)>', text):
    attrs = m.group(1)
    if 'code-block' not in attrs:
        pos = m.start()
        line_no = text[:pos].count('\n') + 1
        sec_pos = text.rfind('id="section-', 0, pos)
        sec_id = text[sec_pos:text.find('"', sec_pos+4)] if sec_pos != -1 else "unknown"
        pre_no_block.append((line_no, sec_id, m.group(0)))

print(f"\nTotal <pre> without 'code-block': {len(pre_no_block)}")
for line_no, sec_id, tag in pre_no_block[:20]:
    print(f"  Line {line_no} ({sec_id}): {tag}")
