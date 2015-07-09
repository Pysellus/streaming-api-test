#!/usr/bin/env python3

'''
    Process two different streams
    in parallel
'''

import rx
import asyncio
from concurrent.futures import ProcessPoolExecutor

import APIReaderTwitter as Twitter

try:
    import json
except ImportError:
    import simplejson as json

def is_not_delete(element):
    return not "delete" in element

def is_delete(element):
    return "delete" in element

def pretty_print(element):
    print(json.dumps(element, indent=4))

def process_deleted():
    twitter_stream = rx.Observable.from_(Twitter.get_iterable())
    deleted_stream = twitter_stream.filter(is_not_delete)
    deleted_stream.subscribe(pretty_print)

def process_tweets():
    twitter_stream = rx.Observable.from_(Twitter.get_iterable())
    tweet_stream = twitter_stream.filter(is_delete)
    tweet_stream.subscribe(pretty_print)

if __name__ == "__main__":
    executor = ProcessPoolExecutor(2)
    loop = asyncio.get_event_loop()
    
    deleted = asyncio.async(loop.run_in_executor(executor, process_deleted))
    tweets  = asyncio.async(loop.run_in_executor(executor, process_tweets))
    
    loop.run_forever()
