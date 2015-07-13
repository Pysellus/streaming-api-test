import json
from rx import Observable

import APIReaderTwitter as Twitter


def is_tweet(element):
    return set(('favorited', 'favorite_count', 'retweeted', 'retweet_count')) <= element.keys()

def is_retweet(element):
    return 'retweeted_status' in element


# https://dev.twitter.com/overview/api/tweets
def original_tweet_has_less_than_50_retweets(element):
    return element['retweeted_status']['retweet_count'] <= 50

# All retweeted tweets should have less than 50 retweets
def test(element):
    if not original_tweet_has_less_than_50_retweets(element):
        print('original tweet has', json.dumps(element['retweeted_status']['retweet_count'], indent=4), "retweets")



stream = Observable.from_(Twitter.get_iterable())

retweeted_tweets = stream \
    # Filter out all non-tweets
    .filter(is_tweet) \
    # Keep only retweets
    .filter(is_retweet)

# In our DSL, this would be:
# `expect(retweeted_tweets)(original_tweet_has_less_than_50_retweets)`
retweeted_tweets.subscribe(test)
