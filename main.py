import os
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        file_path = os.path.join(os.path.dirname(__file__), 'index.html')
        if not os.path.exists(file_path):
            file_path = os.path.join(os.path.dirname(__file__), 'BAO_CAO_CONG_THUC_TINH_TOAN_POWERBI.html')
            
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                self.wfile.write(f.read().encode('utf-8'))
        else:
            self.wfile.write(b"<h1>Bao Cao Power BI</h1>")
        return

# WSGI Application entrypoint
def app(environ, start_response):
    file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read().encode('utf-8')
    else:
        data = b"<h1>Bao Cao Power BI</h1>"
        
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [data]

if __name__ == '__main__':
    import sys
    from http.server import HTTPServer, SimpleHTTPRequestHandler

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('127.0.0.1', port), SimpleHTTPRequestHandler)
    print(f"Serving HTTP at http://127.0.0.1:{port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

