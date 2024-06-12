local baseUrl = "http://localhost/game/corescripts/"
local corescripts = {
	"playerlist",
	"settings",
	"dialogscript"
}
loadfile(baseUrl.."libraryregistration")()
for i,v in pairs(corescripts) do
	delay(0,function()
		loadfile(baseUrl..v)()
	end)
end
local backpackScripts = {
	"backpackbuilder",
	"backpackresizer",
	"loadoutscript"
}
for i,v in pairs(backpackScripts) do
	loadfile(baseUrl..v)()
end