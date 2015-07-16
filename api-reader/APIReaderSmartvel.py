#!/usr/bin/env python3

from AbstractAPIReader import AbstractAPIReader

from Smartvel import Smartvel

class APIReaderSmartvel(AbstractAPIReader):
    def __init__(self, token, endpoint):
        self._token = token
        self._endpoint = endpoint


    def get_iterable(self):
        return Smartvel(self._token, self._endpoint)
