from google.appengine.api import urlfetch
from google.appengine.api import images

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        imageUrl = self.request.get('url1')
        imageUrl2 = self.request.get('url2')
        img = images.Image(urlfetch.Fetch(imageUrl).content)
        img.horizontal_flip()
        img.resize(120, 120)
        result = img.execute_transforms(output_encoding=images.PNG)
        t1 = (result, 0, 0, 1.0, images.TOP_LEFT)

        img2 = images.Image(urlfetch.Fetch(imageUrl2).content)
        img2.resize(20, 20)
        result2 = img2.execute_transforms(output_encoding=images.PNG)
        t2 = (result2, 0, 0, 1.0, images.TOP_LEFT)

        result = images.composite([t1, t2], 120, 120, color=0,output_encoding=images.PNG, quality=None)
        self.response.headers['content-type'] = 'image/png'
        self.response.write(result)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
