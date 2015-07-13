#!/usr/bin/env python3

from Telegram import *
from tg_auth import *

def get_iterable():
    return Telegram(token=API_KEY)
