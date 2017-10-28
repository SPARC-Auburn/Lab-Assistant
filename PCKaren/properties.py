# IMPORTS
# import DefaultSuite
from gtts import gTTS
from sys import platform
import time
import os
import time
import speech_recognition as sr
from sys import platform
if platform == "linux" or platform == "linux2":
    import pygame
else:
    import pyglet

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

        with sr.Microphone(device_index=2, sample_rate = 48000) as source:
            self.r.adjust_for_ambient_noise(source)  # Adjust for ambient noise by listening for 1 second
            # self.r.energy_threshold = 30 #Threshold offset
            print "THRESHOLD: " + str(self.r.energy_threshold)

        print("Initializing {}".format(self.name))

        if self.speak("I'm checking for an internet connection") == False:  # Checks to see gTTS is functioning properly
            print("I could not connect to the Internet, running in offline mode.")
            print("I will not be able to talk, but I can print out whatever respones I have.")
        else:
            self.speak("I'm now connected to the internet!")
            self.speak("My name is " + self.name + " and I am here " + self.purpose)

    def listen(self, prompt):
        self.userCommand = ""
        with sr.Microphone(device_index=2, chunk_size=1024, sample_rate=48000) as source:  # Use for nice USB mics
        # with sr.Microphone(sample_rate = 44100) as source:
            try:
                if prompt != "":
                    self.speak(prompt)
            except:
                pass
            print "THRESHOLD: " + str(self.r.energy_threshold)
            print "Waiting for words..."
            try:
                audio = self.r.listen(source, timeout=5)

                print("...")
                # self.playSound("end.mp3")
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
                self.playsound("start.mp3")
                self.speak("Yes?")
                print "Waiting for command.."
                response_heard = False
                while response_heard == False:
                    print "THRESHOLD: " + str(self.r.energy_threshold)
                    print "Waiting for words..."
                    try:
                        audio = self.r.listen(source, timeout=5)
                        print("...")
                        self.playsound("end.mp3")
                    except:
                        print "Heard nothing"
                        pass
                    try:
                        self.userCommand = self.r.recognize_google(audio)
                        self.userCommand = self.userCommand.lower()
                        response_heard = True
                    except sr.UnknownValueError:
                        print("Unknown Value from Google, or nothing heard")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    except Exception as e:
                        print str(e)

                self.extractintent(self.userCommand)  # Use command
            elif self.userCommand.__contains__("hey karen"):
                print "Getting command.."
                self.userCommand = self.userCommand.split("hey karen ")[1]
                self.extractintent(self.userCommand)
            else:
                pass

    # Text-To-Speech
    def speak(self, whattosay):
        print (whattosay)
        audio_file = "response.mp3"
        tts = gTTS(text=str(whattosay), lang="en")
        tts.save(audio_file)
        self.playsound(audio_file)
        os.remove(audio_file)

    def playsound(self, audio_file):
        if platform == "linux" or platform == "linux2":
            pygame.mixer.pre_init(22050,-16,1,2048)
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        elif platform == "darwin" or platform == "win32":
            sound = pyglet.media.load(audio_file, streaming=False)
            sound.play()
            time.sleep(sound.duration)
            
    # In Listen method, get intent and information from DialogFlow
    def extractintent(self, cmd):
        pass
