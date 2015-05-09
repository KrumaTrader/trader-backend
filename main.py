import webapp2
from models import Product
from google.appengine.ext import ndb


class MainPage(webapp2.RequestHandler):
    def get(self):
    	self.response.write('Hello, World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
