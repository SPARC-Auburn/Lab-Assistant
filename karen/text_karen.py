"""
Program Name: text_karen.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A text based version of Karen.  All commands are inputted and all responses are displayed in the terminal.
"""

import manage_suites


def main():
    while True:
        user_message = raw_input('> ')
        if len(user_message) > 0:
            whattosay = manage_suites.getresponse(user_message)
            print("< " + whattosay)


if __name__ == "__main__":
    main()
