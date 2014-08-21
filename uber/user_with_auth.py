#!/usr/bin/env python
import json

from requests_oauthlib import OAuth2Session

from uber_conf import *

client_id = CLIENT_ID
client_secret = CLIENT_SECRET
redirect_uri = REDIRECT_URI

AUTHORIZATION_BASE_URL = 'https://login.uber.com/oauth/authorize'

def main():
    callback_url = make_url()

    token_url = 'https://login.uber.com/oauth/token'
    token = oauth.fetch_token(token_url, authorization_response=callback_url, client_secret=CLIENT_SECRET)

    resources = ['me', 'history']

    for resource in resources:
      print fetch(resource)

def make_url():
    global oauth
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
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

main()
