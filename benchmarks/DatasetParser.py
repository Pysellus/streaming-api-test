#!/usr/bin/env python3

import json

def get_iterable():
    with open('twitter_data_medium.json') as f:
        result = json.load(f)
    return result
