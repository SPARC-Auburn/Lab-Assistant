"""
Program Name: voice_properties.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: Contains the assistant class which is responsible for recording and decoding mic input and speaking
responses back to the user.
"""
from gtts import gTTS
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
        """Initializes assistant, adjusts for ambient noise, and checks TTS"""
        self.name = name
        self.name = "Karen"
        self.purpose = purpose
        self.voice = voice
        self.location = location
        self.r = sr.Recognizer()
        self.intent = ""

        with sr.Microphone(device_index=2, sample_rate=48000) as source:
            self.r.adjust_for_ambient_noise(source)  # Adjust for ambient noise by listening for 1 second
            # self.r.energy_threshold = 30 #Threshold offset
            print ("THRESHOLD: " + str(self.r.energy_threshold))

        print("Initializing {}...".format(self.name))

        try:
            self.speak("My name is " + self.name + " and I am here " + self.purpose)
        except Exception:
            print("Unable to connect to the Internet")

    # TODO: Figure out more elegant solution using wake word (Hey Karen, OK Karen, etc.)
    def processcommand(self, usermsg, source):
        """
        Processes command from user and deals with wake word detection
        :param usermsg: The message that the user inputted
        :param source: Microphone audio source
        """
        print ("Command heard: " + usermsg)
        if self.userCommand == "hey karen":
            self.playsound("start.mp3")
            self.speak("Yes?")
            print ("Waiting for command..")
            response_heard = False
            while not response_heard:
                print ("THRESHOLD: " + str(self.r.energy_threshold))
                print ("Waiting for words...")
                try:
                    audio = self.r.listen(source, timeout=5)
                    print("...")
                    self.playsound("end.mp3")
                    try:
                        self.userCommand = self.r.recognize_google(audio)
                        self.userCommand = self.userCommand.lower()
                        response_heard = True
                    except sr.UnknownValueError:
                        print("Unknown Value from Google, or nothing heard")
                    except sr.RequestError as e:
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    except Exception as e:
                        print (str(e))
                except Exception:
                    print ("Heard nothing")
                    pass

        elif self.userCommand.__contains__("hey karen"):
            print ("Getting command..")
            self.userCommand = self.userCommand.split("hey karen ")[1]
        else:
            pass

    def listen(self, prompt):
        """Listens to response from microphone and converts to text"""
        self.userCommand = ""
        with sr.Microphone(device_index=2, chunk_size=1024, sample_rate=48000) as source:  # Use for nice USB mics
            # with sr.Microphone(sample_rate = 44100) as source:
            # try:
            #     if prompt != "":
            #         self.speak(prompt)
            # except Exception:
            #     pass
            print ("THRESHOLD: " + str(self.r.energy_threshold))
            print ("Waiting for words...")
            try:
                audio = self.r.listen(source, timeout=5)
                # self.playSound("end.mp3")
                try:
                    self.userCommand = self.r.recognize_google(audio)
                    self.userCommand = self.userCommand.lower()
                    self.processcommand(self.userCommand, source)
                except sr.UnknownValueError:
                    # print("Unknown Value from Google, or nothing heard")
                    print ("...")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                except Exception as e:
                    print (str(e))
            except Exception:
                print ("No audio heard")
                pass

    def speak(self, whattosay):
        """
        Converts text to speech
        :param whattosay: Text to speak
        """
        print (whattosay)
        audio_file = "response.mp3"
        tts = gTTS(text=str(whattosay), lang="en")
        tts.save(audio_file)
        self.playsound(audio_file)
        os.remove(audio_file)

    @staticmethod
    def playsound(audio_file):
        """
        Plays mp3 use process best for each operating system
        :param audio_file: String of location of mp3 file to be played
        """
        if platform == "linux" or platform == "linux2":
            pygame.mixer.pre_init(22050, -16, 1, 2048)
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
