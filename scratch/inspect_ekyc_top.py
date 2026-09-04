import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/ekyc_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the beginning of page-eservice-ekyc
print("Header and section block:")
print(text[:2200])
