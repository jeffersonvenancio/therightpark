from google.appengine.ext import ndb

class Slot(ndb.Model):
    label = ndb.StringProperty()
    pref = ndb.BooleanProperty()

    def to_dict(self):
        result = super(Slot, self).to_dict()
        result['id'] = self.key.id()

        return result

    def isPref(self, value):
        return self.pref
