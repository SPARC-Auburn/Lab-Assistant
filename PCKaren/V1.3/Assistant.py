#IMPORTS
import speech_recognition as sr
from gtts import gTTS
import pygame
from os import remove
import Commands
import DefaultSuite

class Assistant:
	
	self.intent = ""
	self.userCommand = ""
	def __init__(self, name, noise, location):
		
		r = sr.Recognizer()
		with sr.Microphone(sample_rate = 48000) as source:
			r.adjust_for_ambient_noise(source)											#Adjust for ambient noise by listening for 1 second
			r.energy_threshold += 200														#Threshold offset
			print "THRESHOLD: " + str(r.energy_threshold)
		self.name = name
		print("Initializing {})".format(self.name))
		self.noise = noise###If suites all return false#### (Suite commands run their respective commands and return True if something was run)
			###Default to chatbot###
		self.location = location
		if Speak("Checking for Internet connection") == False:										#Checks to see if gTTS is functioning properly
			print("I could not connect to the Internet, running in offline mode.")				
			print("I will not be able to talk, but I can print out whatever respones I have.")
		else:
			Speak("Connected to internet!")		

	def Listen(self, prompt):
		waiting = False
		while True:
			self.userCommand = ""	
			#with sr.Microphone(device_index=2, chunk_size = 2048, sample_rate = 48000) as source: 	#Use for nice USB mics
			with sr.Microphone(sample_rate = 4###If suites all return false#### (Suite commands run their respective commands and return True if something was run)
			###Default to chatbot###8000) as source:
				try:
					if(prompt != ""):
						Speak(prompt)
				except:
					pass
				r.energy_threshold += 200
				print "Waiting for words..."
				audio = r.listen(source)

				print("...")

				try:
					self.userCommand = r.recognize_google(audio)
					self.userCommand.lower()
					if self.userCommand.__contains__("hey karen"):
						print "Getting command.."
						extractIntent(self.userCommand)
						importCommands(self.userCommand, True)
					elif self.userCommand == "hey karen":
						pygame.init()																		
						pygame.mixer.init()
						pygame.mixer.music.load("start.mp3")												#play start listening tone
						pygame.mixer.music.play()
						while pygame.mixer.music.get_busy():
							pygame.time.Clock().tick(10)
						Speak("Yes?")
						print "Waiting for command.."
						waiting = True
					else:
						pass
					if waiting == True:
						extractIntent(self.userCommand)
						importCommands(self.userCommand, False)
						waiting = False
						pygame.init()																	
						pygame.mixer.init()
						pygame.mixer.music.load("end.mp3")												#play stop listening tone
						pygame.mixer.music.play()
						while pygame.mixer.music.get_busy():
							pygame.time.Clock().tick(10)
					else:
						pass
				except sr.UnknownValueError:
					print("Unknown Value from Google, or nothing heard")
				except sr.RequestError as e:
					print("Could not request results from Google Speech Recognition service; {0}".format(e))	
				except:
					print("Unknown error")

	#Text-To-Speech
	def Speak(self, whatToSay):

		print(whatToSay)
		tts = gTTS(text=whatToSay, lang='en')											#Translate text to audio file
		tts.save("temp.mp3")															#save as temp.mp3

		pygame.init()																	#play temp.mp3
		pygame.mixer.init()
		pygame.mixer.music.load("temp.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(10)

		remove("temp.mp3")  															# remove temporary file
		
	#Controls the import of new Command Suites and passes information from Assistant 
	def importCommands(self, cmd, parse):
		if parse == True:
			cmd = cmd.split("hey karen ")[1]
			if DefaultSuite(self.intent, self.userCommand) == False:
				print "No command recognized"
				pass
			###Default to chatbot###
		else:
			if DefaultSuite == False:
				print "No command recognized"
				pass
			###Default to chatbot###
			
	#In Listen method, get intent and information from Wit.Ai		
	def extractIntent(self, cmd):														
		pass
