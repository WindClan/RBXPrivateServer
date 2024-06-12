local url = "http://localhost"
local runService = game:GetService("RunService")
local function createCharacter(plr)
	plr:LoadCharacter()
	plr.Character.Humanoid.Died:connect(function()
		wait(5)
		plr:LoadCharacter()
	end)
	local char = plr.Character
	char["Left Arm"].BrickColor = BrickColor.new("Really black")
	char["Right Arm"].BrickColor = BrickColor.new("Really black")
	char["Left Leg"].BrickColor = BrickColor.new("Really black")
	char["Right Leg"].BrickColor = BrickColor.new("Really black")
	char["Torso"].BrickColor = BrickColor.new("Dark stone grey")
	char["Head"].BrickColor = BrickColor.new("Industrial white")
	local shirt = Instance.new("Shirt",char)
	shirt.ShirtTemplate = url.."/asset?id=8561740"
end

_G.playsolo = function()
	runService:Run()
	game.Players:CreateLocalPlayer(0)
	createCharacter(game.Players.LocalPlayer)
end
_G.loadplace = function(id)
	game:Load(url.."/asset?id="..id)
end