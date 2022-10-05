import time
import webbrowser
import os
import pyperclip

os.system('cls' if os.name=='nt' else 'clear')
time.sleep(1)
print("\n----HACK-TOOL----\n")

while True:
    print('''
    -expc Exploit Camera --- Exploit I.P Cameras getting usernames and password
    -ykt Yorkox Tool --- Do Phishing, DDos, etc.
    -cver Camover --- Exploit I.P Cameras getting usernames and password
    -arat AndroRat --- Manage Camera and Information over an custom Android App.

    -g if you don't have git command installed to copy it

    -web + tool to open his web |EXAMPLE: -web arat
    
    --- Your are going to get copied the command on your clipboard so you can copy it into another Terminal ---
    
        !!ALL THESE HACKING TOOLS ARE GITHUB REPOSITORYS AND ARE NOT MINE. I AM NOT RESPONSABLE FOR THE DAMAGE DONE WiTH THE TOOLS!!
    ''')

    q1 = input("What do you want to open? -x to exit : ")

    if q1 == "expc":
        print("Copied!")
        pyperclip.copy("git clone https://github.com/vanpersiexp/expcamera.git")
        time.sleep(1)
    
    elif q1 == "web expc":
        webbrowser.open("https://github.com/vanpersiexp/expcamera.git")
    
    elif q1 == "ykt":
        print("Copied!")
        pyperclip.copy("git clone https://github.com/yorkox0/yorkox-tool.git")
        time.sleep(1)
    
    elif q1 == "web ykt":
        webbrowser.open("https://github.com/yorkox0/yorkox-tool.git")

    elif q1 == "cver":
        print("Copied!")
        pyperclip.copy("git clone https://github.com/EntySec/CamOver.git")
        time.sleep(1)

    elif q1 == "web cver":
        webbrowser.open("https://github.com/EntySec/CamOver.git")

    elif q1 == "arat":
        print("Copied!")
        pyperclip.copy("git clone https://github.com/MRfky00/AndroRAT.git")
        time.sleep(1)
    
    elif q1 == "web arat":
        webbrowser.open("https://github.com/MRfky00/AndroRAT.git")
    
    elif q1 == "g":
        print("Copied!")
        pyperclip.copy("pip install git")
        time.sleep(1)
    
    elif q1 == "x":
        break

    else:
        os.system('cls' if os.name=='nt' else 'clear')
        print("No Answer to your INPUT")
        time.sleep(1)