import json
import boto3
import os
import openai
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# 환경 변수 로드 및 설정
load_dotenv()

# 환경 변수에서 API 키와 Slack 토큰을 가져옵니다.
chatgpt_api_key = os.getenv('CHATGPT_API_KEY')
slack_token = os.getenv('SLACK_TOKEN')

# OpenAI 클라이언트를 초기화합니다.
openai.api_key = chatgpt_api_key

# Slack 메시지 전송 함수
def send_slack_message(client, channel, message, thread_ts=None):
    # Slack 클라이언트를 이용해 메시지를 전송합니다.
    # 실패시 SlackApiError 예외를 캐치합니다.
    try:
        response = client.chat_postMessage(channel=channel, text=message, thread_ts=thread_ts)
        print("Message sent: ", response["ts"])
    except SlackApiError as e:
        print(f"Slack API Error: {e}")

# AWS Lambda 핸들러 함수
def lambda_handler(event, context):
    # Slack 클라이언트 초기화
    slack_client = WebClient(token=slack_token)
    
    # SQS 이벤트로부터 받은 메시지를 처리합니다.
    for record in event['Records']:
        # SQS 메시지 본문을 파싱합니다.
        body = json.loads(record['body'])
        
        # 필요한 정보를 추출합니다.
        channel = body.get('channel')
        message = body.get('message')
        thread_ts = body.get('thread_ts') or body.get('ts')

        # OpenAI를 사용하여 메시지에 대한 답변을 생성합니다.
        try:
            response = openai.Completion.create(
                model="text-davinci-003", prompt=message, temperature=0.7, max_tokens=150
            )
            response_message = response.choices[0].text.strip()

            # 생성된 답변을 Slack 채널로 전송합니다.
            send_slack_message(slack_client, channel, response_message, thread_ts)
            
        except Exception as e:
            # 예외 처리: 오류 메시지를 Slack으로 전송합니다.
            print(e)
            send_slack_message(slack_client, channel, "오류가 발생했습니다. 다시 시도해주세요.", thread_ts)

    return {'statusCode': 200, 'body': json.dumps('Event processed')}