import os
import json
import urllib3


def lambda_handler(event, context):
    # print(event)
    # print(type(event))
    # print(dir(event))
    # j = json.loads(event)
    payload = json.dumps({'text': f'Issue Created: {event["issue"]["html_url"]}'})
    url = os.getenv("SLACK_URL")
    http = urllib3.PoolManager()
    response = http.request("POST", url, body=payload, headers={"Content-Type": "application/json"})
    return response.data.decode()
