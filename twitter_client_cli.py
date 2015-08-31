
from twitter_rauth import twitter

def main():
    print("Using Twitter consumer key & secret:")
    print(twitter.consumer_key)
    print(twitter.consumer_secret)
    print()
    rt, rts = twitter.get_request_token(
            data=dict(
                oauth_callback='http://localhost:5000/callback'))
    print("Using request token and secret:")
    print(rt)
    print(rts)
    print()
    print("Visit this URL:")
    auth_url = twitter.get_authorize_url(rt)
    print(auth_url)
    print("OAuth verifier?")
    veri = input()
    at, ats = twitter.get_access_token(
            rt, rts, data=dict(oauth_verifier=veri))
    print("Your access tokens:")
    print(at)
    print(ats)
    print()
    sess = twitter.get_session((at, ats))
    resp = sess.get('account/verify_credentials.json')
    j = resp.json()
    screen_name = j['screen_name']
    print("Hello, {}!".format(screen_name))
    return sess

if __name__ == '__main__':
    sess = main()
