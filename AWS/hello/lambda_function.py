import json

def lambda_handler(event, contect):
    print(event)
    
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }