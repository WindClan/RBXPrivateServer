The tool to generate the Roblox script signing certs is [here](https://archive.org/details/rbxsig-tools)
Roblox uses an RSA 1024 keypair exported with Microsoft's Csp blob format so I can't add it to the tool
Once you run the tool rename "PrivateKey.pem" to "scriptsign.pem" and place all the certificate files in this folder
You should have:
- PublicKeyBlob.txt
- PrivateKeyBlob.txt
- scriptsign.pem