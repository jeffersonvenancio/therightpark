import json

from flask import Blueprint, request, session
from google.appengine.api import search
from car.model import Car

cars = Blueprint('cars', __name__)

@cars.route('/', methods=['GET'])
def get_all():
    cars = [u.to_dict() for u in Car.query().fetch()]
    return json.dumps(cars)

@cars.route('/<int:car_id>', methods=['GET'])
def get_by_id(car_id):
    car = Car.get_by_id(car_id).to_dict()
    return json.dumps(car)


@cars.route('/', methods=['POST'], strict_slashes=False)
def add():
    plate = request.form['plate']
    rfid = request.form['rfid']
    pref = request.form['pref']

    car = Car(plate=plate, rfid=rfid, pref=False)
    car.put()

    return '', 204