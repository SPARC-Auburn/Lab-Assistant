# suite.file
"""
Program Name: labsuite.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A collection of functions pertaining to the SPARC lab
"""

import dialogflow

CLIENT_ACCESS_TOKEN = 'c687739558a946c597b4dbe07f17aa5b'


class LabSuite:
    def __init__(self):
        """Initializes DialogFlow agent"""
        self.agent = dialogflow.Agent(CLIENT_ACCESS_TOKEN)
        self.response = ""

    def checkcommand(self, usermsg):
        """
        Sends the DialogFlow agent a message and speaks the response.
        :param usermsg: The message that the user inputted
        :returns True: True if response is found
        :returns False: False if response is not found
        """
        self.agent.sendcommand(usermsg)
        self.response = self.agent.getresponse()
        if len(self.response) <= 0:
            return None
        elif self.response.lower() == "none":
            # Add additional features here if desired
            return None
        else:
            return self.response
