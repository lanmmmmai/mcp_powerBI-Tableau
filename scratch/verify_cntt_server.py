import urllib.request

req = urllib.request.urlopen('http://127.0.0.1:8000')
html = req.read().decode('utf-8')
print('Status code:', req.getcode())
print('HTML length:', len(html))
print('Has new CNTT SVG 2 (text-anchor middle 35,3%):', 'text-anchor="middle" font-size="7.5" fill="#ffffff" font-weight="800">35,3%</text>' in html)
print('Has new CNTT SVG 1 (text-anchor middle 58,8%):', 'text-anchor="middle" font-size="7.5" fill="#ffffff" font-weight="800">58,8%</text>' in html)
