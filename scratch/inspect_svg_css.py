import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see visual-chart-svg CSS
css_pos = text.find('.visual-chart-svg')
if css_pos != -1:
    print("CSS for visual-chart-svg:")
    print(text[css_pos:css_pos+300])
else:
    print("No CSS for visual-chart-svg")
