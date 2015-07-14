"""
    Telegram API - Provides an iterable

    Keeps an internal buffer of updates.
    On next, get the next element from the buffer

    When the buffer is empty, request more updates to the server.

    Also keep track of the offset so we don't get duplicates from the API
"""

import requests
from time import sleep

class Telegram():
    def __init__(self, token):
        self.token = token
        self.buffer = []
        self.offset = 0
        self.update_url = 'https://api.telegram.org/' + self.token + '/getUpdates'

    def __iter__(self):
        return self

    def __next__(self):
        """
        Yield the next element from the buffer.

        If no element is found, fill the buffer,
        and then return the first from it
        """
        if not self.buffer:
            self._fill_update_buffer()

        return self.buffer.pop(0)

    def _fill_update_buffer(self, backoff=0.1, limit=16):
        """
        Fill the buffer with the next N elements.

        If no connection can be made, keep trying until
        limit is reached.
        If the buffer is still empty, keep trying indefinitely
        """
        try:
            payload = {'offset': self.offset}
            response = requests.get(self.update_url, params=payload)
        except requests.exceptions.RequestException as e:
            if backoff >= limit:
                raise e
            else:
                self._wait_and_retry(backoff)

        updates = response.json()['result']

        # If no elements in the queue,
        # call again until an element is received
        if not updates:
            if backoff >= limit:
                backoff = 0.1

            self._wait_and_retry(backoff)
        else:
            self.offset = updates[-1]['update_id'] + 1

        for update in updates:
            self.buffer.append(update)

    def _wait_and_retry(self, seconds_to_wait):
        sleep(seconds_to_wait)
        self._fill_update_buffer(backoff=seconds_to_wait*2)
