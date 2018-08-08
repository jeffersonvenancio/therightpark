import json, datetime

from flask import Blueprint, request, session
from google.appengine.api import search

from park.model import Park
from car.model import Car
from slot.model import Slot

parks = Blueprint('parks', __name__)

@parks.route('/', methods=['GET'])
def get_all():
    parks = [u.to_dict() for u in Park.query().fetch()]
    return json.dumps("")

@parks.route('/<int:park_id>', methods=['GET'])
def get_by_id(park_id):
    park = Park.get_by_id(park_id)
    return json.dumps(park)

@parks.route('/', methods=['POST'], strict_slashes=False)
def add():
    slot_id = request.form['slot_id']
    car_rfid = request.form['car_rfid']
    park_id = request.form['park_id']

    slot = Slot.get_by_id(int(slot_id))
    car = Car.query().filter(Car.rfid == car_rfid).get()
    park = Park.get_by_id(int(park_id))

    if not park :
        park = Park(slot=slot.key, car=car.key, regular = car.pref == slot.pref)
    else:
        now = datetime.datetime.now()
        park.dateOut = now

    park.put()

    return '', 204