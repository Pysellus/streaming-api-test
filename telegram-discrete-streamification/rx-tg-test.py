#!/usr/bin/env python3

import json

from rx import Observable
import APIReaderTelegram as Telegram

def is_message_f(element):
    return element['message']['text'] == "f"

def pretty_print(element):
    print(json.dumps(element, indent=4))

messages = Observable.from_(Telegram.get_iterable())
messages.filter(is_message_f).subscribe(pretty_print)
