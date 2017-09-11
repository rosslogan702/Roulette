"""
Description: Non-random class that is used as a util for generating non-random numbers for testability
Author: Ross Logan 2017
"""
import random

class NonRandom(random.Random):

    def __init__(self, values):
        self.values = values
        self._index = 0

    def choice(self, seq):
        randIndex = self.values[self._index]
        self._index += 1
        return seq[randIndex]


