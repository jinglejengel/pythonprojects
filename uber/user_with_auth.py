#!/usr/bin/env python
import argh
import json

from requests_oauthlib import OAuth2Session

from uber_conf import *

client_id = CLIENT_ID
client_secret = CLIENT_SECRET
redirect_uri = REDIRECT_URI

AUTHORIZATION_BASE_URL = 'https://login.uber.com/oauth/authorize'


def main(callback_url):
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)

    token_url = 'https://login.uber.com/oauth/token'
    token = oauth.fetch_token(token_url, authorization_response=callback_url,
                              client_secret=CLIENT_SECRET)

    resources = ['me', 'history']
    print map(jsonify(fetch(resource)), resources)


def fetch(resource):
    endpoint = 'https://api.uber.com/v1/%s' % resource
    resp = oauth.get(endpoint)
    return resp.json()


def jsonify(payload):
    return json.dumps(payload, sort_keys=True, indent=2, separators=(',', ': '))

argh.dispatch_command(main)
