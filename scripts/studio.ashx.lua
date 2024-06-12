-- Setup studio cmd bar & load core scripts

pcall(function() game:GetService("InsertService"):SetFreeModelUrl("http://localhost/Game/Tools/InsertAsset.ashx?type=fm&q=%s&pg=%d&rs=%d") end)
pcall(function() game:GetService("InsertService"):SetFreeDecalUrl("http://localhost/Game/Tools/InsertAsset.ashx?type=fd&q=%s&pg=%d&rs=%d") end)

pcall(function() game:GetService("ScriptInformationProvider"):SetAssetUrl("http://localhost/Asset/") end)
pcall(function() game:GetService("InsertService"):SetBaseSetsUrl("http://localhost/Game/Tools/InsertAsset.ashx?nsets=10&type=base") end)
pcall(function() game:GetService("InsertService"):SetUserSetsUrl("http://localhost/Game/Tools/InsertAsset.ashx?nsets=20&type=user&userid=%d") end)
pcall(function() game:GetService("InsertService"):SetCollectionUrl("http://localhost/Game/Tools/InsertAsset.ashx?sid=%d") end)
pcall(function() game:GetService("InsertService"):SetAssetUrl("http://localhost/Asset/?id=%d") end)
pcall(function() game:GetService("InsertService"):SetAssetVersionUrl("http://localhost/Asset/?assetversionid=%d") end)

pcall(function() game:GetService("SocialService"):SetFriendUrl("http://localhost/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerid=%d&userid=%d") end)
pcall(function() game:GetService("SocialService"):SetBestFriendUrl("http://localhost/Game/LuaWebService/HandleSocialRequest.ashx?method=IsBestFriendsWith&playerid=%d&userid=%d") end)
pcall(function() game:GetService("SocialService"):SetGroupUrl("http://localhost/Game/LuaWebService/HandleSocialRequest.ashx?method=IsInGroup&playerid=%d&groupid=%d") end)
pcall(function() game:GetService("SocialService"):SetGroupRankUrl("http://localhost/Game/LuaWebService/HandleSocialRequest.ashx?method=GetGroupRank&playerid=%d&groupid=%d") end)
pcall(function() game:GetService("SocialService"):SetGroupRoleUrl("http://localhost/Game/LuaWebService/HandleSocialRequest.ashx?method=GetGroupRole&playerid=%d&groupid=%d") end)
pcall(function() game:GetService("GamePassService"):SetPlayerHasPassUrl("http://localhost/Game/GamePass/GamePassHandler.ashx?Action=HasPass&UserID=%d&PassID=%d") end)
pcall(function() game:GetService("MarketplaceService"):SetProductInfoUrl("http://api.localhost/marketplace/productinfo?assetId=%d") end)
pcall(function() game:GetService("MarketplaceService"):SetDevProductInfoUrl("http://api.localhost/marketplace/productDetails?productId=%d") end)
pcall(function() game:GetService("MarketplaceService"):SetPlayerOwnsAssetUrl("http://api.localhost/ownership/hasasset?userId=%d&assetId=%d") end)

local result = pcall(function() game:GetService("ScriptContext"):AddStarterScript(37801172) end)
if not result then
  pcall(function() game:GetService("ScriptContext"):AddCoreScript(37801172,game:GetService("ScriptContext"),"StarterScript") end)
end

