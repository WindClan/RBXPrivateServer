base = b"""{
   "resolvedAvatarType":"R6",
   "accessoryVersionIds":[

   ],
   "equippedGearVersionIds":[
      
   ],
   "backpackGearVersionIds":[
      
   ],
   "bodyColors":{
      "HeadColor":[HEAD],
      "LeftArmColor":[LARM],
      "LeftLegColor":[LLEG],
      "RightArmColor":[RARM],
      "RightLegColor":[RLEG],
      "TorsoColor":[TORSO]
   },
   "animations":{
      
   },
   "scales":{
      "Width":1.0000,
      "Height":1.0000,
      "Head":1.0000,
      "Depth":1.00,
      "Proportion":0.0000,
      "BodyType":0.0000
   }
}"""
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
type4 = {
    "[HEAD]": b"194",
    "[LARM]": b"194",
    "[RARM]": b"194",
    "[LLEG]": b"194",
    "[RLEG]": b"194",
    "[TORSO]": b"199",
}
def serveGet(req,name,config):
    selType = type4
    req.send_response(200)
    req.end_headers()
    req.wfile.write(base.replace(b"[HEAD]",selType["[HEAD]"]).replace(b"[LARM]",selType["[LARM]"]).replace(b"[RARM]",selType["[RARM]"]).replace(b"[LLEG]",selType["[LLEG]"]).replace(b"[RLEG]",selType["[RLEG]"]).replace(b"[TORSO]",selType["[TORSO]"]))
