#!/usr/bin/env python3

'''
    Filter all "delete" events from the Twitter API
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
def is_not_delete(element):
    return not "delete" in element

# Any -> IO
def pretty_print(element):
    print(json.dumps(element, indent=4))

stream = Stream(Twitter.get_iterable())
stream.filter(is_not_delete).subscribe(pretty_print)
