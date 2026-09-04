# TÀI LIỆU NGHIỆP VỤ CÁC CHỈ SỐ BÁO CÁO POWER BI

---

## MỤC LỤC
1. [PHÂN HỆ 1: BÁO CÁO TỔNG QUAN](#1-phân-hệ-1-báo-cáo-tổng-quan)
   - [1.1. Dư nợ 12 tháng gần nhất & Đường tham chiếu trung bình](#11-dư-nợ-12-tháng-gần-nhất-đường-tham-chiếu-trung-bình)
   - [1.2. Hạn mức Margin & Hạn mức Ứng trước](#12-hạn-mức-margin-hạn-mức-ứng-trước)
   - [1.3. Tỷ trọng Dư nợ theo gói phí](#13-tỷ-trọng-dư-nợ-theo-gói-phí)
   - [1.4. Xếp hạng & Tỷ lệ sử dụng Room Top 15 Cổ phiếu](#14-xếp-hạng-tỷ-lệ-sử-dụng-room-top-15-cổ-phiếu)
   - [1.5. NAV & CASA trung bình tháng](#15-nav-casa-trung-bình-tháng)
   - [1.6. Đánh giá Biến động so với Đỉnh](#16-đánh-giá-biến-động-so-với-đỉnh)
2. [PHÂN HỆ 2: DANH MỤC CHO VAY & QUẢN TRỊ RỦI RO KHÁCH HÀNG](#2-phân-hệ-2-danh-mục-cho-vay-quản-trị-rủi-ro-khách-hàng)
   - [2.1. Tỷ lệ Đảm bảo Tài sản (TSR / GTCK)](#21-tỷ-lệ-đảm-bảo-tài-sản-tsr-gtck)
   - [2.2. Tỷ trọng Dư nợ Top 10 Khách hàng](#22-tỷ-trọng-dư-nợ-top-10-khách-hàng)
   - [2.3. Đánh giá Thanh khoản & Số phiên giải chấp danh mục (Tooltip)](#23-đánh-giá-thanh-khoản-số-phiên-giải-chấp-danh-mục-tooltip)
   - [2.4. Đánh giá Hành vi Vay: Vòng quay dư nợ & Mục đích sử dụng vốn (Tooltip)](#24-đánh-giá-hành-vi-vay-vòng-quay-dư-nợ-mục-đích-sử-dụng-vốn-tooltip)
   - [2.5. Giám sát Room & Hạn mức Deal cho vay (MR3040)](#25-giám-sát-room-hạn-mức-deal-cho-vay-mr3040)
3. [PHÂN HỆ 3: BÁO CÁO CHI TIẾT DƯ NỢ & QUẢN TRỊ RỦI RO HỆ THỐNG](#3-phân-hệ-3-báo-cáo-chi-tiết-dư-nợ-quản-trị-rủi-ro-hệ-thống)
   - [3.1. Lãi suất Cho vay Bình quân Gia quyền (Toàn hệ thống & Theo nhóm)](#31-lãi-suất-cho-vay-bình-quân-gia-quyền-toàn-hệ-thống-theo-nhóm)
   - [3.2. Hạn Mức Cho Vay (HMCV) Room Thường & HMCV Tổng](#32-hạn-mức-cho-vay-hmcv-room-thường-hmcv-tổng)
   - [3.3. Tỷ trọng Dư nợ theo Nhóm KH & Nhóm Chi tiết rủi ro](#33-tỷ-trọng-dư-nợ-theo-nhóm-kh-nhóm-chi-tiết-rủi-ro)
   - [3.4. Tỷ lệ Tài khoản Giao dịch Ký quỹ (TKGDKQ vs None)](#34-tỷ-lệ-tài-khoản-giao-dịch-ký-quỹ-tkgdkq-vs-none)
   - [3.5. Phân nhóm Xếp hạng Cổ phiếu (Rank A, B, C)](#35-phân-nhóm-xếp-hạng-cổ-phiếu-rank-a-b-c)
4. [PHÂN HỆ QUẢN TRỊ RỦI RO: BÁO CÁO THEO DÕI NỢ BẢO LÃNH T0](#4-phân-hệ-quản-trị-rủi-ro-báo-cáo-theo-dõi-nợ-bảo-lãnh-t0)
5. [PHÂN HỆ GIAO DỊCH - DASHBOARD OVERVIEW (BCGD)](#5-phân-hệ-giao-dịch---dashboard-overview-bcgd)
   - [5.1. Bộ 5 Chỉ Số KPI Tổng Quan & Sparklines Xu Hướng (`METRIC_GD_KPI_SUMMARY_SPARKLINES`)](#51-bộ-5-chỉ-số-kpi-tổng-quan-sparklines-xu-hướng-metric_gd_kpi_summary_sparklines)
   - [5.2. Ma Trận Lịch Biến Động GTGD 30 Ngày (Calendar Heatmap) (`METRIC_GD_CALENDAR_HEATMAP_30D`)](#52-ma-trận-lịch-biến-động-gtgd-30-ngày-calendar-heatmap-metric_gd_calendar_heatmap_30d)
   - [5.3. Bảng Phân Bổ Hiệu Suất Theo Chi Nhánh (`METRIC_GD_BRANCH_PERFORMANCE_MATRIX`)](#53-bảng-phân-bổ-hiệu-suất-theo-chi-nhánh-metric_gd_branch_performance_matrix)
   - [5.4. Cơ Chế Chuyển Đổi Chỉ Số Động 3 Cấp Quản Lý (`METRIC_GD_DYNAMIC_DRILLDOWN_LEVELS`)](#54-cơ-chế-chuyển-đổi-chỉ-số-động-3-cấp-quản-lý-metric_gd_dynamic_drilldown_levels)
   - [5.5. Phí Giao Dịch Ròng Tính Hoa Hồng & View Chuyên Sâu (`METRIC_GD_PGDR_COMMISSION_VIEW`)](#55-phí-giao-dịch-ròng-tính-hoa-hồng-view-chuyên-sâu-metric_gd_pgdr_commission_view)
6. [CHỈ SỐ GIAO DỊCH BỔ SUNG: GTGD MTD, TĂNG TRƯỞNG & THỊ PHẦN](#6-chỉ-số-giao-dịch-bổ-sung-gtgd-mtd-tăng-trưởng-thị-phần)
   - [6.1. Giá trị giao dịch MTD (Month-To-Date)](#61-giá-trị-giao-dịch-mtd-month-to-date)
   - [6.2. Tốc độ Tăng trưởng MoM (Month-over-Month) & YoY (Year-over-Year)](#62-tốc-độ-tăng-trưởng-mom-month-over-month-yoy-year-over-year)
   - [6.3. Tỷ lệ Thị phần Công ty (Market Share)](#63-tỷ-lệ-thị-phần-công-ty-market-share)
7. [BẢNG TỔNG HỢP CÔNG THỨC & QUY TẮC ĐÁNH GIÁ TOÀN DIỆN](#7-bảng-tổng-hợp-công-thức-quy-tắc-đánh-giá-toàn-diện)
8. [BÁO CÁO TỔNG HỢP DƯ NỢ THEO MÃ CHỨNG KHOÁN (MR0031)](#8-báo-cáo-tổng-hợp-dư-nợ-theo-mã-chứng-khoán-mr0031)
   - [8.1. Dư nợ quy đổi theo mã chứng khoán & Ngưỡng chặn trần 240 tỷ VNĐ (`METRIC_MR0031_CONVERTED_DEBT`)](#81-dư-nợ-quy-đổi-theo-mã-chứng-khoán-ngưỡng-chặn-trần-240-tỷ-vnđ-metric_mr0031_converted_debt)
   - [8.2. Khối lượng đánh dấu cổ phiếu ký quỹ & Ngưỡng chặn trần 5% cổ phiếu lưu hành (`METRIC_MR0031_MARKED_VOLUME`)](#82-khối-lượng-đánh-dấu-cổ-phiếu-ký-quỹ-ngưỡng-chặn-trần-5-cổ-phiếu-lưu-hành-metric_mr0031_marked_volume)
   - [8.3. Tỷ lệ cho vay ký quỹ áp dụng & Ngoại lệ mã SAM (`METRIC_MR0031_MARGIN_RATE`)](#83-tỷ-lệ-cho-vay-ký-quỹ-áp-dụng-ngoại-lệ-mã-sam-metric_mr0031_margin_rate)
   - [8.4. Ma trận dư nợ theo mã & Bộ lọc trượt đa chiều Range Sliders (`METRIC_MR0031_MATRIX_GRID_FILTER`)](#84-ma-trận-dư-nợ-theo-mã-bộ-lọc-trượt-đa-chiều-range-sliders-metric_mr0031_matrix_grid_filter)
9. [BÁO CÁO ĐỐI SOÁT TIN NHẮN SMS (IT VẬN HÀNH)](#9-báo-cáo-đối-soát-tin-nhắn-sms-it-vận-hành)
   - [9.1. Tổng Sản Lượng Tin Nhắn & Tỷ Lệ Gửi Thành Công (`METRIC_SMS_TOTAL_SUCCESS_RATE`)](#91-tổng-sản-lượng-tin-nhắn-tỷ-lệ-gửi-thành-công-metric_sms_total_success_rate)
   - [9.2. Phân Bổ Sản Lượng Theo Đơn Vị Cung Cấp Cổng Dịch Vụ (`METRIC_SMS_PROVIDER_DISTRIBUTION`)](#92-phân-bổ-sản-lượng-theo-đơn-vị-cung-cấp-cổng-dịch-vụ-metric_sms_provider_distribution)
   - [9.3. Phân Bổ Tin Nhắn Theo Nhà Mạng Telco (`METRIC_SMS_TELCO_BREAKDOWN`)](#93-phân-bổ-tin-nhắn-theo-nhà-mạng-telco-metric_sms_telco_breakdown)
   - [9.4. Phân Loại Trạng Thái & Danh Mục Mã Lỗi Kỹ Thuật (`METRIC_SMS_STATUS_ERROR_TAXONOMY`)](#94-phân-loại-trạng-thái-danh-mục-mã-lỗi-kỹ-thuật-metric_sms_status_error_taxonomy)
   - [9.5. Xu Hướng Sản Lượng Tin Nhắn Lũy Kế Theo Tháng (`METRIC_SMS_MONTHLY_RUNNING_TREND`)](#95-xu-hướng-sản-lượng-tin-nhắn-lũy-kế-theo-tháng-metric_sms_monthly_running_trend)
10. [BÁO CÁO TIẾN ĐỘ DỰ ÁN CNTT (KHỐI CNTT - PMO)](#10-báo-cáo-tiến-độ-dự-án-cntt-khối-cntt---pmo)
   - [10.1. Tổng Quan Danh Mục & Trạng Thái / Ưu Tiên (`METRIC_CNTT_PORTFOLIO_OVERVIEW`)](#101-tổng-quan-danh-mục-trạng-thái-ưu-tiên-metric_cntt_portfolio_overview)
   - [10.2. Phân Loại Dự Án & Phân Bổ Bộ Phận Phụ Trách (`METRIC_CNTT_PROJECT_TYPE_DISTRIBUTION`)](#102-phân-loại-dự-án-phân-bổ-bộ-phận-phụ-trách-metric_cntt_project_type_distribution)
   - [10.3. Bảng Theo Dõi Tiến Độ Toàn Diện & Kế Hoạch Golive (`METRIC_CNTT_PROJECT_TIMELINE_PROGRESS`)](#103-bảng-theo-dõi-tiến-độ-toàn-diện-kế-hoạch-golive-metric_cntt_project_timeline_progress)
   - [10.4. Mô Hình Phân Rã Milestone Trọng Số & Tiến Độ Thực Tế (`METRIC_CNTT_MILESTONE_WEIGHTED_PROGRESS`)](#104-mô-hình-phân-rã-milestone-trọng-số-tiến-độ-thực-tế-metric_cntt_milestone_weighted_progress)
   - [10.5. Đối Soát Tiến Độ Thực Tế vs Tiến Độ Kế Hoạch (`METRIC_CNTT_PLANNED_VS_ACTUAL_GAP`)](#105-đối-soát-tiến-độ-thực-tế-vs-tiến-độ-kế-hoạch-metric_cntt_planned_vs_actual_gap)
11. [BÁO CÁO ESERVICE (CORE FLEX EKYC & QUẢN LÝ KHÁCH HÀNG)](#11-báo-cáo-eservice-core-flex-ekyc-quản-lý-khách-hàng)
   - [11.1. Phân Loại Kênh Mở & Kích Hoạt TKGDCK (`METRIC_EKYC_PLATFORM_CHANNEL`)](#111-phân-loại-kênh-mở-kích-hoạt-tkgdck-metric_ekyc_platform_channel)
   - [11.2. Chuẩn Hóa Trạng Thái Tài Khoản eKYC (`METRIC_EKYC_STATUS_MAPPING`)](#112-chuẩn-hóa-trạng-thái-tài-khoản-ekyc-metric_ekyc_status_mapping)
   - [11.3. Chuẩn Hóa Bước Hành Trình Mở TKGDCK (`METRIC_EKYC_JOURNEY_STEP`)](#113-chuẩn-hóa-bước-hành-trình-mở-tkgdck-metric_ekyc_journey_step)
   - [11.4. Quy Tắc Ưu Tiên Nguồn Định Danh Khách Hàng (`METRIC_EKYC_IDENTITY_FALLBACK`)](#114-quy-tắc-ưu-tiên-nguồn-định-danh-khách-hàng-metric_ekyc_identity_fallback)
   - [11.5. Định Nghĩa Tài Khoản Hoạt Động (Active Account) (`METRIC_MKT_ACTIVE_ACCOUNT`)](#115-định-nghĩa-tài-khoản-hoạt-động-active-account-metric_mkt_active_account)
   - [11.6. Tài Khoản Mới Phát Sinh Trong Ngày (`METRIC_MKT_NEW_ACCOUNT`)](#116-tài-khoản-mới-phát-sinh-trong-ngày-metric_mkt_new_account)
   - [11.7. Giá Trị Giao Dịch Ròng BQ / Khách Hàng Hoạt Động (`METRIC_MKT_PROFIT_PER_CUSTOMER`)](#117-giá-trị-giao-dịch-ròng-bq-khách-hàng-hoạt-động-metric_mkt_profit_per_customer)
   - [11.8. Số Tiền Nộp BQ / Tài Khoản Phát Sinh Nộp (`METRIC_MKT_AVG_DEPOSIT_PER_ACCOUNT`)](#118-số-tiền-nộp-bq-tài-khoản-phát-sinh-nộp-metric_mkt_avg_deposit_per_account)
   - [11.9. Xác Định Môi Giới Trước Đó & Hiện Tại (`METRIC_KHMG_TRANSFER_HISTORY`)](#119-xác-định-môi-giới-trước-đó-hiện-tại-metric_khmg_transfer_history)
   - [11.10. Cờ Khách Hàng Chuyển Vào/Ra Môi Giới Online (`METRIC_KHMG_CUS_IN_OUT`)](#1110-cờ-khách-hàng-chuyển-vàora-môi-giới-online-metric_khmg_cus_in_out)
   - [11.11. Hiệu Suất Đầu Tư Danh Mục TVS (`METRIC_TVS_PERFORMANCE`)](#1111-hiệu-suất-đầu-tư-danh-mục-tvs-metric_tvs_performance)
   - [11.12. Khách Hàng Hoạt Động theo Giao Dịch (TVS) (`METRIC_TVS_ACTIVE_CUSTOMER`)](#1112-khách-hàng-hoạt-động-theo-giao-dịch-tvs-metric_tvs_active_customer)
   - [11.13. Tỷ Trọng Tiền Mặt / Tổng Tài Sản (`METRIC_TVS_CASH_ALLOCATION`)](#1113-tỷ-trọng-tiền-mặt-tổng-tài-sản-metric_tvs_cash_allocation)
   - [11.14. Xếp Hạng Khách Hàng theo GTGD Lũy Kế Tháng (`METRIC_TVS_RANK_GTGD`)](#1114-xếp-hạng-khách-hàng-theo-gtgd-lũy-kế-tháng-metric_tvs_rank_gtgd)
12. [BÁO CÁO TRADEPRO (KHỚP LỆNH, TÍN DỤNG & QUẢN TRỊ RỦI RO)](#12-báo-cáo-tradepro-khớp-lệnh-tín-dụng-quản-trị-rủi-ro)
   - [12.1. Số Khách Hàng Đã Kích Hoạt (`METRIC_TP_ACTIVE_CUSTOMER_COUNT`)](#121-số-khách-hàng-đã-kích-hoạt-metric_tp_active_customer_count)
   - [12.2. Biến Động NAV theo Ngày (`METRIC_TP_NAV_DOD_CHANGE`)](#122-biến-động-nav-theo-ngày-metric_tp_nav_dod_change)
   - [12.3. Phân Loại Cấp Bậc Môi Giới theo MINREVENUE (`METRIC_TP_BROKER_TYPE_CLASSIFICATION`)](#123-phân-loại-cấp-bậc-môi-giới-theo-minrevenue-metric_tp_broker_type_classification)
   - [12.4. Tăng Trưởng Phí Hoa Hồng Ròng theo Tháng (`METRIC_TP_COMMISSION_GROWTH_KPI`)](#124-tăng-trưởng-phí-hoa-hồng-ròng-theo-tháng-metric_tp_commission_growth_kpi)
   - [12.5. Số Ngày Làm Việc Thực Tế trong Tháng (`METRIC_TP_BUSINESS_DAYS_COUNT`)](#125-số-ngày-làm-việc-thực-tế-trong-tháng-metric_tp_business_days_count)
   - [12.6. Xác Định Môi Giới Point-in-Time (`METRIC_TP_POINT_IN_TIME_BROKER`) — *Canonical, dùng chung 6 báo cáo*](#126-xác-định-môi-giới-point-in-time-metric_tp_point_in_time_broker-canonical-dùng-chung-6-báo-cáo)
   - [12.7. Đường Dẫn Tổ Chức & RLS (`METRIC_TP_ORG_PATH_RLS`) — *Canonical*](#127-đường-dẫn-tổ-chức-rls-metric_tp_org_path_rls-canonical)
   - [12.8–12.9. Gán Môi Giới cho Call Margin & Force Sell (`METRIC_TP_CALLMARGIN_ATTRIBUTION`, `METRIC_TP_FORCESELL_ATTRIBUTION`)](#128129-gán-môi-giới-cho-call-margin-force-sell-metric_tp_callmargin_attribution-metric_tp_forcesell_attribution)
   - [12.10. Bảng Tra Cứu Chứng Khoán Đủ Điều Kiện Margin (`METRIC_TP_MARGIN_LOOKUP_TABLE`)](#1210-bảng-tra-cứu-chứng-khoán-đủ-điều-kiện-margin-metric_tp_margin_lookup_table)
   - [12.11. Hiệu Suất Time-Weighted Return (TWR) theo Tháng (`METRIC_TP_NAV_TWR_RETURN`)](#1211-hiệu-suất-time-weighted-return-twr-theo-tháng-metric_tp_nav_twr_return)
   - [12.12. Chỉ Số Hiệu Suất Đầu Tư Hàng Ngày (`METRIC_TP_ROI_DAILY_INDEX`)](#1212-chỉ-số-hiệu-suất-đầu-tư-hàng-ngày-metric_tp_roi_daily_index)
   - [12.13. NAV & Dư Nợ Bình Quân trên Khách Hàng Hoạt Động (`METRIC_TP_NAV_DEBT_PER_CUSTOMER`)](#1213-nav-dư-nợ-bình-quân-trên-khách-hàng-hoạt-động-metric_tp_nav_debt_per_customer)
   - [12.14. So Sánh Dư Nợ Gốc theo Tham Số Ngày (`METRIC_TP_DEBT_PARAM_COMPARISON`)](#1214-so-sánh-dư-nợ-gốc-theo-tham-số-ngày-metric_tp_debt_param_comparison)
   - [12.15. Ghép Hồ Sơ Khách Hàng 360° (`METRIC_TP_CUSTOMER_360_JOIN`)](#1215-ghép-hồ-sơ-khách-hàng-360-metric_tp_customer_360_join)
   - [12.16. Cờ Khách Hàng Hoạt Động & Có Giao Dịch (`METRIC_TP_CUSTOMER_ACTIVE_TRANS_FLAG`)](#1216-cờ-khách-hàng-hoạt-động-có-giao-dịch-metric_tp_customer_active_trans_flag)
   - [12.17. Hợp Nhất Luồng Nộp/Rút Tiền (`METRIC_TP_DEPOSIT_WITHDRAW_UNION`)](#1217-hợp-nhất-luồng-nộprút-tiền-metric_tp_deposit_withdraw_union)
   - [12.18. Đường Dẫn Tổ Chức 3 Nhánh cho Nộp Rút Tiền (`METRIC_TP_CASHFLOW_ORG_PATH`)](#1218-đường-dẫn-tổ-chức-3-nhánh-cho-nộp-rút-tiền-metric_tp_cashflow_org_path)

---

## 1. PHÂN HỆ 1: BÁO CÁO TỔNG QUAN

### 1.1. Dư nợ 12 tháng gần nhất & Đường tham chiếu trung bình

#### A. Công thức tính Dư nợ trung bình 12 tháng ($\overline{\text{Debt}}_{12\text{M}}$):
$$\overline{\text{Debt}}_{12\text{M}} = \frac{1}{12} \sum_{i=1}^{12} \text{Dư nợ tháng}_i$$

* **Ý nghĩa**: Đường màu đỏ nét đứt trên biểu đồ là một đường thẳng nằm ngang cố định bằng giá trị trung bình cộng của 12 tháng gần nhất, giúp nhận diện ngay tháng nào dư nợ đang vượt trên hoặc dưới mức bình quân năm.

#### B. Xác định Đỉnh dư nợ ($\text{Peak Debt}$):
$$\text{Peak Debt} = \max_{i=1..12} (\text{Dư nợ tháng}_i)$$

---

### 1.2. Hạn mức Margin & Hạn mức Ứng trước

#### A. Công thức Hạn mức Còn lại:
$$\text{Hạn mức Còn lại} = \text{Hạn mức Được cấp} - \text{Hạn mức Đã sử dụng}$$

$$\text{Tỷ lệ sử dụng Hạn mức (\%)} = \frac{\text{Hạn mức Đã sử dụng}}{\text{Hạn mức Được cấp}} \times 100\%$$

* **Hiển thị trên biểu đồ Donut**:
  * **Tâm biểu đồ**: Hiển thị 3 dòng: *Được cấp* $\rightarrow$ *Số tiền* $\rightarrow$ *nghìn tỷ*.
  * **Vòng tròn ngoài**: Phân tách rõ phần **Đã sử dụng** và **Còn lại**.

---

### 1.3. Tỷ trọng Dư nợ theo gói phí

#### Công thức tính Tỷ trọng (%):
$$\text{Tỷ trọng Dư nợ của Gói}_k = \frac{\text{Dư nợ gốc của Gói}_k}{\sum_{j=1}^{n} \text{Dư nợ gốc của Gói}_j} \times 100\%$$

* **Hiển thị trên biểu đồ thanh**:
  $$\text{Nhãn hiển thị} = \text{Dư nợ (tỷ đồng)} \ + \ \text{" ("} + \text{Tỷ trọng (\%)} + \text{")"}$$
  * *Ví dụ*: `1.765 tỷ (65,18%)` nghĩa là Gói Titan có dư nợ $1.765$ tỷ đồng, chiếm $65,18\%$ tổng nợ toàn công ty.

---

### 1.4. Xếp hạng & Tỷ lệ sử dụng Room Top 15 Cổ phiếu

#### A. Tỷ lệ sử dụng Room cổ phiếu:
$$\text{Tỷ lệ sử dụng Room}_i = \frac{\text{Room đã sử dụng}_i}{\text{Tổng Room được cấp tối đa}_i} \times 100\%$$

#### B. Xếp hạng Top 15:
$$\text{Thứ hạng (Rank)}_i = \operatorname{Rank}\Big(\text{Dư nợ mã}_i \Big) \quad (i \le 15)$$

---

### 1.5. NAV & CASA trung bình tháng

#### A. Tài sản ròng (NAV) trung bình ngày trong tháng:
$$\overline{\text{NAV}}_{\text{tháng}} = \frac{1}{N} \sum_{d=1}^{N} \text{Tổng NAV ngày}_d$$

#### B. Tiền gửi không kỳ hạn (CASA) trung bình ngày trong tháng:
$$\overline{\text{CASA}}_{\text{tháng}} = \frac{1}{N} \sum_{d=1}^{N} \text{Tổng số dư tiền gửi ngày}_d$$

---

### 1.6. Đánh giá Biến động so với Đỉnh

#### Công thức tính mức độ tăng giảm so với đỉnh lịch sử:
$$\Delta_{\text{so với đỉnh}} \text{ (\%)} = \frac{\text{Giá trị Hiện tại} - \text{Giá trị Đỉnh}}{\text{Giá trị Đỉnh}} \times 100\%$$

---

## 2. PHÂN HỆ 2: DANH MỤC CHO VAY & QUẢN TRỊ RỦI RO KHÁCH HÀNG

### 2.1. Tỷ lệ Đảm bảo Tài sản (TSR / GTCK)

#### Công thức:
$$\text{Tỷ lệ } \frac{\text{TSR}}{\text{GTCK}} = \frac{\text{Tài sản ròng (NAV)}}{\text{Tổng giá trị danh mục Chứng khoán}} \times 100\%$$

$$\text{Trong đó: } \quad \text{Tài sản ròng (NAV)} = \text{Tổng giá trị Chứng khoán} - \text{Tổng Dư nợ}$$

* **Ngưỡng an toàn**:
  * $\text{Tỷ lệ } \frac{\text{TSR}}{\text{GTCK}} \ge 40\%$: Tài khoản **An toàn**.
  * $\text{Tỷ lệ } \frac{\text{TSR}}{\text{GTCK}} < 30\%$: Rơi vào diện cảnh báo gọi ký quỹ (**Margin Call**).

---

### 2.2. Tỷ trọng Dư nợ Top 10 Khách hàng

#### Công thức:
$$\text{\% Top 10} = \frac{\sum_{k=1}^{10} \text{Dư nợ của Khách hàng}_k}{\text{Tổng Dư nợ toàn hệ thống}} \times 100\%$$

---

### 2.3. Đánh giá Thanh khoản & Số phiên giải chấp danh mục (Tooltip)

#### Công thức tính Số phiên xử lý danh mục ($T_{\text{xử lý}}$):
$$T_{\text{xử lý}} = \left\lceil \frac{\text{Khối lượng Cổ phiếu KH nắm giữ}}{\text{Thanh khoản Trung bình 10 phiên gần nhất (TKTBP 10P)}} \right\rceil$$

* **Đánh giá rủi ro thanh khoản**:
  * $T_{\text{xử lý}} \le 2 \text{ phiên}$: **Thanh khoản cao** $\rightarrow$ Dễ xử lý thu hồi nợ.
  * $T_{\text{xử lý}} > 5 \text{ phiên}$: **Thanh khoản kém / Cảnh báo rủi ro cao** $\rightarrow$ Cần nhiều phiên mới thanh lý hết.

---

### 2.4. Đánh giá Hành vi Vay: Vòng quay dư nợ & Mục đích sử dụng vốn (Tooltip)

#### A. Hệ số Vòng quay dư nợ ($V_{\text{nợ}}$):
$$V_{\text{nợ}} = \frac{\text{Tổng Giá trị Giao dịch trong kỳ (GTGD)}}{\text{Dư nợ Bình quân trong kỳ}}$$

#### B. Phân loại mục đích sử dụng vốn:
$$\text{Mục đích vay} = \begin{cases} \textbf{"Trading (Quay vòng)"} & \text{khi } V_{\text{nợ}} > 2 \\ \textbf{"Rút tiền"} & \text{khi } V_{\text{nợ}} \le 2 \end{cases}$$

---

### 2.5. Giám sát Room & Hạn mức Deal cho vay (MR3040)

$$\text{Tổng Dư nợ Còn lại} = \text{Tổng Hạn mức Dư nợ Deal (Max)} - \text{Tổng Dư nợ Đã giải ngân}$$
$$\text{Tổng Room Cổ phiếu Còn lại} = \text{Tổng Room Cho phép (Max)} - \text{Tổng Room Đã vay}$$

---

## 3. PHÂN HỆ 3: BÁO CÁO CHI TIẾT DƯ NỢ & QUẢN TRỊ RỦI RO HỆ THỐNG

### 3.1. Lãi suất Cho vay Bình quân Gia quyền (Toàn hệ thống & Theo nhóm)

#### A. Lãi suất bình quân toàn hệ thống ($\overline{r}_{\text{toàn sàn}}$):
$$\overline{r}_{\text{toàn sàn}} = \frac{\sum_{i=1}^{M} \text{Tiền lãi phát sinh trong năm}_i}{\sum_{i=1}^{M} \text{Dư nợ gốc}_i} = \frac{\sum_{i=1}^{M} \big(\text{Dư nợ}_i \times \text{Lãi suất}_i\big)}{\sum_{i=1}^{M} \text{Dư nợ}_i} \times 100\%$$

#### B. Lãi suất bình quân theo từng Phân nhóm sản phẩm ($\overline{r}_{\text{nhóm } k}$):
$$\overline{r}_{\text{nhóm } k} = \frac{\sum_{j \in \text{Nhóm } k} \big(\text{Dư nợ}_j \times \text{Lãi suất}_j\big)}{\sum_{j \in \text{Nhóm } k} \text{Dư nợ}_j} \times 100\%$$
*(Phân nhóm: **Deal**, **K-plus**, **K-pro**, **Vay 3 bên**, **Thường**)*

* **Ý nghĩa**: Giám sát biên độ sinh lời (Yield on Margin) và rủi ro điều chỉnh lãi suất cạnh tranh trên thị trường.

---

### 3.2. Hạn Mức Cho Vay (HMCV) Room Thường & HMCV Tổng

#### A. Hạn mức Cho vay Room thường ($\text{HMCV}_{\text{thường}}$):
$$\text{HMCV}_{\text{thường}} = \text{Giá chặn cho vay (Price)} \times \text{Tỷ lệ cho vay (\%)} \times \text{Room được cấp}$$
*(Nếu Room cấp $= 0$, tính dựa trên Room thực tế đã sử dụng)*.

#### B. Hạn mức Cho vay Tổng cộng ($\text{HMCV}_{\text{tổng}}$):
$$\text{HMCV}_{\text{tổng}} = \text{HMCV}_{\text{thường}} + \text{Hạn mức Dư nợ Deal vay 705}$$

---

### 3.3. Tỷ trọng Dư nợ theo Nhóm KH & Nhóm Chi tiết rủi ro

#### A. Tỷ trọng theo Nhóm Khách Hàng:
$$\text{Tỷ trọng Nhóm}_k = \frac{\text{Tổng Dư nợ Nhóm}_k}{\text{Tổng Dư nợ Toàn hệ thống}} \times 100\%$$

#### B. Phân loại mức độ đòn bẩy chi tiết:
* **K-plus tỉ lệ cao**: Nhóm tài khoản K-plus được cấp tỷ lệ đòn bẩy vượt khung chuẩn (`klpus = 'Y'`).
* **K-pro đòn bẩy cao**: Nhóm tài khoản K-pro áp dụng chính sách đòn bẩy mở rộng (`kpro = 'Y'`).
* **Deal**: Khách hàng thỏa thuận hạn mức riêng (`private_policy = 'Y'`).
* **Vay 3 bên**: Tài khoản ký quỹ liên kết đối tác ngân hàng tài trợ vốn (`acctype = '3001'`).

---

### 3.4. Tỷ lệ Tài khoản Giao dịch Ký quỹ (TKGDKQ vs None)

$$\text{Tỷ lệ TK có Dư nợ (\%)} = \frac{\text{Số lượng TK có phát sinh Dư nợ}}{\text{Tổng số lượng TK ký quỹ trên hệ thống}} \times 100\%$$
$$\text{Tỷ lệ TK Không Dư nợ (\%)} = \frac{\text{Số lượng TK Dư nợ } = 0}{\text{Tổng số lượng TK ký quỹ trên hệ thống}} \times 100\%$$

---

### 3.5. Phân nhóm Xếp hạng Cổ phiếu (Rank A, B, C)

$$\text{Số lượng Mã theo Phân nhóm} = \begin{cases} 
\text{Tổng số mã trong danh mục Room} & (\text{Nhóm 1}) \\ 
\text{Số mã Rank A có phát sinh Dư nợ} & (\text{Nhóm 2 - Cổ phiếu đầu ngành, rủi ro thấp}) \\ 
\text{Số mã Rank B có phát sinh Dư nợ} & (\text{Nhóm 3 - Cổ phiếu trung bình}) \\ 
\text{Số mã Rank C có phát sinh Dư nợ} & (\text{Nhóm 4 - Cổ phiếu đầu cơ/rủi ro cao}) 
\end{cases}$$

* **Ý nghĩa Quản trị Rủi ro**: Giữ tỷ trọng cho vay tập trung chủ yếu ở **Rank A** ($\ge 70\%$), giới hạn nghiêm ngặt tỷ trọng ở **Rank C** để tránh rủi ro vỡ nợ diện rộng khi thị trường giảm sâu.

---

---

## 4. PHÂN HỆ QUẢN TRỊ RỦI RO: BÁO CÁO THEO DÕI NỢ BẢO LÃNH T0

---

## 5. PHÂN HỆ GIAO DỊCH - DASHBOARD OVERVIEW (BCGD)

### 5.1. Bộ 5 Chỉ Số KPI Tổng Quan & Sparklines Xu Hướng (`METRIC_GD_KPI_SUMMARY_SPARKLINES`)
* **Mục đích:** Giám sát 5 chỉ tiêu trọng yếu toàn công ty: Thị phần (%), Dư Nợ, Giá Trị Giao Dịch, Phí Giao Dịch Ròng tính Hoa hồng (1.098M, -75,00% MoM) và Số lượng tài khoản mở mới (86 TK, -68,95% MoM).
* **Công thức toán học:**
  $$\text{Thị phần DSC (\%)} = \frac{\text{GTGD DSC}}{\text{Tổng GTGD toàn thị trường}} \times 100\%$$
* **Power BI DAX:** `[Market Share - DSC Percent MTD Axis]`, `[HH - Total Current]`.

### 5.2. Ma Trận Lịch Biến Động GTGD 30 Ngày (Calendar Heatmap) (`METRIC_GD_CALENDAR_HEATMAP_30D`)
* **Mục đích:** Biểu đồ nhiệt theo lưới Tuần × Thứ trong tuần thể hiện nhịp biến động thanh khoản (Xanh ngọc: bùng nổ, Hồng đỏ: suy giảm, Xám: trung bình).
* **Power BI DAX:** `[GTGD_Heatmap_30D]`, `[Color_Heatmap_GTGD]`.

### 5.3. Bảng Phân Bổ Hiệu Suất Theo Chi Nhánh (`METRIC_GD_BRANCH_PERFORMANCE_MATRIX`)
* **Mục đích:** Đánh giá đóng góp của 4 chi nhánh: Dịch Vọng Hậu (645B GTGD, 666M PGDR), Hàm Long (272B GTGD, 249M PGDR), Đà Nẵng (135B GTGD, 158M PGDR), Nguyễn Văn Trỗi (28B GTGD, 35M PGDR).

### 5.4. Cơ Chế Chuyển Đổi Chỉ Số Động 3 Cấp Quản Lý (`METRIC_GD_DYNAMIC_DRILLDOWN_LEVELS`)
* **Mục đích:** Chuyển đổi linh hoạt giữa `NAV` | `Dư Nợ` | `GTGD` để phân rã 3 cấp quản lý (Giám đốc, Trưởng phòng, Môi giới).
* **Power BI DAX:** `[Details - Selected Metric Label]`, `[Details - Selected Metric Value]`.

### 5.5. Phí Giao Dịch Ròng Tính Hoa Hồng & View Chuyên Sâu (`METRIC_GD_PGDR_COMMISSION_VIEW`)
* **Mục đích:** Chế độ chuyên biệt theo dõi doanh thu phí hoa hồng 3 cấp quản lý khi bấm nút `Xem PGDR tính HH` / `Quay lại`.
* **Power BI DAX:** `[HH - Manager Current]`, `[HH - Department Current]`, `[HH - Broker Current]`.

## 6. CHỈ SỐ GIAO DỊCH BỔ SUNG: GTGD MTD, TĂNG TRƯỞNG & THỊ PHẦN

> 🌐 **Power BI Service Live Report:** [https://app.powerbi.com/groups/a7a765cc-c54e-42a3-b019-e19490c54e11/reports/5b9f1e5c-ffd9-4699-b5ed-944e75f83ba9/7b17e6d6630c4cb98d01?experience=power-bi](https://app.powerbi.com/groups/a7a765cc-c54e-42a3-b019-e19490c54e11/reports/5b9f1e5c-ffd9-4699-b5ed-944e75f83ba9/7b17e6d6630c4cb98d01?experience=power-bi)


### 6.1. Giá trị giao dịch MTD (Month-To-Date)

$$\text{GTGD}_{\text{MTD}} = \sum_{d = 1}^{\text{Ngày chọn}} \text{GTGD trong ngày}_d$$

---

### 6.2. Tốc độ Tăng trưởng MoM (Month-over-Month) & YoY (Year-over-Year)

#### A. Tăng trưởng so với tháng trước ($\text{Growth}_{\text{MoM}}$):
$$\text{Growth}_{\text{MoM}} \text{ (\%)} = \frac{\text{GTGD Tháng này} - \text{GTGD Tháng trước}}{\text{GTGD Tháng trước}} \times 100\%$$

#### B. Tăng trưởng so với cùng kỳ năm trước ($\text{Growth}_{\text{YoY}}$):
$$\text{Growth}_{\text{YoY}} \text{ (\%)} = \frac{\text{GTGD Kỳ này} - \text{GTGD Cùng kỳ năm trước}}{\text{GTGD Cùng kỳ năm trước}} \times 100\%$$

---

### 6.3. Tỷ lệ Thị phần Công ty (Market Share)

$$\text{Thị phần DSC (MS)} = \frac{\text{Tổng GTGD của DSC}}{\text{Tổng GTGD Toàn Thị trường (HOSE + HNX + UPCOM)}} \times 100\%$$

---

## 7. BẢNG TỔNG HỢP CÔNG THỨC & QUY TẮC ĐÁNH GIÁ TOÀN DIỆN

| Tên Chỉ số | Phân Hệ | Công thức Toán học | Quy tắc Đánh giá / Ngưỡng Cảnh báo |
| :--- | :--- | :--- | :--- |
| **Dư nợ TB 12T** | Tổng quan | $\overline{\text{Debt}} = \frac{1}{12}\sum_{i=1}^{12} \text{Debt}_i$ | So sánh xem tháng hiện tại đang trên hay dưới mức nợ bình quân năm. |
| **Hạn mức Còn lại** | Tổng quan | $\text{Room}_{\text{còn lại}} = \text{Room}_{\text{cấp}} - \text{Nợ}_{\text{đã dùng}}$ | Khi Room còn lại $< 10\% \rightarrow$ Cảnh báo sắp hết room giải ngân. |
| **Tỷ trọng Gói phí** | Tổng quan | $\text{Tỷ trọng}_k = \frac{\text{Nợ Gói}_k}{\sum \text{Nợ}} \times 100\%$ | Nhận diện gói sản phẩm tài chính chiếm ưu thế nhất. |
| **Tỷ lệ TSR / GTCK** | Danh mục cho vay | $\text{TSR / GTCK} = \frac{\text{Tài sản ròng}}{\text{Giá trị CK}} \times 100\%$ | $\ge 40\%$: An toàn \| $< 30\%$: Chạm ngưỡng cảnh báo Margin Call. |
| **Số phiên giải chấp** | Danh mục cho vay | $T_{\text{xử lý}} = \left\lceil \frac{\text{Khối lượng CP}}{\text{TKTBP 10 phiên}} \right\rceil$ | $\le 2$ phiên: Dễ thanh lý \| $> 5$ phiên: Thanh khoản yếu, rủi ro cao. |
| **Vòng quay Dư nợ** | Danh mục cho vay | $V_{\text{nợ}} = \frac{\text{Tổng GTGD}}{\text{Dư nợ TB}}$ | $> 2 \rightarrow$ **Trading** (Quay vòng) \| $\le 2 \rightarrow$ **Rút tiền** (Không GD). |
| **Lãi suất TB Gia quyền** | Quản trị rủi ro | $\overline{r} = \frac{\sum (\text{Debt} \times \text{Rate})}{\sum \text{Debt}} \times 100\%$ | Theo dõi tỷ suất lợi nhuận biên lãi vay (Yield) của công ty. |
| **HMCV Tổng cộng** | Quản trị rủi ro | $\text{HMCV}_{\text{tổng}} = \text{HMCV}_{\text{thường}} + \text{Hạn mức Deal}$ | Đo lường năng lực cấp vốn tối đa theo danh mục được phê duyệt. |
| **Xếp hạng Cổ phiếu** | Quản trị rủi ro | $\text{Phân nhóm: Rank A / B / C}$ | Đảm bảo dư nợ tập trung $\ge 70\%$ ở Rank A, siết chặt Rank C. |
| **Tăng trưởng MoM** | Giao dịch | $\text{MoM} = \frac{\text{Kỳ này} - \text{Tháng trước}}{\text{Tháng trước}} \times 100\%$ | Xanh khi $\ge 0\%$, Đỏ khi $< 0\%$. |
| **Thị phần (MS)** | Giao dịch | $\text{MS} = \frac{\text{GTGD}_{\text{DSC}}}{\text{GTGD}_{\text{Thị trường}}} \times 100\%$ | Đo lường tỷ trọng đóng góp của công ty trên toàn sàn. |
| **Biến động so với đỉnh** | Chung | $\Delta = \frac{\text{Hiện tại} - \text{Đỉnh}}{\text{Đỉnh}} \times 100\%$ | Đo khoảng cách sụt giảm từ mức cao nhất lịch sử. |

---

## 8. BÁO CÁO TỔNG HỢP DƯ NỢ THEO MÃ CHỨNG KHOÁN (MR0031)

### 8.1. Dư nợ quy đổi theo mã chứng khoán & Ngưỡng chặn trần 240 tỷ VNĐ (`METRIC_MR0031_CONVERTED_DEBT`)
* **Mục đích:** Giám sát quy mô dư nợ Margin và tài trợ tài chính theo từng mã cổ phiếu, kiểm soát rủi ro tập trung vốn với mức trần tối đa 240 tỷ VNĐ/mã.
* **Công thức toán học:**
  $$\text{Dư nợ quy đổi} = \min\left(\sum \text{Dư nợ gốc},\; 240.000.000.000\text{ đ}\right)$$
* **Tableau:** `{ FIXED [dim_datetime_id], [ticker] : IF SUM([du_no_quy_doi_final]) > 240000000000 THEN 240000000000 ELSE SUM([du_no_quy_doi_final]) END }`
* **Power BI DAX:**
  ```dax
  DuNo_QuyDoi_Final = 
  VAR RawDebt = SUM(f_MR0031_Detail[du_no_quy_doi_final])
  VAR CapCeiling = 240000000000
  RETURN IF(ISBLANK(RawDebt), 0, IF(RawDebt > CapCeiling, CapCeiling, RawDebt))
  ```

### 8.2. Khối lượng đánh dấu cổ phiếu ký quỹ & Ngưỡng chặn trần 5% cổ phiếu lưu hành (`METRIC_MR0031_MARKED_VOLUME`)
* **Mục đích:** Kiểm soát tổng khối lượng cổ phiếu phong tỏa đánh dấu cho vay không vượt quá 5% tổng lượng cổ phiếu lưu hành của doanh nghiệp niêm yết theo quy chế UBCKNN.
* **Công thức toán học:**
  $$\text{Khối lượng đánh dấu} = \operatorname{INT}\left(\min\left(\sum \text{KL đánh dấu gốc},\; \overline{\text{Số CP lưu hành}} \times 5\%\right)\right)$$
* **Tableau:** `INT({ FIXED [dim_datetime_id], [ticker]: IF SUM([kl_danh_dau_cuoi_cung]) >= AVG([outstanding_shares])*0.05 THEN AVG([outstanding_shares])*0.05 ELSE SUM([kl_danh_dau_cuoi_cung]) END })`
* **Power BI DAX:**
  ```dax
  KhoiLuong_DanhDau = 
  VAR RawVol = SUM(f_MR0031_Detail[kl_danh_dau_cuoi_cung])
  VAR Cap5Pct = AVERAGE(d_Stock_Overview[outstanding_shares]) * 0.05
  RETURN IF(ISBLANK(RawVol), 0, INT(IF(RawVol >= Cap5Pct && Cap5Pct > 0, Cap5Pct, RawVol)))
  ```

### 8.3. Tỷ lệ cho vay ký quỹ áp dụng & Ngoại lệ mã SAM (`METRIC_MR0031_MARGIN_RATE`)
* **Mục đích:** Quản lý tỷ lệ cho vay ký quỹ áp dụng cho từng mã thuộc rổ MR01 (50%, 40%, 30%), xử lý ngoại lệ quy định gán SAM = 30%.
* **Công thức toán học:**
  $$\text{Tỷ lệ vay (\%)} = \operatorname{INT}\left(\overline{\begin{cases} 30\%, & \text{nếu ticker} = \text{'SAM'} \\ \text{Tỷ lệ vay danh mục}, & \text{các mã khác} \end{cases}}\right)$$
* **Tableau:** `INT(AVG(IF [ticker] = 'SAM' THEN 30 ELSE [margin_loan_rate] END))`
* **Power BI DAX:**
  ```dax
  TyLe_Vay_Final = 
  VAR CurrentTicker = SELECTEDVALUE(d_Ticker[ticker])
  RETURN IF(CurrentTicker = "SAM", 30, INT(AVERAGE(f_Credit_Line[margin_loan_rate])))
  ```

### 8.4. Ma trận dư nợ theo mã & Bộ lọc trượt đa chiều Range Sliders (`METRIC_MR0031_MATRIX_GRID_FILTER`)
* **Mục đích:** Bảng ma trận tổng hợp 21 mã cổ phiếu chủ chốt với bộ 3 Range Sliders đầu cột (Dư nợ 0-240B, Khối lượng 0-31.58M CP, Tỷ lệ 0-50%) và chức năng tìm kiếm `Search table`.

---

## 9. BÁO CÁO ĐỐI SOÁT TIN NHẮN SMS (IT VẬN HÀNH)

### 9.1. Tổng Sản Lượng Tin Nhắn & Tỷ Lệ Gửi Thành Công (`METRIC_SMS_TOTAL_SUCCESS_RATE`)
* **Mục đích:** Giám sát chất lượng dịch vụ SMS Gateway: Tổng tin phát sinh (`2.781` SMS), tin gửi thành công (`2.277` SMS, đạt **81,88%**) và tin lỗi (`504` SMS, chiếm **18,12%**).
* **Công thức toán học:**
  $$\text{Tỷ lệ thành công (\%)} = \frac{\operatorname{COUNT}(\text{Tin thành công})}{\text{Tổng tin nhắn}} \times 100\%$$
* **Power BI DAX:** `[SMS_Total_Messages]`, `[SMS_Success_Messages]`, `[SMS_Success_Rate_Pct]`.

### 9.2. Phân Bổ Sản Lượng Theo Đơn Vị Cung Cấp Cổng Dịch Vụ (`METRIC_SMS_PROVIDER_DISTRIBUTION`)
* **Mục đích:** Đối soát chi phí và tải viễn thông giữa các đối tác: Cổng **V2M** (1.931 tin, chiếm **69,43%**) và **VNPAY** (850 tin, chiếm **30,57%**).

### 9.3. Phân Bổ Tin Nhắn Theo Nhà Mạng Telco (`METRIC_SMS_TELCO_BREAKDOWN`)
* **Mục đích:** Thống kê định tuyến theo nhà mạng: **Không xác định** (1.405 tin), **Viettel** (887 tin), **Vinaphone** (288 tin).

### 9.4. Phân Loại Trạng Thái & Danh Mục Mã Lỗi Kỹ Thuật (`METRIC_SMS_STATUS_ERROR_TAXONOMY`)
* **Mục đích:** Bóc tách hơn 50 mã lỗi Gateway thành 4 nhóm nghiệp vụ chính: Thuê bao (005, 01), Mẫu tin nhắn (011, 010), Timeout hạ tầng (08, 05).

### 9.5. Xu Hướng Sản Lượng Tin Nhắn Lũy Kế Theo Tháng (`METRIC_SMS_MONTHLY_RUNNING_TREND`)
* **Mục đích:** Diễn biến 9 tháng năm 2024 (Đỉnh tháng 1/2024 đạt 1.341 SMS; tháng 2 đạt 428 SMS; tháng 4 đạt 376 SMS).

---

## 10. BÁO CÁO TIẾN ĐỘ DỰ ÁN CNTT (KHỐI CNTT - PMO)

### 10.1. Tổng Quan Danh Mục & Trạng Thái / Ưu Tiên (`METRIC_CNTT_PORTFOLIO_OVERVIEW`)
* **Mục đích:** Giám sát 17 dự án CNTT chiến lược: Hoàn thành **58,82%** (10 dự án Done), đang triển khai **41,18%** (7 dự án In Progress); trong đó **82,35%** dự án thuộc mức ưu tiên High.
* **Công thức toán học:**
  $$\text{Tỷ lệ Hoàn thành (\%)} = \frac{\operatorname{COUNTIFS}(\text{Trạng thái} = \text{'Done'})}{\text{Tổng số dự án}} \times 100\%$$
* **Power BI DAX:** `[CNTT_Total_Projects]`, `[CNTT_Done_Projects]`, `[CNTT_Done_Rate_Pct]`.

### 10.2. Phân Loại Dự Án & Phân Bổ Bộ Phận Phụ Trách (`METRIC_CNTT_PROJECT_TYPE_DISTRIBUTION`)
* **Mục đích:** Đánh giá cơ cấu loại dự án (Tư vấn số 41,2%, Core Flex 35,3%, Tài chính số 23,5%) và tải công việc của các phòng ban (IT chủ trì 3 dự án độc lập).

### 10.3. Bảng Theo Dõi Tiến Độ Toàn Diện & Kế Hoạch Golive (`METRIC_CNTT_PROJECT_TIMELINE_PROGRESS`)
* **Mục đích:** Ma trận tiến độ theo dõi ngày bắt đầu, ngày golive và thanh tiến độ hoàn thành gradient màu xanh lá (Thực tập số 25%, WE DEMO 37%, Cập nhật VAT 39,8%, App Forum 94%, KRX 100%).

### 10.4. Mô Hình Phân Rã Milestone Trọng Số & Tiến Độ Thực Tế (`METRIC_CNTT_MILESTONE_WEIGHTED_PROGRESS`)
* **Mục đích:** Bóc tách 11 milestone chuẩn hóa (Phát triển 39%, Phân tích yêu cầu 15%, QA/SIT 10%, UAT 10%...). Tiến độ thực tế = $\sum (\text{Tỉ trọng}_i \times \text{Tiến độ}_i)$.

### 10.5. Đối Soát Tiến Độ Thực Tế vs Tiến Độ Kế Hoạch (`METRIC_CNTT_PLANNED_VS_ACTUAL_GAP`)
* **Mục đích:** Cặp biểu đồ Donut Gauge đối soát: **TIẾN ĐỘ THỰC TẾ** (100,00% - Donut Xanh Lá) vs **TIẾN ĐỘ THEO KẾ HOẠCH** (15,00% - Donut Xanh Dương) tại ngày kiểm soát `01/08/2025`.

---

## 11. BÁO CÁO ESERVICE (CORE FLEX EKYC & QUẢN LÝ KHÁCH HÀNG)

### 11.1. Phân Loại Kênh Mở & Kích Hoạt TKGDCK (`METRIC_EKYC_PLATFORM_CHANNEL`)
* **Mục đích:** Xác định khách hàng khởi tạo/kích hoạt hồ sơ eKYC trên nền tảng App hay Web.
* **Công thức:** $$\text{Kênh} = \begin{cases} \text{"App"} & \text{platform} = \text{"A"} \ \text{"Web"} & \text{platform} = \text{"W"} \end{cases}$$

### 11.2. Chuẩn Hóa Trạng Thái Tài Khoản eKYC (`METRIC_EKYC_STATUS_MAPPING`)
* **Mục đích:** Ánh xạ 9 mã trạng thái CUSTODYCD (A/C/B/R/E/N/T/G/I) sang nhãn tiếng Việt.

### 11.3. Chuẩn Hóa Bước Hành Trình Mở TKGDCK (`METRIC_EKYC_JOURNEY_STEP`)
* **Mục đích:** Chuẩn hóa số bước (step) thành mã B0x có độ dài cố định để sắp xếp đúng thứ tự funnel.
* **Công thức:** $$\text{Step_format} = \begin{cases} \text{"B0"} + \text{step} & \text{step} \lt 10 \ \text{"B"} + \text{step} & \text{step} \ge 10 \end{cases}$$

### 11.4. Quy Tắc Ưu Tiên Nguồn Định Danh Khách Hàng (`METRIC_EKYC_IDENTITY_FALLBACK`)
* **Mục đích:** Khi custody_id tracking chưa khớp CUSTODYCD trên Core, ưu tiên lấy Họ tên/CCCD/Email/SĐT từ dữ liệu tracking; ngược lại lấy từ Core.

### 11.5. Định Nghĩa Tài Khoản Hoạt Động (Active Account) (`METRIC_MKT_ACTIVE_ACCOUNT`)
* **Mục đích:** Một tài khoản được tính "Hoạt động" nếu Total NAV (NAV + Dư nợ vay) &ge; 50 triệu đồng.

### 11.6. Tài Khoản Mới Phát Sinh Trong Ngày (`METRIC_MKT_NEW_ACCOUNT`)
* **Mục đích:** Đếm tài khoản có ngày mở (open_date) trùng ngày báo cáo.

### 11.7. Giá Trị Giao Dịch Ròng BQ / Khách Hàng Hoạt Động (`METRIC_MKT_PROFIT_PER_CUSTOMER`)
* **Công thức:** $$\text{Profit/Cus} = \frac{\text{Net Trans Value lũy kế tháng}}{\text{Số TK Active đầu tháng}}$$

### 11.8. Số Tiền Nộp BQ / Tài Khoản Phát Sinh Nộp (`METRIC_MKT_AVG_DEPOSIT_PER_ACCOUNT`)
* **Mục đích:** Lũy kế số tiền nộp trong kỳ chia số tài khoản duy nhất có phát sinh nộp (không đếm trùng).

### 11.9. Xác Định Môi Giới Trước Đó & Hiện Tại (`METRIC_KHMG_TRANSFER_HISTORY`)
* **Mục đích:** Dùng LAG/LEAD trên broker_from_date theo từng khách hàng để dựng lại lịch sử điều chuyển môi giới.

### 11.10. Cờ Khách Hàng Chuyển Vào/Ra Môi Giới Online (`METRIC_KHMG_CUS_IN_OUT`)
* **Công thức:** $$\text{cus_in/out} = \text{so sánh pre_broker với dim_broker_id hiện tại quanh mã môi giới Online } \text{'0001999018'}$$

### 11.11. Hiệu Suất Đầu Tư Danh Mục TVS (`METRIC_TVS_PERFORMANCE`)
* **Công thức:** $$\text{Hiệu suất} = \frac{\sum \text{Giá vốn} - \sum \text{Giá trị ban đầu}}{\sum \text{Giá trị ban đầu}}$$

### 11.12. Khách Hàng Hoạt Động theo Giao Dịch (TVS) (`METRIC_TVS_ACTIVE_CUSTOMER`)
* **Mục đích:** custody_code được tính vào COUNTD nếu total_tta > 0.

### 11.13. Tỷ Trọng Tiền Mặt / Tổng Tài Sản (`METRIC_TVS_CASH_ALLOCATION`)
* **Công thức:** $$\text{Percentage Cash/Total} = \frac{\sum \text{Tiền mặt}}{\sum \text{Tiền mặt} + \sum \text{NAV_Current}}$$

### 11.14. Xếp Hạng Khách Hàng theo GTGD Lũy Kế Tháng (`METRIC_TVS_RANK_GTGD`)
* **Công thức:** $$\text{Rank GTGD} = \operatorname{\text{RANK_DENSE}}(\sum \text{GTGD lũy kế tháng}, \text{desc})$$

> Chi tiết đầy đủ 8 tab (Nghiệp vụ, Data, DAX, Tableau, Diff, SQL, Test Cases, MCP JSON) của 14 chỉ số trên xem tại `index.html` mục **EService**. EService hiện chưa migrate sang Power BI nên cột DAX/Diff ghi "Chưa migrate".

---

## 12. BÁO CÁO TRADEPRO - KHỐI KINH DOANH TVĐT (10 BÁO CÁO CHUẨN HÓA)

Hệ thống báo cáo TradePro phục vụ chính thức cho **Khối Kinh doanh TVĐT (Tư vấn đầu tư)** gồm 10 báo cáo chuẩn hóa được phân cấp theo STT và tần suất cập nhật:

| STT | Tên Báo Cáo Chuẩn | Phòng Ban Thụ Hưởng | Tần Suất Cập Nhật | Bảng Nguồn Dữ Liệu Chính |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **V2.3_TradePro_Báo cáo Overview** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `mart_broker.customer_nav`, `customer_loan`, `mart_commission.*` |
| **2** | **Prod_tradPro_Baocaodunov2.2** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `mart_broker.customer_loan` *(Log cả ngày nghỉ)* |
| **3** | **Prod_TradePro_Báo cáo NAV v2.1** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `mart_broker.customer_nav` *(Không log ngày nghỉ)* |
| **4** | **Prod_TradePro_Báo cáo nộp rút tiền v2.3** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `fact.report_cash_deposit`, `report_cash_withdrawal` |
| **5** | **Prod_TradePro_Báo cáo tổng hợp doanh số v2.2** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `mart_commission.temp_final_commission_fee_*`, `report_order_trans` |
| **6** | **TradePro_Báo cáo danh mục khách hàng V1.3** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `realtime.cfmast`, `customer_roi_twr`, `bufciaccount`, `customer_portfolio` |
| **7** | **Prod_TradePro_Tra cứu danh mục margin realtime v2.1** | Khối Kinh doanh TVĐT | 10 phút/lần (Realtime) | `realtime.securities_info/risk`, `secbasket`, `afpralloc` |
| **8** | **Prod_TradePro_Báo cáo danh sách call margin v2.1** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `fact.report_margin_call`, `dim.broker_path_new` |
| **9** | **Prod_TradePro_Báo cáo danh sách force sell v2.1** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `fact.report_margin_force_sell`, `dim.broker_path_new` |
| **10** | **Prod_TradePro_Báo cáo danh sách chưa xác nhận lệnh v2.1** | Khối Kinh doanh TVĐT | Hàng ngày (T-1) | `fact.report_order_confirmed`, `dim.broker_path_new` |

### 12.0. Lưu Ý Vận Hành Dữ Liệu Cốt Lõi (Operational Caveats)
1. **Dư nợ (`mart_broker.customer_loan`):** Có log cả ngày nghỉ (thứ 7, CN, ngày lễ vẫn ghi log chốt lãi và dư nợ). Cần kiểm tra dữ liệu update không bị miss ngày.
2. **NAV (`mart_broker.customer_nav`):** KHÔNG log vào ngày nghỉ. Khi xử lý dữ liệu tính chuỗi thời gian hoặc lấy giá trị T-1 cần bỏ qua ngày nghỉ để tránh lỗi NULL hoặc mất dữ liệu.
3. **Tăng trưởng khách hàng:** Căn cứ vào ngày mở tài khoản `OPNDATE` trong bảng `realtime.cfmast`.
4. **Luồng dữ liệu Môi giới:**
   * Dữ liệu cấp MG trở lên lấy từ API 1Office; Cấp CTV lấy từ Core DB Oracle (kiểm tra trên Pam).
   * Hợp nhất qua `broker.py` (pull git prod về để validate nếu gặp lỗi).
   * Khi sửa code gốc: chạy trước trên `broker_added.py` &rarr; `stg.broker_added` và `stg.broker_org_added` kiểm tra trước khi yêu cầu DE merge code.
   * `dim.broker` + `dim.broker_org` &rarr; `dim.broker_path_new` (bảng chính phân quyền dữ liệu RLS).
5. **Luồng tính doanh số 3 cấp (`mart_commission`):**
   * Doanh số MG: `call_table_final_commission_fee_broker` &rarr; `temp_final_commission_fee_broker`.
   * Doanh số Trưởng phòng: `call commission_fee_department` &rarr; `temp_final_commission_fee_department`.
   * Doanh số Giám đốc: `call commission_fee_manager` &rarr; `temp_final_commission_fee_manager`.
   * Tài liệu chi tiết Confluence: [Confluence DSC Page 110330509](https://confluence.dsc.com.vn/pages/viewpage.action?pageId=110330509).

### 12.1. Số Khách Hàng Đã Kích Hoạt (`METRIC_TP_ACTIVE_CUSTOMER_COUNT`)
* **Công thức:** $$\text{KH đã kích hoạt} = \operatorname{COUNTD}(\text{dim_cus_id} \mid \text{CUSTATUS}=\text{'A'} \text{ AND STATUS}=\text{'A'})$$

### 12.2. Biến Động NAV theo Ngày (`METRIC_TP_NAV_DOD_CHANGE`)
* **Công thức:** $$\%\text{DoD NAV} = \frac{\text{NAV}_t - \text{NAV}_{\text{first}}}{|\text{NAV}_{\text{first}}|}$$

### 12.3. Phân Loại Cấp Bậc Môi Giới theo MINREVENUE (`METRIC_TP_BROKER_TYPE_CLASSIFICATION`)
* **Công thức:** $$\text{br_type} = \begin{cases} \text{"GD"} & \text{MINREVENUE = NULL} \ \text{"TPMG"} & \text{MINREVENUE = 60tr} \ \text{"MG"} & \text{MINREVENUE = 15tr} \ \text{"CTV"} & \text{MINREVENUE = 0} \ \text{"Đóng"} & \text{ngược lại} \end{cases}$$

### 12.4. Tăng Trưởng Phí Hoa Hồng Ròng theo Tháng (`METRIC_TP_COMMISSION_GROWTH_KPI`)
* **Công thức:** $$\text{growth_kpi} = \frac{\text{commission_net_trans_value}}{\operatorname{LEAD}(\text{commission_net_trans_value})} - 1$$

### 12.5. Số Ngày Làm Việc Thực Tế trong Tháng (`METRIC_TP_BUSINESS_DAYS_COUNT`)
* **Mục đích:** Đếm ngày loại trừ cuối tuần & ngày lễ (dsc_mst_holiday), dùng cho pace-adjusted run-rate.

### 12.6. Xác Định Môi Giới Point-in-Time (`METRIC_TP_POINT_IN_TIME_BROKER`) — *Canonical, dùng chung 6 báo cáo*
* **Công thức:** $$\text{Môi giới tại ngày } d = \text{dim_broker_id} \mid d \in [\text{broker_from_date}, \text{broker_to_date})$$

### 12.7. Đường Dẫn Tổ Chức & RLS (`METRIC_TP_ORG_PATH_RLS`) — *Canonical*
* **Mục đích:** Ghép path_mg 5 cấp (root→chi nhánh→trưởng phòng→môi giới) + 2 override theo branch_code 0002/0003, dùng cho Row-Level Security.

### 12.8–12.9. Gán Môi Giới cho Call Margin & Force Sell (`METRIC_TP_CALLMARGIN_ATTRIBUTION`, `METRIC_TP_FORCESELL_ATTRIBUTION`)
* **Mục đích:** Áp dụng cơ chế 12.6/12.7 lên fact.report_margin_call / fact.report_margin_force_sell.

### 12.10. Bảng Tra Cứu Chứng Khoán Đủ Điều Kiện Margin (`METRIC_TP_MARGIN_LOOKUP_TABLE`)
* **Mục đích:** Danh mục realtime các mã đủ điều kiện ký quỹ cho KH phổ thông — không có công thức tổng hợp.

### 12.11. Hiệu Suất Time-Weighted Return (TWR) theo Tháng (`METRIC_TP_NAV_TWR_RETURN`)
* **Công thức:** $$r_t = \frac{\text{NAV}_t - \text{NAV}_{t-1} - \text{CF}_t}{\text{NAV}_{t-1} + \max(\text{CF}_t,0)} \qquad \text{TWR} = \exp\Big(\sum_t \ln(1+r_t)\Big) - 1$$

### 12.12. Chỉ Số Hiệu Suất Đầu Tư Hàng Ngày (`METRIC_TP_ROI_DAILY_INDEX`)
* **Công thức:** $$\text{indexx}_t = \frac{\text{end_stock}_t + \text{sell}_t}{\text{stock_amount}_t + \text{buy}_t}$$

### 12.13. NAV & Dư Nợ Bình Quân trên Khách Hàng Hoạt Động (`METRIC_TP_NAV_DEBT_PER_CUSTOMER`)
* **Công thức:** $$\text{NAV/KH} = \frac{\sum \text{NAV}}{\text{Số KH Hoạt động}}$$

### 12.14. So Sánh Dư Nợ Gốc theo Tham Số Ngày (`METRIC_TP_DEBT_PARAM_COMPARISON`)
* **Mục đích:** So sánh Dư nợ gốc tại ngày người dùng chọn (Parameter) với ngày giao dịch gần nhất trước đó.

### 12.15. Ghép Hồ Sơ Khách Hàng 360° (`METRIC_TP_CUSTOMER_360_JOIN`)
* **Mục đích:** LEFT JOIN cfmast với snapshot mới nhất của customer_loan/customer_nav/broker_path_new + GTGD tháng hiện tại.

### 12.16. Cờ Khách Hàng Hoạt Động & Có Giao Dịch (`METRIC_TP_CUSTOMER_ACTIVE_TRANS_FLAG`)
* **Công thức:** $$\text{Active Customer} = \text{CUSTATUS}=\text{'A'} \text{ AND STATUS} \ne \text{'C'}$$
* **Lưu ý:** Định nghĩa "Hoạt động" ở đây khác EService (không dùng ngưỡng NAV).

### 12.17. Hợp Nhất Luồng Nộp/Rút Tiền (`METRIC_TP_DEPOSIT_WITHDRAW_UNION`)
* **Mục đích:** UNION report_cash_deposit (gắn nhãn "Nộp") với report_cash_withdrawal (gắn nhãn "Rút").

### 12.18. Đường Dẫn Tổ Chức 3 Nhánh cho Nộp Rút Tiền (`METRIC_TP_CASHFLOW_ORG_PATH`)
* **Mục đích:** Dựng song song path_mg_new/path_tp_new/path_gd_new phục vụ RLS ở cả 3 cấp quản lý.

> Chi tiết đầy đủ 8 tab của 18 chỉ số trên xem tại `index.html` mục **TradePro**. Hai mục **Đặt Lệnh** và **Báo Cáo Tài Sản** hiện **chưa có nguồn dữ liệu** (không có workbook Tableau hay SQL trong kho lưu trữ) nên chưa được tài liệu hóa công thức — tránh suy diễn logic không có căn cứ. TradePro chưa migrate sang Power BI nên cột DAX/Diff ghi "Chưa migrate".

---

## 13. PHÂN HỆ ESERVICE: BÁO CÁO KHÁCH HÀNG CHUYỂN MÔI GIỚI (PROD TABLEAU)

### 13.1. Xác Định Môi Giới Trước Đó & Hiện Tại (`METRIC_KHMG_TRANSFER_HISTORY`)
* **Mục đích:** Dùng hàm cửa sổ `LEAD(dim_broker_id)` và `LAG(broker_from_date)` sắp xếp theo `broker_from_date DESC` phân vùng theo từng `dim_cus_id` để dựng lại toàn bộ lịch sử biến động môi giới chăm sóc.
* **Quy tắc:**
  $$\text{pre_broker} = \operatorname{LEAD}(\text{dim_broker_id}) \text{ OVER (PARTITION BY dim_cus_id ORDER BY broker_from_date DESC)}$$
* **Số liệu thực tế:** Trong tổng số 1.501 lượt điều chuyển, có 88,5% chuyển sang môi giới cá nhân tại các chi nhánh/phòng giao dịch; 11,5% rút về tự giao dịch (Null).

### 13.2. Cờ Khách Hàng Chuyển Vào / Chuyển Ra Môi Giới Online (`METRIC_KHMG_CUS_IN_OUT`)
* **Mục đích:** Nhận diện chiều di chuyển khách hàng đối với đội Môi giới Online (mã `0001999018`).
* **Công thức phân loại:**
  $$\text{cus_in} = \begin{cases} 1 & \text{pre_broker} \ne \text{'0001999018'} \text{ AND dim_broker_id} = \text{'0001999018'} \\ 0 & \text{ngược lại} \end{cases}$$
  $$\text{cus_out} = \begin{cases} 1 & \text{pre_broker} = \text{'0001999018'} \text{ AND dim_broker_id} \ne \text{'0001999018'} \\ 0 & \text{ngược lại} \end{cases}$$
* **Chỉ số Dashboard KPI (Khớp Dashboard Tableau thực tế):**
  - **Số KH Chuyển Vào (`cus_in = 1`):** **524 KH** (chiếm 34,91%)
  - **Số KH Chuyển Ra (`cus_out = 1`):** **977 KH** (chiếm 65,09%)
  - **Tổng số phát sinh luân chuyển:** **1.501 lượt**
  - **Chênh lệch ròng (Net Migration):** **-453 KH** (Đội Online đóng vai trò phễu mở mới và phân bổ lại KH cần tư vấn deal sang MG chi nhánh).

---

## 14. PHÂN HỆ ESERVICE: BÁO CÁO KHÁCH HÀNG TƯ VẤN SỐ (TVS REPORT - PROD TABLEAU)

* **Bảng dữ liệu nguồn:** `FACT.report_mkt_detail_customer_new`
* **Workbook Tableau:** `V1.0_Eback_Báo cáo chi tiết khách hàng TVS`

### 14.1. Hiệu Suất Đầu Tư Danh Mục & Quy Mô NAV (`METRIC_TVS_PORTFOLIO_PERFORMANCE`)
* **Công thức:**
  $$\text{Performance} = \frac{\text{Tài sản ròng hiện tại} - \text{Vốn gốc đầu tư}}{\text{Vốn gốc đầu tư}} \times 100\%$$
* **Bộ chỉ số thực tế (Kỳ 03/09/2026):**
  - **NAV Toàn Kênh TVS:** **361.925.846.258 VNĐ** (~361,93 Tỷ VNĐ)
  - **NAV Bình Quân (KH có NAV > 0):** **83.427.545 VNĐ** (83,43M/TK)
  - **Số lượng TK có NAV > 0:** **4.301 TK**
  - **Dư Nợ Margin:** **2.834.777.697 VNĐ** (Tỷ lệ đòn bẩy Margin/NAV an toàn đạt 0,78%)

### 14.2. Cờ Khách Hàng Active Giao Dịch (`METRIC_TVS_CHECKACTIVE`)
* **Công thức:**
  $$\text{checkactive} = \begin{cases} 1 & \text{GTGD lũy kế tháng} > 0 \\ 0 & \text{ngược lại} \end{cases}$$
* **Số liệu thực tế:** Ghi nhận **29 khách hàng** phát sinh giao dịch khớp lệnh trong tháng, đóng góp **1.158.742.600 VNĐ** GTGD (tăng ▲ **59,80%** MoM) và tạo ra **851.279 VNĐ** phí môi giới ròng (tăng ▲ **60,82%** MoM). GTGD bình quân đạt **39,95M/KH giao dịch**.

### 14.3. Tỷ Trọng Tiền Mặt & Dòng Tiền Nộp (`METRIC_TVS_CASH_ALLOCATION`)
* **Công thức:**
  $$\text{Percentage} = \frac{\sum \text{Tiền mặt}}{\sum \text{Tiền mặt} + \sum \text{NAV Current}} \times 100\%$$
* **Số liệu thực tế:** Tỷ trọng tiền mặt duy trì **~12,4%** (tương đương 44,9 tỷ khả dụng) phục vụ giải ngân linh hoạt. Tiền nộp bình quân trên mỗi KH active đạt **3.967.225 VNĐ**.

### 14.4. Xếp Hạng Khách Hàng theo GTGD Lũy Kế Tháng (`METRIC_TVS_RANK_GTGD`)
* **Công thức:**
  $$\text{Rank GTGD} = \operatorname{\text{RANK_DENSE}}\big(\sum \text{GTGD lũy kế tháng},\ \text{desc}\big)$$
* **Bảng Top Khách hàng Giao dịch lớn nhất (Khớp 100% Tableau):**
  1. `024C015785`: **577,65M VNĐ** (chiếm 49,8% thanh khoản toàn kênh)
  2. `024C040703`: **200,89M VNĐ** (chiếm 17,3%)
  3. `024C008502`: **130,06M VNĐ** (chiếm 11,2%)
  4. `024C151984` (Lưu Văn Mạnh): **76,16M VNĐ** (chiếm 6,6%)
  5. `024C016581`: **41,43M VNĐ** (chiếm 3,6%)
  * *Top 10 khách hàng chiếm 92,1% tổng giá trị giao dịch của toàn bộ kênh TVS.*

