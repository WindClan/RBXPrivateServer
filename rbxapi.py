from http.cookies import SimpleCookie
from OpenSSL import crypto
import importlib
import requests
import configparser
import os
import base64
import gzip
assetBase = "https://assetdelivery.roblox.com/v1/asset/?"
auth = "https://users.roblox.com/v1/users/authenticated"

key_file = open("certs/scriptsign.pem", "r")
key = key_file.read()
key_file.close()
pkey = crypto.load_privatekey(crypto.FILETYPE_PEM, key)

config = configparser.ConfigParser()
config.read("settings.ini")

def getAssetId(query):
    for param in query.split("&"):
        split = param.split("=")
        if split[0] == "id":
            return split[1]
    return ""
def sendAssetHeaders(req,assetId):
    req.send_header("roblox-assetid", str(assetId))
    
def asset(req,assetId):
    asset = getAssetId(assetId)
    if os.path.isfile("cache/assets/"+asset):
        r = open("cache/assets/"+asset, "rb")
        req.send_response(200)
        req.send_header("content-type", "binary/octet-stream")
        sendAssetHeaders(req,asset)
        req.end_headers()   
        req.wfile.write(r.read())
        r.close()
    else:
        headers = {
            "User-Agent": req.headers["User-Agent"]
        }
        print(headers)
        r = requests.get(assetBase+assetId, headers=headers)
        req.send_response(r.status_code)
        req.send_header("content-type", r.headers["content-type"])
        if r.status_code == 200:
            sendAssetHeaders(req,asset)
        req.end_headers()   
        content = r.content.replace(b"www.roblox.com",b"localhost")
        req.wfile.write(content)
        r.close()
        if r.status_code == 200:
            a = open("cache/assets/"+asset, "wb")
            a.write(content)
            a.close()
        else:
            print(r.status_code)
            print(assetBase+assetId)
            print(r.content)

def script(req,name):
    a = open("scripts/"+name.split("&")[0]+".lua","rb")
    content = b"\r\n"+a.read()
    a.close()
    sign = crypto.sign(pkey, content, "sha1") 
    content = b"%"+base64.b64encode(sign)+b"%"+content
    if config["DEFAULT"]['old-style-hash'] == "no":
        content = b'--rbxsig'+content
    req.send_response(200)
    req.end_headers()
    req.wfile.write(content)
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
def scriptedGet(req,name):
    name = name.split("&")[0]
    if name == "/":
        name = "/index.html"
    module = "webcontent"+name.replace(".","_").replace("/",".").lower()
    print(module)
    a = importlib.import_module(module)
    a.serveGet(req,name,config)