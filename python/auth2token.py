# this code will exchange the authorization code with a access token
# authorization code could be acquired by running the authurlcreate.py script
# the code is appended the the redirect uri
import requests 

API_ENDPOINT = "https://oauth2.googleapis.com/token"
 
data = {'code':'4/8gASKbTip_uUGVmArumlF4B6UbwghE-gPvy8rfUO8P0vSYYc6mPQrQcfQ20-QRxxhnkpuM5MJSb46E8XBVv2e0k', 
      'redirect_uri':'http://localhost:8080/', 
      'client_id':'887597828597-kjg09tgnbhd6sc8pr8r32v71168v8dd7.apps.googleusercontent.com', 
      'client_secret':'-WwzKK48Y5Mq6wa5RhvUAV-1',
      'grant_type' : 'authorization_code',
      'scope' : 'https://www.googleapis.com/auth/contacts https://www.googleapis.com/auth/contacts.readonly https://www.googleapis.com/auth/userinfo.profile',
      'access_type' : 'offline'} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response text 
response = r.text 
print(response) 