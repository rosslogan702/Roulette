"""
Description: Non-random class that is used as a util for generating non-random numbers for testability
Author: Ross Logan 2017
"""
import random

class NonRandom(random.Random):

    def __init__(self):
        self.value = 0

    def setSeed(self, value):
        self.value = value

    def choice(self, seq):
        return seq[self.value]