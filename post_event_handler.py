import json
import os
import boto3
import requests

def lambda_handler(event, context):
    # Slack에서 받은 이벤트를 파싱합니다.
    body = json.loads(event['body'])
    if 'challenge' in body:
        # URL 검증 요청에 응답합니다.
        return {'statusCode': 200, 'body': json.dumps({'challenge': body['challenge']})}
    
    # 메시지 이벤트 처리 로직
    if 'event' in body:
        message_event = body['event']
        # 메시지를 SQS로 전송하는 로직 추가
        sqs = boto3.client('sqs')
        queue_url = 'SQS_QUEUE_URL' # SQS 큐 URL을 여기에 입력하세요.
        sqs_response = sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(message_event))
        
        return {'statusCode': 200, 'body': json.dumps({'message': 'Event processed'})}

    return {'statusCode': 400, 'body': 'No valid event found'}
