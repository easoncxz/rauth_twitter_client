
from flask import Flask, url_for, request, session, redirect
from twitter_rauth import twitter

app = Flask(__name__)
app.debug = True
app.secret_key = 'lol'
app.trc = app.test_request_context

@app.route('/')
def index():
    if 'access' in session:
        at, ats = session['access']
        rauth_sess = twitter.get_session((at, ats))
        resp = rauth_sess.get('account/verify_credentials.json')
        assert resp.status_code == 200
        j = resp.json()
        screen_name = j['screen_name']
        return "Hello, {}!".format(screen_name)
    else:
        return '''<a href="{login_url}">Just login.</a>'''.format(
                login_url=url_for('login'))

@app.route('/login')
def login():
    rt, rts = twitter.get_request_token(
            data={
            'oauth_callback': url_for(
                    'callback', _external=True)})
    session['temp_cred'] = rt, rts
    auth_url = twitter.get_authorize_url(rt)
    return redirect(auth_url)

@app.route('/callback')
def callback():
    rt = request.args['oauth_token']
    rt_, rts = session['temp_cred']
    assert rt == rt_, (rt, rt_)
    veri = request.args['oauth_verifier']
    at, ats = twitter.get_access_token(
            rt, rts, data={'oauth_verifier': veri})
    session['access'] = at, ats
    return redirect(url_for('index'))

def test():
    with app.trc():
        print(url_for('callback'))

def main():
    app.run()

if __name__ == '__main__':
    main()
