# RBXPrivateServer was made by WindClan
print("DO NOT CLOSE THIS WINDOW!!!!")
print("Closing this closes the webserver")
import tkinter as tk
from random import randint
import runServer
import subprocess
from tkinter.filedialog import askopenfilename
clientExec = "client/RobloxApp.exe"
frame = None
selected = None
userId = randint(-9999,-1)
selectedMap = ""
def mainWindow():
    global frame; frame = tk.Tk() 
    frame.title("RBXPrivateServer") 
    frame.geometry('400x200') 
    soloButton = tk.Button(frame, 
                        text = "Play Solo",  
                        command = solo) 
    soloButton.pack()
    serverButton = tk.Button(frame, 
                        text = "Start Server",  
                        command = server) 
    serverButton.pack()
    clientButton = tk.Button(frame, 
                        text = "Start Client",  
                        command = client) 
    clientButton.pack()
    studioButton = tk.Button(frame, 
                        text = "Start Studio",  
                        command = studio) 
    studioButton.pack()
    frame.mainloop() 

def returnToMain():
    frame.destroy()
    mainWindow()

def runClient(args=""):
    subprocess.run(clientExec+" "+args)
def solo():
    global frame; frame.destroy()
    def start():
        if selectedMap != None:
            frame; frame.destroy()
            runClient('-script "loadfile(\'http://localhost/game/visit.ashx\')()" "'+selectedMap.replace("/","\\")+'"')
    frame = tk.Tk() 
    frame.title("RBXPrivateServer - Play solo") 
    frame.geometry('400x200')
    selectMapButton = tk.Button(frame, 
                    text = "Select map",  
                    command = selectMap)
    selectMapButton.pack()
    global selected; selected = tk.Label(frame, text = "Selected map: none")
    selected.pack()
    startButton = tk.Button(frame, 
                    text = "Start",  
                    command = start)
    startButton.pack()
    frame.mainloop() 
def selectMap():
    global selectedMap; selectedMap = askopenfilename()
    selected.config(text = "Selected map: "+selectedMap)
def server():
    global frame; frame.destroy()
    frame = tk.Tk() 
    frame.title("RBXPrivateServer - Start server") 
    frame.geometry('400x200') 
    lbl = tk.Label(frame, text = "Enter port")
    lbl.pack()
    ipinput = tk.Text(frame, 
                   height = 1, 
                   width = 20) 
    ipinput.pack()
    def start():
        if selectedMap != None:
            port = ipinput.get(1.0, "end-1c")
            frame.destroy()
            runClient('-script "loadfile(\'http://localhost/game/gameserver.ashx\')(0,'+port+')" "'+selectedMap.replace("/","\\")+'"')
    selectMapButton = tk.Button(frame, 
                    text = "Select map",  
                    command = selectMap)
    selectMapButton.pack()
    global selected; selected = tk.Label(frame, text = "Selected map: none")
    selected.pack()
    startButton = tk.Button(frame, 
                    text = "Start",  
                    command = start)
    startButton.pack()
    frame.mainloop() 

def client():
    global frame; frame.destroy()
    frame = tk.Tk() 
    frame.title("RBXPrivateServer - Start client") 
    frame.geometry('400x200') 
    lbl = tk.Label(frame, text = "Enter IP")
    lbl.pack()
    ipinput = tk.Text(frame, 
                   height = 1, 
                   width = 20) 
    ipinput.pack()
    lbl = tk.Label(frame, text = "Enter port")
    lbl.pack()
    portinput = tk.Text(frame, 
                   height = 1, 
                   width = 20) 
    portinput.pack()
    def start():
        ip = ipinput.get(1.0, "end-1c")
        port = portinput.get(1.0, "end-1c")
        frame.destroy()
        runClient('-script "loadfile(\'http://localhost/game/join.ashx\')(nil,\''+ip+'\','+port+','+str(userId)+')"')
    startButton = tk.Button(frame, 
                text = "Start",  
                command = start)
    startButton.pack()
    frame.mainloop() 
def studio():
    frame.destroy()
    runClient()

if __name__ == "__main__":
    runServer.startServers()
    mainWindow()

