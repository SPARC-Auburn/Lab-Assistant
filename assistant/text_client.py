"""
Program Name: text_client.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A text based version of the virtual assistant.
All commands are inputted and all responses are displayed in the terminal.
"""

import manage_suites
from time import sleep
from sys import stdout

assistant_name = "Karen"
assistant_purpose = "to assist SPARC members"
assistant_label = assistant_name.upper() + " > "


def main():
    print(assistant_label + "My name is " + assistant_name + " and I am here " + assistant_purpose +
          ". How may I help you?")
    while manage_suites.is_connected():
        user_message = raw_input('< ')
        if len(user_message) > 0:
            whattosay = manage_suites.getresponse(user_message)
            print_slow(assistant_label + whattosay)


def print_slow(message):
    word_list = message.split()
    for word in word_list:
        stdout.write(word + " ")
        sleep(0.25)
    print("")


if __name__ == "__main__":
    print("Starting assistant...")
    sleep(1)
    main()
