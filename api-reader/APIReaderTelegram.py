#!/usr/bin/env python3

from AbstractAPIReader import AbstractAPIReader

from Telegram import Telegram

class APIReaderTelegram(AbstractAPIReader):
    def __init__(self, tg_token):
        self._token = tg_token


    def get_iterable(self):
        return Telegram(token=self._token)
