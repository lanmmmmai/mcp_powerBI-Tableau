import urllib.request

req = urllib.request.urlopen('http://127.0.0.1:8000')
html = req.read().decode('utf-8')
pos = html.find('id="section-sms-5-tab-tableau"')
print(html[pos:pos+350])
