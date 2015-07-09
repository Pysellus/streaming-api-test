#!/usr/bin/env python3

'''
    Infinite loop _before_ or _after_ the subscribe operation is blocking
    and killing it kills the entire program.

    The main difference is the use of an iterable instead of
    an interval.
'''

import time
from rx import Observable
from rx.subjects import Subject

subject = Subject()
source = Observable.from_(range(100))

sub_subject1 = subject.subscribe(
    lambda v : print("Value published to observer 1: {0}".format(v)),
    lambda e : print("Error! {0}".format(e)),
    lambda : print("Completed!")
)

sub_subject2 = subject.subscribe(
    lambda v : print("Value published to observer 2: {0}".format(v)),
    lambda e : print("Error! {0}".format(e)),
    lambda : print("Completed!")
)

# This works as expected
# while True:
#     print("Foo")

# This is blocking
source.subscribe(subject)

# This works as expected
while True:
    print("Foo")
