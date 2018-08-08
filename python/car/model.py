from google.appengine.ext import ndb

class Car(ndb.Model):
    plate = ndb.StringProperty()
    rfid = ndb.StringProperty()
    pref = ndb.BooleanProperty()

    def to_dict(self):
        result = super(Car, self).to_dict()
        result['id'] = self.key.id()

        return result

    def isPref(self, value):
        return self.pref
