import os
from wsgidav.wsgidav_app import WsgiDAVApp
from cheroot import wsgi

HOST = os.getenv("WEBDAV_HOST", "0.0.0.0")
PORT = int(os.getenv("WEBDAV_PORT", "8080"))
SHARE_PATH = os.getenv("SHARE_PATH", "/app/data")
USERNAME = os.getenv("WEBDAV_USERNAME", "admin")
PASSWORD = os.getenv("WEBDAV_PASSWORD", "change-me")

# WsgiDAV configuration
config = {
    "host": HOST,
    "port": PORT,
    "provider_mapping": {
        "/": SHARE_PATH,
    },
    "verbose": 1,
    # Keep CORS open as requested
    "cors": {
        "allow_origin": "*",
        "allow_methods": "GET, HEAD, POST, PUT, DELETE, PROPFIND, PROPPATCH, MKCOL, COPY, MOVE, LOCK, UNLOCK",
        "allow_headers": "Authorization, Content-Type, Depth, If-Match, If-None-Match, Lock-Token, Timeout",
    },
    "simple_dc": {
        "user_mapping": {
            "*": {
                USERNAME: {"password": PASSWORD, "description": "User"}
            }
        }
    },
}

app = WsgiDAVApp(config)
server_addr = (config["host"], config["port"])
server = wsgi.Server(server_addr, app)

try:
    print(f"WebDAV server running at http://{config['host']}:{config['port']}")
    print(f"Serving path: {SHARE_PATH}")
    print(f"Username: {USERNAME}")
    server.start()
except KeyboardInterrupt:
    print("Stopping server...")
    server.stop()
