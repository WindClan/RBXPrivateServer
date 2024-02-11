from http.cookies import SimpleCookie
import requests
import os
assetBase = "https://assetdelivery.roblox.com/v1/asset?"
auth = "https://users.roblox.com/v1/users/authenticated"
def getAssetId(query):
    for param in query.split("&"):
        split = param.split("=")
        if split[0] == "id":
            return split[1]
    return ""
def asset(req,assetId):
    asset = getAssetId(assetId)
    if os.path.isfile("assetcache/"+asset):
        r = open("assetcache/"+asset, "rb")
        req.send_response(200)
        req.send_header("content-type", "binary/octet-stream")
        req.end_headers()   
        req.wfile.write(r.read())
        r.close()
    else:
        r = requests.get(assetBase+assetId)
        req.send_response(r.status_code)
        req.send_header("content-type", r.headers["content-type"])
        req.end_headers()   
        content = r.content.replace(b"www.roblox.com",b"localhost")
        req.wfile.write(content)
        r.close()
        if r.status_code == 200:
            a = open("assetcache/"+asset, "wb")
            a.write(content)
            a.close()

def authenticated(req):
    cookies = SimpleCookie(req.headers.get('Cookie'))
    r=requests.get(auth,cookies=cookies)
    req.send_response(r.status_code)
    req.send_header("content-type", r.headers["content-type"])
    req.end_headers()   
    req.wfile.write(r.content)
    r.close()
def dynamic(req,name):
    try:
        a = open("webcontent/"+name.split("&")[0],"rb")
        req.send_response(200)
        req.end_headers()
        req.wfile.write(a.read())
        a.close()
    except:
        print(name)
        print(req.path)
        req.send_response(404)
        req.end_headers()
