from google.appengine.ext import ndb

class Slot(ndb.Model):
    label = ndb.StringProperty()
    pref = ndb.BooleanProperty()

    def to_dict(self):
        result = {}
        result['id'] = self.key.id()
        result['label'] = self.label
        result['pref'] = self.pref

        return result

    def isPref(self, value):
        return self.pref
