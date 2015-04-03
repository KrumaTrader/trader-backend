import webapp2
from models import Product
from google.appengine.ext import ndb


class MainPage(webapp2.RequestHandler):
    def get(self):
        query = Product.query()
        res = query.fetch()
        for r in res:
            self.response.write("<br>")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
