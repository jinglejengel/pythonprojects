#!/usr/bin/env python
import argh
import json
import redis

from requests_oauthlib import OAuth2Session

from uber_conf import *


r = redis.StrictRedis()

client_id = CLIENT_ID
client_secret = CLIENT_SECRET
redirect_uri = REDIRECT_URI

AUTHORIZATION_BASE_URL = 'https://login.uber.com/oauth/authorize'

def main(user_email):
    global oauth
    try:
      token = eval(r.get(user_email))
      oauth = OAuth2Session(client_id, token=token)
    except:
      oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
      callback_url = make_url()
      token_url = 'https://login.uber.com/oauth/token'
      token = oauth.fetch_token(token_url, authorization_response=callback_url, client_secret=CLIENT_SECRET)

    resources = ['me', 'history']

    for resource in resources:
      res = fetch(resource)
      find_email = json.loads(res)
      if 'email' in find_email:
        r.setex(find_email['email'], token['expires_in'], token)
      print res

def make_url():
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)

    print "Please visit %s and enter in the full callback URL" % authorization_url

    callback = raw_input("Callback URL: ")
    return callback

def fetch(resource):
    endpoint = 'https://api.uber.com/v1/%s' % resource
    resp = oauth.get(endpoint)
    return jsonify(resp.json())


def jsonify(payload):
    return json.dumps(payload, indent=2)

argh.dispatch_command(main)
