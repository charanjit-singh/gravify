import urllib.parse
import hashlib
from validate_email import validate_email
import sentry_sdk

sentry_sdk.init("https://d1a3441649e64a96b52c441233c47f26@sentry.io/1763873") # Automatic bug reporting

class Gravatar():
    
    def __init__(self, email, verify_email=True, default_image=None):
        if verify_email:
            if not validate_email(email):
                raise Exception("Invalid email address")
        
        self.email = email
        self.default_image = default_image

    @property
    def url(self):
        params = {}
        
        if self.default_image != None:
            params["d"] = self.default_image
        
        return "https://www.gravatar.com/avatar/" + self.hash + "?" + urllib.parse.urlencode(params)
    
    @property
    def unsecure_url(self):
        return self.url.replace("https://", "http://")

    @property
    def hash(self):
        return hashlib.md5(self.email.encode("utf-8").lower()).hexdigest()    
