import urllib.parse
import json


def lambda_handler(event, context):
    client_id = event['client_id']
    client_id = urllib.parse.quote(client_id, safe='')

    auth_uri = event['auth_uri']

    redirect_uri = event['redirect_uri']
    redirect_uri = urllib.parse.quote(redirect_uri, safe='')

    # scope = 'https://www.googleapis.com/auth/contacts https://www.googleapis.com/auth/contacts.readonly https://www.googleapis.com/auth/userinfo.profile'
    # scope = 'https://www.googleapis.com/auth/drive.readonly'
    scope = event['scope']
    scope = urllib.parse.quote(scope, safe='')

    part2 = 'client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&scope=' + scope + '&access_type=offline&response_type=code'
    finalurl = auth_uri +'?' +part2
    print(finalurl+'\n')
    
    return {
        'statusCode': 200,
        'url': finalurl
    }




