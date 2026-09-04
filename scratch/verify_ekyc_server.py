import urllib.request

req = urllib.request.urlopen('http://127.0.0.1:8000')
html = req.read().decode('utf-8')
print('Status code:', req.getcode())
print('HTML length:', len(html))
print('Has TOP_DASHBOARD_EKYC:', 'TỔNG QUAN HÀNH TRÌNH MỞ TKGDCK QUA eKYC' in html)
print('Has EKYC SVG 1 (Kênh Web):', 'Cơ Cấu Kênh Mở TKGDCK (Web vs App)' in html)
print('Has EKYC SVG 3 (Phễu Funnel B01-B04):', 'Phễu Chuyển Đổi Hành Trình eKYC' in html)
