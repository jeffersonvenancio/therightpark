import json

from flask import Blueprint, request, session
from google.appengine.api import search

from slot.model import Slot

slots = Blueprint('slots', __name__)

@slots.route('/', methods=['GET'])
def get_all():
    slots = [u.to_dict() for u in Slot.query().fetch()]
    return json.dumps(slots)

@slots.route('/<int:slot_id>', methods=['GET'])
def get_by_id(slot_id):
    slot = Car.get_by_id(slot_id).to_dict()
    return json.dumps(slot)


@slots.route('/', methods=['POST'], strict_slashes=False)
def add():
    label = request.form['label']
    pref = request.form['pref']

    slot = Slot(label=label, pref=False)
    slot.put()

    return '', 204