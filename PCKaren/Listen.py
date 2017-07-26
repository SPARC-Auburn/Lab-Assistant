import Speech
from Commands import *

if Speak("Checking for Internet connection") == False:
    print("I could not connect to the Internet, running in offline mode.")
    print("I will not be able to talk, but I can print out whatever respones I have.")
else:
    Speak("Connected to internet!")

while True:
    print("Listening")
    cmd = Speech.SR("")
    try:
        cmd = cmd.lower()
    except:
        pass
    try:
        print("Command heard: "+cmd)
    except:
        pass
    try:
        if(cmd.__contains__("hey karen")):
            Commands(cmd.split("hey karen ")[1])
    except:
        pass

