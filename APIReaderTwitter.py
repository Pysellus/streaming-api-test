#!/usr/bin/env python3

from auth_tokens import *
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

try:
    import json
except ImportError:
    import simplejson as json

def get_iterable():
	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_stream = TwitterStream(auth=oauth)
	return twitter_stream.statuses.sample()
