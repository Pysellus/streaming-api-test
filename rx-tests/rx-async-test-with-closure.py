#!/usr/bin/env python3

'''
    Process two different streams in parallel,
    retrieving them from the module's scope
'''

import rx
import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import partial

import APIReaderTwitter as Twitter

try:
    import json
except ImportError:
    import simplejson as json

def is_not_delete(element):
    return "delete" in element

def is_delete(element):
    return not "delete" in element

def pretty_print(element):
    print(json.dumps(element, indent=4))


twitter_stream = rx.Observable.from_(Twitter.get_iterable())

deleted_stream = twitter_stream.filter(is_not_delete)
tweet_stream = twitter_stream.filter(is_delete)


def process_deleted():
    deleted_stream.subscribe(pretty_print)

def process_tweets():
    tweet_stream.subscribe(pretty_print)

if __name__ == "__main__":
    executor = ThreadPoolExecutor(2)
    loop = asyncio.get_event_loop()

    deleted = asyncio.async(loop.run_in_executor(executor, process_deleted))
    tweets  = asyncio.async(loop.run_in_executor(executor, process_tweets))

    loop.run_forever()
