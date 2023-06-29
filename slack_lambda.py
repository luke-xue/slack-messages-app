import json
import os
from slack_sdk import WebClient
from datetime import datetime


client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

def lambda_handler(event, context):
    body = json.loads(event.get('body'))
    if body["type"] == "url_verification":
        return body
    elif body["type"] == "event_callback":
        return handle_callback(body)
    else:
        return None
    
def handle_callback(body):
    if body["event"]["type"] == "message":
        user_id = body["event"]["user"]
        ts = body["event"]["ts"]
        user = client.users_info(user=user_id)
        print(body["event"])
        print(user)
        print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
    return None