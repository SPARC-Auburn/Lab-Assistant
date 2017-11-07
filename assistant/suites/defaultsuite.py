# suite.file
"""
Program Name: defaultsuite.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A collection of basic functions
"""

import dialogflow

CLIENT_ACCESS_TOKEN = 'd8cd9faa2fe14731b1187d05b7d6f409'


class DefaultSuite:
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
        self.response = self.agent.getspeech()
        if len(self.response) <= 0:
            return None
        elif self.response.lower() == "none":
            # Add additional features here if desired
            return None
        else:
            return self.response
