"""
Program Name: dialogflow.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: Contains the dialogflow class which is responsible for gathering intent and entity data from dialogflow
"""

from __future__ import print_function
import os
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            os.pardir,
            os.pardir
        )
    )
    import apiai


# TODO: Figure out best way to process more complex commands with intents and entities
class Agent:
    def __init__(self, token):
        """
        Initializees the DialogFlow API
        :param token: the client access token for the agent
        """
        self.ai = apiai.ApiAI(token)
        self.returnedresponse = ""
        self.returnedintent = ""
        self.returnedentity = ""

    def sendcommand(self, usermsg):
        """
        Requests the response from DialogFlow agent
        :param usermsg: The message that the user inputted
        """
        request = self.ai.text_request()
        request.query = usermsg
        response = json.loads(request.getresponse().read())

        result = response['result']
        action = result.get('action')
        actionincomplete = result.get('actionIncomplete', False)

        self.returnedresponse = response['result']['fulfillment']['speech']

    def getresponse(self):
        return self.returnedresponse

    def getintent(self):
        return self.returnedintent

    def getentity(self):
        return self.returnedentity
