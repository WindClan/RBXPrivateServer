from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import rbxapi
import os
class base(BaseHTTPRequestHandler):
    def do_GET(self):
        #print(self.headers)
        url = urlparse(self.path)
        url1 = url.path
        if url1 == "/":
            url1 = "/index.html"
        if url1.lower() == "/favicon.ico":
            rbxapi.dynamic(self,"../cache/favicon.ico")
        elif url1.lower() == "/game/logout.aspx":
            self.send_response(200)
            self.end_headers()
        elif os.path.exists("webcontent/"+url1.lower().split("&")[0].replace(".","_")+".py"):
            rbxapi.scriptedGet(self,url)
        elif len(url1) > 5 and url1[0:6].lower() == "/asset":
            assetId = url.query
            rbxapi.asset(self,assetId)
        elif len(url1) > 5 and url1[0:6].lower() == "/game/":
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
        a = open("cache/dumps/"+name+".dmp","wb")
        a.write(self.rfile.read(int(self.headers.get('content-length'))))
        a.close()
        self.wfile.write(b"done")
