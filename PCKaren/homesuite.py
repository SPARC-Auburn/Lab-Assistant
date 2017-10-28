# suite.file
"""
Program Name: homesuite.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A collection of functions pertaining to home automation.
"""
import random

# TODO: Implement DialogFlow API


def turnonlight(assistant):
    assistant.speak("Turning on the light")


def turnofflight(assistant):
    assistant.speak("Turning off the light")


def homesuitemethod(assistant, intent, userCommand):
    if "turn on" in userCommand:
        turnonlight(assistant)
        return True
    elif "turn off" in userCommand:
        turnofflight(assistant)
        return True
    return False
