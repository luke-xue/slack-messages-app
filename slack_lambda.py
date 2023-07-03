import json
import os
from slack_sdk import WebClient
from datetime import datetime
import pytz
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



from dotenv import load_dotenv

load_dotenv()

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
        print(datetime.fromtimestamp(float(ts)).strftime('%Y-%m-%d %H:%M:%S'))
    return None

def add_message_to_sheet(spreadsheet_id, timestamp, name, message):
    creds, _ = google.auth.default()

    try:
        service = build('sheets', 'v4', credentials=creds)

        requests = []
        requests.append({
            'appendCells': {
                "sheetId": os.environ['SHEET_ID'],
                "rows": [
                    {
                    "values": [
                        {
                        "userEnteredValue": {
                            "stringValue": timestamp
                            }
                        },
                        {
                        "userEnteredValue": {
                            "stringValue": name
                            }
                        },
                        {
                        "userEnteredValue": {
                            "stringValue": message
                            }
                        }
                    ]
                    }
                ],
                "fields": "userEnteredValue"
                }
        })

        body = {
            'requests': requests
        }
        response = service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body).execute()
        return response

    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

add_message_to_sheet(os.environ['SPREADSHEET_ID'],"time","name","text")