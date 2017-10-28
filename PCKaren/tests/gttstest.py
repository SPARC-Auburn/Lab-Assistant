"""
A testing program that utilizes Googles Text To Speech (GTTS) engine and pyglet to speak text.
Ensure that AVbin is installed for pyglet to run properly: https://avbin.github.io/AVbin/Download.html
"""

from gtts import gTTS
import time
import os
import pyglet


def speak(whattosay):
    """
    :param whattosay: String that will be spoken by pyglet
    """
    print (whattosay)
    audio_file = "response.mp3"
    tts = gTTS(text=str(whattosay), lang="en")
    tts.save(audio_file)
    response = pyglet.media.load(audio_file, streaming=False)
    response.play()
    time.sleep(response.duration)
    os.remove(audio_file)


speak("One")
speak("Two")
speak("Three")
speak("It Works!")
