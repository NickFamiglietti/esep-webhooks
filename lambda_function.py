import json
import requests

def lambda_handler(event, context):
    
    post_body = event['body']
    
   
    try:
        data = json.loads(post_body)
        
       
        target_url = 'https://hooks.slack.com/services/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'  
        
        
        response = requests.post(target_url, json=data)
        
        if response.status_code == 200:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Data sent successfully'})
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'message': 'Failed to send data'})
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
