import json

def lambda_handler(event, context):
    j = json.loads(event)
    return {
        'statusCode': 200,
        'body': json.dumps({'text': f'Issue Created: {j["issue"]["html_url"]}'})
    }
