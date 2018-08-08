import json

from flask import Blueprint, request, session
from google.appengine.api import search

from park.model import Park
from car.model import Car
from slot.model import Slot

parks = Blueprint('parks', __name__)

@parks.route('/', methods=['GET'])
def get_all():
    users = [u.to_dict() for u in Park.query().fetch()]
    return json.dumps(users)

@parks.route('/<int:park_id>', methods=['GET'])
def get_by_id(park_id):
    park = Park.get_by_id(park_id).to_dict()
    return json.dumps(park)

@parks.route('/', methods=['POST'], strict_slashes=False)
def add():
    return '', 204