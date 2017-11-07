# suite.file
"""
Program Name: fallbacksuite.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: A collection of fallback responses if other suites do not catch the command.
"""

import dialogflow

CLIENT_ACCESS_TOKEN = '95bf7491a61d49d5862f1465cb4bd5ab'


class FallBackSuite:
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
