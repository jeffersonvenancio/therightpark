import csv, json
import requests

headers = {'content-type' : 'application/x-www-form-urlencoded'}
# url = "http://therightparking.appspot.com"
url = "http://localhost:8080"

# Atualizar park com uma saida
# url += "/api/parks/"
# data = {'park_id' : 5328783104016384}
# resp = requests.put(url, data=data, headers=headers)

# Criar um park
# url += "/api/parks/"
# data = {'slot_id': 5629499534213120, 'car_rfid':'ASD12345678'}
# resp = requests.post(url, data=data, headers=headers)

# Atualizar park com uma saida
url += "/api/slots/"
data = {'label' : 'Vaga 2', 'pref' : True}
resp = requests.post(url, data=data, headers=headers)

print resp.json()