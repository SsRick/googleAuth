from botocore.vendored import requests
import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'gauth-bucket-test'
    key = 'cred.json'
    tokenFile = 'firstToken.json'
    response = s3.get_object(Bucket = bucket, Key = key)
    jsonData = json.loads(response['Body'].read().decode('utf-8'))
    API_ENDPOINT = jsonData["web"]["token_uri"]
    print(event["code"])
    data = {'code':event["code"], 
        'redirect_uri':jsonData["web"]["redirect_uris"][0], 
        'client_id':jsonData["web"]["client_id"], 
        'client_secret':jsonData["web"]["client_secret"],
        'grant_type' : 'authorization_code',
        'scope' : 'https://www.googleapis.com/auth/contacts https://www.googleapis.com/auth/contacts.readonly https://www.googleapis.com/auth/userinfo.profile',
        'access_type' : 'offline'} 

    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data) 

    # extracting response text 
    response = r.text 
    print(response)
    
    body = json.dumps(response)
    response = s3.put_object(Bucket = bucket,
        Key = tokenFile,
        Body = body,
        ContentType='application/json')
    # return response




