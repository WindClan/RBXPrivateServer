import sys
a = open("certs/PublicKeyBlob.txt","rb")
blob = a.read()
a.close()
name = sys.argv[1]
print("This doesn't work on 100% of clients")
print("By pressing enter you may acknowledge you still have to do some work")
input()
a = open(name,"rb+")
contents = a.read()

#Scriptsigning hash
a.seek(0)
start = contents.find(b'BgIAA')
if start != -1:
    a.seek(start)
    a.write(blob)
#Trustcheck URL 1 
a.seek(0)
start = contents.find(b'\x00roblox.com\x00')
if start != -1:
    a.seek(start)
    a.write(b'\x00localhost\x00\x00')
#Trustcheck URL 2
a.seek(0)
start = contents.find(b'\x00roblox.com/\x00')
if start != -1:
    a.seek(start)
    a.write(b'\x00localhost/\x00\x00')
#Misc instance of URL
a.seek(0)
start = contents.find(b'\x2Eroblox.com\x00')
if start != -1:
    a.seek(start)
    a.write(b'\x2Elocalhost\x00\x00')
#Asset URL 1
a.seek(0)
start = contents.find(b'http://www.roblox.com/asset?id=%d')
if start != -1:
    a.seek(start)
    a.write(b'http://localhost/asset/?id=%d\x00\x00\x00\x00')
#Asset URL 2
a.seek(0)
start = contents.find(b'http://www.roblox.com/asset/?id=')
if start != -1:
    a.seek(start)
    a.write(b'http://localhost/asset/?id=\x00\x00\x00\x00\x00')
#Asset URL 3
a.seek(0)
start = contents.find(b'http://www.roblox.com/asset?id=')
if start != -1:
    a.seek(start)
    a.write(b'http://localhost/asset?id=\x00\x00\x00\x00\x00')
#Asset URL 4
a.seek(0)
start = contents.find(b'\x00roblox.com//asset/\x00')
if start != -1:
    a.seek(start)
    a.write(b'\x00localhost//asset/\x00\x00')
#Asset URL 5
a.seek(0)
start = contents.find(b'\x00roblox.com/asset/\x00')
if start != -1:
    a.seek(start)
    a.write(b'\x00localhost/asset/\x00\x00')
#
#API URL
a.seek(0)
start = contents.find(b'https://%sapi.roblox.com/%s/?apiKey=%s')
if start != -1:
    a.seek(start)
    a.write(b'https://%sapi.localhost/%s/?apiKey=%s\x00')
a.close()
print("This does not patch some of the major issues")
print("You also still need to edit AppSettings.xml")
print("Press enter to exit.")
input()
