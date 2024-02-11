from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import rbxapi
class base(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path.lower() == "/asset/getscriptstate.ashx":
            self.send_response(200)
            self.end_headers()
        elif len(url.path) > 5 and url.path[0:6].lower() == "/asset":
            assetId = url.query
            print(assetId)
            print(self.path)
            rbxapi.asset(self,assetId)
        elif url.path.lower() == "/game/getcurrentuser.ashx":
            rbxapi.authenticated(self)
        elif url.path.lower() == "/game/logout.aspx":
            self.send_response(200)
            self.end_headers()
        else:
            rbxapi.dynamic(self,url.path)

