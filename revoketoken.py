# simple code for revoking the token 
import requests

requests.post('https://oauth2.googleapis.com/revoke',
    params={'token': 'ya29.GluwBrgcnzE24i5Wq7p8JbincM3UdME2cDkVzff8bOuj42emIMMdookhr2nqsf-ZikW9weawAxT9qAizwph3ZvHl7HWGd5SYUF0ZZmE_UZ3jbx3BuKXFMIaM_6Rr'},
    headers = {'content-type': 'application/x-www-form-urlencoded'})