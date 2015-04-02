import webapp2
import models

class MainPage(webapp2.RequestHandler):
    def.get(self):
        self.response.headers["Content-Type"] = "text/plain"
        self.response.write("Hello, World!")

applicaton = webapp2.WSGIApplication([
    ("/", MainPage),
    ], debug=True)
