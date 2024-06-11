from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import rbxapi
import os
class base(BaseHTTPRequestHandler):
    def do_GET(self):
        #print(self.headers)
        url = urlparse(self.path)
        if url.path.lower() == "/favicon.ico":
            rbxapi.dynamic(self,"../cache/favicon.ico")
        elif url.path.lower() == "/asset/getscriptstate.ashx":
            self.send_response(200)
            self.end_headers()
        elif len(url.path) > 5 and url.path[0:6].lower() == "/asset":
            assetId = url.query
            rbxapi.asset(self,assetId)
#        elif url.path.lower() == "/game/getcurrentuser.ashx":
#            rbxapi.authenticated(self)
        elif url.path.lower() == "/game/logout.aspx":
            self.send_response(200)
            self.end_headers()
        elif url.path.lower() == "/game/keepalivepinger.ashx":
            self.send_response(200)
            self.end_headers()
        elif os.path.exists("webcontent/"+url.path.lower().split("&")[0].replace(".","_")+".py"):
            rbxapi.scriptedGet(self,url.path)
        elif len(url.path) > 5 and url.path[0:6].lower() == "/game/":
            assetId = url.path[6:len(url.path)]
            rbxapi.script(self,assetId)
        else:
            rbxapi.dynamic(self,url.path)
            
    def do_POST(self):
        url = urlparse(self.path)
        name = ""
        if url.path.lower() == "/error/dmp.ashx":
            name = "crashdump"+str(os.times())
        elif url.path.lower() == "/game/machineconfiguration.ashx":
            name = "machineconfig"+str(os.times())
        else:
            name = "unknown"+str(os.times())
        self.send_response(200)
        self.end_headers()
        a = open("cache/dumps/"+name+".txt","wb")
        a.write(self.rfile.read(int(self.headers.get('content-length'))))
        a.close()
        self.wfile.write(b"done")
