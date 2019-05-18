from botocore.vendored import requests
import json

def lambda_handler(event, context):

    API_ENDPOINT = event["token_uri"]
    print(event["code"])
    data = {'code':event["code"], 
        'redirect_uri':event["redirect_uri"], 
        'client_id':event["client_id"], 
        'client_secret': event["client_secret"],
        'grant_type' : 'authorization_code',
        'scope' : event["scope"],
        'access_type' : 'offline'} 

    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data) 

    # extracting response text 
    response = r.text 
    # print(response)
    return r.json()
    




