import webapp2
from models import store_key, Product

class MainPage(webapp2.RequestHandler):
    def get(self):
    	product = Product(parent=store_key(), name="Test Product", description="Whatever", price=0.99)
    	product_key = product.put()
    	self.response.write(str(product_key))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
