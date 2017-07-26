import speech_recognition as sr
from gtts import gTTS
import pyglet
from time import sleep
from os import remove

r = sr.Recognizer()

def SR(prompt):
    with sr.Microphone() as source:
        userCommand = ""
        r.energy_threshold = 1200
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
    except:
        try:
            userCommand = r.recognize_sphinx(audio)
        except:
            pass
    return userCommand

def Speak(whatToSay):
    try:
        tts = gTTS(text=whatToSay, lang='en')
        tts.save("temp.mp3")
        music = pyglet.media.load("temp.mp3", streaming=False)
        music.play()
        sleep(music.duration)  # prevent from killing
    except:
        print(whatToSay)
        return False

    remove("temp.mp3")  # remove temperory file
