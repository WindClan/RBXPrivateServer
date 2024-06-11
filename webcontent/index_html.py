def serveGet(req,name,config):
    req.send_response(200)
    req.send_header("content-type", "text/html; charset=utf-8")
    req.end_headers()
    req.wfile.write(b'<title>rbxapifixer</title>')
    req.wfile.write(b'<h1>rbxapifixer</h1>')
    req.wfile.write(b'<h3>Config</h3>')
    req.wfile.write(b'<p>'+b'<b>[DEFAULT]</b>'+b'</p>')
    req.wfile.write(b'<p>'+b'hostname: '+config['DEFAULT']['hostname'].encode('cp1252')+b'</p>')
    req.wfile.write(b'<p>'+b'enable-https: '+config['DEFAULT']['enable-https'].encode('cp1252')+b'</p>')
    req.wfile.write(b'<p>'+b'http-port: '+config['DEFAULT']['http-port'].encode('cp1252')+b'</p>')
    req.wfile.write(b'<p>'+b'https-port: '+config['DEFAULT']['https-port'].encode('cp1252')+b'</p>')
    req.wfile.write(b'<p>'+b'old-style-hash: '+config['DEFAULT']['old-style-hash'].encode('cp1252')+b'</p>')
    