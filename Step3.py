# Code2040 Technical Assessment
# Step 3 - Needle in a haystack

import requests
import json

API_TOKEN = '3ed48f8b95093ceeb29e331c21cc35a7'
ENDPOINT1 = 'http://challenge.code2040.org/api/haystack'
ENDPOINT2 = 'http://challenge.code2040.org/api/haystack/validate'

r = requests.post(ENDPOINT1, data = {'token':API_TOKEN})
dictionary = r.json()
needle = dictionary['needle']
haystack = dictionary['haystack']
for i in range(len(haystack)):
    if haystack[i] == needle:
        index = i;
response = requests.post(ENDPOINT2, data = {'token':API_TOKEN, 'needle':index})
print(response.text)
