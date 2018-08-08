import csv, json
import requests

headers = {'content-type' : 'application/x-www-form-urlencoded'}
# url = "http://therightparking.appspot.com/api/parks/"
url = "http://localhost:8080/api/parks/"
data = {'park_id' : 5171003185430528, 'slot_id': 5629499534213120, 'car_rfid':'ASD12345678'}
print requests.post(url, data=data, headers=headers)