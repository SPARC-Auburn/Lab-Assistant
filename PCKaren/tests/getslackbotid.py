"""
Prints out the id of the bot named Karen
Run the following in the terminal: python getslackbotid.py "xoxb-abcd-1234"
with correct token in quotes
"""
from slackclient import SlackClient
import sys


BOT_NAME = 'karen'


def printid(token):
    slack_client = SlackClient(token)
    if __name__ == "__main__":
        api_call = slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == BOT_NAME:
                    print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
        else:
            print("could not find bot user with the name " + BOT_NAME)


if __name__ == "__main__":
    tkn = str(sys.argv[1])
    printid(tkn)
