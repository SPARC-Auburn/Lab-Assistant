#suite.file
import Assistant
from sys import executable
import urllib
from bs4 import BeautifulSoup
import pafy
import vlc
import random
import os
import subprocess
import datetime

#DEFAULT FUNCTIONS
# TODO: Find a better chat-bot interface, or create one

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

def Feelings():
	karens_feelings = [
	"i am bored.  i have not learned any new commands",
	"great. today has been very exciting",
	"it is important to remember computers do not have feelings"
	]
	feeling = random.randrange(0, len(karens_feelings), 1)
	Speak(karens_feelings[feeling])

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


def DefaultSuite(intent, userCommand):
	if (userCommand == "how are you"):
		Feelings()
		return True
	if (userCommand == "tell me a joke"):
		TellJoke()
		return True
	else:
		return False