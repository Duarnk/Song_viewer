import http.server, urllib.request, json, os

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/oembed/'):
            tid = self.path.replace('/oembed/', '')
            try:
                url = f'https://open.spotify.com/oembed?url=https://open.spotify.com/track/{tid}'
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=5) as r:
                    data = r.read()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(data)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
        else:
            # serve ไฟล์ปกติ
            path = self.path.lstrip('/')
            if not path: path = 'bpm_viewer.html'
            try:
                with open(path, 'rb') as f:
                    content = f.read()
                self.send_response(200)
                if path.endswith('.html'): ct = 'text/html'
                elif path.endswith('.css'): ct = 'text/css'
                elif path.endswith('.js'): ct = 'application/javascript'
                else: ct = 'application/octet-stream'
                self.send_header('Content-Type', ct)
                self.end_headers()
                self.wfile.write(content)
            except:
                self.send_response(404)
                self.end_headers()

    def log_message(self, fmt, *args):
        pass

print('Server รันที่ http://localhost:8080')
print('เปิด http://localhost:8080/bpm_viewer.html ใน browser')
http.server.HTTPServer(('', 8080), Handler).serve_forever()
