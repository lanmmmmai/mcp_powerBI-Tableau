# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Perfected SVGs with adjusted font sizes and 2-line legend layout to prevent any collision or overflow

PERFECT_SVG_1 = '''<svg class="visual-chart-svg" viewBox="0 0 380 110" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- KPI Card 1: Total Messages -->
                        <rect x="12" y="10" width="115" height="90" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" />
                        <text x="69" y="28" text-anchor="middle" font-size="9" fill="#475569" font-weight="700">Tổng Tin Nhắn</text>
                        <text x="69" y="56" text-anchor="middle" font-size="16" fill="#0f172a" font-weight="800">2.781</text>
                        <rect x="26" y="68" width="86" height="18" rx="9" fill="#e0f2fe" />
                        <text x="69" y="80.5" text-anchor="middle" font-size="8" fill="#0369a1" font-weight="700">100% Phát sinh</text>

                        <!-- KPI Card 2: Total Success Messages -->
                        <rect x="135" y="10" width="115" height="90" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2" />
                        <text x="192" y="28" text-anchor="middle" font-size="9" fill="#166534" font-weight="700">Gửi Thành Công</text>
                        <text x="192" y="56" text-anchor="middle" font-size="16" fill="#059669" font-weight="800">2.277</text>
                        <rect x="149" y="68" width="86" height="18" rx="9" fill="#dcfce7" />
                        <text x="192" y="80.5" text-anchor="middle" font-size="8" fill="#15803d" font-weight="700">81,88% Đạt chuẩn</text>

                        <!-- Donut Chart: Percentage of Status -->
                        <circle cx="312" cy="48" r="30" fill="none" stroke="#f1f5f9" stroke-width="10" />
                        <!-- Success Arc (81.88% of 188px circumference) -->
                        <circle cx="312" cy="48" r="30" fill="none" stroke="#4f46e5" stroke-width="10" stroke-dasharray="188" stroke-dashoffset="34" transform="rotate(-90 312 48)" />
                        <!-- Fail Arc (18.12%) -->
                        <circle cx="312" cy="48" r="30" fill="none" stroke="#ef4444" stroke-width="10" stroke-dasharray="188" stroke-dashoffset="154" transform="rotate(205 312 48)" />

                        <text x="312" y="45" text-anchor="middle" font-size="8" fill="#64748b" font-weight="600">Thành công</text>
                        <text x="312" y="57" text-anchor="middle" font-size="10" fill="#0f172a" font-weight="800">81,9%</text>

                        <!-- Legend below donut -->
                        <rect x="260" y="88" width="7" height="7" rx="2" fill="#4f46e5" />
                        <text x="270" y="94.5" font-size="7.5" fill="#1e293b" font-weight="700">2.277 (81,9%)</text>
                        <rect x="325" y="88" width="7" height="7" rx="2" fill="#ef4444" />
                        <text x="335" y="94.5" font-size="7.5" fill="#b91c1c" font-weight="700">504 (18,1%)</text>
                      </svg>'''

PERFECT_SVG_2 = '''<svg class="visual-chart-svg" viewBox="0 0 380 124" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Pie Visual for Service Provider (Solid Pie - No inner hole collision) -->
                        <!-- Center cx=85, cy=62, r=48 -->
                        <!-- V2M (69.43% - 1.931): Base Circle Indigo -->
                        <circle cx="85" cy="62" r="48" fill="#4f46e5" />
                        <!-- VNPAY (30.57% - 850): Slice from top 85,14 to 129,82 -->
                        <path d="M 85 62 L 85 14 A 48 48 0 0 1 129 82 Z" fill="#ec4899" stroke="#ffffff" stroke-width="1.5" />

                        <!-- Value labels directly on sectors with comfortable size -->
                        <!-- V2M Value Label -->
                        <text x="60" y="60" text-anchor="middle" font-size="10.5" fill="#ffffff" font-weight="800">1.931</text>
                        <text x="60" y="72" text-anchor="middle" font-size="8" fill="#e0e7ff" font-weight="700">69,4%</text>

                        <!-- VNPAY Value Label -->
                        <text x="115" y="48" text-anchor="middle" font-size="10" fill="#ffffff" font-weight="800">850</text>
                        <text x="115" y="59" text-anchor="middle" font-size="8" fill="#fce7f3" font-weight="700">30,6%</text>

                        <!-- Breakdown Legend / Details on the Right (2-line layout: Never overlaps) -->
                        <rect x="175" y="14" width="195" height="38" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
                        <rect x="183" y="24" width="10" height="10" rx="2" fill="#4f46e5" />
                        <text x="198" y="27" font-size="8.5" fill="#475569" font-weight="600">Đối tác V2M (Chính)</text>
                        <text x="198" y="42" font-size="11" fill="#4338ca" font-weight="800">1.931 tin <tspan font-size="8.5" fill="#6366f1" font-weight="600">(69,43%)</tspan></text>

                        <rect x="175" y="58" width="195" height="38" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
                        <rect x="183" y="68" width="10" height="10" rx="2" fill="#ec4899" />
                        <text x="198" y="71" font-size="8.5" fill="#475569" font-weight="600">Đối tác VNPAY</text>
                        <text x="198" y="86" font-size="11" fill="#be185d" font-weight="800">850 tin <tspan font-size="8.5" fill="#ec4899" font-weight="600">(30,57%)</tspan></text>

                        <text x="175" y="112" font-size="8" fill="#64748b" font-weight="600">* Định tuyến tự động theo chi phí &amp; chất lượng gateway</text>
                      </svg>'''

PERFECT_SVG_3 = '''<svg class="visual-chart-svg" viewBox="0 0 380 126" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Pie for Telco Operator (ĐỐI SOÁT NHÀ MẠNG) -->
                        <!-- Center cx=85, cy=63, r=48 -->
                        <!-- 1. Unidentified slice (1.405 - 50.52%): Right half circle from top to bottom -->
                        <path d="M 85 63 L 85 15 A 48 48 0 0 1 85 111 Z" fill="#4f46e5" stroke="#ffffff" stroke-width="1.5" />
                        <!-- 2. Viettel slice (887 - 31.90%): Bottom-left sector from 85,111 to 43,40 -->
                        <path d="M 85 63 L 85 111 A 48 48 0 0 1 43 40 Z" fill="#ec4899" stroke="#ffffff" stroke-width="1.5" />
                        <!-- 3. Vinaphone slice (288 - 10.36%): Top-left thin sector from 43,40 to 85,15 -->
                        <path d="M 85 63 L 43 40 A 48 48 0 0 1 85 15 Z" fill="#fbcfe8" stroke="#ffffff" stroke-width="1.5" />

                        <!-- Data Labels on Slices (Properly Sized & Contained) -->
                        <!-- 1.405 (Không xác định) -->
                        <text x="110" y="59" text-anchor="middle" font-size="10.5" fill="#ffffff" font-weight="800">1.405</text>
                        <text x="110" y="71" text-anchor="middle" font-size="8" fill="#e0e7ff" font-weight="700">50,5%</text>

                        <!-- 887 (Viettel) -->
                        <text x="62" y="79" text-anchor="middle" font-size="10" fill="#ffffff" font-weight="800">887</text>
                        <text x="62" y="90" text-anchor="middle" font-size="8" fill="#fce7f3" font-weight="700">31,9%</text>

                        <!-- 288 (Vinaphone) - Pointer Callout Line outside thin slice so it never clips -->
                        <circle cx="65" cy="36" r="2.5" fill="#9d174d" />
                        <polyline points="65,36 44,22 20,22" stroke="#9d174d" stroke-width="1.2" fill="none" stroke-linecap="round" />
                        <rect x="6" y="8" width="42" height="19" rx="3" fill="#ffffff" stroke="#f472b6" stroke-width="1" />
                        <text x="27" y="17" text-anchor="middle" font-size="9" font-weight="800" fill="#9d174d">288</text>
                        <text x="27" y="24.5" text-anchor="middle" font-size="6.5" font-weight="700" fill="#be185d">10,4%</text>

                        <!-- Legend / Details on the Right (2-Line layout: Zero Overlap) -->
                        <rect x="175" y="10" width="195" height="30" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
                        <rect x="183" y="18" width="10" height="10" rx="2" fill="#4f46e5" />
                        <text x="198" y="22" font-size="8.5" fill="#475569" font-weight="600">Không xác định</text>
                        <text x="198" y="34" font-size="10.5" fill="#4338ca" font-weight="800">1.405 tin <tspan font-size="8.5" fill="#6366f1" font-weight="600">(50,5%)</tspan></text>

                        <rect x="175" y="44" width="195" height="30" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
                        <rect x="183" y="52" width="10" height="10" rx="2" fill="#ec4899" />
                        <text x="198" y="56" font-size="8.5" fill="#475569" font-weight="600">Viettel</text>
                        <text x="198" y="68" font-size="10.5" fill="#be185d" font-weight="800">887 tin <tspan font-size="8.5" fill="#ec4899" font-weight="600">(31,9%)</tspan></text>

                        <rect x="175" y="78" width="195" height="30" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
                        <rect x="183" y="86" width="10" height="10" rx="2" fill="#fbcfe8" stroke="#be185d" stroke-width="1.2" />
                        <text x="198" y="90" font-size="8.5" fill="#475569" font-weight="600">Vinaphone</text>
                        <text x="198" y="102" font-size="10.5" fill="#9d174d" font-weight="800">288 tin <tspan font-size="8.5" fill="#db2777" font-weight="600">(10,4%)</tspan></text>

                        <!-- Total note -->
                        <text x="175" y="120" font-size="8" fill="#64748b" font-weight="600">Tổng cộng: <tspan fill="#0f172a" font-weight="800">2.781 tin</tspan> (Khớp 100% RECON_013)</text>
                      </svg>'''

PERFECT_SVG_4 = '''<svg class="visual-chart-svg" viewBox="0 0 380 100" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Tier 1: Lỗi Thuê bao / Số ĐT -->
                        <text x="15" y="17" font-size="8.5" fill="#0f172a" font-weight="700">Thuê bao không hợp lệ / Chặn SMS (005, 01)</text>
                        <text x="365" y="17" text-anchor="end" font-size="9.5" fill="#dc2626" font-weight="800">280 tin (55,5%)</text>
                        <rect x="15" y="22" width="350" height="10" rx="2" fill="#ef4444" />

                        <!-- Tier 2: Lỗi Template / Nội dung -->
                        <text x="15" y="50" font-size="8.5" fill="#0f172a" font-weight="700">Sai định dạng Template / Biến số (011, 010)</text>
                        <text x="365" y="50" text-anchor="end" font-size="9.5" fill="#d97706" font-weight="800">140 tin (27,8%)</text>
                        <rect x="15" y="55" width="175" height="10" rx="2" fill="#f59e0b" />

                        <!-- Tier 3: Lỗi Timeout Gateway -->
                        <text x="15" y="82" font-size="8.5" fill="#0f172a" font-weight="700">Gateway Timeout / Mất kết nối Nhà mạng (08, 05)</text>
                        <text x="365" y="82" text-anchor="end" font-size="9.5" fill="#4338ca" font-weight="800">84 tin (16,7%)</text>
                        <rect x="15" y="87" width="105" height="10" rx="2" fill="#6366f1" />
                      </svg>'''

PERFECT_SVG_5 = '''<svg class="visual-chart-svg" viewBox="0 0 380 125" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Y-axis Label -->
                        <text x="15" y="12" font-size="8" fill="#64748b" font-weight="600">Sản lượng tin nhắn (Count of messageid)</text>

                        <!-- Grid lines -->
                        <line x1="25" y1="28" x2="365" y2="28" stroke="#e2e8f0" stroke-dasharray="2,2" />
                        <line x1="25" y1="58" x2="365" y2="58" stroke="#e2e8f0" stroke-dasharray="2,2" />
                        <line x1="25" y1="88" x2="365" y2="88" stroke="#cbd5e1" />

                        <text x="20" y="31" text-anchor="end" font-size="7" fill="#64748b">1.000</text>
                        <text x="20" y="61" text-anchor="end" font-size="7" fill="#64748b">500</text>
                        <text x="20" y="91" text-anchor="end" font-size="7" fill="#64748b">0</text>

                        <!-- Bars -->
                        <!-- 1/2024 (1.341) - Dark Plum -->
                        <rect x="35" y="18" width="24" height="70" rx="2" fill="#581c87" />
                        <text x="47" y="14" text-anchor="middle" font-size="8" fill="#581c87" font-weight="800">1.341</text>
                        <text x="47" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">1/24</text>

                        <!-- 2/2024 (428) -->
                        <rect x="72" y="58" width="24" height="30" rx="2" fill="#c084fc" />
                        <text x="84" y="54" text-anchor="middle" font-size="8" fill="#6b21a8" font-weight="800">428</text>
                        <text x="84" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">2/24</text>

                        <!-- 3/2024 (53) -->
                        <rect x="109" y="84" width="24" height="4" rx="1" fill="#f472b6" />
                        <text x="121" y="80" text-anchor="middle" font-size="7.5" fill="#9d174d" font-weight="800">53</text>
                        <text x="121" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">3/24</text>

                        <!-- 4/2024 (376) -->
                        <rect x="146" y="62" width="24" height="26" rx="2" fill="#c084fc" />
                        <text x="158" y="58" text-anchor="middle" font-size="8" fill="#6b21a8" font-weight="800">376</text>
                        <text x="158" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">4/24</text>

                        <!-- 5/2024 (199) -->
                        <rect x="183" y="74" width="24" height="14" rx="2" fill="#f472b6" />
                        <text x="195" y="70" text-anchor="middle" font-size="7.5" fill="#9d174d" font-weight="800">199</text>
                        <text x="195" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">5/24</text>

                        <!-- 6/2024 (41) -->
                        <rect x="220" y="85" width="24" height="3" rx="1" fill="#f472b6" />
                        <text x="232" y="81" text-anchor="middle" font-size="7.5" fill="#9d174d" font-weight="800">41</text>
                        <text x="232" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">6/24</text>

                        <!-- 7/2024 (91) -->
                        <rect x="257" y="82" width="24" height="6" rx="1" fill="#f472b6" />
                        <text x="269" y="78" text-anchor="middle" font-size="7.5" fill="#9d174d" font-weight="800">91</text>
                        <text x="269" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">7/24</text>

                        <!-- 8/2024 (160) -->
                        <rect x="294" y="77" width="24" height="11" rx="2" fill="#f472b6" />
                        <text x="306" y="73" text-anchor="middle" font-size="7.5" fill="#9d174d" font-weight="800">160</text>
                        <text x="306" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">8/24</text>

                        <!-- 9/2024 (92) -->
                        <rect x="331" y="82" width="24" height="6" rx="1" fill="#f472b6" />
                        <text x="343" y="78" text-anchor="middle" font-size="7.5" fill="#9d174d" font-weight="800">92</text>
                        <text x="343" y="101" text-anchor="middle" font-size="7.5" fill="#1e293b" font-weight="700">9/24</text>
                      </svg>'''

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

sms_start = text.find('id="page-section-sms"')
curr = sms_start
replacements = [PERFECT_SVG_1, PERFECT_SVG_2, PERFECT_SVG_3, PERFECT_SVG_4, PERFECT_SVG_5]

for i, new_svg in enumerate(replacements, 1):
    svg_start = text.find('<svg class="visual-chart-svg"', curr)
    if svg_start == -1:
        print(f"ERROR: Cannot find SVG #{i}")
        break
    svg_end = text.find('</svg>', svg_start) + 6
    old_svg = text[svg_start:svg_end]
    print(f"Replacing SVG #{i}: {len(old_svg)} -> {len(new_svg)}")
    text = text[:svg_start] + new_svg + text[svg_end:]
    curr = svg_start + len(new_svg)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated index.html successfully with perfected SVGs!")
