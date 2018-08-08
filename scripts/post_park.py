import csv, json
import requests

headers = {'content-type' : 'application/x-www-form-urlencoded'}
# url = "http://therightparking.appspot.com/api/parks/"
url = "http://localhost:8080/api/parks/"

# Atualizar park com uma saida
data = {'park_id' : 5328783104016384}
resp = requests.put(url, data=data, headers=headers)

# Criar um park
# data = {'slot_id': 5629499534213120, 'car_rfid':'ASD12345678'}
# resp = requests.post(url, data=data, headers=headers)

print resp.json()