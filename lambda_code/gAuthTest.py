import urllib.parse
import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'gauth-bucket-test'
    key = 'cred.json'

    response = s3.get_object(Bucket = bucket, Key = key)
    jsonData = json.loads(response['Body'].read().decode('utf-8'))

    client_id = jsonData['web']['client_id']
    client_id = urllib.parse.quote(client_id, safe='')

    auth_uri = jsonData['web']['auth_uri']

    redirect_uri = jsonData['web']['redirect_uris'][0]
    redirect_uri = urllib.parse.quote(redirect_uri, safe='')

    scope = 'https://www.googleapis.com/auth/contacts https://www.googleapis.com/auth/contacts.readonly https://www.googleapis.com/auth/userinfo.profile'
    scope = urllib.parse.quote(scope, safe='')

    part2 = 'client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&scope=' + scope + '&access_type=offline&response_type=code'
    finalurl = auth_uri +'?' +part2
    print(finalurl+'\n')
    
    return {
        'statusCode': 200,
        'url': finalurl
    }




