import json

def lamba_handler(event, context):
    j = json.oads(event)
    return {
        'statusCode': 200,
        'body': json.dumps({'text': f'Issue Created: {j["issue"]["html_url"]}'})

    }
