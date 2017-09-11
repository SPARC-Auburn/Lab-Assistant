#IMPORTS
import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import DefaultSuite

############NEED NEW CHATBOT##################
from chatterbot import ChatBot
#############################################

class Assistant:
	
	intent = ""
	userCommand = ""
	def __init__(self, name, voice, purpose, location):
		self.name = name
		self.name = "Karen"
		self.purpose = purpose
		self.voice = voice
		self.location = location
		self.r = sr.Recognizer()
		
		with sr.Microphone(sample_rate = 48000) as source:
			self.r.adjust_for_ambient_noise(source)											#Adjust for ambient noise by listening for 1 second													
			#self.r.energy_threshold = 400																					#Threshold offset
			print "THRESHOLD: " + str(self.r.energy_threshold)
			
		print("Initializing {}".format(self.name))	
		chatbot = ChatBot('Karen', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
		chatbot.train("chatterbot.corpus.english")
		
		if self.Speak("Checking for Internet connection") == False:										#Checks to see if gTTS is functioning properly
			print("I could not connect to the Internet, running in offline mode.")				
			print("I will not be able to talk, but I can print out whatever respones I have.")
		else:
			self.Speak("Connected to internet!")		

	def Listen(self, prompt):
		waiting = False
		while True:
			self.userCommand = ""	
			#with sr.Microphone(device_index=2, chunk_size = 2048, sample_rate = 48000) as source: 	#Use for nice USB mics
			with sr.Microphone(sample_rate = 48000) as source:
				try:
					if(prompt != ""):
						self.Speak(prompt)
				except:
					pass
				print "THRESHOLD: " + str(self.r.energy_threshold)
				print "Waiting for words..."
				audio = self.r.listen(source)

				print("...")

				try:
					self.userCommand = self.r.recognize_google(audio)
					self.userCommand.lower()
				except sr.UnknownValueError:
					print("Unknown Value from Google, or nothing heard")
				except sr.RequestError as e:
					print("Could not request results from Google Speech Recognition service; {0}".format(e))	
				except Exception as e:
					print str(e)
				print "Command heard: " + self.userCommand
				if self.userCommand.__contains__("hey karen"):
					print "Getting command.."
					self.intent = self.extractIntent(self.userCommand)
					self.importCommands(self.userCommand, True)
				elif self.userCommand == "hey karen":
					self.playSound("start.mp3")
					self.Speak("Yes?")
					print "Waiting for command.."
					waiting = True
				else:
					pass
				if waiting == True:
					self.intent = self.extractIntent(self.userCommand)
					self.importCommands(self.userCommand, False)
					waiting = False
					self.playSound("end.mp3")
				else:
					pass

	#Text-To-Speech
	def Speak(self, whatToSay):

		print(whatToSay)
		tts = gTTS(text=whatToSay, lang='en')											#Translate text to audio file
		tts.save("temp.mp3")															#save as temp.mp3

		self.playSound("temp.mp3")

		os.remove("temp.mp3")  															# remove temporary file
	
	#Searches for files with "#suite.file" to import as a suite
	def searchSuites(self):
		for file in os.listdir(os.curdir):
			if file.endswith(".py"):
				f = open(file, "r")
				firstLine = f.readline()
				if firstLine.__contains__("#suite.file"):
					print "Imported " + file[:-3]
					newSuite = __import__(file[:-3])
				
	#Passes information from Assistant to the found suite.files
	def importCommands(self, cmd, parse):
		if parse == True:
			cmd = cmd.split("hey karen ")[1]
			if DefaultSuite(intent, cmd) == False:
				print "No command recognized"
				response = (chatbot.get_response(cmd))
        		print(response)
        		Speak(str(response))
		else:
			if DefaultSuite(intent, cmd) == False:
				print "No command recognized"
				response = (chatbot.get_response(cmd))
        		print(response)
        		Speak(str(response))
			
	#In Listen method, get intent and information from Wit.Ai		
	def extractIntent(self, cmd):
		return self.intent
	
	def playSound(self, audio):
		pygame.init()																	
		pygame.mixer.init()
		pygame.mixer.music.load(audio)												#play tone
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(10)
