# suite.file
import urllib
from bs4 import BeautifulSoup
import pafy
import random
import os
import datetime
# import vlc
# import subprocess
# from properties import *
# from sys import executable

# DEFAULT FUNCTIONS
# TODO: Implement DialogFlow API


def getweather(assistant, place):
    weather_url = "http://www.bing.com/search?q=weather+" + place.replace(" ", "+")
    print(weather_url)
    try:
        with urllib.request.urlopen(weather_url) as url_:
            html = url_.read()
            soup = BeautifulSoup(html, "html.parser")
            print(soup)
            temp = str((soup.findAll(attrs={'class': 'wtr_currTemp b_focusTextLarge'})[0]))
            temp = temp.replace('<div class="wtr_currTemp b_focusTextLarge">', "")
            temp = temp.replace("</div>", "")
            assistant.speak("The temp for" + place + " is " + temp + "degrees")
    except:
        assistant.speak("I couldn't connect to Bing")


def bingsearch(assistant, thingToSearch):
    searchUrl = "http://www.bing.com/search?q=" + thingToSearch.replace(" ", "+")
    print(searchUrl)
    try:
        with urllib.request.urlopen(searchUrl) as url_:
            html = url_.read()
            soup = BeautifulSoup(html, "html.parser")
            print(soup)
            try:
                result = str((soup.findAll(attrs={'class': 'rwrl rwrl_sec rwrl_padref'})[0]))
            except:
                result = str((soup.findAll(attrs={'class': 'b_focusTextMedium'})[0]))
            print("result " + result)
            result = result.replace('<div class="rwrl rwrl_sec rwrl_padref"><p>', "")
            result = result.replace("</p></div>", "")
            result = result.replace('<div class="b_focusTextMedium">', '')
            result = result.replace('</div>', '')
            print(result)
            assistant.speak(result)
    except:
        assistant.speak("I couldn't connect to Bing")


def getyoutubeaudiourl(assistant, searchWords):
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
            counter += 1
            url = ('https://www.youtube.com' + soup.findAll(attrs={'class': 'yt-uix-tile-link'})[1 + counter]['href'])
        song = song.getbestaudio()
        print(song.url)
        return [song.url, searchWords]


def telljoke(assistant):
    jokes = [
        "Your GPA",
        "Why did the chicken cross the road? To get to the sparc lab",
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
    assistant.speak(jokes[joke])
    assistant.speak(laughs[laugh])


# def PlayYoutubeAudio(assistant, url, searchWords):
#     assistant.speak("playing " + searchWords)
#     p.set_mrl(url)
#     p.play()


def feelings(assistant):
    karens_feelings = [
        "i am bored.  i have not learned any new commands",
        "great. today has been very exciting",
        "it is important to remember computers do not have feelings"
    ]
    feeling = random.randrange(0, len(karens_feelings), 1)
    assistant.speak(karens_feelings[feeling])


# def WriteToArduino(thingToWrite):
#     try:
#         ser = serial.Serial(arduinoPort, 9600)
#         ser.write(thingToWrite.encode())
#         Speak("Command sent successfully")
#     except:
#         Speak("Could not connect to Arduino on " + arduinoPort)


def gettotalhours(assistant, person):
    if os.path.isfile("PeopleNoCode/" + person + ".txt"):
        hoursIn = []
        hoursOut = []
        minutesIn = []
        minutesOut = []
        hour = 0.0
        minute = 0.0
        with open("PeopleNoCode/" + person + ".txt", "r") as file:
            for line in file:
                if line.__contains__("Logged in at: "):
                    line = line.replace("Logged in at: ", "")
                    hour = ((line[0:2]))
                    hour = hour.replace(":", "")
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
                totalHours += (hoursOut[i] - hoursIn[i]) + ((((minutesOut[i] * 60) - (minutesIn[i] * 60)) / 60) / 60)
                i += 1
            if (totalHours >= 5):
                assistant.speak(
                    "You have logged " + str(totalHours) + " hours, you can now get pin code access to the spark lab.")
                os.remove("PeopleNoCode/" + person + ".txt")
                with open("PeopleActive/" + person + ".txt", "w") as newFile:
                    newFile.write("Last active: " + str(datetime.datetime.now().date().month) + "/" + str(
                        datetime.datetime.now().date().day))
            else:
                assistant.speak("You have logged " + str(totalHours) + " hours, only " + str(9 - totalHours) + "to go!")

    else:
        assistant.speak("I don't seem to have a file on you.")


def defaultsuitemethod(assistant, intent, userCommand):
    print userCommand
    if "how are you" in userCommand:
        feelings(assistant)
        return True
    elif "tell me a joke" in userCommand:
        telljoke(assistant)
        return True
    else:
        return False
