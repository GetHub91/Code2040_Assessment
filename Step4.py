# Code2040 Technical Assessment
# Step 4 - Prefix

import requests
import json

API_TOKEN = '3ed48f8b95093ceeb29e331c21cc35a7'
ENDPOINT1 = 'http://challenge.code2040.org/api/prefix'
ENDPOINT2 = 'http://challenge.code2040.org/api/prefix/validate'

response = requests.post(ENDPOINT1, data = {'token':API_TOKEN})
dictionary = response.json()
prefix = dictionary['prefix']
wordArray = dictionary['array']
noPrefix = []
for i in range(len(wordArray)):
    if wordArray[i].startswith(prefix) == False:
        noPrefix.append(wordArray[i])
dictionary = {'token':API_TOKEN, 'array':noPrefix}
response = requests.post(ENDPOINT2, json = dictionary)
print(response.text)
