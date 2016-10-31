# Code2040 Technical Assessment
# Step 2 - Reverse a string

import requests

API_TOKEN = '3ed48f8b95093ceeb29e331c21cc35a7'
ENDPOINT1 = 'http://challenge.code2040.org/api/reverse'
ENDPOINT2 = 'http://challenge.code2040.org/api/reverse/validate'

word = requests.post(ENDPOINT1, data = {'token':API_TOKEN})
reversedWord = word.text[::-1]
response = requests.post(ENDPOINT2, data = {'token':API_TOKEN, 'string':reversedWord})
print(response.text)