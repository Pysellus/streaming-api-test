#!/usr/bin/env python3

'''
    Emit elements from the twitter stream at a slower pace


    Pros:
    See rx-stream-pacing

    Cons:
    See rx-stream-pacing
    Two ^C become necessary to stop this script - why?
'''

from rx import Observable
import APIReaderTwitter as Twitter

try:
    import json
except ImportError:
    import simplejson as json

def pretty_print(element):
    print(json.dumps(element, indent=4))

def is_delete(element):
    return not "delete" in element

# Generate an interval sequece, firing once each second
tick = Observable.interval(1000)

# Publish an event from Twitter each tick as a minimum
# If the twitter stream is empty it will just wait for an event to come
source = Observable.from_(Twitter.get_iterable()).zip(
    tick,
    lambda t, _: t
)

# Print each element in intervals, waits a minimum of 1s between events
source.filter(is_delete).subscribe(pretty_print)
