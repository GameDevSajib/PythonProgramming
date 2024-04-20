from http.server import SimpleHTTPRequestHandler as handler
from socketserver import TCPServer
httpd=TCPServer(("192.168.174.128",1234),handler)
httpd.serve_forever()
