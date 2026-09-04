import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('.code-container {')
print(f"Found .code-container at {pos}")
print(repr(text[pos:pos+400]))
