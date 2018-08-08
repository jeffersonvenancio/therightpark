from google.appengine.ext import ndb

from slot.model import Slot
from car.model import Car

class Park(ndb.Model):
    slot = ndb.KeyProperty(kind=Slot)
    car = ndb.KeyProperty(kind=Car)
    dateIn = ndb.DateTimeProperty(auto_now_add=True)
    dateOut = ndb.DateTimeProperty(auto_now_add=False)
    regular = ndb.BooleanProperty()


    def to_dict(self):
        result = {}
        result['id'] = self.key.id()

        car = {}
        car_ent = Car.get_by_id(self.car.id())
        car['plate'] = car_ent.plate
        car['pref'] = car_ent.pref
        result['car'] = car

        slot = {}
        slot_ent = Slot.get_by_id(self.slot.id())
        slot['label'] = slot_ent.label
        slot['pref'] = slot_ent.pref
        result['slot'] = slot

        result['regular'] = self.regular

        return result