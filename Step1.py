# Code2040 Technical Assessment
# Step 1 - Registration

import requests

API_TOKEN = '3ed48f8b95093ceeb29e331c21cc35a7'
REGISTRATION_URL = 'http://challenge.code2040.org/api/register'
GITHUB_URL = 'https://github.com/GetHub91/Code2040_Assessment'

response = requests.post(REGISTRATION_URL, data = {'token':API_TOKEN, 'github':GITHUB_URL} )
print(response.text)