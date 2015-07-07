#!/usr/bin/env python3

from auth_tokens import *
try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.sample()

tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    print(json.dumps(tweet, indent=4))
    if tweet_count <= 0:
        break
