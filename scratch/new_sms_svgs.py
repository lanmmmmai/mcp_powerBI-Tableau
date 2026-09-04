# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Redesigned SVGs for SMS reconciliation report with crystal clear fonts and high contrast

NEW_SVG_1 = '''<svg class="visual-chart-svg" viewBox="0 0 370 110" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- KPI Card 1: Total Messages -->
                        <rect x="12" y="10" width="112" height="90" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2" />
                        <text x="68" y="28" text-anchor="middle" font-size="9.5" fill="#475569" font-weight="700">Tổng Tin Nhắn</text>
                        <text x="68" y="58" text-anchor="middle" font-size="20" fill="#0f172a" font-weight="800">2.781</text>
                        <rect x="25" y="70" width="86" height="18" rx="9" fill="#e0f2fe" />
                        <text x="68" y="82.5" text-anchor="middle" font-size="8.5" fill="#0369a1" font-weight="700">100% Phát sinh</text>

                        <!-- KPI Card 2: Total Success Messages -->
                        <rect x="132" y="10" width="112" height="90" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2" />
                        <text x="188" y="28" text-anchor="middle" font-size="9.5" fill="#166534" font-weight="700">Gửi Thành Công</text>
                        <text x="188" y="58" text-anchor="middle" font-size="20" fill="#059669" font-weight="800">2.277</text>
                        <rect x="145" y="70" width="86" height="18" rx="9" fill="#dcfce7" />
                        <text x="188" y="82.5" text-anchor="middle" font-size="8.5" fill="#15803d" font-weight="700">81,88% Đạt chuẩn</text>

                        <!-- Donut Chart: Percentage of Status -->
                        <circle cx="305" cy="50" r="32" fill="none" stroke="#f1f5f9" stroke-width="12" />
                        <!-- Success Arc (81.88% of 201px circumference) -->
                        <circle cx="305" cy="50" r="32" fill="none" stroke="#4f46e5" stroke-width="12" stroke-dasharray="201" stroke-dashoffset="36" transform="rotate(-90 305 50)" />
                        <!-- Fail Arc (18.12%) -->
                        <circle cx="305" cy="50" r="32" fill="none" stroke="#ef4444" stroke-width="12" stroke-dasharray="201" stroke-dashoffset="165" transform="rotate(205 305 50)" />

                        <text x="305" y="47" text-anchor="middle" font-size="8.5" fill="#64748b" font-weight="600">Thành công</text>
                        <text x="305" y="60" text-anchor="middle" font-size="11" fill="#0f172a" font-weight="800">81,9%</text>

                        <!-- Legend below donut -->
                        <rect x="256" y="88" width="8" height="8" rx="2" fill="#4f46e5" />
                        <text x="268" y="95" font-size="8.5" fill="#1e293b" font-weight="700">2.277 (81,9%)</text>
                        <rect x="320" y="88" width="8" height="8" rx="2" fill="#ef4444" />
                        <text x="332" y="95" font-size="8.5" fill="#b91c1c" font-weight="700">504 (18,1%)</text>
                      </svg>'''

NEW_SVG_2 = '''<svg class="visual-chart-svg" viewBox="0 0 370 122" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Pie / Donut Visual for Service Provider -->
                        <!-- V2M: 69.43% (250 deg), VNPAY: 30.57% (110 deg) -->
                        <!-- Base circle: V2M in Indigo -->
                        <circle cx="92" cy="61" r="46" fill="#4f46e5" />
                        <!-- VNPAY slice: 110 deg from top (angle -90 to +20 deg) -->
                        <path d="M 92 61 L 92 15 A 46 46 0 0 1 135 77 Z" fill="#ec4899" stroke="#ffffff" stroke-width="1.5" />

                        <!-- Inner Hole for Donut -->
                        <circle cx="92" cy="61" r="22" fill="#ffffff" />
                        <text x="92" y="58" text-anchor="middle" font-size="8" fill="#64748b" font-weight="600">Tổng</text>
                        <text x="92" y="70" text-anchor="middle" font-size="9.5" fill="#0f172a" font-weight="800">2.781</text>

                        <!-- Value labels directly on sectors with high contrast -->
                        <!-- V2M Value Label -->
                        <text x="65" y="60" text-anchor="middle" font-size="12" fill="#ffffff" font-weight="800">1.931</text>
                        <text x="65" y="72" text-anchor="middle" font-size="9" fill="#e0e7ff" font-weight="700">69,4%</text>

                        <!-- VNPAY Value Label -->
                        <text x="120" y="44" text-anchor="middle" font-size="11.5" fill="#ffffff" font-weight="800">850</text>
                        <text x="120" y="55" text-anchor="middle" font-size="8.5" fill="#fce7f3" font-weight="700">30,6%</text>

                        <!-- Breakdown Legend / Details on the Right -->
                        <rect x="175" y="16" width="185" height="38" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
                        <rect x="183" y="25" width="12" height="12" rx="3" fill="#4f46e5" />
                        <text x="202" y="32" font-size="10.5" fill="#0f172a" font-weight="700">Đối tác V2M (Chính):</text>
                        <text x="202" y="46" font-size="11.5" fill="#4338ca" font-weight="800">1.931 tin (69,43%)</text>

                        <rect x="175" y="62" width="185" height="38" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
                        <rect x="183" y="71" width="12" height="12" rx="3" fill="#ec4899" />
                        <text x="202" y="78" font-size="10.5" fill="#0f172a" font-weight="700">Đối tác VNPAY:</text>
                        <text x="202" y="92" font-size="11.5" fill="#be185d" font-weight="800">850 tin (30,57%)</text>

                        <text x="175" y="114" font-size="8.5" fill="#64748b" font-weight="600">* Định tuyến tự động theo chi phí &amp; chất lượng gateway</text>
                      </svg>'''

NEW_SVG_3 = '''<svg class="visual-chart-svg" viewBox="0 0 370 126" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Pie Donut for Telco Operator (ĐỐI SOÁT NHÀ MẠNG) -->
                        <!-- Center cx=85, cy=63, r=48 -->
                        <!-- 1. Unidentified slice (1.405 - 50.52%): Right half circle from top to bottom -->
                        <path d="M 85 63 L 85 15 A 48 48 0 0 1 85 111 Z" fill="#4f46e5" stroke="#ffffff" stroke-width="1.5" />
                        <!-- 2. Viettel slice (887 - 31.90%): Bottom-left sector from 85,111 to 43,40 -->
                        <path d="M 85 63 L 85 111 A 48 48 0 0 1 43 40 Z" fill="#ec4899" stroke="#ffffff" stroke-width="1.5" />
                        <!-- 3. Vinaphone slice (288 - 10.36%): Top-left thin sector from 43,40 to 85,15 -->
                        <path d="M 85 63 L 43 40 A 48 48 0 0 1 85 15 Z" fill="#fbcfe8" stroke="#ffffff" stroke-width="1.5" />

                        <!-- Data Labels on Slices (High Contrast & Large Font) -->
                        <!-- 1.405 (Không xác định) -->
                        <text x="110" y="60" text-anchor="middle" font-size="13" fill="#ffffff" font-weight="800">1.405</text>
                        <text x="110" y="73" text-anchor="middle" font-size="9" fill="#e0e7ff" font-weight="700">50,5%</text>

                        <!-- 887 (Viettel) -->
                        <text x="62" y="80" text-anchor="middle" font-size="12.5" fill="#ffffff" font-weight="800">887</text>
                        <text x="62" y="93" text-anchor="middle" font-size="9" fill="#fce7f3" font-weight="700">31,9%</text>

                        <!-- 288 (Vinaphone) - Pointer Callout Line outside thin slice so it never clips -->
                        <circle cx="65" cy="36" r="2.5" fill="#9d174d" />
                        <polyline points="65,36 44,22 18,22" stroke="#9d174d" stroke-width="1.5" fill="none" stroke-linecap="round" />
                        <rect x="4" y="6" width="46" height="22" rx="3" fill="#ffffff" stroke="#f472b6" stroke-width="1" />
                        <text x="27" y="16" text-anchor="middle" font-size="10" font-weight="800" fill="#9d174d">288</text>
                        <text x="27" y="25" text-anchor="middle" font-size="7.5" font-weight="700" fill="#be185d">10,4%</text>

                        <!-- Legend / Details on the Right -->
                        <rect x="175" y="12" width="185" height="28" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
                        <rect x="183" y="20" width="12" height="12" rx="3" fill="#4f46e5" />
                        <text x="202" y="27" font-size="10" fill="#0f172a" font-weight="700">Không xác định:</text>
                        <text x="350" y="27" font-size="11" fill="#4338ca" font-weight="800" text-anchor="end">1.405 (50,5%)</text>

                        <rect x="175" y="44" width="185" height="28" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
                        <rect x="183" y="52" width="12" height="12" rx="3" fill="#ec4899" />
                        <text x="202" y="59" font-size="10" fill="#0f172a" font-weight="700">Viettel:</text>
                        <text x="350" y="59" font-size="11" fill="#be185d" font-weight="800" text-anchor="end">887 (31,9%)</text>

                        <rect x="175" y="76" width="185" height="28" rx="4" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
                        <rect x="183" y="84" width="12" height="12" rx="3" fill="#fbcfe8" stroke="#be185d" stroke-width="1.5" />
                        <text x="202" y="91" font-size="10" fill="#0f172a" font-weight="700">Vinaphone:</text>
                        <text x="350" y="91" font-size="11" fill="#9d174d" font-weight="800" text-anchor="end">288 (10,4%)</text>

                        <!-- Total note -->
                        <text x="175" y="118" font-size="8.5" fill="#64748b" font-weight="600">Tổng cộng: <tspan fill="#0f172a" font-weight="800">2.781 tin</tspan> (Khớp 100% RECON_013)</text>
                      </svg>'''

NEW_SVG_4 = '''<svg class="visual-chart-svg" viewBox="0 0 370 100" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Tier 1: Lỗi Thuê bao / Số ĐT -->
                        <text x="15" y="17" font-size="9" fill="#0f172a" font-weight="700">Thuê bao không hợp lệ / Chặn SMS (005, 01)</text>
                        <text x="355" y="17" text-anchor="end" font-size="10.5" fill="#dc2626" font-weight="800">280 tin (55,5%)</text>
                        <rect x="15" y="22" width="340" height="11" rx="3" fill="#ef4444" />

                        <!-- Tier 2: Lỗi Template / Nội dung -->
                        <text x="15" y="50" font-size="9" fill="#0f172a" font-weight="700">Sai định dạng Template / Biến số (011, 010)</text>
                        <text x="355" y="50" text-anchor="end" font-size="10.5" fill="#d97706" font-weight="800">140 tin (27,8%)</text>
                        <rect x="15" y="55" width="170" height="11" rx="3" fill="#f59e0b" />

                        <!-- Tier 3: Lỗi Timeout Gateway -->
                        <text x="15" y="82" font-size="9" fill="#0f172a" font-weight="700">Gateway Timeout / Mất kết nối Nhà mạng (08, 05)</text>
                        <text x="355" y="82" text-anchor="end" font-size="10.5" fill="#4338ca" font-weight="800">84 tin (16,7%)</text>
                        <rect x="15" y="87" width="102" height="11" rx="3" fill="#6366f1" />
                      </svg>'''

NEW_SVG_5 = '''<svg class="visual-chart-svg" viewBox="0 0 370 125" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
                        <!-- Y-axis Label -->
                        <text x="15" y="12" font-size="8" fill="#64748b" font-weight="600">Sản lượng tin nhắn (Count of messageid)</text>

                        <!-- Grid lines -->
                        <line x1="25" y1="28" x2="355" y2="28" stroke="#e2e8f0" stroke-dasharray="2,2" />
                        <line x1="25" y1="58" x2="355" y2="58" stroke="#e2e8f0" stroke-dasharray="2,2" />
                        <line x1="25" y1="88" x2="355" y2="88" stroke="#cbd5e1" />

                        <text x="20" y="31" text-anchor="end" font-size="7.5" fill="#64748b">1.000</text>
                        <text x="20" y="61" text-anchor="end" font-size="7.5" fill="#64748b">500</text>
                        <text x="20" y="91" text-anchor="end" font-size="7.5" fill="#64748b">0</text>

                        <!-- Bars -->
                        <!-- 1/2024 (1.341) - Dark Plum -->
                        <rect x="35" y="18" width="24" height="70" rx="2" fill="#581c87" />
                        <text x="47" y="14" text-anchor="middle" font-size="9" fill="#581c87" font-weight="800">1.341</text>
                        <text x="47" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">1/24</text>

                        <!-- 2/2024 (428) -->
                        <rect x="70" y="58" width="24" height="30" rx="2" fill="#c084fc" />
                        <text x="82" y="54" text-anchor="middle" font-size="9" fill="#6b21a8" font-weight="800">428</text>
                        <text x="82" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">2/24</text>

                        <!-- 3/2024 (53) -->
                        <rect x="105" y="84" width="24" height="4" rx="1" fill="#f472b6" />
                        <text x="117" y="80" text-anchor="middle" font-size="8.5" fill="#9d174d" font-weight="800">53</text>
                        <text x="117" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">3/24</text>

                        <!-- 4/2024 (376) -->
                        <rect x="140" y="62" width="24" height="26" rx="2" fill="#c084fc" />
                        <text x="152" y="58" text-anchor="middle" font-size="9" fill="#6b21a8" font-weight="800">376</text>
                        <text x="152" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">4/24</text>

                        <!-- 5/2024 (199) -->
                        <rect x="175" y="74" width="24" height="14" rx="2" fill="#f472b6" />
                        <text x="187" y="70" text-anchor="middle" font-size="8.5" fill="#9d174d" font-weight="800">199</text>
                        <text x="187" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">5/24</text>

                        <!-- 6/2024 (41) -->
                        <rect x="210" y="85" width="24" height="3" rx="1" fill="#f472b6" />
                        <text x="222" y="81" text-anchor="middle" font-size="8.5" fill="#9d174d" font-weight="800">41</text>
                        <text x="222" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">6/24</text>

                        <!-- 7/2024 (91) -->
                        <rect x="245" y="82" width="24" height="6" rx="1" fill="#f472b6" />
                        <text x="257" y="78" text-anchor="middle" font-size="8.5" fill="#9d174d" font-weight="800">91</text>
                        <text x="257" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">7/24</text>

                        <!-- 8/2024 (160) -->
                        <rect x="280" y="77" width="24" height="11" rx="2" fill="#f472b6" />
                        <text x="292" y="73" text-anchor="middle" font-size="8.5" fill="#9d174d" font-weight="800">160</text>
                        <text x="292" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">8/24</text>

                        <!-- 9/2024 (92) -->
                        <rect x="315" y="82" width="24" height="6" rx="1" fill="#f472b6" />
                        <text x="327" y="78" text-anchor="middle" font-size="8.5" fill="#9d174d" font-weight="800">92</text>
                        <text x="327" y="103" text-anchor="middle" font-size="8" fill="#1e293b" font-weight="700">9/24</text>
                      </svg>'''

print("New SVGs prepared successfully.")
