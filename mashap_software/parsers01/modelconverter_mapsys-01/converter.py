import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import modelparser

class Home(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class Converter(webapp.RequestHandler):
    def post(self):
        print 'Content-Type: text/plain'
        print ''
        print modelparser.process_xml_string(self.request.get('content'))

application = webapp.WSGIApplication(
                 [('/', Home),
                 ('/convert', Converter)],
                 debug=True)
