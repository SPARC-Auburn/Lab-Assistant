"""
Program Name: voice_client.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A voice based version of Karen.  Uses speech to text and text to speech to interact with user.
"""
from voice_properties import *
import manage_suites

karen = Assistant("Karen", "English", "to assist SPARC members", "SPARC Lab")


def main():
    """Main function that keeps Karen listening and responding"""
    while True:
        karen.listen("")
        user_message = str(karen.userCommand)
        if len(user_message) > 0:
            whattosay = manage_suites.getresponse(user_message)
            karen.speak(whattosay)


if __name__ == "__main__":
    main()
