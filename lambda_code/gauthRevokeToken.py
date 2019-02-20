from botocore.vendored import requests
import json

def lambda_handler(event, context):
    requests.post('https://oauth2.googleapis.com/revoke',
    params={'token': event["token"]},
    headers = {'content-type': 'application/x-www-form-urlencoded'})
    return {
        'statusCode': 200,
        'body': json.dumps('Revoked token!')
    }
