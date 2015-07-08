from time import sleep

class DelayedGenerator():
    def __init__(self, iterable):
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        sleep(1)
        return next(self.iterator)
