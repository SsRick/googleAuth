from botocore.vendored import requests
import json


def lambda_handler(event, context):

    API_ENDPOINT = event['token_uri']
    data = {'refresh_token':event["refresh_token"], 
        'redirect_uri':event["redirect_uri"], 
        'client_id':event["client_id"], 
        'client_secret':event["client_secret"],
        'grant_type' : 'refresh_token',
        'scope' : event["scope"],
        'access_type' : 'offline'} 

    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data) 

    # extracting response text 
    response = r.text 
    # print(response)

    return r.json()    
    # return response




