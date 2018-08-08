from google.appengine.ext import ndb

from slot.model import Slot
from car.model import Car

class Park(ndb.Model):
    slot = ndb.KeyProperty(kind=Slot)
    car = ndb.KeyProperty(kind=Car)
    dateIn = ndb.DateTimeProperty(auto_now_add=True)
    dateOut = ndb.DateTimeProperty(auto_now_add=False)
    regular = ndb.BooleanProperty()
