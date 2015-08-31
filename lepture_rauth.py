
from rauth import OAuth1Service

def make_lepture(ck, cs):
    return OAuth1Service(
            name='lepture',
            consumer_key=ck,
            consumer_secret=cs,
            base_url='http://127.0.0.1:5000/api/',
            request_token_url='http://127.0.0.1:5000/oauth/request_token',
            access_token_url='http://127.0.0.1:5000/oauth/access_token',
            authorize_url='http://127.0.0.1:5000/oauth/authorize')


