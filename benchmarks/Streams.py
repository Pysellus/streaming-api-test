#!/usr/bin/env python3

import rx
import json
import DatasetParser  

def is_tweet(element):
    return set(('favorited', 'favorite_count', 'retweeted', 'retweet_count')) <= element.keys()

def is_delete(element):
    return "delete" in element

def pretty_print(element):
    print(json.dumps(element, indent=4))

def process_stream(s, f):
    s.subscribe(f)

source = rx.Observable.from_(DatasetParser.get_iterable())
deleted = source.filter(is_delete)
tweets = source.filter(is_tweet)
