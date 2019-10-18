import os
import logging
import slack
import ssl as ssl_lib
import certifi
from piazza_bot import PiazzaBot
from authentication import SLACK_BOT_TOKEN

def send_message(web_client):
    message = bot.get_json_payload()
    response = web_client.chat_postMessage(**message)
    
@slack.RTMClient.run_on(event="message")
def reply_message(**payload):
    web_client = payload["web_client"]
    return send_message(web_client)

if __name__ == "__main__":
    bot = PiazzaBot("slack-testing")
    bot.find_unanswered(10)
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    slack_token = SLACK_BOT_TOKEN
    rtm_client = slack.RTMClient(token=slack_token, ssl=ssl_context)
    rtm_client.start()
