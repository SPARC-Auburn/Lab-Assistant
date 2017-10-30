# suite.file
"""
Program Name: defaultsuite.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A collection of basic functions
"""

import dialogflow

CLIENT_ACCESS_TOKEN = 'b3def782c82448d09039f553d5222dc4'


class DefaultSuite:
    def __init__(self):
        """Initializes DialogFlow agent"""
        self.agent = dialogflow.Agent(CLIENT_ACCESS_TOKEN)
        self.response = ""

    def checkcommand(self, usermsg):
        """
        Sends the DialogFlow agent a message and speaks the response.
        :param assistant: The assistant that is interacting with the user
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
