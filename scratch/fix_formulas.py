import os

file_path = r"c:\Users\lan.dm\GIT\sql-query\Web-Vercel\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace(r"\_", "_")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Replaced all \\_ with _ successfully.")
