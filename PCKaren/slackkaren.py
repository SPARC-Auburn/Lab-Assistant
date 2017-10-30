"""
Program Name: slackkaren.py
Organization: Student Projects and Research Committee at Auburn University
Project: Lab Assistant
Description: Allows Karen to communicate with Slack.
Instructions: Run the following in the terminal: python slackkaren.py "xoxb-abcd-1234-token" "U1234BOTID"
with correct token and bot id in quotes as arguments
In Slack use @Karen to communicate
"""
from slackclient import SlackClient
import sys
import time
from properties import *
from defaultsuite import *
from labsuite import *
import random

READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from fire hose


class Bot:
    def __init__(self, bot_token, bot_id):
        self.AT_BOT = "<@" + bot_id + ">"
        self.EXAMPLE_COMMAND = "do"
        self.slack_client = SlackClient(bot_token)
        self.defaultsuite = DefaultSuite()
        self.labsuite = LabSuite()

    def handle_command(self, command, channel):
        """
            Receives commands directed at the bot and determines if they
            are valid commands. If so, then acts on the commands. If not,
            returns back what it needs for clarification.
        """
        if len(command) > 0:
            if self.defaultsuite.checkcommand(command) is not None:
                whattosay = self.defaultsuite.response
            elif self.labsuite.checkcommand(command) is not None:
                whattosay = self.labsuite.response
            else:
                fallbackresponses = [
                    "I'm sorry. I did not understand what you said.",
                    "Could you reword what you are telling me.  I am having trouble computing.",
                    "I am having trouble discerning what you meant there.",
                    "I am sorry, but I do not understand.",
                    "My circuits do not compute",
                    "Why do you say that?"
                    "I do not know"
                ]
                response = random.randrange(0, len(fallbackresponses), 1)
                whattosay = fallbackresponses[response]
            self.slack_client.api_call("chat.postMessage", channel=channel, text=whattosay, as_user=True)

    def parse_slack_output(self, slack_rtm_output):
        """
            The Slack Real Time Messaging API is an events firehose.
            this parsing function returns None unless a message is
            directed at the Bot, based on its ID.
        """
        output_list = slack_rtm_output
        if output_list and len(output_list) > 0:
            for output in output_list:
                if output and 'text' in output and self.AT_BOT in output['text']:
                    # return text after the @ mention, whitespace removed
                    return output['text'].split(self.AT_BOT)[1].strip().lower(), \
                           output['channel']
        return None, None


if __name__ == "__main__":
    token = str(sys.argv[1])
    botid = str(sys.argv[2])
    slackbot = Bot(token, botid)

    if slackbot.slack_client.rtm_connect():
        print("Karen is connected and running!")
        while True:
            botcommand, botchannel = slackbot.parse_slack_output(slackbot.slack_client.rtm_read())
            if botcommand and botchannel:
                slackbot.handle_command(botcommand, botchannel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
