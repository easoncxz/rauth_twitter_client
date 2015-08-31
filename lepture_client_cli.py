
import os
import json
import code

from lepture_rauth import make_lepture

def main():
    print('Paste in Lepture consumer key & secret.')
    lines = []
    while True:
        l = input().strip()
        if l:
            lines.append(l)
        else:
            break
    j_str = '\n'.join(lines)
    j = json.loads(j_str)
    ck, cs = j['consumer_key'], j['consumer_secret']
    lepture = make_lepture(ck, cs)
    # Now has Lepture app
    #rt, rts = lepture.get_request_token(
    #        data=dict(
    #            oauth_callback='http://localhost:5000/callback'))
    t = lepture.get_raw_request_token()
    code.interact(local=vars())

    print("Using request token and secret:")
    print(rt)
    print(rts)
    print()
    print("Visit this URL:")
    auth_url = lepture.get_authorize_url(rt)
    print(auth_url)
    print("OAuth verifier?")
    veri = input()
    at, ats = lepture.get_access_token(
            rt, rts, data=dict(oauth_verifier=veri))
    print("Your access tokens:")
    print(at)
    print(ats)
    print()
    sess = lepture.get_session((at, ats))
    return sess

if __name__ == '__main__':
    main()
