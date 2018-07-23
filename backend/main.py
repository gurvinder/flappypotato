import os
import jinja2
import webapp2

jinja_current_directory = jinja2.Environment(loader=jinja2.FileSystemLoader(
os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_current_directory.get_template(os.chdir('..'))
        self.response.write(template.render())

app = webapp2.WSGIApplication([('/', WelcomePage)], debug=True)