"""
Description: Bin class that holds the winning outcomes for a particular bin on the roulette wheel
Author: Ross Logan 2017
"""

class Bin(object):

    def __init__(self, *outcomes):
        self.outcomes = frozenset(outcomes)

    def add(self, outcome):
        self.outcomes |= frozenset([outcome])

    def __str__(self):
        return ', '.join(map(str, self.outcomes))

