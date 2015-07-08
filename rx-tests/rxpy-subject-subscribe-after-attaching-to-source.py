#!/usr/bin/env python3

'''
    Attaching a Subject to an active stream is blocking
'''

from rx import Observable
from rx.subjects import Subject

subject = Subject()
source = Observable.from_(range(10000))

# Attaching Subject to the Original Oberservable
# Blocking
source.subscribe(subject)


# Subscribing to an attached subject doesn't work until
# the stream to which the subject is attached finishes,
# if ever
sub_subject1 = subject.subscribe(
    lambda v : print("Value published to observer 1: {0}".format(v)),
    lambda e : print("Error! {0}".format(e)),
    lambda : print("Completed!")
)

# => Completed!

sub_subject2 = subject.subscribe(
    lambda v : print("Value published to observer 2: {0}".format(v)),
    lambda e : print("Error! {0}".format(e)),
    lambda : print("Completed!")
)

# => Completed!
