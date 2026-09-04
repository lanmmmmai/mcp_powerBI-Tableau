import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

print(f"style.css length: {len(css)} chars, lines: {len(css.splitlines())}")
print("Has sparkline?", "sparkline" in css)
print("Has heatmap?", "heatmap" in css)
