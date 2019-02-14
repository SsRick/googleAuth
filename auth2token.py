import requests

url = "https://oauth2.googleapis.com/token"

payload = "code=4%2F8QC1hgVA6Bo7NvHjrjCLwx4pfjsBGMYr--cY3fQ9fUTd5iHYm0_zLYROHR-j66ZW_HHZcyxGkLmJzvOa8siCLPo&redirect_uri=http%3A%2F%2Flocalhost%3A8080%2F&client_id=887597828597-kjg09tgnbhd6sc8pr8r32v71168v8dd7.apps.googleusercontent.com&client_secret=-WwzKK48Y5Mq6wa5RhvUAV-1&grant_type=authorization_code&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar&access_type=offline&undefined="
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "daa12b11-efa7-4e9a-ba44-327050a18859"
    }

response = requests.request("POST", url, data=payload)

print(response.text)