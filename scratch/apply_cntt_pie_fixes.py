# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Perfected SVG #35 (Trạng thái & Mức độ ưu tiên)
PERFECT_CNTT_SVG_1 = '''<svg class="visual-chart-svg" viewBox="0 0 380 108" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Chart 1: Trạng Thái (Left) -->
                        <text x="90" y="16" text-anchor="middle" font-size="8" fill="#0f172a" font-weight="700">TRẠNG THÁI DỰ ÁN</text>
                        <!-- Pie: Done 58.82% (Blue), In Progress 41.18% (Orange) -->
                        <circle cx="90" cy="54" r="32" fill="#3b82f6" />
                        <path d="M 90 54 L 90 22 A 32 32 0 0 1 118 69 Z" fill="#f97316" stroke="#ffffff" stroke-width="1.5" />
                        <text x="74" y="58" text-anchor="middle" font-size="7.5" fill="#ffffff" font-weight="800">58,8%</text>
                        <text x="105" y="44" text-anchor="middle" font-size="7.5" fill="#ffffff" font-weight="800">41,2%</text>
                        <text x="50" y="98" font-size="6.5" fill="#1e293b" font-weight="600">Done: 10</text>
                        <text x="105" y="98" font-size="6.5" fill="#c2410c" font-weight="600">In Progress: 7</text>

                        <!-- Divider -->
                        <line x1="185" y1="10" x2="185" y2="98" stroke="#e2e8f0" />

                        <!-- Chart 2: Mức Độ Ưu Tiên (Right) -->
                        <text x="280" y="16" text-anchor="middle" font-size="8" fill="#0f172a" font-weight="700">MỨC ĐỘ ƯU TIÊN</text>
                        <!-- Pie: High 82.35% (Blue), Medium 17.65% (Orange) -->
                        <circle cx="280" cy="54" r="32" fill="#3b82f6" />
                        <path d="M 280 54 L 280 22 A 32 32 0 0 1 308 40 Z" fill="#f97316" stroke="#ffffff" stroke-width="1.5" />
                        <text x="268" y="58" text-anchor="middle" font-size="7.5" fill="#ffffff" font-weight="800">82,4%</text>
                        <text x="297" y="32" text-anchor="middle" font-size="7" fill="#ffffff" font-weight="800">17,6%</text>
                        <text x="240" y="98" font-size="6.5" fill="#1e293b" font-weight="600">High: 14</text>
                        <text x="295" y="98" font-size="6.5" fill="#c2410c" font-weight="600">Medium: 3</text>
                      </svg>'''

# Perfected SVG #36 (Loại dự án & Bộ phận phụ trách)
PERFECT_CNTT_SVG_2 = '''<svg class="visual-chart-svg" viewBox="0 0 380 110" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Left: Project Type Donut/Pie -->
                        <text x="80" y="16" text-anchor="middle" font-size="8" fill="#0f172a" font-weight="700">LOẠI DỰ ÁN</text>
                        <!-- Center cx=80, cy=58, r=34 -->
                        <!-- 1. Tư vấn số (41.2% - Left Half, angle 90° to 270°) -->
                        <path d="M 80 58 L 80 24 A 34 34 0 0 0 80 92 Z" fill="#ef4444" stroke="#ffffff" stroke-width="1.5" />
                        <!-- 2. Core Flex (35.3% - Top Right Quadrant, angle -90° to 0°) -->
                        <path d="M 80 58 L 80 24 A 34 34 0 0 1 114 58 Z" fill="#3b82f6" stroke="#ffffff" stroke-width="1.5" />
                        <!-- 3. Tài chính số (23.5% - Bottom Right Quadrant, angle 0° to 90°) -->
                        <path d="M 80 58 L 114 58 A 34 34 0 0 1 80 92 Z" fill="#f59e0b" stroke="#ffffff" stroke-width="1.5" />
                        
                        <!-- Value labels centered with text-anchor="middle" strictly inside each sector -->
                        <text x="60" y="61" text-anchor="middle" font-size="7.5" fill="#ffffff" font-weight="800">41,2%</text>
                        <text x="95" y="46" text-anchor="middle" font-size="7.5" fill="#ffffff" font-weight="800">35,3%</text>
                        <text x="95" y="73" text-anchor="middle" font-size="7.5" fill="#ffffff" font-weight="800">23,5%</text>

                        <!-- Legend below pie -->
                        <text x="42" y="102" font-size="6.5" fill="#ef4444" font-weight="700">■ TVS</text>
                        <text x="76" y="102" font-size="6.5" fill="#3b82f6" font-weight="700">■ CoreFlex</text>
                        <text x="120" y="102" font-size="6.5" fill="#d97706" font-weight="700">■ TCS</text>

                        <!-- Right: Column Chart Bộ phận phụ trách -->
                        <text x="270" y="16" text-anchor="middle" font-size="8" fill="#0f172a" font-weight="700">BỘ PHẬN PHỤ TRÁCH</text>
                        <line x1="175" y1="85" x2="368" y2="85" stroke="#cbd5e1" />

                        <!-- Bars -->
                        <rect x="180" y="65" width="22" height="20" rx="2" fill="#f97316" />
                        <text x="191" y="60" text-anchor="middle" font-size="7" fill="#0f172a" font-weight="800">1</text>
                        <text x="191" y="96" text-anchor="middle" font-size="6" fill="#64748b">FSS</text>

                        <rect x="212" y="65" width="22" height="20" rx="2" fill="#ef4444" />
                        <text x="223" y="60" text-anchor="middle" font-size="7" fill="#0f172a" font-weight="800">1</text>
                        <text x="223" y="96" text-anchor="middle" font-size="6" fill="#64748b">FTL</text>

                        <rect x="244" y="65" width="22" height="20" rx="2" fill="#10b981" />
                        <text x="255" y="60" text-anchor="middle" font-size="7" fill="#0f172a" font-weight="800">1</text>
                        <text x="255" y="96" text-anchor="middle" font-size="6" fill="#64748b">FTL+MKT</text>

                        <!-- IT Bar (3) -->
                        <rect x="276" y="25" width="22" height="60" rx="2" fill="#06b6d4" />
                        <text x="287" y="20" text-anchor="middle" font-size="8" fill="#0891b2" font-weight="800">3</text>
                        <text x="287" y="96" text-anchor="middle" font-size="6.5" fill="#0f172a" font-weight="800">IT</text>

                        <rect x="308" y="65" width="22" height="20" rx="2" fill="#eab308" />
                        <text x="319" y="60" text-anchor="middle" font-size="7" fill="#0f172a" font-weight="800">1</text>
                        <text x="319" y="96" text-anchor="middle" font-size="6" fill="#64748b">IT+FSS</text>

                        <rect x="340" y="65" width="22" height="20" rx="2" fill="#a855f7" />
                        <text x="351" y="60" text-anchor="middle" font-size="7" fill="#0f172a" font-weight="800">1</text>
                        <text x="351" y="96" text-anchor="middle" font-size="5.5" fill="#64748b">IT+MKT</text>
                      </svg>'''

def update_cntt_svgs(filepath):
    print(f"Updating {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find section-cntt-1
    pos1 = content.find('id="section-cntt-1-tab-math"')
    if pos1 != -1:
        s1 = content.find('<svg class="visual-chart-svg"', pos1)
        e1 = content.find('</svg>', s1) + 6
        old_s1 = content[s1:e1]
        content = content[:s1] + PERFECT_CNTT_SVG_1 + content[e1:]
        print(f"Replaced CNTT SVG 1: {len(old_s1)} -> {len(PERFECT_CNTT_SVG_1)}")

    # Find section-cntt-2
    pos2 = content.find('id="section-cntt-2-tab-math"')
    if pos2 != -1:
        s2 = content.find('<svg class="visual-chart-svg"', pos2)
        e2 = content.find('</svg>', s2) + 6
        old_s2 = content[s2:e2]
        content = content[:s2] + PERFECT_CNTT_SVG_2 + content[e2:]
        print(f"Replaced CNTT SVG 2: {len(old_s2)} -> {len(PERFECT_CNTT_SVG_2)}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath} successfully.")

update_cntt_svgs('index.html')
update_cntt_svgs('BAO_CAO_CONG_THUC_TINH_TOAN_POWERBI.html')
