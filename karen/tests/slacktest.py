"""
Tests the Slack client bot connection.
Run the following in the terminal: python getslackbotid.py "xoxb-abcd-1234-token" "U1234BOTID"
with correct token and bot id in quotes as arguments
In Slack use @Karen to test bot.
"""
from slackclient import SlackClient
import sys
import time

READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from fire hose


class Bot:
    def __init__(self, bot_token, bot_id):
        # constants
        self.AT_BOT = "<@" + bot_id + ">"
        self.EXAMPLE_COMMAND = "do"
        self.slack_client = SlackClient(bot_token)

    def handle_command(self, command, channel):
        """
            Receives commands directed at the bot and determines if they
            are valid commands. If so, then acts on the commands. If not,
            returns back what it needs for clarification.
        """
        response = "Not sure what you mean. Use the *" + self.EXAMPLE_COMMAND + \
                   "* command with numbers, delimited by spaces."
        if command.startswith(self.EXAMPLE_COMMAND):
            response = "Sure...write some more code then I can do that!"
        self.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

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
    karen = Bot(token, botid)

    if karen.slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            botcommand, botchannel = karen.parse_slack_output(karen.slack_client.rtm_read())
            if botcommand and botchannel:
                karen.handle_command(botcommand, botchannel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
