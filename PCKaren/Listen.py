#IMPORTS
print("Initializing...")
import Speech
from Commands import *

#CHECKS
if Speak("Checking for Internet connection") == False:										#Checks to see if gTTS is functioning properly
    print("I could not connect to the Internet, running in offline mode.")				
    print("I will not be able to talk, but I can print out whatever respones I have.")
else:
    Speak("Connected to internet!")
	
maxTimeOut = 10																				#ADJUST THIS FOR TIME OUT
listen = False
timeout = 0

#MAIN LOOP
while True:
	if timeout >= maxTimeOut:															#if timeout loop broke
		pygame.init()																
		pygame.mixer.init()
		pygame.mixer.music.load("end.mp3")												#play stop listening tone
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(10)
			
	listen, startCmd = Speech.startListening("")
	
	print listen
	print startCmd
	
	if listen == True:

		pygame.init()																		
		pygame.mixer.init()
		pygame.mixer.music.load("start.mp3")												#play start listening tone
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(10)
		Speak("Yes?")	
		timeout=0
		print "Timeout reset"
	while listen == True and timeout < maxTimeOut:											#while we are actively accepting commands and the timeout timer has not run out
		cmd = Speech.SR("")
		
		try:
			cmd = cmd.lower()																#ensure the command is in lowercase form
		except:
			pass
		
		try:
			print("Command heard: "+cmd)
		except:
			pass
		
		if cmd == "shut up karen" or cmd == "stop listening":								#we've told karen to stop listening							
			print "No longer listening to commands"
			listen = False
			pygame.init()																	
			pygame.mixer.init()
			pygame.mixer.music.load("end.mp3")												#play stop listening tone
			pygame.mixer.music.play()
			while pygame.mixer.music.get_busy():
				pygame.time.Clock().tick(10)
			break
		else:
			try:
				Commands(cmd)
				timeout=0
				print "Timeout reset"
			except:
				pass
			
		timeout+=1																			#increment timeout
		print "Time out in " + str(maxTimeOut-timeout)

