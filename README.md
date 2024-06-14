# RBXPrivateServer

Tool to host and play private servers, requires a bit of setup

## How to use

1. Install python 3 (duh)
2. Follow the instructions in the certs folder
3. Find a complete archive of a 2011 or 2012 client (must be the same as the person you are playing with!)
4. Drag `RobloxApp.exe` onto `patchclient.py` and read the instructions
5. Place the client in the `client` folder in the program folder
6. Install dependencies for the main program
7. Run the launcher (`launcher.py`)

## Fixing place file assets
Open the rbxl in a text editor and replace all instances of `http://www.roblox.com/asset/?id=` to `http://localhost/asset/?id=`

## License

All the code authored by me is under the MIT license.
This includes all the python scripts.

All of the lua except Visit.ashx was written by Roblox.
All rights to those belong to Roblox.
