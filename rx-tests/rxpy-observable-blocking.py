#!/usr/bin/env python3

'''
    Subscribing to an Observable is a blocking operation
'''

from rx import Observable
import APIReaderTwitter as Twitter

try:
    import json
except ImportError:
    import simplejson as json

# Iterable -> Observable
def Stream(iterable):
    return Observable.from_(iterable)

# Any -> Boolean
def is_delete(element):
    return not "delete" in element

def pretty_print(element):
    print(json.dumps(element, indent=4))

stream = Stream(Twitter.get_iterable())
stream.filter(is_delete).subscribe(pretty_print)

# This line never gets executed
while True:
    print("Foo")
