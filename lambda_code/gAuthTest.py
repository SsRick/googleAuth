import urllib.parse
import json

def lambda_handler(event, context):
    with open('cred.json') as f:
        data = json.load(f)

    client_id = data['web']['client_id']
    client_id = urllib.parse.quote(client_id, safe='')

    auth_uri = data['web']['auth_uri']

    redirect_uri = data['web']['redirect_uris'][0]
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




