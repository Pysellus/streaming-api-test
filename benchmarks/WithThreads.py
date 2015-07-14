#!/usr/bin/env python3

import rx
import Streams

from threading import Thread

if __name__ == '__main__':
    threads = [
        Thread(target=Streams.process_stream, args=(Streams.deleted, Streams.pretty_print)),
        Thread(target=Streams.process_stream, args=(Streams.tweets, Streams.pretty_print))
    ]
    
    for t in threads:
    	t.start()
