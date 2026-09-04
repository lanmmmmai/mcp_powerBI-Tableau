import os

file_path = r"c:\Users\lan.dm\GIT\sql-query\Web-Vercel\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

ranges = [
    (23129, 23204),
    (22678, 22769),
    (22432, 22508),
    (22209, 22296),
    (19502, 20489),
    (19025, 19227)
]

# Create a set of lines to delete (0-indexed)
lines_to_delete = set()
for start, end in ranges:
    for i in range(start - 1, end):
        lines_to_delete.add(i)

new_lines = []
for i, line in enumerate(lines):
    if i not in lines_to_delete:
        new_lines.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Deleted dashboard blocks successfully.")
