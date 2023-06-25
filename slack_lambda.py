import json

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
        print(body["event"]["text"])
    return None