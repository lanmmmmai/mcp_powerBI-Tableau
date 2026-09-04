import urllib.request

req = urllib.request.urlopen('http://127.0.0.1:8000')
print('Status code:', req.getcode())
html = req.read().decode('utf-8')
print('HTML length:', len(html))
print('Has section-sms-5-tab-tableau code-container:', 'id="section-sms-5-tab-tableau">\n            <div class="code-container"' in html)
print('Remaining code-box in served HTML:', html.count('class="code-box"'))
print('Remaining code-copy-btn in served HTML:', html.count('class="code-copy-btn"'))
