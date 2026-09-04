# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# CSS definitions to add
CSS_BCGD = """
    /* BCGD LIVE DASHBOARD VISUALS (THEO POWERBI OVERVIEW) */
    .dsc-dash-container {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
      padding: 1rem 1.25rem;
      margin-bottom: 1.5rem;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #1e293b;
    }
    .dsc-dash-topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px solid #f1f5f9;
      margin-bottom: 1rem;
    }
    .dsc-dash-title {
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: 0.02em;
      color: #0f172a;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .dsc-dash-title::before {
      content: "";
      display: inline-block;
      width: 4px;
      height: 18px;
      background: #00bf5f;
      border-radius: 2px;
    }
    .dsc-dash-controls {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .dsc-dash-date-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: #475569;
    }
    .dsc-dash-date-input {
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      padding: 0.25rem 0.5rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: #0f172a;
      background: #f8fafc;
    }
    .dsc-dash-btn-back {
      background: #2dd4bf;
      color: #ffffff;
      border: none;
      border-radius: 4px;
      padding: 0.35rem 0.9rem;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 2px 4px rgba(45, 212, 191, 0.3);
      transition: background 0.15s ease;
    }
    .dsc-dash-btn-back:hover {
      background: #14b8a6;
    }

    /* KPI Sparkline Cards Grid */
    .dsc-kpi-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }
    @media (max-width: 1024px) {
      .dsc-kpi-grid { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 640px) {
      .dsc-kpi-grid { grid-template-columns: 1fr; }
    }
    .dsc-kpi-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 0.65rem 0.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 1px 3px rgba(0,0,0,0.02);
      position: relative;
      overflow: hidden;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .dsc-kpi-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 10px rgba(0,0,0,0.06);
    }
    .dsc-kpi-info {
      flex: 1;
    }
    .dsc-kpi-name {
      font-size: 0.75rem;
      font-weight: 600;
      color: #475569;
      margin-bottom: 0.25rem;
    }
    .dsc-kpi-val {
      font-size: 1.25rem;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.1;
      margin-bottom: 0.2rem;
    }
    .dsc-kpi-sub {
      font-size: 0.68rem;
      color: #64748b;
      display: flex;
      flex-direction: column;
      gap: 0.1rem;
    }
    .dsc-kpi-sub .red {
      color: #ef4444;
      font-weight: 600;
    }
    .dsc-kpi-sub .green {
      color: #10b981;
      font-weight: 600;
    }
    .dsc-kpi-spark {
      width: 75px;
      height: 40px;
      flex-shrink: 0;
      margin-left: 0.5rem;
    }

    /* Middle Row: Heatmap + Branch Matrix */
    .dsc-mid-grid {
      display: grid;
      grid-template-columns: 1fr 1.3fr;
      gap: 1rem;
      margin-bottom: 1.25rem;
    }
    @media (max-width: 900px) {
      .dsc-mid-grid { grid-template-columns: 1fr; }
    }
    .dsc-box-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 0.75rem;
    }
    .dsc-box-header {
      font-size: 0.82rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 0.65rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    /* Heatmap Table */
    .dsc-heatmap-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 4px;
      font-size: 0.72rem;
    }
    .dsc-heatmap-table th {
      padding: 0.25rem 0.35rem;
      font-weight: 600;
      color: #64748b;
      text-align: center;
      background: transparent;
      border: none;
    }
    .dsc-heatmap-table td {
      padding: 0.5rem 0.25rem;
      text-align: center;
      border-radius: 3px;
      font-weight: 600;
      transition: transform 0.1s ease;
      cursor: pointer;
    }
    .dsc-heatmap-table td:hover {
      transform: scale(1.08);
      box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    }
    .dsc-hm-week {
      color: #64748b;
      font-weight: 500;
      font-style: italic;
      text-align: left !important;
      background: transparent !important;
      cursor: default !important;
    }
    .dsc-hm-gray { background: #cbd5e1; color: #475569; }
    .dsc-hm-light-gray { background: #e2e8f0; color: #64748b; }
    .dsc-hm-pink { background: #fecdd3; color: #9f1239; }
    .dsc-hm-coral { background: #fca5a5; color: #991b1b; }
    .dsc-hm-dark-coral { background: #f43f5e; color: #ffffff; }
    .dsc-hm-light-teal { background: #99f6e4; color: #115e59; }
    .dsc-hm-teal { background: #2dd4bf; color: #0f766e; }
    .dsc-hm-dark-teal { background: #0d9488; color: #ffffff; }

    /* Branch Matrix Table */
    .dsc-matrix-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.75rem;
    }
    .dsc-matrix-table th {
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      padding: 0.45rem 0.5rem;
      border: 1px solid #e2e8f0;
      text-align: center;
    }
    .dsc-matrix-table th:first-child {
      text-align: left;
    }
    .dsc-matrix-table td {
      padding: 0.55rem 0.5rem;
      border: 1px solid #f1f5f9;
      text-align: center;
      color: #1e293b;
    }
    .dsc-matrix-table td:first-child {
      text-align: left;
      font-weight: 600;
      color: #0f172a;
    }
    .dsc-matrix-table tr:hover td {
      background: #f8fafc;
    }
    .dsc-matrix-bubble {
      display: inline-block;
      width: 14px;
      height: 14px;
      border: 2px solid #3b82f6;
      border-radius: 50%;
      background: transparent;
      transition: all 0.2s;
      cursor: pointer;
    }
    .dsc-matrix-bubble:hover {
      background: #3b82f6;
      transform: scale(1.25);
    }

    /* 3 Ranked Bar Charts Grid */
    .dsc-ranks-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.75rem;
    }
    @media (max-width: 900px) {
      .dsc-ranks-grid { grid-template-columns: 1fr; }
    }
    .dsc-rank-col {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 0.75rem;
    }
    .dsc-rank-title {
      font-size: 0.78rem;
      font-weight: 700;
      color: #0f172a;
      padding-bottom: 0.4rem;
      border-bottom: 2px solid #e2e8f0;
      margin-bottom: 0.5rem;
    }
    .dsc-rank-item {
      display: grid;
      grid-template-columns: 100px 1fr 65px;
      align-items: center;
      gap: 0.4rem;
      margin-bottom: 0.35rem;
      font-size: 0.7rem;
    }
    .dsc-rank-name {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      color: #334155;
      font-weight: 500;
    }
    .dsc-rank-bar-bg {
      background: #f1f5f9;
      height: 14px;
      border-radius: 2px;
      overflow: hidden;
      display: flex;
    }
    .dsc-rank-bar-fill {
      height: 100%;
      border-radius: 2px;
      transition: width 0.3s ease;
    }
    .dsc-bar-teal { background: #2dd4bf; }
    .dsc-bar-light-teal { background: #5eead4; }
    .dsc-bar-coral { background: #fca5a5; }
    .dsc-bar-deep-coral { background: #f87171; }
    .dsc-rank-metric {
      font-size: 0.65rem;
      font-weight: 600;
      white-space: nowrap;
      text-align: right;
      color: #475569;
    }
"""

if "/* BCGD LIVE DASHBOARD VISUALS (THEO POWERBI OVERVIEW) */" not in content:
    style_end = content.find('</style>')
    content = content[:style_end] + CSS_BCGD + content[style_end:]
    print("Added BCGD CSS successfully.")

# SVG Sparklines
SPARK_THI_PHAN = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 35 L12 28 L25 38 L38 12 L50 22 L62 5 L75 32 L88 20 L100 25" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SPARK_DU_NO = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 30 L15 10 L30 18 L45 8 L60 25 L75 15 L90 35 L100 38" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SPARK_GTGD = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 25 L12 10 L25 15 L38 8 L50 18 L62 12 L75 28 L88 32 L100 38" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SPARK_PGDR = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 12 L15 15 L30 8 L45 20 L60 14 L75 22 L90 35 L100 38" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

SPARK_TK = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 8 L15 18 L30 12 L45 22 L60 15 L75 35 L90 32 L100 38" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# 1. Full Dashboard Overview Widget to put at top of section-bcgd
DASHBOARD_OVERVIEW_HTML = f'''
              <!-- LIVE DASHBOARD OVERVIEW VISUAL MOCKUP (THEO THIET KE POWER BI DSC) -->
              <div class="dsc-dash-container">
                <div class="dsc-dash-topbar">
                  <div class="dsc-dash-title">DASHBOARD OVERVIEW</div>
                  <div class="dsc-dash-controls">
                    <span class="dsc-dash-date-badge">Ngày:</span>
                    <input type="text" class="dsc-dash-date-input" value="03/09/2026" readonly title="Bộ lọc ngày giao dịch T">
                    <button type="button" class="dsc-dash-btn-back" onclick="alert('Đã tải lại trạng thái tổng quan mặc định!')">Quay lại</button>
                  </div>
                </div>

                <!-- ROW 1: 5 KPI CARDS WITH SPARKLINES -->
                <div class="dsc-kpi-grid">
                  <div class="dsc-kpi-card" title="Thị phần DSC MTD &amp; Xu hướng biến động">
                    <div class="dsc-kpi-info">
                      <div class="dsc-kpi-name">Thị phần</div>
                      <div class="dsc-kpi-val">3,38%</div>
                      <div class="dsc-kpi-sub">
                        <span>vs Ngày trước: <strong style="color:#10b981;">+0,12%</strong></span>
                        <span>vs Tháng trước: <strong style="color:#ef4444;">-0,45%</strong></span>
                      </div>
                    </div>
                    {SPARK_THI_PHAN}
                  </div>

                  <div class="dsc-kpi-card" title="Tổng quy mô Dư nợ Margin hiện hữu">
                    <div class="dsc-kpi-info">
                      <div class="dsc-kpi-name">Dư Nợ</div>
                      <div class="dsc-kpi-val">2.709B</div>
                      <div class="dsc-kpi-sub">
                        <span>vs Ngày trước: <strong style="color:#10b981;">+14B</strong></span>
                        <span>vs Tháng trước: <strong style="color:#10b981;">+128B</strong></span>
                      </div>
                    </div>
                    {SPARK_DU_NO}
                  </div>

                  <div class="dsc-kpi-card" title="Tổng Giá trị Khớp lệnh Toàn công ty">
                    <div class="dsc-kpi-info">
                      <div class="dsc-kpi-name">Giá Trị Giao Dịch</div>
                      <div class="dsc-kpi-val">118B</div>
                      <div class="dsc-kpi-sub">
                        <span>vs Ngày trước</span>
                        <span class="red">-40,55% vs Tháng trước</span>
                      </div>
                    </div>
                    {SPARK_GTGD}
                  </div>

                  <div class="dsc-kpi-card" title="Phí Giao Dịch Ròng cơ sở tính hoa hồng kinh doanh">
                    <div class="dsc-kpi-info">
                      <div class="dsc-kpi-name">PGDR tính Hoa hồng</div>
                      <div class="dsc-kpi-val">276M</div>
                      <div class="dsc-kpi-sub">
                        <span class="red">-53,27% vs Tháng trước</span>
                      </div>
                    </div>
                    {SPARK_PGDR}
                  </div>

                  <div class="dsc-kpi-card" title="Số lượng tài khoản mở mới phát triển trong kỳ">
                    <div class="dsc-kpi-info">
                      <div class="dsc-kpi-name">Tổng số TK mở mới</div>
                      <div class="dsc-kpi-val">19</div>
                      <div class="dsc-kpi-sub">
                        <span class="red">-90,83% vs Tháng trước</span>
                      </div>
                    </div>
                    {SPARK_TK}
                  </div>
                </div>

                <!-- ROW 2: CALENDAR HEATMAP + BRANCH MATRIX -->
                <div class="dsc-mid-grid">
                  <div class="dsc-box-card">
                    <div class="dsc-box-header">
                      <span>Giá trị giao dịch trong 30 ngày</span>
                      <span style="font-size: 0.68rem; color: #64748b; font-weight: normal;">Calendar Heatmap</span>
                    </div>
                    <table class="dsc-heatmap-table">
                      <thead>
                        <tr>
                          <th style="width: 55px;"></th>
                          <th>Th 2</th>
                          <th>Th 3</th>
                          <th>Th 4</th>
                          <th>Th 5</th>
                          <th>Th 6</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td class="dsc-hm-week">Week 32</td>
                          <td class="dsc-hm-light-gray" title="Chưa có phiên">-</td>
                          <td class="dsc-hm-pink" title="GTGD: 88 tỷ (Thấp hơn TB)">88B</td>
                          <td class="dsc-hm-light-gray" title="GTGD: 102 tỷ (Trung bình)">102B</td>
                          <td class="dsc-hm-light-gray" title="GTGD: 110 tỷ (Trung bình)">110B</td>
                          <td class="dsc-hm-light-gray" title="GTGD: 105 tỷ (Trung bình)">105B</td>
                        </tr>
                        <tr>
                          <td class="dsc-hm-week">Week 33</td>
                          <td class="dsc-hm-teal" title="GTGD: 165 tỷ (Tích cực)">165B</td>
                          <td class="dsc-hm-pink" title="GTGD: 92 tỷ (Thấp hơn TB)">92B</td>
                          <td class="dsc-hm-light-gray" title="GTGD: 115 tỷ (Trung bình)">115B</td>
                          <td class="dsc-hm-dark-teal" title="GTGD: 240 tỷ (Đỉnh điểm thanh khoản)">240B</td>
                          <td class="dsc-hm-teal" title="GTGD: 178 tỷ (Tích cực)">178B</td>
                        </tr>
                        <tr>
                          <td class="dsc-hm-week">Week 34</td>
                          <td class="dsc-hm-coral" title="GTGD: 78 tỷ (Sụt giảm)">78B</td>
                          <td class="dsc-hm-dark-coral" title="GTGD: 62 tỷ (Đáy thanh khoản)">62B</td>
                          <td class="dsc-hm-coral" title="GTGD: 80 tỷ (Sụt giảm)">80B</td>
                          <td class="dsc-hm-dark-coral" title="GTGD: 65 tỷ (Đáy thanh khoản)">65B</td>
                          <td class="dsc-hm-teal" title="GTGD: 182 tỷ (Bật tăng hồi phục)">182B</td>
                        </tr>
                        <tr>
                          <td class="dsc-hm-week">Week 35</td>
                          <td class="dsc-hm-light-gray" title="GTGD: 112 tỷ (Trung bình)">112B</td>
                          <td class="dsc-hm-light-gray" title="GTGD: 108 tỷ (Trung bình)">108B</td>
                          <td class="dsc-hm-light-gray" title="GTGD: 118 tỷ (Trung bình)">118B</td>
                          <td class="dsc-hm-teal" title="GTGD: 170 tỷ (Tích cực)">170B</td>
                          <td class="dsc-hm-light-gray" title="Chưa kết thúc phiên">-</td>
                        </tr>
                      </tbody>
                    </table>
                    <div style="display: flex; justify-content: flex-end; align-items: center; gap: 0.5rem; margin-top: 0.4rem; font-size: 0.65rem; color: #64748b;">
                      <span>Quy mô:</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#f43f5e; border-radius:2px;"></span> &lt;70B</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#fca5a5; border-radius:2px;"></span> 70-95B</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#e2e8f0; border-radius:2px;"></span> 95-130B</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#2dd4bf; border-radius:2px;"></span> 130-190B</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#0d9488; border-radius:2px;"></span> &gt;190B</span>
                    </div>
                  </div>

                  <div class="dsc-box-card">
                    <div class="dsc-box-header">
                      <span>Hiệu Suất 4 Chi Nhánh</span>
                      <span style="font-size: 0.68rem; color: #64748b; font-weight: normal;">Bảng Ma Trận Đa Chiều</span>
                    </div>
                    <table class="dsc-matrix-table">
                      <thead>
                        <tr>
                          <th>Chi nhánh</th>
                          <th>NAV</th>
                          <th>Dư Nợ</th>
                          <th>Giá Trị Giao Dịch</th>
                          <th>Phí Giao Dịch Ròng</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>Dịch Vọng Hậu</td>
                          <td><span class="dsc-matrix-bubble" title="Dịch Vọng Hậu - NAV: 4.850 tỷ (52,0%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Dịch Vọng Hậu - Dư Nợ: 1.420 tỷ (52,4%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Dịch Vọng Hậu - GTGD: 68 tỷ (57,6%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Dịch Vọng Hậu - PGDR: 165 triệu (59,8%)"></span></td>
                        </tr>
                        <tr>
                          <td>Hàm Long</td>
                          <td><span class="dsc-matrix-bubble" title="Hàm Long - NAV: 2.100 tỷ (22,5%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Hàm Long - Dư Nợ: 610 tỷ (22,5%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Hàm Long - GTGD: 26 tỷ (22,0%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Hàm Long - PGDR: 58 triệu (21,0%)"></span></td>
                        </tr>
                        <tr>
                          <td>Nguyễn Văn Trỗi</td>
                          <td><span class="dsc-matrix-bubble" title="Nguyễn Văn Trỗi - NAV: 1.450 tỷ (15,5%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Nguyễn Văn Trỗi - Dư Nợ: 430 tỷ (15,9%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Nguyễn Văn Trỗi - GTGD: 15 tỷ (12,7%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Nguyễn Văn Trỗi - PGDR: 34 triệu (12,3%)"></span></td>
                        </tr>
                        <tr>
                          <td>Đà Nẵng</td>
                          <td><span class="dsc-matrix-bubble" title="Đà Nẵng - NAV: 920 tỷ (10,0%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Đà Nẵng - Dư Nợ: 249 tỷ (9,2%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Đà Nẵng - GTGD: 9 tỷ (7,7%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Đà Nẵng - PGDR: 19 triệu (6,9%)"></span></td>
                        </tr>
                      </tbody>
                    </table>
                    <div style="margin-top: 0.5rem; font-size: 0.68rem; color: #64748b; font-style: italic;">
                      * Rà soát đối chiếu: Khớp hoàn toàn 100% số liệu RECON_013 trên kho dữ liệu DSC Data Lake.
                    </div>
                  </div>
                </div>

                <!-- ROW 3: 3 RANKED HORIZONTAL BAR CHARTS -->
                <div class="dsc-ranks-grid">
                  <div class="dsc-rank-col">
                    <div class="dsc-rank-title">PGDR tính HH theo GĐ</div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Ngô Văn Quang">Ngô Văn Quang</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-teal" style="width: 73%;"></div></div>
                      <div class="dsc-rank-metric">73M | <span style="color:#ef4444;">-82,55%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="GĐ Phòng Tư vấn Chứng khoán Đà Nẵng">GĐ PVTV CK ĐN</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-light-teal" style="width: 44%;"></div></div>
                      <div class="dsc-rank-metric">44M | <span style="color:#ef4444;">-50,81%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Minh Sáng">Nguyễn Minh Sáng</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 33%;"></div></div>
                      <div class="dsc-rank-metric">33M | <span style="color:#10b981;">54,19%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Giám đốc Gián tiếp Võ Đình Tuấn">GĐGT Võ Đình Tuấn</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 27%;"></div></div>
                      <div class="dsc-rank-metric">27M | <span style="color:#ef4444;">-58,13%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Xuân Khánh">Nguyễn Xuân Khánh</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 25%;"></div></div>
                      <div class="dsc-rank-metric">25M | <span style="color:#ef4444;">-45,62%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Văn Khuyên">Nguyễn Văn Khuyên</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 16%;"></div></div>
                      <div class="dsc-rank-metric">16M | <span style="color:#10b981;">59,71%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Văn Cường">Nguyễn Văn Cường</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 15%;"></div></div>
                      <div class="dsc-rank-metric">15M | <span style="color:#10b981;">65,84%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="GĐ Gián tiếp LVA">GĐ Gián tiếp LVA</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 13%;"></div></div>
                      <div class="dsc-rank-metric">13M | <span style="color:#ef4444;">-55,63%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Phùng Ngọc Sơn">Phùng Ngọc Sơn</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 12%;"></div></div>
                      <div class="dsc-rank-metric">12M | <span style="color:#ef4444;">-44,77%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Lữ Đình Quân">Lữ Đình Quân</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-deep-coral" style="width: 7%;"></div></div>
                      <div class="dsc-rank-metric">7M | <span style="color:#ef4444;">-52,06%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Hà Hải Như">Nguyễn Hà Hải Như</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-deep-coral" style="width: 4%;"></div></div>
                      <div class="dsc-rank-metric">4M | <span style="color:#10b981;">55,40%</span></div>
                    </div>
                  </div>

                  <div class="dsc-rank-col">
                    <div class="dsc-rank-title">PGDR tính HH theo TP</div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nhâm Việt Bắc">Nhâm Việt Bắc</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-teal" style="width: 66%;"></div></div>
                      <div class="dsc-rank-metric">66M | <span style="color:#ef4444;">-41,95%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Trịnh Nguyễn Minh Đức">Trịnh N. Minh Đức</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 27%;"></div></div>
                      <div class="dsc-rank-metric">27M | <span style="color:#ef4444;">-59,10%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Hồng Quân">Nguyễn Hồng Quân</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 27%;"></div></div>
                      <div class="dsc-rank-metric">27M | <span style="color:#ef4444;">-75,45%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Lê Thị Diệu Ngọc">Lê Thị Diệu Ngọc</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 23%;"></div></div>
                      <div class="dsc-rank-metric">23M | <span style="color:#ef4444;">-34,52%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Phùng Quang Huy">Phùng Quang Huy</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 18%;"></div></div>
                      <div class="dsc-rank-metric">18M | <span style="color:#ef4444;">-47,24%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Lê Hải Đăng">Lê Hải Đăng</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 16%;"></div></div>
                      <div class="dsc-rank-metric">16M | <span style="color:#ef4444;">-48,60%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Thị Minh Tuyền">N.T. Minh Tuyền</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 14%;"></div></div>
                      <div class="dsc-rank-metric">14M | <span style="color:#10b981;">50,23%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Lê Thị Thanh Mai">Lê Thị Thanh Mai</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 13%;"></div></div>
                      <div class="dsc-rank-metric">13M | <span style="color:#ef4444;">-51,96%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Phan Hữu Tuất">Phan Hữu Tuất</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 12%;"></div></div>
                      <div class="dsc-rank-metric">12M | <span style="color:#ef4444;">-65,02%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Bùi Quang Tú">Bùi Quang Tú</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 11%;"></div></div>
                      <div class="dsc-rank-metric">11M | <span style="color:#ef4444;">-42,18%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Đỗ Việt Linh">Đỗ Việt Linh</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-deep-coral" style="width: 7%;"></div></div>
                      <div class="dsc-rank-metric">7M | <span style="color:#10b981;">28,72%</span></div>
                    </div>
                  </div>

                  <div class="dsc-rank-col">
                    <div class="dsc-rank-title">PGDR tính HH theo MG</div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Thị Mai Phương">N.T. Mai Phương</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-teal" style="width: 51%;"></div></div>
                      <div class="dsc-rank-metric">51M | <span style="color:#ef4444;">-70,26%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Lê Ngọc Đồng">N.L. Ngọc Đồng</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-light-teal" style="width: 27%;"></div></div>
                      <div class="dsc-rank-metric">27M | <span style="color:#ef4444;">-67,12%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Văn Công">Nguyễn Văn Công</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-light-teal" style="width: 26%;"></div></div>
                      <div class="dsc-rank-metric">26M | <span style="color:#10b981;">77,27%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Đào Thị Việt Hạnh">Đào Thị Việt Hạnh</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 19%;"></div></div>
                      <div class="dsc-rank-metric">19M | <span style="color:#ef4444;">-67,88%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Thị Minh">Nguyễn Thị Minh</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 11%;"></div></div>
                      <div class="dsc-rank-metric">11M | <span style="color:#ef4444;">-61,07%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Văn Tuấn">Nguyễn Văn Tuấn</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 10%;"></div></div>
                      <div class="dsc-rank-metric">10M | <span style="color:#ef4444;">-83,40%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Nguyễn Đạt Anh">Nguyễn Đạt Anh</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 9%;"></div></div>
                      <div class="dsc-rank-metric">9M | <span style="color:#10b981;">51,02%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Trần Thị Hà">Trần Thị Hà</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 8%;"></div></div>
                      <div class="dsc-rank-metric">8M | <span style="color:#ef4444;">-56,41%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Đặng Thị Hằng">Đặng Thị Hằng</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 7%;"></div></div>
                      <div class="dsc-rank-metric">7M | <span style="color:#ef4444;">-71,08%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Hoàng Tuấn Anh">Hoàng Tuấn Anh</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 6%;"></div></div>
                      <div class="dsc-rank-metric">6M | <span style="color:#ef4444;">-72,73%</span></div>
                    </div>
                    <div class="dsc-rank-item">
                      <div class="dsc-rank-name" title="Ngô Ngọc Hưng">Ngô Ngọc Hưng</div>
                      <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-deep-coral" style="width: 4%;"></div></div>
                      <div class="dsc-rank-metric">4M | <span style="color:#10b981;">29,52%</span></div>
                    </div>
                  </div>
                </div>
              </div>
'''

target_tag = '<!-- 5.1 Bộ 5 Chỉ Số KPI Tổng Quan & Sparklines Xu Hướng -->'
if "<!-- LIVE DASHBOARD OVERVIEW VISUAL MOCKUP" not in content:
    idx = content.find(target_tag)
    if idx != -1:
        content = content[:idx] + DASHBOARD_OVERVIEW_HTML + '\n\n              ' + content[idx:]
        print("Added Dashboard Overview Widget before Section 5.1 successfully.")

# 2. Update Mục 5.1 (section-bcgd-1) formula-right:
# Include the 5 KPI Sparklines visual block + the calculation details
FR_BCGD1 = f'''<div class="formula-right">
                      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
                        <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
                          <span>Biểu Đồ Trực Quan: Bộ 5 KPI &amp; Sparkline (Mục 5.1)</span>
                          <span style="font-size: 0.68rem; color: #10b981; font-weight: 600;">Live Snapshot</span>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin-bottom: 0.5rem;">
                          <div class="dsc-kpi-card" style="padding: 0.4rem 0.5rem;">
                            <div class="dsc-kpi-info">
                              <div class="dsc-kpi-name">Giá Trị Giao Dịch</div>
                              <div class="dsc-kpi-val" style="font-size: 1.1rem;">118B</div>
                              <div class="dsc-kpi-sub"><span class="red">-40,55% MoM</span></div>
                            </div>
                            {SPARK_GTGD}
                          </div>
                          <div class="dsc-kpi-card" style="padding: 0.4rem 0.5rem;">
                            <div class="dsc-kpi-info">
                              <div class="dsc-kpi-name">PGDR tính Hoa hồng</div>
                              <div class="dsc-kpi-val" style="font-size: 1.1rem;">276M</div>
                              <div class="dsc-kpi-sub"><span class="red">-53,27% MoM</span></div>
                            </div>
                            {SPARK_PGDR}
                          </div>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 0.4rem;">
                          <div class="dsc-kpi-card" style="padding: 0.4rem 0.5rem;">
                            <div class="dsc-kpi-info">
                              <div class="dsc-kpi-name">Thị phần</div>
                              <div class="dsc-kpi-val" style="font-size: 0.95rem;">3,38%</div>
                              <div class="dsc-kpi-sub"><span style="color:#10b981; font-size:0.6rem;">+0,12% DoD</span></div>
                            </div>
                          </div>
                          <div class="dsc-kpi-card" style="padding: 0.4rem 0.5rem;">
                            <div class="dsc-kpi-info">
                              <div class="dsc-kpi-name">Dư Nợ</div>
                              <div class="dsc-kpi-val" style="font-size: 0.95rem;">2.709B</div>
                              <div class="dsc-kpi-sub"><span style="color:#10b981; font-size:0.6rem;">+128B MoM</span></div>
                            </div>
                          </div>
                          <div class="dsc-kpi-card" style="padding: 0.4rem 0.5rem;">
                            <div class="dsc-kpi-info">
                              <div class="dsc-kpi-name">TK mở mới</div>
                              <div class="dsc-kpi-val" style="font-size: 0.95rem;">19</div>
                              <div class="dsc-kpi-sub"><span class="red" style="font-size:0.6rem;">-90,83% MoM</span></div>
                            </div>
                          </div>
                        </div>
                      </div>

                      <details class="example-details" open>
                        <summary class="example-summary">Ví Dụ Thực Tế &amp; Minh Họa Trực Quan (Live Simulation)</summary>
                        <div class="example-content">
                          <p class="example-problem">Snapshot KPI Ngày 03/09:<br>• GTGD DSC: <strong>118 tỷ</strong> (-40,55% MoM) | Thị phần: <strong>3,38%</strong>.<br>• Phí GD ròng tính HH: <strong>276 triệu</strong> (-53,27% MoM) | TK mở mới: <strong>19</strong>.</p>
                          <div class="calc-steps">
                            <div class="calc-step">Thị phần = (118 tỷ / Tổng TT 3.490 tỷ) × 100% = 3,38%</div>
                            <div class="calc-step">MoM Phí GD ròng = (276M - 590,7M) / 590,7M = -53,27%</div>
                            <div class="calc-result">Trạng thái: Sparkline ghi nhận xu hướng điều chỉnh giảm theo thanh khoản chung toàn thị trường.</div>
                          </div>
                        </div>
                      </details>
                    </div>'''

# 3. Update Mục 5.2 (section-bcgd-2) formula-right:
# Calendar Heatmap visual component
FR_BCGD2 = f'''<div class="formula-right">
                      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
                        <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.4rem; display: flex; justify-content: space-between; align-items: center;">
                          <span>Biểu Đồ Trực Quan: Giá trị GD 30 ngày (Mục 5.2)</span>
                          <span style="font-size: 0.68rem; color: #0d9488; font-weight: 600;">Calendar Heatmap</span>
                        </div>
                        <table class="dsc-heatmap-table" style="font-size: 0.68rem;">
                          <thead>
                            <tr>
                              <th style="width: 48px;"></th>
                              <th>Th 2</th>
                              <th>Th 3</th>
                              <th>Th 4</th>
                              <th>Th 5</th>
                              <th>Th 6</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td class="dsc-hm-week">W32</td>
                              <td class="dsc-hm-light-gray">-</td>
                              <td class="dsc-hm-pink" title="88 tỷ">88B</td>
                              <td class="dsc-hm-light-gray" title="102 tỷ">102B</td>
                              <td class="dsc-hm-light-gray" title="110 tỷ">110B</td>
                              <td class="dsc-hm-light-gray" title="105 tỷ">105B</td>
                            </tr>
                            <tr>
                              <td class="dsc-hm-week">W33</td>
                              <td class="dsc-hm-teal" title="165 tỷ">165B</td>
                              <td class="dsc-hm-pink" title="92 tỷ">92B</td>
                              <td class="dsc-hm-light-gray" title="115 tỷ">115B</td>
                              <td class="dsc-hm-dark-teal" title="240 tỷ (Đỉnh điểm)">240B</td>
                              <td class="dsc-hm-teal" title="178 tỷ">178B</td>
                            </tr>
                            <tr>
                              <td class="dsc-hm-week">W34</td>
                              <td class="dsc-hm-coral" title="78 tỷ">78B</td>
                              <td class="dsc-hm-dark-coral" title="62 tỷ (Đáy tháng)">62B</td>
                              <td class="dsc-hm-coral" title="80 tỷ">80B</td>
                              <td class="dsc-hm-dark-coral" title="65 tỷ">65B</td>
                              <td class="dsc-hm-teal" title="182 tỷ">182B</td>
                            </tr>
                            <tr>
                              <td class="dsc-hm-week">W35</td>
                              <td class="dsc-hm-light-gray" title="112 tỷ">112B</td>
                              <td class="dsc-hm-light-gray" title="108 tỷ">108B</td>
                              <td class="dsc-hm-light-gray" title="118 tỷ">118B</td>
                              <td class="dsc-hm-teal" title="170 tỷ">170B</td>
                              <td class="dsc-hm-light-gray">-</td>
                            </tr>
                          </tbody>
                        </table>
                        <div style="display: flex; justify-content: flex-end; align-items: center; gap: 0.35rem; margin-top: 0.4rem; font-size: 0.62rem; color: #64748b;">
                          <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:8px; height:8px; background:#f43f5e; border-radius:2px;"></span> &lt;70B</span>
                          <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:8px; height:8px; background:#e2e8f0; border-radius:2px;"></span> 95-130B</span>
                          <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:8px; height:8px; background:#0d9488; border-radius:2px;"></span> &gt;190B</span>
                        </div>
                      </div>

                      <details class="example-details" open>
                        <summary class="example-summary">Quy Luật Nhận Diện Chu Kỳ Thanh Khoản</summary>
                        <div class="example-content">
                          <p class="example-problem">Phân tích ma trận lịch nhiệt 4 tuần gần nhất:<br>• <strong>Đỉnh điểm thanh khoản:</strong> Thứ 5 Tuần 33 đạt <strong>240 tỷ</strong> (màu Xanh Đậm).<br>• <strong>Vùng đáy thanh khoản:</strong> Thứ 3 &amp; Thứ 5 Tuần 34 chỉ đạt <strong>62B - 65B</strong> (màu Hồng Đỏ Đậm).</p>
                          <div class="calc-steps">
                            <div class="calc-step">Nhận xét: Khối lượng giao dịch có tính chu kỳ bùng nổ vào các phiên Thứ 5 và Thứ 6.</div>
                          </div>
                        </div>
                      </details>
                    </div>'''

# 4. Update Mục 5.3 (section-bcgd-3) formula-right:
# Ma trận 4 Chi nhánh visual component
FR_BCGD3 = f'''<div class="formula-right">
                      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
                        <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
                          <span>Biểu Đồ Trực Quan: Ma Trận 4 Chi Nhánh (Mục 5.3)</span>
                          <span style="font-size: 0.68rem; color: #3b82f6; font-weight: 600;">4 Dimensions Matrix</span>
                        </div>
                        <table class="dsc-matrix-table" style="font-size: 0.72rem;">
                          <thead>
                            <tr>
                              <th>Chi nhánh</th>
                              <th>NAV</th>
                              <th>Dư Nợ</th>
                              <th>GTGD</th>
                              <th>PGDR</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td>Dịch Vọng Hậu</td>
                              <td><span class="dsc-matrix-bubble" title="NAV: 4.850 tỷ (52,0%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="Dư Nợ: 1.420 tỷ (52,4%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="GTGD: 68 tỷ (57,6%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="PGDR: 165 triệu (59,8%)"></span></td>
                            </tr>
                            <tr>
                              <td>Hàm Long</td>
                              <td><span class="dsc-matrix-bubble" title="NAV: 2.100 tỷ (22,5%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="Dư Nợ: 610 tỷ (22,5%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="GTGD: 26 tỷ (22,0%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="PGDR: 58 triệu (21,0%)"></span></td>
                            </tr>
                            <tr>
                              <td>Nguyễn Văn Trỗi</td>
                              <td><span class="dsc-matrix-bubble" title="NAV: 1.450 tỷ (15,5%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="Dư Nợ: 430 tỷ (15,9%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="GTGD: 15 tỷ (12,7%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="PGDR: 34 triệu (12,3%)"></span></td>
                            </tr>
                            <tr>
                              <td>Đà Nẵng</td>
                              <td><span class="dsc-matrix-bubble" title="NAV: 920 tỷ (10,0%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="Dư Nợ: 249 tỷ (9,2%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="GTGD: 9 tỷ (7,7%)"></span></td>
                              <td><span class="dsc-matrix-bubble" title="PGDR: 19 triệu (6,9%)"></span></td>
                            </tr>
                          </tbody>
                        </table>
                      </div>

                      <div class="dynamic-ui-box" style="margin: 0; background: var(--bg-surface);">
                        <div class="dynamic-ui-item"><span class="dynamic-ui-label">Top 1 Trọng Số Doanh Thu:</span><strong>Dịch Vọng Hậu (Chiếm ~60% toàn công ty)</strong></div>
                        <div class="dynamic-ui-item"><span class="dynamic-ui-label">Khớp Số Liệu Nguồn:</span><span>100% RECON_013 (Chi nhánh + Hội sở)</span></div>
                      </div>
                    </div>'''

# 5. Update Mục 5.4 (section-bcgd-4) formula-right:
# Metric Switcher Parameter visual component
FR_BCGD4 = f'''<div class="formula-right">
                      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
                        <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; display: flex; justify-content: space-between; align-items: center;">
                          <span>Biểu Đồ Trực Quan: Chuyển Đổi Chỉ Số (Mục 5.4)</span>
                          <span style="font-size: 0.68rem; color: #00bf5f; font-weight: 600;">Parameter Switcher</span>
                        </div>
                        <div style="display: flex; gap: 0.35rem; margin-bottom: 0.75rem; background: #f1f5f9; padding: 3px; border-radius: 4px;">
                          <button type="button" style="flex: 1; border: none; padding: 0.3rem 0; font-size: 0.72rem; font-weight: 700; border-radius: 3px; background: #ffffff; color: #0f172a; box-shadow: 0 1px 2px rgba(0,0,0,0.1); cursor: pointer;">NAV</button>
                          <button type="button" style="flex: 1; border: none; padding: 0.3rem 0; font-size: 0.72rem; font-weight: 600; border-radius: 3px; background: transparent; color: #64748b; cursor: pointer;">Dư Nợ</button>
                          <button type="button" style="flex: 1; border: none; padding: 0.3rem 0; font-size: 0.72rem; font-weight: 700; border-radius: 3px; background: #2dd4bf; color: #ffffff; cursor: pointer;">GTGD (Active)</button>
                          <button type="button" style="flex: 1; border: none; padding: 0.3rem 0; font-size: 0.72rem; font-weight: 600; border-radius: 3px; background: transparent; color: #64748b; cursor: pointer;">PGDR</button>
                        </div>
                        <div style="font-size: 0.72rem; color: #334155; line-height: 1.5; background: #f8fafc; padding: 0.5rem; border-radius: 4px; border: 1px dashed #cbd5e1;">
                          <strong>Góc nhìn điều hành khi chọn [GTGD]:</strong><br>
                          • Toàn DSC: <strong>118B</strong> khớp lệnh.<br>
                          • Top 1 Giám Đốc: <strong>Ngô Văn Quang</strong> (73B quy đổi giao dịch).<br>
                          • Top 1 Trưởng Phòng: <strong>Nhâm Việt Bắc</strong> (66B quy đổi).
                        </div>
                      </div>

                      <details class="example-details" open>
                        <summary class="example-summary">Ví Dụ Thực Tế Chuyển Đổi Cấp Giám Đốc</summary>
                        <div class="example-content">
                          <p class="example-problem">Khi chọn Toggle = <strong>GTGD</strong>, bảng xếp hạng Top Giám Đốc tự động cập nhật:<br>• Top 1: Nguyễn Minh Sáng = <strong>280 tỷ</strong><br>• Top 2: Lê Hải Đăng = <strong>183 tỷ</strong><br>• Top 3: Nguyễn Thị Thái = <strong>145 tỷ</strong></p>
                        </div>
                      </details>
                    </div>'''

# 6. Update Mục 5.5 (section-bcgd-5) formula-right:
# 3 Ranked Bar Charts visual component
FR_BCGD5 = f'''<div class="formula-right">
                      <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 6px; padding: 0.75rem; margin-bottom: 0.75rem;">
                        <div style="font-size: 0.8rem; font-weight: 700; color: #0f172a; margin-bottom: 0.4rem; display: flex; justify-content: space-between; align-items: center;">
                          <span>Biểu Đồ Trực Quan: Xếp Hạng 3 Cấp Nhân Sự (Mục 5.5)</span>
                          <span style="font-size: 0.68rem; color: #2dd4bf; font-weight: 700;">PGDR tính HH</span>
                        </div>
                        <div style="display: grid; grid-template-columns: 1fr; gap: 0.4rem; max-height: 380px; overflow-y: auto; padding-right: 4px;">
                          <!-- Top GĐ -->
                          <div style="font-size: 0.72rem; font-weight: 700; color: #0f172a; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px;">Theo Giám Đốc (GĐ):</div>
                          <div class="dsc-rank-item" style="grid-template-columns: 85px 1fr 65px;">
                            <div class="dsc-rank-name">Ngô Văn Quang</div>
                            <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-teal" style="width: 73%;"></div></div>
                            <div class="dsc-rank-metric">73M | <span style="color:#ef4444;">-82,5%</span></div>
                          </div>
                          <div class="dsc-rank-item" style="grid-template-columns: 85px 1fr 65px;">
                            <div class="dsc-rank-name">GĐ PVTV CK ĐN</div>
                            <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-light-teal" style="width: 44%;"></div></div>
                            <div class="dsc-rank-metric">44M | <span style="color:#ef4444;">-50,8%</span></div>
                          </div>
                          <div class="dsc-rank-item" style="grid-template-columns: 85px 1fr 65px;">
                            <div class="dsc-rank-name">Nguyễn M. Sáng</div>
                            <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 33%;"></div></div>
                            <div class="dsc-rank-metric">33M | <span style="color:#10b981;">+54,2%</span></div>
                          </div>

                          <!-- Top TP -->
                          <div style="font-size: 0.72rem; font-weight: 700; color: #0f172a; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px; margin-top: 0.3rem;">Theo Trưởng Phòng (TP):</div>
                          <div class="dsc-rank-item" style="grid-template-columns: 85px 1fr 65px;">
                            <div class="dsc-rank-name">Nhâm Việt Bắc</div>
                            <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-teal" style="width: 66%;"></div></div>
                            <div class="dsc-rank-metric">66M | <span style="color:#ef4444;">-41,9%</span></div>
                          </div>
                          <div class="dsc-rank-item" style="grid-template-columns: 85px 1fr 65px;">
                            <div class="dsc-rank-name">Trịnh N. Minh Đức</div>
                            <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-coral" style="width: 27%;"></div></div>
                            <div class="dsc-rank-metric">27M | <span style="color:#ef4444;">-59,1%</span></div>
                          </div>

                          <!-- Top MG -->
                          <div style="font-size: 0.72rem; font-weight: 700; color: #0f172a; border-bottom: 1px solid #e2e8f0; padding-bottom: 2px; margin-top: 0.3rem;">Theo Môi Giới (MG):</div>
                          <div class="dsc-rank-item" style="grid-template-columns: 85px 1fr 65px;">
                            <div class="dsc-rank-name">N.T. Mai Phương</div>
                            <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-teal" style="width: 51%;"></div></div>
                            <div class="dsc-rank-metric">51M | <span style="color:#ef4444;">-70,3%</span></div>
                          </div>
                          <div class="dsc-rank-item" style="grid-template-columns: 85px 1fr 65px;">
                            <div class="dsc-rank-name">N.L. Ngọc Đồng</div>
                            <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-light-teal" style="width: 27%;"></div></div>
                            <div class="dsc-rank-metric">27M | <span style="color:#ef4444;">-67,1%</span></div>
                          </div>
                          <div class="dsc-rank-item" style="grid-template-columns: 85px 1fr 65px;">
                            <div class="dsc-rank-name">Nguyễn Văn Công</div>
                            <div class="dsc-rank-bar-bg"><div class="dsc-rank-bar-fill dsc-bar-light-teal" style="width: 26%;"></div></div>
                            <div class="dsc-rank-metric">26M | <span style="color:#10b981;">+77,3%</span></div>
                          </div>
                        </div>
                      </div>

                      <details class="example-details" open>
                        <summary class="example-summary">Kết Quả Đối Soát Báo Cáo Chế Độ Bookmark</summary>
                        <div class="example-content">
                          <p class="example-problem">Dữ liệu thực tế khi click 'Xem PGDR tính HH':<br>• Top 1 Giám đốc: <strong>73 triệu VNĐ</strong> (Ngô Văn Quang).<br>• Top 1 Trưởng phòng: <strong>66 triệu VNĐ</strong> (Nhâm Việt Bắc).<br>• Top 1 Môi giới: <strong>51 triệu VNĐ</strong> (Nguyễn Thị Mai Phương).</p>
                        </div>
                      </details>
                    </div>'''

# Helper to replace formula-right block in section-bcgd-N
fr_replacements = [
    (1, FR_BCGD1),
    (2, FR_BCGD2),
    (3, FR_BCGD3),
    (4, FR_BCGD4),
    (5, FR_BCGD5),
]

for num, new_fr in fr_replacements:
    tab_id = f'section-bcgd-{num}-tab-math'
    pos = content.find(tab_id)
    if pos == -1:
        print(f"ERROR: Cannot find {tab_id}")
        continue
    fr_pos = content.find('<div class="formula-right">', pos)
    fr_end = content.find('</div>\n                  </div>\n                </div>', fr_pos)
    old_fr = content[fr_pos:fr_end+6]
    content = content[:fr_pos] + new_fr + content[fr_end+6:]
    print(f"Replaced formula-right for BCGD {num} successfully.")

# Save modified content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully!")
