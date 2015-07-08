#!/usr/bin/env python3

'''
    Infinite loop _before_ the subscribe operation is blocking
    and killing it kills the entire program.

    Infinite loop _after_ the subscribe operation is blocking too,
    but killing doesn't kill the entire program, because the subscribe
    loop still runs.
'''

import time
from rx import Observable
from rx.subjects import Subject

subject = Subject()
source = Observable.interval(1000)

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

source.subscribe(subject)

# This does not
while True:
    print("Foo")
