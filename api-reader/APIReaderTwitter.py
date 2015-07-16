#!/usr/bin/env python3

from AbstractAPIReader import AbstractAPIReader

from twitter import OAuth, TwitterStream

class APIReaderTwitter(AbstractAPIReader):
    def __init__(self, access_token, access_secret, consumer_key, consumer_secret):
        self._access_token = access_token
        self._access_secret = access_secret
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret


    def get_iterable(self):
        oauth = OAuth(self._access_token, self._access_secret, self._consumer_key, self._consumer_secret)
        return TwitterStream(auth=oauth).statuses.sample()
