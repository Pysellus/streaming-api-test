#!/usr/bin/env python3

'''
    Make a stream emit at the pace of a slower stream

    Pros:
    Introduce a delay between events in an otherwise rapid stream (like range)

    Cons:
    When the stream being delayed runs out of events to push, the zipped stream
    will keep pushing events, defined with the lambda fn passed to the zip operation.
'''

from time import sleep
from rx import Observable

# Generate an interval sequece, firing once each second
interval = Observable.interval(1000)

# 5..10
numbers = Observable.from_(range(5, 11))

# Zip two streams together so it emits at the pace of the slowest stream
source = Observable.zip(
    interval,
    numbers,
    # Because we only push the elements of the `numbers` stream,
    # As soon as it runs out of events, it will keep sending empty
    # events to the subscribers
    lambda _, n: n
)

sub1 = source.subscribe(
    lambda v : print("Value published to observer 1: {0}".format(v)),
    lambda e : print("Error! {0}".format(e)),
    lambda : print("Completed!")
)

sub2 = source.subscribe(
    lambda v : print("Value published to observer 2: {0}".format(v)),
    lambda e : print("Error! {0}".format(e)),
    lambda : print("Completed!")
)

# As noted above, we have to dispose the subscriptions before the `numbers`
# streams runs out, or the program will get stuck listening to empty events
sleep(5)
sub1.dispose()
sub2.dispose()

# => Value published to observer 1: 5
# => Value published to observer 2: 5
# => Value published to observer 1: 6
# => Value published to observer 2: 6
# => Value published to observer 2: 7
# => Value published to observer 1: 7
# => Value published to observer 2: 8
# => Value published to observer 1: 8
