#IMPORTS
import speech_recognition as sr
from gtts import gTTS
import pyglet																		#NOTE: Not used
import pygame
from time import sleep																#NOTE: Not used
from os import remove

# VARIABLES
r = sr.Recognizer()

#CODE
#Wait for "Karen"
def startListening(prompt):	
	
	with sr.Microphone(sample_rate = 48000) as source:								#For laptop mics
	#with sr.Microphone(device_index=2, chunk_size = 2048, sample_rate = 48000) as source: #For USB mics
		userCommands = ""
		r.adjust_for_ambient_noise(source)											#Adjust for ambient noise by listening for 1 second
		print "THRESHOLD: " + str(r.energy_threshold)
		r.energy_threshold += 200														#Threshold offset
																					#NOTE: This delays each listening by 1 second - needs reworking
		try:																		
			if (prompt != ""):
				Speak(prompt)		
		except:
			pass		
		print "Waiting for words..."
		audio = r.listen(source)													#Wait and listen for recognized audio from source
		
	print("...")																	#Heard something
	
	try:
		userCommand = r.recognize_sphinx(audio)										#Attempt to recognize words
	except:
		print "Sphinx recognized no audible words"
		return False, userCommand
	
	if userCommand.__contains__("karen"):											#If we heard "Karen" anywhere in the speech
		return True, userCommand													#Move to recognizing commands, and pass the userCommand
	else:
		return False, userCommand


#Recognizing Commands (more accurate)
def SR(prompt):
	
	#with sr.Microphone(device_index=2, chunk_size = 2048, sample_rate = 48000) as source: #Use for nice USB mics
	with sr.Microphone(sample_rate = 48000) as source:
		userCommand = ""
		r.adjust_for_ambient_noise(source)
		print "THRESHOLD: " + str(r.energy_threshold)
		r.energy_threshold += 230
		
		try:
			if(prompt != ""):
				Speak(prompt)
		except:
			pass
		print "Waiting for words..."
		audio = r.listen(source)
		
	print("...")
	
	try:
		# userCommand = r.recognizer_instance.recognize_wit(audio, "6O77VBF2JYUNJDOU563T5GGXB6EF62OS", show_all = False)
		userCommand = r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Unknown Value from Google, or nothing heard")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))	
	except:
		print("Unknown error")
		
	return userCommand


#Text-To-Speech
def Speak(whatToSay):
	
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
