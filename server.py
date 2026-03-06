# simple_server.py
import http.server
import socketserver
import os

PORT = 8000
PUBLIC_DIR = "public"

# Ensure public directory exists and put a default index.html if missing
os.makedirs(PUBLIC_DIR, exist_ok=True)
index_path = os.path.join(PUBLIC_DIR, "index.html")
if not os.path.exists(index_path):
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("""<!doctype html>
<html>
<head><meta charset="utf-8"><title>Static Page</title></head>
<body>
  <h1>Welcome to the simple static server</h1>
  <p>This page is served by Python's http.server from the <code>public/</code> folder.</p>
</body>
</html>""")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PUBLIC_DIR, **kwargs)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving static files from ./{PUBLIC_DIR} at http://localhost:{PORT}/")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down.")