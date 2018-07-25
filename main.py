import os
import jinja2
import webapp2
from google.appengine.ext import ndb

jinja_current_directory = jinja2.Environment(loader=jinja2.FileSystemLoader(
os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_current_directory.get_template('welcomepage.html')
        self.response.write(template.render())

class GamePage(webapp2.RequestHandler):
    def post(self):
        if self.request.get('username'):
            User(username=self.request.get('username')).put()
        template = jinja_current_directory.get_template('flappypotato.html')
        self.response.write(template.render())

class User(ndb.Model):
    username = ndb.StringProperty()
    score = ndb.IntegerProperty()

app = webapp2.WSGIApplication([('/', WelcomePage), ('/game', GamePage)], debug=True)