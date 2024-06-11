import sys
a = open("certs/PublicKeyBlob.txt","rb")
blob = a.read()
a.close()
name = sys.argv[1]
print("This only replaces the scriptsigning and the ROBLOX asset URLs")
print("By pressing enter you acknowledge you still have to do some work")
input()
a = open(name,"rb+")
contents = a.read()
a.seek(0)
start = contents.find(b'BgIAA')
if start != -1:
    a.seek(start)
    a.write(blob)
    
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
a.close()
print("This did NOT patch trust checks! Press enter to quit")
input()
