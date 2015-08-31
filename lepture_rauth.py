
from rauth import OAuth1Service

CLIENT_KEY = 'cahC56M6XIYmg8sndhfOCtKqzK57HF'
CLIENT_SECRET = 'vJM3oOXoeiw4Ab33G20xds2CoLJ9Un9Fr4DaXbWK'

def make_lepture(ck, cs):
    return OAuth1Service(
            name='lepture',
            consumer_key=ck,
            consumer_secret=cs,
            base_url='http://127.0.0.1:5000/api/',
            request_token_url='http://127.0.0.1:5000/oauth/request_token',
            access_token_url='http://127.0.0.1:5000/oauth/access_token',
            authorize_url='http://127.0.0.1:5000/oauth/authorize')


