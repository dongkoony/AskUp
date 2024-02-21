import os
import requests

def send_slack_message(channel_id, text):
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {os.environ['SLACK_BOT_TOKEN']}"}
    data = {"channel": channel_id, "text": text}
    response = requests.post(url, headers=headers, json=data)
    return response.json()