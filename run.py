import threading
import webserver
import configparser
import wget
import os

config = configparser.ConfigParser()
if os.path.exists("settings.ini"):
    config.read_file(open("settings.ini"))
if config['DEFAULT'] == None:
    config['DEFAULT'] = {'hostname': 'localhost',
                     'password': 'password',
                     'enable-https': 'yes',
                     'http-port': '80',
                     'https-port': '443',
                     'old-style-hash': 'no'
                     }
    with open('settings.ini', 'w') as configfile:
        config.write(configfile)


def startServers():
    if not os.path.isdir("cache"):
        os.mkdir("cache")
        os.mkdir("cache/assets")
        os.mkdir("cache/dumps")
    if not os.path.exists("cache/favicon.ico"):
        wget.download("http://www.roblox.com/favicon.ico",out="cache/favicon.ico")
    threading.Thread(target=webserver.run,args=(config['DEFAULT']['hostname'],False,config['DEFAULT']['password'],int(config['DEFAULT']['http-port']))).start()
    if bool(config['DEFAULT']['enable-https']):
        threading.Thread(target=webserver.run,args=(config['DEFAULT']['hostname'],True,config['DEFAULT']['password'],int(config['DEFAULT']['https-port']))).start()
if __name__ == "__main__":
    startServers()
