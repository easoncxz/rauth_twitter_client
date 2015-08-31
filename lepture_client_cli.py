
import os
import json
import code

from lepture_rauth import make_lepture

def main():
    ck = '38zgEsThKKD26hRcpJr3353Fd3rEQW'
    cs = '87b6cbQrT2PPTiwI4M72NDQDVV0s6vJzFeXHNz7c'
    lepture = make_lepture(ck, cs)
    rt, rts = lepture.get_request_token(
            data=dict(
                oauth_callback='http://localhost:8000/callback'))
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
    sess = main()
