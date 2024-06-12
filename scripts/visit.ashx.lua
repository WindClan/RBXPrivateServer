game.Players:CreateLocalPlayer(0)
game:GetService("RunService"):Run()
local plr = game.Players.LocalPlayer
local loadChar
function loadChar(a)
	if not a then
		wait(5)
	end
	plr:LoadCharacter()
	plr.Character.Humanoid.Died:connect(loadChar)
	local char = plr.Character
	char["Left Arm"].BrickColor = BrickColor.new("Really black")
	char["Right Arm"].BrickColor = BrickColor.new("Really black")
	char["Left Leg"].BrickColor = BrickColor.new("Really black")
	char["Right Leg"].BrickColor = BrickColor.new("Really black")
	char["Torso"].BrickColor = BrickColor.new("Dark stone grey")
	char["Head"].BrickColor = BrickColor.new("Institutional white")
	local shirt = Instance.new("Shirt",char)
	shirt.ShirtTemplate = "http://localhost/asset/?id=8561740"
end

loadChar(true)
loadfile("http://localhost/game/corescripts.ashx")()