# This code will refresh a token which has expired.
# requirement: refresh token
# note: refresh token is only acquired for the first every authorization by google server
# keep this token safe
import requests 

API_ENDPOINT = "https://oauth2.googleapis.com/token"

# data to be sent to api 
data = {'refresh_token':'1/K2TeDrE0hm-z3zkUF5ZW2RbtkT1yfl_z_Rbt6oQsER4', 
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