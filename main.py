import os
import jinja2
import webapp2
from models import User
from models import Visitor

jinja_current_directory = jinja2.Environment(loader=jinja2.FileSystemLoader(
os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_current_directory.get_template('welcomepage.html')
        self.response.write(template.render())

class GamePage(webapp2.RequestHandler):
    def get(self):
        if Visitor.query(Visitor.plays > 0).get():
            newVisitor = Visitor.query(Visitor.plays >= 0).get()
            newVisitor.plays += 1
            newVisitor.put()
        else:
            Visitor(plays = 1).put()
        self.response.headers['Content-Type'] = 'text/html'
        template_vars = {"username": self.request.get("username")}
        template = jinja_current_directory.get_template('flappypotato.html')
        self.response.write(template.render(template_vars))

    def post(self):
        if User.query(User.username == self.request.get('username')[10:]).get():
            returningUser = User.query(User.username == self.request.get('username')[10:]).get()
            if int(self.request.get("score")[7:]) > returningUser.score:
                returningUser.score = int(self.request.get("score")[7:])
                returningUser.put()
        else:
            User(username=self.request.get('username')[10:], score=int(self.request.get("score")[7:])).put()
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_current_directory.get_template('flappypotato.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([('/', WelcomePage), ('/game', GamePage)], debug=True)