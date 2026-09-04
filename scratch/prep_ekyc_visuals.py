# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Biểu đồ Mục 1: Kênh Mở & Kích Hoạt (Web vs App)
SVG_EKYC_1 = '''<div class="visual-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
  <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
    <span>Cơ Cấu Kênh Mở TKGDCK (Web vs App)</span>
    <span style="font-size: 0.68rem; color: #00bf5f; font-weight: 700;">mart_mkt tracking</span>
  </div>
  <svg class="visual-chart-svg" viewBox="0 0 380 120" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
    <!-- Pie Chart (Web 78.5% in Teal, App 21.5% in Indigo) -->
    <!-- Center cx=85, cy=60, r=46 -->
    <!-- Web slice: 78.5% (282.6 deg) from -90 deg to 192.6 deg -->
    <circle cx="85" cy="60" r="46" fill="#0d9488" />
    <!-- App slice: 21.5% (77.4 deg) from top 85,14 to 129,48 -->
    <path d="M 85 60 L 85 14 A 46 46 0 0 1 130 49 Z" fill="#6366f1" stroke="#ffffff" stroke-width="1.5" />

    <!-- Data Labels on Sectors -->
    <text x="65" y="66" text-anchor="middle" font-size="10.5" fill="#ffffff" font-weight="800">78,5%</text>
    <text x="65" y="77" text-anchor="middle" font-size="7.5" fill="#ccfbf1" font-weight="700">Kênh Web</text>

    <text x="112" y="32" text-anchor="middle" font-size="9.5" fill="#ffffff" font-weight="800">21,5%</text>
    <text x="112" y="42" text-anchor="middle" font-size="7" fill="#e0e7ff" font-weight="700">Mobile App</text>

    <!-- Legend & Breakdown on the Right (2-line layout) -->
    <rect x="165" y="12" width="205" height="38" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
    <rect x="173" y="22" width="10" height="10" rx="2" fill="#0d9488" />
    <text x="189" y="26" font-size="8.5" fill="#475569" font-weight="600">Kênh Mở Web (Online 9999):</text>
    <text x="189" y="40" font-size="11" fill="#0f766e" font-weight="800">14.485 hồ sơ <tspan font-size="8.5" fill="#0d9488" font-weight="600">(78,5%)</tspan></text>

    <rect x="165" y="56" width="205" height="38" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
    <rect x="173" y="66" width="10" height="10" rx="2" fill="#6366f1" />
    <text x="189" y="70" font-size="8.5" fill="#475569" font-weight="600">Kênh Mở Mobile App DSC:</text>
    <text x="189" y="84" font-size="11" fill="#4338ca" font-weight="800">3.967 hồ sơ <tspan font-size="8.5" fill="#6366f1" font-weight="600">(21,5%)</tspan></text>

    <text x="165" y="110" font-size="8" fill="#64748b" font-weight="600">Tỷ lệ kích hoạt: Web 81,8% | App 84,6% (App có tỷ lệ cao hơn +2,8%)</text>
  </svg>
</div>'''

# Biểu đồ Mục 2: Cơ Cấu Trạng Thái Hồ Sơ eKYC
SVG_EKYC_2 = '''<div class="visual-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
  <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
    <span>Phân Bổ Trạng Thái Hồ Sơ eKYC</span>
    <span style="font-size: 0.68rem; color: #10b981; font-weight: 700;">82,4% Thành Công</span>
  </div>
  <svg class="visual-chart-svg" viewBox="0 0 380 120" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
    <!-- Horizontal Status Bars -->
    <!-- Status 1: Kích hoạt thành công / Hoạt động -->
    <text x="15" y="16" font-size="8.5" fill="#0f172a" font-weight="700">Kích hoạt thành công / Hoạt động</text>
    <text x="365" y="16" text-anchor="end" font-size="9.5" fill="#059669" font-weight="800">15.204 TK (82,4%)</text>
    <rect x="15" y="20" width="350" height="10" rx="3" fill="#10b981" />

    <!-- Status 2: Đã đăng ký (Chờ hoàn tất xác thực) -->
    <text x="15" y="44" font-size="8.5" fill="#0f172a" font-weight="700">Đã đăng ký (Chờ kích hoạt / OTP)</text>
    <text x="365" y="44" text-anchor="end" font-size="9.5" fill="#2563eb" font-weight="800">1.840 hồ sơ (10,0%)</text>
    <rect x="15" y="48" width="120" height="10" rx="3" fill="#3b82f6" />

    <!-- Status 3: Từ chối eKYC (OCR mờ / Liveness lỗi) -->
    <text x="15" y="72" font-size="8.5" fill="#0f172a" font-weight="700">Từ chối eKYC (OCR / Giấy tờ không hợp lệ)</text>
    <text x="365" y="72" text-anchor="end" font-size="9.5" fill="#dc2626" font-weight="800">920 hồ sơ (5,0%)</text>
    <rect x="15" y="76" width="60" height="10" rx="3" fill="#ef4444" />

    <!-- Status 4: Cần xác minh thủ công (Manual Review) -->
    <text x="15" y="100" font-size="8.5" fill="#0f172a" font-weight="700">Cần xác minh thủ công / Đối chiếu C06</text>
    <text x="365" y="100" text-anchor="end" font-size="9.5" fill="#d97706" font-weight="800">488 hồ sơ (2,6%)</text>
    <rect x="15" y="104" width="35" height="8" rx="3" fill="#f59e0b" />
  </svg>
</div>'''

# Biểu đồ Mục 3: Phễu Hành Trình Mở TKGDCK (eKYC Journey Funnel)
SVG_EKYC_3 = '''<div class="visual-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
  <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
    <span>Phễu Chuyển Đổi Hành Trình eKYC (Step Format B01 &rarr; B04)</span>
    <span style="font-size: 0.68rem; color: #2563eb; font-weight: 700;">Conversion Funnel</span>
  </div>
  <svg class="visual-chart-svg" viewBox="0 0 380 126" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
    <!-- Step B01: Điền thông tin -->
    <rect x="15" y="10" width="350" height="22" rx="4" fill="#eff6ff" stroke="#bfdbfe" />
    <rect x="15" y="10" width="350" height="22" rx="4" fill="#3b82f6" opacity="0.9" />
    <text x="25" y="24" font-size="9" fill="#ffffff" font-weight="700">B01 - Điền thông tin cá nhân &amp; SĐT/Email</text>
    <text x="355" y="24" text-anchor="end" font-size="9.5" fill="#ffffff" font-weight="800">18.452 KH (100%)</text>

    <!-- Step B02: Chụp CCCD / OCR -->
    <rect x="35" y="38" width="310" height="22" rx="4" fill="#e0f2fe" stroke="#7dd3fc" />
    <rect x="35" y="38" width="310" height="22" rx="4" fill="#0284c7" opacity="0.9" />
    <text x="45" y="52" font-size="9" fill="#ffffff" font-weight="700">B02 - Chụp ảnh 2 mặt CCCD &amp; OCR dữ liệu</text>
    <text x="335" y="52" text-anchor="end" font-size="9.5" fill="#ffffff" font-weight="800">16.348 KH (88,6%)</text>

    <!-- Step B03: Xác thực khuôn mặt Liveness -->
    <rect x="55" y="66" width="270" height="22" rx="4" fill="#ccfbf1" stroke="#5eead4" />
    <rect x="55" y="66" width="270" height="22" rx="4" fill="#0d9488" opacity="0.9" />
    <text x="65" y="80" font-size="9" fill="#ffffff" font-weight="700">B03 - Nhận diện khuôn mặt (Face Liveness)</text>
    <text x="315" y="80" text-anchor="end" font-size="9.5" fill="#ffffff" font-weight="800">15.536 KH (84,2%)</text>

    <!-- Step B04: Ký hợp đồng & Hoàn tất -->
    <rect x="75" y="94" width="230" height="22" rx="4" fill="#dcfce7" stroke="#86efac" />
    <rect x="75" y="94" width="230" height="22" rx="4" fill="#10b981" opacity="0.95" />
    <text x="85" y="108" font-size="9" fill="#ffffff" font-weight="700">B04 - Ký hợp đồng &amp; Cấp số TKGDCK</text>
    <text x="295" y="108" text-anchor="end" font-size="9.5" fill="#ffffff" font-weight="800">15.204 KH (82,4%)</text>
  </svg>
  <div style="font-size: 0.68rem; color: #64748b; margin-top: 0.35rem; display: flex; justify-content: space-between;">
    <span>* Rớt lớn nhất: B01 &rarr; B02 (-11,4% do không chụp CCCD)</span>
    <span>Tỷ lệ hoàn tất phễu: <strong style="color: #10b981;">82,4%</strong></span>
  </div>
</div>'''

# Biểu đồ Mục 4: Nguồn Thông Tin Định Danh Khách Hàng (Identity Fallback)
SVG_EKYC_4 = '''<div class="visual-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
  <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
    <span>Cơ Cấu Nguồn Định Danh &amp; Đối Chiếu Dữ Liệu</span>
    <span style="font-size: 0.68rem; color: #6366f1; font-weight: 700;">Fallback Priority</span>
  </div>
  <svg class="visual-chart-svg" viewBox="0 0 380 120" style="background: var(--bg-surface-elevated, #ffffff); border-radius: 6px; border: 1px solid var(--border-color, #e2e8f0); width: 100%; height: auto;">
    <!-- Left: Identity Source Pie -->
    <!-- Center cx=85, cy=58, r=44 -->
    <!-- 1. CCCD gắn chip / C06 (72.5% in Indigo) -->
    <circle cx="85" cy="58" r="44" fill="#4f46e5" />
    <!-- 2. CCCD 12 số OCR (24.0% in Sky blue from top 85,14 to 127,72) -->
    <path d="M 85 58 L 85 14 A 44 44 0 0 1 127 72 Z" fill="#0284c7" stroke="#ffffff" stroke-width="1.5" />
    <!-- 3. Hộ chiếu / Khác (3.5% in Coral) -->
    <path d="M 85 58 L 127 72 A 44 44 0 0 1 121 86 Z" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />

    <text x="65" y="62" text-anchor="middle" font-size="10.5" fill="#ffffff" font-weight="800">72,5%</text>
    <text x="65" y="73" text-anchor="middle" font-size="7" fill="#e0e7ff" font-weight="700">Chip / C06</text>

    <text x="110" y="42" text-anchor="middle" font-size="9" fill="#ffffff" font-weight="800">24,0%</text>
    <text x="110" y="52" text-anchor="middle" font-size="6.5" fill="#e0f2fe" font-weight="700">CCCD 12 số</text>

    <!-- Legend & Reconciliation Rules on the Right -->
    <rect x="165" y="10" width="205" height="30" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
    <rect x="173" y="18" width="10" height="10" rx="2" fill="#4f46e5" />
    <text x="189" y="23" font-size="8.5" fill="#475569" font-weight="600">CCCD Gắn Chip (C06):</text>
    <text x="360" y="23" text-anchor="end" font-size="10" fill="#4338ca" font-weight="800">13.378 (72,5%)</text>

    <rect x="165" y="44" width="205" height="30" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
    <rect x="173" y="52" width="10" height="10" rx="2" fill="#0284c7" />
    <text x="189" y="57" font-size="8.5" fill="#475569" font-weight="600">CCCD 12 số truyền thống:</text>
    <text x="360" y="57" text-anchor="end" font-size="10" fill="#0369a1" font-weight="800">4.428 (24,0%)</text>

    <rect x="165" y="78" width="205" height="30" rx="4" fill="#f8fafc" stroke="#e2e8f0" />
    <rect x="173" y="86" width="10" height="10" rx="2" fill="#f43f5e" />
    <text x="189" y="91" font-size="8.5" fill="#475569" font-weight="600">Hộ chiếu / Nước ngoài:</text>
    <text x="360" y="91" text-anchor="end" font-size="10" fill="#e11d48" font-weight="800">646 (3,5%)</text>

    <text x="165" y="116" font-size="8" fill="#64748b" font-weight="600">Khớp dữ liệu Core CUSTODYCD = custody_id đạt: <tspan fill="#059669" font-weight="800">96,5%</tspan></text>
  </svg>
</div>'''

# Top Summary Dashboard Widget for page-eservice-ekyc
TOP_DASHBOARD_EKYC = '''
              <!-- DASHBOARD TRỰC QUAN MỞ TKGDCK QUA EKYC (CORE FLEX) -->
              <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); padding: 1rem; margin-top: 1rem; margin-bottom: 1.25rem;">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; padding-bottom: 0.75rem; border-bottom: 1px solid #f1f5f9; margin-bottom: 0.85rem;">
                  <div style="font-size: 0.95rem; font-weight: 800; color: #0f172a; display: flex; align-items: center; gap: 0.4rem;">
                    <span style="display: inline-block; width: 4px; height: 16px; background: #00bf5f; border-radius: 2px;"></span>
                    <span>TỔNG QUAN HÀNH TRÌNH MỞ TKGDCK QUA eKYC</span>
                  </div>
                  <div style="display: flex; gap: 0.5rem; align-items: center; font-size: 0.75rem;">
                    <span style="color: #64748b; font-weight: 600;">Kỳ ghi nhận: 15/01/2024 &rarr; 04/09/2026</span>
                    <span class="pill pill-success" style="font-size: 0.7rem; font-weight: 700;">Tableau v2.1 Live</span>
                  </div>
                </div>

                <!-- 4 KPI Cards -->
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.75rem; margin-bottom: 0.85rem;">
                  <div class="kpi-card" style="border-left: 3px solid #3b82f6; padding: 0.65rem 0.75rem; background: #f8fafc;">
                    <div style="font-size: 0.72rem; color: #64748b; font-weight: 600;">Tổng Hồ Sơ Đăng Ký</div>
                    <div style="font-size: 1.3rem; font-weight: 800; color: #0f172a; margin: 0.2rem 0;">18.452</div>
                    <div style="font-size: 0.68rem; color: #10b981; font-weight: 600;">+24,6% MoM tăng trưởng</div>
                  </div>
                  <div class="kpi-card" style="border-left: 3px solid #10b981; padding: 0.65rem 0.75rem; background: #f0fdf4;">
                    <div style="font-size: 0.72rem; color: #166534; font-weight: 600;">Kích Hoạt Thành Công</div>
                    <div style="font-size: 1.3rem; font-weight: 800; color: #059669; margin: 0.2rem 0;">15.204</div>
                    <div style="font-size: 0.68rem; color: #059669; font-weight: 700;">82,4% Tỷ lệ chuyển đổi</div>
                  </div>
                  <div class="kpi-card" style="border-left: 3px solid #0d9488; padding: 0.65rem 0.75rem; background: #f0fdfa;">
                    <div style="font-size: 0.72rem; color: #115e59; font-weight: 600;">Kênh Mở Web (Online)</div>
                    <div style="font-size: 1.3rem; font-weight: 800; color: #0d9488; margin: 0.2rem 0;">14.485</div>
                    <div style="font-size: 0.68rem; color: #0d9488; font-weight: 600;">78,5% Tỷ trọng (Careby 9999)</div>
                  </div>
                  <div class="kpi-card" style="border-left: 3px solid #ef4444; padding: 0.65rem 0.75rem; background: #fef2f2;">
                    <div style="font-size: 0.72rem; color: #991b1b; font-weight: 600;">Hồ Sơ Chưa Hoàn Tất</div>
                    <div style="font-size: 1.3rem; font-weight: 800; color: #dc2626; margin: 0.2rem 0;">3.248</div>
                    <div style="font-size: 0.68rem; color: #ef4444; font-weight: 600;">17,6% Rớt ở B01 - B03</div>
                  </div>
                </div>
              </div>'''

print("Visual components prepared successfully.")
