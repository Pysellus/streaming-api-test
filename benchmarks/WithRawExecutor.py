#!/usr/bin/env python3

import rx
import Streams

import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':
    executor = ThreadPoolExecutor(2)
    loop = asyncio.get_event_loop()

    loop.run_in_executor(executor, partial(Streams.process_stream, Streams.deleted, Streams.pretty_print))
    loop.run_in_executor(executor, partial(Streams.process_stream, Streams.tweets, Streams.pretty_print))
