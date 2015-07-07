#!/usr/bin/env python3

from auth_tokens import *
from rx import Observable


try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.sample()

observable = Observable.from_iterable(iterator)

observable.subscribe(print)


tweet_count = 1
