from random import randint
characters = [
    "http://localhost/Asset/BodyColors.ashx?type=1;http://localhost/asset?id=7074729",
    "http://localhost/Asset/BodyColors.ashx?type=2;http://localhost/asset?id=15432080",
    "http://localhost/Asset/BodyColors.ashx?type=3;http://localhost/asset?id=8561741",
    "http://localhost/Asset/BodyColors.ashx?type=1;http://localhost/asset?id=8561741",
    "http://localhost/Asset/BodyColors.ashx?type=2",
    "http://localhost/Asset/BodyColors.ashx?type=3",
]
def serveGet(req,name,config):
    char = characters[randint(0,len(characters)-1)]
    req.send_response(200)
    req.end_headers()
    req.wfile.write(char.encode("cp1252"))