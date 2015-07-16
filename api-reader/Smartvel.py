#!/usr/bin/env python3

from time import sleep

import requests

class Smartvel():
    def __init__(self, token, endpoint):
        self._request_more = True
        self._token = token
        self._buffer = []
        self._endpoint = endpoint
        self._update_url = 'http://vincent.smartvel.net/v1/' + self._endpoint + '/'


    def __iter__(self):
        return self


    def __next__(self):
        if self._request_more:
            self._fill_update_buffer()
            self._request_more = False

        if not self._buffer:
            raise StopIteration
        
        return self._buffer.pop(0)


    def _fill_update_buffer(self, backoff=0.1, limit=16):
        try:
            payload = {'key': self._token}
            response = requests.get(self._update_url, params=payload)
        except requests.exceptions.RequestException as e:
            if backoff >= limit:
                raise e
            else:
                self._wait_and_retry(backoff)

        updates = response.json()['results']

        # If no elements in the queue,
        # call again until an element is received
        if not updates:
            if backoff >= limit:
                backoff = 0.1

            self._wait_and_retry(backoff)

        self._buffer += updates


    def _wait_and_retry(self, seconds_to_wait):
        sleep(seconds_to_wait)
        self._fill_update_buffer(backoff=seconds_to_wait*2)
