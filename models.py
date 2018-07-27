from google.appengine.ext import ndb

class User(ndb.Model):
    username = ndb.StringProperty()
    score = ndb.IntegerProperty()

class Visitor(ndb.Model):
    plays = ndb.IntegerProperty()