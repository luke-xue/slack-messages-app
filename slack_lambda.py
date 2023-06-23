def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first'], event['last'])  
    return { 
        'message' : message
    }