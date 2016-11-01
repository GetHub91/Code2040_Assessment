# Code2040 Technical Assessment
# Step 5 - The dating game

import requests
import json
import datetime

API_TOKEN = '3ed48f8b95093ceeb29e331c21cc35a7'
ENDPOINT1 = 'http://challenge.code2040.org/api/dating'
ENDPOINT2 = 'http://challenge.code2040.org/api/dating/validate'

response = requests.post(ENDPOINT1, data = {'token':API_TOKEN})
dictionary = response.json()
datestamp = dictionary['datestamp']
interval = dictionary['interval']
new_datestamp = datetime.datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')# parse string
new_datestamp = new_datestamp + datetime.timedelta(seconds=interval)       # add interval
datestamp = new_datestamp.isoformat() + 'Z'                                # convert to string
response = requests.post(ENDPOINT2, data = {'token':API_TOKEN, 'datestamp':datestamp})
print(response.text)
