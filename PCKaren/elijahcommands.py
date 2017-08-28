from Speech import *
from Commands import *
import webbrowser
import math

def ElijahCommands(command):
    command = command.lower()
    if (command == "open a website"):
        #Speak("which website would you like me to open?")
	print("Which website would you like me to open?")
	try:
	   website = raw_input() #http://...
	   webbrowser.open(website, new=0, autoraise=True)
	except webbrowser.Error:
	   print("Browser control error...")
    
