def serveGet(req,name,config):
    req.send_response(200)
    req.end_headers()
    req.wfile.write(b'This shouldnt appear')
    print(req.headers)
    