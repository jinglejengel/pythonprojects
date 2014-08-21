from requests_oauthlib import OAuth2Session
import json

from uber_conf import *

client_id = CLIENT_ID
client_secret = CLIENT_SECRET
redirect_uri = REDIRECT_URI

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
authorization_url, state = oauth.authorization_url(
        'https://login.uber.com/oauth/authorize')

print 'Please go to %s and authorize access.' % authorization_url
authorization_response = raw_input('Enter the full callback URL: ')


token = oauth.fetch_token(
        'https://login.uber.com/oauth/token',
        authorization_response=authorization_response,
        client_secret=client_secret)

prof = oauth.get('https://api.uber.com/v1/me')
hist = oauth.get('https://api.uber.com/v1/history')

print "Your profile is: "
print json.dumps(prof.json(), indent=4)

print

print "Your history is: "
print json.dumps(hist.json(), indent=4)

print
