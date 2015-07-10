#!/usr/bin/env python3

'''
    Attaching a Subject to an active stream is non blocking
    if we publish on ticks

    Cons:
    As soon as `range` runs out, the program will get stuck
    See rx-stream-paced
'''

from rx import Observable
from rx.subjects import Subject

subject = Subject()
tick = Observable.interval(1000)

source = Observable.from_(range(10000)).zip(
    tick,
    lambda n, _: n
)

source.subscribe(subject)

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
