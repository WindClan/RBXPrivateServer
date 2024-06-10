game:GetService("RunService"):Run()
game.Players:CreateLocalPlayer(0)
local player = game.Players.LocalPlayer
player:LoadCharacter()
player.Character.Humanoid.Died:connect(function()
	wait(5)
	player:LoadCharacter()
end)