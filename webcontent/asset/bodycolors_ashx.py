from urllib.parse import parse_qs
bodyColorBase = b"""
<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
	<External>null</External>
	<External>nil</External>
	<Item class="BodyColors">
		<Properties>
			<int name="HeadColor">[HEAD]</int>
			<int name="LeftArmColor">[LARM]</int>
			<int name="LeftLegColor">[LLEG]</int>
			<string name="Name">Body Colors</string>
			<int name="RightArmColor">[RARM]</int>
			<int name="RightLegColor">[RLEG]</int>
			<int name="TorsoColor">[TORSO]</int>
			<bool name="archivable">true</bool>
		</Properties>
	</Item>
</roblox>"""
type1 = {
    "[HEAD]": b"24",
    "[LARM]": b"24",
    "[RARM]": b"24",
    "[LLEG]": b"119",
    "[RLEG]": b"119",
    "[TORSO]": b"23",
}
type2 = {
    "[HEAD]": b"1",
    "[LARM]": b"1",
    "[RARM]": b"1",
    "[LLEG]": b"102",
    "[RLEG]": b"102",
    "[TORSO]": b"27",
}
type3 = {
    "[HEAD]": b"1",
    "[LARM]": b"26",
    "[RARM]": b"26",
    "[LLEG]": b"26",
    "[RLEG]": b"26",
    "[TORSO]": b"27",
}

def serveGet(req,name,config):
    query = parse_qs(name.query)
    if not query["type"]:
        req.send_response(403)
        req.end_headers()
        req.wfile.write(b"Invalid Request")
    else:
        if query["type"] == "1":
            selType = type1
        elif query["type"] == "2":
            selType = type2
        elif query["type"] == "3":
            selType = type3
        else:
            selType = type1
        req.send_response(200)
        req.end_headers()
        req.wfile.write(bodyColorBase.replace(b"[HEAD]",selType["[HEAD]"]).replace(b"[LARM]",selType["[LARM]"]).replace(b"[RARM]",selType["[RARM]"]).replace(b"[LLEG]",selType["[LLEG]"]).replace(b"[RLEG]",selType["[RLEG]"]).replace(b"[TORSO]",selType["[TORSO]"]))