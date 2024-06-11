import json
from http.cookies import SimpleCookie
import requests
authUrl = "https://users.roblox.com/v1/users/authenticated"

def serveGet(req,name,config):
    cookies = SimpleCookie(req.headers.get('Cookie'))
    r=requests.get(authUrl,cookies=cookies)
    req.send_response(200)
    req.send_header("content-type", "text/html; charset=utf-8")
    req.end_headers()   
    a = json.loads(r.content)
    if r.status_code == 200:
        req.wfile.write(a["id"].encode("cp1252"))
    else:
        req.wfile.write(b"null")
    r.close()