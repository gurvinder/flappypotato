import os
import jinja2
import webapp2
from models import User

jinja_current_directory = jinja2.Environment(loader=jinja2.FileSystemLoader(
os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_current_directory.get_template('welcomepage.html')
        self.response.write(template.render())

class GamePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_vars = {"username": self.request.get("username")}
        template = jinja_current_directory.get_template('flappypotato.html')
        self.response.write(template.render(template_vars))

    def post(self):
        User(username=self.request.get('username')[10:], score=int(self.request.get("score")[7:])).put()
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_current_directory.get_template('flappypotato.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([('/', WelcomePage), ('/game', GamePage)], debug=True)