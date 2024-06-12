def serveGet(req,name,config):
    req.send_response(200)
    req.end_headers()
    req.wfile.write(b"0 0 0 00 0 0 0")