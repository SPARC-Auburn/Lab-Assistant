import speech_recognition as sr
from gtts import gTTS
import pyglet
import pygame
from time import sleep
from os import remove

r = sr.Recognizer()

def SR(prompt):
    #with sr.Microphone(device_index=2, chunk_size = 2048, sample_rate = 48000) as source: #Use for nice USB mics
    with sr.Microphone() as source:	#Use for laptops
        userCommand = ""
	r.adjust_for_ambient_noise(source)
        r.energy_threshold += 230
        try:
            if(prompt != ""):
                Speak(prompt)
        except:
            pass
        audio = r.listen(source)
    print("...")
    try:
        # userCommand = r.recognizer_instance.recognize_wit(audio, "6O77VBF2JYUNJDOU563T5GGXB6EF62OS", show_all = False)
        userCommand = r.recognize_google(audio)
    except sr.UnknownValueError:
	print("Unknown Value from Google, trying Sphinx")
        try:
            userCommand = r.recognize_sphinx(audio)
        except:
	    print("Sphinx recognized no command")
            pass
    except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))	
        try:
            userCommand = r.recognize_sphinx(audio)
        except:
	    print("Sphinx recognized no command")
            pass
    except:
	print("Unknown error")
    return userCommand

def Speak(whatToSay):
    try:
	print(whatToSay)
        tts = gTTS(text=whatToSay, lang='en')
        tts.save("temp.mp3")
        pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load("temp.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)
    except:
	print("Error in TTS")
        print(whatToSay)
        return False

    remove("temp.mp3")  # remove temperory file
