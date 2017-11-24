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
import ConfigParser
from sys import platform

if platform == "linux" or platform == "linux2":
    print("OS Detected: Linux")
    import pygame
elif platform == "win32" or platform == "cygwin":
    print("OS Detected: Windows")
    import pyglet
elif platform == "darwin":
    print("OS Detected: MacOS")
    import pyglet
else:
    print("Unkown OS detected.  Compatibility cannot be guaraneteed")
    import pyglet


class Assistant:
    userCommand = ""

    def __init__(self, name, voice, purpose, location, input, output, microphone):
        """Initializes assistant, adjusts for ambient noise, and checks TTS"""
        self.name = name
        self.name = self.name.lower()
        self.purpose = purpose
        self.voice = voice
        self.location = location
        self.r = sr.Recognizer()
        self.mic = microphone
        self.input = input
        self.output = output

        with sr.Microphone(device_index=self.mic, chunk_size=1024, sample_rate=48000) as source:
            self.r.adjust_for_ambient_noise(source)  # Adjust for ambient noise by listening for 1 second
            # self.r.energy_threshold = 30 # Threshold offset
            print ("\tThreshold: " + str(self.r.energy_threshold))

        print("\tInitializing {}...".format(self.name))
        self.speak("My name is " + self.name + " and I am here " + self.purpose + ".  How may I help you?")

    def processcommand(self, usermsg, source):
        """
        Processes command from user and deals with wake word detection
        Returns True if Response was when assistant is awoken
        :param usermsg: The message that the user inputted
        :param source: Microphone audio source
        """
        print ("< " + usermsg)
        wake_words = ["hey", "ok", "okay", "yo", "you", "hi"]
        awake = False
        for word in wake_words:
            if self.userCommand == word + " " + self.name:
                awake = True
        if awake:
            self.playsound("start.mp3")
            self.speak("Yes?")
            print ("\tWaiting for command..")
            response_heard = False
            while not response_heard:
                print ("\tThreshold: " + str(self.r.energy_threshold))
                print ("\tWaiting for command...")
                try:
                    audio = self.r.listen(source, timeout=5)
                    print("...")
                    self.playsound("end.mp3")
                    try:
                        self.userCommand = self.r.recognize_google(audio)
                        self.userCommand = self.userCommand.lower()
                        response_heard = True
                        print ("< " + self.userCommand)
                    except sr.UnknownValueError:
                        print("\tUnknown Value from Google, or nothing heard")
                    except sr.RequestError as e:
                        print("\tCould not request results from Google Speech Recognition service; {0}".format(e))
                    except Exception as e:
                        print (str(e))
                except Exception:
                    print ("\tHeard nothing")
                    pass
            return True
        else:
            for word in wake_words:
                if self.userCommand.__contains__(word + " " + self.name):
                    print ("\tGetting command..")
                    self.userCommand = self.userCommand.split(word + " " + self.name + " ")[1]
                    return True
            return False

    def listen(self):
        """Listens to response from microphone and converts to text"""
        self.userCommand = ""
        with sr.Microphone(device_index=self.mic, chunk_size=1024, sample_rate=48000) as source:
            print ("\tThreshold: " + str(self.r.energy_threshold))
            print ("\tWaiting for words...")
            try:
                audio = self.r.listen(source, timeout=5)
                # self.playSound("end.mp3")
                try:
                    self.userCommand = self.r.recognize_google(audio)
                    self.userCommand = self.userCommand.lower()
                    if not self.processcommand(self.userCommand, source):
                        return False
                    else:
                        return True
                except sr.UnknownValueError:
                    print ("\t...")
                except sr.RequestError as e:
                    print("\tCould not request results from Google Speech Recognition service; {0}".format(e))
                except Exception as e:
                    print (str(e))
            except Exception:
                print ("\tNo audio heard")
                pass

    def speak(self, whattosay):
        """
        Converts text to speech
        :param whattosay: Text to speak
        """
        print (self.name.upper() + " > " + whattosay)
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
        else:
            sound = pyglet.media.load(audio_file, streaming=False)
            sound.play()
            time.sleep(sound.duration)
