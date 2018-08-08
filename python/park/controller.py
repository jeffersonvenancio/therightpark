import json, datetime

from flask import Blueprint, request, session
from google.appengine.api import search

from park.model import Park
from car.model import Car
from slot.model import Slot

parks = Blueprint('parks', __name__)

@parks.route('/', methods=['GET'])
def get_all():
    parks = [p.to_dict() for p in Park.query().fetch()]
    return json.dumps(parks)

@parks.route('/<int:park_id>', methods=['GET'])
def get_by_id(park_id):
    park = Park.get_by_id(park_id)
    return json.dumps(park)

@parks.route('/', methods=['POST'], strict_slashes=False)
def add():
    slot_id = request.form['slot_id']
    car_rfid = request.form['car_rfid']

    slot = Slot.get_by_id(int(slot_id))
    car = Car.query().filter(Car.rfid == car_rfid).get()

    park = Park(slot=slot.key, car=car.key, regular = car.pref == slot.pref)

    park.put()

    return json.dumps(park.to_dict)

@parks.route('/', methods=['PUT'], strict_slashes=False)
def update():
    park_id = request.form['park_id']

    park = Park.get_by_id(int(park_id))

    now = datetime.datetime.now()
    park.dateOut = now

    park.put()

    return json.dumps(park.to_dict())

