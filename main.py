import webapp2
from models import Product
from google.appengine.ext import ndb


class MainPage(webapp2.RequestHandler):
    def get(self):
        product = Product(
            parent=ndb.Key("User", "arnoblalam"),
            name="Test Product",
            description="Whatever", price=0.99)
        product.put()

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
