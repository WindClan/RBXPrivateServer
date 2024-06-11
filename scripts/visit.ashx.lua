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
end

loadChar(true)