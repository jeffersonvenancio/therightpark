import csv, json
import requests

headers = {'content-type' : 'application/x-www-form-urlencoded'}
# url = "http://barzinganow.appspot.com/api/user/"
url = "http://localhost:8080/api/parks/"
data = {'slot_id': 5629499534213120, 'car_rfid':'ASD12345678'}
print requests.post(url, data=data, headers=headers)