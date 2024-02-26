from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Slack 메시지 전송 함수
def send_slack_message(slack_token, channel, message, thread_ts=None):
    # Slack 클라이언트 초기화
    client = WebClient(token=slack_token)
    try:
        # Slack 채널에 메시지 전송
        response = client.chat_postMessage(
            channel=channel,
            text=message,
            link_names=True,
            thread_ts=thread_ts  # 스레드 내 메시지로 전송할 경우 해당 스레드의 timestamp
        )
        print("Message sent: ", response["ts"])  # 메시지 전송 성공 로그
    except SlackApiError as e:
        # Slack API 에러 처리
        print(f"Slack API Error: {e}")

# Slack 블록 메시지 전송 함수
def send_block_message(slack_token, channel, blocks, text, thread_ts=None):
    client = WebClient(token=slack_token)
    try:
        # Slack 채널에 블록 형식의 메시지 전송
        response = client.chat_postMessage(
            channel=channel,
            blocks=blocks,  # 블록 형식의 메시지 내용
            text=text,
            link_names=True,
            thread_ts=thread_ts
        )
        print("Block message sent: ", response["ts"])
    except SlackApiError as e:
        print(f"Slack API Error: {e}")

# Slack 일시적 메시지 전송 함수
def send_ephemeral_message(slack_token, channel, message, user, thread_ts=None):
    client = WebClient(token=slack_token)
    try:
        # 사용자에게만 보이는 일시적 메시지 전송
        response = client.chat_postEphemeral(
            channel=channel,
            text=message,
            user=user,  # 메시지를 받을 사용자 ID
            link_names=True,
            thread_ts=thread_ts
        )
        print("Ephemeral message sent: ", response["message_ts"])
    except SlackApiError as e:
        print(f"Slack API Error: {e}")

# Slack 일시적 블록 메시지 전송 함수
def send_ephemeral_block_message(slack_token, channel, blocks, text, user, thread_ts=None):
    client = WebClient(token=slack_token)
    try:
        # 사용자에게만 보이는 일시적 블록 메시지 전송
        response = client.chat_postEphemeral(
            channel=channel,
            blocks=blocks,
            text=text,
            user=user,
            link_names=True,
            thread_ts=thread_ts
        )
        print("Ephemeral block message sent: ", response["message_ts"])
    except SlackApiError as e:
        print(f"Slack API Error: {e}")
