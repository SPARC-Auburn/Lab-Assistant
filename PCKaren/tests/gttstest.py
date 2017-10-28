"""
A testing program that utilizes Googles Text To Speech (GTTS) engine and pyglet to speak text.
Ensure that AVbin is installed for pyglet to run properly: https://avbin.github.io/AVbin/Download.html
"""

from gtts import gTTS
import time
import os
from sys import platform
if platform == "linux" or platform == "linux2":
    import pygame
else:
    import pyglet   

def speak(whattosay):
    print (whattosay)
    audio_file = "response.mp3"
    tts = gTTS(text=str(whattosay), lang="en")
    tts.save(audio_file)
    playsound(audio_file)
    os.remove(audio_file)

def playsound(audio_file):
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


speak("One")
speak("Two")
speak("Three")
speak("It Works!")
