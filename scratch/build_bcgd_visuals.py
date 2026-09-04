# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Sparkline SVGs
# Sparkline 1: Thi phan (sharp peaks and troughs)
SPARK_THI_PHAN = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 35 L12 28 L25 38 L38 12 L50 22 L62 5 L75 32 L88 20 L100 25" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# Sparkline 2: Du No (wave)
SPARK_DU_NO = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 30 L15 10 L30 18 L45 8 L60 25 L75 15 L90 35 L100 38" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# Sparkline 3: Gia Tri Giao Dich (peaks then drop)
SPARK_GTGD = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 25 L12 10 L25 15 L38 8 L50 18 L62 12 L75 28 L88 32 L100 38" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# Sparkline 4: PGDR tinh HH (sharp drops)
SPARK_PGDR = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 12 L15 15 L30 8 L45 20 L60 14 L75 22 L90 35 L100 38" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# Sparkline 5: Tong so TK mo moi (steep decline)
SPARK_TK = '''<svg class="dsc-kpi-spark" viewBox="0 0 100 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M0 8 L15 18 L30 12 L45 22 L60 15 L75 35 L90 32 L100 38" stroke="#64748b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''

# Full Dashboard Overview Widget
DASHBOARD_OVERVIEW_HTML = f'''
              <!-- LIVE DASHBOARD OVERVIEW VISUAL MOCKUP (THEO THIET KE POWER BI DSC) -->
              <div class="dsc-dash-container">
                <div class="dsc-dash-topbar">
                  <div class="dsc-dash-title">DASHBOARD OVERVIEW</div>
                  <div class="dsc-dash-controls">
                    <span class="dsc-dash-date-badge">Ngày:</span>
                    <input type="text" class="dsc-dash-date-input" value="03/09/2026" readonly title="Bộ lọc ngày giao dịch T">
                    <button type="button" class="dsc-dash-btn-back" onclick="alert('Đã reset về trạng thái xem tổng quan ban đầu!')">Quay lại</button>
                  </div>
                </div>

                <!-- ROW 1: 5 KPI CARDS WITH SPARKLINES -->
                <div class="dsc-kpi-grid">
                  <!-- Card 1: Thị phần -->
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

                  <!-- Card 2: Dư Nợ -->
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

                  <!-- Card 3: Giá Trị Giao Dịch -->
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

                  <!-- Card 4: PGDR tính Hoa hồng -->
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

                  <!-- Card 5: Tổng số TK mở mới -->
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
                  <!-- Left: Giá trị giao dịch trong 30 ngày -->
                  <div class="dsc-box-card">
                    <div class="dsc-box-header">
                      <span>Giá trị giao dịch trong 30 ngày (Calendar Heatmap)</span>
                      <span style="font-size: 0.68rem; color: #64748b; font-weight: normal;">Khớp lệnh MTD</span>
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
                          <td class="dsc-hm-light-gray" title="Chưa có dữ liệu giao dịch">-</td>
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
                          <td class="dsc-hm-dark-coral" title="GTGD: 62 tỷ (Đáy thanh khoản tháng)">62B</td>
                          <td class="dsc-hm-coral" title="GTGD: 80 tỷ (Sụt giảm)">80B</td>
                          <td class="dsc-hm-dark-coral" title="GTGD: 65 tỷ (Đáy thanh khoản tháng)">65B</td>
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
                      <span>Chú giải:</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#f43f5e; border-radius:2px;"></span> &lt;70B</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#fca5a5; border-radius:2px;"></span> 70-95B</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#e2e8f0; border-radius:2px;"></span> 95-130B</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#2dd4bf; border-radius:2px;"></span> 130-190B</span>
                      <span style="display:inline-flex; align-items:center; gap:2px;"><span style="width:10px; height:10px; background:#0d9488; border-radius:2px;"></span> &gt;190B</span>
                    </div>
                  </div>

                  <!-- Right: Ma trận 4 Chi nhánh -->
                  <div class="dsc-box-card">
                    <div class="dsc-box-header">
                      <span>Hiệu Suất Chi Nhánh (Ma Trận 4 Chỉ Số)</span>
                      <span style="font-size: 0.68rem; color: #64748b; font-weight: normal;">4 Chi nhánh toàn quốc</span>
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
                          <td><span class="dsc-matrix-bubble" title="Dịch Vọng Hậu - NAV: 4.850 tỷ (Chiếm 52%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Dịch Vọng Hậu - Dư Nợ: 1.420 tỷ (Chiếm 52,4%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Dịch Vọng Hậu - GTGD: 68 tỷ (Chiếm 57,6%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Dịch Vọng Hậu - PGDR: 165 triệu (Chiếm 59,8%)"></span></td>
                        </tr>
                        <tr>
                          <td>Hàm Long</td>
                          <td><span class="dsc-matrix-bubble" title="Hàm Long - NAV: 2.100 tỷ (Chiếm 22,5%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Hàm Long - Dư Nợ: 610 tỷ (Chiếm 22,5%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Hàm Long - GTGD: 26 tỷ (Chiếm 22,0%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Hàm Long - PGDR: 58 triệu (Chiếm 21,0%)"></span></td>
                        </tr>
                        <tr>
                          <td>Nguyễn Văn Trỗi</td>
                          <td><span class="dsc-matrix-bubble" title="Nguyễn Văn Trỗi - NAV: 1.450 tỷ (Chiếm 15,5%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Nguyễn Văn Trỗi - Dư Nợ: 430 tỷ (Chiếm 15,9%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Nguyễn Văn Trỗi - GTGD: 15 tỷ (Chiếm 12,7%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Nguyễn Văn Trỗi - PGDR: 34 triệu (Chiếm 12,3%)"></span></td>
                        </tr>
                        <tr>
                          <td>Đà Nẵng</td>
                          <td><span class="dsc-matrix-bubble" title="Đà Nẵng - NAV: 920 tỷ (Chiếm 10,0%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Đà Nẵng - Dư Nợ: 249 tỷ (Chiếm 9,2%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Đà Nẵng - GTGD: 9 tỷ (Chiếm 7,7%)"></span></td>
                          <td><span class="dsc-matrix-bubble" title="Đà Nẵng - PGDR: 19 triệu (Chiếm 6,9%)"></span></td>
                        </tr>
                      </tbody>
                    </table>
                    <div style="margin-top: 0.5rem; font-size: 0.68rem; color: #64748b; font-style: italic;">
                      * Rà soát đối chiếu: Tổng 4 chi nhánh khớp hoàn toàn 100% số liệu RECON_013 trên hệ thống dữ liệu nguồn.
                    </div>
                  </div>
                </div>

                <!-- ROW 3: 3 RANKED HORIZONTAL BAR CHARTS -->
                <div class="dsc-ranks-grid">
                  <!-- Cột 1: PGDR tính HH theo GĐ -->
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

                  <!-- Cột 2: PGDR tính HH theo TP -->
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

                  <!-- Cột 3: PGDR tính HH theo MG -->
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

print("Dashboard Overview HTML constructed successfully, length:", len(DASHBOARD_OVERVIEW_HTML))
