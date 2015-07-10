#!/usr/bin/env python3

'''
	Difference between hot and cold observables
'''

# See:
# https://github.com/Reactive-Extensions/RxJS/blob/master/doc/gettingstarted/creating.md#cold-vs-hot-observables

import rx
import datetime
from time import sleep

# Cold Observables only publish events when a subscriptor exists

print("=================================\nCold Observable:")

source = rx.Observable.interval(1000)

sub1 = source.subscribe(
		lambda v : print("Obs 1 got {0}".format(v)),
		lambda e : print("Obs 1 error: {0}".format(e)),
		lambda   : print("Obs1 completed")
)

sub2 = source.subscribe(
		lambda v : print("Obs 2 got {0}".format(v)),
		lambda e : print("Obs2 error: {0}".format(e)),
		lambda   : print("Obs2 completed")
)

sleep(5)

sub1.dispose()
sub2.dispose()

# => Obs 1 got 0
# => Obs 2 got 0
# => Obs 1 got 1
# => Obs 2 got 1
# => Obs 1 got 2
# => Obs 2 got 2
# => Obs 1 got 3
# => Obs 2 got 3


# Hot Observables, on the other hand, continue to publish
# events even when no one is listening

print("=================================\nHot Observable:")

date = datetime.datetime
print("Current time (s): {0}".format(date.now().second))

# Creates the seq
source = rx.Observable.interval(1000)

# Converts `hot` into a hot sequence
hot = source.publish()

# No value is pushed to 1st sub at this point
sub1 = hot.subscribe(
		lambda v : print("Obs1 got: {0}".format(v)),
		lambda e : print("Obs1 error: {0}".format(e)),
		lambda : print("Obs1 completed!")
)

print("Current time after 1st sub (s): {0}".format(date.now().second))

# Idle for 3s
sleep(3)

# `hot` is connected to source and starts publishing values
hot.connect()

print("Current time after connect (s): {0}".format(date.now().second))

sleep(3)

sub2 = hot.subscribe(
		lambda v : print("Obs2 got: {0}".format(v)),
		lambda e : print("Obs2 error: {0}".format(e)),
		lambda : print("Obs2 completed")
)

print("Current time after 2nd sub (s): {0}".format(date.now().second))

# => Current time (s): x
# => Current time after 1st sub (s): x
# => Current time after connect (s): x + n
# => Obs1 got: 0
# => Obs1 got: 1
# => Current time after 2nd sub (s): x + m (m > n)
# => Obs1 got: 2
# => Obs2 got: 2
# => Obs1 got: 3
# => Obs2 got: 3
# => Obs1 got: 4
# => Obs2 got: 4
# => Obs1 got: 5
# => Obs2 got: 5
# => Obs1 got: 6
# => Obs2 got: 6
# => ...
