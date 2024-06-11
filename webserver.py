# Python 3 server example
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from serverclass import *
import time
import ssl
import wget
import os
def run(hostName="localhost",isHttps=False,password="",serverPort=0):
    if serverPort == 0:
        if isHttps:
            serverPort = 443
        else:
            serverPort = 80

    webServer = ThreadingHTTPServer((hostName, serverPort), base)
    if isHttps:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile='./certs/httpscert.pem', keyfile="./certs/httpskey.pem", password=password)
        webServer.socket = context.wrap_socket(webServer.socket, server_side=True)
    print("Server started http://%s:%s" % (hostName, serverPort))
    webServer.serve_forever()

    webServer.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    run()