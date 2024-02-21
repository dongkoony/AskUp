import json
import os
import requests
import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        message_body = json.loads(record['body'])
        response = send_to_chatgpt(message_body['text'])  # ChatGPT API 호출
        send_slack_message(message_body['channel'], response)  # Slack으로 결과 전송

def send_to_chatgpt(text):
    # ChatGPT API 호출 로직 (가상 코드)
    return "ChatGPT 응답"

def send_slack_message(channel, text):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {os.getenv('SLACK_BOT_TOKEN')}",
        "Content-Type": "application/json"
    }
    payload = {
        "channel": channel,
        "text": text
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")
