from Speech import *
from sys import executable
import urllib
from bs4 import BeautifulSoup
import pafy
import vlc
import random
import os
import subprocess
import datetime
# TODO: Find a better chat-bot interface, or create one
from chatterbot import ChatBot

chatbot = ChatBot(
'Karen',
trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

#try:
#    i = vlc.Instance()
#    p = i.media_player_new()
#except:
#    print("VLC could not be found")


def GetWeather(place):
    weatherUrl = "http://www.bing.com/search?q=weather+"+place.replace(" ","+")
    print(weatherUrl)
    try:
        with urllib.request.urlopen(weatherUrl) as url_:
            html = url_.read()
            soup = BeautifulSoup(html, "html.parser")
            print(soup)
    #         wob_t
            temp = str((soup.findAll(attrs={'class': 'wtr_currTemp b_focusTextLarge'})[0]))
            temp = temp.replace('<div class="wtr_currTemp b_focusTextLarge">',"")
            temp = temp.replace("</div>","")
            Speak("The temp for"+place+" is "+temp + "degrees")
    except:
        Speak("I couldn't connect to Bing")

def BingSearch(thingToSearch):
    searchUrl = "http://www.bing.com/search?q=" + thingToSearch.replace(" ", "+")
    print(searchUrl)
    try:
        with urllib.request.urlopen(searchUrl) as url_:
            html = url_.read()
            soup = BeautifulSoup(html, "html.parser")
            print(soup)
            #         wob_t
            try:
                result = str((soup.findAll(attrs={'class': 'rwrl rwrl_sec rwrl_padref'})[0]))
            except:
                result = str((soup.findAll(attrs={'class': 'b_focusTextMedium'})[0]))
            print("result "+result)
            result = result.replace('<div class="rwrl rwrl_sec rwrl_padref"><p>', "")
            result = result.replace("</p></div>", "")
            result = result.replace('<div class="b_focusTextMedium">','')
            result = result.replace('</div>', '')
            print(result)
            Speak(result)
    except:
        Speak("I couldn't connect to Bing")


def GetYoutubeAudioURL(searchWords):
    textToSearch = searchWords
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    with urllib.request.urlopen(url) as url_:
        html = url_.read()
        soup = BeautifulSoup(html, "html.parser")
        url = ('https://www.youtube.com' + soup.findAll(attrs={'class': 'yt-uix-tile-link'})[0]['href'])
        counter = 0
        try:
            song = pafy.new(url)
        except:
            counter+=1
            url = ('https://www.youtube.com' + soup.findAll(attrs={'class': 'yt-uix-tile-link'})[1+counter]['href'])
        song = song.getbestaudio()
        print(song.url)
        return[song.url, searchWords]

def TellJoke():
    jokes = [
        "Your GPA",
        "Why did the chicken cross the road? To get to the spark lab",
        "What did the ghost say to the bee.? . . . Booooo-beeeee!",
        "Why did the chicken fall down the well? He couldn't see that well",
        "2 fish are in a tank, one turns to the other, do you  know how to drive this thing?",
        "Monorails make for good one liners"
    ]
    laughs = [
        "ha.ha.ha.",
        "hardy har har",
        "He. he. he.",
        "Now that's a kneee slapper"
    ]
    joke = random.randrange(0, len(jokes), 1)
    laugh = random.randrange(0, len(laughs), 1)
    Speak(jokes[joke])
    Speak(laughs[laugh])

def PlayYoutubeAudio(url, searchWords):
    Speak("playing " + searchWords)
    p.set_mrl(url)
    p.play()

# def WriteToArduino(thingToWrite):
#     try:
#         ser = serial.Serial(arduinoPort, 9600)
#         ser.write(thingToWrite.encode())
#         Speak("Command sent successfully")
#     except:
#         Speak("Could not connect to Arduino on " + arduinoPort)


def GetTotalHours(person):
    if(os.path.isfile("PeopleNoCode/"+person+".txt")):
        hoursIn = []
        hoursOut = []
        minutesIn = []
        minutesOut = []
        hour = 0.0
        minute = 0.0
        with open("PeopleNoCode/"+person+".txt","r") as file:
            for line in file:
                if line.__contains__("Logged in at: "):
                    line = line.replace("Logged in at: ","")
                    hour = ((line[0:2]))
                    hour = hour.replace(":","")
                    print(line)
                    print(line[3:6])
                    try:
                        minute = float(line[3:6])
                    except:
                        minute = float(line[2:5])
                    minutesIn.append(minute)
                    hoursIn.append(float(hour))
                if line.__contains__("Logged out at: "):
                    line = line.replace("Logged out at: ", "")
                    hour = ((line[0:2]))
                    hour = hour.replace(":", "")
                    minute = float(line[3:6])
                    minutesOut.append(minute)
                    hoursOut.append(float(hour))
                totalHours = 0.0
            i = 0
            file.close()
            print(hoursIn)
            print(hoursOut)
            print(minutesIn)
            print(minutesOut)
            while i < len(hoursIn):
                totalHours += (hoursOut[i] - hoursIn[i]) + ((((minutesOut[i]*60) - (minutesIn[i]*60))/60)/60)
                i+=1
            if(totalHours >= 5):
                Speak("You have logged "+ str(totalHours)+" hours, you can now get pin code access to the spark lab.")
                os.remove("PeopleNoCode/"+person+".txt")
                with open("PeopleActive/"+person+".txt", "w") as newFile:
                    newFile.write("Last active: "+str(datetime.datetime.now().date().month) + "/" + str(datetime.datetime.now().date().day))
            else:
                Speak("You have logged " + str(totalHours) + " hours, only "+str(9-totalHours) + "to go!")

    else:
        Speak("I don't seem to have a file on you.")


# TODO: Possibly make commands into a switch-case statement instead of if-else



def Commands(command):
    command = command.lower()
    if (command == "what time is it"):
        Speak("The time is " + str(datetime.datetime.now().time().hour) + ":" + str(
            datetime.datetime.now().time().minute))
    elif(command == "pause music" or command == "paws music"):
        p.pause()
    elif(command == "play music"):
        p.play()
    elif(command == "pass me the butter"):
        Speak("So thats my purpose? Oh My GOD!")
    
    elif(command.__contains__("logmein") or command.__contains__("log me in")):
        name = command.replace("logmein ", "")
        name = name.replace("log me in ", "")
        name = name.rstrip()
        # Speak("Welcome "+name+", logging you in!")
        while(name == ""):
            Speak("I will need a name for this.")
            name = SR("What is your name?");
            name = name.lower()
            name = name.rstrip()
        if(os.path.isfile("PeopleNoCode/"+name+".txt")):
            with open("PeopleNoCode/"+name+".txt","a")as file:
                file.write("\nLogged in at: "+str(datetime.datetime.now().time().hour)+":"+str(datetime.datetime.now().time().minute) + " on: "+str(datetime.datetime.now().date().month)+"/"+str(datetime.datetime.now().date().day)+"\n")
                Speak("Welcome back "+ name + ", you are now logged in.")
                file.close()
        elif(os.path.isfile("PeopleCode/"+name+".txt")):
            pass
        else:
            Speak("I don't seem to have a file on you. I'll create one. One moment please.")
            with open("PeopleNoCode/" + name + ".txt", "w")as file:
                file.write("\nLogged in at: " + str(datetime.datetime.now().time().hour) + ":" + str(
                    datetime.datetime.now().time().minute) + " on: " +
                           str(datetime.datetime.now().date().month) + "/" + str(datetime.datetime.now().date().day)+"\n")
            Speak("Welcome "+ name + ", you are now logged in!")
    
    elif (command.__contains__("log me out")):
        name = command.replace("log me out ", "")
        print(name)
        try:
            print(name)
            with open("PeopleNoCode/" + name + ".txt", "a")as file:
                file.write("\nLogged out at: " + str(datetime.datetime.now().time().hour) + ":" + str(
                    datetime.datetime.now().time().minute) + " on: " + str(
                    datetime.datetime.now().date().month) + "/" + str(datetime.datetime.now().date().day) + "\n")
                file.close()
                Speak("Goodbye " + name + ", you are now logged out.")
                GetTotalHours(name)
        except:
            Speak("I don't seem to have a file on you. So I can't log you out.")

    elif (command.__contains__("play music")):
        stuff = GetYoutubeAudioURL(command.lower().replace("play music ", ""))
        PlayYoutubeAudio(stuff[0],stuff[1])
    elif(command.__contains__("search being") or command.__contains__("search bing")):
        command = command.replace("search bing ","")
        command = command.replace("search being ", "")
        BingSearch(command)
    elif(command == "what are you"):
        Speak("I am Karen")
    elif(command.__contains__("weather for")):
        GetWeather(command.split("weather for ")[1])
    elif(command == "what is spark"):
        Speak("SPARK is awesome!")
    elif (command == "tell me a joke"):
        TellJoke()
   
    else:
        responce = (chatbot.get_response(command.replace("hey karen ","")))
        print(responce)
        Speak(str(responce))
