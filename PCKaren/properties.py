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
	
	userCommand = ""
	def __init__(self, name, voice, purpose, location):
		self.name = name
		self.name = "Karen"
		self.purpose = purpose
		self.voice = voice
		self.location = location
		self.r = sr.Recognizer()
		self.intent = ""
		
		with sr.Microphone(device_index = 2, sample_rate = 44100) as source:
			self.r.adjust_for_ambient_noise(source)			#Adjust for ambient noise by listening for 1 second													
			#self.r.energy_threshold = 30																					#Threshold offset
			print "THRESHOLD: " + str(self.r.energy_threshold)
			
		print("Initializing {}".format(self.name))	
		self.chatbot = ChatBot('Karen', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')
		#chatbot.train("chatterbot.corpus.english")
		
		if self.Speak("I'm checking for an internet connection") == False:										#Checks to see if gTTS is functioning properly
			print("I could not connect to the Internet, running in offline mode.")				
			print("I will not be able to talk, but I can print out whatever respones I have.")
		else:
			self.Speak("I'm now connected to the internet!")
			self.Speak("My name is " + self.name + " and I am here " + self.purpose) 
			
				
	def Listen(self, prompt):
			self.userCommand = ""	
			with sr.Microphone(device_index=2, chunk_size = 2048, sample_rate = 48000) as source: 	#Use for nice USB mics
			#with sr.Microphone(sample_rate = 44100) as source:
				try:
					if(prompt != ""):
						self.Speak(prompt)
				except:
					pass
				print "THRESHOLD: " + str(self.r.energy_threshold)
				print "Waiting for words..."
				try:
					audio = self.r.listen(source, timeout = 5)
					
					print("...")
					#self.playSound("end.mp3")
					try:
						self.userCommand = self.r.recognize_google(audio)
						self.userCommand = self.userCommand.lower()
					except sr.UnknownValueError:
						print("Unknown Value from Google, or nothing heard")
					except sr.RequestError as e:
						print("Could not request results from Google Speech Recognition service; {0}".format(e))	
					except Exception as e:
						print str(e)
				except:
					print "No audio heard"
					pass

				print "Command heard: " + self.userCommand
				if self.userCommand == "hey karen":
					self.playSound("start.mp3")
					self.Speak("Yes?")
					print "Waiting for command.."
					responseHeard = False
					while responseHeard == False:
						print "THRESHOLD: " + str(self.r.energy_threshold)
						print "Waiting for words..."
						try:
							audio = self.r.listen(source, timeout = 5)
							print("...")
							self.playSound("end.mp3")
						except:
							print "Heard nothing"
							pass
						try:
							self.userCommand = self.r.recognize_google(audio)
							self.userCommand = self.userCommand.lower()
							responseHeard = True
						except sr.UnknownValueError:
							print("Unknown Value from Google, or nothing heard")
						except sr.RequestError as e:
							print("Could not request results from Google Speech Recognition service; {0}".format(e))	
						except Exception as e:
							print str(e)
							
					self.extractIntent(self.userCommand)							#Use command
				elif self.userCommand.__contains__("hey karen"):
					print "Getting command.."
					self.userCommand = self.userCommand.split("hey karen ")[1]
					self.extractIntent(self.userCommand)
				else:
					pass

	#Text-To-Speech
	def Speak(self, whatToSay):

		print(whatToSay)
		tts = gTTS(text=whatToSay, lang='en')											#Translate text to audio file
		tts.save("temp.mp3")															#save as temp.mp3

		self.playSound("temp.mp3")

		os.remove("temp.mp3")  															# remove temporary file
	
			
	#In Listen method, get intent and information from Wit.Ai		
	def extractIntent(self, cmd):
		pass
		###Possibly add ability for custom wit.ai api keys for seperate apps###
		
	def playSound(self, audio):
		pygame.init()																	
		pygame.mixer.init()
		pygame.mixer.music.load(audio)												#play tone
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
			pygame.time.Clock().tick(10)
			
