#!/usr/bin/env python3

'''
    Process two different streams
    in parallel
'''

import rx
import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor

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

def process_stream(stream, fn):
    stream.subscribe(fn)

if __name__ == "__main__":

    executor        = ThreadPoolExecutor(2)

    twitter_stream  = rx.Observable.from_(Twitter.get_iterable())
    deleted_stream  = twitter_stream.filter(is_not_delete)
    tweet_stream    = twitter_stream.filter(is_delete)


    loop = asyncio.get_event_loop()
    
    asyncio.async(loop.run_in_executor(executor, partial(process_stream, deleted_stream, pretty_print)))
    asyncio.async(loop.run_in_executor(executor, partial(process_stream, tweet_stream, pretty_print)))
    
    loop.run_forever()
