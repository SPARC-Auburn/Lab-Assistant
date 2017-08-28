import os
import pygame
import time, sys
from gtts import gTTS
from os import remove
tts = gTTS(text = "This is a speech test", lang='en')
tts.save("testspeech.mp3")
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("testspeech.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
	pygame.time.Clock().tick(10)
print("This is a speech test")




