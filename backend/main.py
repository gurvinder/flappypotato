import os
import jinja2
import webapp2
from models import *
import datetime
from google.appengine.ext import ndb

jinja_current_directory = jinja2.Environment(loader=jinja2.FileSystemLoader(
os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'], autoescape=True)

def commitPostToDatabase(username, title, content):
    postKey = Post(title=title, content=content).put()
    if Author.query().filter(Author.name == username).fetch():
        author = Author.query().filter(Author.name == username).get()
        author.posts.append(postKey)
        authorKey = author.put()
        currentpost = postKey.get()
        currentpost.author = authorKey
        currentpost.put()
    else:
        authorKey = Author(name=username, posts = [postKey]).put()
        currentPost = postKey.get()
        currentpost.author = authorKey
        currentPost.put()

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write("Welcome to the server!")

app = webapp2.WSGIApplication([('/', WelcomePage)], debug=True)