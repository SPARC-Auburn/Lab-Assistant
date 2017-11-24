"""
Program Name: voice_client.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A voice based version of Karen.  Uses speech to text and text to speech to interact with user.
"""
from properties import *
import manage_suites


def main(assistant):
    """Main function that keeps Karen listening and responding"""
    while True:
        if assistant.listen():
            user_message = str(assistant.userCommand)
            if len(user_message) > 0:
                whattosay = manage_suites.getresponse(user_message)
                assistant.speak(whattosay)
        else:
            pass


if __name__ == "__main__":
    print("What microphone input are you using (ex: 1 for built-in and 2 for USB mic)?")
    mic = -1
    while mic not in range(0, 10):
        mic = int(raw_input("< "))
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    name = config.get('ID', 'Name')
    language = config.get('Preferences', 'Language')
    purpose = config.get('ID', 'Purpose')
    set_location = config.get('ID', 'Location')
    input = config.get('Preferences', 'Input')
    output = config.get('Preferences', 'Output')
    karen = Assistant(name, language, purpose, set_location, input, output, mic)
    main(karen)
