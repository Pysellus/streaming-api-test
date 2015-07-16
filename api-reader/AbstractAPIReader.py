#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class AbstractAPIReader(metaclass=ABCMeta):

    @abstractmethod
    def get_iterable(self): pass
