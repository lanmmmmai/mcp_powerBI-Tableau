# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from prep_ekyc_visuals import (
    TOP_DASHBOARD_EKYC,
    SVG_EKYC_1,
    SVG_EKYC_2,
    SVG_EKYC_3,
    SVG_EKYC_4
)

def update_ekyc_page(filepath):
    print(f"\n================ Processing {filepath} ================")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    page_pos = content.find('id="page-eservice-ekyc"')
    if page_pos == -1:
        print("ERROR: id=\"page-eservice-ekyc\" not found!")
        return

    # 1. Add TOP_DASHBOARD_EKYC right before the first article (id="eservice-ekyc-1")
    target_sec1 = '<!-- 1. Phân loại Kênh Mở & Kích hoạt TKGDCK (App / Web) -->'
    if "<!-- DASHBOARD TRỰC QUAN MỞ TKGDCK QUA EKYC" not in content:
        pos_sec1 = content.find(target_sec1, page_pos)
        if pos_sec1 == -1:
            pos_sec1 = content.find('id="eservice-ekyc-1"', page_pos)
            # find previous line
            pos_sec1 = content.rfind('<article', page_pos, pos_sec1)
        if pos_sec1 != -1:
            content = content[:pos_sec1] + TOP_DASHBOARD_EKYC + '\n\n              ' + content[pos_sec1:]
            print("Added TOP_DASHBOARD_EKYC successfully.")

    # 2. Add chart to each section's formula-right
    chart_map = [
        ('eservice-ekyc-1', SVG_EKYC_1),
        ('eservice-ekyc-2', SVG_EKYC_2),
        ('eservice-ekyc-3', SVG_EKYC_3),
        ('eservice-ekyc-4', SVG_EKYC_4),
    ]

    for sec_id, chart_html in chart_map:
        sec_pos = content.find(f'id="{sec_id}"', page_pos)
        if sec_pos == -1:
            print(f"Cannot find {sec_id}")
            continue

        fr_pos = content.find('<div class="formula-right">', sec_pos)
        details_pos = content.find('<details class="example-details"', fr_pos)

        # Check if already added
        existing_check = content[fr_pos:details_pos]
        if 'visual-chart-svg' in existing_check:
            print(f"Chart already in {sec_id}")
            continue

        insert_point = details_pos
        content = content[:insert_point] + chart_html + '\n                  ' + content[insert_point:]
        print(f"Added chart to {sec_id} formula-right successfully.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath} successfully.")

update_ekyc_page('index.html')
update_ekyc_page('BAO_CAO_CONG_THUC_TINH_TOAN_POWERBI.html')
