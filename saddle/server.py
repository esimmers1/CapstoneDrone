import http.server
import socketserver
import socket
import os

def get_ip():
    return [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
    if not ip.startswith("127.")][:1], [[(s.connect(('1.1.1.1', 53)),
    s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
    socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

PORT = 63654
Handler = http.server.SimpleHTTPRequestHandler

IPaddr = get_ip()
IPaddr += ":" if len(IPaddr) > 0 else ""

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port " + IPaddr + str(PORT))
    httpd.serve_forever()
