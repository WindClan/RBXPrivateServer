-- Library Registration Script
-- This script is used to register RbxLua libraries on game servers, so game scripts have
-- access to all of the libraries (otherwise only local scripts do)

local deepakTestingPlace = 3569749
local sc = game:GetService("ScriptContext")
local tries = 0
 
while not sc and tries < 3 do
	tries = tries + 1
	sc = game:GetService("ScriptContext")
	wait(0.2)
end
 
if sc then
	loadfile("http://localhost/asset?id=45284430")()  --RbxGui
	loadfile("http://localhost/asset?id=45374389")() --RbxGear
	if game.PlaceId == deepakTestingPlace then
		sc:RegisterLibrary("Libraries/RbxStatus", "52177566")()
	end
	loadfile("http://localhost/asset?id=60595411")() --RbxUtility
	loadfile("http://localhost/asset?id=73157242")() --RbxStamper
	sc:LibraryRegistrationComplete()
else
	print("failed to find script context, libraries did not load")
end
