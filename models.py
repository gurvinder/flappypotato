class User(ndb.Model):
    username = ndb.StringProperty()
    score = ndb.IntegerProperty()