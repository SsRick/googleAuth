from botocore.vendored import requests

def lambda_handler(event, context):
    API_ENDPOINT = "https://oauth2.googleapis.com/token"
    print(event["refresh_token"])
    data = {'refresh_token':event["refresh_token"], 
        'redirect_uri':'http://localhost:8080/', 
        'client_id':'887597828597-kjg09tgnbhd6sc8pr8r32v71168v8dd7.apps.googleusercontent.com', 
        'client_secret':'-WwzKK48Y5Mq6wa5RhvUAV-1',
        'grant_type' : 'refresh_token',
        'scope' : 'https://www.googleapis.com/auth/contacts https://www.googleapis.com/auth/contacts.readonly https://www.googleapis.com/auth/userinfo.profile',
        'access_type' : 'offline'} 

    # sending post request and saving response as response object 
    r = requests.post(url = API_ENDPOINT, data = data) 

    # extracting response text 
    response = r.text 
    print(response)
    
    return response




