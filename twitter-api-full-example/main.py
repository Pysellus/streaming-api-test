import re
import json
import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor

from rx import Observable

import APIReaderTwitter as Twitter

emoji_re = re.compile(u'['
        u'\U0001F300-\U0001F64F'
        u'\U0001F680-\U0001F6FF'
        u'\u2600-\u26FF\u2700-\u27BF]+',
        re.UNICODE)

# Util
def process_stream(s, f):
    s.subscribe(f)

def count_emoji(text):
    return len(re.findall(emoji_re, text))


# Filters
def is_tweet(element):
    return set(('favorited', 'favorite_count', 'retweeted', 'retweet_count')) <= element.keys()

def is_retweet(element):
    return 'retweeted_status' in element

def is_spanish_tweet(element):
    return element['lang'] == 'es'

def is_japanese_tweet(element):
    return element['lang'] == 'ja'

def has_hashtags(element):
    return len(element['entities']['hashtags']) > 0


# Tests
def tweet_has_more_than_two_emojis(element):
    return count_emoji(element['text']) > 2

# https://dev.twitter.com/overview/api/tweets
def original_tweet_has_less_than_50_retweets(element):
    return element['retweeted_status']['retweet_count'] <= 50

def hashtag_longer_than_twelve_letters(element):
    return all(len(h['text']) > 12 for h in element['entities']['hashtags'])

# Expects
# All retweeted tweets should have less than 50 retweets
def retweet_test(element):
    if not original_tweet_has_less_than_50_retweets(element):
        print('=> Retweet:', json.dumps(element['retweeted_status']['retweet_count'], indent=4), "retweets")

# All elements should have less than 2 emojis
def emoji_test(element):
    if tweet_has_more_than_two_emojis(element):
        print("=> Emoji:", count_emoji(element['text']))

# All elements should have hashtags shorter that 12 characters
def hashtag_test(element):
    if hashtag_longer_than_twelve_letters(element):
        print('=> Hashtag:', json.dumps(element['entities']['hashtags'], indent=4))

if __name__ == "__main__":
    stream = Observable.from_(Twitter.get_iterable())
    tweets = stream.filter(is_tweet)

    # Keep only retweets
    retweeted_tweets = tweets.filter(is_retweet)

    # Keep only tweets in japanese
    in_japanese_tweets = tweets.filter(is_japanese_tweet)

    # Keep all tweets in spanish that contain a hashtag
    spanish_hashtags = tweets.filter(is_spanish_tweet).filter(has_hashtags)

    executor = ThreadPoolExecutor(max_workers = 10)
    loop = asyncio.get_event_loop()

    # In our DSL, this would be `expect(stream)(test)`
    asyncio.async(loop.run_in_executor(executor, partial(process_stream, retweeted_tweets, retweet_test)))
    asyncio.async(loop.run_in_executor(executor, partial(process_stream, in_japanese_tweets, emoji_test)))
    asyncio.async(loop.run_in_executor(executor, partial(process_stream, spanish_hashtags, hashtag_test)))

    loop.run_forever()
