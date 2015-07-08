#!/usr/bin/env python3

'''
    Subscribing to a non-attached subject is not blocking
'''

from rx import Observable
from rx.subjects import Subject

subject = Subject()
source = Observable.from_(range(50))

# Non-Blocking
sub_subject1 = subject.subscribe(
    lambda v : print("Value published to observer 1: {0}".format(v)),
    lambda e : print("Error! {0}".format(e)),
    lambda : print("Completed!")
)

# Non-Blocking
sub_subject2 = subject.subscribe(
    lambda v : print("Value published to observer 2: {0}".format(v)),
    lambda e : print("Error! {0}".format(e)),
    lambda : print("Completed!")
)

# Attach Subject to the Original Oberservable
# Blocking
source.subscribe(subject)
